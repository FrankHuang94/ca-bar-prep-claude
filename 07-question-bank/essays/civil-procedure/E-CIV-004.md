---
id: E-CIV-004
type: single
subjects: [CIV]
coverage_ids: [CIV-MBE-III.D, CIV-MBE-III.E, CIV-MBE-III.F, CIV-MBE-V.A, CIV-MBE-IV.A, CIV-CBX-VI, CIV-SUP-011]
rule_ids: [R-CIV-059, R-CIV-060, R-CIV-061, R-CIV-064, R-CIV-072, R-CIV-073, R-CIV-085, R-CIV-086, R-CIV-078, R-CIV-079, R-CIV-080]
calls:
  - "1. Should the court certify the class Rosa proposes? Discuss."
  - "2. How should the court rule on (a) Rosa's motion to compel and (b) her motion for sanctions? Discuss."
  - "3. Assume the court certified a subclass of Version A customers. How should the court rule on PantryBox's motion for summary judgment against that subclass? Discuss."
  - "4. Is there a right to a jury trial, and if so, on which issues and in what order? Discuss."
issues:
  - {issue: "Rule 23(a): numerosity, commonality (Dukes) by sign-up channel, typicality (Version B; refund), adequacy of Rosa and class counsel", points: 16, call: 1, major: true, rule_ids: [R-CIV-059], coverage_ids: [CIV-MBE-III.D, CIV-CBX-VI]}
  - {issue: "Rule 23(b)(3): predominance (channel-specific consent questions; phone sign-ups), superiority; subclasses", points: 14, call: 1, major: true, rule_ids: [R-CIV-060, R-CIV-061], coverage_ids: [CIV-MBE-III.D, CIV-CBX-VI]}
  - {issue: "Rule 23(b)(2) for the injunction; no individualized damages under (b)(2) (Dukes); (b)(3) notice and opt-out", points: 8, call: 1, major: false, rule_ids: [R-CIV-060], coverage_ids: [CIV-MBE-III.D]}
  - {issue: "Motion to compel: scope and proportionality of the ten-year request; confidentiality is not a privilege (protective order); meet and confer; mandatory expenses", points: 14, call: 2, major: true, rule_ids: [R-CIV-064, R-CIV-072, R-CIV-073], coverage_ids: [CIV-MBE-III.E]}
  - {issue: "Sanctions for violating the discovery order: Rule 37(b)(2) menu; terminating sanctions require willfulness and consideration of lesser sanctions; issue-related, proportionate sanction; expenses", points: 14, call: 2, major: true, rule_ids: [R-CIV-073], coverage_ids: [CIV-MBE-III.E]}
  - {issue: "Summary judgment: standard and burdens; genuine dispute over the pre-checked box; materiality of consent; admissible-form evidence (counsel's information-and-belief declaration)", points: 18, call: 3, major: true, rule_ids: [R-CIV-085, R-CIV-086], coverage_ids: [CIV-MBE-III.F, CIV-MBE-V.A]}
  - {issue: "Seventh Amendment: statutory damages are legal; injunction is equitable; 'penalty' argument", points: 10, call: 4, major: true, rule_ids: [R-CIV-078], coverage_ids: [CIV-MBE-IV.A]}
  - {issue: "Mixed claims: jury decides common issues first (Beacon Theatres); timely demand", points: 6, call: 4, major: false, rule_ids: [R-CIV-079, R-CIV-080], coverage_ids: [CIV-MBE-IV.A]}
time_minutes: 60
source: original
status: draft
last_verified: 2026-11-04
tags: [wave2, W2-E7, class-action, discovery-sanctions, summary-judgment, jury-trial]
---

## Facts

Assume that a federal statute (the "Act") makes it unlawful for a seller to charge a consumer for an automatic renewal unless, before the first charge, the seller obtained the consumer's "express affirmative consent" to the renewal terms. The Act gives each consumer the greater of actual damages or $250 for each unlawful charge, authorizes injunctive relief, and places on the consumer the burden of proving that consent was not obtained.

