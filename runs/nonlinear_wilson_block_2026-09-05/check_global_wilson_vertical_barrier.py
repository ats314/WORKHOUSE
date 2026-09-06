"""Exact, finitely scoped controls for the global Wilson fiber comparison.

No numerical eigenvalue routine, rotor truncation or rank interpolation is used.
The controls do not certify the analytic min-max or elliptic-operator premises.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import platform
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
PROOFS = (
    HERE / "GLOBAL_WILSON_VERTICAL_BARRIER.md",
    HERE / "GLOBAL_WILSON_VERTICAL_BARRIER_SHARPENED.md",
    REPO / "paper/research_notes/G19_WILSON_PHYSICAL_FIBER_FAST_GAP_20260905.md",
    REPO / "paper/research_notes/G19_WILSON_STRIP_BO_AND_TWO_STRIP_SPLITTING_20260905.md",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def zero(expression: sp.Expr | sp.MatrixBase, label: str) -> None:
    entries = list(expression) if isinstance(expression, sp.MatrixBase) else [expression]
    require(all(sp.simplify(entry) == 0 for entry in entries), label)


def frobenius2(matrix: sp.MatrixBase) -> sp.Expr:
    return sp.simplify(sp.trace(matrix.adjoint() * matrix))


def psd_minors(matrix: sp.MatrixBase) -> list[str]:
    zero(matrix - matrix.adjoint(), "Hermitian PSD input")
    values = []
    for size in range(1, matrix.rows + 1):
        for indices in itertools.combinations(range(matrix.rows), size):
            value = sp.simplify(matrix.extract(indices, indices).det())
            require(value.is_nonnegative is True, "nonnegative principal minor")
            values.append(str(value))
    return values


def nonnegative_coefficients(expression: sp.Expr, variables: tuple) -> dict:
    """Exact polynomial certificate on the stated nonnegative orthant."""
    numerator, denominator = sp.fraction(sp.cancel(expression))
    num = sp.Poly(numerator, *variables)
    den = sp.Poly(denominator, *variables)
    require(all(c >= 0 for c in num.coeffs()), "numerator coefficient")
    require(all(c >= 0 for c in den.coeffs()), "denominator coefficient")
    require(den.TC() > 0, "strict denominator on the closed orthant")
    return {
        "expression": str(sp.factor(expression)),
        "numerator": str(num.as_expr()),
        "denominator": str(den.as_expr()),
        "domain": "all variables nonnegative",
    }


def abstract_matrix_control() -> dict:
    coordinates = sp.symbols("a b c d e f g h", real=True)
    a, b, c, d, e, f, g, h = coordinates
    first = sp.Matrix([a + sp.I * b, c + sp.I * d])
    second = sp.Matrix([e + sp.I * f, g + sp.I * h])
    inner = (first.adjoint() * second)[0]
    wedge = first[0] * second[1] - first[1] * second[0]
    zero(
        frobenius2(first) * frobenius2(second)
        - sp.expand_complex(inner * sp.conjugate(inner))
        - sp.expand_complex(wedge * sp.conjugate(wedge)),
        "complex Lagrange identity",
    )
    zero(
        2 * (frobenius2(first) + frobenius2(second))
        - frobenius2(first - second)
        - frobenius2(first + second),
        "parallelogram and adjoint root-pair identity",
    )

    # B and Q need not commute; their explicit Gram factors certify positivity.
    left = sp.Matrix([[1, 0], [1, 2], [0, 1]]) / 10
    right = sp.Matrix([[1, 2], [0, 1], [2, -1]]) / 3
    bmat, qmat = left * left.T, right * right.T
    eta = sp.trace(bmat)
    amat = sp.eye(3) - bmat
    require(0 < eta < sp.Rational(1, 2), "near-neighborhood Gram trace")
    require(bmat * qmat != qmat * bmat, "noncommuting PSD example")
    value = sp.trace(amat * qmat) - (1 - eta) * sp.trace(qmat)
    wedge_sum = sum(
        (left[i, ell] * right[j, m] - left[j, ell] * right[i, m]) ** 2
        for ell in range(left.cols)
        for m in range(right.cols)
        for i in range(3)
        for j in range(i + 1, 3)
    )
    zero(value - wedge_sum, "Gram sum of exterior squares")
    require(value > 0, "strict noncommuting trace bound")
    wrong_q = sp.diag(0, -1)
    wrong_b = sp.diag(sp.Rational(1, 4), 0)
    negative = sp.trace(wrong_b) * sp.trace(wrong_q) - sp.trace(wrong_b * wrong_q)
    require(negative == -sp.Rational(1, 4), "missing-Q-positivity negative control")
    return {
        "symbolic_complex_identities": 2,
        "eta": str(eta),
        "noncommuting_trace_margin": str(value),
        "B_principal_minors": psd_minors(bmat),
        "Q_principal_minors": psd_minors(qmat),
        "A_minus_scalar_principal_minors": psd_minors(eta * sp.eye(3) - bmat),
        "missing_Q_positivity_margin": str(negative),
        "scope": "Arbitrary complex two-vector identities and one exact 3x3 PSD model.",
    }


def su2_group_control() -> dict:
    r = sp.Rational
    pauli = (sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.diag(1, -1))
    generators = tuple(-sp.I * item / 2 for item in pauli)
    for i, first in enumerate(generators):
        for j, second in enumerate(generators):
            zero(-2 * sp.trace(first * second) - int(i == j), "Lie metric normalization")
    casimir = -sum((item * item for item in generators), sp.zeros(2))
    zero(casimir - r(3, 4) * sp.eye(2), "fundamental Casimir")
    axis = (r(2, 3), r(1, 3), r(2, 3))
    axis_matrix = sum((axis[i] * pauli[i] for i in range(3)), sp.zeros(2))
    fmat = r(2, 3) * sp.eye(2) + sp.I * (pauli[0] / 3 + 2 * pauli[1] / 3)
    zero(fmat.adjoint() * fmat - sp.eye(2), "rational quaternion unitarity")
    zero(fmat.det() - 1, "rational quaternion special determinant")

    def adjoint(matrix):
        return sp.Matrix(
            3,
            3,
            lambda i, j: sp.simplify(
                -2 * sp.trace(generators[i] * matrix * generators[j] * matrix.adjoint())
            ),
        )

    cases = []
    for cosine, sine in (
        (sp.Integer(1), sp.Integer(0)),
        (r(3, 5), r(4, 5)),
        (sp.Integer(0), sp.Integer(1)),
    ):
        hmat = cosine * sp.eye(2) + sp.I * sine * axis_matrix
        umat, kmat = hmat * hmat, hmat * fmat
        ymat = fmat.adjoint() * hmat
        zero(hmat.adjoint() * hmat - sp.eye(2), "square-root unitarity")
        zero(hmat.det() - 1, "SU(2) square root")
        zero(kmat * ymat - umat, "actual coarse product")
        zero(
            sp.trace(kmat) + sp.trace(ymat) - 4 * cosine * r(2, 3),
            "exact two-character cancellation identity",
        )

        def v(matrix):
            return 2 - sp.re(sp.trace(matrix))

        triangle = 2 * (v(kmat) + v(ymat)) - v(umat)
        zero(
            triangle - frobenius2(sp.eye(2) - 2 * kmat + umat) / 2,
            "unitary product barrier exact remainder",
        )
        require(triangle >= 0, "product barrier positivity")
        rot = adjoint(umat)
        zero(rot.T * rot - sp.eye(3), "adjoint orthogonality")
        metric = 15 * (8 * sp.eye(3) - rot - rot.T).inv()
        dmat = (sp.eye(3) - rot) * (sp.eye(3) - rot.T)
        zero(metric / r(5, 2) - 6 * (6 * sp.eye(3) + dmat).inv(), "exact strip Schur metric ratio")
        ratio = 6 / (6 + 16 * cosine**2 * (1 - cosine**2))
        direction = sp.Matrix(axis)
        expected = r(5, 2) * (ratio * sp.eye(3) + (1 - ratio) * direction * direction.T)
        zero(metric - expected, "longitudinal and transverse metric eigenvalues")
        halfrot = adjoint(hmat)
        zero(halfrot * metric * halfrot.T - metric, "balanced metric translation")
        eigen_bound = psd_minors(4 * v(umat) * sp.eye(3) - dmat)
        cases.append(
            {
                "cos_half_angle": str(cosine),
                "sin_half_angle": str(sine),
                "coarse_v": str(v(umat)),
                "strip_transverse_ratio": str(ratio),
                "product_barrier_margin": str(triangle),
                "adjoint_root_bound_minors": eigen_bound,
                "metric_global_lower_minors": psd_minors(metric - r(3, 2) * sp.eye(3)),
                "metric_global_upper_minors": psd_minors(r(5, 2) * sp.eye(3) - metric),
            }
        )
        if cosine == 0:
            zero(umat + sp.eye(2), "central minus identity coarse value")
            zero(2 * (v(kmat) + v(ymat)) - 8, "fiber constant potential at -I")
            zero(metric - r(5, 2) * sp.eye(3), "central strip metric")
    return {
        "rational_group_cases": cases,
        "fundamental_Casimir": "3/4",
        "central_minus_I_potential_over_u": 8,
        "minus_I_conditional_gaps": {"bouquet": "3/4", "strip": "15/16"},
        "scope": (
            "Exact actual SU(2) group and metric normalization; "
            "Casimir input gives the -I obstruction."
        ),
    }


def scalar_budget_control() -> dict:
    h, k, u, a, e, s, w = sp.symbols("h k u a e s w", nonnegative=True)
    alpha = sp.Rational(8, 3)
    eta = h / (2 * (1 + h))
    epsilon = 1 / (1 + k)
    t = 1 / (1 + alpha * eta)
    zero(1 - t - alpha * eta * t, "exact kinetic loss")
    certificates = {
        "potential_coefficient_dominates_t": nonnegative_coefficients(1 - eta - t, (h,)),
        "metric_t_at_least_3_over_7": nonnegative_coefficients(t - sp.Rational(3, 7), (h,)),
        "cap_below": nonnegative_coefficients(
            t * (epsilon * u - a) + 4 * u * eta - (epsilon * u - a), (h, k, u, a)
        ),
        "cap_above": nonnegative_coefficients(
            t * (epsilon * u + a) + 4 * u * eta - epsilon * u, (h, k, u, a)
        ),
        "lower_v_at_least_3eta": nonnegative_coefficients(4 * eta - 2 * eta**2 - 3 * eta, (h,)),
        "kinetic_loss_at_most_3eta": nonnegative_coefficients(3 * eta - (1 - t), (h,)),
        "near_affine_loss_margin": nonnegative_coefficients(3 * eta / epsilon - (1 - t), (h, k)),
        "near_joint_scalar_margin": nonnegative_coefficients(
            4 * (e / epsilon + s) * eta - (1 - t) * e - s * (4 * eta - w), (h, k, e, s, w)
        ),
        "away_affine_margin": nonnegative_coefficients(e * (epsilon + w) / epsilon - e, (k, e, w)),
    }
    n = sp.symbols("N", positive=True)
    zero(n * (4 / n) - 4, "large-rank cutoff N epsilon = 4")
    # At N=2,3,4 the other branch is epsilon=1; its condition N<=4 is explicit.
    # m follows from the exact energy identity, not an integration surrogate.
    kinetic, center_e, rank = sp.symbols("kinetic center_e rank", nonnegative=True)
    msymbol = sp.symbols("m", real=True)
    zero(
        center_e
        - (kinetic + 4 * u * rank * (1 - msymbol))
        - (center_e - kinetic - 4 * u * rank + 4 * u * rank * msymbol),
        "central-ground energy identity",
    )
    coarse_v = sp.symbols("coarse_v", real=True)
    expected_at_u = 2 * u * ((rank - msymbol * rank) + (rank - msymbol * (rank - coarse_v)))
    expected_center = 4 * u * rank * (1 - msymbol)
    zero(
        expected_at_u - expected_center - 2 * u * msymbol * coarse_v,
        "unbalanced central-ground trial exact potential difference",
    )
    require(sp.Rational(4, 1) / alpha == sp.Rational(3, 2), "cap energy comparison")
    return {
        "alpha": "8/3",
        "epsilon_N": "min(1,4/N)",
        "parameterization": "eta=h/[2(1+h)], epsilon=1/(1+k); endpoints by continuity",
        "certificates": certificates,
        "large_rank_identity": "N*(4/N)=4; small branch N<=4",
        "principal_angle_margin_squared": "(2)^2-(sqrt(2))^2=2>0",
        "trial_potential_difference": "2*u*m*v(U)",
        "scope": (
            "Exact symbolic scalar identities under declared positivity domains; "
            "no spectral sampling."
        ),
    }


def controls() -> dict:
    if not __debug__:
        raise RuntimeError("Optimized Python is rejected for exact verification.")
    return {
        "matrix": abstract_matrix_control(),
        "su2": su2_group_control(),
        "scalar": scalar_budget_control(),
    }


def source_hashes() -> dict[str, str]:
    return {
        str(path.relative_to(REPO)).replace("\\", "/"): hashlib.sha256(
            path.read_bytes()
        ).hexdigest()
        for path in (*PROOFS, Path(__file__).resolve())
    }


def main() -> None:
    if not __debug__:
        raise RuntimeError("Optimized Python is rejected for exact verification.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(f"Refusing to overwrite {args.output}")
    before = source_hashes()
    payload = controls()
    after = source_hashes()
    require(before == after, "source bytes stable during computation")
    report = {
        "schema": "workhouse-global-wilson-vertical-controls/v1",
        "scope": (
            "Finite exact algebra and group controls, not an all-rank spectral theorem certificate."
        ),
        "runtime": {
            "python": platform.python_version(),
            "sympy": sp.__version__,
            "platform": platform.platform(),
            "optimized": False,
        },
        "sources": before,
        "controls": payload,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(report, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(json.dumps({"output": str(args.output), "families": list(payload), "passed": True}))


if __name__ == "__main__":
    main()
