"""Exact controls for review-derived Q4 and multichannel rate theorems."""

from dataclasses import dataclass

from sympy import Matrix, Rational, simplify, symbols, sympify

from .. import constants as K
from ._core import _suite

spectral_budgets = _suite("Review-derived coercivity and multichannel spectral budgets")
SOURCE = "REVIEW_SPECTRAL_BUDGETS"


def _q(value):
    value = sympify(value)
    if value.is_Rational is not True:
        raise ValueError("Require exact rational inputs")
    return value


@dataclass(frozen=True)
class MultichannelBudget:
    """Zero rate means no positive guarantee; no Wilson input is inferred."""

    rate: object
    raw_rate: object
    time_coefficient: object
    pair_rates: tuple
    horizon_rate: object


def multichannel_budget(decays, errors, s, horizon=None):
    """Optimize finite raw terms (p,m) and (r,ell), with P>0 and R>0."""
    s = _q(s)
    decays = tuple(tuple(map(_q, row)) for row in decays)
    errors = tuple(tuple(map(_q, row)) for row in errors)
    if not decays or not errors or s < 0:
        raise ValueError("Require nonempty families and s>=0")
    if any(len(row) != 2 for row in (*decays, *errors)):
        raise ValueError("Each channel has two parameters")
    if any(p < 0 or m <= 0 or p + 2 * s <= 0 for p, m in decays):
        raise ValueError("Require p>=0, m>0 and p+2s>0")
    if any(r - 2 * s <= 0 or ell < 0 for r, ell in errors):
        raise ValueError("Require r-2s>0 and ell>=0")
    pairs = tuple(
        ((r - 2 * s) * m - (p + 2 * s) * ell) / (p + r) for p, m in decays for r, ell in errors
    )
    horizon_rate = None
    raw = min(pairs)
    if horizon is not None:
        horizon = _q(horizon)
        if horizon <= 0:
            raise ValueError("Require a positive physical horizon")
        horizon_rate = min(m - (p + 2 * s) / horizon for p, m in decays)
        raw = min(raw, horizon_rate)
    rate = max(Rational(0), raw)
    c = max((p + 2 * s) / (m - rate) for p, m in decays) if rate > 0 else None
    return MultichannelBudget(rate, raw, c, pairs, horizon_rate)


@spectral_budgets.check(
    "assembled Q4 has the corrected sharp coercivity and sum of squares",
    f"{SOURCE} Q1-Q2",
)
def _():
    a = K.A_SHP_3
    c = K.C_SHP_HISTORICAL + Rational(25, 1024)
    b = 2 * a + 4 * c
    d, e = a - b / 2, b / 2
    x = Matrix(symbols("x:3", real=True))
    mat = Matrix(3, 3, lambda i, j: a if i == j else b / 2)
    identity = simplify((x.T * mat * x)[0] - d * x.dot(x) - e * sum(x) ** 2)
    ok = (
        c == K.C_SHP_CONTINUATION_SHIFTED
        and b - K.Q4_CROSS == Rational(25, 256)
        and identity == 0
        and d > 0
        and e > 0
        and mat.eigenvals() == {d: 2, a + b: 1}
    )
    return (
        ok,
        f"C={c}; b={b}; exact SOS d={d}, e={e}; eigenvalues {mat.eigenvals()}",
        {
            "Q4_ASSEMBLED_CROSS": b,
            "Q4_ASSEMBLED_COERCIVITY": d,
        },
    )


@spectral_budgets.check(
    "multichannel target intervals yield every sharp pairwise rate",
    f"{SOURCE} M1-M6",
)
def _():
    p, r, s, m, ell, energy = symbols("p r s m ell energy", real=True)
    P, R = p + 2 * s, r - 2 * s
    rate = (R * m - P * ell) / (P + R)
    numerator = simplify(R * (m - energy) - P * (energy + ell))
    ok = simplify(numerator - (P + R) * (rate - energy)) == 0
    c = P / (m - rate)
    ok = ok and simplify(c - R / (rate + ell)) == 0
    ok = ok and simplify(rate.subs(ell, 0) - m * (r - 2 * s) / (p + r)) == 0
    return ok, (
        "Cross-multiplication gives (P+R)(M_jl-E); lower and upper time "
        "endpoints coincide at the pair rate. ell=0 recovers MT4. "
        "Positive-denominator and limiting arguments are analytic."
    )


@spectral_budgets.check(
    "multichannel optimum respects all errors and the physical horizon",
    f"{SOURCE} M2",
)
def _():
    decays, errors = [(1, 2), (3, 4)], [(5, 0), (8, 1)]
    full = multichannel_budget(decays, errors, 1)
    short = multichannel_budget(decays, errors, 1, 2)
    amplified = multichannel_budget([(1, 2)], [(5, 1)], 1)
    zero = multichannel_budget([(1, 2)], [(5, 2)], 1)
    ok = (
        full.rate == 1
        and full.time_coefficient == 3
        and short.rate == Rational(1, 2)
        and short.time_coefficient == 2
        and amplified.rate == Rational(1, 2)
        and zero.rate == 0
        and multichannel_budget(decays, errors, 1, Rational(3, 2)).rate == 0
    )
    return ok, (
        f"Pair rates={full.pair_rates}; full (M,c)=(1,3), horizon 2 gives "
        "(1/2,2). A growing remainder halves the single-channel rate; "
        "ell=2 and the minimum horizon admit no positive guarantee."
    )


@spectral_budgets.check(
    "multichannel sharpness retains the exact one-atom and horizon exponents",
    f"{SOURCE} M3",
)
def _():
    p, r, s, m, ell, h = symbols("p r s m ell h", positive=True)
    P, R = p + 2 * s, r - 2 * s
    theta = R / (P + R)
    rate = (R * m - P * ell) / (P + R)
    ok = (
        simplify(-p * theta + r * (1 - theta) - 2 * s) == 0
        and simplify(m * theta - ell * (1 - theta) - rate) == 0
        and simplify((m - (m - P / h)) * h - P) == 0
    )
    for n in range(1, 17):
        a = Rational(1, 2) ** (2 * n)
        # p=1,r=5,s=1,m=2,ell=1,c=2: M=1/2, X=Y=a^3.
        X, Y, raw = a**-1 * a**4, a**5 / a**2, a**2 * a
        ok = ok and X == Y == raw and raw <= X + Y
    return ok, (
        "Weighted product cutoff exponent is 2s and energy is M_jl; "
        "16 exact atom examples saturate the exponent with a growing error. "
        "AM-GM, continuum support and arbitrary-family sharpness are analytic."
    )
