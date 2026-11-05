---
subject: PRF
topic: Professional Responsibility — decision flowcharts
coverage_ids: [PRF-SUP-003, PRF-SUP-004, PRF-SUP-006, PRF-SUP-007, PRF-CBX-I, PRF-CBX-I.x2, PRF-CBX-II, PRF-CBX-III]
tested_on: [essay]
exam_frequency: {level: high, basis: "Essays: 30 of 31 administrations 2012-02 to 2026-07 (97%)"}
last_verified: 2026-11-04
status: draft
---

# Professional Responsibility — flowcharts

Each chart ends in a California result and an ABA result where they differ. Rule IDs point to [`rule-statements.md`](rule-statements.md).

## 1. Current-client conflict (rule 1.7 / MR 1.7) — R-PRF-021 to R-PRF-024

```mermaid
flowchart TD
  A["Lawyer represents or will represent Client A"] --> B{"Directly adverse to another current client?"}
  B -- Yes --> E{"Consentable? Reasonable belief in competent and diligent representation, not prohibited by law, not a claim between clients in same litigation"}
  B -- No --> C{"Significant risk of material limitation from another client, former client, third person or own interest?"}
  C -- Yes --> E
  C -- No --> D{"CA only: relationship with party or witness, or opposing counsel is relative, cohabitant, client or intimate partner?"}
  D -- Yes --> D1["CA: written disclosure required under rule 1.7 c. ABA: no duty unless significant risk"]
  D -- No --> OK["No 1.7 conflict. Check rule 1.8 specific conflicts"]
  E -- No --> X["Must decline or withdraw"]
  E -- Yes --> F{"Consent from each affected client?"}
  F -- "CA: informed written consent" --> G["Representation permitted"]
  F -- "ABA: informed consent confirmed in writing" --> G
  F -- None --> X
```

## 2. Former client, imputation and screening (rules 1.9–1.10) — R-PRF-034 to R-PRF-037

```mermaid
flowchart TD
  A["New matter adverse to someone the lawyer or the lawyer's old firm represented"] --> B{"Same or substantially related matter?"}
  B -- No --> OK["No former-client conflict; still no use of confidential information"]
  B -- Yes --> C{"Materially adverse to the former client?"}
  C -- No --> OK
  C -- Yes --> D{"Lawyer personally represented the former client, or acquired material confidential information at old firm?"}
  D -- No --> OK
  D -- Yes --> E{"Former client gives informed written consent CA, or informed consent confirmed in writing ABA?"}
  E -- Yes --> OK2["Lawyer and firm may proceed"]
  E -- No --> F["Lawyer personally disqualified; conflict imputed to new firm"]
  F --> G{"Can the firm screen the lateral?"}
  G -- "ABA" --> H["Yes: timely screen, no fee share, written notice, certifications"]
  G -- "California" --> I{"Did the lateral substantially participate in the matter?"}
  I -- Yes --> J["No screen allowed; firm needs former client's informed written consent"]
  I -- No --> K["Screen allowed: timely, no fee share, prompt written notice"]
```

## 3. May the lawyer reveal confidential information? — R-PRF-013 to R-PRF-015

```mermaid
flowchart TD
  A["Information relating to the representation"] --> B{"Client gave informed consent or disclosure impliedly authorized?"}
  B -- Yes --> Y["May disclose within the consent"]
  B -- No --> C{"Needed to prevent death or substantial bodily harm?"}
  C -- Yes --> D{"California: is the threatened harm from a criminal act of the client or another?"}
  D -- Yes --> D1["CA and ABA: may disclose. CA first tries to dissuade and informs client if reasonable; disclose no more than necessary"]
  D -- No --> D2["ABA may disclose if death or harm reasonably certain. CA may not"]
  C -- No --> E{"Client crime or fraud causing substantial financial injury, lawyer's services used?"}
  E -- Yes --> E1["ABA may disclose to prevent, mitigate or rectify. CA may not; consider withdrawal"]
  E -- No --> F{"Lawyer's own claim or defense, ethics advice, court order, conflict check?"}
  F -- Yes --> F1["ABA may disclose as reasonably necessary. CA: no rule-based exception; rely on privilege exceptions and court orders"]
  F -- No --> N["Must not disclose under either system"]
```

## 4. Organization client and constituent wrongdoing (rule 1.13) — R-PRF-055, R-PRF-056

```mermaid
flowchart TD
  A["Lawyer for organization learns constituent is violating a duty to the organization or law imputable to it"] --> B{"Likely substantial injury to the organization?"}
  B -- No --> C["Advise constituent; keep confidential"]
  B -- Yes --> D["Report up, to the highest authority if warranted"]
  D --> E{"Highest authority acts?"}
  E -- Yes --> F["Done; continue representation"]
  E -- No --> G{"ABA: clear violation, substantial injury reasonably certain, and lawyer not hired to investigate or defend?"}
  G -- Yes --> H["ABA: may report out as reasonably necessary"]
  G -- No --> I["ABA: no reporting out"]
  E -- No --> J["California: may NOT reveal 6068 e information; continue urging; may or must resign or withdraw"]
```

## 5. False evidence and client perjury (rule 3.3) — R-PRF-061

```mermaid
flowchart TD
  A["Does the lawyer know the evidence is false?"] -- "No, only suspects" --> B["May present it; criminal defendant may testify; may refuse other evidence reasonably believed false"]
  A -- "Yes, before it is offered" --> C["Do not offer it; remonstrate; if client insists, seek withdrawal"]
  C --> C1{"Criminal defendant insists on testifying?"}
  C1 -- Yes --> C2["CA: narrative approach permitted. ABA: refuse to elicit false testimony"]
  A -- "Yes, after it was offered" --> D["Remonstrate with client to correct"]
  D --> E{"Corrected?"}
  E -- Yes --> OK["Done"]
  E -- No --> F["Seek withdrawal if it will cure"]
  F --> G{"Still uncured?"}
  G -- "ABA" --> H["Disclose to tribunal even if confidential"]
  G -- "California" --> I["No disclosure barred by 6068 e and rule 1.6; withdraw"]
```

