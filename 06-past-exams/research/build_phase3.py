#!/usr/bin/env python3
"""Phase 3 builder: research records (phase3-index.jsonl) -> index CSVs, PAST coverage rows, analysis files.

Input   06-past-exams/research/phase3-index.jsonl   one JSON object per past essay / PT (from search-based research)
Outputs 06-past-exams/index.csv                      one row per essay
        04-performance-test/past-pt-index.csv        one row per PT
        06-past-exams/analyses/<exam>-<item>.md      one analysis per essay
        04-performance-test/analyses/<exam>-<item>.md one analysis per PT
        00-exam-intel/coverage-matrix.csv            + PAST rows for issues no existing row covers

Re-runnable: PAST rows are matched by (subject, heading) so re-running does not duplicate them, and
analysis files are regenerated. Hand edits to generated analyses will be overwritten — put lasting
analysis notes in the `notes` field of the JSONL record instead.
"""
from __future__ import annotations

import calendar
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import common as C  # noqa: E402

DATA = ROOT / "06-past-exams/research/phase3-index.jsonl"
MATRIX = ROOT / C.MATRIX_REL
VERIFY_DEPTH = "V-070"   # analyses are index-level (search-derived)
VERIFY_MAP = "V-071"     # issue -> coverage mapping by research agents
CA_LAW = {"CMP", "WIL", "TRS", "PRF"}
PT_TASKS = {"objective-memo", "persuasive-brief", "client-letter", "demand-letter", "drafting-will",
            "drafting-contract", "drafting-other", "closing-argument", "opening-statement", "discovery-plan", "other"}


