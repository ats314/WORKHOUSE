"""Tests for the exact M10 reduction checks (W6 conditional score domination)."""

import pytest

from workhouse.invariants import w6_score_tail_m10 as m

CHECKS = [
    m.constrained_minimum_potential,
    m.synchronized_tangency_any_cutoff,
    m.potential_floor,
    m.exact_supremum,
    m.synthesis_constants,
    m.hardy_coefficients,
    m.soft_mode_divergence,
]


def test_suite_registration():
    assert m.score_tail.name == "W6 M10 reduction to three obligations"
    assert len(m.score_tail.checks) == len(CHECKS) == 7


@pytest.mark.parametrize("check", CHECKS, ids=[c.__name__ for c in CHECKS])
def test_check_passes(check):
    result = check()
    passed, detail = result[0], result[1]
    assert passed, detail


def test_yields_are_exact_symbolic():
    import sympy as sp

    for check in CHECKS:
        result = check()
        if len(result) == 3:
            for name, value in result[2].items():
                assert isinstance(value, sp.Basic) and value.free_symbols, name
                assert not name.endswith("_NUM")
