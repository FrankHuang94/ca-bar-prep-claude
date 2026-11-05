---
id: E-CIV-001
type: single
subjects: [CIV]
coverage_ids: [CIV-MBE-I.A, CIV-CBX-I, CIV-MBE-I.B, CIV-CBX-II, CIV-MBE-II.A, CIV-MBE-III.D, CIV-CBX-VI, CIV-MBE-VI.D]
rule_ids: [R-CIV-004, R-CIV-006, R-CIV-008, R-CIV-010, R-CIV-011, R-CIV-052, R-CIV-017, R-CIV-047, R-CIV-020, R-CIV-021, R-CIV-022, R-CIV-023, R-CIV-024, R-CIV-037, R-CIV-038, R-CIV-039, R-CIV-040, R-CIV-095, R-CIV-096, R-CIV-098]
calls:
  - "1. Does the federal court have subject-matter jurisdiction over (a) Tomas's claims and (b) VoltRide's counterclaim? Discuss."
  - "2. Does the court have personal jurisdiction over VoltRide and over CellCore? Discuss."
  - "3. Should the court dismiss Tomas's negligence and strict-liability claims as time-barred? Discuss."
  - "4. Assuming Tomas's claims survive, may he use the Brooks judgment to establish that the VR-48 battery pack was defectively designed? Discuss."
issues:
  - {issue: "Diversity: complete diversity; corporate citizenship and the nerve-center test", points: 14, call: 1, major: true, rule_ids: [R-CIV-004, R-CIV-006], coverage_ids: [CIV-MBE-I.A, CIV-CBX-I]}
  - {issue: "Amount in controversy", points: 4, call: 1, rule_ids: [R-CIV-008], coverage_ids: [CIV-MBE-I.A]}
  - {issue: "Counterclaim: compulsory (logical relationship) and supplemental jurisdiction under 1367(a)-(b)", points: 10, call: 1, rule_ids: [R-CIV-010, R-CIV-011, R-CIV-052], coverage_ids: [CIV-MBE-III.D, CIV-CBX-VI]}
  - {issue: "PJ over VoltRide: waiver, long-arm, general vs. specific jurisdiction, fairness", points: 12, call: 2, rule_ids: [R-CIV-047, R-CIV-017, R-CIV-020, R-CIV-021, R-CIV-022, R-CIV-023], coverage_ids: [CIV-MBE-I.B, CIV-CBX-II]}
  - {issue: "PJ over CellCore: stream of commerce (both views), relatedness, fairness", points: 18, call: 2, major: true, rule_ids: [R-CIV-024, R-CIV-022, R-CIV-023], coverage_ids: [CIV-MBE-I.B, CIV-CBX-II]}
  - {issue: "Erie: Rule 3 vs. state commencement-by-service rule (Walker); twin aims; result", points: 22, call: 3, major: true, rule_ids: [R-CIV-037, R-CIV-038, R-CIV-039, R-CIV-040], coverage_ids: [CIV-MBE-II.A]}
  - {issue: "Issue preclusion: governing law (1738) and elements", points: 8, call: 4, rule_ids: [R-CIV-095, R-CIV-098], coverage_ids: [CIV-MBE-VI.D]}
  - {issue: "Non-mutual offensive issue preclusion: Parklane fairness factors", points: 12, call: 4, major: true, rule_ids: [R-CIV-096], coverage_ids: [CIV-MBE-VI.D]}
time_minutes: 60
source: original
status: draft
last_verified: 2026-11-04
tags: [wave1, E1, federal, diversity, personal-jurisdiction, erie, preclusion]
---

# E-CIV-001 — The burning e-bike battery

## Facts

Tomas Reyes has lived in State A for twelve years. In January 2024 he bought an electric bicycle from VoltRide, Inc. through VoltRide's website for $3,400. He paid $1,900 up front and agreed to pay the remaining $1,500 in monthly installments to VoltRide.

