---
subject: BUS
topic: Business Associations — decision flowcharts (Mermaid)
coverage_ids: [BUS-CBX-I, BUS-CBX-II, BUS-CBX-V.A.2, BUS-CBX-V.C, BUS-CBX-V.D.3, BUS-CBX-V.E.5, BUS-CBX-V.F, BUS-CBX-VI, BUS-PAST-001]
tested_on: [essay, PT]
exam_frequency: {level: high, basis: "Essays: 14 of 31 administrations 2012-02 to 2026-07 (45%)"}
last_verified: 2026-11-05
status: draft
---

# Business Associations — flowcharts

Ten decision trees for the analyses you will run most often. Rule IDs point to [`rule-statements.md`](rule-statements.md).

## 1. What kind of entity is it? (R-BUS-021, R-BUS-040, R-BUS-044, R-BUS-051, R-BUS-101, R-BUS-107)

```mermaid
flowchart TD
    A["Business with one or more owners"] --> B{"Was any document filed with the Secretary of State?"}
    B -->|No| C{"How many owners share profits and control?"}
    C -->|One| SP["Sole proprietorship: unlimited personal liability"]
    C -->|Two or more| GP["General partnership by default, intent irrelevant"]
    B -->|Yes| D{"What was filed?"}
    D -->|Articles of incorporation| CORP["Corporation from the filing date"]
    D -->|Articles of organization| LLC["LLC"]
    D -->|Certificate of limited partnership| LP["Limited partnership"]
    D -->|LLP registration by an existing partnership| LLP["LLP: in California only listed professions"]
    D -->|Filing attempted but defective| DEF["Test de facto corporation and corporation by estoppel"]
    DEF -->|Fails| GP
    GP --> EST{"Anyone held out as a partner who is not one?"}
    EST -->|Yes| PBE["Partnership by estoppel as to relying creditors"]
    EST -->|No| NEXT["Go to authority and liability"]
```

## 2. Is the principal bound by the contract? (R-BUS-008 to R-BUS-013, R-BUS-025)

```mermaid
flowchart TD
    A["Agent or partner made a contract with a third party"] --> P{"Is the actor a partner acting for the partnership?"}
    P -->|Yes| P1{"Apparently in the ordinary course of partnership business?"}
    P1 -->|Yes| P2{"Did the third party know or have notice of a lack of authority?"}
    P2 -->|No| BOUND["Principal bound"]
    P2 -->|Yes| ACT
    P1 -->|No| ACT
    P -->|No| ACT{"Actual authority, express or implied?"}
    ACT -->|Yes| BOUND
    ACT -->|No| APP{"Apparent authority traceable to the principal's manifestation to the third party, and reasonable belief?"}
    APP -->|Yes| BOUND
    APP -->|No| RAT{"Ratified with knowledge of material facts, or benefits accepted?"}
    RAT -->|Yes| BOUND
    RAT -->|No| EST{"Estoppel or undisclosed principal rule?"}
    EST -->|Yes| BOUND
    EST -->|No| NOT["Principal not bound; agent liable on implied warranty of authority"]
    BOUND --> AG{"Was the principal disclosed?"}
    AG -->|Disclosed| AG1["Agent not a party"]
    AG -->|Unidentified or undisclosed| AG2["Agent also personally liable"]
```

## 3. Respondeat superior (R-BUS-002, R-BUS-014 to R-BUS-018)

```mermaid
flowchart TD
    A["Worker committed a tort"] --> B{"Employee: did the hirer control manner and means?"}
    B -->|No: independent contractor| IC{"Nondelegable duty, inherently dangerous work, or hirer's own negligence?"}
    IC -->|Yes| LIAB2["Hirer liable on that basis"]
    IC -->|No| NOLIAB["Hirer not liable; contractor liable"]
    B -->|Yes| C{"Within scope: kind of work, time and place, purpose to serve employer?"}
    C -->|Yes| LIAB["Employer vicariously liable; employee also liable"]
    C -->|Deviation| D{"Minor detour or substantial frolic?"}
    D -->|Detour| LIAB
    D -->|Frolic| E["Outside scope until return to employer's business"]
    C -->|Commuting| F{"Exception: paid travel, required vehicle, special errand, business purpose?"}
    F -->|Yes| LIAB
    F -->|No| G["Going and coming rule: outside scope"]
    C -->|Intentional tort| H{"Motive to serve employer, force inherent in job, or in California engendered by the work?"}
    H -->|Yes| LIAB
    H -->|No| I["Outside scope; check negligent hiring or supervision"]
    E --> I
    G --> I
```

