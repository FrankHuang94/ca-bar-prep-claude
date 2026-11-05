---
subject: foundations
topic: Common-law reasoning for a PRC civil-law-trained lawyer — mindset, law vs equity, the jury, two-sided analysis, habits to fix, PRC→US concept map
coverage_ids: []
tested_on: [MBE, essay, PT]
exam_frequency: {level: n/a, basis: "Foundations reference"}
last_verified: 2026-11-05
status: reviewed
---

# Common law for civil lawyers

**Who this is for.** You were trained to reason from a code: find the article, match the facts and state the result. That skill is real and transfers. Precise reading of rules matters on every part of this exam. But California graders reward a different *shape* of reasoning. This file names the differences so you can practise them deliberately.

Read with [us-legal-system.md](us-legal-system.md) (sources and precedent) and [grader-expectations.md](../00-exam-intel/grader-expectations.md) (what graders say they reward).

---

## 1. The mindset shift

| Dimension | PRC code-based reasoning (三段论, statute-first deduction) | Common-law reasoning (what the bar rewards) |
|---|---|---|
| Starting point | The applicable code article is the major premise | The **issue** raised by the facts; the rule is then assembled from cases, statutes and Restatements |
| Where the rule comes from | Enacted text, plus judicial interpretations | Often **synthesized from several decisions**; statutes are read through the cases construing them |
| How rules are phrased | Abstract and general (总则 → 分则) | Element lists with exceptions, and many **open standards** ("reasonable", "material", "substantial", "foreseeable") |
| Role of facts | Minor premise: classify the facts under the article | **The facts decide the case.** The same rule produces opposite results on slightly different facts, and you must show which facts matter and why. |
| Competing rules | Usually one governing article | Several plausible rules (majority/minority, common law/UCC, federal/California). Name the one that applies and why. |
| Uncertainty | The court resolves it and states the answer | **Argue both sides**, then conclude. A reasoned "likely" conclusion is the normal ending. |
| Judicial opinion style | Court's findings and conclusion (本院认为) | Reasons, precedent, analogy, distinction, and often a dissent |
| Your role on the exam | Neutral adjudicator | Lawyer predicting how a court would rule after hearing both sides |

> 🇨🇳 PRC bridge: think of the essay as a 代理词 for *both* sides followed by a short 判决理由. Graders award points mainly for the two advocacy sections (approx.).

---

## 2. The five moves of common-law reasoning

### 2.1 Rule synthesis
- Cases rarely announce the full rule. You build it.
  - *Case A:* a shop owner who ignored a spill for 3 hours was liable.
  - *Case B:* an owner whose employee mopped within 5 minutes was not liable.
  - *Synthesized rule:* an owner breaches the duty to invitees by failing to discover and remedy a dangerous condition it knew of or **should have discovered by reasonable inspection**.
- The PT library tests this directly (see `04-performance-test/method.md`, Phase 2).

### 2.2 Analogy and distinction
- Compare your facts to the precedent's **outcome-determinative facts**.
- "Like the owner in Case A, who left the spill unattended for hours, D left the oil on the floor for two hours, so D had constructive notice."
- Or distinguish: "Unlike Case A, the spill here occurred moments before the fall."

### 2.3 Multiple competing rules
- Expect to state which rule governs.
  - Sale of goods → UCC Article 2; services or land → common law.
  - MBE torts default → pure comparative fault [S-040].
  - Evidence essay → FRE and/or CEC as the call directs [S-083].
- One sentence on *why* that rule applies earns credit.

### 2.4 Fact sensitivity
- Standards ("reasonable person", "material breach", "substantial factor") are decided case by case, usually by a jury.
- Your job is to **use every relevant fact** and say what inference it supports: "Because the sign was posted only at the far entrance, a reasonable jury could find the warning inadequate."

### 2.5 Adversarial framing
- Each issue has a plaintiff's best argument and a defendant's best response.
- The grader wants to see that you can make both, then pick the better one with a reason.

