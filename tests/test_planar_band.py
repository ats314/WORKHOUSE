"""Exact large-N expansion helpers of the planar-band suite, and the census on one cluster."""

import json
from fractions import Fraction

from sympy import Symbol

from workhouse.invariants import planar_band as PB
from workhouse.invariants._core import ROOT

N = Symbol("N")


def test_inv_expansion_matches_a_known_series():
    # t_N = 1/(4N^3) - 1/(16N^5) - 77/(64N^7) - 1021/(256N^9) (constants.HOPPING_LARGE_N)
    power, q = PB.inv_expansion(
        2 * N * (N**2 - 4) / ((N**2 - 1) * (2 * N**2 - 1) * (4 * N**2 - 9)), 7
    )
    assert power == -3
    assert (
        q[0] == Fraction(1, 4)
        and q[2] == Fraction(-1, 16)
        and q[4] == Fraction(-77, 64)
        and q[6] == Fraction(-1021, 256)
    )
    assert q[1] == q[3] == q[5] == 0


def test_inv_expansion_rf_agrees_with_the_sympy_route():
    forms = json.loads((ROOT / PB._FORMS_RUN / "closed_forms.json").read_text(encoding="utf-8"))[
        "forms"
    ]
    for name in ("u_odd", "corner_even", "beta_assembled"):
        a = PB.inv_expansion(PB.rf(forms[name]["factored"]), 5)
        b = PB.inv_expansion_rf(PB._rf(forms[name]), 5)
        assert a == b


def test_channel_census_on_the_two_hop_chain():
    clusters = json.loads(
        (ROOT / PB._CHANNEL_RUN / "certificate.json").read_text(encoding="utf-8")
    )["clusters"]
    row = PB.channel_census(clusters["u_coplanar"], "odd")
    assert row["identity"] and row["channels"] == 74
    assert row["max_channel_power"] == -3 and row["cumulant_power"] == -7
    assert (
        row["totals"][-3] == 0 and row["totals"][-5] == 0 and row["totals"][-7] == Fraction(11, 576)
    )
