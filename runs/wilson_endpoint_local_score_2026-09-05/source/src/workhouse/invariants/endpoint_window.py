"""Scoped finite controls for endpoint spectra and localized quantum sources."""

from fractions import Fraction

import sympy as sp

from ..endpoint_window import exact_endpoint_window_controls
from ._core import _suite

endpoint_window_suite = _suite("literal endpoint spectra and localized true-ground sources")
NOTES = "paper/research_notes/"
ENDPOINT = NOTES + "G19_LITERAL_ENDPOINT_COMPLETE_WINDOW_20260905.md"
SCORE = NOTES + "G19_TRUE_GROUND_LOCALIZED_WILSON_SCORE_20260905.md"
GRADIENT = NOTES + "G19_LOCAL_GRADIENT_EXCITATION_SUPPORT_20260905.md"
PATH = NOTES + "G19_LOCAL_COVARIANT_AVERAGED_PATH_SOURCES_20260905.md"


@endpoint_window_suite.check(
    "complete finite endpoint cluster retains the vacuum and all high source directions",
    ENDPOINT + " sections 2-3.1; exact five-state model",
)
def complete_cluster_check():
    r = exact_endpoint_window_controls()["endpoint"]["endpoint_and_two_lag"]
    return (
        r["fine_energies"] == [0, 1, 4, 9, 20]
        and r["source_dimension"] == 4
        and r["complete_low_rank"] == 3
        and Fraction(r["full_fast_coefficient"]) > 4
        and [x["full_count"] for x in r["threshold_counts"]] == [1, 2, 3],
        "A rational five-state Hamiltonian has an exact vacuum, a complete rank-three "
        "low window and a genuinely high retained source. Exact PSD/inertia checks "
        "verify the full inverse-energy floor, source frame and all three sorted "
        "threshold counts. Infinite spectral calculus, Wilson limits and uniform "
        "copy statements remain analytic.",
    )


@endpoint_window_suite.check(
    "two exact time lags and a complete discarded cap determine strict spectral counts",
    ENDPOINT + " section 3.1 and section 5; finite matrix extension of the prior excited bridge",
)
def two_lag_memory_check():
    r = exact_endpoint_window_controls()["endpoint"]["endpoint_and_two_lag"]
    return (
        r["different_lags_noncommuting"]
        and r["pre_log_dyadic_order"]
        and Fraction(r["actual_discarded_transfer"])
        <= Fraction(r["proven_discarded_transfer_bound"])
        and all(
            x["lower_count"] == x["upper_count"] == x["full_count"] for x in r["threshold_counts"]
        ),
        "Exact normalized two-lag moments have nonzero rank-one leakage and do not "
        "commute. The full omitted transfer satisfies the derived cap. At three "
        "strict thresholds the finite lower and matrix-resolvent upper indices equal "
        "the complete fine count. The leakage identity predates this note; the new "
        "combination uses a complete source frame. No unverified infinite tail is supplied.",
    )


@endpoint_window_suite.check(
    "genuine compressed Markov paths and marginal energy cutoffs expose distinct failures",
    ENDPOINT + " sections 5-6; finite reversible path and separate self-adjoint countermodels",
)
def endpoint_boundary_check():
    r = exact_endpoint_window_controls()["endpoint"]
    return (
        r["Markov_log_counterexample"]["log_transition_13_first_order"] == "-tau^2/4"
        and r["Markov_log_counterexample"]["negative_Markov_rate_for_small_positive_tau"]
        and r["marginal_cutoff_counterexample"]["source_frame_limit"] == "1"
        and r["marginal_cutoff_counterexample"]["marginal_energy_limit"] == "infinity",
        "A four-point reversible path gives a negative off-diagonal coefficient "
        "-tau^2/4 in its compressed transition logarithm. Separately, an exact "
        "self-adjoint source family has overlap tending to one and increasing "
        "full fast floor while its marginal-generator energy diverges. The latter "
        "family is not asserted Wilson or Markov. Neither endpoint positivity nor "
        "L2 overlap supplies a local Markov logarithm or a marginal energy cutoff.",
    )