VoltRide is incorporated in State B. Its headquarters is in State B, where its chief financial officer, general counsel and other senior officers work and where the board meets and approves budgets and strategy. Its chief executive lives in State A and works from a home office there two days a week, spending the rest of the week at headquarters. VoltRide assembles its bicycles at a plant in State D. Its largest facility, a warehouse and customer-service center employing 450 of its 750 workers, is in State A. VoltRide sells bicycles nationwide through its website, and its social-media advertisements name State A cities. About 9% of its sales go to State A residents.

The bicycle's VR-48 battery pack contains lithium cells made by CellCore Corp., which is incorporated in State C and has its only offices and plant there. CellCore sells cells only to VoltRide and delivers them to VoltRide's State D plant. Its supply contract states that the cells are "for incorporation into VoltRide e-bikes sold throughout the United States." CellCore has no offices, employees, advertising or customers in State A. In 2023 two CellCore engineers staffed a booth at a trade show in State A to market cells to other bicycle makers; no sales resulted.

On March 3, 2024, the battery caught fire while charging in Tomas's garage in State A. Tomas suffered serious burns to his arm. His medical bills were $62,000, he lost $18,000 in wages, and his $24,000 car was destroyed. Tomas stopped making installment payments after the fire.

On February 20, 2026, Tomas sued VoltRide and CellCore in the United States District Court for the District of State A, alleging negligence, strict products liability and breach of the implied warranty of merchantability, all under State A law, and seeking $250,000. He served VoltRide on March 20, 2026, within 90 days after filing. State A law provides a two-year limitations period for negligence and strict-liability claims and a four-year period, running from tender of delivery, for warranty claims. A State A statute provides that "an action is commenced, for purposes of the statute of limitations, when the summons and complaint are served on the defendant." State A's long-arm statute reaches as far as the federal Constitution allows.

VoltRide moved to dismiss for lack of subject-matter jurisdiction, arguing that it is a citizen of State A, and moved to dismiss the tort claims as time-barred. It also filed a counterclaim against Tomas for the unpaid $1,500. CellCore moved to dismiss for lack of personal jurisdiction.

In 2025, in a State A state court, another VoltRide customer, Lena Brooks, sued VoltRide after her VR-48 pack caught fire. After a nine-day jury trial in which VoltRide was represented by experienced national counsel, the jury returned a special verdict that the VR-48 pack "was defectively designed because its cells lacked adequate thermal separation" and awarded Brooks $2.1 million. VoltRide did not appeal. Tomas followed the trial in the news and told a friend, "I'll wait and see how Lena's case goes before I sue." In 2024, a federal jury in State E had found, in a suit by a different customer, that the VR-48 pack was not defectively designed. The design did not change between 2023 and mid-2025. State A follows the Restatement (Second) of Judgments and *Parklane Hosiery Co. v. Shore* on issue preclusion.

## Call of the Question

1. Does the federal court have subject-matter jurisdiction over (a) Tomas's claims and (b) VoltRide's counterclaim? Discuss.
2. Does the court have personal jurisdiction over VoltRide and over CellCore? Discuss.
3. Should the court dismiss Tomas's negligence and strict-liability claims as time-barred? Discuss.
4. Assuming Tomas's claims survive, may he use the Brooks judgment to establish that the VR-48 battery pack was defectively designed? Discuss.

## Issue List

| # | Issue | Call | Points |
|---|---|---|---|
| 1 | Diversity: complete diversity; VoltRide's nerve center | 1 | 14 |
| 2 | Amount in controversy | 1 | 4 |
| 3 | Counterclaim: compulsory; supplemental jurisdiction | 1 | 10 |
| 4 | PJ over VoltRide (waiver; merits) | 2 | 12 |
| 5 | PJ over CellCore: stream of commerce | 2 | 18 |
| 6 | Erie: Rule 3 vs. State A's commencement rule | 3 | 22 |
| 7 | Issue preclusion: governing law and elements | 4 | 8 |
| 8 | Non-mutual offensive preclusion: Parklane factors | 4 | 12 |
| | **Total** | | **100** |

## Model Answer

### 1. Subject-matter jurisdiction

