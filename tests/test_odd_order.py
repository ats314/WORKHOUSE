"""The centre-parity theorem's ingredients: the link set T, the criterion, the odd-N vertex."""

from fractions import Fraction

from workhouse import loopcalc as LC
from workhouse.invariants import odd_order as OO


def test_the_link_set_hits_every_face_an_odd_number_of_times():
    for box in (2, 3, 5):
        ok, faces = OO.parity_links(box)
        assert ok and faces == 3 * box**3


def test_the_criterion_closes_even_ranks_and_opens_odd_ranks_at_n_minus_2():
    for n in (4, 6, 8, 10):
        assert not any(OO.odd_order_survives(n, m) for m in range(1, 20, 2))
    for n in (3, 5, 7, 9):
        assert min(m for m in range(1, 20, 2) if OO.odd_order_survives(n, m)) == n - 2
    assert all(OO.odd_order_survives(n, m) for n in range(3, 10) for m in (2, 4, 6))


def test_the_first_odd_vertex_at_three_and_five():
    assert OO.first_odd_vertex(3) == -1
    assert OO.first_odd_vertex(5) == Fraction(-25, 144)

    # the Peter-Weyl path F -> Lambda^2 -> Lambda^3 -> F-bar at N = 5 with E = 2 C_2
    def e(k, n=5):
        return Fraction(k * (n - k) * (n + 1), n)

    assert -1 / ((e(1) - e(2)) * (e(1) - e(3))) == Fraction(-25, 144)


def test_the_first_order_vertex_is_the_engine_s_at_three_and_absent_at_four():
    try:
        LC.set_rank(3)
        h = OO.effective([OO._P])[1]
        assert LC.codd(h, 0, 0) == 1 and LC.ceven(h, 0, 0) == -1
        LC.set_rank(4)
        h = OO.effective([OO._P])[1]
        assert LC.codd(h, 0, 0) == 0 and LC.ceven(h, 0, 0) == 0
    finally:
        LC.set_rank(3)
