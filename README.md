# California Bar Exam (July 2027) — Master Knowledge Base

Personal, exam-focused knowledge base for the **July 27–28, 2027 California General Bar Exam**: five 1-hour essays, one 90-minute Performance Test, and the 200-question MBE. The pass line is 1390/2000.

**Where things stand:** [PROGRESS.md](PROGRESS.md) has phase status and next steps, and [VERIFY-QUEUE.md](VERIFY-QUEUE.md) lists open verification items. [CLAUDE.md](CLAUDE.md) holds the standing rules and conventions for every working session.

## Status dashboard
<!-- BEGIN STATUS -->
| Days to exam | MBE Qs done | MBE accuracy (last 200) | Essays | Written avg | PTs | Matrix mapped | Bank (MCQ/essay/PT) |
|---|---|---|---|---|---|---|---|
| 264 | 0 | — | 0 | — | 0 | 100% | 1050/85/8 |

_Updated 2026-11-05 by `python scripts/dashboard.py`; details in [10-progress/readiness-dashboard.md](10-progress/readiness-dashboard.md)._
<!-- END STATUS -->

## Start here
- [00-exam-intel/admissions-checklist.md](00-exam-intel/admissions-checklist.md): eligibility route, threats to a July 2027 sitting, dated to-do list.
- [00-exam-intel/format-and-scoring.md](00-exam-intel/format-and-scoring.md): what the exam looks like and how it is scored.
- [00-exam-intel/coverage-matrix-guide.md](00-exam-intel/coverage-matrix-guide.md): how completeness is defined and tracked.

## Layout

| Folder | What's in it |
|---|---|
| `00-exam-intel/` | Verified exam facts, admissions checklist, **coverage matrix**, recent law changes, grader expectations, source log |
| `01-study-plan/` | Week-by-week plan, practice targets, spaced repetition (Phase 2) |
| `02-foundations/` | US/CA legal systems, common law for civil lawyers, English–Chinese glossary (Phase 2) |
| `03-subjects/<subject>/` | 13 subjects: primer, outline, rule statements, CA distinctions, checklists, flowcharts, flashcards (Phase 4) |
| `04-performance-test/` | PT method, task-type templates, past-PT index and analyses |
| `05-mbe/` | MBE strategy, subject weighting, tracker for licensed practice questions |
| `06-past-exams/` | Index and analysis of every published CA essay; frequency analysis (Phase 3) |
| `07-question-bank/` | Original MCQs, essays, PTs, simulations; JSON Schemas (Phase 5) |
| `08-high-yield/` | Condensed review sets (Phase 6) |
| `09-exam-strategy/` | Essay method, time management, logistics, mindset (Phase 2) |
| `10-progress/` | Attempt log, error log, weekly reviews, readiness dashboard |
| `config/plan.yml` | Exam date, phases, weekly hours, leave, holidays, targets, benchmarks |
| `scripts/` | Validation and study tools (below) |

## Usage

### Setup
```bash
pip install -r requirements.txt          # Python 3.11+
python scripts/validate.py               # must pass before every commit (CI runs it too)
python -m pytest -q scripts/tests        # tool tests
```

### Practice
```bash
python scripts/quiz.py run --subject evidence --n 20 --timed      # interactive MBE quiz (logs to 10-progress/attempts.csv)
python scripts/quiz.py run --subject mixed --n 33 --difficulty 2  # mixed set
python scripts/quiz.py run --subject torts --subtopic TRT-MBE-II  # only negligence questions
python scripts/quiz.py stats                                      # accuracy by subject
python scripts/quiz.py log --source official --item "NCBE-OPE-3-Q12" --subject EVD --correct N --seconds 120
                                                                  # log a licensed question (no text stored)
```

### Memorization
```bash
python scripts/build_anki.py                          # all flashcards -> exports/ca-bar-2027-all.apkg
python scripts/build_anki.py --subject CMP --include-rules --tag must-know
```
Import the `.apkg` file into Anki. Card IDs are stable, so re-importing updates cards instead of duplicating them.

### Mock exams
```bash
python scripts/build_simulation.py build              # 5 essays + PT + 200 MCQs -> exports/SIM-##/ booklets
python scripts/build_simulation.py score SIM-01 --mbe-answers my-answers.txt
```

### Reports
```bash
python scripts/dashboard.py                           # readiness dashboard + the status block above
python scripts/coverage_report.py --write             # matrix mapping by subject -> 10-progress/coverage-report.md
python scripts/coverage_report.py --require-mapped CTR CIV   # Phase 4 definition-of-done gate
python scripts/frequency_analysis.py                  # past-exam heatmap and top issues (after Phase 3)
python scripts/build_weeks.py --from 2027-W05         # re-render weekly plan files after editing 01-study-plan/schedule.yml
python scripts/bank_targets.py                        # weak MBE topics and essay subjects; where the question bank should grow
```

### Slash commands (Claude Code)
| Command | What it does |
|---|---|
| `/today [hours]` | Exactly what to do today, from the plan and your available time |
| `/quiz <subject\|mixed> [n] [difficulty] [subtopic]` | Timed MBE questions one at a time; every option explained; logged |
| `/essay <subject\|crossover\|past:YYYY-MM-Qn> [timed]` | Essay prompt, then California-style grading on the 40–100 scale |
| `/pt [past:YYYY-MM\|original]` | 90-minute Performance Test, graded against the task |
| `/drill <subject> [n]` | Type rule statements from memory; graded for completeness |
| `/spot <subject\|crossover>` | 10-minute issue-spotting drill with the full issue map |
| `/explain <topic>` | Teach a rule with flowchart and example, then quiz it |
| `/weak-spots` | Diagnose from attempts and the error log; 1-week remediation plan |
| `/weekly-review` | Progress vs. plan; refresh the dashboard; adjust next week |
| `/simulate` | Assemble, run and score a full mock exam |
| `/update-exam-intel` | Re-check State Bar and NCBE pages; update dates, deadlines and law changes |
| `/monthly-maintenance [YYYY-MM]` | Phase 8 cycle: exam intel, dashboard, bank expansion in weak areas, VERIFY burn-down, log |
