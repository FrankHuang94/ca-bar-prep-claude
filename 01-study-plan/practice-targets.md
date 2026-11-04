---
subject: study-plan
topic: Cumulative practice targets, benchmarks and go/adjust criteria
coverage_ids: []
tested_on: [MBE, essay, PT]
exam_frequency: {level: n/a, basis: "Planning document"}
last_verified: 2026-11-04
status: draft
---

# Practice targets and benchmarks

All numbers come from [`schedule.yml`](schedule.yml); `python scripts/build_weeks.py --totals` reprints them. `scripts/dashboard.py` compares your logged attempts (`10-progress/attempts.csv`) with the cumulative targets in `config/plan.yml`.

## 1. Final targets

| Practice | Target | Your suggested range | Time cost (approx.) |
|---|---|---|---|
| MBE questions | **2,170** (1,570 in weekly sets + 600 in the 3 simulations) | 1,800–2,200 | 2,170 × ~4.5 min (1.8 answering + ~2.7 review) ≈ **163 h** |
| Timed essays | **68** (53 + 15 in simulations) | 60+ | 68 × ~1.7 h (60 min writing + ~40 min self-grading) ≈ **115 h** |
| Issue-spotting drills (`/spot`) | **53** | — | 53 × ~20 min ≈ **18 h** |
| Performance Tests | **12** (9 + 3 in simulations) | 8–10 | 12 × ~2.5 h ≈ **30 h** |
| Full simulations | **3** (SIM-01 diagnostic; SIM-02 week −6; SIM-03 week −3) | 3 (−6 and −3) | included above |
| Total study time | **≈ 755 h** | — | Practice ≈ 326 h (43%); learning, memorization, review and MPRE ≈ 429 h (57%) |

## 2. Why these numbers

**MBE: 2,170 questions**
- **Exposure.** NCBE's outline has 387 lines across the 7 subjects (the `MBE` rows of the coverage matrix [S-040]). 2,170 questions is about **5–6 questions per outline line**: enough to see each tested point several times, in different fact patterns, at least once after a delay.
- **Volume relative to the exam.** It equals about 11 full MBEs, or about 12 times the 175 scored questions [S-006].
- **Weighting.** Each subject is 25 scored questions [S-007], so the plan aims for **≥ 280 per subject**. The schedule front-loads the four new subjects. Contracts (≈ 396 including its share of mixed sets) and Civ Pro (≈ 356) get the most; Torts (≈ 261) and Real Property (≈ 256), which you have studied, get fewer. **Bias mixed sets toward Torts and Real Property** in the intensive phase to bring both to ≥ 280.
- **Diminishing returns.** Beyond about 2,200, the marginal question is worth less than the essay and PT practice it would displace, given that the written section is half the score [S-011].

**Essays: 68 timed (≈ 5 per subject)**
- Under the Feb 2026 formula, passing with an MBE at about 1390 needs a written average of about **62.8 per graded unit** [S-011] (see `00-exam-intel/format-and-scoring.md`). For a writer new to IRAC, consistency at 60–65 takes repetition under time pressure.
- Five per subject lets each subject's recurring issues (Phase 3 frequency data) recur at least twice.
- Ten slots are crossovers (≥ 30%, as required for the repo bank). Six are "weakest subject" slots chosen by the dashboard.
- About 60 is the **minimum**. The extra 8 are simulation essays, written under full exam conditions.

**Issue spotting: 53 drills**
- Issue spotting is 35% of the repo rubric (`00-exam-intel/grader-expectations.md` §4), and a missed major issue costs about one band.
- `/spot` trains it in about 20 minutes instead of 100, so it is the cheapest volume in the plan.

**Performance Tests: 12**
- The PT is worth **two essays** [S-010] and depends least on memorized law, so a point gained on the PT is worth twice an essay point.
- One PT per week in the intensive phase gives familiarity with every task type (`04-performance-test/task-types/`) without crowding out essays.

**Simulations: 3**
- **SIM-01 (diagnostic, May 1–2):** sets the second-pass priorities.
- **SIM-02 (week −6) and SIM-03 (week −3):** endurance rehearsals on real weekdays and timing, as you specified.

## 3. Cumulative checkpoints

