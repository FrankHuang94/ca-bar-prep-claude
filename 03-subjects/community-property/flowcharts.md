---
subject: CMP
topic: Community Property — decision-tree flowcharts (Mermaid)
coverage_ids: [CMP-CBX-II, CMP-CBX-II.A, CMP-CBX-II.B, CMP-CBX-II.C, CMP-CBX-II.D, CMP-CBX-II.E-F, CMP-CBX-III.A, CMP-CBX-V.A, CMP-CBX-VI.debts, CMP-CBX-VII.x, CMP-SUP-002]
tested_on: [essay]
exam_frequency: {level: high, basis: "Essays: 17 of 31 administrations 2012-02 to 2026-07 (55%)"}
last_verified: 2026-11-05
status: verified
---

# Community Property — flowcharts

Eight decision trees for the analyses that recur on California CP essays. Rule IDs point to [`rule-statements.md`](rule-statements.md).

## 1. Characterizing one asset (the master loop)

```mermaid
flowchart TD
    A["Asset in the call"] --> B{"Acquired while domiciled in California?"}
    B -- "No" --> C{"Would it be CP if acquired in California?"}
    C -- "Yes" --> C1["QCP: treat as CP at dissolution if both spouses domiciled in CA; at death see chart 8"]
    C -- "No" --> C2["SP of acquiring spouse"]
    B -- "Yes" --> D{"When acquired?"}
    D -- "Before marriage" --> SP["Presumptively SP"]
    D -- "After date of separation" --> SP
    D -- "During marriage" --> E{"Gift, bequest, devise or descent to one spouse?"}
    E -- "Yes" --> SP
    E -- "No" --> CP["Presumptively CP - R-CMP-011"]
    SP --> F{"Changed by prenup or transmutation? See chart 2"}
    CP --> F
    F --> G{"Commingled? See chart 3"}
    G --> H{"Contributions from the other estate? See charts 4 and 5"}
    H --> I["Conclude character; then division or disposition"]
```

## 2. Transmutation (Fam. Code § 852)

```mermaid
flowchart TD
    A["Spouses changed the character of property?"] --> B{"Made before 1 Jan 1985?"}
    B -- "Yes" --> B1["Oral or conduct may suffice - R-CMP-025"]
    B -- "No" --> C{"Gift between spouses of a personal item used by donee and not substantial in value?"}
    C -- "Yes" --> C1["Donee's SP without writing - R-CMP-024"]
    C -- "No" --> D{"Writing signed or accepted by the adversely affected spouse?"}
    D -- "No" --> X["No transmutation; no part-performance exception - Benson"]
    D -- "Yes" --> E{"Expressly states a change in character or ownership?"}
    E -- "No" --> X
    E -- "Yes" --> F{"Does it advantage one spouse?"}
    F -- "Yes" --> G["Presumed undue influence; advantaged spouse must prove free and informed act - R-CMP-016"]
    F -- "No" --> H["Valid transmutation"]
    G --> I{"Rebutted?"}
    I -- "Yes" --> H
    I -- "No" --> X2["Transmutation set aside"]
    H --> J["SP into CP or joint form: consider § 2640 reimbursement unless waived in writing - R-CMP-045"]
```

## 3. Commingled account tracing

```mermaid
flowchart TD
    A["Asset bought from an account holding CP and SP"] --> B{"Records show SP funds on deposit at purchase and intent to use SP?"}
    B -- "Yes" --> D1["Direct tracing: SP - Mix"]
    B -- "No" --> C{"Records show all CP already spent on family expenses at purchase?"}
    C -- "Yes" --> D2["Exhaustion method: SP - See"]
    C -- "No" --> D3["Cannot trace: CP; total recapitulation not enough"]
    A --> E{"SP used to pay family expenses?"}
    E -- "Yes" --> E1["Presumed gift; no reimbursement - R-CMP-031"]
```

## 4. Separate business grown during marriage (Pereira / Van Camp)

```mermaid
flowchart TD
    A["SP business; spouse worked in it during marriage"] --> B{"More than minimal community effort?"}
    B -- "No" --> B1["Growth stays SP - R-CMP-041"]
    B -- "Yes" --> C{"Main cause of growth?"}
    C -- "Spouse's personal skill and effort" --> P["Pereira: SP = capital plus fair return; rest CP - R-CMP-034"]
    C -- "Capital, market or others' work" --> V["Van Camp: CP = reasonable salary minus amounts drawn; rest SP - R-CMP-035"]
    C -- "Mixed or unclear" --> M["Apply both; choose the method that does substantial justice - R-CMP-036"]
    P --> Z["Divide CP portion equally"]
    V --> Z
    M --> Z
```

