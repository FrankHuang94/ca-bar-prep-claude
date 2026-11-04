---
subject: past-exams
topic: Past-exam frequency analysis (Feb 2012 – Jul 2026)
coverage_ids: []
tested_on: [essay, PT]
exam_frequency: {level: n/a, basis: "Analysis of 166 essays and 42 PTs across 31 administrations"}
last_verified: 2026-11-04
status: draft
---

# Past-exam frequency analysis

**Data.** Every California essay and PT the State Bar has published from **Feb 2012 to Jul 2026**:
- **31 administrations, 166 essays and 42 PTs**, indexed in [`index.csv`](index.csv) and [`../04-performance-test/past-pt-index.csv`](../04-performance-test/past-pt-index.csv). Each has an analysis file under `analyses/`.
- Through Feb 2017, each exam had 6 essays and 2 PTs (3-day format). From Jul 2017, 5 essays and 1 PT.
- The Feb 2025 retest booklet is indexed separately as `2025-03`.
- Subject labels follow the State Bar's own table of contents in each selected-answers booklet, which marks crossovers with a slash (e.g., "Wills and Trusts/Community Property") [S-079].

**Reliability.**
- 152 of 208 records are confirmed against State Bar text via search (subject and call); 54 are partial and 2 were not found.
- Issue tags were inferred from the calls and search summaries, not from reading the selected answers [VERIFY V-071].
- Subject-level counts are the most reliable layer. Issue-level counts are indicative only [VERIFY V-070].

## Key findings

1. **Professional Responsibility is near-certain.** It was a labelled subject on **30 of 31** exams (every exam since Jul 2015). It appears both alone and as a crossover (with Business Associations, Evidence, Community Property, Contracts, Criminal). Every PR call in recent years says to answer **"according to California and ABA authorities"**. Treat PR as a guaranteed essay and drill the CA-vs-ABA comparison until it is automatic.
2. **A second tier appears on about half of all exams:** Community Property (17/31), Contracts (16/31), Remedies (16/31), Criminal Law & Procedure (15/31) and Evidence (15/31). Remedies often rides along with another subject as a "what remedies are available?" call (Contracts, Torts, Con Law, BA).
3. **A third tier appears on about 40% of exams:** Business Associations (14/31), Real Property (13/31), Civil Procedure (13/31), Constitutional Law (13/31), Wills & Succession (13/31) and Torts (12/31). They are still expected; with five essays per exam, any of them can appear.
4. **Trusts is the least frequent labelled subject (7/31)** but the most common crossover partner of Wills: **Wills + Trusts (6)**. Study Wills and Trusts as one unit, often with Community Property (**CP + Wills: 4**).
5. **Most common crossover pairs:**
   - Wills + Trusts (6)
   - Contracts + Remedies (4)
   - Community Property + Wills (4)
   - Remedies + Torts (3)
   - then BA + PR, Evidence + PR, Criminal + Evidence (2 each)

   `08-high-yield/crossover-guide.md` (Phase 6) will cover how to organize each.
6. **No subject is "due".** Since 2017 no subject has been absent for more than a few administrations, and the State Bar does not rotate predictably. Use frequency to decide **emphasis and depth**, never to skip a subject.
7. **Since the two-day format (Jul 2017 onward, 100 essays):**
   - PR appears on 20 of 20 exams.
   - CP and Remedies on 11 each; Contracts, Criminal and Evidence on 10 each.
   - Torts on 9; BA, Con Law and Real Property on 8 each; Civ Pro and Wills on 7 each; Trusts on 3.

   Run `python scripts/frequency_analysis.py --since 2017-07 --stdout` for the full table.
8. **California law is explicit in the call.**
   - Community Property, Wills and Trusts calls say "according to California law".
   - Evidence calls name either the **California Evidence Code** or the **FRE**, and switch between exams, so read the call first.
   - PR calls say "California and ABA authorities".
   - The recent Civil Procedure essays whose forum was visible (Jul 2021, Feb 2023) were set in federal court; the California CCP comparison is still in scope [S-084].
9. **PT tasks seen:**
   - objective memos (10 identified);
   - persuasive briefs or points and authorities (5);
   - closing arguments (3);
   - client or advice letters (3);
   - a demand or persuasive letter to opposing counsel;
   - one draft oral argument;
   - 16 tasks not yet determined.

   PT Libraries often cover law **outside** the 13 subjects: arbitration, nonprofit governance, wage-and-hour, platform immunity, attorney discipline. That confirms the PT tests method, not memorized law (`../04-performance-test/method.md`).

