"""The Wilson transfer matrix at finite temporal step (G19; runs/uniform_wilson_window_2026-09-04).

A parallel session (GPT, 2026-09-04) derived, for the symmetric Wilson transfer family
T = exp(tau u V/2) exp(-tau K_eps) exp(tau u V/2) with the clock calibrated on the
fundamental character, the complete second-order C-odd shell at finite temporal step:
the reduced-resolvent weight is d_tau(Delta) = (tau/2) coth(tau Delta/2) rather than
1/Delta, the shell is again t_W times the signed incidence adjacency, and with the exact
SU(3) multipliers lambda_R(eps) the hopping is t_W = 5/612 + 175/280908 eps^2 + O(eps^3).
This module re-derives the exact part of that package from its stated definitions: the
four shared-link channel weights reproduce t_N at every rank at eps -> 0; the SU(3)
multipliers through eps^3 from Cartan Gaussian moments with the Weyl Vandermonde, against
the pinned certificate; and the finite-step hopping, flat scalar and first literal-source
Gram coefficient. The analytic theorems of the note (the uniform kinetic window, the
fixed-order weighted matching) are research-note proofs and are not checked here.
"""

from __future__ import annotations

import json
from functools import cache, lru_cache

from sympy import (
    I,
    Poly,
    Rational,
    S,
    Symbol,
    coth,
    expand,
    factor,
    factorial,
    log,
    series,
    simplify,
)

from ._core import ROOT, _suite

wilson = _suite("the Wilson transfer matrix at finite temporal step")

_RUN = "runs/uniform_wilson_window_2026-09-04"
_NOTE = "paper/research_notes/G19_UNIFORM_WILSON_WINDOW_20260904.md"
_CITE = "G19; " + _NOTE + " sections 5-7; " + _RUN
_N = Symbol("N", positive=True)
_EPS = Symbol("eps")


@cache
def _laplace_certificate() -> dict:
    return json.loads((ROOT / _RUN / "exact_laplace_certificate.json").read_text(encoding="utf-8"))


@cache
def _shell_certificate() -> dict:
    return json.loads((ROOT / _RUN / "window_shell_certificate.json").read_text(encoding="utf-8"))


def _channel_weights(n, d_of_gap):
    """The four channel weights w_rho = -(d_rho/N^2) d(C_F + C_rho/2) of the second-order
    C-odd shell on a shared link, rho the irrep the shared link carries in the intermediate
    state, d the reduced-resolvent weight as a function of the gap."""
    cf = (n**2 - 1) / (2 * n)
    irreps = {
        "1": (S.One, S.Zero),
        "adj": (n**2 - 1, n),
        "lam2": (n * (n - 1) / 2, (n - 2) * (n + 1) / n),
        "sym2": (n * (n + 1) / 2, (n + 2) * (n - 1) / n),
    }
    return {k: -(d / n**2) * d_of_gap(cf + c / 2) for k, (d, c) in irreps.items()}


_CHANNELS_TN = (
    "the four shared-link channels of the second-order C-odd shell reproduce t_N at every rank: "
    "w_rho = -(d_rho/N^2)/(C_F + C_rho/2) for rho = 1, Adj, Lambda^2 F, Sym^2 F, and "
    "(w_Lambda2 + w_Sym2) - (w_1 + w_Adj) = 2N(N^2-4)/((N^2-1)(2N^2-1)(4N^2-9)) identically"
)


