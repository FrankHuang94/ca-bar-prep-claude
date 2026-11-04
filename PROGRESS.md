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
| 4 — Subject content | ✅ **Done (awaiting review)**: all 13 subjects built; all 616 coverage rows mapped | Groups: (1) CTR CIV CON CRM · (2) CMP REM · (3) EVD PRF WIL TRS · (4) TRT PRP BUS |
| 5 — Question bank | 🔄 **Wave 1 done (awaiting review)**: 350 MCQs, 39 essays, 3 PTs | Wave 2 (expansion to targets + simulations) next |
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

## Phase 5 — Wave 1 deliverables (question bank)

| Item | Count | Detail |
|---|---|---|
| MBE-style MCQs | **350** (50 × 7 MBE subjects) | `07-question-bank/mcq/<subject>/*.yaml`; one best answer, explanation for every wrong option, trap type, rule and coverage IDs; difficulty ≈ 12/25/13; answer letters balanced (12–13 each) |
| Essays | **39** (26 single + 13 crossovers = 33%) | 3 per subject incl. crossovers; each: original facts, State Bar-style calls, issue list summing to 100, 60-minute model answer, self-grading rubric |
| Performance Tests | **3** | PT-001 objective memo (UCC warranty), PT-002 persuasive brief (preliminary injunction / implied easement), PT-003 trust drafting + client letter |

- **MCQ distribution** follows the NCBE category weights:
  - Torts: negligence 25 of 50.
  - Crim: constitutional protections 24 of 50.
  - Real Property: the five categories 11/10/9/10/10.
  - Evidence: hearsay 13, relevance/character/experts 16.
  - Con Law: individual rights 25 of 50.
- **No MCQ turns on a VERIFY-tagged or very recent rule.** In particular, nothing depends on the Dec 2026 FRE 801(d)(1)(A) amendment (V-028).
- **Blind answer-key check.** An independent solver answered every MCQ without seeing the key. **It agreed with all 350 keys.**
  - Q-PRP-0037's stem was tightened to say the jurisdiction follows the traditional rule.
  - The other flags were minority-rule notes on items that already state the majority/MBE rule.
- **Crossover essays follow the past-exam pairs:** Wills+Trusts, CP+Wills, Contracts+Remedies, Torts+Remedies, BA+PR, Evidence+PR, Crim+Evidence, CP+PR, Con Law+Real Property, Civ Pro+Evidence, CP+Trusts, Real Property+Wills, BA+Remedies.
- **Governing law in the essays:**
  - Evidence: two essays use the California Evidence Code, two use the FRE.
  - PR: every essay says "California and ABA authorities".
  - CP, Wills and Trusts: California law.
- **PTs** are set in the fictional State of Columbia, with fictional Library law. Each PT opens with a study note that its law is closed-universe.
- **Subject-file corrections the item writers found:**
  - R-PRP-039/040: assignee liability lasts while the assignee holds the leasehold, not "while in possession".
  - R-TRT-028: informed-consent standards are split nationally; California follows *Cobbs*.
  - R-PRP-042: scope note (V-674).
  - R-CIV-106: *Lazar* fraud particularity added.
  - R-CRM-118/110 and R-CON-013: missing case authorities added.
- **Tooling:** the validator now also checks the coverage and rule IDs inside each essay issue (25 tests).
- **Known gaps for Wave 2:**
  - Fourth Amendment and Miranda are under-weighted (3-per-row cap).
  - Uncovered rows include CON I.A and II.A.2/II.A.4/II.B.2/II.C.2/II.C.3/IV.F.3, and CRM II.F/II.G/II.H/IV.F.
  - Only 3 PTs so far.

## Phase 4 — group 4 deliverables (Torts, Real Property, Business Associations) — Phase 4 complete

