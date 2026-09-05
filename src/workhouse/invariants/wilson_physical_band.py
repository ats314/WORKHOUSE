"""Finite exact controls accompanying the analytic complete physical-band theorem."""

from sympy import Rational

from ..wilson_physical_band import exact_controls
from ._core import _suite

physical_band_suite = _suite("the complete Wilson band: finite source and projection controls")
PROOF = "paper/research_notes/G18_WILSON_INFINITE_VOLUME_PHYSICAL_BAND_20260905.md"


@physical_band_suite.check(
    "an exact rational rotated band has a direct rotation and a two-sided projected-source inverse",
    PROOF + " section 5; finite four-dimensional operator algebra",
)
def projector_check():
    result = exact_controls()["rotated_band"]
    certificates = [
        value
        for key, values in result.items()
        if key.endswith("principal_minors")
        for value in values
    ]
    return (
        result["direct_rotation_and_two_sided_inverse_verified"]
        and Rational(result["coefficient_map_determinant"]) != 0
        and all(Rational(value) >= 0 for value in certificates),
        "Exact matrix multiplication verifies direct rotation, both inverse identities "
        "on the band, "
        "and principal-minor certificates for operator/projection errors and both Gram bounds. "
        "This finite model does not certify the infinite-dimensional onto theorem.",
    )


@physical_band_suite.check(
    "a tagged centered finite source family obeys the Gram-Schur bound "
    "and removing centering fails",
    PROOF + " section 4; ten-site sparse tensor vectors",
)
def gram_check():
    result = exact_controls()["source_gram"]
    negative = result["uncentered_negative_control"]
    return (
        Rational(result["gram_schur_bound"]) == Rational(49, 15625)
        and Rational(result["synthesis_norm_upper"]) == Rational(7, 125)
        and result["overlap_inner_product_nonzero"]
        and result["disjoint_centered_inner_products_zero"]
        and Rational(negative["actual_gram_norm"]) > Rational(negative["invalid_centered_bound"]),
        "Four centered terms with three retained source anchors give tagged norm 56/125 and "
        "synthesis norm at most 7/125. Eight disjoint uncentered terms give Gram norm 1/1250, "
        "violating the inapplicable centered bound 1/2500. These are finite vector controls.",
    )


@physical_band_suite.check(
    "a noncommuting four-link transfer agrees with disjoint-activity exhaustion "
    "and local tail certificates",
    PROOF + " section 2.2; exact finite exhaustion mechanism",
)
def exhaustion_check():
    result = exact_controls()["activity_exhaustion"]
    return (
        result["nonzero_activities"] == 6
        and result["disjoint_families"] == 8
        and result["activity_families_killed_by_local_vacuum"] == 1
        and Rational(result["overlap_commutator_frobenius_squared"]) > 0
        and result["nonzero_two_activity_product"]
        and [row["tail_is_nonzero"] for row in result["exhaustions"]] == [True, True, False]
        and all(
            Rational(value) >= 0
            for row in result["exhaustions"]
            for value in row["tail_principal_minors"]
        ),
        "Direct positive congruence matrices equal the expansion of six connected activities "
        "in eight disjoint families. One family vanishes on the local input vacuum; a two-activity "
        "product survives. Three induced exhaustions have exact local tail PSD certificates, "
        "including two nonzero tails. This checks finite action; the infinite-limit "
        "argument remains analytic.",
    )


@physical_band_suite.check(
    "finite source controls distinguish a Gram lower bound, small columns and complete synthesis",
    PROOF + " section 5; completeness negative controls",
)
def completeness_negative_check():
    result = exact_controls()["negative_controls"]
    return (
        result["rectangular_shift_gram_identity"]
        and result["rectangular_shift_missing_vector"] == "e_0"
        and result["column_error_norm"] == "1/8"
        and result["synthesis_error_norm"] == "1"
        and result["unitary_cycle_lengths_checked"] == [5, 9],
        "A rectangular shift has identity Gram but omits e0. A 64-column source map has "
        "column errors 1/8 while its synthesis error is one and it has a kernel. Finite unitary "
        "cycles verify the prefixes of the abstract strong-limit shift counterexample.",
    )


@physical_band_suite.check(
    "exact source and gap margins yield a Gram lower bound above 9/16 and inverse norm below 6/5",
    PROOF + " sections 3-5; rational implications",
)
def scalar_check():
    result = exact_controls()["scalar_margins"]
    return (
        Rational(result["projection_bound"]) < Rational(1, 9)
        and Rational(result["source_difference_bound"]) < Rational(27, 250) < Rational(1, 8)
        and Rational(result["gram_lower"]) == Rational(312481, 419904) > Rational(9, 16)
        and Rational(result["inverse_bound"]) == Rational(648, 559) < Rational(6, 5),
        "The actual norm constants imply projection distance below 1/9, and the source "
        "majorant implies error below 27/250. Rational arithmetic gives Gram bound "
        "312481/419904 and inverse bound 648/559. Analytic and transcendental premises "
        "are retained explicitly; these inequalities do not prove those premises.",
    )
