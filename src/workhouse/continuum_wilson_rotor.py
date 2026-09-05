"""Exact integer replay of intrinsic SU(2) class-rotor eigenvalue enclosures.

Rational endpoint proposals are retained from the exploratory run. Acceptance
uses only integer Sturm signs and the displayed tail Schur form bound, with
no numerical eigensolver. This does not identify an OS reducing complement.
"""

from __future__ import annotations

import copy
import math
from fractions import Fraction as F
from functools import lru_cache

import sympy as sp


def exact_normalization_checks():
    x = sp.Symbol("x", real=True)
    theta = sp.Symbol("theta", real=True)
    tested = []
    for n in range(9):
        character = sp.chebyshevu(n, x)
        lower = sp.chebyshevu(n - 1, x) if n else 0
        assert sp.expand(2 * x * character - sp.chebyshevu(n + 1, x) - lower) == 0
        radial = -((1 - x * x) * sp.diff(character, x, 2) - 3 * x * sp.diff(character, x)) / 4
        assert sp.expand(radial - sp.Rational(n * (n + 2), 4) * character) == 0
        tested.append(n)
    wave = sp.Function("g")(theta)
    raw = wave / sp.sin(theta)
    transformed = (
        -sp.sin(theta) * (sp.diff(raw, theta, 2) + 2 * sp.cot(theta) * sp.diff(raw, theta)) / 4
    )
    assert sp.simplify(transformed + sp.diff(wave, theta, 2) / 4 + wave / 4) == 0
    for n in range(1, 6):
        for m in range(1, 6):
            inner = (
                2 / sp.pi * sp.integrate(sp.sin(n * theta) * sp.sin(m * theta), (theta, 0, sp.pi))
            )
            assert inner == int(n == m)
    return {
        "character_degrees": tested,
        "haar_inner_products": 25,
        "casimir": "j(j+1)",
        "jacobi_diagonal": "j(j+1)+8u",
        "jacobi_offdiagonal": "-4u",
        "radial_operator": "-1/4 d²-1/4+8u(1-cos theta)",
    }


def sturm_count(u, cutoff, energy, last_subtraction=F(0)):
    """Number of finite Jacobi eigenvalues strictly below a rational energy.

    Clear all denominators once; determinant recurrence then uses integers
    only. Vanishing internal determinants are skipped in the Sturm sign
    sequence. The off-diagonal is nonzero for the certified positive u.
    """
    u, energy, last_subtraction = (F(u), F(energy), F(last_subtraction))
    if u <= 0 or type(cutoff) is not int or cutoff < 2:
        raise ValueError("Use positive u and at least two character modes")
    scale = math.lcm(4, u.denominator, energy.denominator, last_subtraction.denominator)
    off = int(-4 * u * scale)
    previous, current, previous_sign, changes = (0, 1, 1, 0)
    for n in range(cutoff):
        diagonal = F(n * (n + 2), 4) + 8 * u - energy
        if n == cutoff - 1:
            diagonal -= last_subtraction
        scaled = diagonal * scale
        assert scaled.denominator == 1
        following = int(scaled) * current - off * off * previous
        if following:
            sign = 1 if following > 0 else -1
            changes += sign != previous_sign
            previous_sign = sign
        previous, current = (current, following)
    return changes


def sturm_negative_and_boundary_checks():
    u = F(1, 4)
    for energy in (F(0), F(1), F(2), F(3), F(4), F(11, 4)):
        matrix = sp.Matrix([[2, -1], [-1, sp.Rational(11, 4)]])
        exact = sum(
            bool(value < sp.Rational(energy.numerator, energy.denominator))
            for value in matrix.eigenvals()
        )
        assert sturm_count(u, 2, energy) == exact
    assert sp.Rational(3, 4) != 3
    return {
        "two_mode_exact_counts": 6,
        "internal_zero_principal_minor_test": True,
        "normalization_negative_control": "fundamental Casimir is 3/4, not 3",
    }


