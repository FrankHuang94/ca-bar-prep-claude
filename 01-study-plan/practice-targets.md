---
subject: study-plan
topic: Cumulative practice targets, benchmarks and go/adjust criteria
coverage_ids: []
tested_on: [MBE, essay, PT]
exam_frequency: {level: n/a, basis: "Planning document"}
last_verified: 2026-11-05
status: reviewed
---

# Practice targets and benchmarks

All numbers come from [`schedule.yml`](schedule.yml); `python scripts/build_weeks.py --totals` reprints them. `scripts/dashboard.py` compares your logged attempts (`10-progress/attempts.csv`) with the cumulative targets in `config/plan.yml`.

> Revised 2026-11-04: from December you study 3–4 h every weekday plus about 20 h on weekends (no leave). The plan totals about 1,200 hours.

## 1. Final targets

| Practice | Target | Your example range | Time cost (approx.) |
|---|---|---|---|
| MBE questions | **3,140** (2,540 in weekly sets + 600 in the 3 simulations) | 1,800–2,200 | 3,140 × ~4.5 min (1.8 answering + ~2.7 review) ≈ **236 h** |
| Timed essays | **109** (94 in weekly practice + 15 in simulations; about 8 per subject) | 60+ | 109 × ~1.7 h ≈ **185 h** |
| Issue-spotting drills (`/spot`) | **74** | — | 74 × ~20 min ≈ **25 h** |
| Performance Tests | **17** (14 + 3 in simulations) | 8–10 | 17 × ~2.5 h ≈ **43 h** |
| Full simulations | **3** (SIM-01 Apr 10–11 diagnostic; SIM-02 Jun 19–20, week −6; SIM-03 Jul 10–11, week −3) | 3 | included above |
| Total study time | **≈ 1,200 h** (1,194 scheduled) | — | Practice ≈ 489 h (41%); learning, memorization, review and MPRE ≈ 705 h (59%) |

Your example ranges assumed about 750 hours. With roughly 450 more hours, the plan raises practice volume proportionally while keeping about 59% of the time for learning and memorization, which you need for six subjects with no coursework.

## 2. Why these numbers

**MBE: 3,140 questions**
- **Exposure.** NCBE's outline has 387 lines across the 7 subjects (the `MBE` rows of the coverage matrix [S-040]). 3,140 questions is about **8 per outline line**, enough to meet each tested point in several fact patterns and after delays.
- **Weighting.** Each subject is 25 scored questions [S-007]. Including mixed sets, the schedule gives **≈ 400–510 questions per subject**: Contracts ≈ 510, Civ Pro ≈ 495, Evidence ≈ 445, Con Law ≈ 440, Torts ≈ 435, Real Property ≈ 415, Crim ≈ 400.
- **Supply.** The repo bank (≥ 1,050 original questions, Phase 5) plus licensed questions you buy as needed. Start licensed NCBE questions by **February**, so that CP2 measures real item difficulty.
- **Diminishing returns.** Beyond about 3,000, extra questions are worth less than essay and PT practice. The written section is half the score [S-011].

**Essays: 109 timed (about 8 per subject)**
- Under the Feb 2026 formula, passing with an MBE at about 1390 needs a written average of about **62.8 per graded unit** [S-011] (`00-exam-intel/format-and-scoring.md`).
- About 8 per subject on average, weighted by Phase 3 frequency: PR gets the most (11 slots plus crossovers), because it appeared on 30 of 31 exams. The rest are crossover and "weakest subject" slots chosen by the dashboard.
- **A timed essay fits a weeknight:** 60 minutes plus 30 minutes of grading.

**Issue spotting: 74 drills**
- Issue spotting is 35% of the repo rubric (`00-exam-intel/grader-expectations.md` §4).
- `/spot` trains it in about 20 minutes, so it is the cheapest volume in the plan.

**Performance Tests: 17**
- The PT is worth **two essays** [S-010] and depends least on memorized law.
- 17 covers every task type (`04-performance-test/task-types/`) at least twice, plus the three simulation PTs.

## 3. Cumulative checkpoints

| Checkpoint | Date | Hours | MBE | Essays | PTs | Spot | Simulations |
|---|---|---|---|---|---|---|---|
| CP1 | Jan 31 | 306 | 660 | 15 | 0 | 16 | 0 |
| CP2 | Mar 28 (first pass done) | 574 | 1,280 | 30 | 2 | 31 | 0 |
| CP3 | May 2 | 754 | 1,880 | 52 | 7 | 43 | 1 |
| CP4 | Jun 20 | 1,017 | 2,660 | 88 | 14 | 60 | 2 |
| CP5 | Jul 11 | 1,131 | 3,040 | 104 | 17 | 67 | 3 |
| Exam | Jul 26 | 1,194 | 3,140 | 109 | 17 | 74 | 3 |