## 4. Partner and owner personal liability for a business debt (R-BUS-028 to R-BUS-030, R-BUS-042, R-BUS-045)

```mermaid
flowchart TD
    A["Business obligation exists"] --> B{"Entity type when the obligation arose?"}
    B -->|General partnership or joint venture| C["All partners jointly and severally liable"]
    C --> C1{"Defendant a partner when incurred?"}
    C1 -->|Joined later| C2["Not personally liable; capital at risk"]
    C1 -->|Yes| C3["Liable, but creditor must first exhaust partnership assets unless exception or own tort"]
    B -->|LLP| D["Partners shielded except own wrongs (incl. own negligent supervision), guarantees and written assumptions"]
    B -->|Limited partnership| E{"General or limited partner?"}
    E -->|General| C
    E -->|Limited| E1{"California: participated in control and creditor knew and reasonably believed she was a GP?"}
    E1 -->|Yes| C
    E1 -->|No| SHIELD["Shielded"]
    B -->|Corporation or LLC| F["Owners shielded"]
    F --> G["Check exceptions: promoter, veil piercing, own tort, guarantee, unlawful distribution"]
```

## 5. Promoter and pre-incorporation contracts (R-BUS-051 to R-BUS-055)

```mermaid
flowchart TD
    A["Contract signed for a business entity"] --> B{"Were articles filed before signing?"}
    B -->|Yes| CORP["Corporation is the party; apply officer authority"]
    B -->|No| C{"Good faith attempt to incorporate and business run as a corporation?"}
    C -->|Yes| DF["Argue de facto corporation; MBCA 2.04 liability if signer knew no filing"]
    C -->|No| D["Signer is a promoter: personally liable"]
    DF --> D
    D --> E{"Did the contract say the third party looks only to the future corporation?"}
    E -->|Yes| REL["Promoter not liable"]
    E -->|No| F{"After formation did the corporation adopt, expressly or by accepting benefits?"}
    F -->|No| G["Corporation not liable; promoter liable"]
    F -->|Yes| H["Corporation liable from adoption; promoter still liable"]
    H --> I{"Novation: all three parties agreed to substitute the corporation?"}
    I -->|Yes| REL
    I -->|No| J["Both liable; promoter may seek indemnity"]
    D --> K{"Co-owners working together before incorporation?"}
    K -->|Yes| L["Partnership liability for co-promoters"]
```

## 6. Piercing the corporate veil (R-BUS-046 to R-BUS-049)

```mermaid
flowchart TD
    A["Creditor seeks to hold owner liable for corporate debt"] --> B["Start: limited liability"]
    B --> C{"Unity of interest? Undercapitalization, commingling, personal use of assets, no formalities, domination"}
    C -->|No| NO["No piercing"]
    C -->|Yes| D{"Inequitable result: fraud, evasion, siphoning, misleading creditor?"}
    D -->|No| NO
    D -->|Yes| E{"Tort or contract creditor?"}
    E -->|Tort| F["Stronger case: involuntary creditor"]
    E -->|Contract| G["Weaker case: could have investigated or demanded a guarantee"]
    F --> H{"Which owners actively participated?"}
    G --> H
    H --> I["Pierce as to active owners only; passive minority not liable"]
    C -.-> CA["California: close corporation 300e and LLC 17703.04 formalities exceptions"]
```

## 7. Director liability: care, BJR, loyalty (R-BUS-061 to R-BUS-070)