## 5. Who paid for the real property? (Moore/Marsden, § 2640, improvements)

```mermaid
flowchart TD
    A["Real property; contributions from more than one estate"] --> B{"Character of the property at acquisition?"}
    B -- "SP of one spouse" --> C{"What did CP pay for?"}
    C -- "Principal on purchase loan" --> MM["Moore and Marsden pro tanto CP share - R-CMP-037"]
    C -- "Improvements" --> IM["Community reimbursement, cost or value added - R-CMP-039"]
    C -- "Interest, taxes, insurance" --> NO["No CP interest; cost of use - R-CMP-040"]
    B -- "CP or joint title at dissolution" --> D{"Did SP pay down payment, improvements or principal?"}
    D -- "Yes" --> W{"Written waiver?"}
    W -- "No" --> R["§ 2640 b reimbursement, no interest, capped at net value - R-CMP-042"]
    W -- "Yes" --> R0["No reimbursement"]
    D -- "No" --> EQ["Divide equity equally"]
    B -- "SP of the other spouse" --> F["§ 2640 c reimbursement unless written transmutation or waiver - R-CMP-043"]
```

## 6. Date of separation and post-separation accounting

```mermaid
flowchart TD
    A["Candidate date of separation"] --> B{"Spouse expressed to the other the intent to end the marriage?"}
    B -- "No" --> X["Not the DOS; try a later date"]
    B -- "Yes" --> C{"Conduct consistent with that intent? Consider all evidence"}
    C -- "No" --> X
    C -- "Yes" --> D["DOS under Fam. Code § 70 - R-CMP-070"]
    D --> E["Later earnings and accumulations are SP - R-CMP-071"]
    D --> F{"SP used to pay a community debt after DOS?"}
    F -- "Yes" --> G["Epstein credit unless gift, support or offset - R-CMP-073"]
    D --> H{"One spouse had exclusive use of a CP asset?"}
    H -- "Yes" --> I["Watts charge - R-CMP-074"]
    D --> J{"Community business grew after DOS?"}
    J -- "Yes" --> K["Apportion post-DOS labor vs community capital - R-CMP-072"]
```

## 7. Can the creditor reach it? (debts)

```mermaid
flowchart TD
    A["Debt of spouse D"] --> B{"When incurred?"}
    B -- "Before marriage" --> C["Community estate liable - § 910"]
    C --> C1{"Is the asset the non-debtor's earnings kept in a separate uncommingled account?"}
    C1 -- "Yes" --> C2["Not reachable - § 911"]
    C1 -- "No" --> C3["Reachable"]
    B -- "During marriage before DOS" --> E["Community estate and D's SP liable; non-debtor SP not liable unless necessaries - §§ 910, 913, 914"]
    B -- "After DOS" --> F["Not a community-estate debt under § 910; allocate under § 2623"]
    E --> G{"Tort?"}
    G -- "Activity for community benefit" --> G1["CP first, then D's SP - § 1000"]
    G -- "Not for community benefit" --> G2["D's SP first, then CP - § 1000"]
```

## 8. Property at death (CP, QCP, SP)

```mermaid
flowchart TD
    A["Spouse dies domiciled in California"] --> B{"Character of each asset?"}
    B -- "CP" --> C["Half belongs to survivor; decedent may will the other half - Prob. Code §§ 100, 6101"]
    B -- "Decedent's QCP: personal property anywhere or CA land" --> D["Half belongs to survivor - Prob. Code §§ 66, 101"]
    B -- "Land in another state" --> E["Not QCP at death; situs law governs"]
    B -- "Survivor's own QCP" --> F["Stays with survivor"]
    B -- "Decedent's SP" --> G["Passes by will or intestacy"]
    D --> H{"Decedent transferred QCP without consideration or consent and kept control or survivorship?"}
    H -- "Yes" --> I["Survivor may recapture one-half - Prob. Code § 102"]
    C --> J{"Will?"}
    G --> J
    J -- "No" --> K["Intestacy: survivor takes all CP, decedent's half of QCP, and 1, 1/2 or 1/3 of SP - § 6401"]
    J -- "Yes" --> L["Check omitted spouse § 21610 and election"]
```