**Essay slots by subject** (non-simulation weeks). Re-weighted after the Phase 3 frequency analysis: PR was on 30 of 31 exams; CP, Contracts, Remedies, Crim and Evidence on about half (`06-past-exams/frequency-analysis.md`).

| PRF | CTR | CMP | CIV | REM | CRM | EVD | BUS | PRP | CON | WIL | TRT | TRS | Crossover | Weakest | Mixed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 11 | 8 | 7 | 6 | 6 | 5 | 5 | 5 | 4 | 3 | 3 | 3 | 2 | 8 | 7 | 4 |

Wills and Trusts are usually tested together (Wills + Trusts was the most common crossover, 6 times), so treat their 5 slots as one unit. Many crossover and "weakest" slots will also carry PR.

The simulation weeks add 22 more: 15 in the simulations and 7 on the weeknights before them.

## 4. Benchmarks and go / adjust / escalate

**How each signal is measured** (by `scripts/dashboard.py`)
- **MBE accuracy:** your **most recent 200 questions**, all sources.
- **Written average:** your last 10 essays, with PTs counted twice, on the 40–100 scale.
- **Volume:** cumulative counts compared with §3.

| ID | Date | MBE accuracy | Written average | Admin gate |
|---|---|---|---|---|
| CP1 | Jan 31 | ≥ 50% | ≥ 55 | Registered as general applicant; credential evaluation ordered; MPRE registered (Jan 21) |
| CP2 | Mar 28 | ≥ 58% | ≥ 60 | MPRE taken; moral character filed; exam application drafted |
| CP3 | May 2 | ≥ 62% | ≥ 62 | Application filed by about Apr 1; SIM-01 reviewed; Cardozo final-transcript date known; exam-week PTO requested |
| CP4 | Jun 20 | ≥ 66% (SIM-02) | ≥ 64 | Cardozo transcript mailing confirmed for June |
| CP5 | Jul 11 | ≥ 68% (SIM-03) | ≥ 65 | Transcript received by the State Bar; Examplify mock exam done |

**Why these thresholds**
- **Written.** The CP5 target of **65** sits one 5-point band above the ~62.8 average that, under the Feb 2026 conversion, passes with an MBE at 1390 [S-011]. That leaves a cushion for one bad answer.
- **MBE.** NCBE publishes **no fixed raw-to-scaled conversion**, and accuracy on practice questions depends on their source. These percentages are **planning targets, not score predictions**. The July 2026 California mean scaled MBE (1377) was *below* the 1390 pass line [S-012], so a passing profile needs an MBE at or above the average taker's.
- **Recalibrate after your first full set of licensed NCBE questions.** If they run materially harder or easier than the repo bank, shift every MBE benchmark by the same amount and note it in `/weekly-review`.

**Decision rules at each checkpoint** (applied by `/weekly-review`)

| Result | Rule | Action |
|---|---|---|
| **Go** | Both signals at or above the benchmark, and volume ≥ 90% of target | Continue unchanged. |
| **Adjust** | MBE up to 5 points below, **or** written up to 3 below, **or** volume 75–90% of target | For the next 2 weeks, move about 25% of learning time to the 2 weakest subjects or skills (`/weak-spots`). Add one `/spot` per week. |
| **Escalate** | MBE more than 5 points below, **or** written more than 3 below, **or** two consecutive "adjust" results, **or** volume < 75% | Change the plan with me. Options: add PTO days, re-weight weekends toward the weakest component, cut low-yield reading, re-sequence subjects. |
| **Sit-or-defer review** | At **CP4**: MBE < 58% **and** written < 58 | You've said retakes are acceptable. Decide deliberately whether July 2027 is a real attempt or a rehearsal. **Feb 2028 is the last exam in this format** [S-027]. **Money:** on the Feb 2027 pattern, withdrawal refunds are 60% within about 30 days after the timely deadline and 30% within about 45 days, then nothing except in limited cases; withdrawal itself stays open until about two weeks before the exam [S-004]. For July 2027 that means about **May 1 (60%)** and **May 16 (30%)** (est. [VERIFY V-016]), so by CP4 no refund is likely. If CP3 (May 2) is already far below target, weigh the refund then. |

**Admin gates are hard.** A missed admin gate is an escalation regardless of scores. Eligibility, the MPRE and application deadlines cannot be recovered by studying harder.

## 5. Logging rules (so the numbers mean something)
- Every MBE question goes into `attempts.csv`: repo questions via `/quiz` or `quiz.py run`; licensed questions via `quiz.py log --source official|commercial`. Never paste licensed question text.
- An essay counts toward the target only if **timed and self-graded** with `/essay`. Untimed or open-book essays (W49) are logged with a note.
- A PT counts if completed in 90 minutes (the untimed W07 PT is logged with a note).
- Simulation items are logged individually (`build_simulation.py score` handles the MBE part).
