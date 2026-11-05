---
subject: EVD
topic: Evidence — essay-ready rule statements (R-EVD-001 to R-EVD-115)
coverage_ids: [EVD-MBE-I, EVD-MBE-I.A, EVD-MBE-I.B, EVD-MBE-I.C, EVD-MBE-I.D, EVD-MBE-I.E, EVD-MBE-II, EVD-MBE-II.A, EVD-MBE-II.B, EVD-MBE-II.C, EVD-MBE-II.D, EVD-MBE-II.E, EVD-MBE-III, EVD-MBE-III.A, EVD-MBE-III.B, EVD-MBE-III.C, EVD-MBE-III.D, EVD-MBE-III.E, EVD-MBE-III.F, EVD-MBE-III.G, EVD-MBE-III.H, EVD-MBE-IV, EVD-MBE-IV.A, EVD-MBE-IV.B, EVD-MBE-IV.C, EVD-MBE-V, EVD-MBE-V.A, EVD-MBE-V.B, EVD-MBE-V.C, EVD-MBE-V.D, EVD-MBE-V.E, EVD-MBE-V.F, EVD-MBE-V.G, EVD-MBE-V.H, EVD-MBE-V.I, EVD-MBE-V.J, EVD-MBE-V.K, EVD-MBE-V.L, EVD-SUP-001, EVD-SUP-002, EVD-SUP-003, EVD-SUP-004, EVD-SUP-005, EVD-SUP-006, EVD-SUP-007, EVD-SUP-008, EVD-SUP-009]
tested_on: [MBE, essay]
exam_frequency: {level: high, basis: "Essays: 15 of 31 administrations 2012-02 to 2026-07 (48%); MBE: 25 scored questions every exam"}
last_verified: 2026-11-05
status: reviewed
---

# Evidence — rule statements

**How to use this file.** Each block gives a rule you can write verbatim on an essay, then its elements, exceptions, authority, the MBE/California split and a short example. `build_anki.py` turns the **Rule (write this)** paragraphs into cards. Order follows [`outline.md`](outline.md).

**Abbreviations.** **FRE** = Federal Rules of Evidence (as in effect July 2027). **CEC** or **§** = California Evidence Code. **Truth-in-Evidence** = Cal. Const. art. I, § 28(f)(2) (Proposition 8, 1982) [S-145].

**Essay default.** The call names the governing law: "under the Federal Rules of Evidence" or "under the California Evidence Code" / "California law". Write the named law; where the other system differs and the call says "compare" or the difference is material, add one sentence. The MBE uses the FRE only [S-040]. All differences are in [`ca-distinctions.md`](ca-distinctions.md).

---

## Framework

### R-EVD-001 — Governing law and the item-by-item method
**Rule (write this):** Evidence must be relevant, not excluded by discretionary balancing, offered by a competent witness in proper form, authenticated, compliant with the best (or secondary) evidence rule, and free of policy exclusions, privileges and hearsay objections; in a criminal case it must also satisfy the Confrontation Clause. Each item is analyzed separately under the law the call names.

**Elements:** For each item: 1. Logical relevance. 2. Legal relevance (FRE 403 / § 352). 3. Specific exclusionary rules (character, policy, privilege). 4. Witness issues (competency, personal knowledge, opinion, form). 5. Writings (authentication, BER / secondary evidence). 6. Hearsay (definition → exclusion → exception; each layer). 7. Confrontation (criminal, testimonial). 8. Limiting instruction.

**Exceptions / defenses:** In a California criminal case, Truth-in-Evidence makes relevant evidence admissible except under listed rules (R-EVD-004).

**Authority:** FRE 101, 402; CEC §§ 300, 350–351; State Bar Evidence essay outline (FRE and CEC, compare and contrast) [S-083]; NCBE MBE outline (FRE "as currently in effect") [S-040].

**MBE vs. CA essay:** MBE: FRE only. Essay: the law named in the call (CEC on about half of recent essays: Feb 2016, Jul 2018, Feb 2020, Feb 2024, Feb 2025 retest, Jul 2026; FRE on Feb 2012, Jul 2014, Feb 2017, Feb 2019, Feb 2023) [VERIFY V-071].

**Example:** "Should the court admit the 911 recording under the California Evidence Code?" Heading "1. 911 recording", then relevance → § 352 → hearsay (§ 1240) → confrontation → authentication → limiting instruction.

### R-EVD-002 — Logical relevance
**Rule (write this):** Evidence is relevant if it has any tendency to make a fact of consequence more or less probable than it would be without the evidence. Relevant evidence is admissible unless a constitution, statute or rule excludes it; irrelevant evidence is never admissible.

**Elements:** 1. Probative: any tendency (a low threshold). 2. Material: the fact matters under the substantive law or to credibility.

**Exceptions / defenses:** Excluded by FRE 403 / § 352, by specific rules (character, policy, privilege, hearsay) and by constitutional rules.

**Authority:** FRE 401, 402; CEC §§ 210 (relevance includes credibility of a witness or hearsay declarant; fact must be "disputed"), 350, 351.

**MBE vs. CA essay:** Same rule. CEC § 210 requires the fact to be **disputed**, so evidence on a conceded point can be irrelevant in California.

**Example:** In a negligence case, testimony that the defendant was texting seconds before the crash makes careless driving more probable — relevant.

### R-EVD-003 — Legal relevance: discretionary exclusion (FRE 403 / § 352)
**Rule (write this):** The court may exclude relevant evidence if its probative value is substantially outweighed by the danger of unfair prejudice, confusing the issues, misleading the jury, undue delay, wasting time, or needlessly presenting cumulative evidence. The balance favors admission.

**Elements:** 1. Measure probative value (how strongly it proves a contested point; need; alternatives). 2. Identify the specific danger (unfair prejudice = tendency to decide on an improper, usually emotional, basis). 3. Ask whether danger **substantially** outweighs value. 4. Consider a limiting instruction or stipulation as a lesser remedy.

**Exceptions / defenses:** Not available against a 609(a)(2) dishonesty conviction; modified balances in 609(a)(1)(B), 609(b), 412(b)(2), 703 and 107. *Old Chief v. United States*, 519 U.S. 172 (1997): where the only purpose is felon status, rejecting the defendant's stipulation was an abuse of discretion.

**Authority:** FRE 403; CEC § 352 (undue consumption of time; substantial danger of undue prejudice, confusing the issues, or misleading the jury); § 352.2 (creative expression) [S-116].

**MBE vs. CA essay:** Same test in substance. In a California criminal case, § 352 is one of the few grounds that survive Truth-in-Evidence, so it does most of the excluding work.

**Example:** Ten autopsy photographs when the cause of death is conceded: modest probative value, substantial emotional prejudice — likely limited to one or two.

### R-EVD-004 — Truth-in-Evidence (Proposition 8)
**Rule (write this):** In California criminal proceedings, relevant evidence shall not be excluded, except under statutes enacted after June 1982 by a two-thirds vote of each house, existing statutory rules of privilege and hearsay, and Evidence Code §§ 352, 782 and 1103. Prior felony convictions may be used without limitation for impeachment, subject to due process and § 352.

**Elements:** 1. Criminal proceeding (including pretrial and post-conviction hearings and juvenile criminal cases). 2. Evidence is relevant. 3. No surviving exclusionary rule applies: hearsay, privilege, § 352, § 782, § 1103, a post-1982 two-thirds statute (e.g., § 1101 as re-enacted in 1986, *People v. Ewoldt* (1994) 7 Cal.4th 380 [S-505]), or a federal constitutional rule.

**Exceptions / defenses:** Does not apply in civil cases. Cannot override federal constitutional exclusion (Fourth Amendment, Confrontation Clause, Miranda): California excludes only where federal law requires (*In re Lance W.* (1985) 37 Cal.3d 873). Which other statutes were re-enacted by two-thirds vote is case-specific [VERIFY V-412].

**Authority:** Cal. Const. art. I, § 28(f)(2), (f)(4) [S-145]; *People v. Castro* (1985) 38 Cal.3d 301; *People v. Wheeler* (1992) 4 Cal.4th 284 [S-502].

**MBE vs. CA essay:** No MBE equivalent. On every CEC criminal essay, write one paragraph: "Because this is a criminal case, Proposition 8 admits all relevant evidence unless an exception applies; here [rule] is/is not preserved."

**Example:** A prosecution witness once shoplifted (misdemeanor conduct of moral turpitude). § 787 would bar specific-act impeachment, but Truth-in-Evidence lets the defense prove the conduct, subject to § 352.

> 🇨🇳 PRC bridge: loosely like the PRC principle that all lawfully obtained material relevant to the facts may be used as evidence (approx.), but Prop 8 operates as a constitutional override of statutory exclusionary rules.

### R-EVD-005 — Preliminary questions decided by the judge
**Rule (write this):** The court decides preliminary questions about whether a witness is qualified, a privilege exists, or evidence is admissible, by a preponderance of the evidence; in doing so it is not bound by the rules of evidence except those on privilege.

**Elements:** Judge questions: hearsay foundations (excitement, business duty, unavailability, conspiracy), privilege elements, expert qualification and reliability, competency, BER excuses.

**Exceptions / defenses:** Hearings on the admissibility of a confession, hearings at which a criminal defendant testifies on a preliminary question and so requests, and other hearings where justice requires are held outside the jury (FRE 104(c)); the opponent may still attack weight before the jury (104(e)).

**Authority:** FRE 104(a), (c)–(e); *Bourjaily v. United States*, 483 U.S. 171 (1987); CEC § 405.

**MBE vs. CA essay:** Same allocation. California courts generally apply the Evidence Code itself when finding preliminary facts [VERIFY V-409].

**Example:** To admit a coconspirator's statement, the judge must consider the statement itself (FRE 801(d)(2), last sentence) together with independent evidence and must find the conspiracy more likely than not.

### R-EVD-006 — Conditional relevance (jury questions)
**Rule (write this):** When the relevance of evidence depends on whether a fact exists, the court admits it if the proponent introduces evidence sufficient to support a finding that the fact exists; the jury then decides whether it does.

**Elements:** Jury-type facts: authenticity, personal knowledge, identity of a speaker or writer, receipt of a letter, commission of a prior act offered under 404(b).

**Exceptions / defenses:** Evidence may be admitted on the condition that proof will be introduced later ("connecting up").

**Authority:** FRE 104(b); *Huddleston v. United States*, 485 U.S. 681 (1988); CEC § 403.

**MBE vs. CA essay:** Same rule.

**Example:** A letter signed "J. Doe" is relevant only if Doe wrote it; testimony from Doe's secretary that she recognizes his signature is enough for the jury to decide.

### R-EVD-007 — Limited admissibility and limiting instructions
**Rule (write this):** If evidence is admissible for one purpose or against one party but not for another, the court, on timely request, must restrict the evidence to its proper scope and instruct the jury accordingly.

**Elements:** 1. Evidence has a proper and an improper use. 2. Timely request. 3. Instruction (or exclusion under 403 if an instruction cannot cure the danger).

**Exceptions / defenses:** Instructions cannot cure a nontestifying codefendant's facially incriminating confession (*Bruton v. United States*, 391 U.S. 123 (1968)).

**Authority:** FRE 105; CEC § 355.

**MBE vs. CA essay:** Same rule. End every essay item that is admitted for a limited purpose with this sentence.

**Example:** A prior act admitted only to show intent: "On request, the court should instruct the jury to consider it only on intent, not as proof of character."

### R-EVD-008 — Objections, motions to strike and offers of proof
**Rule (write this):** A party may claim error in admitting evidence only if it made a timely objection or motion to strike stating the specific ground, unless apparent from context, and in excluding evidence only if it made an offer of proof, unless the substance was apparent; the error must affect a substantial right.

**Elements:** 1. Timely (as soon as the ground is apparent). 2. Specific ground. 3. Ruling on the record. 4. Offer of proof for exclusions. 5. Prejudice.

**Exceptions / defenses:** Definitive pretrial rulings need not be renewed (FRE 103(b)); plain error (103(e)). A testifying defendant must testify to preserve a 609 ruling (*Luce v. United States*, 469 U.S. 38 (1984)); one who introduces his own conviction waives the objection (*Ohler v. United States*, 529 U.S. 753 (2000)).

**Authority:** FRE 103; CEC §§ 353, 354; Cal. Const. art. VI, § 13 (miscarriage of justice) [S-146].

**MBE vs. CA essay:** Same structure.

**Example:** Defense counsel says only "objection" to a hearsay answer; the court overrules. The ground was apparent from context, so the error is likely preserved; an objection on the wrong ground would not be.

## I. Presentation of evidence

### R-EVD-009 — Personal knowledge
**Rule (write this):** A lay witness may testify to a matter only if evidence is introduced sufficient to support a finding that the witness has personal knowledge of it, which may consist of the witness's own testimony.

**Elements:** 1. The witness perceived the matter through the senses. 2. Evidence sufficient for a jury to so find (104(b)).

**Exceptions / defenses:** Experts may rely on facts they did not perceive (FRE 703). Party-opponent statements need no personal knowledge.

**Authority:** FRE 602; CEC §§ 702, 403(a)(2).

**MBE vs. CA essay:** Same rule.

**Example:** A neighbor who "heard from her husband" that the defendant's dog bit the child lacks personal knowledge of the bite.

### R-EVD-010 — Competency of witnesses
**Rule (write this):** Every person is competent to be a witness unless a rule provides otherwise; a witness must have personal knowledge and take an oath or affirmation to testify truthfully. In federal civil cases, state competency law governs claims for which state law supplies the rule of decision.

**Elements:** 1. Capacity to perceive, remember and communicate. 2. Understanding of the duty to tell the truth. 3. Oath or affirmation (FRE 603). 4. Personal knowledge.

**Exceptions / defenses:** State Dead Man's statutes apply in diversity cases through FRE 601; California has none; instead § 1261 admits a decedent's own statement in an action on a claim or demand against the decedent's estate [VERIFY V-409]. Hypnotically refreshed testimony: § 795 conditions [VERIFY V-416]; a per se ban on the defendant's own is unconstitutional (*Rock v. Arkansas*, 483 U.S. 44 (1987)).

**Authority:** FRE 601–603; CEC §§ 700, 701 (disqualified if incapable of expressing himself so as to be understood, or of understanding the duty to tell the truth), 710.

**MBE vs. CA essay:** Same in substance; California keeps two express disqualification grounds (§ 701).

**Example:** A five-year-old who can describe events and promises to tell the truth is competent; her age goes to weight.

### R-EVD-011 — Judges and jurors as witnesses; impeaching a verdict
**Rule (write this):** The presiding judge may not testify, and a juror may not testify before the other jurors. On an inquiry into a verdict's validity, a juror may not testify about deliberations or mental processes, except about extraneous prejudicial information, an outside influence, or a mistake on the verdict form.

**Elements:** Internal matters (votes, reasoning, intoxication, misunderstanding) excluded; external matters (outside research, bribes, threats, media) admissible.

**Exceptions / defenses:** A juror's clear statement relying on racial stereotypes or animus to convict must be considered (*Peña-Rodriguez v. Colorado*, 580 U.S. 206 (2017)). Intoxication is internal (*Tanner v. United States*, 483 U.S. 107 (1987)).

**Authority:** FRE 605, 606; CEC §§ 703, 704, 1150.

**MBE vs. CA essay:** § 1150 admits evidence of statements, conduct, conditions or events likely to have influenced the verdict improperly (overt acts, including statements in deliberations), but not their effect on mental processes — somewhat broader than FRE 606(b). Under §§ 703–704 the presiding judge or a sitting juror may testify only if no party objects; an objection requires a mistrial, whereas FRE 605 bars the judge's testimony outright [VERIFY V-991].

