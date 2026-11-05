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
| 5 — Question bank | ✅ **Done (awaiting review)**: 1,050 MCQs, 84 essays, 8 PTs, 3 simulations | Every item independently reviewed |
| 6 — High-yield and memorization | ✅ **Done (awaiting review)** | 08-high-yield (8 files + README), consistency sweep, Anki decks |
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

## Phase 6 deliverables (high-yield synthesis and memorization)

**`08-high-yield/`** (about 40,000 words, all distilled from the corrected rulebooks, with rule IDs):

| File | What it is |
|---|---|
| `top-rules-mbe-subjects.md` | 15–16 must-know rules per MBE subject, exam-ready, with MBE traps and CA notes |
| `top-rules-california-subjects.md` | 15–16 per essay-only subject (PR with CA vs ABA; CP presumptions/tracing; Probate Code sections) |
| `mbe-vs-california-master-table.md` | Every MBE-vs-California split, per subject, plus the top 25 flips most likely to cost points and when an essay calls for California law |
| `crossover-guide.md` | All tested crossover pairs: triggers, answer skeleton, key rules, traps, links to bank essays (simulation essays marked) |
| `most-tested-issues.md` | Essay issues ranked by how often they were tagged in past essays; MBE categories by NCBE share; a "10 hours left" list |
| `memorization-master.md` | Tier counts and must-know IDs for all 13 subjects; spaced-repetition and `/drill` protocol |
| `mnemonics.md` | 50 original memory aids, each tied to its rule ID |
| `final-2-weeks-review.md` | Day-by-day plan Jul 12–25, matched to plan weeks W28–W29, plus night-before and between-days pages |

**Consistency sweep.**
- The Phase 5 reviews corrected 56 rules, but the subjects' other files still carried the old wording.
- Three agents propagated the corrections, fixing **141 stale statements** across outlines, attack outlines, ca-distinctions, traps, worked examples, flashcards and bank items.
- One example: a flashcard still taught the old strict-liability defense rule.
- No answer key depended on an old rule; all 1,050 keys were verified unchanged.
- Seven remaining rulebook lines (R-REM-085, R-CIV-042 example, R-REM-069, R-PRP-070, R-PRF-026, R-BUS-085/086 summaries) were aligned.

**Independent accuracy review of `08-high-yield/`.** It found 3 HIGH problems, all fixed: one row of the top-25 flips table stated title theory as the majority (lien theory is the majority), outdated Anki instructions, and a mnemonic contradicting R-CIV-096. It also applied 9 MED fixes. The rulebook itself checked out. Memorization cycle 3 was moved to W28, after SIM-03.

**Anki.**
- `build_anki.py` now tags each rule card with its memorization tier.
- Decks (written to the gitignored `exports/`; rebuild with the commands in `memorization-master.md`):
  - full deck: 3,238 cards;
  - must-know deck (must-know flashcards + must-know rule cards): 1,651 cards.

**Plan fixes:**
- Rest days now get 0 hours.
- W29 is a 24-hour taper (3 h weeknights, 9 h Saturday, Sunday Jul 25 off); the plan totals 1,194 h.
- The exam-day logistics file now matches SIM-03 on Jul 10–11.
- 27 tests.

**Gaps noted for Phase 7:**
- No rule statement yet for Pen. Code § 1111 (accomplice corroboration) or the *Pruneyard* mall-speech rule; both appear only in `ca-distinctions.md`.
- The bank has no Con Law + Remedies crossover essay.
- `frequency_analysis.py` lists only the top 15 crossover pairs.

## Phase 5 — Wave 2 deliverables (question bank complete)

| Item | Count | Target | Detail |
|---|---|---|---|
| MBE-style MCQs | **1,050** (150 × 7) | ≥ 150 per MBE subject | Category mix follows NCBE weights (e.g., Torts negligence 75/150; Crim constitutional protections 75/150, with Fourth Amendment 30 and Fifth 20; Evidence I 37 · II 50 · III 13 · IV 12 · V 38; Real Property 30 per category); every MBE matrix row tested |
| Essays | **84** (55 single + 29 crossovers = 35%) | ≥ 8 per subject, ≥ 30% crossovers | Appearances per subject: PR 12 · Remedies 10 · CP, Contracts, Evidence 9 · all others 8 |
| Performance Tests | **8** | ≥ 8 | Objective memo, persuasive brief, drafting (trust; SaaS contract), client letter, demand letter, closing argument, discovery plan |
| Simulations | **3** | ≥ 3 | SIM-01 (Apr 10–11), SIM-02 (Jun 19–20, objective-memo PT), SIM-03 (Jul 10–11, persuasive-brief PT); each 5 essays + 1 PT + 200 MCQs (28–29 per subject) |

**Quality process (the user asked for quality over speed and quantity):**
1. **MCQs.**
   - The writer re-solves every item cold.
   - An **independent reviewer answers every item blind**, writing its answers before seeing the key.
   - The reviewer then audits every explanation line by line.
   - Result: blind solves agreed with **all 700 Wave 2 keys** (and all 350 in Wave 1). About 95 explanation, stem or metadata fixes were applied. No key needed changing; key changes were checked mechanically against the previous commit.
