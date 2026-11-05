---
description: Monthly maintenance cycle (Phase 8) — exam intel, dashboard, bank expansion in weak areas, VERIFY burn-down, log
argument-hint: "[month, e.g. 2026-12; default current]"
---
Run the monthly maintenance cycle for $ARGUMENTS (default: the current month). Read `CLAUDE.md` and `PROGRESS.md` first. **WebSearch cap for the whole cycle: 120.** Give each delegated agent an explicit cap and its own S-/V- ID ranges (the next free IDs are after the last rows of `00-exam-intel/sources.md` and `VERIFY-QUEUE.md`).

1. **Exam intel.** Run `/update-exam-intel`, capped at 40 searches. Put any plan impact (a deadline, fee, format or eligibility change) at the top of your reply. Apply every law change marked **Apply** to the subject files it touches (rule statement, outline, ca-distinctions, flashcards). Then grep `07-question-bank/` and `08-high-yield/` for the affected rule IDs and fix them too.
2. **Dashboard.** Run `python scripts/dashboard.py`.
3. **Weak areas and bank expansion.** Run `python scripts/bank_targets.py`.
   - For each **EXPAND** topic, write new MCQs (or essays) following the Phase 5 pipeline:
     1. writer, then the writer's own cold re-solve;
     2. an independent blind solve, written before the solver sees the key;
     3. an explanation audit;
     4. fixes, then a key check showing that no existing key changed.
   - Keep the length-cue limit: the key is the longest option in no more than about 30% of items.
   - New IDs continue each subject's sequence. Tag new items `phase8` and `<month>`.
   - If there are no attempts yet, skip this step and say so. Never invent weak areas.
   - Also run `/weak-spots` if the user has logged attempts in the last 30 days.
4. **VERIFY burn-down.** Work the High and Med open items first: about 20 items, with at most 60 searches. Use `confirmed-primary (search)` or `confirmed-secondary (search)`.
   - **Resolved items:** move the row to *Resolved* with `python scripts/merge_build_outputs.py --resolve` and replace every inline tag with the confirming source.
   - **Partly confirmed items:** narrow the row to the unconfirmed part.
5. **Status.** A file whose last open tag was cleared moves from `reviewed` to `verified`. A file with a new open tag moves back to `reviewed`. Set `last_verified` on every file you change.
6. **Log the cycle.** Add a dated section to `10-progress/maintenance-log.md` covering:
   - plan impacts;
   - law changes applied;
   - bank items added, by topic;
   - VERIFY counts before and after (open/resolved);
   - anything that needs the user.
7. Run `python scripts/validate.py --strict` and `python -m pytest -q scripts/tests`. If flashcards changed, rebuild the Anki decks (`build_anki.py --include-rules --out exports/ca-bar-2027-full.apkg`; `--tag must-know --include-rules --out exports/ca-bar-2027-must-know.apkg`). Commit in small scoped commits (e.g. `maintenance: <month> exam-intel update`) and push. Summarize in 10 lines or fewer.
