---
subject: exam-intel
topic: What California graders reward (essays and PT)
coverage_ids: []
tested_on: [essay, PT]
exam_frequency: {level: high, basis: "Applies to every essay and PT answer"}
last_verified: 2026-11-04
status: draft
---

# What California graders reward

This file has three layers. Keep them apart when you use it.

1. **§1–§3, official:** what the State Bar itself says. Short quotes from the exam booklets and the State Bar's pages.
2. **§4, my working rubric:** how I will grade your practice answers in `/essay` and `/pt`. It is derived from §1–§3, but it is **not** a State Bar document.
3. **§5, to be built in Phase 3:** patterns drawn from published selected answers.

## 1. Official essay instructions (printed on every exam)

| Instruction | Source | What it means for you |
|---|---|---|
| "Your answer should demonstrate your ability to analyze the facts in the question, to tell the difference between material facts and immaterial facts, and to discern the points of law and fact upon which the case turns." | [S-076] | **Issue-spotting and fact selection are graded.** Use the facts that decide the issue, and say why they matter. |
| "Your answer should evidence your ability to apply the law to the given facts and to reason in a logical, lawyer-like manner from the premises you adopt to a sound conclusion." | [S-076] (older booklets; presence in 2026 booklets [VERIFY V-021]) | **Rule, then application, then conclusion.** The reasoning chain is what earns points. |
| "Do not merely show that you remember legal principles. Instead, try to demonstrate your proficiency in using and applying them." | [S-076] | Reciting a rule with no facts applied earns little. |
| "If your answer contains only a statement of your conclusions, you will receive little or no credit." | [S-076] | Conclusions without reasoning score close to zero. |
| "...you should not volunteer information or discuss legal doctrines which are not pertinent to the resolution of the issues raised by the call of the question." | [S-077] [S-078] (2024–2026 wording) | **Answer the call.** Off-call doctrine costs you time and earns nothing. |
| "Unless a question expressly asks you to use California law, you should answer according to legal theories and principles of general application." | [S-077] [S-078] | **The default is general (majority/common law) principles.** Use California law when the call asks for it. In Evidence, Civil Procedure and Professional Responsibility the scope also tests California rules (§3). |

## 2. Official Performance Test instructions (2012–2024 booklets; 2026 wording not yet confirmed [VERIFY V-021])

| Instruction | Source |
|---|---|
| "You will have two separate sets of materials with which to work: a File and a Library." | [S-076] |
| "The problem is set in the fictional State of Columbia, one of the United States." | [S-076] |
| "The File contains factual materials about your case. The first document is a memorandum containing the instructions for the tasks you are to complete." | [S-076] |
| "The case reports may be real, modified, or written solely for the purpose of this performance test." | [S-076] |
| "Your response will be graded on its compliance with instructions and on its content, thoroughness, and organization." | [S-076] |

**What this means.**
- The PT is a **closed universe**. Use the Library's law even if you know the "real" rule differs, and cite the Library's authorities by name.
- The task memo controls the format, audience and tone. "Compliance with instructions" is graded first.
- The PT is 90 minutes and counts double [S-010]. Your time plan and task-type templates are in `04-performance-test/`, built in Phase 1–2.

## 3. Official grading facts

| Fact | Source |
|---|---|
| Graders score each answer **40–100 in 5-point steps**. An answer must identify the subject and attempt to apply law to facts to earn at least 40; otherwise it gets **0**. | [S-010] |
| "The quality of handwriting or the accuracy of spelling and grammar are not considered." | [S-010] |
| "Six groups, each consisting of experienced graders and up to four apprentice graders, are selected to grade the essay and PT answers." Each group calibrates on sample answers before grading. | [S-010] |
| Answers are identified by code number only. | [S-010] |
| Answers scoring 1350–1389.99 after the first read are **re-read** by different graders, and the two reads are averaged. | [S-010] [S-011] |
| Published selected answers "are not to be considered 'model' or perfect answers." | [S-079] |
| "Professional responsibility issues may be included in conjunction with any subject tested on the examination." | [S-082] |
| Evidence: "Applicants should be prepared to compare and contrast the differences between the Federal Rules and the California Evidence Code." | [S-083] |
| Civil Procedure: "Applicants should be prepared to answer questions that have issues concerning the Federal Rules of Civil Procedure and the California Code of Civil Procedure." | [S-084] |
| Professional Responsibility tests "the California Rules of Professional Conduct, relevant sections of the California Business and Professions Code, and leading federal and state case law on the subject". Two State Bar documents add the ABA Model Rules [VERIFY V-022]. | [S-082] [S-096] |
| Essays can combine subjects ("crossovers"). | [S-097] |

