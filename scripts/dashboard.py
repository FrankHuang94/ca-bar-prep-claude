#!/usr/bin/env python3
"""Regenerate 10-progress/readiness-dashboard.md and the README status block.

Inputs: 10-progress/attempts.csv, config/plan.yml (targets, benchmarks, exam date),
00-exam-intel/coverage-matrix.csv, the question bank and rule statements.

Usage
  python scripts/dashboard.py              # write both files
  python scripts/dashboard.py --stdout     # print the dashboard only

Readiness is a transparent heuristic, NOT a scaled-score prediction:
  * MBE   = accuracy over your most recent 200 MCQs (all sources) vs the plan's benchmark for today
  * Written = mean of your last 10 essay scores (PTs count twice) vs the plan's benchmark
  * Volume  = cumulative MCQ / essay / PT / simulation counts vs the plan's cumulative targets
NCBE does not publish a fixed raw-to-scaled conversion, so no scaled MBE score is estimated.
"""
from __future__ import annotations

import argparse
import datetime as dt
import sys
from collections import Counter, defaultdict

import common as C

STATUS_MARKER = "STATUS"


def parse_date(s) -> dt.date:
    return s if isinstance(s, dt.date) else dt.date.fromisoformat(str(s))


def interpolate(points: list[dict], key: str, day: dt.date) -> float:
    pts = sorted(((parse_date(p["date"]), float(p.get(key, 0))) for p in points), key=lambda x: x[0])
    if not pts:
        return 0.0
    if day <= pts[0][0]:
        return pts[0][1]
    for (d0, v0), (d1, v1) in zip(pts, pts[1:]):
        if d0 <= day <= d1:
            return v0 + (v1 - v0) * ((day - d0).days / max(1, (d1 - d0).days))
    return pts[-1][1]


def current_benchmark(plan: dict, day: dt.date) -> dict:
    bms = sorted(plan.get("benchmarks") or [], key=lambda b: parse_date(b["by"]))
    upcoming = [b for b in bms if parse_date(b["by"]) >= day]
    return upcoming[0] if upcoming else (bms[-1] if bms else {})


def topic_of(cid: str) -> str:
    """EVD-MBE-V.F.2 -> EVD-MBE-V.F (topic level)."""
    head, _, ref = cid.partition("-MBE-")
    if not ref:
        return cid
    return f"{head}-MBE-" + ".".join(ref.split(".")[:2])


def compute(day: dt.date) -> dict:
    plan = C.load_plan()
    att = C.load_attempts()
    mcq = [a for a in att if a["kind"] == "mcq"]
    essays = [a for a in att if a["kind"] == "essay"]
    pts = [a for a in att if a["kind"] == "pt"]
    sims = {a["item_id"] for a in att if a["kind"] == "simulation"}
    recent = mcq[-200:]
    acc = (sum(a["correct"] == "Y" for a in recent) / len(recent)) if recent else None
    by_subj: dict[str, list[int]] = defaultdict(list)
    by_topic: dict[str, list[int]] = defaultdict(list)
    for a in mcq:
        v = 1 if a["correct"] == "Y" else 0
        by_subj[a["subject"]].append(v)
        for cid in C.split_list(a["coverage_ids"])[:1]:
            by_topic[topic_of(cid)].append(v)
    scores = [float(a["score"]) for a in essays[-10:] if a["score"]]
    pt_scores = [float(a["score"]) for a in pts[-3:] if a["score"]]
    weighted = scores + pt_scores * 2
    written = (sum(weighted) / len(weighted)) if weighted else None
    essay_by_subj: dict[str, list[float]] = defaultdict(list)
    for a in essays:
        if a["score"]:
            for s in (a["subject"].split(";") if a["subject"] else ["?"]):
                essay_by_subj[s].append(float(a["score"]))
    secs = [float(a["time_seconds"]) for a in recent if a["time_seconds"]]
    targets = (plan.get("targets") or {}).get("cumulative") or []
    expected = {k: interpolate(targets, k, day) for k in ("mcq", "essays", "pts", "simulations")}
    actual = {"mcq": len(mcq), "essays": len(essays), "pts": len(pts), "simulations": len(sims)}
    matrix = C.load_matrix()
    mapped = sum(r["mapping_status"] in {"mapped", "verified"} for r in matrix)
    bank = {"mcq": len(C.load_mcqs()), "essays": len(C.load_md_items(C.ESSAY_DIR_REL)),
            "pts": len(C.load_md_items(C.PT_DIR_REL)), "rules": len(C.load_rules())}
    exam_day = parse_date(((plan.get("exam") or {}).get("dates") or ["2027-07-27"])[0])
    weak = sorted(((t, v) for t, v in by_topic.items() if len(v) >= 5), key=lambda x: sum(x[1]) / len(x[1]))[:8]
    errors = Counter(a["error_type"] for a in att if a["error_type"] not in {"", "none"})
    return {"day": day, "exam_day": exam_day, "days_left": (exam_day - day).days, "acc": acc, "n_recent": len(recent),
            "avg_secs": (sum(secs) / len(secs)) if secs else None, "by_subj": by_subj, "weak": weak,
            "written": written, "n_written": len(weighted), "essay_by_subj": essay_by_subj,
            "expected": expected, "actual": actual, "benchmark": current_benchmark(plan, day),
            "mapped": mapped, "matrix_rows": len(matrix), "bank": bank, "errors": errors}


def status(value, target, tol) -> str:
    if value is None or target is None:
        return "—"
    return "🟢 on track" if value >= target else ("🟡 watch" if value >= target - tol else "🔴 behind")


