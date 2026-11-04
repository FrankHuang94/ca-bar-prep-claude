---
subject: REM
topic: Remedies — decision flowcharts (Mermaid)
coverage_ids: [REM-CBX-I, REM-CBX-II, REM-CBX-III.a, REM-CBX-III.b, REM-CBX-IV, REM-CBX-V, REM-SUP-001, REM-SUP-002, REM-SUP-003]
tested_on: [essay, PT]
exam_frequency: {level: high, basis: "Essays: 16 of 31 administrations 2012-02 to 2026-07 (52%)"}
last_verified: 2026-11-04
status: draft
---

# Remedies — flowcharts

Ten decision trees for the analyses you will run most often. Rule IDs point to [`rule-statements.md`](rule-statements.md).

## 1. Master flow: which remedies to discuss for one claim (R-REM-001, R-REM-006)

```mermaid
flowchart TD
    A["Claim established: contract, tort, property or constitutional"] --> B{"Did the call name specific remedies?"}
    B -->|Yes| C["Answer only those, in the order named"]
    B -->|No| D["Legal remedies first: compensatory damages"]
    D --> E["Apply limits: causation, foreseeability, certainty, mitigation"]
    E --> F{"Tort with malice, oppression or fraud?"}
    F -->|Yes| G["Punitive damages: CA 3294 and due process"]
    F -->|No| H["No punitive damages; consider nominal damages"]
    G --> R["Restitution: did Defendant gain more than Plaintiff lost?"]
    H --> R
    R --> R1["Legal restitution: quasi-contract, replevin, ejectment"]
    R --> R2["Equitable restitution: constructive trust or equitable lien"]
    R1 --> Q["Equitable remedies: TRO, preliminary and permanent injunction, specific performance, reformation, rescission"]
    R2 --> Q
    Q --> DEF["Equitable defenses"]
    DEF --> BEST["Election: best remedy without double recovery"]
```

## 2. Permanent injunction: I-P-F-B-D (R-REM-055 to R-REM-060)

```mermaid
flowchart TD
    S["Plaintiff seeks a permanent injunction"] --> I{"Is the legal remedy inadequate? Unique, irreparable, speculative, continuing, insolvent defendant"}
    I -->|No| DMG["Deny injunction - damages only"]
    I -->|Yes| P{"Property right or other protectable interest?"}
    P -->|No| DMG
    P -->|Yes| F{"Feasible to enforce? Prohibitory or simple one-time act"}
    F -->|No - ongoing supervision or personal services| ALT["Deny or narrow; consider negative injunction or damages"]
    F -->|Yes| W{"Did defendant act willfully?"}
    W -->|Yes| D2["No balancing - check defenses"]
    W -->|No| BAL{"Is defendant's hardship greatly disproportionate to plaintiff's benefit, considering the public interest?"}
    BAL -->|Yes| ALT2["Deny or tailor relief; award damages instead"]
    BAL -->|No| D2
    D2 --> DEF{"Laches, unclean hands, estoppel, waiver, unconscionability?"}
    DEF -->|Yes| DENY["Injunction barred"]
    DEF -->|No| GRANT["Grant permanent injunction - enforce by contempt"]
```

## 3. TRO and preliminary injunction (R-REM-065 to R-REM-069)

```mermaid
flowchart TD
    A["Harm threatened before trial"] --> B{"Will irreparable harm occur before a noticed hearing can be held?"}
    B -->|Yes| TRO["Seek TRO"]
    B -->|No| PI["Seek preliminary injunction on notice"]
    TRO --> N{"Notice given, or attorney certifies efforts and reasons?"}
    N -->|No| X["No ex parte TRO"]
    N -->|Yes| T2["TRO issues with bond - federal max 14 days plus one extension; California OSC hearing within 15 or 22 days"]
    T2 --> PI
    PI --> Q{"Which court?"}
    Q -->|Federal| W["Winter: likely success, likely irreparable harm, balance of equities, public interest"]
    Q -->|California| IT["IT Corp: likelihood of prevailing and relative interim harm on a sliding scale; some chance of success required"]
    W --> M{"Prohibitory, preserving status quo?"}
    IT --> M
    M -->|Yes| G["Grant if factors met; bond required"]
    M -->|No - mandatory| H["Heightened showing; disfavored"]
```

## 4. Specific performance (R-REM-070 to R-REM-074)

```mermaid
flowchart TD
    A["Plaintiff seeks specific performance"] --> C{"Valid contract with definite terms?"}
    C -->|No| NO["No specific performance - consider restitution"]
    C -->|Yes| K{"Plaintiff performed or ready, willing and able?"}
    K -->|No| NO
    K -->|Yes| T{"Subject matter?"}
    T -->|Land| L["Land is unique; CA 3387 presumption"]
    L --> SF{"Single-family home buyer will occupy?"}
    SF -->|Yes| CONC["Inadequacy conclusively presumed"]
    SF -->|No| REB["Rebuttable presumption"]
    T -->|Goods| G{"Unique, or cover impossible? UCC 2-716"}
    G -->|No| DMG["Cover and damages only"]
    G -->|Yes| OK["Damages inadequate"]
    T -->|Personal services| PS["No specific performance; negative injunction at most"]
    CONC --> FE{"Feasible to enforce?"}
    REB --> FE
    OK --> FE
    FE -->|Yes| DEF{"Defenses: laches, unclean hands, unconscionability or CA 3391 inadequate consideration, mistake, SOF, BFP?"}
    FE -->|No| DMG
    DEF -->|None| GRANT["Grant specific performance, with abatement if needed"]
    DEF -->|Yes| DENY["Deny; damages or restitution remain"]
```

## 5. Equitable restitution: constructive trust or equitable lien? (R-REM-044 to R-REM-049)

