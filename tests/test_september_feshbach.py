"""Regression shields for the September source integration and its scope repairs."""

from fractions import Fraction

import sympy as sp

from workhouse.invariants import feshbach_resolvent as FR
from workhouse.invariants import hodge_feshbach as HF


def test_one_r_word_is_a_nonzero_multiple_of_the_b_monomial():
    # The former checker compared only with q*e2 itself, missing -2*q*e2.
    q, e2, _e3 = HF._elementary()
    b_monomial = HF.KO._mul(q, e2)
    table = HF._table(2)
    for word in ("UR", "RU"):
        sigma, defect = table[word]
        assert sigma != b_monomial
        assert sigma == HF._scale(b_monomial, Fraction(-2))
        assert not defect


def test_ur_lies_outside_the_actual_fourth_order_carrier_span():
    q, e2, _e3 = HF._elementary()
    span = [q, HF.KO._mul(q, q), e2]
    sigma = HF._table(2)["UR"][0]
    exponents = sorted({key for polynomial in [*span, sigma] for key in polynomial})
    matrix = sp.Matrix([[sp.Rational(p.get(key, 0)) for p in span] for key in exponents])
    rhs = sp.Matrix([sp.Rational(sigma.get(key, 0)) for key in exponents])
    assert matrix.rank() == 3
    assert matrix.row_join(rhs).rank() == 4


def test_gamma_has_no_nonzero_carrier_to_normalize():
    # z_j=1 evaluates a Laurent polynomial by summing its coefficients.
    q, _e2, _e3 = HF._elementary()
    assert sum(q.values()) == 0
    assert all(sum(component.values()) == 0 for component in HF._psi().values())
    down = HF.KO.bloch_matrix(HF.KO.down_laplacian())
    up = HF.KO.bloch_matrix(HF.KO.up_laplacian())
    assert all(
        sum(entries.values()) == 0
        for matrix in (down, up)
        for row in matrix.values()
        for entries in row.values()
    )


def test_floating_spectral_checks_are_never_t1():
    tiers = {name: tier for name, _section, tier, _fn in FR.feshbach.checks}
    assert sum(tier == 1 for tier in tiers.values()) == 2
    assert sum(tier == 2 for tier in tiers.values()) == 3
    assert all(
        tier == 2
        for name, tier in tiers.items()
        if "explicit constant" in name or "volume-stable" in name or "FINDING:" in name
    )


def test_variational_sandwich_keeps_optimizer_orientation_for_both_signs():
    for g in (sp.Rational(-1, 3), sp.Rational(1, 4)):
        a0 = sp.Matrix([[3, 1], [1, 2]])
        v = sp.Matrix([[2, -1], [-1, 1]])
        ag = a0 + g * v
        w = sp.Matrix([1, 3])
        assert a0.is_positive_definite and ag.is_positive_definite
        u0, ug = a0.inv() * w, ag.inv() * w
        value = ((u0 - ug).T * w)[0]
        assert g * (ug.T * v * ug)[0] <= value <= g * (u0.T * v * u0)[0]


def test_relative_margin_failure_does_not_imply_loss_of_positivity():
    a0 = sp.eye(2)
    v = sp.eye(2)
    g = sp.Integer(2)
    kappa = sp.Integer(1)
    assert 1 - abs(g) * kappa < 0
    assert (a0 + g * v).is_positive_definite
