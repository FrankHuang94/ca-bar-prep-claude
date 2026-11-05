---
subject: TRS
topic: Trusts — decision-tree flowcharts (Mermaid)
coverage_ids: [TRS-CBX-I, TRS-CBX-I.x, TRS-CBX-I.x2, TRS-CBX-I.J, TRS-CBX-III, TRS-CBX-IV, TRS-CBX-V, TRS-CBX-VIII, TRS-CBX-IX, TRS-CBX-XI, TRS-CBX-XII, TRS-SUP-001, TRS-SUP-002, TRS-SUP-003]
tested_on: [essay]
exam_frequency: {level: low, basis: "Essays: 7 of 31 administrations 2012-02 to 2026-07 (23%); usually tested with Wills"}
last_verified: 2026-11-04
status: draft
---

# Trusts — flowcharts

Eight decision trees for the analyses that recur on California Trusts essays. Rule IDs point to [`rule-statements.md`](rule-statements.md).

## 1. Was a valid express trust created?

```mermaid
flowchart TD
    A["Instrument, words or conduct said to create a trust"] --> B{"Settlor had capacity? R-TRS-003"}
    B -- "No" --> X["No trust; property stays with settlor or estate"]
    B -- "Yes" --> C{"Present intent to impose enforceable duties? R-TRS-004"}
    C -- "No, only precatory words" --> G["Outright gift to transferee - R-TRS-039"]
    C -- "Yes" --> D{"Existing, identifiable property transferred or declared? R-TRS-005"}
    D -- "No, expectancy or unfunded" --> D2{"Pour-over will or later funding? R-TRS-010"}
    D2 -- "No" --> X
    D2 -- "Yes" --> E
    D -- "Yes" --> E{"Lawful purpose? R-TRS-006"}
    E -- "No" --> RT["Trust fails in whole or part: resulting trust - R-TRS-036"]
    E -- "Yes" --> F{"Ascertainable beneficiary? R-TRS-018"}
    F -- "Yes" --> SOF{"Formalities met? Land needs writing; oral personalty needs clear and convincing proof; testamentary needs valid will"}
    F -- "No" --> F2{"Charitable purpose? R-TRS-019"}
    F2 -- "Yes" --> SOF
    F2 -- "No" --> F3{"Pet or honorary purpose? R-TRS-022, R-TRS-023"}
    F3 -- "Yes" --> SOF
    F3 -- "No" --> RT
    SOF -- "Yes" --> M{"Sole trustee is also sole beneficiary? R-TRS-008"}
    SOF -- "No" --> RT2["Express trust fails; check constructive trust - R-TRS-030 to R-TRS-032, R-TRS-038"]
    M -- "Yes" --> MX["Merger: no trust"]
    M -- "No" --> OK["Valid express trust; trustee vacancy is filled by the court - R-TRS-007"]
```

## 2. Was the trust revoked or amended? California after Haggerty

```mermaid
flowchart TD
    A["Settlor tries to revoke or amend"] --> B{"Instrument expressly says irrevocable?"}
    B -- "Yes" --> IRR["Go to chart 3: irrevocable trust"]
    B -- "No" --> C["California: revocable - R-TRS-011. Traditional rule: irrevocable unless power reserved"]
    C --> D{"Settlor alive and acting personally? R-TRS-016"}
    D -- "No, agent or conservator" --> D2{"Agent: trust instrument expressly permits? Conservator: court approval?"}
    D2 -- "No" --> FAIL["Attempt ineffective"]
    D2 -- "Yes" --> E
    D -- "Yes" --> E{"Complied with method stated in the instrument?"}
    E -- "Yes" --> VALID["Revocation or amendment valid"]
    E -- "No" --> F{"Instrument method explicitly exclusive?"}
    F -- "Yes" --> FAIL
    F -- "No" --> G{"Signed writing, not a will, delivered to trustee during life? R-TRS-012, R-TRS-014"}
    G -- "Yes" --> H{"Community property and an amendment?"}
    H -- "Yes" --> H2{"Both spouses joined or consented? R-TRS-015"}
    H2 -- "Yes" --> VALID
    H2 -- "No" --> FAIL
    H -- "No" --> VALID
    G -- "No, it is a will" --> W["Ineffective in CA unless trust permits revocation by will; argue UTC view - R-TRS-013"]
    G -- "No, not delivered" --> SD{"Settlor is sole trustee?"}
    SD -- "Yes" --> VALID2["Arguably valid: holding as trustee may count as delivery; unsettled - R-TRS-012"]
    SD -- "No" --> FAIL
```

