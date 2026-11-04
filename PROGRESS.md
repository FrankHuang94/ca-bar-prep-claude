# PROGRESS

**Target:** California General Bar Exam, **Tue–Wed July 27–28, 2027** (confirmed [S-001]). Fallback: Feb 2028, the last exam in the current format.
**Branch:** `claude/peaceful-darwin-ec2583` (currently the repo's default branch).
**Last updated:** 2026-11-04

## Phase status

| Phase | Status | Notes |
|---|---|---|
| 0 — Exam intelligence | ✅ Done | `00-exam-intel/` written. Coverage matrix v1: 614 rows. 36 items in VERIFY-QUEUE. |
| 1 — Scaffold and tooling | ✅ **Done (awaiting review)** | Structure, CLAUDE.md, config, schemas, 7 scripts, 22 tests, 11 slash commands, CI. Validation passes. |
| 2 — Foundations, strategy, study plan | ⏳ Next | Waiting for the user's "continue" |
| 3 — Past exams | ☐ | Archive covers Feb 2012 → July 2026 [S-079] |
| 4 — Subject content | ☐ | Groups: (1) CTR CIV CON CRM · (2) CMP REM · (3) EVD PRF WIL TRS · (4) TRT PRP BUS |
| 5 — Question bank | ☐ | |
| 6 — High-yield and memorization | ☐ | |
| 7 — Independent QA | ☐ | |
| 8 — Maintenance | ☐ | |

## Phase 1 deliverables
- **Structure:** every folder from the brief.
  - Subject READMEs for all 13 subjects: how each is tested, governing law, coverage-row counts, your coursework status, Phase 4 group.
  - Section READMEs; CSV headers (`attempts.csv`, `06-past-exams/index.csv`, `04-performance-test/past-pt-index.csv`).
  - Templates: `10-progress/error-log.md`, `05-mbe/official-practice-tracker.md`.
- **`CLAUDE.md`:** standing rules, your profile, phase protocol, ID and format conventions, tools, environment notes.
- **`config/plan.yml`:** exam, phases (provisional), weekly template, proposed leave, holidays, LLM, admissions milestones, targets and benchmarks (provisional).
- **Schemas** (`07-question-bank/schema/`): front matter, MCQ, essay, PT, simulation.
- **Scripts** (`scripts/`, shared `common.py`):
  - `validate.py`: front matter, matrix, citations, VERIFY tags, rules, MCQs, essays, PTs, simulations, flashcards, CSVs, links.
  - `coverage_report.py`: with the `--require-mapped` gate.
  - `quiz.py`: interactive + pick/show/log/stats.
  - `build_anki.py`, `build_simulation.py` (build + score), `frequency_analysis.py`, `dashboard.py`.
- **Tests:** `scripts/tests/` (22 pytest tests on a fixture repo) and `requirements.txt`.
- **Slash commands** (`.claude/commands/`): today, quiz, essay, pt, drill, spot, explain, weak-spots, weekly-review, simulate, update-exam-intel.
- **CI:** `.github/workflows/validate.yml` runs validate + pytest + the coverage report on every push and PR.
- **Generated:** `10-progress/readiness-dashboard.md`, `10-progress/coverage-report.md`, README status block.

## Decisions waiting on the user (carried from Phase 0; still open)
1. **Eligibility route (V-012).** PRC **lawyer's practice license (律师执业证)** in good standing, or only the **qualification certificate (法律职业资格证书)**?
2. **LLM end date (V-015).** Cardozo final-term end date and transcript timing. The State Bar must receive a sealed transcript by ≈ July 13, 2027.
3. **Online LLM (V-014).** Written eligibility determination from the Office of Admissions.
4. **Network access.** Allow calbar.ca.gov, ncbex.org, leginfo.legislature.ca.gov, courts.ca.gov, law.cornell.edu, supremecourt.gov, uscourts.gov, americanbar.org (still blocked as of Phase 1).
5. **Phase 2 inputs (optional but useful):**
   - known work travel and blackout weeks;
   - realistic weekday and weekend hours;
   - whether leave from mid-May 2027 is feasible;
   - Lunar New Year or other personal dates.

## Next (Phase 2 plan)
- **`02-foundations/`:**
  - `us-legal-system.md`, `california-legal-system.md`;
  - `common-law-for-civil-lawyers.md`, with the PRC→US concept map;
  - `legal-english-glossary.md` (EN–中文, approx.);
  - `how-the-bar-exam-tests-law.md`.
- **Strategy:**
  - `05-mbe/strategy.md` (and `subject-weighting.md` from the NCBE notes);
  - `09-exam-strategy/` (essay method, time management, exam-day logistics, mindset/fatigue);
  - `04-performance-test/method.md` + `task-types/` (structure only; past-PT examples come in Phase 3).
- **`01-study-plan/`:**
  - `master-plan.md`;
  - 38 weekly files `weeks/2026-W46.md … 2027-W30.md`;
  - `practice-targets.md`, with justification;
  - `spaced-repetition.md`.
- **Finalize `config/plan.yml`:** phases, hours, leave window, targets, benchmarks with go/adjust criteria.

## Handoff notes for a new session
- **Read `CLAUDE.md` first.** It holds all conventions.
- Run `python scripts/validate.py && python -m pytest -q scripts/tests` before every commit.
- **Do not** re-run `00-exam-intel/research/build_matrix_v1.py`. The matrix is now hand-maintained.
- Web search has a shared budget of about 200 calls per turn. Cap each research agent's searches.
- `config/plan.yml` values marked PROVISIONAL are placeholders until Phase 2.
