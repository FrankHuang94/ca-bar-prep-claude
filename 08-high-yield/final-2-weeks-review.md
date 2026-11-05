---
subject: high-yield
topic: Final two weeks — day-by-day review plan, Mon Jul 12 to Sun Jul 25, 2027, plus the night before and the evening between exam days
coverage_ids: []
tested_on: [MBE, essay, PT]
exam_frequency: {level: high, basis: "Final-review weeks 2027-W28 and 2027-W29 of 01-study-plan/schedule.yml; exam Tue-Wed Jul 27-28, 2027 (S-001)"}
last_verified: 2026-11-05
status: reviewed
---

# Final two weeks: Mon Jul 12 – Sun Jul 25, 2027

The exam is **Tue–Wed Jul 27–28, 2027** [S-001]: Day 1 is written (essays and the PT), Day 2 is the MBE. This page turns [`2027-W28`](../01-study-plan/weeks/2027-W28.md), [`2027-W29`](../01-study-plan/weeks/2027-W29.md) and the final-review row of [`master-plan.md`](../01-study-plan/master-plan.md) into a plan for each day. If `schedule.yml` changes, the week files win; adjust this page to match.

## Ground rules

1. **No new material.** You reread, recite and practise briefly. No new Anki cards after W28 ([`spaced-repetition.md`](../01-study-plan/spaced-repetition.md) §6).
2. **Hours follow the week files.**
   - W28: 3.25 h each weeknight and 9.5 h each weekend day, ≈ 35 h.
   - W29: 3 h each weeknight and 9 h on Saturday, 24 h in all. **Sunday Jul 25 is rest (0 h).**
   - Stop by 22:00 on weeknights.
3. **Sleep shift in W29.** From **Mon Jul 19**, get up by **6:30 a.m.** every day, weekends included, and keep a steady bedtime about 8 hours earlier. You must be seated by 8:20 a.m. on both exam days [S-003] [VERIFY V-055].
4. **Practice volume (from the week files).**
   - MBE: 60 questions in W28, 40 in W29.
   - Timed essays: 3 in W28, 2 in W29.
   - `/spot`: 4 in W28, 3 in W29.
   - No PTs.
5. **Simulation items are not fresh practice.** Do not reuse the essays and PTs set aside for SIM-01 to SIM-03 (`python scripts/quiz.py reserved` lists them until each simulation is logged as sat): E-CIV-004, E-CMP-001, E-CON-004, E-CRM-001, E-CTR-002, E-EVD-001, E-PRF-003, E-PRP-005, E-TRT-004, E-WIL-003, E-XO-003, E-XO-012, E-XO-021, E-XO-022, E-XO-027 and PT-001 to PT-003.
   - Every essay named below is outside that list. By July you may have written it once already. If you wrote it in the last four weeks, use the alternative given.
   - `/quiz mixed` draws its own questions.
6. **Every study day includes 10–20 minutes of Anki** (clear due cards only) and the **must-know list** for the day's subjects ([`memorization-master.md`](memorization-master.md) §3).

**Files you reread in these two weeks**
- In this folder: [`most-tested-issues.md`](most-tested-issues.md), [`top-rules-mbe-subjects.md`](top-rules-mbe-subjects.md), [`top-rules-california-subjects.md`](top-rules-california-subjects.md), [`mbe-vs-california-master-table.md`](mbe-vs-california-master-table.md), [`crossover-guide.md`](crossover-guide.md), [`mnemonics.md`](mnemonics.md) and [`memorization-master.md`](memorization-master.md).
- In each subject folder: `attack-outline.md`, `memorization-list.md` and `essay-templates.md`.

## Week view

| | W28: Jul 12–18 | W29: Jul 19–25 |
|---|---|---|
| Theme | SIM-03 review, then all 13 attack outlines and the high-yield files | Must-know tier daily; taper; sleep shift |
| Attack outlines | Wed EVD, CMP · Thu CTR, REM · Fri CRM, CON · Sat CIV, TRT, PRP, BUS · Sun PRF, WIL, TRS | None in full; must-know lists by rotation |
| MBE | Weeknights 8 each; weekends 10 each (60) | Mon–Thu 8 each; Sat 8 (40) |
| Essays | Mon weakest subject · Tue crossover · Wed mixed | Mon · Tue |
| `/spot` | Tue · Thu · Sat · Sun | Tue · Thu · Sat |

