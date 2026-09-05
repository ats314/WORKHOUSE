"""Finite exact controls supporting the harmonic and conditional scale proofs."""

from fractions import Fraction

from ..continuum_scale_comparison import exact_scale_controls
from ..continuum_scale_periodic import exact_periodic_controls
from ._core import _suite

continuum_scale_suite = _suite("continuum scale comparison: boundary, history and Schur controls")
NOTES = "paper/research_notes/"
CELL = NOTES + "G19_WILSON_FINITE_CELL_GAP_AND_BOUNDARY_FORM_20260905.md"
BOUNDARY = NOTES + "G19_WILSON_HARMONIC_BOUNDARY_COMPARISON_20260905.md"
OBSERVABILITY = NOTES + "G19_GAUSSIAN_OS_HISTORY_OBSERVABILITY_20260905.md"
FORM = NOTES + "G19_FORM_SCHUR_SCALE_COMPARISON_20260905.md"
PERIODIC = NOTES + "G19_WILSON_THREE_DIMENSIONAL_HARMONIC_BOUNDARY_20260905.md"


@continuum_scale_suite.check(
    "original-link incidence recovers the quotient metric and retains the discrete IMS defect",
    CELL + " sections 2-5; " + BOUNDARY + " finite original-link controls",
)
def original_link_metric_check():
    result = exact_scale_controls()
    cell = result["finite_cell"]
    return (
        len(result["original_link_incidence"]) == 6
        and len(cell["rectangle_controls"]) == 4
        and cell["transverse_projector_identities"]
        and Fraction(cell["localized_pure_gradient_negative_control"]) > 0,
        "Six exact link complexes recover curl-gradient cancellation, full cycle rank and "
        "inverse face metric. Four finite spectra and a transverse projector verify the "
        "normalization. The discrete IMS identity retains its row bound, while localizing "
        "a pure gradient creates positive energy. General finite-cell asymptotics and "
        "physical invariant-tensor multiplicities remain analytic statements.",
    )


@continuum_scale_suite.check(
    "retained interface squares give exact finite fast floors and a literal face-source factor",
    BOUNDARY + " sections 3-6; finite gluing, LDL and source controls",
)
def retained_boundary_check():
    result = exact_scale_controls()
    rows = result["retained_boundary_gluing"]
    source = result["spectral_frame_and_source_coordinates"]
    return (
        len(rows) == 4
        and all(row["retained_interface_squares"] > 0 for row in rows)
        and [row["box_side"] for row in result["local_rational_Poincare_LDL"]] == [2, 3, 4]
        and source["wrong_outer_boundary_zero_mode_negative_control"],
        "Four tiled rectangles keep every interface and exterior boundary square; exact "
        "Sturm counts meet the retained-dimension bounds. Rational LDL certificates at "
        "box sides 2, 3, 4 and one exact low-mode frame control verify finite cases. The "
        "literal face-source factor is kept separate from an electric dual coordinate. "
        "These checks do not certify all sizes, nonlinear errors or an OS complement.",
    )


@continuum_scale_suite.check(
    "noncommuting Gaussian blocks retain exact memory and replay rational spectral enclosures",
    FORM + " Gaussian oscillator corollary; finite exact matrix and Sturm controls",
)
def gaussian_memory_check():
    result = exact_scale_controls()["gaussian_memory"]
    return (
        result["passed"]
        and len(result["certificates"]) == 2
        and result["positive_frequency_samples"] == result["shifted_frequency_samples"] == 3,
        "One rational noncommuting block verifies the complete Schur resolvent identity, "
        "graph norm and six Loewner sample bounds. Two sorted eigenvalue comparisons "
        "replay from rational isolating intervals by Sturm counts; no numerical eigensolver "
        "participates. The dimension-independent spectral theorem is proved analytically.",
    )


