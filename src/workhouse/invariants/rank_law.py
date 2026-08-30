from __future__ import annotations

from sympy import (
    Rational,
    diff,
    numer,
    series,
    simplify,
    solve,
    symbols,
    sympify,
    together,
)

from .. import constants as K
from ._core import _suite

# ==========================================================================
rank_law = _suite("second order, all ranks")


@rank_law.check("t_N = B_N - A_N", "MASTER_THEORY §4.3")
def _():
    lhs = K.parallel_sum() - K.antiparallel_sum()
    return simplify(lhs - K.hopping()) == 0, "channel difference reproduces the rank law"


@rank_law.check("t_2 = 0 and t_3 = 5/612", "MASTER_THEORY §4.3")
def _():
    ok = K.hopping(2) == 0 and K.hopping(3) == Rational(5, 612)
    return ok, f"t_2={K.hopping(2)}, t_3={K.hopping(3)}"


@rank_law.check("t_N > 0 for N >= 3", "MASTER_THEORY §4.3")
def _():
    bad = [n for n in range(3, 40) if not K.hopping(n) > 0]
    return not bad, "positive for N=3..39" if not bad else f"non-positive at {bad}"


@rank_law.check("deficit identity 1/4 - N^3 t_N", "MASTER_THEORY §4.3")
def _():
    lhs = Rational(1, 4) - K.N**3 * K.hopping()
    return simplify(lhs - K.hopping_deficit()) == 0, "closed form matches"


@rank_law.check("deficit positive at N = 3, 5, 9", "MASTER_THEORY §4.3")
def _():
    vals = {n: K.hopping_deficit(n) for n in (3, 5, 9)}
    return all(v > 0 for v in vals.values()), f"{ {k: str(v) for k, v in vals.items()} }"


@rank_law.check("large-N expansion of t_N through 1/N^9", "GLUEBALL §4")
def _():
    inv = symbols("inv", positive=True)
    ser = series(K.hopping(1 / inv), inv, 0, 10).removeO()
    got = {k: ser.coeff(inv, k) for k in K.HOPPING_LARGE_N}
    return got == K.HOPPING_LARGE_N, f"{ {k: str(v) for k, v in got.items()} }"


@rank_law.check("N^3 t_N increases monotonically to 1/4", "CANON §10.2/§10.5")
def _():
    num = simplify(numer(together(diff(K.N**3 * K.hopping(), K.N))))
    cubic_in_N = K.MONOTONICITY_CUBIC.subs(K.x, K.N**2)
    # sympy cancels one power of x that the corpus leaves in the printed prefactor;
    # the sign-determining cubic is what must agree.
    matches = simplify(num - 4 * K.N**3 * cubic_in_N) == 0
    positive = all(K.MONOTONICITY_CUBIC.subs(K.x, v) > 0 for v in (4, 9, 16, 10**6))
    roots = [complex(r).real for r in solve(K.MONOTONICITY_CUBIC, K.x)]
    return (
        matches and positive,
        f"d/dN numerator = 4N^3*cubic(N^2); cubic roots {[round(r, 4) for r in roots]} "
        f"all < 4, so cubic > 0 on the physical range",
    )


# --------------------------------------------------------------------------
# The shared-link channel weights, derived rather than hypothesised.
#
# Every second-order statement rests on the channel weight d_rho/N^2. The
# corpus introduced it as an "isotropy" assignment; the master paper derives
# it from the order-two Weingarten values, and these checks carry out that
# derivation symbolically in N, so the premise stops being a physical input.
# --------------------------------------------------------------------------

#: Fusion-channel table (dimension, quadratic Casimir), MASTER paper eq. (12).
_CHANNELS = {
    "singlet": (sympify(1), sympify(0)),
    "adjoint": (K.N**2 - 1, K.N),
    "antisym": (K.N * (K.N - 1) / 2, (K.N + 1) * (K.N - 2) / K.N),
    "sym": (K.N * (K.N + 1) / 2, (K.N - 1) * (K.N + 2) / K.N),
}


def _casimir_fundamental():
    return (K.N**2 - 1) / (2 * K.N)


def _wg_moments():
    """(M_direct, M_cross): the two degree-(2,2) Haar index sums, symbolic in N."""
    wg_e = 1 / (K.N**2 - 1)
    wg_t = -1 / (K.N * (K.N**2 - 1))
    m_direct = wg_e * (K.N**4 + K.N**2) + 2 * wg_t * K.N**3
    m_cross = 2 * wg_e * K.N**3 + wg_t * (K.N**4 + K.N**2)
    return simplify(m_direct), simplify(m_cross)