@wilson.check(
    _CHANNELS_TN,
    _CITE + " eq. (12) at eps -> 0; corpus section 4.1",
    rests_on=(
        "the third engine reproduces the all-rank second-order hopping t_N and C-even hopping "
        "ell_N, and leak = hop in both sectors, at N = 3..7 live and N = 3..70 pinned",
    ),
)
def _():
    # The Hamiltonian limit of the note's channel formula: the intermediate state has the
    # six private fundamental links plus the shared link in rho, against the four of the
    # external shell, so the gap is C_F + C_rho/2 and the weight is its inverse. The
    # Lambda^2 and Sym^2 channels are the C-odd exchange, the singlet and adjoint the direct
    # route; their difference is the all-rank hopping the corpus derives otherwise.
    w = _channel_weights(_N, lambda gap: 1 / gap)
    t_n = 2 * _N * (_N**2 - 4) / ((_N**2 - 1) * (2 * _N**2 - 1) * (4 * _N**2 - 9))
    diff = simplify((w["lam2"] + w["sym2"]) - (w["1"] + w["adj"]) - t_n)
    at3 = {k: v.subs(_N, 3) for k, v in w.items()}
    ok = diff == 0 and (at3["lam2"] + at3["sym2"]) - (at3["1"] + at3["adj"]) == Rational(5, 612)
    return ok, (
        "cancel((w_lam2 + w_sym2) - (w_1 + w_adj) - t_N) = "
        + str(diff)
        + "; at N = 3 the weights are "
        + ", ".join(f"w_{k} = {at3[k]}" for k in ("1", "adj", "lam2", "sym2"))
        + ", difference 5/612 = t_3"
    )


def _su3_multipliers() -> dict:
    """lambda_R(eps) through eps^3 for R = 3, 8, 6, from the Laplace expansion of the Wilson
    density exp[-2(3 - Re Tr U)/eps] in Cartan coordinates: Gaussian moments of the
    Vandermonde-weighted rank-two Gaussian with covariance [[1/3, -1/6], [-1/6, 1/3]], the
    Weyl density corrections D1, D2 and the character expansions -- a port of the run's
    exact_su3_laplace.py, kept independent of it."""
    a, b = Symbol("a", real=True), Symbol("b", real=True)
    x = (a, b, -a - b)
    delta = (a - b, 2 * a + b, a + 2 * b)
    vandermonde = delta[0] ** 2 * delta[1] ** 2 * delta[2] ** 2

    @lru_cache(None)
    def moment(i: int, j: int):
        if i < 0 or j < 0:
            return S.Zero
        if i + j == 0:
            return S.One
        if (i + j) % 2:
            return S.Zero
        if i:
            return (i - 1) * Rational(1, 3) * moment(i - 2, j) - j * Rational(1, 6) * moment(
                i - 1, j - 1
            )
        return (j - 1) * Rational(1, 3) * moment(0, j - 2)

    def gaussian(poly):
        return expand(sum(c * moment(i, j) for (i, j), c in Poly(expand(poly), a, b).terms()))

    norm = gaussian(vandermonde)

    def mean(poly):
        return factor(gaussian(vandermonde * poly) / norm)

    a4 = sum(y**4 for y in x) / 12
    a6 = -sum(y**6 for y in x) / 360
    j1 = -sum(y * y for y in delta) / 12
    j2 = (
        sum(y**4 for y in delta) / 360
        + sum(delta[i] ** 2 * delta[j] ** 2 for i in range(3) for j in range(i + 1, 3)) / 144
    )
    d1 = expand(a4 + j1)
    d2 = expand(a6 + a4 * a4 / 2 + j2 + a4 * j1)

    def series_mul(p, q):
        return {
            k: expand(sum(p.get(i, 0) * q.get(k - i, 0) for i in range(k + 1))) for k in range(7)
        }

    f = {j: expand(I**j * sum(y**j for y in x) / factorial(j)) for j in range(7)}
    fb = {j: (-1) ** j * v for j, v in f.items()}
    prod = series_mul(f, fb)
    ff = series_mul(f, f)
    chars = {
        "F": (f, 3),
        "Adj": ({j: prod[j] - (1 if j == 0 else 0) for j in range(7)}, 8),
        "Sym2": ({j: ff[j] - fb[j] for j in range(7)}, 6),
    }
    out = {}
    m1, m2 = mean(d1), mean(d2)
    for name, (char, dim) in chars.items():
        c = [expand(char[2 * j] / dim) for j in range(4)]
        n1 = mean(c[1])
        n2 = mean(c[2] + c[1] * d1)
        n3 = mean(c[3] + c[2] * d1 + c[1] * d2)
        lam = [S.One, n1, factor(n2 - m1 * n1), factor(n3 - m1 * n2 + (m1 * m1 - m2) * n1)]
        out[name] = lam
    out["_norm"], out["_means"] = norm, (m1, m2)
    return out


