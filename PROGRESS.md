# PROGRESS

**Target:** California General Bar Exam, **Tue–Wed July 27–28, 2027** (confirmed [S-001]). Fallback: Feb 2028, the last exam in the current format.
**Branch:** `claude/peaceful-darwin-ec2583` (currently the repo's default branch).
**Last updated:** 2026-11-04

## Phase status

| Phase | Status | Notes |
|---|---|---|
| 0 — Exam intelligence | ✅ Done | `00-exam-intel/` written. Coverage matrix v1: 614 rows. 36 items in VERIFY-QUEUE. |
| 1 — Scaffold and tooling | ✅ Done | Structure, CLAUDE.md, config, schemas, 7 scripts, 22 tests, 11 slash commands, CI. Validation passes. |
| 2 — Foundations, strategy, study plan | ✅ **Done (awaiting review)** | 02-foundations (5 files, 475-term glossary), MBE/essay/PT strategy, 38-week plan; VERIFY V-040–V-060 |
| 3 — Past exams | ⏳ Next | Archive covers Feb 2012 → July 2026 [S-079] |
| 4 — Subject content | ☐ | Groups: (1) CTR CIV CON CRM · (2) CMP REM · (3) EVD PRF WIL TRS · (4) TRT PRP BUS |
| 5 — Question bank | ☐ | |
| 6 — High-yield and memorization | ☐ | |
| 7 — Independent QA | ☐ | |
| 8 — Maintenance | ☐ | |

## Phase 2 deliverables
- **`02-foundations/`:**
  - `us-legal-system.md`, `california-legal-system.md` (court counts verified via courts.ca.gov);
  - `common-law-for-civil-lawyers.md`, with a 57-row PRC→US concept map (approx.);
  - `legal-english-glossary.md` (475 terms, EN–中文, approx.);
  - `how-the-bar-exam-tests-law.md`.
- **`05-mbe/`:** `strategy.md` (approach, elimination, pacing, review taxonomy, worked question), `subject-weighting.md`.
- **`09-exam-strategy/`:** `essay-method.md`, `time-management.md`, `exam-day-logistics.md`, `mindset-and-fatigue.md`.
- **`04-performance-test/`:** `method.md` and 8 task-type templates. PT-SUP-001/002 are mapped.
- **`01-study-plan/`:**
  - `schedule.yml` is the source of truth;
  - 38 generated `weeks/` files (via the new `scripts/build_weeks.py`);
  - `master-plan.md`: phases, Gantt, leave options, rhythms, repo-build dependency, risks;
  - `practice-targets.md`: totals and justification, checkpoints CP1–CP5, go/adjust/escalate rules;
  - `spaced-repetition.md`.
- **`config/plan.yml`:** finalized phases, no leave (PTO for exam week only), targets and benchmarks aligned to the schedule.
- **Totals:** ≈ 754 h · 2,210 MBE · 75 essays · 52 `/spot` drills · 12 PTs · 3 simulations (all on weekends).
- **New sources and verify items:** S-140–S-150 and S-160; V-040–V-044, V-050–V-058 and V-060.

## Rework with the user's inputs (2026-11-04)

**Inputs**
1. Passed the PRC national exam but holds no practice license → **Route B, general applicant**.
2. Cardozo confirmed July 2027 eligibility; the final term ends **May or June 2027**.
3. **No study leave.** Capacity is 3–4 h every weekday + about 20 h on weekends.
4. Keep the agreed build order; the whole repo is being built now.

**Changes**
- **Phase 0:**
  - `admissions-checklist.md` rewritten for Route B only: general-applicant fees, a transcript-timing risk, and exam-week PTO.
  - V-012 and V-014 resolved; V-015 re-scoped to transcript timing.
  - `exam-day-logistics.md` fixed.
- **Phase 1:**
  - `CLAUDE.md` profile updated.
  - `config/plan.yml`: `leave: []`, new `pto:`, LL.M. end date.
  - `build_weeks.py`: new "evenings" day pattern (3.5 h weeknights + ~10 h weekend days).
- **Phase 2:**
  - Intensive and final weeks rebuilt for working full-time: timed essays on weeknights; PTs, long MBE sets and all simulations on weekends.
  - SIM-02 moved to Sat–Sun Jun 19–20 and SIM-03 to Sat–Sun Jul 10–11.
  - `master-plan.md` §4 is now "Making 35–40 h/week work without leave": PTO plan, cut order, sustainability.
  - `practice-targets.md` totals recomputed; `time-management.md` B4 rewritten.

## Decisions waiting on the user
1. **Capacity timing.** Does the 3–4 h/weekday + 20 h/weekend capacity apply **now** (foundation) or only from May? The plan currently assumes from May.
2. **Transcript timing (V-015).** Ask Cardozo when the final transcript issues after the May/June term. It must arrive at the State Bar by about Jul 13.
3. **Plan assumptions** (`master-plan.md` §8):
   - Fall finals week (assumed W51);
   - 2027 LL.M. courses;
   - travel and blackouts;
   - whether you'll buy licensed NCBE practice questions;
   - which optional PTO days are possible.
4. **Network access.** Still blocked (calbar.ca.gov, ncbex.org, leginfo, courts.ca.gov, law.cornell.edu, supremecourt.gov, uscourts.gov, americanbar.org).

## Next (Phase 3 plan): past exams
- **Index every published California essay and PT.** The Past Exams page covers Feb 2012 → July 2026; older files go back to July 2001 [S-079].
  - `06-past-exams/index.csv`: exam, Q#, subjects, issues (coverage_ids), call summary, links.
  - `04-performance-test/past-pt-index.csv`: task type and area.
- **Analyze each question in my own words:** `06-past-exams/analyses/<exam>-Q<n>.md` (issue map, rules needed, how the selected answers organized it, model approach) and `04-performance-test/analyses/`.
- **Add PAST rows to the coverage matrix** for every issue tested that the current rows don't cover. Re-weight subject `exam_frequency`.
- **Frequency analysis:** `python scripts/frequency_analysis.py` plus narrative and caveats in `06-past-exams/frequency-analysis.md`; feed it into `schedule.yml` essay slots and `grader-expectations.md` §5.
- **Constraints:**
  - Direct fetch of calbar.ca.gov is blocked, so indexing relies on search-index snippets (likely partial) unless network access is opened.
  - About 28 administrations × 5–6 questions means research must be batched across agents with search caps. Expect several turns.

## Handoff notes for a new session
- **Read `CLAUDE.md` first.** It holds all conventions.
- Run `python scripts/validate.py && python -m pytest -q scripts/tests` before every commit.
- **Do not** re-run `00-exam-intel/research/build_matrix_v1.py`. The matrix is now hand-maintained.
- Web search has a shared budget of about 200 calls per turn. Cap each research agent's searches.
- `config/plan.yml` values marked PROVISIONAL are placeholders until Phase 2.
