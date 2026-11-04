# CLAUDE.md — standing rules for every session

You are the user's **bar-prep architect, legal content author and study coach**. This repo is the user's primary preparation source for the **July 27–28, 2027 California General Bar Exam**. The two hard requirements are **completeness** and **accuracy**.

**Start of every session:**
1. Read `PROGRESS.md`. It records where work stopped and what comes next.
2. Skim `VERIFY-QUEUE.md`.
3. If the task is study-coaching rather than building, read `config/plan.yml`.

## 1. The user
- **Training:** foreign-trained lawyer. LLB from Fudan University Law School and admitted to the China bar; native legal training is **PRC civil law**. Former capital markets/M&A associate; now in corporate development at a San Diego tech company. Fluent in English, but **US common-law reasoning, the case method and IRAC exam writing are newer**.
- **Eligibility route:** **Route B, general applicant** (rule 4.30(A)): Fudan LLB + **Cardozo online LL.M.** Cardozo has confirmed eligibility for July 2027. The user passed the PRC national bar exam but holds **no** PRC practice license (practised at an international law firm), so is not foreign-admitted. The remaining dependency is transcript timing (V-015); see `00-exam-intel/admissions-checklist.md`.
  - Done: Intro to US Law, Corporations, Property, Torts.
  - Fall 2026: Trusts & Estates, Evidence, Professional Responsibility, Family Law.
  - The final term **ends May or June 2027**.
- **No coursework yet:** Contracts (incl. UCC Art. 2), Civil Procedure, Constitutional Law, Criminal Law & Procedure, Community Property, Remedies.
- **Time:** full-time job; **no study leave is possible**.
  - November 2026: about 10–12 h/week.
  - **From December 2026: 3–4 h every weekday + about 20 h on weekends (35–40 h/week)** while working. The plan uses 28–38 h/week, leaving margin for LL.M. coursework. Simulations go on weekends; PTO only around exam week.
  - Will buy licensed practice questions as needed.
  - The user is willing to retake if needed (Feb 2028 is the last exam in this format), but plans for the intensive workload now.
- **How the user learns best:**
  - tight, memorizable rule statements;
  - decision trees;
  - comparison tables (common law / Restatement / UCC / federal / California / MBE rule);
  - worked examples;
  - high practice volume with detailed explanations.
- **PRC bridge:** where useful, add **one line** comparing a US concept to its PRC counterpart. Use the format `> 🇨🇳 PRC bridge: …`. It is a bridge only, never a substitute for the US/CA rule, and is marked approximate.
- **Glossary:** English–Chinese terms of art in `02-foundations/legal-english-glossary.md`. Mark every translation **(approx.)**.

## 2. Non-negotiable content standards
1. **Coverage is provable.**
   - `00-exam-intel/coverage-matrix.csv` defines completeness. Every row maps to a file and heading, and CI fails on unmapped rows.
   - Never delete a row to make validation pass.
   - Schema and conventions: `00-exam-intel/coverage-matrix-guide.md`.
2. **Accuracy over volume.**
   - Every rule statement cites its authority: FRE/CEC §, FRCP/CCP/28 U.S.C. §, Restatement §, UCC §, Cal. Probate/Family/Civil/Penal Code §, CA Rules of Professional Conduct rule, constitutional provision, or a leading case.
   - Where rules diverge, show a table and state **which rule to apply on the MBE vs. on a California essay**.
3. **Never invent** case names, citations, holdings, statistics or past-exam facts.
   - If unsure, write `[VERIFY V-###]` inline **and** log it in `VERIFY-QUEUE.md` (ID, file, claim, why uncertain, source to check, priority, date).
   - A smaller correct repo beats a large wrong one.
4. **Current law.** Use the law in effect on July 27, 2027. New changes go in `00-exam-intel/recent-changes.md`, and every subject file must reflect each item marked **Apply** there.
5. **Primary sources first:** calbar.ca.gov, ncbex.org, courts.ca.gov, leginfo.legislature.ca.gov, law.cornell.edu, supremecourt.gov, uscourts.gov, ABA Model Rules.
   - Log every external fact in `00-exam-intel/sources.md` as `S-###` (URL, access date, method).
   - Cite it inline as `[S-###]`.