## How SIM-03 (checkpoint CP5) shapes these two weeks

CP5 benchmarks ([`practice-targets.md`](../01-study-plan/practice-targets.md) §4):
- MBE **≥ 68%** on SIM-03;
- written average **≥ 65**;
- transcript received by the State Bar;
- Examplify mock exam done.

These are planning targets, not score predictions. Apply the result on Mon–Tue Jul 12–13.

| CP5 result | What changes on this page |
|---|---|
| **Go** (both at or above) | Nothing. Follow the days as written. |
| **Adjust** (MBE up to 5 points below, or written up to 3 below) | Re-point the "weakest subject" slots: Mon's essay, Sat's `/drill`, Sun's cold-write check and the Jul 24 must-know block all go to the two weakest subjects or skills from `/weak-spots`. If the MBE is the weak signal, swap half the `/quiz mixed` sets for `/quiz <weak subject> 8`. The total volume stays the same. Turn Fri Jul 16's read-only review into a `/spot` if the essays are the weak signal. |
| **Escalate** (more than 5 points / 3 points below) | Decide with me on Mon Jul 12. Options the plan allows: PTO on Fri Jul 16 and Fri Jul 23, and weekend hours re-weighted toward the weak component. **Never** new material, and never at the cost of sleep in W29. |

**If a day is lost** (work spike or illness):
- Cut in this order: (1) the timed essay, (2) the attack-outline reading, (3) the MBE set.
- **Keep** the must-know list, Anki and that day's checklist.
- Do not try to make up a lost day by stacking it onto the next. In W29, protect sleep before anything else.

**Weeknight shape** (adapted from master-plan §3):
- 18:30 timed essay or attack-outline reading;
- 19:30 self-grade or must-know list;
- 20:15 MBE set and review;
- 21:15 `/drill` and Anki;
- 22:00 stop.

## Week 28: SIM-03 review and high-yield reading

### Mon Jul 12 (T−15) · 3.25 h · SIM-03 review 1
- **Evening plan:**
  - 60 min SIM-03 review: MBE misses by subject and category, each with its error type. If the score report is not done yet, run `/simulate`'s score step (`python scripts/build_simulation.py score SIM-03 --mbe-answers <file>`).
  - 75 min timed essay plus self-grading.
  - 20 min MBE.
  - 20 min must-know list.
  - 15 min Anki.
- **Reread:** the weakest subject's rows in [`most-tested-issues.md`](most-tested-issues.md) part (a), then that subject's `essay-templates.md`.
- **Drill / quiz:** `/quiz mixed 8` · `/drill <weakest subject> 8`.
- **Essay:** `/essay <weakest subject on the dashboard> timed`. Pick an essay you have not written since May, and none from the simulation list.
- **Checklist:**
  - [ ] SIM-03 misses logged in `10-progress/error-log.md`.
  - [ ] July 2027 Admittance Ticket Bulletin published? If so, start reading it ([`exam-day-logistics.md`](../09-exam-strategy/exam-day-logistics.md) §2).

### Tue Jul 13 (T−14) · 3.25 h · SIM-03 review 2 and the weak-spot list
- **Evening plan:**
  - 30 min SIM-03 essay and PT self-review.
  - 20 min `/weak-spots 30`: write the **final weak-spot list** (the 10 rule IDs you miss most).
  - 75 min crossover essay.
  - 20 min `/spot`.
  - 20 min MBE.
  - 15 min Anki.
- **Reread:** [`top-rules-california-subjects.md`](top-rules-california-subjects.md) §1 (PR); the PR section of [`mbe-vs-california-master-table.md`](mbe-vs-california-master-table.md) (§3.9); the PR rows of [`mnemonics.md`](mnemonics.md).
- **Drill / quiz:** `/quiz mixed 8` · `/drill professional-responsibility 6`.
- **Essay:** `/essay crossover timed`, using **E-XO-028** (Trusts + PR). Alternative: E-XO-024 (Civ Pro + PR). Organize it with [`crossover-guide.md`](crossover-guide.md).
- **/spot:** `/spot community-property`.
- **Checklist (T−14, from exam-day-logistics §3):**
  - [ ] Cardozo transcript **received** by the State Bar (estimated final eligibility date) [VERIFY V-016].
  - [ ] Admittance ticket received; test site confirmed.
  - [ ] Bulletin read end to end; §2 open items ticked.
  - [ ] Hotel booked for Mon–Wed nights if the commute is over about 30 minutes.
  - [ ] Automatic OS updates off; Examplify requirements checked; administrator rights on the laptop.

