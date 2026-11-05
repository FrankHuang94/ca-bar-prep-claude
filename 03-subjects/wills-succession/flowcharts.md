---
subject: WIL
topic: Wills and Succession — decision-tree flowcharts (Mermaid)
coverage_ids: [WIL-CBX-I, WIL-CBX-II, WIL-CBX-II.C, WIL-CBX-III.x3, WIL-CBX-IV.x, WIL-CBX-interp.E, WIL-CBX-VI, WIL-CBX-VI.F, WIL-CBX-VII, WIL-CBX-VIII, WIL-SUP-002, WIL-SUP-006, WIL-PAST-001]
tested_on: [essay]
exam_frequency: {level: med, basis: "Essays: 13 of 31 administrations 2012-02 to 2026-07 (42%)"}
last_verified: 2026-11-05
status: draft
---

# Wills and Succession — flowcharts

Ten decision trees for the analyses that recur on California Wills essays. Rule IDs point to [`rule-statements.md`](rule-statements.md).

## 1. Estate map: where does each asset go?

```mermaid
flowchart TD
    A["Asset owned or claimed at death"] --> B{"Decedent married?"}
    B -- "Yes" --> C["Characterize: CP, QCP, SP - R-WIL-001"]
    C --> D["Survivor keeps own half of CP and half of decedent QCP"]
    C --> E["Decedent half of CP, half of own QCP, and SP stay in play"]
    B -- "No" --> E
    E --> F{"Nonprobate transfer? JT, POD, Totten, insurance, TOD deed, trust"}
    F -- "Yes" --> G["Passes by its own terms - R-WIL-099 to R-WIL-104"]
    G --> G2{"QCP given away with retained interest and no consent?"}
    G2 -- "Yes" --> G3["Spouse may recapture half - R-WIL-002"]
    F -- "No" --> H{"Valid unrevoked will covers it? See charts 2 and 4"}
    H -- "Yes" --> I["Distribute under will: charts 5 and 6"]
    H -- "No" --> J["Intestacy: chart 9"]
    I --> K{"Omitted spouse or child? Charts 7 and 8"}
```

## 2. Is the will validly executed?

```mermaid
flowchart TD
    A["Document offered as a will"] --> B{"Testamentary intent? Use extrinsic evidence - R-WIL-052"}
    B -- "No" --> X["Not a will"]
    B -- "Yes" --> C{"Executed elsewhere or testator domiciled elsewhere?"}
    C -- "Yes" --> C1{"Valid under place of execution, domicile, abode or nationality law?"}
    C1 -- "Yes" --> OK["Valid execution - R-WIL-053"]
    C1 -- "No" --> D
    C -- "No" --> D{"In writing and signed by testator or proxy in presence?"}
    D -- "No" --> H{"Holographic? Signature and material provisions handwritten"}
    D -- "Yes" --> E{"Two witnesses present at same time who understood it was a will?"}
    E -- "Yes" --> OK
    E -- "No" --> F{"Clear and convincing evidence testator intended it as will when signing?"}
    F -- "Yes" --> OK2["Valid under harmless error - R-WIL-048"]
    F -- "No" --> H
    H -- "Yes" --> H1{"Undated and inconsistent will or possible incapacity?"}
    H1 -- "No" --> OK3["Valid holograph - R-WIL-050"]
    H1 -- "Yes" --> H2["Invalid unless date or capacity proved - R-WIL-051"]
    H -- "No" --> X2["Invalid will: intestacy or prior will"]
    OK --> W{"Witness also a beneficiary?"}
    W -- "Yes" --> W1["Presumption unless two disinterested witnesses - R-WIL-049"]
```

## 3. Undue influence and related attacks

```mermaid
flowchart TD
    A["Gift to a person close to testator"] --> B{"Drafter, fiduciary who transcribed, or care custodian of dependent adult?"}
    B -- "Yes" --> B1{"Exception: relative within 4th degree, court order, charity, small gift, out of state, independent review certificate?"}
    B1 -- "No" --> B2["Statutory presumption, rebut by clear and convincing evidence, drafter conclusive - R-WIL-095"]
    B1 -- "Yes" --> C
    B -- "No" --> C{"Confidential relationship plus active procurement plus undue benefit?"}
    C -- "Yes" --> C1["Common-law presumption, burden shifts to proponent - R-WIL-040"]
    C -- "No" --> D["Contestant must prove undue influence directly"]
    C1 --> E["Weigh vulnerability, authority, tactics, inequity - R-WIL-039"]
    D --> E
    E --> F{"Free will overborne?"}
    F -- "Yes" --> G["Tainted gift fails, rest stands - R-WIL-038"]
    F -- "No" --> H["Gift valid"]
    B2 --> G2["If not rebutted, beneficiary treated as predeceased without issue - R-WIL-098"]
```