**(a) Tomas's claims: diversity.** Federal courts have limited jurisdiction. All of Tomas's claims arise under State A law, so the only basis is diversity: an action between citizens of different States with more than $75,000 in controversy, exclusive of interest and costs (28 U.S.C. § 1332(a)). Diversity must be complete, so no plaintiff may share citizenship with any defendant, measured when the action is filed (*Strawbridge*; *Grupo Dataflux*).

*Tomas* is domiciled in State A, where he has lived for twelve years with no indication of intent to leave. He is a State A citizen.

*CellCore* is a citizen of its State of incorporation and its principal place of business (§ 1332(c)(1)), both State C. It is diverse from Tomas.

*VoltRide* is a citizen of State B, where it is incorporated, and of the State of its principal place of business. Under *Hertz Corp. v. Friend*, the principal place of business is the "nerve center," the place where high-level officers direct, control and coordinate the corporation's activities, normally its actual headquarters.

VoltRide argues that it is a State A citizen because its largest facility, with 450 of 750 employees, is there and its CEO works from State A two days a week. *Hertz* rejected a test based on where the most business activity or employees are located; the size of the State A warehouse is irrelevant. The CEO's partial remote work does not move the nerve center either: the board meets, budgets and strategy are approved, and the other senior officers work at the State B headquarters, and the CEO spends most of the week there. **VoltRide's principal place of business is State B**, so it is a citizen of State B only, and **complete diversity exists**.

**Amount in controversy.** The plaintiff's good-faith claim controls unless it is legally certain that he cannot recover more than $75,000 (*St. Paul Mercury*). Tomas seeks $250,000, supported by $62,000 in medical bills, $18,000 in lost wages, a $24,000 car and pain and suffering. His claims against each defendant exceed $75,000. **The amount requirement is met**, and the court has diversity jurisdiction over Tomas's claims.

**(b) VoltRide's $1,500 counterclaim.** The counterclaim cannot stand alone: although Tomas and VoltRide are diverse, $1,500 is far below the threshold. It needs supplemental jurisdiction.

*Compulsory or permissive?* A counterclaim is compulsory if it arises out of the transaction or occurrence that is the subject of the opposing party's claim (FRCP 13(a)); courts apply a logical-relationship test. VoltRide's claim is for the unpaid price of the very bicycle whose battery Tomas says was defective, and Tomas's warranty claim arises from the same sale. Tomas will likely defend nonpayment by asserting the breach of warranty, so the same evidence will be heard. Tomas might argue that a debt-collection claim is logically distinct from a personal-injury fire, but the shared sale contract supplies a logical relationship. **The counterclaim is likely compulsory.**

*Supplemental jurisdiction.* Under § 1367(a), the court has supplemental jurisdiction over claims that form part of the same case or controversy, deriving from a common nucleus of operative fact (*Gibbs*). The sale of this bicycle is the common nucleus. Section 1367(b), which limits supplemental jurisdiction in diversity cases, restricts only claims *by plaintiffs* against persons joined under Rules 14, 19, 20 or 24; a defendant's counterclaim is not covered. **The court has supplemental jurisdiction over the counterclaim.** Even if it were permissive, it would arguably still fall within § 1367(a) because of the shared transaction.

### 2. Personal jurisdiction

A federal court may exercise personal jurisdiction if the forum State's long-arm statute authorizes it (FRCP 4(k)(1)(A)) and the exercise satisfies due process. State A's long-arm statute reaches the constitutional limit, so the only question is due process: whether each defendant has minimum contacts with State A such that the suit does not offend traditional notions of fair play and substantial justice (*International Shoe*).

**VoltRide.**

*Waiver.* VoltRide moved to dismiss for lack of subject-matter jurisdiction and on limitations grounds without objecting to personal jurisdiction, and it filed a counterclaim. A personal-jurisdiction defense omitted from a party's first Rule 12 motion is waived (FRCP 12(g)(2), 12(h)(1)), so **VoltRide has waived any objection**. The analysis below shows that the result would be the same on the merits.

