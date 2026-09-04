"""Private-link paths as effective links: the reduced clusters compute the same cumulants."""

from fractions import Fraction as F

from workhouse import loopcalc as L
from workhouse import symbolic_rank as SR

P = ((0, 1), (0, 0, 0))
Q_COP = ((0, 1), (1, 0, 0))
Q_PERP = ((0, 2), (0, 0, 0))


def test_reduced_words_collapse_private_runs():
    words = L.reduced_words([P, Q_COP])
    # each face: its shared link plus one effective link of weight three
    for w in words:
        (trace,) = w
        assert len(trace) == 2
        weights = sorted(L.link_weight(lk) for lk, _o in trace)
        assert weights == [1, 3]
    # the shared link is the same letter, traversed oppositely by the two faces
    shared = [(lk, o) for w in words for lk, o in w[0] if L.link_weight(lk) == 1]
    assert shared[0][0] == shared[1][0] and shared[0][1] == -shared[1][1]
    # a lone face is one effective link of weight four
    (lone,) = L.reduced_words([P])
    assert len(lone[0]) == 1 and L.link_weight(lone[0][0][0]) == 4


def test_reduced_second_order_is_the_full_one():
    full = L.Cluster([P, Q_COP])
    red = L.Cluster([P, Q_COP], reduced=True)
    h2f, v2f = full.second_order()
    h2r, v2r = red.second_order()
    assert L.codd(h2r, 0, 1) == L.codd(h2f, 0, 1) == F(-5, 612)
    assert L.ceven(h2r, 0, 1) == L.ceven(h2f, 0, 1) == F(-11, 306)
    assert L.codd(v2r, 0, 1) == L.codd(v2f, 0, 1)


def test_reduced_two_hop_weight_is_x_quantum():
    w = L.cumulant([P, Q_COP, ((0, 1), (2, 0, 0))], 1, reduced=True)
    assert L.block_odd(w) == F(360421351, 40327601932800)
    assert L.block_even(w) == F(948253471, 40327601932800)


def test_reduced_single_contact_over_qn_matches_the_full_form():
    n = SR.N_SYM
    with SR.Symbolic():
        w = L.cumulant([P, ((0, 1), (1, 0, 0)), Q_PERP], 1, reduced=True)
        odd = L.block_odd(w)
    expected = (
        2
        * n**3
        * (n**2 - 4)
        * (10 * n**2 - 13)
        / ((n**2 - 1) ** 3 * (4 * n**2 - 9) ** 2 * (2 * n**2 - 1) ** 2)
    )
    assert odd == expected


def test_weighted_labels_match_the_unreduced_ones():
    # a weight-3 effective link in the adjoint labels as three adjoint links
    eff = L.link(("path", "test-label"), 0)
    L.LINK_WEIGHT[eff] = 3
    per_link = {eff: 3 * SR.N_SYM / 2, 0: SR.E_FUND}
    assert SR.state_label(per_link) == (-3, ("adj", "adj", "adj"))
    per_link = {eff: 3 * SR.E_FUND}
    assert SR.state_label(per_link) == (-1, ())
