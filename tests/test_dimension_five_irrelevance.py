"""Tests for the dimension-five irrelevance and multiscale Cauchy summability invariant suite."""

from workhouse.invariants.dimension_five_irrelevance import (
    _check_cauchy_sum,
    _check_dim_6_leading,
    _check_no_dim_5,
    _check_scaling_gain,
    _check_so4_restoration,
    dim5,
)


def test_no_dim_5_check():
    passed, detail = _check_no_dim_5()
    assert passed is True
    assert "odd Lorentz index count 5" in detail
    assert "parity-odd" in detail


def test_dim_6_leading_check():
    passed, detail = _check_dim_6_leading()
    assert passed is True
    assert "operator realization is separate" in detail


def test_scaling_gain_check():
    passed, detail, val = _check_scaling_gain()
    assert passed is True
    assert "1/9" in detail
    assert "DIM6_MULTISCALE_GAIN" in val


def test_cauchy_sum_check():
    passed, detail, val = _check_cauchy_sum()
    assert passed is True
    assert "9/8" in detail
    assert "CAUCHY_GEOMETRIC_SUM" in val


def test_so4_restoration_check():
    passed, detail = _check_so4_restoration()
    assert passed is True
    assert "requires the separate model estimates" in detail
    assert "establishing OS1" not in detail


def test_dim5_suite_run():
    results = dim5.run()
    assert len(results) == 5
    assert all(r.passed for r in results)
