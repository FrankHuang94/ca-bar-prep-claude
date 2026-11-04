---
subject: CTR
topic: Contracts — decision-tree flowcharts (Mermaid)
coverage_ids: [CTR-CBX-I, CTR-MBE-I.A, CTR-MBE-I.C, CTR-MBE-II.F, CTR-MBE-III.A, CTR-MBE-IV.C, CTR-MBE-IV.F, CTR-MBE-V.A]
tested_on: [MBE, essay]
exam_frequency: {level: high, basis: "Essays: 16 of 31 administrations 2012-02 to 2026-07 (52%); MBE: 25 scored questions every exam"}
last_verified: 2026-11-04
status: draft
---

# Contracts — flowcharts

Eight decision trees for the analyses you will run most often. Rule IDs point to [`rule-statements.md`](rule-statements.md).

## 1. Which law governs? (R-CTR-001, R-CTR-002)

```mermaid
flowchart TD
    A["Contract subject matter?"] --> B{"Goods only? Movable things"}
    B -->|Yes| U["UCC Article 2 governs"]
    B -->|No| C{"Goods and services mixed?"}
    C -->|No - services, land, employment| CL["Common law governs"]
    C -->|Yes| D{"Predominant purpose is goods?"}
    D -->|Yes| U
    D -->|No| CL
    U --> M{"Are the parties merchants?"}
    M -->|Both| MM["Apply merchant rules: 2-201 confirmation, 2-207 additional terms"]
    M -->|Seller only| MS["Merchantability warranty, firm offer, risk passes on receipt"]
    M -->|Neither| NM["General Article 2 rules only"]
```

## 2. Was the offer still open when acceptance took effect? (R-CTR-006 to R-CTR-011, R-CTR-015)

```mermaid
flowchart TD
    O["Valid offer made"] --> I{"Irrevocable? Option, firm offer, part performance, reliance"}
    I -->|Yes| OK1["Offeror cannot revoke during the period"]
    I -->|No| T{"Before acceptance took effect, did the offeree receive revocation, reject, counteroffer, or did time lapse or a party die?"}
    T -->|Yes| DEAD["Power of acceptance ended - no contract"]
    T -->|No| ACC{"How was acceptance sent?"}
    ACC -->|Mail or reasonable medium| DISP["Effective on dispatch"]
    ACC -->|Under an option| REC["Effective on receipt"]
    ACC -->|Offer required receipt| REC
    DISP --> K["Contract formed at dispatch"]
    REC --> K2["Contract formed at receipt"]
    OK1 --> ACC
```

## 3. Battle of the forms, UCC 2-207 (R-CTR-013, R-CTR-014)

```mermaid
flowchart TD
    S["Offer, then a reply with new or different terms"] --> Q1{"Definite and seasonable expression of acceptance?"}
    Q1 -->|No - dickered terms differ| CO["Counteroffer - no contract on the writings"]
    Q1 -->|Yes| Q2{"Expressly conditional on assent to new terms?"}
    Q2 -->|Yes| CO
    Q2 -->|No| K["Contract formed on the writings"]
    K --> Q3{"Additional or different terms?"}
    Q3 -->|Different - conflicting| KO["Knockout rule - both drop out, UCC gap fillers apply"]
    Q3 -->|Additional| Q4{"Both parties merchants?"}
    Q4 -->|No| PR["Mere proposal - out unless offeror expressly agrees"]
    Q4 -->|Yes| Q5{"Offer limited to its terms, material alteration, or objection?"}
    Q5 -->|Any yes| OUT["Term is out"]
    Q5 -->|All no| IN["Term becomes part of the contract"]
    CO --> Q6{"Did both parties perform as if a contract existed?"}
    Q6 -->|Yes| C3["Contract under 2-207 subsection 3 - agreed terms plus gap fillers"]
    Q6 -->|No| NOK["No contract"]
```

## 4. Is the promise enforceable without a bargain? (R-CTR-022 to R-CTR-027)

```mermaid
flowchart TD
    P["Promise"] --> C{"Bargained-for legal detriment?"}
    C -->|Yes| PD{"Only a pre-existing duty owed to promisor?"}
    PD -->|No| ENF["Consideration - enforceable"]
    PD -->|Yes| EX{"Exception? New duty, honest dispute, unforeseen circumstances, UCC goods"}
    EX -->|Yes| ENF
    EX -->|No| PE
    C -->|No - gift, illusory, or past| PB{"Past benefit to promisor, not a gift?"}
    PB -->|Yes| MB["Material benefit rule R2d 86 - enforceable to prevent injustice"]
    PB -->|No| PE{"Foreseeable, actual, reasonable reliance?"}
    PE -->|Yes| PEY["Promissory estoppel - remedy as justice requires"]
    PE -->|No| NO["Unenforceable gratuitous promise"]
```