## 3. Can an irrevocable trust be modified or terminated?

```mermaid
flowchart TD
    A["Request to modify or terminate"] --> B{"Settlor alive and consenting?"}
    B -- "Yes" --> C{"All beneficiaries consent?"}
    C -- "Yes, in writing" --> OK1["Modify or terminate without court; material purpose irrelevant - R-TRS-024"]
    C -- "No" --> C2{"Nonconsenting interests not substantially impaired?"}
    C2 -- "Yes" --> OK2["On petition by the others with settlor consent, court may modify or terminate - R-TRS-024"]
    C2 -- "No" --> E
    B -- "No" --> D{"All beneficiaries consent, incl. representation of minors and unborns?"}
    D -- "Yes" --> D2{"Material purpose remains? Spendthrift, support, age delay"}
    D2 -- "No" --> OK3["Court may terminate - R-TRS-025"]
    D2 -- "Yes" --> D3["Claflin: no. California: court balances reason vs. purpose; spendthrift trust ends only for good cause - R-TRS-025"]
    D -- "No" --> E{"Unforeseen circumstances defeat or impair purposes? R-TRS-026"}
    E -- "Yes" --> OK4["Court may modify administrative or dispositive terms, or terminate"]
    E -- "No" --> F{"Principal small relative to costs? R-TRS-027"}
    F -- "Yes" --> F2{"Principal at most 100,000 dollars and instrument silent?"}
    F2 -- "Yes" --> OK5["Trustee may terminate without court"]
    F2 -- "No" --> OK6["Petition court to terminate"]
    F -- "No" --> G{"Charitable purpose failed? Chart 7"}
    G -- "No" --> STAY["Trust continues on its terms"]
```

## 4. Can a creditor reach the trust?

```mermaid
flowchart TD
    A["Creditor seeks trust assets"] --> B{"Whose creditor?"}
    B -- "Settlor's" --> S1{"Trust revocable?"}
    S1 -- "Yes, settlor alive" --> S2["Reachable to extent of power to revoke - R-TRS-092"]
    S1 -- "Yes, settlor dead" --> S3["Reachable if probate estate inadequate - R-TRS-093"]
    S1 -- "No" --> S4{"Settlor also a beneficiary?"}
    S4 -- "Yes" --> S5["Self-settled: reach max trustee could pay settlor - R-TRS-047"]
    S4 -- "No" --> S6["Not reachable unless voidable transfer"]
    B -- "Beneficiary's" --> C{"Already paid to beneficiary?"}
    C -- "Yes" --> C1["Reachable like any property - R-TRS-042"]
    C -- "No" --> D{"Valid spendthrift clause? R-TRS-041"}
    D -- "No" --> D1{"Discretionary interest? R-TRS-048"}
    D1 -- "Yes" --> D2["Cannot compel distribution; trustee paying after notice of transfer or levy is liable to creditor - R-TRS-048"]
    D1 -- "No" --> D3["Creditor may reach the interest"]
    D -- "Yes" --> E{"Exception creditor?"}
    E -- "Child or spousal support" --> E1["Court may order payment - R-TRS-043"]
    E -- "Felony restitution" --> E2["Reachable - R-TRS-044"]
    E -- "Public support" --> E3["Reachable within statute - R-TRS-045"]
    E -- "General creditor" --> E4["CA: principal already due in full; up to 25 percent of future payments, reduced for support needs, with excess-over-support orders inside the same cap - R-TRS-042, R-TRS-046. General law: barred"]
```

## 5. Did the trustee breach a duty? Run once per act

