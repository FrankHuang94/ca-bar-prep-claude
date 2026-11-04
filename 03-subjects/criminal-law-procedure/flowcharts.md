---
subject: CRM
topic: Criminal Law and Procedure — decision flowcharts (Mermaid)
coverage_ids: [CRM-MBE-I, CRM-MBE-I.B.3, CRM-MBE-III.A.1, CRM-MBE-III.A.2, CRM-MBE-IV.E, CRM-MBE-V.A, CRM-MBE-V.B, CRM-MBE-V.C, CRM-MBE-V.F]
tested_on: [MBE, essay]
exam_frequency: {level: high, basis: "Essays: 15 of 31 administrations 2012-02 to 2026-07 (48%); MBE: 25 scored questions every exam"}
last_verified: 2026-11-04
status: draft
---

# Criminal Law and Procedure — flowcharts

Rule IDs in each node point to [rule-statements.md](rule-statements.md). Run chart 1 for every death, chart 6 for every item of physical evidence, and chart 7 for every statement.

## 1. Homicide classification (run for each death)

```mermaid
flowchart TD
    A["Death of a human being"] --> B{"Defendant's act an actual and proximate cause? R-CRM-012 R-CRM-013"}
    B -->|No| X0["No homicide liability, consider attempt"]
    B -->|Yes| C{"Justified or excused: self-defense, defense of others, law enforcement? R-CRM-020 to R-CRM-026"}
    C -->|Yes| X1["Not guilty"]
    C -->|No| D{"Intent to kill?"}
    D -->|Yes| E{"Adequate provocation, no cooling time, or imperfect self-defense? R-CRM-034 R-CRM-023"}
    E -->|Yes| VM["Voluntary manslaughter"]
    E -->|No| F{"Premeditated and deliberate, or statutory means? R-CRM-033"}
    F -->|Yes| M1["First-degree murder"]
    F -->|No| M2["Second-degree murder"]
    D -->|No| G{"Intent to inflict serious bodily injury? R-CRM-035"}
    G -->|Yes| M2
    G -->|No| H{"Aware of and disregarded a very high risk to life? R-CRM-036"}
    H -->|Yes| M2
    H -->|No| I{"Killing during an inherently dangerous felony? Go to chart 2"}
    I -->|Felony murder applies| M3["Felony murder: first degree if enumerated felony"]
    I -->|No| J{"Criminal negligence, or killing during a malum in se misdemeanor? R-CRM-037 R-CRM-042"}
    J -->|Yes| IM["Involuntary manslaughter"]
    J -->|No| X2["No criminal homicide, civil negligence only"]
```

## 2. Felony murder

```mermaid
flowchart TD
    A["Death during a felony"] --> B{"Enumerated felony or inherently dangerous felony? R-CRM-039"}
    B -->|No| X1["No felony murder, check misdemeanor manslaughter or malice murder"]
    B -->|Yes| C{"Felony independent of the killing, not an assault? R-CRM-040"}
    C -->|No, merges| X1
    C -->|Yes| D{"Defendant guilty of the felony, with no defense?"}
    D -->|No| X1
    D -->|Yes| E{"Death during attempt, commission or flight before reaching temporary safety?"}
    E -->|No| X1
    E -->|Yes| F{"Who did the killing? R-CRM-041"}
    F -->|A felon| G["All co-felons liable if killing in furtherance and foreseeable"]
    F -->|Victim, police or bystander| H{"Jurisdiction rule?"}
    H -->|Agency, majority| X2["No felony murder, consider provocative act or malice murder"]
    H -->|Proximate cause, minority| I{"Victim killed was a co-felon?"}
    I -->|Yes| X3["Usually no liability even here"]
    I -->|No| G2["Felons liable if resistance was foreseeable"]
    G --> CA["California essay only if asked: actual killer, intent-to-kill aider, or major participant with reckless indifference R-CRM-043"]
```

## 3. Attempt

```mermaid
flowchart TD
    A["Crime not completed"] --> B{"Specific intent to commit the target crime? R-CRM-060"}
    B -->|No| X1["No attempt, target crime of recklessness or negligence cannot be attempted"]
    B -->|Yes| C{"Act beyond mere preparation? R-CRM-061"}
    C --> C1["Common law: dangerous proximity to completion"]
    C --> C2["MPC and majority: substantial step strongly corroborative of purpose"]
    C1 --> D{"Test met?"}
    C2 --> D
    D -->|No| X2["Mere preparation, consider solicitation or conspiracy"]
    D -->|Yes| E{"Impossibility claimed? R-CRM-062"}
    E -->|Factual or hybrid legal| F["No defense under modern rule, judge facts as defendant believed"]
    E -->|Pure legal: intended act is not a crime| X3["Defense"]
    E -->|None| F
    F --> G{"Abandonment? R-CRM-063"}
    G -->|Common law| H["No defense once beyond preparation"]
    G -->|MPC: complete and voluntary renunciation| X4["Affirmative defense"]
    G -->|None| H
    H --> I["Guilty of attempt, merges if target crime completed"]
```

