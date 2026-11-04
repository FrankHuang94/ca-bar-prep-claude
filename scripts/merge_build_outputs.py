#!/usr/bin/env python3
"""Merge a content-build agent's outputs into the shared files.

  python scripts/merge_build_outputs.py --mapping CTR-mapping.csv [--sources CTR-sources.md] [--verify CTR-verify.md]

--mapping  CSV with columns coverage_id,target_file,target_heading. Each row's target heading must exist
           (case-insensitive substring of a heading in target_file); the matrix row is then updated and set
           to mapping_status=mapped. Unknown coverage_ids or missing headings are reported and NOT applied.
--sources  Markdown table rows "| S-### | ... |" inserted into 00-exam-intel/sources.md in ID order.
--verify   Markdown table rows "| V-### | ... |" inserted into the Open table of VERIFY-QUEUE.md in ID order.
Duplicate IDs are rejected. Use --dry-run to check without writing.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

import common as C
from validate import load_headings

ROW_RE = {"S": re.compile(r"^\|\s*(S-(\d{3,}))\s*\|"), "V": re.compile(r"^\|\s*(V-(\d{3,}))\s*\|")}


def apply_mapping(path: Path, dry: bool) -> int:
    mpath = C.p(C.MATRIX_REL)
    with mpath.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        cols, rows = reader.fieldnames, list(reader)
    by_id = {r["coverage_id"]: r for r in rows}
    heads: dict[str, list[str]] = {}
    problems = applied = 0
    for m in C.read_csv(path):
        cid, tfile, thead = m["coverage_id"].strip(), m["target_file"].strip(), m["target_heading"].strip()
        if cid not in by_id:
            print(f"  ! unknown coverage_id {cid}")
            problems += 1
            continue
        target = C.p(tfile)
        if not target.exists():
            print(f"  ! {cid}: file {tfile} does not exist")
            problems += 1
            continue
        hs = heads.setdefault(tfile, [h.lower() for h in load_headings(target)])
        if not any(thead.lower() in h for h in hs):
            print(f"  ! {cid}: heading '{thead}' not found in {tfile}")
            problems += 1
            continue
        r = by_id[cid]
        r["target_file"], r["target_heading"], r["mapping_status"] = tfile, thead, "mapped"
        applied += 1
    if not dry:
        with mpath.open("w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=cols)
            w.writeheader()
            w.writerows(rows)
    print(f"mapping {path.name}: applied {applied}, problems {problems}")
    return problems


def insert_rows(kind: str, src: Path, dest_rel: str, anchor_section: str | None, dry: bool) -> int:
    rx = ROW_RE[kind]
    new = [ln.rstrip("\n") for ln in src.read_text(encoding="utf-8").splitlines() if rx.match(ln)]
    dest = C.p(dest_rel)
    lines = dest.read_text(encoding="utf-8").splitlines()
    existing = {rx.match(ln).group(1) for ln in lines if rx.match(ln)}
    dupes = [rx.match(ln).group(1) for ln in new if rx.match(ln).group(1) in existing]
    if dupes:
        print(f"  ! {src.name}: IDs already present, skipped: {dupes}")
    new = [ln for ln in new if rx.match(ln).group(1) not in existing]
    if not new:
        print(f"{src.name}: nothing to add")
        return len(dupes)
    # rows of this kind form one contiguous table (for VERIFY: inside the "## Open" section)
    start, end = 0, len(lines)
    if anchor_section:
        start = next((i for i, ln in enumerate(lines) if ln.strip() == anchor_section), 0)
        if start:
            end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
    idx = [i for i in range(start, end) if rx.match(lines[i])]
    if idx:
        first, last = idx[0], idx[-1]
        block = lines[first:last + 1] + new
        block.sort(key=lambda x: int(rx.match(x).group(2)) if rx.match(x) else 10**9)
        lines[first:last + 1] = block
    else:  # empty table: insert after the header separator row in the region
        sep = next(i for i in range(start, end) if lines[i].startswith("|---"))
        lines[sep + 1:sep + 1] = sorted(new, key=lambda x: int(rx.match(x).group(2)))
    if not dry:
        dest.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{src.name}: added {len(new)} row(s) to {dest_rel}")
    return len(dupes)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Merge build-agent outputs into shared files.")
    ap.add_argument("--mapping", action="append", default=[])
    ap.add_argument("--sources", action="append", default=[])
    ap.add_argument("--verify", action="append", default=[])
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args(argv)
    problems = 0
    for s in a.sources:
        problems += insert_rows("S", Path(s), C.SOURCES_REL, None, a.dry_run)
    for v in a.verify:
        problems += insert_rows("V", Path(v), C.VERIFY_REL, "## Open", a.dry_run)
    for m in a.mapping:
        problems += apply_mapping(Path(m), a.dry_run)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
