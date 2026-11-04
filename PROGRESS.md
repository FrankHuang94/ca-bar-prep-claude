# PROGRESS

**Target:** California General Bar Exam, **Tue–Wed July 27–28, 2027** (confirmed [S-001]). Fallback: Feb 2028, the last exam in the current format.
**Branch:** `claude/peaceful-darwin-ec2583` (currently the repo's default branch).
**Last updated:** 2026-11-04

## Phase status

| Phase | Status | Notes |
|---|---|---|
| 0 — Exam intelligence | ✅ **Done (awaiting review)** | `00-exam-intel/` written. Coverage matrix v1: 614 rows. 36 items in VERIFY-QUEUE. |
| 1 — Scaffold and tooling | ⏳ Next | Waiting for the user's "continue" |
| 2 — Foundations, strategy, study plan | ☐ | |
| 3 — Past exams | ☐ | Archive covers Feb 2012 → July 2026 [S-079] |
| 4 — Subject content | ☐ | |
| 5 — Question bank | ☐ | |
| 6 — High-yield and memorization | ☐ | |
| 7 — Independent QA | ☐ | |
| 8 — Maintenance | ☐ | |

## Phase 0 deliverables
- `00-exam-intel/format-and-scoring.md`: format, timing, phased grading, score math, pass rates (including the foreign-educated category).
- `00-exam-intel/admissions-checklist.md`: eligibility routes, FYLSX answer, threats, dated checklist, fees.
- `00-exam-intel/coverage-matrix.csv` and `coverage-matrix-guide.md`: 614 rows (387 MBE, 176 State Bar essay outline, 51 supplemental); all targets `planned`.
- `00-exam-intel/recent-changes.md`: FRE, FRCP, CCP, CEC, CA RPC, Probate/Family, Supreme Court decisions.
- `00-exam-intel/grader-expectations.md`: official instructions and grading facts, plus the repo's practice rubric.
- `00-exam-intel/format-change-tracker.md`: NextGen from July 2028; California component.
- `00-exam-intel/sources.md`: source log (S-001 … S-133).
- `00-exam-intel/research/`: Phase 0 outline reconstructions and the one-time matrix builder (provenance only).
- `scripts/validate.py`: Phase 0 validator (front matter, matrix schema and mapping, source citations, VERIFY tags).
- `VERIFY-QUEUE.md`: V-001 … V-036.

## Decisions waiting on the user
1. **Eligibility route (V-012).** Do you hold a PRC **lawyer's practice license (律师执业证)** in good standing, or only the **legal professional qualification certificate (法律职业资格证书)**? This decides Route A (attorney applicant, no LLM needed) vs. Route B (LLM route).
2. **LLM end date (V-015).** When does Cardozo's final term end, and when are final transcripts issued? The State Bar must **receive** a sealed transcript about two weeks before the exam (≈ July 13, 2027).
3. **Online LLM (V-014).** Ask the Office of Admissions for a written eligibility determination now.
4. **Network access.** Allow these domains in the environment so Phase 1+ can read primary sources directly and clear V-001, V-023–V-026: calbar.ca.gov, ncbex.org, leginfo.legislature.ca.gov, courts.ca.gov, law.cornell.edu, supremecourt.gov, uscourts.gov, americanbar.org.

## Next (Phase 1 plan)
- Repo scaffold (all folders), `CLAUDE.md` (standing rules, conventions, user profile), `config/plan.yml`.
- JSON Schemas (MCQ, essay, PT, attempts), and scripts: extend `validate.py`; add `coverage_report.py`, `quiz.py`, `build_anki.py`, `build_simulation.py`, `frequency_analysis.py`, `dashboard.py`; `requirements.txt`.
- `.claude/commands/` (11 slash commands), `.github/workflows/validate.yml`, README usage section.
- Validation must pass on the scaffold.

## Handoff notes for a new session
- **Conventions already fixed in Phase 0:**
  - Citations use `[S-###]`, resolved in `00-exam-intel/sources.md`.
  - Uncertainty uses `[VERIFY V-###]`, logged in `VERIFY-QUEUE.md`.
  - Content files need YAML front matter with: subject, topic, coverage_ids, tested_on, exam_frequency {level, basis}, last_verified, status.
  - Coverage IDs are `<SUBJ>-<SOURCE>-<ref>`. Subject codes: BUS, CIV, CMP, CON, CTR, CRM, EVD, PRF, PRP, REM, TRT, WIL, TRS, plus PT.
- Do **not** re-run `00-exam-intel/research/build_matrix_v1.py` after Phase 1: it would overwrite matrix mappings.
- Web search has a shared budget of about 200 calls per turn. Cap each research agent's searches.
