---
subject: REM
topic: Remedies — essay-ready rule statements (R-REM-001 to R-REM-094)
coverage_ids: [REM-CBX-I, REM-CBX-II, REM-CBX-III, REM-CBX-III.a, REM-CBX-III.b, REM-CBX-IV, REM-CBX-V, REM-CBX-VI, REM-SUP-001, REM-SUP-002, REM-SUP-003]
tested_on: [essay, PT]
exam_frequency: {level: high, basis: "Essays: 16 of 31 administrations 2012-02 to 2026-07 (52%)"}
last_verified: 2026-11-04
status: draft
---

# Remedies — rule statements

**How to use this file.** Each block gives a rule you can write verbatim on an essay, then its elements, exceptions, authority, the California point and a short example. `build_anki.py` turns the **Rule (write this)** paragraphs into cards. The order follows [`outline.md`](outline.md) (State Bar essay outline I–VI).

**Remedies is not an MBE subject.** The "MBE vs. CA essay" line therefore says what to write on a California essay: the **general rule** first (California Remedies essays use general principles unless the call asks for California law [S-077]), then a one-sentence "In California, …" where California differs. See [`ca-distinctions.md`](ca-distinctions.md).

**Contract measures live in Contracts.** Where the contract rule is the same, this file cross-references `R-CTR-###` in [`../contracts/rule-statements.md`](../contracts/rule-statements.md) instead of repeating it.

**Abbreviations.** R2d = Restatement (Second) of Contracts; R2d Torts = Restatement (Second) of Torts; R3RUE = Restatement (Third) of Restitution and Unjust Enrichment; UCC = Official Text of Article 2; Civ. Code / CCP = California Civil Code / Code of Civil Procedure; FRCP = Federal Rules of Civil Procedure; Π/Δ = plaintiff/defendant.

---

## I. Basic principles

### R-REM-001 — Classification of remedies
**Rule (write this):** Remedies fall into four families: (1) compensatory damages, which measure the plaintiff's loss; (2) restitution, which measures and strips the defendant's unjust gain; (3) coercive remedies (injunctions and specific performance), which order the defendant to act or refrain from acting; and (4) declaratory remedies, which state the parties' rights without ordering anything. Each family may be legal or equitable in origin, and the plaintiff may plead them in the alternative.

**Elements:** For each claim ask: (1) what loss did Π suffer (damages)? (2) what gain did Δ obtain (restitution)? (3) does Π need Δ to do or stop doing something (injunction / specific performance)? (4) does Π need a ruling on rights (declaratory relief)?

**Exceptions / defenses:** Π cannot recover twice for the same loss (R-REM-005).

**Authority:** R2d § 344 (expectation, reliance, restitution interests); R3RUE § 1 [VERIFY V-350]; Civ. Code §§ 3274, 3281 (compensation as the general remedy; damages defined); 28 U.S.C. § 2201.

**MBE vs. CA essay:** Not tested on the MBE. On every Remedies essay, use this classification as the skeleton: legal remedies → restitution → equitable remedies.

**Example:** A neighbor's wall encroaches on Π's land. Π may seek damages for loss of use (compensatory), the rental value Δ saved (restitution), a mandatory injunction to remove the wall (coercive) and a declaration of the boundary (declaratory).

> 🇨🇳 PRC bridge: roughly parallels the PRC split between 损害赔偿, 不当得利返还, 停止侵害/排除妨碍 and 确认之诉; US law adds the law/equity divide, which PRC law lacks (approx.).

### R-REM-002 — Law vs. equity: the adequacy requirement
**Rule (write this):** Legal remedies (damages, and the restitutionary actions of quasi-contract, replevin and ejectment) are available as of right once liability is proven. Equitable remedies (injunctions, specific performance, constructive trust, equitable lien, reformation, equitable rescission, accounting) are discretionary and are granted only when the legal remedy is inadequate and the balance of equities favors relief.

**Elements:** 1. Identify whether the remedy is legal or equitable. 2. If equitable: inadequacy of the legal remedy + discretion (hardship, feasibility, defenses).

**Exceptions / defenses:** Equitable defenses (laches, unclean hands) apply to equitable remedies; legal claims are governed by statutes of limitations (R-REM-090). California courts also let unclean hands bar some legal claims [VERIFY V-370].

**Authority:** *eBay Inc. v. MercExchange, L.L.C.*, 547 U.S. 388 (2006); *Weinberger v. Romero-Barcelo*, 456 U.S. 305 (1982); Civ. Code § 3422 [S-458]; R2d § 359.

**MBE vs. CA essay:** Not on the MBE. On the essay, the first element of every injunction or specific-performance analysis is "inadequate legal remedy"; say why damages fail.

**Example:** Π seeks to stop Δ from cutting down a 200-year-old oak on Π's land. Money cannot replace the tree, so the legal remedy is inadequate and equity may act.

> 🇨🇳 PRC bridge: PRC courts grant 继续履行 or 停止侵害 without an "inadequate damages" threshold; in the US that threshold is the gateway to every equitable remedy (approx.).

### R-REM-003 — Equity acts in personam; enforcing judgments
**Rule (write this):** A legal judgment for money is enforced by execution against the defendant's property (writs, levies, liens), and the plaintiff stands as an unsecured judgment creditor. An equitable decree operates on the defendant personally and is enforced by contempt: the court can fine or jail a defendant who disobeys. Because equity acts in personam, a court with personal jurisdiction over the defendant may order the defendant to act even with respect to property located elsewhere.

**Elements:** Legal: money judgment → execution. Equitable: personal order → contempt (R-REM-078).

**Exceptions / defenses:** A court cannot directly transfer title to land in another state, but it can order the defendant to convey. FRCP 70 lets a court have a disobeyed act done by another at the disobedient party's expense, or divest title to property within its jurisdiction.

**Authority:** FRCP 70; CCP §§ 1209, 1218 [S-473]; *Int'l Union, United Mine Workers v. Bagwell*, 512 U.S. 821 (1994).

**MBE vs. CA essay:** Not on the MBE. On the essay, the enforcement point explains why Π prefers an equitable remedy against an insolvent or uncooperative Δ (contempt, priority over creditors with a constructive trust).

**Example:** A California court with jurisdiction over Δ orders her to convey an Oregon cabin to Π under a land contract. If she refuses, she is in contempt.

### R-REM-004 — Jury trial with mixed legal and equitable claims
**Rule (write this):** In federal court the Seventh Amendment preserves a jury for legal claims; when legal and equitable claims share common factual issues, the legal claims are tried to the jury first so the judge's equitable findings do not foreclose the jury's determination. Equitable claims and remedies are decided by the judge.

**Elements:** 1. Classify each claim and remedy as legal or equitable. 2. Common issues of fact go to the jury first. 3. The judge then decides equitable relief consistent with the verdict.

**Exceptions / defenses:** The Seventh Amendment does not apply to the states. California's jury right (Cal. Const., art. I, § 16) follows the historical law/equity line; the court decides equitable claims and may try them first [VERIFY V-362].

**Authority:** U.S. Const. amend. VII; *Beacon Theatres, Inc. v. Westover*, 359 U.S. 500 (1959); *Dairy Queen, Inc. v. Wood*, 369 U.S. 469 (1962); *C & K Engineering Contractors v. Amber Steel Co.* (1978) 23 Cal.3d 1 [VERIFY V-362].

**MBE vs. CA essay:** Jury right is a Civil Procedure MBE topic; on a Remedies essay it is at most a one-line point when the call mentions trial.

**Example:** Π sues for breach of contract damages and specific performance arising from the same sale. The jury decides whether a contract was formed and breached; the judge then decides specific performance.

### R-REM-005 — Election of remedies and no double recovery
**Rule (write this):** A plaintiff may plead inconsistent remedies in the alternative but must elect among them before judgment and may not recover twice for the same loss. Expectation damages and restitution (or rescission) are generally inconsistent, because one affirms the contract and the other unwinds it. Damages and an injunction can be combined when they cover different periods or harms (damages for past harm, an injunction against future harm).

**Elements:** 1. List all available remedies. 2. Identify which overlap (same loss) and which are cumulative. 3. Choose the combination that maximizes recovery without duplication.

**Exceptions / defenses:** In California, a claim for damages is not inconsistent with relief based on rescission: the aggrieved party gets complete relief, including restitution and consequential damages, but no duplicate items (Civ. Code § 1692) [S-462]. Under the UCC, rescission for fraud does not bar damages (UCC § 2-721).

**Authority:** Civ. Code § 1692 [S-462]; *Runyan v. Pacific Air Industries, Inc.* (1970) 2 Cal.3d 304 [S-462]; UCC § 2-721; R2d § 378.

**MBE vs. CA essay:** Not on the MBE. On the essay, end with a short "Election / best remedy" paragraph recommending which remedy (or combination) best serves Π.

**Example:** A buyer defrauded into buying a condo may keep it and sue for damages, or rescind and recover the price plus consequential losses (in California, both via § 1692), but not keep the condo and also recover the price.

### R-REM-006 — The remedies essay framework
**Rule (write this):** For each claim, analyze remedies in this order: (1) legal remedies — compensatory damages with their limits (causation, foreseeability, certainty, mitigation), then nominal and punitive damages; (2) restitution — legal (quasi-contract, replevin, ejectment) and equitable (constructive trust, equitable lien); (3) equitable remedies — injunction (TRO, preliminary, permanent) or specific performance, element by element, with defenses; then conclude on which remedy best serves the plaintiff.

**Elements:** Damages → limits → punitive → restitution (legal, equitable) → coercive relief → defenses → election.

**Exceptions / defenses:** If the call names specific remedies ("TRO, preliminary injunction and specific performance"), answer only those, in the order named.

**Authority:** State Bar Remedies essay outline [S-091] [VERIFY V-024]; Phase 3 past-exam index [VERIFY V-071].

**MBE vs. CA essay:** Not on the MBE. This structure fits the open-ended call "What remedies can Π obtain?" (tested on about half of all administrations).

**Example:** Feb 2025 retest Q5 (encroaching fence) called for preliminary injunction, permanent injunction and damages; use three headings in that order, each with its elements [VERIFY V-071].

---

## II. Legal remedies (damages)

### R-REM-007 — Compensatory damages: purpose and kinds
**Rule (write this):** Compensatory damages are money awarded to put the plaintiff in the position it would have occupied had the wrong not occurred (tort) or had the contract been performed (contract). General damages flow naturally from the wrong; special (consequential) damages result from the plaintiff's particular circumstances and must be specifically pleaded and proven.

**Elements:** 1. A legal wrong. 2. Loss (detriment) to person or property. 3. Causation. 4. Measurement within the limits of foreseeability, certainty and mitigation (R-REM-008 to R-REM-011).

**Exceptions / defenses:** No loss → nominal damages only (R-REM-094).

**Authority:** Civ. Code §§ 3281, 3282, 3300, 3333 [S-469]; R2d § 347; *Hadley v. Baxendale* (1854) 9 Ex. 341.

**MBE vs. CA essay:** Not on the MBE. In California, the tort measure is "all the detriment proximately caused," whether it could have been anticipated or not (Civ. Code § 3333); the contract measure adds the foreseeability limit (Civ. Code § 3300).

**Example:** A negligent driver totals Π's car and breaks her arm. General damages: the car's value and pain and suffering. Special damages: medical bills, lost wages and the rental car.

### R-REM-008 — Causation
**Rule (write this):** The plaintiff must prove the defendant's wrong caused each item of loss: the loss would not have occurred but for the wrong, or the wrong was a substantial factor in bringing it about. In tort, the loss must also fall within the scope of proximate cause.

**Elements:** 1. Actual cause (but-for / substantial factor). 2. Proximate cause (tort) or foreseeability at contracting (contract).

**Exceptions / defenses:** Intervening superseding causes cut off liability; the eggshell-plaintiff rule makes Δ liable for the full extent of a physical injury even if unforeseeably severe.

**Authority:** Civ. Code §§ 3300, 3333 [S-469]; R2d § 347.

**MBE vs. CA essay:** Not on the MBE (causation in negligence is a Torts MBE topic). On a Remedies essay, give each item of damages one causation sentence.

**Example:** A contractor's late completion delays Π's restaurant opening. Profits lost during the delay are caused by the breach; losses from a later citywide shutdown are not.

### R-REM-009 — Foreseeability: contract vs. tort
**Rule (write this):** In contract, consequential damages are recoverable only if they were foreseeable to the breaching party at the time of contracting, either because they arise naturally from the breach or because of special circumstances the breaching party knew of (*Hadley v. Baxendale*). In tort, the plaintiff recovers all detriment proximately caused by the wrong, so the test is proximate cause rather than foreseeability at the time of any agreement.

**Elements:** Contract: (1) general damages, or (2) special damages + Δ's knowledge of the special circumstances at formation. Tort: proximate cause.

**Exceptions / defenses:** Contract: a court may limit foreseeable damages to avoid disproportionate compensation (R2d § 351(3)). Tort: intentional tortfeasors are liable for a broader range of consequences.

**Authority:** *Hadley v. Baxendale* (1854) 9 Ex. 341; R2d § 351; UCC § 2-715(2)(a); Civ. Code §§ 3300, 3333 [S-469]; cross-reference R-CTR-092.

**MBE vs. CA essay:** Not on the MBE for Remedies (the contract rule is a Contracts MBE topic). On the essay, label each item "general" or "consequential" and test foreseeability for consequential items.

**Example:** A shipper loses a mill's broken crankshaft. Lost mill profits are not recoverable unless the shipper knew at contracting that the mill was idle without the shaft.

> 🇨🇳 PRC bridge: similar to the PRC Civil Code's 可预见性规则 for contract damages (approx.).

### R-REM-010 — Certainty
**Rule (write this):** Damages must be proven with reasonable certainty: the fact of loss must be established with certainty, but the amount may be a reasonable estimate. Lost profits of an established business may be proven from its history; lost profits of a new or unestablished business are recoverable only if proven by reliable evidence such as comparable businesses, market data or expert projections. If expectation damages are too speculative, the plaintiff may fall back on reliance damages or restitution.

**Elements:** 1. Fact of loss certain. 2. Amount reasonably estimable. 3. Lost profits: established business history, or reliable comparables for a new venture.

**Exceptions / defenses:** The traditional "new business rule" barred lost profits outright; modern courts treat it as an evidentiary hurdle. Uncertainty created by Δ's own wrong is resolved against Δ.

**Authority:** R2d § 352; Civ. Code § 3301; *Sargon Enterprises, Inc. v. University of Southern California* (2012) 55 Cal.4th 747 [VERIFY V-366]; cross-reference R-CTR-093.

**MBE vs. CA essay:** Not on the MBE for Remedies. On the essay, address certainty for every lost-profit claim and say whether reliance damages are the better fallback.