| Checkpoint | Date | Hours | MBE | Essays | PTs | Spot | Simulations |
|---|---|---|---|---|---|---|---|
| CP1 | Jan 31 | 129 | 305 | 4 | 0 | 6 | 0 |
| CP2 | Mar 28 | 219 | 550 | 7 | 0 | 13 | 0 |
| CP3 | May 2 | 306 | 970 | 18 | 3 | 21 | 1 |
| CP4 | Jun 20 | 562 | 1,670 | 48 | 9 | 39 | 2 |
| CP5 | Jul 11 | 686 | 2,070 | 63 | 12 | 46 | 3 |
| Exam | Jul 26 | 755 | 2,170 | 68 | 12 | 53 | 3 |

**Essay slots by subject** (non-simulation). Phase 3 frequency data will re-weight the WEAK/MIX/crossover slots:

| CTR | CIV | EVD | CON | CRM | CMP | REM | PRF | WIL | TRS | BUS | TRT | PRP | Crossover | Weakest | Mixed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5 | 4 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 10 | 6 | 5 |

## 4. Benchmarks and go / adjust / escalate

**How each signal is measured** (by `scripts/dashboard.py`)
- **MBE accuracy:** over your **most recent 200 questions**, all sources.
- **Written average:** your last 10 essays, with PTs counted twice, on the 40–100 scale.
- **Volume:** cumulative counts compared with §3.

| ID | Date | MBE accuracy | Written average | Admin gate |
|---|---|---|---|---|
| CP1 | Jan 31 | ≥ 50% | ≥ 55 | Eligibility route decided; written determination requested; MPRE registered (Jan 21) |
| CP2 | Mar 28 | ≥ 56% | ≥ 58 | MPRE taken; moral character filed; exam application drafted |
| CP3 | May 2 | ≥ 60% (SIM-01) | ≥ 60 | Application filed by about Apr 1; leave confirmed |
| CP4 | Jun 20 | ≥ 65% (SIM-02) | ≥ 63 | Plan to mail the sealed transcript or CGS by about Jun 25 |
| CP5 | Jul 11 | ≥ 68% (SIM-03) | ≥ 65 | Examplify mock exam done; hotel booked |

**Why these thresholds**
- **Written.** The CP5 target of **65** sits one 5-point band above the ~62.8 average that, under the Feb 2026 conversion, passes with an MBE at 1390 [S-011]. That leaves a cushion for one bad answer. Earlier targets climb toward it from a realistic start (55) for a writer new to IRAC.
- **MBE.** NCBE publishes **no fixed raw-to-scaled conversion**, and accuracy on practice questions depends on their source and difficulty. These percentages are **planning targets, not score predictions**. They are set so the MBE is not a liability: the July 2026 California mean scaled MBE (1377) was *below* the 1390 pass line [S-012], so a passing profile needs an MBE at or above the average taker's.
- **Recalibrate after your first full set of licensed NCBE questions.** If those run materially harder or easier than the repo bank, shift every MBE benchmark by the same amount and note it in `/weekly-review`.

**Decision rules at each checkpoint** (applied by `/weekly-review`)

| Result | Rule | Action |
|---|---|---|
| **Go** | Both signals at or above the benchmark, and volume ≥ 90% of target | Continue the schedule unchanged. |
| **Adjust** | MBE up to 5 points below, **or** written up to 3 points below, **or** volume 75–90% of target | For the next 2 weeks, move about 25% of learning time to the 2 weakest subjects or skills (`/weak-spots`). Add one `/spot` per week. Re-check at the next weekly review. |
| **Escalate** | MBE more than 5 points below, **or** written more than 3 below, **or** two consecutive "adjust" results, **or** volume < 75% | Change the plan with me: start leave earlier (option A), cut low-yield reading, raise timed-practice share, re-sequence subjects. |
| **Sit-or-defer review** | At **CP4**: MBE < 58% **and** written < 58 | Decide deliberately whether to sit in July 2027 or withdraw and target **Feb 2028**, the last exam in this format [S-027]. Check the State Bar's withdrawal deadline and refund rules first [VERIFY V-060]. |

**Admin gates are hard.** A missed admin gate is an escalation regardless of scores. Eligibility, the MPRE and application deadlines cannot be recovered by studying harder.

## 5. Logging rules (so the numbers mean something)
- Every MBE question goes into `attempts.csv`: repo questions via `/quiz` or `quiz.py run`; licensed questions via `quiz.py log --source official|commercial`. Never paste licensed question text.
- An essay counts toward the target only if **timed and self-graded** with `/essay`. Untimed or open-book essays are logged with a note.
- A PT counts if completed in 90 minutes (the untimed W14 PT is logged with a note).
- Simulation items are logged individually (`build_simulation.py score` does the MBE part).
