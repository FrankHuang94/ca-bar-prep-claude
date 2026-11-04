#!/usr/bin/env python3
"""Validate the CA Bar (July 2027) knowledge base.

Checks
  front-matter   YAML front matter on every Markdown file in a numbered folder (JSON Schema),
                 and every front-matter coverage_id exists in the coverage matrix
  matrix         coverage-matrix.csv schema, enums, unique IDs, parent links, and NO UNMAPPED ROWS
                 (mapped/verified rows, or all rows with --strict, must point to an existing heading)
  citations      every [S-###] resolves in 00-exam-intel/sources.md; source rows have URL + date
  verify         every [VERIFY V-###] is logged in VERIFY-QUEUE.md; no bare [VERIFY]
  rules          rule IDs (R-XXX-###) unique, prefix matches the subject folder
  mcq            07-question-bank/mcq/**.yaml against mcq.schema.json + key/explanation consistency,
                 IDs unique, subject/folder agreement, coverage_ids and rule_ids exist
  essays / pt    front matter against essay/pt schemas, required sections, issue points sum to 100
  simulations    manifests reference existing items, no duplicates
  flashcards     03-subjects/*/flashcards.csv columns, unique IDs, rule_id exists
  csv            attempts.csv, past-exam indexes: headers and enumerations
  links          relative Markdown links resolve to existing files

Usage
  python scripts/validate.py            # all checks
  python scripts/validate.py --strict   # also require every matrix row's target file + heading to exist
Exit code 0 = pass, 1 = errors.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

from jsonschema import Draft202012Validator

import common as C

CONTENT_DIR_RE = re.compile(r"^\d\d-")
SOURCE_REF_RE = re.compile(r"\[(S-\d{3,})\]")
SOURCE_ROW_RE = re.compile(r"^\|\s*(S-\d{3,})\s*\|")
VERIFY_TAG_RE = re.compile(r"\[VERIFY(?:\s+(V-\d{3,}))?\]")
VERIFY_ROW_RE = re.compile(r"^\|\s*(V-\d{3,})\s*\|")
HEADING_RE = re.compile(r"^#{1,6}\s+(.*?)\s*#*\s*$")
LINK_RE = re.compile(r"(?<!!)\[[^\]\n]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")

MATRIX_COLUMNS = ["coverage_id", "subject_code", "subject", "source", "source_ref", "level", "parent_id",
                  "heading", "tested_on", "ca_specific", "weight_note", "target_file", "target_heading",
                  "mapping_status", "source_status", "source_id", "notes"]
MATRIX_SOURCES = {"MBE", "CBX", "SUP", "PAST"}
MATRIX_LEVELS = {"category", "topic", "subtopic", "item"}
MAPPING_STATUS = {"planned", "mapped", "verified"}
SOURCE_STATUS = {"confirmed-primary", "secondary", "unconfirmed"}
TESTED_ON = {"MBE", "essay", "PT", "none"}
ESSAY_SECTIONS = ["Facts", "Call of the Question", "Issue List", "Model Answer", "Self-Grading Rubric"]
PT_SECTIONS = ["Task Memorandum", "File", "Library", "Model Answer", "Grading Rubric"]
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "raw", "exports", "__pycache__", ".pytest_cache"}


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)


def rel(path: Path) -> str:
    return str(path.relative_to(C.root()))


def schema(name: str) -> Draft202012Validator:
    with C.p(C.SCHEMA_DIR_REL, f"{name}.schema.json").open(encoding="utf-8") as fh:
        return Draft202012Validator(json.load(fh))


def schema_errors(validator: Draft202012Validator, obj) -> list[str]:
    out = []
    for e in sorted(validator.iter_errors(obj), key=lambda e: list(e.path)):
        where = "/".join(str(x) for x in e.path) or "(root)"
        out.append(f"{where}: {e.message}")
    return out


def walk(pattern: str) -> list[Path]:
    out = []
    for f in sorted(C.root().rglob(pattern)):
        parts = f.relative_to(C.root()).parts
        if set(parts) & SKIP_DIRS or parts[:2] == ("scripts", "tests"):
            continue
        out.append(f)
    return out


def is_question_item(path: Path) -> bool:
    r = rel(path)
    return (r.startswith(C.ESSAY_DIR_REL + "/") and path.name.startswith("E-")) or \
           (r.startswith(C.PT_DIR_REL + "/") and path.name.startswith("PT-"))


def content_files() -> list[Path]:
    return [f for f in walk("*.md") if CONTENT_DIR_RE.match(f.relative_to(C.root()).parts[0])
            and not is_question_item(f)]


def strip_code_blocks(text: str) -> list[tuple[int, str]]:
    """Lines outside fenced code blocks, with 1-based line numbers."""
    out, fenced = [], False
    for n, line in enumerate(text.splitlines(), start=1):
        if line.lstrip().startswith("```"):
            fenced = not fenced
            continue
        if not fenced:
            out.append((n, line))
    return out


# --------------------------------------------------------------------------- matrix
def check_matrix(rep: Report, strict: bool) -> list[dict]:
    path = C.p(C.MATRIX_REL)
    if not path.exists():
        rep.error(f"{C.MATRIX_REL}: missing")
        return []
    header = C.csv_header(path)
    if header != MATRIX_COLUMNS:
        rep.error(f"{C.MATRIX_REL}: columns must be exactly {MATRIX_COLUMNS}, got {header}")
        return []
    rows = C.read_csv(path)
    names = {c: s.name for c, s in C.SUBJECTS.items()} | C.EXTRA_CODES
    ids: set[str] = set()
    heading_cache: dict[Path, list[str]] = {}
    for i, r in enumerate(rows, start=2):
        loc = f"{C.MATRIX_REL}:{i}"
        cid = r["coverage_id"].strip()
        if not cid:
            rep.error(f"{loc}: empty coverage_id")
            continue
        if cid in ids:
            rep.error(f"{loc}: duplicate coverage_id {cid}")
        ids.add(cid)
        code = r["subject_code"]
        if code not in names:
            rep.error(f"{loc}: unknown subject_code '{code}'")
        elif r["subject"] != names[code]:
            rep.error(f"{loc}: subject '{r['subject']}' does not match code {code}")
        if not cid.startswith(f"{code}-{r['source']}-"):
            rep.error(f"{loc}: coverage_id must start with '{code}-{r['source']}-'")
        for col, allowed in [("source", MATRIX_SOURCES), ("level", MATRIX_LEVELS),
                             ("mapping_status", MAPPING_STATUS), ("source_status", SOURCE_STATUS)]:
            if r[col] not in allowed:
                rep.error(f"{loc}: {col} must be one of {sorted(allowed)}")
        tested = C.split_list(r["tested_on"])
        if not tested or any(t not in TESTED_ON for t in tested):
            rep.error(f"{loc}: tested_on must be ';'-separated values from {sorted(TESTED_ON)}")
        if r["ca_specific"] not in {"Y", "N"}:
            rep.error(f"{loc}: ca_specific must be Y or N")
        if not r["heading"].strip():
            rep.error(f"{loc}: empty heading")
        if not r["target_file"].strip() or not r["target_heading"].strip():
            rep.error(f"{loc}: UNMAPPED row {cid} (target_file and target_heading required)")
        elif strict or r["mapping_status"] in {"mapped", "verified"}:
            target = C.p(r["target_file"])
            if not target.exists():
                rep.error(f"{loc}: {cid} maps to missing file {r['target_file']}")
            else:
                heads = heading_cache.setdefault(target, [h.lower() for h in load_headings(target)])
                want = r["target_heading"].strip().lower()
                if not any(want in h for h in heads):
                    rep.error(f"{loc}: {cid} heading '{r['target_heading']}' not found in {r['target_file']}")
    for i, r in enumerate(rows, start=2):
        pid = r["parent_id"].strip()
        if pid and pid not in ids:
            rep.error(f"{C.MATRIX_REL}:{i}: parent_id {pid} does not exist")
    return rows


def load_headings(path: Path) -> list[str]:
    return [m.group(1).strip() for _, line in strip_code_blocks(path.read_text(encoding="utf-8"))
            if (m := HEADING_RE.match(line))]


# --------------------------------------------------------------------------- front matter
def check_front_matter(rep: Report, matrix_ids: set[str]) -> None:
    v = schema("content-front-matter")
    for f in content_files():
        fm, _ = C.parse_front_matter(f.read_text(encoding="utf-8"))
        if fm is None:
            rep.error(f"{rel(f)}: missing or invalid YAML front matter")
            continue
        for e in schema_errors(v, fm):
            rep.error(f"{rel(f)}: front matter {e}")
        for cid in fm.get("coverage_ids") or []:
            if isinstance(cid, str) and cid not in matrix_ids:
                rep.error(f"{rel(f)}: coverage_id {cid} not in coverage matrix")


# --------------------------------------------------------------------------- citations / verify
def check_citations_and_verify(rep: Report, rows: list[dict]) -> None:
    sources = C.p(C.SOURCES_REL)
    source_ids: set[str] = set()
    if not sources.exists():
        rep.error(f"{C.SOURCES_REL}: missing")
    else:
        for n, line in enumerate(sources.read_text(encoding="utf-8").splitlines(), start=1):
            m = SOURCE_ROW_RE.match(line)
            if not m:
                continue
            sid = m.group(1)
            if sid in source_ids:
                rep.error(f"{C.SOURCES_REL}:{n}: duplicate source id {sid}")
            source_ids.add(sid)
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if not any(c.startswith("http") for c in cells):
                rep.error(f"{C.SOURCES_REL}:{n}: source {sid} has no URL")
            if not any(re.fullmatch(r"\d{4}-\d{2}-\d{2}", c) for c in cells):
                rep.error(f"{C.SOURCES_REL}:{n}: source {sid} has no access date (YYYY-MM-DD)")
    queue = C.p(C.VERIFY_REL)
    queue_ids: set[str] = set()
    if queue.exists():
        for line in queue.read_text(encoding="utf-8").splitlines():
            if m := VERIFY_ROW_RE.match(line):
                if m.group(1) in queue_ids:
                    rep.error(f"{C.VERIFY_REL}: duplicate entry {m.group(1)}")
                queue_ids.add(m.group(1))
    else:
        rep.error(f"{C.VERIFY_REL}: missing")
    doc_files = {"CLAUDE.md", "README.md", "PROGRESS.md"}
    for f in walk("*.md"):
        if f == queue:
            continue
        in_tooling = rel(f).startswith((".claude/", ".github/"))
        for n, line in strip_code_blocks(f.read_text(encoding="utf-8")):
            for sid in SOURCE_REF_RE.findall(line):
                if f != sources and sid not in source_ids:
                    rep.error(f"{rel(f)}:{n}: citation [{sid}] not found in sources.md")
            for m in VERIFY_TAG_RE.finditer(line):
                vid = m.group(1)
                if vid is None:
                    if "`[VERIFY]`" in line or f.name in doc_files or in_tooling:
                        continue  # documentation of the convention itself
                    rep.error(f"{rel(f)}:{n}: bare [VERIFY] tag; use [VERIFY V-###] and log it in VERIFY-QUEUE.md")
                elif vid not in queue_ids and not in_tooling:
                    rep.error(f"{rel(f)}:{n}: [VERIFY {vid}] not logged in VERIFY-QUEUE.md")
    for r in rows:
        for s in C.split_list(r["source_id"]):
            if s not in source_ids:
                rep.error(f"{C.MATRIX_REL}: {r['coverage_id']} cites unknown source {s}")


# --------------------------------------------------------------------------- rules
def check_rules(rep: Report) -> dict[str, dict]:
    rules = C.load_rules()
    for rid, info in rules.items():
        for d in info["dupes"]:
            rep.error(f"{d}: duplicate rule ID {rid} (first at {info['file']}:{info['line']})")
        folder = Path(info["file"]).parent.name
        code = C.SLUG_TO_CODE.get(folder)
        if code and rid[2:5] != code:
            rep.error(f"{info['file']}:{info['line']}: rule {rid} prefix does not match subject folder ({code})")
    return rules


# --------------------------------------------------------------------------- MCQ
def check_mcqs(rep: Report, matrix_ids: set[str], rules: dict) -> set[str]:
    v = schema("mcq")
    seen: dict[str, str] = {}
    for q in C.load_mcqs():
        f = q.pop("_file")
        qid = q.get("id", "?")
        for e in schema_errors(v, q):
            rep.error(f"{f}: {qid}: {e}")
        if qid in seen:
            rep.error(f"{f}: duplicate MCQ id {qid} (also in {seen[qid]})")
        seen[qid] = f
        subj = q.get("subject")
        if isinstance(qid, str) and subj and not qid.startswith(f"Q-{subj}-"):
            rep.error(f"{f}: {qid}: id prefix does not match subject {subj}")
        folder = Path(f).parent.name
        if subj in C.SUBJECTS and folder != C.SUBJECTS[subj].slug:
            rep.error(f"{f}: {qid}: subject {subj} must live in mcq/{C.SUBJECTS[subj].slug}/")
        ans, opts = q.get("answer"), q.get("options") or {}
        wrong = set(opts) - {ans}
        given = set((q.get("explanation_each_wrong_option") or {}).keys())
        if ans in given:
            rep.error(f"{f}: {qid}: explanation_each_wrong_option must not explain the correct answer {ans}")
        if wrong and given != wrong:
            rep.error(f"{f}: {qid}: explanation_each_wrong_option must cover exactly {sorted(wrong)}")
        if len(set(opts.values())) != len(opts):
            rep.error(f"{f}: {qid}: duplicate option text")
        for cid in q.get("coverage_ids") or []:
            if cid not in matrix_ids:
                rep.error(f"{f}: {qid}: coverage_id {cid} not in coverage matrix")
        for rid in q.get("rule_ids") or []:
            if rid not in rules:
                rep.error(f"{f}: {qid}: rule_id {rid} not found in any rule-statements.md")
    return set(seen)


# --------------------------------------------------------------------------- essays / PTs
def body_sections(body: str) -> list[str]:
    return [line[3:].strip() for _, line in strip_code_blocks(body) if line.startswith("## ")]


def check_essays(rep: Report, matrix_ids: set[str], rules: dict) -> set[str]:
    v = schema("essay")
    ids: dict[str, str] = {}
    for item in C.load_md_items(C.ESSAY_DIR_REL):
        f, fm = item["_file"], item["_fm"]
        eid = fm.get("id", "?")
        if not fm:
            rep.error(f"{f}: missing or invalid front matter")
            continue
        for e in schema_errors(v, fm):
            rep.error(f"{f}: {e}")
        if eid in ids:
            rep.error(f"{f}: duplicate essay id {eid} (also in {ids[eid]})")
        ids[eid] = f
        if Path(f).stem != eid:
            rep.error(f"{f}: file name must be {eid}.md")
        subjects = fm.get("subjects") or []
        if fm.get("type") == "crossover":
            if len(subjects) < 2:
                rep.error(f"{f}: crossover essay needs >= 2 subjects")
            if not str(eid).startswith("E-XO-") or Path(f).parent.name != "crossover":
                rep.error(f"{f}: crossover essays use E-XO-### ids and live in essays/crossover/")
        elif subjects:
            code = subjects[0]
            if not str(eid).startswith(f"E-{code}-") or Path(f).parent.name != C.SUBJECTS[code].slug:
                rep.error(f"{f}: single-subject essay must be E-{code}-### in essays/{C.SUBJECTS[code].slug}/")
        pts = sum(i.get("points", 0) for i in fm.get("issues") or [] if isinstance(i, dict))
        if fm.get("issues") and pts != 100:
            rep.error(f"{f}: issue points must sum to 100 (got {pts})")
        missing = [s for s in ESSAY_SECTIONS if s not in body_sections(item["_body"])]
        if missing:
            rep.error(f"{f}: missing sections {missing}")
        check_refs(rep, f, fm, matrix_ids, rules)
    return set(ids)


def check_pts(rep: Report, matrix_ids: set[str], rules: dict) -> set[str]:
    v = schema("pt")
    ids: dict[str, str] = {}
    for item in C.load_md_items(C.PT_DIR_REL):
        f, fm = item["_file"], item["_fm"]
        pid = fm.get("id", "?")
        if not fm:
            rep.error(f"{f}: missing or invalid front matter")
            continue
        for e in schema_errors(v, fm):
            rep.error(f"{f}: {e}")
        if pid in ids:
            rep.error(f"{f}: duplicate PT id {pid}")
        ids[pid] = f
        if Path(f).stem != pid:
            rep.error(f"{f}: file name must be {pid}.md")
        missing = [s for s in PT_SECTIONS if s not in body_sections(item["_body"])]
        if missing:
            rep.error(f"{f}: missing sections {missing}")
        check_refs(rep, f, fm, matrix_ids, rules)
    return set(ids)


def check_refs(rep: Report, f: str, fm: dict, matrix_ids: set[str], rules: dict) -> None:
    for cid in fm.get("coverage_ids") or []:
        if cid not in matrix_ids:
            rep.error(f"{f}: coverage_id {cid} not in coverage matrix")
    for rid in fm.get("rule_ids") or []:
        if rid not in rules:
            rep.error(f"{f}: rule_id {rid} not found in any rule-statements.md")


def check_simulations(rep: Report, mcq_ids: set[str], essay_ids: set[str], pt_ids: set[str]) -> None:
    v = schema("simulation")
    base = C.p(C.SIM_DIR_REL)
    if not base.exists():
        return
    for f in sorted(base.glob("SIM-*.yaml")):
        data = C.load_yaml(f)
        for e in schema_errors(v, data):
            rep.error(f"{rel(f)}: {e}")
        if not isinstance(data, dict):
            continue
        items = list(data.get("essays") or []) + (data.get("mbe") or {}).get("am", []) + \
            (data.get("mbe") or {}).get("pm", [])
        for item, n in Counter(items).items():
            if n > 1:
                rep.error(f"{rel(f)}: {item} appears {n} times")
        for e in data.get("essays") or []:
            if e not in essay_ids:
                rep.error(f"{rel(f)}: unknown essay {e}")
        if data.get("pt") and data["pt"] not in pt_ids:
            rep.error(f"{rel(f)}: unknown PT {data['pt']}")
        for q in (data.get("mbe") or {}).get("am", []) + (data.get("mbe") or {}).get("pm", []):
            if q not in mcq_ids:
                rep.error(f"{rel(f)}: unknown MCQ {q}")


# --------------------------------------------------------------------------- flashcards / CSVs
def check_flashcards(rep: Report, rules: dict) -> None:
    seen: dict[str, str] = {}
    base = C.p(C.SUBJECTS_DIR_REL)
    for f in sorted(base.glob("*/flashcards.csv")) if base.exists() else []:
        header = C.csv_header(f)
        if header != C.FLASHCARD_COLUMNS:
            rep.error(f"{rel(f)}: columns must be {C.FLASHCARD_COLUMNS}, got {header}")
            continue
        code = C.SLUG_TO_CODE.get(f.parent.name)
        for i, r in enumerate(C.read_csv(f), start=2):
            fid = r["id"]
            if not C.FLASH_ID_RE.match(fid):
                rep.error(f"{rel(f)}:{i}: bad flashcard id {fid!r} (F-XXX-####)")
            elif code and fid[2:5] != code:
                rep.error(f"{rel(f)}:{i}: {fid} prefix does not match folder subject {code}")
            if fid in seen:
                rep.error(f"{rel(f)}:{i}: duplicate flashcard id {fid} (also {seen[fid]})")
            seen[fid] = rel(f)
            if not r["front"].strip() or not r["back"].strip():
                rep.error(f"{rel(f)}:{i}: empty front/back")
            if r["rule_id"] and r["rule_id"] not in rules:
                rep.error(f"{rel(f)}:{i}: rule_id {r['rule_id']} not found")


def check_csvs(rep: Report, matrix_ids: set[str]) -> None:
    specs = [(C.ATTEMPTS_REL, C.ATTEMPT_COLUMNS), (C.PAST_INDEX_REL, C.PAST_INDEX_COLUMNS),
             (C.PAST_PT_INDEX_REL, C.PAST_PT_COLUMNS)]
    for relpath, cols in specs:
        path = C.p(relpath)
        if path.exists() and C.csv_header(path) != cols:
            rep.error(f"{relpath}: columns must be {cols}, got {C.csv_header(path)}")
    path = C.p(C.ATTEMPTS_REL)
    if path.exists() and C.csv_header(path) == C.ATTEMPT_COLUMNS:
        ids = set()
        for i, r in enumerate(C.read_csv(path), start=2):
            loc = f"{C.ATTEMPTS_REL}:{i}"
            if r["attempt_id"] in ids:
                rep.error(f"{loc}: duplicate attempt_id {r['attempt_id']}")
            ids.add(r["attempt_id"])
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", r["date"]):
                rep.error(f"{loc}: date must be YYYY-MM-DD")
            if r["kind"] not in C.ATTEMPT_KINDS:
                rep.error(f"{loc}: kind must be one of {sorted(C.ATTEMPT_KINDS)}")
            if r["error_type"] not in C.ERROR_TYPES:
                rep.error(f"{loc}: error_type must be one of {sorted(C.ERROR_TYPES)}")
            if r["source"] not in C.ATTEMPT_SOURCES:
                rep.error(f"{loc}: source must be one of {sorted(C.ATTEMPT_SOURCES)}")
            if r["subject"] and r["subject"] not in C.SUBJECTS and r["subject"] not in {"MIX", "PT", "XO"}:
                rep.error(f"{loc}: subject must be a subject code, MIX, PT or XO")
    path = C.p(C.PAST_INDEX_REL)
    if path.exists() and C.csv_header(path) == C.PAST_INDEX_COLUMNS:
        for i, r in enumerate(C.read_csv(path), start=2):
            loc = f"{C.PAST_INDEX_REL}:{i}"
            if not re.fullmatch(r"\d{4}-(02|03|07|10)", r["exam"]):
                rep.error(f"{loc}: exam must be YYYY-02 or YYYY-07 (special sittings: 2020-10, 2025-03)")
            for s in C.split_list(r["subjects"]):
                if s not in C.SUBJECTS:
                    rep.error(f"{loc}: unknown subject code {s}")
            for cid in C.split_list(r["issues"]):
                if cid not in matrix_ids:
                    rep.error(f"{loc}: issue {cid} not in coverage matrix")


# --------------------------------------------------------------------------- links
def check_links(rep: Report) -> None:
    for f in walk("*.md"):
        for n, line in strip_code_blocks(f.read_text(encoding="utf-8")):
            for target in LINK_RE.findall(line):
                if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                    continue
                path_part = target.split("#", 1)[0]
                if not path_part:
                    continue
                dest = (f.parent / path_part).resolve()
                if not dest.exists():
                    rep.error(f"{rel(f)}:{n}: broken link -> {target}")


# --------------------------------------------------------------------------- main
def run(strict: bool = False) -> Report:
    rep = Report()
    rows = check_matrix(rep, strict)
    matrix_ids = {r["coverage_id"] for r in rows}
    check_front_matter(rep, matrix_ids)
    check_citations_and_verify(rep, rows)
    rules = check_rules(rep)
    mcq_ids = check_mcqs(rep, matrix_ids, rules)
    essay_ids = check_essays(rep, matrix_ids, rules)
    pt_ids = check_pts(rep, matrix_ids, rules)
    check_simulations(rep, mcq_ids, essay_ids, pt_ids)
    check_flashcards(rep, rules)
    check_csvs(rep, matrix_ids)
    check_links(rep)
    rep.stats = {"content_files": len(content_files()), "coverage_rows": len(rows), "rules": len(rules),
                 "mcq": len(mcq_ids), "essays": len(essay_ids), "pts": len(pt_ids)}
    return rep


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate the CA Bar knowledge base.")
    ap.add_argument("--strict", action="store_true", help="require every matrix target file/heading to exist")
    args = ap.parse_args()
    rep = run(args.strict)
    for w in rep.warnings:
        print(f"WARN  {w}")
    for e in rep.errors:
        print(f"ERROR {e}")
    s = rep.stats
    print(f"\nChecked {s['content_files']} content files, {s['coverage_rows']} coverage rows, {s['rules']} rules, "
          f"{s['mcq']} MCQs, {s['essays']} essays, {s['pts']} PTs: "
          f"{len(rep.errors)} error(s), {len(rep.warnings)} warning(s).")
    return 1 if rep.errors else 0


if __name__ == "__main__":
    sys.exit(main())
