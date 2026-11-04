#!/usr/bin/env python3
"""Render 01-study-plan/weeks/<ISO week>.md from 01-study-plan/schedule.yml + config/plan.yml.

Usage
  python scripts/build_weeks.py --force              # (re)write every week file
  python scripts/build_weeks.py --from 2027-W05      # re-render this week and later (after a plan change)
  python scripts/build_weeks.py --totals             # print cumulative practice totals per checkpoint only

Without --force/--from, existing week files are left untouched (only missing weeks are written).
Also refreshes the generated overview table in 01-study-plan/master-plan.md (marker WEEK-TABLE).
"""
from __future__ import annotations

import argparse
import datetime as dt
import sys

import yaml

import common as C

SCHEDULE_REL = "01-study-plan/schedule.yml"
WEEKS_REL = "01-study-plan/weeks"
MASTER_REL = "01-study-plan/master-plan.md"
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# share of the week's hours per day, by day pattern
PATTERNS = {
    "working": [0.11, 0.11, 0.11, 0.11, 0.06, 0.25, 0.25],          # foundation/integration alongside work
    "evenings": [0.092, 0.092, 0.092, 0.092, 0.092, 0.27, 0.27],    # intensive without leave: 3-4 h weeknights + ~10 h/day weekends
    "leave": [0.155, 0.155, 0.155, 0.155, 0.155, 0.155, 0.07],      # full-time study leave (if config/plan.yml lists one)
}


def week_monday(week: str) -> dt.date:
    year, w = week.split("-W")
    return dt.date.fromisocalendar(int(year), int(w), 1)


def parse_date(s) -> dt.date:
    return s if isinstance(s, dt.date) else dt.date.fromisoformat(str(s))


def on_leave(plan: dict, monday: dt.date) -> bool:
    for lv in plan.get("leave") or []:
        if parse_date(lv["start"]) <= monday <= parse_date(lv["end"]):
            return True
    return False


def pattern_for(w: dict, plan: dict, monday: dt.date) -> str:
    if on_leave(plan, monday) and w["phase"] in {"intensive", "final-review", "exam"}:
        return "leave"
    if w["phase"] in {"intensive", "final-review", "exam"} or w["hours"] >= 25:
        return "evenings"  # 3-4 h weeknights + ~10 h weekend days while working
    return "working"


def fmt_hours(h: float) -> str:
    return f"{h:g}" if h else "0"


def subj_label(code: str) -> str:
    if code in C.SUBJECTS:
        return C.SUBJECTS[code].name
    return {"MIX": "mixed (all subjects)", "XO": "crossover", "WEAK": "weakest subject (dashboard)"}.get(code, code)


def quiz_cmds(mbe: dict, sim: dict | None = None) -> list[str]:
    out = []
    in_sim = 200 if sim else 0
    for code, n in (mbe.get("mix") or {}).items():
        if code == "MIX" and in_sim:
            take = min(n, in_sim)
            out.append(f"{take} inside {sim['id']} (`/simulate`)")
            n, in_sim = n - take, in_sim - take
            if not n:
                continue
        target = "mixed" if code == "MIX" else C.SUBJECTS[code].slug
        out.append(f"`/quiz {target} {n}`")
    return out