## What this changes in the plan
- **More PR essays.** The essay slots in `01-study-plan/schedule.yml` were re-weighted toward PR (about one PR or PR-crossover essay a week from April), Community Property and Remedies.
- **Wills + Trusts + CP are studied and practised together** (W10 first pass; W22 second pass).
- **Subject READMEs** now carry an `exam_frequency` level based on this table: **high** = MBE subject or on ≥ 45% of essays; **med** = 35–45%; **low** = < 35%.
- **New coverage rows from past essays:** `BUS-PAST-001` (insider loans and equitable subordination, Feb 2017 Q4) and `WIL-PAST-001` (conservatorship effects on testamentary gifts, Feb 2015 Q6). Every other tagged issue mapped to an existing row.

## Caveats
- Frequency is about **emphasis, not prediction**. Every subject on the scope list remains testable [S-041].
- PR issues embedded in another subject's question are counted only when the State Bar's label includes PR, so the counts may slightly undercount PR.
- Question numbers for a few items were inferred by elimination: Jul 2012 Q5/Q6, Jul 2013 Q6, Jul 2014 Q4. A few search summaries conflicted on numbering: Feb 2020 Q1, Feb 2022 Q4/Q5, Feb 2025 Q3/Q4. These affect issue tags, not the subject totals.

## Generated tables
<!-- BEGIN GENERATED-FREQUENCY -->
_Generated by `scripts/frequency_analysis.py` on 2026-11-04 from 166 essay questions across 31 administrations (2012-02 → 2026-07)._

> Past frequency is a guide to emphasis, not a prediction. Every subject on the scope list remains testable.

### Subject totals and recency

| Subject | Essays tested | Share of essays | Administrations with subject | Last tested | Administrations since |
|---|---|---|---|---|---|
| Professional Responsibility | 30 | 18% | 30/31 | 2026-07 | 0 |
| Community Property | 17 | 10% | 17/31 | 2026-07 | 0 |
| Contracts | 17 | 10% | 16/31 | 2026-02 | 1 |
| Remedies | 17 | 10% | 16/31 | 2026-07 | 0 |
| Criminal Law and Procedure | 15 | 9% | 15/31 | 2026-07 | 0 |
| Evidence | 15 | 9% | 15/31 | 2026-07 | 0 |
| Business Associations | 14 | 8% | 14/31 | 2026-07 | 0 |
| Real Property | 14 | 8% | 13/31 | 2026-02 | 1 |
| Civil Procedure | 13 | 8% | 13/31 | 2026-02 | 1 |
| Constitutional Law | 13 | 8% | 13/31 | 2025-07 | 2 |
| Torts | 13 | 8% | 12/31 | 2025-07 | 2 |
| Wills and Succession | 13 | 8% | 13/31 | 2026-07 | 0 |
| Trusts | 7 | 4% | 7/31 | 2025-07 | 2 |

### Heatmap (essays per administration; ■ = 1, ■■ = 2)