## 4. Conspiracy and Pinkerton

```mermaid
flowchart TD
    A["Two or more people acting together"] --> B{"Agreement, express or inferred? R-CRM-065"}
    B -->|No| X1["No conspiracy, check accomplice liability R-CRM-069"]
    B -->|Yes| C{"Other party genuinely agreed, or an undercover agent or feigning?"}
    C -->|Feigning| D{"Bilateral or unilateral jurisdiction?"}
    D -->|Bilateral, common law| X2["No conspiracy, solicitation may apply R-CRM-064"]
    D -->|Unilateral, MPC| E
    C -->|Genuine| E{"Intent to agree and intent to achieve the object? R-CRM-066"}
    E -->|No| X1
    E -->|Yes| F{"Overt act required and present?"}
    F -->|Required but absent| X3["No conspiracy yet, withdrawal still possible"]
    F -->|Present or not required| G{"Wharton's rule or protected-class bar? R-CRM-068"}
    G -->|Yes| X4["No conspiracy"]
    G -->|No| H["Guilty of conspiracy, does not merge with target crime"]
    H --> I{"Other crimes by co-conspirators? R-CRM-067"}
    I --> J{"In furtherance, foreseeable, and before defendant withdrew?"}
    J -->|Yes| K["Liable under Pinkerton, not under MPC unless accomplice"]
    J -->|No| L["Not liable for that crime"]
```

## 5. Defenses to a charge

```mermaid
flowchart TD
    A["Defendant charged"] --> B{"Does a fact negate an element?"}
    B --> B1["Mistake of fact: honest for specific intent, reasonable for general intent R-CRM-010"]
    B --> B2["Voluntary intoxication: specific intent only R-CRM-018"]
    B --> B3["Mistake of law: only official reliance or element-negating R-CRM-011"]
    A --> C{"Justification?"}
    C --> C1["Self-defense: imminent threat, proportional force, aggressor and retreat rules R-CRM-020 to R-CRM-022"]
    C --> C2["Defense of others or property: no deadly force for property R-CRM-024 R-CRM-025"]
    C --> C3["Necessity: greater harm avoided, no alternative, not at fault R-CRM-027"]
    A --> D{"Excuse?"}
    D --> D1["Insanity: M'Naghten, irresistible impulse, MPC R-CRM-015"]
    D --> D2["Duress: threat of death or serious injury, not for murder R-CRM-028"]
    D --> D3["Involuntary intoxication, infancy R-CRM-018 R-CRM-019"]
    A --> E{"Government conduct?"}
    E --> E1["Entrapment: subjective predisposition test vs. objective test R-CRM-029"]
```

## 6. Fourth Amendment — one item of physical evidence

```mermaid
flowchart TD
    A["Item of evidence the defendant wants suppressed"] --> B{"Obtained by government or its agent? R-CRM-072"}
    B -->|No, private search| X1["Admissible"]
    B -->|Yes| C{"Defendant has standing: own REP or property interest? R-CRM-075"}
    C -->|No| X1
    C -->|Yes| D{"Search: REP invaded or physical trespass to gather information? R-CRM-073 R-CRM-074"}
    D -->|No: open fields, trash, public view, third-party records| X1
    D -->|Yes| E{"Valid warrant: probable cause, particularity, neutral magistrate, no Franks problem? R-CRM-082"}
    E -->|Yes| X1
    E -->|No warrant or defective| F{"Exception applies?"}
    F --> F1["Search incident to lawful arrest, Gant for cars, Riley for phones R-CRM-083"]
    F --> F2["Automobile with probable cause R-CRM-084"]
    F --> F3["Plain view R-CRM-085"]
    F --> F4["Consent by person with actual or apparent authority R-CRM-086"]
    F --> F5["Exigency or emergency aid R-CRM-087"]
    F --> F6["Terry stop and frisk, traffic stop R-CRM-077 to R-CRM-079"]
    F --> F7["Inventory, checkpoint, border, school, parolee R-CRM-088"]
    F1 --> G{"Any exception satisfied on these facts?"}
    F2 --> G
    F3 --> G
    F4 --> G
    F5 --> G
    F6 --> G
    F7 --> G
    G -->|Yes| X1
    G -->|No| H{"Exclusionary-rule limit? R-CRM-090 to R-CRM-092"}
    H --> H1["Independent source, inevitable discovery, attenuation"]
    H --> H2["Good-faith reliance on warrant, statute, precedent or database"]
    H --> H3["Knock-and-announce violation only"]
    H --> H4["Use limited to impeachment, grand jury, parole hearing"]
    H1 --> I{"Limit applies?"}
    H2 --> I
    H3 --> I
    H4 --> I
    I -->|Yes| X2["Admissible for that purpose"]
    I -->|No| X3["Suppress, California follows the same federal rule R-CRM-090"]
```

