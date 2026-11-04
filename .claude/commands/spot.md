---
description: 10-minute issue-spotting drill; list the issues, then see the full issue map
argument-hint: "<subject|crossover>"
---
Run a 10-minute issue-spotting drill. Arguments: $ARGUMENTS

1. Pick an essay from `07-question-bank/essays/<slug or crossover>/`, preferring ones not used in `/essay` or `/spot` (check `attempts.csv`). Before Phase 5, use a past exam that has an analysis in `06-past-exams/analyses/`.
2. Show the Facts and the Call. Run `date +%s` and say: "10 minutes: list every issue, one line each, in the order you would write them."
3. When the user replies:
   - compare against the item's point-weighted `## Issue List`;
   - show a table of each issue, its points, and spotted / missed;
   - mark the **major** issues;
   - point out ordering problems, such as threshold issues not placed first;
   - name the fact that should have triggered each missed issue.
4. Score = points spotted out of 100. Log: `python scripts/quiz.py log --kind spot --item <ID> --subject <CODE or XO> --score <pts> --max 100 --seconds <s>`
5. For each missed **major** issue, add the rule ID to `10-progress/error-log.md` with root cause `misread` or `didnt-know`.
