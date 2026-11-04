# VERIFY-QUEUE

Every uncertain fact in the repo is tagged inline as `[VERIFY V-###]` and logged here.
`scripts/validate.py` fails if an inline tag has no entry here, or if a bare `[VERIFY]` (no ID) appears in content.

**How to clear an item:** confirm it against the primary source named in the row, fix the content, remove the inline tag,
add the source to `00-exam-intel/sources.md`, and move the row to *Resolved* with the date and the source ID.

**Verification strength used in this repo**

| Level | Meaning |
|---|---|
| `confirmed-primary` | Text read on the primary source (calbar.ca.gov, ncbex.org, leginfo, courts, Cornell LII, supremecourt.gov, ABA). |
| `confirmed-primary (search)` | Primary-source text quoted back by a web search index, not read on the page itself. Good, but re-check by direct fetch when access allows. |
| `secondary` | Only a secondary source (news, law school, commercial site) supports it. Always carries a `[VERIFY]` tag. |
| `unconfirmed` | No source found. Always carries a `[VERIFY]` tag. |

## Open

| ID | File | Claim to verify | Why uncertain | Primary source to check | Priority | Opened |
|---|---|---|---|---|---|---|
| V-001 | 00-exam-intel/sources.md | Every source marked `search`: re-read the page directly and confirm the quoted facts | Phase 0 network policy blocked direct fetch | Each URL in sources.md | High | 2026-11-04 |
| V-002 | 00-exam-intel/format-and-scoring.md | Whether Examplify allows moving unused time between essays and the PT within a session | Not found | July 2027 bulletin / laptops page [S-008] | Med | 2026-11-04 |
| V-003 | 00-exam-intel/format-and-scoring.md | Third grading phase eliminated with the 1390 cut (July 2020) | Single source | Grading page [S-010] | Low | 2026-11-04 |
| V-004 | 00-exam-intel/format-and-scoring.md | No merits appeal of essay grades | Not searched | Grading / results pages | Low | 2026-11-04 |
| V-005 | 00-exam-intel/format-and-scoring.md | California MBE scaled score = NCBE scaled score × 10 | Inference | Scaling Explained [S-081] | Low | 2026-11-04 |
| V-006 | 00-exam-intel/format-and-scoring.md | Nov 2024 study adjustment does not apply to July 2027 | Inference from "2025 or 2026" wording | Supreme Court order [S-038] | Low | 2026-11-04 |
| V-007 | 00-exam-intel/format-and-scoring.md | July 2026 foreign-educated pass rates (12.9% first-time, 10.2% repeat) | Preliminary figures, single search pass | July 2026 statistics PDF (when posted) | Low | 2026-11-04 |
| V-008 | 00-exam-intel/format-and-scoring.md | Current text and subdivision numbering of B&P § 6046.6 after SB 253 | Not read verbatim | leginfo § 6046.6 | Low | 2026-11-04 |
| V-009 | 00-exam-intel/format-change-tracker.md | Explicit statement that Feb 2028 uses the current GBX format | Only implied (last stand-alone MBE Feb 2028) | Feb 2028 exam page when posted | High | 2026-11-04 |
| V-010 | 00-exam-intel/format-change-tracker.md | California component: final recommendation due June 2027; candidate subject list | From State Bar news description, page not pinned | Supreme Court order text; [S-039] | Low | 2026-11-04 |
| V-011 | 00-exam-intel/format-change-tracker.md | AB 2109 (UBE switch by 2029) final status | No history found after Mar 2026 | leginfo bill status [S-031] | Low | 2026-11-04 |
| V-012 | 00-exam-intel/admissions-checklist.md | Whether the user's PRC credential counts as being "fully admitted ... without restrictions"; which PRC authority issues an acceptable Certificate of Good Standing; electronic acceptance | No PRC-specific primary source | **User's documents + written answer from the Office of Admissions** | **Critical** | 2026-11-04 |
| V-013 | 00-exam-intel/admissions-checklist.md | 2024 Guidelines are operative: PR mandatory; 12 bar-subject units suggested (degree) or required (non-degree); 36-month limit | Older web page conflicts | Guidelines PDF [S-052]; June 21, 2024 CBE minutes | High | 2026-11-04 |
| V-014 | 00-exam-intel/admissions-checklist.md | Online LLM units from an ABA-approved school are accepted for rule 4.30(A) | No primary text either way | **Written eligibility determination from the Office of Admissions** | **Critical** | 2026-11-04 |
| V-015 | 00-exam-intel/admissions-checklist.md | Non-degree "20 units completed" option, and conditional clearance, for an LLM finishing near the exam | Unconfirmed | Office of Admissions; [S-052] [S-057] | **Critical if LLM ends after ~June 2027** | 2026-11-04 |
| V-016 | 00-exam-intel/admissions-checklist.md | July 2027 deadlines: application open ~Mar 1; timely Apr 1; final Jun 1; eligibility ~Jul 13; test-center change ~early Jul; laptop/mock ~Jul 23; upload ~Jul 29 | Not yet published; estimated from rules and 2026 pattern | July 2027 exam page | High | 2026-11-04 |
| V-017 | 00-exam-intel/admissions-checklist.md | Approved credential-evaluator list is current; agency fees and turnaround | List possibly stale | [S-056]; agency sites | Med | 2026-11-04 |
| V-018 | 00-exam-intel/admissions-checklist.md | Late-laptop fee $60 vs. $100 | Conflicting fee-schedule versions | Appendix A [S-028] | Low | 2026-11-04 |
| V-019 | 00-exam-intel/admissions-checklist.md | Whether the 90-day law-student registration rule applies to foreign LLM students | Unconfirmed | Registration page [S-059]; Title 4 | Med | 2026-11-04 |
| V-020 | 00-exam-intel/admissions-checklist.md | Fingerprint processing fee; New Attorney Training completion deadline | Not found | [S-064]; NAT rules | Low | 2026-11-04 |
| V-021 | 00-exam-intel/grader-expectations.md | 2026 booklets still carry the "lawyer-like manner" sentence; 2026 PT instruction wording | Matches came from older booklets | Jul 2026 booklet [S-078] | Low | 2026-11-04 |
| V-022 | 00-exam-intel/grader-expectations.md | PR outline scope sentence includes the ABA Model Rules/Model Code | Paraphrased in search output | PR outline PDF [S-082] | Med | 2026-11-04 |
| V-023 | 00-exam-intel/coverage-matrix-guide.md | 97 MBE rows with approximate wording; Torts IV.D not confirmed for the MBE | Search paraphrase | MBE outline PDF [S-040] | Med | 2026-11-04 |
| V-024 | 00-exam-intel/coverage-matrix-guide.md | CBX rows paraphrased or conflicting (incl. Wills III.E vs. V); CBX coverage IDs provisional | Search paraphrase | 13 CBX outline PDFs [S-082]–[S-094] | High (before Phase 4) | 2026-11-04 |
| V-025 | 00-exam-intel/coverage-matrix-guide.md | Ten CBX outline sections not captured (SUP stand-in rows added) | Not returned by search | 13 CBX outline PDFs | High (before Phase 4) | 2026-11-04 |
| V-026 | 00-exam-intel/coverage-matrix-guide.md | The undated CBX essay outlines remain the official essay scope; PR asterisk footnote on Scope page | No date or reaffirmation found | Scope page [S-041]; Office of Admissions | Med | 2026-11-04 |
| V-027 | 00-exam-intel/recent-changes.md | No NCBE lag policy and no State Bar cutoff for testable law; no 28 U.S.C. §§ 1332/1391/1441 amendments since 2011 | Absence not confirmed | ncbex.org; calbar.ca.gov; uscode.house.gov | Med | 2026-11-04 |
| V-028 | 00-exam-intel/recent-changes.md | FRE 801(d)(1)(A) amendment took effect Dec 1, 2026 (Congress did not act); exact text | Pending at Phase 0 | uscourts.gov current FRE text | High | 2026-11-04 |
| V-029 | 00-exam-intel/recent-changes.md | SB 66 effective date; CCP § 231.7 application to civil trials from Jan 1, 2026 | Secondary only / missing | leginfo | Low | 2026-11-04 |
| V-030 | 00-exam-intel/recent-changes.md | AB 2556 effective date; Truth-in-Evidence status not re-checked | Not confirmed | leginfo; Cal. Const. art. I, § 28 | Low | 2026-11-04 |
| V-031 | 00-exam-intel/recent-changes.md | Adoption status of CA RPC AI amendments before July 2027; AB 931 section number | Pending / secondary | calbar ethics news; leginfo | Med | 2026-11-04 |
| V-032 | 00-exam-intel/recent-changes.md | New ABA Model Rule 1.14 title and text | Not retrieved | ABA [S-127] | Low | 2026-11-04 |
| V-033 | 00-exam-intel/recent-changes.md | Haggerty v. Thornton: disapproved Court of Appeal case and pin cites | Secondary | Official opinion | Low | 2026-11-04 |
| V-034 | 00-exam-intel/recent-changes.md | OT2025 U.S. Supreme Court holdings (about half secondary-sourced) | Secondary | supremecourt.gov slip opinions | High (before Phase 4 Con Law/Crim/Civ Pro) | 2026-11-04 |
| V-035 | 00-exam-intel/recent-changes.md | OT2022–OT2024 U.S. Supreme Court holdings listed from model knowledge | Not re-checked in Phase 0 | supremecourt.gov | Med | 2026-11-04 |
| V-036 | 00-exam-intel/recent-changes.md | Kuciemba v. Victory Woodworks (2023) holding and citation | Secondary only | Official opinion | Low | 2026-11-04 |
| V-060 | 01-study-plan/practice-targets.md | State Bar withdrawal deadline and refund rules for the July 2027 exam (needed for the CP4 sit-or-defer decision) | Not researched | July 2027 exam page; Appendix A [S-028] | Med | 2026-11-04 |

## Resolved

| ID | File | Claim | Resolution | Source | Resolved |
|---|---|---|---|---|---|
