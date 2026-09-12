"""The sixth-order cluster engines: matrix series, Pieri rules, and the registered checks."""

from fractions import Fraction as F

import pytest

from workhouse import loopcalc as L
from workhouse import sixth_order_characters as CH
from workhouse import sixth_order_cluster as SC
from workhouse import symbolic_rank as SR
from workhouse.invariants.sixth_order_cluster import cluster


@pytest.mark.parametrize("name,section,tier,fn", cluster.checks, ids=[x[0] for x in cluster.checks])
def test_registered_check(name, section, tier, fn):
    result = fn()
    assert result[0], result[1]


def test_matrix_series_square_root_squares_to_the_metric():
    # (I + X)^(1/2) (I + X)^(1/2) = I + X and (I + X)^(1/2) (I + X)^(-1/2) = I, order by order.
    m2 = [[F(1, 3), F(1, 5)], [F(1, 5), F(-1, 7)]]
    m3 = [[F(0), F(2, 9)], [F(2, 9), F(1, 11)]]
    metric = [SC._mat_eye(2), SC._mat_zero(2), m2, m3, SC._mat_zero(2)]
    sqrt = SC._series_power(metric, F(1, 2), 4)
    inv = SC._series_power(metric, F(-1, 2), 4)
    assert SC._series_mul(sqrt, sqrt, 4) == metric
    assert SC._series_mul(sqrt, inv, 4) == [SC._mat_eye(2)] + [SC._mat_zero(2)] * 4


def test_pieri_rules_count_the_tensor_products():
    # F x F = sym + antisym; F x Fbar = adj + singlet; box counts are conserved.
    assert CH.multiply_fundamental({((1,), ()): 1}, False) == {((2,), ()): 1, ((1, 1), ()): 1}
    assert CH.multiply_fundamental({((1,), ()): 1}, True) == {((1,), (1,)): 1, ((), ()): 1}
    v = {((2, 1), (1,)): 1}
    out = CH.multiply_fundamental(v, False)
    assert set(out) == {((3, 1), (1,)), ((2, 2), (1,)), ((2, 1, 1), (1,)), ((2, 1), ())}


def test_character_series_matches_the_su3_note_at_second_order_where_generic_rules_apply():
    # At N = 3 the generic Pieri rules are wrong from three boxes on, but the second-order
    # vacuum energy uses only F, Fbar and the adjoint: -3/4 in the note's convention.
    vac = CH.bloch_series(2, CH.VACUUM, sign=-1, casimir=CH.casimir_rank(3))
    assert vac["energies"][2] == F(-3, 4)


def test_second_order_pair_hops_over_qn_reproduce_the_all_rank_formula():
    n = SR.N_SYM
    with SR.Symbolic(min_rank=9):
        space = SC.ModelSpace(SC.PAIRS["coplanar"], reduced=True)
        f = SC.folded_words(space, 2)
        hop, hop_even = SC.odd_even(f["H2"], 0, 1)
    t_n = 2 * n * (n**2 - 4) / ((n**2 - 1) * (2 * n**2 - 1) * (4 * n**2 - 9))
    ell_n = -2 * n * (3 * n**2 - 5) / ((n**2 - 1) * (4 * n**2 - 9) * (2 * n**2 - 1))
    assert hop == -t_n and hop_even == ell_n


def test_krylov_projector_equals_the_factored_reference():
    L.set_rank(3)
    P = L.plaquette((0, 1), (0, 0, 0))
    vec = L.multiply(L.multiply({P: F(1)}, P), L.conj(P))
    for lk in sorted(L.links_of(vec)):
        a = sorted(L._project_link_factored(vec, lk), key=lambda x: x[0])
        b = sorted(L._project_link(vec, lk), key=lambda x: x[0])
        assert a == b
