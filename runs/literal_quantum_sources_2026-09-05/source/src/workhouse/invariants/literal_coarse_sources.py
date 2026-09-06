"""Finite exact evidence for literal-source and whole-complement mechanisms."""

from fractions import Fraction

from ..literal_coarse_sources import exact_literal_coarse_controls
from ._core import _suite

literal_coarse_suite = _suite("literal coarse sources: vacuum, Gauss, score and quantum complement")
NOTES = "paper/research_notes/"
LITERAL = NOTES + "G19_WILSON_LITERAL_VACUUM_COARSE_SOURCES_20260905.md"
GAUSS = NOTES + "G19_WILSON_COMMON_GAUSS_LITERAL_FAST_FLOOR_20260905.md"
SCORE = NOTES + "G19_GROUND_MARGINAL_SCHUR_SCORE_20260905.md"
GAUSSIAN = NOTES + "G19_GAUSSIAN_QUANTUM_FAST_SOURCES_20260905.md"
CENTER = NOTES + "G19_TRUE_GROUND_CENTER_SCORE_OBSTRUCTION_20260905.md"


@literal_coarse_suite.check(
    "true weighted vacuum sources preserve the exact coarse form and vacuum subtraction",
    LITERAL + " literal isometry, projection and ground-state transform; finite graph control",
)
def literal_form_check():
    result = exact_literal_coarse_controls()["literal"]["literal_weighted_graph"]
    return (
        result["source_Gram_equals_marginal"]
        and result["vacuum_in_literal_range_exact"]
        and result["coarse_conductance"] == "11"
        and result["raw_uniform_projection_not_idempotent"]
        and result["omitted_vacuum_shift"] == "13",
        "An exact connected four-point weighted graph has a positive nonproduct true "
        "vacuum, the actual marginal source Gram, and coarse conductance 11. Replacing "
        "the marginal by uniform weights breaks idempotence; omitting the vacuum "
        "shift leaves energy 13. This checks the finite ground transform, not Wilson "
        "elliptic domains, its literal asymptotic, or an OS history identification.",
    )


@literal_coarse_suite.check(
    "vacuum-exact copies preserve compressed and full inverse-energy floors",
    LITERAL + " complete low-space leakage, independent copies and inverse-energy addendum; "
    "finite controls",
)
def independent_copy_check():
    result = exact_literal_coarse_controls()["literal"]
    rows = result["tensor_leakage"]["models"]
    inverse = exact_literal_coarse_controls()["literal_inverse"]
    return (
        [row["copies"] for row in rows] == [1, 2, 3]
        and all(row["compressed_floor"] == "127/25" and row["floor_attained"] for row in rows)
        and result["unbounded_multiplier_counterexample"]["norm_error_limit"] == "0"
        and result["unbounded_multiplier_counterexample"]["multiplied_error_limit"] == "4"
        and inverse["passed"]
        and inverse["full_form_floor"] == "175/37"
        and inverse["restricted_compression_floor"] == "127/25"
        and Fraction(inverse["wrong_full_floor_determinant"]) < 0,
        "Exact one-, two- and three-copy leakage Grams retain the vacuum and refined "
        "floor 127/25; full compression PSD is checked for one and two copies. The "
        "complete additive low spectrum is accounted for. A symbolic sequence converges "
        "in L2 but its unboundedly multiplied error tends to 4, verifying why bounded "
        "cutoffs precede the limit. An independent inverse-energy calculation gives "
        "the full form floor 175/37, rejects promoting 127/25 beyond QHQ, and yields "
        "a whole-window frame bound 27/175. All-copy and Wilson limits remain analytic.",
    )


@literal_coarse_suite.check(
    "common Gauss pair singlets retain orthogonal leakage and exclude the higher chirality shell",
    GAUSS + " equivariant projection, complete low supports and refined floor; finite SO3 model",
)
def common_gauss_check():
    result = exact_literal_coarse_controls()["common_gauss"]
    return (
        [row["copies"] for row in result["tensor_controls"]] == [1, 2, 3, 5]
        and result["uniform_refined_floor"] == "191/50"
        and Fraction(result["three_adjoint_chirality_energy"])
        > Fraction(result["common_gauss_threshold"])
        and Fraction(result["wrong_vacuum_losses"][-1]) > Fraction(99, 100),
        "A rational nine-dimensional local SO(3) model directly checks equivariance, "
        "radial and pair-singlet leakage and arbitrary low-support superpositions for "
        "1/2/3/5 copies. The floor 191/50 is attained. A genuine three-adjoint invariant "
        "is above the chosen threshold, while rotating the vacuum creates product "
        "loss. This is finite representation algebra, not Wilson localization or "
        "an interacting-volume theorem.",
    )


