"""Exact finite tensor controls for the transported-transfer extraction lemma.

Two-level, two-link interaction examples test the algebra, not Wilson rotors.
No floating point arithmetic or eigenvalue fitting is used.
"""

from itertools import combinations, product
from math import factorial
import json

import sympy as sp


def subsets(sites):
    return [tuple(c) for n in range(len(sites) + 1) for c in combinations(sites, n)]


def partitions(sites):
    if not sites:
        yield ()
        return
    first, *rest = sites
    for tail in partitions(tuple(rest)):
        yield ((first,),) + tail
        for j, block in enumerate(tail):
            yield tail[:j] + ((first,) + block,) + tail[j + 1 :]


def embed(matrix, support, sites):
    """Direct basis-index embedding, including noncontiguous tensor factors."""
    support = tuple(support)
    sites = tuple(sites)
    positions = [sites.index(i) for i in support]
    outside = [j for j, i in enumerate(sites) if i not in support]
    basis = list(product((0, 1), repeat=len(sites)))
    result = sp.zeros(len(basis))
    for row, a in enumerate(basis):
        ai = sum(a[p] << (len(positions) - k - 1) for k, p in enumerate(positions))
        for col, b in enumerate(basis):
            if all(a[p] == b[p] for p in outside):
                bi = sum(b[p] << (len(positions) - k - 1) for k, p in enumerate(positions))
                result[row, col] = matrix[ai, bi]
    return result


def free(sites):
    return sp.diag(*[sp.Rational(1, 2) ** sum(bits) for bits in product((0, 1), repeat=len(sites))])


exchange = sp.zeros(4)
exchange[1, 2] = exchange[2, 1] = sp.Rational(1, 64)


def overlapping_family(sites):
    result = free(sites)
    for edge in ((0, 1), (1, 2)):
        if set(edge) <= set(sites):
            outside = tuple(i for i in sites if i not in edge)
            result += embed(exchange, edge, sites) * embed(free(outside), outside, sites)
    if sites == (0, 1, 2):
        result[7, 7] += sp.Rational(1, 256)
    return result


def disconnected_family(sites):
    result = sp.eye(2 ** len(sites))
    for component in ((0, 1), (2, 3)):
        support = tuple(i for i in sites if i in component)
        local = free(support)
        if support == component:
            local += exchange
        result *= embed(local, support, sites)
    return result


def check(name, ambient, family):
    gs = {s: family(s) for s in subsets(ambient)}
    fs = {}
    counts = {"subsystems": len(gs), "anchoring_checks": 0, "expansion_checks": 0}
    for sites, g in gs.items():
        assert g == g.T
        assert g[:, 0] == sp.eye(g.rows)[:, 0]
        # Independent exact diagonal-dominance certificates on the excited block.
        for row in range(1, g.rows):
            radius = sum(abs(g[row, col]) for col in range(1, g.cols) if col != row)
            assert g[row, row] >= radius
            assert 1 - g[row, row] >= radius
        if not sites:
            continue
        c = sp.zeros(g.rows)
        for partition in partitions(sites):
            term = sp.eye(g.rows)
            for block in partition:
                term *= embed(gs[block], block, sites)
            c += (-1) ** (len(partition) - 1) * factorial(len(partition) - 1) * term
        if len(sites) == 1:
            assert c == free(sites)
            fs[sites] = sp.zeros(2)
        else:
            fs[sites] = c
        assert fs[sites] == fs[sites].T
        assert fs[sites][:, 0] == sp.zeros(g.rows, 1)
        assert fs[sites][0, :] == sp.zeros(1, g.cols)
        counts["anchoring_checks"] += 1

    # Enumerate disjoint ACTIVITY families, independently of partition inversion.
    for sites, g in gs.items():
        activities = [s for s, f in fs.items() if set(s) <= set(sites) and f != sp.zeros(f.rows)]
        rebuilt = sp.zeros(g.rows)
        for chosen in subsets(tuple(range(len(activities)))):
            supports = [activities[j] for j in chosen]
            if any(set(a) & set(b) for a, b in combinations(supports, 2)):
                continue
            used = set().union(*(set(s) for s in supports)) if supports else set()
            outside = tuple(i for i in sites if i not in used)
            term = embed(free(outside), outside, sites)
            for support in supports:
                term *= embed(fs[support], support, sites)
            rebuilt += term
        assert rebuilt == g
        counts["expansion_checks"] += 1

    if name == "overlapping_noncommuting":
        left = embed(fs[(0, 1)], (0, 1), ambient)
        right = embed(fs[(1, 2)], (1, 2), ambient)
        assert left * right != right * left
        expected = sp.zeros(8)
        expected[7, 7] = sp.Rational(1, 256)
        assert fs[ambient] == expected
        counts["nonzero_overlap_commutator"] = True
    else:
        crossing = [s for s in fs if set(s) & {0, 1} and set(s) & {2, 3}]
        for s in crossing:
            assert fs[s] == sp.zeros(2 ** len(s))
        assert fs[(0, 1)] == exchange and fs[(2, 3)] == exchange
        counts["disconnected_zero_checks"] = len(crossing)
    return {"model": name, **counts, "passed": True}


if __name__ == "__main__":
    records = [
        check("overlapping_noncommuting", (0, 1, 2), overlapping_family),
        check("disconnected_product", (0, 1, 2, 3), disconnected_family),
    ]
    print(json.dumps({"arithmetic": "exact rational", "models": records}, indent=2))
