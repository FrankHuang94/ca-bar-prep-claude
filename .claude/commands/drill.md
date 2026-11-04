---
description: Rule-statement drill — type rules from memory, graded for completeness against rule-statements.md
argument-hint: "<subject> [n=8]"
---
Run a rule drill. Arguments: $ARGUMENTS

1. Load `03-subjects/<slug>/rule-statements.md`. If it doesn't exist yet (Phase 4), say so and stop.
2. Choose n rules, prioritizing:
   1. rules in `rule_ids_missed` in `10-progress/attempts.csv` or in `10-progress/error-log.md` for this subject;
   2. rules due under `01-study-plan/spaced-repetition.md`;
   3. rules on `memorization-list.md` "must-know";
   4. random.
3. For each rule, show only its **ID and title** and ask the user to type the essay-ready rule statement (and elements, if any).
4. Compare the attempt with the `**Rule (write this):**` text and the `**Elements:**`. Score it 0–3:
   - 0: wrong or blank;
   - 1: gist only;
   - 2: right rule, missing an element or qualifier;
   - 3: complete and essay-ready.

   Show the canonical statement, highlight what was missing, and give a short memory hook.
5. Log each rule: `python scripts/quiz.py log --kind drill --item R-XXX-### --subject <CODE> --score <0-3> --max 3 [--rules R-XXX-### if score<3] --error-type <didnt-know if 0-1, else misapplied>`
6. Finish with a list of rules scoring 0–1, to re-drill in 2 days.
