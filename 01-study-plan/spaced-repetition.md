---
subject: study-plan
topic: Spaced repetition and memorization system
coverage_ids: []
tested_on: [MBE, essay]
exam_frequency: {level: n/a, basis: "Planning document"}
last_verified: 2026-11-04
status: draft
---

# Spaced repetition and memorization

**Goal:** you can write every must-know rule statement from memory, and recognize the rule behind every MBE fact pattern, on July 27. This system has five loops. `/today` reads them to build each day's "due" list.

## 1. The five loops

| Loop | What | Tool | Cadence |
|---|---|---|---|
| 1. Flashcards | Rule fragments, elements, CA-vs-MBE splits, numbers (e.g. deadlines, thresholds) | Anki deck built by `python scripts/build_anki.py --include-rules` from `03-subjects/*/flashcards.csv` and `rule-statements.md` | **Daily**, 10–20 min (more on leave). Anki schedules the intervals. |
| 2. Rule drills | Full essay-ready rule statements typed from memory | `/drill <subject>` | Expanding intervals: §2 |
| 3. Missed MBE questions | Questions you got wrong | `quiz.py pick` puts missed questions first once ≥ 2 days old | Automatic, inside every `/quiz` |
| 4. Error log | Rules you missed on any item, with root cause | `10-progress/error-log.md` "Revisit on" column | +3, +7, +14 days after the miss |
| 5. Memorization cycles | Attack outlines and memorization lists, subject by subject | `03-subjects/*/attack-outline.md`, `memorization-list.md` | Intensive: 3 full cycles (W25, W26, W27); final 2 weeks: must-know tier daily |

## 2. Rule-drill intervals

When a rule is first learned (the week its subject is studied), drill it on day 0. Then follow the schedule below, using the `/drill` score (0–3):

| Score | Next drill |
|---|---|
| 3 (complete, essay-ready) | Next interval: **3 → 7 → 21 → 45 days**, then every 45 days until the exam |
| 2 (missing an element or qualifier) | Same interval again |
| 0–1 | Back to 1 day, and add an error-log row |

- **Must-know rules** (`memorization-list.md`) never go longer than **21 days** without a drill after May 1.
- `/today` finds due rules by reading the dates and scores of your `--kind drill` rows in `10-progress/attempts.csv`.

## 3. Anki settings (recommended)

| Setting | Foundation (working) | On leave |
|---|---|---|
| New cards per day | 15–20 | 30–40 |
| Maximum reviews per day | No cap. Clear all due cards. | No cap |
| Deck order | Subjects in study order. Add each subject's deck the week you start it. | All subjects |

Re-export after each content phase (`build_anki.py`). Note IDs are stable, so Anki updates cards in place and keeps your review history.

## 4. Interleaving and decay rules
- **Interleaving:** from week 4, every weekly MBE target includes **≥ 30% questions from subjects studied earlier**. The `mix` in `schedule.yml` already does this.
- **Decay check:** if a studied subject has **no MBE or drill attempt in 21 days**, `/today` adds a 15–20 question refresher set and a 10-rule drill for it.
- **Crossover rehearsal:** from W19, at least one crossover essay per week. Crossovers test whether you can retrieve two subjects' rules in one sitting.

## 5. Weekly memory review (Sunday, inside `/weekly-review`)
1. Clear all due Anki cards.
2. Re-drill every rule that scored 0–1 this week.
3. Read the week's error-log rows and write each one's memory hook again from memory.
4. Skim the attack outline of each subject studied this week. This takes 10 minutes per subject.

## 6. Memorization cycles (intensive and final review)

| Cycle | Week | What |
|---|---|---|
| Subject cycles | W19–W23 | During each subject's second pass: its attack outline from memory, then compare and correct |
| Cycle 1 | W25 | All 13 attack outlines: write each one's skeleton (headings + rule names) from memory in 15 min, then fix the gaps |
| Cycle 2 | W26 | Same, aiming for the full rule statements of the must-know tier |
| Cycle 3 | W27 | Same, timed, after SIM-03 |
| Final | W28–W29 | `08-high-yield/final-2-weeks-review.md` and the must-know tier daily; no new cards after W28 |

## 7. How `/today` builds the due list (priority order)
1. Admissions deadlines within 14 days (hard gates).
2. Anki due cards.
3. Error-log rows whose "Revisit on" date has passed.
4. Rule drills due under §2.
5. Missed MBE questions due for review (first picks of `quiz.py pick`).
6. Decay refreshers under §4.
7. The week's planned learning and practice from `weeks/<ISO week>.md`.
