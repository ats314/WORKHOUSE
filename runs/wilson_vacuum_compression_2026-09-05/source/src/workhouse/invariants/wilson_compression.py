"""Exact controls for the sharper local vacuum-compression bound."""

from sympy import I, Rational, SparseMatrix, expand, symbols

from ..wilson_vacuum_chart import product_chart
from ._core import _suite

compression_suite = _suite("the Wilson vacuum correction is exact orthogonal compression")
NOTE = "paper/research_notes/G18_VACUUM_COMPRESSION_BOUND_20260905.md"


def compression_controls() -> dict:
    """A symbolic complex block and a separately computed Wilson tensor model."""
    d, e, k, ell, x, y, z, w, a, b, c, h = symbols("d e k ell x y z w a b c h", real=True)
    kinetic = SparseMatrix([[1, 0, 0], [0, d, k + I * ell], [0, k - I * ell, e]])
    omega = SparseMatrix([1, 0, 0])
    chi = SparseMatrix([0, x + I * y, z + I * w])
    column = chi - kinetic * chi
    residual = SparseMatrix(
        [
            [0, column[1].conjugate(), column[2].conjugate()],
            [column[1], a, b + I * c],
            [column[2], b - I * c, h],
        ]
    )
    generator = chi * omega.H - omega * chi.H
    q = SparseMatrix.eye(3) - omega * omega.H
    corrected = residual + kinetic * generator - generator * kinetic
    symbolic = (corrected - q * residual * q).applyfunc(expand).is_zero_matrix
    model = product_chart(3, ((0, 1), (1, 2)))
    q8 = SparseMatrix.diag(0, *([1] * 7))
    local = model.second_rotated[(1, 1)] == q8 * model.first_rotated[(1, 1)] * q8
    # A scalar vacuum part cannot disappear by this commutator. This control
    # detects accidentally omitting the normalization hypothesis.
    unnormalized = residual + omega * omega.H
    omitted = (
        unnormalized + kinetic * generator - generator * kinetic - q * unnormalized * q
    ).applyfunc(expand)
    return {
        "complex_symbolic_block": symbolic,
        "exact_overlap_model": local,
        "unnormalized_defect_is_vacuum_projector": omitted == omega * omega.H,
    }


@compression_suite.check(
    "the vacuum-column commutator is exactly orthogonal compression QAQ, "
    "with a scalar-normalization negative control",
    "G18; " + NOTE + "; symbolic complex three-state block and exact overlapping tensor model",
)
def _():
    checks = compression_controls()
    return all(checks.values()), (
        f"{checks}; the generic finite-matrix statement is separately Lean-checked. "
        "Operator norm and infinite-dimensional consequences use the analytic proof."
    )


@compression_suite.check(
    "compression and Perron damping sharpen the uniform quadratic bound to "
    "118872/125 times f_star squared",
    "G18; " + NOTE + "; exact combination of the previously proved support census",
)
def _():
    delta = Rational(4, 5)
    compressed = 16 + 2 * 336 + Rational(2592, 5)
    connected = (1 + delta) * (Rational(16, 2) + 336)
    disjoint = Rational(2592, 5) * delta**2
    full = connected + disjoint
    return (
        compressed == Rational(6032, 5)
        and connected == Rational(3096, 5)
        and disjoint == Rational(41472, 125)
        and full == Rational(118872, 125),
        f"QAQ alone: {compressed}; retaining Perron damping: "
        f"{connected} f_star^2 + {disjoint} (J s1)^2 <= {full} f_star^2. "
        "These are sufficient norm-bound constants, not perturbative physical coefficients.",
        {
            "WILSON_CHART_COMPRESSION_SUPPORT_FACTOR": compressed,
            "WILSON_CHART_DAMPED_SUPPORT_FACTOR": full,
        },
    )