| Subject | Rules | Flashcards | Outline (words) | Rows mapped | New verify items |
|---|---|---|---|---|---|
| Torts | 115 (R-TRT-001–115) | 149 | ~17,100 (NCBE I–IV + State Bar outline sections) | 49/49 | V-600–V-611 |
| Real Property | 121 (R-PRP-001–121) | 147 | ~11,800 (+ ~30,100 rule statements; NCBE I–V + State Bar labels) | 104/104 | V-650–V-673 |
| Business Associations | 109 (R-BUS-001–109) | 129 | ~11,500 (State Bar outline I–VI + BUS-PAST-001) | 13/13 | V-700–V-729 |

- **Torts:** NCBE outline with negligence in depth. CA distinctions cover § 1714/*Rowland*, *Brown v. USA Taekwondo*, *Li* pure comparative fault, Prop 51, *Knight* assumption of risk, *Thing* bystander NIED, *Barker*/*Soule* design defect, MICRA and *Rattagan*.
- **Real Property:** NCBE outline with State Bar labels. CA distinctions cover race-notice (Civ. Code § 1214), adverse possession with taxes (CCP § 325), USRAP, *Riddle* severance, the warranty of habitability, *Kendall*, the Tenant Protection Act, Civ. Code § 1662 risk of loss, deeds of trust, and the one-action/anti-deficiency rules. Takings, trusts of land and spousal ownership are cross-referenced by rule ID.
- **Business Associations:** agency, partnerships (RUPA), LPs, LLPs, corporations (veil piercing, BJR/§ 309, § 310, § 500 distributions, § 800 derivative suits), securities (10b-5, insider trading, § 16(b)), LLCs and equitable subordination. California calls appear to ask for general law (V-700), so California Corporations Code points are added where the codes differ.
- **`recent-changes.md` additions (Torts):**
  - *Gilead Tenofovir Cases* (Aug 2026) — Apply [VERIFY V-603];
  - *Sanchez v. Rojas* (review of *Elden*) — watch [V-604];
  - MICRA 2027 caps $510,000 / $700,000 [V-601];
  - CCP § 377.34(b) survival pain-and-suffering window closed for actions filed from 2026 — Apply [V-602].
- **Spot-checked (accurate):**
  - Torts: bystander NIED, design defect burden shift, express assumption, Prop 51, § 1714/*Rowland*.
  - Real Property: recording-act types, adverse possession (incl. CCP § 325), RAP traps, severance, habitability, Uniform Vendor and Purchaser Risk Act, *Kendall*, § 580b.
  - Business Associations: BJR, § 310, § 500/501, veil piercing, § 16(b), *Dirks*/*Salman*, *Jones v. Ahmanson*.

### Phase 4 totals
- **13 subjects × 14–15 files:** 1,432 rule statements and 1,806 flashcards.
- **Coverage:** `coverage_report.py --require-mapped` passes for every code (616/616 rows mapped). `validate.py --strict`: 0 errors, 0 warnings.
- **Sources:** 502 logged. **VERIFY queue:** 335 open, 5 resolved. Most open items need a direct read of leginfo / courts.ca.gov / calbar.ca.gov, which this environment cannot fetch (V-001). They are the Phase 7 QA workload.

## Phase 4 — group 3 deliverables (Evidence, Professional Responsibility, Wills & Succession, Trusts)

| Subject | Rules | Flashcards | Outline (words) | Rows mapped | New verify items |
|---|---|---|---|---|---|
| Evidence | 115 (R-EVD-001–115) | 145 | ~23,500 (NCBE I–V + CA notes + State Bar outline section) | 92/92 | V-400–V-417 |
| Professional Responsibility | 100 (R-PRF-001–100) | 138 | ~8,400 (+ ~22,900 rule statements, ~3,900 CA-vs-ABA table) | 18/18 | V-450–V-473 |
| Wills & Succession | 105 (R-WIL-001–105) | 138 | ~15,500 (State Bar outline I–VIII + 7 SUP topics) | 42/42 | V-500–V-540 |
| Trusts | 96 (R-TRS-001–096) | 118 | ~11,600 (State Bar outline I–XII + 3 SUP topics) | 18/18 | V-550–V-594 |