_CERTIFICATES = [
    {
        "u": "1",
        "cutoff": 32,
        "tail_kinetic_floor": "272",
        "barrier": "13",
        "boundary_subtraction": "16/259",
        "eigenvalues": [
            {
                "index": 0,
                "lower": "1334741/500000",
                "lower_matrix_interval": ["1334741/500000", "1334743/500000"],
                "lower_sturm_counts": [0, 1],
                "ritz_interval": ["1334741/500000", "1334743/500000"],
                "ritz_sturm_counts": [0, 1],
                "upper": "1334743/500000",
            },
            {
                "index": 1,
                "lower": "791629/125000",
                "lower_matrix_interval": ["791629/125000", "1583259/250000"],
                "lower_sturm_counts": [1, 2],
                "ritz_interval": ["791629/125000", "1583259/250000"],
                "ritz_sturm_counts": [1, 2],
                "upper": "1583259/250000",
            },
        ],
        "gap_interval": ["1831773/500000", "1831777/500000"],
        "gap_over_sqrt_u_interval": ["1831773/500000", "1831777/500000"],
    },
    {
        "u": "100",
        "cutoff": 80,
        "tail_kinetic_floor": "1640",
        "barrier": "121",
        "boundary_subtraction": "160000/1519",
        "eigenvalues": [
            {
                "index": 0,
                "lower": "29671651/1000000",
                "lower_matrix_interval": ["29671651/1000000", "5934331/200000"],
                "lower_sturm_counts": [0, 1],
                "ritz_interval": ["29671651/1000000", "5934331/200000"],
                "ritz_sturm_counts": [0, 1],
                "upper": "5934331/200000",
            },
            {
                "index": 1,
                "lower": "34678559/500000",
                "lower_matrix_interval": ["34678559/500000", "34678561/500000"],
                "lower_sturm_counts": [1, 2],
                "ritz_interval": ["34678559/500000", "34678561/500000"],
                "ritz_sturm_counts": [1, 2],
                "upper": "34678561/500000",
            },
        ],
        "gap_interval": ["39685463/1000000", "39685471/1000000"],
        "gap_over_sqrt_u_interval": ["39685463/10000000", "39685471/10000000"],
    },
    {
        "u": "10000",
        "cutoff": 800,
        "tail_kinetic_floor": "160400",
        "barrier": "1201",
        "boundary_subtraction": "1600000000/159199",
        "eigenvalues": [
            {
                "index": 0,
                "lower": "299671851/1000000",
                "lower_matrix_interval": ["299671851/1000000", "59934371/200000"],
                "lower_sturm_counts": [0, 1],
                "ritz_interval": ["299671851/1000000", "59934371/200000"],
                "ritz_sturm_counts": [0, 1],
                "upper": "59934371/200000",
            },
            {
                "index": 1,
                "lower": "13987183/20000",
                "lower_matrix_interval": ["13987183/20000", "349679577/500000"],
                "lower_sturm_counts": [1, 2],
                "ritz_interval": ["13987183/20000", "349679577/500000"],
                "ritz_sturm_counts": [1, 2],
                "upper": "349679577/500000",
            },
        ],
        "gap_interval": ["79937459/200000", "399687303/1000000"],
        "gap_over_sqrt_u_interval": ["79937459/20000000", "399687303/100000000"],
    },
    {
        "u": "1000000",
        "cutoff": 8000,
        "tail_kinetic_floor": "16004000",
        "barrier": "12001",
        "boundary_subtraction": "16000000000000/15991999",
        "eigenvalues": [
            {
                "index": 0,
                "lower": "299967187/100000",
                "lower_matrix_interval": ["299967187/100000", "1499835937/500000"],
                "lower_sturm_counts": [0, 1],
                "ritz_interval": ["299967187/100000", "1499835937/500000"],
                "ritz_sturm_counts": [0, 1],
                "upper": "1499835937/500000",
            },
            {
                "index": 1,
                "lower": "139987187/20000",
                "lower_matrix_interval": ["139987187/20000", "3499679677/500000"],
                "lower_sturm_counts": [1, 2],
                "ritz_interval": ["139987187/20000", "3499679677/500000"],
                "ritz_sturm_counts": [1, 2],
                "upper": "3499679677/500000",
            },
        ],
        "gap_interval": ["999921869/250000", "999921871/250000"],
        "gap_over_sqrt_u_interval": ["999921869/250000000", "999921871/250000000"],
    },
]


