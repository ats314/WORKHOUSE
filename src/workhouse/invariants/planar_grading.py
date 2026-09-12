"""The single-face planar grading law over Q(N): orders eight and ten, and the irrep channels.

ADR 0046 conjectured that the order-2k band coefficient is ``N^-(4k-1)`` while
its resolvent channels are ``N^-(2k-1)``, verified it at ``k = 1, 2`` on the
fourth-order cluster cumulants, and recorded that a per-channel label rule fails
on 47 of its 1,772 channel forms. ADR 0047 proved the odd orders are
determinant families. The G9 suite ("G9 direct sixth order on one face and the
shared-link pairs, any rank") then settled the one-face case at ``k = 3``
exactly over Q(N), including the ``N^-11`` order-six C-parity splitting, and
bounded the seven word-formula pieces of (F6) at ``O(N^-5)``.

This module continues that line on the same one-face object -- the C-parity
splitting of the one-plaquette diagonal,

    S_m(N) = odd_m - even_m = -2 K_m[0][1],

the off-diagonal Bloch element in the rank-generic character engine
``sixth_order_characters.bloch_series`` -- and adds three things, recorded in
``paper/research_notes/PLANAR_GRADING_SINGLE_FACE_20260911.md`` (ADR 0048):

1. **Orders eight and ten (k = 4, 5), exactly.** Nothing in the corpus had gone
   past order six on this object. The exponent is ``-(2m-1)`` and

       c_2 = -4, c_4 = -32, c_6 = -1748/3, c_8 = -123332/9, c_10 = -49593808/135.

2. **The tau-normalisation.** With ``u = N^2 tau/2`` the order-``m`` term is
   ``(c_m/2^m) N tau^m``: every even order carries the same single power of N,
   so the single-face band per unit N is a function of ``tau`` alone, with
   ``b_2 = -1`` and ``b_4 = -2`` exactly.

3. **Where the cancellation lives.** Splitting ``S_m`` by the intermediate state
   gives exactly four channels at every even ``m >= 4`` -- the singlet, the
   adjoint, and the two two-box states -- **each of order ``N^-(m-1)``**, with
   leading coefficients ``(-4, +2, +1, +1)`` times ``2^(m/2-2)``, summing to
   zero. The cancellation is between channels of EQUAL order, carried entirely
   by their relative coefficients, which is why no per-channel label rule can
   reproduce it. This is a different decomposition from the word-formula pieces
   of (F6) that the G9 suite bounds.

Scope, kept explicit: this is the one-plaquette diagonal, not the cluster
cumulant ``beta_N``. ADR 0046's cluster conjecture is not discharged here, and
G16's overlap theorem is untouched. Each order is an exact computation at that
order; the general-``m`` law remains a conjecture, now verified at k = 1..5 on
this channel.
"""

from __future__ import annotations

import json

import sympy as sp

from .. import sixth_order_characters as CH
from . import odd_order as OO
from ._core import ROOT, _suite

grading = _suite("the single-face planar grading law through tenth order (G16)")

_RUN = "runs/planar_grading_2026-09-11"
_CITE = "G16; G14; G9; " + _RUN + "; ADR 0048; ADR 0046; ADR 0047; the G9 one-face suite"
_N = sp.Symbol("N")

#: Orders re-derived live over Q(N); order 10 is read from the run (its series costs a minute).
LIVE_ORDERS = (2, 4, 6, 8)
PINNED_ORDER = 10

#: ``c_m``: the planar coefficient of ``N^(2m-1) S_m``, exactly.
PLANAR = {
    2: sp.Integer(-4),
    4: sp.Integer(-32),
    6: sp.Rational(-1748, 3),
    8: sp.Rational(-123332, 9),
    10: sp.Rational(-49593808, 135),
}

#: The four irrep channels of the splitting and their leading coefficients in units of
#: ``2^(m/2-2)``: the singlet carries twice the adjoint, the adjoint twice each two-box state.
CHANNEL_LAW = {
    "((), ())": sp.Integer(-4),
    "((1,), (1,))": sp.Integer(2),
    "((2,), ())": sp.Integer(1),
    "((1, 1), ())": sp.Integer(1),
}

#: The integer-rank cross-check is an extrapolation, so it is compared within this tolerance.
CROSS_CHECK_TOLERANCE = 1e-4


def _certificate() -> dict:
    return json.loads((ROOT / _RUN / "certificate.json").read_text(encoding="utf-8"))