PantryBox, Inc., a Delaware corporation headquartered in Texas, sells meal-kit subscriptions online nationwide. From January 2024 through December 2025, about 410,000 customers signed up for a "14-day free trial" that automatically converted into a $79-per-month subscription. They signed up in one of three ways:
- **Version A web page** (January–June 2024; about 150,000 customers). The page contained a checkbox next to the words "I agree to automatic renewal at $79/month," printed in small light-gray type. PantryBox says the box was unchecked unless the customer checked it.
- **Version B web page** (July 2024–December 2025; about 220,000 customers). There was no checkbox; the renewal terms appeared only behind a "Terms" link at the bottom of the page.
- **Telephone** (about 40,000 customers). Sales representatives followed scripts that changed several times; some read the renewal terms aloud and some did not. Recordings exist for only some calls.

Rosa Delgado, a California resident, signed up through Version B in August 2024 and was charged $79 three times before she cancelled. After she complained, PantryBox refunded her third charge. Represented by Brennan & Ochoa LLP, a firm that has litigated many consumer class actions, Rosa sued PantryBox in the U.S. District Court for the Northern District of California. On behalf of "all persons charged by PantryBox for an automatic renewal from January 2024 through December 2025," she seeks $250 per unlawful charge for each class member and an injunction requiring a clear, unchecked consent box. Her complaint demands a jury trial.

Rosa served a request for "all documents concerning the design, testing or performance of any PantryBox sign-up page since the company's founding in 2014," and a separate request for the A/B test results comparing the Version A and Version B pages. PantryBox objected to the first request as overbroad and refused to produce anything in response to the second, calling the results "confidential business information." After two unsuccessful meet-and-confer calls, Rosa moved to compel.

The court ordered PantryBox to produce its 2024–2025 sign-up testing data within 30 days under a protective order. PantryBox produced some data but not a spreadsheet titled "Checkbox default = ON: conversion +18%," dated February 2024. A former PantryBox engineer later revealed the spreadsheet. PantryBox's vice president called the omission "an oversight." Rosa moved for sanctions, asking the court to enter a default judgment or, alternatively, to treat as established that the Version A checkbox was pre-checked.

After discovery, PantryBox moved for summary judgment against the Version A customers. It submitted an engineer's declaration and archived screenshots showing an unchecked box, and argued that checking a box is "express affirmative consent" as a matter of law. Rosa opposed with the spreadsheet, declarations from three Version A customers stating that the box was already checked when they reached the page and that they never noticed it, an expert report on the small gray type, and a declaration from her lawyer stating "on information and belief" that "thousands of customers were confused."

PantryBox has also moved to strike the jury demand. It argues that the case is "fundamentally equitable" because Rosa seeks an injunction, and that the $250 awards are a statutory "penalty" for the judge to decide.

## Call of the Question

1. Should the court certify the class Rosa proposes? Discuss.
2. How should the court rule on (a) Rosa's motion to compel and (b) her motion for sanctions? Discuss.
3. Assume the court certified a subclass of Version A customers. How should the court rule on PantryBox's motion for summary judgment against that subclass? Discuss.
4. Is there a right to a jury trial, and if so, on which issues and in what order? Discuss.

## Issue List

| # | Issue | Call | Points |
|---|---|---|---|
| 1 | Rule 23(a) prerequisites | 1 | 16 |
| 2 | Rule 23(b)(3) predominance and superiority; subclasses | 1 | 14 |
| 3 | Rule 23(b)(2); notice and opt-out | 1 | 8 |
| 4 | Motion to compel | 2 | 14 |
| 5 | Sanctions for violating the order | 2 | 14 |
| 6 | Summary judgment against the Version A subclass | 3 | 18 |
| 7 | Seventh Amendment right | 4 | 10 |
| 8 | Order of trial (Beacon Theatres); demand | 4 | 6 |

## Model Answer

The case is in federal court on a federal claim, so the Federal Rules of Civil Procedure and federal law govern.

### 1. Class certification

A class action may proceed only if the four Rule 23(a) prerequisites are met and the action fits a Rule 23(b) category. The court must conduct a rigorous analysis, which may overlap with the merits (*Dukes*).

**A. Rule 23(a).**
- **Numerosity.** About 410,000 customers is far too many to join. Satisfied.
- **Commonality.** There must be a common contention whose truth or falsity resolves an issue central to every member's claim "in one stroke" (*Dukes*). PantryBox will argue that "did each customer give express affirmative consent?" has no single answer across three different sign-up methods. That is right as to the class as Rosa defined it. But within each web version the question is uniform. Every Version B customer saw the same page with no checkbox, and every Version A customer saw the same checkbox page, so whether that page produced "express affirmative consent" can be answered once for each. The phone channel, with changing scripts and partial recordings, yields no common answer.
- **Typicality.** The representative's claims must arise from the same course of conduct and legal theory as the class's. Rosa's Version B claim is typical of Version B customers. She is not typical of Version A or phone customers, whose claims turn on different facts. Her refund of one charge does not make her atypical: she still claims $250 for each of two unrefunded charges, and refunds go to damages, not to liability.
- **Adequacy.** Rosa has no apparent conflict with other customers. Brennan & Ochoa has class-action experience and can be appointed class counsel (Rule 23(g)). Adequacy is satisfied for the customers she can typically represent.

