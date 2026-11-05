#!/usr/bin/env python3
"""Assemble, render and score full-length mock exams (5 essays + 1 PT + 200 MBE questions).

Build
  python scripts/build_simulation.py build                 # next SIM-## id, random seed
  python scripts/build_simulation.py build --seed 42 --allow-short
  python scripts/build_simulation.py render SIM-01          # rewrite booklets from the manifest
Score the MBE part after you sit it
  python scripts/build_simulation.py score SIM-01 --mbe-answers my-answers.txt
      (answers file: 200 letters A-D in order; whitespace/commas/newlines ignored; '-' = blank)

Assembly rules
  * Essays: 5, shaped like a real session: exactly one involves PR, at least one crossover, at least
    one California-law subject (CP/Wills/Trusts), no subject in two essays; weighted by past-exam
    frequency (06-past-exams/index.csv); essays used in an earlier simulation are excluded.
  * PT: 1 not used in an earlier simulation.
  * MBE: 200 = 29 x 4 subjects + 28 x 3 subjects (rotated by seed) — NCBE scores 25 per subject plus
    25 unscored pretest items, so a near-even split mirrors the real exam. Within a subject, questions
    are spread round-robin across NCBE categories. Previously-simulated questions are excluded.
  * Without --allow-short, the build fails if the bank cannot supply a complete exam.

Outputs
  07-question-bank/simulations/SIM-##.yaml   manifest (committed)
  exports/SIM-##/                            printable booklets + answer key (gitignored)
"""
from __future__ import annotations

import argparse
import random
import re
import sys
from collections import Counter, defaultdict

import yaml

import common as C
import quiz

ESSAYS_PER_EXAM, MBE_TOTAL = 5, 200


def used_items() -> set[str]:
    used: set[str] = set()
    base = C.p(C.SIM_DIR_REL)
    for f in sorted(base.glob("SIM-*.yaml")) if base.exists() else []:
        d = C.load_yaml(f) or {}
        used |= set(d.get("essays") or []) | set((d.get("mbe") or {}).get("am", [])) | \
            set((d.get("mbe") or {}).get("pm", []))
        if d.get("pt"):
            used.add(d["pt"])
    return used


def next_id() -> str:
    base = C.p(C.SIM_DIR_REL)
    nums = [int(m.group(1)) for f in (base.glob("SIM-*.yaml") if base.exists() else [])
            if (m := C.SIM_ID_RE.match(f.stem))]
    return f"SIM-{(max(nums) + 1) if nums else 1:02d}"


def subject_weights() -> dict[str, float]:
    counts = Counter()
    for r in C.read_csv(C.p(C.PAST_INDEX_REL)):
        if r.get("type") == "essay":
            counts.update(C.split_list(r["subjects"]))
    return {c: float(counts.get(c, 0)) + 1.0 for c in C.SUBJECTS}  # +1 smoothing


CA_LAW_SUBJECTS = {"CMP", "WIL", "TRS"}


def pick_essays(rng: random.Random, used: set[str]) -> tuple[list[str], int]:
    """Five essays shaped like a real California session.

    Constraints, relaxed in order only if the bank cannot meet them: exactly one essay involves
    Professional Responsibility; at least one crossover; at least one California-law subject
    (Community Property, Wills, Trusts); no subject appears in two essays. Remaining picks are
    weighted by past-exam frequency of the essay's subjects.
    """
    items = [e for e in C.load_md_items(C.ESSAY_DIR_REL) if e["_fm"].get("id") and e["_fm"]["id"] not in used]
    weights = subject_weights()
    subj = lambda e: set(e["_fm"].get("subjects") or [])
    wt = lambda e: max(weights.get(s, 1.0) for s in subj(e)) if subj(e) else 1.0
    chosen: list[dict] = []
    covered: set[str] = set()

    def take(cands: list[dict]) -> bool:
        cands = [e for e in cands if e not in chosen]
        if not cands:
            return False
        e = rng.choices(cands, weights=[wt(x) for x in cands], k=1)[0]
        chosen.append(e)
        covered.update(subj(e))
        return True

    fresh = lambda e: not (subj(e) & covered)
    # 1. exactly one PR essay (single or crossover)
    take([e for e in items if "PRF" in subj(e)])
    # 2. at least one crossover
    if not any(e["_fm"].get("type") == "crossover" for e in chosen):
        take([e for e in items if e["_fm"].get("type") == "crossover" and fresh(e) and "PRF" not in subj(e)])
    # 3. at least one California-law subject
    if not (covered & CA_LAW_SUBJECTS):
        take([e for e in items if subj(e) & CA_LAW_SUBJECTS and fresh(e) and "PRF" not in subj(e)])
    # 4. fill with essays on new subjects, no further PR
    while len(chosen) < ESSAYS_PER_EXAM and take([e for e in items if fresh(e) and "PRF" not in subj(e)]):
        pass
    # 5. relax: distinct primary subject only
    primaries = {e["_fm"]["subjects"][0] for e in chosen}
    while len(chosen) < ESSAYS_PER_EXAM and take([e for e in items if e["_fm"]["subjects"][0] not in primaries]):
        primaries.add(chosen[-1]["_fm"]["subjects"][0])
    rng.shuffle(chosen)
    return [e["_fm"]["id"] for e in chosen], ESSAYS_PER_EXAM - len(chosen)