@endpoint_window_suite.check(
    "the conditional physical-clock loss obeys its rational summable majorant",
    ENDPOINT + " section 7; eight finite steps and a symbolic scalar identity",
)
def conditional_clock_check():
    r = exact_endpoint_window_controls()["endpoint"]["conditional_clock_budget"]
    return (
        len(r["finite_steps"]) == 8
        and all(Fraction(x["loss"]) <= Fraction(2, (x["j"] + 1) ** 2) for x in r["finite_steps"])
        and 0 < Fraction(r["finite_gap_factor"]) < 1,
        "Eight exact spacings/time steps and an arbitrary-symbol denominator "
        "identity verify the proposed inverse-gap budget. The convergent infinite "
        "product is an analytic consequence under the stated hierarchy hypotheses. "
        "No interacting hierarchy, locality, Euclidean limit or mass trajectory is constructed.",
    )


@endpoint_window_suite.check(
    "actual leading SU2 metric and invariant vacuum forcing retain the connection coefficient",
    SCORE + " sections 1-2; finite order-two Lie algebra",
)
def localized_metric_check():
    r = exact_endpoint_window_controls()["localized_score"]
    return (
        r["metric"]["coarse_constant"] == 6
        and r["metric"]["balanced_residual_linear_coefficient"] == "7/24"
        and r["metric"]["centralizer_annihilated"]
        and r["ground_forcing"]["invariant_gaussian_order_g_forcing"] == 0
        and sp.sympify(r["ground_forcing"]["noninvariant_gaussian_negative"]) != 0,
        "Exact SU2 adjoint-matrix Taylor algebra gives coarse metric 6I and residual "
        "connection 7 ad_Q/24. Invariant Gaussian forcing cancels; an anisotropic "
        "Gaussian supplies a nonzero negative control. These are finite coefficients, "
        "not certification of the fixed-SU(N) true-ground Sobolev expansion or its remainder.",
    )


@endpoint_window_suite.check(
    "localized score contractions distinguish class cancellation from common Gauss pairs",
    SCORE + " sections 4-6; exact SU2 Gaussian covariance and Schur exponents",
)
def localized_score_check():
    r = exact_endpoint_window_controls()["localized_score"]
    return (
        sp.simplify(sp.sympify(r["fisher"]["conditional_coefficient"]) - 49 / (72 * sp.sqrt(5)))
        == 0
        and r["fisher"]["radial_contraction"] == 0
        and r["common_gauss"]["independent_score_variance"] == 2
        and r["schur"] == {"general_relative_power_g": 2, "local_class_relative_power_g": 4},
        "Exact covariance yields 49 ad_Q*ad_Q/(72 sqrt(5)); its radial contraction "
        "vanishes. A pair satisfies total Gauss cancellation while its independent "
        "fiber variances add to 2. Scalar substitution gives relative powers g^2 "
        "and g^4 under the analytic fast-floor/remainder hypotheses. The control "
        "does not prove those hypotheses or bound the high retained space.",
    )


@endpoint_window_suite.check(
    "complete centered radial and pair profiles retain the local bad-gradient bound",
    GRADIENT + " sections 1-3 and 5; finite exact tensor forms",
)
def local_gradient_support_check():
    r = exact_endpoint_window_controls()["local_gradient"]
    return (
        r["uniform_relative_bound"] == "1/20"
        and [x["copies"] for x in r["tensor_cases"]] == [1, 2, 3, 5]
        and all(x["offdiagonal_zero"] for x in r["tensor_cases"])
        and r["noncentered_profile_negative_cross"] == "1/10",
        "All Gram and form entries for 1/2/3/5 copies are computed, including "
        "overlapping pair singlets and nonzero local radial/color mixing. Exact "
        "centering cancels cross terms and preserves the relative cap 1/20 on "
        "arbitrary full-profile superpositions. Removing centering creates cross "
        "term 1/10. All-copy and actual Wilson derivative conclusions remain analytic.",
    )


