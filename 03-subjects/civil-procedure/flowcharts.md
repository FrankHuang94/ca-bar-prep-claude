---
subject: CIV
topic: Civil Procedure — decision trees (Mermaid)
coverage_ids: [CIV-MBE-I.A, CIV-MBE-I.B, CIV-MBE-I.D, CIV-MBE-II.A, CIV-MBE-III.D, CIV-MBE-III.E, CIV-MBE-V.C, CIV-MBE-VI.D, CIV-MBE-VII.A]
tested_on: [MBE, essay]
exam_frequency: {level: high, basis: "Essays: 13 of 31 administrations 2012-02 to 2026-07 (42%); MBE: 25 scored questions every exam"}
last_verified: 2026-11-04
status: draft
---

# Civil Procedure — flowcharts

Each chart cites the rule blocks in [rule-statements.md](rule-statements.md). Labels avoid parentheses so the diagrams render in any Mermaid viewer.

## 1. Federal subject-matter jurisdiction (R-CIV-001 to R-CIV-012)

```mermaid
flowchart TD
    A["Claim filed in or removed to federal court"] --> B{"Does federal law create the claim, or is a substantial federal issue necessarily raised on the face of the well-pleaded complaint?"}
    B -- Yes --> FQ["Federal question jurisdiction under 28 USC 1331"]
    B -- No --> C{"Complete diversity at filing? Check every plaintiff against every defendant"}
    C -- No --> SUP{"Is there another anchor claim with original jurisdiction?"}
    C -- Yes --> D{"Amount exceeds 75,000 dollars, aggregated only per plaintiff per defendant?"}
    D -- Yes --> DIV["Diversity jurisdiction under 28 USC 1332"]
    D -- No --> CAFA{"Class of 100 or more, over 5 million, minimal diversity?"}
    CAFA -- Yes --> CA2["CAFA jurisdiction under 1332 d"]
    CAFA -- No --> SUP
    FQ --> E["For each other claim: common nucleus of operative fact? Supplemental under 1367 a"]
    DIV --> F{"Claim by a plaintiff against a party joined under Rule 14, 19, 20 or 24, or by a Rule 19 or 24 plaintiff?"}
    F -- Yes --> G["Barred by 1367 b unless independent diversity and amount"]
    F -- No --> E
    SUP -- Yes --> E
    SUP -- No --> H["Dismiss for lack of SMJ; never waived"]
    E --> I{"Discretion to decline under 1367 c: novel state issue, predominance, federal claims gone, exceptional circumstances?"}
    I -- Decline --> J["Dismiss or remand state claims; tolling under 1367 d"]
    I -- Keep --> K["Court hears all claims"]
```

## 2. Removal and remand (R-CIV-013 to R-CIV-016)

```mermaid
flowchart TD
    A["Action pending in state court"] --> B{"Would the federal court have original jurisdiction based on the complaint?"}
    B -- No --> X["Not removable; federal defense does not count"]
    B -- Yes --> C{"Removing party is a defendant to the plaintiff's claim?"}
    C -- No --> X2["Plaintiffs and third-party counterclaim defendants cannot remove"]
    C -- Yes --> D{"Diversity-only case with a properly joined and served forum-State defendant?"}
    D -- Yes --> X3["Forum-defendant rule bars removal; procedural defect waived unless remand sought within 30 days"]
    D -- No --> E{"Notice filed within 30 days of formal service or of the other paper showing removability?"}
    E -- No --> X4["Untimely; procedural defect"]
    E -- Yes --> F{"All properly joined and served defendants consent?"}
    F -- No --> X5["Unanimity defect; procedural"]
    F -- Yes --> G{"Diversity case removed more than one year after commencement?"}
    G -- Yes --> H{"Plaintiff acted in bad faith to prevent removal?"}
    H -- No --> X6["Too late"]
    H -- Yes --> OK["Removal proper to district embracing state court"]
    G -- No --> OK
    OK --> R{"Later: SMJ lost, e.g. federal claims amended away or nondiverse party joined?"}
    R -- Yes --> RM["Remand required; Royal Canin; 1447 c and e"]
    R -- No --> K["Federal court keeps case"]
```

## 3. Personal jurisdiction (R-CIV-017 to R-CIV-027)