**Worked contrast: the same facts written two ways**
- **Facts:** a customer slips on cooking oil in a grocery aisle. The oil had been there about two hours. The customer was reading her phone while walking.

| PRC-style (scores poorly) | Bar-style IRAC (scores well) |
|---|---|
| "The store had fault under tort law and is liable. The customer was also at fault, so damages are reduced." | **Negligence: duty.** A possessor of land owes invitees a duty of reasonable care, including reasonable inspection. The customer entered to shop, so she is an invitee. **Breach.** The store must discover and remedy dangers it should discover by reasonable inspection. The customer will argue that two hours is ample time for an inspection to find a spill, which gives the store constructive notice. The store will respond that it inspects hourly and the spill may have been recent; nothing shows employees saw it. Given two hours and a busy aisle, a jury would likely find constructive notice and breach. **Causation and damages:** ... **Defense: comparative negligence.** The store will argue she was not watching where she walked. Under pure comparative fault her recovery is reduced by her percentage of fault, not barred. **Conclusion:** the store is likely liable, with damages reduced for her share of fault. |

---

## 3. Law and equity

English law developed two court systems: the **common-law courts**, which awarded money damages, and the **Court of Chancery**, which gave relief "in equity" when the common-law remedy was inadequate. US courts merged them procedurally: "There is one form of action—the civil action" (Fed. R. Civ. P. 2); California likewise has "but one form of civil actions" (Code Civ. Proc. § 307). **The distinction still decides five things on the exam:**

| Question | Law | Equity |
|---|---|---|
| Typical remedies | Compensatory and punitive damages, restitution at law, replevin, ejectment | Injunction, specific performance, rescission, reformation, constructive trust, equitable lien, accounting |
| Threshold | Available as of right once liability is shown | Requires an **inadequate legal remedy** (e.g., land or unique goods, irreparable harm) and is **discretionary** (balancing hardships, feasibility of enforcement) |
| Jury | Jury right for legal claims (federal: U.S. Const. amend. VII, "Suits at common law") | No jury right; the judge decides |
| Defenses | Statute of limitations, etc. | **Laches** (unreasonable delay causing prejudice), **unclean hands**, plus legal defenses |
| Property concepts | Legal title | **Equitable title**: the trust exists because equity enforces the trustee's obligation to beneficiaries; also equitable servitudes and equitable conversion |

Remedies essays are built on this table. See [Remedies](../03-subjects/remedies/README.md).

> 🇨🇳 PRC bridge: PRC law has no law/equity split. 继续履行 is an ordinary statutory remedy, while US specific performance is an exceptional equitable one (approx.).

---

## 4. The jury and why it shapes doctrine

| Source | Right |
|---|---|
| U.S. Const. amend. VI | Criminal jury trial; a guilty verdict for a serious offense must be unanimous (*Ramos v. Louisiana* (2020)) |
| U.S. Const. amend. VII | Civil jury in federal "Suits at common law" where the value in controversy exceeds twenty dollars. Binds federal courts only. |
| Cal. Const. art. I, § 16 | California jury right; in a civil cause three-fourths of the jury may render a verdict |

**Division of labour:** the **judge** decides questions of law and admissibility, and instructs the jury. The **jury** finds facts and applies open standards to them.

**Why this matters to you:**
1. **Evidence law exists largely because of juries.** It filters what lay fact-finders hear, e.g., hearsay, character evidence and FRE 403 balancing.
2. **Procedure is built around jury control.** Summary judgment, judgment as a matter of law and new-trial motions all ask whether a *reasonable jury* could find for a party.
3. **Essay phrasing.** Close fact questions are "for the jury". Write "a reasonable jury could find ..." and then say which way it would *likely* go.

> 🇨🇳 PRC bridge: 人民陪审员 sit with professional judges and decide together. A US jury deliberates alone and returns a verdict the judge generally must accept (approx.).

---

## 5. How bar examiners reward two-sided analysis

The State Bar's own instructions ask you to show you can "discern the points of law and fact upon which the case turns". A bare conclusion earns "little or no credit" [S-076]. Two-sided analysis is how you show *where the case turns*.

