"""Boundary, mutation and independent controls for the local formal spectrum."""

import pytest
import sympy as sp

from workhouse import local_class_wick as wick
from workhouse.invariants import local_class_wick as checks


def test_zero_order_and_invalid_branches():
    assert wick.gap_series("even", 0) == (2,)
    assert wick.gap_series("odd", 0) == (3,)
    for parity in ("other", "", None):
        with pytest.raises(ValueError):
            wick.gap_series(parity)
    with pytest.raises(ValueError):
        wick.eigen_series(1, 2)
    with pytest.raises(ValueError):
        wick.eigen_series(2, -1)


def test_radial_reduction_mutant_loses_the_known_angular_term():
    true = wick.gap_series("even")[2].subs(checks.RANK, 3)
    radial = -sp.Rational(327, 9216)
    assert true != radial
    assert true - radial == sp.Rational(1, 576)


def test_small_rank_identities_and_covariance_normalization():
    assert checks.check_quotient()[0]
    rank = checks.RANK
    assert (
        sp.cancel(
            wick.moment((3, 3)).as_expr()
            - 3 * (rank - 2) * (rank - 1) * (rank + 1) * (rank + 2) / (8 * rank)
        )
        == 0
    )
    assert sp.cancel(wick.moment((2,)).as_expr() - (rank**2 - 1) / 2) == 0


def test_wrong_sign_and_invalid_denominator_are_not_certified():
    even = wick.gap_series("even")[5]
    assert all(x > 0 for x in checks.sign_witness("even", even))
    assert not all(x > 0 for x in checks.sign_witness("even", -even))
    with pytest.raises(ArithmeticError):
        checks.sign_witness("even", -1 / (checks.RANK + 1))


def test_resolvent_retains_all_nonresonant_shells():
    p = wick.monomial((3, 4))
    s = 3
    r = wick.resolvent(p, s)
    q = wick.add(p, wick.scale(wick.shell(p, s), -1))
    assert not wick.add(wick.scale(r, s), wick.scale(wick.number(r), -1), wick.scale(q, -1))
    assert wick.shell(r, s) == {}


def test_final_su3_anchors_are_rederived():
    even = wick.beta_coefficients("even")
    odd = wick.beta_coefficients("odd")
    assert even[4].subs(checks.RANK, 3) == -sp.Rational(56673445, 1528823808)
    assert odd[4].subs(checks.RANK, 3) == -sp.Rational(290599777, 6115295232)
    assert sp.simplify(odd[3].subs(checks.RANK, 3) / sp.sqrt(6)) == -sp.Rational(
        15674731, 764411904
    )


def test_recorded_coefficients_compare_by_exact_identity():
    assert checks.check_coefficients()[0]


def test_cartesian_oracle_preserves_received_source_tree(tmp_path, monkeypatch):
    source = checks.RECEIVED / "independent_su3.py"
    target = tmp_path / source.name
    original = source.read_bytes()
    target.write_bytes(original)
    monkeypatch.setattr(checks, "RECEIVED", tmp_path)
    assert checks.cartesian_gaps.__wrapped__(2, 0) == {"even": (2,)}
    assert target.read_bytes() == original
    assert list(tmp_path.iterdir()) == [target]
