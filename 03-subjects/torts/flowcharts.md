---
subject: TRT
topic: Torts — decision-tree flowcharts (Mermaid)
coverage_ids: [TRT-MBE-I.B, TRT-MBE-II, TRT-MBE-II.A, TRT-MBE-II.D.3, TRT-MBE-II.E.2, TRT-MBE-II.E.3, TRT-MBE-II.F, TRT-MBE-II.G.2, TRT-MBE-III, TRT-MBE-IV.B]
tested_on: [MBE, essay]
exam_frequency: {level: high, basis: "Essays: 12 of 31 administrations 2012-02 to 2026-07 (39%); MBE: 25 scored questions every exam"}
last_verified: 2026-11-05
status: verified
---

# Torts — flowcharts

Nine decision trees for the analyses you will run most often. Rule IDs point to [`rule-statements.md`](rule-statements.md). "CA" boxes show where California departs from the majority/MBE rule ([`ca-distinctions.md`](ca-distinctions.md)).

## 1. Negligence master flow (R-TRT-018 to R-TRT-046)

```mermaid
flowchart TD
    A["Plaintiff injured by defendant's careless conduct"] --> D{"Duty? Foreseeable plaintiff; special rules for failure to act, land, emotional harm, economic loss"}
    D -->|No duty| N1["No negligence claim"]
    D -->|Duty| S{"Standard of care: reasonable person, child, professional, carrier, statute"}
    S --> B{"Breach? Risk-utility, custom, negligence per se, res ipsa"}
    B -->|No| N2["No liability"]
    B -->|Yes| C{"But-for cause, or substantial factor for multiple causes?"}
    C -->|No| N3["No liability"]
    C -->|Yes| P{"Proximate cause: foreseeable type of harm and no superseding cause?"}
    P -->|No| N4["No liability"]
    P -->|Yes| H{"Actual damages: physical injury or property damage?"}
    H -->|No| X["Only special rules: NIED, economic loss"]
    H -->|Yes| DEF{"Defenses: comparative fault, assumption of risk, immunity, limitations"}
    DEF --> R["Liability, reduced by plaintiff's percentage of fault"]
```

## 2. Is there a duty to act or to protect from a third person? (R-TRT-021 to R-TRT-023)

```mermaid
flowchart TD
    A["Harm came from defendant's failure to act or from a third person"] --> M{"Is it really misfeasance - defendant's own risky act?"}
    M -->|Yes| G["Ordinary duty of reasonable care"]
    M -->|No - nonfeasance| R{"Special relationship with plaintiff or with the dangerous person?"}
    R -->|Yes| CA1{"CA: do the Rowland factors limit the duty - Brown two-step?"}
    CA1 -->|No| DUTY["Duty to take reasonable protective steps"]
    CA1 -->|Yes| ND["No duty"]
    R -->|No| P{"Did defendant create the peril?"}
    P -->|Yes| DUTY
    P -->|No| U{"Did defendant voluntarily undertake to help, causing reliance or increased risk?"}
    U -->|Yes| DUTY2["Duty to act reasonably in the undertaking"]
    U -->|No| S{"Statute or contract requires action?"}
    S -->|Yes| DUTY
    S -->|No| ND2["No duty - no liability for failing to rescue"]
    DUTY --> T{"Therapist and patient threat?"}
    T -->|Yes| TAR["Tarasoff; CA Civil Code 43.92: communicated serious threat, identifiable victim; warn victim and police"]
```

## 3. Land entrants (R-TRT-047 to R-TRT-051)

```mermaid
flowchart TD
    A["Entrant injured by condition or activity on land"] --> CA{"California essay?"}
    CA -->|Yes| ROW["Rowland: reasonable care to all entrants; status is a factor; check Civil Code 846 recreational use"]
    CA -->|No - majority or MBE| Q{"Entrant's status?"}
    Q -->|Trespasser| T{"Discovered or anticipated?"}
    T -->|No| T1["Only refrain from willful or wanton harm"]
    T -->|Yes| T2["Warn of known, concealed, artificial, deadly conditions; reasonable care in activities"]
    Q -->|Child trespasser| AN{"All five attractive nuisance factors met?"}
    AN -->|Yes| AN1["Reasonable care as to the artificial condition"]
    AN -->|No| T
    Q -->|Licensee - social guest| L["Warn of known concealed dangers; no duty to inspect"]
    Q -->|Invitee - customer or public| I["Inspect, discover, warn or repair"]
    I --> SC{"Stayed within scope of invitation?"}
    SC -->|No| L
```

## 4. Emotional distress without physical injury (R-TRT-054 to R-TRT-057)

```mermaid
flowchart TD
    A["Plaintiff suffers emotional distress, no physical impact"] --> I{"Defendant acted intentionally or recklessly with outrageous conduct?"}
    I -->|Yes| IIED["IIED: severe distress; third parties present under 46 subsection 2"]
    I -->|No - negligence| Z{"Plaintiff in the zone of physical danger?"}
    Z -->|Yes| ZD["Recovery; many states require physical manifestation"]
    Z -->|No| DV{"Duty owed directly to plaintiff: assumed, by law, or relationship such as doctor and patient?"}
    DV -->|Yes| BURG["Direct victim recovery - CA Burgess and Molien"]
    DV -->|No| BY{"Bystander: closely related, present and aware of injury-causing event, serious distress?"}
    BY -->|All three| THING["Recovery under Thing v. La Chusa"]
    BY -->|Missing one| NO["No recovery; note Elden cohabitant rule is under review"]
```

## 5. Products liability - strict liability analysis (R-TRT-081 to R-TRT-087)

