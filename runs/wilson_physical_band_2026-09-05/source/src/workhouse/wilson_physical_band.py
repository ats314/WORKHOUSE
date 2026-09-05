"""Finite controls for the complete-band continuation, not its infinite theorem.

The activity model reuses the previously verified positive congruence engine
as its input construction; the new disjoint-family exhaustion, local-action
certificates and source Gram controls are separate calculations.
"""

from __future__ import annotations

import itertools
from functools import lru_cache

import sympy as sp

from workhouse import wilson_activity_extraction as extraction


def psd(matrix):
    """All principal minors, an exact finite PSD certificate."""
    assert matrix == matrix.T
    minors = []
    for size in range(1, matrix.rows + 1):
        for positions in itertools.combinations(range(matrix.rows), size):
            determinant = matrix.extract(positions, positions).det()
            assert determinant >= 0
            minors.append(str(determinant))
    return minors


def rotated_band():
    cosines = (sp.Rational(399, 401), sp.Rational(1599, 1601))
    sines = (sp.Rational(40, 401), sp.Rational(80, 1601))
    unitary = sp.zeros(4)
    for i, (c, s) in enumerate(zip(cosines, sines, strict=True)):
        assert c * c + s * s == 1
        unitary[i, i] = unitary[i + 2, i + 2] = c
        unitary[i + 2, i] = s
        unitary[i, i + 2] = -s
    identity = sp.eye(4)
    p0 = sp.diag(1, 1, 0, 0)
    p = unitary * p0 * unitary.T
    assert unitary.T * unitary == identity
    c, d = sp.Rational(3, 4), sp.Rational(1, 4)
    free = c * p0 + d * (identity - p0)
    dressed = unitary * free * unitary.T
    gap = c - d
    epsilon = gap * max(sines)
    delta = max(sines)
    assert epsilon <= gap / 10
    assert delta <= epsilon / (gap - epsilon) <= sp.Rational(1, 9)
    error = dressed - free
    norm_certificate = psd(epsilon**2 * identity - error**2)
    assert (epsilon**2 * identity - error**2).det() == 0
    projection_certificate = psd(delta**2 * identity - (p - p0) ** 2)
    assert (delta**2 * identity - (p - p0) ** 2).det() == 0
    rotation = p * p0 + (identity - p) * (identity - p0)
    square_root = sp.diag(*cosines, *cosines)
    assert rotation.T * rotation == identity - (p - p0) ** 2 == square_root**2
    assert rotation * square_root.inv() == unitary
    assert unitary * p0 == p * unitary
    assert unitary + unitary.T == 2 * square_root
    j0 = identity[:, :2]
    perturbation = sp.Matrix([[1, 2], [2, -1], [2, 4], [4, -2]]) / 5
    assert perturbation.T * perturbation == sp.eye(2)
    eta = sp.Rational(1, 8)
    source = j0 + eta * perturbation
    a0, a = p * j0, p * source
    inverse0 = j0.T * square_root.inv() * unitary.T
    assert inverse0 * a0 == sp.eye(2)
    assert a0 * inverse0 * p == p
    coefficient_map = sp.eye(2) + inverse0 * p * (source - j0)
    assert a == a0 * coefficient_map
    assert coefficient_map.det() != 0
    inverse = coefficient_map.inv() * inverse0
    assert inverse * a == sp.eye(2)
    assert a * inverse * p == p
    lower = sp.Rational(559, 648)
    gram = source.T * p * source
    gram_lower = psd(gram - lower**2 * sp.eye(2))
    gram_upper = psd((1 + eta) ** 2 * sp.eye(2) - gram)
    assert lower > sp.Rational(3, 4)
    assert 1 / lower < sp.Rational(6, 5)
    return {
        "epsilon": str(epsilon),
        "gap": str(gap),
        "projection_norm": str(delta),
        "projection_bound": str(epsilon / (gap - epsilon)),
        "source_error": str(eta),
        "gram_lower": str(lower**2),
        "operator_norm_principal_minors": norm_certificate,
        "projection_norm_principal_minors": projection_certificate,
        "gram_lower_principal_minors": gram_lower,
        "gram_upper_principal_minors": gram_upper,
        "coefficient_map_determinant": str(coefficient_map.det()),
        "direct_rotation_and_two_sided_inverse_verified": True,
    }


