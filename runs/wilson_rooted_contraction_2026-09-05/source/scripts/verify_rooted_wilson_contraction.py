"""Record exact finite controls supporting the analytic rooted contraction theorem."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import asdict
from pathlib import Path

import sympy

from workhouse.invariants.rooted_creator import rooted_creator_suite
from workhouse.rooted_creator import sample_controls, theorem_constants

ROOT = Path(__file__).resolve().parents[1]
SOURCES = (
    "scripts/verify_rooted_wilson_contraction.py",
    "scripts/verify_rooted_creator_obstruction.py",
    "src/workhouse/rooted_creator.py",
    "src/workhouse/invariants/rooted_creator.py",
    "tests/test_rooted_creator.py",
    "lean/Workhouse/RootedScalarBounds.lean",
    "lean/Workhouse.lean",
    "paper/research_notes/G18_ROOTED_WILSON_CONTRACTION_20260905.md",
    "paper/research_notes/G18_WILSON_CREATOR_THERMODYNAMIC_LIMIT_20260905.md",
    "paper/research_notes/G18_SAME_WEIGHT_CREATOR_OBSTRUCTION_20260905.md",
)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError("Choose a fresh output path; existing evidence is preserved")
    results = list(rooted_creator_suite.run())
    if not all(result.passed for result in results):
        raise AssertionError(results)
    report = {
        "schema": "workhouse-rooted-wilson-contraction/v1",
        "passed": True,
        "exact_check_count": len(results),
        "checks": [asdict(result) for result in results],
        "finite_binary_controls": asdict(sample_controls()),
        "finite_model_constants": theorem_constants(),
        "analytic_result": {
            "evidence": "written Hilbert-space proofs, independently reviewed",
            "hypotheses": [
                "four distinct links per interaction, at most four interactions per link",
                "bounded local potentials of norm at most J_star",
                "additive free kinetic energy with link vacuum and excited gap gamma > 0",
                "0 < tau <= tau0 and mu >= gamma*tau0/2",
            ],
            "u_star": "min(9*gamma/(309680*J_star*exp(4*mu)), 9/(8450*tau0*J_star*exp(4*mu)))",
            "creator_ball_radius": "1/16",
            "contraction_constant_bound": "1/2",
            "infinite_lattice_object": "analytic stabilized creator coefficient family",
            "local_root_error": "(1/8)*q^(N+1)/(1-q), q=abs(u)/r < 1, r < u_star",
        },
        "verification_scope": "The passed field concerns the finite exact checks above. "
        "They do not machine-certify the analytic contraction theorem or its "
        "infinite-lattice consequence. The separate Lean theorem certifies "
        "a real rational Taylor inequality used in the active-plaquette obstruction.",
        "remaining_operator_work": [
            "physical state and GNS realization of the coefficient family",
            "controlled unitary chart or justified physical metric",
            "complete excited Riesz range and weighted source identification",
        ],
        "base_revision": "e6380a25a88ea4764deeb32358967ee44e3ecfe4",
        "sources": {
            name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in SOURCES
        },
        "runtime": {"python": sys.version.split()[0], "sympy": sympy.__version__},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(report, indent=2, sort_keys=True, default=str) + "\n")
    print(f"{len(results)}/{len(results)} exact finite controls passed; wrote {args.output}")


if __name__ == "__main__":
    main()
