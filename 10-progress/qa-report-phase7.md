---
subject: progress
topic: Phase 7 independent QA report
coverage_ids: []
tested_on: [none]
exam_frequency: {level: n/a, basis: "Process record"}
last_verified: 2026-11-05
status: verified
---

# Phase 7 — independent QA report (2026-11-05)

Phase 7 asked one question of every file: **is it accurate?** Reviewers who had not written the content checked it against primary sources found by search, the repo's logged sources and their own knowledge. They fixed what they found and logged what they could not settle. This page records what was checked, what was wrong, what is still open, and what the `status` field now means.

## 1. What was checked

| Wave | Scope | Method |
|---|---|---|
| A1 | Community Property, Wills, Trusts, Business Associations, Remedies, Professional Responsibility, plus exam intel, study plan, foundations, MBE and exam-strategy files | Each subject's open VERIFY items searched (10–25 searches per reviewer); every rule statement read for elements, burdens, exceptions, section numbers, case names, majority/minority and plurality labels, and the MBE vs. CA (or CA vs. ABA) line; derivative files (outline, ca-distinctions, flashcards, key authorities, traps, flowcharts) checked for the same points |
| A2 | Contracts, Civil Procedure, Constitutional Law, Criminal Law and Procedure, Evidence, Real Property, Torts | Same method (10–12 searches each), plus the notes forwarded from the Wave 1 MCQ audits |
| B — MCQs | The 350 Wave 1 MCQs (the 700 Wave 2 items were blind-solved and audited in Phase 5) | Explanation audit of every Wave 1 item; length-cue rebalancing with blind re-solves; every key checked unchanged by script after each edit |
| B — essays and PTs | All 39 Wave 1 essays; PT-001 to PT-003 (the Wave 2 essays and PT-004 to PT-008 were independently reviewed in Phase 5); new crossover E-XO-030 | Independent legal-accuracy review of facts, calls, rules, analysis and rubric; reviewers applied their own HIGH and MED fixes |
| Consistency | Every cross-folder conflict a reviewer found (high-yield tables, recent-changes, essays, other subjects) | Forwarded to the coordinator and fixed in the same commit as the subject merge |

Severity scale used throughout: **HIGH** = wrong law or a wrong conclusion; **MED** = incomplete or overstated; **LOW** = wording or citation form.

## 2. Rule statements: findings by subject

