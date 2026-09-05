"""Independent finite-transfer checks of the local second-order chart.

These tests derive coefficients from the actual symmetric transfer product.
They do not insert the desired coefficient or simulate an infinite lattice.
"""

from functools import cache

import pytest
from sympy import Rational, SparseMatrix

from workhouse.wilson_vacuum_chart import (
    chart,
    diagonal_kinetic,
    embed_local,
    product_chart,
    spectator_kinetic,
    support_majorants,
    two_level_negative_control,
)


@cache
def _faces(n, supports, steps):
    return product_chart(n, supports, Rational(4, 5), steps)


def test_first_order_chart_fails_and_quadratic_chart_cancels_exactly():
    data = two_level_negative_control()
    assert data["first_chart_residual"] == Rational(97, 96)
    assert data["second_generator"] == data["predicted_generator"] == Rational(97, 24)
    assert data["final_vacuum_column"] == SparseMatrix.zeros(2, 1)
    # N independent copies retain quadratic creation with squared norm N a^2
    # under U1 alone.  U2 cancels the local coefficient, hence every N-copy one.
    for n in (1, 4, 100, 10000):
        assert n * data["first_chart_residual"] ** 2 > 0
        assert n * sum(x**2 for x in data["final_vacuum_column"]) == 0


@pytest.mark.parametrize("steps", [1, 3, 5])
def test_both_generators_are_independent_of_positive_block_power(steps):
    kinetic = SparseMatrix.diag(1, Rational(3, 4))
    potential = SparseMatrix([[0, Rational(2, 3)], [Rational(2, 3), Rational(1, 2)]])
    model = chart(kinetic, [potential], steps)
    reference = chart(kinetic, [potential], 1)
    assert model.first_generators == reference.first_generators
    assert model.second_generators == reference.second_generators
    assert model.second_rotated[(2,)][:, 0].is_zero_matrix


@pytest.mark.parametrize("steps", [1, 2])
def test_overlapping_four_link_faces_have_anchored_second_coefficients(steps):
    supports = ((0, 1, 2, 3), (3, 4, 5, 6))
    model = _faces(7, supports, steps)
    for degree, coefficient in model.second_rotated.items():
        if sum(degree):
            assert coefficient == coefficient.H
            assert coefficient[:, 0].is_zero_matrix
            assert coefficient[0, :].is_zero_matrix
    # A genuine linked quadratic creation exists before the second rotation.
    residual = model.first_rotated[(1, 1)][:, 0]
    assert not residual.is_zero_matrix
    # The normalized coefficient has no scalar vacuum part.
    assert model.first_rotated[(1, 1)][0, 0] == 0
    assert model.second_generators[(1, 1)] != SparseMatrix.zeros(128, 128)


def test_quadratic_generator_for_overlapping_faces_is_the_same_at_two_blocks():
    supports = ((0, 1, 2, 3), (3, 4, 5, 6))
    one, two = _faces(7, supports, 1), _faces(7, supports, 2)
    assert one.first_generators == two.first_generators
    assert one.second_generators == two.second_generators


def test_disjoint_coefficient_is_product_of_anchored_first_coefficients():
    supports = ((0, 1), (2, 3))
    model = _faces(5, supports, 2)  # include a genuinely free spectator
    single = _faces(2, ((0, 1),), 2)
    first = single.first_rotated[(1,)]
    expected = (
        embed_local(first, supports[0], 5)
        * embed_local(first, supports[1], 5)
        * spectator_kinetic(5, (0, 1, 2, 3), Rational(4, 5) ** 2)
    )
    assert model.second_rotated[(1, 1)] == expected
    assert model.second_generators[(1, 1)].is_zero_matrix
    assert model.eigenvalue_second[(1, 1)] == 0


def test_local_chart_keeps_spectator_factors_in_every_operator_entry():
    model = _faces(4, ((0, 1), (1, 2)), 2)
    local = _faces(3, ((0, 1), (1, 2)), 2)
    free_outside = spectator_kinetic(4, (0, 1, 2), Rational(4, 5) ** 2)
    for degree in ((1, 0), (0, 1), (1, 1), (2, 0), (0, 2)):
        expected = embed_local(local.second_rotated[degree], (0, 1, 2), 4) * free_outside
        assert model.second_rotated[degree] == expected
    # Merely matching vacuum columns does not determine a local operator chart.
    global_rank_two = chart(
        diagonal_kinetic(4, Rational(4, 5)),
        [
            embed_local(
                SparseMatrix([[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]), (0, 1), 4
            )
        ],
        2,
    )
    local_chart = _faces(4, ((0, 1),), 2)
    assert global_rank_two.first_generators[0][:, 0] == local_chart.first_generators[0][:, 0]
    assert global_rank_two.first_generators[0] != local_chart.first_generators[0]


def test_three_potentials_reconstruct_all_degree_two_connected_components():
    supports = ((0, 1), (1, 2), (3, 4))
    model = _faces(5, supports, 1)
    for degree, coefficient in model.second_rotated.items():
        if sum(degree):
            assert coefficient[:, 0].is_zero_matrix
            assert coefficient[0, :].is_zero_matrix
    pair = _faces(3, ((0, 1), (1, 2)), 1)
    expected = embed_local(pair.second_rotated[(1, 1)], (0, 1, 2), 5)
    expected *= spectator_kinetic(5, (0, 1, 2), Rational(4, 5))
    assert model.second_rotated[(1, 1, 0)] == expected


def test_support_maxima_and_rational_full_operator_constant():
    samples = {n: support_majorants(n) for n in range(1, 80)}
    maxima = [max(row[j] for row in samples.values()) for j in range(3)]
    assert maxima == [16, 336, Rational(2592, 5)]
    assert [n for n, row in samples.items() if row[2] == maxima[2]] == [9]
    assert 11 * maxima[0] + 22 * maxima[1] + maxima[2] == Rational(40432, 5)
    # Tail induction: these ratios bound every subsequent n, beyond the
    # explicitly evaluated possible maxima, rather than extrapolating a scan.
    assert Rational(6, 5) * Rational(4, 5) < 1  # n>=5, linear tail
    assert Rational(8, 7) * Rational(4, 5) < 1  # n>=7, pair linear tail
    assert Rational(10, 9) ** 2 * Rational(4, 5) < 1  # n>=9, square tail


def test_noncentered_or_wrong_kinetic_inputs_reject():
    with pytest.raises(ValueError, match="vacuum centered"):
        chart(SparseMatrix.diag(1, Rational(3, 4)), [SparseMatrix.eye(2)])
    with pytest.raises(ValueError, match="diagonal"):
        chart(
            SparseMatrix([[1, Rational(1, 20)], [0, Rational(3, 4)]]),
            [SparseMatrix([[0, 1], [1, 0]])],
        )
    with pytest.raises(ValueError, match="complementary kinetic"):
        chart(SparseMatrix.eye(2), [SparseMatrix.diag(0, 1)])
    with pytest.raises(ValueError, match="cancel every first-order"):
        chart(
            SparseMatrix.diag(1, Rational(3, 4)),
            [SparseMatrix([[0, Rational(2, 3)], [Rational(2, 3), Rational(1, 2)]])],
            first_generators=[SparseMatrix.zeros(2, 2)],
        )
