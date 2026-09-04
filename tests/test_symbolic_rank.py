"""The engine over Q(N): the field, the symbolic primitives, and one cumulant end to end."""

from fractions import Fraction as F

import pytest

from workhouse import loopcalc as L
from workhouse import symbolic_rank as SR


def test_field_arithmetic_and_specialisation():
    n = SR.N_SYM
    a = SR.RF(1, 2 * n)
    b = n * n - 1
    assert (a * b).at(3) == F(4, 3) and (a * b) == SR.CF_SYM
    assert SR.RF(3) == 3 and SR.RF(0) == 0 and not SR.RF(0) and SR.RF(1, 2) == F(1, 2)
    assert (n**2 - 4) / (n - 2) == n + 2  # gcd cancellation
    assert hash(SR.RF(6, 4)) == hash(SR.RF(3, 2))
    with pytest.raises(ZeroDivisionError):
        (1 / (n - 3)).at(3)
    assert SR.rational_roots((n * n - 4).num) == [F(-2), F(2)]


def test_symbolic_weingarten_is_the_numeric_inverse_at_every_rank():
    for n in (2, 3):
        wg = SR.weingarten_symbolic(n)
        for rank in (5, 7, 11):
            num = L._weingarten(n, rank)
            assert all(wg[p].at(rank) == num[p] for p in wg)
    wg2 = SR.weingarten_symbolic(2)
    n = SR.N_SYM
    assert wg2[(0, 1)] == 1 / (n * n - 1) and wg2[(1, 0)] == -1 / (n * (n * n - 1))


def test_casimirs_and_names():
    n = SR.N_SYM
    assert SR.casimir_symbolic((1,), ()) == SR.CF_SYM
    assert SR.casimir_symbolic((1,), (1,)) == n
    assert SR.casimir_symbolic((2,), ()) == (n + 2) * (n - 1) / n
    assert SR.casimir_symbolic((1, 1), ()) == (n - 2) * (n + 1) / n
    assert SR.ENERGY_NAME[SR.E_FUND] == "F"
    assert SR.ENERGY_NAME[SR.RF(0)] == "1"
    assert SR.ENERGY_NAME[n / 2] == "adj"
    assert SR.irrep_name((2,), (1,)) == SR.irrep_name((1,), (2,)) == "2|1"


def test_second_order_over_qn_is_the_all_rank_formula():
    n = SR.N_SYM
    with SR.Symbolic() as S:
        pair = L.Cluster([((0, 1), (0, 0, 0)), ((0, 1), (1, 0, 0))])
        h2, _ = pair.second_order()
        hop, hop_even = L.codd(h2, 0, 1), L.ceven(h2, 0, 1)
    t_n = 2 * n * (n**2 - 4) / ((n**2 - 1) * (2 * n**2 - 1) * (4 * n**2 - 9))
    ell_n = -2 * n * (3 * n**2 - 5) / ((n**2 - 1) * (4 * n**2 - 9) * (2 * n**2 - 1))
    assert hop == -t_n and hop_even == ell_n
    assert S.stats["components_verified"] > 0
    # the context restores the integer engine
    assert L.N == 3 and L.F is F and L.weingarten(2)[(0, 1)] == F(1, 8)


def test_the_context_restores_the_engine_after_an_error():
    with pytest.raises(RuntimeError), SR.Symbolic():
        raise RuntimeError("inside")
    assert L.N == 3 and F(4, 3) == L.CF


def test_state_label_reads_the_per_link_energies():
    n = SR.N_SYM
    per_link = {
        0: SR.E_FUND,
        1: SR.E_FUND,
        2: n / 2,
        3: SR.RF(0),
        4: SR.E_FUND * 0 + SR.casimir_symbolic((2,), ()) / 2,
    }
    assert SR.state_label(per_link) == (-2, ("adj", "sym"))
    assert SR.label_text(("direct", (2, ("adj",)), (4, ()))) == "direct (2, adj) (4, -)"
