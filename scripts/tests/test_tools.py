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
    (repo / "exports/SIM-01/answer-key.md").unlink()
    assert build_simulation.main(["render", "SIM-01"]) == 0
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


def test_build_weeks(repo, capsys):
    import build_weeks
    (repo / "01-study-plan").mkdir(exist_ok=True)
    (repo / "01-study-plan/schedule.yml").write_text(
        "weeks:\n"
        "- {week: 2027-W16, phase: integration, hours: 18, theme: Fixture A, learn: [x], mbe: {n: 60, mix: {EVD: 30, MIX: 30}},"
        " essays: {n: 2, subjects: [EVD, CTR], mode: timed}, spot: 2, pt: {n: 1, mode: timed}, checkpoint: CP9}\n"
        "- {week: 2027-W17, phase: intensive, hours: 40, theme: Fixture B, learn: [y], mbe: {n: 200, mix: {MIX: 200}},"
        " essays: {n: 5, subjects: [MIX], mode: simulation}, spot: 0, pt: {n: 1, mode: simulation},"
        " sim: {id: SIM-01, days: [Tue, Wed]}, overrides: {Tue: 'SIM day 1', Wed: 'SIM day 2'}}\n")
    (repo / "01-study-plan/master-plan.md").write_text(
        "---\nsubject: study-plan\ntopic: Fixture master\ncoverage_ids: []\ntested_on: [none]\n"
        "exam_frequency: {level: n/a, basis: fixture}\nlast_verified: 2026-11-04\nstatus: draft\n---\n"
        "# M\n<!-- BEGIN WEEK-TABLE -->\nx\n<!-- END WEEK-TABLE -->\n")
    assert build_weeks.main(["--force"]) == 0
    a = (repo / "01-study-plan/weeks/2027-W16.md").read_text()
    b = (repo / "01-study-plan/weeks/2027-W17.md").read_text()
    assert "Week 2027-W16 · Mon Apr 19" in a and "`/quiz evidence 30`" in a and "**CP9**" in a
    assert "200 inside SIM-01 (`/simulate`)" in b and "**SIM day 1**" in b and "/quiz mixed" not in b
    assert "Cumulative after this week | 58 h · 260 MBE · 7 essays · 2 PTs" in b
    master = (repo / "01-study-plan/master-plan.md").read_text()
    assert "[2027-W17](weeks/2027-W17.md)" in master and "**Totals:** 58 hours" in master
    before = b
    (repo / "01-study-plan/weeks/2027-W17.md").write_text(before + "\nhand edit\n")
    assert build_weeks.main([]) == 0  # no --force: existing files untouched
    assert "hand edit" in (repo / "01-study-plan/weeks/2027-W17.md").read_text()
    assert build_weeks.main(["--from", "2027-W17"]) == 0
    assert "hand edit" not in (repo / "01-study-plan/weeks/2027-W17.md").read_text()
    assert validate.run().errors == []


def test_merge_build_outputs(repo, tmp_path, capsys):
    import merge_build_outputs as M
    m = tmp_path / "map.csv"
    m.write_text("coverage_id,target_file,target_heading\n"
                 "CTR-MBE-I.A,03-subjects/evidence/outline.md,FRE vs CEC\n"
                 "CTR-MBE-I,03-subjects/evidence/outline.md,No such heading\n"
                 "XXX-MBE-I,03-subjects/evidence/outline.md,V Hearsay\n")
    s = tmp_path / "s.md"
    s.write_text("| S-005 | New source | Pub | https://example.org/new | 2026-11-04 | search | x |\n"
                 "| S-001 | Dup | Pub | https://example.org/d | 2026-11-04 | search | x |\n")
    v = tmp_path / "v.md"
    v.write_text("| V-009 | x | later | y | z | Low | 2026-11-04 |\n| V-003 | x | earlier | y | z | Low | 2026-11-04 |\n")
    rc = M.main(["--mapping", str(m), "--sources", str(s), "--verify", str(v)])
    assert rc == 1  # one missing heading, one unknown id, one duplicate source
    rows = {r["coverage_id"]: r for r in C.load_matrix()}
    assert rows["CTR-MBE-I.A"]["mapping_status"] == "mapped" and rows["CTR-MBE-I"]["mapping_status"] == "planned"
    src = (repo / "00-exam-intel/sources.md").read_text()
    assert "| S-005 | New source" in src and src.count("| S-001 |") == 1
    q = (repo / "VERIFY-QUEUE.md").read_text()
    assert q.index("| V-001 |") < q.index("| V-003 |") < q.index("| V-009 |")


def test_simulation_items_reserved_until_sat(repo, capsys):
    build_simulation.main(["build", "--seed", "5", "--allow-short", "--no-render"])
    m = C.load_yaml(repo / "07-question-bank/simulations/SIM-01.yaml")
    sim_mcqs = set(m["mbe"]["am"] + m["mbe"]["pm"])
    assert sim_mcqs and sim_mcqs <= C.reserved_sim_items()
    assert not sim_mcqs & {q["id"] for q in quiz.pick("MIX", 50, seed=1)}
    assert quiz.main(["reserved"]) == 0 and "PT-001" in capsys.readouterr().out
    quiz.log_attempt(kind="simulation", item_id="SIM-01", subject="MIX", score=0, max_score=1, source="repo")
    assert C.reserved_sim_items() == set()
    assert sim_mcqs & {q["id"] for q in quiz.pick("MIX", 50, seed=1)}
