"""Test harness: each test gets a fresh copy of the fixture repo (plus the real JSON Schemas)."""
from __future__ import annotations

import shutil
import sys
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).resolve().parents[1]
REPO = SCRIPTS.parent
sys.path.insert(0, str(SCRIPTS))


@pytest.fixture
def repo(tmp_path, monkeypatch) -> Path:
    dst = tmp_path / "repo"
    shutil.copytree(SCRIPTS / "tests" / "fixtures" / "repo", dst)
    shutil.copytree(REPO / "07-question-bank" / "schema", dst / "07-question-bank" / "schema")
    monkeypatch.setenv("CABAR_ROOT", str(dst))
    return dst
