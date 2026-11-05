"""Shared constants, paths and loaders for the CA Bar knowledge-base scripts.

Every script in scripts/ imports this module. Running `python scripts/<name>.py`
puts scripts/ on sys.path, so `import common` works without packaging.

Set the environment variable CABAR_ROOT to point the tools at another repo
root (the test suite does this with a temporary fixture repo).
"""
from __future__ import annotations

import csv
import datetime as dt
import hashlib
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator

import yaml

# --------------------------------------------------------------------------- paths
ROOT = Path(os.environ.get("CABAR_ROOT", Path(__file__).resolve().parent.parent)).resolve()


def root() -> Path:
    """Repo root (re-read CABAR_ROOT so tests can switch roots at runtime)."""
    return Path(os.environ.get("CABAR_ROOT", ROOT)).resolve()


def p(*parts: str) -> Path:
    return root().joinpath(*parts)


MATRIX_REL = "00-exam-intel/coverage-matrix.csv"
SOURCES_REL = "00-exam-intel/sources.md"
VERIFY_REL = "VERIFY-QUEUE.md"
PLAN_REL = "config/plan.yml"
ATTEMPTS_REL = "10-progress/attempts.csv"
ERROR_LOG_REL = "10-progress/error-log.md"
DASHBOARD_REL = "10-progress/readiness-dashboard.md"
PAST_INDEX_REL = "06-past-exams/index.csv"
PAST_PT_INDEX_REL = "04-performance-test/past-pt-index.csv"
FREQ_REL = "06-past-exams/frequency-analysis.md"
SCHEMA_DIR_REL = "07-question-bank/schema"
MCQ_DIR_REL = "07-question-bank/mcq"
ESSAY_DIR_REL = "07-question-bank/essays"
PT_DIR_REL = "07-question-bank/pt"
SIM_DIR_REL = "07-question-bank/simulations"
SUBJECTS_DIR_REL = "03-subjects"
EXPORTS_REL = "exports"

# --------------------------------------------------------------------------- subjects


@dataclass(frozen=True)
class Subject:
    code: str
    name: str
    slug: str
    mbe: bool
    ca_law: bool  # California law governs the essay (vs. general principles + CA distinctions)


SUBJECTS: dict[str, Subject] = {s.code: s for s in [
    Subject("BUS", "Business Associations", "business-associations", False, False),
    Subject("CIV", "Civil Procedure", "civil-procedure", True, False),
    Subject("CMP", "Community Property", "community-property", False, True),
    Subject("CON", "Constitutional Law", "constitutional-law", True, False),
    Subject("CTR", "Contracts", "contracts", True, False),
    Subject("CRM", "Criminal Law and Procedure", "criminal-law-procedure", True, False),
    Subject("EVD", "Evidence", "evidence", True, False),
    Subject("PRF", "Professional Responsibility", "professional-responsibility", False, True),
    Subject("PRP", "Real Property", "real-property", True, False),
    Subject("REM", "Remedies", "remedies", False, False),
    Subject("TRT", "Torts", "torts", True, False),
    Subject("WIL", "Wills and Succession", "wills-succession", False, True),
    Subject("TRS", "Trusts", "trusts", False, True),
]}
SLUG_TO_CODE = {s.slug: c for c, s in SUBJECTS.items()}
MBE_CODES = [c for c, s in SUBJECTS.items() if s.mbe]
EXTRA_CODES = {"PT": "Performance Test"}  # coverage-matrix-only pseudo subject

# Non-subject values allowed in front-matter `subject`
META_SUBJECTS = {"exam-intel", "study-plan", "foundations", "performance-test", "mbe",
                 "past-exams", "question-bank", "high-yield", "exam-strategy", "progress", "meta",
                 "crossover"}

SUBJECT_FILES = ["README.md", "primer.md", "outline.md", "rule-statements.md", "ca-distinctions.md",
                 "mbe-rules.md", "issue-checklist.md", "attack-outline.md", "flowcharts.md",
                 "worked-examples.md", "traps.md", "key-authorities.md", "essay-templates.md",
                 "memorization-list.md", "flashcards.csv"]