def day_plan(w: dict, plan: dict, monday: dt.date) -> list[tuple[str, str, float, str]]:
    pat = pattern_for(w, plan, monday)
    weights = PATTERNS[pat]
    holidays = {parse_date(h["date"]): h["name"] for h in plan.get("holidays") or []}
    admin = {}
    for a in plan.get("admissions") or []:
        admin.setdefault(parse_date(a["date"]), []).append(a["task"])
    overrides = w.get("overrides") or {}
    learn_short = "; ".join(x.split(":")[0] for x in w.get("learn") or [])[:110]
    essays = w.get("essays") or {}
    n_ess = essays.get("n", 0) if essays.get("mode") != "simulation" else 0
    pt = w.get("pt") or {}
    n_pt = pt.get("n", 0) if pt.get("mode") != "simulation" else 0
    spot = w.get("spot", 0)
    rows = []
    if pat == "working":
        essay_days = ["Sat", "Wed", "Sun"][:n_ess]
        pt_day = "Sun" if n_pt else None
        spot_days = ["Tue", "Thu", "Sat"][:spot]
    elif pat == "evenings":
        essay_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sun"][:n_ess]
        pt_day = "Sat" if n_pt else None
        spot_days = ["Tue", "Thu", "Sat", "Sun"][:spot]
    else:
        essay_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"][:n_ess]
        pt_day = "Sat" if n_pt else None
        spot_days = ["Tue", "Thu", "Mon", "Wed"][:spot]
    for i, d in enumerate(DAYS):
        date = monday + dt.timedelta(days=i)
        hrs = round(w["hours"] * weights[i] * 4) / 4
        parts = []
        if d in overrides:
            parts.append(f"**{overrides[d]}**")
        elif pat == "working":
            if d in {"Mon", "Tue", "Wed", "Thu"}:
                parts.append(f"Learn: {learn_short} · MBE mini-set + review")
            elif d == "Fri":
                parts.append("Light: `/drill` on this week's rules")
            elif d == "Sat":
                parts.append("Learn block (outline + rule statements)")
            else:
                parts.append("Timed MBE set + full review · `/weekly-review`")
        elif pat == "evenings" and w["phase"] in {"foundation", "integration"}:
            if d == "Sat":
                parts.append(f"Long block (~{fmt_hours(hrs)} h): learn {learn_short} (AM) · timed MBE set + review (PM)")
            elif d == "Sun":
                parts.append("Long block: timed MBE set + review · learn/consolidate · `/weekly-review`")
            else:
                parts.append(f"Evening (3–4 h): learn {learn_short} (≈90 min) · MBE set + review · rule statements")
        elif pat == "evenings":
            if d in {"Sat", "Sun"}:
                if w["phase"] == "final-review":
                    parts.append("Long block: high-yield reading + attack outlines · short timed MBE set")
                elif d == "Sat":
                    parts.append("Long block (~10 h): second-pass reading (AM) · long timed MBE set + review (PM)")
                else:
                    parts.append("Long block (~10 h): timed MBE set + review · second-pass reading · `/weekly-review`")
            elif w["phase"] == "final-review":
                parts.append("Evening: short timed MBE set + must-know list")
            else:
                parts.append("Evening (3–4 h): timed MBE set (15–20 Qs) + review · rule statements")
        else:
            if d == "Sun":
                parts.append("Rest / light: Anki + `/weekly-review`")
            elif w["phase"] == "final-review":
                parts.append("AM high-yield reading · short timed MBE set · PM memorization list")
            else:
                parts.append("AM timed MBE set + review · PM second-pass reading + rule statements")
        if d in essay_days and d not in overrides:
            subj = (essays.get("subjects") or ["MIX"])[essay_days.index(d) % len(essays.get("subjects") or ["MIX"])]
            parts.append(f"Essay ({essays.get('mode', 'timed')}): {subj_label(subj)} → `/essay`")
        if d == pt_day and d not in overrides:
            parts.append(f"PT ({pt.get('mode', 'timed')}) → `/pt`")
        if d in spot_days and d not in overrides:
            parts.append("`/spot` (10 min)")
        if d not in overrides and w["phase"] != "exam" and not any("Anki" in x for x in parts):
            parts.append("Anki 10–20 min")
        note = []
        if date in holidays:
            note.append(f"🎌 {holidays[date]}")
        for t in admin.get(date, []):
            note.append(f"📌 {t}")
        rows.append((d, date.strftime("%b %d"), hrs, " · ".join(parts) + (" — " + "; ".join(note) if note else "")))
    return rows


