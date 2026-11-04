#!/usr/bin/env python3
"""Repository validator for the CA Bar (July 2027) knowledge base.

Phase 0 checks (extended in Phase 1+):
  1. YAML front matter on every content file (numbered top-level folders).
  2. coverage-matrix.csv: schema, enums, unique IDs, parent links, and a
     target_file + target_heading on every row ("no unmapped rows").
  3. Source citations: every [S-###] marker resolves to a row in
     00-exam-intel/sources.md; every source row is well-formed.
  4. Uncertainty tracking: every [VERIFY V-###] tag resolves to an entry in
     VERIFY-QUEUE.md; bare [VERIFY] tags (no ID) are errors.

Usage:
  python scripts/validate.py              # all checks
  python scripts/validate.py --strict     # also require target files/headings to exist
Exit code 0 = pass, 1 = errors found.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
MATRIX = ROOT / "00-exam-intel" / "coverage-matrix.csv"
SOURCES = ROOT / "00-exam-intel" / "sources.md"
VERIFY_QUEUE = ROOT / "VERIFY-QUEUE.md"

CONTENT_DIR_RE = re.compile(r"^\d\d-")
FRONT_MATTER_KEYS = [
    "subject",
    "topic",
    "coverage_ids",
    "tested_on",
    "exam_frequency",
    "last_verified",
    "status",
]
STATUS_VALUES = {"draft", "reviewed", "verified"}
TESTED_ON_VALUES = {"MBE", "essay", "PT", "none"}

MATRIX_COLUMNS = [
    "coverage_id",
    "subject_code",
    "subject",
    "source",
    "source_ref",
    "level",
    "parent_id",
    "heading",
    "tested_on",
    "ca_specific",
    "weight_note",
    "target_file",
    "target_heading",
    "mapping_status",
    "source_status",
    "source_id",
    "notes",
]
SUBJECT_CODES = {
    "BUS": "Business Associations",
    "CIV": "Civil Procedure",
    "CMP": "Community Property",
    "CON": "Constitutional Law",
    "CTR": "Contracts",
    "CRM": "Criminal Law and Procedure",
    "EVD": "Evidence",
    "PRF": "Professional Responsibility",
    "PRP": "Real Property",
    "REM": "Remedies",
    "TRT": "Torts",
    "WIL": "Wills and Succession",
    "TRS": "Trusts",
    "PT": "Performance Test",
}
MATRIX_SOURCES = {"MBE", "CBX", "PAST", "SUP"}
MATRIX_LEVELS = {"category", "topic", "subtopic", "item"}
MAPPING_STATUS = {"planned", "mapped", "verified"}
SOURCE_STATUS = {"confirmed-primary", "secondary", "unconfirmed"}

SOURCE_REF_RE = re.compile(r"\[(S-\d{3,})\]")
SOURCE_ROW_RE = re.compile(r"^\|\s*(S-\d{3,})\s*\|")
VERIFY_TAG_RE = re.compile(r"\[VERIFY(?:\s+(V-\d{3,}))?\]")
VERIFY_ROW_RE = re.compile(r"^\|\s*(V-\d{3,})\s*\|")
HEADING_RE = re.compile(r"^#{1,6}\s+(.*?)\s*#*\s*$")


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)


def rel(p: Path) -> str:
    return str(p.relative_to(ROOT))


def content_files() -> list[Path]:
    files: list[Path] = []
    for d in sorted(ROOT.iterdir()):
        if d.is_dir() and CONTENT_DIR_RE.match(d.name):
            for f in sorted(d.rglob("*.md")):
                if "raw" in f.relative_to(ROOT).parts:
                    continue
                files.append(f)
    return files


def all_markdown() -> list[Path]:
    skip = {".git", "node_modules", ".venv", "venv"}
    out = []
    for f in sorted(ROOT.rglob("*.md")):
        parts = set(f.relative_to(ROOT).parts)
        if parts & skip or "raw" in parts:
            continue
        out.append(f)
    return out


def parse_front_matter(text: str) -> dict | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    try:
        data = yaml.safe_load(text[4:end])
    except yaml.YAMLError:
        return None
    return data if isinstance(data, dict) else None


def check_front_matter(rep: Report) -> None:
    for f in content_files():
        fm = parse_front_matter(f.read_text(encoding="utf-8"))
        if fm is None:
            rep.error(f"{rel(f)}: missing or invalid YAML front matter")
            continue
        for key in FRONT_MATTER_KEYS:
            if key not in fm:
                rep.error(f"{rel(f)}: front matter missing '{key}'")
        if fm.get("status") not in STATUS_VALUES:
            rep.error(f"{rel(f)}: status must be one of {sorted(STATUS_VALUES)}")
        tested = fm.get("tested_on")
        if tested is not None:
            vals = tested if isinstance(tested, list) else [tested]
            bad = [v for v in vals if v not in TESTED_ON_VALUES]
            if bad:
                rep.error(f"{rel(f)}: tested_on has invalid values {bad}")
        if "coverage_ids" in fm and not isinstance(fm["coverage_ids"], list):
            rep.error(f"{rel(f)}: coverage_ids must be a list")
        freq = fm.get("exam_frequency")
        if freq is not None and not (isinstance(freq, dict) and "level" in freq and "basis" in freq):
            rep.error(f"{rel(f)}: exam_frequency must be a mapping with 'level' and 'basis'")


def load_headings(path: Path) -> set[str]:
    heads = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        m = HEADING_RE.match(line)
        if m:
            heads.add(m.group(1).strip().lower())
    return heads


def check_matrix(rep: Report, strict: bool) -> list[dict]:
    if not MATRIX.exists():
        rep.error(f"{rel(MATRIX)}: missing")
        return []
    with MATRIX.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames != MATRIX_COLUMNS:
            rep.error(f"{rel(MATRIX)}: columns must be exactly {MATRIX_COLUMNS}, got {reader.fieldnames}")
            return []
        rows = list(reader)
    ids: set[str] = set()
    heading_cache: dict[Path, set[str]] = {}
    for i, r in enumerate(rows, start=2):
        loc = f"{rel(MATRIX)}:{i}"
        cid = r["coverage_id"].strip()
        if not cid:
            rep.error(f"{loc}: empty coverage_id")
            continue
        if cid in ids:
            rep.error(f"{loc}: duplicate coverage_id {cid}")
        ids.add(cid)
        code = r["subject_code"]
        if code not in SUBJECT_CODES:
            rep.error(f"{loc}: unknown subject_code '{code}'")
        elif r["subject"] != SUBJECT_CODES[code]:
            rep.error(f"{loc}: subject '{r['subject']}' does not match code {code}")
        if not cid.startswith(f"{code}-{r['source']}-"):
            rep.error(f"{loc}: coverage_id must start with '{code}-{r['source']}-'")
        if r["source"] not in MATRIX_SOURCES:
            rep.error(f"{loc}: source must be one of {sorted(MATRIX_SOURCES)}")
        if r["level"] not in MATRIX_LEVELS:
            rep.error(f"{loc}: level must be one of {sorted(MATRIX_LEVELS)}")
        tested = [t for t in r["tested_on"].split(";") if t]
        if not tested or any(t not in TESTED_ON_VALUES for t in tested):
            rep.error(f"{loc}: tested_on must be ';'-separated values from {sorted(TESTED_ON_VALUES)}")
        if r["ca_specific"] not in {"Y", "N"}:
            rep.error(f"{loc}: ca_specific must be Y or N")
        if r["mapping_status"] not in MAPPING_STATUS:
            rep.error(f"{loc}: mapping_status must be one of {sorted(MAPPING_STATUS)}")
        if r["source_status"] not in SOURCE_STATUS:
            rep.error(f"{loc}: source_status must be one of {sorted(SOURCE_STATUS)}")
        if not r["heading"].strip():
            rep.error(f"{loc}: empty heading")
        # Completeness rule: every row must be mapped to a file + heading.
        if not r["target_file"].strip() or not r["target_heading"].strip():
            rep.error(f"{loc}: UNMAPPED row {cid} (target_file/target_heading required)")
        elif strict or r["mapping_status"] in {"mapped", "verified"}:
            target = ROOT / r["target_file"]
            if not target.exists():
                rep.error(f"{loc}: {cid} maps to missing file {r['target_file']}")
            else:
                heads = heading_cache.setdefault(target, load_headings(target))
                if r["target_heading"].strip().lower() not in heads:
                    rep.error(f"{loc}: {cid} heading '{r['target_heading']}' not found in {r['target_file']}")
    for i, r in enumerate(rows, start=2):
        pid = r["parent_id"].strip()
        if pid and pid not in ids:
            rep.error(f"{rel(MATRIX)}:{i}: parent_id {pid} does not exist")
    return rows


def load_source_ids(rep: Report) -> set[str]:
    if not SOURCES.exists():
        rep.error(f"{rel(SOURCES)}: missing")
        return set()
    ids: set[str] = set()
    for n, line in enumerate(SOURCES.read_text(encoding="utf-8").splitlines(), start=1):
        m = SOURCE_ROW_RE.match(line)
        if not m:
            continue
        sid = m.group(1)
        if sid in ids:
            rep.error(f"{rel(SOURCES)}:{n}: duplicate source id {sid}")
        ids.add(sid)
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not any(c.startswith("http") for c in cells):
            rep.error(f"{rel(SOURCES)}:{n}: source {sid} has no URL")
        if not any(re.fullmatch(r"\d{4}-\d{2}-\d{2}", c) for c in cells):
            rep.error(f"{rel(SOURCES)}:{n}: source {sid} has no access date (YYYY-MM-DD)")
    return ids


def check_citations_and_verify(rep: Report, rows: list[dict]) -> None:
    source_ids = load_source_ids(rep)
    queue_ids: set[str] = set()
    if VERIFY_QUEUE.exists():
        for line in VERIFY_QUEUE.read_text(encoding="utf-8").splitlines():
            m = VERIFY_ROW_RE.match(line)
            if m:
                queue_ids.add(m.group(1))
    else:
        rep.error("VERIFY-QUEUE.md: missing")
    for f in all_markdown():
        if f in {VERIFY_QUEUE}:
            continue
        for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), start=1):
            for sid in SOURCE_REF_RE.findall(line):
                if f != SOURCES and sid not in source_ids:
                    rep.error(f"{rel(f)}:{n}: citation [{sid}] not found in sources.md")
            for m in VERIFY_TAG_RE.finditer(line):
                vid = m.group(1)
                if vid is None:
                    if "`[VERIFY]`" in line or f.name in {"CLAUDE.md", "README.md", "PROGRESS.md"}:
                        continue  # documentation of the convention itself
                    rep.error(f"{rel(f)}:{n}: bare [VERIFY] tag; use [VERIFY V-###] and log it in VERIFY-QUEUE.md")
                elif vid not in queue_ids:
                    rep.error(f"{rel(f)}:{n}: [VERIFY {vid}] not logged in VERIFY-QUEUE.md")
    for r in rows:
        sid = r["source_id"].strip()
        for s in [x for x in sid.split(";") if x]:
            if s not in source_ids:
                rep.error(f"{rel(MATRIX)}: {r['coverage_id']} cites unknown source {s}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--strict", action="store_true", help="require every matrix target file/heading to exist")
    args = ap.parse_args()

    rep = Report()
    check_front_matter(rep)
    rows = check_matrix(rep, args.strict)
    check_citations_and_verify(rep, rows)

    for w in rep.warnings:
        print(f"WARN  {w}")
    for e in rep.errors:
        print(f"ERROR {e}")
    n_files = len(content_files())
    print(f"\nChecked {n_files} content files, {len(rows)} coverage rows: "
          f"{len(rep.errors)} error(s), {len(rep.warnings)} warning(s).")
    return 1 if rep.errors else 0


if __name__ == "__main__":
    sys.exit(main())
