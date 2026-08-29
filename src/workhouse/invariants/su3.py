from __future__ import annotations

from sympy import (
    Matrix,
    Rational,
    expand,
    eye,
    simplify,
    sin,
    symbols,
)

from .. import constants as K
from ._core import _suite
from ._shared import _bridge_towers

# ==========================================================================
su3_series = _suite("SU(3) second and third order")


@su3_series.check("d_- - 4 t_- = 11/306", "PAPER eq. (7)")
def _():
    v = K.D_MINUS_2 - 4 * K.T_MINUS_2
    return v == Rational(11, 306), f"= {v}"


@su3_series.check("t_- equals the rank law at N = 3", "MASTER_THEORY §4.3")
def _():
    return K.hopping(3) == K.T_MINUS_2, f"{K.T_MINUS_2} == {K.hopping(3)}"


@su3_series.check("C-even bandwidth = top - bottom = 88/153", "PAPER App. B")
def _():
    w = K.BAND_EVEN_TOP - K.BAND_EVEN_BOTTOM
    return w == K.BAND_EVEN_WIDTH, f"= {w}"


@su3_series.check("C-odd manifold width = 5/51", "PAPER App. B")
def _():
    w = K.BAND_ODD_TOP - K.BAND_ODD_FLAT
    return w == K.BAND_ODD_WIDTH, f"= {w}"


@su3_series.check("d_3 = 7/32 + 12*leak_3 - 4*b_3", "MASTER_THEORY §4.4")
def _():
    v = Rational(7, 32) + 12 * K.LEAK_3 - 4 * K.B_3
    return v == K.D_3, f"= {v}"


@su3_series.check("E_flat and t(u) carry the ledger coefficients", "MASTER_THEORY §4.4")
def _():
    e, t = K.e_flat(), K.t_series()
    ok = (
        e.coeff(K.u, 0) == Rational(8, 3)
        and e.coeff(K.u, 1) == 1
        and e.coeff(K.u, 2) == Rational(11, 306)
        and e.coeff(K.u, 3) == K.D_3
        and t.coeff(K.u, 2) == K.T_MINUS_2
        and t.coeff(K.u, 3) == K.B_3
    )
    return ok, "E_flat = 8/3 + u + 11/306 u^2 - 109151/249696 u^3"


@su3_series.check(
    "d_- = 1/2 + 12*leak_2, and leak_2 = -11/306",
    "ENGINE_FLUX_su3_domino_d3.py / MASTER paper §5",
)
def _():
    leak_2 = Rational(-11, 306)
    ok = Rational(1, 2) + 12 * leak_2 == K.D_MINUS_2 and leak_2 == K.T_PLUS_2
    return ok, (
        "the C-odd second-order diagonal is the tower term 1/2 plus twelve "
        "per-neighbour leakages of -11/306; that leakage equals the C-even "
        "hopping exactly — the vacuum-route mechanism, order 2"
    )


@su3_series.check(
    "leak_3 is assembled from the domino diagonal and the vacuum piece",
    "ENGINE_FLUX_su3_domino_d3.py locks",
)
def _():
    tower_3_minus = Rational(7, 32)
    tower_3_plus = Rational(101, 200)
    odd_ok = K.D3_ODD_DOMINO - K.VAC3_DOMINO - tower_3_minus == K.LEAK_3
    even_ok = K.D3_EVEN_DOMINO - K.VAC3_DOMINO - tower_3_plus == K.T3_EVEN
    return odd_ok and even_ok, (
        f"leak_3 = D3_odd - vac_3 - 7/32 = {K.D3_ODD_DOMINO} - ({K.VAC3_DOMINO}) "
        f"- 7/32 = {K.LEAK_3}; the C-even mirror gives leak_3+ = t_3+ = "
        f"{K.T3_EVEN}, the vacuum-route identity at order 3"
    )


@su3_series.check(
    "one assembly formula gives every registered band value",
    "ENGINE_FLUX_su3_domino_d3.py / MASTER paper eq. (30)",
)
def _():
    u_, bridge_minus, bridge_plus = _bridge_towers()
    tower = {
        (2, "-"): bridge_minus.coeff(u_, 2),
        (3, "-"): bridge_minus.coeff(u_, 3),
        (2, "+"): bridge_plus.coeff(u_, 2),
        (3, "+"): bridge_plus.coeff(u_, 3),
    }
    leak = {
        (2, "-"): Rational(-11, 306),
        (2, "+"): Rational(-11, 306),  # = t_2+, vacuum-route identity
        (3, "-"): K.LEAK_3,
        (3, "+"): K.T3_EVEN,  # = t_3+, same identity one order up
    }
    hop = {
        (2, "-"): K.T_MINUS_2,
        (2, "+"): K.T_PLUS_2,
        (3, "-"): K.B_3,
        (3, "+"): K.T3_EVEN,
    }

    def assemble(lam, r, s):
        return tower[(r, s)] + 12 * leak[(r, s)] + lam * hop[(r, s)]

    targets = [
        (assemble(0, 2, "-"), K.D_MINUS_2),
        (assemble(-4, 2, "-"), K.BAND_ODD_FLAT),
        (assemble(8, 2, "-"), K.BAND_ODD_TOP),
        (assemble(0, 2, "+"), K.D_PLUS_2),
        (assemble(12, 2, "+"), K.BAND_EVEN_BOTTOM),
        (assemble(-4, 2, "+"), K.BAND_EVEN_TOP),
        (assemble(-4, 3, "-"), K.D_3),
        (assemble(8, 3, "-"), K.D3_TOP),
        (assemble(12, 3, "+"), K.M3_EVEN_K0),
    ]
    ok = all(got == want for got, want in targets)
    return ok, (
        "E_s(lambda, r) = tower_{r,s} + 12 leak_{r,s} + lambda t_{r,s} with the "
        "tower terms from the certified 4*Delta(3u/2) conversion reproduces all "
        "nine registered diagonal and band values across both sectors and both "
        "orders — the coupling erratum (C4/G2) and the band ledger are one "
        "statement"
    )