**B. Rule 23(b)(3): predominance and superiority.** Common questions must predominate over individual ones, and a class action must be superior to other methods.
- *Version B.* Liability turns on a uniform page, and damages are a fixed $250 multiplied by the number of charges shown in PantryBox's billing records. Common issues predominate.
- *Version A.* Whether a pre-checked or small-print checkbox satisfies the Act is a common question. PantryBox will argue that each customer's attention to the box is individual, but the statute asks what PantryBox obtained, which depends on the page's design, not each customer's state of mind. Predominance is likely met.
- *Phone.* Whether each representative read the terms, and whether each recording exists, must be resolved call by call. Individual issues predominate, so the phone customers should be excluded.
- *Superiority.* Each claim is worth a few hundred dollars, far too little to justify an individual suit. One class proceeding is efficient and manageable with PantryBox's own billing data.

**Subclasses.** A class may be divided into subclasses, each treated as a class (Rule 23(c)(5)). The court should certify a **Version B subclass** with Rosa as representative, and a **Version A subclass** only if a Version A customer is added as its representative (Rosa's claim is not typical of it). It should exclude phone customers. Each member must have Article III standing to recover damages (*TransUnion*); being charged $79 without consent is a concrete monetary injury.

**C. Rule 23(b)(2) and notice.** A (b)(2) class is proper when the defendant acted on grounds generally applicable to the class, so that a single injunction is appropriate for the class as a whole. A uniform injunction requiring a clear, unchecked consent box fits (b)(2). But individualized monetary relief such as $250 per charge cannot be pursued under (b)(2) (*Dukes*); it requires (b)(3). For the (b)(3) damages subclasses, Rosa must give the best notice practicable, including individual notice to members identifiable through reasonable effort (here, by email to the addresses PantryBox holds), with the right to opt out, and she must bear the cost (*Eisen*). A certification order may be appealed by permission if a petition is filed within 14 days (Rule 23(f)).

**Conclusion:** deny certification of the class as defined. Certify a (b)(3) Version B damages subclass, a Version A subclass if an adequate representative is added, and a (b)(2) injunction class; exclude phone customers.

### 2. Discovery

**A. Motion to compel.** Parties may obtain discovery of any nonprivileged matter relevant to a claim or defense and proportional to the needs of the case, considering the importance of the issues, the amount in controversy, the parties' relative access to information and resources, the importance of the discovery, and whether the burden outweighs the likely benefit (Rule 26(b)(1)).
- *Request 1 (all sign-up materials since 2014).* The class period is 2024–2025. Ten earlier years of page designs are of marginal relevance and impose a heavy burden. PantryBox's overbreadth objection is largely valid, and the court should limit the request to the class period, perhaps with some lead-up time (when the 2024 pages were designed).
- *Request 2 (A/B test results).* These go to the heart of the case: they show how PantryBox designed the consent pages and why. The amount at stake (potentially tens of millions of dollars in statutory damages) and PantryBox's exclusive control of the data weigh heavily toward production. "Confidential business information" is not a privilege. The proper response is a protective order limiting use and disclosure (Rule 26(c)(1)), not a refusal to produce.
- *Procedure and expenses.* Rosa certified good-faith efforts to confer, as Rule 37(a)(1) requires. When a motion to compel is granted, the court **must** award the movant's reasonable expenses, including attorney's fees, unless the opposing position was substantially justified or an award would be unjust (Rule 37(a)(5)). PantryBox's overbreadth objection to Request 1 was justified, but its flat refusal on Request 2 was not.

**Conclusion:** grant the motion as to Request 2 and as to Request 1 limited to the relevant period, under a protective order; award Rosa expenses at least for the Request 2 portion. This is essentially what the court did.

**B. Sanctions for violating the order.** If a party fails to obey a discovery order, the court may issue just orders, including directing that designated facts be taken as established, prohibiting the party from supporting or opposing designated claims or defenses, striking pleadings, dismissing, or entering a default judgment. It must also order the disobedient party to pay the reasonable expenses caused by the failure unless it was substantially justified (Rule 37(b)(2)). Severe sanctions such as default require willfulness, bad faith or fault, consideration of lesser sanctions, and a relationship between the sanction and the misconduct (*NHL v. Metropolitan Hockey Club*).
- *Violation.* The order required production of the 2024–2025 testing data. The February 2024 spreadsheet ("Checkbox default = ON") is squarely within it, and PantryBox did not produce it.
- *Willfulness.* PantryBox calls it "an oversight." Rosa will point out that the one document withheld was the single most damaging one: it suggests PantryBox tested and adopted a pre-checked box because it boosted conversions. That it surfaced only through a former engineer supports an inference of deliberate suppression. A court could reasonably find willfulness.
- *Choosing a sanction.* Default judgment would end the case for all claims, including Version B claims that the spreadsheet does not affect, so it is likely disproportionate. A sanction tied to the misconduct is more appropriate: an order **taking as established that the Version A checkbox was pre-checked by default**, or precluding PantryBox from offering evidence that it was unchecked. Either relates directly to the suppressed document and cures the prejudice. The court must also award Rosa the expenses caused by the violation.

**Conclusion:** deny default judgment; grant the alternative issue-related sanction (or at least preclusion), plus expenses.

### 3. Summary judgment against the Version A subclass

The court shall grant summary judgment if there is no genuine dispute as to any material fact and the movant is entitled to judgment as a matter of law (Rule 56(a)). A fact is material if it might affect the outcome; a dispute is genuine if a reasonable jury could find for the non-movant. The court views the evidence in the light most favorable to the non-movant and does not weigh credibility (*Anderson v. Liberty Lobby*). A movant that does not bear the burden of proof may discharge its initial burden by negating an element or by showing the non-movant lacks evidence. The non-movant must then cite particular record materials, in admissible form, showing a genuine dispute (*Celotex*; Rule 56(c)).

- *PantryBox's showing.* The subclass bears the burden of proving that consent was not obtained. PantryBox's engineer's declaration and archived screenshots, if believed, show a customer had to check an unchecked box, which supports consent. PantryBox has carried its initial burden.
- *Material fact.* Whether the box was pre-checked is material: a customer who merely failed to uncheck a pre-checked box arguably gave no "affirmative" consent, while one who checked it herself arguably did. The small gray type also bears on whether any consent was "express."
- *Genuine dispute.* Rosa offers (1) three customers' sworn declarations, based on personal knowledge, that the box was already checked; (2) the "default = ON" spreadsheet; and (3) expert evidence about the type. A reasonable jury could credit this evidence over PantryBox's engineer. Choosing between them is a credibility determination for the jury. If the court imposed the issue-establishing sanction in Part 2, the pre-checked default is established, and summary judgment is even more clearly improper.
- *Counsel's declaration.* Declarations must be made on personal knowledge and set out admissible facts (Rule 56(c)(4)). Rosa's lawyer's "information and belief" assertion about confused customers must be disregarded, but Rosa does not need it.
- *As a matter of law?* PantryBox argues that checking a box is consent as a matter of law. That argument assumes its version of the disputed fact. Whether a pre-checked, faintly printed box satisfies the Act cannot be decided for PantryBox on this record.

**Conclusion:** deny summary judgment.

### 4. Jury trial

**A. Right to a jury.** The Seventh Amendment preserves the right to a jury in suits at common law, determined claim by claim by comparing the action to 18th-century actions and, more importantly, by asking whether the remedy sought is legal or equitable. The right extends to new statutory causes of action that seek legal relief (*Curtis v. Loether*; *Terry*).
- *Statutory damages.* A claim for money damages for a statutory wrong is analogous to a common-law action for damages, and money damages are the classic legal remedy (*Curtis*). The $250-per-charge award is legal.
- *PantryBox's "penalty" argument.* Even for civil penalties, the jury decides liability; only the *amount* of a discretionary penalty may be left to the judge (*Tull*). Here the Act fixes the amount at $250 per charge, so there is nothing discretionary to assign to the judge, and the jury right on liability is unaffected.
- *Injunction.* Injunctive relief is equitable and is decided by the judge.

**B. Order of trial.** When legal and equitable claims share common factual issues, the jury must decide the legal claims and the common issues first, so that the judge's ruling on the equitable claim does not preclude the jury's determination (*Beacon Theatres*; *Dairy Queen*). Whether PantryBox obtained express affirmative consent through each web version is common to both the damages and the injunction claims. The jury decides those issues first, and the judge then decides the injunction consistent with the verdict. Rosa preserved the right by demanding a jury in her complaint (Rule 38(b)). A party cannot lose the jury right by labeling the case "fundamentally equitable" or by the sequence of trial.

**Conclusion:** deny the motion to strike. The class is entitled to a jury on liability and damages, tried first; the judge decides the injunction afterward.

## Self-Grading Rubric

| Issue | Points | Full credit requires | Rule IDs |
|---|---|---|---|
| Rule 23(a) | 16 | Each prerequisite applied; *Dukes* commonality tested channel by channel; typicality limited to Version B; refund goes to damages; adequacy including 23(g) counsel | R-CIV-059 |
| Rule 23(b)(3); subclasses | 14 | Predominance by channel (phone fails); superiority with small claims; 23(c)(5) subclasses and need for a Version A representative; *TransUnion* standing noted | R-CIV-060, R-CIV-061 |
| (b)(2); notice | 8 | Uniform injunction fits (b)(2); *Dukes* bars individual damages under (b)(2); (b)(3) individual notice, opt-out, plaintiff pays (*Eisen*); 23(f) | R-CIV-060 |
| Motion to compel | 14 | 26(b)(1) relevance and proportionality factors applied to both requests; confidentiality handled by 26(c) protective order; meet-and-confer; mandatory 37(a)(5) expenses with the substantial-justification exception | R-CIV-064, R-CIV-072, R-CIV-073 |
| Sanctions | 14 | Violation of an order; 37(b)(2)(A) menu; willfulness argued both ways; default disproportionate (Version B unaffected); issue-related sanction; mandatory expenses | R-CIV-073 |
| Summary judgment | 18 | Standard; *Celotex* burden shifting with the consumer's burden; materiality of the pre-checked box; genuine dispute from declarations, spreadsheet and expert; credibility for the jury; counsel's information-and-belief declaration disregarded; interaction with the sanction | R-CIV-085, R-CIV-086 |
| Seventh Amendment | 10 | Historical analogue plus remedy; statutory damages legal (*Curtis*); *Tull* answer to the penalty argument; injunction equitable | R-CIV-078 |
| Order of trial | 6 | Common issues to the jury first (*Beacon Theatres*); timely demand in the complaint | R-CIV-079, R-CIV-080 |

**Scoring on the 40–100 scale** (`00-exam-intel/grader-expectations.md` §4).
- **75+:** certification analyzed channel by channel with subclasses and the (b)(2)/(b)(3) split; discovery answer distinguishes the motion to compel (proportionality, protective order, mandatory fees) from Rule 37(b) sanctions (graduated, willfulness for default); summary judgment applies *Celotex* and identifies the credibility dispute; jury answer uses *Curtis*, *Tull* and *Beacon Theatres*.
- **65–70:** right outcomes with one call thin, e.g., no subclasses, or no *Tull* response.
- **55–60:** certifies the whole class without addressing the phone channel, or grants summary judgment by weighing the engineer's declaration against the customers'.
- **45–50:** confuses Rule 11 with discovery sanctions, or says injunction claims eliminate the jury right.

**Common mistakes**
1. Treating "did each customer consent?" as automatically individual. The statute focuses on what the seller obtained, so a uniform page produces a common answer; only the varying phone scripts do not.
2. Certifying damages under (b)(2). *Dukes* forbids individualized monetary relief in a (b)(2) class.
3. Treating "confidential" as a privilege. Confidential business information is produced under a protective order.
4. Jumping to default judgment. Terminating sanctions require willfulness and consideration of lesser, issue-related sanctions.
5. Letting the judge decide the injunction first on the common consent issue, contrary to *Beacon Theatres*.

**Accuracy notes.** The "Act" is a stated assumption, so no particular federal consumer statute's text is in issue. The *Tull* point is limited to its holding (jury on liability; judge may set the amount of a discretionary civil penalty); the answer does not need to decide whether a court could ever set fixed statutory damages. Rule 23(c)(5) (subclasses) and Rule 56(c)(4) (declarations on personal knowledge) are current rule text.