### Wed Jul 14 (T−13) · 3.25 h · Evidence + Community Property
- **Reread:** the Evidence and CP attack outlines; [`top-rules-mbe-subjects.md`](top-rules-mbe-subjects.md) §5 (EVD) and [`top-rules-california-subjects.md`](top-rules-california-subjects.md) §2 (CP); [`mbe-vs-california-master-table.md`](mbe-vs-california-master-table.md) §3.1 (Evidence).
- **Drill / quiz:** `/quiz mixed 8` · `/drill evidence 8`.
- **Essay:** `/essay crossover timed`, using **E-XO-016** (CP + Wills). Alternative: E-XO-002 (CP + Wills).
- **Checklist:**
  - [ ] Register in Examplify and download the mock exam. The window is T−12 to T−5; do not leave it to the deadline.

### Thu Jul 15 (T−12) · 3.25 h · Contracts + Remedies
- **Reread:** the Contracts and Remedies attack outlines; [`top-rules-mbe-subjects.md`](top-rules-mbe-subjects.md) §1 (CTR) and [`top-rules-california-subjects.md`](top-rules-california-subjects.md) §5 (REM); [`crossover-guide.md`](crossover-guide.md) §2 (Contracts + Remedies) and §4 (Torts + Remedies); the Contracts and Remedies rows of [`mnemonics.md`](mnemonics.md).
- **Drill / quiz:** `/quiz mixed 8` · `/drill contracts 8` · `/drill remedies 6`.
- **/spot:** `/spot remedies`.
- **Checklist:**
  - [ ] Final weak-spot list: every rule on it drilled at least once.

### Fri Jul 16 (T−11) · 3.25 h · Criminal + Con Law (lighter evening)
- **Reread:** the Criminal and Con Law attack outlines; §3 (CON) and §4 (CRM) of [`top-rules-mbe-subjects.md`](top-rules-mbe-subjects.md).
- **Drill / quiz:** `/quiz mixed 8` · `/drill criminal-law-procedure 8`.
- **Essay or /spot:** none scheduled. Instead, a 10-minute read-only review of Criminal Template 3 (suppression, item by item).
- **Checklist:**
  - [ ] Stop by 21:30. This is the week's lighter evening.

### Sat Jul 17 (T−10) · 9.5 h · Civ Pro, Torts, Real Property, BA
- **Plan:** start at **08:20** as on exam days.
  - 2 h Civ Pro.
  - 2 h Torts.
  - Lunch.
  - 2 h Real Property.
  - 1.5 h BA.
  - 30 min MBE.
  - 20 min `/spot`.
  - Anki.
  - Free evening.
- **Reread:** these four attack outlines; [`top-rules-mbe-subjects.md`](top-rules-mbe-subjects.md) §2 (CIV), §6 (PRP) and §7 (TRT); [`top-rules-california-subjects.md`](top-rules-california-subjects.md) §6 (BA); [`most-tested-issues.md`](most-tested-issues.md) part (b).
- **Drill / quiz:** `/quiz mixed 10` · `/drill civil-procedure 8` · `/drill torts 8`.
- **/spot:** `/spot torts`.
- **Checklist:**
  - [ ] **Examplify mock exam completed and uploaded this weekend.** Keep the confirmation.

### Sun Jul 18 (T−9) · 9.5 h · PR, Wills, Trusts
- **Plan:**
  - 2.5 h PR.
  - 2 h Wills + Trusts.
  - Lunch.
  - 1.5 h cold-write check of the must-know rules for your two weakest subjects ([`memorization-master.md`](memorization-master.md) §5).
  - 30 min MBE.
  - 20 min `/spot`.
  - `/weekly-review`.
  - Anki.
