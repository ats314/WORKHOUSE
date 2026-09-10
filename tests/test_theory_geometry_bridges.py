"""Exact algebra and scope counterexamples for the new geometry bridges."""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest
import sympy as sp

PATH = Path(__file__).resolve().parents[1] / "scripts" / "verify_theory_geometry_bridges.py"
SPEC = importlib.util.spec_from_file_location("theory_geometry_bridges", PATH)
assert SPEC is not None and SPEC.loader is not None
BRIDGES = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BRIDGES)


@pytest.mark.parametrize("name", list(BRIDGES.CHECKERS))
def test_exact_bridge_controls(name):
    passed, evidence = BRIDGES.CHECKERS[name]()
    assert passed, evidence


def test_three_coordinate_bound_must_not_be_extended_to_four():
    value = BRIDGES.anisotropy_variance([sp.Rational(4, 5), *([sp.Rational(1, 15)] * 3)])
    assert value == sp.Rational(484, 5625)
    assert value > sp.Rational(2, 25)


def test_zero_and_nodal_inputs_do_not_give_strict_energy_bounds():
    for coordinates in (
        [0, 0, 0],
        [1, 0, 0],
        [sp.Rational(1, 2)] * 2 + [0],
        [sp.Rational(1, 3)] * 3,
    ):
        assert BRIDGES.anisotropy_variance(coordinates) == 0


def test_full_graph_and_exchange_are_necessary():
    checks = BRIDGES.source_congruence_residuals()
    assert checks["omitted_exchange_rejected"]
    assert checks["frozen_graph_rejected"]
