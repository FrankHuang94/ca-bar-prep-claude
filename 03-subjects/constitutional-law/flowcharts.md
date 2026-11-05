---
subject: CON
topic: Constitutional Law — decision flowcharts (Mermaid)
coverage_ids: [CON-MBE-I.C.1, CON-MBE-II.A.1, CON-MBE-II.B.4, CON-MBE-III.B.1, CON-MBE-IV.B, CON-MBE-IV.C, CON-MBE-IV.D, CON-MBE-IV.F.1, CON-MBE-IV.F.2]
tested_on: [MBE, essay]
exam_frequency: {level: high, basis: "Essays: 13 of 31 administrations 2012-02 to 2026-07 (42%); MBE: 25 scored questions every exam"}
last_verified: 2026-11-05
status: verified
---

# Constitutional Law — flowcharts

Rule IDs in each node point to [rule-statements.md](rule-statements.md).

## 1. Justiciability (run for each plaintiff)

```mermaid
flowchart TD
    A["Federal court suit"] --> B{"Injury in fact: concrete, particularized, actual or imminent? R-CON-009"}
    B -->|No| X1["Dismiss: no standing"]
    B -->|Yes| C{"Fairly traceable to defendant and likely redressed? R-CON-010"}
    C -->|No| X1
    C -->|Yes| D{"Asserting someone else's rights or suing as taxpayer, organization, state or intervenor? R-CON-011 to R-CON-014"}
    D -->|Yes| D2{"Special test met?"}
    D2 -->|No| X1
    D2 -->|Yes| E
    D -->|No| E{"Ripe: fit for decision and hardship if delayed? R-CON-015"}
    E -->|No| X2["Dismiss: not ripe"]
    E -->|Yes| F{"Still a live controversy? R-CON-016"}
    F -->|No| G{"Exception: repetition evading review, voluntary cessation, damages claim, class action?"}
    G -->|No| X3["Dismiss: moot"]
    G -->|Yes| H
    F -->|Yes| H{"Political question? R-CON-017"}
    H -->|Yes| X4["Dismiss: nonjusticiable"]
    H -->|No| I{"State itself sued for damages? R-CON-005"}
    I -->|Yes| X5["Barred unless waiver or valid abrogation; sue officer for prospective relief instead"]
    I -->|No| M["Reach the merits"]
```

## 2. Validity of a federal statute

```mermaid
flowchart TD
    A["Congress enacts a statute"] --> B{"Enumerated power? R-CON-020"}
    B --> C1["Commerce: channels, instrumentalities, substantial effects R-CON-021 R-CON-022"]
    B --> C2["Tax: revenue-raising, not a penalty R-CON-023"]
    B --> C3["Spending conditions: Dole five factors R-CON-024"]
    B --> C4["Section 5: congruent and proportional, state actors only R-CON-027"]
    B --> C5["Other: war, treaty, property, immigration R-CON-025 R-CON-026 R-CON-030"]
    C1 --> D{"Any power fits?"}
    C2 --> D
    C3 --> D
    C4 --> D
    C5 --> D
    D -->|No| X1["Invalid: beyond federal power"]
    D -->|Yes| E{"Commands state legislature or officers? R-CON-046"}
    E -->|Yes| X2["Invalid: commandeering"]
    E -->|No| F{"Violates separation of powers: legislative veto, line-item veto, congressional appointment or removal? R-CON-035 to R-CON-039"}
    F -->|Yes| X3["Invalid"]
    F -->|No| G{"Violates an individual right? Go to chart 4"}
    G -->|Yes| X4["Invalid as applied or on its face"]
    G -->|No| OK["Valid"]
```

## 3. State law that affects interstate business

