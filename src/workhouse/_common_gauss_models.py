"""Exact finite controls for the common-Gauss literal projection lemma.

The rational model carries scalar vac/radial sectors and two SO(3)
adjoints. It tests finite algebra, not Wilson asymptotics. No third-party
library is needed. The checker refuses optimized Python and overwrites.
"""

from __future__ import annotations

import itertools
from fractions import Fraction as F

if not __debug__:
    raise RuntimeError("This exact verifier requires Python assertions enabled.")

V = 0
R = 1
S = 2
A = (3, 4, 5)
B = (6, 7, 8)
ALPHA = F(7, 4)
BETA = F(9, 4)
RADIAL = F(7, 2)
NEXT_PHYSICAL = F(4)
C_R, S_R = F(4, 5), F(3, 5)
C_A, S_A = F(12, 13), F(5, 13)


def add_scaled(target, source, coefficient=F(1)):
    for state, value in source.items():
        new = target.get(state, F(0)) + coefficient * value
        if new:
            target[state] = new
        else:
            target.pop(state, None)
    return target


def inner(left, right):
    return sum((value * right.get(state, F(0)) for state, value in left.items()), F(0))


def project_one(state):
    if state == V:
        return {V: F(1)}
    if state == R:
        return {R: C_R**2, S: C_R * S_R}
    if state == S:
        return {R: C_R * S_R, S: S_R**2}
    if state in A:
        axis = A.index(state)
        return {A[axis]: C_A**2, B[axis]: C_A * S_A}
    axis = B.index(state)
    return {A[axis]: C_A * S_A, B[axis]: S_A**2}


def project(vector):
    answer = {}
    for state, coefficient in vector.items():
        partial = {(): coefficient}
        for local in state:
            next_partial = {}
            for prefix, value in partial.items():
                for output, factor in project_one(local).items():
                    next_partial[prefix + (output,)] = value * factor
            partial = next_partial
        add_scaled(answer, partial)
    return answer


def complement(vector):
    return add_scaled(dict(vector), project(vector), F(-1))


def state_at(count, entries):
    state = [V] * count
    for place, value in entries.items():
        state[place] = value
    return tuple(state)


def low_vectors(count):
    result = [("vacuum", (), {state_at(count, {}): F(1)}, F(0))]
    for i in range(count):
        result.append(("radial", (i,), {state_at(count, {i: R}): F(1)}, RADIAL))
    for i, j in itertools.combinations(range(count), 2):
        singlet = {state_at(count, {i: a, j: a}): F(1) for a in A}
        result.append(("pair", (i, j), singlet, 2 * ALPHA))
    return result


def local_energy(state):
    if state == V:
        return F(0)
    if state == R:
        return RADIAL
    if state == S:
        return NEXT_PHYSICAL
    return ALPHA if state in A else BETA


def energy(vector):
    return sum(
        (value**2 * sum((local_energy(i) for i in state), F(0)) for state, value in vector.items()),
        F(0),
    )


def rotate(vector, axis1, axis2):
    """Infinitesimal simultaneous SO(3) generator on both adjoint copies."""
    result = {}
    for state, value in vector.items():
        for factor, local in enumerate(state):
            multiplet = A if local in A else B if local in B else ()
            if not multiplet:
                continue
            index = multiplet.index(local)
            if index == axis1:
                new_axis, sign = axis2, F(1)
            elif index == axis2:
                new_axis, sign = axis1, F(-1)
            else:
                continue
            new = list(state)
            new[factor] = multiplet[new_axis]
            add_scaled(result, {tuple(new): sign * value})
    return result


