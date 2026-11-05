---
subject: progress
topic: Phase 8 maintenance log (monthly cycles)
coverage_ids: []
tested_on: [none]
exam_frequency: {level: n/a, basis: "Process record"}
last_verified: 2026-11-05
status: verified
---

# Maintenance log

Each month, run `/monthly-maintenance` (`.claude/commands/monthly-maintenance.md`). It covers:
1. `/update-exam-intel`;
2. the dashboard;
3. question-bank expansion where `scripts/bank_targets.py` shows weak areas;
4. VERIFY burn-down;
5. status update;
6. a new entry here.

The **June 2027 sweep** (`00-exam-intel/recent-changes.md` §10) is the last full check before the exam.

## Cycle 1 — November 2026 (2026-11-05)

### Plan impacts
- **No date moved.** The July 2027 application deadlines are fixed by rule:
  - timely: **Thu Apr 1, 2027**;
  - final: **Tue Jun 1, 2027** (also the accommodations deadline).

  "(est)" has been removed from the checklist, `config/plan.yml` and weeks W13 and W22. The July 2027 exam page is not posted yet, so the other July dates stay estimates (V-016).
- **Fees unchanged** (June 2026 Appendix A).
- **Your action: register with the State Bar now.** The 90-day law-student registration rule also covers foreign-educated general applicants, and you are past 90 days into the LL.M. (`00-exam-intel/admissions-checklist.md` §3, V-019).
- **Exam day.** Bring your own non-mechanical #2 pencils to the MBE. Notes in the MBE question book are allowed. Packing lists are updated.

### Law changes found and applied
| Change | Subject | Marking |
|---|---|---|
| *Enbridge Energy v. Nessel* (2026): the 30-day removal deadline is nonjurisdictional but cannot be equitably tolled | Civ Pro | Apply |
| *Fuentes v. Empire Nissan* (Cal. 2026): fine print goes only to procedural unconscionability | Contracts (CA) | Apply |
| AB 628: working stove and refrigerator added to Civ. Code § 1941.1 (leases from Jan 1, 2026) | Real Property (CA) | Apply (low) |
| *Landor*: no RLUIPA individual-capacity damages | Con Law | Apply (low) |
| *Chevron v. Plaquemines*, *Pitts*, *Ellingburg*: now confirmed from the opinions (V-034 closed) | Civ Pro, Evidence, Crim, Con Law | Apply (low) |
| *FCC v. AT&T*; the CRPC AI comment amendments; *Li v. ArcSoft* (V-1040); *Sanchez v. Rojas* (V-604) | Civ Pro / Con Law; PR; BA; Torts | Watch |
| AB 931 details, AB 2199, AB 1297, AB 1134, AB 515, *J.O. v. Superior Court* | various | Low |

No 2026-session change was found to the CCP, the Evidence Code, the Family Code community-property sections, the Corporations Code or the Penal Code (V-1020 keeps a June 2027 re-check).

### VERIFY burn-down
| | Before (end of Phase 7) | After cycle 1 |
|---|---|---|
| Open | 283 | **267** (11 High, 66 Med, 190 Low) |
| Resolved | 123 | **144** |
| Sources | 734 | **820** |

**Rule substance corrected this cycle**, to re-learn if you have already studied them:

*Wills and Trusts*
- **R-WIL-013:** the § 259 exception applies if the decedent later became substantially able to manage his or her finances and resist undue influence.
- **R-WIL-088:** the court may exempt a specific gift from abatement only where pro rata abatement would defeat the decedent's obvious intention.
- **R-WIL-017:** a putative spouse also inherits from separate property (*Estate of Leslie*).
- **R-TRS-007:** a trustee vacancy is filled under the instrument, then by a trust company, then by the court.
- **R-TRS-081 (outline IX):** § 16441 interest is the greater of the legal rate or the interest actually received.

*Contracts, Torts, Criminal and Real Property*
- **R-CTR-061 / R-TRT-089:** California enacted no UCC § 2-318, so case-law privity applies.
- **R-CRM-023:** imperfect self-defense is also barred where the defendant's felony created the circumstances.
- **R-CRM-043:** § 189(f) requires no malice.
- **R-PRP-046 (Tenant Protection Act):** the 15-year exemption runs from the certificate of occupancy; relocation assistance is one month's rent.

*Business Associations and Remedies*
- **R-BUS-065:** after disinterested board approval, the challenger bears the § 310 burden.
- **R-REM-071:** a California seller may get specific performance (*Laske*).
- **R-REM-078:** proof beyond a reasonable doubt for punitive contempt (*Mitchell*).

### Question bank
`bank_targets.py`: **no attempts are logged yet**, so there is no weak-area signal and no expansion this cycle. Of each MBE subject's 150 MCQs, about 85 are reserved for the three simulations and about 65 are free for practice. Licensed questions fill the rest; log them with `quiz.py log --source official --coverage <row>` so they count toward weak-area detection.

### Copyright audit (closing the Phase 7 item)
All six checks pass:
1. committed files;
2. long quotations;
3. past-question fidelity (26 essays and all 8 PTs);
4. MCQ sources;
5. mnemonics;
6. attribution.

One mnemonic label was corrected. Borderline: the coverage matrix reproduces official outline headings. That is fine for private study; paraphrase them before any public sharing. Details are in `qa-report-phase7.md` §6.

### Tooling added
- `scripts/bank_targets.py`, with a test.
- The `/monthly-maintenance` command.

### Needs you
- Register with the State Bar (above).
- Ask Cardozo when the final transcript will be issued (V-015).
- Start logging attempts in December so next month's cycle can target weak areas.