```mermaid
flowchart TD
    A["State or local law affecting commerce"] --> B{"Valid federal law on point? R-CON-051"}
    B -->|Express, field or conflict| X1["Preempted"]
    B -->|No preemption| C{"Congress clearly authorized it? R-CON-052"}
    C -->|Yes| C2["DCC claim fails; still check equal protection and P and I"]
    C -->|No| D{"State acting as market participant or favoring its own public entity? R-CON-049"}
    D -->|Yes| D2["DCC does not apply; still check Article IV P and I for individuals"]
    D -->|No| E{"Discriminates against out-of-state commerce on face, purpose or effect? R-CON-047"}
    E -->|Yes| F{"Legitimate local purpose and no reasonable nondiscriminatory alternative?"}
    F -->|No| X2["Invalid under DCC"]
    F -->|Yes| OK1["Valid, rare: Maine v. Taylor"]
    E -->|No| G{"Pike: burden clearly excessive compared with local benefits? R-CON-048"}
    G -->|Yes| X2
    G -->|No| OK2["Valid under DCC"]
    C2 --> H
    D2 --> H
    OK1 --> H
    OK2 --> H{"Individual out-of-state citizen denied a fundamental right such as livelihood? R-CON-053"}
    H -->|Yes| I{"Substantial reason and substantial relationship?"}
    I -->|No| X3["Invalid under Article IV P and I"]
    I -->|Yes| OK3["Valid"]
    H -->|No| OK3
```

## 4. Individual rights: choosing the test

```mermaid
flowchart TD
    A["Government action burdens a person"] --> B{"State action? R-CON-054 R-CON-055"}
    B -->|No| X1["No constitutional claim, except Thirteenth Amendment"]
    B -->|Yes| C{"Which right?"}
    C --> S["Speech, religion, association: chart 6 or 7"]
    C --> T["Property taken: chart 8"]
    C --> P["Procedure before deprivation: chart 9"]
    C --> G["Arms: text, then historical tradition R-CON-065"]
    C --> E{"Classification or fundamental right?"}
    E --> F1{"Race, national origin, state alienage, or fundamental right burdened?"}
    F1 -->|Yes| SS["Strict scrutiny: compelling interest, narrowly tailored; government burden"]
    F1 -->|No| F2{"Sex or nonmarital birth?"}
    F2 -->|Yes| IS["Intermediate: important interest, substantially related; government burden"]
    F2 -->|No| RB["Rational basis: legitimate interest, rationally related; challenger burden"]
    RB --> AN{"Evidence of animus toward a group?"}
    AN -->|Yes| X2["Fails even rational basis"]
    AN -->|No| OK["Usually valid"]
```

## 5. Equal protection: is there a suspect classification?

```mermaid
flowchart TD
    A["Law treats people differently"] --> B{"Classification on the face of the law? R-CON-067"}
    B -->|Yes| T["Apply tier for that class"]
    B -->|No| C{"Neutral law applied in a discriminatory way?"}
    C -->|Yes| T
    C -->|No| D{"Disparate impact plus discriminatory purpose shown by Arlington Heights factors?"}
    D -->|Yes| T
    D -->|No| RB["Rational basis R-CON-074"]
    T --> E{"Which class?"}
    E --> R1["Race or national origin: strict R-CON-068"]
    E --> R2["State alienage: strict unless political function R-CON-070"]
    E --> R3["Federal alienage: rational basis R-CON-070"]
    E --> R4["Sex: intermediate, exceedingly persuasive justification R-CON-071"]
    E --> R5["Nonmarital children: intermediate R-CON-073"]
    E --> R6["Age, disability, wealth, sexual orientation federally: rational basis R-CON-074"]
```

## 6. Free speech

```mermaid
flowchart TD
    A["Law restricts expression"] --> B{"Speech or expressive conduct? R-CON-105"}
    B -->|Conduct only| X0["No First Amendment issue"]
    B -->|Expressive conduct| OB{"Interest unrelated to message?"}
    OB -->|Yes| OBT["O'Brien test"]
    OB -->|No| CB
    B -->|Speech| U{"Unprotected category: incitement, true threat, fighting words, obscenity, child pornography? R-CON-097 to R-CON-099"}
    U -->|Yes, elements met| X1["May be regulated, but no viewpoint lines within category"]
    U -->|No| SET{"Special setting: school, employee, commercial, government speech, prison? R-CON-096 R-CON-101 to R-CON-104 R-CON-116"}
    SET -->|Yes| SP["Apply the setting test: Tinker, Pickering, Central Hudson, Summum, Turner"]
    SET -->|No| CB{"Content-based or viewpoint-based? R-CON-092"}
    CB -->|Yes| SS["Strict scrutiny R-CON-093"]
    CB -->|No| FO{"Forum type? R-CON-095"}
    FO -->|Traditional or designated| TPM["TPM: significant interest, narrowly tailored, ample alternatives R-CON-094"]
    FO -->|Limited or nonpublic| RV["Reasonable and viewpoint-neutral"]
    SS --> FA
    TPM --> FA
    RV --> FA
    SP --> FA
    OBT --> FA{"Facial problems: prior restraint, vagueness, overbreadth? R-CON-106 to R-CON-108"}
    FA -->|Yes| X2["Invalid on its face"]
    FA -->|No| END["Decide as applied"]
```