def _rf(x):
    """A ``symbolic_rank`` rational function as a cancelled sympy expression."""
    return sp.cancel(x.to_sympy()) if hasattr(x, "to_sympy") else sp.cancel(x)


def _v(vec):
    """``V = chi_F + chi_F-bar`` on a character vector, as ``bloch_series`` applies it."""
    out = CH.multiply_fundamental(vec, False)
    for key, value in CH.multiply_fundamental(vec, True).items():
        out[key] = out.get(key, 0) + value
    return {key: value for key, value in out.items() if value}


def splitting(series, m):
    """``S_m(N) = odd_m - even_m`` as an exact rational function of N."""
    return sp.cancel(_rf(series["odd"][m]) - _rf(series["even"][m]))


def splitting_channels(series, m) -> dict:
    """``S_m`` split by the intermediate state, exactly over Q(N).

    ``S_m = -2 K_m[0][1]``, and ``K_m[0][1]`` is the coefficient of the first
    face word in ``V`` applied to the order-(m-1) perturbed vector of the
    second, so each intermediate state contributes one term. The checks below
    verify that the parts sum to ``S_m``, which makes this a decomposition
    rather than an estimate.
    """
    model, chi = series["model"], series["chi"]
    out = {}
    for state, coefficient in chi[m - 1][1].items():
        amplitude = _v({state: coefficient / coefficient}).get(model[0])
        if amplitude is None:
            continue
        out[state] = sp.cancel(-2 * _rf(coefficient) * _rf(amplitude))
    return {k: v for k, v in out.items() if v != 0}


def tau_coefficient(m: int):
    """``b_m = c_m / 2^m``: the coefficient of ``tau^m`` in ``S(u)/N``, with ``u = N^2 tau/2``."""
    return sp.nsimplify(PLANAR[m] / sp.Integer(2) ** m)


def _leading(expr, power):
    return sp.nsimplify(sp.limit(expr * _N**power, _N, sp.oo))


# ---------------------------------------------------------------- checks
_LAW = (
    "one face over Q(N): the C-parity splitting at even order m is exactly c_m N^-(2m-1) for "
    "m = 2, 4, 6, 8 with c_m = -4, -32, -1748/3, -123332/9 -- the ADR 0046 law at k = 4, past "
    "the k = 3 the G9 one-face suite already settled"
)


@grading.check(_LAW, _CITE)
def _():
    series = CH.bloch_series(max(LIVE_ORDERS), CH.PLAQUETTE, sign=1)
    ok, detail = True, []
    for m in LIVE_ORDERS:
        s = splitting(series, m)
        lead = _leading(s, 2 * m - 1)
        ok = ok and lead == PLANAR[m] and lead != 0
        # the exponent is exactly 2m - 1: one power lower still diverges
        ok = ok and sp.limit(sp.Abs(s) * _N ** (2 * m), _N, sp.oo) is sp.oo
        detail.append(f"m = {m}: N^{2 * m - 1} S_m -> {lead}")
    cert = _certificate()["planar_coefficients"]
    ok = ok and sp.Rational(cert[str(PINNED_ORDER)]) == PLANAR[PINNED_ORDER]
    return (
        ok,
        (
            "; ".join(detail)
            + f"; order {PINNED_ORDER} pinned from the run at c_10 = {PLANAR[10]}, exponent -19. "
            "Exact rational functions of N from the rank-generic Bloch series. The object is the "
            "one-plaquette diagonal, not the cluster cumulant beta_N"
        ),
        {
            "SINGLE_FACE_PLANAR_C6": PLANAR[6],
            "SINGLE_FACE_PLANAR_C8": PLANAR[8],
            "SINGLE_FACE_PLANAR_C10": PLANAR[10],
        },
    )


_TAU = (
    "the tau-normalisation: with u = N^2 tau/2 every even order of the single-face band carries "
    "the same single power of N, so S(u)/N is a function of tau alone with b_2 = -1, b_4 = -2"
)


