"""Exact finite controls for Gaussian OS history observability.

These check finite covariance, incidence, and invariant-polynomial identities.
They do not certify the general Fock-density theorem or a nonlinear Wilson RG.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as s


def require(statement: bool, message: str) -> None:
    if not statement:
        raise RuntimeError(message)


def main() -> dict:
    rows = []
    omega = s.Matrix([[2, 1], [1, 2]])
    b = s.Matrix([[1, 0]])
    covariance = (2 * omega).inv()
    # h=log(2); the two eigenvalues of exp(-h Omega) are 1/2 and 1/8.
    transfer = s.Matrix([[s.Rational(5, 16), -s.Rational(3, 16)],
                         [-s.Rational(3, 16), s.Rational(5, 16)]])
    require(omega * transfer == transfer * omega, "sampled transfer commutator")
    require(set(transfer.eigenvals()) == {s.Rational(1, 2), s.Rational(1, 8)},
            "sampled transfer eigenvalues")
    krylov = b.T.row_join(omega * b.T)
    sampled = b.T.row_join(transfer * b.T)
    require(krylov.det() == 1 and sampled.det() == -s.Rational(3, 16),
            "continuous or sampled observability determinant")
    cn = [(b * covariance * transfer**n * b.T)[0] for n in range(5)]
    require(all(cn[n] == s.Rational(1, 4) * s.Rational(1, 2)**n
                + s.Rational(1, 12) * s.Rational(1, 8)**n for n in range(5)),
            "two-frequency covariance decomposition")
    os_gram = s.Matrix([[cn[0], cn[1]], [cn[1], cn[2]]])
    require(os_gram.det() > 0, "two sampled histories fail to see both frequencies")
    rows.append({"check": "one equal-time coordinate reconstructs two frequencies",
                 "passed": True, "krylov_det": str(krylov.det()),
                 "sampled_det": str(sampled.det()),
                 "reflected_gram_det": str(os_gram.det()),
                 "markov_covariance_defect": str(cn[0] * cn[2] - cn[1]**2)})

    degenerate = 2 * s.eye(2)
    selected = s.Matrix([[1, -1]])
    require(b.T.row_join(degenerate * b.T).rank() == 1,
            "degenerate frequency rank obstruction")
    require(selected.T.row_join(omega * selected.T).rank() == 1,
            "exact eigenspace selection rank obstruction")
    rows.append({"check": "degenerate and exactly unobserved frequency controls",
                 "passed": True, "ranks": [1, 1]})

    # Original seven-link strip cycle Gram, with one shared edge of opposite sign.
    cycles = s.Matrix([[1, 1, 1, 1, 0, 0, 0],
                       [-1, 0, 0, 0, 1, 1, 1]])
    c = cycles * cycles.T
    require(c == s.Matrix([[4, -1], [-1, 4]]), "seven-link cycle Gram")
    w1, w2, eps = s.symbols("w1 w2 eps", real=True)
    weights = s.diag(w1, w2)
    coarse = s.Matrix([1, 1])
    raw_det = s.factor(coarse.row_join(weights * c * coarse).det())
    require(s.expand(raw_det - 3 * (w2 - w1)) == 0,
            "weighted strip observability")
    a = s.Matrix([[3, s.sqrt(15) * eps], [s.sqrt(15) * eps, 5]])
    observed = s.Matrix([s.sqrt(3), 0])
    white_det = s.simplify(observed.row_join(a * observed).det())
    require(white_det == 3 * s.sqrt(15) * eps, "white-coordinate determinant")
    lam = s.symbols("lam")
    require(s.factor(a.charpoly(lam).as_expr())
            == lam**2 - 8 * lam + 15 - 15 * eps**2,
            "weighted frequency polynomial")
    high_lambda = 4 + s.sqrt(1 + 15 * eps**2)
    high_residue = 3 / (4 * s.sqrt(high_lambda)) * (1 - 1 / s.sqrt(1 + 15 * eps**2))
    residue_coefficient = s.simplify(s.limit(high_residue / eps**2, eps, 0))
    require(residue_coefficient == 9 * s.sqrt(5) / 8,
            "small observed high-frequency residue")
    require(s.simplify(2 * s.sqrt(5) - s.sqrt(3) - s.sqrt(5)).is_positive,
            "mixed physical singlet should precede the pure fiber singlet")
    rows.append({"check": "actual weighted seven-link strip",
                 "passed": True, "raw_det": str(raw_det),
                 "white_det": str(white_det),
                 "frequency_polynomial": str(a.charpoly(lam).as_expr()),
                 "high_residue_epsilon2_coefficient": str(residue_coefficient),
                 "symmetric_complement_energy": "sqrt(3)+sqrt(5)",
                 "intrinsic_fiber_class_energy": "2*sqrt(5)"})

    # Frequencies 1,2 and h=log(2): the three quadratic rates are 2,3,4.
    nodes = [s.Rational(1, 4), s.Rational(1, 8), s.Rational(1, 16)]
    factors = [s.Integer(1), s.Integer(2), s.Integer(1)]
    quadratic = s.Matrix([[factors[j] * nodes[j]**k for j in range(3)]
                          for k in range(3)])
    require(quadratic.det() != 0, "quadratic singlet reconstruction")
    require(quadratic.inv() * quadratic == s.eye(3), "exact quadratic inverse")
    rows.append({"check": "three regular times separate all quadratic singlets",
                 "passed": True, "determinant": str(quadratic.det()),
                 "inverse": [[str(v) for v in row] for row in quadratic.inv().tolist()]})

    coords = s.symbols("x0:3 y0:3 z0:3")
    x, y, z = [s.Matrix(coords[j:j+3]) for j in (0, 3, 6)]
    chirality = s.expand(x.row_join(y).row_join(z).det())
    vectors = [x, y, z]
    for axis in range(3):
        e = s.eye(3)[:, axis]
        rotation_derivative = sum(
            sum((e.cross(v))[k] * s.diff(chirality, v[k]) for k in range(3))
            for v in vectors)
        require(s.expand(rotation_derivative) == 0, "chirality Gauss invariance")
    reflect = {v[0]: -v[0] for v in vectors}
    require(s.expand(chirality.subs(reflect, simultaneous=True) + chirality) == 0,
            "chirality reflection parity")
    qform = s.expand((2*x + 3*y + 5*z).dot(2*x + 3*y + 5*z))
    require(s.expand(qform.subs(reflect, simultaneous=True) - qform) == 0,
            "radial observable reflection parity")
    omega3 = s.diag(1, 2, 3)
    b3 = s.Matrix([2, 3, 5])
    observable3 = b3.row_join(omega3 * b3).row_join(omega3**2 * b3)
    require(observable3.det() != 0 and chirality != 0,
            "three-mode physical-algebra negative control")
    rows.append({"check": "one-particle observability does not imply arbitrary physical cyclicity",
                 "passed": True, "three_mode_krylov_det": str(observable3.det()),
                 "chirality": str(chirality),
                 "simultaneous_rotation_derivatives": ["0", "0", "0"],
                 "chirality_reflection_parity": -1,
                 "radial_reflection_parity": 1})

    payload = {"passed": all(row["passed"] for row in rows),
               "exact_check_count": len(rows), "checks": rows,
               "scope": "Finite exact controls only; the accompanying note proves the general OS/Fock statements."}
    target = Path(__file__).with_name("gaussian_os_observability_controls.json")
    target.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"passed": payload["passed"], "exact_check_count": len(rows),
                      "output": str(target)}, indent=2))
    return payload


if __name__ == "__main__":
    main()