def resolve_subject(token: str) -> str | None:
    """Accept a code (EVD), slug (evidence) or name (Evidence); return the code."""
    t = token.strip()
    if t.upper() in SUBJECTS:
        return t.upper()
    if t.lower() in SLUG_TO_CODE:
        return SLUG_TO_CODE[t.lower()]
    for c, s in SUBJECTS.items():
        if s.name.lower() == t.lower():
            return c
    return None


# --------------------------------------------------------------------------- IDs
RULE_ID_RE = re.compile(r"\bR-([A-Z]{3})-(\d{3})\b")
RULE_HEADING_RE = re.compile(r"^#{2,4}\s+(R-[A-Z]{3}-\d{3})\b")
MCQ_ID_RE = re.compile(r"^Q-([A-Z]{3})-(\d{4})$")
ESSAY_ID_RE = re.compile(r"^E-([A-Z]{3}|XO)-(\d{3})$")
PT_ID_RE = re.compile(r"^PT-(\d{3})$")
SIM_ID_RE = re.compile(r"^SIM-(\d{2})$")
FLASH_ID_RE = re.compile(r"^F-([A-Z]{3})-(\d{4})$")

# --------------------------------------------------------------------------- CSV schemas
ATTEMPT_COLUMNS = ["attempt_id", "date", "kind", "item_id", "subject", "coverage_ids", "score",
                   "max_score", "correct", "answer_given", "time_seconds", "rule_ids_missed",
                   "error_type", "source", "notes"]
ATTEMPT_KINDS = {"mcq", "essay", "pt", "drill", "spot", "simulation"}
ERROR_TYPES = {"", "none", "didnt-know", "misapplied", "misread", "timing", "careless"}
ATTEMPT_SOURCES = {"repo", "official", "commercial", "past-exam"}

FLASHCARD_COLUMNS = ["id", "front", "back", "rule_id", "tags"]
PAST_INDEX_COLUMNS = ["exam", "q_num", "type", "subjects", "issues", "call_summary", "question_link",
                      "selected_answers_link", "analysis_file", "notes"]
PAST_PT_COLUMNS = ["exam", "pt_id", "title", "task_type", "area", "question_link",
                   "selected_answers_link", "analysis_file", "notes"]


def read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def csv_header(path: Path) -> list[str] | None:
    if not path.exists():
        return None
    with path.open(newline="", encoding="utf-8") as fh:
        return next(csv.reader(fh), None)


def append_csv_row(path: Path, columns: list[str], row: dict) -> None:
    new = not path.exists() or path.stat().st_size == 0
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=columns, extrasaction="raise")
        if new:
            w.writeheader()
        w.writerow({c: row.get(c, "") for c in columns})


def split_list(value: str) -> list[str]:
    return [x.strip() for x in (value or "").split(";") if x.strip()]


# --------------------------------------------------------------------------- front matter
def parse_front_matter(text: str) -> tuple[dict | None, str]:
    """Return (front-matter dict or None, body)."""
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---", 4)
    if end == -1:
        return None, text
    try:
        data = yaml.safe_load(text[4:end])
    except yaml.YAMLError:
        return None, text
    body = text[end + 4:].lstrip("\n")
    return (normalize(data) if isinstance(data, dict) else None), body