## 4. Revocation, revival and DRR

```mermaid
flowchart TD
    A["Was the will or a gift revoked?"] --> B{"Later valid will or codicil?"}
    B -- "Yes" --> B1["Revoked expressly or to extent inconsistent - R-WIL-077"]
    B -- "No" --> C{"Burned, torn, cancelled, obliterated or destroyed?"}
    C -- "Yes" --> C1{"By testator, or another in testator presence and at direction, with intent?"}
    C1 -- "Yes" --> C2["Revoked in whole or part - R-WIL-078"]
    C1 -- "No" --> NR["Not revoked, prove by copy"]
    C -- "No" --> D{"Original missing, last in testator possession, competent to death?"}
    D -- "Yes" --> D1["Presumed revoked, rebuttable - R-WIL-081"]
    D -- "No" --> E{"Divorce or annulment after will?"}
    E -- "Yes" --> E1["Gifts and nominations to ex-spouse revoked - R-WIL-082"]
    E -- "No" --> NR
    B1 --> R{"Revoking will later revoked?"}
    R -- "By physical act" --> R1["Earlier will revived only if circumstances or declarations show intent - R-WIL-084"]
    R -- "By third will" --> R2["Revived only if third will terms show intent"]
    C2 --> DRR{"Revocation based on mistaken belief that new gift or revival works?"}
    R1 --> DRR
    DRR -- "Yes" --> DRR1["Disregard revocation if closer to intent - R-WIL-085"]
    DRR -- "No" --> FIN["Revocation stands, intestacy or other will"]
```

## 5. Handwritten changes to a will

```mermaid
flowchart TD
    A["Words struck out and new words written in"] --> B{"Made by testator or at direction in presence?"}
    B -- "No" --> B1["No effect, original text stands if provable"]
    B -- "Yes" --> C{"New words plus signature in testator handwriting?"}
    C -- "Yes" --> C1["Valid holographic codicil - R-WIL-055"]
    C -- "No" --> D["New gift fails"]
    D --> E{"Strike-out made with intent to revoke?"}
    E -- "No" --> E1["Original gift stands"]
    E -- "Yes" --> F["Partial revocation by act - R-WIL-079"]
    F --> G{"Revocation conditional on new gift being valid?"}
    G -- "Yes" --> G1["DRR: original gift restored - R-WIL-085"]
    G -- "No" --> G2["Gift revoked, falls to residue"]
```

## 6. Lapse, anti-lapse and failed gifts

```mermaid
flowchart TD
    A["Beneficiary died before testator or before signing"] --> B{"Survival proved by clear and convincing evidence?"}
    B -- "Yes" --> OK["Gift passes to beneficiary estate"]
    B -- "No" --> C{"Will requires survival or gives substitute gift?"}
    C -- "Yes" --> F["Anti-lapse displaced - R-WIL-064"]
    C -- "No" --> D{"Beneficiary kindred of testator or of spouse or former spouse?"}
    D -- "No" --> F
    D -- "Yes" --> E{"Beneficiary left issue? Class member dead at signing and known?"}
    E -- "Issue, not excluded" --> E1["Issue take by representation - R-WIL-063"]
    E -- "No issue or excluded" --> F
    F --> G{"Alternative disposition in will?"}
    G -- "Yes" --> G1["Alternative taker"]
    G -- "No" --> H{"Failed gift residuary?"}
    H -- "No" --> H1["Falls into residue - R-WIL-065"]
    H -- "Yes" --> H2{"Other residuary takers?"}
    H2 -- "Yes" --> H3["Share to other residuary takers"]
    H2 -- "No" --> H4["Intestacy"]
```

## 7. Ademption, satisfaction and the conservator's sale

