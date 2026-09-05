"""Exact rational controls for the contour/tree majorant and final constants."""

from fractions import Fraction as F
from itertools import product
from math import factorial
import json


def exp_series(series):
    assert series[0] == 0
    result = [F(0)] * len(series)
    result[0] = F(1)
    for n in range(1, len(series)):
        result[n] = sum(k * series[k] * result[n-k] for k in range(1, n+1)) / n
    return result


def connected(word, supports):
    reached = {0}
    while True:
        enlarged = reached | {
            j for j in range(len(word))
            if any(supports[word[j]] & supports[word[k]] for k in reached)
        }
        if enlarged == reached:
            return len(reached) == len(word)
        reached = enlarged


def tree_control():
    supports = [{0, 1}, {1, 2}, {2, 3}]
    degree = 7
    b = F(1, 250)  # e^(kappa |A|) a_A, with kappa=log(2), a_A=1/1000.
    trees = [[F(0)] * (degree + 1) for _ in supports]
    # Height truncation stabilizes every coefficient through the target degree.
    for _ in range(degree):
        updated = []
        for support in supports:
            children = [sum(trees[j][n] for j, other in enumerate(supports) if support & other)
                        for n in range(degree + 1)]
            exponential = exp_series(children)
            updated.append([F(0)] + [b * exponential[n-1] for n in range(1, degree+1)])
        trees = updated
    comparisons = 0
    for root in range(4):
        total_connected = F(0)
        total_tree = F(0)
        for n in range(1, degree+1):
            count = sum(
                1 for word in product(range(len(supports)), repeat=n)
                if any(root in supports[j] for j in word) and connected(word, supports)
            )
            connected_coefficient = F(count, factorial(n)) * b**n
            tree_coefficient = sum(trees[j][n] for j, support in enumerate(supports) if root in support)
            assert connected_coefficient <= tree_coefficient
            comparisons += 1
            total_connected += connected_coefficient
            total_tree += tree_coefficient
        # exp(|A|)<=3^|A|, so the primitive supersolution bound is rational.
        epsilon = max(sum(F(6 ** len(support), 1000) for support in supports if i in support)
                      for i in range(4))
        assert epsilon <= 1
        assert total_connected <= total_tree <= epsilon
    return {"supports": len(supports), "orders": degree,
            "root_order_comparisons": comparisons, "repeated_supports": True,
            "passed": True}


def constant_control():
    q = F(1, 10000)
    unitary = F(48, 435) * 4*q/(1-q)**2
    scalar = F(72, 145) * q/(1-q)**2
    magnetic = F(5184, 313200000)
    total = unitary + scalar + magnetic
    assert total < F(1, 2500) < F(1, 400)
    return {"unitary_upper": str(unitary), "scalar_upper": str(scalar),
            "magnetic_upper": str(magnetic), "total_upper": str(total),
            "margin_to_1_over_2500": str(F(1, 2500)-total), "passed": True}


if __name__ == "__main__":
    print(json.dumps({"arithmetic": "exact rational",
                      "tree_control": tree_control(),
                      "constant_control": constant_control()}, indent=2))