| Subject | HIGH | MED | LOW | VERIFY items resolved | The HIGH items |
|---|---|---|---|---|---|
| Remedies | 1 | 9 | 13 | 10 | R-REM-046 counted the same loss twice |
| Professional Responsibility | 1 | 8 | 7 | 9 | R-PRF-069: CRPC 3.7(a)(3) lets a prosecutor be advocate-witness with the head of office's consent |
| Community Property | 1 | 7 | 11 | 16 | R-CMP-014: *Brace* leaves the survivorship effect of joint-tenancy title at death undisturbed |
| Business Associations | 2 | 12 | 11 | 7 | R-BUS-069 (Corp. Code § 315 reaches officers only); R-BUS-095 (*Wilkes* burden) |
| Trusts | 2 | 17 | 7 | 17 | R-TRS-046 (*Carmack*: § 15307 orders count inside the 25% cap); R-TRS-016 (§ 15401(c): the trust instrument must permit an agent to revoke) |
| Wills and Succession | 2 | 13 | 14 | 15 | R-WIL-017 (§ 78(d), *Lahey*); R-WIL-100 (*Brace*) |
| Contracts | 0 | 9 | 6 | 4 | — |
| Civil Procedure | 0 | 9 | 11 | 8 | — |
| Constitutional Law | 0 | 12 | 27 | 4 | — |
| Criminal Law and Procedure | 0 | 5 | 17 | 3 | — |
| Evidence | 2 | 7 | 13 | 8 | R-EVD-047 (§ 352.2's third factor is "factual detail not otherwise publicly available"); R-EVD-102 (§ 240(a)(6) lists refusal to testify, but only after a contempt finding) |
| Real Property | 0 | 9 | 9 | 3 | — |
| Torts | 1 | 8 | 10 | 4 | R-TRT-009: courts divide on whether consent to mutual combat is effective (R2d § 892C is not the majority rule) |
| **Total** | **12** | **125** | **156** | **108** | |

Exam intel and the other non-subject files resolved 10 more items (§ 4).

**Patterns worth knowing as a student.** Most MED fixes fell into five groups:
1. **Plurality opinions stated as holdings.** About 40 cases are now labelled (*Hein*, *NFIB*'s Commerce Clause holding, *Town of Greece* II-B, *Kirby*, *Baldwin*, *Powell*, *Egelhoff*, *Seibert*'s test, *Burnham*, *Shady Grove*'s test, *Dun & Bradstreet* and others). On an essay, cite them for the result, not as a majority rule.
2. **"Majority" claims that are really trends.** Self-severance of a joint tenancy, mutual-combat consent, and lien-theory uniformity were all overstated.
3. **California points missing from general rules.** Examples: Civ. Code § 1692 damages with rescission; Fam. Code § 6701; § 3423(e); Pen. Code § 1111; *Pruneyard*; § 1223's foundation; *Christian S.*; *B.B. v. County of Los Angeles*.
4. **Wrong section or subsection numbers**, now corrected (Civ. Code §§ 694/695, CCP § 1446(b)(3), Gov. Code § 818, § 911.2 and others).
5. **Currency.** SB 95 (California's 2022 UCC amendments), the 2024 FRE 804(b)(3)(B) wording, FRE 801(d)(1)(A) as amended Dec. 1, 2026, and the October Term 2025 decisions are now dated and sourced.

**Gaps filled:** R-CON-118 (California free speech in shopping centers: *Robins v. Pruneyard*, *Fashion Valley*, *Ralphs*) and R-CRM-121 (Pen. Code § 1111 accomplice corroboration), each with a flashcard and a memorization tier. The rulebook now has **1,434 rules**.

## 3. Question bank

| Item | Result |
|---|---|
| Wave 1 MCQ explanation audit (350 items) | 104 explanation fixes (Real Property 16, Con Law/Crim 33, Evidence/Torts 17, Contracts/Civ Pro 38). **No answer key changed**; a script compared all 1,050 keys after every edit |
| Length cues | The correct answer was the longest option in 31–32 of 50 items in some Wave 1 sets; now 2–13 of 50 per subject. Blind re-solves of the edited items agreed with every key (47/47 and 73/73) |
| Wave 1 essays (39) | 2 HIGH, 40 MED fixed. HIGH: E-XO-006 (wrongly said California's rule 3.7 consent exception excludes prosecutors); E-XO-009 (misdefined "self-created hardship" and skipped the Gov. Code § 65906 comparison; the conclusion changed) |
| PT-001 to PT-003 | PT-003 HIGH (inconsistent family dates) fixed; 13 MED fixed across the three |
| New essay E-XO-030 (Con Law + Remedies) | Written and independently reviewed: 0 HIGH, 7 MED and 7 LOW; all MED fixes applied. The bank now holds 85 essays, 30 of them crossovers (35%) |
| Essay follow-ups from the subject QA | Applied to about 20 essays (accuracy notes, resolved tags, *Pereira*/*Van Camp* presented as an argument, rule 5.4(a)(5)–(6), four omitted-spouse exceptions, and others) |

Simulation-reserved items were reviewed like all others; their booklets were re-rendered after the edits.

## 4. VERIFY queue

| | End of Phase 6 | End of Phase 7 |
|---|---|---|
| Open | 344 | 283 |
| Resolved (with the confirming source) | 5 | 123 |
| Sources logged in `00-exam-intel/sources.md` | 519 | 734 |

Resolving an item meant finding the text by search (marked `confirmed-primary (search)` or `confirmed-secondary (search)`), replacing every inline tag with the confirming `[S-###]`, and moving the row to the Resolved table. Where only part of a claim was confirmed, the row was **narrowed** to the unconfirmed part rather than closed. New items (about 50) record doubts the reviewers found and could not settle within their search budgets.

**Open items by priority:** 12 High, 81 Med, 190 Low. The High items are mostly exam logistics, dates and pending law: V-001, V-009, V-013, V-015, V-016, V-024, V-025, V-034, V-050, V-602, V-604 and V-700.

**What is left, and why.**
- **Direct reads of primary sites (V-001).** This environment blocks direct fetches of leginfo, courts.ca.gov, calbar.ca.gov, ncbex.org, law.cornell.edu and supremecourt.gov, so search-confirmed facts carry `(search)`. They should be re-read directly when access allows.
- **Future events.**
  - The July 2027 deadlines (V-016).
  - *Sanchez v. Rojas*, which may overrule *Elden* (V-604).
  - Whether survival pain-and-suffering damages are restored (V-602).
  - October Term 2026 decisions.
  - These are on the June 2027 re-check list in `00-exam-intel/recent-changes.md` §10.
- **Your action.** Cardozo's transcript timing (V-015).
- **Low-priority citations given from model knowledge.** These are mostly California Court of Appeal reporter cites and Restatement section numbers. They are tagged where they appear, and no essay or MCQ answer turns on a tagged point.

## 5. What `status` means now

| Status | Meaning |
|---|---|
| `verified` | Independently reviewed for accuracy (Phase 5 or 7), and the file (or MCQ item) contains no tag for an open VERIFY item |
| `reviewed` | Independently reviewed, but at least one open `[VERIFY V-###]` tag remains. The tagged point is the one to double-check; the rest of the file was reviewed |
| `draft` | Not in the independent-review scope: performance-test method and task-type files, the 166 past-exam analyses, generated weekly plans and progress reports |

`verified` is not a guarantee. It means a reviewer who did not write the content checked it, and nothing in it is still flagged. Facts confirmed by search still need the direct re-read in V-001.

| Area | `verified` | `reviewed` |
|---|---|---|
| Subject files (`03-subjects/`, 176 files) | 81 | 95 |
| Essays and PTs (93 files) | 77 | 16 |
| MCQ items | 1,050 | 0 |
| High-yield (9 files) | 2 | 7 |
| Exam intel, study plan, foundations, MBE, past-exam summaries, exam strategy (27 files) | 10 | 17 |

Most `reviewed` subject files carry one or two Low-priority tags on a citation, not on the rule itself. To see every open tag in a file, search it for `[VERIFY`.

## 6. Residual risks and how the repo handles them

- **A rule you memorize could still be wrong.** Each rule cites its authority, so a doubt can be checked in minutes. Log any error you find in `10-progress/error-log.md` and it is fixed in Phase 8.
- **Law can change before July 2027.** `/update-exam-intel` re-checks monthly; the June 2027 sweep is scheduled.
- **The California written-section outlines were captured from search snippets.** Ten outline sections stand in as SUP rows (V-024, V-025). Re-confirm them from the State Bar PDFs when access allows.
