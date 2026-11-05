---
subject: high-yield
topic: Crossover essay guide — how the tested subject pairs interlock, with answer skeletons
coverage_ids: []
tested_on: [essay]
exam_frequency: {level: high, basis: "31 of the 166 indexed essays (2012-02 to 2026-07) carried two or more subject labels; pair counts from 06-past-exams/frequency-analysis.md and index.csv"}
last_verified: 2026-11-05
status: draft
---

# Crossover essay guide

**Why this matters.** About **1 essay in 5** on past California exams carried two subject labels (31 of 166, Feb 2012 – Jul 2026). The State Bar marks them with a slash ("Wills and Trusts/Community Property"). A crossover is graded like any essay: answer **each call**, in order, with a conclusion for every issue. The danger is spending 50 minutes on the subject you know best.

**How to use each entry.** *Triggers* tell you which fact switches on which subject. The *skeleton* is the heading order to type into your answer before you write. The *rules* are the 3–5 rule IDs you will almost certainly need (full text in each subject's `rule-statements.md`). *Traps* are the mistakes that cost the most points. *Bank* links go to the repo's own crossover essays.

**Simulation essays.** E-XO-003 (SIM-02), E-XO-012 and E-XO-021 (SIM-01), and E-XO-022 and E-XO-027 (SIM-03) are held back by `python scripts/quiz.py reserved`. They are marked **(simulation — do not open before sitting it)**.

Past-exam references come from [`../06-past-exams/index.csv`](../06-past-exams/index.csv). Issue descriptions are index-level, inferred from the calls [VERIFY V-071].

## The general method (from `essay-method.md` §7)

1. **Organize by the call, not by the subject list in your head.** One heading per numbered call.
2. **Split your minutes by call** in the outline (e.g., 30 / 25 / 5).
3. **Threshold issues first:** a will's validity before its gifts; characterization before distribution; liability before remedies.
4. **Ethics last** unless the call puts it first: a separate "Professional Responsibility" part, lawyer by lawyer, duty by duty, ABA then California.
5. **Watch for the second subject changing the first** (e.g., community-property character limits what a will can give).

See [`../09-exam-strategy/essay-method.md`](../09-exam-strategy/essay-method.md) and the governing-law table in [`mbe-vs-california-master-table.md`](mbe-vs-california-master-table.md) §1.

## Index of tested pairs

| # | Pair | Times | Past essays | Bank essays |
|---|---|---|---|---|
| 1 | Wills + Trusts | 6 | Feb 2012 Q1; Jul 2013 Q5; Feb 2015 Q6; Feb 2016 Q1; Feb 2019 Q1 (with CP); Feb 2025 Q2 | E-XO-001, E-XO-014 |
| 2 | Contracts + Remedies | 4 | Feb 2016 Q4; Jul 2017 Q3; Feb 2020 Q3; Jul 2023 Q5 | E-XO-015; E-XO-003 (simulation) |
| 3 | Community Property + Wills | 4 | Feb 2018 Q5; Feb 2019 Q1; Jul 2022 Q5; Jul 2026 Q2 | E-XO-002, E-XO-016 |
| 4 | Torts + Remedies | 3 | Feb 2017 Q2; Feb 2022 Q3; Jul 2024 Q5 | E-XO-004, E-XO-017 |
| 5 | Business Associations + PR | 2 | Jul 2014 Q3; Jul 2015 Q5 | E-XO-005, E-XO-018 |
| 6 | Evidence + PR | 2 | Jul 2017 Q2; Feb 2022 Q4 | E-XO-006, E-XO-019 |
| 7 | Criminal + Evidence | 2 | Feb 2024 Q4; Jul 2026 Q5 | E-XO-007, E-XO-020 |
| 8 | Community Property + PR | 1 | Jul 2012 Q2 | E-XO-008; E-XO-022 (simulation) |
| 9 | Con Law + Real Property | 1 | Jul 2015 Q6 | E-XO-009 |
| 10 | Contracts + PR | 1 | Feb 2018 Q1 | E-XO-021 (simulation) |
| 11 | Community Property + Trusts | 1 | Feb 2019 Q1 (with Wills) | E-XO-011 |
| 12 | Civil Procedure + Evidence | 1 | Feb 2019 Q4 | E-XO-010 |
| 13 | Con Law + Remedies | 1 | Jul 2019 Q2 | none in the bank |
| 14 | Real Property + Wills | 1 | Oct 2020 Q3 | E-XO-012 (simulation) |
| 15 | Business Associations + Remedies | 1 | Feb 2022 Q5 | E-XO-013 |

Two more one-time pairs appear in `index.csv` but fall below the generated top-15 table: **BA + Torts** (Jul 2023 Q1) and **Criminal + PR** (Jul 2025 Q5). See the end of this file.

---

## 1. Wills + Trusts (6 times — the most common pair)

**Governing law.** Wills: California. Trusts: read the call; if silent, general rule plus the Probate Code section [VERIFY V-550].

**Triggers.**
- Will leaves property "to the trustee of my trust" → pour-over (§ 6300).
- Signed note, letter or later will changing the trust → revocation / amendment methods; *Haggerty*.
- Gift to the lawyer who drafted, or to a caregiver → disqualified donee (§ 21380) in either instrument.
- Charity's purpose fails or is impractical → cy pres.
- Trustee invests, sells, hires a relative or takes a gift → trustee duties and remedies.
- Child born or spouse married after both instruments → omitted heir reaching the trust (§ 21601; R-TRS-077).

**Skeleton.**
```text
I.   Inventory: what passes outside probate (funded trust, JT, POD) vs. by will
II.  The will: execution (attested / holographic / harmless error); pour-over (§ 6300)
III. The trust: valid? revocable (§ 15400)? amended or revoked — which version controls?
IV.  Gifts inside both instruments: § 21380 disqualified donees; undue influence; no-contest clause
V.   Trustee: duties breached → remedies (surcharge, removal, constructive trust)
VI.  Distribution, claimant by claimant
```

**Rules most often needed.** R-WIL-061 (pour-over, trust within 60 days) · R-TRS-011 to R-TRS-014 (revocable default; statutory method; no revocation by will; amendment under *Haggerty*) [VERIFY V-033] · R-WIL-095 / R-TRS-076 (disqualified donees) · R-TRS-021 (cy pres) · R-TRS-052, R-TRS-053 (loyalty; self-dealing).

**Traps.**
- Writing the traditional "irrevocable unless reserved" rule as the answer. California: revocable unless expressly irrevocable.
- Letting a later will revoke or amend a living trust. The statutory method needs a writing **other than a will** delivered to the trustee.
- Treating an instrument's amendment clause as exclusive when it does not say so **explicitly**.
- Forgetting that funded trust property never enters the probate estate.

**Bank.** [E-XO-001](../07-question-bank/essays/crossover/E-XO-001.md) (pour-over, *Haggerty*, drafter-trustee gift, trustee breaches) · [E-XO-014](../07-question-bank/essays/crossover/E-XO-014.md) (capacity, undue influence, care-custodian gift, no-contest clause, spendthrift and support exceptions).

---

## 2. Contracts + Remedies (4 times)

**Governing law.** General principles: common law or UCC Article 2. Add the California sentences (§ 3387, § 1671, *IT Corp.*) only where they change the result.

**Triggers.**
- One-of-a-kind goods (an antique, a chess piece) → specific performance under UCC 2-716, often with a **TRO and preliminary injunction** against resale.
- Land → specific performance; Civ. Code § 3387.
- Artist, performer or employee walks out → no specific performance; negative injunction (R-REM-064).
- Misrepresentation, mistake or a mis-typed writing → rescission and restitution, or reformation.
- Liquidated-damages clause or forfeited deposit → penalty analysis; restitution for the breaching party (R-CTR-109).

**Skeleton.**
```text
I.   Governing law (UCC vs. common law) — one line
II.  Breach: material? repudiation? who breached first?
III. Damages: expectation (+ incidental, consequential), certainty, mitigation; liquidated-damages clause
IV.  Restitution (non-breaching party; breaching party's deposit)
V.   Equitable relief: specific performance (contract, conditions, inadequate remedy, feasibility, defenses)
     or rescission / reformation
VI.  Provisional relief if asked: TRO → preliminary injunction (likelihood, harm, balance, bond)
VII. Election of remedies; best remedy
```

**Rules most often needed.** R-CTR-089 (expectation damages) · R-REM-070 / R-REM-071 / R-REM-072 (SP elements; land; unique goods) · R-REM-066, R-REM-067 (preliminary injunction: *Winter*, *IT Corp.*) · R-REM-043, R-REM-075 (rescission; reformation) · R-CTR-096 (liquidated damages; § 1671(b)).

**Traps.**
- Skipping "inadequate legal remedy" before specific performance; that step is the heart of the SP analysis.
- Forgetting the **bond** for a TRO or preliminary injunction.
- Ordering specific performance of personal services.
- Recovering both expectation damages and full restitution: say which remedy the plaintiff should elect.

**Bank.** [E-XO-015](../07-question-bank/essays/crossover/E-XO-015.md) (construction repudiation, liquidated damages, reliance, breaching party's restitution) · [E-XO-003](../07-question-bank/essays/crossover/E-XO-003.md) **(simulation — do not open before sitting it)**.

---

## 3. Community Property + Wills (4 times)

**Governing law.** California for both; the call says so.

**Triggers.**
- "Moved to California from State X" → quasi-community property (R-CMP-003).
- Land in State X → at death **not** QCP; situs law governs.
- Decedent put QCP into joint tenancy with a child, or kept control of it → recapture (Prob. Code § 102).
- Will "gives our house" or other assets the survivor half-owns → equitable election (R-CMP-095).
- Marriage after the will → omitted spouse; no will → spouse's intestate share.
- Will witnessed oddly or signed in another state → § 6110 / § 6113 (R-WIL-047, R-WIL-048, R-WIL-053).

**Skeleton.**
```text
Intro: CA is a CP state; at death survivor keeps half of CP and half of decedent's QCP;
       decedent can will only SP + half CP + half own QCP (Prob. Code §§ 100, 101, 6101)
I.   Validity of the will (if challenged)
II.  Characterize each asset (domicile at acquisition; presumptions; title; transmutation)
III. Effect of death on each asset (QCP definition at death; § 102 recapture; nonprobate transfers)
IV.  Distribution: under the will (election?) or intestacy (§ 6401); omitted spouse / child
V.   Each claimant's total
```

**Rules most often needed.** R-CMP-091 / R-WIL-001 (testamentary power) · R-CMP-092 (QCP at death; out-of-state land) · R-CMP-093 (§ 102 recapture) · R-WIL-086 (omitted spouse's share) · R-WIL-016 / R-CMP-094 (spouse's intestate share).

**Traps.**
- Using the **dissolution** definition of QCP (land "wherever situated") at **death**. At death, out-of-state land is outside QCP (Prob. Code § 66).
- Splitting the **survivor's own** QCP. Only the decedent's QCP is divided.
- Letting the will pass the survivor's half of CP.
- Writing "elective share". California has none.

**Bank.** [E-XO-002](../07-question-bank/essays/crossover/E-XO-002.md) (will validity under § 6113; QCP; out-of-state cabin; omitted spouse) · [E-XO-016](../07-question-bank/essays/crossover/E-XO-016.md) (§ 102 recapture; POD account; equitable election; omitted child).

---

## 4. Torts + Remedies (3 times)

**Governing law.** General principles, plus the California remedy sentences (§ 3294, § 3343, § 3346).

**Triggers.**
- Continuing noise, odor or runoff from a neighbor → nuisance (R-TRT-092), then an injunction with balancing.
- A structure over the line → trespass; removal vs. relative hardship / equitable easement (R-REM-061).
- Lies in a sale → fraud: damages measure (out-of-pocket vs. benefit of the bargain), rescission.
- Chattel taken, sold or held → conversion or trespass to chattels (R-TRT-007, R-TRT-008); replevin (R-REM-041); constructive trust over proceeds.
- Deliberate or spiteful conduct → punitive damages.

**Skeleton.**
```text
I.   Liability: one paragraph per tort, with defenses (conclusion for each)
II.  Damages: measure per tort; limits (causation, certainty, mitigation); punitive (§ 3294)
III. Restitution: disgorgement; replevin / ejectment; rescission; constructive trust and tracing
IV.  Injunction: inadequate remedy, property interest, feasibility, balancing, defenses; tailoring
V.   Best remedy / election
```

**Rules most often needed.** R-REM-024 (nuisance damages: permanent vs. continuing) · R-REM-023 (fraud damages; § 3343) · R-REM-028 (§ 3294 punitive damages) · R-REM-055 / R-REM-062 (permanent injunction; nuisance injunction alternatives) · R-REM-044 (constructive trust).

**Traps.**
- Calling noise or odor a trespass. California treats it as nuisance unless there is physical damage or deposit (R-TRT-006).
- Forgetting the punitive-damages predicates: actual damages and evidence of D's financial condition (R-REM-030).
- Choosing an equitable remedy without explaining why damages are inadequate.

**Bank.** [E-XO-004](../07-question-bank/essays/crossover/E-XO-004.md) (nuisance, trespass, culvert encroachment, injunction balancing) · [E-XO-017](../07-question-bank/essays/crossover/E-XO-017.md) (conversion, replevin, TRO, constructive trust and tracing, punitive damages).

---

## 5. Business Associations + Professional Responsibility (2 times)

**Governing law.** BA: general principles plus a Corporations Code sentence [VERIFY V-700]. PR: California and ABA.

**Triggers.**
- Lawyer is also a director, officer, partner or investor → business transaction with a client; personal-interest conflict.
- Lawyer learns that an officer is breaking the law → organization as client; reporting up vs. out.
- One lawyer for the company and its CEO (or for both sides of a derivative dispute) → joint representation.
- Lawyer trades on client information → insider trading (misappropriation, R-BUS-091) plus loyalty and confidentiality (R-PRF-019).
- Firm set up with a nonlawyer, or as a California LLC → fee sharing and UPL (R-PRF-080, R-PRF-082), entity limits.

**Skeleton.**
```text
Part 1 — BA (per call): entity type and liability; directors' / partners' duties; remedies
Part 2 — PR, lawyer by lawyer:
   1. Who is the client? (organization, not its officers)
   2. Conflicts (written consent in CA); business transactions (1.8.1 / MR 1.8(a))
   3. Confidentiality; reporting up (both) / reporting out (ABA only)
   4. Other duties raised (competence, fees, 5.4)
```

**Rules most often needed.** R-BUS-109 (the lawyer for the organization) · R-PRF-055, R-PRF-056 (reporting up; reporting out differs) · R-PRF-026 (business transactions, stock for fees) · R-PRF-024 (joint representation of entity and constituent) · R-BUS-065 (§ 310 when the lawyer-director is interested).

**Traps.**
- Treating the CEO as the client.
- Approving reporting out under California law. It violates rule 1.13(c) and § 6068(e).
- Missing that a California law firm cannot be an LLC (R-BUS-108) and that LLP status is limited to listed professions (R-BUS-044).

**Bank.** [E-XO-005](../07-question-bank/essays/crossover/E-XO-005.md) (§ 310 lease, corporate opportunity, lawyer-director, reporting out) · [E-XO-018](../07-question-bank/essays/crossover/E-XO-018.md) (partnership by conduct, nonlawyer partner, UPL, convertible note).

---

## 6. Evidence + Professional Responsibility (2 times)

**Governing law.** Evidence: the code the call names (CEC or FRE). PR: California and ABA.

**Triggers.**
- Lawyer subpoenaed about what the client said → attorney-client privilege and its exceptions.
- Lawyer receives a weapon, bloody clothing or a document from the client → physical evidence; turnover; privilege for the communication but not the object.
- A third person sat in on the meeting → confidentiality element; waiver.
- Misdirected email or memo → inadvertent disclosure; stop reading and notify in California (R-PRF-075).
- Lawyer will testify → lawyer-as-witness rule.

**Skeleton.**
```text
Part 1 — Evidence, item by item: privilege (holder, elements, exception, waiver);
         work product; hearsay of any statement offered
Part 2 — Ethics: confidentiality is broader than privilege; handling evidence (3.4(a));
         candor; lawyer as witness; withdrawal
```

**Rules most often needed.** R-EVD-063 (privilege elements) · R-EVD-065 (exceptions: crime-fraud; California § 956.5) · R-PRF-016 (confidentiality vs. privilege vs. work product) · R-PRF-020 (physical evidence; *Meredith*) · R-PRF-069 (lawyer as witness: ABA hardship vs. California written consent).

**Traps.**
- Merging the two duties. Privilege answers "can a court compel it?"; confidentiality answers "may the lawyer reveal it?".
- Saying the privilege shields the physical object itself. It protects the communication; the lawyer must turn the object over after a reasonable time.
- Applying the FRE when the call names the CEC.

**Bank.** [E-XO-006](../07-question-bank/essays/crossover/E-XO-006.md) (CEC privilege, crime-fraud, mirror turnover, false statement at bail hearing) · [E-XO-019](../07-question-bank/essays/crossover/E-XO-019.md) (CEC hearsay and privilege items; lawyer as witness; inadvertent disclosure).

---

## 7. Criminal Law and Procedure + Evidence (2 times)

**Governing law.** Both past essays named the **CEC** and the U.S. Constitution. Crimes: general principles.

**Triggers.**
- 911 call, statement to police, lab report → hearsay **and** Confrontation (testimonial?).
- Defendant's prior acts → 404(b) / § 1101(b); domestic violence → § 1109 (CEC only).
- Defendant testifies with prior convictions → 609 vs. moral turpitude + § 352.
- Evidence from a search → Fourth Amendment; Truth-in-Evidence explains why federal law decides.
- Defendant's own statements → Miranda and voluntariness (R-CRM-093 to R-CRM-100).

**Skeleton.**
```text
Part 1 (if called) — Crimes: each crime → elements → defenses
Part 2 — Each item / trial point:
   1. Prop 8 sentence (CEC criminal case)
   2. Relevance; § 352 / 403
   3. Specific rule: character, impeachment, privilege, hearsay (exception)
   4. Constitution: Confrontation; Miranda; Fourth Amendment
   5. Ruling
```

**Rules most often needed.** R-EVD-004 (Truth-in-Evidence) · R-EVD-110, R-EVD-111 (*Crawford*; primary-purpose test) · R-CRM-090 (exclusionary rule; California excludes only as federal law requires) · R-EVD-042 / R-EVD-044 (other acts; § 1109) · R-EVD-025 / R-EVD-026 (conviction impeachment).

**Traps.**
- Stopping after a hearsay exception. A testimonial statement of a declarant who does not testify still fails Confrontation unless the declarant is unavailable and the defendant had a prior opportunity to cross-examine.
- Applying a broader California exclusionary rule. There is none after Prop 8.
- Forgetting the Prop 8 opener on a CEC criminal item.

**Bank.** [E-XO-007](../07-question-bank/essays/crossover/E-XO-007.md) (FRE: burglary and robbery; 911 call; photo identification; 404(b); 609) · [E-XO-020](../07-question-bank/essays/crossover/E-XO-020.md) (CEC: kidnapping; body-camera statement under § 1235; § 1109; § 1103 victim character).

---

## 8. Community Property + Professional Responsibility (1 time)

**Governing law.** CP: California. PR: California and ABA.

**Triggers.**
- Tort or debt of one spouse → which property is liable (community estate; order of satisfaction, R-CMP-088).
- Lawyer paid from community funds, or takes a lien on the home → third-party payor; business transaction (*Fletcher* charging lien).
- One lawyer for both spouses in a dissolution → joint representation of directly adverse parties. It cannot be consented to once one spouse asserts a claim against the other in the same litigation (rule 1.7(d)(3)); otherwise test consentability and get each spouse's informed written consent (R-PRF-021, R-PRF-024).
- Contingent or bonus fee in a divorce → prohibited contingent fee.
- Spouse hiding assets → spousal fiduciary duty; § 1101 remedies (R-CMP-068); lawyer must not assist (R-PRF-007).

**Skeleton.**
```text
Part 1 — CP, asset by asset (or debt by debt): character → liability to creditors → division
Part 2 — Ethics: conflicts (joint representation; third-party payor); fees (§ 6148; no contingency
         in dissolution); confidentiality between co-clients; assisting concealment; withdrawal
```

**Rules most often needed.** R-CMP-084 (community estate liable for either spouse's debts) · R-CMP-063 (spousal fiduciary duty) · R-PRF-024 (joint representation) · R-PRF-044 (no contingent fee in a dissolution) · R-PRF-026 / R-PRF-029 (lien as a business transaction; third-party payment).

**Traps.**
- Confusing "who owns it" (characterization) with "what a creditor can reach" (liability). They are separate questions.
- Missing that a fee lien on community property is a rule 1.8.1 transaction in California.

**Bank.** [E-XO-008](../07-question-bank/essays/crossover/E-XO-008.md) (LLC interest, 401(k), hidden account; joint representation; no fee agreement) · [E-XO-022](../07-question-bank/essays/crossover/E-XO-022.md) **(simulation — do not open before sitting it)**.

---

## 9. Constitutional Law + Real Property (1 time)

**Governing law.** Federal Constitution; Real Property general principles.

**Triggers.** A city conditions a permit on dedicating land or paying a fee → exactions. A regulation wipes out value → *Lucas* / *Penn Central*. Physical occupation → per se taking. Variance or rezoning denied → zoning law. Subdivision restrictions → servitudes.

**Skeleton.**
```text
I.   Real Property (per call): covenant / servitude creation, notice, enforcement, defenses;
     zoning (variance: area vs. use; hardship)
II.  Ripeness and standing for the takings claim
III. Taking? physical (per se) → exaction (Nollan / Dolan / Koontz) → total wipeout → Penn Central
IV.  Public use; just compensation; remedy
```

**Rules most often needed.** R-CON-080 (exactions) · R-CON-078, R-CON-079 (physical and regulatory takings) · R-CON-015 (ripeness) · R-PRP-072 (variances) · R-PRP-053 (common scheme; California recorded-instrument rule).

**Traps.**
- Treating a monetary fee as outside *Nollan*/*Dolan*; *Koontz* applies them to money demands.
- Granting a **use** variance in California (none exist; R-PRP-072).

**Bank.** [E-XO-009](../07-question-bank/essays/crossover/E-XO-009.md) (CC&Rs vs. a bed-and-breakfast; variance; bike-path dedication and park fee).

---

## 10. Contracts + Professional Responsibility (1 time)

**Governing law.** Contracts: general principles. PR: California and ABA.

**Triggers.** A seller hid or misstated a defect → misrepresentation / nondisclosure; rescission. The lawyer offers false expert testimony or a false statement in that suit → candor and false evidence. A **fee agreement** is itself the contract → formation, modification and the fee rules.

**Skeleton.**
```text
Part 1 — Contract claim: formation / defenses (misrepresentation, nondisclosure, mistake) → remedy
Part 2 — Ethics: candor (3.3); false evidence (ABA disclose vs. CA no disclosure);
         truthfulness (4.1); fees (unconscionable; § 6148) if the contract is the fee deal
```

**Rules most often needed.** R-CTR-037, R-CTR-038 (misrepresentation; nondisclosure) · R-CTR-105 / R-REM-043 (rescission) · R-PRF-061 (false evidence) · R-PRF-060 (candor) · R-PRF-042 (written fee agreement).

**Traps.** Using the ABA's disclose-to-the-court remedy as the California answer; forgetting that a mid-representation fee change is a contract modification **and** a business transaction issue.

**Bank.** [E-XO-021](../07-question-bank/essays/crossover/E-XO-021.md) **(simulation — do not open before sitting it)**.

---

## 11. Community Property + Trusts (1 time)

**Governing law.** California (Feb 2019 Q1 also involved Wills).

**Triggers.** Spouses put CP into a revocable trust → does the transfer change character? Who can revoke or amend? A creditor or ex-spouse wants a beneficiary's trust interest → spendthrift clause and its exceptions. Creditors of a settlor → revocable trust assets reachable.

**Skeleton.**
```text
I.   Characterize each asset (trust title does not by itself transmute)
II.  Revocation / amendment of a joint revocable trust holding CP
III. Creditors: settlor's (revocable trust) or beneficiary's (spendthrift; support exception)
IV.  Trustee duties (accumulation vs. mandatory payments)
```

**Rules most often needed.** R-TRS-015 (CP in a joint revocable trust: one spouse may revoke, both must modify) [VERIFY V-585] · R-CMP-022 (transmutation needs an express writing) · R-TRS-092 (settlor's creditors and revocable trusts) · R-TRS-043 (support exception to spendthrift) · R-CMP-017 (gifts and inheritances as SP).

**Traps.** Treating a transfer into a revocable trust as a transmutation; applying the general rule that spendthrift clauses bar all general creditors (California lets them reach part; R-TRS-046).

**Bank.** [E-XO-011](../07-question-bank/essays/crossover/E-XO-011.md) (boat tracing; home in a revocable trust; inherited account; spousal-support exception).

---

## 12. Civil Procedure + Evidence (1 time)

**Governing law.** Feb 2019 Q4 was a federal case under the FRE.

**Triggers.** Motion to dismiss or remand → diversity (domicile; corporate nerve center), removal. Request for an incident report → discovery scope, privilege, work product. Testimony at trial → hearsay, opposing-party statements, best evidence. Lost video → Rule 37(e) (R-CIV-071).

**Skeleton.**
```text
I.   Jurisdiction: SMJ (diversity / federal question); removal and remand
II.  Discovery: scope; privilege (state law governs in diversity — FRE 501); work product;
     spoliation sanctions
III. Trial evidence, item by item
```

**Rules most often needed.** R-CIV-004, R-CIV-005, R-CIV-006 (diversity; citizenship) · R-CIV-013 (removal) · R-EVD-062 (privilege law in diversity) · R-CIV-066 (work product) · R-EVD-090 (employee statements).

**Traps.** Applying federal privilege law to a state-law claim in diversity; treating an ordinary-course incident report as work product without asking whether it was prepared in anticipation of litigation.

**Bank.** [E-XO-010](../07-question-bank/essays/crossover/E-XO-010.md) (remand; incident report; lost video; employee statement).

---

## 13. Constitutional Law + Remedies (1 time)

**Governing law.** Federal. Jul 2019 Q2: a church sought a TRO, a preliminary injunction and declaratory relief against a city ban, on First Amendment grounds.

**Triggers.** "Seeks a TRO / preliminary injunction / declaratory judgment" against a government rule → justiciability first, then the merits as "likelihood of success", then the equitable factors.

**Skeleton** (Con Law essay-templates, Template 8).
```text
I.   Justiciability: standing; ripeness (pre-enforcement)
II.  Merits = likelihood of success (Free Exercise / Speech analysis, concise)
III. TRO: likelihood; irreparable harm before a hearing; balance; public interest; notice; bond
IV.  Preliminary injunction: same four factors (Winter) after notice and hearing
V.   Declaratory relief: actual controversy (28 U.S.C. § 2201)
```

**Rules most often needed.** R-CON-008, R-CON-015 (standing; ripeness) · R-CON-087 (Free Exercise: neutral and generally applicable laws) · R-REM-065, R-REM-066 (federal TRO; *Winter*) · R-REM-091 (declaratory judgment).

**Traps.** Writing the full merits twice (once for the TRO, once for the PI): analyze once and cross-refer. Using California's *IT Corp.* test in a federal case.

**Bank.** No Con Law + Remedies crossover in the bank yet. Use [`../03-subjects/constitutional-law/essay-templates.md`](../03-subjects/constitutional-law/essay-templates.md) Template 8.

---

## 14. Real Property + Wills (1 time)

**Governing law.** Oct 2020 Q3 asked what interests four family members held in a parcel and whether claims for taxes or rents lay; Wills issues are California law.

**Triggers.** A deed into joint tenancy, then a death or a later conveyance → survivorship and severance. A will devising land → will validity, then what the will can reach (JT land passes outside the will). One cotenant in possession paying taxes → cotenant contribution and rents. A mortgage on devised land → no exoneration.

**Skeleton.**
```text
I.   Timeline of title: each deed and death, in date order
II.  Form of co-ownership (JT vs. TIC); severance; survivorship
III. Will validity and what passes under it (only property not passing by survivorship)
IV.  Cotenant claims: possession, rents, taxes, improvements
V.   Each claimant's interest
```

**Rules most often needed.** R-PRP-020, R-PRP-021 (JT creation; severance, *Riddle*) · R-PRP-024, R-PRP-025 (cotenants' rents, contribution, accounting) · R-WIL-047 (will execution) · R-WIL-073 (no exoneration of a specific gift) · R-PRP-115 (transfer by will and operation of law).

**Traps.** Letting a will pass joint-tenancy land; forgetting that a cotenant in sole possession owes no rent absent ouster or agreement, but may claim contribution for taxes only beyond the rental value of her occupancy (R-PRP-024, R-PRP-025).

**Bank.** [E-XO-012](../07-question-bank/essays/crossover/E-XO-012.md) **(simulation — do not open before sitting it)**.

---

## 15. Business Associations + Remedies (1 time)

**Governing law.** General principles; California remedy sentences where useful.

**Triggers.** Owners of an unincorporated venture sued on its lease → was it a partnership (personal liability; exhaustion, R-BUS-029) or a defective entity or pierced veil (R-BUS-047)? One partner takes a business opportunity or competes → loyalty breach; constructive trust or disgorgement. A partner is about to sell the diverted asset → TRO / preliminary injunction; lis pendens (R-REM-074).

**Skeleton.**
```text
I.   Entity: partnership formed? (or corporation / LLC; veil piercing)
II.  Liability: entity, then owners personally (exhaustion)
III. Fiduciary breach (loyalty, care)
IV.  Remedies: damages vs. disgorgement; constructive trust / equitable lien and tracing;
     injunction (TRO, PI); accounting; dissociation or dissolution
```

**Rules most often needed.** R-BUS-021 (partnership formation) · R-BUS-028 (partners' personal liability) · R-BUS-034 (partner's duty of loyalty) · R-REM-044 (constructive trust) · R-REM-037 (disgorgement of profits).

**Traps.** Forgetting that profit sharing raises a presumption of partnership; choosing a constructive trust without tracing or without checking for a bona fide purchaser.

**Bank.** [E-XO-013](../07-question-bank/essays/crossover/E-XO-013.md) (partnership opportunity; constructive trust; TRO; disgorgement).

---

## Also seen once (outside the generated top-15 table)

| Pair | Past essay | How it worked | Rules |
|---|---|---|---|
| BA + Torts | Jul 2023 Q1 | Which defendants (the attorney, the law-firm partnership, the partners) are liable for a car accident | R-BUS-014 (scope of employment), R-BUS-027 (partnership liable for a partner's tort), R-BUS-028, R-BUS-045 (LLP shield) |
| Criminal + PR | Jul 2025 Q5 | Ethics of the prosecutor and defense lawyer (California and ABA), plus the guilty plea and sentence | R-PRF-070 (prosecutor), R-PRF-011 (plea offers), R-PRF-005 (client decides the plea), R-CRM-115 (guilty pleas) |

## Bank crossovers for pairs not yet tested

| Essay | Pair | Note |
|---|---|---|
| [E-XO-023](../07-question-bank/essays/crossover/E-XO-023.md) | Con Law + Criminal | Speech limits on a criminal statute; suppression |
| [E-XO-024](../07-question-bank/essays/crossover/E-XO-024.md) | Civil Procedure + PR | Motions, joinder, Rule 11, discovery; lawyers' ethics |
| [E-XO-025](../07-question-bank/essays/crossover/E-XO-025.md) | Real Property + Remedies | Marketable title; risk of loss; land-sale remedies |
| [E-XO-026](../07-question-bank/essays/crossover/E-XO-026.md) | Contracts + BA | Agency and partnership authority on contracts |
| [E-XO-027](../07-question-bank/essays/crossover/E-XO-027.md) | Civil Procedure + Remedies | **(simulation — do not open before sitting it)** |
| [E-XO-028](../07-question-bank/essays/crossover/E-XO-028.md) | Trusts + PR | Gift to a lawyer-trustee's relative; dual fees; trustee removal |
| [E-XO-029](../07-question-bank/essays/crossover/E-XO-029.md) | Torts + Evidence | Products and negligence claims; FRE items |
