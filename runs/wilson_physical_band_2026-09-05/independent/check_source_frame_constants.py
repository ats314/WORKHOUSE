"""Exact scalar controls for the literal-source frame derivation.

These rational checks verify only the displayed numerical implications.
They do not certify source locality, the Gram-Schur estimate, an actual
Wilson transfer limit, or the infinite-dimensional onto lemma.
"""

from fractions import Fraction as F
import json


def main() -> None:
    epsilon = F(1, 998)
    gap = F(1024, 15625)
    projection_bound = 2 * epsilon / (gap - 2 * epsilon)
    generator_times_rank = F(568, 145) / 80000
    source_difference = 2160 * F(1, 20000)
    checks = {
        "positive_contour_denominator": gap - 2 * epsilon > 0,
        "projection_distance_below_one_quarter": projection_bound < F(1, 4),
        "generator_bound_times_rank": generator_times_rank <= F(1, 20000),
        "coarse_source_difference": source_difference == F(27, 250),
        "source_difference_below_one_eighth": source_difference < F(1, 8),
        "coefficient_map_neumann_bound": F(1, 4) + F(1, 8) == F(3, 8),
        "lower_frame_bound": (1 - F(1, 4) - F(1, 8)) ** 2 == F(25, 64),
        "upper_frame_bound": (1 + F(1, 8)) ** 2 == F(81, 64),
        "synthesis_inverse_bound": 1 / (1 - F(1, 4) - F(1, 8)) == F(8, 5),
        "minimum_support_four_weight": F(1, 2) ** 4 == F(1, 16),
        "minimum_support_four_moment": 4 * F(1, 2) ** 4 == F(1, 4),
        "gram_schur_synthesis_constant": F(1, 16) * F(1, 4) == F(1, 8) ** 2,
        "extra_coupling_denominator": 1252800000 * 8 == 10022400000,
    }
    assert all(checks.values()), checks
    print(json.dumps({
        "scope": "Exact rational margins only; analytic hypotheses remain explicit.",
        "checks": checks,
        "projection_bound": str(projection_bound),
        "generator_times_rank": str(generator_times_rank),
        "source_difference_bound": str(source_difference),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