| Subject | '12-2 | '12-7 | '13-2 | '13-7 | '14-2 | '14-7 | '15-2 | '15-7 | '16-2 | '16-7 | '17-2 | '17-7 | '18-2 | '18-7 | '19-2 | '19-7 | '20-2 | '20-10 | '21-2 | '21-7 | '22-2 | '22-7 | '23-2 | '23-7 | '24-2 | '24-7 | '25-2 | '25-3 | '25-7 | '26-2 | '26-7 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PRF | ■ | ■ | ■ | ■ | ■ | ■ | · | ■ | ■ | ■ | ■ | ■ | ■ | ■ | ■ | ■ | ■ | ■ | ■ | ■ | ■ | ■ | ■ | ■ | ■ | ■ | ■ | ■ | ■ | ■ | ■ |
| CMP | · | ■ | · | ■ | ■ | ■ | · | ■ | · | ■ | · | ■ | ■ | ■ | ■ | · | · | · | ■ | · | ■ | ■ | · | · | ■ | · | · | ■ | · | ■ | ■ |
| CTR | · | ■ | · | ■ | · | ■ | ■ | · | ■■ | ■ | · | ■ | ■ | ■ | · | ■ | ■ | · | ■ | · | · | ■ | · | ■ | ■ | · | · | · | · | ■ | · |
| REM | · | · | ■ | ■ | ■ | · | ■ | · | ■ | · | ■ | ■ | · | · | · | ■ | ■ | ■ | · | · | ■■ | · | · | ■ | · | ■ | ■ | ■ | · | · | ■ |
| CRM | · | ■ | ■ | · | · | ■ | · | ■ | · | · | ■ | · | ■ | · | · | ■ | · | ■ | · | ■ | ■ | · | · | ■ | ■ | · | ■ | · | ■ | · | ■ |
| EVD | ■ | ■ | · | · | · | ■ | · | · | ■ | · | ■ | ■ | · | ■ | ■ | · | ■ | · | ■ | · | ■ | · | ■ | · | ■ | · | · | ■ | · | · | ■ |
| BUS | ■ | · | ■ | · | · | ■ | ■ | ■ | · | · | ■ | · | · | · | · | · | ■ | ■ | · | · | ■ | ■ | · | ■ | · | ■ | · | · | ■ | · | ■ |
| PRP | ■ | · | · | · | ■ | · | ■ | ■■ | · | ■ | · | · | ■ | · | ■ | · | · | ■ | ■ | · | · | · | ■ | · | · | ■ | ■ | · | · | ■ | · |
| CIV | · | ■ | ■ | · | ■ | · | ■ | ■ | · | ■ | · | ■ | · | · | ■ | ■ | · | · | · | ■ | · | · | ■ | · | · | ■ | · | · | · | ■ | · |
| CON | ■ | · | · | ■ | ■ | · | · | ■ | · | ■ | · | · | ■ | ■ | · | ■ | · | · | · | · | · | ■ | ■ | · | ■ | · | · | ■ | ■ | · | · |
| TRT | · | · | ■ | · | · | ■ | · | · | ■ | · | ■ | ■ | · | · | ■ | · | ■ | · | · | ■ | ■ | · | · | ■■ | · | ■ | · | · | ■ | · | · |
| WIL | ■ | ■ | · | ■ | · | · | ■ | · | ■ | · | ■ | · | ■ | · | ■ | · | · | ■ | · | ■ | · | ■ | · | · | · | · | ■ | · | · | · | ■ |
| TRS | ■ | · | · | ■ | · | · | ■ | · | ■ | · | · | · | · | · | ■ | · | · | · | · | · | · | · | · | · | · | · | ■ | · | ■ | · | · |

### Most-tested issues by subject

