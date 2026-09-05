"""Independent exact finite controls for partition-cumulant activity extraction.

Ordered positive congruence models retain noncommuting overlap operators.
Closed partition Mobius inversion is compared with a root-block recursion
that does not enumerate partitions and uses a separate tensor embedding.
No Wilson activity norm, spectral flow, or infinite-volume bound is proved.
"""

from __future__ import annotations

import itertools
from fractions import Fraction
from math import factorial

import sympy as sp

DEFAULT_U = sp.Rational(1, 10)
DEFAULT_D = sp.Rational(1, 4)


def subsets(sites):
    return [tuple(s) for size in range(len(sites) + 1) for s in itertools.combinations(sites, size)]


def partitions(sites):
    """Restricted-growth strings, independent of root-block reconstruction."""
    if not sites:
        yield ()
        return

    def visit(labels, maximum):
        if len(labels) == len(sites):
            yield tuple(
                tuple(site for site, label in zip(sites, labels, strict=True) if label == j)
                for j in range(maximum + 1)
            )
        else:
            for label in range(maximum + 2):
                yield from visit((*labels, label), max(maximum, label))

    yield from visit((0,), 0)


def _binary_index(word):
    return sum(value << (len(word) - i - 1) for i, value in enumerate(word))


def _partition_positions(blocks, sites):
    flat = [site for block in blocks for site in block]
    if len(flat) != len(sites) or set(flat) != set(sites):
        raise ValueError("Tensor blocks must partition the ambient sites")
    return [[sites.index(site) for site in block] for block in blocks]


def tensor_entries(blocks, matrices, sites):
    """Tensor entries on the ambient basis, with no Kronecker products."""
    positions = _partition_positions(blocks, sites)
    basis = tuple(itertools.product((0, 1), repeat=len(sites)))
    answer = sp.ones(len(basis))
    for block, matrix in zip(positions, matrices, strict=True):
        assert matrix.shape == (2 ** len(block), 2 ** len(block))
        for row, left in enumerate(basis):
            for col, right in enumerate(basis):
                answer[row, col] *= matrix[
                    _binary_index(tuple(left[p] for p in block)),
                    _binary_index(tuple(right[p] for p in block)),
                ]
    return answer


def tensor_permuted(blocks, matrices, sites):
    """Independent Kronecker product followed by an explicit basis permutation."""
    positions = _partition_positions(blocks, sites)
    if not blocks:
        return sp.ones(1)
    tensor = sp.kronecker_product(*matrices)
    order = [position for block in positions for position in block]
    permutation = sp.zeros(2 ** len(sites))
    for column, word in enumerate(itertools.product((0, 1), repeat=len(sites))):
        permutation[_binary_index(tuple(word[p] for p in order)), column] = 1
    return permutation.T * tensor * permutation


def mobius_cumulants(family):
    """Closed-partition cumulants, including singleton C_i=G_i."""
    answer = {}
    for sites in sorted(family, key=lambda s: (len(s), s)):
        if not sites:
            continue
        value = sp.zeros(2 ** len(sites))
        for partition in partitions(sites):
            k = len(partition)
            value += (
                (-1) ** (k - 1)
                * factorial(k - 1)
                * tensor_entries(partition, [family[block] for block in partition], sites)
            )
        answer[sites] = value
    return answer


def rooted_cumulants(family):
    """Independent inversion by the block containing the smallest site.

    G_X=sum_{B contains min(X)} C_B tensor G_{X minus B}; isolate B=X.
    This path neither constructs partitions nor calls mobius_cumulants.
    """
    answer = {}
    for sites in sorted(family, key=lambda s: (len(s), s)):
        if not sites:
            continue
        value = family[sites].copy()
        for tail in subsets(sites[1:]):
            block = (sites[0], *tail)
            if block == sites:
                continue
            complement = tuple(site for site in sites if site not in block)
            value -= tensor_permuted(
                (block, complement), (answer[block], family[complement]), sites
            )
        answer[sites] = value
    return answer


def components(sites, edges):
    remaining = set(sites)
    result = []
    while remaining:
        part = {min(remaining)}
        while True:
            enlarged = part | {
                site
                for edge in edges
                if set(edge) <= set(sites) and part.intersection(edge)
                for site in edge
            }
            if enlarged == part:
                break
            part = enlarged
        remaining -= part
        result.append(tuple(sorted(part)))
    return tuple(result)


def edge_projection():
    return sp.Matrix(
        [
            [0, 0, 0, 0],
            [0, sp.Rational(1, 2), sp.Rational(1, 2), 0],
            [0, sp.Rational(1, 2), sp.Rational(1, 2), 0],
            [0, 0, 0, 0],
        ]
    )