## 6. Is the fee arrangement valid in California? — R-PRF-041 to R-PRF-045

```mermaid
flowchart TD
  A["Fee arrangement"] --> B{"Criminal defense contingency, or fee contingent on divorce, support or a property settlement in lieu of support?"}
  B -- Yes --> X["Prohibited under both systems"]
  B -- No --> C{"Contingency fee?"}
  C -- Yes --> D{"B&P 6147: signed by both, rate, costs, related matters, not set by law and negotiable?"}
  D -- No --> V["Voidable by client; reasonable fee only"]
  D -- Yes --> U
  C -- No --> E{"Total expense foreseeably over 1000 dollars?"}
  E -- No --> U
  E -- Yes --> F{"Signed writing under B&P 6148, or exception: emergency, prior same services, written waiver, corporate client?"}
  F -- No --> V
  F -- Yes --> U{"Unconscionable under CA rule 1.5 or unreasonable under MR 1.5?"}
  U -- Yes --> X2["Violation; refund excess"]
  U -- No --> W{"Labelled nonrefundable?"}
  W -- Yes --> W1{"True retainer for availability only, agreed in writing?"}
  W1 -- No --> X3["Violates rule 1.5 d; unearned part refundable"]
  W1 -- Yes --> OK["Valid"]
  W -- No --> OK
```

## 7. Fee division between lawyers in different firms — R-PRF-046

```mermaid
flowchart TD
  A["Two lawyers not in same firm will split a fee"] --> B{"Which system?"}
  B -- ABA --> C{"Split proportional to work, or each assumes joint responsibility?"}
  C -- No --> CX["ABA violation: pure referral fee not allowed"]
  C -- Yes --> D{"Client agrees to the arrangement and shares, confirmed in writing, and total reasonable?"}
  D -- Yes --> COK["ABA: proper"]
  D -- No --> CX2["ABA violation"]
  B -- California --> E{"Written agreement between the lawyers?"}
  E -- No --> EX["CA violation; split unenforceable, quantum meruit only"]
  E -- Yes --> F{"Client consented in writing after full written disclosure of the split, identities and terms?"}
  F -- No --> EX
  F -- Yes --> G{"Total fee not increased by the split, and not unconscionable?"}
  G -- Yes --> EOK["CA: proper, even as a pure referral fee"]
  G -- No --> EX
```

## 8. Withdrawal — R-PRF-050 to R-PRF-053

```mermaid
flowchart TD
  A["Should the lawyer stop representing the client?"] --> B{"Mandatory ground? Rule violation will result; impairment; discharged; CA harassing suit; ABA client persists in using services for crime or fraud"}
  B -- Yes --> M["Must withdraw"]
  B -- No --> C{"Permissive ground? Non-payment after warning; client crime or fraud; unreasonable difficulty; client assents; ABA repugnant or no material adverse effect"}
  C -- No --> S["Must stay"]
  C -- Yes --> P["May withdraw"]
  M --> T{"Court permission required?"}
  P --> T
  T -- Yes --> T1["Seek leave; do not reveal confidences; continue if ordered"]
  T -- No --> T2["Proceed"]
  T1 --> Z["Protect client: notice, time, return all client materials even if unpaid in CA, refund unearned fees"]
  T2 --> Z
```

## 9. Must the lawyer report another lawyer? (rule 8.3) — R-PRF-091

```mermaid
flowchart TD
  A["Lawyer learns of another lawyer's conduct"] --> B{"California: credible evidence of a criminal act, dishonesty, fraud, deceit, reckless or intentional misrepresentation, or misappropriation?"}
  B -- Yes --> C{"Raises substantial question about honesty, trustworthiness or fitness?"}
  C -- Yes --> D{"Information protected by 6068 e, rule 1.6 or 1.8.2, a lawyer assistance program, mediation or privilege?"}
  D -- Yes --> N["No duty to report that information"]
  D -- No --> R["CA: must report to State Bar or tribunal without undue delay"]
  C -- No --> O["CA: no duty; may report"]
  B -- No --> O
  A --> E{"ABA: knows of any rule violation raising substantial question about honesty, trustworthiness or fitness?"}
  E -- Yes --> F{"Information protected by rule 1.6 or a lawyer assistance program?"}
  F -- No --> R2["ABA: must inform the appropriate authority"]
  F -- Yes --> N
  E -- No --> O2["ABA: no duty"]
```

## 10. Out-of-state lawyer working on a California matter — R-PRF-082, R-PRF-083

```mermaid
flowchart TD
  A["Lawyer licensed elsewhere, not in California"] --> B{"Holding out as California lawyer, or resident office or systematic and continuous presence here?"}
  B -- Yes --> X["UPL: B&P 6125 and 6126; rule 5.5 b; no fees for California work under Birbrower"]
  B -- No --> C{"Fits a Rule of Court: pro hac vice 9.40, arbitration 9.43, in-house 9.46, litigation 9.47, non-litigation 9.48?"}
  C -- Yes --> OK["Permitted if the rule's conditions are met"]
  C -- No --> X
  A --> D{"MPRE / ABA comparison: temporary practice with local lawyer, related to proceeding or ADR, or related to home practice?"}
  D -- Yes --> OK2["ABA MR 5.5 c permits"]
  D -- No --> X2["ABA violation"]
```
