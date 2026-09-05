"""Precisely scoped finite controls for the physical scale-block continuation."""

from fractions import Fraction

from sympy import Rational, simplify, sqrt, sympify

from ..continuum_wilson_block import exact_block_controls
from ..continuum_wilson_rotor import exact_rotor_controls
from ._core import _suite

continuum_block_suite = _suite("physical Wilson blocks: exact metric, rotor and shell controls")
NOTES = "paper/research_notes/"
GRADIENT = NOTES + "G19_CONDITIONAL_GRADIENT_REPAIR_20260905.md"
ROTOR = NOTES + "G19_WILSON_PHYSICAL_FIBER_FAST_GAP_20260905.md"
SHELLS = NOTES + "G19_WILSON_TWO_SQUARE_PHYSICAL_SHELLS_20260905.md"
BO = NOTES + "G19_WILSON_STRIP_BO_AND_TWO_STRIP_SPLITTING_20260905.md"


@continuum_block_suite.check(
    "conditional Gaussian covariance is sharp in the quotient metric and retains a nonzero score",
    GRADIENT + " sections 1-5; finite covariance and Lie algebra controls",
)
def conditional_gradient_check():
    result = exact_block_controls()["conditional_gradient"]
    return (
        result["quotient_average_sizes"] == [2, 4, 16]
        and result["unweighted_average_negative_control_factor"] == 16
        and result["two_coarse_commutator_norm_squared"] == "1",
        "Exact inversion recovers the sharp two-coordinate Gaussian covariance. "
        "Three averaging maps attain contraction in the quotient metric; the unweighted "
        "16-coordinate average has factor 16. Lie traces retain the mixed quartic and "
        "a nonzero two-coarse commutator. No global conditional or RG estimate is certified.",
    )


@continuum_block_suite.check(
    "the actual strip metric and Gaussian contractions give the declared "
    "Born-Huang and vertical shifts",
    BO + " sections 1-4; symbolic jets and exact ranks 2, 3, 4",
)
def born_oppenheimer_check():
    result = exact_block_controls()
    return (
        result["metric_jets"]["vertical_kinetic_at_identity"] == "5/4"
        and [row["N"] for row in result["lie_gaussian_contractions"]] == [2, 3, 4]
        and simplify(
            sympify(result["scalar_constants"]["ground_derivative_norm_coefficient"])
            - 49 / (144 * sqrt(5))
        )
        == 0,
        "The co-metric is expanded before completing its square. Exact Lie/Gaussian "
        "contractions recover the vertical shift, 49N/(96sqrt(5)) Born-Huang coefficient, "
        "coarse angular metric and Haar scalar. These finite coefficient controls do not "
        "machine-certify the analytic ground-state asymptotics.",
    )


@continuum_block_suite.check(
    "joint Gauss cancellation holds in mixed polynomial controls "
    "and physical source limits are orthogonal",
    SHELLS + "; finite invariant polynomial and Gaussian source controls",
)
def physical_gauss_and_sources_check():
    result = exact_block_controls()
    gauss = result["physical_gauss"]
    sources = result["two_strip_selfenergy"]
    return (
        gauss["jointly_invariant_polynomials"] == 7
        and gauss["arbitrary_function_divergence_identity"]
        and gauss["noninvariant_negative_control"] != "0"
        and sources["single_strip_source_squared_norms_general"]
        == ["3*d/2", "d*sqrt(15)/4", "5*d/2"],
        "Seven invariant polynomials, including mixed terms, have zero first coupling; "
        "an arbitrary-function divergence identity is checked symbolically in SU(2), and a "
        "noninvariant polynomial retains a nonzero coupling. The centered Q², Q·Z, Z² "
        "Gaussian source Gram matrix is diagonal. Full group parity and source asymptotics "
        "remain analytic statements.",
    )


@continuum_block_suite.check(
    "four SU2 intrinsic rotor enclosures replay by integer Sturm signs and a tail Schur bound",
    ROTOR + " and the sealed rotor operator derivation; exact fixed-u certificate replay",
)
def intrinsic_rotor_check():
    result = exact_rotor_controls()
    rows = result["replayed_enclosures"]
    return (
        [row["u"] for row in rows] == ["1", "100", "10000", "1000000"]
        and result["normalization"]["haar_inner_products"] == 25
        and result["corrupted_interval_rejected"]
        and not result["numerical_eigensolver_used"]
        and all(Fraction(row["gap_over_sqrt_u_interval"][1]) < 4 for row in rows),
        "Nine character degrees and 25 Haar products fix the Casimir normalization. "
        "Integer determinant signs accept four untruncated fixed-u class-rotor gap "
        "enclosures using the explicit analytic tail comparison; an altered interval is "
        "rejected. No eigensolver participates in acceptance, and this is not an OS "
        "complement or continuum-gap certificate.",
    )


@continuum_block_suite.check(
    "original seven-link product logarithms independently reproduce "
    "the SU2 radial and mixed corrections",
    BO + " original-link independent control; exact Gaussian Rayleigh coefficients",
)
def original_link_check():
    result = exact_block_controls()["original_seven_link_SU2"]
    return (
        result["balanced_comparison_difference"] == "0"
        and Rational(result["product_log_self_energy"]) == Rational(1, 10)
        and Rational(result["mixed_minus_radial"]) == Rational(201, 320),
        "A separate calculation starts from the seven-link left/right derivatives in "
        "original face logarithms, with quartic and Haar terms. Its distinct self-energy "
        "coefficient 1/10 gives the same radial gap correction and mixed/local splitting "
        "201/320. This certifies coefficients, not the global asymptotic remainder.",
    )


@continuum_block_suite.check(
    "the two-strip on-shell self-energy leaves a positive angular term "
    "and splits the first singlet shell",
    BO + " sections 6-7; exact finite oscillator effective matrices",
)
def multistrip_shell_check():
    result = exact_block_controls()
    coupling, shell = result["two_strip_selfenergy"], result["first_shell_SU2_matrix"]
    return (
        Rational(coupling["normalized_net_angular_coefficient"]) == Rational(11, 20)
        and coupling["mixed_shell_denominator_negative_control"]
        and Rational(shell["mixed_minus_local"]) == Rational(201, 320)
        and Rational(shell["omitted_metric_negative_control_split"]) < 0,
        "Exact Gaussian polynomial action verifies the on-shell denominator sqrt(5), "
        "self-energy -49/80 and net angular coefficient 11/80. Symbolic-rank moments and "
        "the full SU(2) 3×3 effective matrix yield splitting (54N²-15)/(160N). Mixed-energy "
        "and omitted-metric negative controls fail as required. Analytic localization "
        "and quasimode remainder estimates are not machine-certified.",
    )
