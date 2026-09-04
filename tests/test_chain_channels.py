"""The channel decomposition of the two-hop weight sums to u and labels every energy."""

from fractions import Fraction as F

from workhouse import chain_channels as CC


def test_labels_are_the_irrep_excesses():
    ex = CC.excess_table(3)
    assert ex["lam"] == F(1) and ex["adj"] == F(9, 4) and ex["sym"] == F(5, 2)
    # N = 3 coincidences: 4 + 2 lam = 6 and 4 + sym = 2 + 2 adj; the position fixes the reading
    assert CC.label_energy(3, F(6), "middle") == (4, ("lam", "lam"))
    assert CC.label_energy(4, F(20, 3), "middle") == (4, ("lam", "lam"))
    assert CC.label_energy(3, F(13, 2), "middle") == (4, ("sym",))
    assert CC.label_energy(3, F(2), "outer") == (2, ())
    assert CC.label_energy(3, F(4), "outer") == (4, ())
    assert CC.label_energy(3, F(17, 4), "outer") == (2, ("adj",))
    assert CC.label_energy(3, F(6), "outer") is None


def test_coplanar_chain_decomposes_into_74_channels_summing_to_x_quantum():
    d = CC.decompose(CC.COPLANAR, 3)
    assert len(d) == 74
    assert sum(1 for k in d if k[0] == "direct") == 58
    assert sum(1 for k in d if k[0] == "fold3") == 16
    assert sum(d.values()) == F(360421351, 40327601932800)
    # the pure-fundamental chain channel: -4/(N(N^2-1)^3) at N = 3
    assert d[("direct", (2, ()), (4, ()), (2, ()))] == F(-4, 3 * 8**3)