**What these facts imply.**
- **Graders read fast and compare answers.** Calibration means your answer is scored against the other answers in the pile, not against a perfect answer. An answer that is **organized, hits the main issues and shows its reasoning** beats one that is brilliant on a single issue and silent on others.
- **Headings matter** even though spelling does not. They let a grader find each issue in seconds.
- **A zero is possible** if you do not attempt to apply law to facts, for example when you run out of time. A thin answer under every call is far better than a blank call.

## 4. Repo working rubric (Claude's, for practice grading, not the State Bar's)

`/essay` scores your practice answers on the same 40–100 scale, using five weighted criteria:

| Criterion | Weight | What "full credit" looks like |
|---|---|---|
| **Issues spotted** | 35% | Every major issue in the call (the ones a top answer would head) plus most minor ones. Each major issue missed costs about one band (5 points). |
| **Rule accuracy** | 20% | Exam-ready rule statement with correct elements, a correct CA-vs-general split where relevant, and no misstatements. |
| **Analysis depth** | 30% | Element-by-element application with specific facts quoted or paraphrased, both sides argued where the facts cut both ways, and inferences explained ("because..."). |
| **Organization** | 10% | Headings track the call of the question; IRAC (Issue, Rule, Application, Conclusion) under each heading; logical order (threshold issues first). |
| **Conclusions** | 5% | A clear conclusion for every issue, including "likely" conclusions on close calls, and an answer to every call. |

**Score bands (repo convention)**

| Band | Typical profile |
|---|---|
| 75–85+ | All major issues, accurate rules, strong two-sided analysis, clean structure. |
| 65–70 | **Passing-level target.** All or almost all major issues, mostly accurate rules, real application of facts. |
| 55–60 | One major issue missed, **or** rules stated with thin application. |
| 45–50 | Several issues missed, or mostly conclusions. |
| 40 | Subject identified, minimal attempt to apply law. |

Phase 3 will calibrate these bands against published selected answers, so they stay tied to actual California grading rather than my assumptions.

### For a civil-law-trained writer: the habits that cost points
- **Code-style deduction without facts.** Writing "under § X, the contract is void" is a conclusion. Graders want *rule → these facts → therefore*.
- **One-sided analysis.** PRC judgments state the court's view. Bar graders reward "Plaintiff will argue ... ; however, Defendant will respond ...", then a reasoned conclusion.
- **Skipping "obvious" elements.** Every element of the rule should get at least one sentence of application. Mark a truly undisputed element as satisfied in one short line.
- **Over-long rule recitation.** A one- to three-sentence rule is the target. Spend the words on application.

## 5. Selected-answer patterns (Phase 3)

These patterns come from the Phase 3 indexing of 166 published essays and 42 PTs (Feb 2012 – Jul 2026). They were drawn from search summaries of the State Bar's selected-answers booklets, not full reads [VERIFY V-070]. The State Bar describes selected answers as high-scoring answers by applicants who passed, "not to be considered 'model' or perfect answers" [S-079].

| Pattern | What it means for your answers |
|---|---|
| **Structure follows the call.** Numbered calls become numbered top-level headings. Calls that name parties are answered party by party. Calls that list items (statements, exhibits, conduct) are answered item by item. | Build the outline from the call before reading the facts in detail. |
| **Threshold issues first:** standing before the merits, governing law (UCC vs. common law) before breach, entity liability before individual liability, Fourth Amendment standing before suppression. | Every subject's `issue-checklist.md` (Phase 4) lists its threshold issues in order. |
| **Short rule, then specific facts, then a hedged conclusion** ("likely", "probably") for each issue, not only at the end. | Matches the repo rubric in §4. Never leave an issue without its own conclusion. |
| **Two selected answers can reach opposite conclusions on the same issue** (e.g., Jul 2013 Q1 referral, Feb 2016 Q1 trust revocation, Jul 2018 Q3 conflict, Feb 2025 Q1 suppression) and both were published. | Graders reward issue recognition, a correct rule and reasoned two-sided application more than the "right" outcome. |
| **Passing answers spot secondary issues** beyond the obvious ones (an extra tort between other parties; confidentiality alongside a conflict). | Run the full issue checklist; one sentence on a minor issue can earn credit. |
| **Asset by asset in Community Property.** Each asset is characterized, the presumptions applied, transmutation tested (a writing is required), then reimbursement or apportionment and the remedy. | Use the CP essay template (Phase 4). |
| **Item by item in Evidence.** Each piece of evidence gets its own heading, running relevance, hearsay definition, exclusions, exceptions, then confrontation and other objections. | The call says whether the **CEC or the FRE** governs; it changes between exams. |
| **Actor by actor in PR, then duty by duty**, comparing the **California and ABA** rules point by point where they differ. | Every PR rule in `rule-statements.md` needs a "CA vs. ABA" line. |
| **PT answers follow the task memo's own questions** and any format memo in the File. They apply the Library's factors item by item and respect scope limits ("do not address Miranda"). | `../04-performance-test/method.md` steps 1–4; read the format memo in the File as part of the instructions. |