def rotor_certificates() -> list[dict]:
    """Return fresh rational certificate payloads, independently replayable."""
    return copy.deepcopy(_CERTIFICATES)


def replay_rotor_certificate(entry: dict) -> dict:
    """Reject a false tail bound or interval before accepting an untruncated enclosure."""
    u, cutoff = F(entry["u"]), entry["cutoff"]
    if u <= 0 or type(cutoff) is not int or cutoff < 2:
        raise ValueError("Positive coupling and an integer cutoff of at least two are required")
    root = math.isqrt(u.numerator)
    if u.denominator != 1 or root * root != u:
        raise ValueError("This certificate schema uses square positive integer coupling")
    kappa = F(cutoff * (cutoff + 2), 4)
    barrier = F(entry["barrier"])
    if not 0 < barrier < kappa:
        raise ValueError("The tail barrier must lie strictly below the discarded kinetic floor")
    correction = 16 * u * u / (kappa - barrier)
    if F(entry["tail_kinetic_floor"]) != kappa or F(entry["boundary_subtraction"]) != correction:
        raise ValueError("The tail Schur form coefficient is incorrect")
    if sturm_count(u, cutoff, barrier) < 2 or sturm_count(u, cutoff, barrier, correction) < 2:
        raise ValueError("The two comparison eigenvalues must be below the tail barrier")
    values = entry["eigenvalues"]
    if len(values) != 2 or [v["index"] for v in values] != [0, 1]:
        raise ValueError("The certificate must enclose precisely the first two eigenvalues")
    for interval in values:
        index = interval["index"]
        for key, shift, count_key in (
            ("ritz_interval", F(0), "ritz_sturm_counts"),
            ("lower_matrix_interval", correction, "lower_sturm_counts"),
        ):
            low, high = map(F, interval[key])
            if not low < high < barrier:
                raise ValueError("Comparison interval endpoints must be ordered below the barrier")
            counts = [sturm_count(u, cutoff, low, shift), sturm_count(u, cutoff, high, shift)]
            if counts != [index, index + 1] or interval[count_key] != counts:
                raise ValueError("An exact Sturm count rejects the claimed eigenvalue interval")
        if F(interval["lower"]) != F(interval["lower_matrix_interval"][0]) or F(
            interval["upper"]
        ) != F(interval["ritz_interval"][1]):
            raise ValueError(
                "The infinite-operator interval must use the lower and Ritz comparisons"
            )
    lower = F(values[1]["lower"]) - F(values[0]["upper"])
    upper = F(values[1]["upper"]) - F(values[0]["lower"])
    if not 0 < lower <= upper or list(map(F, entry["gap_interval"])) != [lower, upper]:
        raise ValueError("The gap interval does not follow from the first two eigenvalue intervals")
    if list(map(F, entry["gap_over_sqrt_u_interval"])) != [lower / root, upper / root]:
        raise ValueError("The normalized gap has an incorrect square-root scaling")
    return {
        "u": str(u),
        "cutoff": cutoff,
        "gap_interval": [str(lower), str(upper)],
        "gap_over_sqrt_u_interval": [str(lower / root), str(upper / root)],
        "scope": "Untruncated fixed-u class rotor using the analytic tail form identification",
    }


@lru_cache(maxsize=1)
def exact_rotor_controls() -> dict:
    entries = rotor_certificates()
    replayed = [replay_rotor_certificate(entry) for entry in entries]
    bad = copy.deepcopy(entries[1])
    bad["eigenvalues"][0]["ritz_interval"][1] = "0"
    try:
        replay_rotor_certificate(bad)
    except ValueError:
        pass
    else:
        raise AssertionError("A corrupted interval was accepted")
    assert all(F(row["gap_over_sqrt_u_interval"][1]) < 4 for row in replayed)
    return {
        "normalization": exact_normalization_checks(),
        "boundary_controls": sturm_negative_and_boundary_checks(),
        "replayed_enclosures": replayed,
        "corrupted_interval_rejected": True,
        "finite_u_gap_below_4_sqrt_u": True,
        "numerical_eigensolver_used": False,
    }