```mermaid
flowchart TD
    A["Trustee act or omission"] --> R{"Trust revocable and settlor alive?"}
    R -- "Yes" --> R2["Duties owed to settlor; written direction is a defense; beneficiaries sue after death - R-TRS-065"]
    R -- "No" --> L{"Trustee personally interested? Buys, sells, borrows, invests in own business"}
    L -- "Yes" --> L2{"Authorized by instrument, informed consent, or court?"}
    L2 -- "No" --> LB["Loyalty breach; fair price no defense - R-TRS-053, R-TRS-055"]
    L2 -- "Yes" --> P
    L -- "No" --> P{"Investment decision?"}
    P -- "Yes" --> P2{"Prudent for portfolio and purposes; diversified; reviewed promptly? R-TRS-057, R-TRS-058"}
    P2 -- "No" --> PB["Prudence breach, judged without hindsight"]
    P2 -- "Yes" --> I
    P -- "No" --> I{"Favors one beneficiary or trust over another? R-TRS-056"}
    I -- "Yes" --> IB["Impartiality breach"]
    I -- "No" --> O{"Other duties: follow terms, preserve, earmark, inform, account, delegate? R-TRS-050 to R-TRS-063"}
    O -- "Breached" --> OB["Breach of that duty"]
    O -- "Met" --> NB["No breach"]
    LB --> REM["Chart 6: remedies"]
    PB --> REM
    IB --> REM
    OB --> REM
```

## 6. Remedies and liability after a breach

```mermaid
flowchart TD
    A["Breach established - R-TRS-078"] --> B{"Self-dealing?"}
    B -- "Yes" --> B1["Elect: rescind and recover property, or affirm and take profit - R-TRS-079"]
    B -- "No" --> C["Surcharge: loss plus interest, trustee profit, or lost profit - R-TRS-081"]
    B1 --> D{"Property traceable?"}
    C --> D
    D -- "Yes" --> D1{"Held by BFP for value without actual knowledge? R-TRS-095"}
    D1 -- "Yes" --> D2["BFP keeps it; pursue proceeds and trustee"]
    D1 -- "No" --> D3["Constructive trust if value rose; equitable lien if fell - R-TRS-080"]
    D -- "No" --> E["Personal money judgment against trustee"]
    D2 --> F
    D3 --> F
    E --> F{"Trustee defenses?"}
    F --> F1["Exculpatory clause: not for intentional, grossly negligent, bad-faith, reckless breach or profit - R-TRS-084"]
    F --> F2["Beneficiary consent or release with full knowledge - R-TRS-085"]
    F --> F3["Three years after adequate account, else discovery - R-TRS-086"]
    F --> F4["Court excuse for reasonable good-faith conduct - R-TRS-082"]
    F --> G["Also: remove trustee, cut compensation, liability of co-trustee or successor - R-TRS-073, R-TRS-083"]
```

## 7. Charitable trust and cy pres

```mermaid
flowchart TD
    A["Gift for a purpose"] --> B{"Charitable purpose benefiting public or indefinite class? R-TRS-019"}
    B -- "No" --> B2["Private, honorary or pet trust rules - R-TRS-018, R-TRS-022, R-TRS-023"]
    B -- "Yes" --> C["Valid charitable trust; may be perpetual; AG enforces - R-TRS-020"]
    C --> D{"Specific purpose now impossible, impracticable, illegal, or wasteful?"}
    D -- "No" --> D1["Carry out as written; deviation only for administrative terms - R-TRS-026"]
    D -- "Yes" --> E{"Gift over on failure stated?"}
    E -- "Yes" --> E1["Gift over takes"]
    E -- "No" --> F{"General charitable intent? Breadth of purpose, donor history, words"}
    F -- "Yes" --> G["Cy pres: court picks purpose as near as possible - R-TRS-021"]
    F -- "No" --> H["Trust fails: resulting trust to settlor or estate - R-TRS-036"]
    G --> G2{"Proposed new purpose close to original?"}
    G2 -- "No" --> G3["Court chooses a closer purpose"]
    G2 -- "Yes" --> G4["Approve modification"]
```

## 8. The trust failed: where does the property go?

```mermaid
flowchart TD
    A["Express trust fails in whole or part"] --> B{"Wrongdoing by holder? Fraud, undue influence, secret trust promise"}
    B -- "Yes" --> CT["Constructive trust for intended taker - R-TRS-038, R-TRS-032"]
    B -- "No" --> C{"Inter vivos or testamentary?"}
    C -- "Inter vivos" --> RT["Resulting trust to settlor - R-TRS-036"]
    RT --> RT2{"Settlor dead?"}
    RT2 -- "Yes" --> W
    RT2 -- "No" --> SET["Settlor takes back"]
    C -- "Testamentary" --> W{"Will has a residuary clause that survives?"}
    W -- "Yes, failed gift was specific or general" --> RES["Falls into residue - R-TRS-040"]
    W -- "Failed gift was part of residue" --> OR["Other residuary takers; else intestacy"]
    W -- "No valid residue" --> INT["Intestacy to heirs - R-WIL-016, R-WIL-018"]
```
