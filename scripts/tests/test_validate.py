"""Validator: the fixture repo is clean, and each class of defect is caught."""
from __future__ import annotations

import validate


def errors(**kw) -> list[str]:
    return validate.run(**kw).errors


def test_fixture_repo_is_valid(repo):
    assert errors() == []


def test_mcq_missing_wrong_option_explanation(repo):
    f = repo / "07-question-bank/mcq/contracts/Q-CTR-0001.yaml"
    f.write_text(f.read_text().replace('D: "FIXTURE why D is wrong."', ""))
    assert any("explanation_each_wrong_option must cover exactly" in e for e in errors())


def test_mcq_explaining_correct_answer_is_flagged(repo):
    f = repo / "07-question-bank/mcq/contracts/Q-CTR-0001.yaml"
    f.write_text(f.read_text().replace("{B:", '{A: "FIXTURE explains the key itself.", B:'))
    assert any("must not explain the correct answer" in e for e in errors())


def test_mcq_unknown_rule_and_coverage(repo):
    f = repo / "07-question-bank/mcq/contracts/Q-CTR-0001.yaml"
    f.write_text(f.read_text().replace("R-CTR-001", "R-CTR-999").replace("CTR-MBE-I.A]", "CTR-MBE-IX]"))
    errs = errors()
    assert any("rule_id R-CTR-999" in e for e in errs)
    assert any("coverage_id CTR-MBE-IX" in e for e in errs)


def test_duplicate_mcq_id(repo):
    f = repo / "07-question-bank/mcq/evidence/fixture-hearsay.yaml"
    f.write_text(f.read_text().replace("Q-EVD-0002", "Q-EVD-0001"))
    assert any("duplicate MCQ id" in e for e in errors())


def test_essay_points_must_sum_to_100(repo):
    f = repo / "07-question-bank/essays/evidence/E-EVD-001.md"
    f.write_text(f.read_text().replace("points: 40", "points: 30"))
    assert any("must sum to 100" in e for e in errors())


def test_essay_missing_section(repo):
    f = repo / "07-question-bank/essays/evidence/E-EVD-001.md"
    f.write_text(f.read_text().replace("## Self-Grading Rubric", "## Rubric"))
    assert any("missing sections" in e for e in errors())


def test_duplicate_rule_id(repo):
    f = repo / "03-subjects/evidence/rule-statements.md"
    f.write_text(f.read_text().replace("R-EVD-002", "R-EVD-001"))
    assert any("duplicate rule ID R-EVD-001" in e for e in errors())


def test_unmapped_matrix_row(repo):
    f = repo / "00-exam-intel/coverage-matrix.csv"
    f.write_text(f.read_text().replace("03-subjects/contracts/outline.md,I Formation", ",I Formation"))
    assert any("UNMAPPED row CTR-MBE-I" in e for e in errors())


def test_mapped_row_heading_must_exist(repo):
    f = repo / "03-subjects/evidence/outline.md"
    f.write_text(f.read_text().replace("### V.F Business records", "### V.F Records"))
    assert any("heading 'V.F Business records' not found" in e for e in errors())


def test_strict_mode_requires_planned_targets(repo):
    assert errors() == []
    assert any("maps to missing file 03-subjects/contracts/outline.md" in e for e in errors(strict=True))


def test_citation_verify_and_link_checks(repo):
    f = repo / "03-subjects/evidence/outline.md"
    f.write_text(f.read_text() + "\nBad [S-999] and [VERIFY] and [VERIFY V-123] and [x](missing.md)\n")
    errs = errors()
    assert any("citation [S-999]" in e for e in errs)
    assert any("bare [VERIFY]" in e for e in errs)
    assert any("[VERIFY V-123] not logged" in e for e in errs)
    assert any("broken link -> missing.md" in e for e in errs)


def test_front_matter_schema(repo):
    f = repo / "03-subjects/evidence/outline.md"
    f.write_text(f.read_text().replace("status: draft", "status: final"))
    assert any("front matter status" in e for e in errors())


def test_flashcard_rule_must_exist(repo):
    f = repo / "03-subjects/evidence/flashcards.csv"
    f.write_text(f.read_text().replace("R-EVD-001", "R-EVD-404"))
    assert any("rule_id R-EVD-404 not found" in e for e in errors())
