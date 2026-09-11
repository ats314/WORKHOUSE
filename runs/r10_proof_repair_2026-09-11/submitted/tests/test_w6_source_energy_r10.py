"""Tests for W6 source-vacuum energy transport jets (R10)."""

from workhouse.invariants import w6_source_energy_r10


def test_h0_energy_contraction():
    ok, msg = w6_source_energy_r10.check_h0_energy_contraction()
    assert ok
    assert "kappa_P = 1" in msg


def test_h1_fiberwise_score_variance():
    ok, msg = w6_source_energy_r10.check_h1_fiberwise_score_variance()
    assert ok
    assert "kappa_0 g^-2" in msg


def test_h2_conditional_dirichlet_energy():
    ok, msg = w6_source_energy_r10.check_h2_conditional_dirichlet_energy()
    assert ok
    assert "kappa_1 g^-2" in msg


def test_h3_fast_to_source_coupling():
    ok, msg = w6_source_energy_r10.check_h3_fast_to_source_coupling()
    assert ok
    assert "kappa_2 g^-2" in msg


def test_h4_vacuum_cross_source_energy():
    ok, msg = w6_source_energy_r10.check_h4_vacuum_cross_source_energy()
    assert ok
    assert "kappa_3 g^-2" in msg


def test_r10_order_zero_bound():
    ok, msg = w6_source_energy_r10.check_r10_order_zero_bound()
    assert ok
    assert "d_0 g^-1" in msg


def test_vacuum_cross_derivatives():
    ok, msg = w6_source_energy_r10.check_vacuum_cross_derivatives()
    assert ok
    assert "d_nu,r g^(-r-1)" in msg


def test_kato_projection_derivatives():
    ok, msg = w6_source_energy_r10.check_kato_projection_derivatives()
    assert ok
    assert "d_P,r g^(-r-1)" in msg


def test_transported_residual_bridge():
    ok, msg = w6_source_energy_r10.check_transported_residual_bridge()
    assert ok
    assert "M_j(s) <= c_j s^-j" in msg