**Example:** A brand-new food truck loses its permit through Δ's breach. Its projected profits are speculative, so it recovers its reliance expenditures instead (R-CTR-107).

### R-REM-011 — Mitigation (avoidable consequences)
**Rule (write this):** A plaintiff cannot recover damages for losses it could have avoided with reasonable effort and without undue risk, burden or humiliation after the wrong. The defendant bears the burden of proving the plaintiff failed to mitigate, and the plaintiff recovers the reasonable costs of mitigation even if the effort fails.

**Elements:** 1. A loss that reasonable steps would have avoided. 2. Δ proves the failure. 3. Recovery reduced by the avoidable amount; mitigation costs added.

**Exceptions / defenses:** An employee need not accept different or inferior work (*Parker v. Twentieth Century-Fox Film Corp.* (1970) 3 Cal.3d 176). A lost-volume seller's resale is not mitigation. In tort, the same avoidable-consequences rule applies (e.g., failing to get medical care).

**Authority:** R2d § 350; R2d Torts § 918 [VERIFY V-363]; *Rockingham County v. Luten Bridge Co.*, 35 F.2d 301 (4th Cir. 1929); cross-reference R-CTR-095.

**MBE vs. CA essay:** Not on the MBE for Remedies. On the essay, give a short mitigation paragraph in every damages answer, using any facts about what Π did after the wrong.

**Example:** After Δ's fence blocks Π's driveway, Π lets his delivery business lapse for six months rather than renting a nearby space for $500 a month. His lost profits are reduced to what renting would have avoided, plus the rent.

> 🇨🇳 PRC bridge: the PRC Civil Code also has a 减损规则 (duty to take appropriate measures to prevent further loss) (approx.).

### R-REM-012 — Collateral source rule
**Rule (write this):** Benefits the plaintiff receives from a source independent of the tortfeasor, such as insurance or gifts, do not reduce the tortfeasor's liability for damages. In California, however, a plaintiff's recovery for past medical expenses is limited to the amounts actually paid or incurred, not the higher amounts billed.

**Elements:** 1. A benefit to Π. 2. From a source wholly independent of Δ. 3. Δ gets no credit.

**Exceptions / defenses:** Payments by Δ or Δ's insurer do reduce liability. Contract damages do not generally follow the rule.

**Authority:** *Helfend v. Southern Cal. Rapid Transit Dist.* (1970) 2 Cal.3d 1 [S-472]; *Howell v. Hamilton Meats & Provisions, Inc.* (2011) 52 Cal.4th 541 [S-472]; R2d Torts § 920A [VERIFY V-363].

**MBE vs. CA essay:** Not on the MBE for Remedies (it appears in Torts). On a Remedies/Torts essay, one sentence: Δ gets no credit for Π's insurance; in California, medical damages are capped at the amount paid.

**Example:** Π's insurer pays $40,000 of a $90,000 hospital bill, which the hospital accepts in full payment. Δ cannot reduce damages because insurance paid; under *Howell*, past medical damages are $40,000, not $90,000.

### R-REM-013 — Future losses and present value
**Rule (write this):** A plaintiff recovers in a single action for all past and reasonably certain future losses caused by the wrong, such as future medical costs, lost earning capacity and future pain and suffering. Future economic losses are reduced to present value; non-economic damages are left to the jury's judgment.

**Elements:** 1. Future loss reasonably certain. 2. Estimated amount. 3. Discount economic losses to present value.

**Exceptions / defenses:** A continuing nuisance or trespass allows successive suits instead of one award for all future harm (R-REM-024).

**Authority:** Civ. Code § 3283 (damages for detriment certain to result in the future); R2d Torts § 913A [VERIFY V-363].

**MBE vs. CA essay:** Not on the MBE for Remedies. One sentence on the essay when Π's injuries are permanent.

**Example:** A 30-year-old surgeon loses fine motor control. She recovers the present value of her lost lifetime earning capacity, not the raw sum of future salaries.

### R-REM-014 — Contract damages: expectation, reliance, restitution
**Rule (write this):** For breach of contract the injured party ordinarily recovers expectation damages — the value of the promised performance, plus incidental and consequential damages, minus costs avoided — subject to foreseeability, certainty and mitigation. If expectation cannot be proven with certainty, it may recover reliance damages (expenditures in preparation and performance) or restitution of the benefit conferred.

**Elements:** Expectation formula (R-CTR-089); UCC buyer's and seller's measures (R-CTR-099, R-CTR-102, R-CTR-103); reliance (R-CTR-107); restitution (R-CTR-108, R-CTR-109).

**Exceptions / defenses:** No punitive damages for breach (R-REM-031); emotional-distress damages only in limited contracts (R-REM-025).

**Authority:** R2d §§ 344, 347, 349, 371; UCC §§ 2-706, 2-708, 2-710, 2-711 to 2-715; Civ. Code §§ 3300, 3358; cross-reference R-CTR-089 to R-CTR-109.

**MBE vs. CA essay:** The contract measures are tested on the Contracts MBE. On a Remedies essay, state the measure, compute it with the facts' numbers, then apply the limits.

**Example:** A caterer repudiates a $20,000 wedding contract; a substitute costs $26,000. Expectation damages are $6,000 plus incidental search costs.

### R-REM-015 — Land-sale contracts: buyer's damages when the seller breaches
**Rule (write this):** When a seller wrongfully refuses to convey, the buyer may recover the difference between the market value of the land at the time of breach and the contract price, plus incidental and foreseeable consequential damages and the return of any payments. Under the minority "English rule," a seller who cannot convey because of a title defect, and who acted in good faith, is liable only for the buyer's deposit and expenses.

**Elements:** 1. Breach by seller. 2. Market value at breach − contract price. 3. Plus deposit returned, title/escrow expenses, consequential damages. 4. Alternative: specific performance (R-REM-071).

**Exceptions / defenses:** A bad-faith seller is liable for benefit-of-the-bargain damages under every rule.

**Authority:** Majority (American) rule; *Flureau v. Thornhill* (1776) (English rule); Civ. Code § 3306 (price paid, title and document expenses, the difference between price and value at breach, expenses of preparing to enter, consequential damages, interest) [S-461] [VERIFY V-355].

**MBE vs. CA essay:** Land-sale damages are a Real Property MBE topic. On the essay, state the benefit-of-the-bargain measure; in California, § 3306 gives that measure without a good-faith limitation [VERIFY V-355].

**Example:** S contracts to sell Blackacre to B for $500,000 and refuses to close when the value rises to $560,000. B recovers $60,000 plus her deposit and escrow costs, or seeks specific performance.

### R-REM-016 — Land-sale contracts: seller's damages when the buyer breaches
**Rule (write this):** When a buyer wrongfully refuses to complete the purchase, the seller may recover the contract price minus the market value of the land at the time of breach, plus incidental damages such as resale costs, less any deposit retained. A resale at arm's length shortly after breach is evidence of market value. A seller may keep a deposit only to the extent it is a valid liquidated-damages amount or does not exceed actual damages.

**Elements:** 1. Buyer's breach. 2. Contract price − market value at breach. 3. Plus incidental and foreseeable consequential damages. 4. Credit for deposit.

**Exceptions / defenses:** In California, even a willfully defaulting buyer recovers the deposit in excess of the seller's actual damages (*Freedman v. Rector* (1951) 37 Cal.2d 16 [S-210]); residential deposits are governed by Civ. Code §§ 1675–1678 [VERIFY V-107].

**Authority:** Civ. Code § 3307 [S-461]; Civ. Code § 1671 [S-200]; cross-reference R-CTR-096, R-CTR-109.

**MBE vs. CA essay:** Real Property MBE topic. On the essay, compute the difference and address the deposit.

**Example:** B backs out of a $700,000 purchase; the market value at breach is $660,000 and S spends $5,000 relisting. S recovers $45,000, credited against B's $35,000 deposit, leaving $10,000.

### R-REM-017 — Liquidated damages
**Rule (write this):** A contract clause fixing damages is enforceable if, at the time of contracting, actual damages were difficult to estimate and the amount was a reasonable forecast of the probable loss; a clause that is unreasonably large is an unenforceable penalty, and the plaintiff is left to actual damages. A valid clause is usually the exclusive measure of damages for the breach it covers.

**Elements:** 1. Damages difficult to estimate at formation. 2. Reasonable forecast. 3. Not intended as a penalty.

**Exceptions / defenses:** A valid clause does not by itself bar specific performance unless the clause is meant as an exclusive alternative. In California, a clause in most contracts is presumed valid unless the challenger proves it was unreasonable when made (Civ. Code § 1671(b)); consumer and residential-lease clauses are void unless actual damages would be impracticable or extremely difficult to fix (§ 1671(c)–(d)) [S-200] [VERIFY V-107].

**Authority:** R2d § 356; UCC § 2-718(1); Civ. Code § 1671 [S-200]; cross-reference R-CTR-096.

**MBE vs. CA essay:** The general rule is a Contracts MBE topic. On the essay, add the § 1671(b) presumption in one sentence when the clause is in a commercial contract.

**Example:** A construction contract sets $1,000 per day of delay for a hotel whose lost room revenue was hard to forecast. The clause is a reasonable forecast and is enforced.

### R-REM-018 — Personal injury damages
**Rule (write this):** A personally injured plaintiff recovers economic damages (past and future medical expenses, lost earnings and lost earning capacity, and other out-of-pocket costs) and non-economic damages (past and future pain and suffering, emotional distress, disfigurement, loss of enjoyment of life). The defendant takes the plaintiff as it finds her and is liable for the full extent of the injury, even if a pre-existing condition made it unusually severe.

**Elements:** 1. Economic items, each proven with reasonable certainty. 2. Non-economic items, valued by the trier of fact. 3. Future items reduced to present value (economic).

**Exceptions / defenses:** Mitigation (failure to seek treatment); comparative fault reduces recovery (Torts). In California, each defendant's liability for non-economic damages is several only, in proportion to fault (Civ. Code § 1431.2) [VERIFY V-363].

**Authority:** Civ. Code § 3333 [S-469]; R2d Torts §§ 903, 905, 924 [VERIFY V-363]; *Howell* (2011) 52 Cal.4th 541 [S-472].

**MBE vs. CA essay:** Damages are an occasional Torts MBE topic. On a Torts/Remedies essay, list the categories and match each to a fact.

**Example:** Π, a hemophiliac, bleeds heavily after a minor battery. Δ is liable for the full medical cost and Π's suffering under the eggshell-plaintiff rule.

### R-REM-019 — Damages for harm to land
**Rule (write this):** For physical harm to land or structures, the plaintiff recovers either the diminution in the property's market value or the reasonable cost of restoring it, usually whichever is less, plus damages for loss of use and, in an action by an occupant, discomfort and annoyance. Restoration costs exceeding the diminution in value may be awarded where the owner has a personal reason to restore the property to its original condition and the cost is reasonable.

**Elements:** 1. Harm to land. 2. Diminution in value vs. cost of restoration. 3. Loss of use / annoyance. 4. Personal-reason exception for restoration.

**Exceptions / defenses:** Statutory multiples for injuries to trees (R-REM-020).

**Authority:** R2d Torts § 929 [VERIFY V-363]; *Heninger v. Dunn* (1980) 101 Cal.App.3d 858 [S-477]; Civ. Code § 3333 [S-469].

**MBE vs. CA essay:** Not on the MBE for Remedies. On the essay, give both measures, compute them, and argue whether the personal-reason exception applies.

**Example:** Δ bulldozes a 50-year-old native garden on Π's lot. Market value drops $8,000, but restoring the plantings costs $40,000. Because Π lives there and valued the garden personally, a court may award a reasonable restoration cost above the $8,000 diminution.

### R-REM-020 — Trespass, encroachment, wrongful occupation and injury to trees
**Rule (write this):** A trespass to land is actionable without proof of harm, so the plaintiff recovers at least nominal damages, plus actual damage to the land and, for wrongful occupation, the reasonable rental value of the use (mesne profits). For a permanent encroachment that is allowed to remain, the owner recovers the value of the land taken or the diminution in value of the whole parcel. In California, damages for wrongful injury to trees or timber on another's land are trebled, or only doubled where the trespass was casual and involuntary or the defendant believed the land was its own.

**Elements:** 1. Intentional entry (trespass) or encroachment. 2. Measure: nominal; physical harm (R-REM-019); rental value of use; value of land taken. 3. Statutory multiple for trees (California).

**Exceptions / defenses:** The tree multiplier requires a trespass on another's land and does not reach negligently spread fires (*Scholes v. Lambirth Trucking Co.* (2020)) [S-460] [VERIFY V-354].

**Authority:** Civ. Code §§ 3334 (wrongful occupation) [VERIFY V-357], 3346 [S-460] [VERIFY V-354]; R2d Torts §§ 158, 929 [VERIFY V-363].

