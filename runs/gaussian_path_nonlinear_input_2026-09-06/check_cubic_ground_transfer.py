"""Independent finite controls; not a certificate of analytic remainders."""

from __future__ import annotations
import argparse
import hashlib
import json
import sys
from pathlib import Path
import sympy as s


def controls():
    imaginary = s.I
    pauli = [s.Matrix([[0, 1], [1, 0]]), s.Matrix([[0, -imaginary], [imaginary, 0]]), s.diag(1, -1)]
    basis = [-imaginary * p / 2 for p in pauli]
    vectors = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 2, 3)]
    mats = [sum((a * t for a, t in zip(v, basis)), s.zeros(2)) for v in vectors]
    word_controls = []
    for word in [(1, 2, -3, -4), (1, 2, 3), (1, 2, -1, -2), (2, -4, 3, 1), (1, 1, 2, 3)]:
        zs = [(1 if i > 0 else -1) * mats[abs(i) - 1] for i in word]
        coeff = [s.eye(2), s.zeros(2), s.zeros(2), s.zeros(2)]
        for z in zs:
            coeff = [
                sum(
                    (coeff[j] * z ** (k - j) / s.factorial(k - j) for j in range(k + 1)), s.zeros(2)
                )
                for k in range(4)
            ]
        actual = -s.re(s.trace(coeff[3]))
        f1 = sum(zs, s.zeros(2))
        f2 = sum((a * b - b * a for i, a in enumerate(zs) for b in zs[i + 1 :]), s.zeros(2)) / 2
        predicted = -s.re(s.trace(f1 * f2))
        assert s.simplify(actual - predicted) == 0
        word_controls.append({"word": word, "cubic": str(actual)})
    assert any(s.Rational(x["cubic"]) != 0 for x in word_controls)
    xs = s.symbols("x0:9", real=True)
    x = s.Matrix(3, 3, xs)
    p = x.det()
    omega = s.Matrix([[3, 1, 0], [1, 4, 1], [0, 1, 5]])
    assert all(omega[:i, :i].det() > 0 for i in range(1, 4))
    drift = sum((omega * x)[i, a] * s.diff(p, x[i, a]) for i in range(3) for a in range(3))
    assert s.expand(drift - 12 * p) == 0
    assert sum(s.diff(p, z, 2) for z in xs) == 0
    first_corrector = -p / 12
    assert (
        s.expand(
            sum(
                (omega * x)[i, a] * s.diff(first_corrector, x[i, a])
                for i in range(3)
                for a in range(3)
            )
            + p
        )
        == 0
    )
    sig = s.Matrix(
        [
            [2, s.Rational(1, 3), s.Rational(1, 5)],
            [s.Rational(1, 3), 3, s.Rational(1, 7)],
            [s.Rational(1, 5), s.Rational(1, 7), 4],
        ]
    )
    contraction = sum(
        sig[i, j] * s.diff(p, x[i, a], x[j, a])
        for i in range(3)
        for j in range(3)
        for a in range(3)
    )
    assert s.expand(contraction) == 0
    broken = s.diff(p, x[0, 0], x[1, 1]) / 5
    assert s.expand(broken - x[2, 2] / 5) == 0
    omega4 = [s.Integer(2), s.Integer(3), s.Integer(5), s.Integer(7)]
    denom = [sum(omega4[j] for j in range(4) if j != i) for i in range(4)]
    assert denom == [15, 14, 12, 10]
    assert s.binomial(2, 3) == 0
    ys = s.symbols("y0:6", real=True)
    y = s.Matrix(2, 3, ys)
    moving = [y.row(0).cross(y.row(1)), 2 * y.row(0).cross(y.row(1))]
    divergence = sum(s.diff(moving[i][a], y[i, a]) for i in range(2) for a in range(3))
    assert s.expand(divergence) == 0
    # Three retained spatial components are needed for a nonzero density cubic.
    zfield = [x.row(1).cross(x.row(2)), s.zeros(1, 3), s.zeros(1, 3)]
    div3 = sum(s.diff(zfield[i][a], x[i, a]) for i in range(3) for a in range(3))
    assert div3 == 0
    source_correction = 2 * sum(x[i, a] * zfield[i][a] for i in range(3) for a in range(3))
    assert s.expand(source_correction - 2 * p) == 0
    # This symmetric tensor is not a group-invariant SU(3) d tensor.
    symmetric = sum(z**3 for z in xs)
    assert sum(s.diff(symmetric, z, 2) for z in xs) != 0
    # Invariance alone does not imply a spatial-rank-two cancellation.
    su3_h = s.diag(1, 1, -2)
    assert s.trace(su3_h**3) == -6
    assert s.re(s.trace((s.I * su3_h) ** 3)) == 0
    return {
        "signed_word_cubic": word_controls,
        "non_diagonal_ground_drift": "12 det(x)",
        "corrector": "-det(x)/12",
        "color_diagonal_contraction": "0",
        "broken_color_contraction": "x8/5",
        "exterior_rank2": 0,
        "rank4_frequency_denominators": [str(a) for a in denom],
        "bracket_source_divergence": "0",
        "moving_source_density_term": "2 det(x)",
        "symmetric_tensor_negative": True,
        "su3_symmetric_invariant_at_one_copy": "Tr(diag(1,1,-2)^3)=-6",
        "actual_antihermitian_real_trace": "0",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if sys.flags.optimize:
        raise RuntimeError("Exact controls require assertions enabled")
    if args.output.exists():
        raise FileExistsError(args.output)
    payload = controls()
    sources = {
        p.name: hashlib.sha256(p.read_bytes()).hexdigest()
        for p in [Path(__file__), Path(__file__).with_name("CUBIC_GROUND_TRANSFER.md")]
    }
    report = {
        "schema": "wilson-cubic-ground-controls/v1",
        "sources": sources,
        "controls": payload,
        "passed": True,
        "scope": "Finite exact coefficients only; first-jet completeness, analytic localization, nonlinear coordinate domains and infinite-volume bounds are not machine-certified.",
    }
    with args.output.open("x", encoding="utf-8") as stream:
        json.dump(report, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(
        "PASS: signed Wilson words, ground forcing, conditional contractions and moving-source term"
    )


if __name__ == "__main__":
    main()