@continuum_scale_suite.check(
    "sampled Gaussian histories see frequencies that one equal-time coordinate omits",
    OBSERVABILITY + " finite covariance, observability and weighted-strip controls",
)
def history_observability_check():
    result = exact_scale_controls()["os_observability"]
    rows = result["checks"]
    return (
        result["passed"]
        and Fraction(rows[0]["reflected_gram_det"]) > 0
        and rows[1]["ranks"] == [1, 1]
        and rows[2]["symmetric_complement_energy"] == "sqrt(3)+sqrt(5)",
        "Exact sampled covariance has a positive two-history Gram determinant, including "
        "both normal frequencies. Degenerate and unobserved eigenspaces retain rank one. "
        "The weighted seven-link strip has the stated determinant and high-frequency "
        "residue. Its mixed physical singlet lies below the pure fiber class excitation. "
        "Finite observability does not machine-certify Fock density or nonlinear blocking.",
    )


@continuum_scale_suite.check(
    "quadratic singlet reconstruction does not erase an unobserved physical chirality",
    OBSERVABILITY + " physical-algebra limits; finite invariant polynomial controls",
)
def physical_source_algebra_check():
    rows = exact_scale_controls()["os_observability"]["checks"]
    return (
        Fraction(rows[3]["determinant"]) != 0
        and Fraction(rows[4]["three_mode_krylov_det"]) != 0
        and rows[4]["simultaneous_rotation_derivatives"] == ["0", "0", "0"]
        and rows[4]["chirality_reflection_parity"] == -1
        and rows[4]["radial_reflection_parity"] == 1,
        "Three regular times exactly invert the quadratic singlet Vandermonde matrix. "
        "A separate three-mode SU(2) polynomial is Gauss invariant and odd under reflection, "
        "while the radial observed algebra is even despite full one-particle observability. "
        "This finite countercontrol distinguishes linear observability from physical "
        "source cyclicity; it does not assert a literal Wilson-source identification.",
    )


@continuum_scale_suite.check(
    "closed-form Schur controls retain the graph norm, vacuum and entire low-window frame",
    FORM + " rational matrix, graph-frame and inverse-budget controls",
)
def closed_form_scale_check():
    result = exact_scale_controls()["closed_form_schur"]
    return (
        len(result["noncommuting_shift_controls"]) == 3
        and result["vacuum_graph_dimension"] == 1
        and result["whole_window"]["rank"] == result["whole_window"]["onto_rank"] == 2
        and Fraction(result["whole_window"]["frame_lower"]) == Fraction(85701591, 86415616)
        and result["large_cross_term"]["omitted_mass_false_bound"] == "1/2",
        "Rational matrices check the shifted square and inertia at three energies, a "
        "dressed vacuum and complete rank-two low-window graph frame. Omitting the graph "
        "norm gives a false scalar lower bound. An eight-step rational inverse-energy "
        "budget verifies the conditional recursion. General closed forms, infinite-rank "
        "onto and the actual Wilson scale hypotheses remain analytic or open as stated.",
    )


@continuum_scale_suite.check(
    "periodic three-dimensional links retain Hodge, interface and harmonic-mode constraints",
    PERIODIC + " finite integer, rational Green-kernel and explicit fast-field controls",
)
def periodic_harmonic_boundary_check():
    result = exact_periodic_controls()
    rows = result["periodic_controls"]
    return (
        result["d1_d0_and_d2_d1_zero"]
        and result["exact_componentwise_Hodge"]
        and result["positive_interface_decomposition"]
        and result["short_period_requires_separate_convention"]
        and [row["link_count"] for row in rows] == [81, 192]
        and all(row["harmonic_cochain_directions_retained"] == 3 for row in rows)
        and rows[1]["projected_box_tail_nonzero_entries"] == 88,
        "Periods 3 and 4 verify complete integer Hodge/Bianchi and interface matrices, "
        "a rational Fourier Green pseudoinverse, selected Coulomb projections, three "
        "retained harmonic directions and explicit fast fields. The eight-box witness "
        "has 88 projected entries outside its raw support. These finite controls do not "
        "compute the full retained projection or certify the all-size bound, an "
        "unregulated Gaussian vacuum, a nonlinear quantum fast gap or an OS block map.",
    )
