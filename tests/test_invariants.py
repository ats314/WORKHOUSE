"""Every registered invariant runs as its own test case."""

import pytest

from workhouse.invariants import SUITES

CASES = [(s.name, name, tier, fn) for s in SUITES for name, _sec, tier, fn in s.checks]


@pytest.mark.parametrize(
    ("suite", "name", "tier", "fn"),
    CASES,
    ids=[f"{s}::{n}" for s, n, _t, _f in CASES],
)
def test_invariant(suite, name, tier, fn):
    passed, detail = fn()
    assert passed, f"[{suite}] T{tier} {name}: {detail}"


def test_every_suite_has_checks():
    empty = [s.name for s in SUITES if not s.checks]
    assert not empty, f"suites with no checks: {empty}"


def test_every_check_declares_a_tier_it_can_support():
    """T2 means the verdict rests on a float; T1 means it does not.

    Declared, not inferred -- but a T1 check that compares against a `*_NUM`
    constant or a stated tolerance is mislabelled, and that mislabelling is how
    a numerical agreement quietly starts being quoted as an exact one.
    """
    import inspect
    import re

    numeric = re.compile(r"_NUM\b|TOLERANCE|\d+e-\d+|isclose")
    wrong = []
    for suite in SUITES:
        for name, _sec, tier, fn in suite.checks:
            body = inspect.getsource(fn)
            if tier == 1 and numeric.search(body):
                wrong.append(f"{suite.name}::{name}")
    assert not wrong, f"checks resting on floats but declared T1: {wrong}"
