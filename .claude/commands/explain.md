---
description: Teach one rule or topic from the repo content (rule, flowchart, worked example), then quiz me on it
argument-hint: "<topic, rule ID, or coverage_id — e.g. 'hearsay within hearsay' or R-EVD-031>"
---
Teach this topic: $ARGUMENTS

Teach **only from repo content**:
- Locate the topic with `grep -ril` across `03-subjects/*/{primer,outline,rule-statements,flowcharts,worked-examples,ca-distinctions,traps}.md` and `00-exam-intel/coverage-matrix.csv`.
- If the repo doesn't cover it yet, say so. Do not improvise law. Offer to add it to the subject's build list, and log a `[VERIFY V-###]` item if there is a factual question.

Structure:
1. **Big picture:** 3–4 plain-English sentences (from `primer.md`).
2. **Rule:** the essay-ready statement, verbatim from `rule-statements.md`, with its ID and authority.
3. **Elements / exceptions / defenses** as a short list.
4. **Splits:** the CA vs. federal/majority/MBE table from `ca-distinctions.md`, with which rule to use where.
5. **Flowchart:** the Mermaid decision tree from `flowcharts.md`. If none exists, draw a small one from the outline and label it "draft".
6. **Worked example:** from `worked-examples.md`.
7. **Traps:** from `traps.md`.
8. Optional **PRC bridge** line, if the subject file has one.

Then **quiz** the user:
- run `python scripts/quiz.py pick --subject <CODE> --n 3 --subtopic <coverage_id> --full` and administer the questions as in `/quiz`, logging each;
- if the bank has none yet, ask 3 short-answer checks and log them as `--kind drill`.
