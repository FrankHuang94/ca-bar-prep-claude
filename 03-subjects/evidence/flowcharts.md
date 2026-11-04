---
subject: EVD
topic: Evidence — decision trees (Mermaid)
coverage_ids: [EVD-MBE-I.D, EVD-MBE-I.D.3, EVD-MBE-II.A, EVD-MBE-II.C, EVD-MBE-II.D, EVD-MBE-III.A, EVD-MBE-III.B, EVD-MBE-IV.A, EVD-MBE-V.A, EVD-MBE-V.L, EVD-SUP-002, EVD-SUP-009]
tested_on: [MBE, essay]
exam_frequency: {level: high, basis: "Essays: 15 of 31 administrations 2012-02 to 2026-07 (48%); MBE: 25 scored questions every exam"}
last_verified: 2026-11-04
status: draft
---

# Evidence — flowcharts

Each chart cites the rule blocks in [rule-statements.md](rule-statements.md). Labels avoid parentheses and inner quotation marks so the diagrams render in any Mermaid viewer. "CEC" means the California Evidence Code.

## 1. The item-by-item sequence (R-EVD-001 to R-EVD-008)

```mermaid
flowchart TD
    A["Item of evidence offered"] --> B{"Which law does the call name?"}
    B -- FRE --> C["Apply FRE; note CEC only if asked to compare"]
    B -- CEC --> D{"Criminal case?"}
    D -- Yes --> P8["Truth-in-Evidence: relevant evidence admissible unless hearsay, privilege, 352, 782, 1103 or a two-thirds statute excludes it"]
    D -- No --> C2["Apply the CEC as written"]
    C --> R
    P8 --> R
    C2 --> R
    R{"Logically relevant: any tendency to prove a fact of consequence?"} -- No --> X["Exclude"]
    R -- Yes --> S{"Probative value substantially outweighed by unfair prejudice, confusion or waste? FRE 403 or CEC 352"}
    S -- Yes --> X
    S -- No --> T["Check character, policy exclusions and privileges"]
    T --> U["Check witness issues: competency, personal knowledge, opinion, form"]
    U --> V["If a writing or object: authentication, then best evidence or secondary evidence rule"]
    V --> W["If an out-of-court statement offered for truth: hearsay analysis for each layer"]
    W --> Y{"Criminal case and testimonial statement offered by prosecution?"}
    Y -- Yes --> Z["Confrontation Clause analysis"]
    Y -- No --> L["Limiting instruction on request; conclude"]
    Z --> L
```

## 2. Is it hearsay, and is it admissible? (R-EVD-083 to R-EVD-109)

```mermaid
flowchart TD
    A["Out-of-court words or conduct"] --> B{"Is it a statement: an assertion by a person, or conduct intended as an assertion?"}
    B -- No --> NH["Not hearsay: machine output, non-assertive conduct; check authentication"]
    B -- Yes --> C{"Offered to prove the truth of the matter asserted?"}
    C -- No --> NP["Not hearsay: verbal act, effect on listener, notice, circumstantial state of mind, impeachment; give limiting instruction"]
    C -- Yes --> D{"Declarant testifies and is subject to cross about a prior statement?"}
    D -- Yes --> E["Prior inconsistent, prior consistent or identification: FRE 801 d 1 or CEC 1235 to 1238"]
    D -- No --> F{"Offered against the party who made, adopted, authorized it, or whose employee or coconspirator made it?"}
    F -- Yes --> G["Party admission: FRE 801 d 2 or CEC 1220 to 1224; employee rule narrower in CEC"]
    F -- No --> H{"Fits an 803 or CEC exception not needing unavailability? PSI, excited, state of mind, medical, recorded recollection, business, public, treatise"}
    H -- Yes --> I["Admissible under that exception; note CEC gaps: no general PSI, medical, treatise"]
    H -- No --> J{"Declarant unavailable?"}
    J -- Yes --> K{"Former testimony, against interest, dying declaration, forfeiture, or CEC 1370?"}
    K -- Yes --> I
    K -- No --> M
    J -- No --> M{"FRE only: residual exception 807 with trustworthiness, necessity and notice?"}
    M -- Yes --> I
    M -- No --> X["Inadmissible hearsay"]
    I --> Z["Repeat for every layer, then confrontation if criminal"]
    E --> Z
    G --> Z
```