- **Reread:** the PR, Wills and Trusts attack outlines; [`top-rules-california-subjects.md`](top-rules-california-subjects.md) §1, §3 and §4; [`crossover-guide.md`](crossover-guide.md) §1 (Wills + Trusts) and §3 (CP + Wills); [`mbe-vs-california-master-table.md`](mbe-vs-california-master-table.md) §2 (the top 25 flips).
- **Drill / quiz:** `/quiz mixed 10` · `/drill professional-responsibility 10`.
- **/spot:** `/spot crossover`.
- **Checklist:**
  - [ ] All 13 attack outlines reread this week.
  - [ ] Examplify mock uploaded (finish today if not).
  - [ ] Hotel or commute decided.

## Week 29: must-know daily, taper and sleep shift

From today: **up by 6:30 a.m.** Do 15 minutes of Anki before work, so you practise retrieval at exam hour. Each evening covers the day's **must-know rotation** (memorization-master §3 IDs, checked against `rule-statements.md`).

### Mon Jul 19 (T−8) · 3 h · must-know: PR + Evidence
- **Reread:** the PR and Evidence `memorization-list.md` must-know tiers; Evidence "California gaps and additions".
- **Drill / quiz:** `/quiz mixed 8` · `/drill professional-responsibility 6` · `/drill evidence 6`.
- **Essay:** `/essay crossover timed`, using **E-XO-006** (Evidence + PR). Alternative: E-XO-019.
- **Checklist:**
  - [ ] Up at 6:30.
  - [ ] Lights out on schedule.

### Tue Jul 20 (T−7) · 3 h · must-know: CP, Wills, Trusts
- **Morning (before work):** **drive the route** at the real time and arrive by 7:50 a.m.; note parking and the walk to the entrance.
- **Reread:** the CP, Wills and Trusts must-know tiers; the CP formulas; [`mnemonics.md`](mnemonics.md) #29–31 and #44–48.
- **Drill / quiz:** `/quiz mixed 8` · `/drill community-property 8`.
- **Essay:** `/essay crossover timed`, using **E-XO-015** (Contracts + Remedies). Alternative: E-XO-017 (Torts + Remedies).
- **/spot:** `/spot wills-succession`.
- **Checklist:**
  - [ ] Buy supplies that fit the 2027 bulletin: one-gallon clear bag, foam earplugs, an allowed water bottle [VERIFY V-050].

