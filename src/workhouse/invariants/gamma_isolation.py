"""The T1 triplet at Gamma, and the uniform isolation of the flat band on the punctured zone.

The corpus leaves open a "uniform near-Gamma isolated-band theorem": the
second-order splitting between the flat band and the two dispersive bands is
``t(u) q_a(k)``, of order ``u^2 |k|^2``, and the fourth-order kernel is of order
``u^4``, so for ``|k| <~ u`` the two are said to compete (MASTER_THEORY §12;
G11's exclusion radius ``|k| >= K u`` is the recorded workaround).

Two facts remove the competition. At ``k = 0`` the three plaquette
orientations span the ``T_1`` irrep of the cubic group -- the three
polarisations of the ``1^{+-}`` state at rest -- so every cubic-covariant
effective Hamiltonian is a *scalar* there, at every order (Schur); and
inversion kills the linear term, so every order's deviation from its Gamma
scalar is ``O(|k|^2)``, not just the second order's. On the Hodge form this is
explicit: ``H4(k) - s I`` is built from ``L_up``, ``Lambda = B B^dagger`` and
its cross-plane half, all of which vanish quadratically at Gamma, and the
Hodge Laplacian ``L_down + L_up = q_a I`` turns the bound into arithmetic:

    H4 - s I = q_a [ (-nu~ + 2C) P_c + eps(k) P_t ] - 2C diag(a),
    eps(k) = u q_a - 8u - pi~,   P_c = carrier projector,  P_t = 1 - P_c,

so ``||H4(k) - s I|| <= C_iso q_a(k)`` with ``C_iso = -nu~ = 5/48`` for the
assembled ``C_shp`` (the condition is ``-nu~ + 2C >= |pi~| + 4u`` and
``C <= 0``, both exact). By Weyl's inequality the lowest band of
``t(u) Lambda + u^4 (H4 - sI)`` is then isolated from the other two at every
``k != 0``, with relative gap ``>= q_a (t_3 u^2 - 2 C_iso u^4)``, for every
``0 < u < u* = sqrt(t_3 / (2 C_iso)) = sqrt(2/51)``. No exclusion radius.
The triple degeneracy at ``k = 0`` itself is exact and unavoidable, and
harmless: it is the spin-1 multiplet at rest.

What this does not claim: it is a statement about the fourth-order effective
Hamiltonian. Every higher order has the same structure by the same symmetry,
but bounding their sum is the convergence question of G17, not settled here.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import pi, sin, sqrt

from .. import constants as K
from .. import kernel_orbits as KO
from ._core import _suite

gamma = _suite("the T1 triplet at Gamma and the uniform isolation of the flat band")
_CITE = "G11; MASTER_THEORY §3 (singular at Gamma), §5, §12 (the near-Gamma competition); ADR 0028"
_PLANES = KO.PLANES


def _rat(x) -> Fraction:
    return Fraction(x.p, x.q)


def _amps(rho: Fraction) -> dict:
    return {
        "u": _rat(K.X_QUANTUM),
        "nu": _rat(K.NU_ORBIT),
        "pi": _rat(K.PI_ORBIT),
        "sigma": _rat(K.SIGMA_ORBIT),
        "rho": rho,
    }


def _forms() -> dict[str, dict]:
    """The Hodge form for both recorded C_shp values; neither is preferred (rule 2)."""
    return {
        "assembled": KO.hodge_form(_amps(_rat(K.RHO_ASSEMBLED))),
        "historical": KO.hodge_form(_amps(_rat(K.RHO_ORBIT))),
    }


def _at_zero(laurent: dict) -> Fraction:
    return sum(laurent.values(), Fraction(0))


def _linear(laurent: dict) -> tuple:
    return tuple(sum((c * e[i] for e, c in laurent.items()), Fraction(0)) for i in range(3))


def _scale(records: dict, c: Fraction) -> dict:
    return {k: c * v for k, v in records.items() if c * v}


def _q_a_records() -> dict:
    """``q_a(k) I`` as records: ``sum_i (2 - T_i - T_i^-1)`` on every plane."""
    out = {}
    for p in _PLANES:
        out[(p, p, (0, 0, 0))] = Fraction(6)
        for i in range(3):
            for sgn in (1, -1):
                e = [0, 0, 0]
                e[i] = sgn
                out[(p, p, tuple(e))] = Fraction(-1)
    return out


def _diag_records(records: dict) -> dict:
    return {k: v for k, v in records.items() if k[0] == k[1]}


_T1_IRREP = (
    "the three plaquette orientations at k = 0 carry an irreducible representation of the "
    "cubic group (the T1 triplet), so every cubic-covariant effective Hamiltonian is a scalar "
    "at Gamma at every order"
)


@gamma.check(_T1_IRREP, _CITE)
def _():
    # chi(g) = trace of g on the oriented planes; the rep is irreducible iff sum chi^2 = |G|.
    group = KO.cubic_group()
    chars = []
    for g in group:
        tr = 0
        for p in _PLANES:
            image, sign = KO.act_plane(g, p)
            if image == p:
                tr += sign
        chars.append(tr)
    norm = sum(c * c for c in chars)
    return norm == len(group) == 48, (
        f"character norm sum chi(g)^2 = {norm} over the {len(group)} signed axis permutations, "
        f"equal to the group order, so the orientation triplet is one irreducible T1; by Schur any "
        "operator commuting with the group is a scalar on it. The k = 0 subspace of the "
        "one-plaquette C-odd sector is exactly this triplet: the three polarisations of the "
        "1^{+-} state at rest"
    )


_SCALAR_AT_GAMMA = (
    "the fourth-order kernel at Gamma is the scalar q_band^(4) on the orientation triplet, for "
    "either recorded C_shp, and has no linear term in k"
)


@gamma.check(_SCALAR_AT_GAMMA, _CITE, rests_on=(_T1_IRREP,))
def _():
    out = {}
    for name, form in _forms().items():
        S = KO.bloch_matrix(KO.hodge_records(form))
        h0 = [[_at_zero(S[o][i]) for i in _PLANES] for o in _PLANES]
        scalar = h0[0][0]
        is_scalar = all(h0[a][b] == (scalar if a == b else 0) for a in range(3) for b in range(3))
        no_linear = all(_linear(S[o][i]) == (0, 0, 0) for o in _PLANES for i in _PLANES)
        by_form = 2 * form["nu~"] + 16 * form["u"] + 4 * form["pi~"] + form["sigma~"]
        out[name] = (is_scalar, no_linear, scalar, by_form)
    ok = all(v[0] and v[1] and v[2] == v[3] == _rat(K.Q_BAND_4) for v in out.values())
    return ok, (
        f"H4(0) = s I with s = {out['assembled'][2]} = q_band^(4) for the assembled and the "
        f"historical C_shp alike (C multiplies the cross-plane half of B B^dagger, which "
        f"vanishes at Gamma), s = 2nu~ + 16u + 4pi~ + sigma~; every entry's linear term at "
        f"Gamma is zero "
        f"(inversion). The Gamma anchor is the same scalar in both kernels, which is why a scalar "
        "re-anchoring could never decide C2"
    )


_HODGE_ALGEBRA = (
    "the Hodge Laplacian on plaquettes is the scalar q_a: L_down + L_up = q_a I, Lambda^2 = q_a "
    "Lambda, L_up Lambda = 0, so Lambda = q_a P_t and L_up = q_a P_c"
)


@gamma.check(_HODGE_ALGEBRA, _CITE)
def _():
    down, up, qa = KO.down_laplacian(), KO.up_laplacian(), _q_a_records()
    total = KO.combine((1, down), (1, up)) == qa
    idem = KO.compose(down, down) == KO.compose(qa, down)
    orth = KO.compose(up, down) == {}
    up_idem = KO.compose(up, up) == KO.compose(qa, up)
    ok = total and idem and orth and up_idem
    return ok, (
        f"as exact record algebra: L_down + L_up = q_a I ({total}), Lambda^2 = q_a Lambda "
        f"({idem}), L_up Lambda = 0 ({orth}), L_up^2 = q_a L_up ({up_idem}); Lambda = B B^dagger "
        "has eigenvalues 0 on the carrier and q_a (twice) on the transverse bands, L_up the reverse"
    )


_BOUND = (
    "the fourth-order kernel is bounded by C_iso q_a(k) away from its Gamma scalar, C_iso = 5/48 "
    "for the assembled C_shp, so the flat band is isolated at every k != 0 for u^2 < 2/51 -- no "
    "exclusion radius"
)


@gamma.check(_BOUND, _CITE, rests_on=(_SCALAR_AT_GAMMA, _HODGE_ALGEBRA))
def _():
    # H4 - sI = -nu~ L_up + u (S^2 - 16) - pi~ (S + 4) - 2C R with S + 4 = Lambda,
    # L_up = q_a - Lambda, S^2 - 16 = (q_a - 8) Lambda, R = Lambda - diag(Lambda):
    # verified as records, then bounded.
    down, qa, ident = KO.down_laplacian(), _q_a_records(), KO.identity()
    lam = down
    up = KO.combine((1, qa), (-1, lam))
    lam_sq = KO.compose(lam, lam)
    cross = KO.combine((1, lam), (-1, _diag_records(lam)))
    t3 = _rat(K.T_MINUS_2)
    rows = {}
    for name, form in _forms().items():
        s = 2 * form["nu~"] + 16 * form["u"] + 4 * form["pi~"] + form["sigma~"]
        lhs = KO.combine((1, KO.hodge_records(form)), (-s, ident))
        rhs = KO.combine(
            (-form["nu~"], up),
            (form["u"], KO.combine((1, lam_sq), (-8, lam))),
            (-form["pi~"], lam),
            (-2 * form["C"], cross),
        )
        decomposed = lhs == rhs
        # eps(k) = u q_a - 8u - pi~ ranges over [-8u - pi~, 4u - pi~] as q_a runs over [0, 12]
        sup_eps = max(abs(-8 * form["u"] - form["pi~"]), abs(4 * form["u"] - form["pi~"]))
        carrier_coeff = -form["nu~"] + 2 * form["C"]
        # ||q_a [(-nu~ + 2C) P_c + eps P_t] - 2C diag(a)||
        #     <= q_a (max(|-nu~ + 2C|, sup|eps|) + 2|C|)
        c_iso = max(abs(carrier_coeff), sup_eps) + 2 * abs(form["C"])
        u_star_sq = t3 / (2 * c_iso)
        rows[name] = (decomposed, carrier_coeff, sup_eps, c_iso, u_star_sq)
    asm = rows["assembled"]
    tight = asm[1] >= asm[2] and _forms()["assembled"]["C"] <= 0 and asm[3] == Fraction(5, 48)
    ok = all(r[0] for r in rows.values()) and tight and asm[4] == Fraction(2, 51)
    return (
        ok,
        (
            f"H4 - sI decomposes exactly as records for both kernels; assembled: -nu~ + 2C = "
            f"{asm[1]} >= sup|eps| = {asm[2]} and C <= 0, so C_iso = -nu~ = 5/48 exactly and "
            f"u*^2 = t_3/(2 C_iso) = {asm[4]} (u* = {sqrt(float(asm[4])):.5f}); historical: "
            f"C_iso = {rows['historical'][3]} = {float(rows['historical'][3]):.5f}, u*^2 = "
            f"{rows['historical'][4]} (u* = {sqrt(float(rows['historical'][4])):.5f}). By Weyl, "
            "E1(k) - E0(k) >= q_a(k) (t(u) - 2 C_iso u^4) >= q_a(k) u^2 (t_3 - 2 C_iso u^2) > 0 "
            "at every k != 0 below u*, using t(u) >= t_3 u^2 (b_3 > 0). The lowest band is the "
            "carrier's"
        ),
        {"U_STAR_SQ_ISOLATION": Fraction(2, 51)},
    )


_TIGHT = (
    "the isolation bound is tight: the numerical supremum of ||H4(k) - sI|| / q_a(k) over the "
    "zone is 5/48, attained on an axis, and the fourth-order band gap obeys the bound at every "
    "sampled k"
)


@gamma.check(_TIGHT, _CITE, tier=2, rests_on=(_BOUND,))
def _():
    import mpmath as mp

    mp.mp.dps = 20
    form = _forms()["assembled"]
    S = KO.bloch_matrix(KO.hodge_records(form))
    lam = KO.bloch_matrix(KO.down_laplacian())
    s = 2 * form["nu~"] + 16 * form["u"] + 4 * form["pi~"] + form["sigma~"]

    def ev(L, k):
        return sum(
            mp.mpf(c.numerator) / c.denominator * mp.expj(sum(e[i] * k[i] for i in range(3)))
            for e, c in L.items()
        )

    def mat(SS, k):
        return mp.matrix([[ev(SS[o][i], k) for i in _PLANES] for o in _PLANES])

    def eigs(M):
        E, _ = mp.eigh(M)
        return sorted(float(x) for x in E)

    def q_a(k):
        return sum(4 * sin(x / 2) ** 2 for x in k)

    H0 = float(s) * mp.eye(3)
    grid = [-pi + 2 * pi * j / 8 for j in range(9)]
    near = [
        (1e-3, 0.0, 0.0),
        (1e-3, 1e-3, 0.0),
        (1e-3, 1e-3, 1e-3),
        (1e-3, 2e-3, 3e-3),
        (0.0, 0.0, 2e-3),
    ]
    sup, where = 0.0, None
    for k in list(product(grid, repeat=3)) + near:
        q = q_a(k)
        if q < 1e-12:
            continue
        r = max(abs(x) for x in eigs(mat(S, k) - H0)) / q
        if r > sup:
            sup, where = r, k
    c_iso = 5 / 48
    tol = 1e-9
    t3 = float(_rat(K.T_MINUS_2))
    gaps_ok = True
    worst_margin = None
    for u in (0.05, 0.10, 0.19):
        bound = t3 * u**2 - 2 * c_iso * u**4
        for k in [
            (0.3, 0.0, 0.0),
            (0.01, 0.02, 0.0),
            (pi, pi, pi),
            (1e-3, 0.0, 0.0),
            (1.0, 2.0, 0.5),
        ]:
            M = t3 * u**2 * mat(lam, k) + u**4 * (mat(S, k) - H0)
            e = eigs(M)
            margin = (e[1] - e[0]) / q_a(k) - bound
            gaps_ok = gaps_ok and margin >= -tol
            worst_margin = margin if worst_margin is None else min(worst_margin, margin)
    ok = abs(sup - c_iso) <= tol and gaps_ok
    return ok, (
        f"sup over a 9^3 grid plus five near-Gamma points of ||H4(k) - sI||/q_a(k) = {sup:.12f} "
        f"vs 5/48 = {c_iso:.12f} (|diff| <= {tol}), attained at k = {where}; with t_3 u^2 as the "
        f"second-order term, (E1 - E0)/q_a exceeds t_3 u^2 - 2 (5/48) u^4 at every sampled (u, k), "
        f"worst margin {worst_margin:.3e}. Tolerance {tol} on floats; the exact statement is "
        "the T1 bound this rests on"
    )


_BAND_THEOREM = (
    "a band theorem at fourth order: on the punctured zone the lowest band is E_flat + u^4 "
    "(s + A q_a + 4C e2/q_a) up to a remainder bounded by C_iso^2 u^6 q_a / (t_3 - 2 C_iso u^2), "
    "uniformly in k"
)


@gamma.check(_BAND_THEOREM, _CITE, rests_on=(_BOUND,))
def _():
    # The carrier expectation of H4 - sI is the corpus dispersion, exactly as Laurent
    # polynomials: psi^dagger (H4 - sI) psi = A q_a^2 + 4C e2 with |psi|^2 = q_a, i.e. the
    # centered shape A q_a + 4C e2/q_a with B = D = 0. With the isolation gap of the previous
    # check, the Kato-Temple inequality bounds the lowest eigenvalue of
    # M = t u^2 Lambda + u^4 (H4 - sI) by |E_0 - u^4 mu(k)| <= ||E||^2 / delta with
    # ||E|| <= C_iso u^4 q_a and delta >= q_a (t_3 u^2 - 2 C_iso u^4): the remainder is
    # C_iso^2 u^6 q_a / (t_3 - 2 C_iso u^2), so a fixed-momentum coefficient theorem IS a band
    # theorem at this order. The bound is then tested numerically on a grid (floats; the exact
    # content is the Laurent identity and the constants).
    import mpmath as mp

    mp.mp.dps = 20
    form = _forms()["assembled"]
    s = 2 * form["nu~"] + 16 * form["u"] + 4 * form["pi~"] + form["sigma~"]
    centered = KO.combine((1, KO.hodge_records(form)), (-s, KO.identity()))
    expectation = KO.bloch(centered.items())
    a_shp = Fraction(5, 48)
    c_shp = form["C"]
    # q_a and e2 as Laurent polynomials in z_i = e^{i k_i}
    qa = _q_a_records()
    qa_l = KO.bloch_matrix(qa)[_PLANES[0]][_PLANES[0]]
    e2_l = {}
    for i in range(3):
        for j in range(i + 1, 3):
            ai = {(0, 0, 0): Fraction(2)}
            aj = {(0, 0, 0): Fraction(2)}
            for sgn in (1, -1):
                ei, ej = [0, 0, 0], [0, 0, 0]
                ei[i], ej[j] = sgn, sgn
                ai[tuple(ei)] = Fraction(-1)
                aj[tuple(ej)] = Fraction(-1)
            e2_l = KO._add(e2_l, KO._mul(ai, aj))
    target = KO._add(KO._mul(qa_l, qa_l), e2_l, Fraction(0))
    target = KO._add({e: a_shp * c for e, c in KO._mul(qa_l, qa_l).items()}, e2_l, 4 * c_shp)
    identity = expectation == {e: c for e, c in target.items() if c}
    c_iso = Fraction(5, 48)
    t3 = _rat(K.T_MINUS_2)

    S = KO.bloch_matrix(KO.hodge_records(form))
    lam = KO.bloch_matrix(KO.down_laplacian())

    def ev(L, k):
        return sum(
            mp.mpf(c.numerator) / c.denominator * mp.expj(sum(e[i] * k[i] for i in range(3)))
            for e, c in L.items()
        )

    def mat(SS, k):
        return mp.matrix([[ev(SS[o][i], k) for i in _PLANES] for o in _PLANES])

    def q_a(k):
        return sum(4 * sin(x / 2) ** 2 for x in k)

    def e2(k):
        a = [4 * sin(x / 2) ** 2 for x in k]
        return a[0] * a[1] + a[0] * a[2] + a[1] * a[2]

    H0 = float(s) * mp.eye(3)
    worst = 0.0
    grid = [-pi + 2 * pi * j / 6 for j in range(7)]
    points = list(product(grid, repeat=3)) + [(1e-3, 0.0, 0.0), (1e-3, 2e-3, 3e-3), (0.2, 0.1, 0.0)]
    for u in (0.05, 0.10, 0.15):
        remainder_const = float(c_iso) ** 2 * u**6 / (float(t3) - 2 * float(c_iso) * u**2)
        for k in points:
            q = q_a(k)
            if q < 1e-12:
                continue
            M = float(t3) * u**2 * mat(lam, k) + u**4 * (mat(S, k) - H0)
            E, _ = mp.eigh(M)
            e0 = min(float(x) for x in E)
            mu = float(a_shp) * q + 4 * float(c_shp) * e2(k) / q
            ratio = abs(e0 - u**4 * mu) / (remainder_const * q)
            worst = max(worst, ratio)
    ok = identity and worst <= 1.0
    return ok, (
        f"psi^dagger (H4 - sI) psi = A q_a^2 + 4C e2 exactly as Laurent polynomials ({identity}), "
        f"A = {a_shp}, C = {c_shp}: the centered dispersion A q_a + 4C e2/q_a with B = D = 0; "
        f"Kato-Temple remainder C_iso^2 u^6 q_a/(t_3 - 2 C_iso u^2) with C_iso = 5/48; over a 7^3 "
        f"grid plus three near-Gamma points at u = 0.05, 0.10, 0.15 the worst |E_0 - u^4 mu| is "
        f"{worst:.4f} of the bound (<= 1). On T_L^3 every k != 0 has q_a >= 4 sin^2(pi/L), so the "
        "finite-volume isolation at fourth order closes as L^-2 with the same constants"
    )