def pick_pt(rng: random.Random, used: set[str]) -> str | None:
    pts = [x["_fm"]["id"] for x in C.load_md_items(C.PT_DIR_REL) if x["_fm"].get("id") and x["_fm"]["id"] not in used]
    return rng.choice(pts) if pts else None


def pick_mcqs(rng: random.Random, used: set[str]) -> tuple[list[str], dict[str, int]]:
    codes = list(C.MBE_CODES)
    rng.shuffle(codes)
    quotas = {c: (29 if i < 4 else 28) for i, c in enumerate(codes)}
    bank = [q for q in C.load_mcqs() if q["id"] not in used]
    chosen, short = [], {}
    for code, quota in quotas.items():
        by_cat: dict[str, list[str]] = defaultdict(list)
        for q in bank:
            if q["subject"] == code:
                cat = re.sub(r"^(\w+-MBE-[IVX]+).*$", r"\1", (q.get("coverage_ids") or ["?"])[0])
                by_cat[cat].append(q["id"])
        for lst in by_cat.values():
            rng.shuffle(lst)
        cats = sorted(by_cat)
        rng.shuffle(cats)
        got = []
        while len(got) < quota and any(by_cat.values()):
            for cat in cats:
                if by_cat[cat] and len(got) < quota:
                    got.append(by_cat[cat].pop())
        if len(got) < quota:
            short[code] = quota - len(got)
        chosen += got
    rng.shuffle(chosen)
    return chosen, short


def section(body: str, name: str) -> str:
    m = re.search(rf"(?ms)^## {re.escape(name)}\s*\n(.*?)(?=^## |\Z)", body)
    return m.group(1).strip() if m else ""


def render(manifest: dict) -> None:
    sid = manifest["id"]
    out = C.p(C.EXPORTS_REL, sid)
    out.mkdir(parents=True, exist_ok=True)
    essays = {e["_fm"]["id"]: e for e in C.load_md_items(C.ESSAY_DIR_REL)}
    pts = {e["_fm"]["id"]: e for e in C.load_md_items(C.PT_DIR_REL)}
    bank = {q["id"]: q for q in C.load_mcqs()}

    def essay_block(i, eid):
        b = essays[eid]["_body"]
        return f"## Essay {i}\n\n{section(b, 'Facts')}\n\n**{section(b, 'Call of the Question')}**\n\n(60 minutes)\n"

    am = manifest["essays"][:3]
    pm = manifest["essays"][3:]
    (out / "day1-am-essays.md").write_text(
        f"# {sid} — Day 1 morning (3 hours): Essays 1–3\n\nAnswer according to legal theories and principles of "
        "general application unless a question asks you to use California law.\n\n" +
        "\n".join(essay_block(i, e) for i, e in enumerate(am, 1)), encoding="utf-8")
    pt_text = ""
    if manifest.get("pt"):
        b = pts[manifest["pt"]]["_body"]
        pt_text = (f"\n## Performance Test (90 minutes)\n\n### Task Memorandum\n\n{section(b, 'Task Memorandum')}\n\n"
                   f"### File\n\n{section(b, 'File')}\n\n### Library\n\n{section(b, 'Library')}\n")
    (out / "day1-pm-essays-pt.md").write_text(
        f"# {sid} — Day 1 afternoon (3.5 hours): Essays 4–5 and the Performance Test\n\n" +
        "\n".join(essay_block(i, e) for i, e in enumerate(pm, 4)) + pt_text, encoding="utf-8")
    key = [f"# {sid} — MBE answer key\n", "| # | Question | Answer | Subject |", "|---|---|---|---|"]
    for label, ids, start in [("am", manifest["mbe"]["am"], 1), ("pm", manifest["mbe"]["pm"], 101)]:
        lines = [f"# {sid} — Day 2 {'morning' if label == 'am' else 'afternoon'} MBE (3 hours, 100 questions)\n"]
        for n, qid in enumerate(ids, start):
            q = bank[qid]
            lines += [f"**{n}.** {q['stem']}\n", f"{q['call']}\n"] + [f"- ({k}) {q['options'][k]}" for k in "ABCD"] + [""]
            key.append(f"| {n} | {qid} | {q['answer']} | {q['subject']} |")
        (out / f"day2-{label}-mbe.md").write_text("\n".join(lines), encoding="utf-8")
    (out / "answer-key.md").write_text("\n".join(key) + "\n", encoding="utf-8")
    print(f"rendered booklets to {out.relative_to(C.root())}/")


