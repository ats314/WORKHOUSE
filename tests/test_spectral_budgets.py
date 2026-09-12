"""Independent envelope optimization and invalid-premise adversaries."""

from itertools import combinations

import pytest
from sympy import Rational, symbols

from workhouse.invariants.moving_time_gap import power_budget
from workhouse.invariants.spectral_budgets import multichannel_budget


@pytest.mark.parametrize(
    "decays,errors,s,h",
    [
        ([], [(5, 0)], 1, 2),
        ([(1, 2)], [], 1, 2),
        ([(0, 2)], [(5, 0)], 0, 2),
        ([(1, 0)], [(5, 0)], 1, 2),
        ([(1, 2)], [(2, 0)], 1, 2),
        ([(1, 2)], [(5, -1)], 1, 2),
        ([(1, 2)], [(5, 0)], -1, 2),
        ([(1, 2)], [(5, 0)], 1, 0),
        ([(1, 2)], [(5, 0)], 0.5, 2),
        ([(1, 2)], [(5, 0)], 1, symbols("h")),
    ],
)
def test_invalid_hypotheses_are_not_silently_relaxed(decays, errors, s, h):
    with pytest.raises(ValueError):
        multichannel_budget(decays, errors, s, h)


def envelope_optimum(decays, errors, s, h):
    # Independently optimize the lower envelope of affine lines in x=1/c.
    # Include ALL line intersections, not the implementation's pair-rate formula.
    lines = [(Rational(m), -Rational(p + 2 * s)) for p, m in decays]
    lines += [(-Rational(ell), Rational(r - 2 * s)) for r, ell in errors]
    floor = 1 / Rational(h)
    candidates = [floor]
    for (b1, k1), (b2, k2) in combinations(lines, 2):
        if k1 != k2:
            x = (b2 - b1) / (k1 - k2)
            if x >= floor:
                candidates.append(x)
    return max(Rational(0), max(min(b + k * x for b, k in lines) for x in candidates))


@pytest.mark.parametrize("h", [Rational(1, 3), 2, 3, 11])
@pytest.mark.parametrize(
    "decays,errors,s",
    [
        ([(1, 2), (3, 4)], [(5, 0), (8, 1)], 1),
        ([(2, 3), (0, 1)], [(7, 0), (3, 1)], 1),
        ([(1, 2)], [(5, 3)], 1),
        ([(2, 3), (1, 5), (4, 2)], [(6, 0), (8, 1), (9, 2)], 0),
    ],
)
def test_agrees_with_independent_piecewise_linear_optimizer(decays, errors, s, h):
    result = multichannel_budget(decays, errors, s, h)
    assert result.rate == envelope_optimum(decays, errors, s, h)
    if result.rate > 0:
        c = result.time_coefficient
        assert 0 < c <= h
        assert all(c * (m - result.rate) - p - 2 * s >= 0 for p, m in decays)
        assert all(r - 2 * s - c * (result.rate + ell) >= 0 for r, ell in errors)


@pytest.mark.parametrize("h", [None, 2, 3, 10])
def test_reduces_to_original_one_plateau_budget(h):
    old = power_budget(1, 5, 1, 2, h)
    new = multichannel_budget([(1, 2)], [(5, 0)], 1, h)
    assert (new.rate, new.time_coefficient) == (old.rate, old.time_coefficient)


def test_time_amplification_cannot_be_dropped():
    assert multichannel_budget([(1, 2)], [(5, 0)], 1).rate == 1
    assert multichannel_budget([(1, 2)], [(5, 1)], 1).rate == Rational(1, 2)
    assert multichannel_budget([(1, 2)], [(5, 2)], 1).rate == 0


def test_order_and_duplicate_terms_do_not_change_exponential_rate():
    a = multichannel_budget([(1, 2), (3, 4)], [(5, 0), (8, 1)], 1)
    b = multichannel_budget([(3, 4), (1, 2), (3, 4)], [(8, 1), (5, 0)], 1)
    assert (a.rate, a.time_coefficient) == (b.rate, b.time_coefficient)