## 3. Character evidence (R-EVD-035 to R-EVD-046)

```mermaid
flowchart TD
    A["Evidence of a person's trait or prior acts"] --> B{"Is character itself an element: defamation, negligent entrustment, custody, entrapment?"}
    B -- Yes --> IN["Character in issue: any method including specific acts"]
    B -- No --> C{"Offered to attack or support a witness's credibility?"}
    C -- Yes --> IMP["Use impeachment rules: 608, 609 or CEC 786 to 788 and Prop 8"]
    C -- No --> D{"Offered for a non-propensity purpose such as motive, intent, identity, plan, knowledge, absence of mistake?"}
    D -- Yes --> OA["404 b or CEC 1101 b: proof sufficient for jury, Ewoldt similarity, 403 or 352, limiting instruction, notice under FRE"]
    D -- No --> E{"Sexual-assault or child-molestation case? Or CEC domestic-violence case?"}
    E -- Yes --> PR["Propensity allowed: FRE 413 to 415 or CEC 1108, 1109, subject to 403 or 352"]
    E -- No --> F{"Criminal case and the accused offers his own or the victim's pertinent trait?"}
    F -- Yes --> MR["Mercy rule: reputation or opinion; CEC 1103 allows specific acts for the victim; prosecution may rebut and show defendant's same trait"]
    F -- No --> G{"Homicide and defense claims victim was first aggressor? FRE only"}
    G -- Yes --> PC["Prosecution may show victim's peacefulness"]
    G -- No --> X["Inadmissible propensity evidence"]
```

## 4. Impeachment by prior conviction (R-EVD-025, R-EVD-026)

```mermaid
flowchart TD
    A["Witness has a prior conviction"] --> B{"Which law?"}
    B -- FRE --> C{"More than 10 years since conviction or release, whichever later?"}
    C -- Yes --> C1["Admit only if probative value substantially outweighs prejudice, with written notice"]
    C -- No --> D{"Elements required a dishonest act or false statement?"}
    D -- Yes --> D1["Must admit, felony or misdemeanor"]
    D -- No --> E{"Punishable by more than one year?"}
    E -- No --> E1["Not admissible under 609"]
    E -- Yes --> F{"Is the witness the criminal defendant?"}
    F -- Yes --> F1["Admit only if probative value outweighs prejudice to the defendant"]
    F -- No --> F2["Admit unless excluded under 403"]
    B -- CEC --> G{"Criminal case?"}
    G -- Yes --> H{"Felony involving moral turpitude, judged by least adjudicated elements?"}
    H -- Yes --> H1["Admissible subject to 352: honesty, remoteness, similarity, effect on testifying"]
    H -- No --> H2{"Misdemeanor conduct involving moral turpitude?"}
    H2 -- Yes --> H3["Conduct admissible under Wheeler subject to 352; conviction record is hearsay unless excepted"]
    H2 -- No --> X1["Not admissible to impeach"]
    G -- No --> I{"Felony?"}
    I -- Yes --> I1["Civil: admissible under 788 subject to 352"]
    I -- No --> X1
```

## 5. Privilege analysis (R-EVD-062 to R-EVD-072)

```mermaid
flowchart TD
    A["Testimony or document sought"] --> B{"Which privilege law? FRE 501 common law, state law for state-law civil claims, or CEC statutes"}
    B --> C{"Communication or relationship covered: lawyer, spouse, physician, psychotherapist, clergy?"}
    C -- No --> X["No privilege"]
    C -- Yes --> D{"Confidential, and made for the protected purpose?"}
    D -- No --> X
    D -- Yes --> E{"Who is the holder, and is the holder asserting it?"}
    E --> F{"Exception: crime-fraud, breach of duty, joint clients, patient-litigant, dangerous patient, crimes against spouse or child, CEC 956.5, CEC physician privilege in criminal case?"}
    F -- Yes --> X
    F -- No --> G{"Waived by voluntary disclosure of a significant part or consent? FRE 502 or CEC 912"}
    G -- Yes --> X
    G -- No --> P["Privileged: exclude; CEC 913 no comment"]
    A --> S{"Spouse called against spouse?"}
    S -- Yes --> T["Testimonial privilege: FRE criminal only, witness spouse holds; CEC 970 and 971 all cases"]
```