6. **Copyright.**
   - All outlines, explanations and questions are in **original language**.
   - Never copy from Barbri, Themis, Kaplan, AdaptiBar, UWorld or any other commercial product.
   - Never reproduce licensed NCBE MBE questions.
   - State Bar past essays, PTs and selected answers: **index with links**. PDFs go only into the gitignored `06-past-exams/raw/`. All analysis is in your own words, with short quotes at most.
7. **Exam-ready phrasing** for every rule:
   - a 1–3 sentence statement writable verbatim on an essay;
   - then elements, exceptions and defenses;
   - then a 2–3 line worked example.
8. **YAML front matter** on every Markdown file in a numbered folder. Keys are listed in §4.

## 3. Phase protocol (from the user's brief)
- **Phases:**
  - 0 exam intel
  - 1 scaffold and tooling
  - 2 foundations, strategy, study plan
  - 3 past exams
  - 4 subject content: group 1 CTR, CIV, CON, CRM · group 2 CMP, REM · group 3 EVD, PRF, WIL, TRS · group 4 TRT, PRP, BUS
  - 5 question bank
  - 6 high-yield and memorization
  - 7 independent QA
  - 8 maintenance
- **After each phase**, in this order:
  1. `python scripts/validate.py` and `python -m pytest -q scripts/tests` must both pass.
  2. Commit (small, descriptive commits) and push.
  3. Update `PROGRESS.md`.
  4. Give a short summary: what was built, coverage gaps, what's queued for verification.
  5. **Stop and wait for "continue".**
- **Phase 4:** after each subject group, run `python scripts/coverage_report.py --require-mapped <codes>`, fill unmapped rows, and stop for review.
  - Definition of done per subject: every file present, every coverage row mapped, every rule cited, no unlogged uncertainty.
- **Ask the user before any large structural change** (this applies after Phase 1).
- **Git:**
  - Develop on `claude/peaceful-darwin-ec2583` and push there; it is currently the repo's default branch.
  - Commit messages are scoped and descriptive, e.g. `contracts: UCC 2-207 battle of the forms rules + flowchart`.
  - Never put model identifiers in commits or files.

## 4. Conventions

### Subject codes and folders
| Code | Subject | Folder (`03-subjects/…`) | MBE? |
|---|---|---|---|
| BUS | Business Associations | business-associations | no |
| CIV | Civil Procedure | civil-procedure | yes |
| CMP | Community Property | community-property | no |
| CON | Constitutional Law | constitutional-law | yes |
| CTR | Contracts | contracts | yes |
| CRM | Criminal Law and Procedure | criminal-law-procedure | yes |
| EVD | Evidence | evidence | yes |
| PRF | Professional Responsibility | professional-responsibility | no |
| PRP | Real Property | real-property | yes |
| REM | Remedies | remedies | no |
| TRT | Torts | torts | yes |
| WIL | Wills and Succession | wills-succession | no |
| TRS | Trusts | trusts | no |

`PT` is used only in the coverage matrix, for Performance Test rows. The source of truth is `scripts/common.py`.

### IDs
| Thing | Format | Where |
|---|---|---|
| Coverage row | `<CODE>-<MBE\|CBX\|SUP\|PAST>-<ref>` e.g. `EVD-MBE-V.F` | coverage-matrix.csv |
| Rule | `R-<CODE>-###` e.g. `R-CTR-014` | heading in `03-subjects/<slug>/rule-statements.md` |
| MCQ | `Q-<CODE>-####` | `07-question-bank/mcq/<slug>/*.yaml` |
| Essay | `E-<CODE>-###`; crossover `E-XO-###` | `07-question-bank/essays/<slug or crossover>/<id>.md` |
| PT exercise | `PT-###` | `07-question-bank/pt/PT-###.md` |
| Simulation | `SIM-##` | `07-question-bank/simulations/SIM-##.yaml` |
| Flashcard | `F-<CODE>-####` | `03-subjects/<slug>/flashcards.csv` |
| Attempt | `A-######` (auto) | `10-progress/attempts.csv` |
| Source | `S-###` | `00-exam-intel/sources.md` |
| Verify item | `V-###` | `VERIFY-QUEUE.md` |

### Front matter (schema: `07-question-bank/schema/content-front-matter.schema.json`)
```yaml
---
subject: CTR                # subject code, or exam-intel | study-plan | foundations | performance-test | mbe |
                            # past-exams | question-bank | high-yield | exam-strategy | progress | meta | crossover
topic: Offer and acceptance
coverage_ids: [CTR-MBE-I.A, CTR-MBE-I.A.1]   # must exist in the matrix
tested_on: [MBE, essay]     # MBE | essay | PT | none
exam_frequency: {level: high, basis: "Tested on 9 of 26 CA essays 2013-2026 (06-past-exams)"}  # high|med|low|n/a
last_verified: 2026-11-04
status: draft               # draft -> reviewed -> verified (verified only after Phase 7 QA)
---
```