def ordered_transfer_family(ambient, edges, u=DEFAULT_U, d=DEFAULT_D):
    if not isinstance(u, (int, Fraction, sp.Rational)) or not isinstance(
        d, (int, Fraction, sp.Rational)
    ):
        raise TypeError("Transfer parameters must be exact rational numbers")
    u, d = sp.Rational(u), sp.Rational(d)
    if not 0 <= u < 1 or not 0 < d <= 1:
        raise ValueError("Use 0<=u<1 and 0<d<=1 for the positive contraction factors")
    local = edge_projection()
    assert local * local == local and local == local.T
    family, positive_certificates = {}, {}
    for sites in subsets(ambient):
        free = sp.diag(*(d ** sum(word) for word in itertools.product((0, 1), repeat=len(sites))))
        product = sp.eye(2 ** len(sites))
        count = 0
        for edge in edges:
            if set(edge) <= set(sites):
                outside = tuple(site for site in sites if site not in edge)
                embedded = tensor_entries(
                    (edge, outside), (local, sp.eye(2 ** len(outside))), sites
                )
                assert embedded * embedded == embedded and embedded == embedded.T
                product = product * (sp.eye(product.rows) - u * embedded)
                count += 1
        family[sites] = product.T * free * product
        determinant = product.det()
        expected = (1 - u) ** (count * 2 ** max(0, len(sites) - 2))
        assert determinant == expected > 0
        assert all(value > 0 for value in free.diagonal())
        positive_certificates[sites] = {
            "det_B": str(determinant),
            "smallest_D_entry": str(min(free.diagonal())),
        }
    return family, positive_certificates


def check_family(name, ambient, edges):
    family, positivity = ordered_transfer_family(ambient, edges)
    closed, rooted = mobius_cumulants(family), rooted_cumulants(family)
    assert closed == rooted
    activities = {
        sites: (sp.zeros(2) if len(sites) == 1 else cumulant) for sites, cumulant in closed.items()
    }
    disconnected = []
    reconstruction = 0
    for sites, transfer in family.items():
        dimension = transfer.rows
        vacuum = sp.eye(dimension)[:, 0]
        assert transfer == transfer.T and transfer * vacuum == vacuum
        component_list = components(sites, edges)
        assert transfer == tensor_permuted(
            component_list, [family[c] for c in component_list], sites
        )
        rebuilt = sp.zeros(dimension)
        for partition in partitions(sites):
            rebuilt += tensor_permuted(partition, [closed[c] for c in partition], sites)
        assert rebuilt == transfer
        reconstruction += 1
        if not sites:
            continue
        activity = activities[sites]
        assert activity == activity.T
        assert activity * vacuum == sp.zeros(dimension, 1)
        assert vacuum.T * activity == sp.zeros(1, dimension)
        if len(component_list) > 1:
            assert activity == sp.zeros(dimension)
            disconnected.append(sites)
    overlap = None
    if ((0, 1) in edges) and ((1, 2) in edges):
        outside_left = tuple(site for site in ambient if site not in (0, 1))
        outside_right = tuple(site for site in ambient if site not in (1, 2))
        left = tensor_entries(
            ((0, 1), outside_left), (activities[(0, 1)], sp.eye(2 ** len(outside_left))), ambient
        )
        right = tensor_entries(
            ((1, 2), outside_right), (activities[(1, 2)], sp.eye(2 ** len(outside_right))), ambient
        )
        commutator = left * right - right * left
        overlap = sp.trace(commutator.T * commutator)
        assert overlap > 0
    return {
        "name": name,
        "ambient": ambient,
        "ordered_edges": edges,
        "subsystems": len(family),
        "reconstruction_count": reconstruction,
        "vacuum_anchoring_count": len(activities),
        "disconnected_cancellations": disconnected,
        "closed_formula_equals_root_block_recursion": True,
        "overlap_commutator_frobenius_squared": str(overlap) if overlap is not None else None,
        "full_activity_nonzero": activities[ambient] != sp.zeros(2 ** len(ambient)),
        "positivity_congruences": [
            {"sites": sites, **values} for sites, values in positivity.items()
        ],
        "activities": [
            {
                "sites": sites,
                "matrix": [[str(v) for v in activity.row(i)] for i in range(activity.rows)],
            }
            for sites, activity in activities.items()
        ],
    }


def missing_factorization_control():
    ambient = (0, 1)
    family = {
        sites: sp.diag(
            *(
                sp.Rational(1, 1 + sum(word))
                for word in itertools.product((0, 1), repeat=len(sites))
            )
        )
        for sites in subsets(ambient)
    }
    for transfer in family.values():
        assert transfer == transfer.T and transfer[0, 0] == 1
        assert all(value > 0 for value in transfer.diagonal())
    cumulants = mobius_cumulants(family)
    assert cumulants == rooted_cumulants(family)
    factorized = tensor_permuted(((0,), (1,)), (family[(0,)], family[(1,)]), ambient)
    expected = sp.diag(0, 0, 0, sp.Rational(1, 12))
    assert family[ambient] != factorized
    assert cumulants[ambient] == family[ambient] - factorized == expected
    return {
        "family": "G_X=(I+sum_i q_i)^(-1)",
        "positive_and_vacuum_fixing": True,
        "component_factorization_fails": True,
        "disconnected_activity_11_entry": "1/12",
        "scope": (
            "Two disconnected binary sites: vacuum fixing alone does not imply connected support."
        ),
    }


def exact_controls():
    return {
        "models": [
            check_family("ordered_chain", (0, 1, 2, 3), ((0, 1), (1, 2), (2, 3))),
            check_family("disjoint_edges", (0, 1, 2, 3), ((0, 1), (2, 3))),
        ],
        "missing_factorization": missing_factorization_control(),
        "scope": (
            "Finite exact extraction algebra only; no uniform Wilson activity or marked norm bound."
        ),
    }