```mermaid
flowchart TD
    A["Injury from a product"] --> S{"Defendant a commercial seller in the chain: maker, component maker, distributor, retailer, lessor?"}
    S -->|No - casual seller or service| NEG["Use negligence or warranty only"]
    S -->|Yes| D{"Type of defect?"}
    D -->|Unit differs from design| MD["Manufacturing defect - liable even with all possible care"]
    D -->|Whole line dangerous| DD{"Consumer expectations test or risk-benefit?"}
    DD --> CE["Ordinary consumer's safety expectations for everyday products - CA Soule limit"]
    DD --> RB["Risks outweigh benefits; feasible alternative; CA Barker shifts burden to defendant"]
    D -->|No adequate warning| WD["Knowable risk; not obvious; learned intermediary for drugs"]
    MD --> C{"Defect existed when it left defendant; caused physical injury or other property damage?"}
    CE --> C
    RB --> C
    WD --> C
    C -->|No| NL["No strict liability; consider warranty for economic loss"]
    C -->|Yes| DF{"Defenses: unforeseeable misuse, alteration, assumption of risk, comparative fault"}
    DF --> OUT["Liability, reduced by plaintiff's fault; retailer may seek indemnity from manufacturer"]
```

## 6. Defamation: which fault and damages rules? (R-TRT-096 to R-TRT-100)

```mermaid
flowchart TD
    A["False defamatory statement of fact, of and concerning plaintiff, published"] --> P{"Plaintiff a public official or public figure?"}
    P -->|Yes| AM["Plaintiff proves falsity and actual malice by clear and convincing evidence"]
    P -->|No| PC{"Matter of public concern?"}
    PC -->|Yes| G["Plaintiff proves falsity and at least negligence; presumed or punitive damages need actual malice - Gertz"]
    PC -->|No| DB["Common law: presumed and punitive damages without actual malice - Dun and Bradstreet"]
    AM --> F{"Libel or slander?"}
    G --> F
    DB --> F
    F -->|Libel| LB["General damages presumed; CA 45a: special damages if not defamatory on its face"]
    F -->|Slander| SL{"Per se category: crime, loathsome disease, business, sexual misconduct?"}
    SL -->|Yes| SP["General damages presumed"]
    SL -->|No| SD["Special damages required"]
    LB --> DEF["Defenses: truth, opinion, absolute and qualified privileges - CA Civil Code 47; retraction 48a"]
    SP --> DEF
    SD --> DEF
```

## 7. Apportionment among multiple defendants (R-TRT-041 to R-TRT-043, R-TRT-070)

```mermaid
flowchart TD
    A["Two or more defendants caused plaintiff's harm"] --> DIV{"Harm divisible with reasonable basis to apportion?"}
    DIV -->|Yes| SEP["Each pays only for the harm it caused"]
    DIV -->|No - indivisible| PF["Reduce total by plaintiff's percentage of fault - pure comparative"]
    PF --> J{"Which jurisdiction?"}
    J -->|MBE default| JS["Joint and several: plaintiff collects all from any defendant"]
    J -->|California| P51["Economic damages joint and several; non-economic damages several by percentage - Prop 51"]
    JS --> CON["Paying defendant seeks contribution by fault share"]
    P51 --> CON2["Comparative equitable indemnity; good faith settlement bars claims against settlor - CCP 877"]
```

## 8. Assumption of risk and sports injuries (R-TRT-071 to R-TRT-073)

```mermaid
flowchart TD
    A["Plaintiff hurt in risky activity"] --> E{"Signed a release?"}
    E -->|Yes| V{"Clear, covers negligence, no public interest under Tunkl, not gross negligence or intentional?"}
    V -->|Yes| BAR1["Express assumption bars the negligence claim"]
    V -->|No| IMP
    E -->|No| IMP{"California essay?"}
    IMP -->|No - majority or MBE| K{"Plaintiff knew the specific risk and voluntarily encountered it?"}
    K -->|Yes| CF["Implied assumption: reduces recovery as comparative fault"]
    K -->|No| NEG["Ordinary negligence analysis"]
    IMP -->|Yes| INH{"Risk inherent in the sport or recreational activity?"}
    INH -->|Yes| ROLE{"Defendant's role?"}
    ROLE -->|Co-participant| CP["Liable only for intentional injury or conduct totally outside the range of the sport"]
    ROLE -->|Coach or instructor| KH["Kahn: liable for intentional injury or reckless conduct outside ordinary coaching"]
    ROLE -->|Owner or operator| OW["No duty for inherent risks; duty not to increase them - Avila"]
    INH -->|No - risk created by defendant| SEC["Secondary assumption: comparative fault under Li"]
```

## 9. Vicarious liability (R-TRT-063 to R-TRT-067)

```mermaid
flowchart TD
    A["Tortfeasor acted for someone else"] --> E{"Employee - employer controls manner and means?"}
    E -->|Yes| SC{"Within scope: kind of work, time and space, purpose to serve; CA foreseeable outgrowth?"}
    SC -->|Yes| RS["Employer vicariously liable - respondeat superior"]
    SC -->|No - frolic or personal| DIR
    E -->|No - independent contractor| EX{"Exception: nondelegable duty, inherently dangerous work, apparent agency?"}
    EX -->|Yes| RS2["Hirer liable for contractor's negligence"]
    EX -->|No| DIR{"Hirer or employer itself negligent in hiring, supervising, entrusting?"}
    DIR -->|Yes| OWN["Direct liability for own negligence"]
    DIR -->|No| NONE["No liability of the principal"]
    RS2 --> PRV{"CA: injured person is the contractor's own employee?"}
    PRV -->|Yes| PRIV["Privette: hirer generally not liable unless retained control affirmatively contributed"]
```
