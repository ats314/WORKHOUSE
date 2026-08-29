from __future__ import annotations

from sympy import (
    Rational,
    expand,
)

from ._core import _suite
from ._shared import _bridge_towers

# ---------------------------------------------------------------------------
# Coupling erratum (C4/G2). The archived Y = 2*beta/3 = 4u line was a label
# error; the printed coefficients were already canonical-u. G2 asked for "a
# single conversion statement" — here it is as arithmetic: the printed tower
# coefficients written as functions of beta/4 reproduce the printed u-towers
# under u = beta/6 exactly, and would be off by 4^r under the Y reading.

coupling = _suite("coupling erratum (C4/G2)")


@coupling.check(
    "the printed towers are canonical-u: 4*Delta(3u/2) reproduces them verbatim",
    "UNIFIED §2.1 / C4",
)
def _():
    u, bridge_minus, bridge_plus = _bridge_towers()
    tower_minus = expand(Rational(8, 3) + u + u**2 / 2 + Rational(7, 32) * u**3)
    tower_plus = expand(Rational(8, 3) - u + Rational(13, 20) * u**2 + Rational(101, 200) * u**3)
    ok = bridge_minus == tower_minus and bridge_plus == tower_plus
    return ok, (
        "with b2- = 1/18, b3- = 7/432, b2+ = 13/180, b3+ = 101/2700 as printed, "
        "4*Delta_-(3u/2) = 8/3 + u + u^2/2 + 7/32 u^3 and 4*Delta_+(3u/2) = "
        "8/3 - u + 13/20 u^2 + 101/200 u^3 exactly — both sides printed tables, "
        "consistent only in u = beta/6"
    )


@coupling.check(
    "the 4**r rescaling breaks the bridge: order 2 off by 16, order 3 by 64",
    "UNIFIED §2.1 / C4 / G2",
)
def _():
    u, bridge_minus, _bridge_plus = _bridge_towers()
    rescaled = expand(Rational(8, 3) + u / 4 + u**2 / 32 + Rational(7, 2048) * u**3)
    ratio2 = bridge_minus.coeff(u, 2) / rescaled.coeff(u, 2)
    ratio3 = bridge_minus.coeff(u, 3) / rescaled.coeff(u, 3)
    ok = bridge_minus != rescaled and ratio2 == 16 and ratio3 == 64
    return ok, (
        f"reading the archived Y = 4u line as a coordinate would demand coefficient_r/4^r; "
        f"the printed table differs from that by exactly {ratio2} at u^2 and {ratio3} at u^3 "
        "— the single conversion statement G2 asked for, as arithmetic"
    )