### Wed Jul 21 (T−6) · 3 h · must-know: Contracts, Remedies, BA
- **Reread:** the Contracts, Remedies and BA must-know tiers.
- **Drill / quiz:** `/quiz mixed 8` · `/drill contracts 6` · `/drill remedies 6`.
- **Essay or /spot:** none scheduled. Instead, a 10-minute read-only review of the openers of Contracts Template 1 and Remedies Template 1.
- **Checklist:**
  - [ ] Examplify mock confirmation saved.
  - [ ] MBE-day pencil rule re-checked in the 2027 bulletin (2026: bring your own non-mechanical #2 pencils; erasers allowed) [S-003] [S-1736].

### Thu Jul 22 (T−5) · 3 h · must-know: Civ Pro, Con Law
- **Reread:** the Civ Pro and Con Law must-know tiers; the Civ Pro numbers table.
- **Drill / quiz:** `/quiz mixed 8` · `/drill civil-procedure 8`.
- **/spot:** `/spot constitutional-law`.
- **Checklist:**
  - [ ] Packing list drafted from exam-day-logistics §5.
  - [ ] PTO for Fri confirmed if available.

### Fri Jul 23 (T−4) · 3 h (PTO if possible) · must-know: Criminal, Torts, Real Property
- **Reread:** the Criminal, Torts and Real Property must-know tiers; all of [`mnemonics.md`](mnemonics.md) once (30 min).
- **Drill / quiz:** `/drill criminal-law-procedure 6` · `/drill torts 6`. No MBE set today.
- **Essay or /spot:** none. Read the two exam-day pages below.
- **Checklist:**
  - [ ] **Examplify mock exam deadline (est.)**. It must already be done [VERIFY V-016].

### Sat Jul 24 (T−3) · 9 h · light rehearsal
- **Plan:**
  - Start at **08:20**: `/spot` (20 min).
  - 3 h on [`most-tested-issues.md`](most-tested-issues.md) part (c), worked as written.
  - Lunch.
  - At 13:45, `/quiz mixed 8` plus review.
  - Must-know tiers for your three weakest subjects.
  - Anki.
  - Stop by 18:00.
- **Drill / quiz:** `/quiz mixed 8` · `/drill <weakest subject> 8`.
- **/spot:** `/spot business-associations`.
- **Checklist (T−3):**
  - [ ] Exam files downloaded when the State Bar instructs.
  - [ ] Laptop restarted and Examplify tested.
  - [ ] Laptop charged; charger packed.

### Sun Jul 25 (T−2) · rest
- **Rest.** At most 30 minutes, only if it calms you: the one-page list in [`most-tested-issues.md`](most-tested-issues.md) part (c). No drills and no MBE.
- **Checklist (T−2):**
  - [ ] Admittance ticket printed, two copies (one stays in the car).
  - [ ] Physical government photo ID placed with the ticket.
  - [ ] Lunches planned for both days.
  - [ ] Up at 6:30 again tomorrow.

## The night before: Mon Jul 26 (PTO)

**Day.**
- At most 2–3 h of light review of the must-know lists ([`2027-W30`](../01-study-plan/weeks/2027-W30.md)).
- Take the pre-exam site visit if offered (2026: 2:00–4:00 p.m.) [VERIFY V-052].

**Evening, in order.**
1. **Pack the bag and put it by the door** ([`exam-day-logistics.md`](../09-exam-strategy/exam-day-logistics.md) §5):
   - [ ] printed ticket and physical ID, **inside** the bag;
   - [ ] laptop, charged, with the exam files downloaded;
   - [ ] charger;
   - [ ] clear bag with pens, foam earplugs and medication;
   - [ ] water bottle;
   - [ ] lunch and snacks;
   - [ ] layers;
   - [ ] car keys and a parking card.
2. **One page, 20 minutes at most:** your essay approach card ([`essay-method.md`](../09-exam-strategy/essay-method.md)) and your PT method card ([`method.md`](../04-performance-test/method.md)). Nothing new.
3. **Know the shape of Day 1** ([`time-management.md`](../09-exam-strategy/time-management.md)):
   - morning: Essays 1–3 (3 h);
   - afternoon: Essays 4–5 + PT (3.5 h).
   - Write each session's actual start time and your stop times on scratch paper.
4. **Timing.** Be seated by **8:20 a.m.**, so arrive at least 30 minutes early [S-003] [VERIFY V-055]. Arriving one hour or more after a session starts means you are refused admission [S-003].
5. Normal dinner. Set two alarms. Usual bedtime. A restless night is common and does not decide the exam ([`mindset-and-fatigue.md`](../09-exam-strategy/mindset-and-fatigue.md) §5).

## Between Day 1 and Day 2: Tue Jul 27 evening

1. **Answer files.**
   - After each session, exit Examplify as instructed and **do not open or change the answer files**; the bulletin's sanction is a zero for the session [S-003] [S-009].
   - Upload as soon as the instructions allow [VERIFY V-051] and keep the confirmation.
   - The deadline is about **noon PT Thu Jul 29** [VERIFY V-016]. A late upload costs 10 written scaled points [S-009].
2. **Let Day 1 go.** Do not discuss the questions, reread your answers or look anything up.
3. **Eat a proper dinner and take a short walk.**
4. **Warm-up: 30 minutes at most, then stop.** Choose one:
   - `/quiz mixed 10 1` (easy items);
   - your final weak-spot list;
   - the MBE-subject rows of [`mnemonics.md`](mnemonics.md) (#1–23 and #37–43).
5. **Pack for Day 2:**
   - [ ] ticket and ID;
   - [ ] clear bag with foam earplugs and medication;
   - [ ] non-mechanical soft-lead #2 pencils (2026: test centers do not provide them) and an eraser [S-003] [S-1736];
   - [ ] water, lunch, layers;
   - [ ] **no laptop needed.**
6. **MBE mechanics.**
   - Answers count only if they are on the Scantron, and **no extra time is given to transfer them** [S-003]. Bubble as you go.
   - Each session is 3 hours with no scheduled break [S-006]. Use the pacing checkpoints in [`05-mbe/strategy.md`](../05-mbe/strategy.md) §5.
   - Default rules: FRE only; pure comparative fault with joint and several liability; common-law felony murder with the agency rule; no California rules ([`mbe-vs-california-master-table.md`](mbe-vs-california-master-table.md)).
7. **Usual bedtime; up at 6:30.** Day 2 morning is the same routine as Day 1.

**After Day 2:** upload by the deadline if not done, then rest. Results are expected in late October or early November [S-012].
