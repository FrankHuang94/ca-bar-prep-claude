---
description: Assemble and run a full mock exam (5 essays + PT + 200 MCQ), then produce a score report
argument-hint: "[build|score SIM-##] [--allow-short]"
---
Full-length simulation. Arguments: $ARGUMENTS

**Build**
1. Run `python scripts/build_simulation.py build`.
   - If the bank is too small, it reports the shortfall. Before Phase 5 is complete, ask whether to run a partial mock (`--allow-short`).
2. It writes:
   - a manifest at `07-question-bank/simulations/SIM-##.yaml` (commit it);
   - booklets in `exports/SIM-##/`: day1-am-essays, day1-pm-essays-pt, day2-am-mbe, day2-pm-mbe, answer-key.

   Tell the user where the booklets are and **never show the answer key**.
3. Give the schedule. It mirrors the real exam [S-003]:
   - Day 1 morning: Essays 1–3 (3 h).
   - Day 1 afternoon: Essays 4–5 + PT (3.5 h).
   - Day 2: two 3-hour MBE sessions of 100 questions each, no breaks within a session.
   Recommend the real start times (seated by 8:20 a.m.) and taking it on two consecutive days.

**Score** (after the user sits it)
1. **MBE:** the user saves 200 answer letters in order (`-` = blank) to a file. Then run `python scripts/build_simulation.py score SIM-## --mbe-answers <file>`, which logs each question.
2. **Essays and PT:** grade each one the user pastes, exactly as in `/essay` and `/pt`, and log each with `quiz.py log` (`--notes SIM-##`).
3. Write the report to `10-progress/simulation-reports/SIM-##.md` (front matter `subject: progress`) with:
   - MBE accuracy overall and by subject;
   - pace;
   - essay and PT scores, plus the **written raw total out of 700** (5 essays + 2 × PT);
   - the average per graded unit compared with the ~60–65 band in `00-exam-intel/format-and-scoring.md`;
   - the top 5 fixes;
   - the comparison with the current benchmark in `config/plan.yml`.

   **Do not claim a scaled score.** The written-to-scale formula changes every administration.
4. Run `python scripts/dashboard.py` and `python scripts/validate.py`, then commit and push.
