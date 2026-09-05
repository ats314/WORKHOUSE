"""Exact finite-support controls for the resolvent-composed creator map.

The analytic theorem controls a complete ball; the sample checks below only
recompute their expressly named finite-binary instances.
"""

from fractions import Fraction

from ..rooted_creator import (
    family,
    flip,
    flow_tangent_controls,
    sample_controls,
    sample_families,
    star,
    star_exp,
    star_log,
    theorem_constants,
)
from ._core import _suite

rooted_creator_suite = _suite("the resolvent-composed rooted creator map: exact finite controls")
PROOF = "paper/research_notes/G18_ROOTED_WILSON_CONTRACTION_20260905.md"


@rooted_creator_suite.check(
    "the moving-weight creator constants place the six-link Pauli model inside the "
    "explicit contraction domain using a rational upper bound for atanh(kappa)",
    "G18; " + PROOF + " equations (2), (3a), (3b); exact rational specialization",
)
def _():
    data = theorem_constants()
    ok = (
        tuple(data[key] for key in ("A", "B", "C", "L"))
        == (Fraction(16900, 9), Fraction(33280, 9), Fraction(6500), Fraction(619360, 9))
        and data["u_star"] == Fraction(9, 9_909_760)
        and 0 < data["u_upper"] < data["u_star"]
        and all(value > 0 for key, value in data.items() if key.endswith("margin"))
    )
    return ok, (
        f"R=1/4, weight=2, gamma=1/2, tau0=J=1: u_star={data['u_star']}; "
        f"atanh(1/10^8)<=u_upper={data['u_upper']}; all four margins are positive. "
        "The analytic bound log(2)>=1/2 supplies the stated kinetic and weight premises."
    )


@rooted_creator_suite.check(
    "finite disjoint-support creator exp/log invert exactly, and a Pauli-flip "
    "negative control detects replacement of the nilpotent creator product",
    "G18; " + PROOF + " section 2; exact six-link bitmask creator algebra",
)
def _():
    inputs = sample_families()
    single = family(2, ((1, Fraction(1)),))
    inversion = all(star_log(star_exp(value)) == value for value in inputs.values())
    negative_control = star(single, single) == family(2) and flip(single, 1) != family(2)
    return inversion and negative_control, (
        "Three exact inputs: zero, one six-link creator, and 63 mixed coefficients; "
        f"log(exp(v))=v: {inversion}; creator-square versus flip-square control: "
        f"{negative_control}. No support truncation occurs within the six-link model."
    )


@rooted_creator_suite.check(
    "the normalized magnetic creator-flow differential equals direct nilpotent "
    "operator conjugation on three exact six-link families",
    "G18; " + PROOF + " sections 2 and 4; separate output-partition and basis-action paths",
)
def _():
    data = {name: flow_tangent_controls(value) for name, value in sample_families().items()}
    return all(all(checks.values()) for checks in data.values()), (
        f"{data}; the operator path applies raising operators to input basis vectors, "
        "while the differential path uses the normalized star logarithm."
    )


@rooted_creator_suite.check(
    "the full kinetic resolvent-composed creator map preserves the radius-1/16 "
    "ball on three specified six-link inputs and has pair ratios below one half",
    "G18; " + PROOF + " equation (19); exact finite-binary instances only",
)
def _():
    data = sample_controls()
    return data.passed, (
        f"input norms={data.input_norms}; all three exact image norms<=1/16 and "
        "all three exact pair ratios<=1/2; nonzero normalizers and the independent "
        f"mixed-kick zero-input formula checked={data.normalizers_nonzero and data.zero_formula}. "
        "This finite sample control does not replace the complete-ball analytic proof."
    )