**Example:** A juror looked up the defendant's prior arrests online and told the others; jurors may testify to that extraneous information.

### R-EVD-012 — Refreshing recollection
**Rule (write this):** A witness whose memory fails may use any writing or object to refresh it and then testify from revived memory; the item is not evidence. The adverse party may inspect a writing used to refresh, cross-examine on it, and introduce relevant portions.

**Elements:** 1. Witness lacks memory. 2. Item shown. 3. Memory revived; testimony from memory, not reading. 4. Production on demand.

**Exceptions / defenses:** FRE: production is mandatory for writings used while testifying; discretionary ("if justice requires") for writings used before testifying. Jencks Act governs government witness statements in criminal cases.

**Authority:** FRE 612; CEC § 771 [S-521].

**MBE vs. CA essay:** Differs. Under § 771, production is mandatory whether the writing was used **before or while** testifying, and testimony is **stricken** if it is not produced (unless the writing is unavailable to the proponent).

**Example:** An officer reads his report the night before trial. Federal court: production only if the judge finds justice requires; California: the defense is entitled to it or the testimony on that subject is stricken.

### R-EVD-013 — Lay opinion
**Rule (write this):** A lay witness may give an opinion only if it is rationally based on the witness's perception, helpful to clearly understanding the testimony or determining a fact in issue, and not based on scientific, technical or other specialized knowledge.

**Elements:** 1. Perception. 2. Helpfulness (not merely telling the jury what to decide). 3. No specialized knowledge.

**Exceptions / defenses:** Common permitted opinions: speed, intoxication, emotion, identity, handwriting or voice familiarity, sanity of an acquaintance, owner's value of own property. Excluded: legal conclusions, opinions on credibility, speculation about another's knowledge.

**Authority:** FRE 701; CEC § 800.

**MBE vs. CA essay:** Same in substance; § 800 has no express third prong, but § 801 handles specialized matters.

**Example:** "The driver was weaving and slurring; he was drunk" — admissible lay opinion. "The crash was caused by a brake defect" — needs an expert.

### R-EVD-014 — Judicial notice
**Rule (write this):** A court may take judicial notice of an adjudicative fact that is not subject to reasonable dispute because it is generally known within the court's territorial jurisdiction or can be accurately and readily determined from sources whose accuracy cannot reasonably be questioned. In a civil case the jury must accept the fact as conclusive; in a criminal case the jury may, but need not, accept it.

**Elements:** 1. Adjudicative fact. 2. Indisputable (general knowledge or verifiable). 3. On the court's motion or on request with information (mandatory then). 4. Opportunity to be heard. 5. Any stage.

**Exceptions / defenses:** Legislative facts and law are outside FRE 201.

**Authority:** FRE 201; CEC §§ 451 (mandatory), 452 (permissive), 453 (mandatory on request), 457 (instruction) [S-522].

**MBE vs. CA essay:** California also notices law and lists categories; whether it follows the FRE 201(f) criminal-case instruction is unconfirmed [VERIFY V-403].

**Example:** That July 4, 2026 fell on a Saturday can be noticed from a calendar.

### R-EVD-015 — Civil presumptions and burdens
**Rule (write this):** In a federal civil case, a presumption shifts to the opposing party only the burden of producing evidence to rebut it; the burden of persuasion stays with the party who had it. In California, presumptions affecting the burden of producing evidence work the same way, but presumptions that implement public policy shift the burden of proof.

**Elements:** 1. Basic fact proved. 2. Presumed fact follows. 3. Rebuttal evidence sufficient to support a contrary finding → FRE/§ 604 presumption disappears (inference may remain); § 606 presumption → opponent must disprove.

**Exceptions / defenses:** In diversity cases, state law governs presumptions on state-law claims (FRE 302).

**Authority:** FRE 301, 302; CEC §§ 115, 500, 600–606, 641 (mailed letter received), 662 (legal title — clear and convincing to rebut).

**MBE vs. CA essay:** Differs for public-policy presumptions (§ 606).

**Example:** Plaintiff proves a letter was properly mailed; defendant testifies it never arrived. Under FRE 301 the presumption bursts and the jury weighs the evidence.

### R-EVD-016 — Presumptions in criminal cases
**Rule (write this):** A mandatory presumption that relieves the prosecution of proving an element beyond a reasonable doubt, or shifts the burden of persuasion to the defendant, violates due process; a permissive inference is valid if, on the facts, the inferred fact more likely than not flows from the proved fact.

**Elements:** 1. Characterize the instruction (mandatory vs. permissive) as a reasonable juror would. 2. Mandatory burden-shifting → unconstitutional. 3. Permissive → rational-connection test.

**Exceptions / defenses:** Affirmative defenses (e.g., insanity) may be placed on the defendant where they are not elements.

**Authority:** *In re Winship*, 397 U.S. 358 (1970); *Sandstrom v. Montana*, 442 U.S. 510 (1979); *County Court of Ulster County v. Allen*, 442 U.S. 140 (1979).

**MBE vs. CA essay:** Same (federal due process).

**Example:** "The law presumes a person intends the ordinary consequences of his voluntary acts" in a murder case is an unconstitutional mandatory presumption.

### R-EVD-017 — Court control of examination
**Rule (write this):** The court exercises reasonable control over the mode and order of examining witnesses and presenting evidence so as to make them effective for determining the truth, avoid wasting time, and protect witnesses from harassment or undue embarrassment.

**Elements:** Order of trial; recalling witnesses; limiting repetitive or abusive questioning; court may call and question witnesses (FRE 614).

**Exceptions / defenses:** Must not curtail cross-examination on bias in a criminal case (Confrontation Clause, *Davis v. Alaska*, 415 U.S. 308 (1974)).

**Authority:** FRE 611(a), 614; CEC §§ 765, 772, 775, 778.

**MBE vs. CA essay:** Same.

**Example:** The court stops counsel from asking a sexual-assault complainant the same humiliating question a fifth time.

### R-EVD-018 — Scope of cross-examination
**Rule (write this):** Cross-examination should not go beyond the subject matter of the direct examination and matters affecting the witness's credibility, though the court may allow inquiry into additional matters as if on direct.

**Elements:** 1. Within the subject matter of direct (read broadly). 2. Or credibility. 3. Otherwise the cross-examiner must call the witness in its own case (or the court permits, without leading).

**Exceptions / defenses:** A testifying criminal defendant may be crossed on matters within the scope of direct; he does not waive the privilege for unrelated crimes.

**Authority:** FRE 611(b); CEC §§ 761, 773.

**MBE vs. CA essay:** Same.

**Example:** A witness who testified only about the color of the light may not be crossed about the plaintiff's medical bills.

### R-EVD-019 — Leading questions
**Rule (write this):** Leading questions should not be used on direct examination except as necessary to develop the witness's testimony; they are ordinarily permitted on cross-examination and when a party calls a hostile witness, an adverse party, or a witness identified with an adverse party.

**Elements:** 1. Does the question suggest the answer? 2. Which examination? 3. Any exception (preliminary matters, children, forgetful witness, hostile/adverse witness)?

