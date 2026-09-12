"""Exact local Wilson class spectra over Q(N), using a polynomial shell resolvent.

The formal recurrence and source convention are in
docs/derivations/local-class-wick-spectrum.md. No rank interpolation, matrix
Gram inversion, compact-group remainder or continuum identification is used.
The rational-function field backend keeps native full replay inexpensive.
"""

from __future__ import annotations

from functools import lru_cache
from math import factorial

import sympy as s
from sympy.polys.fields import FracElement, field

FIELD, N = field("N", s.QQ)
Poly = dict[tuple[int, ...], FracElement]


def clean(p: Poly) -> Poly:
    return {m: c for m, c in p.items() if c}


def add(*ps: Poly) -> Poly:
    out: Poly = {}
    for p in ps:
        for m, c in p.items():
            out[m] = out.get(m, 0) + c
    return clean(out)


def scale(p: Poly, c) -> Poly:
    return clean({m: c * v for m, v in p.items()})


def monomial(ds, c=1) -> Poly:
    ds = tuple(ds)
    if 1 in ds:
        return {}
    return {tuple(sorted(d for d in ds if d > 1)): FIELD(c) * N ** ds.count(0)}


def mul(p: Poly, q: Poly) -> Poly:
    out: Poly = {}
    for m, c in p.items():
        for n, d in q.items():
            key = tuple(sorted(m + n))
            out[key] = out.get(key, 0) + c * d
    return clean(out)


@lru_cache(None)
def lower_monomial(m: tuple[int, ...]) -> Poly:
    """D=Delta/2 on traces for Tr(T_a T_b)=delta_ab, P0=N, P1=0."""
    terms = []
    for i, k in enumerate(m):
        rest = m[:i] + m[i + 1 :]
        for ell in range(k - 1):
            terms.append(monomial(rest + (ell, k - 2 - ell), s.Rational(k, 2)))
        terms.append(monomial(rest + (k - 2,), -s.Rational(k * (k - 1), 2) / N))
        for j in range(i + 1, len(m)):
            ell = m[j]
            rest2 = m[:i] + m[i + 1 : j] + m[j + 1 :]
            terms.append(monomial(rest2 + (k + ell - 2,), k * ell))
            terms.append(monomial(rest2 + (k - 1, ell - 1), -k * ell / N))
    return add(*terms)


def lower(p: Poly) -> Poly:
    return add(*(scale(lower_monomial(m), c) for m, c in p.items()))


def number(p: Poly) -> Poly:
    return add({m: sum(m) * c for m, c in p.items()}, scale(lower(p), -1))


def heat(p: Poly, sign: int) -> Poly:
    """exp(sign D/2), a terminating polynomial operation."""
    out, term, k = p, p, 0
    while term:
        k += 1
        term = scale(lower(term), s.Rational(sign, 2 * k))
        out = add(out, term)
    return out


@lru_cache(None)
def moment(m: tuple[int, ...]):
    if not m:
        return FIELD.one
    degree = sum(m)
    if degree % 2:
        return FIELD.zero
    # Stationarity E[(Euler-D)p]=0, proved by Gaussian integration by parts.
    return sum((c * moment(k) for k, c in lower_monomial(m).items()), FIELD.zero) / degree


def inner(p: Poly, q: Poly):
    return sum((c * moment(m) for m, c in mul(p, q).items()), FIELD.zero)


def shell(p: Poly, degree: int) -> Poly:
    h = heat(p, 1)
    return heat({m: c for m, c in h.items() if sum(m) == degree}, -1)


def resolvent(p: Poly, degree: int) -> Poly:
    h = heat(p, 1)
    return heat({m: c / (degree - sum(m)) for m, c in h.items() if sum(m) != degree}, -1)


def perturbation(j: int) -> Poly:
    return monomial((2 * j + 2,), s.Rational((-1) ** j, 2**j * factorial(2 * j + 2)))


@lru_cache(None)
def eigen_series(degree: int, order: int):
    """Derive one simple formal branch; verify every polynomial residual."""
    if degree not in (0, 2, 3) or order < 0:
        raise ValueError("Use shells 0, 2 or 3 and a nonnegative order")
    psi0 = heat(monomial((degree,)) if degree else {(): FIELD.one}, -1)
    norm = inner(psi0, psi0)
    _require(norm != 0, "nonzero generic norm")
    _require(not add(number(psi0), scale(psi0, -degree)), "initial eigen-equation")
    states, energies, checks = [psi0], [FIELD(degree)], []
    for n in range(1, order + 1):
        forcing = add(*(mul(perturbation(j), states[n - j]) for j in range(1, n + 1)))
        energy = inner(psi0, forcing) / norm
        energies.append(energy)
        rhs = add(forcing, *(scale(states[n - j], -energies[j]) for j in range(1, n + 1)))
        obstruction = shell(rhs, degree)
        _require(not obstruction, f"resonant shell {degree}, order {n}")
        # The last state is unnecessary to compute E_order, but retaining it
        # gives a coefficient-level residual certificate for every order.
        state = resolvent(rhs, degree)
        _require(inner(psi0, state) == 0, f"normalization {degree}, order {n}")
        _require(
            not add(scale(state, degree), scale(number(state), -1), scale(rhs, -1)),
            f"residual {degree}, order {n}",
        )
        states.append(state)
        checks.append(
            {
                "order": n,
                "residual_zero": True,
                "normalization_zero": True,
                "resonant_shell_zero": True,
                "state_terms": len(state),
            }
        )
    return tuple(s.factor(e.as_expr()) for e in energies), tuple(checks)


def _require(condition, description):
    if not condition:
        raise ArithmeticError(description)


@lru_cache(None)
def gap_series(parity: str, order: int = 5) -> tuple[s.Expr, ...]:
    """Return coefficients of g*Delta, g=sqrt(2N/beta), from the recurrence."""
    if parity not in ("even", "odd"):
        raise ValueError("parity must be even or odd")
    degree = 2 if parity == "even" else 3
    vacuum, _ = eigen_series(0, order)
    excited, _ = eigen_series(degree, order)
    return tuple(s.factor(a - b) for a, b in zip(excited, vacuum, strict=True))


def beta_coefficients(parity: str, order: int = 5) -> tuple[s.Expr, ...]:
    """Return c0 through c_(order-1); formal fixed-rank local coefficients."""
    rank = N.as_expr()
    return tuple(
        s.factor((2 * rank) ** s.Rational(j - 1, 2) * a)
        for j, a in enumerate(gap_series(parity, order))
        if j
    )