## 7. Religion clauses

```mermaid
flowchart TD
    A["Government action touching religion"] --> B{"Burdens religious practice?"}
    B -->|Yes| C{"Neutral: no targeting or hostility? R-CON-087"}
    C -->|No| SS["Strict scrutiny"]
    C -->|Yes| D{"Generally applicable: no individualized exemptions and no better treatment of comparable secular activity?"}
    D -->|No| SS
    D -->|Yes| E{"Religious exclusion from public benefit, or parental religious upbringing like Yoder? R-CON-088"}
    E -->|Yes| SS
    E -->|No| RB["Rational basis under Smith; check RFRA if federal or RLUIPA if institutionalized person or land use R-CON-089"]
    A --> F{"Government endorses, funds or sponsors religion?"}
    F -->|Yes| G{"Coercion to participate, or denominational preference? R-CON-090 R-CON-091"}
    G -->|Yes| X1["Establishment Clause violation, or strict scrutiny for preferences"]
    G -->|No| H{"Consistent with historical practice and understanding?"}
    H -->|Yes| OK["Valid: legislative prayer, longstanding monuments, private-choice aid"]
    H -->|No| X2["Likely invalid"]
```

## 8. Takings

```mermaid
flowchart TD
    A["Government action affecting property"] --> B{"Permanent physical occupation or government-authorized access or appropriation? R-CON-078"}
    B -->|Yes| PT["Per se taking"]
    B -->|No| C{"Permit conditioned on dedication or money? R-CON-080"}
    C -->|Yes| D{"Essential nexus and rough proportionality?"}
    D -->|No| PT
    D -->|Yes| OK1["No taking"]
    C -->|No| E{"All economically beneficial use eliminated? R-CON-079"}
    E -->|Yes| F{"Background nuisance or property law already barred the use?"}
    F -->|No| PT
    F -->|Yes| OK1
    E -->|No| G["Penn Central: economic impact, investment-backed expectations, character of action"]
    G --> H{"Goes too far?"}
    H -->|Yes| PT
    H -->|No| OK1
    PT --> I{"Public use? R-CON-077"}
    I -->|Yes| J["Just compensation: fair market value; temporary takings too R-CON-081"]
    I -->|No| X1["Taking invalid even with compensation"]
```

## 9. Procedural due process

```mermaid
flowchart TD
    A["Government deprives a person of something"] --> B{"Intentional government deprivation, not mere negligence? R-CON-057"}
    B -->|No| X1["No due process claim"]
    B -->|Yes| C{"Property: legitimate claim of entitlement under law or contract?"}
    C -->|Yes| E
    C -->|No| D{"Liberty: bodily freedom, parental rights, reputation plus loss of status?"}
    D -->|No| X1
    D -->|Yes| E["Mathews balance: private interest, risk of error and value of safeguards, government interest R-CON-058"]
    E --> F{"Was the process given enough? Notice, opportunity to be heard, neutral decisionmaker, right timing"}
    F -->|Yes| OK["Valid"]
    F -->|No| X2["Violation: order the process due; damages under 1983 if caused harm"]
```

## 10. Appointment and removal

```mermaid
flowchart TD
    A["Federal official"] --> B{"Officer: continuing position with significant authority? R-CON-035"}
    B -->|No| EM["Employee: Appointments Clause does not apply"]
    B -->|Yes| C{"Principal or inferior: supervised by a Senate-confirmed officer?"}
    C -->|Principal| D["Appointment: President with Senate consent"]
    C -->|Inferior| E["Appointment: may be vested in President, courts, or department heads"]
    D --> F{"Exercises executive power? R-CON-036"}
    F -->|Yes| G["President may remove at will; for-cause limits invalid after Slaughter, but Federal Reserve treated differently in Cook"]
    E --> H{"Removal limited to good cause by a principal officer, one layer only?"}
    H -->|Yes| OK["Valid under Morrison"]
    H -->|No, two layers| X1["Invalid under Free Enterprise Fund"]
    A --> I{"Does Congress itself appoint or remove, other than impeachment? R-CON-038"}
    I -->|Yes| X2["Invalid: Buckley, Bowsher"]
```
