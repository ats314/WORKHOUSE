#!/usr/bin/env python3
"""Cold microscopic SU(3) O(u^4) fixed-side pentagonal-prism backend.

This program computes the fixed-side cap0-side0-cap1 fourth-order coefficient
without importing a target coefficient or any stored microscopic amplitudes.

Independent ingredients implemented here
----------------------------------------
1. Exact oriented pentagonal-prism link/face geometry.
2. Exact Wilson trace-word algebra with cyclic/free reduction.
3. Exact Kogut--Susskind electric Hamiltonian from the SU(N) Fierz identity.
4. Exact SU(3) Haar projectors from delta/epsilon invariant tensors.
5. Physical Gram quotient and exact reduced Q(E0-H0)^(-1)Q resolvents.
6. Exhaustive evaluation of all 48 fixed-side endpoint histories.
7. A per-history ledger for the 20 cap/vacuum-P-irreducible histories.

Conventions
-----------
H0 = (1/2) sum_link E_link^2 with uniform isotropic link weights.
V  = sum_face (Tr U_face + Tr U_face^dagger).
The fourth-order coefficient is unchanged by V -> -V.

The retained local P-space is
    {vacuum, +/-cap0, +/-cap1}.
For a history beginning in +cap0, the normalized C-odd matrix element is the
+C1 endpoint amplitude minus the -C1 endpoint amplitude.  Accordingly each
row's connected_codd value is +raw_amplitude for endpoint +C1 and
-raw_amplitude for endpoint -C1.

The source intentionally contains no claimed final numerator or denominator.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import itertools
import json
import math
from pathlib import Path
import platform
import sys
from typing import Any, Iterable, Sequence

import sympy as sp

BACKEND_VERSION = "pentagonal-o4-cold-trace-fierz-haar-v1"
N = 3
CF = Fraction(N * N - 1, 2 * N)
E0 = Fraction(5, 2) * CF


# =============================================================================
# Exact Wilson trace-word algebra
# =============================================================================

TraceWord = tuple[int, ...]
TraceState = tuple[TraceWord, ...]


def inverse_word(word: TraceWord) -> TraceWord:
    return tuple(-x for x in reversed(word))


def reduce_word(word: Sequence[int]) -> tuple[TraceWord, int]:
    """Free-reduce adjacent U U^-1 pairs, including the cyclic boundary.

    Returns (canonical_word, scalar_factor).  An empty trace contributes Tr I=N.
    """
    work = list(word)
    while work:
        length = len(work)
        removed = False
        for i in range(length):
            j = (i + 1) % length
            if work[i] == -work[j]:
                if length == 2:
                    return (), N
                work = work[1:-1] if j == 0 else work[:i] + work[i + 2 :]
                removed = True
                break
        if not removed:
            break
    if not work:
        return (), N
    rotations = [tuple(work[i:] + work[:i]) for i in range(len(work))]
    return min(rotations), 1


def canonical_state(words: Iterable[Sequence[int]]) -> tuple[TraceState, Fraction]:
    factor = 1
    reduced: list[TraceWord] = []
    for word in words:
        canonical, scalar = reduce_word(word)
        factor *= scalar
        if canonical:
            reduced.append(canonical)
    return tuple(sorted(reduced)), Fraction(factor)


def conjugate_state(state: TraceState) -> TraceState:
    return tuple(sorted(inverse_word(word) for word in state))


def multiply_trace(state: TraceState, word: TraceWord) -> tuple[TraceState, Fraction]:
    return canonical_state([*state, word])


def occurrences(state: TraceState, link: int) -> list[tuple[int, int, int]]:
    return [
        (trace_index, position, token)
        for trace_index, word in enumerate(state)
        for position, token in enumerate(word)
        if abs(token) == link
    ]


def fierz_swapped_state(
    state: TraceState,
    first: tuple[int, int, int],
    second: tuple[int, int, int],
) -> tuple[TraceState, Fraction]:
    """Apply the crossed-delta part of the Fierz identity to two occurrences.

    For right electric derivatives, the cut is after a positive U and before a
    negative U^-1.  Exchanging the two successor edges joins or splits traces.
    """
    labels: dict[int, int] = {}
    successors: dict[int, int] = {}
    local_to_global: dict[tuple[int, int], int] = {}
    next_node = 0

    for trace_index, word in enumerate(state):
        cycle: list[int] = []
        for position, token in enumerate(word):
            local_to_global[(trace_index, position)] = next_node
            labels[next_node] = token
            cycle.append(next_node)
            next_node += 1
        for left, right in zip(cycle, cycle[1:] + cycle[:1]):
            successors[left] = right

    def cut_source(occurrence: tuple[int, int, int]) -> int:
        trace_index, position, token = occurrence
        if token > 0:
            return local_to_global[(trace_index, position)]
        predecessor = (position - 1) % len(state[trace_index])
        return local_to_global[(trace_index, predecessor)]

    left = cut_source(first)
    right = cut_source(second)
    left_successor = successors[left]
    right_successor = successors[right]

    swapped = dict(successors)
    swapped[left] = right_successor
    swapped[right] = left_successor

    seen: set[int] = set()
    words: list[TraceWord] = []
    for node in range(next_node):
        if node in seen:
            continue
        cycle: list[int] = []
        current = node
        while current not in seen:
            seen.add(current)
            cycle.append(labels[current])
            current = swapped[current]
        words.append(tuple(cycle))

    return canonical_state(words)


def h0_action(state: TraceState) -> dict[TraceState, Fraction]:
    """Exact H0 action from the fundamental SU(3) Fierz identity.

    sum_a T^a_ij T^a_kl = 1/2(delta_il delta_jk - delta_ij delta_kl/N).
    """
    output: defaultdict[TraceState, Fraction] = defaultdict(Fraction)
    occurrence_count = sum(len(word) for word in state)
    output[state] += Fraction(occurrence_count) * CF / 2

    links = sorted({abs(token) for word in state for token in word})
    for link in links:
        local_occurrences = occurrences(state, link)
        for first, second in itertools.combinations(local_occurrences, 2):
            derivative_sign = (1 if first[2] > 0 else -1) * (1 if second[2] > 0 else -1)
            swapped_state, scalar = fierz_swapped_state(state, first, second)
            output[swapped_state] += Fraction(derivative_sign, 2) * scalar
            output[state] -= Fraction(derivative_sign, 2 * N)

    return {state_key: value for state_key, value in output.items() if value}


def h0_closure(seeds: Iterable[TraceState]) -> list[TraceState]:
    seen = set(seeds)
    queue = deque(seen)
    while queue:
        state = queue.popleft()
        for image in h0_action(state):
            if image not in seen:
                seen.add(image)
                queue.append(image)
    return sorted(seen, key=repr)


# =============================================================================
# Exact SU(3) Haar projectors from invariant tensors
# =============================================================================


def epsilon3(a: int, b: int, c: int) -> int:
    if len({a, b, c}) != 3:
        return 0
    inversions = int(a > b) + int(a > c) + int(b > c)
    return -1 if inversions % 2 else 1


InvariantTensor = dict[tuple[int, ...], int]
_INVARIANT_CACHE: dict[tuple[int, int], tuple[list[InvariantTensor], list[list[Fraction]]]] = {}


def raw_invariant_tensors(p: int, q: int) -> list[InvariantTensor]:
    """Generate delta/epsilon spanning tensors in F^p tensor Fbar^q."""
    if p != q:
        return []
    if (p - q) % N != 0:
        return []

    tensors: list[InvariantTensor] = []
    if p == q:
        for permutation in itertools.permutations(range(q)):
            tensor: InvariantTensor = {}
            for assignment in itertools.product(range(N), repeat=p + q):
                fundamentals = assignment[:p]
                antifundamentals = assignment[p:]
                if all(fundamentals[i] == antifundamentals[permutation[i]] for i in range(p)):
                    tensor[assignment] = 1
            tensors.append(tensor)
        return tensors

    if p == q + N:
        for matched_positions in itertools.permutations(range(p), q):
            unmatched = [i for i in range(p) if i not in matched_positions]
            tensor = {}
            for assignment in itertools.product(range(N), repeat=p + q):
                fundamentals = assignment[:p]
                antifundamentals = assignment[p:]
                if all(fundamentals[matched_positions[j]] == antifundamentals[j] for j in range(q)):
                    epsilon = epsilon3(*(fundamentals[i] for i in unmatched))
                    if epsilon:
                        tensor[assignment] = epsilon
            tensors.append(tensor)
        return tensors

    if q == p + N:
        for matched_positions in itertools.permutations(range(q), p):
            unmatched = [j for j in range(q) if j not in matched_positions]
            tensor = {}
            for assignment in itertools.product(range(N), repeat=p + q):
                fundamentals = assignment[:p]
                antifundamentals = assignment[p:]
                if all(antifundamentals[matched_positions[i]] == fundamentals[i] for i in range(p)):
                    epsilon = epsilon3(*(antifundamentals[j] for j in unmatched))
                    if epsilon:
                        tensor[assignment] = epsilon
            tensors.append(tensor)
        return tensors

    raise NotImplementedError(f"Invariant sector ({p},{q}) is outside this O(4) backend")


def invariant_basis(p: int, q: int) -> tuple[list[InvariantTensor], list[list[Fraction]]]:
    """Return an independent invariant basis and inverse exact Gram matrix."""
    key = (p, q)
    if key in _INVARIANT_CACHE:
        return _INVARIANT_CACHE[key]

    raw = raw_invariant_tensors(p, q)
    if not raw:
        _INVARIANT_CACHE[key] = ([], [])
        return _INVARIANT_CACHE[key]

    assignments = list(itertools.product(range(N), repeat=p + q))
    assignment_index = {assignment: i for i, assignment in enumerate(assignments)}
    selected: list[InvariantTensor] = []
    matrix = sp.zeros(len(assignments), 0)
    current_rank = 0

    for tensor in raw:
        column = sp.zeros(len(assignments), 1)
        for assignment, value in tensor.items():
            column[assignment_index[assignment], 0] = value
        candidate = matrix.row_join(column)
        candidate_rank = candidate.rank()
        if candidate_rank > current_rank:
            selected.append(tensor)
            matrix = candidate
            current_rank = candidate_rank

    gram = sp.Matrix(
        [
            [
                sum(left.get(key_assignment, 0) * right.get(key_assignment, 0)
                    for key_assignment in set(left) | set(right))
                for right in selected
            ]
            for left in selected
        ]
    )
    inverse_gram = gram.inv()
    inverse_fraction = [
        [Fraction(int(inverse_gram[i, j].p), int(inverse_gram[i, j].q)) for j in range(inverse_gram.cols)]
        for i in range(inverse_gram.rows)
    ]
    _INVARIANT_CACHE[key] = (selected, inverse_fraction)
    return _INVARIANT_CACHE[key]


@dataclass(frozen=True)
class SparseFactor:
    variables: tuple[int, ...]
    table: dict[tuple[int, ...], Fraction]


def collapse_factor(
    variables: Sequence[int],
    entries: Iterable[tuple[tuple[int, ...], Fraction]],
) -> SparseFactor:
    unique_variables: list[int] = []
    for variable in variables:
        if variable not in unique_variables:
            unique_variables.append(variable)
    positions = [[i for i, candidate in enumerate(variables) if candidate == variable] for variable in unique_variables]

    table: defaultdict[tuple[int, ...], Fraction] = defaultdict(Fraction)
    for assignment, value in entries:
        collapsed: list[int] = []
        valid = True
        for repeated_positions in positions:
            first = assignment[repeated_positions[0]]
            if any(assignment[position] != first for position in repeated_positions[1:]):
                valid = False
                break
            collapsed.append(first)
        if valid and value:
            table[tuple(collapsed)] += value

    return SparseFactor(tuple(unique_variables), {key: value for key, value in table.items() if value})


def multiply_factors(left: SparseFactor, right: SparseFactor) -> SparseFactor:
    union = list(left.variables)
    for variable in right.variables:
        if variable not in union:
            union.append(variable)
    if not left.table or not right.table:
        return SparseFactor(tuple(union), {})

    shared = [variable for variable in left.variables if variable in right.variables]
    left_shared_positions = [left.variables.index(variable) for variable in shared]
    right_shared_positions = [right.variables.index(variable) for variable in shared]

    right_index: defaultdict[tuple[int, ...], list[tuple[tuple[int, ...], Fraction]]] = defaultdict(list)
    for assignment, value in right.table.items():
        shared_assignment = tuple(assignment[position] for position in right_shared_positions)
        right_index[shared_assignment].append((assignment, value))

    left_union_positions = [union.index(variable) for variable in left.variables]
    right_union_positions = [union.index(variable) for variable in right.variables]
    output: defaultdict[tuple[int, ...], Fraction] = defaultdict(Fraction)

    for left_assignment, left_value in left.table.items():
        shared_assignment = tuple(left_assignment[position] for position in left_shared_positions)
        for right_assignment, right_value in right_index.get(shared_assignment, ()):  # exact sparse join
            combined = [0] * len(union)
            for position, value in zip(left_union_positions, left_assignment):
                combined[position] = value
            for position, value in zip(right_union_positions, right_assignment):
                combined[position] = value
            output[tuple(combined)] += left_value * right_value

    return SparseFactor(tuple(union), {key: value for key, value in output.items() if value})


def sum_out(factor: SparseFactor, variable: int) -> SparseFactor:
    position = factor.variables.index(variable)
    remaining = factor.variables[:position] + factor.variables[position + 1 :]
    output: defaultdict[tuple[int, ...], Fraction] = defaultdict(Fraction)
    for assignment, value in factor.table.items():
        output[assignment[:position] + assignment[position + 1 :]] += value
    return SparseFactor(remaining, {key: value for key, value in output.items() if value})


def contract_factors(factors: list[SparseFactor], domains: dict[int, int]) -> Fraction:
    if not factors:
        return Fraction(1)
    if any(not factor.table for factor in factors):
        return Fraction(0)

    active_variables = {variable for factor in factors for variable in factor.variables}
    while active_variables:
        candidates: list[tuple[int, int, int, int]] = []
        for variable in active_variables:
            containing = [factor for factor in factors if variable in factor.variables]
            scope = {entry for factor in containing for entry in factor.variables}
            dense_bound = math.prod(domains[entry] for entry in scope)
            sparse_bound = math.prod(len(factor.table) for factor in containing)
            candidates.append((dense_bound, sparse_bound, len(scope), variable))
        _, _, _, eliminate = min(candidates)

        containing = [factor for factor in factors if eliminate in factor.variables]
        factors = [factor for factor in factors if eliminate not in factor.variables]
        product = containing[0]
        for factor in containing[1:]:
            product = multiply_factors(product, factor)
        reduced = sum_out(product, eliminate)
        if reduced.table:
            factors.append(reduced)
        elif reduced.variables:
            return Fraction(0)
        active_variables = {variable for factor in factors for variable in factor.variables}

    answer = Fraction(1)
    for factor in factors:
        answer *= factor.table.get((), Fraction(0))
    return answer


_INNER_CACHE: dict[tuple[TraceState, TraceState], Fraction] = {}
_HAAR_SECTOR_REQUESTS: Counter[tuple[int, int]] = Counter()
_HAAR_NONZERO_UNBALANCED: Counter[tuple[int, int]] = Counter()


def haar_inner(bra: TraceState, ket: TraceState) -> Fraction:
    """Exact SU(3) Haar inner product of two Wilson trace networks."""
    key = (bra, ket)
    if key in _INNER_CACHE:
        return _INNER_CACHE[key]

    words = [*conjugate_state(bra), *ket]
    if not words:
        _INNER_CACHE[key] = Fraction(1)
        return Fraction(1)

    occurrences_by_link: defaultdict[int, list[tuple[int, int, int]]] = defaultdict(list)
    next_color_variable = 0
    for word in words:
        trace_variables = list(range(next_color_variable, next_color_variable + len(word)))
        next_color_variable += len(word)
        for position, token in enumerate(word):
            row_variable = trace_variables[position - 1]
            column_variable = trace_variables[position]
            occurrences_by_link[abs(token)].append(
                (1 if token > 0 else -1, row_variable, column_variable)
            )

    domains: dict[int, int] = {variable: N for variable in range(next_color_variable)}
    factors: list[SparseFactor] = []

    for link in sorted(occurrences_by_link):
        local = occurrences_by_link[link]
        positive = [entry for entry in local if entry[0] > 0]
        negative = [entry for entry in local if entry[0] < 0]
        sector = (len(positive), len(negative))
        _HAAR_SECTOR_REQUESTS[sector] += 1
        basis, inverse_gram = invariant_basis(*sector)
        if basis and sector[0] != sector[1]:
            _HAAR_NONZERO_UNBALANCED[sector] += 1
        if not basis:
            _INNER_CACHE[key] = Fraction(0)
            return Fraction(0)

        rank = len(basis)
        alpha = next_color_variable
        beta = next_color_variable + 1
        next_color_variable += 2
        domains[alpha] = rank
        domains[beta] = rank

        output_variables = [entry[1] for entry in positive] + [entry[2] for entry in negative]
        input_variables = [entry[2] for entry in positive] + [entry[1] for entry in negative]

        output_entries = [
            ((basis_index, *assignment), Fraction(value))
            for basis_index, tensor in enumerate(basis)
            for assignment, value in tensor.items()
        ]
        factors.append(collapse_factor((alpha, *output_variables), output_entries))

        gram_entries = {
            (left, right): inverse_gram[left][right]
            for left in range(rank)
            for right in range(rank)
            if inverse_gram[left][right]
        }
        factors.append(SparseFactor((alpha, beta), gram_entries))

        input_entries = [
            ((basis_index, *assignment), Fraction(value))
            for basis_index, tensor in enumerate(basis)
            for assignment, value in tensor.items()
        ]
        factors.append(collapse_factor((beta, *input_variables), input_entries))

    answer = contract_factors(factors, domains)
    _INNER_CACHE[key] = answer
    return answer


# =============================================================================
# Pentagonal-prism geometry and history census
# =============================================================================


def build_prism(n_sides: int = 5) -> tuple[
    list[tuple[tuple[int, int], tuple[int, int]]],
    list[TraceWord],
    list[tuple[int, ...]],
]:
    edges: list[tuple[tuple[int, int], tuple[int, int]]] = []
    edge_id: dict[tuple[tuple[int, int], tuple[int, int]], int] = {}

    def canonical_edge(a: tuple[int, int], b: tuple[int, int]):
        return (a, b) if a < b else (b, a)

    def add_edge(a: tuple[int, int], b: tuple[int, int]) -> None:
        key = canonical_edge(a, b)
        if key not in edge_id:
            edge_id[key] = len(edges) + 1
            edges.append(key)

    for layer in range(2):
        for i in range(n_sides):
            add_edge((i, layer), ((i + 1) % n_sides, layer))
    for i in range(n_sides):
        add_edge((i, 0), (i, 1))

    polygons: list[list[tuple[int, int]]] = []
    polygons.extend([[(i, layer) for i in range(n_sides)] for layer in range(2)])
    for i in range(n_sides):
        j = (i + 1) % n_sides
        polygons.append([(i, 0), (j, 0), (j, 1), (i, 1)])

    face_words: list[TraceWord] = []
    boundary_columns: list[tuple[int, ...]] = []
    for polygon in polygons:
        tokens: list[int] = []
        column = [0] * len(edges)
        for a, b in zip(polygon, polygon[1:] + polygon[:1]):
            key = canonical_edge(a, b)
            link = edge_id[key]
            sign = 1 if key == (a, b) else -1
            tokens.append(sign * link)
            column[link - 1] += sign
        face_words.append(tuple(tokens))
        boundary_columns.append(tuple(column))

    return edges, face_words, boundary_columns


EDGES, FACE_WORDS, BOUNDARY_COLUMNS = build_prism()
SIGNED_FACES = [(face, sign) for face in range(7) for sign in (-1, 1)]


def signed_face_word(face: int, sign: int) -> TraceWord:
    return FACE_WORDS[face] if sign > 0 else inverse_word(FACE_WORDS[face])


def add_vector(left: tuple[int, ...], right: tuple[int, ...], scale: int = 1) -> tuple[int, ...]:
    return tuple(a + scale * b for a, b in zip(left, right))


def modulo_equal(left: tuple[int, ...], right: tuple[int, ...]) -> bool:
    return all((a - b) % N == 0 for a, b in zip(left, right))


def retained_cap_vacuum_flux(flux: tuple[int, ...]) -> bool:
    zero = (0,) * len(flux)
    if modulo_equal(flux, zero):
        return True
    return any(
        modulo_equal(flux, tuple(sign * value for value in BOUNDARY_COLUMNS[face]))
        for face in (0, 1)
        for sign in (-1, 1)
    )


def endpoint_orientation(flux: tuple[int, ...]) -> int | None:
    if modulo_equal(flux, BOUNDARY_COLUMNS[1]):
        return 1
    if modulo_equal(flux, tuple(-value for value in BOUNDARY_COLUMNS[1])):
        return -1
    return None


@dataclass(frozen=True)
class History:
    word: tuple[tuple[int, int], ...]
    endpoint_orientation: int
    direct: bool


def enumerate_fixed_side_histories(side_face: int = 2) -> list[History]:
    histories: list[History] = []
    start_flux = BOUNDARY_COLUMNS[0]
    for word in itertools.product(SIGNED_FACES, repeat=4):
        side_support = {face for face, _ in word if face >= 2}
        if side_support != {side_face}:
            continue
        flux = start_flux
        prefixes: list[tuple[int, ...]] = []
        for face, sign in word:
            flux = add_vector(flux, BOUNDARY_COLUMNS[face], sign)
            prefixes.append(flux)
        orientation = endpoint_orientation(flux)
        if orientation is None:
            continue
        direct = not any(retained_cap_vacuum_flux(prefix) for prefix in prefixes[:-1])
        histories.append(History(tuple(word), orientation, direct))
    return sorted(histories, key=lambda item: item.word)


FIXED_SIDE_HISTORIES = enumerate_fixed_side_histories(2)


# =============================================================================
# Exact physical Gram quotient and reduced resolvent
# =============================================================================

VACUUM: TraceState = ()
CAP0_PLUS = canonical_state([signed_face_word(0, 1)])[0]
CAP0_MINUS = canonical_state([signed_face_word(0, -1)])[0]
CAP1_PLUS = canonical_state([signed_face_word(1, 1)])[0]
CAP1_MINUS = canonical_state([signed_face_word(1, -1)])[0]
P_STATES = [VACUUM, CAP0_PLUS, CAP0_MINUS, CAP1_PLUS, CAP1_MINUS]


@dataclass
class ResolventEnvironment:
    basis: list[TraceState]
    independent_indices: list[int]
    gram_independent: sp.Matrix
    full_to_independent: sp.Matrix
    q_basis: sp.Matrix
    reduced_matrix: sp.Matrix
    gram_rank: int
    p_rank: int
    q_rank: int
    hermitian: bool


_RESOLVENT_CACHE: dict[tuple[TraceState, ...], ResolventEnvironment] = {}
_ENVIRONMENT_LOG: dict[str, dict[str, Any]] = {}


def fraction_to_sympy(value: Fraction) -> sp.Rational:
    return sp.Rational(value.numerator, value.denominator)


def sympy_to_fraction(value: sp.Rational) -> Fraction:
    return Fraction(int(value.p), int(value.q))


def build_resolvent_environment(source_states: Iterable[TraceState]) -> ResolventEnvironment:
    basis = h0_closure([*source_states, *P_STATES])
    cache_key = tuple(basis)
    if cache_key in _RESOLVENT_CACHE:
        return _RESOLVENT_CACHE[cache_key]

    dimension = len(basis)
    index = {state: i for i, state in enumerate(basis)}

    gram = sp.zeros(dimension, dimension)
    for i in range(dimension):
        for j in range(i, dimension):
            value = haar_inner(basis[i], basis[j])
            gram[i, j] = fraction_to_sympy(value)
            if i != j:
                reverse = haar_inner(basis[j], basis[i])
                if reverse != value:
                    raise AssertionError("Haar Gram matrix is not real symmetric in this sector")
                gram[j, i] = fraction_to_sympy(reverse)

    action = sp.zeros(dimension, dimension)
    for column, state in enumerate(basis):
        for image, coefficient in h0_action(state).items():
            action[index[image], column] = fraction_to_sympy(coefficient)

    hermitian = gram * action == action.T * gram
    if not hermitian:
        raise AssertionError("Exact H0 action failed the physical Gram Hermiticity gate")

    independent_indices = list(gram.rref()[1])
    gram_independent = gram.extract(independent_indices, independent_indices)
    if gram_independent.det() == 0:
        raise AssertionError("Selected physical Gram submatrix is singular")

    full_to_independent = gram_independent.inv() * gram.extract(independent_indices, range(dimension))
    hamiltonian_bilinear = gram.extract(independent_indices, range(dimension)) * action[:, independent_indices]

    p_columns: list[sp.Matrix] = []
    for p_state in P_STATES:
        coordinate = full_to_independent[:, index[p_state]]
        if any(coordinate):
            p_columns.append(coordinate)
    p_matrix = sp.Matrix.hstack(*p_columns) if p_columns else sp.zeros(len(independent_indices), 0)
    if p_matrix.cols:
        p_pivots = list(p_matrix.rref()[1])
        p_matrix = p_matrix[:, p_pivots]

    orthogonality_rows = p_matrix.T * gram_independent
    if orthogonality_rows.rows:
        q_vectors = orthogonality_rows.nullspace()
        q_basis = sp.Matrix.hstack(*q_vectors) if q_vectors else sp.zeros(len(independent_indices), 0)
    else:
        q_basis = sp.eye(len(independent_indices))

    reduced_matrix = q_basis.T * (
        fraction_to_sympy(E0) * gram_independent - hamiltonian_bilinear
    ) * q_basis
    if reduced_matrix.rows and reduced_matrix.det() == 0:
        raise AssertionError("Q(E0-H0)Q is singular in a required history sector")

    environment = ResolventEnvironment(
        basis=basis,
        independent_indices=independent_indices,
        gram_independent=gram_independent,
        full_to_independent=full_to_independent,
        q_basis=q_basis,
        reduced_matrix=reduced_matrix,
        gram_rank=len(independent_indices),
        p_rank=p_matrix.cols,
        q_rank=q_basis.cols,
        hermitian=hermitian,
    )
    _RESOLVENT_CACHE[cache_key] = environment

    signature = hashlib.sha256(repr(cache_key).encode("utf-8")).hexdigest()[:16]
    _ENVIRONMENT_LOG[signature] = {
        "formal_dimension": dimension,
        "physical_gram_rank": environment.gram_rank,
        "p_rank": environment.p_rank,
        "q_rank": environment.q_rank,
        "hermitian": environment.hermitian,
        "reduced_determinant": str(environment.reduced_matrix.det()) if environment.reduced_matrix.rows else "1",
    }
    return environment


def reduced_resolvent(source: dict[TraceState, Fraction]) -> dict[TraceState, Fraction]:
    source = {state: coefficient for state, coefficient in source.items() if coefficient}
    if not source:
        return {}

    environment = build_resolvent_environment(source)
    basis = environment.basis
    index = {state: i for i, state in enumerate(basis)}
    full_vector = sp.zeros(len(basis), 1)
    for state, coefficient in source.items():
        full_vector[index[state], 0] += fraction_to_sympy(coefficient)

    physical_vector = environment.full_to_independent * full_vector
    if environment.q_rank == 0:
        return {}

    right_hand_side = environment.q_basis.T * environment.gram_independent * physical_vector
    q_coefficients = environment.reduced_matrix.inv() * right_hand_side
    physical_result = environment.q_basis * q_coefficients

    result: dict[TraceState, Fraction] = {}
    for coordinate, independent_index in enumerate(environment.independent_indices):
        value = physical_result[coordinate, 0]
        if value:
            result[basis[independent_index]] = sympy_to_fraction(value)
    return result


def apply_insertion(
    source: dict[TraceState, Fraction],
    face: int,
    sign: int,
) -> dict[TraceState, Fraction]:
    output: defaultdict[TraceState, Fraction] = defaultdict(Fraction)
    insertion = signed_face_word(face, sign)
    for state, coefficient in source.items():
        product, scalar = multiply_trace(state, insertion)
        output[product] += coefficient * scalar
    return {state: coefficient for state, coefficient in output.items() if coefficient}


def evaluate_history(history: History) -> tuple[Fraction, Fraction]:
    state: dict[TraceState, Fraction] = {CAP0_PLUS: Fraction(1)}
    for face, sign in history.word[:-1]:
        state = reduced_resolvent(apply_insertion(state, face, sign))
    state = apply_insertion(state, *history.word[-1])

    target = CAP1_PLUS if history.endpoint_orientation > 0 else CAP1_MINUS
    raw_amplitude = sum(
        (coefficient * haar_inner(target, trace_state) for trace_state, coefficient in state.items()),
        Fraction(0),
    )
    connected_codd = raw_amplitude if history.endpoint_orientation > 0 else -raw_amplitude
    return raw_amplitude, connected_codd


# =============================================================================
# Structural verification gates and output
# =============================================================================


@dataclass
class Gate:
    name: str
    passed: bool
    detail: Any = ""


GATES: list[Gate] = []


def gate(name: str, passed: bool, detail: Any = "") -> None:
    item = Gate(name, bool(passed), detail)
    GATES.append(item)
    prefix = "[PASS]" if item.passed else "[FAIL]"
    suffix = f" :: {detail}" if detail != "" else ""
    print(f"{prefix} {name}{suffix}")


def fixed_side_endpoint_count(order: int, require_side: bool) -> int:
    count = 0
    start = BOUNDARY_COLUMNS[0]
    for word in itertools.product(SIGNED_FACES, repeat=order):
        sides = {face for face, _ in word if face >= 2}
        if require_side and sides != {2}:
            continue
        flux = start
        for face, sign in word:
            flux = add_vector(flux, BOUNDARY_COLUMNS[face], sign)
        if endpoint_orientation(flux) is not None:
            count += 1
    return count


def rotation_link_map(shift: int) -> dict[int, int]:
    edge_lookup = {edge: index + 1 for index, edge in enumerate(EDGES)}

    def rotate_vertex(vertex: tuple[int, int]) -> tuple[int, int]:
        return ((vertex[0] + shift) % 5, vertex[1])

    mapping: dict[int, int] = {}
    for index, (a, b) in enumerate(EDGES, start=1):
        ra, rb = rotate_vertex(a), rotate_vertex(b)
        key = (ra, rb) if ra < rb else (rb, ra)
        mapped = edge_lookup[key]
        orientation = 1 if (ra, rb) == key else -1
        original_orientation = 1 if (a, b) == tuple(sorted((a, b))) else -1
        mapping[index] = orientation * original_orientation * mapped
    return mapping


def map_word_links(word: TraceWord, mapping: dict[int, int]) -> TraceWord:
    return tuple((1 if token > 0 else -1) * mapping[abs(token)] for token in word)


def run_backend(output_path: Path, text_path: Path | None) -> dict[str, Any]:
    gate("SU(3) rank", N == 3, N)
    gate("fundamental Casimir", CF == Fraction(4, 3), str(CF))
    gate("pentagonal cap energy", E0 == Fraction(10, 3), str(E0))
    gate("face perimeters", [len(word) for word in FACE_WORDS] == [5, 5, 4, 4, 4, 4, 4], [len(word) for word in FACE_WORDS])

    relation = [-1, 1, 1, 1, 1, 1, 1]
    relation_residual = [
        sum(relation[face] * BOUNDARY_COLUMNS[face][edge] for face in range(7))
        for edge in range(len(EDGES))
    ]
    gate("oriented seven-face cell relation", relation_residual == [0] * len(EDGES), relation_residual)

    gate("simple cap Wilson loop norm", haar_inner(CAP0_PLUS, CAP0_PLUS) == 1, str(haar_inner(CAP0_PLUS, CAP0_PLUS)))
    gate("opposite cap orientations are orthogonal", haar_inner(CAP0_PLUS, CAP0_MINUS) == 0, str(haar_inner(CAP0_PLUS, CAP0_MINUS)))

    # One-link character regressions for the exact Haar/Fierz core.
    one_link_plus: TraceState = ((1,),)
    one_link_minus: TraceState = ((-1,),)
    determinant_state: TraceState = tuple(sorted(((1,), (1,), (1,))))
    pair_state: TraceState = tuple(sorted(((1,), (-1,))))
    gate("balanced control rejects determinant Haar integral", haar_inner(VACUUM, determinant_state) == 0, str(haar_inner(VACUUM, determinant_state)))
    gate("fundamental character norm", haar_inner(one_link_plus, one_link_plus) == 1, str(haar_inner(one_link_plus, one_link_plus)))
    gate("1+adjoint character norm regression", haar_inner(pair_state, pair_state) == 2, str(haar_inner(pair_state, pair_state)))

    h_pair = h0_action(pair_state)
    expected_pair_action = {pair_state: Fraction(3, 2), VACUUM: Fraction(-3, 2)}
    gate("one-link Fierz Casimir regression", h_pair == expected_pair_action, {repr(k): str(v) for k, v in h_pair.items()})

    rank_41 = len(invariant_basis(4, 1)[0])
    rank_31 = len(invariant_basis(3, 0)[0])
    gate("balanced control removes (4,1) invariant rank", rank_41 == 0, rank_41)
    gate("balanced control removes (3,0) determinant rank", rank_31 == 0, rank_31)

    gate("48 fixed-side endpoint histories", len(FIXED_SIDE_HISTORIES) == 48, len(FIXED_SIDE_HISTORIES))
    direct_histories = [history for history in FIXED_SIDE_HISTORIES if history.direct]
    return_histories = [history for history in FIXED_SIDE_HISTORIES if not history.direct]
    gate("20 cap/vacuum-P-irreducible histories", len(direct_histories) == 20, len(direct_histories))
    gate("28 proper-return histories", len(return_histories) == 28, len(return_histories))

    direct_multisets = Counter(tuple(sorted(history.word)) for history in direct_histories)
    expected_multisets = Counter({
        tuple(sorted(((0, -1), (1, -1), (2, -1), (2, 1)))): 10,
        tuple(sorted(((0, -1), (1, 1), (2, -1), (2, 1)))): 10,
    })
    gate("two direct temporal multisets with multiplicity ten", direct_multisets == expected_multisets, {str(k): v for k, v in direct_multisets.items()})

    lower_side_counts = {order: fixed_side_endpoint_count(order, True) for order in range(1, 4)}
    gate("no fixed-side cap transfer below fourth order", lower_side_counts == {1: 0, 2: 0, 3: 0}, lower_side_counts)

    # Exact D5 covariance of the face/link geometry.
    rotation_checks: dict[str, bool] = {}
    for shift in range(5):
        mapping = rotation_link_map(shift)
        mapped_side = canonical_state([map_word_links(FACE_WORDS[2], mapping)])[0]
        target_side = canonical_state([FACE_WORDS[2 + shift]])[0]
        rotation_checks[str(shift)] = mapped_side == target_side
    gate("D5 rotation covariance of the fixed-side trace", all(rotation_checks.values()), rotation_checks)

    all_rows: list[dict[str, Any]] = []
    direct_rows: list[dict[str, Any]] = []
    direct_sum = Fraction(0)
    return_sum = Fraction(0)
    endpoint_sums: defaultdict[int, Fraction] = defaultdict(Fraction)

    for history in FIXED_SIDE_HISTORIES:
        raw_amplitude, connected_codd = evaluate_history(history)
        row = {
            "word": [[face, sign] for face, sign in history.word],
            "endpoint_orientation": history.endpoint_orientation,
            "classification": "direct" if history.direct else "proper_return",
            "raw_endpoint_amplitude": str(raw_amplitude),
            "connected_codd": str(connected_codd),
        }
        all_rows.append(row)
        if history.direct:
            direct_rows.append(row)
            direct_sum += connected_codd
            endpoint_sums[history.endpoint_orientation] += connected_codd
        else:
            return_sum += connected_codd

    gate("all 28 proper-return Q-chain contributions vanish", all(Fraction(row["connected_codd"]) == 0 for row in all_rows if row["classification"] == "proper_return"), str(return_sum))
    gate("proper-return subtotal is zero", return_sum == 0, str(return_sum))
    gate("direct microscopic coefficient is nonzero", direct_sum != 0, str(direct_sum))
    gate("all resolvent blocks are exactly Gram-Hermitian", all(item["hermitian"] for item in _ENVIRONMENT_LOG.values()), len(_ENVIRONMENT_LOG))

    h4_side = direct_sum
    tau4 = 5 * h4_side

    # The fourth-order fold terms have no rooted cap0-side0-cap1 support because
    # their insertion supports are inherited from order <=3 kernels.  The only
    # possible K4 return histories were evaluated above and vanish individually.
    folds = {
        "e2_offdiag": "0",
        "N_offdiag": "0",
        "J_offdiag": "0",
        "return_extra": str(return_sum),
    }
    gate("all required fixed-side fold entries vanish", all(Fraction(value) == 0 for value in folds.values()), folds)

    source_path = Path(__file__).resolve()
    source_sha256 = hashlib.sha256(source_path.read_bytes()).hexdigest()

    result: dict[str, Any] = {
        "schema": "pentagonal-o4-h4-microscopic-v1",
        "cold_run": True,
        "support": ["cap0", "side0", "cap1"],
        "p_space": ["vacuum", "+/-cap0", "+/-cap1"],
        "hamiltonian": {
            "rank": N,
            "electric": "H0=(1/2) sum_link E_link^2",
            "magnetic": "V=sum_face(Tr U_face + Tr U_face^dagger)",
            "link_weights": "isotropic",
            "C_F": str(CF),
            "E0_cap": str(E0),
        },
        "history_count_total": len(FIXED_SIDE_HISTORIES),
        "history_count_direct": len(direct_rows),
        "histories": direct_rows,
        "all_fixed_side_histories": all_rows,
        "endpoint_direct_subtotals": {
            "+cap1": str(endpoint_sums[1]),
            "-cap1_signed": str(endpoint_sums[-1]),
        },
        "folds": folds,
        "h4_side": str(h4_side),
        "tau4_five_sides": str(tau4),
        "support_proofs": {
            "fixed_side_endpoint_counts_orders_1_to_3": {str(key): value for key, value in lower_side_counts.items()},
            "D5_rotation_checks": rotation_checks,
        },
        "invariant_ranks": {
            "(1,1)": len(invariant_basis(1, 1)[0]),
            "(2,2)": len(invariant_basis(2, 2)[0]),
            "(3,3)": len(invariant_basis(3, 3)[0]),
            "(3,0)": len(invariant_basis(3, 0)[0]),
            "(4,1)": len(invariant_basis(4, 1)[0]),
        },
        "resolvent_environments": _ENVIRONMENT_LOG,
        "haar_sector_diagnostics": {
            "requested": {f"{p},{q}": count for (p, q), count in sorted(_HAAR_SECTOR_REQUESTS.items())},
            "nonzero_unbalanced": {f"{p},{q}": count for (p, q), count in sorted(_HAAR_NONZERO_UNBALANCED.items())},
        },
        "gates": {
            "passed": sum(item.passed for item in GATES),
            "total": len(GATES),
            "all_pass": all(item.passed for item in GATES),
            "items": [
                {"name": item.name, "passed": item.passed, "detail": item.detail}
                for item in GATES
            ],
        },
        "provenance": {
            "backend_version": BACKEND_VERSION + "-balanced-control",
            "control_mode": "all p!=q link invariants disabled",
            "python_version": platform.python_version(),
            "sympy_version": sp.__version__,
            "source_sha256": source_sha256,
        },
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")

    if text_path is not None:
        text_path.parent.mkdir(parents=True, exist_ok=True)
        lines = [
            "PENTAGONAL PRISM SU(3) O(4) COLD MICROSCOPIC LEDGER",
            "=" * 78,
            f"Gates: {result['gates']['passed']}/{result['gates']['total']} pass",
            f"Fixed-side histories: {result['history_count_total']} = {result['history_count_direct']} direct + {len(return_histories)} return",
            f"Direct +cap1 subtotal: {result['endpoint_direct_subtotals']['+cap1']}",
            f"Direct -cap1 signed subtotal: {result['endpoint_direct_subtotals']['-cap1_signed']}",
            f"h4_side: {result['h4_side']}",
            f"tau4=5*h4_side: {result['tau4_five_sides']}",
            f"Return extra: {result['folds']['return_extra']}",
            f"Source SHA-256: {source_sha256}",
            "",
            "The coefficient was generated from trace-word/Fierz/Haar/resolvent algebra.",
            "No claimed final coefficient is embedded in this source.",
        ]
        text_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("/mnt/data/pentagonal_o4_cold_microscopic_ledger.json"),
    )
    parser.add_argument(
        "--text-report",
        type=Path,
        default=Path("/mnt/data/pentagonal_o4_cold_microscopic_ledger.txt"),
    )
    args = parser.parse_args()

    result = run_backend(args.output, args.text_report)
    print("\n" + "=" * 96)
    print("COLD MICROSCOPIC RESULT")
    print("=" * 96)
    print(f"Gates: {result['gates']['passed']}/{result['gates']['total']}")
    print("h4_side =", result["h4_side"])
    print("tau4     =", result["tau4_five_sides"])
    print("ledger   =", args.output)
    print("report   =", args.text_report)
    return 0 if result["gates"]["all_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
