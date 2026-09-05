"""Exact finite tensor controls for the Wilson creator parent construction.

The analytic theorem is separate. These reusable controls compare direct
basis action, tensor products, a disjoint-support creation exponential and
an independent rational congruence replay. No numerical eigenvalues enter.
The supplied g=1-K1-M1**2 uses declared rational upper bounds on creator
vector norms. Neither an auxiliary parent gap nor finite verification
identifies the physical Wilson excited space.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction
from math import factorial

import sympy as sp

from .rooted_creator import family, star_exp

F = Fraction


def rational(value):
    if not isinstance(value, (int, F, sp.Rational)):
        raise TypeError("Creator coefficients must be exact integers or rationals")
    return (
        sp.Rational(value.numerator, value.denominator)
        if isinstance(value, F)
        else sp.Rational(value)
    )


def matrix_digest(matrix):
    body = json.dumps(
        [[str(v) for v in matrix.row(i)] for i in range(matrix.rows)], separators=(",", ":")
    )
    return hashlib.sha256(body.encode()).hexdigest()


def embedded_creator(dimensions, support, vector):
    """Basis-action implementation; it never constructs tensor products."""
    basis = tuple(itertools.product(*(range(d) for d in dimensions)))
    lookup = {word: i for i, word in enumerate(basis)}
    matrix = sp.zeros(len(basis))
    assert support and len(set(support)) == len(support)
    for col, word in enumerate(basis):
        if any(word[i] for i in support):
            continue
        for local, coefficient in vector.items():
            assert len(local) == len(support)
            assert all(0 < a < dimensions[i] for i, a in zip(support, local, strict=True))
            output = list(word)
            for i, a in zip(support, local, strict=True):
                output[i] = a
            matrix[lookup[tuple(output)], col] += rational(coefficient)
    return matrix


def kronecker_creator(dimensions, support, vector):
    """Independent rank-one local-matrix tensor embedding."""
    total = sp.zeros(sp.prod(dimensions))
    for local, coefficient in vector.items():
        factors = []
        for i, d in enumerate(dimensions):
            if i in support:
                factor = sp.zeros(d)
                factor[local[support.index(i)], 0] = 1
            else:
                factor = sp.eye(d)
            factors.append(factor)
        total += rational(coefficient) * sp.kronecker_product(*factors)
    return total


def direct_creation_state(dimensions, creators):
    """Disjoint-subset expansion, independent of all operator matrices.

    Commuting nilpotence removes factorials: one chooses each support at most
    once, and intersecting supports contribute zero.
    """
    basis = tuple(itertools.product(*(range(d) for d in dimensions)))
    lookup = {word: i for i, word in enumerate(basis)}
    result = sp.zeros(len(basis), 1)
    for bits in itertools.product((False, True), repeat=len(creators)):
        selected = [item for bit, item in zip(bits, creators, strict=True) if bit]
        all_links = [i for support, _ in selected for i in support]
        if len(all_links) != len(set(all_links)):
            continue
        for choices in itertools.product(*(vector.items() for _, vector in selected)):
            word = [0] * len(dimensions)
            coefficient = sp.Integer(1)
            for (support, _), (local, value) in zip(selected, choices, strict=True):
                coefficient *= rational(value)
                for i, a in zip(support, local, strict=True):
                    word[i] = a
            result[lookup[tuple(word)]] += coefficient
    return result


def nilpotent_exp(matrix, links):
    power = sp.eye(matrix.rows)
    result = power.copy()
    for degree in range(1, links + 1):
        power = power * matrix
        result += power / factorial(degree)
    assert power * matrix == sp.zeros(matrix.rows)
    return result


def exact_psd_certificate(matrix):
    """Elimination with exact rational Schur complements and reconstruction."""
    assert matrix == matrix.T
    size = matrix.rows
    remainder = [[F(matrix[i, j]) for j in range(size)] for i in range(size)]
    upper = sp.eye(size)
    diagonal = []
    for i in range(size):
        pivot = remainder[i][i]
        assert pivot >= 0, f"negative rational pivot at {i}: {pivot}"
        diagonal.append(pivot)
        if not pivot:
            assert not any(remainder[i][j] for j in range(i, size)), "zero pivot with nonzero row"
            continue
        for j in range(i + 1, size):
            upper[i, j] = rational(remainder[i][j] / pivot)
        for j in range(i + 1, size):
            for k in range(j, size):
                remainder[j][k] -= remainder[i][j] * remainder[i][k] / pivot
                remainder[k][j] = remainder[j][k]
    diagonal_matrix = sp.diag(*(rational(d) for d in diagonal))
    # Independent symbolic multiplication checks the entire certificate.
    assert upper.T * diagonal_matrix * upper == matrix
    return {
        "dimension": size,
        "matrix_sha256": matrix_digest(matrix),
        "rank": sum(d != 0 for d in diagonal),
        "diagonal": [str(d) for d in diagonal],
        "unit_upper_off_diagonal": [
            [i, j, str(upper[i, j])] for i in range(size) for j in range(i + 1, size) if upper[i, j]
        ],
        "exact_reconstruction": True,
    }


def verify_model(name, dimensions, creators):
    if not dimensions or any(not isinstance(d, int) or d < 2 for d in dimensions):
        raise ValueError("Each link must have a vacuum and at least one excited dimension")
    size = int(sp.prod(dimensions))
    basis = tuple(itertools.product(*(range(d) for d in dimensions)))
    zero = sp.zeros(size)
    vacuum = sp.eye(size)[:, 0]
    local_q = [sp.diag(*(int(word[i] != 0) for word in basis)) for i in range(len(dimensions))]
    embedded = []
    for support, vector in creators:
        direct = embedded_creator(dimensions, support, vector)
        assert direct == kronecker_creator(dimensions, support, vector)
        embedded.append(direct)
    total_creator = sum(embedded, zero)
    exponential = nilpotent_exp(total_creator, len(dimensions))
    inverse = nilpotent_exp(-total_creator, len(dimensions))
    assert exponential * inverse == sp.eye(size)
    psi = direct_creation_state(dimensions, creators)
    assert exponential * vacuum == psi
    assert psi[0] == 1
    norm_squared = (psi.T * psi)[0]
    assert norm_squared > 0
    projection = psi * psi.T / norm_squared
    assert projection == projection.T and projection * projection == projection
    anchor = [
        sum((a for (support, _), a in zip(creators, embedded, strict=True) if i in support), zero)
        for i in range(len(dimensions))
    ]
    parents = [q - a for q, a in zip(local_q, anchor, strict=True)]
    for i, parent in enumerate(parents):
        assert parent * parent == parent
        assert parent == exponential * local_q[i] * inverse
        assert parent * psi == sp.zeros(size, 1)
        assert parent * projection == zero
        for other in parents:
            assert parent * other == other * parent
    # The singular lower bound for each oblique idempotent is itself checked
    # by rational congruence, independently of the final parent gap.
    idempotent_singular_controls = [
        exact_psd_certificate((p.T * p) ** 2 - p.T * p) for p in parents
    ]
    # Check the orthogonal-overlap mechanism used to improve the row bound.
    overlap_controls = []
    for x, ((sx, vx), ax) in enumerate(zip(creators, embedded, strict=True)):
        for y, ((sy, vy), ay) in enumerate(zip(creators, embedded, strict=True)):
            if y < x:
                continue
            commutator = ax * ay.T - ay.T * ax
            if not set(sx).intersection(sy):
                assert commutator == zero
                continue
            bound_squared = sum(rational(v) ** 2 for v in vx.values()) * sum(
                rational(v) ** 2 for v in vy.values()
            )
            certificate = exact_psd_certificate(
                bound_squared * sp.eye(size) - commutator.T * commutator
            )
            overlap_controls.append(
                {
                    "creators": [x, y],
                    "bound_squared": str(bound_squared),
                    "certificate": certificate,
                }
            )
    for i, j in itertools.combinations(range(len(dimensions)), 2):
        shared = sum(
            (
                a
                for (support, _), a in zip(creators, embedded, strict=True)
                if i in support and j in support
            ),
            zero,
        )
        assert shared * shared == zero
        assert (shared + shared.T) ** 2 == shared * shared.T + shared.T * shared
        assert (shared * shared.T) * (shared.T * shared) == zero
    hamiltonian = sum((p.T * p for p in parents), zero)
    assert hamiltonian * psi == sp.zeros(size, 1)
    # ||w_X||_2 <= ||w_X||_1, a declared rational upper bound.
    rooted_mass = [
        sum(
            len(support) * sum(abs(rational(v)) for v in vector.values())
            for support, vector in creators
            if i in support
        )
        for i in range(len(dimensions))
    ]
    m1_upper = max(rooted_mass)
    k1_upper = max(
        sum(
            (len(support) - 1) * sum(abs(rational(v)) for v in vector.values())
            for support, vector in creators
            if i in support
        )
        for i in range(len(dimensions))
    )
    conservative_g = 1 - 2 * m1_upper - 2 * m1_upper**2
    g = 1 - k1_upper - m1_upper**2
    assert g >= conservative_g
    assert g > 0
    weighted_upper = max(
        sum(
            2 ** len(support) * sum(abs(rational(v)) for v in vector.values())
            for support, vector in creators
            if i in support
        )
        for i in range(len(dimensions))
    )
    if weighted_upper <= sp.Rational(1, 8):
        assert m1_upper <= sp.Rational(1, 16)
        assert k1_upper <= sp.Rational(1, 32)
        assert g >= sp.Rational(247, 256)
    h_certificate = exact_psd_certificate(hamiltonian)
    assert h_certificate["rank"] == size - 1
    gap_certificate = exact_psd_certificate(hamiltonian**2 - g * hamiltonian)
    # Also certify the equivalent lower bound on the orthogonal complement.
    direct_gap_certificate = exact_psd_certificate(hamiltonian - g * (sp.eye(size) - projection))

    # Dropping the positive quadratic term is an actual false construction.
    linear_only = sum((q - a - a.T for q, a in zip(local_q, anchor, strict=True)), zero)
    omitted = sum((a.T * a for a in anchor), zero)
    assert hamiltonian == linear_only + omitted
    negative_witness = (psi.T * linear_only * psi)[0]
    assert negative_witness == -(psi.T * omitted * psi)[0] <= 0
    if negative_witness < 0:
        assert linear_only * psi != sp.zeros(size, 1)
    binary_oracle = None
    if all(d == 2 for d in dimensions):
        entries = [
            (sum(1 << i for i in support), F(vector[(1,) * len(support)]))
            for support, vector in creators
        ]
        expected = star_exp(family(len(dimensions), entries))
        for index, word in enumerate(basis):
            mask = sum(value << i for i, value in enumerate(word))
            assert psi[index] == rational(expected[mask])
        binary_oracle = "workhouse.rooted_creator.star_exp agrees with independent tensor paths"
    return {
        "name": name,
        "link_dimensions": dimensions,
        "creators": [
            {"support": support, "entries": [[local, str(v)] for local, v in vector.items()]}
            for support, vector in creators
        ],
        "norm_bound": "Each ||w_X||_2 is bounded above by the exact rational coefficient l1 norm.",
        "M1_upper": str(m1_upper),
        "K1_upper": str(k1_upper),
        "rooted_weight2_upper": str(weighted_upper),
        "within_rooted_one_eighth_ball": bool(weighted_upper <= sp.Rational(1, 8)),
        "g_lower": str(g),
        "conservative_g_lower": str(conservative_g),
        "vacuum_coefficient": "1",
        "state_norm_squared": str(norm_squared),
        "state": [str(v) for v in psi],
        "commuting_idempotents": True,
        "exact_similarity": True,
        "unique_common_kernel": True,
        "hamiltonian_psd": h_certificate,
        "idempotent_singular_controls": idempotent_singular_controls,
        "overlap_commutator_controls": overlap_controls,
        "H_squared_minus_gH_psd": gap_certificate,
        "H_minus_g_orthogonal_complement_psd": direct_gap_certificate,
        "negative_control": {
            "omission": "sum A_i.T A_i",
            "psi_T_H_linear_psi": str(negative_witness),
            "vacuum_annihilation_fails": linear_only * psi != sp.zeros(size, 1),
        },
        "binary_oracle": binary_oracle,
    }


def disjoint_condition_number_control():
    a = sp.Rational(1, 32)
    shear = sp.Matrix([[1, 0], [a, 1]])
    q = sp.diag(0, 1)
    parent = shear * q * shear.inv()
    h = parent.T * parent
    lam = sp.Symbol("lambda")
    assert sp.expand(h.charpoly(lam).as_expr() - lam * (lam - (1 + a * a))) == 0
    local_norm2 = (shear[:, 0].T * shear[:, 0])[0]
    inverse_norm2 = (shear.inv()[:, 0].T * shear.inv()[:, 0])[0]
    assert local_norm2 == inverse_norm2 == 1 + a * a
    # For n disjoint single-link creators, both similarity norms have this
    # product-vector lower bound, hence cond(S_n)>=(1+a^2)^n.
    lower_at_8192 = (1 + a * a) ** 8192
    assert lower_at_8192 > 1000
    return {
        "a": str(a),
        "M1": str(a),
        "parent_gap_for_every_n": str(1 + a * a),
        "local_characteristic_polynomial": str(h.charpoly(lam).as_expr()),
        "rooted_weight2_norm": "1/16",
        "vacuum_norm_squared_for_n": "(1025/1024)^n",
        "similarity_condition_number_lower_bound": "(1025/1024)^n",
        "bound_at_n_8192_exceeds_1000_exactly": True,
        "scope": (
            "Tensor factorization establishes these formulas for all positive n; "
            "no full 2^8192 matrix is constructed."
        ),
        "consequence": (
            "A rooted bound does not imply a volume-uniform norm or condition number "
            "for the global creator exponential."
        ),
    }


def control_cases():
    """Fresh exact data for six finite controls; callers may vary a copy."""
    return [
        (
            "rooted_radius_overlapping_multibody",
            (2, 2, 2),
            [
                ((0,), {(1,): F(1, 64)}),
                ((0, 1), {(1, 1): F(1, 128)}),
                ((1, 2), {(1, 1): F(-1, 128)}),
                ((0, 1, 2), {(1, 1, 1): F(1, 512)}),
            ],
        ),
        (
            "binary_overlapping_chain",
            (2, 2, 2, 2),
            [
                ((0,), {(1,): F(1, 50)}),
                ((0, 1), {(1, 1): F(1, 100)}),
                ((1, 2), {(1, 1): F(-1, 80)}),
                ((2, 3), {(1, 1): F(1, 100)}),
                ((0, 1, 2), {(1, 1, 1): F(1, 150)}),
            ],
        ),
        ("binary_disjoint_singles", (2, 2, 2, 2), [((i,), {(1,): F(1, 8)}) for i in range(4)]),
        (
            "binary_stronger_overlap",
            (2, 2, 2),
            [
                ((0, 1), {(1, 1): F(1, 15)}),
                ((1, 2), {(1, 1): F(-1, 15)}),
            ],
        ),
        (
            "ternary_vector_creators",
            (3, 3, 3),
            [
                ((0, 1), {(1, 2): F(1, 60), (2, 1): F(-1, 80)}),
                ((1, 2), {(2, 1): F(1, 70), (1, 2): F(1, 90)}),
                ((0,), {(2,): F(1, 40)}),
                ((0, 1, 2), {(1, 2, 1): F(1, 180)}),
            ],
        ),
        (
            "mixed_link_dimensions",
            (2, 3, 2),
            [
                ((0, 2), {(1, 1): F(1, 20)}),
                ((0, 1), {(1, 1): F(1, 50), (1, 2): F(-1, 60)}),
                ((1, 2), {(2, 1): F(1, 70)}),
            ],
        ),
    ]


def matrix_hash(matrix):
    rows = [[str(matrix[i, j]) for j in range(matrix.cols)] for i in range(matrix.rows)]
    return hashlib.sha256(json.dumps(rows, separators=(",", ":")).encode()).hexdigest()


def replay_psd(matrix, certificate):
    n = matrix.rows
    assert certificate["dimension"] == n
    assert certificate["matrix_sha256"] == matrix_hash(matrix)
    pivots = [sp.Rational(d) for d in certificate["diagonal"]]
    assert len(pivots) == n and all(d >= 0 for d in pivots)
    upper = sp.eye(n)
    positions = set()
    for i, j, value in certificate["unit_upper_off_diagonal"]:
        assert 0 <= i < j < n and (i, j) not in positions
        positions.add((i, j))
        upper[i, j] = sp.Rational(value)
    assert matrix == upper.T * sp.diag(*pivots) * upper
    rank = sum(d != 0 for d in pivots)
    assert certificate["rank"] == rank
    return rank


def replay_model(case):
    dims = case["link_dimensions"]
    size = int(sp.prod(dims))
    operators = []
    norms_squared = []
    for record in case["creators"]:
        support = record["support"]
        matrix = sp.zeros(size)
        norm2 = 0
        for excitations, value in record["entries"]:
            value = sp.Rational(value)
            norm2 += value**2
            factors = []
            for site, dim in enumerate(dims):
                if site in support:
                    factor = sp.zeros(dim)
                    excitation = excitations[support.index(site)]
                    assert 0 < excitation < dim
                    factor[excitation, 0] = value if site == support[0] else 1
                else:
                    factor = sp.eye(dim)
                factors.append(factor)
            matrix += sp.kronecker_product(*factors)
        operators.append(matrix)
        norms_squared.append(norm2)
    q = []
    for site in range(len(dims)):
        factors = [
            sp.diag(0, *([1] * (dim - 1))) if site == i else sp.eye(dim)
            for i, dim in enumerate(dims)
        ]
        q.append(sp.kronecker_product(*factors))
    anchors = [
        sum(
            (a for a, r in zip(operators, case["creators"], strict=True) if i in r["support"]),
            sp.zeros(size),
        )
        for i in range(len(dims))
    ]
    parents = [qi - ai for qi, ai in zip(q, anchors, strict=True)]
    h = sum((p.T * p for p in parents), sp.zeros(size))
    psi = sp.Matrix([sp.Rational(v) for v in case["state"]])
    assert psi[0] == 1
    for p in parents:
        assert p * p == p and p * psi == sp.zeros(size, 1)
        assert all(p * p2 == p2 * p for p2 in parents)
    norm2 = (psi.T * psi)[0]
    assert norm2 == sp.Rational(case["state_norm_squared"])
    projection = psi * psi.T / norm2
    mass = [
        sum(
            len(r["support"]) * sum(abs(sp.Rational(v)) for _, v in r["entries"])
            for r in case["creators"]
            if i in r["support"]
        )
        for i in range(len(dims))
    ]
    reduced_mass = [
        sum(
            (len(r["support"]) - 1) * sum(abs(sp.Rational(v)) for _, v in r["entries"])
            for r in case["creators"]
            if i in r["support"]
        )
        for i in range(len(dims))
    ]
    m, k = max(mass), max(reduced_mass)
    weighted = max(
        sum(
            2 ** len(r["support"]) * sum(abs(sp.Rational(v)) for _, v in r["entries"])
            for r in case["creators"]
            if i in r["support"]
        )
        for i in range(len(dims))
    )
    assert weighted == sp.Rational(case["rooted_weight2_upper"])
    assert bool(weighted <= sp.Rational(1, 8)) == case["within_rooted_one_eighth_ball"]
    assert m == sp.Rational(case["M1_upper"]) and k == sp.Rational(case["K1_upper"])
    g = 1 - k - m * m
    assert g == sp.Rational(case["g_lower"]) > 0
    if weighted <= sp.Rational(1, 8):
        assert m <= sp.Rational(1, 16) and k <= sp.Rational(1, 32)
        assert g >= sp.Rational(247, 256)
    assert replay_psd(h, case["hamiltonian_psd"]) == size - 1
    replay_psd(h * h - g * h, case["H_squared_minus_gH_psd"])
    replay_psd(h - g * (sp.eye(size) - projection), case["H_minus_g_orthogonal_complement_psd"])
    for p, c in zip(parents, case["idempotent_singular_controls"], strict=True):
        replay_psd((p.T * p) ** 2 - p.T * p, c)
    for row in case["overlap_commutator_controls"]:
        x, y = row["creators"]
        c = operators[x] * operators[y].T - operators[y].T * operators[x]
        bound2 = norms_squared[x] * norms_squared[y]
        assert bound2 == sp.Rational(row["bound_squared"])
        replay_psd(bound2 * sp.eye(size) - c.T * c, row["certificate"])
    linear_only = sum((qi - ai - ai.T for qi, ai in zip(q, anchors, strict=True)), sp.zeros(size))
    witness = (psi.T * linear_only * psi)[0]
    assert witness == sp.Rational(case["negative_control"]["psi_T_H_linear_psi"]) <= 0
    return {"name": case["name"], "dimension": size, "g": str(g), "success": True}
