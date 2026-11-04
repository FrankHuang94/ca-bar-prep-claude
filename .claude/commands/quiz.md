---
description: Timed MBE-style questions one at a time from the repo bank; grade, explain every option, log
argument-hint: "<subject|mixed> [n=10] [difficulty 1-3] [subtopic coverage_id prefix, e.g. EVD-MBE-V]"
---
Run an MBE-style quiz. Arguments: $ARGUMENTS. The first argument is a subject (code, slug or name) or `mixed`; n defaults to 10.

1. Fetch the questions:
   `python scripts/quiz.py pick --subject <s> --n <n> [--difficulty d] [--subtopic p] --full`
   - The JSON contains the answers. **Never reveal or hint at an answer before the user commits.**
   - If the bank has no matching questions (it is filled in Phase 5), say so and stop. Do not improvise questions outside the validated bank.
2. Present **one question at a time**:
   - `Question k/n [ID · subject]`, then the stem, the call, and options (A)–(D);
   - run `date +%s` to note the start time;
   - remind the user the target pace is about 1.8 min (108 s) per question.
3. When the user answers with a letter, compute the seconds elapsed (`date +%s`).
   - **If correct:** log immediately with `python scripts/quiz.py log --id <ID> --answer <X> --seconds <s>`.
   - **If wrong:** first show the explanation, then ask for the root cause:
     1 didn't know the rule · 2 misapplied · 3 misread facts · 4 timing · 5 careless.

     Log with `--error-type didnt-know|misapplied|misread|timing|careless`. Then append a row to `10-progress/error-log.md` (date, item, rule ID, root cause, what went wrong in the user's words, a memory hook, revisit date = today + 3 days).
4. Each explanation covers:
   - why the key is right, with the rule and its authority;
   - **why each wrong option is wrong**, naming the commonly confused rule it baits;
   - the trap type;
   - the rule ID(s) and a link to `03-subjects/<slug>/rule-statements.md`;
   - a one-line memory hook.
5. At the end show the score, average seconds per question and the missed rule IDs. Suggest `/drill <subject>` on the missed rules and `/explain` for any rule missed twice.

Use Socratic hints only if the user asks for one; a hint costs the question, so log it as wrong with `--error-type didnt-know`.
