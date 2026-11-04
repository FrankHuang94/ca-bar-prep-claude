---
description: Analyze attempts and the error log; produce a targeted 1-week remediation plan
argument-hint: "[days to look back, default 30]"
---
Diagnose weak spots and build a remediation week. Arguments: $ARGUMENTS (look-back window in days; default 30).

1. Read `10-progress/attempts.csv` (filter by date) and `10-progress/error-log.md`. Compute:
   - MBE accuracy by subject and by topic (coverage_id at topic level; at least 5 attempts);
   - average seconds per question;
   - essay and PT averages by subject;
   - error-type mix;
   - the 10 most-missed rule IDs;
   - rules that were drilled but are still missed.
   You may run `python scripts/dashboard.py --stdout` for a baseline.
2. Diagnose the **3–5 highest-leverage problems**, weighted by exam impact:
   - MBE subject weight (each subject is 25 scored questions);
   - essay frequency (`06-past-exams/frequency-analysis.md`);
   - the PT counting double.
   Separate knowledge gaps (didnt-know) from skill gaps (misapplied, misread, timing).
3. Write a **7-day remediation plan**. Each day's tasks fit `config/plan.yml` hours and give:
   - the exact files to read;
   - the `/quiz <subject> <n> <difficulty> <subtopic>` commands;
   - `/drill` targets with rule IDs;
   - one `/essay` or `/spot` per weak essay subject.
   Define what success looks like by day 7, as accuracy or score targets.
4. Save it as `10-progress/weekly-reviews/<YYYY-MM-DD>-weak-spots.md`, with front matter (`subject: progress`). Run `python scripts/validate.py`, then commit with message `progress: weak-spots plan <date>`.
