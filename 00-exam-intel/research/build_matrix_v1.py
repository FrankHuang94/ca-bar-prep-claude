#!/usr/bin/env python3
"""HISTORICAL — Phase 0 one-time builder for 00-exam-intel/coverage-matrix.csv (v1).

Do NOT re-run after Phase 1: the matrix is hand-maintained from then on and this
script would overwrite mappings. Kept for provenance only.

Original description:

Sources:
  research/C-mbe-outline.csv  (NCBE MBE Subject Matter Outline, reconstructed via search)
  research/D-ca-scope.csv     (State Bar CBX-Outline-*.pdf essay outlines, reconstructed via search)
  SUP rows below              (author-added rows for CA distinctions / outline gaps; pending confirmation)
"""
import csv
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RES = HERE
OUT = HERE.parent / "coverage-matrix.csv"

COLUMNS = ["coverage_id", "subject_code", "subject", "source", "source_ref", "level", "parent_id",
           "heading", "tested_on", "ca_specific", "weight_note", "target_file", "target_heading",
           "mapping_status", "source_status", "source_id", "notes"]

SUBJ = {  # name -> (code, folder slug, CBX outline source id)
    "Business Associations": ("BUS", "business-associations", "S-085"),
    "Civil Procedure": ("CIV", "civil-procedure", "S-084"),
    "Community Property": ("CMP", "community-property", "S-086"),
    "Constitutional Law": ("CON", "constitutional-law", "S-087"),
    "Contracts": ("CTR", "contracts", "S-088"),
    "Criminal Law and Procedure": ("CRM", "criminal-law-procedure", "S-089"),
    "Evidence": ("EVD", "evidence", "S-083"),
    "Professional Responsibility": ("PRF", "professional-responsibility", "S-082"),
    "Real Property": ("PRP", "real-property", "S-090"),
    "Remedies": ("REM", "remedies", "S-091"),
    "Torts": ("TRT", "torts", "S-092"),
    "Wills and Succession": ("WIL", "wills-succession", "S-094"),
    "Trusts": ("TRS", "trusts", "S-093"),
}
CODE_NAME = {v[0]: k for k, v in SUBJ.items()}
CODE_SLUG = {v[0]: v[1] for v in SUBJ.values()}
CA_LAW_SUBJECTS = {"Community Property", "Wills and Succession", "Trusts", "Professional Responsibility"}
MBE_SUBJECTS = {"Civil Procedure", "Constitutional Law", "Contracts", "Criminal Law and Procedure",
                "Evidence", "Real Property", "Torts"}
MBE_LEVEL = {"category": "category", "topic": "topic", "subtopic": "subtopic", "sub-subtopic": "item"}
CBX_LEVEL = {"0": "item", "1": "category", "2": "topic", "3": "subtopic", "4": "item"}

