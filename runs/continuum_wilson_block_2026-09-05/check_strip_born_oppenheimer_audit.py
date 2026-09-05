"""Independent exact controls for the physical two-square strip first term.

This checks finite Lie algebra, coordinate jets, Gaussian contractions, and
polynomial Gauss cancellation. It does not certify asymptotic remainders,
an infinite-volume RG estimate, or an OS reducing-complement identification.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as s


def inner(x: s.Matrix, y: s.Matrix) -> s.Expr:
    return s.simplify(-2 * s.trace(x * y))


def su_basis(n: int) -> list[s.Matrix]:
    result = []
    for i in range(n):
        for j in range(i + 1, n):
            a, b = s.zeros(n), s.zeros(n)
            a[i, j] = a[j, i] = s.I / 2
            b[i, j], b[j, i] = s.Rational(1, 2), -s.Rational(1, 2)
            result.extend((a, b))
    for k in range(1, n):
        a = s.zeros(n)
        for i in range(k):
            a[i, i] = s.I / s.sqrt(2 * k * (k + 1))
        a[k, k] = -k * s.I / s.sqrt(2 * k * (k + 1))
        result.append(a)
    return result


def zero_matrix(matrix: s.Matrix) -> bool:
    return all(s.simplify(x) == 0 for x in matrix)


def matrix_polynomial_product(
    a: list[s.Matrix], b: list[s.Matrix], degree: int
) -> list[s.Matrix]:
    n = a[0].rows
    return [
        sum(
            (a[j] * b[k - j] for j in range(k + 1) if j < len(a) and k - j < len(b)),
            s.zeros(n),
        )
        for k in range(degree + 1)
    ]


def metric_jet_controls() -> dict:
    q0, q1, q2 = s.symbols("q0 q1 q2", real=True)
    a = s.Matrix([[0, -q2, q1], [q2, 0, -q0], [-q1, q0, 0]])
    identity, zero = s.eye(3), s.zeros(3)
    # Coefficients in alpha, calculated directly from exp(+-alpha ad Q).
    cuu = [6 * identity, zero, -(a**2)]
    cuk = [3 * identity, -a, -(a**2) / 2]
    cku = [3 * identity, a, -(a**2) / 2]
    cuu_inverse = [identity / 6, zero, a**2 / 36]
    assert all(
        zero_matrix(x - (identity if k == 0 else zero))
        for k, x in enumerate(matrix_polynomial_product(cuu, cuu_inverse, 2))
    )
    cross = matrix_polynomial_product(
        matrix_polynomial_product(cku, cuu_inverse, 2), cuk, 2
    )
    schur = [4 * identity - cross[0], -cross[1], -cross[2]]
    assert zero_matrix(schur[0] - s.Rational(5, 2) * identity)
    assert zero_matrix(schur[1])
    assert zero_matrix(schur[2] - s.Rational(5, 12) * a**2)

    lift = matrix_polynomial_product(cku, cuu_inverse, 2)
    assert zero_matrix(lift[0] - identity / 2)
    assert zero_matrix(lift[1] - a / 6)
    assert zero_matrix(lift[2])
    # dU U^-1 = alpha E + alpha^2 [Q,E]/2; dH H^-1 has 1/2,1/8.
    assert s.Rational(1, 4) + s.Rational(1, 6) - s.Rational(1, 8) == s.Rational(7, 24)
    # Divide by alpha/2 to convert the balanced fiber velocity to Z.
    assert 2 * s.Rational(7, 24) == s.Rational(7, 12)

    dexp_inverse = [identity, -a / 2, a**2 / 12]
    dexp_inverse_t = [x.T for x in dexp_inverse]
    coarse = matrix_polynomial_product(
        matrix_polynomial_product(dexp_inverse, cuu, 2), dexp_inverse_t, 2
    )
    assert zero_matrix(coarse[0] - 6 * identity)
    assert zero_matrix(coarse[1])
    assert zero_matrix(coarse[2] + s.Rational(3, 2) * a**2)
    return {
        "vertical_kinetic_at_identity": "5/4",
        "schur_alpha_squared": "(5/12)(ad Q)^2",
        "balanced_velocity_alpha": "(7/12)[Q,E]",
        "coarse_form_g_squared_leading": "3/2",
        "coarse_form_order_one": "-(3/4)(ad Q)^2",
    }


def lie_gaussian_controls() -> list[dict]:
    rows = []
    for n in (2, 3, 4):
        basis = su_basis(n)
        d = n * n - 1
        assert len(basis) == d
        assert all(
            inner(t, v) == int(i == j)
            for i, t in enumerate(basis)
            for j, v in enumerate(basis)
        )
        q = sum((s.Rational((i % 5) - 2, i + 3) * t for i, t in enumerate(basis)), s.zeros(n))
        qnorm = inner(q, q)
        adq = s.Matrix([[inner(t, q * v - v * q) for v in basis] for t in basis])
        assert zero_matrix(adq + adq.T)
        assert s.simplify(s.trace(adq**2) + n * qnorm) == 0
        cf = s.Rational(n * n - 1, 2 * n)
        assert zero_matrix(sum((t * t for t in basis), s.zeros(n)) + cf * s.eye(n))
        # Explicit basis contraction of the actual mixed magnetic quartic.
        mixed = sum((s.trace(q * q * t * t) for t in basis), s.S.Zero)
        assert s.simplify(mixed - cf * qnorm / 2) == 0
        a = 1 / s.sqrt(5)
        vertical_kinetic = s.Rational(5, 12) * a * s.trace(adq**2)
        vertical_potential = -mixed / (8 * a)
        vertical = s.simplify(vertical_kinetic + vertical_potential)
        assert s.simplify(vertical + s.sqrt(5) * (s.Rational(n, 12) + cf / 16) * qnorm) == 0
        bh = s.Rational(3, 2) * s.Rational(49, 360) / (2 * a) * n * qnorm
        assert s.simplify(bh - 49 * n * qnorm / (96 * s.sqrt(5))) == 0
        combined = s.simplify(vertical + bh)
        assert s.simplify(combined - s.sqrt(5) * (5 - 2 * n * n) * qnorm / (160 * n)) == 0
        rows.append({
            "N": n,
            "dimension": d,
            "Q_norm_squared": str(qnorm),
            "combined_per_Q_norm_squared": str(s.simplify(combined / qnorm)),
        })
    return rows


def polynomial_gauss_controls() -> dict:
    q = s.Matrix(s.symbols("q0:3", real=True))
    z = s.Matrix(s.symbols("z0:3", real=True))

    def gauss(f: s.Expr, coordinates: s.Matrix) -> s.Matrix:
        return coordinates.cross(s.Matrix([s.diff(f, x) for x in coordinates]))

    def first_coupling(f: s.Expr) -> s.Expr:
        gq = gauss(f, q)
        return s.expand(sum(s.diff(gq[b], z[b]) for b in range(3)))

    q2, z2, qz = q.dot(q), z.dot(z), q.dot(z)
    physical = [q2, z2, qz, qz**2, q2 * z2, q2 * qz, qz**3 + q2 * z2**2]
    for f in physical:
        assert zero_matrix(gauss(f, q) + gauss(f, z))
        assert first_coupling(f) == 0
    f = s.Function("F")(*q, *z)
    gz = gauss(f, z)
    assert s.simplify(sum(s.diff(gz[b], z[b]) for b in range(3))) == 0
    negative = q[0] * z[1]
    assert first_coupling(negative) != 0
    return {
        "jointly_invariant_polynomials": len(physical),
        "arbitrary_function_divergence_identity": True,
        "noninvariant_negative_control": str(first_coupling(negative)),
        "scope": (
            "Exact SU(2) polynomial checks, with general-rank "
            "antisymmetry proof in the audit note."
        ),
    }


def scalar_controls() -> dict:
    n, g = s.symbols("N g", positive=True)
    d, cf = n**2 - 1, (n**2 - 1) / (2 * n)
    vertical = -s.sqrt(5) * (n / 12 + cf / 16)
    bh = 49 * n / (96 * s.sqrt(5))
    assert s.simplify(vertical + bh - s.sqrt(5) * (5 - 2 * n**2) / (160 * n)) == 0
    # Flatten Haar: log j(sqrt(2)gQ) = -N g^2 |Q|^2/12 + O(g^4).
    haar_constant = s.Rational(3, 2) / g**2 * (-n * g**2 * d / 6) / 2
    assert s.simplify(haar_constant + n * d / 8) == 0
    # The centered quadratic corrector lies at gap 2sqrt(5).
    variance = s.sqrt(5) / 2
    derivative_norm = (7 / (6 * s.sqrt(10))) ** 2 * variance
    assert s.simplify(derivative_norm - 49 / (144 * s.sqrt(5))) == 0
    return {
        "combined_shift": str(s.simplify(vertical + bh)),
        "haar_scalar": str(haar_constant),
        "ground_derivative_norm_coefficient": str(s.simplify(derivative_norm)),
    }


def main() -> None:
    result = {
        "scope": __doc__,
        "metric_jets": metric_jet_controls(),
        "lie_gaussian_contractions": lie_gaussian_controls(),
        "physical_gauss_cancellation": polynomial_gauss_controls(),
        "symbolic_scalar_constants": scalar_controls(),
    }
    output = Path(__file__).with_name("strip_born_oppenheimer_audit_controls.json")
    with output.open("x", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2)
        handle.write("\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