@grading.check(_TAU, _CITE, rests_on=(_LAW,))
def _():
    ok = tau_coefficient(2) == -1 and tau_coefficient(4) == -2
    ok = ok and tau_coefficient(6) == sp.Rational(-437, 48)
    ok = ok and tau_coefficient(8) == sp.Rational(-30833, 576)
    ok = ok and tau_coefficient(10) == sp.Rational(-3099613, 8640)
    # the N-power bookkeeping itself: S_m u^m = (c_m/2^m) N tau^m
    tau, n = sp.symbols("tau N", positive=True)
    for m in PLANAR:
        term = (PLANAR[m] * n ** (-(2 * m - 1))) * (n**2 * tau / 2) ** m
        ok = ok and sp.simplify(term - tau_coefficient(m) * n * tau**m) == 0
    return (
        ok,
        (
            "b_m = c_m/2^m = -1, -2, -437/48, -30833/576, -3099613/8640 at m = 2, 4, 6, 8, 10; "
            "substituting u = N^2 tau/2 into c_m N^-(2m-1) u^m gives b_m N tau^m at every one of "
            "them, so the single-face band per unit N is a rank-independent function of tau"
        ),
        {"SINGLE_FACE_TAU_B6": tau_coefficient(6), "SINGLE_FACE_TAU_B8": tau_coefficient(8)},
    )


_CHANNELS = (
    "the cancellation is between channels of EQUAL order: splitting S_m by the intermediate "
    "state gives exactly four channels at every even m >= 4, each O(N^-(m-1)), with leading "
    "coefficients (-4, +2, +1, +1) x 2^(m/2-2) summing to zero"
)


@grading.check(_CHANNELS, _CITE, rests_on=(_LAW,))
def _():
    series = CH.bloch_series(max(LIVE_ORDERS), CH.PLAQUETTE, sign=1)
    ok, detail = True, []
    for m in LIVE_ORDERS:
        parts = splitting_channels(series, m)
        # a decomposition, not an estimate
        ok = ok and sp.simplify(sum(parts.values()) - splitting(series, m)) == 0
        scale = sp.Integer(2) ** (m // 2 - 2)
        leads = {str(state): _leading(value, m - 1) for state, value in parts.items()}
        if m == 2:
            # the degenerate order: only the singlet and the adjoint exist
            ok = ok and leads == {"((), ())": sp.Integer(-2), "((1,), (1,))": sp.Integer(2)}
        else:
            ok = ok and set(leads) == set(CHANNEL_LAW)
            ok = ok and all(leads[k] == CHANNEL_LAW[k] * scale for k in CHANNEL_LAW)
        ok = ok and sum(leads.values()) == 0
        detail.append(f"m = {m}: " + ", ".join(f"{k} {v}" for k, v in sorted(leads.items())))
    return ok, (
        "; ".join(detail)
        + ". Every channel is O(N^-(m-1)) -- ADR 0046's channel content -- and the suppression to "
        "N^-(2m-1) is carried entirely by the relative coefficients, so no rule assigning an order "
        "per channel can reproduce it (ADR 0046's 47 failing forms). This is a different "
        "decomposition from the word-formula pieces of (F6) that the G9 suite bounds"
    )


_CROSS = (
    "an independent integer-rank engine agrees: the one-plaquette character engine of ADR 0047 "
    "at N = 60..200, extrapolated in 1/N^2, reproduces c_2, c_4, c_6, c_8"
)


@grading.check(_CROSS, _CITE, tier=2, rests_on=(_LAW,))
def _():
    cert = _certificate()["integer_rank_cross_check"]
    ok, detail = True, []
    for m in (2, 4, 6, 8):
        row = cert[str(m)]
        ok = ok and sp.Rational(row["exact"]) == PLANAR[m]
        ok = ok and row["relative_gap"] < CROSS_CHECK_TOLERANCE
        detail.append(
            f"m = {m}: {row['extrapolated']:.6f} vs {float(PLANAR[m]):.6f} "
            f"(rel {row['relative_gap']:.1e})"
        )
    # live, cheaply, at the two orders the odd-order engine is fastest on
    for m in (2, 4):
        n = 120
        row = OO.towers(n, m)
        scaled = (row[f"tower{m}_odd"] - row[f"tower{m}_even"]) * sp.Integer(n) ** (2 * m - 1)
        ok = ok and abs(scaled / PLANAR[m] - 1) < sp.Rational(1, 100)
    return ok, (
        "; ".join(detail)
        + f". Agreement within {CROSS_CHECK_TOLERANCE:.0e} relative, degrading with order as the "
        "extrapolation does. The ADR 0047 engine shares no primitive with the rank-generic Bloch "
        "series -- it works at integer rank with Fraction arithmetic and reaches the limit only by "
        "extrapolation -- so this is an independent confirmation of the exact coefficients. T2: "
        "the comparison is a tolerance on an extrapolated value, not an exact identity"
    )