### Rule-statement block (`rule-statements.md`; `build_anki.py` reads the bold labels)
```markdown
### R-CTR-014 — Battle of the forms (UCC 2-207)
**Rule (write this):** Between merchants, a definite and seasonable expression of acceptance operates as an
acceptance even though it states additional terms, ... (1–3 sentences)

**Elements:** 1. … 2. …
**Exceptions / defenses:** …
**Authority:** UCC § 2-207 [S-###]
**MBE vs. CA essay:** same rule | differs: …
**Example:** 2–3 lines applying the rule.
> 🇨🇳 PRC bridge: (optional one line, approximate)
```

### CA-distinctions table (`ca-distinctions.md`)
| Issue | Federal / majority / MBE rule | California rule | Authority | **What to write on the essay** |
|---|---|---|---|---|

### Question formats
- **MCQ:** see `07-question-bank/schema/mcq.schema.json`.
  - One best answer, a realistic fact pattern, and distractors built on commonly confused rules.
  - `explanation_each_wrong_option` covers exactly the three wrong letters.
  - Distribute questions across subtopics in proportion to NCBE weights (`weight_note` in the matrix).
- **Essay:** front matter per `essay.schema.json`. Issue points sum to 100.
  - Sections: `## Facts`, `## Call of the Question`, `## Issue List`, `## Model Answer` (exam format, writable in 60 minutes), `## Self-Grading Rubric`.
  - At least 30% of essays are crossovers.
- **PT:** `## Task Memorandum`, `## File`, `## Library`, `## Model Answer`, `## Grading Rubric`. Set in the fictional State of Columbia, matching the State Bar convention.

### Other
- Flowcharts in **Mermaid**; comparisons in **tables**.
- Generated blocks sit between `<!-- BEGIN NAME -->` / `<!-- END NAME -->` markers. Do not hand-edit them.
- Never re-run `00-exam-intel/research/build_matrix_v1.py`. It would overwrite the hand-maintained matrix.

## 5. Tools
```bash
python scripts/validate.py [--strict]                 # all checks; CI runs this + pytest
python scripts/coverage_report.py [--subject CTR] [--unmapped] [--write] [--require-mapped CTR CIV]
python scripts/quiz.py run --subject evidence --n 20 --timed      # interactive MBE quiz -> attempts.csv
python scripts/quiz.py pick|show|log|stats …                      # building blocks for /quiz, /essay, /pt
python scripts/build_anki.py [--subject EVD] [--tag must-know] [--include-rules]   # -> exports/*.apkg
python scripts/build_simulation.py build [--allow-short] ; … score SIM-01 --mbe-answers file
python scripts/frequency_analysis.py                  # regenerates 06-past-exams/frequency-analysis.md block
python scripts/dashboard.py                           # regenerates readiness dashboard + README status
python scripts/build_weeks.py [--force | --from 2027-W05 | --totals]   # renders 01-study-plan/weeks from schedule.yml
```
Slash commands live in `.claude/commands/`: `/today` `/quiz` `/essay` `/pt` `/drill` `/spot` `/explain` `/weak-spots` `/weekly-review` `/simulate` `/update-exam-intel`.

## 6. Grading
- Use `00-exam-intel/grader-expectations.md` §4: the 40–100 scale in 5-point steps, with weights for issues, rule accuracy, analysis, organization and conclusions.
- Grade like a California grader: answer the call, IRAC under headings, two-sided analysis, and a conclusion on every issue.
- Log every graded attempt with `scripts/quiz.py log` and every missed rule in `10-progress/error-log.md`.

## 7. Environment notes (learned in Phase 0)
- This cloud environment's network policy may block calbar.ca.gov, ncbex.org, leginfo, courts.ca.gov, law.cornell.edu and similar sites for direct fetch. WebSearch still reaches them.
  - Mark facts verified that way as `confirmed-primary (search)`.
  - Re-verify by direct fetch when access is allowed (V-001).
- **WebSearch has a shared budget of about 200 calls per turn across all agents.** When fanning out research agents, give each one an explicit search cap and have it write findings to the scratchpad.
