---
subject: mbe
topic: MBE subject and category weighting, NCBE assumptions, study-time allocation
coverage_ids: []
tested_on: [MBE]
exam_frequency: {level: high, basis: "Applies to every MBE question"}
last_verified: 2026-11-05
status: reviewed
---

# MBE subject weighting

NCBE publishes how its scored questions are spread across subjects, and, for each subject, roughly how they are spread across the outline's categories. This file turns those statements into approximate question counts, then into study-time decisions.

**Sources:**
- The distribution notes in NCBE's MBE Subject Matter Outline [S-040], as captured in the coverage matrix's `weight_note` column and in `00-exam-intel/research/phase0-ncbe-mbe-outline.csv`.
- Subject counts from NCBE's MBE pages [S-006] [S-007].

All question counts are **approximations derived from NCBE's fractions**, not NCBE figures.

## 1. Subject level

| Fact | Source |
|---|---|
| 200 questions = 175 scored + 25 unscored pretest | [S-006] [S-007] |
| **25 scored questions in each of 7 subjects**: Civil Procedure, Constitutional Law, Contracts, Criminal Law and Procedure, Evidence, Real Property, Torts | [S-007] |
| How the 25 pretest questions are spread across subjects | Not stated in the sources logged so far. Do not assume an even spread. |

**Every subject is worth the same on the MBE.** No subject can be "skipped" in favour of a strong one.

## 2. Category distributions (NCBE's notes)

The quoted text is NCBE's distribution note as captured in Phase 0 (via search) [S-040]. "≈ Scored Qs" = NCBE fraction × 25, rounded. NCBE does **not** split a group of categories further, so this table does not either.

### Civil Procedure (CIV)
> "Approximately two-thirds of the Civil Procedure questions on the MBE will be based on categories I, III, and V, and approximately one-third will be based on the remaining categories—II, IV, VI, and VII." [S-040]

| Group | Categories | NCBE share | ≈ Scored Qs |
|---|---|---|---|
| A | I Jurisdiction and venue · III Pretrial procedures · V Motions | ~2/3 | **~17** |
| B | II Law applied by federal courts · IV Jury trials · VI Verdicts and judgments · VII Appealability and review | ~1/3 | ~8 |

### Constitutional Law (CON)
> "Approximately half of the Constitutional Law questions on the MBE will be based on category IV, and approximately half will be based on the remaining categories—I, II, and III." [S-040]

| Group | Categories | NCBE share | ≈ Scored Qs |
|---|---|---|---|
| A | IV Individual rights | ~1/2 | **~12–13** |
| B | I Nature of judicial review · II Separation of powers · III Relation of nation and states | ~1/2 | ~12–13 |

### Contracts (CTR)
> "Approximately half of the Contracts questions on the MBE will be based on categories I and IV, and approximately half will be based on the remaining categories—II, III, V, and VI." [S-040]
>
> "Approximately one-fourth of the Contracts questions on the MBE will be based on the Official Text of Articles 1 and 2 of the Uniform Commercial Code." [S-040]

| Group | Categories | NCBE share | ≈ Scored Qs |
|---|---|---|---|
| A | I Formation · IV Performance, breach, and discharge | ~1/2 | **~12–13** |
| B | II Defenses to enforceability · III Contract content and meaning · V Remedies · VI Third-party rights | ~1/2 | ~12–13 |
| Cross-cutting | UCC Articles 1 and 2 (sale of goods), in any category | ~1/4 | **~6** |

### Criminal Law and Procedure (CRM)
> "Approximately half of the Criminal Law and Procedure questions on the MBE will be based on category V, and approximately half will be based on the remaining categories—I, II, III, and IV." [S-040]

| Group | Categories | NCBE share | ≈ Scored Qs |
|---|---|---|---|
| A | V Constitutional protection of accused persons | ~1/2 | **~12–13** |
| B | I Homicide · II Other crimes · III Inchoate crimes; parties · IV General principles | ~1/2 | ~12–13 |

### Evidence (EVD)
> "Approximately one-quarter of the Evidence questions on the MBE will be based on category I, one-third on category II, one-quarter on category V, and the remainder on categories III and IV." [S-040] (Phase 0 search quote. The Phase 7 reviewer recalled a different split, about one-third each for I, V and II–IV together, possibly from an older outline; re-read this note on the PDF before relying on the Evidence II weighting [VERIFY V-960].)

| Category | NCBE share | ≈ Scored Qs |
|---|---|---|
| I Presentation of evidence | ~1/4 | ~6 |
| II Relevancy and reasons for excluding relevant evidence | ~1/3 | **~8** |
| V Hearsay and circumstances of its admissibility | ~1/4 | ~6 |
| III Privileges and other policy exclusions + IV Writings, recordings, and photographs | remainder (~1/6) | ~4 |

### Real Property (PRP)
> "Approximately one-fifth of the Real Property questions on the MBE will be based on each of the categories I through V." [S-040]

| Category | NCBE share | ≈ Scored Qs |
|---|---|---|
| I Ownership of real property | ~1/5 | ~5 |
| II Rights in real property | ~1/5 | ~5 |
| III Real estate contracts | ~1/5 | ~5 |
| IV Mortgages/security devices | ~1/5 | ~5 |
| V Titles | ~1/5 | ~5 |

### Torts (TRT)
> "Approximately half of the Torts questions on the MBE will be based on category II, and approximately half will be based on the remaining categories—I, III, and IV." [S-040]

| Group | Categories | NCBE share | ≈ Scored Qs |
|---|---|---|---|
| A | II Negligence | ~1/2 | **~12–13** |
| B | I Intentional torts · III Strict liability and products liability · IV Other torts | ~1/2 | ~12–13 |