**When to argue both sides**
- **Do it** when a fact can be read two ways, an element is genuinely disputed, or the law splits (majority/minority; FRE/CEC).
- **Don't** manufacture a dispute for an element the facts clearly satisfy. Write "Element X is satisfied because [fact]" in one line and move on.

**Sentence frames**
- "P will argue that ___ because [fact]. D will respond that ___ because [fact]. The better argument is ___ because ___."
- "Although [fact cutting against], [fact cutting for] is more significant because ___. Therefore ___ is likely satisfied."
- "If the court finds ___, then ___; if not, ___." Use this for facts the question leaves open, and keep it short.
- "Under the majority rule ___; California, however, ___. Under either rule, the result here is ___."

**Conclude every issue.** "Likely", "probably" and "a court would likely find" are normal and expected. Hedging without a conclusion is not.

---

## 6. Ten habits that cost civil-law-trained candidates points, and the fix

| # | Habit | Why it costs points | Fix |
|---|---|---|---|
| 1 | **Code-first deduction**: "Under § X, the contract is void." | A conclusion with no application earns little credit [S-076]. | Rule → **these facts** → "because" → conclusion. Quote or paraphrase specific facts in every paragraph. |
| 2 | **Judgment voice**: stating only the winning view | Graders look for the dispute; a one-sided answer hides it. | Use the P-argues / D-responds frame on every contested element (§5). |
| 3 | **Hunting for the one governing article** | US problems usually have several possible claims, defenses and rule sets. | Before writing, list every claim and defense within the call, then decide which deserve full IRAC. |
| 4 | **Skipping "obvious" elements** | Points are often allocated per element. | One line per undisputed element; full analysis only where disputed. |
| 5 | **Treatise-length rule recitals** (all articles, all exceptions) | Time is spent where few points are. | A 1–3 sentence rule from `rule-statements.md`, then application. Add exceptions only when the facts raise them. |
| 6 | **Importing PRC solutions**: court adjusts the 违约金, renegotiates under 情势变更, 定金 doubled | These are not US rules and read as legal error. | Learn the US rule first; use the bridge table below **only as a memory hook**. |
| 7 | **Ignoring parties, posture and remedy** | Calls are framed as "What claims may P bring against D, and what remedies?" | For every issue, ask: who v. whom, what claim, what defense, what remedy. Organize headings that way. |
| 8 | **Organizing by code structure instead of by the call** | The grader cannot find your answer to each call. | Headings mirror the call: Call 1 → claims → issues. Threshold issues (jurisdiction, standing, formation) come first. |
| 9 | **Treating facts as fixed and complete** | Many points come from **inferences** ("she left within an hour, suggesting ...") and from spotting ambiguity. | Ask of each fact: why did the examiner include this? Nearly every fact is there to be used. |
| 10 | **Hedging English and passive voice** | Slow to read, and graders read fast. | Short sentences, active verbs, and the legal term of art (see [legal-english-glossary.md](legal-english-glossary.md)). Spelling and grammar are not graded [S-010], but clarity is. |

---

## 7. PRC → US concept map

> **⚠ All rows are approximate bridges.** A bridge is a memory hook only. It is never the rule. On the exam, write the US/California rule from the subject's `rule-statements.md`. PRC article references are to the PRC Civil Code (民法典, 2020) unless another statute is named. All PRC references are pending a check against the official text [VERIFY V-040]; a Phase 7 spot check confirmed art. 533 (情势变更) against a Supreme People's Court commentary [S-1305].