2. **Essays.** Every Wave 2 essay passed an independent legal-accuracy review: governing law, rule accuracy, fact fidelity, two-sided analysis and rubric.
   - **9 HIGH findings fixed**, including:
     - a takings claim against a State sent to federal court (*Will*);
     - the ABA fee-basis duty attributed to California;
     - *Epstein* credits;
     - trustee-transaction protection;
     - the ABA "related persons" gift rule.
   - Many MED and LOW fixes.
3. **PTs.** Independent review for closed-universe fidelity, task-memo compliance and internal consistency. It found 8 HIGH problems in PT-004 to PT-008, all fixed: deadline arithmetic, facts contradicted by the File, a value comparison, an enforceability point, a missing caption, and a request that contradicted its memo.
4. **Rulebook corrections found during the process (about 60).** The most important:
   - Torts: the strict-liability defense rule (comparative fault reduces, not bars) and the trespasser carve-out.
   - Real Property: foreclosure-price inadequacy; mortgage-transfer and prepayment defaults; assignee privity.
   - Evidence: FRE 801(d)(2) ("must consider").
   - Con Law: *Noel Canning*; several plurality labels; *Knick*/*Will*.
   - Contracts: waiver retraction and the § 20 misunderstanding rule.
   - PR: ABA 4.2 comment [7]; rule 1.8.1.
   - BA: MBCA vote; California appraisal exclusivity.
   - Crim: *DeFillippo*, *Thornton*, *Patane*/*Muniz* pluralities.
   - Civ Pro: *Lazar*, Rule 11(c)(5)(A).
   - New VERIFY items were logged where wording rests on secondary sources: V-418, V-674–V-676, V-730–V-731, V-830–V-831.

**Tooling:**
- The validator checks issue-level IDs in essays.
- `quiz.py` holds back simulation items until the simulation is sat (`quiz.py reserved`; `/essay` and `/pt` respect it).
- `build_simulation.py` builds exam-shaped essay sets (one PR essay, at least one crossover, at least one California-law subject, no repeated subject) and has a `render` command.
- 26 tests.

**Resilience:** two container restarts interrupted agents mid-task. All agents were resumed from their transcripts and no work was lost. Pre-review snapshots were committed so work could not be lost; review fixes followed in separate commits.

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

- **Evidence:** every rule gives the FRE and CEC versions. The ~55-row `ca-distinctions.md` covers Truth-in-Evidence (Prop 8), character, impeachment, hearsay, privileges, expert gatekeeping (*Kelly*/*Sargon*/*Sanchez*) and the secondary evidence rule. The FRE 801(d)(1)(A) amendment (effective Dec 1, 2026) is taught as current law with a pre/post split table [S-101]. Essay templates follow the item-by-item method.
- **PR:** every rule has a **CA vs. ABA** line. The ~55-row CA/ABA table and a State Bar Act duty table are included. `outline.md` follows the State Bar outline I–VIII, with dedicated confidentiality (I.D) and loyalty (I.E) sections and MPRE notes.
- **Wills and Trusts:** keyed to the Probate Code. Trusts cross-references R-WIL IDs for pour-overs, no-contest clauses, disqualified donees and nonprobate transfers.
- **Cross-subject fixes the builders found:**
  - Community Property now cites Prob. Code **§ 5040** for nonprobate transfers to a former spouse (former § 5600, now the TOD-deed statute); V-324 resolved.
  - The closing-argument PT template now states that **CA rule 3.4(g)** bars personal opinion only on the guilt or innocence of an accused; V-058 resolved (wording tracked as V-450).
  - Trusts governing law: calls vary, so read the call and give the general rule plus the Probate Code section. V-057 resolved; the remaining check is V-550. `essay-method.md` updated.
  - `recent-changes.md` §7: Prob. Code **§ 15408** $100,000 threshold (SB 1127, 2024) [S-1103].
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

## Next: Phase 7 — independent QA
- **Subject-file QA:** independent reviewer subagents audit every subject's 15 files for legal accuracy, internal consistency, coverage and citation integrity, then fix the findings. Subjects whose rule statements have not yet had a question-level audit (CP, Wills, Trusts, BA, Remedies, PR) get the deepest review.
- **VERIFY queue:** close what can be confirmed by search (`confirmed-primary (search)`); re-scope the rest; list the items that need a direct read of leginfo, courts.ca.gov or calbar.ca.gov (V-001).
- **Fill the gaps noted above** (§ 1111, *Pruneyard*, a Con Law + Remedies essay, the crossover table).
- **Mark files `verified`** only after QA. Rename `EVD-CBX-II?`. Produce the QA report.

## Handoff notes for a new session
- **Read `CLAUDE.md` first.** It holds all conventions.
- Run `python scripts/validate.py && python -m pytest -q scripts/tests` before every commit.
- **Do not** re-run `00-exam-intel/research/build_matrix_v1.py`. The matrix is now hand-maintained.
- Web search has a shared budget of about 200 calls per turn. Cap each research agent's searches.
- `config/plan.yml` values marked PROVISIONAL are placeholders until Phase 2.