## 3. The biggest blocks of scored questions

Sorted by approximate scored questions. Each line is a single category, or a group NCBE treats as one block.

| Rank | Block | ≈ Scored Qs | Note |
|---|---|---|---|
| 1 | Civ Pro I + III + V (jurisdiction/venue, pretrial, motions) | ~17 | You have no Civ Pro coursework. This block is the priority. |
| 2 | Torts II Negligence | ~12–13 | LLM Torts done. Keep it sharp. |
| 2 | Con Law IV Individual rights | ~12–13 | No coursework |
| 2 | Crim V Constitutional protections (4th, 5th, 6th Amendments) | ~12–13 | No coursework |
| 2 | Contracts I + IV (formation; performance, breach, discharge) | ~12–13 | No coursework |
| 6 | Evidence II Relevance and its exclusions | ~8 | LLM Evidence in Fall 2026 |
| 7 | Contracts: UCC Articles 1–2 (cross-cutting) | ~6 | Overlaps rank 2 |
| 7 | Evidence I Presentation; Evidence V Hearsay | ~6 each | |
| 9 | Each Real Property category, incl. **IV Mortgages** | ~5 each | Mortgages is a full fifth. Do not skip it. |

## 4. NCBE's subject-specific assumptions

These are the defaults the MBE tells you to assume. They override your instincts and any California rule.

| Subject | NCBE assumption | Status | Source |
|---|---|---|---|
| Civil Procedure | Assume the Federal Rules of Civil Procedure **as currently in effect**, and the sections of Title 28 of the U.S. Code on trial and appellate jurisdiction, venue and transfer. | confirmed (search) | [S-040] |
| Constitutional Law | "The terms 'Constitution,' 'constitutional,' and 'unconstitutional' refer to the **federal** Constitution unless indicated otherwise." | confirmed (search) | [S-040] |
| Contracts | Assume the **Official Text of UCC Articles 1 and 2** has been adopted and is in effect; about 1/4 of Contracts questions are based on it. | confirmed (search) | [S-040] |
| Evidence | Answer every Evidence question under the **Federal Rules of Evidence, as currently in effect**. | confirmed (search) | [S-040] |
| Torts | Assume **survival actions and wrongful-death claims are available**. **Joint and several liability** and **pure comparative fault** apply unless the question says otherwise. | confirmed (search) | [S-040] |
| Criminal Law and Procedure; Real Property | No subject-wide assumption note was captured in Phase 0. Do not assume there is none. | [VERIFY V-054] | [S-040] |

**What "as currently in effect" means for July 2027.**
- Federal rule amendments that take effect before the exam can be tested. The pending ones are tracked in [recent-changes.md](../00-exam-intel/recent-changes.md), for example the FRE 801(d)(1)(A) amendment (V-028).
- Whether NCBE applies any lag before testing a new rule is open item V-027.
- **On the MBE, never apply a California rule** (Evidence Code, CCP, Civil Code). California rules belong on essays when the call asks for them (see [essay-method.md](../09-exam-strategy/essay-method.md) §6).

**Which outline applies.** The distributions above come from the January 2023 outline PDF [S-040], which was still the MBE outline NCBE served in November 2026 searches. Two points are open [VERIFY V-054]:
- whether NCBE confirms it for July 2027 (the last MBE-only cycles end in February 2028);
- whether the distribution notes describe scored questions only.

## 5. What this means for your study time

### Rule 1: weight time by scored questions, then adjust for your gaps
- Each MBE subject is about **1/7 of the MBE** (25 of 175 scored) [S-007], and the MBE is **half** of the total score [S-011]. Each subject is therefore about 7% of your total score through the MBE alone, before counting essays.
- **Your four no-coursework subjects (Contracts, Civil Procedure, Constitutional Law, Criminal Law and Procedure) carry 100 of the 175 scored MBE questions (57%).** They are also essay subjects. This is why the study plan front-loads them.

### Rule 2: inside each subject, split time roughly by category share
Example: 10 hours of Evidence MBE practice ≈ 2.5 h presentation (I), 3.3 h relevance (II), 2.5 h hearsay (V), and 1.7 h privileges plus writings (III + IV).

| Subject | Where the first half of your practice should go |
|---|---|
| Civil Procedure | I Jurisdiction and venue, III Pretrial, V Motions (~2/3) |
| Constitutional Law | IV Individual rights (~1/2): equal protection, due process, First Amendment |
| Contracts | I Formation and IV Performance/breach (~1/2), with UCC Article 2 threaded through (~1/4) |
| Criminal Law and Procedure | V Constitutional protections (~1/2) |
| Evidence | II Relevance (~1/3), then I Presentation and V Hearsay (~1/4 each) |
| Real Property | Even across all five categories, including Mortgages |
| Torts | II Negligence (~1/2) |

### Rule 3: let your error data override the averages
- After about 4–6 weeks of practice, `/weak-spots` and `python scripts/quiz.py stats` show which categories you actually miss.
- A category worth about 5 questions where you score 40% is worth more study time than a category worth about 12 questions where you already score 80%.

### Rule 4: mind the essay side
- The same subjects appear on the written section, where the State Bar's scope and California law apply.
- Phase 3 (`06-past-exams/frequency-analysis.md`) added essay frequency: among the MBE subjects, Contracts, Criminal Law and Evidence each appeared on about half of the 31 exams, and Civil Procedure, Constitutional Law, Real Property and Torts on about 40%. Final allocations combine both.
- MBE weighting alone should not decide your time for Community Property, Remedies, Wills, Trusts, Business Associations or Professional Responsibility, which are essay-only.
