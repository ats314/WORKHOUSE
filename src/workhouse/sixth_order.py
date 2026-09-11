"""Exact sixth-order folds and carrier reduction; no inferred Wilson weights.

Electric words use D=Q/(E0-H0), P and V, after shifting V_original by
its first-order scalar aI if P V_original P=aP. Hodge words use S,U,R.
These alphabets are deliberately distinct: a lattice walk is neither one.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction as F
from functools import cache

import sympy as sp

from . import kernel_orbits as KO


def _normal(word):
    out = []
    for letter in word:
        if out and {out[-1], letter} == {"P", "D"}:
            return None
        if out and out[-1] == letter == "P":
            continue
        out.append(letter)
        if out[-3:] == ["P", "V", "P"]:
            return None
    return tuple(out)


def add(*terms):
    out = defaultdict(F)
    for scale, expr in terms:
        for word, value in expr.items():
            out[word] += scale * value
    return {word: value for word, value in out.items() if value}


def mul(left, right):
    out = defaultdict(F)
    for a, x in left.items():
        for b, y in right.items():
            word = _normal(a + b)
            if word is not None:
                out[word] += x * y
    return {word: value for word, value in out.items() if value}


def adjoint(expr):
    return {tuple(reversed(word)): value for word, value in expr.items()}


def _series_mul(a, b, order):
    return [add(*[(1, mul(a[j], b[n - j])) for j in range(n + 1)]) for n in range(order + 1)]


def _series_power(metric, exponent, order):
    unit = [{("P",): F(1)}] + [{} for _ in range(order)]
    perturbation = [dict(item) for item in metric]
    perturbation[0] = {}
    total, power = unit, unit
    for k in range(1, order + 1):
        power = _series_mul(power, perturbation, order)
        c = F(sp.binomial(exponent, k))
        total = [add((1, x), (c, y)) for x, y in zip(total, power, strict=True)]
    return total


@cache
def folded_series(order=6):
    """Bloch recursion and canonical Hermitian metric, with PVP=0.

    chi_n = D V chi_(n-1) - D sum_(j=1..n-1) chi_(n-j) H_j,
    H_n = P V chi_(n-1), chi_0=P. H_odd is NOT dropped.
    Hermitian H = (P+chi*chi)^1/2 H_B (P+chi*chi)^-1/2.
    This generates every formal fold, but evaluates no electric/Haar matrix.
    """
    p, d, v = ({(letter,): F(1)} for letter in "PDV")
    chi, bloch = [p], [{}]
    for n in range(1, order + 1):
        bloch.append(mul(mul(p, v), chi[n - 1]))
        correction = add(*[(1, mul(chi[n - j], bloch[j])) for j in range(1, n)])
        chi.append(add((1, mul(mul(d, v), chi[n - 1])), (-1, mul(d, correction))))
    metric = [p] + [
        add(*[(1, mul(adjoint(chi[j]), chi[n - j])) for j in range(1, n)])
        for n in range(1, order + 1)
    ]
    sqrt = _series_power(metric, sp.Rational(1, 2), order)
    invsqrt = _series_power(metric, sp.Rational(-1, 2), order)
    hermitian = _series_mul(_series_mul(sqrt, bloch, order), invsqrt, order)
    normalized_wave = _series_mul(chi, invsqrt, order)
    return {"bloch": bloch, "hermitian": hermitian, "wave": normalized_wave, "metric": metric}


def evaluate_words(expr, matrices):
    n = matrices["P"].rows
    result = sp.zeros(n)
    for word, coefficient in expr.items():
        term = sp.eye(n)
        for letter in word:
            term = term * matrices[letter]
        result += sp.Rational(coefficient) * term
    return result


Q, E2, E3 = sp.symbols("q e2 e3")


@cache
def carrier_word(word):
    """Compute sigma(word) in Q[q,e2,e3], including the empty word.

    In the polynomial carrier gauge U_ij=a_j, R=diag(a)-U,
    S=(q-4)I-U, psi=1 and the left carrier is a^T.
    The result is also checked against the spatial Laurent implementation.
    """
    if set(word) - set("SUR"):
        raise ValueError("Hodge words contain only S,U,R")
    a = sp.symbols("a1:4")
    up = sp.ones(3, 1) * sp.Matrix([a])
    gens = {"U": up, "S": (sum(a) - 4) * sp.eye(3) - up, "R": sp.diag(*a) - up}
    vector = sp.ones(3, 1)
    for letter in reversed(word):
        vector = (gens[letter] * vector).applyfunc(sp.expand)
    value = sp.expand((sp.Matrix([a]) * vector)[0])
    symmetric, remainder, mapping = sp.symmetrize(value, a, formal=True)
    if remainder != 0:
        raise ValueError(f"non-symmetric carrier word: {word}")
    return sp.expand(symmetric.subs(dict(zip((x[0] for x in mapping), (Q, E2, E3), strict=True))))


def reduce_support(support):
    """Combine supplied weighted words BEFORE testing shape membership.

    Does not assert these supplied coefficients are physical dynamics.
    """
    coefficients = {word: sp.sympify(c) for word, c in support.items()}
    if any(c.has(sp.Float) for c in coefficients.values()):
        raise TypeError("Exact word reduction refuses floating-point coefficients")
    return sp.factor(sum(c * carrier_word(w) for w, c in coefficients.items()))


def as_laurent(poly):
    """Convert a polynomial in q,e2,e3 to the exact spatial Laurent ring."""
    result = {}
    for powers, coeff in sp.Poly(poly, Q, E2, E3).terms():
        term = {(0, 0, 0): F(coeff)}
        for base, power in zip((KO.E1, KO.E2, KO.E3), powers, strict=True):
            for _ in range(power):
                term = KO._mul(term, base)
        result = KO._add(result, term)
    return result


def h4_support():
    from .invariants.gamma_isolation import _forms

    form = _forms()["assembled"]
    return {
        "": 2 * form["nu~"] + form["sigma~"],
        "U": -form["nu~"],
        "S": -form["pi~"],
        "SS": form["u"],
        "R": -2 * form["C"],
    }


def mixing_terms():
    """All 25 H4-Q-H4 pairs, with q^3 cleared from lambda_6."""
    t = sp.Rational(5, 612)
    support = h4_support()
    return {
        (a, b): sp.expand(
            -sp.Rational(ca * cb)
            / t
            * (Q * carrier_word(a + b) - carrier_word(a) * carrier_word(b))
        )
        for a, ca in support.items()
        for b, cb in support.items()
    }


def combination_report(direct_support=None):
    """Exact known mixing and conditional direct assembly, with unknown explicit."""
    mixing = sp.factor(sum(mixing_terms().values()))
    direct = None if direct_support is None else reduce_support(direct_support)
    numerator = None if direct is None else sp.expand(Q**2 * direct + mixing)
    return {
        "direct_h6_supplied": direct is not None,
        "direct_sigma": None if direct is None else str(direct),
        "mixing_q3_cleared": str(mixing),
        "combined_q3_cleared": None if numerator is None else str(numerator),
        "unavoidable_remainder_mod_q": str(sp.expand(mixing).subs(Q, 0)),
        "symmetric_remainder_mod_q2": str(sp.rem(sp.expand(mixing), Q**2, Q)),
        "direct_word_support_status": "unknown"
        if direct is None
        else "caller-supplied; provenance required",
        "physical_qe2_e3_coefficients": "not determined by the census or the mixing calculation",
    }


def single_plaquette_series(order=6, odd=True):
    """Actual SU(3) one-face character Hamiltonian and all scalar folds.

    H0 chi_(p,q)=2 C2(p,q) chi_(p,q), V=-(chi_3+chi_3bar).
    Haar-orthonormal irreducible characters implement the exact Gram quotient.
    Odd basis (chi_(p,q)-chi_(q,p))/sqrt(2), p>q; vacuum uses all characters.
    Dynamic support is generated by the SU(3) fundamental fusion rule.
    """
    target = (1, 0) if odd else (0, 0)

    def energy(rep):
        p, q = rep
        return F(2 * (p * p + p * q + q * q + 3 * p + 3 * q), 3)

    def interaction(vector):
        out = defaultdict(F)
        for (p, q), c in vector.items():
            for r, s in (
                (p + 1, q),
                (p - 1, q + 1),
                (p, q - 1),
                (p, q + 1),
                (p + 1, q - 1),
                (p - 1, q),
            ):
                if min(r, s) < 0 or (odd and r == s):
                    continue
                if odd and r < s:
                    out[(s, r)] += c
                else:
                    out[(r, s)] -= c
        return {rep: c for rep, c in out.items() if c}

    e0 = energy(target)
    vectors, energies = [{target: F(1)}], [e0]
    supports = []
    for n in range(1, order + 1):
        rhs = interaction(vectors[n - 1])
        energies.append(rhs.get(target, F(0)))
        for j in range(1, n + 1):
            for rep, c in vectors[n - j].items():
                rhs[rep] = rhs.get(rep, F(0)) - energies[j] * c
        assert rhs.get(target, F(0)) == 0
        vector = {}
        for rep, c in rhs.items():
            if rep != target and c:
                if e0 == energy(rep):
                    raise ValueError(f"unprojected electric degeneracy: {rep}")
                vector[rep] = c / (e0 - energy(rep))
        vectors.append(vector)
        supports.append(sorted(vector))
    return {"energies": energies, "supports": supports, "vectors": vectors}
