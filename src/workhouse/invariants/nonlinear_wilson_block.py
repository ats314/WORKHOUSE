"""Finitely scoped exact controls for nonlinear single Wilson blocks."""

from fractions import Fraction

from ..nonlinear_wilson_block import exact_nonlinear_controls
from ._core import _suite

nonlinear_wilson_suite = _suite("nonlinear Wilson block: global barriers and ground geometry")
NOTES = "paper/research_notes/"
GLOBAL = NOTES + "G19_WILSON_GLOBAL_VERTICAL_BARRIER_20260905.md"
BUNDLE = NOTES + "G19_WILSON_GROUND_BUNDLE_RELATIVE_FORM_20260905.md"
COMPLEMENT = NOTES + "G19_WILSON_ACTUAL_BLOCK_FAST_COMPLEMENT_20260905.md"


@nonlinear_wilson_suite.check(
    "noncommuting positive trace comparison retains its required positivity hypotheses",
    GLOBAL + " sections 2-4; finite matrix and symbolic Lagrange controls",
)
def positive_trace_check():
    result = exact_nonlinear_controls()["matrix"]
    return (
        result["symbolic_complex_identities"] == 2
        and Fraction(result["noncommuting_trace_margin"]) > 0
        and Fraction(result["missing_Q_positivity_margin"]) == Fraction(-1, 4),
        "Two arbitrary-symbol complex vector identities and one noncommuting rational "
        "3x3 Gram model verify the trace comparison and positive principal minors. "
        "Removing positivity of the second factor gives the exact margin -1/4. "
        "This certifies algebraic controls, not the SU(N) elliptic or min-max theorem.",
    )


@nonlinear_wilson_suite.check(
    "actual SU2 fiber metrics expose the central conditional-gap obstruction",
    GLOBAL + " sections 4 and 7; exact rational group, adjoint and Casimir controls",
)
def actual_fiber_metric_check():
    result = exact_nonlinear_controls()["su2"]
    return (
        len(result["rational_group_cases"]) == 3
        and result["fundamental_Casimir"] == "3/4"
        and result["central_minus_I_potential_over_u"] == 8
        and result["minus_I_conditional_gaps"] == {"bouquet": "3/4", "strip": "15/16"},
        "Three exact SU(2) group points verify the original product, character identity, "
        "strip Schur metric, adjoint bound and balanced translation. At product -I "
        "the potential is exactly 8u, while the normalized Casimir gives conditional "
        "gaps 3/4 and 15/16. The controls do not establish a uniform nonlinear full "
        "fast compression or substitute the class gap at generic coarse holonomy.",
    )


@nonlinear_wilson_suite.check(
    "symbolic fiber budgets preserve spectral caps and the joint Wilson potential",
    GLOBAL + " sections 3-6; exact scalar controls with explicit domains",
)
def spectral_budget_check():
    result = exact_nonlinear_controls()["scalar"]
    return (
        result["alpha"] == "8/3"
        and result["epsilon_N"] == "min(1,4/N)"
        and len(result["certificates"]) == 9
        and result["trial_potential_difference"] == "2*u*m*v(U)",
        "Nine rational-function certificates have nonnegative polynomial coefficients "
        "on their stated parameter domains. They retain the strip metric loss, cap "
        "and affine budgets, joint Wilson coefficient and unbalanced trial identity. "
        "No rotor eigenvalue, infinite-dimensional min-max premise, ground positivity "
        "or full-block vacuum subtraction is machine-certified by these controls.",
    )


@nonlinear_wilson_suite.check(
    "ground-bundle lift geometry retains the anisotropic Casimir graph estimate",
    BUNDLE + " exact lift, vertical metric and finite spin-one controls",
)
def ground_bundle_geometry_check():
    result = exact_nonlinear_controls()["ground_bundle"]
    return (
        result["passed"]
        and result["residual_at_identity"] == ["0", "0"]
        and result["ad_X_linear_coefficients"] == ["1/8", "7/24"]
        and result["strip_S_second_derivative_at_identity"] == "5/6"
        and result["exact_second_derivative_sum_equals_L_squared"]
        and result["anisotropic_graph_estimate"],
        "Symbolic rational functions verify the exact strip metric and residual lifts, "
        "including coefficients 1/8, 7/24 and the scaled 7/12. A noncommuting spin-one "
        "matrix model verifies the Casimir second-derivative identity and squared "
        "graph bound by exact principal minors. The uniform quantum-ground derivative "
        "and relative form theorem remain analytic statements.",
    )


@nonlinear_wilson_suite.check(
    "complete low-space leakage preserves vacuum-subtracted compression and the mixed singlet",
    COMPLEMENT + " finite rational projection and physical Hermite controls",
)
def actual_complement_mechanism_check():
    result = exact_nonlinear_controls()["actual_complement"]
    return (
        result["passed"]
        and len(result["rational_cases"]) == 3
        and result["normalized_projection_energy_limit"] == "44"
        and result["scaled_compressed_floor_limit"] == "7"
        and result["physical_mixed_harmonic_excitation"] == "sqrt(3)+sqrt(5)"
        and result["mixed_polynomial_Gauss_invariant"]
        and result["no_inference_that_P_contains_true_vacuum"],
        "Three rational four-state examples retain full-vacuum subtraction, leakage of "
        "the complete low subspace and the projected-trial energy cost. Exact scalar "
        "limits are 44 and 7 in that finite model. A three-component polynomial is "
        "Gauss invariant and has mixed oscillator energy sqrt(3)+sqrt(5). These checks "
        "do not certify convergence of the actual Wilson ground projection, its "
        "infinite-dimensional compression asymptotic or any volume-uniform extension.",
    )
