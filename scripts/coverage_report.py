#!/usr/bin/env python3
"""Coverage report: how much of the coverage matrix is mapped to content and to practice items.

Usage
  python scripts/coverage_report.py                      # summary table (all subjects)
  python scripts/coverage_report.py --subject CTR        # one subject, incl. row-level gaps
  python scripts/coverage_report.py --unmapped           # list every row not yet mapped
  python scripts/coverage_report.py --write              # also write 10-progress/coverage-report.md
  python scripts/coverage_report.py --require-mapped CTR CIV
        # exit 1 unless every row of those subjects is mapped (Phase 4 definition of done)

"Mapped" means mapping_status is mapped/verified AND the target heading exists in the target file.
"""
from __future__ import annotations

import argparse
import sys
from collections import defaultdict

import common as C
from validate import load_headings

REPORT_REL = "10-progress/coverage-report.md"


def analyse(rows: list[dict]) -> dict:
    heads_cache: dict = {}
    mcq_refs: dict[str, int] = defaultdict(int)
    essay_refs: dict[str, int] = defaultdict(int)
    for q in C.load_mcqs():
        for cid in q.get("coverage_ids") or []:
            mcq_refs[cid] += 1
    for item in C.load_md_items(C.ESSAY_DIR_REL) + C.load_md_items(C.PT_DIR_REL):
        for cid in item["_fm"].get("coverage_ids") or []:
            essay_refs[cid] += 1
    out = []
    for r in rows:
        target = C.p(r["target_file"]) if r["target_file"] else None
        heading_ok = False
        if target and target.exists():
            heads = heads_cache.setdefault(target, [h.lower() for h in load_headings(target)])
            heading_ok = any(r["target_heading"].strip().lower() in h for h in heads)
        mapped = r["mapping_status"] in {"mapped", "verified"} and heading_ok
        out.append({**r, "_mapped": mapped, "_heading_ok": heading_ok,
                    "_mcq": mcq_refs.get(r["coverage_id"], 0), "_essay": essay_refs.get(r["coverage_id"], 0)})
    return {"rows": out}


def summarize(rows: list[dict]) -> list[dict]:
    by: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        by[r["subject_code"]].append(r)
    order = list(C.SUBJECTS) + ["PT"]
    table = []
    for code in order:
        rs = by.get(code, [])
        if not rs:
            continue
        mbe_rows = [r for r in rs if "MBE" in r["tested_on"]]
        table.append({
            "code": code, "rows": len(rs),
            "mapped": sum(r["_mapped"] for r in rs),
            "verified": sum(r["mapping_status"] == "verified" for r in rs),
            "unconfirmed_src": sum(r["source_status"] == "unconfirmed" for r in rs),
            "with_mcq": sum(r["_mcq"] > 0 for r in mbe_rows), "mbe_rows": len(mbe_rows),
            "with_essay": sum(r["_essay"] > 0 for r in rs),
        })
    return table


def pct(a: int, b: int) -> str:
    return f"{(100 * a / b):.0f}%" if b else "—"


def render(table: list[dict], rows: list[dict], subjects: list[str] | None, show_unmapped: bool) -> str:
    lines = ["| Subject | Rows | Mapped | Verified | Source unconfirmed | MBE rows with MCQs | Rows with essay/PT |",
             "|---|---|---|---|---|---|---|"]
    tot = defaultdict(int)
    for t in table:
        if subjects and t["code"] not in subjects:
            continue
        name = C.SUBJECTS[t["code"]].name if t["code"] in C.SUBJECTS else C.EXTRA_CODES.get(t["code"], t["code"])
        lines.append(f"| {name} ({t['code']}) | {t['rows']} | {t['mapped']} ({pct(t['mapped'], t['rows'])}) | "
                     f"{t['verified']} | {t['unconfirmed_src']} | {t['with_mcq']}/{t['mbe_rows']} | {t['with_essay']} |")
        for k in ("rows", "mapped", "verified", "unconfirmed_src", "with_mcq", "mbe_rows", "with_essay"):
            tot[k] += t[k]
    lines.append(f"| **Total** | {tot['rows']} | {tot['mapped']} ({pct(tot['mapped'], tot['rows'])}) | {tot['verified']} | "
                 f"{tot['unconfirmed_src']} | {tot['with_mcq']}/{tot['mbe_rows']} | {tot['with_essay']} |")
    if show_unmapped or subjects:
        gaps = [r for r in rows if not r["_mapped"] and (not subjects or r["subject_code"] in subjects)]
        lines += ["", f"### Not yet mapped ({len(gaps)})", "",
                  "| coverage_id | heading | planned target | status |", "|---|---|---|---|"]
        for r in gaps:
            why = "heading missing" if r["mapping_status"] != "planned" and not r["_heading_ok"] else r["mapping_status"]
            lines.append(f"| {r['coverage_id']} | {r['heading'][:90]} | {r['target_file']} › {r['target_heading'][:50]} | {why} |")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Coverage-matrix mapping report.")
    ap.add_argument("--subject", action="append", help="subject code/slug (repeatable)")
    ap.add_argument("--unmapped", action="store_true", help="list rows not yet mapped")
    ap.add_argument("--write", action="store_true", help=f"write {REPORT_REL}")
    ap.add_argument("--require-mapped", nargs="+", metavar="CODE",
                    help="exit 1 unless every row of these subjects is mapped")
    args = ap.parse_args(argv)
    subjects = [C.resolve_subject(s) or s.upper() for s in args.subject] if args.subject else None
    data = analyse(C.load_matrix())
    table = summarize(data["rows"])
    text = render(table, data["rows"], subjects, args.unmapped)
    print(text)
    if args.write:
        out = C.p(REPORT_REL)
        out.parent.mkdir(parents=True, exist_ok=True)
        fm = ("---\nsubject: progress\ntopic: Coverage report (generated)\ncoverage_ids: []\ntested_on: [none]\n"
              "exam_frequency: {level: n/a, basis: \"Generated report\"}\n"
              f"last_verified: {C.today()}\nstatus: draft\n---\n\n")
        out.write_text(fm + "# Coverage report\n\n_Generated by `scripts/coverage_report.py` on "
                       f"{C.today()}. Do not edit by hand._\n\n" + render(table, data["rows"], None, True) + "\n",
                       encoding="utf-8")
        print(f"\nwrote {REPORT_REL}")
    if args.require_mapped:
        need = {C.resolve_subject(s) or s.upper() for s in args.require_mapped}
        missing = [r["coverage_id"] for r in data["rows"] if r["subject_code"] in need and not r["_mapped"]]
        if missing:
            print(f"\nFAIL: {len(missing)} unmapped row(s) in {sorted(need)}", file=sys.stderr)
            return 1
        print(f"\nOK: every row in {sorted(need)} is mapped")
    return 0


if __name__ == "__main__":
    sys.exit(main())