_MULTIPLIERS = (
    "the exact SU(3) Wilson multipliers through eps^3 from Cartan Gaussian moments with the Weyl "
    "Vandermonde: lambda_3 = 1 - 2/3 eps + 1/36 eps^2 + 13/648 eps^3, lambda_8 = 1 - 3/2 eps + "
    "11/16 eps^2 + 1/96 eps^3, lambda_6 = 1 - 5/3 eps + 65/72 eps^2 - 55/1296 eps^3; the "
    "calibrated clock is tau = eps + 7/24 eps^2 + 13/144 eps^3 and the calibrated energies "
    "k(8) = 3/2 - 5/96 eps^2, k(6) = 5/3 - 5/72 eps^2"
)


@wilson.check(_MULTIPLIERS, _CITE + " section 6; exact_laplace_certificate.json")
def _():
    # Live: the port above. Pinned: the package's own certificate, string for string.
    m = _su3_multipliers()
    cert = _laplace_certificate()
    expected = {
        "F": [S.One, Rational(-2, 3), Rational(1, 36), Rational(13, 648)],
        "Adj": [S.One, Rational(-3, 2), Rational(11, 16), Rational(1, 96)],
        "Sym2": [S.One, Rational(-5, 3), Rational(65, 72), Rational(-55, 1296)],
    }
    live_ok = all(m[k] == v for k, v in expected.items())
    pinned_ok = all(
        [str(c) for c in m[k]] == cert["representations"][k]["lambda_coefficients"]
        for k in expected
    )
    lam = {k: sum(m[k][j] * _EPS**j for j in range(4)) for k in expected}
    cf = Rational(4, 3)
    tau = expand(series(-(2 / cf) * log(lam["F"]), _EPS, 0, 4).removeO())
    k8 = expand(series(-log(lam["Adj"]) / tau, _EPS, 0, 3).removeO())
    k6 = expand(series(-log(lam["Sym2"]) / tau, _EPS, 0, 3).removeO())
    tau_ok = tau == _EPS + Rational(7, 24) * _EPS**2 + Rational(13, 144) * _EPS**3
    k_ok = (
        k8 == Rational(3, 2) - Rational(5, 96) * _EPS**2
        and k6 == Rational(5, 3) - Rational(5, 72) * _EPS**2
    )
    ok = live_ok and pinned_ok and tau_ok and k_ok and m["_norm"] == Rational(3, 2)
    ok = ok and m["_means"] == (Rational(-1, 6), Rational(-5, 108))
    return (
        ok,
        (
            f"Vandermonde normalization {m['_norm']}, density-correction means {m['_means']}; "
            f"lambda_3 coefficients {[str(c) for c in m['F']]}, "
            f"lambda_8 {[str(c) for c in m['Adj']]}, lambda_6 {[str(c) for c in m['Sym2']]}; "
            f"tau = {tau}; k(8) = {k8}; k(6) = {k6}; the pinned certificate agrees string for "
            f"string: {pinned_ok}"
        ),
        {
            "TAU_W_EPS2": Rational(7, 24),
            "K_W_ADJ_EPS2": Rational(-5, 96),
            "K_W_SEXTET_EPS2": Rational(-5, 72),
        },
    )