- **Evidence:** every rule gives the FRE and CEC versions. The ~55-row `ca-distinctions.md` covers Truth-in-Evidence (Prop 8), character, impeachment, hearsay, privileges, expert gatekeeping (*Kelly*/*Sargon*/*Sanchez*) and the secondary evidence rule. The FRE 801(d)(1)(A) amendment (effective Dec 1, 2026) is taught as current law with a pre/post split table [VERIFY V-028]. Essay templates follow the item-by-item method.
- **PR:** every rule has a **CA vs. ABA** line. The ~55-row CA/ABA table and a State Bar Act duty table are included. `outline.md` follows the State Bar outline I–VIII, with dedicated confidentiality (I.D) and loyalty (I.E) sections and MPRE notes.
- **Wills and Trusts:** keyed to the Probate Code. Trusts cross-references R-WIL IDs for pour-overs, no-contest clauses, disqualified donees and nonprobate transfers.
- **Cross-subject fixes the builders found:**
  - Community Property now cites Prob. Code **§ 5040** for nonprobate transfers to a former spouse (former § 5600, now the TOD-deed statute); V-324 resolved.
  - The closing-argument PT template now states that **CA rule 3.4(g)** bars personal opinion only on the guilt or innocence of an accused; V-058 resolved (wording tracked as V-450).
  - Trusts governing law: calls vary, so read the call and give the general rule plus the Probate Code section. V-057 resolved; the remaining check is V-550. `essay-method.md` updated.
  - `recent-changes.md` §7: Prob. Code **§ 15408** $100,000 threshold (SB 1127, 2024) [VERIFY V-556].
- **Older amendments the build surfaced:**
  - § 6300 pour-over (2018): the trust instrument may be signed up to 60 days after the will.
  - § 6124: the lost-will presumption covers only a will that cannot be found.
- **Spot-checked (accurate):**
  - Wills: attested-will formalities, harmless error, holographic wills, anti-lapse (incl. class members), omitted-spouse share, DRR.
  - PR: § 6068(e) confidentiality, rule 1.5.1 fee division, rule 1.7, rule 1.8.10, rule 3.10, rule 7.3.
  - Evidence: Prop 8 exceptions, *Castro* moral turpitude, FRE 613(b)/804(b)(3) 2024 amendments, CEC § 1230.
  - Trusts: § 15400 default, *Haggerty*, spendthrift, prudent investor, cy pres, resulting trusts.
- **Coverage gate** passes for all 10 subjects built so far: 448 subject rows, 450 of 616 matrix rows mapped including the 2 PT rows.
- **Matrix note:** `EVD-CBX-II?` has a "?" in its ID (Phase 0 numbering conflict), so it cannot appear in front matter. It is mapped; rename it during Phase 7 QA.

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

## Next: Phase 5 — Wave 2 (expansion to targets) and simulations
- **MCQs:** from 50 to **150 per MBE subject** (+700). Fill uncovered matrix rows first, then weight by NCBE share (Fourth Amendment/Miranda, negligence, hearsay, Real Property categories). Every batch gets a blind answer-key check before commit.
- **Essays:** from 3 to **8 per subject** (≥ 30% crossovers). Weight PR, CP, Contracts, Remedies and Evidence highest, per frequency.
- **PTs:** from 3 to **8**, covering the remaining task types (client letter, demand letter, closing argument, drafting a contract, discovery/other).
- **Simulations:** build **SIM-01–SIM-03** with `scripts/build_simulation.py`, matching the plan dates (Apr 10–11, Jun 19–20, Jul 10–11). Each gets 5 essays + 1 PT + 200 MCQs not used elsewhere.

## Handoff notes for a new session
- **Read `CLAUDE.md` first.** It holds all conventions.
- Run `python scripts/validate.py && python -m pytest -q scripts/tests` before every commit.
- **Do not** re-run `00-exam-intel/research/build_matrix_v1.py`. The matrix is now hand-maintained.
- Web search has a shared budget of about 200 calls per turn. Cap each research agent's searches.
- `config/plan.yml` values marked PROVISIONAL are placeholders until Phase 2.