```mermaid
flowchart TD
    A["Challenged board decision; take each director separately"] --> B{"Did this director have a conflict or personal benefit, or lack independence?"}
    B -->|No| C{"Informed decision: reasonable inquiry, adequate time, reliance on experts?"}
    C -->|Yes| D{"Good faith and rational business purpose?"}
    D -->|Yes| BJR["BJR protects; no liability"]
    D -->|No| WASTE["Bad faith or waste: liable"]
    C -->|No| CARE["Duty of care breach: gross negligence"]
    CARE --> EX{"Exculpation clause covers it?"}
    EX -->|Yes| NOD["No damages; injunction still possible"]
    EX -->|No: reckless disregard or pattern of inattention in California| LIAB["Liable if causation and damages"]
    B -->|Yes| LOY["Duty of loyalty"]
    LOY --> SH{"Safe harbor: full disclosure and approval by disinterested directors or shareholders?"}
    SH -->|Shareholders| OK["Protected; California 310a1 needs no fairness showing"]
    SH -->|Directors| JR{"California: also just and reasonable?"}
    JR -->|Yes| OK
    JR -->|No| FAIR
    SH -->|None| FAIR{"Defendant proves entire fairness: fair dealing and fair price?"}
    FAIR -->|Yes| OK
    FAIR -->|No| LIAB2["Liable: rescission, damages, disgorgement"]
```

## 8. Shareholder suit procedure (R-BUS-081 to R-BUS-084)

```mermaid
flowchart TD
    A["Shareholder wants to sue"] --> B{"Who was injured and who gets the recovery?"}
    B -->|Shareholder individually| DIR["Direct suit: no demand or bond requirements"]
    B -->|Corporation| DER["Derivative suit"]
    DER --> S{"Owned shares at time of wrong and still owns them?"}
    S -->|No| S1{"California: court permits under 800b1 factors?"}
    S1 -->|No| DISMISS["Dismissed for lack of standing"]
    S1 -->|Yes| DEM
    S -->|Yes| DEM{"Demand made on the board?"}
    DEM -->|Yes and refused| WR["Refusal reviewed under BJR"]
    DEM -->|No| FUT{"Futility pleaded with particularity: half the board benefited, faces likely liability, or lacks independence?"}
    FUT -->|No| DISMISS2["Dismissed; MBCA requires universal demand and 90 days"]
    FUT -->|Yes| BOND{"California: defendant moves for bond within 30 days?"}
    BOND -->|Yes| BOND1["Court may require up to 50000 dollars total"]
    BOND -->|No| MERITS["Merits: care, BJR, loyalty"]
    BOND1 --> MERITS
    MERITS --> SLC{"Independent committee moves to dismiss?"}
    SLC --> REC["Recovery to corporation; court approves settlement"]
```

## 9. Insider trading and short-swing profits (R-BUS-088 to R-BUS-092)

```mermaid
flowchart TD
    A["Trade while aware of material nonpublic information"] --> B{"Trader's relationship?"}
    B -->|Director, officer, employee, company lawyer or accountant| CL["Classical theory: disclose or abstain"]
    B -->|Received tip| T{"Tipper breached duty for personal benefit and tippee knew or should have known?"}
    T -->|Yes| LIAB["Tippee and tipper liable"]
    T -->|No| NOT["No 10b-5 tippee liability"]
    B -->|Outsider entrusted with information by a source| MIS["Misappropriation: deceived the source"]
    B -->|Tender offer information from bidder or target| TO["Rule 14e-3: no duty needed"]
    CL --> LIAB
    MIS --> LIAB
    TO --> LIAB
    A --> P{"Public reporting company and trader is officer, director or more than 10 percent holder?"}
    P -->|Yes| SS{"Purchase and sale within less than six months?"}
    SS -->|Yes| S16["Section 16b: issuer recovers profit, strict liability"]
    SS -->|No| N16["No 16b liability"]
```

## 10. Insider loan in the company's bankruptcy (R-BUS-099, R-BUS-100)

```mermaid
flowchart TD
    A["Insider lent money to the company, which is now in bankruptcy"] --> B{"Real debt? Note, interest, maturity, repayment not tied to profits, adequate capital, outside lenders available"}
    B -->|No| EQ["Recharacterize as equity: paid after all creditors"]
    B -->|Yes| C{"Inequitable conduct: control abuse, undercapitalization, self-preference, misleading creditors?"}
    C -->|No| PAY["Allowed unsecured claim, paid pro rata"]
    C -->|Yes| D{"Harm to creditors or unfair advantage to insider?"}
    D -->|Yes| SUB["Equitable subordination under 510c to the extent of harm"]
    D -->|No| PAY
    A --> E{"Insider repaid within one year before filing?"}
    E -->|Yes| PREF["Trustee may avoid as an insider preference"]
```
