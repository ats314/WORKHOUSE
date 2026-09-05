"""Exact Gaussian polynomial control of the two-strip on-shell first term.

Only the leading oscillator and its explicitly derived first coupling are
checked. This is not a uniform complement, multiscale, or continuum bound.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as s


def expectation(polynomial: s.Expr, variables: list, variances: list) -> s.Expr:
    result = s.S.Zero
    for powers, coefficient in s.Poly(s.expand(polynomial), *variables).terms():
        moment = coefficient
        for power, variance in zip(powers, variances, strict=True):
            if power % 2:
                moment = s.S.Zero
                break
            if power:
                moment *= s.factorial2(power - 1) * variance ** (power // 2)
        result += moment
    return s.simplify(result)


def exact_control() -> dict:
    q1 = s.Matrix(s.symbols("q10:13", real=True))
    q2 = s.Matrix(s.symbols("q20:23", real=True))
    z1 = s.Matrix(s.symbols("z10:13", real=True))
    z2 = s.Matrix(s.symbols("z20:23", real=True))
    qs, zs = list(q1) + list(q2), list(z1) + list(z2)
    variables = qs + zs
    variances = [s.sqrt(3) / 2] * 6 + [s.sqrt(5) / 2] * 6

    def angular(f: s.Expr, q: s.Matrix) -> s.Matrix:
        return q.cross(s.Matrix([s.diff(f, x) for x in q]))

    def oscillator_above_ground(f: s.Expr) -> s.Expr:
        result = sum(-s.Rational(3, 2) * s.diff(f, x, 2) + s.sqrt(3) * x * s.diff(f, x) for x in qs)
        result += sum(
            -s.Rational(5, 2) * s.diff(f, x, 2) + s.sqrt(5) * x * s.diff(f, x) for x in zs
        )
        return s.expand(result)

    psi = q1.dot(q2)
    l1, l2 = angular(psi, q1), angular(psi, q2)
    assert l1 + l2 == s.zeros(3, 1)
    assert l1 != s.zeros(3, 1)
    coarse_energy = 2 * s.sqrt(3)
    assert s.simplify(oscillator_above_ground(psi) - coarse_energy * psi) == 0
    for component in list(l1) + list(l2):
        assert s.simplify(oscillator_above_ground(component) - coarse_energy * component) == 0

    coefficient = 7 / (2 * s.sqrt(10))
    image = s.expand(coefficient * (z1.dot(l1) + z2.dot(l2)))
    assert image != 0
    assert s.simplify(oscillator_above_ground(image) - (coarse_energy + s.sqrt(5)) * image) == 0
    # The image itself is jointly gauge invariant in all four variables.
    total_gauss = sum((angular(image, q) for q in (q1, q2, z1, z2)), s.zeros(3, 1))
    assert all(s.simplify(x) == 0 for x in total_gauss)

    norm_psi = expectation(psi**2, variables, variances)
    norm_angular = expectation(l1.dot(l1) + l2.dot(l2), variables, variances)
    norm_image = expectation(image**2, variables, variances)
    assert norm_psi == s.Rational(9, 4)
    assert norm_angular == 9
    assert s.simplify(norm_image - 49 * s.sqrt(5) * norm_angular / 80) == 0
    schur = s.simplify(-norm_image / s.sqrt(5) / norm_psi)
    direct = s.Rational(3, 4) * norm_angular / norm_psi
    net = s.simplify(direct + schur)
    assert schur == -s.Rational(49, 20)
    assert direct == 3
    assert net == s.Rational(11, 20)

    # Scalar algebra holds for arbitrary rank; the norm identity uses C_adj=N.
    n = s.symbols("N", integer=True, positive=True)
    assert s.simplify((s.Rational(3, 4) - s.Rational(49, 80)) * 2 * n) == 11 * n / 40
    # A denominator substitution is wrong on a non-eigenfunction spanning
    # distinct coarse shells at a single energy parameter.
    shell_four = (q1.dot(q1) - 5 * s.sqrt(3) / 2) * psi
    # The radial multiplication contains a lower shell too; project it away
    # using the oscillator polynomial itself to produce an exact shell-four vector.
    shell_four = s.expand(
        (oscillator_above_ground(shell_four) - coarse_energy * shell_four) / (2 * s.sqrt(3))
    )
    assert shell_four != 0
    assert s.simplify(oscillator_above_ground(shell_four) - 4 * s.sqrt(3) * shell_four) == 0
    image_four = s.expand(
        coefficient * (z1.dot(angular(shell_four, q1)) + z2.dot(angular(shell_four, q2)))
    )
    assert image_four != 0
    fixed_energy_denominator_error = s.expand(
        oscillator_above_ground(image_four) - (coarse_energy + s.sqrt(5)) * image_four
    )
    assert fixed_energy_denominator_error != 0

    # Centered literal source limits for a single strip.
    q, z = q1, z1
    sigma_q, sigma_z = s.sqrt(3) / 2, s.sqrt(5) / 2
    source_polynomials = [q.dot(q) - 3 * sigma_q, q.dot(z), z.dot(z) - 3 * sigma_z]
    source_gram = s.Matrix(
        [
            [expectation(f * h, variables, variances) for h in source_polynomials]
            for f in source_polynomials
        ]
    )
    assert source_gram == s.diag(s.Rational(9, 2), 3 * s.sqrt(15) / 4, s.Rational(15, 2))

    return {
        "scope": __doc__,
        "witness": "(Q1 dot Q2) times the product coarse Gaussian, SU(2)",
        "coarse_excitation": str(coarse_energy),
        "image_excitation": str(coarse_energy + s.sqrt(5)),
        "witness_norm_squared": str(norm_psi),
        "angular_norm_squared": str(norm_angular),
        "image_norm_squared": str(norm_image),
        "normalized_schur_coefficient": str(schur),
        "normalized_direct_metric_coefficient": str(direct),
        "normalized_net_angular_coefficient": str(net),
        "all_rank_normalized_net": "11*N/40",
        "mixed_shell_denominator_negative_control": True,
        "single_strip_centered_source_gram_SU2": str(source_gram),
        "single_strip_source_squared_norms_general": ["3*d/2", "d*sqrt(15)/4", "5*d/2"],
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


if __name__ == "__main__":
    result = exact_control()
    with (
        Path(__file__)
        .with_name("multistrip_selfenergy_controls.json")
        .open("x", encoding="utf-8") as handle
    ):
        json.dump(result, handle, indent=2)
        handle.write("\n")
    print(json.dumps(result, indent=2))