_FINITE_STEP = (
    "the second-order C-odd shell of the symmetric Wilson transfer generator at finite temporal "
    "step: with d_tau(Delta) = (tau/2) coth(tau Delta/2) the hopping is t_W = 5/612 + "
    "175/280908 eps^2 + O(eps^3), the flat scalar s_2W = 11/306 - 89159/2247264 eps^2, and the "
    "first literal-source Gram coefficient -2 d_tau(E_F) = -3/4 - 4/9 eps^2"
)


@wilson.check(
    _FINITE_STEP,
    _CITE + " eqs. (11)-(18); window_shell_certificate.json",
    rests_on=(_CHANNELS_TN, _MULTIPLIERS),
)
def _():
    # The note's finite-step weight replaces 1/Delta by (tau/2) coth(tau Delta/2) in every
    # channel; the gaps use the calibrated energies, k(F) = C_F/2 exactly and k(8), k(6)
    # from the multipliers. The scalar follows the SU(3) ledger's same-face sextet route,
    # disjoint bubble and twelve-neighbour count; the source coefficient is -2 d_tau(E_F)
    # against the Hamiltonian -2/E_F = -3/4.
    m = _su3_multipliers()
    lam = {k: sum(m[k][j] * _EPS**j for j in range(4)) for k in ("F", "Adj", "Sym2")}
    cf = Rational(4, 3)
    tau = series(-(2 / cf) * log(lam["F"]), _EPS, 0, 4).removeO()
    k8 = series(-log(lam["Adj"]) / tau, _EPS, 0, 3).removeO()
    k6 = series(-log(lam["Sym2"]) / tau, _EPS, 0, 3).removeO()

    def d_tau(gap):
        return series(tau / 2 * coth(tau * gap / 2), _EPS, 0, 3).removeO()

    w = {
        "1": -Rational(1, 9) * d_tau(cf),
        "adj": -Rational(8, 9) * d_tau(cf + k8),
        "lam2": -Rational(3, 9) * d_tau(cf + cf / 2),
        "sym2": -Rational(6, 9) * d_tau(cf + k6),
    }
    a_w, b_w = w["1"] + w["adj"], w["lam2"] + w["sym2"]
    t_w = expand(series(b_w - a_w, _EPS, 0, 3).removeO())
    e_f = Rational(8, 3)
    ell_w = a_w + b_w + 2 * d_tau(e_f)
    sigma_w = -d_tau(4 * k6 - e_f)
    s2_w = expand(series(sigma_w + 2 * d_tau(e_f) + 12 * ell_w - 4 * t_w, _EPS, 0, 3).removeO())
    source = expand(series(-2 * d_tau(e_f), _EPS, 0, 3).removeO())
    t2, s2, g2 = Rational(175, 280908), Rational(-89159, 2247264), Rational(-4, 9)
    ok = t_w == Rational(5, 612) + t2 * _EPS**2
    ok = ok and s2_w == Rational(11, 306) + s2 * _EPS**2
    ok = ok and source == Rational(-3, 4) + g2 * _EPS**2
    # the Hamiltonian limit of the same expressions is the SU(3) second-order ledger
    ok = ok and t_w.subs(_EPS, 0) == Rational(5, 612) and s2_w.subs(_EPS, 0) == Rational(11, 306)
    # the package's own certificate records the two eps^2 coefficients as strings
    pinned_text = json.dumps(_shell_certificate())
    pinned_ok = '"175/280908"' in pinned_text and '"-89159/2247264"' in pinned_text
    return (
        ok and pinned_ok,
        (
            f"t_W = {t_w}; s_2W = {s2_w}; -2 d_tau(E_F) = {source}; at eps = 0 the SU(3) "
            f"ledger's 5/612 and 11/306; the pinned certificate carries the same two eps^2 "
            f"coefficients: {pinned_ok}"
        ),
        {"T_W_EPS2": t2, "S_2W_EPS2": s2, "G_W_SOURCE_EPS2": g2},
    )
