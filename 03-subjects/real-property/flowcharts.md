---
subject: PRP
topic: Real Property — decision trees (Mermaid)
coverage_ids: [PRP-MBE-I.A, PRP-MBE-I.B, PRP-MBE-I.C, PRP-MBE-I.D.1, PRP-MBE-II.A, PRP-MBE-II.B, PRP-MBE-IV.F, PRP-MBE-V.A, PRP-MBE-V.D.1]
tested_on: [MBE, essay]
exam_frequency: {level: high, basis: "Essays: 13 of 31 administrations 2012-02 to 2026-07 (42%); MBE: 25 scored questions every exam"}
last_verified: 2026-11-05
status: verified
---

# Real Property — flowcharts

Each chart is a decision tree for one recurring analysis. Rule IDs point to [`rule-statements.md`](rule-statements.md).

## 1. Classifying a defeasible fee and its future interest (R-PRP-002 to R-PRP-005)

```mermaid
flowchart TD
  A["Grant of a fee with a limiting event?"] -->|No| B["Fee simple absolute"]
  A -->|Yes| C["Only words of purpose or motive, such as for school purposes?"]
  C -->|Yes| B
  C -->|No| D["Who takes if the event happens?"]
  D -->|Grantor| E["Durational words: so long as, while, until?"]
  E -->|Yes| F["Fee simple determinable plus possibility of reverter - automatic"]
  E -->|No, conditional words plus right to re-enter| G["Fee simple subject to condition subsequent plus right of entry - must elect"]
  D -->|Third party| H["Fee simple subject to executory limitation plus shifting executory interest"]
  H --> I["Run the RAP on the executory interest"]
  I -->|Fails| J["Strike gift over: durational words leave FSD in grantee and reverter in grantor; conditional words leave fee simple absolute"]
  I -->|Valid| K["Executory interest stands"]
  F --> L["California: treat as condition subsequent with power of termination; 30-year limit"]
```

## 2. Classifying remainders and executory interests (R-PRP-008 to R-PRP-011)

```mermaid
flowchart TD
  A["Future interest created in a transferee?"] -->|No, in grantor| B["Reversion, possibility of reverter, or right of entry"]
  A -->|Yes| C["Can it take on the natural end of a prior life estate or term?"]
  C -->|No, it cuts short a prior estate or follows a gap| D["Executory interest - shifting or springing"]
  C -->|Yes| E["Remainder"]
  E --> F["Taker born and ascertained, and no condition precedent?"]
  F -->|No| G["Contingent remainder - grantor keeps reversion"]
  F -->|Yes| H["Vested remainder"]
  H --> I["Class that can still grow?"]
  I -->|Yes| J["Vested subject to open"]
  I -->|No| K["Condition subsequent can take it away?"]
  K -->|Yes| L["Vested subject to complete divestment"]
  K -->|No| M["Indefeasibly vested"]
```

## 3. Rule against perpetuities (R-PRP-014 to R-PRP-016)

```mermaid
flowchart TD
  A["Interest subject to the RAP? Contingent remainder, executory interest, class gift, option in gross, ROFR"] -->|No| B["RAP does not apply"]
  A -->|Yes| C["When created? Deed at delivery, will at death, revocable trust when irrevocable"]
  C --> D["What must happen for it to vest?"]
  D --> E["Is there a life in being at creation such that the interest must vest or fail within 21 years after that life ends?"]
  E -->|Yes, in every possible scenario| F["Valid at common law"]
  E -->|No, some scenario vests too late| G["Void at common law - strike it and reread the grant"]
  G --> H["Jurisdiction has USRAP? California yes"]
  H -->|Yes| I["Wait and see: valid if it actually vests or fails within 90 years"]
  I -->|Does not| J["Court reforms to approximate intent within 90 years"]
  H -->|No| K["Interest void; check class gift all-or-nothing and fallback interests"]
```

## 4. Joint tenancy: what happened to it? (R-PRP-020 to R-PRP-022)

```mermaid
flowchart TD
  A["Valid joint tenancy created? Four unities and express survivorship language"] -->|No| B["Tenancy in common"]
  A -->|Yes| C["Inter vivos act by one joint tenant?"]
  C -->|Conveyance to third party| D["Severed as to that share: transferee is tenant in common"]
  C -->|Deed to self or written declaration| E["California: severs if recorded before death, or signed within 3 days before and recorded within 7 days after death"]
  C -->|Mortgage or deed of trust| F["Title theory: severs. Lien theory, most states and California: no severance; lien dies with mortgagor"]
  C -->|Lease| G["No severance in California; lease ends at lessor death"]
  C -->|Contract to sell| H["Usually severs by equitable conversion"]
  C -->|Will only| I["No severance; survivor takes all"]
  C -->|Kills cotenant| J["Severance; killer does not take by survivorship"]
```

## 5. Tenant's remedies for possession and condition problems (R-PRP-030 to R-PRP-038)

```mermaid
flowchart TD
  A["What went wrong?"] --> B["Prior occupant still in possession at start"]
  B --> B1["English rule majority: landlord in breach; tenant may terminate or abate rent and recover damages. American rule: sue the holdover"]
  A --> C["Landlord physically excludes tenant"]
  C --> C1["Actual eviction: total ends rent; partial by landlord suspends all rent"]
  A --> D["Serious condition problem"]
  D --> E["Residential lease?"]
  E -->|Yes| F["Warranty of habitability: notice and reasonable time, then stay and withhold or reduce rent, repair and deduct, damages, or terminate"]
  F --> F1["California: repair and deduct up to one month rent, twice in 12 months; UD defense"]
  E -->|No, commercial| G["Constructive eviction: substantial interference, notice, failure to cure, vacate within reasonable time"]
  G -->|Tenant stayed too long| G1["Waived; damages only"]
  A --> H["Landlord retaliates after complaint"]
  H --> H1["Retaliatory eviction defense; California 180-day presumption"]
```