@su3_series.check(
    "the two band spans ARE the two incidence spectra",
    "MASTER paper §4.5 / ENGINE_FLUX_su3_domino_d3.py key corrected_Ceven_bandwidth_16|t|",
)
def _():
    def adjacency_spectrum(mat):
        return (mat * mat.T.conjugate() - 4 * eye(3)).eigenvals()

    signed = Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])  # every d_j = e^{i0}-1 = 0
    # the unsigned incidence removes the orientation signs from the matrix AND
    # replaces e^{ik}-1 by e^{ik}+1; at Gamma every entry is 2, at R every 0
    unsigned_gamma = Matrix([[2, 2, 0], [2, 0, 2], [0, 2, 2]])
    unsigned_r = Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    signed_gamma_ok = adjacency_spectrum(signed) == {-4: 3}
    unsigned_ok = adjacency_spectrum(unsigned_gamma) == {12: 1, 0: 2} and adjacency_spectrum(
        unsigned_r
    ) == {-4: 3}
    # signed spectrum over the zone is {-4, q-4, q-4} with q in [0, 12]
    widths_ok = 12 * K.T_MINUS_2 == K.BAND_ODD_WIDTH and 16 * abs(K.T_PLUS_2) == K.BAND_EVEN_WIDTH
    return signed_gamma_ok and unsigned_ok and widths_ok, (
        "signed adjacency spans [-4, 8] (q in [0,12]): width 12 t_- = 5/51; the "
        "unsigned adjacency is {12, 0, 0} at Gamma and {-4, -4, -4} at R — no "
        "shared eigenvalue, so no unsigned level is momentum independent — "
        "spanning 16: width 16|t_+| = 88/153; each sector's bandwidth is its own "
        "incidence spectrum, so the unsigned control is the C-even sector, not a "
        "hypothetical"
    )


@su3_series.check(
    "FINDING: no Gamma-point datum can constrain the hopping",
    "MASTER paper Rmk. 12 / HAMER_1989",
)
def _():
    eps = symbols("eps")
    d3_family = Rational(7, 32) + 12 * (K.LEAK_3 + eps / 3) - 4 * (K.B_3 + eps)
    invariant = simplify(d3_family - K.D_3) == 0
    top_family = Rational(7, 32) + 12 * (K.LEAK_3 + eps / 3) + 8 * (K.B_3 + eps)
    top_shift = expand(top_family - (Rational(7, 32) + 12 * K.LEAK_3 + 8 * K.B_3))
    k1, k2, k3 = symbols("k1 k2 k3", real=True)
    q = 4 * (sin(k1 / 2) ** 2 + sin(k2 / 2) ** 2 + sin(k3 / 2) ** 2)
    q_gamma = q.subs({k1: 0, k2: 0, k3: 0})
    return invariant and top_shift == 12 * eps and q_gamma == 0, (
        "the one-parameter family (b_3 + eps, leak_3 + eps/3) leaves d_3 — and "
        "with q(0) = 0 every Gamma-point datum — exactly unchanged, while the "
        "lambda = 8 band top moves by 12 eps; Hamer's rest-frame agreement pins "
        "the combination 12 leak_3 - 4 b_3, never the hopping itself"
    )


@su3_series.check(
    "the manuscript's SU(3) ledger is this registry, value by value",
    "MASTER paper App. C",
)
def _():
    ledger = [
        (Rational(8, 3), K.e_flat().coeff(K.u, 0)),
        (Rational(1), K.e_flat().coeff(K.u, 1)),
        (Rational(5, 612), K.T_MINUS_2),
        (Rational(11, 306), K.BAND_ODD_FLAT),
        (Rational(1975, 124848), K.B_3),
        (Rational(-12331, 249696), K.LEAK_3),
        (Rational(-109151, 249696), K.D_3),
    ]
    ok = all(printed == registered for printed, registered in ledger)
    return ok, (
        "all seven table rows match the registry exactly. Their SCOPE is not "
        "uniform, and saying 'the other six specialise all-rank statements' "
        "was wrong: the u^0 row and the u^2 BB^dagger coefficient are the "
        "all-rank 2 C_F and t_N; the u^1 row is SU(3)-only (the epsilon "
        "channel, vanishing for N >= 4); the u^2 flat scalar inherits the "
        "SU(3) tower term through the assembly formula; and the three u^3 rows "
        "are SU(3)-only AND conditional on the supplied domino ledger. A "
        "ledger table whose rows carry different statuses under one heading is "
        "how a conditional value gets read as an all-rank one"
    )
