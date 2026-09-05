"""Finite exact oracle for the connected vacuum-chart induction.

This is an arbitrary-fixed-order tensor model, with ordinary multivariate
coefficients and ordered matrix products. It checks the analytic recursion;
finite matrices do not prove the infinite-dimensional norm estimates.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from math import factorial

from sympy import MatrixBase, Rational, SparseMatrix

from .wilson_vacuum_chart import (
    DEFAULT_RATIO,
    ONE,
    Degree,
    Polynomial,
    degrees,
    diagonal_kinetic,
    embed_local,
    face_flip,
    multiply,
    power,
    vacuum_generator,
)


def exponential(a: Polynomial, order: int) -> Polynomial:
    """Formal exponential of a matrix polynomial with zero constant term."""
    key, matrix = next(iter(a.items()))
    zero = (0,) * len(key)
    if zero in a and not a[zero].is_zero_matrix:
        raise ValueError("Formal exponential requires a zero constant term")
    result = {zero: SparseMatrix.eye(matrix.rows)}
    term = result
    for j in range(1, order + 1):
        term = multiply(term, a, order)
        for degree, coefficient in term.items():
            result[degree] = result.get(
                degree, SparseMatrix.zeros(matrix.rows)
            ) + coefficient / factorial(j)
    return result


def difference(a: Degree, b: Degree) -> Degree | None:
    result = tuple(x - y for x, y in zip(a, b, strict=True))
    return result if min(result) >= 0 else None


def normalize(raw: Polynomial, order: int) -> tuple[Polynomial, dict]:
    """Solve the unrotated eigenproblem, then divide by its actual eigenvalue.

    No vacuum-chart coefficients enter this normalization. The eigenvector
    gauge has constant vacuum component one and all higher vacuum components zero.
    """
    zero = next(key for key in raw if sum(key) == 0)
    base = raw[zero]
    omega = SparseMatrix(base.rows, 1, {(0, 0): 1})
    vectors = {zero: omega}
    values = {zero: Rational(1)}
    keys = degrees(len(zero), order)
    for alpha in keys[1:]:
        rhs = SparseMatrix.zeros(base.rows, 1)
        for beta in keys[1:]:
            rest = difference(alpha, beta)
            if rest is not None and beta in raw:
                rhs += raw[beta] * vectors[rest]
            if rest is not None and rest != zero and beta in values:
                rhs -= values[beta] * vectors[rest]
        values[alpha] = rhs[0]
        vectors[alpha] = SparseMatrix(
            base.rows, 1, {(i, 0): rhs[i] / (1 - base[i, i]) for i in range(1, base.rows) if rhs[i]}
        )
    inverse = {zero: Rational(1)}
    for alpha in keys[1:]:
        inverse[alpha] = -sum(
            values[beta] * inverse[rest]
            for beta in keys[1:]
            if (rest := difference(alpha, beta)) is not None
        )
    normalized = {}
    for alpha in keys:
        normalized[alpha] = sum(
            (
                inverse[rest] * coefficient
                for beta, coefficient in raw.items()
                if (rest := difference(alpha, beta)) is not None
            ),
            SparseMatrix.zeros(base.rows),
        )
    return normalized, values


def components(supports: tuple[tuple[int, ...], ...], alpha: Degree) -> list[tuple[int, ...]]:
    """Connected components of the distinct active supports, by shared sites."""
    remaining = {p for p, value in enumerate(alpha) if value}
    out = []
    while remaining:
        component = {min(remaining)}
        remaining -= component
        while touching := {
            p
            for p in remaining
            if any(not set(supports[p]).isdisjoint(supports[q]) for q in component)
        }:
            component |= touching
            remaining -= touching
        out.append(tuple(sorted(component)))
    return out


@dataclass
class FormalChart:
    raw: Polynomial
    normalized: Polynomial
    rotated: Polynomial
    generators: dict[Degree, MatrixBase]
    eigenvalues: dict


@lru_cache(maxsize=128)
def product_recursion(
    site_count: int,
    supports: tuple[tuple[int, ...], ...],
    order: int = 3,
    ratio: Rational = DEFAULT_RATIO,
    steps: int = 1,
    tau: Rational = ONE,
) -> FormalChart:
    """Compute an actual finite transfer, then recursively attach local charts.

    Cached results are shared; callers must not mutate returned matrices/dicts.
    Local coefficients are obtained in their minimal active subsystem, whereas
    the global normalization and conjugations use the entire finite model.
    """
    if order < 1 or steps < 1 or site_count < 1 or not supports or tau <= 0:
        raise ValueError("Positive order, block power, site count and step are required")
    count = len(supports)
    kinetic = diagonal_kinetic(site_count, ratio)
    zero = (0,) * count
    magnetic = exponential(
        {
            tuple(int(j == p) for j in range(count)): tau * face_flip(site_count, support) / 2
            for p, support in enumerate(supports)
        },
        order,
    )
    raw = power(multiply(multiply(magnetic, {zero: kinetic}, order), magnetic, order), steps, order)
    normalized, values = normalize(raw, order)
    rotated = normalized
    generators = {}
    for n in range(1, order + 1):
        homogeneous = {}
        for alpha in degrees(count, n):
            if sum(alpha) != n:
                continue
            parts = components(supports, alpha)
            if len(parts) > 1:
                if not rotated[alpha][:, 0].is_zero_matrix:
                    raise AssertionError("Disconnected coefficient was not already anchored")
                generators[alpha] = SparseMatrix.zeros(kinetic.rows)
                continue
            active = parts[0]
            union = tuple(sorted(set().union(*(set(supports[p]) for p in active))))
            if len(active) == count and len(union) == site_count:
                generator = vacuum_generator(raw[zero], rotated[alpha][:, 0])
            else:
                local_supports = tuple(tuple(union.index(i) for i in supports[p]) for p in active)
                local = product_recursion(len(union), local_supports, n, ratio, steps, tau)
                generator = embed_local(
                    local.generators[tuple(alpha[p] for p in active)], union, site_count
                )
            homogeneous[alpha] = generator
            generators[alpha] = generator
        left = exponential({key: -value for key, value in homogeneous.items()}, order)
        right = exponential(homogeneous, order)
        rotated = multiply(multiply(left, rotated, order), right, order)
    return FormalChart(raw, normalized, rotated, generators, values)