def negative_controls():
    # Rectangular finite restriction of the infinite unilateral shift.
    shift = sp.zeros(6, 5)
    for i in range(5):
        shift[i + 1, i] = 1
    assert shift.T * shift == sp.eye(5)
    assert shift * shift.T == sp.diag(0, 1, 1, 1, 1, 1)
    # Small columns do not control synthesis norm or completeness.
    count = 64
    defect = sp.ones(count) / count
    source = sp.eye(count) - defect
    assert defect**2 == defect
    assert source * sp.ones(count, 1) == sp.zeros(count, 1)
    assert all((defect[:, i].T * defect[:, i])[0] == sp.Rational(1, count) for i in range(count))
    # Finite checks of the strongly convergent cycle example on a common space.
    cycle_checks = []
    for length in (5, 9):
        cycle = sp.zeros(length + 1)
        cycle[0, length] = 1
        for i in range(length):
            cycle[i + 1, i] = 1
        assert cycle.T * cycle == sp.eye(length + 1)
        for i in range(4):
            assert cycle[:, i] == sp.eye(length + 1)[:, i + 1]
        assert cycle.T[:, 0] == sp.eye(length + 1)[:, length]
        cycle_checks.append(length)
    return {
        "rectangular_shift_gram_identity": True,
        "rectangular_shift_missing_vector": "e_0",
        "small_column_example_size": count,
        "column_error_norm": "1/8",
        "synthesis_error_norm": "1",
        "source_kernel_vector": "(1,...,1)",
        "unitary_cycle_lengths_checked": cycle_checks,
        "scope": (
            "Finite witnesses; the infinite unilateral shift and strong-limit arguments "
            "are proved in the companion note"
        ),
    }


def scalar_margins():
    epsilon, gap = sp.Rational(1, 998), sp.Rational(1024, 15625)
    delta = epsilon / (gap - epsilon)
    generator_times_rank = sp.Rational(568, 145) / 80000
    source = 2160 * generator_times_rank
    coarse_source = sp.Rational(27, 250)
    lower = sp.Rational(559, 648)
    assert epsilon < gap / 10
    assert delta < sp.Rational(1, 9)
    assert generator_times_rank < sp.Rational(1, 20000)
    assert source < coarse_source < sp.Rational(1, 8)
    assert 1 - sp.Rational(1, 9) ** 2 - sp.Rational(1, 8) == lower
    assert lower**2 > sp.Rational(9, 16)
    assert 1 / lower < sp.Rational(6, 5)
    assert sp.Rational(1, 16) * sp.Rational(1, 4) == sp.Rational(1, 8) ** 2
    return {
        "epsilon": str(epsilon),
        "gap": str(gap),
        "projection_bound": str(delta),
        "rank_times_integrated_generator": str(generator_times_rank),
        "source_difference_bound": str(source),
        "coarse_source_difference": str(coarse_source),
        "minimum_singular_bound": str(lower),
        "gram_lower": str(lower**2),
        "inverse_bound": str(1 / lower),
        "source_coupling_denominator": 10022400000,
        "premises": ["e^2<9", "sqrt(2)<3/2", "exp(2G)<2", "analytic tagged and activity estimates"],
    }


def _inner(left, right):
    return sum(sp.conjugate(value) * right.get(word, 0) for word, value in left.items())


def _add_vectors(vectors):
    answer = {}
    for vector in vectors:
        for word, value in vector.items():
            answer[word] = answer.get(word, 0) + value
    return answer