*General jurisdiction.* A corporation is subject to general jurisdiction where it is "at home," paradigmatically its State of incorporation and principal place of business (*Daimler*; *BNSF*). VoltRide is at home in State B. A large warehouse in State A is substantial business activity, but *BNSF* held that even extensive in-state operations do not make a corporation at home. **No general jurisdiction in State A.**

*Specific jurisdiction.* VoltRide must have purposefully availed itself of the forum, the claim must arise out of or relate to those contacts, and jurisdiction must be reasonable (*Burger King*; *Ford*). VoltRide sells directly to State A residents through its website, ships bicycles there, runs advertisements naming State A cities, and earns about 9% of its sales there. These are deliberate contacts with the forum market. Tomas's claims arise directly from one of those sales, a bicycle sold to and used by a State A resident that injured him in State A. Jurisdiction is fair: VoltRide has a 450-employee facility in State A, State A has a strong interest in injuries to its residents, and Tomas was injured at home in State A. **The court has specific jurisdiction over VoltRide.**

**CellCore.**

CellCore has no offices, employees, advertising or customers in State A and ships its cells to State D. Its only possible link is the stream of commerce: its cells reach State A inside VoltRide's bicycles.

*Purposeful availment.* The Supreme Court has never produced a majority opinion on the stream of commerce, so both views should be applied.

