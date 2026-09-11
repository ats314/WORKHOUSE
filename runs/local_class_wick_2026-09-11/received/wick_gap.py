"""Exact formal local Wilson class gaps via traceless Gaussian shell calculus.

All operations use Q(N); no rank interpolation or Gram-matrix inversion.
Run with Python + SymPy: python wick_gap.py --order 4 --out coefficients.json
"""
from __future__ import annotations

import argparse
import json
import time
from functools import lru_cache
from math import factorial
from pathlib import Path

import sympy as s

N = s.Symbol("N", positive=True)
Poly = dict[tuple[int, ...], s.Expr]


def clean(p: Poly) -> Poly:
    return {m: z for m, c in p.items() if (z := s.cancel(c)) != 0}


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
    return {tuple(sorted(d for d in ds if d > 1)): s.sympify(c) * N ** ds.count(0)}


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
        rest = m[:i] + m[i + 1:]
        for ell in range(k - 1):
            terms.append(monomial(rest + (ell, k - 2 - ell), s.Rational(k, 2)))
        terms.append(monomial(rest + (k - 2,), -s.Rational(k * (k - 1), 2) / N))
        for j in range(i + 1, len(m)):
            ell = m[j]
            rest2 = m[:i] + m[i + 1:j] + m[j + 1:]
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
        return s.S.One
    degree = sum(m)
    if degree % 2:
        return s.S.Zero
    # Stationarity E[(Euler-D)p]=0, proved by Gaussian integration by parts.
    return s.cancel(sum(c * moment(k) for k, c in lower_monomial(m).items()) / degree)


def inner(p: Poly, q: Poly):
    return s.factor(sum(c * moment(m) for m, c in mul(p, q).items()))


def shell(p: Poly, degree: int) -> Poly:
    h = heat(p, 1)
    return heat({m: c for m, c in h.items() if sum(m) == degree}, -1)


def resolvent(p: Poly, degree: int) -> Poly:
    h = heat(p, 1)
    return heat({m: c / (degree - sum(m)) for m, c in h.items() if sum(m) != degree}, -1)


def perturbation(j: int) -> Poly:
    return monomial((2 * j + 2,), s.Rational((-1) ** j, 2 ** j * factorial(2 * j + 2)))


def eigen_series(degree: int, order: int):
    psi0 = heat(monomial((degree,)) if degree else {(): s.S.One}, -1)
    norm = inner(psi0, psi0)
    assert norm != 0
    assert not add(number(psi0), scale(psi0, -degree))
    states, energies, checks = [psi0], [s.Integer(degree)], []
    for n in range(1, order + 1):
        started = time.monotonic()
        forcing = add(*(mul(perturbation(j), states[n - j]) for j in range(1, n + 1)))
        energy = s.factor(inner(psi0, forcing) / norm)
        energies.append(energy)
        rhs = add(forcing, *(scale(states[n - j], -energies[j]) for j in range(1, n + 1)))
        obstruction = shell(rhs, degree)
        assert not obstruction, (degree, n, obstruction)
        # The last state is unnecessary to compute E_order, but retaining it
        # gives a coefficient-level residual certificate for every order.
        state = resolvent(rhs, degree)
        assert inner(psi0, state) == 0
        assert not add(scale(state, degree), scale(number(state), -1), scale(rhs, -1))
        states.append(state)
        checks.append({"order": n, "residual_zero": True, "normalization_zero": True,
                       "resonant_shell_zero": True, "state_terms": len(state)})
        print(f"shell={degree} order={n} E={energy} terms={len(state)} seconds={time.monotonic()-started:.2f}", flush=True)
    return energies, checks


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--order", type=int, default=3)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError(args.out)
    result = {"schema": "local-class-wick/v1", "parameter": "g=sqrt(2*N/beta)",
              "scope": "formal local Wilson oscillator series; no remainder or continuum certificate",
              "order": args.order, "energies": {}, "checks": {}, "gaps": {}}
    eigen = {}
    for degree in (0, 2, 3):
        eigen[degree], checks = eigen_series(degree, args.order)
        result["energies"][str(degree)] = [str(e) for e in eigen[degree]]
        result["checks"][str(degree)] = checks
    for degree, parity in ((2, "even"), (3, "odd")):
        gap = [s.factor(eigen[degree][j] - eigen[0][j]) for j in range(args.order + 1)]
        result["gaps"][parity] = {
            "g_series": [str(e) for e in gap],
            "beta_coefficients": [str(s.factor((2*N)**s.Rational(j-1, 2)*gap[j])) for j in range(1, args.order+1)],
            "SU3_g_series": [str(e.subs(N, 3)) for e in gap],
        }
        print(parity, result["gaps"][parity], flush=True)
    args.out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
