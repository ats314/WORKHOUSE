"""Exact tests beyond the derived quadratic construction."""

from math import comb

from sympy import Rational

from workhouse.wilson_chart_recursion import product_recursion
from workhouse.wilson_vacuum_chart import embed_local, product_chart, spectator_kinetic


def test_degree_two_matches_separate_specialized_implementation():
    supports = ((0, 1), (1, 2))
    general = product_recursion(3, supports, 4, steps=2)
    specialized = product_chart(3, supports, steps=2)
    for key, value in specialized.second_rotated.items():
        assert general.rotated[key] == value
    for key, value in specialized.second_generators.items():
        assert general.generators[key] == value


def test_single_face_matches_closed_two_by_two_spectral_formula_through_four():
    # For a pure flip, the vacuum doublet has trace (1+d) cosh(tau*z),
    # determinant d, and exact diagonalizing angle atan(A*sinh(tau*z))/2.
    ratio, tau, steps = Rational(3, 5), Rational(2, 3), 3
    d = ratio**2
    a = (1 + d) / (1 - d)
    c2 = (1 + d) / (2 * (1 - d))
    c4 = ((1 + d) * (c2 / 2 + Rational(1, 24)) - c2**2) / (1 - d)
    model = product_recursion(2, ((0, 1),), 4, ratio, steps, tau)
    assert model.eigenvalues[(2,)] == steps * tau**2 * c2
    assert model.eigenvalues[(4,)] == tau**4 * (steps * c4 + comb(steps, 2) * c2**2)
    assert model.generators[(1,)][3, 0] == tau * a / 2
    assert model.generators[(3,)][3, 0] == tau**3 * (a / 12 - a**3 / 6)
    assert model.generators[(2,)].is_zero_matrix
    assert model.generators[(4,)].is_zero_matrix


def test_fourth_order_overlap_and_third_order_chain_anchor_all_coefficients():
    for model in (
        product_recursion(3, ((0, 1), (1, 2)), 4),
        product_recursion(4, ((0, 1), (1, 2), (2, 3)), 3),
    ):
        for key, value in model.rotated.items():
            if sum(key):
                assert value == value.H
                assert value[:, 0].is_zero_matrix
                assert value[0, :].is_zero_matrix
        assert any(not s.is_zero_matrix for k, s in model.generators.items() if sum(k) == 3)


def test_cubic_and_quartic_generators_are_block_independent():
    supports = ((0, 1), (1, 2))
    one = product_recursion(3, supports, 4)
    two = product_recursion(3, supports, 4, steps=2)
    assert one.generators == two.generators
    assert one.rotated[(2, 2)] != two.rotated[(2, 2)]


def test_disconnected_cubic_and_quartic_coefficients_with_spectator():
    single = product_recursion(2, ((0, 1),), 4)
    model = product_recursion(5, ((0, 1), (2, 3)), 4)
    outside = spectator_kinetic(5, (0, 1, 2, 3), Rational(4, 5))
    for alpha in ((2, 1), (1, 2), (2, 2), (3, 1), (1, 3)):
        expected = (
            embed_local(single.rotated[(alpha[0],)], (0, 1), 5)
            * embed_local(single.rotated[(alpha[1],)], (2, 3), 5)
            * outside
        )
        assert model.rotated[alpha] == expected
        assert model.generators[alpha].is_zero_matrix


def test_connected_cubic_coefficient_on_nonvacuum_spectators():
    supports = ((0, 1), (1, 2))
    local = product_recursion(3, supports, 3)
    global_model = product_recursion(4, supports, 3)
    outside = spectator_kinetic(4, (0, 1, 2), Rational(4, 5))
    for alpha in ((2, 1), (1, 2)):
        assert (
            global_model.rotated[alpha] == embed_local(local.rotated[alpha], (0, 1, 2), 4) * outside
        )
        assert global_model.generators[alpha] == embed_local(local.generators[alpha], (0, 1, 2), 4)
