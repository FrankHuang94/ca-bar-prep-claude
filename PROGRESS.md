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
| 3 — Past exams | ✅ Done | 31 administrations (Feb 2012–Jul 2026): 166 essays + 42 PTs indexed and analyzed (index-level); frequency analysis; 2 PAST rows | Archive covers Feb 2012 → July 2026 [S-079] |
| 4 — Subject content | 🔄 **Groups 1–2 done (awaiting review)**: CTR, CIV, CON, CRM, CMP, REM; next group 3 (EVD, PRF, WIL, TRS) | Groups: (1) CTR CIV CON CRM · (2) CMP REM · (3) EVD PRF WIL TRS · (4) TRT PRP BUS |
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

## Phase 4 — group 2 deliverables (Community Property, Remedies)

| Subject | Rules | Flashcards | Outline (words) | Rows mapped | New verify items |
|---|---|---|---|---|---|
| Community Property | 103 (R-CMP-001–103) | 126 | ~15,300 (State Bar outline I–VIII + 5 SUP topics) | 51/51 | V-300–V-333 |
| Remedies | 94 (R-REM-001–094) | 120 | ~8,400 (State Bar outline I–VI) | 11/11 | V-350–V-371 |

- California-only subjects, so no `mbe-rules.md` (14 files each). Outlines follow the State Bar essay-outline structure.
- Remedies cross-references the contract damages rules (R-CTR-089–109) instead of repeating them.
- **Spot-checked:** transmutation (Fam. Code §§ 850, 852(a); *Benson*) and the specific-performance presumption for land (Civ. Code § 3387). Both accurate.
- **Coverage gate** passes for all six subjects built so far: 278 rows.

## Phase 4 — group 1 deliverables (Contracts, Civil Procedure, Constitutional Law, Criminal Law & Procedure)

All 15 files per subject. All **216 coverage rows mapped** (`coverage_report.py --require-mapped CTR CIV CON CRM` passes).

| Subject | Rules | Flashcards | Outline (words) | Rows mapped | New verify items |
|---|---|---|---|---|---|
| Contracts | 117 (R-CTR-001–117) | 150 | ~15,600 | 45/45 | V-100–V-114 |
| Civil Procedure | 120 (incl. 18 CCP rules) | 150 | ~10,200 (+ ~4,400 CA distinctions) | 50/50 | V-150–V-162 |
| Constitutional Law | 117 | 146 | ~24,500 | 68/68 | V-200–V-206 |
| Criminal Law & Procedure | 120 | 150 | ~24,700 | 53/53 | V-250–V-260 |

- **Built by 4 parallel subagents** from a shared brief (`CLAUDE.md` formats; NCBE-numbered outlines; matrix target headings).
- **Merged with the new `scripts/merge_build_outputs.py`**, which checks headings and inserts source and verify rows in ID order.
- **`recent-changes.md` additions:** Trump v. Cook, Hemani, Mullin v. Doe, GEO Group, Barrett, Hunter, and California Prop 36.
- **Spot-checked rules** (2-207, CA summary judgment 81/20/11, third-party standing, Miranda custody): citations and statements accurate.

## Phase 3 deliverables
- **`06-past-exams/index.csv`:** 166 essays, each with subjects, issue coverage_ids, call summary (my words), links to the question and selected-answer PDFs, and its analysis file.
- **`04-performance-test/past-pt-index.csv`:** 42 PTs with task type and area.
- **Analysis files:** `06-past-exams/analyses/<exam>-Q<n>.md` (166) and `04-performance-test/analyses/<exam>-<PT>.md` (42). Each has the question in brief, an issue map with coverage rows, the answer structure where captured, and a model approach. **Index-level only**: built from search summaries (V-070, V-071).
- **`06-past-exams/frequency-analysis.md`:** narrative plus generated tables (`scripts/frequency_analysis.py`). Key results:
  - **PR on 30/31 exams**;
  - CP 17, Contracts 16, Remedies 16, Crim 15, Evidence 15, BA 14, Real Property/Civ Pro/Con Law/Wills 13, Torts 12, Trusts 7 (usually with Wills);
  - top crossovers: Wills+Trusts, Contracts+Remedies, CP+Wills.
- **`00-exam-intel/grader-expectations.md` §5:** selected-answer patterns.
- **Coverage matrix v1.1:** +2 PAST rows (`BUS-PAST-001`, `WIL-PAST-001`); all other tagged issues mapped to existing rows.
- **Plan updates:** essay slots re-weighted (PR 11 + crossovers; CP 7; Remedies 6). Subject READMEs carry `exam_frequency` levels.
- **Provenance:** `06-past-exams/research/phase3-index.jsonl` (research records) and `build_phase3.py` (re-runnable builder).
- **Open item:** selected-answer headings and PT task types (16 undetermined) need a direct read of the PDFs once calbar.ca.gov is reachable.

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
1. ~~Capacity timing~~ **Answered:** the capacity applies from December. The plan is re-built at ≈ 1,200 h: first pass of all 13 subjects by Mar 28, SIM-01 on Apr 10–11, ≈ 3,140 MBE · 109 essays · 17 PTs · 74 `/spot` drills. Licensed questions are bought as needed.
2. **Transcript timing (V-015).** Ask Cardozo when the final transcript issues after the May/June term. It must arrive at the State Bar by about Jul 13.
3. **Plan assumptions** (`master-plan.md` §8):
   - Fall finals week (assumed W51);
   - 2027 LL.M. courses;
   - travel and blackouts;
   - which optional PTO days are possible.
4. **Network access.** Still blocked (calbar.ca.gov, ncbex.org, leginfo, courts.ca.gov, law.cornell.edu, supremecourt.gov, uscourts.gov, americanbar.org).

## Next (Phase 4 plan): subject content
- **Groups, in study order:** (1) CTR, CIV, CON, CRM · (2) CMP, REM · (3) EVD, PRF, WIL, TRS · (4) TRT, PRP, BUS.
- **Every subject folder gets all 15 files.** MBE subjects' `outline.md` follows NCBE numbering. California-only subjects follow the State Bar outline structure, informed by the past-exam issue maps.
- **Depth follows frequency**, using `06-past-exams/frequency-analysis.md` and each subject's issue list from `index.csv`.
- **Rule statements** in the CLAUDE.md format (`R-<CODE>-###`), each with an authority, an MBE-vs-CA line and an example. Apply every **Apply** item in `00-exam-intel/recent-changes.md`.
- **After each group:** `python scripts/coverage_report.py --require-mapped <codes>`; set rows to `mapped`; stop for review.
- **Subagents** build 2–3 subjects in parallel, each with an explicit WebSearch cap, distinct `V-###`/`S-###` ranges, and no shared-file edits. The coordinator merges sources, verify rows and matrix mappings.

## Handoff notes for a new session
- **Read `CLAUDE.md` first.** It holds all conventions.
- Run `python scripts/validate.py && python -m pytest -q scripts/tests` before every commit.
- **Do not** re-run `00-exam-intel/research/build_matrix_v1.py`. The matrix is now hand-maintained.
- Web search has a shared budget of about 200 calls per turn. Cap each research agent's searches.
- `config/plan.yml` values marked PROVISIONAL are placeholders until Phase 2.
