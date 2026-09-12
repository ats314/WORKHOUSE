"""The single-face planar grading law: the decomposition is exact, the law is exact."""

import pytest
import sympy as sp

from workhouse import sixth_order_characters as CH
from workhouse.invariants import planar_grading as PG


@pytest.fixture(scope="module")
def series():
    return CH.bloch_series(8, CH.PLAQUETTE, sign=1)


def test_the_irrep_split_is_a_decomposition_not_an_estimate(series):
    for m in (2, 4, 6, 8):
        parts = PG.splitting_channels(series, m)
        assert sp.simplify(sum(parts.values()) - PG.splitting(series, m)) == 0


def test_every_channel_sits_two_orders_above_the_splitting(series):
    n = sp.Symbol("N")
    for m in (4, 6, 8):
        for value in PG.splitting_channels(series, m).values():
            # each channel is exactly N^-(m-1), not N^-(2m-1)
            assert sp.limit(value * n ** (m - 1), n, sp.oo) != 0
        assert sp.limit(PG.splitting(series, m) * n ** (m - 1), n, sp.oo) == 0


def test_the_channel_coefficients_cancel_exactly(series):
    n = sp.Symbol("N")
    for m in (4, 6, 8):
        leads = [
            sp.limit(v * n ** (m - 1), n, sp.oo) for v in PG.splitting_channels(series, m).values()
        ]
        assert sum(leads) == 0
        assert sorted(leads) == sorted(
            c * sp.Integer(2) ** (m // 2 - 2) for c in PG.CHANNEL_LAW.values()
        )


def test_the_tau_coefficients_are_exact_rationals():
    assert PG.tau_coefficient(2) == -1
    assert PG.tau_coefficient(4) == -2
    assert PG.tau_coefficient(6) == sp.Rational(-437, 48)
    assert PG.tau_coefficient(8) == sp.Rational(-30833, 576)
    assert PG.tau_coefficient(10) == sp.Rational(-3099613, 8640)


def test_the_planar_coefficients_match_the_series(series):
    n = sp.Symbol("N")
    for m in (2, 4, 6, 8):
        assert sp.limit(PG.splitting(series, m) * n ** (2 * m - 1), n, sp.oo) == PG.PLANAR[m]