- *"Stream of commerce plus" (O'Connor plurality in* Asahi*; Kennedy plurality in* Nicastro*).* Mere awareness that a product will reach the forum is not enough; the defendant must target the forum, for example by designing the product for that market, advertising there, establishing channels for customer advice, or using a distributor as its sales agent there. CellCore sells to one customer in another State. Its supply contract shows awareness of nationwide sales but no conduct aimed at State A specifically. Tomas will point to the 2023 State A trade show as targeting. But that marketing was aimed at other bicycle makers, produced no sales, and has nothing to do with the cells in Tomas's bicycle. Under this view, **CellCore did not purposefully avail itself of State A.**
- *"Pure" stream of commerce (Brennan concurrence in* Asahi*).* A defendant that places goods in a regular and anticipated flow into the forum, knowing the final product is marketed there, has purposefully availed itself. CellCore knew its cells would go into bicycles "sold throughout the United States," and about 9% of VoltRide's sales go to State A, meaning a steady, predictable volume of CellCore cells reaches the State each year. This is not the single isolated sale that Justice Breyer found insufficient in *Nicastro*. Under this view, **the contacts suffice.**

*Relatedness and fairness.* If purposeful availment exists, the claim relates to it: the claim concerns a CellCore cell that reached State A through that flow and injured a State A resident there (*Ford*). Fairness would favor Tomas, given State A's interest and Tomas's need for a single forum, although CellCore's burden of defending far from its only location in State C is real.

*Conclusion.* The answer depends on which view the court follows. Because the most recent Supreme Court plurality (*Nicastro*) required forum-directed conduct, and CellCore's only forum-directed act is unrelated to this claim, **the court will likely grant CellCore's motion to dismiss**, though the regular volume of cells flowing into State A makes this a close question.

### 3. Are the tort claims time-barred? (Erie)

A federal court hearing state-law claims in diversity applies state substantive law and federal procedural law (*Erie*; Rules of Decision Act, 28 U.S.C. § 1652). Under *Klaxon*, it applies the forum State's choice-of-law rules, and every relevant event occurred in State A, so State A's two-year limitations period governs the tort claims. It ran on March 3, 2026. Tomas filed on February 20 but served VoltRide on March 20. Whether the claims are timely therefore depends on when the action "commenced."

**Is there a Federal Rule on point?** If a valid Federal Rule is sufficiently broad to control the issue, it applies despite contrary state law (*Hanna v. Plumer*). Tomas will argue FRCP 3, which says "a civil action is commenced by filing a complaint," directly collides with State A's statute, so Rule 3 governs and his February 20 filing was timely. He will add that he served within Rule 4(m)'s 90 days.

VoltRide will respond, correctly, that the Supreme Court rejected this argument in *Walker v. Armco Steel Corp.* There the Court held that Rule 3 governs the date from which the Federal Rules' own time periods run, but it was not intended to toll a state statute of limitations or displace a State's rule about when an action is commenced for limitations purposes. Courts read the Rules to avoid needless conflict with state law. Because Rule 3 is not "sufficiently broad" to answer this question, there is no direct collision, and Rule 4(m) concerns the time for service, not tolling.

**Unguided Erie analysis.** Without a Federal Rule on point, the court asks whether ignoring the state rule would be outcome-determinative in a way that undermines Erie's twin aims of discouraging forum shopping and avoiding inequitable administration of the laws (*Guaranty Trust v. York*; *Hanna*).

- *Outcome.* The choice decides whether the tort claims survive at all. Limitations rules are the classic substantive rule under *York*.
- *Forum shopping and inequity.* If federal court allowed filing alone to stop the clock, a State A plaintiff who could not serve in time would choose federal court to gain extra time, and identical State A plaintiffs would be barred in state court but not in federal court only because of diversity of citizenship.
- *Countervailing federal interest.* Unlike the judge-jury allocation in *Byrd*, no strong federal policy requires a filing rule for state-law limitations periods. State A's service requirement is part of its definition of how long a defendant remains exposed to suit, so it is bound up with state-created rights.

**State A's rule applies.** The tort actions commenced on March 20, 2026, more than two years after the March 3, 2024 fire. **The court should dismiss the negligence and strict-liability claims as time-barred.** The warranty claim survives: its four-year period runs from tender in January 2024, so it is timely under either rule.

### 4. Preclusive effect of the Brooks judgment

**Governing law.** Federal courts give a state-court judgment the same preclusive effect it would have in the courts of the State that rendered it (U.S. Const. art. IV, § 1; 28 U.S.C. § 1738). The Brooks judgment was entered by a State A court, so State A law applies, and State A follows the Restatement (Second) of Judgments and *Parklane*.

**Elements.** Issue preclusion bars relitigating an issue of fact that was actually litigated and determined by a valid, final judgment, where the determination was essential to the judgment and the party against whom it is asserted had a full and fair opportunity to litigate it.

- *Same issue.* Brooks determined that the VR-48 pack "was defectively designed because its cells lacked adequate thermal separation." Tomas's pack is a VR-48 built while the design was unchanged, so the issue is identical.
- *Actually litigated and determined.* A nine-day trial ended in a special verdict on that very question.
- *Final and valid.* VoltRide did not appeal; the judgment is final.
- *Essential.* The defect finding was necessary to the liability verdict and the $2.1 million award.
- *Against a party.* VoltRide, the party to be bound, was a party in Brooks, represented by national counsel.

**Non-mutual offensive use.** Tomas was not a party to Brooks and wants to use the finding as a sword. Mutuality is not required, but offensive non-mutual preclusion is discretionary and should be denied where (1) the plaintiff could easily have joined the earlier action, (2) the defendant lacked incentive to litigate vigorously, (3) the judgment is inconsistent with earlier judgments, or (4) the second action offers procedural opportunities unavailable in the first (*Parklane*).

- *Incentive.* This factor favors Tomas. A design-defect claim exposing VoltRide to $2.1 million and to suits by every VR-48 owner gave it every incentive to fight, and it did, for nine days with national counsel.
- *Procedural opportunities.* Both cases offered full discovery and a jury, so this factor is neutral or favors Tomas.
- *Wait and see.* This factor cuts strongly against Tomas. He knew of Brooks's suit, followed the trial and said, "I'll wait and see how Lena's case goes." Tomas will argue he could not "easily" have joined a stranger's suit about a different fire. But his own words show the strategic waiting that *Parklane* aims to discourage: had Brooks lost, he would not be bound.
- *Inconsistent judgments.* This factor is decisive. A 2024 State E federal jury found the same VR-48 design *not* defective. When a defendant has won one case and lost another on the same issue, allowing a later plaintiff to pick the favorable result is unfair, the very example *Parklane* gives.

**Conclusion.** Although the elements are met, the court will likely **deny offensive issue preclusion** because of the inconsistent prior verdict and Tomas's wait-and-see conduct. Tomas must prove the design defect himself, and the Brooks evidence may still help him do so.

## Self-Grading Rubric

| Issue | Points | Full credit requires | Rule IDs |
|---|---|---|---|
| Diversity; nerve center | 14 | Complete diversity; each party's citizenship; *Hertz* nerve center applied to HQ vs. CEO's remote days vs. warehouse size; conclusion | R-CIV-004, R-CIV-006 |
| Amount in controversy | 4 | Good-faith claim; legal-certainty test; > $75,000 per defendant | R-CIV-008 |
| Counterclaim | 10 | Rule 13(a) logical relationship; § 1367(a) common nucleus; § 1367(b) does not bar defendants' claims; $1,500 cannot stand alone | R-CIV-010, R-CIV-011, R-CIV-052 |
| PJ over VoltRide | 12 | Waiver by omission from the Rule 12 motion (12(g)(2), (h)(1)); Rule 4(k)(1)(A) + long-arm; not at home (*Daimler*/*BNSF*); specific jurisdiction with purposeful availment, relatedness, fairness | R-CIV-047, R-CIV-017, R-CIV-020, R-CIV-021, R-CIV-022, R-CIV-023 |
| PJ over CellCore | 18 | Both stream-of-commerce views applied to facts (supply-contract recital, 9% volume, trade show); relatedness (*Ford*); fairness; reasoned conclusion | R-CIV-024, R-CIV-022, R-CIV-023 |
| Erie / Walker | 22 | *Erie*/*Klaxon* framing; *Hanna* direct-collision step; Rule 3 not on point (*Walker*); *York* outcome; twin aims; *Byrd*; dates applied; warranty claim survives | R-CIV-037, R-CIV-038, R-CIV-039, R-CIV-040 |
| Issue preclusion elements | 8 | § 1738 / State A law; five elements applied | R-CIV-095, R-CIV-098 |
| Parklane factors | 12 | Offensive non-mutual use is discretionary; all four factors applied; inconsistent judgment and wait-and-see statement used | R-CIV-096 |
| **Total** | **100** | | |

**Scoring on the 40–100 scale** (`00-exam-intel/grader-expectations.md` §4):
- **75+:** applies *Hertz* to the specific facts, gives both stream-of-commerce views, correctly uses *Walker* (not *Hanna*) to resolve the Rule 3 argument, and works through the *Parklane* factors with the inconsistent-verdict point.
- **65:** right framework on all four calls but thin application, for example concluding on stream of commerce without applying both views.
- **55:** misses *Walker* and applies Rule 3, or omits the counterclaim, or treats preclusion as automatic once the elements are met.
- **45 or below:** confuses subject-matter and personal jurisdiction, or answers the Erie call with "federal courts apply federal procedure" alone.

**Common mistakes**
1. Using a "place of operations" or "most employees" test for the principal place of business. *Hertz* adopted the nerve-center test.
2. Treating Rule 3 as a direct collision. *Walker* held that it does not address state limitations commencement.
3. Applying § 1367(b) to a defendant's counterclaim. It limits claims by plaintiffs.
4. Giving only one stream-of-commerce view. With no majority opinion, both must be applied.
5. Stopping issue preclusion at the elements. Offensive non-mutual use always needs the *Parklane* fairness factors.

> 🇨🇳 PRC bridge: a PRC court's prior effective judgment can establish facts in later litigation that a party need not prove again, subject to rebuttal; US offensive non-mutual preclusion is narrower and discretionary (approx.).

**Accuracy notes.** Rules follow R-CIV-004, -006, -010, -011, -018, -024, -038 to -040, -095, -096, -098. The Erie analysis relies on *Walker v. Armco Steel Corp.*, 446 U.S. 740 (1980), as summarized in R-CIV-038 and R-CIV-040; no recent or pending decision is needed for any answer. The stream-of-commerce split is presented as a split, as R-CIV-024 directs. The waiver point follows R-CIV-047 (FRCP 12(g)(2), (h)(1)).
