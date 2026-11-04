---
subject: question-bank
topic: Question bank (Phase 5)
coverage_ids: []
tested_on: [MBE, essay, PT]
exam_frequency: {level: n/a, basis: "Scaffold file"}
last_verified: 2026-11-04
status: draft
---

# Question bank

All items are **original** (`source: original`); no NCBE or commercial questions are reproduced.

| Folder | Format | Schema |
|---|---|---|
| `mcq/<subject>/*.yaml` | one question, or `questions: [...]` per file | `schema/mcq.schema.json` |
| `essays/<subject>/E-XXX-###.md`, `essays/crossover/E-XO-###.md` | front matter + Facts / Call of the Question / Issue List / Model Answer / Self-Grading Rubric | `schema/essay.schema.json` |
| `pt/PT-###.md` | front matter + Task Memorandum / File / Library / Model Answer / Grading Rubric | `schema/pt.schema.json` |
| `simulations/SIM-##.yaml` | manifest written by `scripts/build_simulation.py` | `schema/simulation.schema.json` |

Targets: ≥150 MCQs per MBE subject, ≥8 essays per subject (≥30% crossovers), ≥8 PTs, ≥3 simulations.
