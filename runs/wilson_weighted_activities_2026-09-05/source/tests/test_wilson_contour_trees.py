"""Independent labeled-tree and formal recursion checks."""

from fractions import Fraction

from workhouse.wilson_contour_trees import exact_tree_control


def test_marked_tree_recursion_and_connected_majorant():
    result = exact_tree_control()
    assert result["ordered_graphs"] == sum(3**n for n in range(1, 6))
    assert result["coefficient_comparisons"] == 20
    for check in result["comparisons"]:
        assert check["marked_tree_sum"] == check["recursion"]
        assert Fraction(check["connected_unmarked"]) <= Fraction(check["marked_tree_sum"])


def test_repeated_support_requires_the_root_mark():
    result = exact_tree_control()
    assert Fraction(result["repeated_support_marked_quadratic"]) == Fraction(1, 49)
    assert Fraction(result["missing_root_mark_would_give"]) == Fraction(1, 98)
