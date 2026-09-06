"""Preserved independent exact Fourier controls.

Source: next_covariant_block_sources/check_fourier_alias_independent.py
Original SHA256: 958a72cfcc8be4d7ce765d9469f31e1894f50585f30c52c1b2d34e94766632a2
Finite identities only; all-size source theorem remains analytic.
"""

from __future__ import annotations

import itertools
from collections import Counter
from fractions import Fraction

import sympy as sp


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def exact_zero(value: sp.Expr) -> bool:
    return sp.simplify(value) == 0


def controls() -> dict:
    z = sp.Symbol("z")
    moments = []
    for length in range(1, 13):
        polynomial = sum(z**s for s in range(length)) / length
        require(
            sp.expand((z - 1) * polynomial - (z**length - 1) / length) == 0,
            "cochain phase identity failed",
        )
        second = Counter(s - t for s, t in itertools.product(range(length), repeat=2))
        fourth = Counter(s - t + v - w for s, t, v, w in itertools.product(range(length), repeat=4))
        second_alias = {
            q // length: Fraction(count, length) for q, count in second.items() if q % length == 0
        }
        fourth_alias = {
            q // length: Fraction(count, length**3)
            for q, count in fourth.items()
            if q % length == 0
        }
        expected_fourth = {0: Fraction(2 * length**2 + 1, 3 * length**2)}
        if length > 1:
            expected_fourth[-1] = Fraction(length**2 - 1, 6 * length**2)
            expected_fourth[1] = Fraction(length**2 - 1, 6 * length**2)
        require(second_alias == {0: Fraction(1)}, "second alias moment failed")
        require(fourth_alias == expected_fourth, "fourth alias moment failed")
        variance = sum(
            Fraction((s - t) ** 2, 2 * length**4)
            for s, t in itertools.product(range(length), repeat=2)
        )
        require(
            variance == Fraction(length**2 - 1, 12 * length**2),
            "principal characteristic-function variance failed",
        )
        moments.append(
            {
                "L": length,
                "fourth_alias_Laurent_coefficients": {
                    str(key): str(value) for key, value in sorted(fourth_alias.items())
                },
                "principal_variance_coefficient": str(variance),
            }
        )

    # n=4,L=2,K=(pi,pi,0). Every listed number is algebraic and exact.
    coarse = sp.Matrix([1, -1, 0])
    D = sp.Matrix([-2, -2, 0])
    require(exact_zero((D.conjugate().T * coarse)[0]), "coarse is not transverse")
    aliases = []
    omitted_direction_negative = None
    for phases in itertools.product((sp.I, -sp.I), (sp.I, -sp.I), (1, -1)):
        averages = [sp.Rational(1, 2) * (1 + phase) for phase in phases]
        common = sp.prod(averages)
        lift = sp.Matrix(
            [sp.conjugate(common * averages[i]) * coarse[i] / sp.sqrt(2) for i in range(3)]
        )
        d = sp.Matrix([phase - 1 for phase in phases])
        require(exact_zero((d.conjugate().T * lift)[0]), "fine lift is not transverse")
        norm = sp.simplify((lift.conjugate().T * lift)[0])
        aliases.append({"phases": [str(x) for x in phases], "norm_squared": str(norm)})
        if phases == (sp.I, -sp.I, 1):
            wrong = sp.conjugate(common) * coarse / sp.sqrt(2)
            defect = sp.simplify((d.conjugate().T * wrong)[0])
            omitted_direction_negative = sp.simplify(sp.conjugate(defect) * defect)
            require(
                omitted_direction_negative == sp.Rational(1, 2),
                "missing-direction negative changed",
            )
    principal = sp.Rational(1, 8)
    total = sum(sp.sympify(row["norm_squared"]) for row in aliases)
    require(total == sp.Rational(1, 2), "alias total normalization changed")
    require((total - principal) / principal == 3, "normalized tail is not 3")
    return {
        "scope": "Exact finite cochain/alias identities; all-size fast bound is analytic.",
        "moment_cases": moments,
        "transverse_alias_case": {
            "n": 4,
            "L": 2,
            "coarse_K": "(pi,pi,0)",
            "aliases": aliases,
            "principal_norm_squared": str(principal),
            "tail_to_principal_ratio": "3",
            "missing_direction_factor_divergence_squared": str(omitted_direction_negative),
        },
    }
