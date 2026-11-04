"""End-to-end checks for quiz, coverage report, simulation, Anki, frequency analysis and dashboard."""
from __future__ import annotations

import zipfile

import build_anki
import build_simulation
import common as C
import coverage_report
import dashboard
import frequency_analysis
import quiz
import validate


def test_quiz_pick_filters_and_prioritizes(repo):
    ids = [q["id"] for q in quiz.pick("EVD", 5, seed=1)]
    assert sorted(ids) == ["Q-EVD-0001", "Q-EVD-0002"]
    assert [q["id"] for q in quiz.pick("EVD", 5, subtopic="EVD-MBE-V.F")] == ["Q-EVD-0001"]
    assert [q["id"] for q in quiz.pick("MIX", 10, difficulty=3)] == ["Q-CTR-0001"]


def test_quiz_log_mcq_and_generic(repo, capsys):
    assert quiz.main(["log", "--id", "Q-EVD-0001", "--answer", "c", "--seconds", "100", "--error-type", "misread"]) == 0
    assert quiz.main(["log", "--id", "Q-EVD-0002", "--answer", "D", "--seconds", "80"]) == 0
    assert quiz.main(["log", "--kind", "essay", "--item", "E-EVD-001", "--subject", "evidence", "--score", "65",
                      "--rules", "R-EVD-001", "--error-type", "misapplied"]) == 0
    assert quiz.main(["log", "--source", "official", "--item", "NCBE-OPE-1-Q1", "--subject", "EVD",
                      "--correct", "N", "--coverage", "EVD-MBE-V"]) == 0
    rows = C.load_attempts()
    assert [r["attempt_id"] for r in rows] == ["A-000001", "A-000002", "A-000003", "A-000004"]
    assert rows[0]["correct"] == "N" and rows[0]["rule_ids_missed"] == "R-EVD-001" and rows[0]["error_type"] == "misread"
    assert rows[1]["correct"] == "Y" and rows[1]["error_type"] == "none"
    assert rows[2]["kind"] == "essay" and rows[2]["subject"] == "EVD" and rows[2]["score"] == "65.0"
    assert rows[3]["source"] == "official"
    assert validate.run().errors == []
    # missed question is not yet due for review (same day), unseen questions come first
    assert quiz.pick("MIX", 1, seed=3)[0]["id"] == "Q-CTR-0001"


def test_coverage_report_gate(repo, capsys):
    assert coverage_report.main(["--require-mapped", "EVD"]) == 0
    assert coverage_report.main(["--require-mapped", "CTR"]) == 1
    assert coverage_report.main(["--write"]) == 0
    assert (repo / "10-progress/coverage-report.md").exists()


def test_simulation_short_bank(repo, capsys):
    assert build_simulation.main(["build", "--seed", "5"]) == 1  # bank too small, no --allow-short
    assert build_simulation.main(["build", "--seed", "5", "--allow-short"]) == 0
    m = C.load_yaml(repo / "07-question-bank/simulations/SIM-01.yaml")
    assert m["complete"] is False and m["pt"] == "PT-001"
    assert set(m["essays"]) == {"E-EVD-001", "E-XO-001"} or len(m["essays"]) == 1
    assert len(m["mbe"]["am"]) + len(m["mbe"]["pm"]) == 3
    assert (repo / "exports/SIM-01/answer-key.md").exists()
    assert validate.run().errors == []
    # a second build must not reuse simulated items
    assert build_simulation.main(["build", "--seed", "6", "--allow-short", "--no-render"]) == 0
    m2 = C.load_yaml(repo / "07-question-bank/simulations/SIM-02.yaml")
    assert m2["mbe"]["am"] == [] and m2["pt"] is None


def test_simulation_score(repo, capsys):
    build_simulation.main(["build", "--seed", "5", "--allow-short", "--no-render"])
    m = C.load_yaml(repo / "07-question-bank/simulations/SIM-01.yaml")
    bank = {q["id"]: q for q in C.load_mcqs()}
    answers = "".join(bank[q]["answer"] for q in m["mbe"]["am"] + m["mbe"]["pm"])
    ans_file = repo / "answers.txt"
    ans_file.write_text(answers)
    assert build_simulation.main(["score", "SIM-01", "--mbe-answers", str(ans_file)]) == 0
    rows = C.load_attempts()
    assert sum(r["correct"] == "Y" for r in rows if r["kind"] == "mcq") == 3
    assert rows[-1]["kind"] == "simulation" and rows[-1]["score"] == "3"


def test_anki_build(repo, capsys):
    out = repo / "exports/test.apkg"
    assert build_anki.main(["--subject", "EVD", "--include-rules", "--out", str(out)]) == 0
    assert out.exists() and zipfile.is_zipfile(out)
    n, _ = build_anki.build(["EVD"], {"must-know"}, False, repo / "exports/tag.apkg")
    assert n == 1
    n, _ = build_anki.build(["EVD"], set(), True, repo / "exports/all.apkg")
    assert n == 4  # 2 flashcards + 2 rule cards


def test_frequency_analysis(repo, capsys):
    assert frequency_analysis.main([]) == 0
    text = (repo / "06-past-exams/frequency-analysis.md").read_text()
    assert "<!-- BEGIN GENERATED-FREQUENCY -->" in text
    assert "| Evidence | 2 | 67% |" in text and "Contracts + Evidence" in text
    assert frequency_analysis.main([]) == 0  # idempotent: block replaced, not duplicated
    assert (repo / "06-past-exams/frequency-analysis.md").read_text().count("BEGIN GENERATED-FREQUENCY") == 1
    assert validate.run().errors == []


def test_dashboard(repo, capsys):
    quiz.main(["log", "--id", "Q-EVD-0001", "--answer", "B", "--seconds", "90"])
    quiz.main(["log", "--kind", "essay", "--item", "E-EVD-001", "--subject", "EVD", "--score", "60"])
    assert dashboard.main(["--date", "2026-12-01"]) == 0
    text = (repo / "10-progress/readiness-dashboard.md").read_text()
    assert "days to the exam" in text and "| Evidence | 1 | 100% |" in text
    readme = (repo / "README.md").read_text()
    assert "old" not in readme and "| Days to exam |" in readme
    assert validate.run().errors == []