```mermaid
flowchart TD
    A["Defendant objects to PJ in first Rule 12 response?"] -- No --> W["Objection waived"]
    A -- Yes --> B{"Statutory basis: state long-arm via Rule 4k1A, bulge, federal statute, or 4k2?"}
    B -- No --> N["No PJ"]
    B -- Yes --> C{"Traditional basis: served while present, domicile, consent, registration statute with express consent?"}
    C -- Yes --> Y["PJ exists"]
    C -- No --> D{"Defendant at home in forum: incorporation State or principal place of business, or exceptional case?"}
    D -- Yes --> Y
    D -- No --> E{"Purposeful availment or direction by defendant's own conduct?"}
    E -- No --> N
    E -- Yes --> F{"Claim arises out of or relates to those contacts?"}
    F -- No --> N
    F -- Yes --> G{"Defendant shows a compelling case that jurisdiction is unreasonable under the fairness factors?"}
    G -- Yes --> N
    G -- No --> Y
```

## 4. Venue and transfer (R-CIV-031 to R-CIV-036)

```mermaid
flowchart TD
    A["Case filed in federal district"] --> R{"Removed case?"}
    R -- Yes --> RV["Venue is the district embracing the state court; 1391 does not apply"]
    R -- No --> B{"All defendants reside in one State and this district is home to any of them?"}
    B -- Yes --> P["Venue proper"]
    B -- No --> C{"Substantial part of events or property in this district?"}
    C -- Yes --> P
    C -- No --> D{"No district anywhere satisfies b1 or b2, and a defendant is subject to PJ here?"}
    D -- Yes --> P
    D -- No --> IMP["Venue improper"]
    IMP --> T1["1406 a: dismiss or transfer in interest of justice; transferee applies its own law"]
    P --> FS{"Valid forum-selection clause naming another forum?"}
    FS -- Yes --> AM["Atlantic Marine: transfer or FNC dismissal absent extraordinary public-interest reasons"]
    FS -- No --> CONV{"Convenience of parties and witnesses and interest of justice favor another district where the case might have been brought?"}
    CONV -- Yes --> T2["1404 a transfer; transferor's law follows the case"]
    CONV -- No --> FNC{"Better forum is foreign or state court?"}
    FNC -- Yes --> FN["Forum non conveniens: adequate forum plus private and public factors"]
    FNC -- No --> STAY["Case stays"]
```

## 5. Erie analysis (R-CIV-037 to R-CIV-040)

```mermaid
flowchart TD
    A["State-law claim in federal court; state and federal practice differ"] --> B{"Is a federal statute on point and constitutional?"}
    B -- Yes --> FS["Apply the federal statute, e.g. 1404 a in Stewart"]
    B -- No --> C{"Is a Federal Rule sufficiently broad to answer the question?"}
    C -- Yes --> D{"Does the Rule really regulate procedure under the Rules Enabling Act?"}
    D -- Yes --> FR["Apply the Federal Rule: Hanna, Shady Grove, Berk v. Choy"]
    D -- No --> SL["Apply state law"]
    C -- No --> E{"Would ignoring the state rule change the outcome so as to encourage forum shopping or inequitable administration?"}
    E -- No --> FP["Apply federal practice"]
    E -- Yes --> F{"Is the state rule bound up with state-created rights, or only form and mode with a strong countervailing federal interest such as the jury?"}
    F -- Bound up --> SL
    F -- Federal interest outweighs --> FP2["Apply federal practice: Byrd"]
```

## 6. Required joinder under Rule 19 (R-CIV-054, R-CIV-055)

```mermaid
flowchart TD
    A["Absent person X"] --> B{"Without X, can the court give complete relief among existing parties?"}
    B -- No --> REQ["X is a required party"]
    B -- Yes --> C{"Does X claim an interest that the case may impair as a practical matter?"}
    C -- Yes --> REQ
    C -- No --> D{"Would X's absence expose a party to double or inconsistent obligations?"}
    D -- Yes --> REQ
    D -- No --> NR["Not required; e.g. joint tortfeasors under Temple"]
    REQ --> E{"Is joinder feasible: X subject to service and joinder will not destroy SMJ?"}
    E -- Yes --> J["Court orders X joined; if X objects to venue and venue becomes improper, X is dismissed"]
    E -- No --> F["Rule 19 b factors: prejudice, ways to reduce it, adequacy of judgment, plaintiff's alternative forum"]
    F --> G{"Equity and good conscience favor proceeding?"}
    G -- Yes --> PR["Proceed without X"]
    G -- No --> DM["Dismiss the action"]
```

## 7. Discovery dispute on an essay (R-CIV-062 to R-CIV-073)