## 7. Statements — Miranda and related rights

```mermaid
flowchart TD
    A["Statement the defendant wants suppressed"] --> B{"Voluntary: no police coercion overbearing the will? R-CRM-093"}
    B -->|No| X1["Excluded for all purposes, including impeachment"]
    B -->|Yes| C{"Formal charges filed and police or agent deliberately elicited on the charged offense? R-CRM-102"}
    C -->|Yes, no valid waiver| X2["Excluded from case-in-chief under the Sixth Amendment, may impeach"]
    C -->|No| D{"Custody: reasonable person not free to leave, station-house pressures? R-CRM-094"}
    D -->|No| X3["Miranda does not apply, admissible"]
    D -->|Yes| E{"Interrogation: questions or words police should know are likely to elicit incrimination? R-CRM-095"}
    E -->|No, volunteered or booking| X3
    E -->|Yes| F{"Public-safety question? R-CRM-099"}
    F -->|Yes| X3
    F -->|No| G{"Adequate warnings given? R-CRM-096"}
    G -->|No| H{"Deliberate two-step with later warned statement? R-CRM-100"}
    H -->|Yes, no cure| X4["Both statements excluded from case-in-chief"]
    H -->|No| X5["Unwarned statement excluded from case-in-chief, usable to impeach, physical fruits admissible"]
    G -->|Yes| I{"Knowing, intelligent, voluntary waiver, express or implied?"}
    I -->|No| X5
    I -->|Yes| J{"Did suspect unambiguously invoke silence or counsel? R-CRM-097 R-CRM-098"}
    J -->|No| X3
    J -->|Silence| K{"Scrupulously honored: time, new warnings, new subject?"}
    K -->|Yes| X3
    K -->|No| X5
    J -->|Counsel| L{"Suspect reinitiated, or 14-day break from custody?"}
    L -->|Yes, with new waiver| X3
    L -->|No| X5
```

## 8. Identification evidence

```mermaid
flowchart TD
    A["Out-of-court identification"] --> B{"Live lineup or show-up after formal charges? R-CRM-106"}
    B -->|Yes| C{"Counsel present or validly waived?"}
    C -->|No| X1["Exclude lineup ID, in-court ID only with independent source by clear and convincing evidence"]
    C -->|Yes| D
    B -->|No: pre-charge or photo array| D{"Police-arranged procedure unnecessarily suggestive? R-CRM-107"}
    D -->|No| X2["Admissible, weight for the jury"]
    D -->|Yes| E{"Reliable anyway under Biggers factors: opportunity, attention, prior description, certainty, time?"}
    E -->|Yes| X2
    E -->|No| X3["Exclude, in-court ID only if independent source"]
```

## 9. Double jeopardy

```mermaid
flowchart TD
    A["Second prosecution or multiple punishment"] --> B{"Same sovereign? R-CRM-117"}
    B -->|No: state and federal, or two states| X1["No bar"]
    B -->|Yes| C{"Jeopardy attached in first proceeding: jury sworn, first witness sworn, or plea accepted? R-CRM-116"}
    C -->|No| X1
    C -->|Yes| D{"Same offense under Blockburger, or lesser-included?"}
    D -->|No| E{"Issue of ultimate fact already decided by acquittal? Ashe"}
    E -->|Yes| X2["Barred by collateral estoppel"]
    E -->|No| X1
    D -->|Yes| F{"How did the first proceeding end?"}
    F -->|Acquittal or conviction| X3["Barred, unless greater offense not yet complete"]
    F -->|Hung jury| X1
    F -->|Mistrial over objection| G{"Manifest necessity?"}
    G -->|Yes| X1
    G -->|No| X3
    F -->|Mistrial on defense motion| H{"Prosecution goaded the motion?"}
    H -->|Yes| X3
    H -->|No| X1
    F -->|Reversal on appeal| I{"Insufficient evidence?"}
    I -->|Yes| X3
    I -->|No| X1
```