def stringify(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {str(key): stringify(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [stringify(item) for item in value]
    return value


def controls():
    # Direct projection and Lie-generator identities, independently of the
    # tensor compression formulas under test.
    for local in range(9):
        vector = {(local,): F(1)}
        assert project(project(vector)) == project(vector)
        for axes in ((0, 1), (0, 2), (1, 2)):
            assert project(rotate(vector, *axes)) == rotate(project(vector), *axes)
    assert project({(V,): F(1)}) == {(V,): F(1)}
    d_r2 = S_R**2
    d_a2 = S_A**2
    d_pair2 = 2 * d_a2 - d_a2**2
    threshold = min(NEXT_PHYSICAL, ALPHA + BETA, 3 * ALPHA)
    assert threshold > max(RADIAL, 2 * ALPHA)
    floor = threshold - max(
        (threshold - RADIAL) * d_r2,
        (threshold - 2 * ALPHA) * d_pair2,
    )
    assert floor == F(191, 50)

    tensor_reports = []
    for count in (1, 2, 3, 5):
        vectors = low_vectors(count)
        errors = [complement(entry[2]) for entry in vectors]
        for i, (kind, support, vector, _) in enumerate(vectors):
            norm2 = inner(vector, vector)
            expected = F(0) if kind == "vacuum" else d_r2 if kind == "radial" else d_pair2
            assert inner(errors[i], errors[i]) == norm2 * expected
            assert inner(vector, project(vector)) == norm2 * (1 - expected)
            for state in errors[i]:
                assert tuple(j for j, item in enumerate(state) if item != V) == support
            for axes in ((0, 1), (0, 2), (1, 2)):
                assert rotate(vector, *axes) == {}
                assert rotate(errors[i], *axes) == {}
            for j in range(i):
                assert inner(errors[i], errors[j]) == 0

        # A deterministic superposition includes every distinct pair support.
        superposition, superposition_error = {}, {}
        predicted_norm2, predicted_error2 = F(0), F(0)
        for i, (kind, _, vector, _) in enumerate(vectors):
            coefficient = F((-1) ** i * (i + 1), i + 2)
            add_scaled(superposition, vector, coefficient)
            add_scaled(superposition_error, errors[i], coefficient)
            norm2 = inner(vector, vector)
            predicted_norm2 += coefficient**2 * norm2
            expected = F(0) if kind == "vacuum" else d_r2 if kind == "radial" else d_pair2
            predicted_error2 += coefficient**2 * norm2 * expected
        assert complement(superposition) == superposition_error
        assert inner(superposition, superposition) == predicted_norm2
        assert inner(superposition_error, superposition_error) == predicted_error2
        assert predicted_error2 <= max(d_r2, d_pair2) * predicted_norm2

        # The local radial error is an actual eigenvector of the compressed
        # form and attains the uniform floor in this chosen model.
        radial_q = errors[1]
        assert project(radial_q) == {}
        quotient = energy(radial_q) / inner(radial_q, radial_q)
        assert quotient == floor
        tensor_reports.append(
            {
                "copies": count,
                "complete_low_dimension": len(vectors),
                "cross_pair_count": count * (count - 1) // 2,
                "superposition_error_squared": predicted_error2,
                "attained_uniform_floor": quotient,
            }
        )

    # A single adjoint is not invariant, whereas a two-adjoint trace is.
    assert rotate({(A[0],): F(1)}, 0, 1)
    pair = low_vectors(2)[-1][2]
    assert all(rotate(pair, *axes) == {} for axes in ((0, 1), (0, 2), (1, 2)))

    # A genuinely new three-site invariant exists (chirality), but its exact
    # energy is above the selected threshold. It cannot be omitted by a
    # blanket assertion that only quadratic invariants exist.
    chirality = {}
    for perm in itertools.permutations(range(3)):
        inversions = sum(perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3))
        chirality[tuple(A[i] for i in perm)] = F((-1) ** inversions)
    assert all(rotate(chirality, *axes) == {} for axes in ((0, 1), (0, 2), (1, 2)))
    assert energy(chirality) / inner(chirality, chirality) == 3 * ALPHA > threshold

    # Exact-vacuum inclusion is necessary: a rotated scalar vacuum projector
    # has a growing product-vacuum error despite zero excited factors.
    wrong_vacuum_losses = [1 - C_R ** (2 * copies) for copies in (1, 2, 8, 32)]
    assert all(
        left < right
        for left, right in zip(wrong_vacuum_losses[:-1], wrong_vacuum_losses[1:], strict=True)
    )
    assert wrong_vacuum_losses[-1] > F(99, 100)

    return stringify(
        {
            "scope": (
                "finite rational SO(3) representation/projection algebra; "
                "no Wilson localization certificate"
            ),
            "local_model_dimension": 9,
            "slow_adjoint_gap": ALPHA,
            "first_outside_adjoint_gap": BETA,
            "radial_gap": RADIAL,
            "next_local_physical_gap": NEXT_PHYSICAL,
            "common_gauss_threshold": threshold,
            "radial_leakage_squared": d_r2,
            "adjoint_leakage_squared": d_a2,
            "pair_leakage_squared": d_pair2,
            "uniform_refined_floor": floor,
            "tensor_controls": tensor_reports,
            "three_adjoint_chirality_energy": 3 * ALPHA,
            "wrong_vacuum_losses": wrong_vacuum_losses,
        }
    )


# Derived from immutable original under next_nonlinear/:
# next_literal_common/check_common_gauss_literal_projection.py
# Original SHA256: 8dc64c7d2e451a8434d82a0db96d368c22a3b0011b6b16ed7e26670d530775b3
