#!/usr/bin/env python3
"""MBE-style quiz from the question bank, logging every attempt to 10-progress/attempts.csv.

Interactive (terminal):
  python scripts/quiz.py run --subject evidence --n 10 --timed
  python scripts/quiz.py run --subject mixed --n 33 --difficulty 2 --subtopic EVD-MBE-V

Building blocks (used by the /quiz slash command):
  python scripts/quiz.py pick --subject EVD --n 5 [--difficulty 2] [--subtopic EVD-MBE-V] [--seed 7]
  python scripts/quiz.py show Q-EVD-0001 [--reveal]
  python scripts/quiz.py log  --id Q-EVD-0001 --answer B --seconds 95 [--error-type misread]
  python scripts/quiz.py log  --kind essay --item E-CTR-001 --subject CTR --score 65 --max 100 \
                              --rules "R-CTR-004;R-CTR-011" --error-type misapplied
  python scripts/quiz.py log  --source official --item "NCBE-OPE-4-Q17" --subject EVD --correct N \
                              --seconds 120 --coverage EVD-MBE-V.F       # licensed question: no text stored
  python scripts/quiz.py stats

Selection policy for `pick`/`run` (spaced practice):
  1. questions answered wrong whose last attempt is >= 2 days old (review),
  2. never-attempted questions,
  3. everything else, least recently seen first.
`mixed` draws evenly across the 7 MBE subjects.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import random
import sys
import textwrap
import time

import common as C

TARGET_SECONDS = 108  # ~1.8 minutes per MBE question (200 questions / 6 hours)


def last_attempts(attempts: list[dict]) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for a in attempts:
        if a["kind"] == "mcq" and a["source"] == "repo":
            out[a["item_id"]] = a  # file order == chronological order
    return out


def filter_bank(bank: list[dict], subject: str | None, difficulty: int | None, subtopic: str | None) -> list[dict]:
    out = []
    for q in bank:
        if subject and subject != "MIX" and q.get("subject") != subject:
            continue
        if difficulty and q.get("difficulty") != difficulty:
            continue
        if subtopic and not any(c == subtopic or c.startswith(subtopic + ".") or c.startswith(subtopic)
                                for c in q.get("coverage_ids") or []):
            continue
        out.append(q)
    return out


def prioritize(pool: list[dict], attempts: list[dict], rng: random.Random) -> list[dict]:
    last = last_attempts(attempts)
    today = dt.date.today()
    review, unseen, rest = [], [], []
    for q in pool:
        a = last.get(q["id"])
        if a is None:
            unseen.append(q)
        elif a["correct"] == "N" and (today - dt.date.fromisoformat(a["date"])).days >= 2:
            review.append(q)
        else:
            rest.append((a["date"], q))
    rng.shuffle(review)
    rng.shuffle(unseen)
    rest.sort(key=lambda x: x[0])
    return review + unseen + [q for _, q in rest]


def pick(subject: str, n: int, difficulty: int | None = None, subtopic: str | None = None,
         seed: int | None = None) -> list[dict]:
    rng = random.Random(seed)
    bank = C.load_mcqs()
    attempts = C.load_attempts()
    if subject == "MIX":
        per = {c: prioritize(filter_bank(bank, c, difficulty, subtopic), attempts, rng) for c in C.MBE_CODES}
        chosen, i = [], 0
        while len(chosen) < n and any(per.values()):
            code = C.MBE_CODES[i % len(C.MBE_CODES)]
            if per[code]:
                chosen.append(per[code].pop(0))
            i += 1
        rng.shuffle(chosen)
        return chosen
    return prioritize(filter_bank(bank, subject, difficulty, subtopic), attempts, rng)[:n]


def find(qid: str) -> dict:
    for q in C.load_mcqs():
        if q["id"] == qid:
            return q
    raise SystemExit(f"question {qid} not found")


def render(q: dict, number: int | None = None, reveal: bool = False) -> str:
    w = lambda s: textwrap.fill(" ".join(str(s).split()), width=96)
    head = f"Question {number} " if number else ""
    lines = [f"{head}[{q['id']} · {C.SUBJECTS[q['subject']].name} · difficulty {q['difficulty']}]", "",
             w(q["stem"]), "", w(q["call"]), ""]
    for k in "ABCD":
        lines.append(textwrap.fill(f"({k}) {q['options'][k]}", width=96, subsequent_indent="    "))
    if reveal:
        lines += ["", explanation(q)]
    return "\n".join(lines)


def explanation(q: dict) -> str:
    w = lambda s: textwrap.fill(" ".join(str(s).split()), width=96, subsequent_indent="    ")
    out = [f"Correct answer: ({q['answer']})", w("Why: " + q["explanation_correct"]), ""]
    for k in "ABCD":
        if k != q["answer"]:
            out.append(w(f"({k}) wrong: {q['explanation_each_wrong_option'][k]}"))
    out += ["", f"Trap type: {q['trap_type']}", "Authority: " + "; ".join(q["authority"]),
            "Rules: " + ", ".join(q["rule_ids"]) + "   Coverage: " + ", ".join(q["coverage_ids"])]
    return "\n".join(out)


def log_attempt(**kw) -> dict:
    attempts = C.load_attempts()
    row = {c: "" for c in C.ATTEMPT_COLUMNS}
    row.update({k: ("" if v is None else str(v)) for k, v in kw.items() if k in row})
    row["attempt_id"] = C.next_attempt_id(attempts)
    row["date"] = row["date"] or C.today()
    if row["kind"] not in C.ATTEMPT_KINDS:
        raise SystemExit(f"kind must be one of {sorted(C.ATTEMPT_KINDS)}")
    if row["error_type"] not in C.ERROR_TYPES:
        raise SystemExit(f"error_type must be one of {sorted(C.ERROR_TYPES)}")
    if row["source"] not in C.ATTEMPT_SOURCES:
        raise SystemExit(f"source must be one of {sorted(C.ATTEMPT_SOURCES)}")
    C.append_csv_row(C.p(C.ATTEMPTS_REL), C.ATTEMPT_COLUMNS, row)
    return row


def log_mcq(q: dict, answer: str, seconds: float | None, error_type: str = "", notes: str = "") -> dict:
    answer = answer.strip().upper()
    correct = answer == q["answer"]
    return log_attempt(kind="mcq", item_id=q["id"], subject=q["subject"], coverage_ids=";".join(q["coverage_ids"]),
                       score=1 if correct else 0, max_score=1, correct="Y" if correct else "N",
                       answer_given=answer, time_seconds=round(seconds) if seconds is not None else "",
                       rule_ids_missed="" if correct else ";".join(q["rule_ids"]),
                       error_type="none" if correct else (error_type or "didnt-know"), source="repo", notes=notes)


# --------------------------------------------------------------------------- commands
def cmd_pick(a) -> int:
    qs = pick(a.subject, a.n, a.difficulty, a.subtopic, a.seed)
    if a.full:
        print(json.dumps([{k: v for k, v in q.items() if not k.startswith("_")} for q in qs], indent=2))
    else:
        print(json.dumps([q["id"] for q in qs]))
    if len(qs) < a.n:
        print(f"note: only {len(qs)} matching question(s) in the bank", file=sys.stderr)
    return 0


def cmd_show(a) -> int:
    print(render(find(a.id), reveal=a.reveal))
    return 0


def cmd_log(a) -> int:
    if a.kind == "mcq" and a.source == "repo":
        if not a.id or not a.answer:
            raise SystemExit("repo MCQ logging needs --id and --answer")
        q = find(a.id)
        row = log_mcq(q, a.answer, a.seconds, a.error_type or "", a.notes or "")
        print(("CORRECT" if row["correct"] == "Y" else f"WRONG (you: {row['answer_given']})") + f" — logged {row['attempt_id']}")
        print(explanation(q))
        return 0
    subject = C.resolve_subject(a.subject) if a.subject else ""
    if a.subject and not subject and a.subject.upper() in {"MIX", "PT", "XO"}:
        subject = a.subject.upper()
    if a.kind == "mcq":
        if a.correct not in {"Y", "N"}:
            raise SystemExit("non-repo MCQ logging needs --correct Y|N")
        score, max_score, correct = (1 if a.correct == "Y" else 0), 1, a.correct
    else:
        if a.score is None:
            raise SystemExit(f"{a.kind} logging needs --score (and --max)")
        score, max_score, correct = a.score, a.max, ""
    row = log_attempt(kind=a.kind, item_id=a.item or a.id or "", subject=subject, coverage_ids=a.coverage or "",
                      score=score, max_score=max_score, correct=correct, answer_given=a.answer or "",
                      time_seconds=round(a.seconds) if a.seconds is not None else "", rule_ids_missed=a.rules or "",
                      error_type=a.error_type or ("none" if correct == "Y" else ""), source=a.source,
                      notes=a.notes or "")
    print(f"logged {row['attempt_id']}: {row['kind']} {row['item_id']} {row['score']}/{row['max_score']}")
    return 0


def ask(prompt: str) -> str:
    """input() that treats end-of-input (Ctrl-D / closed pipe) as quit."""
    try:
        return input(prompt)
    except EOFError:
        print()
        return "Q"


def cmd_run(a) -> int:
    qs = pick(a.subject, a.n, a.difficulty, a.subtopic, a.seed)
    if not qs:
        print("No matching questions in the bank yet.")
        return 1
    right, total_t = 0, 0.0
    for i, q in enumerate(qs, start=1):
        print("\n" + "=" * 96 + "\n" + render(q, i) + "\n")
        t0 = time.monotonic()
        ans = ""
        while ans not in {"A", "B", "C", "D", "Q"}:
            ans = ask("Your answer (A-D, Q to quit): ").strip().upper()
        if ans == "Q":
            break
        secs = time.monotonic() - t0
        total_t += secs
        err = ""
        if ans != q["answer"]:
            print("Why did you miss it? 1=didn't know rule 2=misapplied 3=misread facts 4=timing 5=careless")
            err = {"1": "didnt-know", "2": "misapplied", "3": "misread", "4": "timing", "5": "careless"}.get(
                ask("> ").strip(), "didnt-know")
        row = log_mcq(q, ans, secs, err)
        right += row["correct"] == "Y"
        flag = "  (over 1.8 min)" if a.timed and secs > TARGET_SECONDS else ""
        print(("\nCORRECT" if row["correct"] == "Y" else "\nWRONG") + f" — {secs:.0f}s{flag}\n" + explanation(q))
    done = i if ans != "Q" else i - 1
    if done:
        print(f"\nScore: {right}/{done} ({100 * right / done:.0f}%) · avg {total_t / done:.0f}s per question "
              f"(target ≤ {TARGET_SECONDS}s). Logged to {C.ATTEMPTS_REL}.")
    return 0


def cmd_stats(_a) -> int:
    rows = [r for r in C.load_attempts() if r["kind"] == "mcq"]
    if not rows:
        print("No MCQ attempts logged yet.")
        return 0
    by: dict[str, list[int]] = {}
    for r in rows:
        by.setdefault(r["subject"] or "?", []).append(1 if r["correct"] == "Y" else 0)
    print("| Subject | Attempts | Accuracy |\n|---|---|---|")
    for s, v in sorted(by.items()):
        print(f"| {s} | {len(v)} | {100 * sum(v) / len(v):.0f}% |")
    allv = [x for v in by.values() for x in v]
    print(f"| **All** | {len(allv)} | {100 * sum(allv) / len(allv):.0f}% |")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="MBE-style quiz and attempt logger.")
    sub = ap.add_subparsers(dest="cmd", required=True)

    def add_filters(sp):
        sp.add_argument("--subject", default="MIX", help="code/slug/name, or 'mixed'")
        sp.add_argument("--n", type=int, default=10)
        sp.add_argument("--difficulty", type=int, choices=[1, 2, 3])
        sp.add_argument("--subtopic", help="coverage_id prefix, e.g. EVD-MBE-V")
        sp.add_argument("--seed", type=int)

    sp = sub.add_parser("pick")
    add_filters(sp)
    sp.add_argument("--full", action="store_true", help="print full question JSON (includes answers)")
    sp = sub.add_parser("run")
    add_filters(sp)
    sp.add_argument("--timed", action="store_true")
    sp = sub.add_parser("show")
    sp.add_argument("id")
    sp.add_argument("--reveal", action="store_true")
    sp = sub.add_parser("log")
    sp.add_argument("--kind", default="mcq", choices=sorted(C.ATTEMPT_KINDS))
    sp.add_argument("--id", help="bank question id (repo MCQ)")
    sp.add_argument("--item", help="item id for non-MCQ or non-repo items")
    sp.add_argument("--answer")
    sp.add_argument("--correct", choices=["Y", "N"])
    sp.add_argument("--score", type=float)
    sp.add_argument("--max", type=float, default=100)
    sp.add_argument("--seconds", type=float)
    sp.add_argument("--subject")
    sp.add_argument("--coverage", help="';'-separated coverage_ids")
    sp.add_argument("--rules", help="';'-separated rule_ids missed")
    sp.add_argument("--error-type", choices=sorted(C.ERROR_TYPES - {""}))
    sp.add_argument("--source", default="repo", choices=sorted(C.ATTEMPT_SOURCES))
    sp.add_argument("--notes")
    sub.add_parser("stats")
    a = ap.parse_args(argv)
    if getattr(a, "subject", None) is not None and a.cmd in {"pick", "run"}:
        a.subject = "MIX" if a.subject.lower() in {"mixed", "mix"} else (C.resolve_subject(a.subject) or a.subject)
        if a.subject != "MIX" and a.subject not in C.MBE_CODES:
            raise SystemExit(f"--subject must be an MBE subject or 'mixed' (got {a.subject})")
    return {"pick": cmd_pick, "show": cmd_show, "log": cmd_log, "run": cmd_run, "stats": cmd_stats}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