def normalize(obj):
    """Convert YAML dates to ISO strings so JSON Schema validation works."""
    if isinstance(obj, dict):
        return {k: normalize(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [normalize(v) for v in obj]
    if isinstance(obj, (dt.date, dt.datetime)):
        return obj.isoformat()
    return obj


def load_yaml(path: Path):
    with path.open(encoding="utf-8") as fh:
        return normalize(yaml.safe_load(fh))


# --------------------------------------------------------------------------- loaders
def load_matrix() -> list[dict]:
    return read_csv(p(MATRIX_REL))


def load_plan() -> dict:
    path = p(PLAN_REL)
    return load_yaml(path) if path.exists() else {}


def iter_mcq_files() -> Iterator[Path]:
    base = p(MCQ_DIR_REL)
    if base.exists():
        yield from sorted(base.rglob("*.yaml"))
        yield from sorted(base.rglob("*.yml"))


def load_mcqs() -> list[dict]:
    """All MCQs. A YAML file holds one question (mapping) or `questions: [...]`."""
    out = []
    for f in iter_mcq_files():
        data = load_yaml(f)
        items = data.get("questions", []) if isinstance(data, dict) and "questions" in data else [data]
        for q in items:
            if isinstance(q, dict):
                q = dict(q)
                q["_file"] = str(f.relative_to(root()))
                out.append(q)
    return out


def load_md_items(rel_dir: str) -> list[dict]:
    """Essay / PT markdown items: front matter + body + path."""
    base = p(rel_dir)
    out = []
    if not base.exists():
        return out
    for f in sorted(base.rglob("*.md")):
        if f.name == "README.md":
            continue
        fm, body = parse_front_matter(f.read_text(encoding="utf-8"))
        out.append({"_file": str(f.relative_to(root())), "_fm": fm or {}, "_body": body})
    return out


def load_rules() -> dict[str, dict]:
    """rule_id -> {subject, file, title, line} from every rule-statements.md."""
    rules: dict[str, dict] = {}
    base = p(SUBJECTS_DIR_REL)
    if not base.exists():
        return rules
    for f in sorted(base.glob("*/rule-statements.md")):
        for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), start=1):
            m = RULE_HEADING_RE.match(line)
            if m:
                rid = m.group(1)
                rules.setdefault(rid, {"subject": rid[2:5], "file": str(f.relative_to(root())),
                                       "title": line.lstrip("#").strip(), "line": n, "dupes": []})
                if rules[rid]["line"] != n or rules[rid]["file"] != str(f.relative_to(root())):
                    rules[rid]["dupes"].append(f"{f.relative_to(root())}:{n}")
    return rules


def load_flashcards() -> list[dict]:
    cards = []
    base = p(SUBJECTS_DIR_REL)
    if not base.exists():
        return cards
    for f in sorted(base.glob("*/flashcards.csv")):
        for r in read_csv(f):
            r = dict(r)
            r["_file"] = str(f.relative_to(root()))
            cards.append(r)
    return cards


def load_attempts() -> list[dict]:
    return read_csv(p(ATTEMPTS_REL))


def next_attempt_id(attempts: list[dict] | None = None) -> str:
    attempts = load_attempts() if attempts is None else attempts
    nums = [int(a["attempt_id"][2:]) for a in attempts if a.get("attempt_id", "").startswith("A-")
            and a["attempt_id"][2:].isdigit()]
    return f"A-{(max(nums) + 1) if nums else 1:06d}"


def stable_int(text: str, bits: int = 31) -> int:
    """Deterministic integer from text (for Anki model/deck IDs)."""
    return int(hashlib.sha1(text.encode()).hexdigest(), 16) % (1 << bits)


def today() -> str:
    return dt.date.today().isoformat()


# --------------------------------------------------------------------------- markers
def replace_between_markers(text: str, name: str, new_block: str) -> str:
    """Replace content between <!-- BEGIN name --> and <!-- END name --> (append if absent)."""
    begin, end = f"<!-- BEGIN {name} -->", f"<!-- END {name} -->"
    block = f"{begin}\n{new_block.rstrip()}\n{end}"
    if begin in text and end in text:
        pre = text.split(begin)[0]
        post = text.split(end, 1)[1]
        return pre + block + post
    return text.rstrip() + "\n\n" + block + "\n"

def reserved_sim_items() -> set[str]:
    """Item ids (MCQ, essay, PT) set aside for a simulation that has not been sat yet.

    A simulation counts as sat once attempts.csv has a row with kind 'simulation' and item_id SIM-##.
    Practice pickers exclude reserved items so a simulation stays a fresh diagnostic.
    """
    base = p(SIM_DIR_REL)
    if not base.exists():
        return set()
    taken = {a["item_id"] for a in load_attempts() if a.get("kind") == "simulation"}
    out: set[str] = set()
    for f in sorted(base.glob("SIM-*.yaml")):
        d = load_yaml(f) or {}
        if f.stem in taken:
            continue
        mbe = d.get("mbe") or {}
        out |= set(d.get("essays") or []) | set(mbe.get("am") or []) | set(mbe.get("pm") or [])
        if d.get("pt"):
            out.add(d["pt"])
    return out