**Exceptions / defenses:** Court discretion; "friendly" cross (an adverse party's own employee crossed by its counsel) may be restricted.

**Authority:** FRE 611(c); CEC §§ 764, 767, 776.

**MBE vs. CA essay:** Same.

**Example:** On direct, "You saw the defendant run the red light, didn't you?" is leading; "What color was the light?" is not.

### R-EVD-020 — Objectionable form of questions
**Rule (write this):** Questions are objectionable if they are compound, argumentative, assume facts not in evidence, call for speculation or a narrative, have been asked and answered, mislead, or harass; an answer that does not respond to the question may be stricken on motion.

**Elements:** Identify the defect; object immediately; ask to strike any answer.

**Exceptions / defenses:** Court discretion under FRE 611(a); narrative answers may be allowed for clarity. At common law only the examining party may move to strike a nonresponsive answer.

**Authority:** FRE 611(a); CEC §§ 765, 766, 767.

**MBE vs. CA essay:** Same, except that § 766 lets **any** party move to strike a nonresponsive answer.

**Example:** "When did you stop overbilling the client?" assumes a fact not in evidence.

### R-EVD-021 — Exclusion of witnesses
**Rule (write this):** At a party's request the court must order witnesses excluded so they cannot hear other testimony, and may also order excluded witnesses not to learn of or access trial testimony; it may not exclude a party who is a natural person, an entity party's designated representative, a person essential to the presentation of a party's case, or a person authorized by statute to be present.

**Elements:** 1. Request (or court's motion). 2. Exemptions. 3. Optional order against disclosure or access (2023).

**Exceptions / defenses:** Crime victims under federal and California law.

**Authority:** FRE 615 (as amended Dec. 1, 2023) [S-104] [VERIFY V-415]; CEC § 777; Cal. Const. art. I, § 28(b) [S-145].

**MBE vs. CA essay:** Same in substance.

**Example:** The plaintiff's damages expert may remain to hear the plaintiff's testimony because the expert's presence is essential to forming an opinion.

### R-EVD-022 — Impeachment: who may impeach; the collateral-matter limit
**Rule (write this):** Any party, including the party that called the witness, may attack the witness's credibility. Extrinsic evidence may be used to impeach on bias, prior convictions, capacity and non-collateral inconsistencies or contradictions, but not on collateral matters or specific instances of untruthfulness.

**Elements:** Methods: bias/interest; inconsistent statements; convictions; character for untruthfulness; sensory or mental defects; contradiction. Religious beliefs may not be used (FRE 610; § 789).

**Exceptions / defenses:** A party may not call a witness solely as a pretext to place inadmissible hearsay before the jury (largely moot under amended 801(d)(1)(A) [S-101] and § 1235).

**Authority:** FRE 607, 608, 610; CEC §§ 780, 785, 786, 789.

**MBE vs. CA essay:** Same principle; California's § 780 lists the credibility factors and has no fixed collateral-matter bar — § 352 controls extrinsic impeachment on collateral points (R-EVD-033).

**Example:** A party whose own witness unexpectedly changes his story may impeach him with his earlier statement.

### R-EVD-023 — Prior inconsistent statements: impeachment and extrinsic proof
**Rule (write this):** A witness may be impeached with a prior statement inconsistent with the trial testimony, without first showing it to the witness. Under FRE 613(b) as amended in 2024, extrinsic evidence of the statement is admissible only after the witness has had an opportunity to explain or deny it and the adverse party an opportunity to examine on it, unless the court orders otherwise, and only if the matter is not collateral.

**Elements:** 1. Inconsistency (contradiction, material omission, feigned forgetfulness). 2. Good-faith basis. 3. Disclosure to opposing counsel on request. 4. Foundation before extrinsic evidence. 5. Not collateral.

**Exceptions / defenses:** The foundation rule does not apply to an opposing party's statement under 801(d)(2). Post-Miranda silence cannot be used (*Doyle v. Ohio*, 426 U.S. 610 (1976)); pre-arrest silence can (*Jenkins v. Anderson*, 447 U.S. 231 (1980)); voluntary Miranda-defective statements can (*Harris v. New York*, 401 U.S. 222 (1971)).

**Authority:** FRE 613 [S-105]; CEC §§ 769, 770, 1235.

**MBE vs. CA essay:** Differs on timing: § 770 admits extrinsic evidence if the witness was given an opportunity to explain or deny **or** has not been excused from further testimony (foundation may follow). Substantive use: see R-EVD-085.

**Example:** A witness testifies the light was red; he told a friend it was green. Counsel must ask him about it before calling the friend under amended FRE 613(b); in California, counsel may call the friend first if the witness remains subject to recall.

### R-EVD-024 — Bias, interest and motive
**Rule (write this):** A witness may be impeached by evidence of bias, interest or motive to testify falsely; because bias is not a collateral matter, it may be shown on cross-examination and, subject to FRE 403 and the court's control, by extrinsic evidence.

**Elements:** 1. Relationship, payment, deal, hostility, litigation interest, organizational loyalty. 2. Most courts require a foundation question before extrinsic proof.

**Exceptions / defenses:** 403 limits; in a criminal case, undue restriction of bias cross can violate confrontation (*Davis v. Alaska*, 415 U.S. 308 (1974)).

**Authority:** *United States v. Abel*, 469 U.S. 45 (1984); FRE 611; CEC § 780(f).

**MBE vs. CA essay:** Same.

**Example:** A prosecution witness testifies under a plea deal reducing his sentence; the deal is admissible to show motive to favor the government.

### R-EVD-025 — Impeachment by prior conviction (FRE 609)
**Rule (write this):** A witness's conviction for a crime punishable by more than one year is admissible to impeach, subject to Rule 403 for ordinary witnesses and, for a criminal defendant, only if its probative value outweighs its prejudicial effect to the defendant. A conviction for any crime whose elements required proving (or the witness's admitting) a dishonest act or false statement must be admitted. Convictions more than ten years old require that probative value substantially outweigh prejudicial effect and written notice.

**Elements:** 1. Felony or crimen falsi. 2. The right balancing test for the witness. 3. Ten years from conviction or release, whichever is later. 4. No pardon based on rehabilitation or innocence. 5. Juvenile adjudications only against non-defendant witnesses in criminal cases.

**Exceptions / defenses:** Pending appeal does not bar use. Only name, date and sentence come in unless the witness opens the door. The 2026 proposed amendment to 609 was withdrawn [S-106].

**Authority:** FRE 609; *Luce v. United States*, 469 U.S. 38 (1984).

**MBE vs. CA essay:** Differs — California uses moral turpitude (R-EVD-026).

**Example:** A testifying defendant charged with robbery has a four-year-old robbery felony: high similarity weighs toward exclusion under 609(a)(1)(B). His six-year-old misdemeanor conviction for filing a false police report must be admitted under 609(a)(2).

### R-EVD-026 — Impeachment by prior conviction and moral turpitude (California)
**Rule (write this):** In a California criminal case, a witness may be impeached with any prior felony conviction involving moral turpitude — a readiness to do evil, judged by the least adjudicated elements — subject to the court's discretion under § 352; misdemeanor conduct involving moral turpitude may also be shown. In civil cases, § 788 permits impeachment by felony convictions, subject to § 352.

**Elements:** Criminal: 1. Felony conviction (art. I, § 28(f)(4)) or misdemeanor conduct (Wheeler). 2. Moral turpitude (theft, fraud, violence with intent to injure; not simple possession). 3. § 352 factors: bearing on honesty, remoteness, similarity to the charged offense, effect on the defendant's decision to testify. Civil: 1. Felony. 2. § 352.

**Exceptions / defenses:** *Wheeler* held that the record of a misdemeanor conviction is hearsay when offered to prove the conduct, so the conduct must be proved by admissible evidence; a certified conviction record may now qualify under § 452.5(b) [VERIFY V-409]. In civil cases art. I, § 28(f) and the criminal-case rulings do not apply; the court must still weigh the conviction under § 352, and the criminal moral-turpitude cases serve only as guidelines (*Robbins v. Wong* (1994) 27 Cal.App.4th 261, 273–274) [S-504] [S-1553].

**Authority:** Cal. Const. art. I, § 28(f)(4) [S-145]; CEC §§ 352, 788; *People v. Castro* (1985) 38 Cal.3d 301; *People v. Wheeler* (1992) 4 Cal.4th 284 [S-502]; *Robbins v. Wong* (1994) 27 Cal.App.4th 261 [S-504] [S-1553].

**MBE vs. CA essay:** MBE: FRE 609. CA essay: moral turpitude + § 352, misdemeanor conduct allowed in criminal cases.

**Example:** A defendant's prior felony forgery conviction (dishonesty = moral turpitude) is admissible to impeach him under California law, subject to § 352; it would also be automatically admissible under FRE 609(a)(2).

### R-EVD-027 — Specific instances of untruthful conduct (FRE 608(b))
**Rule (write this):** Except for criminal convictions, extrinsic evidence is not admissible to prove specific instances of a witness's conduct in order to attack or support the witness's character for truthfulness, but the court may allow inquiry on cross-examination into instances probative of truthfulness or untruthfulness.

**Elements:** 1. Conduct probative of (un)truthfulness. 2. Good-faith basis. 3. Asked on cross. 4. Examiner takes the answer.

**Exceptions / defenses:** The bar applies only to character-for-truthfulness use; extrinsic evidence offered to show bias or contradict a material fact is allowed.

**Authority:** FRE 608(b).

**MBE vs. CA essay:** Differs (R-EVD-028).

**Example:** Counsel may ask, "Didn't you falsely claim a law degree on your résumé?" If the witness denies it, counsel cannot introduce the résumé.

### R-EVD-028 — Specific instances of conduct (California)
**Rule (write this):** In California civil cases, specific instances of conduct are inadmissible to attack or support a witness's credibility, even on cross-examination. In criminal cases, Truth-in-Evidence supersedes that bar, so prior conduct involving moral turpitude is admissible to impeach, subject to § 352.

**Elements:** Criminal: 1. Conduct shows moral turpitude. 2. Relevant to credibility. 3. § 352 (time, confusion, mini-trials).

**Exceptions / defenses:** § 352 often excludes minor or remote conduct; hearsay rules still govern how the conduct is proved.

**Authority:** CEC §§ 787, 352; Cal. Const. art. I, § 28(f)(2) [S-145]; *People v. Wheeler* (1992) 4 Cal.4th 284 [S-502].

**MBE vs. CA essay:** Differs from FRE 608(b): broader in criminal cases (extrinsic proof possible), narrower in civil cases (no inquiry at all).

**Example:** In a California assault prosecution, the defense may prove a prosecution witness's earlier insurance fraud through another witness, subject to § 352.

### R-EVD-029 — Character for truthfulness: opinion and reputation
**Rule (write this):** A witness's credibility may be attacked or supported by reputation or opinion testimony about the witness's character for truthfulness, but evidence of truthful character is admissible only after the witness's character for truthfulness has been attacked.

**Elements:** 1. Only the trait of truthfulness. 2. Foundation: knowledge of reputation in a relevant community, or acquaintance sufficient for an opinion. 3. Support only after attack (not after mere contradiction or bias).

**Exceptions / defenses:** The character witness may be asked on cross about specific instances (608(b)(2)).

**Authority:** FRE 608(a); CEC §§ 786, 790.

**MBE vs. CA essay:** Same.

**Example:** After the defense calls a witness who says the victim is "a known liar", the prosecution may call a witness who says the victim is honest.

### R-EVD-030 — Capacity to observe, remember or relate
**Rule (write this):** A witness may be impeached by evidence of a defect in the capacity to perceive, remember or communicate, such as poor eyesight, intoxication at the time of the event, or a mental condition affecting reliability, and extrinsic evidence is allowed.

**Elements:** 1. Defect existed at the time of perception or testimony. 2. Logically affects reliability. 3. 403 / § 352.

**Exceptions / defenses:** Mental-health history that does not bear on reliability is excluded as prejudicial.

**Authority:** FRE 401, 403, 607; CEC § 780(c).

**MBE vs. CA essay:** Same.

**Example:** An eyewitness was not wearing her prescribed glasses at night 60 feet away; her optometrist may testify.

### R-EVD-031 — Impeaching a hearsay declarant
**Rule (write this):** When a hearsay statement or a statement of an agent, authorized speaker or coconspirator has been admitted, the declarant's credibility may be attacked, and then supported, by any evidence that would be admissible if the declarant had testified, and the declarant's inconsistent statements may be used without giving an opportunity to explain or deny.

**Elements:** 1. Hearsay admitted. 2. Impeachment method that would be allowed for a live witness. 3. No foundation needed for inconsistent statements.

**Exceptions / defenses:** The party against whom the statement was admitted may call the declarant and examine as on cross.

**Authority:** FRE 806; CEC §§ 1202, 1203.

**MBE vs. CA essay:** Same.

**Example:** The prosecution admits the victim's excited utterance naming the defendant; the defense may show the victim's prior fraud conviction and an earlier statement naming someone else.

### R-EVD-032 — Rehabilitation
**Rule (write this):** An impeached witness may be rehabilitated by explanation on redirect, by evidence of good character for truthfulness after an attack on that character, and by a prior consistent statement offered to rebut a charge of recent fabrication or improper motive (made before the motive arose) or, under the FRE, to rehabilitate after an attack on another ground.

**Elements:** 1. Prior impeachment. 2. Responsive rehabilitation. 3. For consistent statements: timing (pre-motive) and declarant testifies and is subject to cross.

**Exceptions / defenses:** No bolstering of an unimpeached witness.

**Authority:** FRE 608(a), 801(d)(1)(B); *Tome v. United States*, 513 U.S. 150 (1995); CEC §§ 790, 791, 1236.

**MBE vs. CA essay:** § 791 admits consistent statements only (a) after an inconsistent statement, if made before it, or (b) to rebut a charge of recent fabrication, bias or improper motive, if made before it arose — no FRE "other ground" door.

**Example:** Defense claims the victim invented the accusation after a custody dispute began; her identical statement to a teacher before the dispute is admissible.

### R-EVD-033 — Contradiction
**Rule (write this):** A witness may be impeached by evidence that facts in the testimony are untrue; cross-examination is always allowed, but extrinsic contradiction is allowed only on matters that are not collateral.

**Elements:** 1. Specific testimony. 2. Contradicting evidence. 3. Non-collateral: relevant to a substantive issue or independently admissible to impeach.

**Exceptions / defenses:** A witness who opens the door with a sweeping claim may be contradicted with evidence that would otherwise be excluded. A **testifying defendant** may even be contradicted with illegally obtained evidence (*Walder v. United States*, 347 U.S. 62 (1954); *United States v. Havens*, 446 U.S. 620 (1980)), but that impeachment exception does not extend to other defense witnesses (*James v. Illinois*, 493 U.S. 307 (1990)).

**Authority:** FRE 403, 607, 611(a); CEC §§ 351, 352, 780(i); *People v. Lavergne* (1971) 4 Cal.3d 735, 742 [S-1557].

**MBE vs. CA essay:** Differs. California has no automatic collateral-matter rule: contradiction on a collateral point is relevant to credibility (§ 780(i)) and admissible unless excluded under § 352, where its collateral character lowers its probative value (*Lavergne*) [S-1557]. In criminal cases Truth-in-Evidence points the same way.

**Example:** A witness says she saw the crash on her way to church; proof that she was actually at work that morning is collateral unless it shows she could not have seen the crash. FRE: extrinsic proof excluded. California: no automatic bar; the court weighs it under § 352 and may exclude it as time-consuming with little probative value.

### R-EVD-034 — Proceedings where the rules apply
**Rule (write this):** The Federal Rules of Evidence apply in civil and criminal trials but, except for privileges, not to the court's preliminary-fact findings, grand juries, sentencing, probation and supervised-release revocation, extradition, preliminary examinations, warrants or bail.

**Elements:** 1. Type of proceeding. 2. Privileges always apply.

**Exceptions / defenses:** Constitutional rights may still require reliability in some proceedings.

**Authority:** FRE 101, 1101; CEC § 300; Pen. Code § 872(b) (officer hearsay at preliminary hearings) [VERIFY V-406].

**MBE vs. CA essay:** California applies the Code in every action unless a statute provides otherwise; Truth-in-Evidence covers pretrial and post-conviction criminal hearings.

**Example:** At a federal sentencing hearing, a probation officer's report containing hearsay may be considered.

## II. Relevancy, character, authentication and experts

### R-EVD-035 — Character evidence: the propensity ban
**Rule (write this):** Evidence of a person's character or character trait is not admissible to prove that on a particular occasion the person acted in accordance with that character, because the inference invites decision on an improper basis.

**Elements:** 1. Identify the purpose: character in issue, propensity, impeachment, or a non-character purpose. 2. If propensity, apply the ban and its exceptions (R-EVD-037, 038, 043, 044).

**Exceptions / defenses:** Criminal "mercy rule" (accused's and victim's traits); sexual-offense propensity (FRE 413–415; § 1108); domestic-violence propensity (§ 1109); character in issue; impeachment (607–609).

**Authority:** FRE 404(a)(1); CEC § 1101(a); *People v. Ewoldt* (1994) 7 Cal.4th 380 (§ 1101 survives Prop 8 through its 1986 re-enactment) [S-505].

**MBE vs. CA essay:** Same ban. In California criminal cases, mention that § 1101 survives Truth-in-Evidence.

**Example:** In a civil battery suit, the plaintiff may not prove the defendant's violent reputation to show he probably struck first.

> 🇨🇳 PRC bridge: PRC procedure has no categorical character-evidence ban; prior bad acts are weighed by the court (approx.). US law excludes them from the jury as a rule, not a weight question.

### R-EVD-036 — Character in issue
**Rule (write this):** When a person's character or trait is an essential element of a charge, claim or defense, it may be proved by reputation, opinion or specific instances of conduct.

**Elements:** Character itself must be what the substantive law makes decisive: defamation (truth of a character statement), negligent hiring or entrustment, child custody, entrapment (predisposition).

**Exceptions / defenses:** If character is offered only circumstantially, it is not "in issue".

**Authority:** FRE 405(b); CEC § 1100.

**MBE vs. CA essay:** Same.

**Example:** In a negligent-entrustment suit, the owner's knowledge of the driver's three prior DUI convictions may be proved by the convictions themselves.

### R-EVD-037 — The accused's own character (mercy rule)
**Rule (write this):** A criminal defendant may offer evidence of his own pertinent character trait to show he did not commit the crime, and if he does, the prosecution may rebut it; under the FRE and § 1102 the evidence must be reputation or opinion, and the prosecution may cross-examine the character witness about relevant specific acts.

**Elements:** 1. Criminal case. 2. Defendant opens the door. 3. Pertinent trait (honesty for fraud, peacefulness for assault, law-abidingness generally). 4. Reputation or opinion only.

**Exceptions / defenses:** The prosecution cannot initiate. Rebuttal may include "have you heard/did you know" questions (R-EVD-040) and its own reputation or opinion witnesses.

**Authority:** FRE 404(a)(2)(A), 405(a); CEC § 1102.

**MBE vs. CA essay:** Same.

**Example:** An embezzlement defendant calls a coworker who testifies he has a reputation for honesty; the prosecutor may ask whether the coworker heard he was fired for padding expenses.

### R-EVD-038 — The victim's character (self-defense)
**Rule (write this):** A criminal defendant may offer evidence of the alleged victim's pertinent trait, such as violence, to show the victim acted in conformity; the prosecution may then rebut it and offer evidence of the defendant's same trait. In a homicide case under the FRE, the prosecution may offer evidence of the victim's peacefulness to rebut any evidence that the victim was the first aggressor.

**Elements:** 1. Criminal case. 2. Pertinent victim trait. 3. Method: FRE — reputation or opinion; CEC § 1103(a) — opinion, reputation **or specific instances**. 4. Door-opening consequences.

**Exceptions / defenses:** Rape shield bars sexual-character evidence (FRE 412; § 1103(c)). Evidence of the victim's violent acts known to the defendant is admissible on his reasonable fear, not as character.

**Authority:** FRE 404(a)(2)(B)–(C), 405(a); CEC § 1103(a)–(b).

**MBE vs. CA essay:** Differs: California admits specific instances of the victim's character and, after defense evidence of the victim's violence, specific instances of the defendant's violence (§ 1103(b)); no codified first-aggressor rule.

**Example:** Claiming self-defense, D calls a witness who says V has a violent reputation. Under the FRE the prosecution may now prove D's violent reputation; under § 1103(b) it may also prove D's specific past assaults.

### R-EVD-039 — Methods of proving character
**Rule (write this):** When character evidence is admissible, it may be proved by reputation or opinion testimony; specific instances of conduct are allowed only when character is an essential element or on cross-examination of a character witness.

**Elements:** Reputation (community) or opinion (personal acquaintance); specific instances only in R-EVD-036 or R-EVD-040 settings.

**Exceptions / defenses:** California permits specific instances for the victim's character and the defendant's violent character (§ 1103) and generally under § 1100 where character is admissible.

**Authority:** FRE 405; CEC §§ 1100, 1102, 1103.

**MBE vs. CA essay:** Differs as noted.

**Example:** A defense witness may say "In my opinion D is peaceful" but may not describe D's charity work on direct to prove peacefulness.

### R-EVD-040 — Cross-examining a character witness
**Rule (write this):** A character witness may be asked on cross-examination whether she has heard of, or knows about, specific relevant acts of the person, including arrests, to test her knowledge and standards, if the examiner has a good-faith basis; extrinsic proof of the acts is not allowed.

**Elements:** 1. Witness testified to character. 2. Act relevant to the trait. 3. Good-faith basis. 4. Limiting instruction.

**Exceptions / defenses:** 403 limits remote or highly inflammatory questions.

**Authority:** FRE 405(a); *Michelson v. United States*, 335 U.S. 469 (1948).

**MBE vs. CA essay:** Same.

**Example:** "Have you heard that the defendant was arrested for assault last year?" may be asked of a witness who testified to his peaceful reputation.

### R-EVD-041 — Habit and routine practice
**Rule (write this):** Evidence of a person's habit or an organization's routine practice may be admitted to prove that on a particular occasion the person or organization acted in accordance with it, with or without corroboration or an eyewitness.

**Elements:** 1. Specific, repeated, semi-automatic response to a recurring situation. 2. Sufficient number of instances. 3. Not a general disposition (that is character).

**Exceptions / defenses:** Intentional or moral conduct (violence, honesty) is rarely habit. § 1104 excludes a trait of care or skill to prove the quality of conduct.

**Authority:** FRE 406; CEC §§ 1104, 1105.

**MBE vs. CA essay:** Same.

**Example:** A secretary testifies the office stamps and mails every letter placed in the out-tray by 5 p.m.; this routine practice proves the letter was mailed.

### R-EVD-042 — Other crimes, wrongs or acts
**Rule (write this):** Evidence of other crimes, wrongs or acts is inadmissible to prove character and conforming conduct, but may be admitted for another purpose, such as motive, opportunity, intent, preparation, plan, knowledge, identity, absence of mistake or lack of accident, if the jury could find the act occurred and its probative value is not substantially outweighed by unfair prejudice.

**Elements:** 1. Non-propensity purpose genuinely in dispute. 2. Relevance without a character inference. 3. Sufficient proof for a jury to find the act (104(b)) — acquittal no bar (*Dowling v. United States*, 493 U.S. 342 (1990)). 4. 403 / § 352. 5. Limiting instruction. 6. Criminal cases (FRE): reasonable written pretrial notice stating purpose and reasoning.

**Exceptions / defenses:** Identity requires a distinctive signature; intent requires the least similarity (*Ewoldt*). Acts that are part of the charged crime are not "other" acts.

**Authority:** FRE 404(b); *Huddleston v. United States*, 485 U.S. 681 (1988); CEC § 1101(b) (adds absence of good-faith belief in consent in sex-offense prosecutions); *People v. Ewoldt* (1994) 7 Cal.4th 380 [S-505].

**MBE vs. CA essay:** Same in substance; California uses Ewoldt's sliding scale of similarity and has no notice rule.

**Example:** D is charged with burglary of a home by drilling the lock and leaving a playing card; his two earlier burglaries with the same signature are admissible on identity.

### R-EVD-043 — Sexual-offense propensity (FRE 413–415; § 1108)
**Rule (write this):** In a case in which the defendant is accused of sexual assault or child molestation, evidence that he committed another sexual assault or child molestation is admissible and may be considered on any matter to which it is relevant, including propensity, subject to the court's discretion to exclude it as unduly prejudicial.

**Elements:** 1. Charged sexual offense. 2. Other sexual offense (conviction not needed). 3. Notice (FRE: 15 days before trial). 4. 403 / § 352: similarity, remoteness, frequency, intervening events, need, risk of confusion.

**Exceptions / defenses:** California applies only in criminal actions; the FRE also cover civil cases (FRE 415).

**Authority:** FRE 413, 414, 415; CEC § 1108; *People v. Falsetta* (1999) 21 Cal.4th 903 (upholding § 1108 because § 352 protects fairness).

**MBE vs. CA essay:** Same in criminal cases; California has no civil counterpart to FRE 415.

**Example:** In a rape prosecution, another woman's testimony that D sexually assaulted her two years earlier is admissible to show propensity, subject to balancing.

### R-EVD-044 — Domestic-violence propensity (§ 1109)
**Rule (write this):** In a California criminal action in which the defendant is accused of an offense involving domestic violence, evidence of the defendant's other acts of domestic violence is not made inadmissible by § 1101 if it survives § 352; acts more than ten years before the charged offense are inadmissible unless the court finds admission in the interest of justice.

**Elements:** 1. Criminal action. 2. Charged offense involving domestic violence. 3. Other DV acts. 4. § 352. 5. Ten-year limit. 6. Disclosure to the defense. "Domestic violence" takes its meaning from Pen. Code § 13700 (abuse against a spouse, former spouse, cohabitant, former cohabitant, a person with whom the suspect has had a child, or a person with whom the suspect is having or has had a dating or engagement relationship) [S-1828] and, subject to a § 352 hearing, for acts no more than five years before the charged offense, the broader Fam. Code § 6211 definition (§ 1109(d)(3)) [S-1550].

**Exceptions / defenses:** The section also admits other acts of elder or dependent-person abuse, and of child abuse, when the charged offense is of that kind; the ten-year limit (§ 1109(e)) applies to every category [S-1550].

**Authority:** CEC § 1109 [S-514] [S-1550].

**MBE vs. CA essay:** California only; no FRE counterpart (in federal court such acts come in only under 404(b)).

**Example:** In a California battery prosecution of D for hitting his live-in partner, his prior assault on an ex-girlfriend six years ago is admissible to show propensity, subject to § 352.

### R-EVD-045 — Rape shield (FRE 412)
**Rule (write this):** In a civil or criminal proceeding involving alleged sexual misconduct, evidence offered to prove that a victim engaged in other sexual behavior or to prove the victim's sexual predisposition is inadmissible, subject to narrow exceptions.

**Elements:** Criminal exceptions: specific instances to show another source of semen, injury or physical evidence; specific instances with the defendant offered on consent (or by the prosecutor); evidence whose exclusion would violate constitutional rights. Civil: admissible only if probative value substantially outweighs harm to the victim and unfair prejudice; reputation only if the victim placed it in controversy.

**Exceptions / defenses:** Procedure: written motion 14 days before trial, notice to victim, in camera hearing.

**Authority:** FRE 412.

**MBE vs. CA essay:** California uses §§ 1103(c), 782 and 1106 (R-EVD-046).

**Example:** D charged with rape offers evidence that the complainant had consensual sex with him the previous week, on consent — admissible under 412(b)(1)(B).

### R-EVD-046 — Rape shield (California)
**Rule (write this):** In California prosecutions for specified sex offenses, opinion, reputation and specific-instance evidence of the complaining witness's sexual conduct is inadmissible to prove consent, except conduct with the defendant; evidence of sexual conduct offered to attack the complainant's credibility is admissible only after a written motion, offer of proof, affidavit and hearing outside the jury, and subject to § 352.

**Elements:** 1. Purpose: consent (§ 1103(c)) vs. credibility (§ 782). 2. Prior conduct with the defendant excepted. 3. § 782 procedure. 4. § 352.

**Exceptions / defenses:** Civil sexual-harassment, assault and battery cases: § 1106 bars evidence of the plaintiff's sexual conduct to prove consent or absence of injury [VERIFY V-417]. AB 2556 extends §§ 782 and 1103 to offenses alleged in detention facilities [S-117] [VERIFY V-030].

**Authority:** CEC §§ 782, 1103(c), 1106; Cal. Const. art. I, § 28(f)(2) (preserves §§ 782 and 1103) [S-145].

**MBE vs. CA essay:** California's credibility route (§ 782) is broader than FRE 412's exceptions but is tightly procedural.

**Example:** D seeks to show the complainant made a false rape claim against another man; he must proceed by § 782 motion and hearing.

### R-EVD-047 — Creative expression in criminal cases (§ 352.2)
**Rule (write this):** In a California criminal proceeding, before admitting a form of creative expression such as a defendant's rap lyrics, the court must weigh, in a hearing outside the jury's presence, its probative value against the substantial danger of undue prejudice under § 352, treating the expression as having minimal probative value for its literal truth unless it was created near in time to the charged crime, bears a sufficient level of similarity to the charged crime, or includes factual detail not otherwise publicly available, and treating as undue prejudice the risk that the jury will draw propensity or racial-bias inferences.

**Elements:** 1. Creative expression offered in a criminal proceeding. 2. Hearing outside the jury. 3. Presumed minimal literal-truth value unless one of the three links exists (near in time; similar; non-public detail). 4. Consider propensity and racial-bias risk in § 352 balancing. 5. Ruling and reasons stated on the record.

**Exceptions / defenses:** The minimal-value presumption concerns literal truth; expression offered for another purpose is still weighed at the § 352.2 hearing, with the same propensity and racial-bias concerns. The statute limits, but does not ban, creative-expression evidence.

**Authority:** CEC § 352.2 (AB 2799, Stats. 2022, ch. 973, eff. Jan. 1, 2023) [S-116] [S-1556].

**MBE vs. CA essay:** California only; under FRE 403 the same concerns are weighed without a statutory presumption.

**Example:** Prosecutors offer D's year-old rap video describing shootings in general terms; § 352.2 makes its literal-truth value minimal, so it is likely excluded.

### R-EVD-048 — Authentication: the standard
**Rule (write this):** Before an item is admitted, the proponent must produce evidence sufficient to support a finding that the item is what the proponent claims it is; the jury decides ultimate genuineness.

**Elements:** 1. Identify the claim ("this is the email D sent"). 2. Prima facie evidence (104(b)). 3. Opponent may contest weight.

**Exceptions / defenses:** Self-authenticating items need no extrinsic foundation (R-EVD-050).

**Authority:** FRE 901(a); CEC §§ 1400, 1401.

**MBE vs. CA essay:** Same. In California, secondary evidence of a writing's content must also be authenticated (§ 1401(b)).

**Example:** A contract is authenticated by a witness who saw the defendant sign it.

### R-EVD-049 — Authentication: methods
**Rule (write this):** An item may be authenticated by testimony of a witness with knowledge, lay familiarity with handwriting not acquired for litigation, comparison by an expert or the jury, distinctive characteristics and circumstances, voice identification by anyone who has heard the voice, telephone-call circumstances, public-record custody, ancient-document conditions, or evidence that a process produces an accurate result.

**Elements:** Match the method to the item: signatures (familiarity/comparison), emails and texts (distinctive content plus device or account link), phone calls (number called plus self-identification), photos (fair and accurate depiction), recordings (voice ID plus accuracy).

**Exceptions / defenses:** An incoming caller's self-identification alone is insufficient. Ancient documents: 20 years (FRE) vs. 30 years (California presumption, § 643 [VERIFY V-409]). Reply-letter doctrine.

**Authority:** FRE 901(b); CEC §§ 1410–1421.

**MBE vs. CA essay:** Same methods; different ancient-document age.

**Example:** A text message signed "—J" referring to a private meeting only D and the victim knew of, sent from a number registered to D, is authenticated by distinctive characteristics.

### R-EVD-050 — Self-authentication
**Rule (write this):** Certain items require no extrinsic evidence of authenticity, including sealed and signed public documents, certified copies of public records, official publications, newspapers and periodicals, trade inscriptions, notarized documents, commercial paper, and business or electronic records accompanied by a qualifying certification.

**Elements:** Fit the item to a FRE 902 category; for 902(11)–(14), give advance written notice and make the record available.

**Exceptions / defenses:** Self-authentication answers authenticity only; hearsay and BER objections remain.

**Authority:** FRE 902; CEC §§ 1450–1454, 1530–1532 (official writings and copies).

**MBE vs. CA essay:** Similar; California relies more on presumptions (e.g., §§ 1552–1553).

**Example:** A newspaper article is self-authenticating as a newspaper, but its content offered for truth is still hearsay.

### R-EVD-051 — Photographs, video, electronic and machine output
**Rule (write this):** A photograph or video is authenticated by a witness who testifies it fairly and accurately depicts what it purports to show, or by evidence that the recording system produces accurate results; machine-generated output is not hearsay because no person makes a statement, though its accuracy must be authenticated.

**Elements:** 1. Pictorial (witness with knowledge, need not be photographer) or silent-witness (system reliability, chain of custody) theory. 2. No material alteration. 3. 403 for gruesome or misleading images.

**Exceptions / defenses:** Statements captured in a recording are separately hearsay-tested.

**Authority:** FRE 901(b)(1), (9), 1001; CEC §§ 1552, 1553; *People v. Goldsmith* (2014) 59 Cal.4th 258 (red-light camera images: presumption of accuracy; not hearsay) [S-509].

**MBE vs. CA essay:** Same result; California's §§ 1552–1553 presumptions place on the opponent the burden of producing contrary evidence.

**Example:** An ATM camera image is authenticated by the bank's security manager who explains the system and its time-stamping; the image is not hearsay.

### R-EVD-052 — Real evidence and chain of custody
**Rule (write this):** Real evidence is authenticated by testimony that the object is readily identifiable as the item involved or, for fungible or alterable items, by a chain of custody sufficient to show it is the same item in substantially the same condition; gaps go to weight unless they make tampering reasonably likely.

**Elements:** 1. Identification or chain. 2. Condition unchanged or change explained. 3. Relevance and 403.

**Exceptions / defenses:** Not every custodian must testify.

**Authority:** FRE 901(a), 901(b)(1); CEC § 1400 et seq.

**MBE vs. CA essay:** Same.

**Example:** A bag of cocaine marked with the officer's initials and a sealed evidence number is admissible though a lab clerk who logged it in does not testify.

### R-EVD-053 — Demonstrative evidence, illustrative aids and experiments
**Rule (write this):** A court may allow an illustrative aid to help the jury understand evidence or argument if its utility is not substantially outweighed by the danger of unfair prejudice, confusion, misleading the jury, undue delay or waste of time; it is not evidence and does not go to the jury room absent consent or good cause. Experiments are admissible if conducted under substantially similar conditions.

**Elements:** 1. Fair and accurate representation. 2. Helpfulness. 3. FRE 107 balancing. 4. Record preserved. 5. Experiments: substantial similarity.

**Exceptions / defenses:** Summaries offered as evidence fall under FRE 1006; reconstructions that state conclusions are expert evidence (702).

**Authority:** FRE 107 (eff. Dec. 1, 2024) [S-105], 403, 1006; CEC §§ 352, 765.

**MBE vs. CA essay:** California has no codified FRE 107; § 352 governs.

**Example:** A computer animation of the crash prepared by the plaintiff's reconstruction expert must meet 702; a simple diagram of the intersection used by an eyewitness is an illustrative aid.

### R-EVD-054 — Expert testimony (FRE 702 as amended 2023)
**Rule (write this):** A witness qualified as an expert by knowledge, skill, experience, training or education may testify in the form of an opinion if the proponent demonstrates to the court that it is more likely than not that the expert's specialized knowledge will help the trier of fact, the testimony is based on sufficient facts or data, it is the product of reliable principles and methods, and the opinion reflects a reliable application of those principles and methods to the facts.

**Elements:** 1. Qualification. 2. Helpfulness. 3. Sufficient basis. 4. Reliable method. 5. Reliable application. Each by a preponderance (104(a)).

**Exceptions / defenses:** The 2023 amendment rejects treating basis and application as mere weight; the opinion must stay within what the method supports.

**Authority:** FRE 702 [S-104]; *Daubert v. Merrell Dow Pharmaceuticals, Inc.*, 509 U.S. 579 (1993); *Kumho Tire Co. v. Carmichael*, 526 U.S. 137 (1999).

**MBE vs. CA essay:** California: §§ 720, 801, 802 with *Sargon* and *Kelly* (R-EVD-060).

**Example:** A toxicologist's opinion that a drug caused the plaintiff's liver failure is excluded if the studies she relied on involved doses ten times higher and she offers no bridge.

### R-EVD-055 — Expert qualifications
**Rule (write this):** A witness may testify as an expert if qualified by knowledge, skill, experience, training or education on the specific subject of the opinion; the judge decides qualification, and gaps in qualification go to weight once the threshold is met.

**Elements:** 1. Subject-specific expertise. 2. Shown before the opinion if challenged (voir dire). 3. Any of the five sources.

**Exceptions / defenses:** Court-appointed experts (FRE 706; § 730).

**Authority:** FRE 702, 104(a), 706; CEC §§ 720, 721(a), 730.

**MBE vs. CA essay:** Same.

**Example:** A body-shop owner with 25 years' experience may testify to repair costs without a degree.

### R-EVD-056 — Bases of expert opinion
**Rule (write this):** An expert may base an opinion on facts or data personally observed, presented at trial, or made known to the expert, and if experts in the field would reasonably rely on that kind of information, it need not be admissible; but the proponent may disclose inadmissible underlying facts to the jury only if their probative value in helping the jury evaluate the opinion substantially outweighs their prejudicial effect.

**Elements:** 1. Source of facts. 2. Reasonable reliance in the field. 3. Reverse-403 for disclosure by proponent. 4. Opinion may be given without first stating the basis (705).

**Exceptions / defenses:** In a criminal case, testimonial hearsay relayed as basis faces confrontation (R-EVD-057, R-EVD-112).

**Authority:** FRE 703, 705; CEC §§ 801(b), 802, 803.

**MBE vs. CA essay:** California's *Sanchez* rule bars relating case-specific hearsay as true (R-EVD-057).

**Example:** A physician may rely on a radiologist's report she did not prepare because doctors routinely rely on such reports.

### R-EVD-057 — Expert basis and case-specific hearsay (Sanchez; Smith)
**Rule (write this):** An expert may relate general background information in the field, but may not relate case-specific out-of-court statements as true and accurate support for the opinion unless they are independently proven by admissible evidence or fall within a hearsay exception; if the statements are testimonial and offered against a criminal defendant, the Confrontation Clause also bars them absent unavailability and a prior opportunity for cross-examination.

**Elements:** 1. General background vs. case-specific facts. 2. Offered for truth? (Yes, when the opinion depends on their truth.) 3. Independent proof or exception. 4. Testimonial → Crawford.

**Exceptions / defenses:** Hypothetical questions based on facts proven by competent evidence are allowed.

**Authority:** *People v. Sanchez* (2016) 63 Cal.4th 665; *Smith v. Arizona* (2024) [VERIFY V-035]; FRE 703.

**MBE vs. CA essay:** California since 2016; federal courts now reach a similar "for its truth" conclusion under *Smith* for confrontation purposes.

**Example:** A gang expert may explain gang culture generally, but may not tell the jury that police reports say D is a gang member unless those facts are independently proven.

### R-EVD-058 — Ultimate-issue opinions
**Rule (write this):** An opinion is not objectionable just because it embraces an ultimate issue, but in a criminal case an expert may not state an opinion about whether the defendant did or did not have a mental state or condition constituting an element of the crime or a defense.

**Elements:** 1. Ultimate issue → allowed if helpful. 2. Criminal mental-state opinion about the defendant → barred (704(b)). 3. Legal conclusions and credibility opinions → excluded under 702/403.

**Exceptions / defenses:** Testimony about what most members of a group know or intend is not an opinion about the defendant's own mental state (*Diaz v. United States* (2024) [VERIFY V-035]).

**Authority:** FRE 704; CEC § 805; Pen. Code § 29 (in the guilt phase, an expert testifying about a defendant's mental illness, disorder or defect may not testify whether the defendant had or did not have the required mental states, such as purpose, intent, knowledge or malice aforethought) [S-1554].

**MBE vs. CA essay:** Same result; California's mental-state bar is in Pen. Code § 29, not the Evidence Code.

**Example:** A psychiatrist may testify that D suffers from schizophrenia that causes delusions, but not that D "lacked the intent to kill".

### R-EVD-059 — Federal reliability gatekeeping (Daubert/Kumho)
**Rule (write this):** The trial judge must ensure that all expert testimony is both reliable and relevant, considering factors such as testability, peer review and publication, known or potential error rate, standards controlling the technique, and general acceptance, and may exclude opinions connected to the data only by the expert's say-so.

**Elements:** 1. Reliability of method. 2. Fit to the facts. 3. Applies to scientific, technical and experience-based testimony. 4. Preponderance standard.

**Exceptions / defenses:** Appellate review is for abuse of discretion (*Joiner*). General acceptance is one factor, not a requirement (Frye superseded in federal courts).

**Authority:** *Daubert*, 509 U.S. 579 (1993); *General Electric Co. v. Joiner*, 522 U.S. 136 (1997); *Kumho Tire*, 526 U.S. 137 (1999); FRE 702.

**MBE vs. CA essay:** California uses Sargon and Kelly instead (R-EVD-060).

**Example:** An engineer's untested theory that a tire failed from a manufacturing defect, without any recognized method for excluding misuse, is excluded under Kumho.

### R-EVD-060 — California gatekeeping (Sargon; Kelly)
**Rule (write this):** A California trial court must exclude expert opinion that is based on matter of a type on which an expert may not reasonably rely, on reasons unsupported by the material relied on, or on speculation. Evidence derived from a new scientific technique is admissible only if the technique is generally accepted as reliable in the relevant scientific community, the witness is qualified, and correct scientific procedures were used.

**Elements:** Sargon: 1. Type of matter reasonably relied on. 2. Logical support. 3. Not speculative. Kelly: 1. New scientific technique. 2. General acceptance. 3. Qualified witness. 4. Correct procedures in this case.

**Exceptions / defenses:** Kelly does not apply to ordinary expert opinion (medical opinions, accepted techniques); Sargon governs those.

**Authority:** CEC §§ 801(b), 802; *Sargon Enterprises, Inc. v. University of Southern California* (2012) 55 Cal.4th 747; *People v. Kelly* (1976) 17 Cal.3d 24; *People v. Leahy* (1994) 8 Cal.4th 587 (Kelly survives Daubert) [S-510].

**MBE vs. CA essay:** Differs: general acceptance is required for new scientific techniques in California.

**Example:** A novel voice-stress analysis offered in a California prosecution is inadmissible without proof of general acceptance in the scientific community.

### R-EVD-061 — Proper subject matter for expert testimony
**Rule (write this):** Expert testimony is proper when specialized knowledge will help the trier of fact understand the evidence or determine a fact in issue; under California law the subject must be sufficiently beyond common experience that the opinion would assist the trier of fact.

**Elements:** 1. Subject beyond lay knowledge (or meaningfully helpful). 2. No opinion on credibility. 3. No legal conclusions.

**Exceptions / defenses:** Syndrome evidence (battered-person, child-abuse accommodation) explains behavior but may not prove the abuse occurred; § 1107 admits intimate-partner-battering testimony in California criminal cases [VERIFY V-409].

**Authority:** FRE 702(a); CEC § 801(a).

**MBE vs. CA essay:** California's "beyond common experience" phrasing is slightly stricter.

**Example:** Expert testimony that a car traveling 60 mph covers 88 feet per second is unnecessary — jurors can do that math.

## III. Privileges and policy exclusions

### R-EVD-062 — Privilege: governing law
**Rule (write this):** In federal court, privileges are governed by federal common law as interpreted in the light of reason and experience, except that in civil cases state privilege law governs claims and defenses for which state law supplies the rule of decision. In California, privileges exist only by statute.

**Elements:** 1. Forum and type of claim. 2. Identify the holder. 3. Elements. 4. Exceptions. 5. Waiver. 6. No comment on the claim (California § 913).

**Exceptions / defenses:** Privileges apply at every stage of every proceeding (FRE 1101(c); § 910) and survive Truth-in-Evidence [S-145].

**Authority:** FRE 501; CEC §§ 910, 911, 913, 915; *Costco Wholesale Corp. v. Superior Court* (2009) 47 Cal.4th 725 (court may not order disclosure of attorney-client material to rule on the claim) [S-517].

**MBE vs. CA essay:** Differs in source and content (federal common law vs. California statutes); see R-EVD-063 to 072.

**Example:** In a federal diversity suit on a California contract, California's privilege law governs a claim of physician-patient privilege.

> 🇨🇳 PRC bridge: PRC law imposes confidentiality duties on lawyers and doctors (e.g., under the Lawyers Law) but does not have a general US-style evidentiary privilege that the client can invoke to block testimony (approx.).

### R-EVD-063 — Attorney-client privilege: elements
**Rule (write this):** A client has a privilege to refuse to disclose, and to prevent others from disclosing, confidential communications between the client and the lawyer, or their representatives, made for the purpose of obtaining or providing legal advice or services.

**Elements:** 1. Client (including prospective client). 2. Lawyer acting as a lawyer. 3. Communication (not underlying facts, not pre-existing documents). 4. Confidential (no unnecessary third parties). 5. For legal advice. 6. Holder: client; lawyer must assert it.

**Exceptions / defenses:** R-EVD-065; waiver R-EVD-067. Physical evidence of a crime is not a communication and must not be concealed.

**Authority:** Federal common law (FRE 501); *Upjohn Co. v. United States*, 449 U.S. 383 (1981); CEC §§ 951–955, 917 (presumption of confidentiality).

**MBE vs. CA essay:** Same elements. In PR crossovers, distinguish the privilege (evidentiary) from the duty of confidentiality (Bus. & Prof. Code § 6068(e)(1); CRPC 1.6).

**Example:** A client's email to her lawyer asking whether a contract term is enforceable is privileged; the fact that she signed the contract is not.

### R-EVD-064 — Attorney-client privilege: entity clients
**Rule (write this):** Under federal law, a corporation's privilege covers communications from employees at any level made at the direction of superiors to secure legal advice for the corporation, concerning matters within their duties, made in confidence. Under California law, an employee's statement is privileged if the employee spoke as the corporation's representative with the dominant purpose of transmitting information to counsel, rather than as an independent witness.

**Elements:** Federal (Upjohn): 1. Employee communication. 2. At superiors' direction. 3. For legal advice. 4. Within duties. 5. Confidential. California (Chadbourne): 1. Employer's dominant purpose. 2. Employee as corporate representative vs. independent witness.

**Exceptions / defenses:** The corporation holds the privilege; employees cannot waive or assert it personally.

**Authority:** *Upjohn Co. v. United States*, 449 U.S. 383 (1981); *D.I. Chadbourne, Inc. v. Superior Court* (1964) 60 Cal.2d 723 [S-518].

**MBE vs. CA essay:** Differs in test; results usually align.

**Example:** After a forklift accident, in-house counsel interviews the driver at the CEO's request; the interview notes are privileged under Upjohn and likely under Chadbourne.

### R-EVD-065 — Attorney-client privilege: exceptions and duration
**Rule (write this):** There is no privilege where the client sought or used the lawyer's services to enable or aid anyone to commit or plan a crime or fraud, for communications relevant to a breach of duty between lawyer and client, between joint clients in later litigation between them, or between parties claiming through the same deceased client; California adds an exception where the lawyer reasonably believes disclosure is necessary to prevent a criminal act likely to result in death or substantial bodily harm.

**Elements:** 1. Crime-fraud (future or ongoing; client's purpose controls). 2. Breach of duty. 3. Joint clients. 4. Deceased client. 5. California § 956.5.

**Exceptions / defenses:** Federal: the privilege survives death (*Swidler & Berlin v. United States*, 524 U.S. 399 (1998)); in camera review for crime-fraud on a threshold showing (*United States v. Zolin*, 491 U.S. 554 (1989)). California: privilege lasts while a holder exists (personal representative) [VERIFY V-414].

**Authority:** CEC §§ 956, 956.5, 957, 958, 962; federal common law.

**MBE vs. CA essay:** California's § 956.5 is unique; it pairs with Bus. & Prof. Code § 6068(e)(2).

**Example:** A client asks his lawyer how to transfer assets to defeat a creditor's pending judgment; the communication is not privileged (fraud).

### R-EVD-066 — Work product
**Rule (write this):** Documents and tangible things prepared in anticipation of litigation by or for a party or its representative are protected from discovery unless the requesting party shows substantial need and inability to obtain their substantial equivalent without undue hardship, and an attorney's mental impressions, conclusions, opinions and legal theories receive near-absolute protection.

**Elements:** 1. Prepared in anticipation of litigation. 2. By or for a party or representative. 3. Ordinary vs. opinion work product. 4. Need/hardship showing for ordinary.

**Exceptions / defenses:** Waived by disclosure to an adversary. California: an attorney's impressions, conclusions, opinions, research or theories are not discoverable under any circumstances; other work product only if denial would unfairly prejudice the party or cause injustice; the attorney holds the protection.

**Authority:** *Hickman v. Taylor*, 329 U.S. 495 (1947); FRCP 26(b)(3); CCP § 2018.030; *Coito v. Superior Court* (2012) 54 Cal.4th 480.

**MBE vs. CA essay:** Differs in standard and holder.

**Example:** A lawyer's memo analyzing witness credibility is opinion work product; the opposing party cannot obtain it.

### R-EVD-067 — Waiver of privilege
**Rule (write this):** A privilege is waived when the holder, without coercion, discloses a significant part of the communication or consents to disclosure; in federal proceedings, an inadvertent disclosure of attorney-client or work-product material is not a waiver if the holder took reasonable steps to prevent it and promptly took reasonable steps to rectify it, and an intentional disclosure extends to undisclosed material only on the same subject that in fairness ought to be considered together.

**Elements:** 1. Holder's voluntary disclosure. 2. Significant part. 3. Scope (subject-matter waiver only if intentional and fair). 4. Inadvertence safe harbor.

**Exceptions / defenses:** Disclosures reasonably necessary for the consultation (to an interpreter, to a co-client) are not waivers (§ 912(d)). Refreshing a witness with privileged material can waive.

**Authority:** FRE 502; CEC § 912.

**MBE vs. CA essay:** Similar; FRE 502's inadvertence and court-order rules have no exact California statute.

**Example:** A paralegal mistakenly emails a privileged memo to opposing counsel; the firm demands its return the next morning — no waiver under FRE 502(b).

### R-EVD-068 — Spousal testimonial privilege
**Rule (write this):** Under federal law, in a criminal case the witness-spouse may refuse to testify against the defendant-spouse, but may choose to testify. Under California law, a married person has a privilege not to testify against the spouse, and not to be called as a witness by a party adverse to the spouse, in any civil or criminal proceeding.

**Elements:** 1. Valid marriage at the time of testimony. 2. Testimony against the spouse (any subject, including pre-marital events). 3. Holder: witness-spouse.

**Exceptions / defenses:** Federal: crimes against the other spouse or a child. California § 972(e): a criminal proceeding in which the defendant-spouse is charged with a crime against the person or property of the other spouse, or of a child, parent, relative or cohabitant of either (whether committed before or during the marriage), with bigamy, or with failure to provide (Pen. Code §§ 270, 270a) [S-1559]; § 972 also excepts proceedings between the spouses and certain other proceedings [VERIFY V-992]. Waiver (§ 973(a)): a spouse who testifies in a proceeding to which the other spouse is a party, or testifies against the spouse in any proceeding, loses the privilege in that proceeding; § 973(b): no privilege in a civil proceeding brought or defended for the immediate benefit of the spouse [S-1559].

**Authority:** *Trammel v. United States*, 445 U.S. 40 (1980); CEC §§ 970–973 [S-1559].

**MBE vs. CA essay:** Differs: federal applies only in criminal cases; California applies in all proceedings and adds the right not to be called.

**Example:** H is prosecuted for tax fraud; W, still married to him, may refuse to testify at trial about anything, but may testify if she chooses (federal).

### R-EVD-069 — Confidential marital communications privilege
**Rule (write this):** Either spouse may refuse to disclose, and may prevent the other from disclosing, a confidential communication made between them during a valid marriage; the privilege survives divorce and death and applies in civil and criminal cases.

**Elements:** 1. Communication (not mere conduct). 2. During the marriage. 3. In confidence. 4. Both spouses hold it.

**Exceptions / defenses:** Crime or fraud furtherance; proceedings between spouses; crimes against the spouse or a child; in California, communications offered by a defendant-spouse in a criminal case [VERIFY V-409].

**Authority:** Federal common law (FRE 501); CEC §§ 980–987.

**MBE vs. CA essay:** Same core rule.

**Example:** After divorce, W is asked about H's whispered confession during the marriage that he set the fire; H can block it (the communications privilege survives), though the testimonial privilege ended with the marriage.

### R-EVD-070 — Physician-patient privilege (California)
**Rule (write this):** California gives a patient a privilege to refuse to disclose, and to prevent others from disclosing, confidential communications between patient and physician made for diagnosis or treatment; it does not apply in criminal proceedings or where the patient tenders his own condition. Federal law recognizes no general physician-patient privilege.

**Elements:** 1. Physician. 2. Patient. 3. Confidential communication. 4. For diagnosis or treatment. 5. Holder: patient.

**Exceptions / defenses:** Patient-litigant (§ 996); criminal proceedings (§ 998); services to commit a crime or tort (§ 997); other statutory exceptions.

**Authority:** CEC §§ 990–1007; FRE 501 (no federal privilege; state law in diversity).

**MBE vs. CA essay:** California only; mention its criminal-case exception on a CEC essay.

**Example:** In a California personal-injury suit, the plaintiff cannot invoke the privilege for her treating doctor's notes about the injury she sued for.

### R-EVD-071 — Psychotherapist-patient privilege
**Rule (write this):** A patient may refuse to disclose, and prevent others from disclosing, confidential communications with a licensed psychotherapist (including psychiatrists, psychologists and clinical social workers) made for diagnosis or treatment; the federal privilege admits no case-by-case balancing, and California's applies in civil and criminal cases.

**Elements:** 1. Licensed psychotherapist. 2. Confidential communication. 3. For diagnosis or treatment. 4. Holder: patient.

**Exceptions / defenses:** Patient-litigant (§ 1016); court-ordered examinations (§ 1017); crime or tort services (§ 1018); dangerous patient where disclosure is necessary to prevent danger (§ 1024).

**Authority:** *Jaffee v. Redmond*, 518 U.S. 1 (1996); CEC §§ 1010–1027.

**MBE vs. CA essay:** Same core; California's statutory exceptions are explicit.

**Example:** A police officer's counseling sessions with a licensed clinical social worker after a shooting are privileged in a federal civil-rights suit.

### R-EVD-072 — Other privileges
**Rule (write this):** Other recognized privileges include the privilege against self-incrimination, the clergy-penitent privilege, the government's privileges for informer identity and official information, and, in California, statutory privileges for sexual-assault and domestic-violence counselors, trade secrets and mediation communications; a California newsperson is immune from contempt for refusing to disclose sources.

**Elements:** Identify holder, confidentiality, purpose, and statutory exceptions for each.

**Exceptions / defenses:** Informer privilege yields where disclosure is essential to a fair defense (*Roviaro v. United States*, 353 U.S. 53 (1957)); no First Amendment reporter's privilege before a grand jury (*Branzburg v. Hayes*, 408 U.S. 665 (1972)); no comment on a defendant's silence (*Griffin v. California*, 380 U.S. 609 (1965)).

**Authority:** U.S. Const. amend. V; CEC §§ 940, 1033, 1034, 1035.8, 1037.5, 1040, 1041, 1060, 1070, 1119; Cal. Const. art. I, § 2(b).

**MBE vs. CA essay:** California has more statutory privileges; federal courts recognize fewer.

**Example:** A penitent's confession to a priest is privileged in both systems; a statement to a rape-crisis counselor is privileged by statute in California.

### R-EVD-073 — Liability insurance
**Rule (write this):** Evidence that a person was or was not insured against liability is not admissible to prove that the person acted negligently or otherwise wrongfully, but may be admitted for another purpose such as proving a witness's bias or prejudice, or agency, ownership or control.

**Elements:** 1. Offered to show fault → excluded. 2. Other purpose genuinely disputed → admissible with limiting instruction.

**Exceptions / defenses:** 403 for gratuitous references.

**Authority:** FRE 411; CEC § 1155.

**MBE vs. CA essay:** Same.

**Example:** A defense witness is an adjuster for the defendant's insurer; the employment is admissible to show bias.

### R-EVD-074 — Subsequent remedial measures
**Rule (write this):** When measures are taken after an injury that would have made the injury less likely, evidence of the measures is not admissible to prove negligence, culpable conduct, a product or design defect, or a need for a warning, but may be admitted for impeachment or, if disputed, to prove ownership, control or the feasibility of precautionary measures.

**Elements:** 1. Measure taken after the event. 2. By the defendant (third-party measures not covered). 3. Purpose. 4. Exception genuinely disputed.

**Exceptions / defenses:** Pre-accident measures are not covered. California's § 1151 covers negligence and culpable conduct but **not strict products liability** (*Ault v. International Harvester Co.* (1974) 13 Cal.3d 113).

**Authority:** FRE 407; CEC § 1151.

**MBE vs. CA essay:** Differs for strict products liability: admissible in California to prove defect.

**Example:** After a ladder collapses, the maker adds a brace. Federal: inadmissible to prove design defect. California strict-liability claim: admissible.

### R-EVD-075 — Compromise offers and negotiations
**Rule (write this):** Offers or acceptances of valuable consideration in compromising, or attempting to compromise, a disputed claim, and conduct or statements made during the compromise negotiations, are not admissible to prove or disprove the validity or amount of the claim or to impeach by prior inconsistent statement or contradiction; they may be admitted for other purposes such as bias, negating undue delay, or proving obstruction.

**Elements:** 1. Disputed claim (validity or amount). 2. Offer, acceptance, or negotiation statement. 3. Prohibited purpose.

**Exceptions / defenses:** FRE: statements in negotiations with a public office exercising regulatory authority are admissible in a later criminal case. California § 1152 has no textual dispute requirement and also covers humanitarian offers [S-511]; § 1154 covers a claimant's offers to discount.

**Authority:** FRE 408; CEC §§ 1152, 1154.

**MBE vs. CA essay:** Similar; California's coverage is broader (humanitarian offers; prospective claims).

**Example:** In settlement talks D says, "Fine, my brakes were bad — I'll pay $10,000." Both the offer and the admission are inadmissible to prove liability.

### R-EVD-076 — Medical expenses, humanitarian offers and expressions of sympathy
**Rule (write this):** Evidence of furnishing, offering or promising to pay medical, hospital or similar expenses resulting from an injury is not admissible to prove liability, but statements of fact made with the offer are admissible. In California, offers made from humanitarian motives are excluded with compromise offers, and expressions of sympathy about an accident victim's pain, suffering or death are inadmissible to prove liability in a civil action, though accompanying statements of fault are not excluded by that rule.

**Elements:** 1. Offer to pay medical expenses (FRE 409) or humanitarian offer (§ 1152). 2. Sympathy statement or gesture (§ 1160). 3. Separate any admission of fault.

**Exceptions / defenses:** Whether California excludes a fault statement accompanying a humanitarian offer outside negotiations is unsettled [VERIFY V-405].

**Authority:** FRE 409; CEC §§ 1152, 1160.

**MBE vs. CA essay:** Differs: § 1160 has no FRE counterpart; FRE 409 admits accompanying statements.

**Example:** "I'm so sorry you're hurt. I'll pay your hospital bill — I wasn't watching the road." FRE: the offer is excluded, "I wasn't watching the road" is admissible as a party statement. California: "I'm so sorry" is excluded by § 1160; the fault statement is not excluded by § 1160.

### R-EVD-077 — Pleas and plea discussions
**Rule (write this):** A withdrawn guilty plea, a nolo contendere plea, statements made in plea proceedings on either, and statements made during plea discussions with an attorney for the prosecuting authority that do not result in a guilty plea or result in a withdrawn plea, are not admissible against the defendant who made the plea or participated in the discussions.

**Elements:** 1. Type of plea or discussion. 2. With a prosecutor (or someone with authority). 3. Offered against the defendant.

**Exceptions / defenses:** Completeness; perjury prosecutions for sworn, on-record, counseled statements; waiver by agreement (*United States v. Mezzanatto*, 513 U.S. 196 (1995)). A guilty plea not withdrawn is a party admission.

**Authority:** FRE 410; CEC § 1153; Pen. Code § 1016 (nolo pleas) [VERIFY V-409].

**MBE vs. CA essay:** Similar; California's nolo rule differs for felonies.

**Example:** D tells an FBI agent with no authority to bargain, "I'll confess if you go easy on me." Not a plea discussion with a prosecutor; admissible.

## IV. Writings, recordings and photographs

### R-EVD-078 — Best evidence rule: when it applies
**Rule (write this):** To prove the content of a writing, recording or photograph, the original is required unless an exception applies; the rule applies only when the proponent seeks to prove the content — where the writing is legally operative or the witness's knowledge comes from the writing — and not when the fact exists independently.

**Elements:** 1. Writing, recording or photograph (including electronic data). 2. Content in issue or knowledge derived from it. 3. Original, duplicate, or excuse.

**Exceptions / defenses:** Collateral matters; public records (FRE 1005); summaries (1006); party's own testimony or written admission (1007).

**Authority:** FRE 1001, 1002, 1005–1008.

**MBE vs. CA essay:** California uses the secondary evidence rule (R-EVD-080).

**Example:** A witness may testify that she paid $500 though a receipt exists; she may not testify to what a lost contract said without satisfying 1004.

### R-EVD-079 — Duplicates and excuses for the original
**Rule (write this):** A duplicate is admissible to the same extent as the original unless a genuine question is raised about the original's authenticity or circumstances make admitting the duplicate unfair; other evidence of content is admissible if the originals were lost or destroyed without the proponent's bad faith, cannot be obtained by judicial process, are in the opponent's control after notice and not produced, or concern a collateral matter.

**Elements:** 1. Duplicate = accurate mechanical or electronic reproduction. 2. Challenge grounds. 3. Excuses under 1004. 4. No degrees of secondary evidence.

**Exceptions / defenses:** Handwritten copies are not duplicates.

**Authority:** FRE 1001(e), 1003, 1004.

**MBE vs. CA essay:** California: § 1521 admits copies unless genuine dispute plus justice, or unfairness; § 1523 limits oral testimony.

**Example:** A photocopy of a promissory note is admissible unless the defendant raises a genuine question that the original signature was forged.

### R-EVD-080 — California secondary evidence rule
**Rule (write this):** In California, the content of a writing may be proved by an original or by otherwise admissible secondary evidence, but the court must exclude secondary evidence if a genuine dispute exists about material terms and justice requires exclusion, or if admission would be unfair; oral testimony of a writing's content is inadmissible unless (1) the proponent has no copy (or original) available and the original was lost or destroyed without the proponent's fraudulent intent, could not reasonably be procured, or is collateral, or (2) the writing consists of numerous accounts offered for their general result.

**Elements:** 1. "Writing" (includes photos, recordings, electronic data, § 250). 2. Copy → § 1521 test. 3. Oral testimony → § 1523 exceptions. 4. Criminal cases → § 1522 [VERIFY V-409]. 5. Authentication (§ 1401).

**Exceptions / defenses:** Printouts of computer data and digital images are presumed accurate (§§ 1552–1553).

**Authority:** CEC §§ 1520, 1521, 1522, 1523 [S-506] [S-507].

**MBE vs. CA essay:** California only. Write: "The best evidence rule has been replaced by the secondary evidence rule."

**Example:** A photocopy of an advertisement is admissible in California unless the parties genuinely dispute its terms; a witness's oral description of it is barred unless § 1523 applies.

### R-EVD-081 — Summaries of voluminous evidence
**Rule (write this):** A summary, chart or calculation offered to prove the content of voluminous admissible writings, recordings or photographs that cannot be conveniently examined in court is admissible as evidence, whether or not the underlying evidence has been introduced, if the underlying material is made available to the other parties.

**Elements:** 1. Voluminous. 2. Underlying material admissible. 3. Available for examination. 4. Accurate and non-argumentative.

**Exceptions / defenses:** Summaries used only to illustrate admitted evidence or argument are illustrative aids under FRE 107.

**Authority:** FRE 1006 (as amended Dec. 1, 2024) [S-105]; CEC § 1523(d).

**MBE vs. CA essay:** Similar result.

**Example:** An accountant's chart totaling 10,000 invoices is admissible if the invoices were made available to the defense.

### R-EVD-082 — Rule of completeness
**Rule (write this):** If a party introduces all or part of a statement, written or oral, an adverse party may require the introduction at that time of any other part, or any other statement, that in fairness ought to be considered at the same time, and may do so over a hearsay objection.

**Elements:** 1. Part of a statement introduced. 2. Remainder needed to correct a misleading impression. 3. Timing: at that time. 4. Hearsay no bar.

**Exceptions / defenses:** Only what fairness requires; not a general license to admit self-serving statements.

**Authority:** FRE 106 (as amended Dec. 1, 2023) [S-104]; CEC § 356.

**MBE vs. CA essay:** Now largely the same; California has long covered oral conversations.

**Example:** The prosecution plays D's statement "I hit him"; D may require the next sentence, "after he pulled a knife on me".

## V. Hearsay and confrontation

### R-EVD-083 — Hearsay: definition
**Rule (write this):** Hearsay is a statement, other than one made by the declarant while testifying at the current trial or hearing, offered to prove the truth of the matter asserted; it is inadmissible unless an exclusion or exception applies. A statement is an oral or written assertion, or nonverbal conduct intended as an assertion.

**Elements:** 1. Statement (assertion by a person). 2. Out of court. 3. Offered for its truth. Then: 4. Exclusion (FRE 801(d)) or exception (803, 804, 807; CEC §§ 1220–1390). 5. Each layer (805/§ 1201). 6. Confrontation if criminal.

**Exceptions / defenses:** Non-assertive conduct, machine output and animal behavior are not statements.

**Authority:** FRE 801(a)–(c), 802; CEC §§ 225, 1200.

**MBE vs. CA essay:** Same definition; under the CEC, party admissions and prior witness statements are hearsay within exceptions.

**Example:** W testifies, "My neighbor told me the defendant's car ran the red light," offered to prove the car ran the light — hearsay.

> 🇨🇳 PRC bridge: PRC procedure has no general hearsay exclusion; out-of-court witness statements (证人证言) can be admitted and weighed, though courts prefer witnesses to appear (出庭作证) (approx.). US law excludes them unless an exception fits.

### R-EVD-084 — Non-hearsay purposes
**Rule (write this):** An out-of-court statement is not hearsay when offered for a purpose other than its truth, such as legally operative words, the effect on the listener or reader, the declarant's state of mind shown circumstantially, impeachment, or to show the statement was false.

**Elements:** 1. Identify the purpose. 2. Confirm the inference does not depend on the declarant being right. 3. 403 / § 352 risk of misuse. 4. Limiting instruction.

**Exceptions / defenses:** A purported non-truth purpose that is not genuinely in issue is a subterfuge; courts look at whether the purpose is relevant.

**Authority:** FRE 801(c); CEC § 1200.

**MBE vs. CA essay:** Same.

**Example:** In a slip-and-fall case, an employee's warning to the manager "the aisle is wet" is offered to show notice, not that the aisle was wet — not hearsay.

### R-EVD-085 — Prior inconsistent statements as substantive evidence
**Rule (write this):** Under FRE 801(d)(1)(A) as amended effective December 1, 2026, a prior statement of a witness who testifies and is subject to cross-examination about it is not hearsay if it is inconsistent with the witness's testimony, so it is admissible for its truth, subject to Rule 403 and the Rule 613(b) foundation. California has long admitted such statements for their truth under § 1235 if the § 770 foundation is met.

**Elements:** 1. Declarant testifies. 2. Subject to cross about the statement. 3. Inconsistent (including feigned memory loss). 4. Foundation (613(b) / § 770). 5. 403 / § 352.

**Exceptions / defenses:** Before Dec. 1, 2026 the FRE required that the statement have been made under penalty of perjury at a trial, hearing, other proceeding or deposition; otherwise it was impeachment only. Confirm the amendment took effect [S-101].

**Authority:** FRE 801(d)(1)(A) [S-101] [S-102]; CEC §§ 770, 1235; *California v. Green*, 399 U.S. 149 (1970); *People v. Green* (1971) 3 Cal.3d 981 [S-519].

**MBE vs. CA essay:** Now largely the same. Learn the old rule too, for older practice questions.

**Example:** At trial W says she did not see who fired; she told police the night of the shooting that D fired. Under the amended FRE and § 1235, the police statement is substantive evidence that D fired.

### R-EVD-086 — Prior consistent statements
**Rule (write this):** A testifying witness's prior consistent statement is admissible for its truth if offered to rebut an express or implied charge of recent fabrication or improper influence or motive and made before that motive arose, or, under the FRE, to rehabilitate the witness's credibility when attacked on another ground.

**Elements:** 1. Declarant testifies and is subject to cross. 2. Consistent. 3. Proper rehabilitative purpose. 4. Pre-motive timing (for fabrication/motive attacks).

**Exceptions / defenses:** No bolstering an unimpeached witness.

**Authority:** FRE 801(d)(1)(B); *Tome v. United States*, 513 U.S. 150 (1995); CEC §§ 791, 1236.

**MBE vs. CA essay:** California is narrower: § 791 has no "other ground" clause, but also admits a consistent statement made before an admitted inconsistent statement.

**Example:** Defense suggests V invented the charge after D fired her; V's text to a friend before the firing describing the assault is admissible.

### R-EVD-087 — Prior identification
**Rule (write this):** A testifying witness's prior statement identifying a person as someone the witness perceived earlier is admissible for its truth, and may be proved through the witness or another person who observed the identification.

**Elements:** 1. Declarant testifies and is subject to cross. 2. Statement of identification. 3. California: made when the event was fresh in memory, and the witness testifies it was a true reflection of his opinion then.

**Exceptions / defenses:** Suggestive procedures raise due process issues (Crim Pro). Memory loss at trial does not defeat cross-examination (*United States v. Owens*, 484 U.S. 554 (1988)).

**Authority:** FRE 801(d)(1)(C); CEC § 1238.

**MBE vs. CA essay:** Same in substance; California spells out the extra foundation.

**Example:** The victim picked D from a lineup the day after the robbery but at trial says she is unsure; the officer may testify to the lineup identification.

### R-EVD-088 — Party admissions
**Rule (write this):** A statement made by a party and offered against that party is admissible; it need not have been against interest when made or based on personal knowledge. The FRE define it as not hearsay; the CEC treats it as an exception.

**Elements:** 1. Declarant is a party (individual or representative capacity). 2. Offered by the opponent. 3. Relevant.

**Exceptions / defenses:** Only against the party who made it (limiting instruction in multi-party cases; *Bruton* for criminal codefendants). Plea-related statements excluded by 410 / § 1153.

**Authority:** FRE 801(d)(2)(A); CEC § 1220.

**MBE vs. CA essay:** Same result; different label.

**Example:** At the accident scene, D says, "I was looking at my phone." P may offer it against D.

### R-EVD-089 — Adoptive admissions (including silence)
**Rule (write this):** A statement is admissible against a party who, with knowledge of its content, manifested adoption of it or belief in its truth by words or conduct, including silence when a reasonable person would have denied it.

**Elements:** For silence: 1. Party heard and understood. 2. Able to respond. 3. Circumstances naturally called for a denial. 4. Failure to deny.

**Exceptions / defenses:** Silence after Miranda warnings cannot be used (*Doyle v. Ohio*, 426 U.S. 610 (1976)).

**Authority:** FRE 801(d)(2)(B); CEC § 1221.

**MBE vs. CA essay:** Same.

**Example:** At a party, A says to D, "You're the one who keyed my car"; D shrugs and walks away. A jury could find adoption.

### R-EVD-090 — Authorized and employee admissions
**Rule (write this):** Under the FRE, a statement is admissible against a party if made by a person the party authorized to speak on the subject, or by the party's agent or employee on a matter within the scope of that relationship while it existed. California admits an agent's statement only if the party authorized it, or where the party's liability is based on the declarant's conduct.

**Elements:** FRE: 1. Agency or employment. 2. Matter within scope. 3. During the relationship. 4. Independent evidence of the relationship (statement alone not enough). CEC: 1. Authority to speak (§ 1222), or 2. derivative liability (§ 1224, civil actions only). *Labis* applied § 1224 to an employee's statement in a respondeat-superior case, distinguishing contrary dictum in *Markley v. Beagle* (1967) 66 Cal.2d 951, 960 [S-503].

**Exceptions / defenses:** Statements after employment ends are not covered. Successor liability: since 2024, statements admissible against a predecessor or principal are admissible against a party whose liability derives from them [S-105].

**Authority:** FRE 801(d)(2)(C)–(D); CEC §§ 1222, 1224 [S-523]; *Labis v. Stopper* (1970) 11 Cal.App.3d 1003 [S-503] [S-1826].

**MBE vs. CA essay:** Differs: no general vicarious-admission rule in California.

**Example:** A delivery driver tells a police officer after a crash, "I was rushing to make my quota." FRE: admissible against the employer (within scope, during employment). California: admissible against the employer only via § 1222 (authority to speak) or § 1224.

### R-EVD-091 — Co-conspirator statements
**Rule (write this):** A statement by a party's coconspirator made during and in furtherance of the conspiracy is admissible against the party; the court must find the conspiracy and participation by a preponderance, must consider the statement itself, but cannot rely on it alone.

**Elements:** 1. Conspiracy existed. 2. Declarant and party members. 3. During the conspiracy. 4. In furtherance (not narratives, confessions or post-arrest statements). 5. Independent evidence.

**Exceptions / defenses:** No conspiracy charge needed. A statement to an undercover officer can still be in furtherance (nontestimonial).

**Authority:** FRE 801(d)(2)(E); *Bourjaily v. United States*, 483 U.S. 171 (1987); CEC § 1223; *People v. Hardy* (1992) 2 Cal.4th 86, 139; CALCRIM No. 418 [S-1558].

**MBE vs. CA essay:** Differs in the foundation. FRE: the judge finds the conspiracy and membership by a preponderance (104(a)), considering the statement itself. CEC § 1223: the proponent needs only **prima facie** evidence, **independent of the statement**, sufficient to sustain a finding of the conspiracy (the court may admit the statement subject to that proof); in a criminal case the jury is then told to use the statement only if the conspiracy is proved by a preponderance with evidence other than the statement (CALCRIM No. 418). § 1223(b) also reaches statements made before the party joined the conspiracy [S-1558].

**Example:** Before the robbery, X tells a lookout, "D will drive the getaway car." Admissible against D. After arrest, X tells police D drove — not in furtherance.

### R-EVD-092 — Multiple hearsay
**Rule (write this):** Hearsay within hearsay is admissible only if each part of the combined statements conforms with an exclusion or exception.

**Elements:** 1. Identify every declarant and layer. 2. Apply the definition and an exception to each.

**Exceptions / defenses:** A layer offered for a non-truth purpose needs no exception.

**Authority:** FRE 805; CEC § 1201.

**MBE vs. CA essay:** Same.

**Example:** A hospital record states "Patient says a red truck hit him." Layer 1 (record) → business record; layer 2 (patient) → medical diagnosis (FRE 803(4)); in California the second layer needs another exception, such as § 1240 if the patient was still excited (§ 1250 covers only present pain, not how the injury happened).

### R-EVD-093 — Present sense impression; California contemporaneous statement
**Rule (write this):** Under the FRE, a statement describing or explaining an event or condition, made while or immediately after the declarant perceived it, is admissible. California has no general present sense impression exception; it admits only a statement offered to explain, qualify or make understandable the declarant's own conduct, made while the declarant was engaged in that conduct.

**Elements:** FRE: 1. Describes or explains. 2. Perceived by declarant. 3. Contemporaneous. CEC § 1241: 1. Explains declarant's own conduct. 2. Made during it.

**Exceptions / defenses:** If the declarant was excited, use the excited utterance / spontaneous statement exception instead.

**Authority:** FRE 803(1); CEC § 1241.

**MBE vs. CA essay:** Differs — a California gap.

**Example:** A driver says calmly to her passenger, "That blue truck is going way too fast." FRE: admissible PSI. CEC: not under § 1241 (it is not about her own conduct); try § 1240 if she was startled.

### R-EVD-094 — Excited utterance / spontaneous statement
**Rule (write this):** A statement relating to (CEC: narrating, describing or explaining) a startling event or condition, made while the declarant was under the stress of excitement caused by it, is admissible.

**Elements:** 1. Startling event. 2. Statement relates to it. 3. Under stress at the time (time lapse, tone, injury, questioning). 4. Declarant perceived the event (CEC express).

**Exceptions / defenses:** Statements to police after an emergency ends may be testimonial (Confrontation).

**Authority:** FRE 803(2); CEC § 1240.

**MBE vs. CA essay:** Same.

**Example:** Sobbing on a 911 call two minutes after a beating, V says, "Deb hit me with a bottle." Admissible as a spontaneous statement; nontestimonial if it sought help in an ongoing emergency.

### R-EVD-095 — Then-existing state of mind
**Rule (write this):** A statement of the declarant's then-existing state of mind, such as intent, plan, motive, design or emotion, or of a then-existing physical condition, is admissible, but not a statement of memory or belief to prove the fact remembered or believed, except concerning the declarant's will.

**Elements:** 1. Present (not past) state. 2. Relevant use: state itself in issue, or intent to prove the declarant's later conduct (*Hillmon*). 3. No backward-looking fact proof (*Shepard*). 4. California: not untrustworthy (§ 1252).

**Exceptions / defenses:** Intent offered to prove another person's conduct is admitted cautiously (corroboration in many courts).

**Authority:** FRE 803(3); *Mutual Life Insurance Co. v. Hillmon*, 145 U.S. 285 (1892); *Shepard v. United States*, 290 U.S. 96 (1933); CEC §§ 1250, 1252.

**MBE vs. CA essay:** Same core; California adds the § 1252 trustworthiness filter, and its will-statement exception (§ 1260) requires the declarant to be unavailable [VERIFY V-409].

**Example:** V told a friend, "I'm going to break up with D tonight." Admissible to show V's plan and that she probably did so — and, if motive is in issue, to show D's motive.

### R-EVD-096 — Physical condition and prior state of mind (California § 1251)
**Rule (write this):** A statement of then-existing pain or bodily condition is admissible under both systems; California also admits a statement of the declarant's prior mental or physical state if the declarant is unavailable and the prior state itself is in issue.

**Elements:** § 1251: 1. Declarant unavailable. 2. Statement of past state. 3. That past state is an issue in the case. 4. Not offered to prove other facts. 5. Not untrustworthy (§ 1252).

**Exceptions / defenses:** FRE has no general past-condition exception outside 803(4).

**Authority:** FRE 803(3); CEC §§ 1250, 1251, 1252.

**MBE vs. CA essay:** California adds § 1251.

**Example:** A deceased worker told a coworker a week before death, "My chest hurt badly all last month." In a California civil suit where his past condition is itself in issue, § 1251 can admit it.

### R-EVD-097 — Statements for medical diagnosis or treatment
**Rule (write this):** Under the FRE, a statement made for, and reasonably pertinent to, medical diagnosis or treatment describing medical history, past or present symptoms or sensations, their inception, or their general cause is admissible, but not statements of fault. California has no general equivalent; it admits such statements only by a minor victim, made when under 12, describing child abuse or neglect.

**Elements:** FRE: 1. Purpose of diagnosis or treatment (to anyone). 2. Reasonably pertinent. 3. History, symptoms, cause — not fault. CEC § 1253: 1. Victim now a minor. 2. Statement made when under 12. 3. Describes child abuse or neglect. 4. § 1252.

**Exceptions / defenses:** Federal courts often admit a child victim's identification of an abuser as pertinent to treatment.

**Authority:** FRE 803(4); CEC § 1253 [S-500].

**MBE vs. CA essay:** Differs — a major California gap; use § 1250 for present pain instead.

**Example:** P tells an ER nurse, "My neck hurts; a car rear-ended me; the other driver was texting." FRE: first two parts admissible, "texting" is not. CEC: "my neck hurts" via § 1250; the rest needs another exception.

### R-EVD-098 — Recorded recollection
**Rule (write this):** A record on a matter the witness once knew but now cannot recall well enough to testify fully and accurately, made or adopted by the witness when the matter was fresh in memory and accurately reflecting the witness's knowledge, may be read into evidence, but may be received as an exhibit only if offered by an adverse party.

**Elements:** 1. Witness on the stand. 2. Insufficient present recollection (after attempted refreshing). 3. Made or adopted when fresh. 4. Accurate (California: witness testifies the statement was true). 5. Authenticated.

**Exceptions / defenses:** Multi-person records are allowed if each participant testifies to their part.

**Authority:** FRE 803(5); CEC § 1237 [S-520].

**MBE vs. CA essay:** Same.

**Example:** A warehouse clerk who wrote down a truck's license plate as it sped away cannot recall the number at trial; her note may be read to the jury.

### R-EVD-099 — Business records
**Rule (write this):** A record of an act, event, condition, opinion or diagnosis made at or near the time by, or from information transmitted by, someone with knowledge, kept in the course of a regularly conducted activity as a regular practice, shown by a custodian, qualified witness or certification, is admissible unless the opponent shows the source or circumstances indicate a lack of trustworthiness.

**Elements:** 1. Regular course of business. 2. Regular practice to make the record. 3. At or near the time. 4. Person with knowledge under a business duty (each link). 5. Foundation by custodian/qualified witness/902(11). 6. Trustworthiness.

**Exceptions / defenses:** Records prepared for litigation may be untrustworthy (*Palmer v. Hoffman*, 318 U.S. 109 (1943)); outsiders' statements need their own exception (805). Forensic reports prepared for prosecution are testimonial.

**Authority:** FRE 803(6), 803(7), 902(11); CEC §§ 1270, 1271, 1272; *People v. Reyes* (1974) 12 Cal.3d 486 [S-515].

**MBE vs. CA essay:** Differs: § 1271 covers acts, conditions and events (California courts exclude opinions and diagnoses), and the **proponent** must show trustworthiness.

**Example:** The bank's custodian testifies that ATM transaction logs are generated automatically at the time of each withdrawal and kept in the ordinary course; the logs are admissible (and the machine-generated data may not be hearsay at all).

### R-EVD-100 — Public records
**Rule (write this):** A record of a public office setting out the office's activities, matters observed under a legal duty to report (but not, in a criminal case, matters observed by law enforcement), or, in civil cases and against the government in criminal cases, factual findings from a legally authorized investigation, is admissible unless the opponent shows a lack of trustworthiness.

**Elements:** 1. Public office. 2. Category (activities / duty-observed matters / investigative findings). 3. Criminal-case limits. 4. Trustworthiness.

**Exceptions / defenses:** Factual findings include opinions and conclusions (*Beech Aircraft Corp. v. Rainey*, 488 U.S. 153 (1988)). Statements of witnesses within a report need their own exception.

**Authority:** FRE 803(8), 803(9), 803(10); CEC §§ 1280, 1284.

**MBE vs. CA essay:** California's § 1280 requires the proponent to show trustworthiness and has no express police-report bar, but confrontation and multiple-hearsay limits apply.

**Example:** A fire marshal's report concluding the fire started at a faulty outlet is admissible in a civil suit; a police report offered by the prosecution against the accused is not admissible under 803(8).

### R-EVD-101 — Learned treatises
**Rule (write this):** Under the FRE, a statement in a treatise, periodical or pamphlet is admissible for its truth if called to an expert's attention on cross or relied on by the expert on direct and established as a reliable authority, and it may be read into evidence but not received as an exhibit. California has no general learned-treatise exception; such publications may be used to cross-examine an expert under § 721(b), not as substantive evidence.

**Elements:** FRE: 1. Expert on the stand. 2. Reliable authority (admission, other expert, judicial notice). 3. Read only. CEC: 1. Expert referred to, considered or relied on it; or it is admitted; or established as reliable authority. 2. Impeachment use only.

**Exceptions / defenses:** CEC § 1341 admits only historical works, books of science or art, and published maps or charts, made by persons indifferent between the parties, to prove facts of general notoriety and interest [S-1555].

**Authority:** FRE 803(18); CEC §§ 721(b) [S-512], 1341 [S-1555].

**MBE vs. CA essay:** Differs.

**Example:** P's counsel reads a passage from a recognized surgical textbook to the defense expert on cross. FRE: substantive evidence. CEC: only to test the expert's opinion.

### R-EVD-102 — Unavailability
**Rule (write this):** Under FRE 804(a), a declarant is unavailable if exempted by privilege, refuses to testify despite a court order, testifies to not remembering the subject matter, cannot testify because of death or then-existing illness or infirmity, or is absent and the proponent could not procure attendance by process or other reasonable means; a proponent who wrongfully caused the unavailability cannot rely on it.

**Elements:** One listed ground, shown by the proponent (104(a)); reasonable diligence for absence.

**Exceptions / defenses:** California § 240(a) lists privilege, disqualification, death or then-existing physical or mental illness or infirmity, inability to compel attendance, absence despite reasonable diligence, and (since 2010, § 240(a)(6)) **persistent refusal to testify despite having been found in contempt**; expert proof of crime-caused trauma can establish infirmity [S-516] [S-513] [S-1551]. Memory loss is not listed as such. Where a mental infirmity has left the witness with no memory of the events, the California Supreme Court allowed former testimony as from an unavailable witness under the "then-existing … mental illness or infirmity" ground (*People v. Alcala* (1992) 4 Cal.4th 742) [S-1827]; whether a claimed or feigned lack of memory without such an infirmity qualifies is not settled in the sources checked [VERIFY V-990].

**Authority:** FRE 804(a); CEC § 240 [S-516] [S-1551].

**MBE vs. CA essay:** Similar. California's refusal ground needs a **contempt finding**, not just a court order; memory loss is not a listed ground.

**Example:** A witness invokes the Fifth Amendment and the court sustains it; she is unavailable.

### R-EVD-103 — Former testimony
**Rule (write this):** Testimony given as a witness at a trial, hearing or lawful deposition is admissible if the declarant is unavailable and it is offered against a party who had, or in a civil case whose predecessor in interest had, an opportunity and similar motive to develop it by direct, cross or redirect examination.

**Elements:** 1. Unavailable. 2. Former testimony under oath. 3. Same party (or civil predecessor in interest; California civil: any party with similar interest and motive). 4. Opportunity and similar motive.

**Exceptions / defenses:** Grand jury testimony offered against the defendant fails (no opportunity to cross). California § 1291 also admits testimony against the party who offered it before.

**Authority:** FRE 804(b)(1); CEC §§ 1290, 1291, 1292; FRCP 32(a).

**MBE vs. CA essay:** California § 1292 is broader in civil cases (no predecessor-in-interest requirement), but not available against a criminal defendant.

**Example:** A witness who testified at the first trial dies before the retrial; her testimony, cross-examined by the same defendant, is admissible.

### R-EVD-104 — Statement against interest
**Rule (write this):** A statement by an unavailable declarant that, when made, was so contrary to the declarant's pecuniary or proprietary interest, or so tended to invalidate the declarant's claim or expose the declarant to civil or criminal liability, that a reasonable person would have made it only if true, is admissible; in a criminal case a statement offered as tending to expose the declarant to criminal liability must be supported by corroborating circumstances that clearly indicate its trustworthiness, after considering the totality of circumstances under which it was made and any evidence that supports or undermines it. California also includes statements risking hatred, ridicule or social disgrace.

**Elements:** 1. Unavailable. 2. Against interest when made. 3. Reasonable-person test. 4. Only self-inculpatory portions. 5. FRE criminal (whichever side offers it): corroborating circumstances clearly indicating trustworthiness — since Dec. 1, 2024, judged "after considering the totality of circumstances under which it was made and any evidence that supports or undermines it" (FRE 804(b)(3)(B)) [S-105].

**Exceptions / defenses:** Collateral and blame-shifting portions are excluded (*Williamson v. United States*, 512 U.S. 594 (1994); *People v. Leach* (1975) 15 Cal.3d 419; *People v. Duarte* (2000) 24 Cal.4th 603) [S-508]. California reads the statement in context: a portion that is not itself disserving may come in if it is inextricably tied to a specifically disserving statement, judged by the circumstances in which it was made (*People v. Samuels* (2005) 36 Cal.4th 96; *People v. Grimes* (2016) 1 Cal.5th 698) [VERIFY V-1015]. Testimonial statements to police face Crawford.

**Authority:** FRE 804(b)(3) (as amended Dec. 1, 2024) [S-105]; CEC § 1230.

**MBE vs. CA essay:** California adds social interest and has no statutory corroboration clause (courts require trustworthiness).

**Example:** Before dying, X told his sister, "I set the warehouse fire." Admissible for D, who is charged with the arson, if corroborated (FRE): the court looks at the circumstances of the statement and at all the evidence — e.g., X's gasoline receipt supports it; D's own fingerprints on the gas can undermine it.

### R-EVD-105 — Dying declaration
**Rule (write this):** Under the FRE, in a homicide prosecution or a civil case, a statement made by a declarant who believed death was imminent, concerning its cause or circumstances, is admissible if the declarant is unavailable. In California, a dying person's statement about the cause and circumstances of his death, made on personal knowledge under a sense of immediately impending death, is admissible in any case.

**Elements:** 1. Belief in imminent death. 2. About cause or circumstances. 3. FRE: homicide or civil case; unavailable (need not die). CEC: declarant died; any case; personal knowledge.

**Exceptions / defenses:** Treated as a historical exception to Crawford (dictum).

**Authority:** FRE 804(b)(2); CEC § 1242.

**MBE vs. CA essay:** Differs in case type (California: any case) and death requirement.

**Example:** In an attempted-murder prosecution where the victim later dies, the FRE do not admit his dying declaration unless the charge is homicide; California admits it.

### R-EVD-106 — Forfeiture by wrongdoing
**Rule (write this):** A statement is admissible against a party that wrongfully caused, or acquiesced in wrongfully causing, the declarant's unavailability and did so intending that result; the party forfeits both the hearsay objection and the confrontation right.

**Elements:** 1. Wrongdoing (not necessarily criminal). 2. Caused unavailability. 3. Intent to prevent testimony. 4. Preponderance.

**Exceptions / defenses:** Killing without intent to prevent testimony does not forfeit confrontation (*Giles v. California*, 554 U.S. 353 (2008)).

**Authority:** FRE 804(b)(6); CEC § 1390 (enacted by AB 1723 (2010), in force from 2011; its Jan. 1, 2016 sunset was repealed in 2015 by AB 593) [S-513] [S-1552].

**MBE vs. CA essay:** Same principle, but § 1390 adds conditions: the party must have engaged in, or aided and abetted, wrongdoing that was intended to, and did, procure the declarant's unavailability; the proponent proves it by a preponderance at a foundational hearing outside the jury; the finding may not rest solely on the declarant's unconfronted statement and must be supported by **independent corroborative evidence**; and the judge may consider whether the statement is trustworthy and reliable [S-1552].

**Example:** D threatens a witness's family until she flees the state before trial; her prior statements to police are admissible against D.

### R-EVD-107 — Residual exception
**Rule (write this):** Under the FRE, a hearsay statement not admissible under another exception is admissible if it is supported by sufficient guarantees of trustworthiness, considering the totality of circumstances and any corroboration, and is more probative on the point than any other evidence reasonably obtainable, with advance written notice. California has no residual exception.

**Elements:** 1. Trustworthiness (totality + corroboration). 2. Necessity (more probative than alternatives). 3. Notice.

**Exceptions / defenses:** Used sparingly; testimonial statements still face Crawford.

**Authority:** FRE 807 (as amended 2019).

**MBE vs. CA essay:** Differs: on a CEC essay, write "California has no residual exception."

**Example:** A detailed, sworn statement by a deceased eyewitness that misses 804(b)(1) may qualify under 807 if strongly corroborated.

### R-EVD-108 — Other federal exceptions
**Rule (write this):** Other hearsay exceptions include ancient documents prepared before January 1, 1998 whose authenticity is established, market reports, reputation concerning character, family and property records, and a final judgment of a felony conviction offered to prove a fact essential to the judgment.

**Elements:** For 803(22): 1. Judgment after trial or guilty plea (not nolo). 2. Crime punishable by more than one year. 3. Fact essential to the judgment. 4. Prosecution may use against others only for impeachment.

**Exceptions / defenses:** Pending appeal does not affect admissibility.

**Authority:** FRE 803(9)–(23), 804(b)(4).

**MBE vs. CA essay:** California counterparts are scattered (e.g., § 1300 judgments [VERIFY V-409]).

**Example:** In a civil suit for assault damages, D's felony assault conviction after trial is admissible to prove he committed the assault.

### R-EVD-109 — California-only exceptions
**Rule (write this):** California admits statements of an unavailable declarant narrating or describing the infliction or threat of physical injury upon the declarant, made at or near the time, within five years before the action, under trustworthy circumstances, and in writing, electronically recorded, or made to a physician, nurse, paramedic or law enforcement official; it also has specific exceptions for child-abuse statements, decedents' statements in actions against their estates, and felony judgments in civil actions.

**Elements:** § 1370: 1. Unavailable. 2. Narrates infliction or threat on the declarant. 3. At or near the time. 4. Within five years of filing. 5. Trustworthy. 6. Writing, recording, or to medical or police personnel. 7. Notice.

**Exceptions / defenses:** Testimonial statements (to police after the emergency) remain barred by Crawford unless the declarant was cross-examined.

**Authority:** CEC §§ 1370 [S-501], 1360 [VERIFY V-413], 1261 and 1300 [VERIFY V-409].

**MBE vs. CA essay:** California only.

**Example:** A domestic-violence victim who has since died wrote in her diary, the night of an attack, "D choked me tonight." § 1370 can admit it in D's prosecution (a diary entry is nontestimonial).

### R-EVD-110 — Confrontation Clause: the Crawford rule
**Rule (write this):** In a criminal prosecution, the Confrontation Clause bars admission of a testimonial statement of a declarant who does not testify at trial unless the declarant is unavailable and the defendant had a prior opportunity for cross-examination.

**Elements:** 1. Criminal case, offered by the prosecution. 2. Hearsay offered for its truth. 3. Testimonial. 4. Declarant does not testify. 5. Unavailability plus prior cross → admissible.

**Exceptions / defenses:** Declarant testifies and is subject to cross; non-truth purpose; forfeiture by wrongdoing (*Giles*); dying declarations (historical, dictum).

**Authority:** U.S. Const. amend. VI; *Crawford v. Washington*, 541 U.S. 36 (2004).

**MBE vs. CA essay:** Same in all courts; Truth-in-Evidence cannot override it.

**Example:** The victim's recorded station-house statement naming D, made the day after the assault, is inadmissible if the victim does not testify and D never cross-examined her.

### R-EVD-111 — Testimonial statements: the primary-purpose test
**Rule (write this):** A statement is testimonial when its primary purpose, viewed objectively, is to establish or prove past events potentially relevant to later criminal prosecution; statements made to enable police to meet an ongoing emergency, and most statements to people who are not law enforcement, are nontestimonial.

**Elements:** Factors: ongoing emergency; formality; who asked and why; declarant's condition; whether describing past events or present danger; recipient (police vs. teacher, friend).

**Exceptions / defenses:** A conversation can shift from nontestimonial to testimonial once the emergency ends.

**Authority:** *Davis v. Washington*, 547 U.S. 813 (2006) (with *Hammon v. Indiana*); *Michigan v. Bryant*, 562 U.S. 344 (2011); *Ohio v. Clark*, 576 U.S. 237 (2015).

**MBE vs. CA essay:** Same.

**Example:** A 911 caller says, "He's hitting me — he's still here!" (nontestimonial). Ten minutes later, after police arrive and separate the parties, she writes a statement describing the attack (testimonial).

### R-EVD-112 — Forensic reports and expert conduits
**Rule (write this):** A forensic report prepared to prove a fact at trial is testimonial, so the analyst who made it must be available for cross-examination, and a surrogate who did not perform or observe the test cannot substitute; when an expert relays an absent analyst's statements as the basis of an opinion that depends on their truth, the statements are offered for their truth.

**Elements:** 1. Report created for prosecution use. 2. Analyst's availability. 3. Expert basis: truth-dependence; then testimonial?

**Exceptions / defenses:** Notice-and-demand statutes may require the defendant to request the analyst.

**Authority:** *Melendez-Diaz v. Massachusetts*, 557 U.S. 305 (2009); *Bullcoming v. New Mexico*, 564 U.S. 647 (2011); *Smith v. Arizona* (2024) [VERIFY V-035]; *People v. Sanchez* (2016) 63 Cal.4th 665.

**MBE vs. CA essay:** Same; California's Sanchez rule also applies outside criminal cases as a hearsay rule.

**Example:** The state offers a lab certificate that the powder was cocaine without calling the chemist — Confrontation Clause violation.

### R-EVD-113 — Codefendant confessions (Bruton)
**Rule (write this):** In a joint trial, admitting a nontestifying codefendant's confession that facially incriminates the defendant violates the Confrontation Clause even with a limiting instruction; a confession redacted to eliminate the defendant's name and any reference to his existence, or to refer neutrally to another person without obvious redaction, may be admitted with a limiting instruction.

**Elements:** 1. Joint trial. 2. Codefendant does not testify. 3. Confession facially incriminates (name, obvious blank) vs. neutral redaction. 4. Remedies: sever, redact, exclude.

**Exceptions / defenses:** If the codefendant testifies and is cross-examined, no Bruton problem.

**Authority:** *Bruton v. United States*, 391 U.S. 123 (1968); *Richardson v. Marsh*, 481 U.S. 200 (1987); *Gray v. Maryland*, 523 U.S. 185 (1998); *Samia v. United States* (2023) [VERIFY V-035].

**MBE vs. CA essay:** Same.

**Example:** A's confession says "B and I robbed the store"; in a joint trial where A does not testify, it cannot be admitted unredacted against B.

### R-EVD-114 — Face-to-face confrontation
**Rule (write this):** The Confrontation Clause guarantees a face-to-face meeting with witnesses at trial, which may be dispensed with only on a case-specific finding that the procedure is necessary to protect a particular child witness from trauma caused by the defendant's presence, with the testimony's reliability otherwise assured.

**Elements:** 1. Procedure limiting face-to-face contact (screen, one-way video). 2. Individualized finding of necessity. 3. Oath, cross, observation of demeanor preserved.

**Exceptions / defenses:** A generalized statutory presumption of trauma is not enough.

**Authority:** *Coy v. Iowa*, 487 U.S. 1012 (1988); *Maryland v. Craig*, 497 U.S. 836 (1990); *Pitts v. Mississippi*, 607 U.S. 1 (2025) (per curiam) [S-1721].

**MBE vs. CA essay:** Same.

**Example:** A court places a screen between a 7-year-old and the defendant under a statute, without hearing evidence about this child — Confrontation Clause violation.

### R-EVD-115 — Right to present a defense
**Rule (write this):** Due process and the Compulsory Process Clause forbid applying evidence rules mechanically or arbitrarily to exclude reliable, critical defense evidence, such as another person's trustworthy confessions or evidence of third-party guilt.

**Elements:** 1. Evidence critical to the defense. 2. Reliability indicators. 3. Rule applied arbitrarily or disproportionately to its purpose.

**Exceptions / defenses:** States may still exclude unreliable or marginally relevant evidence under ordinary rules.

**Authority:** *Chambers v. Mississippi*, 410 U.S. 284 (1973); *Holmes v. South Carolina*, 547 U.S. 319 (2006); *Rock v. Arkansas*, 483 U.S. 44 (1987).

**MBE vs. CA essay:** Same.

**Example:** A trial court excludes three corroborated confessions by another man solely because the hearsay rule lacks a matching exception; the exclusion may violate due process.