## 5. Statute of frauds (R-CTR-042 to R-CTR-048)

```mermaid
flowchart TD
    A["Contract alleged"] --> B{"Within the statute? Marriage, one year, land, executor, goods 500 or more, surety"}
    B -->|No| OKN["No writing needed"]
    B -->|Yes| C{"Signed writing by party to be charged with essential terms?"}
    C -->|Yes| OKW["Statute satisfied"]
    C -->|No| D{"Goods?"}
    D -->|Yes| E{"Merchant confirmation unanswered 10 days, special manufacture, admission, or paid or accepted goods?"}
    E -->|Yes| OKU["Enforceable to that extent"]
    E -->|No| R
    D -->|No| F{"Land with part performance, full performance of one-year deal, or main purpose surety?"}
    F -->|Yes| OKC["Enforceable"]
    F -->|No| R{"Promissory estoppel - serious reliance?"}
    R -->|Yes| PE["Enforceable as justice requires"]
    R -->|No| UN["Unenforceable - restitution only"]
```

## 6. Parol evidence (R-CTR-049 to R-CTR-052)

```mermaid
flowchart TD
    A["Extrinsic evidence offered"] --> T{"Made after the writing?"}
    T -->|Yes| ADM1["Not barred by the rule - check NOM clause and SOF"]
    T -->|No - prior or contemporaneous| P{"Purpose: fraud, mistake, duress, illegality, condition precedent, reformation?"}
    P -->|Yes| ADM2["Admissible - California admits fraud even if contradictory, Riverisland"]
    P -->|No| INT{"To interpret an ambiguous term?"}
    INT -->|Yes| ADM3["Admissible - California: if reasonably susceptible, PG and E"]
    INT -->|No| W{"Writing intended as final?"}
    W -->|No| ADM4["Admissible"]
    W -->|Yes| CON{"Does the term contradict the writing?"}
    CON -->|Yes| EXC1["Excluded"]
    CON -->|No - consistent additional term| CI{"Writing complete and exclusive?"}
    CI -->|No - partial integration| ADM5["Admissible to supplement"]
    CI -->|Yes| NAT{"Separate consideration, or term naturally omitted? UCC: would not certainly be included"}
    NAT -->|Yes| ADM6["Admissible"]
    NAT -->|No| EXC2["Excluded"]
```

## 7. Breach and the injured party's options (R-CTR-062 to R-CTR-070)

```mermaid
flowchart TD
    S["Performance issue"] --> TIME{"Before performance was due?"}
    TIME -->|Yes| UNQ{"Unequivocal refusal or disabling act?"}
    UNQ -->|Yes| AR["Anticipatory repudiation: sue now, wait, or urge retraction - mitigate"]
    UNQ -->|No - doubts only| AA["Demand adequate assurance - no assurance in 30 days means repudiation"]
    TIME -->|No - performance due| G{"Goods?"}
    G -->|Yes| PT["Perfect tender - reject, accept, or partial - subject to cure and installments"]
    G -->|No| COND{"Express condition failed?"}
    COND -->|Yes| EXC{"Excused? Waiver, prevention, forfeiture"}
    EXC -->|No| NODUTY["No duty arises"]
    EXC -->|Yes| MAT
    COND -->|No| MAT{"Material breach? R2d 241 factors"}
    MAT -->|Yes| TOT["Suspend, then terminate after cure period - total breach damages"]
    MAT -->|No| PART["Minor breach - damages only, must keep performing"]
```

## 8. UCC risk of loss (R-CTR-077 to R-CTR-080)

```mermaid
flowchart TD
    A["Goods lost or damaged"] --> AG{"Agreement allocates risk?"}
    AG -->|Yes| FOLLOW["Follow the agreement"]
    AG -->|No| BR{"Did a party breach?"}
    BR -->|Seller tendered nonconforming goods| SEL["Risk stays on seller until cure or acceptance"]
    BR -->|Buyer repudiated after identification| BUY["Risk on buyer for a reasonable time, to extent seller is uninsured"]
    BR -->|No breach| CAR{"Carrier involved?"}
    CAR -->|Shipment contract, FOB seller| SHIP["Risk passes on due delivery to carrier"]
    CAR -->|Destination contract, FOB buyer| DEST["Risk passes on tender at destination"]
    CAR -->|No carrier| BAIL{"Goods held by bailee?"}
    BAIL -->|Yes| BAILR["Risk passes on document or bailee acknowledgment"]
    BAIL -->|No| MER{"Seller a merchant?"}
    MER -->|Yes| RCPT["Risk passes on receipt by buyer"]
    MER -->|No| TEND["Risk passes on tender"]
```