def cumulative(weeks: list[dict]) -> list[dict]:
    tot = {"hours": 0.0, "mbe": 0, "essays": 0, "pt": 0, "spot": 0}
    out = []
    for w in weeks:
        tot["hours"] += w["hours"]
        tot["mbe"] += (w.get("mbe") or {}).get("n", 0)
        tot["essays"] += (w.get("essays") or {}).get("n", 0)
        tot["pt"] += (w.get("pt") or {}).get("n", 0)
        tot["spot"] += w.get("spot", 0)
        out.append(dict(tot))
    return out


def render(w: dict, cum: dict, plan: dict, idx: int, n_weeks: int) -> str:
    monday = week_monday(w["week"])
    sunday = monday + dt.timedelta(days=6)
    exam = parse_date(((plan.get("exam") or {}).get("dates") or ["2027-07-27"])[0])
    weeks_left = (exam - monday).days // 7
    pat = pattern_for(w, plan, monday)
    mbe, essays, pt = w.get("mbe") or {}, w.get("essays") or {}, w.get("pt") or {}
    fm = (f"---\nsubject: study-plan\ntopic: \"Week {w['week']} ({monday:%b %d} – {sunday:%b %d, %Y})\"\n"
          f"coverage_ids: []\ntested_on: [MBE, essay, PT]\n"
          f"exam_frequency: {{level: n/a, basis: \"Weekly study plan\"}}\nlast_verified: {C.today()}\nstatus: draft\n---\n\n")
    lines = [f"# Week {w['week']} · {monday:%a %b %d} – {sunday:%a %b %d, %Y}",
             "",
             "_Generated from `01-study-plan/schedule.yml` by `scripts/build_weeks.py` — edit the schedule, not this file._",
             "",
             f"**Theme:** {w['theme']}",
             "",
             "| | |", "|---|---|",
             f"| Phase | {w['phase']} (week {idx + 1} of {n_weeks}; {weeks_left} weeks to the exam) |",
             f"| Target hours | **{fmt_hours(w['hours'])} h** ({ {'leave': 'study leave / full-time', 'evenings': 'while working: 3–4 h weeknights + ~10 h per weekend day'}.get(pat, 'alongside full-time work') }) |",
             f"| MBE questions | {mbe.get('n', 0)} ({', '.join(f'{subj_label(k)} {v}' for k, v in (mbe.get('mix') or {}).items()) or '—'}) |",
             f"| Essays | {essays.get('n', 0)}"
             + (f" ({essays.get('mode', 'timed')}: {', '.join(subj_label(s) for s in essays.get('subjects') or [])})" if essays.get('n') else "") + " |",
             f"| Issue-spotting drills | {w.get('spot', 0)} |",
             f"| Performance Tests | {pt.get('n', 0)}" + (f" ({pt.get('mode')})" if pt.get('n') else "") + " |",
             f"| Cumulative after this week | {fmt_hours(cum['hours'])} h · {cum['mbe']} MBE · {cum['essays']} essays · {cum['pt']} PTs · {cum['spot']} spot drills |"]
    if w.get("sim"):
        lines.append(f"| Simulation | **{w['sim']['id']}** on {' + '.join(w['sim']['days'])} → `/simulate` |")
    if w.get("checkpoint"):
        lines.append(f"| Checkpoint | **{w['checkpoint']}** — see `01-study-plan/practice-targets.md` (go / adjust / escalate) |")
    if w.get("buffer"):
        lines.append("| Buffer week | Yes — absorbs slippage, travel or holidays |")
    lines += ["", "## Learn", ""] + [f"- {x}" for x in w.get("learn") or []] + \
             ["", "## Reinforce", ""] + ([f"- {x}" for x in w.get("reinforce") or []] or ["- —"])
    cmds = quiz_cmds(mbe, w.get("sim"))
    lines += ["", "## Practice commands", ""]
    lines += ([f"- MBE: {' · '.join(cmds)}"] if cmds else []) + \
             ([f"- Essays: `/essay <subject> timed` ×{essays['n']}"] if essays.get("n") and essays.get("mode") != "simulation" else []) + \
             ([f"- Issue spotting: `/spot <subject>` ×{w['spot']}"] if w.get("spot") else []) + \
             ([f"- PT: `/pt` ×{pt['n']}"] if pt.get("n") and pt.get("mode") != "simulation" else []) + \
             ["- Daily: Anki (due cards) and `/drill <subject>` on this week's rules — see `01-study-plan/spaced-repetition.md`"]
    lines += ["", "## Day by day", "", "| Day | Date | Hours | Plan |", "|---|---|---|---|"]
    for d, date, hrs, text in day_plan(w, plan, monday):
        lines.append(f"| {d} | {date} | {fmt_hours(hrs)} | {text} |")
    if w.get("notes"):
        lines += ["", "## Notes", "", w["notes"]]
    lines += ["", "## End-of-week check", "",
              "- [ ] Hours done ≈ target", "- [ ] MBE target met and every miss reviewed (error type logged)",
              "- [ ] Essays/PT graded and logged; missed rules added to `10-progress/error-log.md`",
              "- [ ] `/weekly-review` run (updates the dashboard and next week)"]
    return fm + "\n".join(lines) + "\n"