def tagged_source_control():
    """Sparse exact excited vectors with ten sites, three tags and four terms."""
    # A vector key is its exact excited support; omitted sites are vacuum.
    terms = (
        (
            0,
            frozenset((0, 1, 2, 3)),
            {frozenset((2,)): sp.Rational(3, 500), frozenset((3,)): sp.Rational(4, 500)},
        ),
        (0, frozenset((0, 1, 2, 3, 4)), {frozenset((4,)): sp.Rational(1, 200)}),
        (
            1,
            frozenset((2, 3, 4, 5)),
            {frozenset((2,)): sp.Rational(3, 625), frozenset((4,)): sp.Rational(4, 625)},
        ),
        (2, frozenset((6, 7, 8, 9)), {frozenset((7,)): sp.Rational(1, 80)}),
    )
    anchors = (frozenset((0, 1, 2, 3)), frozenset((2, 3, 4, 5)), frozenset((6, 7, 8, 9)))
    norms = [sp.sqrt(_inner(vector, vector)) for _, _, vector in terms]
    assert all(value.is_Rational for value in norms)
    for tag, support, vector in terms:
        assert anchors[tag] <= support
        assert frozenset() not in vector
        assert all(word <= support for word in vector)
    d = max(
        sum(
            2 ** len(support) * norm
            for (_, support, _), norm in zip(terms, norms, strict=True)
            if i in support
        )
        for i in range(10)
    )
    vectors = [_add_vectors([vector for tag, _, vector in terms if tag == p]) for p in range(3)]
    gram = sp.Matrix([[_inner(left, right) for right in vectors] for left in vectors])
    assert gram[0, 1] != 0 and gram[0, 2] == gram[1, 2] == 0
    rows = [sum(abs(value) for value in gram.row(i)) for i in range(3)]
    assert max(rows) <= d**2 / 64
    certificate = psd(d**2 / 64 * sp.eye(3) - gram)
    # Eight disjoint four-site terms with a nonzero local vacuum component
    # violate the proposed bound if its centering premise is dropped.
    amplitude = sp.Rational(1, 100)
    uncentered_gram = amplitude**2 * sp.ones(8)
    uncentered_d = 16 * amplitude
    witness = sp.ones(8, 1)
    rayleigh = (witness.T * uncentered_gram * witness)[0] / (witness.T * witness)[0]
    assert rayleigh == 8 * amplitude**2 > uncentered_d**2 / 64
    return {
        "tags": 3,
        "terms": 4,
        "sites": 10,
        "tagged_weight_two_norm": str(d),
        "gram": [[str(value) for value in gram.row(i)] for i in range(3)],
        "gram_row_max": str(max(rows)),
        "gram_schur_bound": str(d**2 / 64),
        "synthesis_norm_upper": str(d / 8),
        "gram_bound_principal_minors": certificate,
        "overlap_inner_product_nonzero": True,
        "disjoint_centered_inner_products_zero": True,
        "uncentered_negative_control": {
            "disjoint_terms": 8,
            "actual_gram_norm": str(rayleigh),
            "invalid_centered_bound": str(uncentered_d**2 / 64),
        },
    }


def _disjoint_families(supports):
    """Enumerate support families directly, without set partitions."""
    yield ()
    for count in range(1, len(supports) + 1):
        for family in itertools.combinations(supports, count):
            if sum(map(len, family)) == len(set().union(*map(set, family))):
                yield family


def _embed_with_free(matrix, support, ambient):
    d = sp.Rational(1, 4)
    outside = tuple(i for i in ambient if i not in support)
    free = sp.diag(*(d ** sum(word) for word in itertools.product((0, 1), repeat=len(outside))))
    return extraction.tensor_permuted((support, outside), (matrix, free), ambient)