**MBE vs. CA essay:** Not on the MBE for Remedies. On a California essay involving trees (Feb 2015 Q4's oak tree [VERIFY V-071]), mention § 3346 multiple damages and the injunction to prevent cutting.

**Example:** Δ, knowing the boundary, cuts three of Π's mature redwoods to improve his view. Π recovers the trees' value (or restoration cost) trebled under § 3346.

### R-REM-021 — Conversion damages
**Rule (write this):** A plaintiff whose chattel was converted recovers its fair market value at the time and place of conversion, plus interest from that date; in effect the defendant is forced to buy the chattel. Alternatively, the plaintiff may recover the specific chattel by replevin (R-REM-041) or the defendant's gain from selling or using it by restitution (R-REM-037).

**Elements:** 1. Conversion (serious interference with Π's right to control a chattel). 2. Value at the time of conversion + interest. 3. Consequential losses where proven.

**Exceptions / defenses:** In California the value at conversion plus interest is the presumed measure; Π may instead recover an amount sufficient to indemnify for the natural and proximate loss, plus fair compensation for time and money properly spent pursuing the property (Civ. Code § 3336) [S-468] [VERIFY V-357]. Property with a peculiar value to its owner may be valued at that value against a willful wrongdoer or one with notice (Civ. Code § 3355) [VERIFY V-357].

**Authority:** R2d Torts §§ 222A, 927 [VERIFY V-363]; Civ. Code § 3336 [S-468]; CACI No. 2102 [S-468].

**MBE vs. CA essay:** Conversion is a Torts topic. On a Remedies essay, compare the damages measure (value at conversion) with replevin (get the thing back) and restitution (Δ's resale profit), and recommend one.

**Example:** Δ takes Π's vintage guitar worth $8,000 and sells it for $12,000. Π may recover $8,000 plus interest in damages, or $12,000 in restitution, or replevy the guitar if it can be found.

### R-REM-022 — Trespass to chattels and damage to personal property
**Rule (write this):** For a lesser interference with a chattel, or for damage to it, the plaintiff recovers the cost of repair or the diminution in value, plus the value of the lost use (for example, reasonable rental of a substitute) during the period of deprivation. Where repair would cost more than the chattel was worth, the loss is treated as total and measured by pre-injury value.

**Elements:** 1. Intermeddling or damage. 2. Repair cost or diminution. 3. Loss of use.

**Exceptions / defenses:** Mitigation: Π must arrange repairs within a reasonable time.

**Authority:** R2d Torts §§ 217, 218, 928 [VERIFY V-363]; Civ. Code § 3333 [S-469].

**MBE vs. CA essay:** Torts topic; one sentence on a Remedies essay.

**Example:** Δ borrows Π's delivery van without permission and dents it. Π recovers the $1,500 repair bill and $300 for renting a van for three days.

### R-REM-023 — Fraud damages: out-of-pocket vs. benefit of the bargain
**Rule (write this):** A defrauded party may recover either its out-of-pocket loss (the value of what it gave minus the value of what it received) or, under the majority rule for fraud in a bargaining transaction, its benefit of the bargain (the value the property would have had if as represented minus the value received), plus consequential damages and, for intentional fraud, punitive damages. In California, a person defrauded in the purchase, sale or exchange of property is limited to out-of-pocket loss plus additional consequential damages (Civ. Code § 3343), except that some courts allow benefit-of-the-bargain damages against a fiduciary.

**Elements:** 1. Fraud established (Torts). 2. Choose the measure. 3. Consequential and punitive damages. 4. Alternative: rescission and restitution (R-REM-043).

**Exceptions / defenses:** Benefit-of-the-bargain damages must be proven with reasonable certainty.

**Authority:** R2d Torts § 549 [VERIFY V-363]; Civ. Code § 3343 [VERIFY V-351]; *Alliance Mortgage Co. v. Rothwell* (1995) 10 Cal.4th 1226 [S-453]; CACI Nos. 1923–1924 [S-454].

**MBE vs. CA essay:** Not on the MBE. On a California essay (fraud in a sale: Jul 2024 Q5 baseballs; Feb 2017 Q2 condo [VERIFY V-071]), give the general benefit-of-the-bargain rule, then "In California, § 3343 limits a defrauded buyer to out-of-pocket loss unless Δ was a fiduciary."

**Example:** Δ sells Π a baseball, falsely "signed by Babe Ruth," for $50,000. Genuine, it would be worth $80,000; unsigned, it is worth $200. Out-of-pocket: $49,800. Benefit of the bargain: $79,800.

### R-REM-024 — Nuisance damages: permanent vs. continuing
**Rule (write this):** If a nuisance is permanent (it cannot or will not be abated at reasonable cost), the plaintiff recovers in one action all past and future damages, measured by the diminution in the property's market value. If it is continuing (abatable), the plaintiff recovers only past damages, including loss of use and discomfort and annoyance, and may sue again for later harm or seek an injunction.

**Elements:** 1. Nuisance established. 2. Permanent or continuing? 3. Matching measure.

**Exceptions / defenses:** Coming to the nuisance is a factor, not a bar (R-REM-062).

**Authority:** R2d Torts §§ 929, 930 [VERIFY V-363]; *Boomer v. Atlantic Cement Co.*, 26 N.Y.2d 219 (1970).

**MBE vs. CA essay:** Not on the MBE for Remedies. On a nuisance/remedies essay (Feb 2022 Q3 theater noise [VERIFY V-071]), state both measures, then turn to the injunction.

**Example:** A plant's dust can be stopped with $50,000 filters. The nuisance is continuing: Π recovers past annoyance and loss-of-use damages and seeks an injunction requiring the filters.

### R-REM-025 — Emotional-distress damages
**Rule (write this):** Emotional-distress damages are recoverable as part of the damages for intentional torts, for intentional or negligent infliction of emotional distress within those torts' limits, and as discomfort and annoyance in trespass and nuisance. In contract, they are recoverable only where the breach also caused bodily harm or the contract or breach is of a kind that makes serious emotional disturbance particularly likely.

**Elements:** 1. Tort: proven distress caused by the tort. 2. Contract: bodily harm, or a contract whose central purpose is emotional (funeral, mortuary, delivery of death notice).

**Exceptions / defenses:** California denies emotional-distress damages for negligent construction of a home (*Erlich v. Menezes* (1999) 21 Cal.4th 543).

**Authority:** R2d § 353; *Erlich v. Menezes* (1999) 21 Cal.4th 543; cross-reference R-CTR-098.

**MBE vs. CA essay:** Not on the MBE for Remedies. One sentence on the essay; flag the contract limit.

**Example:** A mortuary loses Π's mother's remains. Distress damages are recoverable because the contract's purpose made distress particularly likely.

### R-REM-026 — Punitive damages: the general standard
**Rule (write this):** Punitive (exemplary) damages may be awarded to punish and deter a defendant whose tortious conduct was malicious, willful and wanton, or in reckless disregard of the plaintiff's rights; they are not available for mere negligence or for breach of contract. The amount considers the reprehensibility of the conduct, the harm caused, and the defendant's wealth, within due-process limits.

**Elements:** 1. A tort (not mere breach). 2. Aggravated mental state (malice, oppression, fraud, reckless indifference). 3. Usually an award of actual damages. 4. Amount within due-process limits (R-REM-027).

**Exceptions / defenses:** Many states require clear and convincing evidence; some states bar or cap punitive damages by statute.

**Authority:** R2d Torts § 908 [VERIFY V-363]; R2d § 355; Civ. Code § 3294 [S-451].

**MBE vs. CA essay:** Not on the MBE. On a California essay, state this rule, then the California § 3294 standard (R-REM-028).

**Example:** A landlord who removes a tenant's door to force her out mid-winter commits a willful tort; punitive damages are available. A landlord who negligently fails to fix a heater is not liable for punitive damages.

> 🇨🇳 PRC bridge: the PRC Civil Code allows 惩罚性赔偿 only in specified areas, such as knowing sale of defective products, serious intentional IP infringement and intentional environmental harm; US punitive damages are a general tort remedy for aggravated conduct (approx.).

### R-REM-027 — Punitive damages: due-process limits
**Rule (write this):** A grossly excessive punitive award violates the Due Process Clause. Courts review it under three guideposts: (1) the degree of reprehensibility of the defendant's conduct (the most important), (2) the ratio between the punitive award and the actual or potential harm to the plaintiff, and (3) the difference between the award and civil penalties for comparable misconduct. Few awards exceeding a single-digit ratio satisfy due process, and where compensatory damages are substantial a ratio near 1:1 may be the limit.

**Elements:** Reprehensibility factors: physical (not merely economic) harm; indifference to health or safety; a financially vulnerable target; repeated conduct; intentional malice, trickery or deceit rather than accident.

**Exceptions / defenses:** A jury may not punish the defendant directly for harm to non-parties, though that harm may bear on reprehensibility (*Philip Morris USA v. Williams*, 549 U.S. 346 (2007)). Punishment must be for conduct that harmed the plaintiff, not dissimilar or out-of-state lawful conduct.

**Authority:** U.S. Const. amend. XIV; *BMW of North America, Inc. v. Gore*, 517 U.S. 559 (1996); *State Farm Mut. Auto. Ins. Co. v. Campbell*, 538 U.S. 408 (2003); *Pacific Mut. Life Ins. Co. v. Haslip*, 499 U.S. 1 (1991).

**MBE vs. CA essay:** Not on the MBE. On the essay, apply the three guideposts to the facts whenever the facts give a punitive figure or a large ratio.

**Example:** A jury awards $10,000 compensatory and $2 million punitive damages for a car dealer's undisclosed repainting. The 200:1 ratio, purely economic harm and comparable fines of a few thousand dollars make the award grossly excessive (the *Gore* pattern).

### R-REM-028 — Punitive damages in California (Civil Code § 3294)
**Rule (write this):** In California, punitive damages may be recovered in an action for breach of an obligation not arising from contract where the plaintiff proves by clear and convincing evidence that the defendant was guilty of oppression, fraud or malice. Malice is conduct intended to injure the plaintiff, or despicable conduct carried on with a willful and conscious disregard of the rights or safety of others; oppression is despicable conduct that subjects a person to cruel and unjust hardship in conscious disregard of that person's rights; fraud is an intentional misrepresentation, deceit or concealment of a material fact known to the defendant, intended to deprive a person of property or legal rights or otherwise cause injury.

**Elements:** 1. A non-contract claim (tort). 2. Oppression, fraud or malice as defined. 3. Clear and convincing evidence. 4. Predicates: actual damages and evidence of Δ's financial condition (R-REM-030).

**Exceptions / defenses:** No punitive damages for breach of contract, however willful (R-REM-031). Evidence of Δ's profits or financial condition is held back until liability for punitive damages is found, on Δ's application (Civ. Code § 3295(d)) [VERIFY V-369].

**Authority:** Civ. Code § 3294(a), (c) [S-451] [VERIFY V-369]; Civ. Code § 3295.

**MBE vs. CA essay:** Not on the MBE. On a California essay, cite § 3294 by number; graders reward "clear and convincing evidence of oppression, fraud or malice."

**Example:** A seller who knowingly conceals termite damage to close a house sale commits fraud as defined in § 3294(c)(3); punitive damages are available on clear and convincing proof.

### R-REM-029 — Punitive damages against employers and entities
**Rule (write this):** Under the general (complicity) approach, an employer is liable for punitive damages based on an employee's act only if it authorized or ratified the act, was reckless in employing an unfit employee, or the employee was a managerial agent acting in the scope of employment. In California, an employer is liable for punitive damages based on an employee's conduct only if it had advance knowledge of the employee's unfitness and employed him with conscious disregard of others' rights or safety, authorized or ratified the wrongful conduct, or was itself guilty of oppression, fraud or malice; for a corporation, that knowledge, authorization, ratification or act must be by an officer, director or managing agent.

**Elements:** 1. Employee's malicious conduct. 2. Corporate fault through an officer, director or managing agent. 3. A managing agent exercises substantial discretionary authority over decisions that ultimately determine corporate policy.

**Exceptions / defenses:** The power to hire and fire alone does not make a supervisor a managing agent.

**Authority:** Civ. Code § 3294(b) [S-451]; *White v. Ultramar, Inc.* (1999) 21 Cal.4th 563 [S-452]; R2d Torts § 909 [VERIFY V-363].

**MBE vs. CA essay:** Not on the MBE. Use on a Torts/BA/Remedies crossover where the defendant is a company.

**Example:** A store clerk falsely imprisons a shopper. The chain is liable for compensatory damages under respondeat superior, but for punitive damages only if, say, the regional manager who sets loss-prevention policy ratified the detention.

### R-REM-030 — Punitive damages: predicates (actual damages; financial condition)
**Rule (write this):** Most courts require an award of compensatory damages before punitive damages may be awarded; jurisdictions divide on whether nominal damages suffice. In California, actual damages are a predicate for punitive damages, and the plaintiff must introduce evidence of the defendant's financial condition, because a reviewing court cannot judge whether the award is excessive without it.

**Elements:** 1. Actual damages awarded. 2. Π's evidence of Δ's financial condition (net worth or comparable measure; income alone is inadequate).

**Exceptions / defenses:** Without financial-condition evidence, a California punitive award is reversed.

**Authority:** *Adams v. Murakami* (1991) 54 Cal.3d 105 [S-464]; *Cheung v. Daley* (1995) 35 Cal.App.4th 1673 [S-470]; *Kizer v. County of San Mateo* (1991) and *Mother Cobb's Chicken Turnovers, Inc. v. Fox* (1937) [VERIFY V-356].

**MBE vs. CA essay:** Not on the MBE. One sentence on a California essay that asks about punitive damages.

**Example:** A jury awards $1 nominal and $50,000 punitive damages for a trespass that caused no harm. In California, the punitive award fails for lack of actual damages [VERIFY V-356].

### R-REM-031 — No punitive damages for breach of contract
**Rule (write this):** Punitive damages are not recoverable for breach of contract, even a willful breach, unless the conduct constituting the breach is also an independent tort for which punitive damages are recoverable.

**Elements:** 1. Is there an independent tort (fraud, conversion, bad faith by an insurer)? 2. If so, apply R-REM-028.

**Exceptions / defenses:** California recognizes tort liability for breach of the implied covenant of good faith only in the insurance context.

**Authority:** R2d § 355; Civ. Code § 3294(a) [S-451] ("obligation not arising from contract"); cross-reference R-CTR-098, R-CTR-117.

**MBE vs. CA essay:** The contract rule is a Contracts MBE topic. On the essay, say no punitives for the breach, then ask whether a tort claim (fraud) opens the door.

**Example:** A supplier cuts off deliveries to extract a higher price. However cynical, that is a breach of contract: no punitive damages unless the supplier also lied in a way that amounts to fraud.

### R-REM-032 — Economic loss rule
**Rule (write this):** A party to a contract generally cannot recover in tort for purely economic losses caused by the other party's failure to perform; the economic loss rule confines such losses to contract remedies. Tort recovery remains available where the defendant breached a duty independent of the contract, such as fraud inducing the contract, conduct causing personal injury or damage to other property, or, in California, fraudulent concealment during performance that meets every element of the tort independently and exposes the plaintiff to a risk of harm beyond what the parties contemplated.

**Elements:** 1. Contractual relationship. 2. Purely economic loss? 3. Independent tort duty and harm beyond the bargain?

**Exceptions / defenses:** Physical injury to persons or to property other than the product itself takes the claim outside the rule.

**Authority:** *Robinson Helicopter Co., Inc. v. Dana Corp.* (2004) 34 Cal.4th 979; *Rattagan v. Uber Technologies, Inc.* (2024) 17 Cal.5th 1 [S-132]; cross-reference R-CTR-117.

**MBE vs. CA essay:** Not tested as a Remedies MBE rule. On a California essay, it decides whether tort remedies (punitive damages, § 3333 measure) are open; cite *Rattagan* for fraud during performance.

**Example:** A contractor knowingly hides that it used substandard rebar while performing a building contract, exposing the owner to collapse risk. Under *Rattagan* the owner may sue in fraud as well as contract and seek punitive damages.

### R-REM-033 — Attorney's fees and costs
**Rule (write this):** Under the American rule, each party pays its own attorney's fees unless a statute or contract provides otherwise. Prevailing parties recover costs as provided by statute.

**Elements:** 1. Fee-shifting statute (e.g., 42 U.S.C. § 1988; Cal. CCP § 1021.5 private attorney general). 2. Contract clause. 3. Equitable exceptions (common fund; bad-faith litigation).

**Exceptions / defenses:** In California, a contractual fee clause for one party is reciprocal: the prevailing party on the contract recovers fees whether or not the clause names it (Civ. Code § 1717).

**Authority:** CCP §§ 1021, 1021.5; Civ. Code § 1717; 42 U.S.C. § 1988.

**MBE vs. CA essay:** Not on the MBE. One line on the essay when the facts mention a fee clause or a public-interest claim.

**Example:** A lease says the landlord recovers fees if it sues to collect rent. The tenant wins the landlord's suit and recovers its fees under § 1717.

### R-REM-034 — Prejudgment interest
**Rule (write this):** A plaintiff entitled to damages that are certain, or capable of being made certain by calculation, recovers interest from the day the right to recover vested. Interest on unliquidated damages is discretionary, and in California tort cases and cases of oppression, fraud or malice it may be awarded in the trier of fact's discretion.

**Elements:** 1. Liquidated (certain) sum → interest as of right. 2. Unliquidated → discretionary.

**Exceptions / defenses:** Conversion damages carry interest from the conversion (R-REM-021).

**Authority:** Civ. Code §§ 3287, 3288 [VERIFY V-359]; Civ. Code § 3336 [S-468].

**MBE vs. CA essay:** Not on the MBE. A one-line add-on to a damages paragraph.

**Example:** A buyer fails to pay a $40,000 invoice due March 1. The seller recovers $40,000 plus interest from March 1.

---

## III. Restitution

### R-REM-035 — Purpose of restitution; unjust enrichment
**Rule (write this):** Restitution prevents unjust enrichment: a person who has been unjustly enriched at the expense of another must restore the benefit. Unlike damages, which measure the plaintiff's loss, restitution measures the defendant's gain, so it is the better remedy when the defendant gained more than the plaintiff lost, when the plaintiff's loss is hard to prove, or when no enforceable contract exists.

**Elements:** 1. Δ received a benefit. 2. At Π's expense. 3. Retention without payment would be unjust.

**Exceptions / defenses:** No restitution for gifts, for benefits conferred officiously, or where a valid contract allocates the risk (R-REM-040). Bona fide purchaser and change of position defenses (R-REM-049).

**Authority:** R3RUE § 1 [VERIFY V-350]; R2d §§ 344(c), 370–371; Civ. Code §§ 2223, 2224 [S-463].

**MBE vs. CA essay:** Restitution in contract is a Contracts MBE topic. On a Remedies essay, open the restitution section with this rule, then choose legal or equitable restitution. California courts disagree whether "unjust enrichment" is itself a cause of action; plead it as quasi-contract or a constructive trust [VERIFY V-361].

**Example:** A bank mistakenly credits $25,000 to Δ's account and Δ spends it on a car. The bank lost $25,000 and Δ gained $25,000: restitution is available even though no contract or tort exists.

> 🇨🇳 PRC bridge: close to 不当得利 in the PRC Civil Code; but US equitable restitution (constructive trust) can give a property right with priority over creditors, which a PRC 不当得利 claim (a 债权) does not (approx.).

### R-REM-036 — Measuring restitution: innocent recipient vs. conscious wrongdoer
**Rule (write this):** Restitution is measured by the benefit to the defendant. An innocent recipient pays the reasonable value of what it received, or, where more just, only the actual increase in its wealth. A conscious wrongdoer or a fiduciary in breach must disgorge the full gain, including profits made from the plaintiff's property, and is not allowed to keep any of the profit.

**Elements:** 1. Characterize Δ: innocent or conscious wrongdoer. 2. Value of benefit (market value of goods or services) vs. increase in Δ's assets vs. Δ's profits. 3. Choose the measure that fits Δ's culpability.

**Exceptions / defenses:** An innocent recipient who changed position in good faith may reduce liability (R-REM-049).

**Authority:** R2d § 371; R3RUE §§ 49–51 [VERIFY V-350].

**MBE vs. CA essay:** Not on the MBE in this form. On the essay, say which measure applies and why (Δ's state of mind).

**Example:** Δ, believing in good faith that he owned it, paints Π's fence at a market value of $2,000; the house's value rises $500. A court may limit restitution to $500 for an innocent improver. Had Δ knowingly used Π's paint, Π would recover its full value.

### R-REM-037 — Disgorgement of profits ("waiver of tort")
**Rule (write this):** A plaintiff whose property was wrongfully taken or used may "waive the tort and sue in assumpsit," recovering the defendant's gain from the wrong (sale proceeds, profits or the value of use saved) instead of the plaintiff's loss. This is valuable when the defendant's gain exceeds the plaintiff's loss.

**Elements:** 1. Δ's wrong (conversion, trespass, fraud, breach of fiduciary duty, IP infringement). 2. Δ's measurable gain. 3. Causal link between the wrong and the gain.

**Exceptions / defenses:** Π must elect: it cannot recover both its loss and Δ's gain for the same item (R-REM-005).

**Authority:** *Olwell v. Nye & Nissen Co.*, 26 Wash.2d 282 (1946); R3RUE §§ 40–44, 51 [VERIFY V-350].

**MBE vs. CA essay:** Not on the MBE. On the essay, compare damages (Π's loss) with disgorgement (Δ's gain) using the numbers.

**Example:** Δ secretly uses Π's idle egg-washing machine for three years, saving $10,000 in labor; the machine's rental value was $1,500. Π recovers the $10,000 Δ saved (*Olwell*).

### R-REM-038 — Quasi-contract (contract implied in law)
**Rule (write this):** Quasi-contract is a legal restitutionary remedy that imposes an obligation to pay for a benefit where no enforceable contract exists: the plaintiff conferred a benefit on the defendant, the defendant knew of and accepted or retained it, and it would be unjust for the defendant to keep it without paying. Recovery is a money judgment for the reasonable value of the benefit.

**Elements:** 1. Benefit conferred. 2. Δ's knowledge and acceptance or retention. 3. Unjust to retain without payment. 4. No enforceable contract covering the matter.

**Exceptions / defenses:** As a legal remedy it gives Π no priority over Δ's other creditors and no claim to specific property; if Δ is insolvent, consider a constructive trust.

**Authority:** R2d §§ 370–371, 375–377; R3RUE § 1 [VERIFY V-350]; cross-reference R-CTR-018.

**MBE vs. CA essay:** Quasi-contract is tested on the Contracts MBE as "restitution." On the essay, it is the first legal restitutionary remedy you discuss.

**Example:** An oral contract to build a barn is unenforceable for some reason; the builder finishes half and the owner refuses to pay. The builder recovers the reasonable value of the work in quasi-contract.

> 🇨🇳 PRC bridge: functionally similar to a 不当得利 claim for money (approx.).

### R-REM-039 — Quantum meruit
**Rule (write this):** Quantum meruit ("as much as he deserved") allows a person who rendered services at the defendant's request, or with the defendant's knowledge and with an expectation of payment, to recover their reasonable value. It applies where a contract is unenforceable, where the parties never agreed on price, where the defendant's breach entitles the plaintiff to restitution instead of damages, and, subject to an offset for the defendant's damages, to a plaintiff who is itself in breach.

**Elements:** 1. Services rendered. 2. Δ requested or knowingly accepted them. 3. Both parties expected payment. 4. Reasonable value.

**Exceptions / defenses:** Courts split on whether a non-breaching plaintiff's restitution is capped at the contract price; a breaching plaintiff never recovers more than the pro rata contract price (R-CTR-109).

**Authority:** R2d §§ 371, 373, 374; cross-reference R-CTR-108, R-CTR-109.

**MBE vs. CA essay:** Contracts MBE topic. On a Contracts/Remedies essay (Jul 2014 Q1 landscaping [VERIFY V-071]), present quantum meruit as the alternative when expectation damages are low or uncertain.

**Example:** A landscaper completes 60% of a losing $30,000 job before the owner repudiates; the work's market value is $24,000. She may elect restitution in quantum meruit rather than expectation damages.

### R-REM-040 — Limits on restitution: volunteers, officious intermeddlers, emergencies
**Rule (write this):** A person who confers a benefit officiously — without request and without giving the recipient a chance to decline — is not entitled to restitution; neither is one who intended a gift. Exceptions allow recovery for emergency services by a professional to protect life or health, for performing another's duty to supply necessaries, and for benefits conferred by mistake.

**Elements:** 1. Was the benefit requested or knowingly accepted? 2. Was there an opportunity to decline? 3. Was Π acting gratuitously? 4. Does an exception apply (emergency, necessaries, mistake)?

**Exceptions / defenses:** A good-faith improver of another's land may recover in some jurisdictions (California has a statutory good-faith-improver remedy, CCP § 871.1 et seq.) [VERIFY V-368].

**Authority:** R3RUE §§ 2, 20, 22 [VERIFY V-350].

**MBE vs. CA essay:** Not on the MBE in this form. On the essay, raise this when Π "helped" Δ without being asked.

**Example:** A doctor treats an unconscious accident victim at the scene and recovers the reasonable value of the care. A neighbor who repaints Π's house while Π is on vacation, unasked, recovers nothing.

> 🇨🇳 PRC bridge: the emergency-services exception overlaps with PRC 无因管理 (negotiorum gestio) (approx.).

### R-REM-041 — Replevin (California: claim and delivery)
**Rule (write this):** Replevin is a legal action to recover possession of specific personal property wrongfully held by the defendant, plus damages for its detention. The plaintiff must show a right to immediate possession. A writ of possession may issue before judgment after notice and a hearing at which the plaintiff shows the probable validity of its claim, usually on posting a bond; the sheriff, not the court's contempt power, enforces it.

**Elements:** 1. Π's right to immediate possession of specific chattel. 2. Δ's wrongful detention. 3. Pre-judgment writ: notice + hearing + probable validity + undertaking.

**Exceptions / defenses:** Pre-judgment seizure without notice and hearing violates due process except in narrow cases (*Fuentes v. Shevin*, 407 U.S. 67 (1972)). If the chattel has been destroyed or cannot be found, replevin fails: sue for conversion damages or a constructive trust on proceeds. A buyer of goods has a UCC replevin right for identified goods it cannot cover (UCC § 2-716(3)).

**Authority:** CCP § 511.010 et seq.; § 512.010 (writ of possession) [S-475]; UCC § 2-716(3); FRCP 64.

**MBE vs. CA essay:** Not on the MBE. On the essay, replevin is the legal route to get a unique chattel back; compare it with specific performance (contract) and a constructive trust (proceeds, insolvency).

**Example:** Δ refuses to return Π's family portrait after a loan. Π files for claim and delivery and, after a hearing, obtains a writ of possession; the sheriff seizes the portrait.

> 🇨🇳 PRC bridge: comparable to a 返还原物请求权 (claim for return of the original thing) (approx.).

### R-REM-042 — Ejectment and mesne profits
**Rule (write this):** Ejectment is a legal action by one entitled to possession of real property to recover possession from a person wrongfully in possession, together with mesne profits (the fair rental value of the land during the wrongful occupation). The judgment is enforced by the sheriff.

**Elements:** 1. Π's title or right to possession. 2. Δ's wrongful possession. 3. Mesne profits for the period.

**Exceptions / defenses:** Against a holdover tenant, use the summary unlawful-detainer action (CCP § 1159 et seq.). For a structure that encroaches on Π's land, ejectment may be impractical; seek a mandatory injunction (R-REM-061).

**Authority:** Common law; Civ. Code § 3334 [VERIFY V-357]; CCP § 1159 et seq.

**MBE vs. CA essay:** Not on the MBE. On a Remedies/Real Property essay, mention ejectment as the legal route to possession of land.

**Example:** Δ moves into Π's vacant cabin and refuses to leave. Π sues in ejectment and recovers possession plus six months' fair rental value.

### R-REM-043 — Rescission and restitution (legal and equitable rescission)
**Rule (write this):** Rescission unwinds a contract that is voidable (fraud, material misrepresentation, mistake, duress, undue influence, incapacity) or materially breached, and each party restores what it received. At law, the plaintiff rescinds by giving notice and tendering back what it received, then sues for restitution; in equity, the court decrees rescission, cancels the instrument and orders restoration. California merges the two: the party rescinds by promptly giving notice and restoring or offering to restore everything of value received, then sues for relief based on rescission, which may include consequential damages.

**Elements:** 1. Ground. 2. Prompt notice after discovery. 3. Restoration or offer to restore. 4. No bar (affirmation, unreasonable delay, bona fide purchaser, unclean hands).

**Exceptions / defenses:** A court may excuse an imperfect tender where restoration is impossible and offset the value instead.

**Authority:** R2d §§ 164, 175, 376, 380–381 [VERIFY V-111]; Civ. Code §§ 1689, 1691, 1692 [S-462]; cross-reference R-CTR-105.

**MBE vs. CA essay:** The contract grounds are tested on the Contracts MBE. On a Remedies essay (Feb 2016 Q4 insurance; Feb 2014 Q6 home buyer [VERIFY V-071]), list the ground, notice, restoration and bars, and add § 1692 for California.

**Example:** Π buys a house after Δ lies about flooding. Within weeks of discovering the truth, Π notifies Δ, offers to reconvey and sues; she recovers the price plus moving costs (consequential damages under § 1692).

> 🇨🇳 PRC bridge: US rescission covers both PRC 撤销 (avoidance of a voidable contract) and 解除 (termination for breach), followed by 返还 and 赔偿 (approx.).

### R-REM-044 — Constructive trust
**Rule (write this):** A constructive trust is an equitable restitutionary remedy that compels a defendant who holds title to specific property acquired by wrongdoing or unjust enrichment (fraud, theft or conversion, breach of fiduciary duty, mistake) to convey that property, or its traceable product, to the plaintiff. Because the plaintiff takes the property itself, it captures any increase in value and takes priority over the defendant's unsecured creditors; the decree is enforced by contempt.

**Elements:** 1. Δ holds title to specific property. 2. Acquired through Δ's wrongful conduct or unjust enrichment at Π's expense. 3. The property is Π's or traceable to Π's property (R-REM-047, R-REM-048). 4. Legal remedy inadequate (unique property, Δ insolvent, or Π wants the appreciation). 5. No bona fide purchaser (R-REM-049).

**Exceptions / defenses:** No constructive trust over property that cannot be traced. Equitable defenses apply. Secured creditors with prior perfected interests keep priority.

**Authority:** Civ. Code §§ 2223, 2224 (one who wrongfully detains a thing, or gains it by fraud, accident, mistake, undue influence, violation of a trust or other wrongful act, is an involuntary trustee) [S-463]; R3RUE § 55 [VERIFY V-350].

**MBE vs. CA essay:** Not on the MBE. On a California essay (Jul 2026 Q3 four assets; Jul 2023 Q5 embezzled funds; Feb 2013 Q3 sale proceeds [VERIFY V-071]), go asset by asset: wrongful acquisition → tracing → BFP → constructive trust or lien.

**Example:** Δ embezzles $100,000 from his employer and buys stock that is now worth $180,000. The employer obtains a constructive trust over the stock and its $80,000 gain.

> 🇨🇳 PRC bridge: no direct PRC equivalent; a PRC 不当得利 claim is personal, whereas a constructive trust gives a proprietary claim to the asset and its gains (approx.).

### R-REM-045 — Equitable lien
**Rule (write this):** An equitable lien is a security interest that equity imposes on specific property of the defendant to secure the plaintiff's restitution claim, where the plaintiff's money or property was wrongfully used to acquire, improve or pay down debt on that property. The plaintiff may force a sale of the property to satisfy the claim and, if the proceeds fall short, obtain a deficiency judgment for the balance as a general creditor.

**Elements:** 1. Δ's wrongful use of Π's money or property. 2. Traceable into specific property of Δ. 3. Unjust enrichment. 4. Legal remedy inadequate (priority needed).

**Exceptions / defenses:** BFP and equitable defenses. Some courts allow an equitable lien on a homestead where fraud was used to acquire or improve it [VERIFY V-350].

**Authority:** R3RUE § 56 [VERIFY V-350]; common law.

**MBE vs. CA essay:** Not on the MBE. On the essay, discuss it immediately after the constructive trust and choose between them (R-REM-046).

**Example:** Δ uses $60,000 stolen from Π to build an addition to his own house. Π gets an equitable lien on the house for $60,000, not ownership of the house.

### R-REM-046 — Choosing between constructive trust and equitable lien
**Rule (write this):** Where the traced asset has risen in value, a constructive trust is better, because the plaintiff takes the asset and its appreciation. Where the asset has fallen in value, an equitable lien is better, because the plaintiff can sell the asset and still sue for a deficiency. Where the plaintiff's money paid for only part of an asset or improved property the defendant already owned, courts give a proportionate share or an equitable lien rather than the whole asset.

**Elements:** 1. Compare the asset's current value with the amount taken. 2. Up → constructive trust. 3. Down → equitable lien plus deficiency. 4. Mixed funds or improvements → pro rata share or lien.

**Exceptions / defenses:** An innocent donee may be limited to a lien rather than a trust where a trust would be harsh [VERIFY V-350].

**Authority:** R3RUE §§ 55, 56, 58 [VERIFY V-350].

**MBE vs. CA essay:** Not on the MBE. On the essay, this choice is where graders look for analysis; do the arithmetic for each asset.

**Example:** With $50,000 stolen from Π, Δ buys a painting now worth $30,000 and a lot now worth $90,000. Π takes a constructive trust on the lot ($90,000) and an equitable lien on the painting ($30,000 plus a $20,000 deficiency claim).

### R-REM-047 — Tracing through exchanges
**Rule (write this):** A claimant may follow its property through substitutions into whatever the wrongdoer acquired with it, and may claim the product (by constructive trust) or a lien on it. Tracing ends when the property passes to a bona fide purchaser for value or is dissipated so that no identifiable product remains.

**Elements:** 1. Identify Π's original property. 2. Follow each exchange (sale, purchase, deposit). 3. Identify the current product. 4. Check for BFP or dissipation.

**Exceptions / defenses:** If the trail goes cold (spent on a vacation, meals), Π is left with a personal money claim.

**Authority:** R3RUE § 58 [VERIFY V-350].

**MBE vs. CA essay:** Not on the MBE. On the essay, write the chain explicitly ("Π's $20,000 → Δ's bank account → the car").

**Example:** Δ steals Π's diamond ring, sells it for $15,000 and uses the $15,000 to buy a motorcycle. Π may claim the motorcycle by constructive trust.

### R-REM-048 — Tracing into commingled funds
**Rule (write this):** When a wrongdoer mixes the claimant's money with its own, the wrongdoer is presumed to withdraw its own money first, so the claimant's funds remain in the account as long as possible; but the claimant's claim against the account cannot exceed the lowest intermediate balance after the deposit, because later deposits of the wrongdoer's own money do not restore it. If the wrongdoer withdraws funds and buys an asset and then dissipates the rest, the claimant may trace into the asset.

**Elements:** 1. Commingled account. 2. Track the balance after each transaction. 3. Lowest balance after Π's funds went in = ceiling on Π's claim to the account. 4. Assets bought with withdrawals: Π may elect to trace into them when the remaining balance is insufficient.

**Exceptions / defenses:** Where the wrongdoer commingled several victims' funds, courts often distribute pro rata. Later deposits count only if the wrongdoer intended them as restitution.

**Authority:** R3RUE § 59 [S-465] [VERIFY V-350].

**MBE vs. CA essay:** Not on the MBE. On the essay (Jul 2023 Q5 asked what Acme could recover from Barbara's checking account [VERIFY V-071]), lay out the balances in a short table and apply the rule.

**Example:** Δ deposits $10,000 stolen from Π into an account holding $2,000 of his own (balance $12,000). He spends $9,000 on a cruise (balance $3,000), then deposits $5,000 of his salary (balance $8,000). Π's claim against the account is capped at $3,000, the lowest intermediate balance.

### R-REM-049 — Bona fide purchasers and change of position
**Rule (write this):** A bona fide purchaser — one who acquires legal title for value, in good faith and without notice of the claimant's rights — takes free of the claimant's equitable claims (constructive trust, equitable lien), leaving the claimant to pursue the wrongdoer or the proceeds. A donee or a purchaser with notice takes subject to the claim. An innocent recipient who, in good faith, changed its position in reliance on the transfer (for example, by spending the money) may reduce its liability by that amount.

**Elements:** 1. Value paid. 2. Good faith. 3. No actual, constructive or inquiry notice. 4. For goods: did the wrongdoer have voidable title (fraud → can pass good title to a good-faith purchaser) or void title (theft → cannot)?

**Exceptions / defenses:** A thief cannot pass title, so the owner may replevy stolen goods even from a good-faith buyer; a person who obtained goods by fraud has voidable title and can pass good title to a good-faith purchaser for value (UCC § 2-403(1)). Change of position is not available to a conscious wrongdoer.

**Authority:** UCC § 2-403(1); R3RUE §§ 65, 66 [VERIFY V-350].

**MBE vs. CA essay:** Voidable title under § 2-403 is a Contracts MBE point. On a Remedies essay with several assets (Jul 2026 Q3 [VERIFY V-071]), test each transferee: purchaser for value without notice, or donee?

**Example:** Δ defrauds Π into transferring a condo, then gives it to his sister, who knows nothing. Because she paid nothing, Π can impose a constructive trust on the condo in her hands. Had she paid market value in good faith, Π could reach only the sale proceeds in Δ's hands.

### R-REM-050 — Resulting trust
**Rule (write this):** A resulting trust arises by operation of law when the circumstances show that the holder of legal title was not meant to have the beneficial interest: chiefly when one person pays the purchase price and title is taken in another's name (a purchase-money resulting trust), and when an express trust fails or does not exhaust the trust property. The title holder must convey to the person who paid or to the settlor's estate.

**Elements:** 1. Purchase-money: A pays, title to B, no intent to give. 2. Failed or surplus express trust.

**Exceptions / defenses:** When the payor and title holder are close family (spouse, child), a gift is presumed instead, rebuttable by evidence.

**Authority:** Common law; Restatement (Third) of Trusts [VERIFY V-350].

**MBE vs. CA essay:** Not on the MBE. On a Trusts/Remedies essay, distinguish it from a constructive trust: a resulting trust rests on presumed intent, a constructive trust on wrongdoing.

**Example:** Aunt pays $300,000 for a condo and has title put in her business partner's name for convenience. The partner holds the condo on a resulting trust for Aunt.

### R-REM-051 — Subrogation
**Rule (write this):** Subrogation allows a person who has paid a debt for which another was primarily liable — under compulsion, to protect its own interest, or because its money was wrongfully used to pay the debt — to step into the creditor's shoes and enforce the creditor's rights, including any security, against the person who was primarily liable. It prevents the debtor's unjust enrichment from having its debt discharged with someone else's money.

**Elements:** 1. Π's money paid Δ's (or a third party's) obligation. 2. Π was not a mere volunteer, or its money was taken wrongfully. 3. Π takes over the creditor's rights and priority.

**Exceptions / defenses:** A volunteer who pays another's debt without compulsion or interest generally has no subrogation.

**Authority:** R3RUE § 57 [VERIFY V-350]; common law (insurer and surety subrogation).

**MBE vs. CA essay:** Not on the MBE. On the essay, use it when stolen money paid off Δ's mortgage: Π is subrogated to the bank's first-priority mortgage lien.

**Example:** Δ uses $80,000 embezzled from Π to pay off the mortgage on his home. Π is subrogated to the bank's mortgage, with the bank's priority over Δ's later creditors.

### R-REM-052 — Indemnity
**Rule (write this):** Indemnity shifts the entire loss from a party who has paid a liability to the party who should bear it, either because a contract so provides (express indemnity) or because the payor was only secondarily or vicariously liable while the other was primarily at fault (implied or equitable indemnity).

**Elements:** 1. Π paid a liability. 2. Δ is primarily responsible (by contract or by fault). 3. Recovery of the amount paid.

**Exceptions / defenses:** In California, equitable indemnity among joint tortfeasors is apportioned by comparative fault (*American Motorcycle Assn. v. Superior Court* (1978) 20 Cal.3d 578) [VERIFY V-367].

**Authority:** Common law; *American Motorcycle* [VERIFY V-367].

**MBE vs. CA essay:** Not on the MBE in this form (Torts touches it). One paragraph on a Torts/BA/Remedies essay with an employer paying for an employee's tort.

**Example:** An employer pays a $200,000 judgment for its driver's negligence under respondeat superior. It may seek indemnity from the driver, who was primarily at fault.

### R-REM-053 — Contribution
**Rule (write this):** Contribution lets a joint tortfeasor who has paid more than its fair share of a common liability recover the excess from the other tortfeasors, traditionally in equal (pro rata) shares and in comparative-fault jurisdictions in proportion to fault.

**Elements:** 1. Common liability to Π. 2. Payor paid more than its share. 3. Recover the excess.

**Exceptions / defenses:** In California, a good-faith settlement with Π bars other joint tortfeasors' claims for contribution or comparative indemnity against the settling tortfeasor (CCP § 877.6) [VERIFY V-367].

**Authority:** CCP § 875 et seq. [VERIFY V-367]; common law.

**MBE vs. CA essay:** Joint-tortfeasor contribution is a Torts MBE point. Rarely more than a line on a Remedies essay.

**Example:** Two drivers jointly injure Π; one pays the whole $100,000 judgment. With fault split 70/30, she recovers $30,000 from the other driver.

### R-REM-054 — Equitable accounting
**Rule (write this):** An accounting is an equitable remedy that requires a defendant who holds money or profits that belong in conscience to the plaintiff — typically a fiduciary such as a trustee, partner or agent, or a defendant whose dealings are too complex for a jury to unravel — to account for all receipts and disburse the amount found due, including profits made from the plaintiff's property.

**Elements:** 1. Fiduciary or confidential relationship, or complex accounts. 2. Δ received money or profits for which it must account. 3. Inadequate legal remedy.

**Exceptions / defenses:** Equitable defenses; Δ may prove legitimate deductions (expenses) from gross receipts.

**Authority:** Common law; R3RUE § 51 [VERIFY V-350].

**MBE vs. CA essay:** Not on the MBE. On a BA/Trusts/Remedies crossover, pair it with a constructive trust over the profits.

**Example:** A partner diverts partnership customers to his own side business. The other partners obtain an accounting of the side business's profits.

---

## IV. Equitable remedies

### R-REM-055 — Permanent injunction: the essay elements
**Rule (write this):** A permanent injunction is a final court order, after a trial on the merits, commanding the defendant to do (mandatory) or refrain from doing (prohibitory) an act. The plaintiff must show (1) an inadequate legal remedy (irreparable harm), (2) a property right or other protectable interest, (3) that enforcement is feasible, (4) that the balance of hardships, including the public interest, favors relief, and (5) that no equitable defense bars relief.

**Elements:** Mnemonic **I-P-F-B-D** ("I Prefer Fair, Balanced Decrees"): Inadequate legal remedy; Protectable interest; Feasibility; Balancing of hardships; no Defenses. A valid underlying claim is assumed (Π must win on the merits).

**Exceptions / defenses:** Laches, unclean hands, estoppel, unconscionability, undue hardship (R-REM-081 to R-REM-090).

**Authority:** Civ. Code § 3422 [S-458]; CCP § 526; *eBay Inc. v. MercExchange, L.L.C.*, 547 U.S. 388 (2006); *Weinberger v. Romero-Barcelo*, 456 U.S. 305 (1982).

**MBE vs. CA essay:** Not on the MBE. This is the most-tested Remedies rule on California essays (equitable remedies appear in about half of the Remedies essays indexed [VERIFY V-071]); use a sub-heading for each element.

**Example:** Δ's new shed blocks Π's recorded easement to the beach. Damages cannot restore access, Π has a property right, ordering removal of a shed is easy to enforce, the shed costs little to move, and Δ has no defense. A permanent mandatory injunction issues.

> 🇨🇳 PRC bridge: functionally like a judgment ordering 停止侵害/排除妨碍/恢复原状, but issued only after the "inadequate damages" and balancing tests and enforced by contempt (approx.).

### R-REM-056 — Permanent injunction in federal court: the eBay four-factor test
**Rule (write this):** In federal court a plaintiff seeking a permanent injunction must demonstrate (1) that it has suffered an irreparable injury; (2) that remedies available at law, such as monetary damages, are inadequate to compensate for that injury; (3) that, considering the balance of hardships between the plaintiff and defendant, a remedy in equity is warranted; and (4) that the public interest would not be disserved by a permanent injunction. No category of case (even patent infringement) gets an automatic injunction.

**Elements:** Irreparable injury; inadequate legal remedy; balance of hardships; public interest.

**Exceptions / defenses:** A statute may displace traditional equitable discretion only by clear command (*Weinberger*).

**Authority:** *eBay Inc. v. MercExchange, L.L.C.*, 547 U.S. 388 (2006).

**MBE vs. CA essay:** Not on the MBE. On a California essay, the I-P-F-B-D elements (R-REM-055) are the standard; add one sentence that federal courts apply the *eBay* factors when the case is in federal court or arises under federal law.

**Example:** A patent holder that licenses but does not make the product proves infringement. The court weighs the four factors and may award a reasonable royalty instead of an injunction.

### R-REM-057 — Inadequate legal remedy / irreparable harm
**Rule (write this):** The legal remedy is inadequate, and the harm irreparable, when money cannot make the plaintiff whole: the subject matter is unique (land, heirlooms, works of art, rare chattels); damages are too speculative or difficult to measure (lost goodwill, environmental or aesthetic harm, loss of constitutional rights); the harm is continuing, so damages would require a multiplicity of suits; or the defendant is insolvent and could not pay a judgment.

**Elements:** Uniqueness; speculative damages; multiplicity of suits; insolvency; irreversible harm (demolition, felling a tree).

**Exceptions / defenses:** Courts are divided on whether Δ's insolvency alone makes damages inadequate. Purely economic harm that is calculable is not irreparable.

**Authority:** Civ. Code § 3422 [S-458]; R2d §§ 359, 360; *Winter v. Natural Resources Defense Council, Inc.*, 555 U.S. 7 (2008).

**MBE vs. CA essay:** Not on the MBE. On the essay, name the specific reason damages fail; "money is not enough" earns little.

**Example:** Δ threatens to demolish a historic building Π contracted to buy. Once demolished it cannot be replaced, so the harm is irreparable.

### R-REM-058 — Property right or protectable interest
**Rule (write this):** Historically equity protected only property rights; modern courts grant injunctions to protect any legally protectable interest, including personal and constitutional rights, privacy and contract rights. On an essay, state the traditional requirement and conclude that the plaintiff's interest qualifies.

**Elements:** 1. Identify Π's interest (land ownership, easement, chattel, contract right, civil right). 2. Note the modern view.

**Exceptions / defenses:** —

**Authority:** Common law; Civ. Code § 3422 [S-458] (obligation "existing in favor of the applicant").

**MBE vs. CA essay:** Not on the MBE. A one- or two-sentence element on the essay.

**Example:** A church seeking to enjoin an ordinance that bars candle burning in worship asserts a First Amendment right, a protectable interest under the modern view (Jul 2019 Q2 pattern [VERIFY V-071]).

### R-REM-059 — Feasibility of enforcement
**Rule (write this):** Courts consider whether an injunction can be enforced practically. Prohibitory (negative) injunctions are easy to enforce because the court need only punish a violation. Mandatory injunctions that require ongoing supervision, cooperation between hostile parties, skill or judgment, or performance outside the court's territory, are disfavored, and personal-service contracts are not specifically enforced.

**Elements:** 1. Negative or mandatory? 2. One-time act or continuing supervision? 3. Requires personal services, skill or taste? 4. Acts outside the jurisdiction (court can still order Δ personally)?

**Exceptions / defenses:** Courts do order one-time affirmative acts (remove an encroachment, convey land) without difficulty.

**Authority:** R2d §§ 366, 367; Civ. Code § 3390 [VERIFY V-108].

**MBE vs. CA essay:** Not on the MBE. On the essay, say whether the order is negative or mandatory and how much supervision it needs.

**Example:** An order that a builder "complete the house to the owner's satisfaction" over 18 months is hard to supervise; an order that a neighbor "remove the fence by June 1" is easy.

### R-REM-060 — Balancing of hardships and the public interest
**Rule (write this):** The court weighs the hardship to the plaintiff if the injunction is denied against the hardship to the defendant (and to third parties and the public) if it is granted, and may deny relief, or award damages instead, where the defendant's hardship is greatly disproportionate to the plaintiff's benefit. A defendant who acted willfully or in bad faith gets no balancing: the injunction issues even at great cost to it.

**Elements:** 1. Π's hardship if denied. 2. Δ's hardship if granted. 3. Public interest (jobs, health, free speech). 4. Δ's good faith or willfulness.

**Exceptions / defenses:** Courts may tailor relief (delay, conditions, a compensated injunction) rather than deny it.

**Authority:** R2d § 364; *eBay*, 547 U.S. 388 (2006); *Boomer v. Atlantic Cement Co.*, 26 N.Y.2d 219 (1970); *Hirshfield v. Schwartz* (2001) 91 Cal.App.4th 749 [S-466].

**MBE vs. CA essay:** Not on the MBE. On the essay, argue both sides with the dollar figures in the facts, and state whether Δ acted willfully.

**Example:** A factory employing 300 people emits noise that annoys five neighbors. The hardship of closure is greatly disproportionate; the court may award permanent damages or order noise limits instead of closure.

### R-REM-061 — Encroachments: relative hardship and equitable easements
**Rule (write this):** A landowner is ordinarily entitled to a mandatory injunction requiring removal of an encroaching structure. But where the encroacher acted innocently (not willfully or negligently), the owner will not suffer irreparable injury from the encroachment, and the hardship of removal would be greatly disproportionate to the hardship of leaving it, a court may refuse the injunction and instead award damages; California courts in that situation may create an equitable easement in favor of the encroacher, on payment of compensation to the owner.

**Elements:** 1. Encroacher innocent (the "paramount" factor). 2. No irreparable injury to Π (unless the public interest is affected). 3. Δ's hardship from removal greatly disproportionate. 4. Compensation to Π.

**Exceptions / defenses:** A willful or negligent encroacher (built after notice or without a survey) gets no balancing; removal is ordered.

**Authority:** *Christensen v. Tucker* (1952) 114 Cal.App.2d 554 and *Hirshfield v. Schwartz* (2001) 91 Cal.App.4th 749 [S-466].

**MBE vs. CA essay:** Not on the MBE. On a California essay (Feb 2025 retest Q5 fence [VERIFY V-071]), apply all three factors and discuss the equitable easement as the alternative outcome.

**Example:** Relying on an old survey, Δ builds a garage that extends two feet onto Π's vacant side lot. Removal would cost $90,000; the strip is worth $3,000 to Π. A court may deny removal and grant Δ an equitable easement on paying Π the strip's value.

### R-REM-062 — Nuisance injunctions and their alternatives
**Rule (write this):** Once a nuisance is established, the court decides whether to enjoin it by weighing the hardships and the public interest. It may enjoin the activity outright, enjoin it on conditions (hours, filters), award permanent damages in lieu of an injunction, or, where the plaintiff came to the nuisance, grant an injunction conditioned on the plaintiff paying the defendant's cost of relocating.

**Elements:** 1. Nuisance (Torts). 2. Balancing. 3. Choose: full injunction, partial or conditional injunction, permanent damages, compensated injunction.

**Exceptions / defenses:** Coming to the nuisance is a factor, not an absolute defense.

**Authority:** *Boomer v. Atlantic Cement Co.*, 26 N.Y.2d 219 (1970) (permanent damages instead of injunction); *Spur Industries, Inc. v. Del E. Webb Development Co.*, 108 Ariz. 178, 494 P.2d 700 (1972) (compensated injunction); R2d Torts § 840D [VERIFY V-363].

**MBE vs. CA essay:** Not on the MBE. On a Torts/Remedies essay (Feb 2022 Q3 theater noise [VERIFY V-071]), discuss partial injunctions (hours, volume) as the practical middle ground.

**Example:** Π buys a house next to a long-established outdoor theater and sues over concert noise. A court may limit performances to 10 p.m. rather than close the theater, given that Π came to the nuisance.

### R-REM-063 — Injunctions affecting speech
**Rule (write this):** A court order forbidding speech before a final determination that the speech is unprotected is a prior restraint and is presumptively unconstitutional, so equity traditionally will not enjoin defamation. In California, after a trial determines that specific statements are defamatory, the court may permanently enjoin the defendant from repeating those statements if the injunction is narrowly tailored to them.

**Elements:** 1. Speech at issue? 2. Pre-trial (prior restraint, almost never) or post-adjudication (narrow injunction possible)? 3. Narrow tailoring.

**Exceptions / defenses:** Trade secrets, IP and true threats may be enjoined; conduct (trespass, harassment) may be enjoined even if expressive.

**Authority:** U.S. Const. amend. I; *Balboa Island Village Inn, Inc. v. Lemen* (2007) 40 Cal.4th 1141 [S-476].

**MBE vs. CA essay:** Prior restraint is a Con Law MBE topic. On a Remedies essay with defamation or protest facts, raise it under feasibility or the public interest.

**Example:** After a trial finds that Δ falsely told customers that Π's restaurant served dog meat, the court may enjoin Δ from repeating those specific statements, but not from criticizing the restaurant generally.

### R-REM-064 — Personal-service contracts: no specific performance; negative injunctions
**Rule (write this):** Courts will not order specific performance of a contract for personal services, because forced labor raises Thirteenth Amendment concerns, supervision is impractical, and the quality of compelled service cannot be assured. But a court may issue a negative injunction barring an employee whose services are unique from working for a competitor during the contract term, if doing so is reasonable and does not leave the employee without a way to earn a living.

**Elements:** 1. Personal-service contract → no SP. 2. Negative injunction: unique services; during the contract term; reasonable scope; not depriving the employee of a livelihood.

**Exceptions / defenses:** In California, an injunction to prevent breach of a personal-service contract is available only for a written contract for services of a special, unique or extraordinary character that meets statutory minimum-compensation conditions (Civ. Code § 3423(e)) [S-459] [VERIFY V-352]; post-employment non-compete covenants are void (Bus. & Prof. Code § 16600; R-CTR-041).

**Authority:** U.S. Const. amend. XIII; R2d § 367; *Lumley v. Wagner* (1852) 1 De G.M. & G. 604; Civ. Code §§ 3390, 3423(e) [S-459] [VERIFY V-108] [VERIFY V-352].

**MBE vs. CA essay:** The general rule is a Contracts MBE point. On a California essay (Feb 2020 Q3 artist painting borders [VERIFY V-071]), deny SP of the artist's services and consider damages or a negative injunction.

**Example:** A famous chef under a three-year written contract quits to cook for a rival across the street. The court will not order her to cook, but may bar her from cooking for the rival during the term if the contract meets the California conditions.

### R-REM-065 — Temporary restraining order (federal)
**Rule (write this):** A temporary restraining order preserves the status quo for the short time until a preliminary-injunction hearing can be held. It may issue without notice to the adverse party only if specific facts in an affidavit or verified complaint clearly show that immediate and irreparable injury will result before the adverse party can be heard, and the movant's attorney certifies in writing the efforts made to give notice and why notice should not be required. An ex parte TRO expires at the time set by the court, not more than 14 days, unless extended for good cause for a like period or by consent.

**Elements:** 1. Immediate irreparable harm before a hearing can be held. 2. Likelihood of success and the other *Winter* factors. 3. Notice, or a certified reason for no notice. 4. Security (FRCP 65(c)). 5. Duration ≤ 14 days (+ one extension).

**Exceptions / defenses:** The adverse party may move to dissolve or modify on 2 days' notice (FRCP 65(b)(4)). A TRO extended beyond the rule's limit is treated as an appealable preliminary injunction (*Granny Goose Foods, Inc. v. Teamsters*, 415 U.S. 423 (1974)).

**Authority:** FRCP 65(b), (c); *Granny Goose Foods*, 415 U.S. 423 (1974).

**MBE vs. CA essay:** TRO procedure is a Civil Procedure MBE point. On a Remedies essay, analyze the TRO first (call order), stressing urgency and notice.

**Example:** A seller announces an auction tomorrow of a painting the buyer claims under contract. The buyer's lawyer calls the seller's lawyer, gets no answer, and certifies that; the court issues a TRO barring the sale until a hearing.

> 🇨🇳 PRC bridge: comparable to 诉前行为保全 (pre-suit conduct preservation), which also requires urgency and usually security (approx.).

### R-REM-066 — Preliminary injunction (federal): Winter
**Rule (write this):** A preliminary injunction preserves the status quo pending a trial on the merits and issues only after notice to the adverse party. The plaintiff must establish (1) that it is likely to succeed on the merits, (2) that it is likely to suffer irreparable harm in the absence of preliminary relief, (3) that the balance of equities tips in its favor, and (4) that an injunction is in the public interest. A mere possibility of irreparable harm is not enough; a preliminary injunction is an extraordinary remedy never awarded as of right.

**Elements:** Likelihood of success; likely irreparable harm; balance of equities; public interest; notice (FRCP 65(a)(1)); security (FRCP 65(c)).

**Exceptions / defenses:** Some circuits still weigh the factors on a sliding scale ("serious questions" on the merits plus a balance of hardships tipping sharply toward Π). The court may consolidate the hearing with trial (FRCP 65(a)(2)).

**Authority:** *Winter v. Natural Resources Defense Council, Inc.*, 555 U.S. 7 (2008); FRCP 65(a), (c).

**MBE vs. CA essay:** Civil Procedure MBE point. On a Remedies essay, use the *Winter* factors when the case is in federal court (constitutional challenges, Jul 2019 Q2 [VERIFY V-071]); otherwise use the California test (R-REM-067).

**Example:** A church challenging a city's candle ban shows a strong free-exercise claim, ongoing loss of worship practice, little harm to the city from a short delay and a public interest in protecting constitutional rights. A preliminary injunction is likely.

### R-REM-067 — Preliminary injunction and TRO in California courts
**Rule (write this):** A California trial court deciding whether to grant a preliminary injunction weighs two interrelated factors: (1) the likelihood that the plaintiff will prevail on the merits at trial, and (2) the relative interim harm to the parties from issuing or withholding the injunction. The greater the plaintiff's showing on one factor, the less it must show on the other, but no injunction may issue unless there is some possibility the plaintiff will ultimately prevail. A TRO may issue without notice on a verified complaint or affidavit showing that great or irreparable injury will result before the matter can be heard on notice; the order to show cause must then be heard within 15 days (22 for good cause), and the applicant must post an undertaking.

**Elements:** 1. Likelihood of prevailing. 2. Relative interim harm (sliding scale). 3. Grounds in CCP § 526. 4. Undertaking (CCP § 529). 5. TRO: irreparable injury before a noticed hearing; prompt OSC hearing.

**Exceptions / defenses:** Notice rules for ex parte applications are in the California Rules of Court [VERIFY V-353].

**Authority:** *IT Corp. v. County of Imperial* (1983) 35 Cal.3d 63 [S-455]; *Butt v. State of California* (1992) 4 Cal.4th 668 [S-456]; CCP §§ 526, 527 [S-457] [VERIFY V-353], 529 [S-478].

**MBE vs. CA essay:** Not on the MBE. On a California essay, give the general (*Winter*-style) factors and add one sentence that California courts use the *IT Corp.* two-factor sliding scale.

**Example:** A buyer of a unique chess piece shows a strong contract claim and that the seller is about to sell it abroad; the seller would suffer only delay. A California court is likely to grant a preliminary injunction against the sale.

### R-REM-068 — Security (bond) and damages for a wrongful injunction
**Rule (write this):** A court may grant a TRO or preliminary injunction only if the movant gives security in an amount the court considers proper to pay the costs and damages sustained by a party found to have been wrongfully enjoined. A wrongfully enjoined defendant's recovery is generally limited to the amount of the bond.

**Elements:** 1. Bond set by the court. 2. Later finding that Δ was wrongfully enjoined. 3. Recovery up to the bond.

**Exceptions / defenses:** The United States and some public entities are exempt; in California, the undertaking is mandatory except as listed in the statute (CCP § 529(b)) [S-478].

**Authority:** FRCP 65(c); CCP § 529 [S-478].

**MBE vs. CA essay:** Civil Procedure MBE point. On the essay, end the TRO/PI analysis with "Π must post a bond."

**Example:** A court enjoins a shipment pending trial and sets a $50,000 bond. If the plaintiff loses, the defendant recovers its proven losses from the delay up to $50,000.

### R-REM-069 — Status quo; mandatory preliminary injunctions
**Rule (write this):** A preliminary injunction usually preserves the status quo ante litem — the last actual, peaceable, uncontested state of affairs before the dispute. A mandatory preliminary injunction, which requires the defendant to take affirmative action before trial, is disfavored; many courts issue it only on a clear showing that the law and facts strongly favor the plaintiff.

**Elements:** 1. Identify the last peaceable status. 2. Prohibitory (preserves it) or mandatory (changes it)? 3. Mandatory → heightened showing.

**Exceptions / defenses:** An order restoring the last peaceable status (e.g., "reopen the gate you just locked") can be mandatory in form but preserves the status quo.

**Authority:** Common law; FRCP 65.

**MBE vs. CA essay:** Not on the MBE. On the essay, note whether the requested interim order is prohibitory or mandatory.

**Example:** Π asks the court, before trial, to order Δ to tear down a half-built wall on the disputed strip. Removal is mandatory and drastic; the court is more likely to enjoin further construction pending trial.

### R-REM-070 — Specific performance: the elements
**Rule (write this):** Specific performance is an order compelling a party to perform its contract. The plaintiff must show (1) a valid contract with definite and certain terms; (2) that its own conditions have been performed or it is ready, willing and able to perform; (3) that the legal remedy is inadequate; (4) that enforcement is feasible; and (5) that no equitable defense applies. Mutuality of remedy is no longer required if the plaintiff's own performance is assured.

**Elements:** Mnemonic **CCIFD** (as in Contracts): Contract with certain terms; Conditions satisfied; Inadequate legal remedy; Feasibility; no Defenses.

**Exceptions / defenses:** Laches, unclean hands, unconscionability or inadequate consideration (R-REM-087), mistake, misrepresentation, statute of frauds, sale to a BFP (R-REM-089).

**Authority:** R2d §§ 357, 359, 360, 362, 363, 364, 366, 367; UCC § 2-716; Civ. Code §§ 3384, 3386, 3390, 3391 [S-474] [VERIFY V-108]; cross-reference R-CTR-104.

**MBE vs. CA essay:** Contracts MBE topic (R-CTR-104). On a Remedies essay, give each element its own sentence and use the facts on price, uniqueness and Π's readiness to pay.

**Example:** B contracts to buy S's lakefront cabin for $400,000, has loan approval and tenders the price; S refuses to close. All five elements are met and B gets specific performance.

### R-REM-071 — Specific performance of contracts to convey land
**Rule (write this):** Every parcel of land is treated as unique, so damages are presumed inadequate for a seller's breach of a contract to convey, and the buyer may obtain specific performance. Most courts also allow the seller to compel the buyer to pay the price. In California, it is presumed that the breach of an agreement to transfer real property cannot be adequately relieved by money; the presumption is conclusive for a single-family dwelling that the party seeking performance intends to occupy, and otherwise affects the burden of proof.

**Elements:** 1. CCIFD (R-REM-070). 2. Land → inadequacy presumed. 3. California § 3387: conclusive for a single-family home the buyer will occupy; rebuttable otherwise.

**Exceptions / defenses:** Specific performance against a buyer is less readily granted in California, where the seller's damages are usually adequate [VERIFY V-355]. A BFP who bought without notice defeats the buyer's claim (R-REM-074).

**Authority:** Civ. Code § 3387 [S-450]; R2d § 360; cross-reference R-CTR-104.

**MBE vs. CA essay:** Real Property/Contracts MBE point (land is unique). On a California essay, cite § 3387 and say whether the property is a single-family home the buyer will live in.

**Example:** B contracts to buy a house she plans to live in; the seller gets a higher offer and refuses to close. Under § 3387 damages are conclusively inadequate, so B gets specific performance.

### R-REM-072 — Specific performance of contracts for unique goods
**Rule (write this):** Specific performance of a contract for the sale of goods may be decreed where the goods are unique or in other proper circumstances, such as when the buyer cannot obtain substitute goods (cover). Goods are unique when one-of-a-kind or irreplaceable — works of art, heirlooms, antiques, rare collectibles, custom items without a market substitute. A buyer also has a right to replevy goods identified to the contract if after reasonable effort it cannot cover.

**Elements:** 1. Contract for goods. 2. Unique, or other proper circumstances (inability to cover, output/requirements contract with no alternative source). 3. CCIFD.

**Exceptions / defenses:** Mass-produced goods available on the market are not unique; the buyer covers and recovers damages (UCC § 2-712). A buyer who has paid may also recover goods on the seller's insolvency (UCC § 2-502).

**Authority:** UCC §§ 2-502, 2-711(2), 2-716; cross-reference R-CTR-102, R-CTR-104.

**MBE vs. CA essay:** Contracts MBE point. On a California essay (Jul 2017 Q3 chess queen; Oct 2020 Q5 painting [VERIFY V-071]), argue uniqueness from the facts (age, provenance, sentimental tie, no comparable sales).

**Example:** A collector contracts to buy the only surviving queen from a famous 18th-century chess set. No substitute exists, so specific performance is available under § 2-716.

### R-REM-073 — Specific performance with abatement
**Rule (write this):** When the seller cannot convey exactly what it promised (less acreage, a minor title defect or encumbrance), the buyer may elect to take what the seller can convey with a reduction (abatement) in the price that reflects the deficiency. A seller whose defect is minor and compensable may obtain specific performance with an abatement, but cannot force a buyer to accept a materially different property.

**Elements:** 1. Deficiency in quantity, quality or title. 2. Buyer's election. 3. Price reduced by the value of the shortfall.

**Exceptions / defenses:** If the deficiency is material, the buyer may refuse and sue for damages or restitution.

**Authority:** Common law; R2d § 358 [VERIFY V-371].

**MBE vs. CA essay:** Not on the MBE in this form. On the essay, add it when the land turns out smaller or encumbered.

**Example:** S contracts to sell 100 acres for $1 million but owns only 95. B may compel conveyance of the 95 acres for $950,000.

### R-REM-074 — Protecting a specific-performance claim pending suit (lis pendens; bona fide purchasers)
**Rule (write this):** A buyer's right to specific performance is lost if the seller conveys to a bona fide purchaser for value without notice. A plaintiff suing over title to or possession of land protects its claim by recording a notice of pendency of action (lis pendens), which gives constructive notice to later purchasers and encumbrancers; for goods, the plaintiff seeks a TRO or preliminary injunction against sale.

**Elements:** 1. Risk of transfer to a BFP. 2. Land: record lis pendens. 3. Chattels: TRO/PI against transfer.

**Exceptions / defenses:** A later purchaser with actual or constructive notice takes subject to the buyer's equitable rights.

**Authority:** CCP § 405.20 et seq. [VERIFY V-360]; FRCP 65.

**MBE vs. CA essay:** Recording-act notice is a Real Property MBE topic. On the essay, mention lis pendens (land) or the TRO against sale (chattels) as the practical first step.

**Example:** B sues S for specific performance of a ranch contract and records a lis pendens the same day. A buyer who later purchases from S takes subject to B's claim.

### R-REM-075 — Reformation
**Rule (write this):** Reformation rewrites a written instrument so that it expresses the agreement the parties actually made, where the writing departs from that agreement because of a mutual mistake in expression, or because of one party's fraud or a unilateral mistake the other party knew of. The party seeking reformation must prove the prior agreement, usually by clear and convincing evidence; the parol evidence rule, the statute of frauds and the claimant's negligence in failing to read do not bar it.

**Elements:** 1. A prior agreement (meeting of the minds). 2. A writing that departs from it. 3. Mutual mistake in expression, or fraud / known unilateral mistake. 4. Clear and convincing proof. 5. No bar (BFP who relied on the writing; laches).

**Exceptions / defenses:** Reformation is not available to make a new bargain the parties never reached; that is a mistake in formation (rescission).

**Authority:** R2d §§ 155, 157, 166; Civ. Code § 3399; cross-reference R-CTR-106.

**MBE vs. CA essay:** Contracts MBE point. On a California essay (Oct 2020 Q5 omitted painting; Jul 2023 Q5 omitted mineral rights; Feb 2016 Q4 insurance coverage; Feb 2015 Q4 road description [VERIFY V-071]), it is often the first equitable remedy: reform the writing, then enforce it as reformed.

**Example:** Buyer and seller agree the sale of a house includes two paintings, but the typed contract lists only one. The buyer may reform the contract to include the second painting, then seek specific performance or replevin of it.

### R-REM-076 — Rescission of insurance policies (California)
**Rule (write this):** Under the California Insurance Code, an insurer may rescind a policy for the applicant's concealment of a fact it was bound to disclose, whether intentional or unintentional, or for a representation that is false in a material point. Materiality is judged by the probable effect the true facts would have had on the insurer in deciding whether to issue the policy or at what premium. Rescission voids the policy from the start, and the insurer must return the premiums.

**Elements:** 1. Concealment or misrepresentation in the application. 2. Materiality to the insurer's decision. 3. Prompt notice and return of premiums. 4. No waiver or estoppel (e.g., insurer accepted premiums with knowledge).

**Exceptions / defenses:** Waiver, estoppel, laches. The insured may cross-claim for reformation if the policy misstates the agreed coverage.

**Authority:** Ins. Code §§ 331, 359 [S-471] [VERIFY V-364]; Civ. Code §§ 1689, 1691 [S-462].

**MBE vs. CA essay:** Not on the MBE. On a California essay (Feb 2016 Q4 [VERIFY V-071]), analyze the insurer's rescission, then the insured's defenses and reformation counterclaim.

**Example:** An applicant states that her two shops are in one town when one is in a flood zone elsewhere. If the insurer would have charged more or refused, the misstatement is material and the insurer may rescind and refund the premiums.

### R-REM-077 — Cancellation of instruments
**Rule (write this):** Equity may order a void or voidable written instrument (a deed, note or contract) delivered up and cancelled where leaving it outstanding is reasonably likely to cause the plaintiff serious injury, for example by clouding title.

**Elements:** 1. Instrument void or voidable as to Π. 2. Reasonable apprehension of serious injury if left outstanding. 3. Adjudication and cancellation.

**Exceptions / defenses:** BFP who relied on the instrument; equitable defenses.

**Authority:** Civ. Code § 3412 [VERIFY V-368].

**MBE vs. CA essay:** Not on the MBE. On the essay, pair it with rescission of a fraudulently obtained deed.

**Example:** Δ induces elderly Π by undue influence to sign a deed to her house. Π obtains cancellation of the recorded deed and a decree quieting title.

### R-REM-078 — Contempt: civil and criminal
**Rule (write this):** Disobedience of an equitable decree is punishable by contempt. Civil contempt is remedial: coercive sanctions (daily fines or jail until the contemnor complies — the contemnor "holds the keys") or compensatory fines paid to the injured party. Criminal contempt punishes completed disobedience with a fixed fine or jail term to vindicate the court's authority and requires criminal procedural protections, including proof beyond a reasonable doubt and, for serious penalties, a jury. Contempt requires a valid, clear order, the contemnor's knowledge of it, ability to comply, and willful disobedience.

**Elements:** 1. Valid order. 2. Knowledge. 3. Ability to comply. 4. Willful violation. 5. Classify the sanction: coercive, compensatory, or punitive.

**Exceptions / defenses:** Inability to comply is a defense to coercive sanctions. In California, punishment for contempt is limited by statute (generally a fine up to $1,000 and up to five days in jail per act) (CCP § 1218) [S-473]; imprisonment to coerce an act within the person's power continues until it is performed (CCP § 1219) [VERIFY V-358].

**Authority:** *Int'l Union, United Mine Workers v. Bagwell*, 512 U.S. 821 (1994); CCP §§ 1209, 1218 [S-473], 1219 [VERIFY V-358].

**MBE vs. CA essay:** Not on the MBE. On a Remedies essay, mention contempt as the enforcement mechanism and as an advantage of equitable relief.

**Example:** Δ ignores an order to remove an encroaching fence. The court fines him $200 a day until he removes it (civil coercive) and, after a separate proceeding, may impose a fixed fine for the past defiance (criminal).

> 🇨🇳 PRC bridge: comparable to the coercive measures for obstructing civil proceedings and the offense of refusing to execute a judgment (拒不执行判决、裁定罪) (approx.).

### R-REM-079 — Collateral bar rule
**Rule (write this):** In federal courts, a party who violates an injunction issued by a court with jurisdiction may not defend against contempt by arguing that the injunction was erroneous or even unconstitutional; it must obey and challenge the order through appeal or a motion to modify. The rule does not apply to an order that is transparently invalid or issued without jurisdiction, or where no timely avenue for review existed.

**Elements:** 1. Court had jurisdiction. 2. Order not transparently invalid. 3. Adequate opportunity to seek review → defense barred.

**Exceptions / defenses:** California does not follow the collateral bar rule for orders that are void, including unconstitutional orders: the contemnor may challenge validity in the contempt proceeding (*In re Berry* (1968) 68 Cal.2d 137) [VERIFY V-358].

**Authority:** *Walker v. City of Birmingham*, 388 U.S. 307 (1967).

**MBE vs. CA essay:** Not on the MBE. On an essay where a protester or party defies an order, state the federal rule and the California difference.

**Example:** Marchers defy a state-court injunction against parading without a permit, believing it unconstitutional. Under *Walker* they cannot raise its invalidity as a defense to federal-style contempt; in California, they could challenge a void order [VERIFY V-358].

### R-REM-080 — Who is bound; form and scope of injunctions
**Rule (write this):** An injunction binds only the parties; their officers, agents, servants, employees and attorneys; and other persons in active concert or participation with them, and only if they receive actual notice of the order. Every injunction must state the reasons it issued, state its terms specifically, and describe in reasonable detail, without referring to other documents, the acts restrained or required. Relief should be no broader than necessary to give the plaintiff complete relief.

**Elements:** 1. Person within Rule 65(d)(2). 2. Actual notice. 3. Specific terms.

**Exceptions / defenses:** Federal courts lack authority under the Judiciary Act to issue "universal" injunctions protecting non-parties beyond what complete relief to the plaintiffs requires (*Trump v. CASA, Inc.* (2025)) [VERIFY V-035].

**Authority:** FRCP 65(d); *Trump v. CASA, Inc.* (2025) [VERIFY V-035].

**MBE vs. CA essay:** Rule 65(d) is a Civil Procedure MBE point. On the essay, a sentence when a third party (buyer, employee) might be bound.

**Example:** An injunction bars Δ from selling a painting. Δ's gallery agent, served with the order, is bound; an unrelated buyer with no notice is not.

---

## V. Equitable defenses

### R-REM-081 — Laches
**Rule (write this):** Laches bars equitable relief where the plaintiff unreasonably delayed in asserting its claim after it knew or should have known of it, and the delay prejudiced the defendant. Delay alone is not enough; the defendant must show prejudice, such as lost evidence or a change of position (for example, building in reliance on the plaintiff's silence).

**Elements:** 1. Π knew or should have known of the claim. 2. Unreasonable delay. 3. Prejudice to Δ.

**Exceptions / defenses:** The clock starts when Π learned or should have learned of the wrong. Laches does not ordinarily bar a legal claim for damages filed within the statute of limitations (R-REM-090).

**Authority:** Common law; *Petrella v. Metro-Goldwyn-Mayer, Inc.*, 572 U.S. 663 (2014).

**MBE vs. CA essay:** Not on the MBE. On the essay, measure the delay with the facts' dates and identify the prejudice.

**Example:** Π watches Δ build a $300,000 house partly on Π's strip for eight months without objecting, then sues for removal. Laches (and estoppel) may bar the mandatory injunction, leaving Π with damages.

> 🇨🇳 PRC bridge: unlike 诉讼时效 (a fixed statutory period), laches is a discretionary equitable bar that turns on unreasonable delay plus prejudice (approx.).

### R-REM-082 — Unclean hands
**Rule (write this):** A plaintiff who has acted inequitably, in bad faith or unlawfully in the same transaction that is the subject of the suit is barred from equitable relief ("he who comes into equity must come with clean hands"). The misconduct must relate directly to the matter in litigation; unrelated wrongdoing is irrelevant.

**Elements:** 1. Π's inequitable conduct. 2. Directly related to the claim. 3. Harm to Δ or to the integrity of the court.

**Exceptions / defenses:** California courts have applied unclean hands to bar some legal claims as well as equitable ones [VERIFY V-370].

**Authority:** Common law (equitable maxim).

**MBE vs. CA essay:** Not on the MBE. On the essay, look for Π's own lies, threats or self-help in the same deal.

**Example:** A buyer seeking specific performance of a land contract had secretly bribed the seller's agent to steer the property to him. Unclean hands bars specific performance.

### R-REM-083 — In pari delicto
**Rule (write this):** Where both parties are equally at fault in an illegal or immoral transaction, the court leaves them where it finds them: it will neither enforce the bargain nor order restitution. Relief is allowed where the plaintiff is less at fault, belongs to the class a regulatory statute protects, or withdrew before the illegal purpose was carried out.

**Elements:** 1. Illegal or immoral transaction. 2. Comparable fault. 3. No exception.

**Exceptions / defenses:** Locus poenitentiae (withdrawal in time); a protected-class plaintiff; a plaintiff induced by fraud or duress.

**Authority:** Common law; R2d §§ 197–199 [VERIFY V-371].

**MBE vs. CA essay:** Illegality is a Contracts MBE point. On the essay, raise it when Π seeks restitution of money paid for an illegal purpose.

**Example:** Π pays Δ $20,000 to bribe a zoning official; Δ keeps the money and does nothing. Π cannot recover in restitution because both parties are in pari delicto.

### R-REM-084 — Equitable estoppel
**Rule (write this):** A party is estopped from asserting a right when, by words, conduct or silence when it had a duty to speak, it led the other party to believe certain facts, intending or expecting reliance, and the other party, ignorant of the truth, reasonably relied on that belief to its detriment.

**Elements:** 1. Representation or misleading conduct/silence. 2. Intent or expectation of reliance. 3. Δ's ignorance of the truth. 4. Reasonable, detrimental reliance.

**Exceptions / defenses:** Estoppel requires detrimental reliance; waiver does not (R-REM-085).

**Authority:** Evid. Code § 623; common law.

**MBE vs. CA essay:** Not on the MBE. On the essay, combine it with laches when Π stood by while Δ built or spent.

**Example:** Π tells Δ, "I don't care where the fence goes," and Δ builds a costly fence a foot onto Π's land. Π is estopped from demanding removal.

### R-REM-085 — Waiver
**Rule (write this):** Waiver is the intentional relinquishment of a known right, express or implied from conduct inconsistent with an intent to enforce it; unlike estoppel, it does not require detrimental reliance.

**Elements:** 1. Knowledge of the right. 2. Intentional relinquishment (words or conduct).

**Exceptions / defenses:** A waiver of a condition not yet due may be retracted by notice received while a reasonable time remains for the condition to occur, unless the other party has materially changed position in reliance on the waiver (R2d § 84(2); R-CTR-064).

**Authority:** Common law; Civ. Code § 3516 (acquiescence in error takes away the right of objecting to it).

**MBE vs. CA essay:** Waiver of conditions is a Contracts MBE point. On the essay, raise it when Π accepted late performance or premiums after learning the facts.

**Example:** An insurer that learns of a misstatement in the application but keeps accepting premiums for two years may be held to have waived rescission.

### R-REM-086 — Undue hardship
**Rule (write this):** A court may deny an injunction or specific performance where the burden on the defendant (or on third parties or the public) would be greatly disproportionate to the benefit to the plaintiff, unless the defendant acted willfully or in bad faith. Undue hardship is the defensive face of the balancing-of-hardships element.

**Elements:** 1. Δ's hardship. 2. Π's benefit. 3. Gross disproportion. 4. Δ's good faith.

**Exceptions / defenses:** Hardship that arose after contracting and was caused by Δ's own conduct carries little weight.

**Authority:** R2d § 364(1)(b); *Hirshfield v. Schwartz* (2001) 91 Cal.App.4th 749 [S-466]; cross-reference R-REM-060.

**MBE vs. CA essay:** Not on the MBE. On the essay, discuss it under "Balancing of hardships" and again under "Defenses" only if the facts are strong.

**Example:** Removing a hospital wing that encroaches 18 inches on an unused alley would cost millions; Π gains little. Undue hardship supports damages instead of removal for an innocent encroacher.

### R-REM-087 — Unconscionability and inadequate consideration
**Rule (write this):** Specific performance may be refused where the contract was unfair when made — the exchange was grossly inadequate or the bargain was obtained through unfair practices — even if the contract would support damages. In California, specific performance cannot be enforced against a party who did not receive adequate consideration, or as to whom the contract is not just and reasonable.

**Elements:** 1. Measure fairness at the time of contracting. 2. Gross inadequacy or unfair practices. 3. California: Π must show adequate consideration and a just and reasonable contract.

**Exceptions / defenses:** Inadequate consideration alone does not make a contract unenforceable at law, so Π may still get damages.

**Authority:** R2d § 364(1)(c); Civ. Code § 3391 [S-474]; UCC § 2-302.

**MBE vs. CA essay:** Unconscionability is a Contracts MBE point. On a California essay seeking specific performance, add one sentence under defenses on § 3391 adequacy of consideration.

**Example:** An elderly owner, confused about values, agrees to sell a $900,000 parcel for $300,000. Specific performance is denied for inadequate consideration even if damages might be available.

### R-REM-088 — Changed circumstances: modifying or dissolving an injunction
**Rule (write this):** A court that issued an injunction retains power to modify or dissolve it when a significant change in facts or law makes continued enforcement inequitable or no longer necessary. Changed circumstances after contracting may also make specific performance inequitable.

**Elements:** 1. Significant change in fact or law after the decree. 2. Continued enforcement inequitable or unnecessary. 3. Modification suitably tailored.

**Exceptions / defenses:** A party's own regret or increased cost is not enough.

**Authority:** *Rufo v. Inmates of Suffolk County Jail*, 502 U.S. 367 (1992); FRCP 60(b)(5); CCP § 533 [VERIFY V-365].

**MBE vs. CA essay:** Not on the MBE. On the essay, raise it when a long-running injunction meets new facts (a rezoning, a new statute).

**Example:** An injunction restricts a factory's operating hours because of nearby homes; years later the area is rezoned industrial and the homes are gone. The factory may move to dissolve the injunction.

### R-REM-089 — Other defenses to specific performance
**Rule (write this):** In addition to the general equitable defenses, specific performance may be defeated by any defense to the contract itself — lack of formation or definiteness, the statute of frauds (unless part performance or estoppel applies), mistake, misrepresentation, impossibility or impracticability — and by the plaintiff's own failure to perform its conditions or the defendant's prior sale to a bona fide purchaser.

**Elements:** List each contract defense raised by the facts and test it briefly.

**Exceptions / defenses:** Part performance (possession plus payment or improvements) takes an oral land contract out of the statute of frauds for specific performance.

**Authority:** R2d §§ 129, 357–369; cross-reference R-CTR-042, R-CTR-104.

**MBE vs. CA essay:** Contracts MBE points. On the essay, give each defense a short paragraph under "Defenses."

**Example:** An oral agreement to sell a farm is unenforceable under the statute of frauds, but the buyer moved in, paid part of the price and built a barn; part performance supports specific performance.

### R-REM-090 — Laches vs. statute of limitations
**Rule (write this):** Legal claims are governed by statutes of limitations, and equitable claims primarily by laches, although courts often borrow the analogous limitations period as a guide. Within the limitations period, laches generally cannot bar a claim for legal relief (damages), though it may bar or limit equitable relief.

**Elements:** 1. Is the claim legal or equitable? 2. Legal → statute of limitations. 3. Equitable → laches (with the statute as a guide).

**Exceptions / defenses:** —

**Authority:** *Petrella v. Metro-Goldwyn-Mayer, Inc.*, 572 U.S. 663 (2014); *SCA Hygiene Products Aktiebolag v. First Quality Baby Products, LLC*, 580 U.S. 328 (2017).

**MBE vs. CA essay:** Not on the MBE. On the essay, say that a delayed Π may lose the injunction but keep damages.

**Example:** Π sues for trespass damages four years after the fence went up, within the five-year limitations period. Her damages claim survives even if laches bars a removal order.

---

## VI. Declaratory remedies

### R-REM-091 — Declaratory judgment
**Rule (write this):** In a case of actual controversy, a court may declare the rights and other legal relations of an interested party, whether or not further relief is or could be sought. A declaratory judgment binds the parties but orders nothing; coercive relief based on it may be granted later. In California, any person interested under a written instrument or contract, or with respect to property, may seek a declaration of rights and duties, even before any breach.

**Elements:** 1. Actual, justiciable controversy (R-REM-092). 2. Interested party. 3. Appropriate subject (contract meaning, constitutionality of a statute, insurance coverage, title).

**Exceptions / defenses:** Declaratory relief is discretionary (R-REM-092). Whether a jury is available depends on whether the underlying issue is legal or equitable.

**Authority:** 28 U.S.C. §§ 2201, 2202; FRCP 57; CCP § 1060 [S-467].

**MBE vs. CA essay:** Not on the MBE as a Remedies rule. On a California essay (Jul 2019 Q2 church: TRO, preliminary injunction and declaratory relief [VERIFY V-071]), analyze declaratory relief after the injunctions as the remedy that settles the legal question.

**Example:** A tenant disputes whether a lease renewal option is still open. Rather than risk breach, she seeks a declaration of her right to renew.

> 🇨🇳 PRC bridge: similar to a 确认之诉 (action for a declaration/confirmation) (approx.).

### R-REM-092 — Actual controversy; discretion to refuse
**Rule (write this):** A declaratory judgment requires a dispute that is definite and concrete, touching the legal relations of parties with adverse legal interests, and real and substantial enough to admit of specific relief, rather than an advisory opinion on hypothetical facts. The court may decline relief where a declaration is not necessary or proper at the time under all the circumstances. A plaintiff threatened with enforcement of an allegedly unconstitutional statute may seek a declaration without first violating the law.

**Elements:** 1. Adverse parties. 2. Concrete, ripe dispute. 3. Declaration would resolve it. 4. Court's discretion.

**Exceptions / defenses:** Declaratory relief against a threatened state prosecution does not require the showing of irreparable harm needed for an injunction (*Steffel v. Thompson*, 415 U.S. 452 (1974)).

**Authority:** *MedImmune, Inc. v. Genentech, Inc.*, 549 U.S. 118 (2007); *Steffel v. Thompson*, 415 U.S. 452 (1974); *Wilton v. Seven Falls Co.*, 515 U.S. 277 (1995); CCP § 1061 [S-467].

**MBE vs. CA essay:** Justiciability is a Con Law / Civil Procedure MBE topic. On the essay, one paragraph on ripeness and the court's discretion.

**Example:** A city announces it will enforce a new ordinance next month; a church that will be affected has an actual controversy and may seek a declaration that the ordinance is unconstitutional now.

### R-REM-093 — Quiet title
**Rule (write this):** An action to quiet title establishes the plaintiff's title to real property against adverse claims and removes clouds on title, producing a judgment that binds the parties (and, under statutory procedures, others with notice). In California the action is statutory.

**Elements:** 1. Π's claimed title. 2. Δ's adverse claim. 3. Determination of the parties' interests.

**Exceptions / defenses:** Adverse possession, estoppel and the recording acts often decide the merits (Real Property).

**Authority:** CCP § 760.010 et seq. [VERIFY V-368].

**MBE vs. CA essay:** Not on the MBE as a remedy. On a Real Property/Remedies essay, pair it with cancellation or ejectment.

**Example:** After a forged deed is recorded, the true owner sues to quiet title and cancel the deed.

### R-REM-094 — Nominal damages
**Rule (write this):** Nominal damages — a trivial sum such as $1 — are awarded when the plaintiff proves the defendant violated a legal right but cannot prove actual loss. They vindicate the right, establish a precedent (for example, a boundary or an easement), may carry costs, and redress a completed injury for standing purposes.

**Elements:** 1. Invasion of a legal right (trespass, battery, breach of contract, constitutional violation). 2. No proven actual loss.

**Exceptions / defenses:** Negligence requires actual damage, so nominal damages are not available for negligence alone. In California, nominal damages alone do not support punitive damages [VERIFY V-356].

**Authority:** Civ. Code § 3360; R2d § 346(2); *Uzuegbunam v. Preczewski*, 592 U.S. 279 (2021).

**MBE vs. CA essay:** Nominal damages appear in Torts and Contracts MBE questions. On a Remedies essay, always mention them when the harm is small or unproven.

**Example:** Δ walks across Π's lawn every day without causing damage. Π recovers nominal damages for the trespass and an injunction against future entries.
