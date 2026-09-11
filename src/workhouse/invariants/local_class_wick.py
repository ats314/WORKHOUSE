"""Exact formal local spectra; full analytic eigenvalue remainders stay separate."""

from __future__ import annotations

import contextlib
import io
import json
import types
from functools import lru_cache
from pathlib import Path

import sympy as sp

from workhouse import local_class_wick as wick

from ._core import _suite

suite = _suite("local class Wick spectrum over all ranks")
CITE = "LOCAL_CLASS_WICK_SPECTRUM"
ROOT = Path(__file__).resolve().parents[3]
RECEIVED = ROOT / "runs/local_class_wick_2026-09-11/received"
RANK = wick.N.as_expr()
RECURRENCE = "local class Wick recurrence has zero polynomial residuals through order five"
COEFFICIENTS = "local class Wick coefficients reproduce the retained all-rank certificate"
SIGNS = "local class Wick corrections c0 through c4 are negative at every allowed rank"
QUOTIENT = "local class Wick small-rank trace quotient and SU2 odd exclusion"
CARTESIAN = "local class Wick independent Cartesian SU3 and SU2 expansions through order five"


@suite.check(RECURRENCE, CITE + " section 3")
def check_recurrence():
    rows = [row for degree in (0, 2, 3) for row in wick.eigen_series(degree, 5)[1]]
    fields = ("residual_zero", "normalization_zero", "resonant_shell_zero")
    passed = len(rows) == 15 and all(row[field] for row in rows for field in fields)
    return passed, (
        "45 polynomial identities over Q(N), with the complete order-five state in each "
        "of shells 0,2,3. Finite formal recurrence; no all-order convergence/remainder claim."
    )


@suite.check(COEFFICIENTS, CITE + " sections 4-4.1", rests_on=(RECURRENCE,))
def check_coefficients():
    received = json.loads((RECEIVED / "coefficients_order5.json").read_text())
    passed = True
    for parity in ("even", "odd"):
        expected = tuple(
            sp.sympify(value, locals={"N": RANK}) for value in received["gaps"][parity]["g_series"]
        )
        passed &= all(
            sp.cancel(actual - prior) == 0
            for actual, prior in zip(wick.gap_series(parity), expected, strict=True)
        )
    return (
        passed,
        "Both complete symbolic gap series match the independent original engine through beta^-2; "
        "c3- and c4+/- retain exact rank formulas. "
        "Prior c0,c1,c2,c3+ and SU3 c4 anchors are recovered.",
        {
            "LOCAL_CLASS_C3_ODD_SU3_RADICAL_FACTOR": sp.factor(
                6 * wick.gap_series("odd")[4].subs(RANK, 3)
            ),
            "LOCAL_CLASS_C4_EVEN_SU3": wick.beta_coefficients("even")[4].subs(RANK, 3),
            "LOCAL_CLASS_C4_ODD_SU3": wick.beta_coefficients("odd")[4].subs(RANK, 3),
        },
    )


def sign_witness(parity: str, coefficient: sp.Expr) -> tuple[sp.Expr, ...]:
    """Positive numerator coefficients after z=N^2 is shifted by its minimum."""
    numerator, denominator = sp.fraction(sp.factor(-coefficient))
    denom = sp.Poly(denominator, RANK)
    if denom.length() != 1 or denom.LC() <= 0:
        raise ArithmeticError("expected a strictly positive monomial denominator")
    poly = sp.Poly(numerator, RANK)
    if any(power[0] % 2 for power, _ in poly.terms()):
        raise ArithmeticError("expected an even numerator")
    z = sp.Symbol("z")
    in_z = sum(value * z ** (power[0] // 2) for power, value in poly.terms())
    return tuple(sp.Poly(in_z.subs(z, z + (4 if parity == "even" else 9)), z).all_coeffs())


@suite.check(SIGNS, CITE + " section 4.2", rests_on=(COEFFICIENTS,))
def check_signs():
    witnesses = [
        sign_witness(parity, coef)
        for parity in ("even", "odd")
        for coef in wick.gap_series(parity)[1:]
    ]
    return all(c > 0 for row in witnesses for c in row), (
        "Ten strictly positive shifted numerator polynomials: z=N^2=x+4 (even), x+9 (odd). "
        "Hence c0..c4<0 for N>=2 even and N>=3 odd. This is a coefficient-sign theorem."
    )


@suite.check(QUOTIENT, CITE + " sections 1-2")
def check_quotient():
    relation = wick.add(wick.monomial((4,)), wick.monomial((2, 2), -sp.S.Half))
    derivative = wick.lower(relation)
    odd_norm = wick.moment((3, 3)).as_expr()
    even = wick.heat(wick.monomial((2,)), -1)
    passed = (
        all(coef.as_expr().subs(RANK, 3) == 0 for coef in derivative.values())
        and wick.inner(relation, relation).as_expr().subs(RANK, 3) == 0
        and odd_norm.subs(RANK, 2) == 0
        and wick.inner(even, even).as_expr().subs(RANK, 2) == sp.Rational(3, 2)
    )
    return passed, (
        "SU3 P4=P2^2/2 has zero Gaussian norm and its Laplacian vanishes; "
        "SU2 P3 has zero norm while the centered P2 norm is 3/2. No spurious SU2 odd branch."
    )


@lru_cache(None)
def cartesian_gaps(rank: int, order: int = 5) -> dict[str, tuple[sp.Expr, ...]]:
    """Execute the pinned independent Cartesian Laplacian, not the trace engine."""
    if rank not in (2, 3):
        raise ValueError("Cartesian oracle is implemented for ranks 2 and 3")
    path = RECEIVED / "independent_su3.py"
    # The source is pinned evidence. Compile in memory so loading it never
    # creates bytecode files inside the received run directory.
    module = types.ModuleType("local_class_cartesian")
    module.__file__ = str(path)
    exec(compile(path.read_bytes(), str(path), "exec"), module.__dict__)
    x, y = module.x, module.y
    if rank == 3:
        delta = x * (x * x - 3 * y * y)
        seeds = (delta, delta * (x * x + y * y), delta * y * (3 * x * x - y * y))
    else:
        module.trace_even = lambda k: sp.Rational(1, 2 ** (k // 2 - 1)) * x**k
        seeds = (x, x**3)
    with contextlib.redirect_stdout(io.StringIO()):
        series = [module.solve(seed, order) for seed in seeds]
    return {
        parity: tuple(sp.factor(a - b) for a, b in zip(values, series[0], strict=True))
        for parity, values in zip(("even", "odd"), series[1:], strict=False)
    }


@suite.check(CARTESIAN, CITE + " section 5", rests_on=(COEFFICIENTS,))
def check_cartesian():
    passed = all(
        values == tuple(c.subs(RANK, rank) for c in wick.gap_series(parity))
        for rank in (2, 3)
        for parity, values in cartesian_gaps(rank).items()
    )
    return passed, (
        "Independent Cartesian differentiation and elementary Gaussian monomial integrals "
        "agree for all six coefficients of SU3 even/odd and SU2 even. Exact fixed-rank controls."
    )