## 6. Tenant abandons before the term ends (R-PRP-033, R-PRP-047)

```mermaid
flowchart TD
  A["Tenant vacates and stops paying"] --> B["Did landlord accept surrender? Express or by retaking for own use"]
  B -->|Yes| C["Lease ends; tenant owes rent accrued before surrender"]
  B -->|No| D["Jurisdiction requires mitigation?"]
  D -->|Yes, modern majority and California| E["Landlord must make reasonable reletting efforts"]
  E --> F["Damages: unpaid rent plus lease rent minus reasonably obtainable rent, plus reletting costs"]
  F --> F1["California 1951.2: tenant proves avoidable amount; 1951.4 lock-in if lease allows"]
  D -->|No, traditional| G["Landlord may leave vacant and sue for rent as it comes due"]
```

## 7. Does a promise about land bind a successor? (R-PRP-050 to R-PRP-056)

```mermaid
flowchart TD
  A["Promise about use of land; plaintiff sues a successor of the promisor"] --> B["What remedy is sought?"]
  B -->|Damages| C["Real covenant: writing, intent, touch and concern, horizontal privity, vertical privity, notice"]
  B -->|Injunction| D["Equitable servitude: writing or common scheme, intent, touch and concern, notice"]
  D --> E["No writing in this deed?"]
  E -->|Yes| F["Common scheme: general plan plus notice. California: needs a recorded instrument such as a recorded declaration of restrictions"]
  C --> G["All elements met?"]
  D --> G
  F --> G
  G -->|No| H["Not enforceable against successor"]
  G -->|Yes| I["Scope: does the use violate the restriction?"]
  I -->|Yes| J["Defenses: changed conditions, acquiescence, abandonment, laches, unclean hands, release, merger"]
  J -->|Defense fails| K["Enforce: damages or injunction"]
  J -->|Defense succeeds| H
```

## 8. Was an easement created, and by which method? (R-PRP-061 to R-PRP-065)

```mermaid
flowchart TD
  A["Signed writing granting or reserving the right?"] -->|Yes| B["Express easement; scope by terms"]
  A -->|No| C["Were the two parcels once commonly owned?"]
  C -->|Yes| D["Apparent and continuous use before severance, reasonably necessary?"]
  D -->|Yes| E["Easement implied from prior use"]
  D -->|No| F["Strict necessity at severance, such as landlocked?"]
  F -->|Yes| G["Easement by necessity; ends with necessity"]
  F -->|No| H["Check prescription and estoppel"]
  C -->|No| H
  H --> I["Open, continuous, adverse use for the statutory period? California 5 years"]
  I -->|Yes| J["Prescriptive easement; scope = use during period"]
  I -->|No| K["Permission plus substantial foreseeable reliance?"]
  K -->|Yes| L["Easement by estoppel or irrevocable license"]
  K -->|No| M["Revocable license only"]
```

## 9. Recording acts: who wins? (R-PRP-116 to R-PRP-119)

```mermaid
flowchart TD
  A["Two claimants from the same grantor"] --> B["Is the earlier interest void, such as forged or undelivered?"]
  B -->|Yes| C["Later taker wins; nothing passed earlier"]
  B -->|No| D["Is the later taker a purchaser or mortgagee for value?"]
  D -->|No, donee or heir| E["Earlier interest wins"]
  D -->|Yes| F["Notice when value paid? Actual, record within chain of title, or inquiry from possession"]
  F -->|Yes| E
  F -->|No| G["Statute type"]
  G -->|Notice| H["Later BFP wins"]
  G -->|Race-notice, California| I["Did later BFP record before the earlier interest?"]
  I -->|Yes| H
  I -->|No| E
  G -->|Race| J["Whoever recorded first wins"]
  H --> K["Shelter rule protects the BFP's transferees"]
```

## 10. Foreclosure: what happens to each interest? (R-PRP-099 to R-PRP-104)

```mermaid
flowchart TD
  A["Mortgage being foreclosed"] --> B["Interest senior to it?"]
  B -->|Yes| C["Unaffected; buyer takes subject to it"]
  B -->|No, junior| D["Holder joined or given required notice?"]
  D -->|Yes| E["Extinguished; paid from surplus in priority order"]
  D -->|No| F["Survives; keeps right to redeem"]
  A --> G["Proceeds: costs, then foreclosing debt, then juniors, then owner"]
  G --> H["Shortfall: deficiency judgment?"]
  H --> I["California: nonjudicial trustee sale?"]
  I -->|Yes| J["No deficiency, no post-sale redemption"]
  I -->|No, judicial| K["Purchase-money loan on owner-occupied 1 to 4 units or seller-financed?"]
  K -->|Yes| J2["No deficiency"]
  K -->|No| L["Deficiency limited to debt minus fair value; 1-year redemption"]
```

## 11. Adverse possession, with the California overlay (R-PRP-105 to R-PRP-108)

```mermaid
flowchart TD
  A["Possession actual, open and notorious, exclusive, hostile, continuous?"] -->|No| B["No title; consider prescriptive easement or agreed boundary"]
  A -->|Yes| C["For the full statutory period, using tacking if in privity?"]
  C -->|No| B
  C -->|Yes| D["Owner under disability when possession began, or a future interest not yet possessory, or government land?"]
  D -->|Yes| E["Period does not run against that owner or interest"]
  D -->|No| F["California: 5 years and all taxes levied and assessed paid?"]
  F -->|No| B
  F -->|Yes| G["Title by adverse possession; quiet title to make it marketable"]
```