@literal_coarse_suite.check(
    "intrinsic conditional score retains connection terms and the sharp full-gap factor",
    SCORE + " sections 2-4; exact noncommuting Fisher, torus and two-state controls",
)
def intrinsic_score_check():
    result = exact_literal_coarse_controls()["score"]
    return (
        result["passed"]
        and result["nonzero_connection_torus"]["exact_cross_form"] == "-1/8"
        and result["nonzero_connection_torus"]["omitted_density_connection_negative_control"]
        and result["nonzero_connection_torus"]["omitted_divergence_negative_control"]
        and result["sharp_gap_model"]["wrong_fisher_factor_rejected"],
        "A noncommuting positive metric/Fisher matrix verifies the covariance cap. "
        "An exactly integrated compact torus model has cross form -1/8 and needs "
        "both density-connection and fiber-divergence terms. A two-state matrix "
        "attains the sharp gap, rejects a missing factor two, and obeys the Schur "
        "sandwich. No uniform Wilson score, marginal gap or full-Q premise is certified.",
    )


@literal_coarse_suite.check(
    "inverse-frequency source geometry controls all particles in the checked tensor sectors",
    GAUSSIAN + " sections 2-4; exact matrix bridge and one-through-four particle controls",
)
def gaussian_complement_check():
    result = exact_literal_coarse_controls()["gaussian"]
    return (
        len(result["matrix_chains"]) == 2
        and all(row["source_geometry_noncommuting"] for row in result["matrix_chains"])
        and [row["particles"] for row in result["tensor_sectors"]["sectors"]] == [1, 2, 3, 4],
        "Two noncommuting rational matrix models verify the full stiffness premise, "
        "inverse-frequency source map, compressed inverse and full frequency floor. "
        "Exact PSD elimination in ordered tensor sectors 1 through 4 checks both "
        "the fast-number bound and the entire complement. Restriction to symmetric "
        "bosons is valid; operator monotonicity, Wick density and all-sector "
        "second quantization remain the analytic proof's responsibility.",
    )


@literal_coarse_suite.check(
    "complete Gaussian low windows distinguish physical wrong-source weights "
    "and retained zero modes",
    GAUSSIAN + " sections 5-8; full finite window, physical counterexample and regulator controls",
)
def gaussian_source_scope_check():
    result = exact_literal_coarse_controls()["gaussian"]
    return (
        result["full_low_window"]["low_dimension"] == 26
        and result["full_low_window"]["proven_frame_lower"] == "3/4"
        and Fraction(result["wrong_source_physical_counterexample"]["rayleigh"])
        == Fraction(803, 1364)
        and result["wrong_source_physical_counterexample"]["color_rotation_derivatives_zero"]
        and result["retained_zero_mode_regulator"]["zero_mode_variance_diverges"]
        and not result["retained_zero_mode_regulator"]["unregulated_Gaussian_vacuum_claimed"],
        "The complete 26-state window contains every slow occupation 0 through 25 "
        "and has source frame at least 3/4. A ten-boson wrong-weight complementary "
        "trial has exact quotient 803/1364 below the proposed unit floor; its degree-ten "
        "SO(3) invariant color lift is checked explicitly. Four rational regulated "
        "models retain their fast floor while the zero-mode variance diverges. No "
        "unregulated vacuum, nonlinear Wilson or all-history source theorem is inferred.",
    )


@literal_coarse_suite.check(
    "central true-ground score retains Haar drift and the actual horizontal metric",
    CENTER + " exact Riccati, Haar and SU2 geometry controls; reconstructed trial scope",
)
def central_score_obstruction_check():
    result = exact_literal_coarse_controls()["central_score"]
    trial = result["positive_reconstructed_trial"]
    geometry = result["SU2_geometry"]
    return (
        result["passed"]
        and result["wilson_scalar_identity"]["actual_bouquet_a"] == 4
        and trial["mean_s_squared"] == "96/113"
        and trial["mean_d_squared"] == "4/113"
        and trial["omitted_Haar_drift_rejected"]
        and trial["not_a_Wilson_ground"]
        and geometry["fundamental_Casimir"] == "3/4"
        and geometry["per_axis_Fisher"] == "E(s^2)/12"
        and len(geometry["cases"]) == 3,
        "Symbolic Riccati subtraction and normalized radial Haar integration retain "
        "the Fisher coefficients 64/3, -16/3 and a/2. Three rational SU(2) points "
        "check the original-link metric, horizontal half-connection and class-angle "
        "derivatives; exact axis integration gives I/3. A positive reconstructed "
        "trial has moments 96/113 and 4/113, rejects omitted Haar drift, and is "
        "explicitly not a Wilson ground. The actual Wilson linear-u obstruction "
        "uses its analytic positive-ground equation and O(sqrt(u)) energy bound.",
    )
