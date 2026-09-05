"""Exact finite checks of the ordered-contour rooted-tree coefficients.

Enumerated labeled overlap graphs (Kirchhoff cofactors) are compared with
formal exponential recursion. This checks marking and factorials through
degree five; the all-orders operator norm theorem is an analytic proof.
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import factorial

import sympy as sp


def _exponential_coefficients(coefficients, degree):
    """Formal exp with zero constant input, using its differential equation."""
    result = [Fraction(1)]
    for n in range(1, degree + 1):
        result.append(sum(k * coefficients[k] * result[n - k] for k in range(1, n + 1)) / n)
    return result


def _tree_recursion(supports, weights, degree):
    answer = [[Fraction(0)] * (degree + 1) for _ in supports]
    for n in range(1, degree + 1):
        for i, support in enumerate(supports):
            exponent = [
                sum(answer[j][k] for j, other in enumerate(supports) if support & other)
                for k in range(degree)
            ]
            answer[i][n] = weights[i] * _exponential_coefficients(exponent, n - 1)[n - 1]
    return answer


def _spanning_trees(word, supports):
    if len(word) == 1:
        return 1
    laplacian = sp.zeros(len(word))
    for i in range(len(word)):
        for j in range(i):
            if supports[word[i]] & supports[word[j]]:
                laplacian[i, i] += 1
                laplacian[j, j] += 1
                laplacian[i, j] -= 1
                laplacian[j, i] -= 1
    return int(laplacian[:-1, :-1].det())


@lru_cache(maxsize=1)
def exact_tree_control():
    """Check every coefficient at four roots through five insertion orders."""
    supports = (frozenset((0, 1)), frozenset((1, 2)), frozenset((2, 3)))
    weights = (Fraction(1, 7), Fraction(1, 11), Fraction(1, 13))
    degree = 5
    recursion = _tree_recursion(supports, weights, degree)
    tree_sums = [[Fraction(0)] * (degree + 1) for _ in range(4)]
    connected_sums = [[Fraction(0)] * (degree + 1) for _ in range(4)]
    graph_count = 0
    connected_count = 0
    for n in range(1, degree + 1):
        for word in product(range(len(supports)), repeat=n):
            graph_count += 1
            trees = _spanning_trees(word, supports)
            if not trees:
                continue
            connected_count += 1
            weight = Fraction(1, factorial(n))
            for label in word:
                weight *= weights[label]
            for root in range(4):
                marks = sum(root in supports[label] for label in word)
                if marks:
                    connected_sums[root][n] += weight
                    tree_sums[root][n] += weight * marks * trees
    comparisons = []
    for root in range(4):
        for n in range(1, degree + 1):
            expected = sum(recursion[i][n] for i, support in enumerate(supports) if root in support)
            actual = tree_sums[root][n]
            connected = connected_sums[root][n]
            if actual != expected or connected > actual:
                raise AssertionError((root, n, actual, expected, connected))
            comparisons.append(
                {
                    "root": root,
                    "degree": n,
                    "connected_unmarked": str(connected),
                    "marked_tree_sum": str(actual),
                    "recursion": str(expected),
                }
            )
    # Two equal support labels give one edge, two root marks, and a 1/2!
    # simplex factor. This is the smallest witness that the factor matters.
    repeated_support_marked_quadratic = weights[0] ** 2
    if repeated_support_marked_quadratic == repeated_support_marked_quadratic / 2:
        raise AssertionError("Factorial negative control became degenerate")
    return {
        "scope": "Finite tree marking and factorial identities, not the all-orders operator bound",
        "degree": degree,
        "ordered_graphs": graph_count,
        "connected_graphs": connected_count,
        "coefficient_comparisons": len(comparisons),
        "comparisons": comparisons,
        "repeated_support_marked_quadratic": str(repeated_support_marked_quadratic),
        "missing_root_mark_would_give": str(repeated_support_marked_quadratic / 2),
    }