def exhaustion_control():
    """Direct congruence transfers versus activity exhaustion on local vectors.

    The four-site chain has overlapping noncommuting edge factors. Its
    connected activities include larger supports, and two disjoint edge
    activities act nontrivially together. This checks the anchored omitted
    activity mechanism behind local strong convergence, in finite dimension.
    """
    ambient = (0, 1, 2, 3)
    transfers, _ = extraction.ordered_transfer_family(
        ambient, ((0, 1), (1, 2), (2, 3)), u=sp.Rational(1, 10), d=sp.Rational(1, 4)
    )
    cumulants = extraction.mobius_cumulants(transfers)
    activities = {
        support: value
        for support, value in cumulants.items()
        if len(support) >= 2 and value != sp.zeros(value.rows)
    }
    norms = {
        support: max(sum(abs(x) for x in matrix.row(i)) for i in range(matrix.rows))
        for support, matrix in activities.items()
    }
    left = extraction.tensor_permuted(((0, 1), (2, 3)), (activities[(0, 1)], sp.eye(4)), ambient)
    right = extraction.tensor_permuted(((1, 2), (0, 3)), (activities[(1, 2)], sp.eye(4)), ambient)
    commutator = left * right - right * left
    commutator_square = sp.trace(commutator.T * commutator)
    assert commutator_square > 0
    supports = tuple(activities)
    local_support = (0, 3)
    embedding = sp.zeros(16, 4)
    for column, word in enumerate(itertools.product((0, 1), repeat=2)):
        embedding[8 * word[0] + word[1], column] = 1
    assert embedding.T * embedding == sp.eye(4)
    terms = {}
    for family in _disjoint_families(supports):
        if not family:
            terms[family] = sp.diag(
                *(sp.Rational(1, 4) ** sum(word) for word in itertools.product((0, 1), repeat=4))
            )
            continue
        covered = tuple(sorted(set().union(*map(set, family))))
        outside = tuple(i for i in ambient if i not in covered)
        free = sp.diag(
            *(
                sp.Rational(1, 4) ** sum(word)
                for word in itertools.product((0, 1), repeat=len(outside))
            )
        )
        terms[family] = extraction.tensor_permuted(
            (*family, outside), (*[activities[s] for s in family], free), ambient
        )
    assert sum(terms.values(), sp.zeros(16)) == transfers[ambient]
    vanished = 0
    nonzero_disjoint_product = False
    for family, matrix in terms.items():
        if any(set(s).isdisjoint(local_support) for s in family):
            assert matrix * embedding == sp.zeros(16, 4)
            vanished += 1
        if len(family) == 2 and matrix * embedding != sp.zeros(16, 4):
            nonzero_disjoint_product = True
    assert vanished > 0 and nonzero_disjoint_product
    a = sum(value for s, value in norms.items() if not set(s).isdisjoint(local_support))
    assert 0 < a < 1
    reports = []
    for volume in ((0, 3), (0, 1, 3), ambient):
        approximate = _embed_with_free(transfers[volume], volume, ambient)
        restriction = sum(
            (
                matrix
                for family, matrix in terms.items()
                if all(set(s) <= set(volume) for s in family)
            ),
            sp.zeros(16),
        )
        assert restriction == approximate
        error = (transfers[ambient] - approximate) * embedding
        omitted = sum(
            value
            for s, value in norms.items()
            if not set(s).isdisjoint(local_support) and not set(s) <= set(volume)
        )
        # exp(a)<=1/(1-a); this is a conservative rational version of the
        # general exp(a(S))*a_out(S,Gamma) local-tail estimate.
        bound = omitted / (1 - a)
        certificate = psd(bound**2 * sp.eye(4) - error.T * error)
        assert (error == sp.zeros(16, 4)) == (volume == ambient)
        reports.append(
            {
                "volume": list(volume),
                "omitted_activity_mass": str(omitted),
                "local_operator_tail_bound": str(bound),
                "tail_principal_minors": certificate,
                "tail_is_nonzero": volume != ambient,
            }
        )
    return {
        "ambient_sites": 4,
        "model_parameters": {"u": "1/10", "d": "1/4"},
        "overlap_commutator_frobenius_squared": str(commutator_square),
        "local_input_sites": list(local_support),
        "nonzero_activities": len(activities),
        "disjoint_families": len(terms),
        "activity_families_killed_by_local_vacuum": vanished,
        "nonzero_two_activity_product": nonzero_disjoint_product,
        "touching_activity_mass_upper": str(a),
        "exhaustions": reports,
        "scope": (
            "Finite four-link exact activity exhaustion and local-action tail certificates; "
            "not an infinite-volume proof"
        ),
    }


@lru_cache(maxsize=1)
def exact_controls():
    return {
        "rotated_band": rotated_band(),
        "source_gram": tagged_source_control(),
        "activity_exhaustion": exhaustion_control(),
        "scalar_margins": scalar_margins(),
        "negative_controls": negative_controls(),
        "scope": (
            "Finite exact projector, source Gram, activity exhaustion and rational controls; "
            "no uniform Wilson analytic theorem is machine-certified"
        ),
    }
