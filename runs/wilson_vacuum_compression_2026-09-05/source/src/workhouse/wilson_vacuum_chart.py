"""Exact finite product-transfer oracle for the second-order vacuum chart.

This module computes ordinary multivariate Taylor coefficients of the actual
symmetric transfer power.  It is a finite tensor-model oracle, not an SU(N)
truncation or an infinite-volume proof.  All coefficient operations use exact
rationals.  The analytic operator statement lives in the accompanying note.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from itertools import product

from sympy import MatrixBase, Rational, SparseMatrix

Degree = tuple[int, ...]
Polynomial = dict[Degree, MatrixBase]
ONE = Rational(1)
DEFAULT_RATIO = Rational(4, 5)
CONTROL_RATIO = Rational(3, 4)
CONTROL_V = Rational(2, 3)
CONTROL_H = Rational(1, 2)


def degrees(variables: int, order: int = 2) -> list[Degree]:
    return sorted(
        (d for d in product(range(order + 1), repeat=variables) if sum(d) <= order),
        key=lambda d: (sum(d), d),
    )


def multiply(a: Polynomial, b: Polynomial, order: int = 2) -> Polynomial:
    """Multiply matrix-valued polynomials, retaining noncommutative order."""
    out: Polynomial = {}
    for da, ma in a.items():
        for db, mb in b.items():
            dc = tuple(x + y for x, y in zip(da, db, strict=True))
            if sum(dc) <= order:
                value = ma * mb
                out[dc] = out[dc] + value if dc in out else value
    return out


def power(a: Polynomial, exponent: int, order: int = 2) -> Polynomial:
    if exponent < 0:
        raise ValueError("A transfer power must be nonnegative")
    zero = next(d for d in a if sum(d) == 0)
    out = {zero: SparseMatrix.eye(a[zero].rows)}
    for _ in range(exponent):
        out = multiply(out, a, order)
    return out


def linear_exponential(generators: Sequence[MatrixBase], sign: int = 1) -> Polynomial:
    """exp(sign * sum(z_p S_p)) to ordinary Taylor order two."""
    count = len(generators)
    if not count:
        raise ValueError("At least one generator is required")
    zero = (0,) * count
    first = {}
    for p, matrix in enumerate(generators):
        key = tuple(int(j == p) for j in range(count))
        first[key] = sign * matrix
    second = {d: matrix / 2 for d, matrix in multiply(first, first).items()}
    return {zero: SparseMatrix.eye(generators[0].rows), **first, **second}


def diagonal_kinetic(site_count: int, ratio: Rational) -> MatrixBase:
    """A product contraction with one vacuum and one excitation at each site."""
    if not 0 < ratio < 1:
        raise ValueError("The one-site excited multiplier must lie in (0, 1)")
    size = 1 << site_count
    return SparseMatrix(size, size, {(i, i): ratio ** i.bit_count() for i in range(size)})


def face_flip(site_count: int, support: Sequence[int]) -> MatrixBase:
    """Multiplication by a product of Z_2 characters, in the electric basis."""
    support = tuple(support)
    if not support or len(set(support)) != len(support):
        raise ValueError("A face support must contain distinct sites")
    if min(support) < 0 or max(support) >= site_count:
        raise ValueError("Face support lies outside the tensor product")
    mask = sum(1 << i for i in support)
    size = 1 << site_count
    return SparseMatrix(size, size, {(i ^ mask, i): 1 for i in range(size)})


def embed_local(local: MatrixBase, support: Sequence[int], site_count: int) -> MatrixBase:
    """Embed a local operator with identity on all spectator sites."""
    support = tuple(support)
    if local.shape != (1 << len(support),) * 2:
        raise ValueError("Local matrix dimension does not match its support")
    if len(set(support)) != len(support) or any(i < 0 or i >= site_count for i in support):
        raise ValueError("Invalid support")
    spectators = tuple(i for i in range(site_count) if i not in support)

    def scatter(bits: int, positions: Sequence[int]) -> int:
        return sum(((bits >> j) & 1) << pos for j, pos in enumerate(positions))

    entries = {}
    for (r, c), value in local.todok().items():
        local_r, local_c = scatter(r, support), scatter(c, support)
        for spectator in range(1 << len(spectators)):
            fixed = scatter(spectator, spectators)
            entries[local_r | fixed, local_c | fixed] = value
    size = 1 << site_count
    return SparseMatrix(size, size, entries)


def spectator_kinetic(site_count: int, support: Sequence[int], ratio: Rational) -> MatrixBase:
    outside_mask = sum(1 << i for i in range(site_count) if i not in support)
    size = 1 << site_count
    return SparseMatrix(
        size, size, {(i, i): ratio ** (i & outside_mask).bit_count() for i in range(size)}
    )


def vacuum_generator(kinetic: MatrixBase, vacuum_column: MatrixBase) -> MatrixBase:
    """Solve (1-D) chi = Q a and return |chi><vac|-|vac><chi|."""
    if vacuum_column[0] != 0:
        raise ValueError("A scalar vacuum component cannot be removed by a commutator")
    entries = {}
    for i in range(1, kinetic.rows):
        if vacuum_column[i] != 0:
            value = vacuum_column[i] / (1 - kinetic[i, i])
            entries[i, 0] = value
            entries[0, i] = -value.conjugate()
    return SparseMatrix(kinetic.rows, kinetic.rows, entries)


@dataclass
class Chart:
    raw: Polynomial
    normalized: Polynomial
    first_rotated: Polynomial
    second_rotated: Polynomial
    first_generators: tuple[MatrixBase, ...]
    second_generators: dict[Degree, MatrixBase]
    eigenvalue_second: dict[Degree, Rational]


def chart(
    kinetic: MatrixBase,
    potentials: Sequence[MatrixBase],
    steps: int = 1,
    tau: Rational = ONE,
    first_generators: Sequence[MatrixBase] | None = None,
) -> Chart:
    """Independently compute the finite-volume Taylor eigenproblem and chart.

    The global second generator is deliberately obtained from the global
    eigenproblem. Tests compare it with independently computed local connected
    generators; locality is therefore a result of the comparison, not an input.
    """
    count = len(potentials)
    if count == 0 or steps < 1:
        raise ValueError("At least one potential and one time step are required")
    if any(v.shape != kinetic.shape or v != v.H or v[0, 0] != 0 for v in potentials):
        raise ValueError("Potentials must be Hermitian, compatible, and vacuum centered")
    if (
        kinetic.rows != kinetic.cols
        or kinetic != SparseMatrix.diag(*kinetic.diagonal())
        or kinetic[0, 0] != 1
    ):
        raise ValueError(
            "This oracle uses a diagonal product contraction with vacuum at index zero"
        )
    if any(value.is_real is not True or not 0 <= value < 1 for value in kinetic.diagonal()[1:]):
        raise ValueError("Every complementary kinetic multiplier must be real and in [0, 1)")
    zero = (0,) * count
    magnetic = linear_exponential([tau * v / 2 for v in potentials])
    fine = multiply(multiply(magnetic, {zero: kinetic}), magnetic)
    raw = power(fine, steps)
    base = raw[zero]
    units = [tuple(int(j == p) for j in range(count)) for p in range(count)]
    columns = [raw[d][:, 0] for d in units]
    first = (
        tuple(first_generators)
        if first_generators is not None
        else tuple(vacuum_generator(base, col) for col in columns)
    )
    if len(first) != count or any(s.shape != base.shape or -s != s.H for s in first):
        raise ValueError("First generators must be compatible and anti-Hermitian")
    if any(
        not (col + (base * s - s * base)[:, 0]).is_zero_matrix
        for col, s in zip(columns, first, strict=True)
    ):
        raise ValueError("Supplied first generators must cancel every first-order vacuum column")
    # At first order the normalized eigenvector coefficient is S1 |vac>.
    eig2 = {}
    normalized = dict(raw)
    for d in degrees(count):
        if sum(d) != 2:
            continue
        correction = 0
        for dp in units:
            rest = tuple(x - y for x, y in zip(d, dp, strict=True))
            if rest in units:
                q = units.index(rest)
                correction += (raw[dp] * first[q][:, 0])[0]
        # Repeated p contributes once because its single unit is visited once.
        eig2[d] = raw[d][0, 0] + correction
        normalized[d] = raw[d] - eig2[d] * base
    a = multiply(multiply(linear_exponential(first, -1), normalized), linear_exponential(first))
    second = {d: vacuum_generator(base, a[d][:, 0]) for d in a if sum(d) == 2}
    rotated = dict(a)
    for d, generator in second.items():
        rotated[d] = a[d] + base * generator - generator * base
    return Chart(raw, normalized, a, rotated, first, second, eig2)


def product_chart(
    site_count: int,
    supports: Sequence[Sequence[int]],
    ratio: Rational = DEFAULT_RATIO,
    steps: int = 1,
    tau: Rational = ONE,
) -> Chart:
    """Use LOCAL first/second charts, and compare them with a global expansion.

    A global rank-two vacuum rotation would have the same vacuum column but
    different spectator action.  It is deliberately not used as the local
    chart in this function.
    """
    supports = [tuple(s) for s in supports]
    potentials = [face_flip(site_count, s) for s in supports]

    def first_for(n: int, local_supports: Sequence[Sequence[int]]) -> tuple[MatrixBase, ...]:
        out = []
        for support in local_supports:
            size = len(support)
            single = ratio**size
            amplitude = tau * (1 + single) / (2 * (1 - single))
            local = SparseMatrix(
                1 << size,
                1 << size,
                {
                    ((1 << size) - 1, 0): amplitude,
                    (0, (1 << size) - 1): -amplitude,
                },
            )
            out.append(embed_local(local, support, n))
        return tuple(out)

    result = chart(
        diagonal_kinetic(site_count, ratio), potentials, steps, tau, first_for(site_count, supports)
    )
    base = result.raw[(0,) * len(supports)]
    second = {}
    rotated = dict(result.first_rotated)
    for degree in degrees(len(supports)):
        if sum(degree) != 2:
            continue
        active = [p for p, order in enumerate(degree) if order]
        if len(active) == 2 and set(supports[active[0]]).isdisjoint(supports[active[1]]):
            generator = SparseMatrix.zeros(base.rows, base.cols)
        else:
            union = tuple(sorted(set().union(*(set(supports[p]) for p in active))))
            local_supports = [tuple(union.index(i) for i in supports[p]) for p in active]
            local = chart(
                diagonal_kinetic(len(union), ratio),
                [face_flip(len(union), support) for support in local_supports],
                steps,
                tau,
                first_for(len(union), local_supports),
            )
            local_degree = tuple(degree[p] for p in active)
            generator = embed_local(local.second_generators[local_degree], union, site_count)
        second[degree] = generator
        rotated[degree] = result.first_rotated[degree] + base * generator - generator * base
    result.second_generators = second
    result.second_rotated = rotated
    return result


def support_majorants(n: int, delta: Rational = DEFAULT_RATIO) -> tuple[Rational, ...]:
    """Geometry-only bounds before multiplying by local operator bounds."""
    if n < 1 or not 0 < delta <= Rational(4, 5):
        raise ValueError("Require n >= 1 and 0 < delta <= 4/5")
    return (
        4 * n * delta ** max(n - 4, 0),
        48 * n * delta ** max(n - 7, 0),
        8 * n**2 * delta ** max(n - 8, 0),
    )


def two_level_negative_control(
    delta: Rational = CONTROL_RATIO, v: Rational = CONTROL_V, h: Rational = CONTROL_H
) -> dict:
    """A quadratic vacuum source survives U1, and vanishes after U2."""
    model = chart(SparseMatrix.diag(1, delta), [SparseMatrix([[0, v], [v, h]])])
    predicted = h * v * (1 + 6 * delta + delta**2) / (8 * (1 - delta) ** 2)
    residual = model.first_rotated[(2,)][1, 0]
    return {
        "first_chart_residual": residual,
        "second_generator": model.second_generators[(2,)][1, 0],
        "predicted_generator": predicted,
        "final_vacuum_column": model.second_rotated[(2,)][:, 0],
        "model": model,
    }
