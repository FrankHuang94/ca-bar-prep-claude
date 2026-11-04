---
description: California-style essay practice — get a prompt, paste your answer, get graded on the 40–100 scale and logged
argument-hint: "<subject|crossover|past:YYYY-MM-Qn> [timed]"
---
Run one essay practice. Arguments: $ARGUMENTS

**Pick the prompt**
- **Subject or `crossover`:** choose an essay from `07-question-bank/essays/<slug or crossover>/`. Prefer one the user has not attempted (check `10-progress/attempts.csv`, kind `essay`).
- Show **only** the `## Facts` and `## Call of the Question` sections. Never show the issue list or the model answer before grading.
- **`past:YYYY-MM-Qn`:** look up the row in `06-past-exams/index.csv` and give the official link. If the PDF is in `06-past-exams/raw/`, read the question from there for grading. **Do not paste the State Bar's text into any repo file.**
- If no matching essay exists yet (the bank is filled in Phase 5), say so and offer a past-exam question instead.
- **Timed:** run `date +%s`, state 60 minutes total, and recommend about 15 min reading/outlining and about 45 min writing.

**Grade the pasted answer like a California grader** (`00-exam-intel/grader-expectations.md` §4)
1. **Issues spotted (35%):** compare against the essay's `## Issue List` (point-weighted) or, for past exams, against `06-past-exams/analyses/<exam>-Q<n>.md`. List each issue as ✅ spotted, ◐ thin, or ❌ missed, with its points.
2. **Rule accuracy (20%):** check every stated rule against `03-subjects/<slug>/rule-statements.md`. Quote the correct rule ID for each misstatement. Check CA-vs-general choices against `ca-distinctions.md`.
3. **Analysis depth (30%):** were facts actually used? Was the analysis two-sided? Were inferences explained?
4. **Organization (10%):** headings track the call, IRAC under each heading, logical order.
5. **Conclusions (5%):** every issue and every call answered.

Then give:
- a **score on the 40–100 scale in 5-point steps**, with one line explaining the band;
- the missed rules as IDs;
- the three most valuable fixes;
- a short "how a 75+ answer would have handled issue X" excerpt in your own words.

**Log it**
```
python scripts/quiz.py log --kind essay --item <ID or past:YYYY-MM-Qn> --subject <CODE or XO> --score <S> --max 100 \
    --seconds <s if timed> --rules "R-..;R-.." --error-type <dominant cause> [--source past-exam]
```
Also add one `10-progress/error-log.md` row per missed rule.