**Professional Responsibility**
- PRF-SUP-004 — Duty of loyalty: conflicts of interest (current clients, former clients, imputat — 12×
- PRF-CBX-III — III. [Lawyer as advocate] (incl. candor to tribunal; fairness to opposing party  — 8×
- PRF-SUP-003 — Duty of confidentiality vs. attorney-client privilege and work product; exceptio — 8×
- PRF-SUP-001 — California Rules of Professional Conduct vs. ABA Model Rules: compare and contra — 8×
- PRF-SUP-005 — Competence, diligence and communication — 6×
- PRF-CBX-I.x2 — Fees (fee agreements; unconscionable fees; contingent fees; referral fees) — 6×
- PRF-CBX-I — I. [Client-lawyer relationship] (scope of representation; conflicts of interest; — 5×
- PRF-CBX-I.x1 — Scope of representation and allocation of authority — 3×

**Community Property**
- CMP-CBX-II.A — Presumptions (general community property presumption; presumptions based on titl — 5×
- CMP-CBX-III.A — A. General rules (equal management; fiduciary duties; gifts; real property incl. — 4×
- CMP-CBX-I.B.x3 — Quasi-community property — 4×
- CMP-CBX-I.B.x2 — Separate property — 3×
- CMP-CBX-II — II. Characterization of property — 3×
- CMP-CBX-II.B — Agreements that alter characterization (premarital agreements; transmutation) — 3×
- CMP-CBX-VI.debts — [Allocation of debts and liabilities] Property liable for debts: a. Premarital d — 2×
- CMP-CBX-V.A — A. Determining date of separation — 2×

**Contracts**
- CTR-MBE-V.A — Expectation interest (direct, incidental, and consequential damages) — 7×
- CTR-MBE-IV.C — Breach (material and partial breach; anticipatory repudiation) [exact wording/su — 5×
- CTR-CBX-I — I. Introductory principles/applicable law (types of agreements: sale of goods vs — 5×
- CTR-MBE-I.A — Mutual assent (offer and acceptance; unilateral, bilateral, and implied-in-fact  — 3×
- CTR-MBE-V.F — Specific performance and injunction — 2×
- CTR-MBE-V.E — Rescission and reformation — 2×
- CTR-MBE-IV.E — Express and implied warranties in sale-of-goods contracts — 2×
- CTR-MBE-V.G — Reliance and restitution interests — 1×

**Remedies**
- REM-CBX-IV — IV. Equitable remedies (injunctions; specific performance; reformation; rescissi — 8×
- REM-CBX-II — II. Legal remedies (damages, incl. measurement for contract and real property cl — 5×
- REM-CBX-I — I. Basic principles (legal vs. equitable remedies; classification of remedies) — 4×
- REM-CBX-III.b — Equitable restitutionary remedies: constructive and resulting trusts; equitable  — 3×
- REM-CBX-V — V. Equitable defenses (laches; unclean hands; in pari delicto; estoppel; undue h — 3×
- REM-SUP-001 — Provisional relief: temporary restraining orders and preliminary injunctions — 3×
- REM-CBX-VI — VI. Declaratory remedies (declaratory judgments; reformation; nominal damages) — 1×
- REM-CBX-III — III. [numeral not displayed; restitution block] Purpose of restitution — 1×

**Criminal Law and Procedure**
- CRM-MBE-V.A — Arrest, search and seizure — 9×
- CRM-MBE-V.B — Confessions and privilege against self-incrimination — 4×
- CRM-MBE-III.A.1 — Attempts — 3×
- CRM-MBE-III.A.2 — Conspiracy — 2×
- CRM-MBE-II.A — Theft and receiving stolen goods — 2×
- CRM-MBE-V.E — Fair trial and guilty pleas — 2×
- CRM-MBE-IV.E — Justification and excuse — 2×
- CRM-MBE-II.B — Robbery — 2×

**Evidence**
- EVD-MBE-V.A.1 — What is hearsay — 3×
- EVD-MBE-V.A.3 — Statements attributable to party-opponent — 2×
- EVD-MBE-IV.A — Requirement of original — 2×
- EVD-SUP-001 — Federal Rules of Evidence vs. California Evidence Code: compare and contrast — 2×
- EVD-MBE-V.F — Business records — 2×
- EVD-CBX-I — I. Presentation of evidence — 2×
- EVD-MBE-III.B — Attorney-client and work product — 2×
- EVD-CBX-hs — Hearsay and exceptions — 2×

**Business Associations**
- BUS-CBX-II — II. General Partnerships (formation incl. partnership by estoppel; partner liabi — 4×
- BUS-CBX-V.D.3 — Fiduciary duties - care and loyalty (V.D.3) — 4×
- BUS-CBX-V.A.2 — Piercing the corporate veil (V.A.2) — 3×
- BUS-CBX-V.C — C. Formation — 3×
- BUS-CBX-V — V. Corporations — 3×
- BUS-CBX-I — I. Agency (formation; principal-agent relationship; termination; contract liabil — 3×
- BUS-CBX-V.x — Closely held corporations; non-profit corporations — 2×
- BUS-CBX-V.E.5 — Derivative actions (V.E.5) — 2×

**Real Property**
- PRP-MBE-I.B.1 — Types: tenancy in common and joint tenancy — 3×
- PRP-MBE-V.D.1 — Recording acts (types of recording acts, indexes, chain of title) [wording/numbe — 3×
- PRP-MBE-I.C.3 — Transfers by landlord or tenant [number inferred] — 2×
- PRP-MBE-I.B.2 — Rights and obligations of cotenants [search output also mentions partition and s — 2×
- PRP-MBE-I.C.2 — Possession and rent [number inferred] — 2×
- PRP-MBE-I.C.4 — Termination (including surrender, mitigation of damages, anticipatory breach, an — 2×
- PRP-MBE-II.B.2 — Methods of creation (express, implied, prescription) [may carry lettered sub-ite — 2×
- PRP-MBE-II.D.2 — Protection of pre-existing property rights — 1×

**Civil Procedure**
- CIV-MBE-I.A — Federal subject-matter jurisdiction (federal question, diversity, supplemental,  — 7×
- CIV-MBE-III.E — Discovery (including e-discovery), disclosure, and sanctions — 5×
- CIV-MBE-I.B — Personal jurisdiction — 3×
- CIV-MBE-V.A — Pretrial motions, including motions addressed to face of pleadings, motions to d — 2×
- CIV-MBE-IV.A — Right to jury trial — 2×
- CIV-MBE-I.C — Service of process and notice — 2×
- CIV-MBE-I.D — Venue, forum non conveniens, and transfer — 2×
- CIV-MBE-III.A — Preliminary injunctions and temporary restraining orders — 1×

**Constitutional Law**
- CON-MBE-I.C.1 — The "case or controversy" requirement, including the prohibition on advisory opi — 4×
- CON-MBE-IV.D — Takings — 2×
- CON-MBE-IV.F.1.a — Free exercise — 2×
- CON-MBE-IV.F.2.e — Regulation of, or impositions upon, public school students, public employment, l — 2×
- CON-MBE-IV.C — Equal protection — 2×
- CON-MBE-III.B.1 — Negative implications of the commerce clause — 2×
- CON-MBE-IV.E — Other protections, including the privileges and immunities clauses, the contract — 2×
- CON-MBE-IV.F.2 — Freedom of expression — 1×

**Torts**
- TRT-CBX-I.x3 — Intentional torts to property (trespass to land; trespass to chattel; conversion — 4×
- TRT-MBE-IV.C — Claims based on misrepresentations, and defenses — 3×
- TRT-MBE-II — Negligence — 3×
- TRT-MBE-I.A — Harms to the person, such as assault, battery, false imprisonment, and inflictio — 3×
- TRT-MBE-II.F.2 — Independent contractors and nondelegable duties — 2×
- TRT-MBE-IV.B — Claims based on defamation and invasion of privacy, defenses, and constitutional — 2×
- TRT-MBE-IV.A — Claims based on nuisance, and defenses — 2×
- TRT-MBE-III — Strict liability and products liability: common law strict liability, including  — 2×

**Wills and Succession**
- WIL-CBX-IV.x — Witnessed wills; holographic wills; extrinsic evidence; witnesses; choice of law — 4×
- WIL-CBX-VIII — VIII. Omitted children (born or adopted after execution; denial of share; manner — 3×
- WIL-CBX-VII — VII. Omitted spouses (share of spouse married after execution; circumstances whe — 3×
- WIL-CBX-VI — VI. Revocation and revival of wills — 2×
- WIL-CBX-II.E — E. Adopted children — 2×
- WIL-CBX-I — I. General provisions (CP/QCP at death; recapture by surviving spouse; spouse's  — 2×
- WIL-PAST-001 — Conservatorship effects on testamentary gifts (conservator's acts; ademption/aba — 1×
- WIL-CBX-interp.x — Changes occurring after execution — 1×

**Trusts**
- TRS-CBX-I.J — J. Modification and termination of trust — 2×
- TRS-CBX-IX — IX. Trustee liability to beneficiary — 2×
- TRS-SUP-003 — Charitable trusts and cy pres — 2×
- TRS-CBX-V — V. Duties of trustee (standard of care; loyalty; prudent investing; self-dealing — 2×
- TRS-CBX-I.x — Definition; required parties; creation of a valid trust / valid trust purposes;  — 1×
- TRS-SUP-001 — Revocability of trusts: California default rule vs. majority rule; methods of re — 1×
- TRS-CBX-VIII — VIII. Remedying breach of trust — 1×
- TRS-CBX-XI — XI. Trust or trustee liability to third party — 1×

### Crossover pairs

| Pair | Times |
|---|---|
| Trusts + Wills and Succession | 6 |
| Contracts + Remedies | 4 |
| Community Property + Wills and Succession | 4 |
| Remedies + Torts | 3 |
| Business Associations + Professional Responsibility | 2 |
| Evidence + Professional Responsibility | 2 |
| Criminal Law and Procedure + Evidence | 2 |
| Community Property + Professional Responsibility | 1 |
| Constitutional Law + Real Property | 1 |
| Contracts + Professional Responsibility | 1 |
| Community Property + Trusts | 1 |
| Civil Procedure + Evidence | 1 |
| Constitutional Law + Remedies | 1 |
| Real Property + Wills and Succession | 1 |
| Business Associations + Remedies | 1 |

### Performance Tests

| Task type | Count |
|---|---|
| undetermined | 16 |
| objective-memo | 10 |
| persuasive-brief | 5 |
| other | 4 |
| closing-argument | 3 |
| client-letter | 3 |
| demand-letter | 1 |
<!-- END GENERATED-FREQUENCY -->
