---
description: 90-minute Performance Test practice graded against task requirements and format
argument-hint: "[past:YYYY-MM | original]"
---
Run one Performance Test. Arguments: $ARGUMENTS. The default is `original`.

**Setup**
- **`original`:** pick an unattempted `07-question-bank/pt/PT-###.md` that is not listed by `python scripts/quiz.py reserved` (held back for a simulation) and present its Task Memorandum, File and Library.
- **`past:YYYY-MM`:** give the link from `04-performance-test/past-pt-index.csv`. If the PDF is in `06-past-exams/raw/`, use it for grading. Never paste State Bar text into repo files.
- Run `date +%s`. Remind the user of the 90-minute plan in `04-performance-test/method.md` and of the task-type template in `04-performance-test/task-types/`.

**Grade** (the State Bar grades on "compliance with instructions and on its content, thoroughness, and organization"):
1. **Task compliance (30%):** right document type, audience, tone, format and length; every instruction in the memo followed.
2. **Use of the Library (25%):** correct rules drawn from the provided authorities, cited by name. No outside law substituted for the Library's.
3. **Use of the File (25%):** relevant facts applied, irrelevant ones ignored, gaps or ambiguities flagged as the task requires.
4. **Organization and completeness (20%):** headings and structure fit the task; every requested part delivered.

Give:
- a score from 40 to 100 in 5-point steps;
- the strongest and weakest parts;
- what a top answer would have structured differently;
- a time-management note.

**Log it**
`python scripts/quiz.py log --kind pt --item <PT-### or past:YYYY-MM> --subject PT --score <S> --max 100 --seconds <s> [--source past-exam]`
Then add an error-log row for each recurring problem.
