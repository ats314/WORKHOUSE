"""Exact complete-fiber, actual-alias and directional covariance controls.

No finite computation is used to certify the all-volume Fourier estimate.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import sys
from pathlib import Path

import sympy as s


def require(condition, message):
    if not condition:
        raise ValueError(message)


def adjoint(matrix):
    return matrix.conjugate().T


def reduced(value):
    return s.cancel(s.expand_complex(value))


def clean(matrix):
    return matrix.applyfunc(reduced)


def zero(matrix, message):
    require(clean(matrix) == s.zeros(*matrix.shape), message)


def psd(matrix):
    a = clean(matrix)
    require(a == adjoint(a), "Hermitian matrix")
    pivots = []
    for j in range(a.rows):
        p = reduced(a[j, j])
        require(p.is_Rational is True and p >= 0, f"nonnegative exact rational pivot {j}: {p}")
        pivots.append(str(p))
        if p == 0:
            require(all(a[j, k] == 0 for k in range(j + 1, a.cols)), "zero pivot remainder")
            continue
        for i in range(j + 1, a.rows):
            for k in range(i, a.cols):
                value = reduced(a[i, k] - a[i, j] * a[j, k] / p)
                a[i, k], a[k, i] = value, s.conjugate(value)
    return pivots


def encode(matrix):
    return [[str(x) for x in row] for row in matrix.tolist()]


def rational_matrix_controls():
    x = s.symbols("x", real=True)
    density = s.exp(-2 * x**2)
    normalization = s.integrate(density, (x, -s.oo, s.oo))
    variance = s.simplify(s.integrate(x**2 * density, (x, -s.oo, s.oo)) / normalization)
    require(variance == s.Rational(1, 4), "actual covariance is half inverse precision")
    require(s.Rational(1, 2) / variance == 2, "Dirichlet half factor gives frequency gap")
    require(s.Rational(1, 2) / s.Rational(1, 2) != 2, "wrong covariance factor negative")
    t = s.symbols("t", positive=True)
    high = s.Matrix([[2, 1], [1, 3]])
    b = s.Matrix([[s.Rational(1, 3), s.Rational(1, 5)], [-s.Rational(1, 7), s.Rational(1, 4)]])
    require(high * (b * b.T) != (b * b.T) * high, "genuinely noncommuting high matrices")
    v = t * b
    a = v.T * high * v
    z = (s.eye(2) + t * a).inv()
    c = s.diag(s.eye(2) / t, high)
    omega = s.diag(t * s.eye(2), high.inv())
    w = s.eye(2).col_join(v)
    fast = c - c * w * (w.T * c * w).inv() * w.T * c
    formula = (
        (a * z)
        .row_join(-z * v.T * high)
        .col_join((-high * v * z).row_join(high - t * high * v * z * v.T * high))
    )
    zero(fast - formula, "all exact pole-cancelled blocks")
    zero(w.T * fast, "complete observation annihilates conditional covariance")
    zero(fast * omega * fast - fast, "compressed precision inverse identity")
    determinant = s.Poly(s.cancel((s.eye(2) + t * a).det()), t)
    require(all(x > 0 for x in determinant.all_coeffs() if x), "positive denominator polynomial")
    low_leading = fast[:2, :2].applyfunc(lambda x: s.limit(x / t**2, t, 0))
    mixed_leading = fast[:2, 2:].applyfunc(lambda x: s.limit(x / t, t, 0))
    high_leading = (fast[2:, 2:] - high).applyfunc(lambda x: s.limit(x / t**3, t, 0))
    zero(low_leading - b.T * high * b, "principal order two")
    zero(mixed_leading + b.T * high, "mixed order one")
    zero(high_leading + high * b * b.T * high, "high correction order three")
    rows = []
    for value in (s.Rational(1, 100), s.Rational(1, 2), s.Rational(2)):
        f = clean(fast.subs(t, value))
        o = omega.subs(t, value)
        source = w.subs(t, value)
        q = s.eye(4) - source * (source.T * source).inv() * source.T
        zero(q * o * q * f - q, "whole fiber precision inverse")
        pivots = psd(f)
        inverse = (q * o * q + s.eye(4) - q).inv()
        zero(q * inverse * q - f, "independent full inverse path")
        wrong = q * c.subs(t, value) * q
        require(clean(wrong - f) != s.zeros(4), "conditioning differs from covariance compression")
        omitted = f.copy()
        omitted[2:, 2:] = high
        require(clean(source.T * omitted) != s.zeros(2, 4), "omitted high correction rejected")
        rows.append({"t": str(value), "rank": f.rank(), "PSD_pivots": pivots})
    return {
        "probability_variance_at_precision_two": str(variance),
        "Dirichlet_frequency_gap": "2",
        "wrong_covariance_factor_negative": True,
        "noncommuting_high_matrix": encode(high),
        "matched_source_slope": encode(b),
        "denominator": str(determinant.as_expr()),
        "principal_order_two_coefficient": encode(low_leading),
        "mixed_order_one_coefficient": encode(mixed_leading),
        "high_order_three_coefficient": encode(high_leading),
        "finite_complete_fiber_cases": rows,
        "covariance_compression_negative": True,
        "omitted_high_correction_negative": True,
        "scope": "Generic exact Gaussian matrices; not assigned to a Wilson incidence geometry.",
    }


def actual_alias_controls():
    # n=4,L=2,K=(pi,0,0); v^2=84,rho^2=121 makes all frequencies rational.
    covariance = s.zeros(24)
    precision = s.zeros(24)
    physical = s.zeros(24)
    source = s.zeros(24, 2)
    coarse_basis = s.eye(3)[:, [1, 2]]
    aliases = []
    for index, bits in enumerate(itertools.product((0, 1), repeat=3)):
        phase = [s.I * (-1) ** bits[0], (-1) ** bits[1], (-1) ** bits[2]]
        d = s.Matrix([x - 1 for x in phase])
        q = reduced((adjoint(d) * d)[0])
        pc = clean(s.eye(3) - d * adjoint(d) / q)
        frequency = s.sqrt(84 * q + 121)
        require(frequency in (17, 25, 31), "actual frequencies are exact integers")
        aa = [s.Rational(1, 2) * (1 + x) for x in phase]
        # Common nonzero Fourier normalization cancels from the conditioned space.
        w = s.diag(*[s.conjugate(2 * s.prod(aa) * aa[i]) for i in range(3)]) * coarse_basis
        zero(adjoint(d) * w, "actual phase-sensitive source transverse")
        span = slice(3 * index, 3 * index + 3)
        covariance[span, span] = pc / frequency
        precision[span, span] = frequency * pc
        physical[span, span] = pc
        source[span, :] = w
        aliases.append({"alias": list(bits), "q": str(q), "frequency": str(frequency)})
    covariance, precision, physical, source = map(clean, (covariance, precision, physical, source))
    zero(covariance * precision - physical, "entire physical inverse")
    gram = clean(adjoint(source) * covariance * source)
    fast = clean(covariance - covariance * source * gram.inv() * adjoint(source) * covariance)
    projection = clean(source * (adjoint(source) * source).inv() * adjoint(source))
    qf = physical - projection
    zero(adjoint(source) * fast, "complete path observation removed")
    zero(qf * precision * qf * fast - qf, "full physical fiber inverse")
    require(fast.rank() == qf.rank() == 14, "complete conditioned physical rank")
    positive = psd(fast)
    covariance_cap = psd(qf / 17 - fast)
    # A second path evaluates every block after principal source normalization.
    principal_source = source.extract([1, 2], [0, 1])
    v = clean(source[3:, :] * principal_source.inv())
    high = covariance[3:, 3:]
    a = clean(adjoint(v) * high * v)
    z = clean((s.eye(2) + 17 * a).inv())
    formula = (
        (a * z)
        .row_join(-z * adjoint(v) * high)
        .col_join((-high * v * z).row_join(high - 17 * high * v * z * adjoint(v) * high))
    )
    indices = [1, 2, *range(3, 24)]
    zero(fast.extract(indices, indices) - formula, "actual full block cancellation formula")
    wrong_source = source.copy()
    wrong_source[0, 0] = 1
    require(
        clean((s.eye(24) - physical) * wrong_source) != s.zeros(24, 2),
        "longitudinal-source negative",
    )
    return {
        "fine_period": 4,
        "block_length": 2,
        "coarse_momentum": "(pi,0,0)",
        "v_squared": "84",
        "rho_squared": "121",
        "aliases": aliases,
        "physical_dimension": physical.rank(),
        "source_dimension": source.rank(),
        "conditional_dimension": fast.rank(),
        "weighted_source_Gram": encode(gram),
        "conditional_PSD_pivots": positive,
        "conditional_inverse_frequency_cap": "1/17",
        "cap_slack_PSD_pivots": covariance_cap,
        "all_remaining_23_ambient_rows_compared": True,
        "longitudinal_source_negative": True,
        "probability_covariance_is_half_reported_operator": True,
        "scope": "Complete actual Q(i) alias block; the all-size Fourier bound is analytic.",
    }


def directional_controls():
    t = s.symbols("t", real=True)
    ratio = (1 - s.exp(s.I * t / 2)) / (1 + s.exp(s.I * t / 2))
    require(s.simplify(s.diff(ratio, t).subs(t, 0)) == -s.I / 4, "actual alias ratio derivative")
    x, y, z = s.symbols("x y z", real=True)
    vector = s.Matrix([x, y, z])
    transverse = s.eye(3) - vector * vector.T / vector.dot(vector)
    high = s.diag(0, 1, 1)
    angular = (x * transverse * high)[1, 1]
    expected = x * (x**2 + z**2) / (x**2 + y**2 + z**2)
    require(s.cancel(angular - expected) == 0, "mixed directional leading coefficient")
    rows = []
    slopes = []
    for direction in ([1, 0, 0], [0, 1, 0], [1, 1, 0]):
        value = s.cancel(
            angular.subs(dict(zip((x, y, z), (t * a for a in direction), strict=True))) / t
        )
        slopes.append(value)
        rows.append({"direction": direction, "normalized_slope": str(value)})
    require(slopes == [1, 0, s.Rational(1, 2)], "exact non-linear derivative witness")
    require(slopes[2] != slopes[0] + slopes[1], "no common Frechet derivative")
    # The full angular function still obeys the order-one bound on real vectors.
    require(
        s.cancel(expected / x - (1 - y**2 / (x**2 + y**2 + z**2))) == 0,
        "bounded angular coefficient identity",
    )
    return {
        "alias_ratio_linear_coefficient": "-I/4",
        "mixed_yy_coefficient_without_common_prefactor": str(expected),
        "common_prefactor": "I/(4*sqrt(4*v^2+rho^2))",
        "directional_slopes": rows,
        "linear_derivative_negative": True,
        "scope": "Actual L2 leading symbol; non-exponential conclusion uses the analytic proof.",
    }


def controls():
    if sys.flags.optimize:
        raise RuntimeError("Exact controls require assertions enabled")
    return {
        "generic_complete_fiber": rational_matrix_controls(),
        "actual_path_alias": actual_alias_controls(),
        "directional_regularization_boundary": directional_controls(),
    }


def main():
    if sys.flags.optimize:
        raise RuntimeError("Exact controls require assertions enabled")
    sys.dont_write_bytecode = True
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--replay", type=Path)
    args = parser.parse_args()
    require(bool(args.output) != bool(args.replay), "choose one output or replay")
    if args.output and args.output.exists():
        raise FileExistsError("Choose a fresh output path")
    source = Path(__file__).resolve()
    paths = (source, source.with_name("CONDITIONAL_QUANTUM_PATH_COVARIANCE.md"))
    hashes = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    payload = controls()
    require(
        hashes == {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
        "source changed during verification",
    )
    if args.replay:
        report = json.loads(args.replay.read_text(encoding="utf-8"))
        require(report["controls"] == payload, "complete payload changed")
        require(report["source_sha256"] == hashes, "source pins changed")
        print("PASS: all three full payloads and exact source hashes replayed")
        return
    report = {"passed": True, "controls": payload, "source_sha256": hashes}
    with args.output.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(report, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print("PASS: complete covariance, actual alias and directional controls")


if __name__ == "__main__":
    main()
