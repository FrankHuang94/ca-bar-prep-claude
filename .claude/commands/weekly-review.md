---
description: Weekly review — progress vs plan, refresh the dashboard, adjust next week
argument-hint: "[ISO week, default current]"
---
Run the weekly review for $ARGUMENTS (default: the current ISO week, `date +%G-W%V`).

1. Run `python scripts/dashboard.py`. Read `10-progress/readiness-dashboard.md`, this week's plan `01-study-plan/weeks/<week>.md`, and `config/plan.yml` (targets and benchmarks).
2. Compare **planned vs. done** for the week: hours (ask the user for actual hours if they weren't logged), MCQs, essays, PTs, drills, and subjects covered. Check cumulative volume and the **benchmark** for the current date.
3. Decide for each benchmark: **go**, **adjust** or **escalate**.
   - **adjust:** rebalance next week.
   - **escalate:** the plan itself needs to change, for example adding hours, moving the leave start or cutting scope. Propose the change and ask the user before editing `config/plan.yml`.
4. Write `10-progress/weekly-reviews/<week>.md` (front matter `subject: progress`) with:
   - wins;
   - misses and why;
   - metrics table;
   - benchmark status;
   - changes to next week.
5. Apply the adjustments in `01-study-plan/schedule.yml`, which is the source of truth, then re-render with `python scripts/build_weeks.py --from <next week>`. List the edits in the review. Never hand-edit the generated week files.
6. Run `python scripts/validate.py`. Commit (`progress: weekly review <week>`) and push.