@endpoint_window_suite.check(
    "an any-bad event fails while componentwise centered score variances add",
    GRADIENT + " sections 4-6; exact product-event and score controls",
)
def componentwise_gradient_check():
    r = exact_endpoint_window_controls()["local_gradient"]
    rows = r["global_bad_event_counterexample"]
    return (
        [x["copies"] for x in rows] == [1, 2, 3, 5, 10]
        and all(x["sum_local_bad_gradient_ratio"] == "0" for x in rows)
        and Fraction(rows[-1]["global_bad_gradient_ratio"]) > Fraction(9, 10)
        and Fraction(r["centered_product_score_squared_norm"]) > 0,
        "Exact independent-event enumeration makes the global any-bad gradient "
        "ratio exceed 9/10 at ten copies although every active local bad-gradient "
        "ratio is zero. Centered product-score covariance is independently summed. "
        "This isolates the necessary componentwise mechanism without certifying "
        "an interacting factorization, Wilson cutoff rate or infinite-volume bound.",
    )


@endpoint_window_suite.check(
    "actual averaged path sources obey gauge covariance cochain restriction and transverse rank",
    PATH + " sections 2-4; exact n4 L2 incidence and noncommuting SU2 holonomies",
)
def covariant_path_check():
    r = exact_endpoint_window_controls()["covariant_path"]["geometry"]
    return (
        r["period"] == 4
        and r["block_length"] == 2
        and r["coarse_transverse_rank"] == 17
        and r["four_exact_cochain_identities"]
        and r["two_cube_support"]
        and r["real_space_fourier_plane_wave_equalities"] == 1536
        and r["retained_constant_amplitudes"] == ["1/4"] * 3
        and r["naive_box_transverse_defect_nonzero_entries"] > 0
        and len(r["noncommuting_gauge_covariances"]) == 2,
        "The exact n=4,L=2 original-link path matrix obeys both cochain squares "
        "and anchor cancellation, has transverse rank 17, retains all three "
        "harmonic directions and matches 1536 direct plane-wave evaluations. Two "
        "noncommuting SU2 configurations verify gauge covariance; naive box means "
        "fail transversality. Path averages are matrix-valued and need not be "
        "unitary. The all-size rank/source theorem remains analytic.",
    )


@endpoint_window_suite.check(
    "all finite complex Fourier blocks satisfy the full physical source floor",
    PATH + " sections 4-6; exact Qi full matrices and independent alias controls",
)
def covariant_fourier_floor_check():
    payload = exact_endpoint_window_controls()
    r = payload["covariant_path"]["fourier"]
    independent = payload["fourier_alias"]
    return (
        r["exact_field"] == "Q(i)"
        and r["full_form_constant"] == "1/132"
        and len(r["all_eight_alias_blocks"]) == 8
        and r["false_constant_100_rejected"]
        and r["pi_upper_integer_margin"] > 0
        and len(independent["moment_cases"]) == 12
        and independent["transverse_alias_case"]["tail_to_principal_ratio"] == "3"
        and independent["transverse_alias_case"]["missing_direction_factor_divergence_squared"]
        == "1/2",
        "Exact Hermitian elimination in all eight 24x24 Q(i) blocks checks the "
        "full finite inequality K >= (P_C-P_S)/132 and rejects constant 100. An "
        "independent enumeration checks alias moments at lengths 1 through 12, "
        "a transverse eight-alias lift and the omitted-direction defect 1/2. "
        "The all-size constant 1/(33 L^2), inverse-frequency Gaussian source "
        "identification and regulated full-Fock conclusion are analytic; no "
        "unregulated vacuum or nonlinear coarse law is certified.",
    )