```mermaid
flowchart TD
    A["Request for specific item"] --> B{"Did movant meet and confer and certify it?"}
    B -- No --> DEN["Deny motion to compel; no fees"]
    B -- Yes --> C{"Relevant to a claim or defense and proportional to the needs of the case?"}
    C -- No --> LIM["Deny or limit; protective order possible"]
    C -- Yes --> D{"Privileged, e.g. attorney-client?"}
    D -- Yes --> PL["Protected; withholding party must log it"]
    D -- No --> E{"Prepared in anticipation of litigation by or for a party or representative?"}
    E -- Yes --> F{"Opinion work product?"}
    F -- Yes --> PROT["Protected"]
    F -- No --> G{"Substantial need and no substantial equivalent without undue hardship?"}
    G -- No --> PROT
    G -- Yes --> ORD["Order production of factual portions"]
    E -- No --> H{"Expert material: consulting expert facts or opinions?"}
    H -- Yes --> I{"Exceptional circumstances?"}
    I -- No --> PROT
    I -- Yes --> ORD
    H -- No --> ORD
    ORD --> S["Grant motion; award expenses unless substantially justified; Rule 37 b sanctions for later violation"]
```

## 8. Post-trial motions (R-CIV-087 to R-CIV-090)

```mermaid
flowchart TD
    A["Verdict returned"] --> B{"Did the party move for JMOL under Rule 50 a before submission?"}
    B -- Yes --> C["Renewed JMOL within 28 days: no legally sufficient evidentiary basis for a reasonable jury"]
    B -- No --> D["No renewed JMOL; sufficiency not reviewable on appeal"]
    A --> E{"Grounds for new trial: clear weight of evidence, excessive damages, legal error, misconduct, new evidence?"}
    E -- Yes --> F["Rule 59 motion within 28 days; judge may weigh evidence; remittitur allowed, additur not"]
    A --> G{"More than 28 days after judgment?"}
    G -- Yes --> H{"Which Rule 60 b ground?"}
    H -->|Mistake, new evidence, fraud| I["Reasonable time, no more than one year"]
    H -->|Void, satisfied, any other reason| J["Reasonable time; void judgments included under Coney Island"]
    C --> K["Timely 50 b, 52 b, 59 and early 60 motions suspend the 30-day appeal clock"]
    F --> K
```

## 9. Claim and issue preclusion (R-CIV-094 to R-CIV-098, R-CIV-114, R-CIV-115)

```mermaid
flowchart TD
    A["Second suit; earlier judgment exists"] --> B{"Which court rendered the first judgment?"}
    B -->|State court| L1["Apply the rendering State's preclusion law: 28 USC 1738"]
    B -->|Federal question| L2["Apply federal preclusion law"]
    B -->|Federal diversity| L3["Federal common law adopting the forum State's law: Semtek"]
    L1 --> C
    L2 --> C
    L3 --> C
    C{"Valid final judgment on the merits? California: appeal finished or time to appeal expired"} -- No --> NO["No preclusion yet"]
    C -- Yes --> D{"Same claim? Federal: same transaction. California: same primary right"}
    D -- Yes --> E{"Same parties or privies, same alignment?"}
    E -- Yes --> CP["Claim preclusion bars the second suit"]
    E -- No --> F
    D -- No --> F{"Same issue actually litigated, decided and essential to the first judgment?"}
    F -- No --> NO2["No preclusion"]
    F -- Yes --> G{"Party to be bound was a party or privy with a full and fair opportunity?"}
    G -- No --> NO2
    G -- Yes --> H{"Non-mutual offensive use?"}
    H -- Yes --> I["Parklane fairness factors decide"]
    H -- No --> IP["Issue preclusion applies"]
```

## 10. Can this order be appealed now? (R-CIV-099 to R-CIV-101, R-CIV-118)

```mermaid
flowchart TD
    A["District court order"] --> B{"Final decision ending the case on the merits?"}
    B -- Yes --> AP["Appeal under 1291 within 30 days"]
    B -- No --> C{"Rule 54 b judgment with no-just-reason-for-delay finding?"}
    C -- Yes --> AP
    C -- No --> D{"Order granting, refusing, modifying or dissolving an injunction?"}
    D -- Yes --> AP2["Appeal under 1292 a 1"]
    D -- No --> E{"Class certification order?"}
    E -- Yes --> AP3["Petition under Rule 23 f within 14 days"]
    E -- No --> F{"Judge certified controlling question of law under 1292 b?"}
    F -- Yes --> AP4["Apply to court of appeals within 10 days; discretionary"]
    F -- No --> G{"Collateral order: conclusive, separate from merits, effectively unreviewable later?"}
    G -- Yes --> AP5["Immediate appeal, e.g. qualified immunity denial"]
    G -- No --> H["Wait for final judgment; mandamus only for clear abuse"]
```