```mermaid
flowchart TD
    A["Gift under will"] --> B{"Specific gift? R-WIL-068"}
    B -- "No: general, demonstrative or residuary" --> B1["No ademption, check abatement - R-WIL-075"]
    B -- "Yes" --> C{"Item in estate at death?"}
    C -- "Yes" --> C1["Passes, subject to liens, no exoneration - R-WIL-073"]
    C -- "No" --> D{"Sold, condemned or insured by conservator, agent or trustee while incapacitated?"}
    D -- "Yes" --> D1["General pecuniary gift of net price or proceeds, unless conservatorship ended and T survived 1 year - R-WIL-074"]
    D -- "No" --> E{"Unpaid sale price, award, insurance or foreclosure at death?"}
    E -- "Yes" --> E1["Beneficiary takes unpaid amount - R-WIL-070"]
    E -- "No" --> F{"Securities changed by issuer action?"}
    F -- "Yes" --> F1["Beneficiary takes resulting securities - R-WIL-071"]
    F -- "No" --> G{"Traceable change in form and no intent to adeem?"}
    G -- "Yes" --> G1["No ademption under Mason - R-WIL-069"]
    G -- "No" --> G2["Gift adeemed"]
    A --> S{"Lifetime gift to beneficiary with writing or same property?"}
    S -- "Yes" --> S1["Satisfaction pro tanto - R-WIL-072"]
```

## 8. Omitted spouse

```mermaid
flowchart TD
    A["Surviving spouse not provided for"] --> B{"Married after execution of ALL wills, codicils and revocable trusts?"}
    B -- "No" --> X["Not omitted, spouse keeps own CP and QCP half only"]
    B -- "Yes" --> C{"Intent to omit appears on face of instruments?"}
    C -- "Yes" --> X2["No share - R-WIL-087"]
    C -- "No" --> D{"Transfer outside will intended in lieu?"}
    D -- "Yes" --> X2
    D -- "No" --> E{"Valid waiver under 140 to 147?"}
    E -- "Yes" --> X2
    E -- "No" --> CC{"Spouse was care custodian of dependent-adult decedent who died within 6 months of marriage?"}
    CC -- "Yes, no clear and convincing rebuttal" --> X2
    CC -- "No, or rebutted" --> F["Share: decedent half CP + half QCP + SP intestate share capped at one half - R-WIL-086"]
    F --> G["Funded from undisposed property, then pro rata - R-WIL-088"]
```

## 9. Omitted child

```mermaid
flowchart TD
    A["Child not provided for"] --> B{"Born or adopted after ALL testamentary instruments?"}
    B -- "No" --> B1{"Omitted only because believed dead or unknown?"}
    B1 -- "Yes" --> S["Intestate share - R-WIL-092"]
    B1 -- "No" --> X["No claim"]
    B -- "Yes" --> C{"Intent to omit on face of instruments?"}
    C -- "Yes" --> X2["No share - R-WIL-091"]
    C -- "No" --> D{"Decedent had a child and left substantially all to omitted child's other parent?"}
    D -- "Yes" --> X2
    D -- "No" --> E{"Transfer outside will in lieu?"}
    E -- "Yes" --> X2
    E -- "No" --> F["Intestate share of whole estate - R-WIL-090"]
    F --> G["Funded from undisposed property, then pro rata - R-WIL-088"]
```

## 10. Intestate distribution ladder

```mermaid
flowchart TD
    A["Intestate property"] --> B{"Surviving spouse or domestic partner?"}
    B -- "Yes" --> C["Spouse takes all CP and decedent half of QCP - R-WIL-016"]
    C --> D{"Decedent left issue?"}
    D -- "One child or line" --> D1["Spouse 1/2 SP, issue 1/2"]
    D -- "Two or more children or lines" --> D2["Spouse 1/3 SP, issue 2/3"]
    D -- "None" --> E{"Parent or parent issue?"}
    E -- "Yes" --> E1["Spouse 1/2 SP, parents, else siblings line 1/2"]
    E -- "No" --> E2["Spouse takes all SP"]
    B -- "No" --> F{"Issue?"}
    F -- "Yes" --> F1["Issue by representation - R-WIL-011"]
    F -- "No" --> G{"Parents?"}
    G -- "Yes" --> G1["Parents equally, unless barred - R-WIL-028"]
    G -- "No" --> H{"Issue of parents?"}
    H -- "Yes" --> H1["Siblings line by representation"]
    H -- "No" --> I{"Grandparents or their issue?"}
    I -- "Yes" --> I1["Grandparents, else their issue"]
    I -- "No" --> J{"Issue of predeceased spouse?"}
    J -- "Yes" --> J1["Stepchildren line"]
    J -- "No" --> K["Next of kin, then predeceased spouse parents line, then escheat - R-WIL-021"]
```
