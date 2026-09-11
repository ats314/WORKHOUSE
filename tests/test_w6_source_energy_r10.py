"""Adversarial checks for R10 proof repairs and scientific-status boundaries."""

import sympy as sp

from workhouse import derivation_statements
from workhouse.invariants import w6_source_energy_r10 as r10


def test_changing_measure_term_is_required():
    actual, frozen, correction = r10.conditional_derivative_terms(r10.Y)
    assert actual == sp.Rational(1, 6)
    assert actual != frozen
    assert actual == frozen + correction


def test_corrected_rule_handles_explicit_w_dependence():
    phi = r10.Y + r10.W * r10.Y**2
    actual, frozen, correction = r10.conditional_derivative_terms(phi)
    assert frozen == sp.Rational(1, 3)
    assert correction == sp.Rational(1, 6)
    assert actual == sp.Rational(1, 2)


def test_independent_measure_has_zero_correction():
    actual, frozen, correction = r10.conditional_derivative_terms(r10.W * r10.Y**2, a=0)
    assert actual == frozen == sp.Rational(1, 3)
    assert correction == 0


def test_centered_product_cannot_drop_measure_derivative():
    actual, frozen, correction = r10.conditional_derivative_terms((r10.Y - r10.W / 6) ** 2)
    assert actual == -r10.W / 18
    assert frozen == 0
    assert correction == actual


def test_full_projection_recurrence_and_missing_term_mutant():
    t, jets, missing = r10.projection_jet_data()
    assert all(
        (actual - represented).applyfunc(sp.simplify) == sp.zeros(2) for actual, represented in jets
    )
    actual, represented = jets[2]
    truncated = represented - missing
    assert (actual - truncated).subs(t, 1) == sp.Matrix([[0, -1], [-1, 0]])


def test_registered_counterchecks_detect_the_two_power_errors():
    assert r10.check_diffusion_gap_power()[0]
    assert r10.check_covariance_power_obstruction()[0]


def test_conditional_repair_does_not_close_the_actual_target():
    docs = derivation_statements.load()["documents"]
    rows = {s["id"]: s for d in docs for s in d["statements"]}
    assert rows["DERIV:W6_GROUND_JETS_TRANSPORT_BUDGET:SOURCE_ENERGY_JETS_R10"]["status"] == "open"
    assert (
        rows["DERIV:W6_SOURCE_GENERATOR_SCORE_FRAME:CONDITIONAL_ENERGY_H0_H4"]["status"] == "open"
    )
    assert (
        rows["DERIV:W6_SOURCE_GENERATOR_SCORE_FRAME:R10_ORDER_ZERO_REDUCTION"]["status"]
        == "conditional"
    )
    reduction = rows["DERIV:W6_SOURCE_ENERGY_JETS_R10:H4_FROM_H0"]
    assert reduction["status"] == "proven"
    assert any("H0" in h for h in reduction["hypotheses"])
    assert reduction["lean"] == []
