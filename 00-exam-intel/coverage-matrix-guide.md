---
subject: exam-intel
topic: Coverage matrix — schema, ID scheme, status and known gaps
coverage_ids: []
tested_on: [none]
exam_frequency: {level: n/a, basis: "Reference file, not a tested topic"}
last_verified: 2026-11-04
status: draft
---

# Coverage matrix guide

`coverage-matrix.csv` defines what "complete" means for this repo. Every topic the exam can test is a row. Every row must point to the file and heading that teaches it. `scripts/validate.py` fails if any row is unmapped.

## Where the rows come from (v1 Phase 0; v1.1 after Phase 3)

| `source` | Meaning | Rows | Built from |
|---|---|---|---|
| `MBE` | NCBE MBE Subject Matter Outline: every category, topic and subtopic in NCBE's numbering | 387 | [S-040], reconstructed line by line via search (`research/phase0-ncbe-mbe-outline.csv`) |
| `CBX` | State Bar essay outlines (the `CBX-Outline-*.pdf` "content maps") for all 13 subjects | 176 | [S-082]–[S-094], reconstructed via search (`research/phase0-calbar-essay-outlines.csv`) |
| `SUP` | Author-added rows: California distinctions the scope statements require, and stand-ins for outline sections the search could not capture | 51 | Scope statements [S-082] [S-083] [S-084], plus Phase 0 gap list |
| `PAST` | Issues from published California essays (2012–2026) that no existing row covered | 2 | `06-past-exams/index.csv` (Phase 3: 166 essays, 410+ issue tags; all other issues mapped to existing rows) |

Total **616 rows**. By verification status, **434** are `confirmed-primary` (search-quoted primary text) and **182** are `unconfirmed`. Phase 3 tagged every published essay's issues to these rows; frequency by subject is in `06-past-exams/frequency-analysis.md`.

| Subject | Code | Rows | Confirmed | Unconfirmed | CA-specific |
|---|---|---|---|---|---|
| Business Associations | BUS | 13 | 1 | 12 | 0 |
| Civil Procedure | CIV | 50 | 35 | 15 | 11 |
| Community Property | CMP | 51 | 18 | 33 | 51 |
| Constitutional Law | CON | 68 | 61 | 7 | 0 |
| Contracts | CTR | 45 | 38 | 7 | 0 |
| Criminal Law and Procedure | CRM | 53 | 46 | 7 | 1 |
| Evidence | EVD | 92 | 76 | 16 | 9 |
| Professional Responsibility | PRF | 18 | 4 | 14 | 18 |
| Real Property | PRP | 104 | 97 | 7 | 0 |
| Remedies | REM | 11 | 2 | 9 | 0 |
| Torts | TRT | 49 | 42 | 7 | 0 |
| Wills and Succession | WIL | 42 | 10 | 32 | 42 |
| Trusts | TRS | 18 | 3 | 15 | 18 |
| Performance Test | PT | 2 | 1 | 1 | 0 |

**The weak spots are the California-only subjects.** The State Bar's essay outlines for Business Associations, Professional Responsibility, Remedies, Trusts and Wills came back mostly paraphrased, so those rows are thin and "unconfirmed". **Phase 3 (past-exam issues) is the main fix.** Every issue tested on a published California essay becomes a `PAST` row, which gives those subjects a frequency-weighted, verified topic list before Phase 4 content is written.

## Columns

| Column | Values / rule |
|---|---|
| `coverage_id` | `<SUBJ>-<SOURCE>-<ref>`, e.g. `EVD-MBE-V.F`, `CMP-CBX-II.C.x1.a`, `CIV-SUP-006`. Stable once Phase 4 begins. |
| `subject_code` / `subject` | One of the 13 subject codes above, or `PT` |
| `source` | `MBE`, `CBX`, `SUP`, `PAST` |
| `source_ref` | Human-readable pointer into the source document |
| `level` | `category` > `topic` > `subtopic` > `item` |
| `parent_id` | `coverage_id` of the parent row, or blank |
| `heading` | Topic text as the source states it. Bracketed notes such as `[letter inferred]` are research annotations. |
| `tested_on` | `;`-separated: `MBE`, `essay`, `PT` |
| `ca_specific` | `Y` if California law governs or a CA-vs-federal distinction is tested |
| `weight_note` | NCBE distribution note, for MBE category rows |
| `target_file` / `target_heading` | Where the topic is taught. In v1 every target is **planned** (the file does not exist yet). |
| `mapping_status` | `planned` → `mapped` (heading exists; the validator checks it) → `verified` (Phase 7 QA) |
| `source_status` | `confirmed-primary`, `secondary`, `unconfirmed` |
| `source_id` | `S-###` from `sources.md` |
| `notes` | Provenance notes, e.g. "wording approximate" |

## Conventions for Phase 4 authors
- **MBE subjects:** `outline.md` follows NCBE numbering (`## I Jurisdiction and venue`, `### I.A Federal subject-matter jurisdiction`), so MBE rows map one-to-one. CBX and SUP rows for MBE subjects map either to the matching NCBE heading or to a heading in `ca-distinctions.md`.
- **California-only subjects:** `outline.md` follows the State Bar essay outline's structure, corrected against the PDF once it can be read directly.
- When you write a heading that covers a row, update its `target_heading` to the real heading text and set `mapping_status` to `mapped`. The validator then checks that the heading exists. The check is a case-insensitive substring match.
- **Never delete a row to make validation pass.** If a row is a duplicate, map it to the same heading and note the duplicate.

## Known gaps and provisional items
- 97 MBE rows have approximately quoted wording, and Torts IV.D (interference with business relations) is not confirmed for the MBE [VERIFY V-023].
- CBX rows are mostly paraphrased, and their `coverage_id`s stay provisional until the 13 outline PDFs are read directly [VERIFY V-024].
- Ten outline sections were not captured at all. SUP rows stand in for them [VERIFY V-025].
- The CBX outlines are undated. Whether they remain the official essay scope is unconfirmed, though nothing indicates they were withdrawn [VERIFY V-026].
- `PAST` rows were added in Phase 3: `BUS-PAST-001` and `WIL-PAST-001`.