| PRC concept (中文) | Closest US concept | Key difference (what to unlearn) | Where tested |
|---|---|---|---|
| Codified law as the primary source (民法典) | Common law + statutes; Restatements as persuasive | US case law is primary law. Many contract, tort and property rules have no statute at all. | All |
| 指导性案例 (SPC guiding cases) | Binding precedent (stare decisis) | Every published US appellate holding binds lower courts in its hierarchy, not just selected cases | Essays, PT |
| 三段论 (statute → facts → conclusion) | IRAC (Issue, Rule, Application, Conclusion) | The "A" must be two-sided and fact-specific | Essays, PT |
| 要约 / 承诺 (arts. 472, 479) | Offer / acceptance (Restatement (Second) of Contracts §§ 24, 50) | Mailbox rule: acceptance is generally effective on **dispatch** (§ 63); the PRC generally uses arrival. Common-law mirror-image rule vs UCC § 2-207. | MBE, essay (CTR) |
| Certain offers irrevocable by law | Offers freely revocable unless: option (supported by consideration), merchant's firm offer (UCC § 2-205), reliance (§ 87(2)) | The US default is revocable until accepted | MBE, essay (CTR) |
| No consideration requirement (contract = agreement) | **Consideration**: a bargained-for exchange (§ 71) | A gratuitous promise is unenforceable without consideration or a substitute (§ 90). Modification needs consideration at common law (pre-existing duty rule) but not under UCC § 2-209(1). | MBE, essay (CTR) |
| 赠与 revocable before transfer (art. 658) | Gift: requires intent, **delivery**, acceptance; a promise to give is generally unenforceable | Delivery completes the gift; no general revocation right afterwards | CTR, PRP, WIL |
| 缔约过失责任 (art. 500) | Promissory estoppel (§ 90; § 87(2); *Drennan v. Star Paving Co.* (1958) 51 Cal.2d 409) | No general US duty to negotiate in good faith. Pre-contract recovery usually requires a **promise** relied on. | CTR essays |
| 诚信原则 (art. 7) | Implied covenant of good faith and fair dealing (§ 205; UCC § 1-304) | The US covenant governs **performance and enforcement** of an existing contract; it is not a free-standing general clause. | CTR |
| Form freedom (art. 469) | **Statute of frauds** (UCC § 2-201; Civ. Code § 1624) | Listed contracts (land, > 1 year, goods ≥ $500, suretyship, marriage, executors) need a signed writing or an exception | MBE, essay (CTR) |
| 违约金, court may adjust (art. 585) | Liquidated damages vs **penalty** (§ 356; UCC § 2-718(1); Civ. Code § 1671) | A US court does **not** adjust the amount. A clause is enforced as written or struck as a penalty, and the claimant then proves actual damages. | CTR, REM |
| 定金 (arts. 586–588) | Earnest-money deposit, usually analysed as liquidated damages; breaching buyer's restitution (UCC § 2-718(2)) | No double-return rule (定金罚则) | CTR, REM |
| 情势变更 (art. 533) | Impracticability (§ 261; UCC § 2-615); frustration of purpose (§ 265) | Narrow **discharge** doctrines; a US court will not renegotiate or rewrite the contract | MBE, essay (CTR) |
| 不可抗力 (arts. 180, 590) | Force-majeure **clause** (contractual) + impossibility / impracticability | No statutory force-majeure defense at common law; a clause is read by its own terms | CTR |
| 继续履行 as a primary remedy (arts. 577, 580) | **Specific performance**: equitable, only if damages are inadequate (land, unique goods; UCC § 2-716) | Money damages are the default | CTR, REM |
| 可得利益 + foreseeability limit (art. 584) | Expectation damages; *Hadley v. Baxendale* foreseeability; mitigation; certainty | Similar core. The US adds strict certainty for lost profits and allows no punitive damages for breach of contract. | CTR, REM |
| 法定解除 (art. 563) | Material breach; anticipatory repudiation; UCC perfect tender (§ 2-601) with cure | The termination right turns on **materiality** (common law) or perfect tender (UCC) | MBE, essay (CTR) |
| 表见代理 (art. 172) | Apparent authority (Restatement (Third) of Agency § 2.03) | Based on the **principal's** manifestation to the third party | BUS |
| 法人人格否认 (Company Law) | Piercing the corporate veil | Equitable and fact-intensive (alter ego, undercapitalization, fraud); no fixed statutory list | BUS |
| 股东代表诉讼 (Company Law) | Shareholder **derivative suit** (demand or futility; Corp. Code § 800) | Procedural preconditions (demand, contemporaneous ownership, bond) are the tested points | BUS |
| 董监高 忠实 / 勤勉 义务 (Company Law) | Duty of **loyalty** and duty of **care**; business judgment rule | The BJR presumption protects informed, good-faith decisions; conflicts go to loyalty and safe harbors | BUS |
| 善意取得 (art. 311) | Bona fide purchaser; UCC § 2-403 (voidable title; entrustment to a merchant) | A **thief** passes no title even to a good-faith buyer; a voidable title can pass | CTR (UCC), PRP |
| Registration makes real rights effective (art. 209) | Deed **delivery** transfers title; **recording acts** (race / notice / race-notice) protect later BFPs | An unrecorded deed is valid between the parties | MBE, essay (PRP) |
| 土地所有权 vs 建设用地使用权 (land state- or collectively owned) | **Fee simple absolute** and the other estates; future interests | Private freehold ownership of land; estates and future interests, incl. the Rule Against Perpetuities | MBE, essay (PRP) |
| 居住权 (art. 366) | Life estate; lease; license | A life estate is a freehold, with waste duties and future interests following it | PRP |
| 地役权 (art. 372) | Easement: express, implied, by necessity, by prescription | US easements also arise **without agreement** (implication, prescription) | MBE, essay (PRP) |
| 抵押权 | Mortgage; **deed of trust** (common in California) | Foreclosure, priority and recording rules; purchase-money rules | MBE, essay (PRP) |
| 过错责任 (art. 1165) | **Negligence** (duty, breach, actual and proximate cause, damages) + separate **intentional torts** | No general tort clause; each tort has its own elements | MBE, essay (TRT) |
| 过错推定 (art. 1165, ¶ 2) | *Res ipsa loquitur* | In most US jurisdictions a permissible **inference** of negligence, not a shift of the burden | MBE, essay (TRT) |
| 无过错责任 (art. 1166); 高度危险作业 (art. 1236) | Strict liability: abnormally dangerous activities (Restatement (Second) of Torts §§ 519–520), wild animals | Narrow, judge-made categories | MBE, essay (TRT) |
| 产品责任 (art. 1202) | Strict products liability (Restatement (Second) of Torts § 402A; *Greenman v. Yuba Power Products, Inc.* (1963) 59 Cal.2d 57); negligence; warranty | Three defect types (manufacturing, design, warning) and multiple theories, each analysed separately | MBE, essay (TRT) |
| 用人单位责任 (art. 1191) | **Respondeat superior** (scope of employment) | Frolic vs detour; independent contractors generally excluded | TRT, BUS |
| 与有过失 (art. 1173) | Comparative negligence (pure is the MBE default [S-040]; California: *Li v. Yellow Cab Co.* (1975) 13 Cal.3d 804) vs contributory negligence | Several regimes exist (pure, modified, contributory); state which applies | MBE, essay (TRT) |
| 连带责任 (arts. 178, 1168) | Joint and several liability; contribution; California several liability for non-economic damages (Civ. Code § 1431.2) | The MBE default is joint and several [S-040] | MBE, essay (TRT) |
| 精神损害赔偿 (art. 1183) | IIED; NIED (bystander rules, e.g., *Thing v. La Chusa* (1989) 48 Cal.3d 644); pain and suffering as damages | Separate torts with strict elements and limits | MBE, essay (TRT) |
| 惩罚性赔偿 (only where a statute provides) | **Punitive damages** for malicious, oppressive or fraudulent torts (Civ. Code § 3294) | Generally available in tort; **never** for breach of contract alone | TRT, REM |
| 名誉权 | Defamation, constrained by the First Amendment (*New York Times Co. v. Sullivan*, 376 U.S. 254 (1964)) | Constitutional fault requirements (actual malice for public officials) | TRT, CON |
| 夫妻共同财产 (art. 1062) / 个人财产 (art. 1063); divorce division (art. 1087) | California **community property** (Fam. Code §§ 760, 770); equal division (§ 2550) | Presumptions, **tracing** and apportionment formulas; mandatory equal division of CP rather than judicial discretion | CMP |
| 夫妻财产约定 (art. 1065) | Premarital agreements; **transmutation** (Fam. Code § 852: express written declaration) | Strict writing rule for changing the character of property during marriage | CMP |
| 法定继承 (art. 1127; 遗嘱 prevails, art. 1123) | **Intestate succession** (Prob. Code §§ 6401, 6402); wills prevail | California: the spouse takes the decedent's half of CP; separate property is shared with issue or parents | WIL |
| 遗嘱形式; latest will prevails (art. 1142) | Attested and **holographic** wills (Prob. Code §§ 6110, 6111); revocation by later instrument or physical act (§ 6120) | Witness rules, harmless error (§ 6110(c)(2)), and revocation doctrines such as dependent relative revocation | WIL |
| 必留份 (art. 1141) | No forced heirship; omitted spouse and child statutes (Prob. Code §§ 21610, 21620); CP protects the spouse | A testator may disinherit children if intentional | WIL |
| 信托法 (PRC Trust Law) | Express trusts: trustee holds **legal** title, beneficiaries hold **equitable** title; fiduciary duties | Rooted in equity. California trusts are revocable unless expressly irrevocable (Prob. Code § 15400). | TRS |
| 管辖 (级别 / 地域) | Subject-matter jurisdiction + **personal jurisdiction** (due process) + venue | Personal jurisdiction is a **constitutional** limit tested every time | MBE, essay (CIV) |
| 既判力 | Claim preclusion (res judicata) and issue preclusion (collateral estoppel) | Non-mutual issue preclusion; California's primary-rights theory | MBE, essay (CIV) |
| 两审终审; 再审 | One appeal as of right from a **final judgment**; narrow post-judgment relief (Fed. R. Civ. P. 60(b)) | No general retrial or supervision of final judgments | CIV |
| 谁主张，谁举证 | Burden of production and burden of persuasion; standards: preponderance, clear and convincing, beyond a reasonable doubt | Allocation and standards are tested explicitly | EVD, CIV |
| Court-led evidence gathering | **Party-driven discovery** (Fed. R. Civ. P. 26; CCP discovery) | Broad pre-trial exchange; sanctions; privileges | CIV |
| Written witness statements (证人证言) | **Hearsay** rule; Confrontation Clause | Out-of-court statements offered for their truth are excluded unless an exception applies | MBE, essay (EVD) |
| 非法证据排除 (PRC Criminal Procedure Law) | **Exclusionary rule** (*Mapp v. Ohio*, 367 U.S. 643 (1961)); fruit of the poisonous tree; California Prop 8 | A remedy for constitutional violations, with exceptions (good faith, inevitable discovery, independent source, attenuation) | MBE, essay (CRM) |
| 人民陪审员 | **Jury** | Lay jurors decide facts alone (§4 above) | CIV, CRM, EVD |
| 罪刑法定 (PRC Criminal Law art. 3) | Principle of legality; statutory crimes; Model Penal Code | The MBE mixes common-law and MPC definitions; know both | MBE, essay (CRM) |
| 犯罪构成 | **Actus reus** + **mens rea** + causation + concurrence; then defenses | Mental-state hierarchy (purpose, knowledge, recklessness, negligence; specific vs general intent) | MBE, essay (CRM) |
| 共同犯罪 (主犯 / 从犯) | Accomplice liability; **conspiracy** as a separate crime (*Pinkerton v. United States*, 328 U.S. 640 (1946)) | Conspiracy does not merge with the completed offense | MBE, essay (CRM) |
| 律师法; 律师执业行为规范 | California Rules of Professional Conduct; B&P § 6068; ABA Model Rules | California's confidentiality duty is stricter, and the California and ABA rules differ in many places | PRF |
| Constitution not directly justiciable | **Judicial review** (*Marbury v. Madison*, 5 U.S. (1 Cranch) 137 (1803)); constitutional litigation | Courts strike down statutes, so standing, levels of scrutiny and state action are central | MBE, essay (CON) |