def overview(weeks: list[dict], cums: list[dict], plan: dict) -> str:
    rows = ["| Week | Dates | Phase | Hours | Theme | MBE | Essays | PT | Cum. MBE / essays / PT |",
            "|---|---|---|---|---|---|---|---|---|"]
    for w, c in zip(weeks, cums):
        m = week_monday(w["week"])
        tag = f" **{w['checkpoint']}**" if w.get("checkpoint") else ""
        rows.append(f"| [{w['week']}](weeks/{w['week']}.md) | {m:%b %d} | {w['phase']} | {fmt_hours(w['hours'])} | "
                    f"{w['theme']}{tag} | {(w.get('mbe') or {}).get('n', 0)} | {(w.get('essays') or {}).get('n', 0)} | "
                    f"{(w.get('pt') or {}).get('n', 0)} | {c['mbe']} / {c['essays']} / {c['pt']} |")
    t = cums[-1]
    rows += ["", f"**Totals:** {fmt_hours(t['hours'])} hours · {t['mbe']} MBE questions · {t['essays']} essays "
             f"(incl. simulations) · {t['pt']} PTs · {t['spot']} issue-spotting drills."]
    return "\n".join(rows)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Render weekly plan files from schedule.yml.")
    ap.add_argument("--force", action="store_true", help="overwrite every week file")
    ap.add_argument("--from", dest="start", help="re-render this ISO week (YYYY-Www) and later")
    ap.add_argument("--totals", action="store_true", help="print cumulative totals at checkpoints and exit")
    a = ap.parse_args(argv)
    weeks = (C.load_yaml(C.p(SCHEDULE_REL)) or {}).get("weeks") or []
    plan = C.load_plan()
    cums = cumulative(weeks)
    if a.totals:
        for w, c in zip(weeks, cums):
            if w.get("checkpoint") or w is weeks[-1]:
                print(f"{w['week']} {w.get('checkpoint', 'END')}: {c}")
        return 0
    out_dir = C.p(WEEKS_REL)
    out_dir.mkdir(parents=True, exist_ok=True)
    written = 0
    for i, (w, c) in enumerate(zip(weeks, cums)):
        path = out_dir / f"{w['week']}.md"
        due = a.force or (a.start and w["week"] >= a.start) or not path.exists()
        if due:
            path.write_text(render(w, c, plan, i, len(weeks)), encoding="utf-8")
            written += 1
    gk = out_dir / ".gitkeep"
    if gk.exists() and written:
        gk.unlink()
    master = C.p(MASTER_REL)
    if master.exists():
        master.write_text(C.replace_between_markers(master.read_text(encoding="utf-8"), "WEEK-TABLE",
                                                    overview(weeks, cums, plan)), encoding="utf-8")
    print(f"wrote {written} week file(s); totals: {cums[-1] if cums else {}}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