def exam_label(exam: str) -> str:
    y, m = exam.split("-")
    return f"{calendar.month_name[int(m)]} {y}"


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def load_records() -> list[dict]:
    recs, seen = [], set()
    for n, line in enumerate(DATA.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        r = json.loads(line)
        key = (r["exam"], r["item"])
        if key in seen:
            print(f"warning: duplicate record {key} (line {n}) skipped", file=sys.stderr)
            continue
        seen.add(key)
        r["subjects"] = [s for s in (r.get("subjects") or []) if s in C.SUBJECTS]
        recs.append(r)
    recs.sort(key=lambda r: (r["exam"], r["item"]))
    return recs


def add_past_rows(recs: list[dict]) -> dict:
    with MATRIX.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        cols, rows = reader.fieldnames, list(reader)
    ids = {r["coverage_id"] for r in rows}
    past = {(r["subject_code"], norm(r["heading"])): r["coverage_id"] for r in rows if r["source"] == "PAST"}
    counters = {}
    for r in rows:
        if r["source"] == "PAST":
            code, _, num = r["coverage_id"].split("-", 2)
            counters[code] = max(counters.get(code, 0), int(num))
    stats = {"new_rows": 0, "remapped_invalid": 0}
    for rec in recs:
        for iss in rec.get("issues") or []:
            cid = (iss.get("coverage_id") or "").strip()
            if rec["type"] == "PT" and (cid.startswith("NEW:") or (cid and cid not in ids)):
                iss["coverage_id"] = "PT-SUP-002"  # PT Library law is closed-universe, not a subject to learn
                continue
            if cid.startswith("NEW:") or (cid and cid not in ids):
                if cid.startswith("NEW:"):
                    _, code, heading = cid.split(":", 2)
                else:  # agent cited a row that does not exist -> treat as a new issue
                    code = cid.split("-")[0] if cid.split("-")[0] in C.SUBJECTS else (rec["subjects"] or ["PRF"])[0]
                    heading = iss.get("label") or cid
                    stats["remapped_invalid"] += 1
                code = code.strip().upper()
                if code not in C.SUBJECTS:
                    if rec["type"] == "PT" or not rec["subjects"]:
                        iss["coverage_id"] = "PT-SUP-002" if rec["type"] == "PT" else ""
                        continue  # PT library topics are not exam-subject coverage rows
                    code = rec["subjects"][0]
                heading = heading.strip().rstrip(".")
                key = (code, norm(heading))
                if key not in past:
                    counters[code] = counters.get(code, 0) + 1
                    new_id = f"{code}-PAST-{counters[code]:03d}"
                    slug = C.SUBJECTS[code].slug
                    rows.append({
                        "coverage_id": new_id, "subject_code": code, "subject": C.SUBJECTS[code].name,
                        "source": "PAST", "source_ref": f"Past CA essay {rec['exam']} {rec['item']}",
                        "level": "topic", "parent_id": "", "heading": heading,
                        "tested_on": "essay" if rec["type"] == "essay" else "PT",
                        "ca_specific": "Y" if code in CA_LAW else "N", "weight_note": "",
                        "target_file": f"03-subjects/{slug}/outline.md", "target_heading": heading,
                        "mapping_status": "planned",
                        "source_status": "confirmed-primary" if rec.get("status") == "confirmed-primary" else "unconfirmed",
                        "source_id": "S-079",
                        "notes": f"Added in Phase 3 from {rec['exam']} {rec['item']}; issue not covered by an existing row",
                    })
                    past[key] = new_id
                    ids.add(new_id)
                    stats["new_rows"] += 1
                iss["coverage_id"] = past[key]
    with MATRIX.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
    stats["headings"] = {r["coverage_id"]: r["heading"] for r in rows}
    return stats


def fm(subject: str, topic: str, cov: list[str], tested: str) -> str:
    cov_s = ", ".join(dict.fromkeys(cov))
    topic = topic.replace('"', "'")
    return (f"---\nsubject: {subject}\ntopic: \"{topic}\"\ncoverage_ids: [{cov_s}]\ntested_on: [{tested}]\n"
            f"exam_frequency: {{level: n/a, basis: \"Single past question\"}}\nlast_verified: {C.today()}\nstatus: draft\n---\n\n")


def links(rec: dict) -> str:
    out = []
    if rec.get("question_url"):
        out.append(f"[Question booklet]({rec['question_url']})")
    if rec.get("answers_url"):
        out.append(f"[Selected answers]({rec['answers_url']})")
    return " · ".join(out) or "Not captured — see the [Past Exams page](https://www.calbar.ca.gov/admissions/applicant-resources/past-exams)"


def analysis(rec: dict, headings: dict) -> str:
    subj_names = ", ".join(f"{C.SUBJECTS[s].name} ({s})" for s in rec["subjects"]) or "not determined"
    primary = rec["subjects"][0] if rec["subjects"] else ("meta" if rec["type"] == "essay" else "performance-test")
    is_pt = rec["type"] == "PT"
    cov = [i["coverage_id"] for i in rec.get("issues") or [] if i.get("coverage_id")]
    if rec["type"] == "PT":
        cov = ["PT-SUP-002"] + cov
    title = f"{exam_label(rec['exam'])} — {'Performance Test ' + rec['item'] if is_pt else 'Question ' + rec['item'][1:]}"
    if is_pt and rec.get("pt_area"):
        title += f" ({rec['pt_area']})"
    elif rec["subjects"]:
        title += f" ({' + '.join(C.SUBJECTS[s].name for s in rec['subjects'])})"
    lines = [f"# {title}", "",
             f"> **Index-level analysis.** It was built from State Bar materials via search, because direct access to "
             f"calbar.ca.gov was blocked in Phase 3. Facts and calls are paraphrased in my own words. Read the official "
             f"PDF for the full question [VERIFY {VERIFY_DEPTH}].", "",
             "| | |", "|---|---|",
             f"| Exam | {exam_label(rec['exam'])}, {'Performance Test ' + rec['item'] if is_pt else 'Question ' + rec['item'][1:]} |",
             f"| Subjects | {subj_names}{' — **crossover**' if len(rec['subjects']) > 1 else ''} |"]
    if is_pt:
        lines.append(f"| Task | {rec.get('pt_task') or 'not determined'} · area: {rec.get('pt_area') or 'not determined'} |")
    lines += [f"| Official PDFs | {links(rec)} |", f"| Index status | {rec.get('status', 'partial')} |", "",
              "## The question in brief (my words)", "",
              (rec.get("facts") or "_Facts not captured._"), "",
              f"**Call:** {rec.get('call') or '_not captured_'}", "",
              "## Issue map", ""]
    issues = rec.get("issues") or []
    if issues:
        lines += ["| # | Issue | Coverage row | Basis |", "|---|---|---|---|"]
        for k, iss in enumerate(issues, 1):
            cid = iss.get("coverage_id", "")
            lines.append(f"| {k} | {iss.get('label', '')} | `{cid}` — {headings.get(cid, '')[:70]} | {iss.get('basis', '')} |")
        lines += ["", f"_Issue labels and their coverage-row mapping came from the research pass and need checking against the official question [VERIFY {VERIFY_MAP}]._"]
    else:
        lines.append("_No issues captured; see the official PDF._")
    lines += ["", "## How the selected answers organized it", ""]
    if rec.get("answer_structure"):
        lines += [f"{k}. {h}" for k, h in enumerate(rec["answer_structure"], 1)]
    else:
        lines.append("_Headings not captured in the Phase 3 search output._")
    lines += ["", "## Model approach (my words)", ""]
    if is_pt:
        lines += [f"1. Read the task memo first: the deliverable is a **{rec.get('pt_task') or 'see the memo'}**. Match its "
                  f"format, audience and tone to `04-performance-test/task-types/`.",
                  "2. Mine the Library for the governing rules, cite them by name, and apply only the File's facts "
                  "(see `04-performance-test/method.md`).",
                  "3. Budget about 35–45 minutes for reading and outlining and about 45–55 for writing; finish every part the memo asks for."]
    else:
        n = max(1, len(issues))
        mins = max(5, round(45 / n))
        lines += ["1. **Follow the call.** One top-level heading per call. Under it, one sub-heading per issue, in the order of the issue map.",
                  f"2. **Time.** About 15 minutes to outline, then about {mins} minutes of writing per issue ({n} issues mapped). Spend more on the issues the facts develop most.",
                  "3. **For each issue:** a 1–3 sentence rule (from the subject's `rule-statements.md`), then element-by-element application with the specific facts, both sides where the facts cut both ways, and a conclusion.",
                  "4. **California law.** Use it only where the call asks for it, or where the subject is tested under California law "
                  "(Community Property, Wills, Trusts, PR, and the CEC/CCP comparisons in Evidence and Civil Procedure; see `00-exam-intel/grader-expectations.md`)."]
    if rec.get("notes"):
        lines += ["", "## Research notes", "", rec["notes"]]
    return fm(primary if not is_pt else "performance-test", title, cov, "PT" if is_pt else "essay") + "\n".join(lines) + "\n"


def main() -> int:
    recs = load_records()
    stats = add_past_rows(recs)
    headings = stats["headings"]
    ess_dir, pt_dir = ROOT / "06-past-exams/analyses", ROOT / "04-performance-test/analyses"
    ess_dir.mkdir(parents=True, exist_ok=True)
    pt_dir.mkdir(parents=True, exist_ok=True)
    for d in (ess_dir, pt_dir):
        for f in d.glob("*.md"):
            f.unlink()
        gk = d / ".gitkeep"
        if gk.exists():
            gk.unlink()
    ess_rows, pt_rows = [], []
    for rec in recs:
        fname = f"{rec['exam']}-{rec['item']}.md"
        if rec["type"] == "essay":
            (ess_dir / fname).write_text(analysis(rec, headings), encoding="utf-8")
            ess_rows.append({
                "exam": rec["exam"], "q_num": rec["item"][1:], "type": "essay",
                "subjects": ";".join(rec["subjects"]),
                "issues": ";".join(dict.fromkeys(i["coverage_id"] for i in rec.get("issues") or [] if i.get("coverage_id"))),
                "call_summary": (rec.get("call") or "").replace("\n", " "),
                "question_link": rec.get("question_url") or "", "selected_answers_link": rec.get("answers_url") or "",
                "analysis_file": f"06-past-exams/analyses/{fname}", "notes": rec.get("status", ""),
            })
        else:
            (pt_dir / fname).write_text(analysis(rec, headings), encoding="utf-8")
            task = rec.get("pt_task") if rec.get("pt_task") in PT_TASKS else ("undetermined" if not rec.get("pt_task") else "other")
            pt_rows.append({
                "exam": rec["exam"], "pt_id": rec["item"], "title": (rec.get("call") or "")[:120],
                "task_type": task, "area": rec.get("pt_area") or "",
                "question_link": rec.get("question_url") or "", "selected_answers_link": rec.get("answers_url") or "",
                "analysis_file": f"04-performance-test/analyses/{fname}", "notes": rec.get("status", ""),
            })
    for path, cols, rows in [(ROOT / C.PAST_INDEX_REL, C.PAST_INDEX_COLUMNS, ess_rows),
                             (ROOT / C.PAST_PT_INDEX_REL, C.PAST_PT_COLUMNS, pt_rows)]:
        with path.open("w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=cols)
            w.writeheader()
            w.writerows(rows)
    print(f"records: {len(recs)} · essays: {len(ess_rows)} · PTs: {len(pt_rows)} · new PAST rows: {stats['new_rows']} "
          f"· invalid ids remapped: {stats['remapped_invalid']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