## 6. Best evidence rule and California secondary evidence rule (R-EVD-078 to R-EVD-081)

```mermaid
flowchart TD
    A["Evidence about a writing, recording or photograph"] --> B{"Is the content being proved: operative document or knowledge from the writing?"}
    B -- No --> N["Rule does not apply; independent knowledge is fine"]
    B -- Yes --> C["Authenticate first: FRE 901 or CEC 1400 and 1401"]
    C --> D{"Which law?"}
    D -- FRE --> E{"Original or duplicate offered?"}
    E -- Original --> OK["Admissible on this ground"]
    E -- Duplicate --> F{"Genuine question of authenticity or unfairness?"}
    F -- No --> OK
    F -- Yes --> G{"Excuse under 1004: lost without bad faith, unobtainable, opponent controls after notice, collateral?"}
    E -- Other evidence --> G
    G -- Yes --> OK
    G -- No --> X["Exclude"]
    D -- CEC --> H{"Secondary evidence such as a copy?"}
    H -- Copy --> I{"Genuine dispute on material terms and justice requires exclusion, or unfair? Criminal: 1522"}
    I -- No --> OK
    I -- Yes --> X
    H -- Oral testimony --> J{"1523 exception: lost without fraud, not procurable, collateral, numerous accounts?"}
    J -- Yes --> OK
    J -- No --> X
```

## 7. Confrontation Clause (R-EVD-110 to R-EVD-114)

```mermaid
flowchart TD
    A["Prosecution offers an out-of-court statement against the accused"] --> B{"Offered for its truth? Expert basis counts if the opinion depends on it"}
    B -- No --> OKC["No confrontation issue; check hearsay and limiting instruction"]
    B -- Yes --> C{"Testimonial: primary purpose to prove past events for prosecution?"}
    C -- No --> OKC2["No confrontation issue: ongoing emergency, statements to friends or teachers, business records"]
    C -- Yes --> D{"Declarant testifies at trial and is subject to cross?"}
    D -- Yes --> OKC3["Clause satisfied"]
    D -- No --> E{"Declarant unavailable and defendant had a prior opportunity to cross-examine?"}
    E -- Yes --> OKC3
    E -- No --> F{"Defendant wrongfully caused unavailability intending to prevent testimony?"}
    F -- Yes --> OKC4["Forfeited: Giles"]
    F -- No --> G{"Dying declaration?"}
    G -- Yes --> OKC5["Historical exception, dictum"]
    G -- No --> X["Barred by Crawford even if a hearsay exception applies"]
    A --> J{"Joint trial with a nontestifying codefendant's confession?"}
    J -- Yes --> K["Bruton: facially incriminating barred; neutral redaction plus instruction allowed under Richardson and Samia"]
```

## 8. Expert testimony (R-EVD-054 to R-EVD-061)

```mermaid
flowchart TD
    A["Proposed expert opinion"] --> B{"Qualified by knowledge, skill, experience, training or education on this subject?"}
    B -- No --> X["Exclude"]
    B -- Yes --> C{"Helpful: beyond common experience?"}
    C -- No --> X
    C -- Yes --> D{"Which law?"}
    D -- FRE --> E{"Proponent shows by a preponderance: sufficient facts, reliable method, reliable application? Daubert factors"}
    E -- No --> X
    E -- Yes --> F{"Criminal case opinion on defendant's mental-state element?"}
    F -- Yes --> X2["Barred by 704 b; describe diagnosis only"]
    F -- No --> OK["Admissible; inadmissible bases disclosed only on reverse 403"]
    D -- CEC --> G{"New scientific technique?"}
    G -- Yes --> H{"Kelly: general acceptance, qualified witness, correct procedures?"}
    H -- No --> X
    H -- Yes --> I
    G -- No --> I{"Sargon: reasonable basis, logical support, not speculative?"}
    I -- No --> X
    I -- Yes --> J{"Relates case-specific hearsay as true?"}
    J -- Yes --> X3["Sanchez: only if independently proven or excepted; Crawford if testimonial"]
    J -- No --> OK2["Admissible; Pen. Code 29 bars mental-state opinions in guilt phase"]
```