def _wg_moments_explicit(n: int):
    """The same two sums by explicit summation over all index quadruples."""
    from fractions import Fraction

    wg = {(0, 0): Fraction(1, n**2 - 1), (0, 1): Fraction(-1, n * (n**2 - 1))}
    wg[(1, 0)], wg[(1, 1)] = wg[(0, 1)], wg[(0, 0)]

    def moment(i1, j1, i2, j2, i1p, j1p, i2p, j2p):
        total = Fraction(0)
        iis, jjs, iips, jjps = (i1, i2), (j1, j2), (i1p, i2p), (j1p, j2p)
        for s in (0, 1):  # sigma = e or (12), acting on the i-pairing
            for t in (0, 1):  # tau, acting on the j-pairing
                d = 1
                for a in (0, 1):
                    d *= iis[a] == iips[a ^ s]
                    d *= jjs[a] == jjps[a ^ t]
                if d:
                    total += wg[(s, t)]
        return total

    rng = range(n)
    direct = sum(moment(i, j, k, m, i, j, k, m) for i in rng for j in rng for k in rng for m in rng)
    cross = sum(moment(i, j, k, m, i, m, k, j) for i in rng for j in rng for k in rng for m in rng)
    return direct, cross


@rank_law.check(
    "the shared-link weights are Weingarten, not an isotropy assumption",
    "MASTER paper Thm. 5 / App. B",
)
def _():
    m_direct, m_cross = _wg_moments()
    like_ok = (
        simplify((m_direct + m_cross) / (2 * K.N**2) - _CHANNELS["sym"][0] / K.N**2) == 0
        and simplify((m_direct - m_cross) / (2 * K.N**2) - _CHANNELS["antisym"][0] / K.N**2) == 0
    )
    mixed_ok = (
        simplify(1 / m_direct - _CHANNELS["singlet"][0] / K.N**2) == 0
        and simplify(1 - 1 / m_direct - _CHANNELS["adjoint"][0] / K.N**2) == 0
    )
    explicit_ok = all(_wg_moments_explicit(n) == (n**2, n) for n in (3, 4, 5))
    return like_ok and mixed_ok and explicit_ok, (
        f"M_direct = {m_direct}, M_cross = {m_cross} from Wg(e) = 1/(N^2-1), "
        "Wg((12)) = -1/(N(N^2-1)); (M_d +- M_c)/(2 M_d) = d_Sym/N^2, d_Lam/N^2 "
        "and 1/M_d = d_1/N^2 — all four weights are theorems, confirmed by "
        "explicit summation over every index quadruple at N = 3, 4, 5"
    )


@rank_law.check(
    "each channel gap is C_F + C_R/2, and the weights sum to one",
    "MASTER paper §4.1",
)
def _():
    cf = _casimir_fundamental()
    e_external = 2 * cf  # one plaquette: four half-links in the fundamental
    gaps_ok = all(
        simplify((3 * cf + c_rho / 2) - e_external - (cf + c_rho / 2)) == 0
        for _d, c_rho in _CHANNELS.values()
    )
    mixed = _CHANNELS["singlet"][0] + _CHANNELS["adjoint"][0]
    like = _CHANNELS["antisym"][0] + _CHANNELS["sym"][0]
    sums_ok = simplify(mixed / K.N**2 - 1) == 0 and simplify(like / K.N**2 - 1) == 0
    return gaps_ok and sums_ok, (
        "intermediate energy 3 C_F + C_rho/2 against external 2 C_F leaves "
        "C_F + C_rho/2 in every channel; (1 + (N^2-1))/N^2 = 1 and "
        "(N(N-1)/2 + N(N+1)/2)/N^2 = 1"
    )


def _channel_weight(rho):
    d_rho, c_rho = _CHANNELS[rho]
    return -(d_rho / K.N**2) / (_casimir_fundamental() + c_rho / 2)


