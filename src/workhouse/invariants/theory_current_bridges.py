"""Exact controls for the reviewed current and geometry derivations.

The source statements retain their analytic/domain hypotheses. These checks
certify the named algebra and finite controls, not the full physical theorem.
"""

from __future__ import annotations

import json
import runpy
from functools import lru_cache
from pathlib import Path

import sympy as sp

from ._core import _suite

bridges = _suite("reviewed theory current and geometry bridges")
_ROOT = Path(__file__).resolve().parents[3]
_GEOMETRY = "THEORY_GEOMETRY_RICCATI_BRIDGES; TG1-TG8; G14; G19"
_SOURCE = "SOURCE_CURRENT_SPECTRAL_BRIDGES; SCB0A-SCB6; G19"
_OPERATOR = "complete square first cometric and differential operator identity"
_CURRENT = "complete square first residual current exact Gaussian moments"
_BUDGET = "complete square first current joint radial bound below one over 840"


@lru_cache(maxsize=2)
def _checks(script: str):
    return runpy.run_path(str(_ROOT / "scripts" / script))


@bridges.check("three-coordinate sharp anisotropy stationary and boundary algebra", _GEOMETRY)
def _sharp_anisotropy():
    passed, detail = _checks("verify_theory_geometry_bridges.py")["check_anisotropy_maximum"]()
    return passed, detail, {"ANISOTROPY_THREE_RATIONAL_UPPER": sp.Rational(2, 25)}


@bridges.check("Hodge secular cubic and induced eighth-order moment identities", _GEOMETRY)
def _hodge_moments():
    return _checks("verify_theory_geometry_bridges.py")["check_hodge_secular_and_moments"]()


@bridges.check("full Schur source congruence and retained metric algebra", _GEOMETRY)
def _source_congruence():
    return _checks("verify_theory_geometry_bridges.py")["check_source_congruence"]()


@bridges.check("scalar-source Schur parity and mixed-parity negative control", _GEOMETRY)
def _scalar_parity():
    return _checks("verify_theory_geometry_bridges.py")["check_scalar_source_parity"]()


@bridges.check(
    "abstract Riccati default contraction and residual amplification constants", _GEOMETRY
)
def _riccati_constants():
    return _checks("verify_theory_geometry_bridges.py")["check_riccati_default"]()


def _source_control(function: str):
    record = _checks("verify_source_current_bridges.py")[function]()
    return record["passed"], json.dumps(record, sort_keys=True)


@bridges.check(_OPERATOR, _SOURCE)
def _square_operator():
    return _source_control("cometric_and_operator_control")


@bridges.check(_CURRENT, _SOURCE, rests_on=(_OPERATOR,))
def _square_current():
    return _source_control("current_moment_control")


@bridges.check(_BUDGET, _SOURCE, rests_on=(_CURRENT,))
def _square_budget():
    passed, detail = _source_control("radial_budget_control")
    return passed, detail, {"SQUARE_FIRST_CURRENT_RATIONAL_UPPER": sp.Rational(1, 840)}


@bridges.check("degenerate energy square completion and kernel example", _SOURCE)
def _variational_completion():
    return _source_control("variational_completion_control")


@bridges.check("selected inverse testing and moving source centering algebra", _SOURCE)
def _residual_centering():
    return _source_control("residual_and_centering_control")


@bridges.check("tiny exponential tangent and incomplete source dark-state counterexample", _SOURCE)
def _source_totality_control():
    return _source_control("source_totality_negative_control")


@bridges.check(
    "normalized exponential variance and cumulant double-integral polynomial identity", _SOURCE
)
def _normalized_sources():
    return _source_control("normalized_source_control")
