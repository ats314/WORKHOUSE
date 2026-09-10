"""Tests for theory graph protocol agent conformance checker."""

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import check_graph_conformance as C

FIXTURE_PATH = Path(__file__).resolve().parents[1] / "tests/fixtures/theory_graph_conformance.json"


@pytest.fixture
def fixture():
    return json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))


def test_conformance_exercise_omits_answers(fixture):
    ex = C.exercise(fixture)
    assert "expected_answers" not in ex
    assert "briefing" in ex
    assert "questions" in ex


def test_conformance_fingerprint_deterministic(fixture):
    fp1 = C.fingerprint(fixture)
    fp2 = C.fingerprint(fixture)
    assert fp1 == fp2
    assert len(fp1) == 64


def test_conformance_validation_passes_expected(fixture):
    submission = {
        "schema": C.ANSWER_SCHEMA,
        "fixture_fingerprint": C.fingerprint(fixture),
        "agent": {"name": "test-agent", "model": "test-model"},
        "answers": dict(fixture["expected_answers"]),
    }
    errors = C.validate_answers(fixture, submission)
    assert errors == []


def test_conformance_validation_detects_wrong_answers(fixture):
    submission = {
        "schema": C.ANSWER_SCHEMA,
        "fixture_fingerprint": C.fingerprint(fixture),
        "agent": {"name": "test-agent", "model": "test-model"},
        "answers": {**fixture["expected_answers"], "c2_status": "open"},
    }
    errors = C.validate_answers(fixture, submission)
    assert any("c2_status" in e for e in errors)