def render(d: dict) -> str:
    bm = d["benchmark"]
    acc = f"{100 * d['acc']:.0f}% (last {d['n_recent']})" if d["acc"] is not None else "no MCQs yet"
    wr = f"{d['written']:.1f} (last {d['n_written']} weighted)" if d["written"] is not None else "no essays yet"
    out = [f"_Generated {d['day'].isoformat()} by `scripts/dashboard.py`. Heuristic only — see the script docstring._", "",
           f"**{d['days_left']} days to the exam ({d['exam_day'].isoformat()}).**", "",
           "## Readiness", "", "| Signal | Now | Benchmark | Status |", "|---|---|---|---|",
           f"| MBE accuracy | {acc} | {('%.0f%%' % (100 * bm['mbe_accuracy'])) if bm.get('mbe_accuracy') else '—'}"
           f" by {bm.get('by', '—')} | {status(d['acc'], bm.get('mbe_accuracy'), 0.05)} |",
           f"| Written average (40–100) | {wr} | {bm.get('essay_avg', '—')} by {bm.get('by', '—')} | "
           f"{status(d['written'], bm.get('essay_avg'), 5)} |",
           f"| MBE pace | {('%.0fs/question' % d['avg_secs']) if d['avg_secs'] else '—'} | ≤108s | "
           f"{('🟢' if d['avg_secs'] and d['avg_secs'] <= 108 else '🟡') if d['avg_secs'] else '—'} |", "",
           "## Practice volume vs plan", "", "| Item | Done | Expected by today | Status |", "|---|---|---|---|"]
    for k, label in [("mcq", "MBE questions"), ("essays", "Essays"), ("pts", "Performance Tests"), ("simulations", "Full simulations")]:
        exp = d["expected"][k]
        out.append(f"| {label} | {d['actual'][k]} | {exp:.0f} | {status(d['actual'][k], exp, max(1, 0.1 * exp)) if exp else '—'} |")
    out += ["", "## MBE accuracy by subject", "", "| Subject | Attempts | Accuracy |", "|---|---|---|"]
    for code in C.MBE_CODES:
        v = d["by_subj"].get(code, [])
        out.append(f"| {C.SUBJECTS[code].name} | {len(v)} | {(f'{100 * sum(v) / len(v):.0f}%') if v else '—'} |")
    out += ["", "## Essay averages by subject", "", "| Subject | Essays | Average |", "|---|---|---|"]
    for code, s in C.SUBJECTS.items():
        v = d["essay_by_subj"].get(code, [])
        out.append(f"| {s.name} | {len(v)} | {(f'{sum(v) / len(v):.1f}') if v else '—'} |")
    out += ["", "## Weakest MBE topics (≥5 attempts)", ""]
    out += [f"- {t}: {100 * sum(v) / len(v):.0f}% over {len(v)}" for t, v in d["weak"]] or ["- not enough data yet"]
    out += ["", "## Error types", ""]
    out += [f"- {k}: {n}" for k, n in d["errors"].most_common()] or ["- none logged yet"]
    b = d["bank"]
    out += ["", "## Repo build-out", "",
            f"- Coverage matrix mapped: {d['mapped']}/{d['matrix_rows']} rows ({100 * d['mapped'] / max(1, d['matrix_rows']):.0f}%)",
            f"- Rule statements: {b['rules']} · MCQs: {b['mcq']} · Essays: {b['essays']} · PTs: {b['pts']}"]
    return "\n".join(out)


def readme_block(d: dict) -> str:
    acc = f"{100 * d['acc']:.0f}%" if d["acc"] is not None else "—"
    wr = f"{d['written']:.1f}" if d["written"] is not None else "—"
    b = d["bank"]
    return (f"| Days to exam | MBE Qs done | MBE accuracy (last 200) | Essays | Written avg | PTs | Matrix mapped | Bank (MCQ/essay/PT) |\n"
            f"|---|---|---|---|---|---|---|---|\n"
            f"| {d['days_left']} | {d['actual']['mcq']} | {acc} | {d['actual']['essays']} | {wr} | {d['actual']['pts']} | "
            f"{100 * d['mapped'] / max(1, d['matrix_rows']):.0f}% | {b['mcq']}/{b['essays']}/{b['pts']} |\n\n"
            f"_Updated {d['day'].isoformat()} by `python scripts/dashboard.py`; details in "
            f"[10-progress/readiness-dashboard.md](10-progress/readiness-dashboard.md)._")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Regenerate the readiness dashboard.")
    ap.add_argument("--stdout", action="store_true")
    ap.add_argument("--date", help="pretend today is YYYY-MM-DD (testing)")
    a = ap.parse_args(argv)
    d = compute(parse_date(a.date) if a.date else dt.date.today())
    body = render(d)
    if a.stdout:
        print(body)
        return 0
    fm = ("---\nsubject: progress\ntopic: Readiness dashboard (generated)\ncoverage_ids: []\ntested_on: [none]\n"
          "exam_frequency: {level: n/a, basis: \"Generated report\"}\n"
          f"last_verified: {d['day'].isoformat()}\nstatus: draft\n---\n\n# Readiness dashboard\n\n")
    out = C.p(C.DASHBOARD_REL)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(fm + body + "\n", encoding="utf-8")
    readme = C.p("README.md")
    if readme.exists():
        readme.write_text(C.replace_between_markers(readme.read_text(encoding="utf-8"), STATUS_MARKER,
                                                    readme_block(d)), encoding="utf-8")
    print(f"updated {C.DASHBOARD_REL} and README status block")
    return 0


if __name__ == "__main__":
    sys.exit(main())