def cmd_build(a) -> int:
    seed = a.seed if a.seed is not None else random.randrange(1, 10**6)
    rng = random.Random(seed)
    used = used_items()
    essays, essay_short = pick_essays(rng, used)
    pt = pick_pt(rng, used)
    mcqs, mcq_short = pick_mcqs(rng, used)
    complete = essay_short == 0 and pt is not None and not mcq_short
    shortfall = {}
    if essay_short:
        shortfall["essays"] = essay_short
    if pt is None:
        shortfall["pt"] = 1
    if mcq_short:
        shortfall["mcq"] = mcq_short
    if not complete and not a.allow_short:
        print(f"Bank too small for a full exam: shortfall {shortfall}. Re-run with --allow-short for a partial mock.")
        return 1
    sid = a.id or next_id()
    manifest = {"id": sid, "created": C.today(), "seed": seed, "essays": essays, "pt": pt,
                "mbe": {"am": mcqs[:100], "pm": mcqs[100:200]}, "complete": complete}
    if shortfall:
        manifest["shortfall"] = shortfall
    path = C.p(C.SIM_DIR_REL, f"{sid}.yaml")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(manifest, sort_keys=False), encoding="utf-8")
    print(f"wrote {path.relative_to(C.root())}: {len(essays)} essays, PT={pt}, {len(mcqs)} MCQs"
          + ("" if complete else f" (PARTIAL, shortfall {shortfall})"))
    if not a.no_render:
        render(manifest)
    return 0


def parse_answers(text: str) -> list[str]:
    return [ch for ch in text.upper() if ch in "ABCD-"]


def cmd_score(a) -> int:
    manifest = C.load_yaml(C.p(C.SIM_DIR_REL, f"{a.id}.yaml"))
    ids = manifest["mbe"]["am"] + manifest["mbe"]["pm"]
    answers = parse_answers(open(a.mbe_answers, encoding="utf-8").read())
    if len(answers) != len(ids):
        raise SystemExit(f"expected {len(ids)} answers, got {len(answers)}")
    bank = {q["id"]: q for q in C.load_mcqs()}
    by: dict[str, list[int]] = defaultdict(list)
    for qid, ans in zip(ids, answers):
        q = bank[qid]
        row = quiz.log_mcq(q, "" if ans == "-" else ans, None, "", notes=a.id)
        by[q["subject"]].append(1 if row["correct"] == "Y" else 0)
    total = sum(sum(v) for v in by.values())
    quiz.log_attempt(kind="simulation", item_id=a.id, subject="MIX", score=total, max_score=len(ids),
                     source="repo", notes="MBE portion")
    print(f"{a.id} MBE: {total}/{len(ids)} ({100 * total / len(ids):.1f}%)\n\n| Subject | Correct | Accuracy |\n|---|---|---|")
    for code in C.MBE_CODES:
        v = by.get(code, [])
        if v:
            print(f"| {C.SUBJECTS[code].name} | {sum(v)}/{len(v)} | {100 * sum(v) / len(v):.0f}% |")
    print("\nEssays and the PT are graded with /essay and /pt and logged with `quiz.py log --kind essay|pt`.")
    return 0


def cmd_render(a) -> int:
    path = C.p(C.SIM_DIR_REL, f"{a.id}.yaml")
    if not path.exists():
        raise SystemExit(f"{a.id}: manifest not found")
    render(C.load_yaml(path))
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Assemble/score full mock exams.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build")
    b.add_argument("--id")
    b.add_argument("--seed", type=int)
    b.add_argument("--allow-short", action="store_true")
    b.add_argument("--no-render", action="store_true")
    s = sub.add_parser("score")
    s.add_argument("id")
    s.add_argument("--mbe-answers", required=True)
    r = sub.add_parser("render", help="(re)write printable booklets for an existing manifest")
    r.add_argument("id")
    a = ap.parse_args(argv)
    return {"build": cmd_build, "score": cmd_score, "render": cmd_render}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
