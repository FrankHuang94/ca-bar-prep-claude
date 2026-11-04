---
description: Tell me exactly what to study today, given the plan and my available time
argument-hint: "[hours available, e.g. 1.5h] [notes, e.g. 'tired' or 'travel']"
---
Build today's study session for the July 2027 California bar. Arguments: $ARGUMENTS

1. Get today's date (`date +%F`) and ISO week (`date +%G-W%V`). Read `config/plan.yml`:
   - current phase and its focus and hour band;
   - `weekly_template` hours for today's weekday;
   - holidays, blackouts and leave;
   - `admissions` items due in the next 14 days.
2. Read this week's file `01-study-plan/weeks/<ISO week>.md` if it exists. Before Phase 2 it won't; use the phase focus instead and say so.
3. Available time is the hours given in the arguments if any, otherwise the `weekly_template` value. On a holiday or blackout, propose a light session.
4. Collect what is **due**:
   - missed MCQs due for review: `python scripts/quiz.py pick --subject mixed --n 10`, whose first picks are review items;
   - `10-progress/error-log.md` rows whose "Revisit on" date is today or earlier;
   - spaced-repetition reviews per `01-study-plan/spaced-repetition.md`;
   - any admissions deadline within 14 days. Put it at the top in bold.
5. Output a **time-boxed plan** that adds up to the available time. Each block gives:
   - minutes;
   - the exact files to read (repo paths);
   - the exact commands or slash commands to run, e.g. `/quiz evidence 15`, `/drill contracts 8`;
   - one line on why.

   Always include some MBE practice and a flashcard/rule-drill block. Follow the week file's essay or PT cadence.
6. End with one sentence on what tomorrow should pick up if today's plan isn't finished.

Do not edit files. Keep the answer under about 25 lines.
