#!/usr/bin/env python3
"""Export flashcards (and optionally every rule statement) to an Anki .apkg deck.

Usage
  python scripts/build_anki.py                               # all subjects -> exports/ca-bar-2027-all.apkg
  python scripts/build_anki.py --subject EVD --subject CMP   # selected subjects
  python scripts/build_anki.py --tag must-know               # only cards carrying a tag
  python scripts/build_anki.py --include-rules               # add one card per R-XXX-### rule statement
  python scripts/build_anki.py --out exports/my-deck.apkg

Sources
  03-subjects/<subject>/flashcards.csv   columns: id, front, back, rule_id, tags (tags ';'-separated)
  03-subjects/<subject>/rule-statements.md  "### R-XXX-### Title" + "**Rule (write this):** ..." paragraph

Deck and note IDs are deterministic, so re-importing an updated deck updates cards in place
instead of duplicating them. Output goes to exports/ (gitignored).
"""
from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path

import genanki

import common as C

DECK_ROOT = "CA Bar July 2027"
RULE_TEXT_RE = re.compile(r"\*\*Rule \(write this\):\*\*\s*(.+?)(?=\n\s*\n|\n\*\*|\Z)", re.S)

MODEL = genanki.Model(
    C.stable_int("ca-bar-2027-basic-model"),
    "CA Bar 2027 — Basic",
    fields=[{"name": "Front"}, {"name": "Back"}, {"name": "RuleID"}, {"name": "CardID"}],
    templates=[{
        "name": "Card 1",
        "qfmt": "<div class='front'>{{Front}}</div>",
        "afmt": "{{FrontSide}}<hr id='answer'><div class='back'>{{Back}}</div>"
                "<div class='meta'>{{RuleID}} · {{CardID}}</div>",
    }],
    css=".card{font-family:-apple-system,Segoe UI,sans-serif;font-size:19px;text-align:left;line-height:1.45}"
        ".meta{margin-top:14px;font-size:12px;color:#888}",
)


def md_to_html(text: str) -> str:
    t = html.escape(text.strip())
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<i>\1</i>", t)
    return t.replace("\n", "<br>")


def rule_cards(code: str) -> list[dict]:
    path = C.p(C.SUBJECTS_DIR_REL, C.SUBJECTS[code].slug, "rule-statements.md")
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    cards = []
    parts = re.split(r"(?m)^(#{2,4}\s+R-[A-Z]{3}-\d{3}\b.*)$", text)
    for head, body in zip(parts[1::2], parts[2::2]):
        rid = re.search(r"R-[A-Z]{3}-\d{3}", head).group(0)
        title = head.lstrip("#").strip()
        m = RULE_TEXT_RE.search(body)
        if not m:
            continue
        cards.append({"id": f"RULE-{rid}", "front": f"State the rule: {title}", "back": m.group(1).strip(),
                      "rule_id": rid, "tags": "rule-statement"})
    return cards


def build(subjects: list[str], tags: set[str], include_rules: bool, out: Path) -> tuple[int, Path]:
    decks: dict[str, genanki.Deck] = {}
    count = 0
    for code in subjects:
        name = f"{DECK_ROOT}::{C.SUBJECTS[code].name}"
        deck = decks.setdefault(code, genanki.Deck(C.stable_int(name), name))
        csv_path = C.p(C.SUBJECTS_DIR_REL, C.SUBJECTS[code].slug, "flashcards.csv")
        cards = C.read_csv(csv_path) + (rule_cards(code) if include_rules else [])
        for card in cards:
            card_tags = set(C.split_list(card.get("tags", "")))
            if tags and not (card_tags & tags):
                continue
            anki_tags = sorted({t.replace(" ", "_") for t in card_tags} | {code})
            deck.add_note(genanki.Note(
                model=MODEL,
                fields=[md_to_html(card["front"]), md_to_html(card["back"]), card.get("rule_id", ""), card["id"]],
                tags=anki_tags,
                guid=genanki.guid_for("ca-bar-2027", card["id"]),
            ))
            count += 1
    out.parent.mkdir(parents=True, exist_ok=True)
    genanki.Package([d for d in decks.values()]).write_to_file(str(out))
    return count, out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Build an Anki deck from flashcards and rule statements.")
    ap.add_argument("--subject", action="append", help="subject code/slug (repeatable); default all")
    ap.add_argument("--tag", action="append", default=[], help="only cards with this tag (repeatable)")
    ap.add_argument("--include-rules", action="store_true", help="add one card per rule statement")
    ap.add_argument("--out", help="output .apkg path")
    a = ap.parse_args(argv)
    subjects = [C.resolve_subject(s) for s in a.subject] if a.subject else list(C.SUBJECTS)
    if None in subjects:
        raise SystemExit("unknown subject")
    label = "all" if not a.subject else "-".join(s.lower() for s in subjects)
    out = Path(a.out) if a.out else C.p(C.EXPORTS_REL, f"ca-bar-2027-{label}.apkg")
    n, path = build(subjects, set(a.tag), a.include_rules, out)
    print(f"wrote {n} card(s) to {path}")
    if n == 0:
        print("note: no cards yet — flashcards.csv files are filled in Phase 4/6", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
