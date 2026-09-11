"""Tests for W6 conditional score tail control and M10 domination."""

from workhouse.invariants import w6_score_tail_m10 as m


def test_suite_registration():
    suite = m.score_tail
    assert suite.name == "W6 conditional score tail control (M10)"
    assert len(suite.checks) == 9


def test_synchronized_tangency():
    passed, detail = m.check_synchronized_tangency_s12_s13()
    assert passed, detail


def test_quadratic_jet_bound():
    passed, detail = m.check_quadratic_jet_bound_cF()
    assert passed, detail


def test_agmon_tube_moments():
    passed, detail = m.check_agmon_tube_moments_s14()
    assert passed, detail


def test_relative_amplitude_gradient():
    passed, detail = m.check_relative_amplitude_gradient()
    assert passed, detail


def test_tube_variance_bound():
    passed, detail = m.check_tube_variance_bound_s14()
    assert passed, detail


def test_outside_deviation_bound():
    passed, detail = m.check_outside_deviation_bound_s15()
    assert passed, detail


def test_antipodal_gauge_variance():
    passed, detail = m.check_antipodal_gauge_variance()
    assert passed, detail


def test_m10_score_domination():
    passed, detail = m.check_m10_score_domination()
    assert passed, detail


def test_hardy_constant_instantiation():
    passed, detail = m.check_hardy_constant_instantiation_m11_m15()
    assert passed, detail