```mermaid
flowchart TD
    A["Defendant obtained plaintiff's money or property wrongfully"] --> T{"Can it be traced into a specific asset defendant now holds?"}
    T -->|No - dissipated| Q["Legal restitution only: quasi-contract money judgment"]
    T -->|Yes| B{"Asset now held by a bona fide purchaser for value without notice?"}
    B -->|Yes| PR["No claim to the asset; trace into sale proceeds or sue defendant"]
    B -->|No - defendant or a donee| V{"Asset bought entirely with plaintiff's funds?"}
    V -->|No - partly, or improvements to defendant's property| LIEN1["Equitable lien or proportionate share; subrogation if a debt was paid off"]
    V -->|Yes| U{"Has the asset risen or fallen in value?"}
    U -->|Risen| CT["Constructive trust: plaintiff takes the asset and its gain"]
    U -->|Fallen| EL["Equitable lien plus deficiency judgment"]
    CT --> PRI["Priority over defendant's unsecured creditors; enforce by contempt"]
    EL --> PRI
    LIEN1 --> PRI
```

## 6. Commingled bank account: lowest intermediate balance (R-REM-048)

```mermaid
flowchart TD
    A["Plaintiff's money deposited into defendant's account with defendant's own money"] --> B["Track the balance after every withdrawal and deposit"]
    B --> C{"Did withdrawals reduce the balance below plaintiff's amount?"}
    C -->|No| D["Defendant presumed to spend own money first; plaintiff claims full amount from the account"]
    C -->|Yes| E["Plaintiff's claim to the account is capped at the lowest intermediate balance"]
    E --> F{"Later deposits of defendant's own money?"}
    F -->|Yes| G["They do not restore plaintiff's share unless intended as restitution"]
    F -->|No| H["Cap stays at the lowest balance"]
    E --> I{"Were withdrawals used to buy an identifiable asset?"}
    I -->|Yes| J["Plaintiff may trace into that asset for the shortfall"]
    I -->|No| K["Shortfall is a personal money claim only"]
```

## 7. Each item of damages: the four limits (R-REM-007 to R-REM-011)

```mermaid
flowchart TD
    A["Item of loss claimed"] --> B{"Caused by the wrong? But-for or substantial factor"}
    B -->|No| X["Not recoverable"]
    B -->|Yes| C{"Contract or tort?"}
    C -->|Contract| D{"Natural consequence, or special circumstance known at contracting? Hadley"}
    C -->|Tort| E{"Within proximate cause? CA 3333"}
    D -->|No| X
    D -->|Yes| F{"Proven with reasonable certainty?"}
    E -->|No| X
    E -->|Yes| F
    F -->|No| R["Fall back to reliance or restitution"]
    F -->|Yes| G{"Could plaintiff have avoided it by reasonable effort?"}
    G -->|Yes| H["Reduce by avoidable amount; add mitigation costs"]
    G -->|No| OK["Recoverable in full"]
```

## 8. Punitive damages (R-REM-026 to R-REM-031)

```mermaid
flowchart TD
    A["Plaintiff seeks punitive damages"] --> B{"Is the claim a tort, not merely breach of contract?"}
    B -->|No| C{"Is there an independent tort such as fraud?"}
    C -->|No| X["No punitive damages"]
    C -->|Yes| D
    B -->|Yes| D{"Malice, oppression or fraud? CA 3294 by clear and convincing evidence"}
    D -->|No| X
    D -->|Yes| E{"Defendant is a company?"}
    E -->|Yes| F{"Officer, director or managing agent knew, authorized, ratified or acted?"}
    F -->|No| X
    F -->|Yes| G
    E -->|No| G{"Actual damages awarded and evidence of defendant's financial condition?"}
    G -->|No| X
    G -->|Yes| H["Amount: reprehensibility, ratio near single digits, comparable penalties - Gore and State Farm"]
```

## 9. Encroachment: removal or equitable easement? (R-REM-061)

```mermaid
flowchart TD
    A["Defendant's structure encroaches on plaintiff's land"] --> B{"Was the encroachment willful or negligent?"}
    B -->|Yes| R["Mandatory injunction to remove, regardless of cost"]
    B -->|No - innocent| C{"Will plaintiff suffer irreparable injury if it stays?"}
    C -->|Yes| R
    C -->|No| D{"Is removal hardship to defendant greatly disproportionate to plaintiff's hardship?"}
    D -->|No| R
    D -->|Yes| E["Deny removal; damages or a California equitable easement on payment of compensation"]
    R --> L{"Did plaintiff delay while defendant built, or consent?"}
    L -->|Yes| LE["Laches or estoppel may bar removal"]
    L -->|No| OK["Removal ordered"]
```

## 10. Writing does not match the deal: reformation or rescission? (R-REM-043, R-REM-075)

```mermaid
flowchart TD
    A["Dispute over a written contract or deed"] --> B{"Did the parties reach an actual agreement that the writing misstates?"}
    B -->|Yes| C{"Mutual mistake in expression, or fraud or known unilateral mistake about the writing?"}
    C -->|Yes| D{"Clear and convincing proof; no bona fide purchaser relying on the writing?"}
    D -->|Yes| REF["Reformation, then enforce as reformed by specific performance, injunction or damages"]
    D -->|No| NOREF["Reformation barred"]
    C -->|No| NOREF
    B -->|No - no meeting of the minds or a flawed bargain| E{"Ground to avoid: fraud, mutual mistake on a basic assumption, duress, undue influence?"}
    E -->|Yes| RES["Rescission and restitution: notice, restore, no affirmation or delay; CA 1692 adds consequential damages"]
    E -->|No| ENF["Enforce the writing as written"]
```
