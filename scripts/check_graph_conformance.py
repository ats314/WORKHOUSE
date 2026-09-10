"""Score an agent's answers to the frozen theory-graph exercise.

``--prompt`` exposes the frozen inputs and questions, never the scoring key.
A score describes the submitted answers, not universal or future agent compliance.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests/fixtures/theory_graph_conformance.json"
ANSWER_SCHEMA = "workhouse-theory-graph/conformance-answer/v1"


def exercise(fixture: dict) -> dict:
    return {key: value for key, value in fixture.items() if key != "expected_answers"}


def fingerprint(fixture: dict) -> str:
    raw = json.dumps(exercise(fixture), sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def validate_answers(fixture: dict, submission: dict) -> list[str]:
    if not isinstance(submission, dict):
        return ["submission must be a JSON object"]
    errors = []
    if submission.get("schema") != ANSWER_SCHEMA:
        errors.append(f"schema must be {ANSWER_SCHEMA}")
    if submission.get("fixture_fingerprint") != fingerprint(fixture):
        errors.append("fixture_fingerprint does not match the frozen exercise")
    agent = submission.get("agent")
    if not isinstance(agent, dict) or not all(
        isinstance(agent.get(key), str) and agent[key].strip() for key in ("name", "model")
    ):
        errors.append("agent.name and agent.model must identify the actual responding agent")
    answers = submission.get("answers")
    if not isinstance(answers, dict):
        return errors + ["answers must be an object"]
    expected = fixture["expected_answers"]
    for key, value in expected.items():
        actual = answers.get(key)
        if type(actual) is not type(value) or actual != value:
            errors.append(f"incorrect or missing answer: {key}")
    for key in sorted(set(answers) - set(expected)):
        errors.append(f"unrecognized answer: {key}")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path, default=FIXTURE)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--prompt", action="store_true")
    modes.add_argument("--answers", type=Path)
    args = parser.parse_args(argv)
    try:
        fixture = json.loads(args.fixture.read_text(encoding="utf-8"))
        if args.prompt:
            print(
                json.dumps(
                    {
                        "instruction": "Use only this frozen exercise. Return one JSON object "
                        "with schema, fixture_fingerprint, agent {name, model}, and answers. "
                        "Use your actual identity; if the model version is unavailable say so. "
                        "Answer every named question with the type required by answer_schema. "
                        "Do not consult a scoring key or another agent's response.",
                        "schema": ANSWER_SCHEMA,
                        "fixture_fingerprint": fingerprint(fixture),
                        "exercise": exercise(fixture),
                    },
                    ensure_ascii=True,
                    indent=2,
                )
            )
            return 0
        submission = json.loads(args.answers.read_text(encoding="utf-8"))
        errors = validate_answers(fixture, submission)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors = [str(exc)]
        submission = {}
    print(
        json.dumps(
            {
                "passed": not errors,
                "agent": submission.get("agent") if isinstance(submission, dict) else None,
                "errors": errors,
                "scope": "This submitted response to this frozen exercise only.",
            },
            ensure_ascii=True,
            indent=2,
        )
    )
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