# NCBE distribution notes -> category weight notes (25 scored questions per subject) [S-040]
WEIGHTS = {
    ("CIV", "I"): "I+III+V together ~2/3 of CivPro MBE (~17 of 25 scored)",
    ("CIV", "III"): "I+III+V together ~2/3 of CivPro MBE (~17 of 25 scored)",
    ("CIV", "V"): "I+III+V together ~2/3 of CivPro MBE (~17 of 25 scored)",
    ("CIV", "II"): "II+IV+VI+VII together ~1/3 of CivPro MBE (~8 of 25 scored)",
    ("CIV", "IV"): "II+IV+VI+VII together ~1/3 of CivPro MBE (~8 of 25 scored)",
    ("CIV", "VI"): "II+IV+VI+VII together ~1/3 of CivPro MBE (~8 of 25 scored)",
    ("CIV", "VII"): "II+IV+VI+VII together ~1/3 of CivPro MBE (~8 of 25 scored)",
    ("CON", "IV"): "~1/2 of Con Law MBE (~12-13 of 25 scored)",
    ("CON", "I"): "I+II+III together ~1/2 of Con Law MBE",
    ("CON", "II"): "I+II+III together ~1/2 of Con Law MBE",
    ("CON", "III"): "I+II+III together ~1/2 of Con Law MBE",
    ("CTR", "I"): "I+IV together ~1/2 of Contracts MBE; ~1/4 of all Contracts Qs are UCC Arts 1-2",
    ("CTR", "IV"): "I+IV together ~1/2 of Contracts MBE; ~1/4 of all Contracts Qs are UCC Arts 1-2",
    ("CTR", "II"): "Remaining categories ~1/2 [second half of NCBE sentence unconfirmed]",
    ("CTR", "III"): "Remaining categories ~1/2 [second half of NCBE sentence unconfirmed]",
    ("CTR", "V"): "Remaining categories ~1/2 [second half of NCBE sentence unconfirmed]",
    ("CTR", "VI"): "Remaining categories ~1/2 [second half of NCBE sentence unconfirmed]",
    ("CRM", "V"): "~1/2 of Crim MBE (constitutional protections; ~12-13 of 25 scored)",
    ("CRM", "I"): "I-IV together ~1/2 of Crim MBE",
    ("CRM", "II"): "I-IV together ~1/2 of Crim MBE",
    ("CRM", "III"): "I-IV together ~1/2 of Crim MBE",
    ("CRM", "IV"): "I-IV together ~1/2 of Crim MBE",
    ("EVD", "I"): "~1/4 of Evidence MBE (~6 of 25 scored)",
    ("EVD", "II"): "~1/3 of Evidence MBE (~8 of 25 scored)",
    ("EVD", "V"): "~1/4 of Evidence MBE (~6 of 25 scored)",
    ("EVD", "III"): "III+IV together = remainder (~1/6, ~4 of 25 scored)",
    ("EVD", "IV"): "III+IV together = remainder (~1/6, ~4 of 25 scored)",
    ("PRP", "I"): "~1/5 of Real Property MBE (~5 of 25 scored)",
    ("PRP", "II"): "~1/5 of Real Property MBE (~5 of 25 scored)",
    ("PRP", "III"): "~1/5 of Real Property MBE (~5 of 25 scored)",
    ("PRP", "IV"): "~1/5 of Real Property MBE (~5 of 25 scored)",
    ("PRP", "V"): "~1/5 of Real Property MBE (~5 of 25 scored)",
    ("TRT", "II"): "~1/2 of Torts MBE (negligence; ~12-13 of 25 scored)",
    ("TRT", "I"): "I+III+IV together ~1/2 of Torts MBE",
    ("TRT", "III"): "I+III+IV together ~1/2 of Torts MBE",
    ("TRT", "IV"): "I+III+IV together ~1/2 of Torts MBE",
}


def clean_heading(h: str) -> str:
    """Short planned heading: drop bracket notes, leading numerals/letters, trailing parentheticals."""
    h = re.sub(r"\[[^\]]*\]", "", h)
    h = re.sub(r"^\s*(?:[IVX]+|[A-Z]|\d+|[a-z])\.\s+", "", h.strip())
    h = re.sub(r"\s*\(.*\)\s*$", "", h)
    h = re.sub(r"\s+", " ", h).strip(" :;-")
    return h


def mbe_status(s):
    s = s.upper()
    if s.startswith("CONFIRMED-APPROX"):
        return "confirmed-primary", "wording approximate in search output; verify against PDF"
    if s.startswith("CONFIRMED"):
        return "confirmed-primary", ""
    return "unconfirmed", "UNCONFIRMED in Phase 0 research; verify against PDF"


def cbx_status(s):
    s = s.upper()
    if s.startswith("CONFIRMED"):
        return "confirmed-primary", ""
    if s.startswith("CONFLICTING"):
        return "unconfirmed", "CONFLICTING numbering/placement across search summaries; verify against PDF"
    return "unconfirmed", "wording/numbering paraphrased by search summary; verify against PDF"


