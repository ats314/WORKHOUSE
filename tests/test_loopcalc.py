"""The third engine's primitives, against closed forms and the runs' registered constants."""

from fractions import Fraction as F

import pytest

from workhouse import loopcalc as L


def test_weingarten_closed_forms():
    n = 3
    wg2 = L.weingarten(2)
    assert wg2[(0, 1)] == F(1, n * n - 1) and wg2[(1, 0)] == F(-1, n * (n * n - 1))
    wg3 = L.weingarten(3)
    assert wg3[(0, 1, 2)] == F(n * n - 2, n * (n * n - 1) * (n * n - 4))
    assert wg3[(1, 0, 2)] == F(-1, (n * n - 1) * (n * n - 4))
    assert wg3[(1, 2, 0)] == F(2, n * (n * n - 1) * (n * n - 4))


def test_haar_moments_count_singlets():
    """int |tr U|^{2k} over SU(3) counts singlets in 3^k x 3bar^k; the determinant
    family counts the one singlet of 3^3."""
    P = L.plaquette((0, 1), (0, 0, 0))
    Pb = L.plaquette((0, 1), (0, 0, 0), True)
    PP = L.product(P, P)
    PPP = L.product(PP, P)
    assert L.inner(P, {P: F(1)}) == 1
    assert L.inner(P, {Pb: F(1)}) == 0
    assert L.inner(PP, {PP: F(1)}) == 2
    assert L.inner(PPP, {PPP: F(1)}) == 6
    assert L.inner(Pb, {PP: F(1)}) == 1  # (3,0): the baryonic vertex
    assert L.inner(P, {L.product(PP, PP): F(1)}) == 3  # (4,1): n = 4 > N, pseudoinverse
    with pytest.raises(NotImplementedError):
        L.inner(L.product(Pb, L.product(Pb, Pb)), {PPP: F(1)})  # pure six: refused


def test_h0_eigenvalues():
    P = L.plaquette((0, 1), (0, 0, 0))
    assert L.apply_h0({P: F(1)}) == {P: F(8, 3)}
    PPb = L.product(P, L.conj(P))
    energies = sorted(e for e, _c in L.eigen_components({PPb: F(1)}))
    # four links, each singlet (0) or adjoint (3/2)
    assert energies == sorted(F(3, 2) * k for k in (0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4))
    for e, comp in L.eigen_components({PPb: F(1)}):
        assert L.is_eigenvector(comp, e)


def test_second_order_constants():
    single = L.Cluster([((0, 1), (0, 0, 0))])
    pair = L.Cluster([((0, 1), (0, 0, 0)), ((0, 1), (1, 0, 0))])
    perp = L.Cluster([((0, 1), (0, 0, 0)), ((0, 2), (0, 0, 0))])
    h2s, _ = single.second_order()
    h2, _ = pair.second_order()
    h2p, _ = perp.second_order()
    assert L.codd(h2, 0, 1) == F(-5, 612)
    assert L.codd(h2p, 0, 1) == F(5, 612)
    assert L.ceven(h2, 0, 1) == F(-11, 306)
    assert L.codd(h2, 0, 0) - L.codd(h2s, 0, 0) + F(3, 4) == F(-11, 306)


def test_chain_amplitude_is_x_quantum():
    x_quantum = F(360421351, 40327601932800)
    w = L.cumulant([((0, 1), (0, 0, 0)), ((0, 1), (1, 0, 0)), ((0, 1), (2, 0, 0))], 1)
    assert L.block_odd(w) == x_quantum
    assert L.block_even(w) == F(948253471, 40327601932800)


def test_corner_cumulant_in_both_bases():
    corner = F(-2580244782961, 398756546697600)
    P = ((0, 1), (0, 0, 0))
    X = ((1, 2), (1, 0, 0))
    w = L.cumulant([P, X, ((2, 0), (0, 0, 0))], 1)
    assert L.block_odd(w) == corner and L.block_even(w) == F(-56022878647, 4153714028100)
    w2 = L.cumulant([P, X, ((0, 2), (0, 0, 0))], 1)
    assert L.block_odd(w2) == -corner and L.block_even(w2) == F(-56022878647, 4153714028100)


def test_neighbour_census():
    P = ((0, 1), (0, 0, 0))
    assert len(L.plaquettes_sharing_a_link([P, ((2, 0), (0, 0, 0))])) == 18
    assert len(L.plaquettes_sharing_a_link([P, ((0, 1), (1, 0, 0))])) == 20
    assert len(L.plaquettes_sharing_a_link([P, ((0, 1), (0, 0, 1))])) == 20


def test_charpoly_spectra_agree_with_the_su3_table():
    P = L.plaquette((0, 1), (0, 0, 0))
    X = L.plaquette((1, 2), (0, 0, 0))
    for word in (L.product(P, L.conj(P)), L.product(P, X), L.product(L.product(P, X), L.conj(X))):
        for link in L.links_of({word: F(1)}):
            a, b = L.content(word).get(link, [0, 0])
            assert set(L.link_spectrum(word, link)) <= set(L.link_energies(a, b))
            # the closure's spectrum contains every energy the content can carry
            # that the word actually populates; at least the largest one appears
            assert max(L.link_spectrum(word, link)) in L.link_energies(a, b)


def test_rank_generic_second_order_matches_the_all_rank_formulas():
    from workhouse import constants as K

    try:
        for n in (4, 5):
            L.set_rank(n)
            pair = L.Cluster([((0, 1), (0, 0, 0)), ((0, 1), (1, 0, 0))])
            h2, _ = pair.second_order()
            t_n = F(K.hopping(n).p, K.hopping(n).q)
            ell_n = F(K.even_hopping(n).p, K.even_hopping(n).q)
            assert L.codd(h2, 0, 1) == -t_n
            assert L.ceven(h2, 0, 1) == ell_n
    finally:
        L.set_rank(3)
