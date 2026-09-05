"""Exact finite controls accompanying the analytic weighted Wilson chart."""

from sympy import Rational

from ..wilson_contour_trees import exact_tree_control
from ..wilson_creator_velocity import exact_controls
from ._core import _suite

creator_velocity_suite = _suite("the Wilson weighted chart: exact creator velocity controls")
CHART = "paper/research_notes/G18_WILSON_CARDINALITY_UNITARY_CHART_20260905.md"
BOUND = "paper/research_notes/G18_WILSON_WEIGHTED_ACTIVITY_BOUND_20260905.md"


@creator_velocity_suite.check(
    "22 finite creator-tangent columns agree with independent tensor matrices "
    "and real-linear inversion transports the normalized vacuum line",
    "G18; " + CHART + " section 2; exact 3x3x2 and complex 3x2 finite tensor controls",
)
def _():
    models = exact_controls()["models"]
    ok = sum(model["map_columns_checked"] for model in models) == 22 and all(
        model["independent_exponential_and_map"]
        and model["real_linear_inverse_residual_zero"]
        and model["normalized_vacuum_line_transport"]
        for model in models
    )
    return ok, (
        "Support convolution and direct rank-one tensor matrices agree for all 22 columns. "
        "Exact inverses solve b-K conjugate(b)=dot(w), including entangled overlapping creators. "
        "The two finite spaces check the algebra, not the volume-uniform analytic theorem."
    )


@creator_velocity_suite.check(
    "two exact rooted matrix contraction certificates bound nonzero four-term Neumann remainders",
    "G18; " + CHART + " equations (1)-(3); finite coefficient-l1 rooted norm controls",
)
def _():
    models = exact_controls()["models"]
    constants = [Rational(model["finite_rooted_matrix_bound"]) for model in models]
    ok = constants == [Rational(1321, 112500), Rational(123, 5000)] and all(
        model["neumann_remainder_nonzero"]
        and model["neumann_remainder_within_bound"]
        and 0
        < Rational(model["neumann_remainder_norm"])
        <= Rational(model["neumann_remainder_bound"])
        for model in models
    )
    return ok, (
        "Column-anchor certificates bound the finite rooted coefficient-l1 operator norms by "
        "1321/112500 and 123/5000. Exact nonzero four-term remainders lie below q^4/(1-q) "
        "times the tangent norm. These finite bounds are independent of the analytic "
        "general estimate."
    )


@creator_velocity_suite.check(
    "the creator chart factorizes on four disjoint tensor links and a complex one-link path "
    "has the exact vacuum phase 1/198",
    "G18; " + CHART + " section 2.2; component and phase controls",
)
def _():
    result = exact_controls()
    factor = result["factorization"]
    phase = result["phase_control"]
    return (
        all(
            factor[key]
            for key in (
                "global_inverse_equals_embedded_local_inverses",
                "cross_component_velocities_zero",
                "generator_is_tensor_sum",
                "creation_exponential_factorizes",
            )
        )
        and phase["line_transport_exact"]
        and phase["normalized_vector_phase_rate"] == "1/198",
        "The four-link global inverse equals the embedded component inverses, "
        "with no cross-component "
        "velocity. For w=1/10 and dot(w)=i/20, b=5i/99 and S psi-dot(psi)=i psi/198. "
        "Thus general complex paths require vacuum-line transport with its scalar phase.",
    )


@creator_velocity_suite.check(
    "connected ordered contour words equal partition cumulants through degree three "
    "with noncommuting overlap projectors",
    "G18; " + BOUND + " section 4; three binary links and two ordered insertion intervals",
)
def _():
    contour = exact_controls()["ordered_contour"]
    return (
        contour["connected_words_equal_partition_cumulants"]
        and contour["connected_words_per_order"] == [0, 0, 6, 24]
        and Rational(contour["overlap_commutator_frobenius_squared"]) == Rational(3, 4),
        "Independent matrix powers with partition subtraction equal 6 quadratic and 24 cubic "
        "connected ordered words. The edge-projector commutator has Frobenius square 3/4. "
        "This finite polynomial control preserves ordering and kinetic contractions; it does not "
        "certify convergence of the general contour expansion.",
    )


@creator_velocity_suite.check(
    "exact rational majorant consequences give creator velocity 1/6, activity 1/2500 "
    "and full-operator bound 1/998 below the shell threshold",
    "G18; " + CHART + " section 3 and " + BOUND + " section 5; stated transcendental premises",
)
def _():
    bounds = exact_controls()["scalar_bounds"]
    ok = (
        Rational(bounds["chart_contraction_upper"]) == Rational(3, 16)
        and Rational(bounds["chart_velocity_upper"]) == Rational(1, 6)
        and Rational(bounds["primitive_upper"]) < Rational(1, 2500)
        and Rational(bounds["full_operator_upper"]) == Rational(1, 998)
        and Rational(bounds["full_operator_upper"]) < Rational(bounds["relative_gap_threshold"])
    )
    return ok, (
        "Exact arithmetic checks q<=1/10000, E<=(568/145)q<1/2500, "
        "eta/[2(1/5-eta)]<=1/998<512/78125, and the creator bounds 9/64, 3/16, 1/6. "
        "The elementary exponential/logarithmic inequalities and the analytic majorant formulas "
        "are explicit premises, not conclusions of this rational check."
    )


@creator_velocity_suite.check(
    "363 labeled overlap graphs reproduce 20 marked-tree coefficients "
    "through degree five at four roots",
    "G18; " + BOUND + " section 4; exact Kirchhoff enumeration versus formal tree recursion",
)
def _():
    trees = exact_tree_control()
    ok = (
        trees["ordered_graphs"] == 363
        and trees["coefficient_comparisons"] == 20
        and all(
            row["marked_tree_sum"] == row["recursion"]
            and Rational(row["connected_unmarked"]) <= Rational(row["marked_tree_sum"])
            for row in trees["comparisons"]
        )
        and Rational(trees["repeated_support_marked_quadratic"]) == Rational(1, 49)
        and Rational(trees["missing_root_mark_would_give"]) == Rational(1, 98)
    )
    return ok, (
        "Kirchhoff spanning-tree counts on 363 ordered overlap graphs agree with "
        "20 formal exponential-recursion coefficients. Connected unmarked coefficients "
        "are bounded by the marked-tree sums. A repeated support gives 1/49; omitting "
        "its root multiplicity gives the incorrect 1/98. Scope: finite degrees one to five."
    )