def build():
    rows, ids = [], set()

    def add(r):
        if r["coverage_id"] in ids:
            sys.exit(f"duplicate id {r['coverage_id']}")
        ids.add(r["coverage_id"])
        rows.append(r)

    # ---------------- MBE rows ----------------
    with (RES / "phase0-ncbe-mbe-outline.csv").open(newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            if r["level"] == "note":
                continue
            subj = r["subject"].strip()
            code, slug, _ = SUBJ[subj]
            ref = r["ncbe_ref"].strip()
            st, note = mbe_status(r["status"])
            head = r["heading"].strip()
            add({
                "coverage_id": f"{code}-MBE-{ref}",
                "subject_code": code, "subject": subj, "source": "MBE",
                "source_ref": f"NCBE MBE Subject Matter Outline {subj} {ref}",
                "level": MBE_LEVEL[r["level"]],
                "parent_id": f"{code}-MBE-{r['parent_ref'].strip()}" if r["parent_ref"].strip() else "",
                "heading": head, "tested_on": "MBE;essay", "ca_specific": "N",
                "weight_note": WEIGHTS.get((code, ref), ""),
                "target_file": f"03-subjects/{slug}/outline.md",
                "target_heading": f"{ref} {clean_heading(head)}",
                "mapping_status": "planned", "source_status": st, "source_id": "S-040", "notes": note,
            })

    # ---------------- CBX rows ----------------
    gaps = []
    with (RES / "phase0-calbar-essay-outlines.csv").open(newline="", encoding="utf-8") as fh:
        cbx = list(csv.DictReader(fh))
    for r in cbx:
        subj = r["subject"].strip()
        if subj not in SUBJ:  # Feb-2025-only MCQ maps etc.
            continue
        code, slug, src = SUBJ[subj]
        raw = r["calbar_ref"].strip()
        status = r["status"].strip().upper()
        if status.startswith("NOT FOUND"):
            gaps.append(f"{subj}: {r['heading'].strip()}")
            continue
        if r["level"].strip() == "0" and not raw.startswith("WS-stat"):
            continue  # boilerplate / governing-law statements (kept in exam-intel prose)
        ref = re.sub(r"^[A-Z]{1,3}-", "", raw)
        st, note = cbx_status(r["status"])
        pref = r["parent_ref"].strip()
        parent = ""
        if pref and " or " not in pref:
            parent = f"{code}-CBX-{re.sub(r'^[A-Z]{1,3}-', '', pref)}"
        head = r["heading"].strip()
        is_ca = subj in CA_LAW_SUBJECTS or bool(re.search(r"California|anti-SLAPP|demurrer|CCP|Evidence Code|Probate", head))
        add({
            "coverage_id": f"{code}-CBX-{ref}",
            "subject_code": code, "subject": subj, "source": "CBX",
            "source_ref": f"State Bar essay outline {subj} {ref}",
            "level": CBX_LEVEL.get(r["level"].strip(), "item"),
            "parent_id": parent, "heading": head,
            "tested_on": "essay;PT", "ca_specific": "Y" if is_ca else "N",
            "weight_note": "",
            "target_file": f"03-subjects/{slug}/" + ("ca-distinctions.md" if is_ca and subj in MBE_SUBJECTS else "outline.md"),
            "target_heading": clean_heading(head) or head,
            "mapping_status": "planned", "source_status": st, "source_id": src,
            "notes": "; ".join(x for x in [note, "coverage_id provisional until outline PDF is read directly" if st != "confirmed-primary" else ""] if x),
        })

    for r in rows:
        if r["parent_id"] and r["parent_id"] not in ids:
            r["notes"] = "; ".join(x for x in [r["notes"], f"parent {r['parent_id']} not in matrix"] if x)
            r["parent_id"] = ""

    # ---------------- SUP rows ----------------
    for code, n, heading, target, src, st, ca, note in SUP:
        subj = CODE_NAME.get(code, "Performance Test")
        slug = CODE_SLUG.get(code)
        tfile = target if "/" in target else f"03-subjects/{slug}/{target}"
        add({
            "coverage_id": f"{code}-SUP-{n:03d}",
            "subject_code": code, "subject": subj, "source": "SUP",
            "source_ref": "Author-added (Phase 0): CA distinction or outline gap",
            "level": "topic", "parent_id": "", "heading": heading,
            "tested_on": "PT" if code == "PT" else "essay",
            "ca_specific": ca, "weight_note": "",
            "target_file": tfile, "target_heading": clean_heading(heading) or heading,
            "mapping_status": "planned", "source_status": st, "source_id": src, "notes": note,
        })

    with OUT.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(rows)
    return rows, gaps


GAP = "Outline line not captured in Phase 0; author-added pending confirmation from outline PDF / Phase 3 past exams"
SCOPE = "Required by State Bar scope statement (compare/contrast CA and federal); specific sub-areas author-identified"
SUP = [
    # code, n, heading, target (file in subject folder or repo path), source, source_status, ca_specific, note
    ("EVD", 1, "Federal Rules of Evidence vs. California Evidence Code: compare and contrast", "ca-distinctions.md", "S-083", "confirmed-primary", "Y", "Scope statement quoted verbatim"),
    ("EVD", 2, "Proposition 8 / Right to Truth-in-Evidence in criminal cases and its exceptions", "ca-distinctions.md", "S-083", "unconfirmed", "Y", "Not a named outline heading; appears in selected answers per Phase 0 research; confirm in Phase 3"),
    ("EVD", 3, "Discretionary exclusion: California balancing vs. FRE 403", "ca-distinctions.md", "S-083", "unconfirmed", "Y", SCOPE),
    ("EVD", 4, "Character and propensity evidence: California vs. federal rules (incl. victim character; sexual assault and domestic violence cases)", "ca-distinctions.md", "S-083", "unconfirmed", "Y", SCOPE),
    ("EVD", 5, "Impeachment: California vs. federal rules (incl. prior convictions and prior inconsistent statements)", "ca-distinctions.md", "S-083", "unconfirmed", "Y", SCOPE),
    ("EVD", 6, "Hearsay definitions and exceptions: California vs. federal differences", "ca-distinctions.md", "S-083", "unconfirmed", "Y", SCOPE),
    ("EVD", 7, "Privileges: California statutory privileges vs. federal common-law privileges", "ca-distinctions.md", "S-083", "unconfirmed", "Y", SCOPE),
    ("EVD", 8, "Lay and expert opinion: California vs. federal standards", "ca-distinctions.md", "S-083", "unconfirmed", "Y", SCOPE),
    ("EVD", 9, "Secondary evidence rule (California) vs. best evidence rule (FRE)", "ca-distinctions.md", "S-083", "unconfirmed", "Y", SCOPE),
    ("CIV", 1, "Federal Rules of Civil Procedure vs. California Code of Civil Procedure: compare and contrast", "ca-distinctions.md", "S-084", "confirmed-primary", "Y", "Scope statement quoted verbatim"),
    ("CIV", 2, "California court subject-matter jurisdiction (superior courts; limited vs. unlimited civil cases)", "ca-distinctions.md", "S-084", "unconfirmed", "Y", SCOPE),
    ("CIV", 3, "California personal jurisdiction (long-arm statute) and service of process", "ca-distinctions.md", "S-084", "unconfirmed", "Y", SCOPE),
    ("CIV", 4, "California venue rules", "ca-distinctions.md", "S-084", "unconfirmed", "Y", SCOPE),
    ("CIV", 5, "California joinder and cross-complaints vs. federal counterclaims and crossclaims", "ca-distinctions.md", "S-084", "unconfirmed", "Y", SCOPE),
    ("CIV", 6, "California discovery differences (incl. initial disclosures on demand)", "ca-distinctions.md", "S-084", "unconfirmed", "Y", SCOPE),
    ("CIV", 7, "California summary judgment and summary adjudication", "ca-distinctions.md", "S-084", "unconfirmed", "Y", SCOPE),
    ("CIV", 8, "Claim preclusion: California primary rights theory vs. federal transactional test; issue preclusion", "ca-distinctions.md", "S-084", "unconfirmed", "Y", SCOPE),
    ("CIV", 9, "California jury trial right, jury size and verdict rules", "ca-distinctions.md", "S-084", "unconfirmed", "Y", SCOPE),
    ("CIV", 10, "California post-trial motions and appeals (final judgment rule; writs)", "ca-distinctions.md", "S-084", "unconfirmed", "Y", SCOPE),
    ("CIV", 11, "Discovery, summary judgment, trial, judgments, preclusion and appeals (CBX outline sections not captured)", "outline.md", "S-084", "unconfirmed", "N", GAP),
    ("PRF", 1, "California Rules of Professional Conduct vs. ABA Model Rules: compare and contrast", "ca-distinctions.md", "S-082", "confirmed-primary", "Y", "Scope statement; ABA portion wording unconfirmed"),
    ("PRF", 2, "State Bar Act (Bus. & Prof. Code) duties of attorneys, incl. statutory duty of confidentiality", "ca-distinctions.md", "S-082", "confirmed-primary", "Y", "Scope statement names relevant B&P sections"),
    ("PRF", 3, "Duty of confidentiality vs. attorney-client privilege and work product; exceptions", "outline.md", "S-082", "unconfirmed", "Y", GAP),
    ("PRF", 4, "Duty of loyalty: conflicts of interest (current clients, former clients, imputation, screening)", "outline.md", "S-082", "unconfirmed", "Y", GAP),
    ("PRF", 5, "Competence, diligence and communication", "outline.md", "S-082", "unconfirmed", "Y", GAP),
    ("PRF", 6, "Duty to report misconduct (California rule 8.3)", "outline.md", "S-082", "unconfirmed", "Y", "Recent rule (eff. 2023-08-01); see recent-changes.md"),
    ("PRF", 7, "Unauthorized practice of law and multijurisdictional practice", "outline.md", "S-082", "unconfirmed", "Y", GAP),
    ("CMP", 1, "Putative spouses and quasi-marital property", "outline.md", "S-086", "unconfirmed", "Y", GAP),
    ("CMP", 2, "Community payments on a spouse's separately owned real property (pro tanto apportionment)", "outline.md", "S-086", "unconfirmed", "Y", GAP),
    ("CMP", 3, "Post-separation payments and use of assets (reimbursement credits and use charges)", "outline.md", "S-086", "unconfirmed", "Y", GAP),
    ("CMP", 4, "Life insurance, stock options and other special assets", "outline.md", "S-086", "unconfirmed", "Y", GAP),
    ("CMP", 5, "Deviation from equal distribution: outline items VI.B.6-7 (not captured)", "outline.md", "S-086", "unconfirmed", "Y", GAP),
    ("WIL", 1, "Classification of testamentary gifts (specific, general, demonstrative, residuary)", "outline.md", "S-094", "unconfirmed", "Y", GAP),
    ("WIL", 2, "Ademption (by extinction; by satisfaction)", "outline.md", "S-094", "unconfirmed", "Y", GAP),
    ("WIL", 3, "Abatement", "outline.md", "S-094", "unconfirmed", "Y", GAP),
    ("WIL", 4, "Mistake and reformation of wills", "outline.md", "S-094", "unconfirmed", "Y", GAP),
    ("WIL", 5, "No-contest clauses", "outline.md", "S-094", "unconfirmed", "Y", GAP),
    ("WIL", 6, "Presumptive disqualification of certain donees (drafters, fiduciaries, care custodians)", "outline.md", "S-094", "unconfirmed", "Y", GAP),
    ("WIL", 7, "Will substitutes and nonprobate transfers", "outline.md", "S-094", "unconfirmed", "Y", GAP),
    ("TRS", 1, "Revocability of trusts: California default rule vs. majority rule; methods of revocation and modification", "outline.md", "S-093", "unconfirmed", "Y", GAP + "; see Haggerty v. Thornton in recent-changes.md"),
    ("TRS", 2, "Pour-over wills and testamentary additions to trusts", "outline.md", "S-093", "unconfirmed", "Y", GAP),
    ("TRS", 3, "Charitable trusts and cy pres", "outline.md", "S-093", "unconfirmed", "Y", GAP),
    ("REM", 1, "Provisional relief: temporary restraining orders and preliminary injunctions", "outline.md", "S-091", "unconfirmed", "N", GAP),
    ("REM", 2, "Limits on damages: causation, foreseeability, certainty, mitigation", "outline.md", "S-091", "unconfirmed", "N", GAP),
    ("REM", 3, "Punitive damages", "outline.md", "S-091", "unconfirmed", "N", GAP),
    ("CON", 1, "Constitutional Law CBX outline section IV (not captured; covered by MBE outline rows)", "outline.md", "S-087", "unconfirmed", "N", GAP),
    ("CTR", 1, "Contract defenses (statute of frauds, parol evidence, mistake, etc.) — CBX outline numbering not captured", "outline.md", "S-088", "unconfirmed", "N", GAP),
    ("CRM", 1, "Specific crimes and remaining criminal procedure (CBX outline sections II, IV and rest not captured)", "outline.md", "S-089", "unconfirmed", "N", GAP),
    ("CRM", 2, "California-specific criminal law distinctions (if any) on essays", "ca-distinctions.md", "S-089", "unconfirmed", "Y", "Confirm in Phase 3 whether essays test CA Penal Code distinctions"),
    ("PT", 1, "Performance Test method: File and Library, task memo compliance, 90-minute time plan", "04-performance-test/method.md", "S-076", "confirmed-primary", "N", "From State Bar PT instructions"),
    ("PT", 2, "Performance Test task types (enumerate from past PTs in Phase 3)", "04-performance-test/method.md", "S-079", "unconfirmed", "N", "Expand into one row per task type in Phase 3"),
]

if __name__ == "__main__":
    rows, gaps = build()
    from collections import Counter
    print("rows:", len(rows))
    print(Counter((r["subject_code"], r["source"]) for r in rows))
    print(Counter(r["source_status"] for r in rows))
    print("gap placeholders dropped:", len(gaps))
    for g in gaps:
        print("  -", g)
