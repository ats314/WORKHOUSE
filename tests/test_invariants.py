"""Every registered invariant runs as its own test case."""

import pytest

from workhouse.invariants import SUITES

CASES = [(s.name, name, fn) for s in SUITES for name, _sec, fn in s.checks]


@pytest.mark.parametrize(("suite", "name", "fn"), CASES, ids=[f"{s}::{n}" for s, n, _ in CASES])
def test_invariant(suite, name, fn):
    passed, detail = fn()
    assert passed, f"[{suite}] {name}: {detail}"


def test_every_suite_has_checks():
    empty = [s.name for s in SUITES if not s.checks]
    assert not empty, f"suites with no checks: {empty}"
