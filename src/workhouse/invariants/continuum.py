"""What is exact in the continuum-bridge insert.

The G19 insert merged on 2026-08-30 is mostly analysis, and analysis enters at
T3. Two pieces of it are finite exact computations, and those are checked here
so that G19 has machine-checked content and a graph edge rather than only a
register entry:

* the reflection-positivity counterexample that closes off the stochastic
  blocking route -- a two-point measure, exactly evaluated;
* the two-loop scaling exponents the necessary continuum law is written in,
  which are rational functions of N evaluated at 3;
* one transcription in the G18 internal-sheet closure -- that its symbol
  coefficient 5/612 is the shared-link hopping this repository derives, not a
  near neighbour of it.

Neither makes the continuum bridge less open. They pin the arithmetic the
insert's prose depends on.
"""

from __future__ import annotations

from fractions import Fraction

from sympy import Rational, pi, simplify, symbols

from .. import constants as K
from ._core import _suite

bridge19 = _suite("continuum and fixed-spacing bridges (G18, G19)")

_G19 = "G19; paper/research_notes/G19_CONTINUUM_BRIDGE_INSERT.tex"
_G18 = "G18; paper/research_notes/G18_INTERNAL_BBDAGGER_SHEET_CLOSURE_20260830.tex"


@bridge19.check(
    "the equivariant Markov blocking counterexample is exact: integral = -1",
    _G19,
)
def _():
    # Remark "Equivariant Markov blocking is insufficient". The fine space is
    # one point; the coarse space is X' = {(s_-, s_+) : s_pm = +-1} with
    # reflection (s_-, s_+) -> (s_+, s_-). The law
    #     nu = (1/2) delta_{(+1,-1)} + (1/2) delta_{(-1,+1)}
    # is reflection invariant, and the induced Markov kernel is reflection
    # equivariant and maps every positive-time observable to a fine constant.
    # For F(s_-, s_+) = s_+ the reflected pairing is nevertheless negative, so
    # equivariance plus one-sided mapping do NOT give reflection positivity.
    support = {(1, -1): Fraction(1, 2), (-1, 1): Fraction(1, 2)}

    def theta(point):
        return (point[1], point[0])

    def f(point):  # the positive-time observable
        return point[1]

    invariant = all(support[theta(x)] == w for x, w in support.items())
    pairing = sum(w * f(theta(x)) * f(x) for x, w in support.items())
    # and the same functional is a legitimate positive-time observable: it
    # depends on s_+ alone.
    one_sided = len({f((a, b)) for a in (-1, 1) for b in (-1, 1) if b == 1}) == 1
    ok = invariant and one_sided and pairing == -1 and sum(support.values()) == 1
    return ok, (
        f"nu is reflection invariant ({invariant}) and F depends on s_+ alone ({one_sided}), "
        f"yet integral (Theta F) F dnu = E[s_- s_+] = {pairing} exactly, not >= 0. So the "
        "deterministic Balaban-form result proved in the same section does not extend to a "
        "softened stochastic constraint: equivariance and one-sided mapping are not sufficient "
        "conditions. The sufficient replacement the insert gives is a reflection factorisation, "
        "K((Theta' F) G) = (Theta TF)(TG), which this measure does not admit"
    )


@bridge19.check(
    "the two-loop exponents of the necessary continuum law are 51/121 and 86/121",
    _G19,
)
def _():
    # Conditional result "Necessary continuum scaling of an electric-unit
    # branch" is written with the universal pure-gauge coefficients
    #   b_0 = 11N/(48 pi^2),  b_1 = 34N^2/(3 (16 pi^2)^2),  p = b_1/(2 b_0^2).
    # At N = 3 the pi's cancel out of p entirely, and the essential exponential
    # exp[-sqrt(u)/(2 b_0)] becomes exp[-(8 pi^2/11) sqrt u]. Exact symbolic
    # arithmetic, so the printed exponents are re-derived rather than trusted.
    n = symbols("N", positive=True)
    b0 = 11 * n / (48 * pi**2)
    b1 = 34 * n**2 / (3 * (16 * pi**2) ** 2)
    p_sym = simplify(b1 / (2 * b0**2))
    p3 = simplify(p_sym.subs(n, 3))
    half = simplify((1 + p3) / 2)
    inv_2b0 = simplify(1 / (2 * b0.subs(n, 3)))
    ok = (
        simplify(p_sym - Rational(51, 121)) == 0  # p is N-independent
        and p3 == Rational(51, 121)
        and half == Rational(86, 121)
        and simplify(inv_2b0 - 8 * pi**2 / 11) == 0
    )
    return ok, (
        f"p = b_1/(2 b_0^2) = {p_sym} symbolically -- the N dependence and both powers of pi "
        f"cancel -- so at N = 3, p = {p3} and (1+p)/2 = {half}, the exponent on u in the "
        f"necessary law. And 1/(2 b_0) = {inv_2b0} at N = 3, which is the 8 pi^2/11 in the "
        "essential exponential exp[-(8 pi^2/11) sqrt u]. The scaling law itself stays "
        "conditional on the Hamiltonian-Wilson matching the insert names as the open object; "
        "only its exponents are established here"
    )


@bridge19.check(
    "the G18 sheet coefficient 5/612 is the registered shared-link hopping",
    _G18,
)
def _():
    # The internal-sheet closure proves the exact orthonormal-symbol
    # coefficient [u^2] h_u = sigma_2 I + (5/612) BB^dagger. Nothing else in
    # that insert is a finite exact computation, so this is what G18 can be
    # held to here: the rational it prints is the C-odd shared-link hopping
    # this repository derives from Haar moments, t_N = 2N(N^2-4) /
    # ((N^2-1)(2N^2-1)(4N^2-9)) at N = 3, and not a near neighbour of it.
    #
    # A transcription guard, not a proof of the sheet theorem, which stays T3.
    printed = Fraction(5, 612)
    derived = Fraction(K.hopping(3).p, K.hopping(3).q)
    registered = Fraction(K.T_MINUS_2.p, K.T_MINUS_2.q)
    ok = printed == derived == registered
    return ok, (
        f"the insert prints 5/612; hopping(3) derives {derived} from the rank law and the "
        f"registry records T_MINUS_2 = {registered}. All three agree exactly, so the sheet "
        "coefficient is t_3 and the identification in the merge note is not a coincidence of "
        "decimals. The theorem the coefficient sits inside is analysis and remains T3; this "
        "check guards only the transcription"
    )