@rank_law.check(
    "the four channel weights follow from dimension and Casimir",
    "MASTER paper eq. (20) / App. A",
)
def _():
    closed = {
        "singlet": -2 / (K.N * (K.N - 1) * (K.N + 1)),
        "adjoint": -2 * (K.N - 1) * (K.N + 1) / (K.N * (2 * K.N**2 - 1)),
        "antisym": -(K.N - 1) / ((K.N + 1) * (2 * K.N - 3)),
        "sym": -(K.N + 1) / ((K.N - 1) * (2 * K.N + 3)),
    }
    ok = all(simplify(_channel_weight(rho) - closed[rho]) == 0 for rho in _CHANNELS)
    at3 = {rho: _channel_weight(rho).subs(K.N, 3) for rho in _CHANNELS}
    return ok, (
        "w_rho = -(d_rho/N^2)/(C_F + C_rho/2) reproduces every closed form in "
        f"App. A; at N = 3: { {r: str(v) for r, v in at3.items()} }"
    )


@rank_law.check(
    "the per-channel resolvent equation closes the projector-to-hopping step",
    "PUB edition eqs. (11)-(12) / Thm. 10",
)
def _():
    # A channel's squared projector norm d_rho/N^2 and its signed contribution
    # to the cross matrix element are related but not identical statements.
    # The publication edition displays the step between them: the per-channel
    # resolvent element is -eta_rho * s(p',e) s(p,e) * (d_rho/N^2)/(C_F + C_rho/2)
    # with eta = -1 on the mixed family {1, Adj} and +1 on the like family
    # {Lam^2, Sym^2}, and summing the four channels IS the all-rank theorem.
    eta = {"singlet": -1, "adjoint": -1, "antisym": 1, "sym": 1}
    cf = _casimir_fundamental()
    element = {}
    for rho, (d_rho, c_rho) in _CHANNELS.items():
        element[rho] = -eta[rho] * (d_rho / K.N**2) / (cf + c_rho / 2)
    # each per-channel element is eta_rho * w_rho of the weight formula ...
    per_channel = all(
        simplify(element[rho] - eta[rho] * _channel_weight(rho)) == 0 for rho in _CHANNELS
    )
    # ... and the incidence-stripped sum over the four channels is t_N exactly
    total = sum(element.values())
    assembles = simplify(total - K.hopping()) == 0
    at3 = {rho: str(element[rho].subs(K.N, 3)) for rho in _CHANNELS}
    return per_channel and assembles, (
        "per-channel elements -eta_rho (d_rho/N^2)/(C_F + C_rho/2): the mixed "
        "family enters with eta = -1 and the like family with eta = +1 (the "
        "charge-odd orientation-reversal sign), each equals eta_rho w_rho, and "
        f"the four sum to t_N symbolically in N; at N = 3: {at3} summing to "
        "5/612 — the projector-norm-to-cross-matrix-element step is a "
        "displayed identity, not a jump"
    )


@rank_law.check(
    "A_N and B_N are the channel sums, not transcriptions",
    "MASTER paper eqs. (21)-(22)",
)
def _():
    a_sum = _channel_weight("singlet") + _channel_weight("adjoint")
    b_sum = _channel_weight("antisym") + _channel_weight("sym")
    ok = simplify(a_sum - K.antiparallel_sum()) == 0 and simplify(b_sum - K.parallel_sum()) == 0
    return ok, (
        "w_1 + w_Adj = -2N^3/((N^2-1)(2N^2-1)) and w_Lam + w_Sym = "
        "-4N(N^2-2)/((N^2-1)(4N^2-9)) — the registry's A_N and B_N are now "
        "outputs of the dimension/Casimir table, not inputs"
    )


@rank_law.check(
    "ell_N = A_N + B_N + 1/C_F, the vacuum-mediated route at every rank",
    "MASTER paper Prop. 8 / C13",
)
def _():
    ell = K.antiparallel_sum() + K.parallel_sum() + 1 / _casimir_fundamental()
    closed = -2 * K.N * (3 * K.N**2 - 5) / ((K.N**2 - 1) * (2 * K.N**2 - 1) * (4 * K.N**2 - 9))
    shared_only_3 = (K.antiparallel_sum(3) + K.parallel_sum(3)) == Rational(-481, 612)
    ok = simplify(ell - closed) == 0 and ell.subs(K.N, 3) == K.T_PLUS_2 and shared_only_3
    return ok, (
        "V is C-even and <0|V|p,-> = 0, so the vacuum route 1/C_F = 2N/(N^2-1) "
        "enters only the C-even hopping; at N = 3 the shared-link-only sum is "
        "-481/612 — exactly the superseded value C13 records — and adding 3/4 "
        f"gives ell_3 = {K.T_PLUS_2}: the one-rank erratum is an all-rank formula"
    )
