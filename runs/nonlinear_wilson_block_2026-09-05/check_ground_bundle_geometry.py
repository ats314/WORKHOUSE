"""Exact finite metric and lift controls for the near-I ground-bundle proof.

These check the common rational functions of Ad(H), the first lift
coefficients, and a finite SU(2) Casimir identity. They do not certify
the uniform ground derivative, gap or projected-form theorem.
"""

import json
from pathlib import Path

import sympy as s


def controls():
    if not __debug__:
        raise RuntimeError("Exact controls require assertions enabled")
    q = s.Symbol("q", nonzero=True)
    c = 8 - q**2 - q**-2
    b = (4 - q**-2) / c
    schur = 4 - (4 - q**-2) * (4 - q**2) / c
    assert s.cancel(schur - 15 / c) == 0
    root_derivative = 1 / (1 + q)
    bouquet = (s.Rational(1, 2) - root_derivative) / q
    strip = (b - root_derivative) / q
    bouquet_factor = (q - 1) / (2 * q * (1 + q))
    strip_factor = (q - 1) * (q**2 + 5*q + 1) / (q**2 * c * (1 + q))
    assert s.cancel(bouquet - bouquet_factor) == 0
    assert s.cancel(strip - strip_factor) == 0
    assert bouquet.subs(q, 1) == strip.subs(q, 1) == 0
    # q=exp(t/2), with t the spectral variable of ad(X).
    bouquet_linear = s.diff(bouquet, q).subs(q, 1) / 2
    strip_linear = s.diff(strip, q).subs(q, 1) / 2
    assert bouquet_linear == s.Rational(1, 8)
    assert strip_linear == s.Rational(7, 24)
    # Converting a coarse alpha E tangent and fiber alpha Z/2 chart
    # multiplies either coefficient by 2 alpha.
    assert 2 * strip_linear == s.Rational(7, 12)
    assert 2 * bouquet_linear == s.Rational(1, 4)
    t = s.Symbol("t", real=True)
    shifted_s = (15 / c).subs(q, s.exp(t / 2))
    assert s.simplify(shifted_s.subs(t, -t) - shifted_s) == 0
    assert s.simplify(s.diff(shifted_s, t).subs(t, 0)) == 0
    assert s.simplify(s.diff(shifted_s, t, 2).subs(t, 0)) == s.Rational(5, 6)

    # Spin-one matrices give a noncommuting anisotropic kinetic example.
    # D_a are Haar-skew representation generators; the Casimir is central.
    jx = s.Matrix([[0, 1, 0], [1, 0, 1], [0, 1, 0]]) / s.sqrt(2)
    jy = s.Matrix([[0, -s.I, 0], [s.I, 0, -s.I], [0, s.I, 0]]) / s.sqrt(2)
    jz = s.diag(1, 0, -1)
    derivatives = [s.I * j for j in (jx, jy, jz)]
    casimir = -sum((d * d for d in derivatives), s.zeros(3))
    coefficients = s.Matrix([[2, s.Rational(1, 3), 0],
                             [s.Rational(1, 3), 3, 0], [0, 0, 4]])
    kinetic = -sum((coefficients[a, b] * derivatives[a] * derivatives[b]
                    for a in range(3) for b in range(3)), s.zeros(3)) / 2
    assert casimir == 2 * s.eye(3)
    assert kinetic * casimir == casimir * kinetic
    second_sum = sum(((a*b).adjoint() * (a*b) for a in derivatives
                      for b in derivatives), s.zeros(3))
    assert second_sum == casimir**2
    # The coefficient floor S>=I makes T>=L/2. Check it exactly in
    # this noncommuting example, including the squared graph estimate.
    assert all(value >= 0 for value in (coefficients - s.eye(3)).eigenvals())
    assert all(value >= 0 for value in (kinetic**2 - casimir**2 / 4).eigenvals())
    return {"passed": True, "scope": __doc__,
            "strip_schur_identity": "15/(8-q^2-q^-2)",
            "bouquet_residual_factor": str(s.factor(bouquet)),
            "strip_residual_factor": str(s.factor(strip)),
            "residual_at_identity": ["0", "0"],
            "ad_X_linear_coefficients": [str(bouquet_linear), str(strip_linear)],
            "strip_scaled_Z_coefficient": "7/12",
            "strip_S_second_derivative_at_identity": "5/6",
            "spin_one_casimir": "2 I",
            "exact_second_derivative_sum_equals_L_squared": True,
            "anisotropic_graph_estimate": True}


if __name__ == "__main__":
    target = Path(__file__).with_suffix(".json")
    result = controls()
    with target.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(json.dumps(result, indent=2))
