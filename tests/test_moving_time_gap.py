"""Adversarial domain and constrained-optimality checks for the exact budget."""

import pytest
from sympy import Rational, symbols

from workhouse.invariants.moving_time_gap import power_budget


@pytest.mark.parametrize("args", [(-1, 5, 1, 2), (1, 0, 1, 2), (1, 5, -1, 2), (1, 5, 1, 0)])
def test_rejects_invalid_power_law_hypotheses(args):
    with pytest.raises(ValueError):
        power_budget(*args)


@pytest.mark.parametrize("bad", [0.5, "0.5", symbols("unknown")])
def test_refuses_float_or_unresolved_inputs(bad):
    with pytest.raises(ValueError):
        power_budget(1, 5, bad, 2)


@pytest.mark.parametrize("bad", [0, -1, 0.5])
def test_refuses_invalid_or_inexact_physical_horizon(bad):
    with pytest.raises(ValueError):
        power_budget(1, 5, 1, 2, bad)


def test_no_margin_is_not_a_positive_gap():
    assert power_budget(1, 2, 1, 2).rate == 0
    assert power_budget(1, 1, 1, 2).rate == 0
    assert power_budget(1, 5, 1, 2, Rational(3, 2)).rate == 0
    assert power_budget(1, 5, 1, 2, Rational(7, 5)).rate == 0


def test_no_prefactor_growth_boundary_has_a_flat_optimum():
    for horizon in (Rational(1, 100), 1, 100):
        result = power_budget(0, 3, 0, 2, horizon)
        assert result.rate == 2
        assert result.time_coefficient <= horizon


def test_optimum_dominates_independent_rational_grid():
    for p, r, s, m, horizon in [
        (1, 5, 1, 2, 10),
        (1, 5, 1, 2, 2),
        (0, 7, 2, 3, 9),
        (2, 9, 1, Rational(1, 3), 30),
    ]:
        result = power_budget(p, r, s, m, horizon)
        for j in range(1, 201):
            c = Rational(j, 200) * horizon
            above = result.rate + Rational(1, 1000)
            assert c * (m - above) - p - 2 * s <= 0 or r - 2 * s - c * above <= 0
        below, c = result.rate / 2, result.time_coefficient
        assert c * (m - below) - p - 2 * s > 0
        assert r - 2 * s - c * below > 0
