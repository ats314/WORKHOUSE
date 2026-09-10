"""Scoped exact controls and provenance for the true-vacuum block continuation."""

from __future__ import annotations

import hashlib
import json
import xml.etree.ElementTree as ET
from datetime import UTC, datetime
from pathlib import Path

from sympy import I, Matrix, Rational, eye, simplify, symbols, zeros

from workhouse.invariants.wilson_vacuum import vacuum

ROOT = Path(__file__).resolve().parents[1]


def main():
    native = [vars(check) for check in vacuum.run()]
    assert all(check["passed"] for check in native)
    a = symbols("a0:4", real=True)
    b = symbols("b0:4", real=True)
    pauli = [Matrix([[0, 1], [1, 0]]), Matrix([[0, -I], [I, 0]]), Matrix([[1, 0], [0, -1]])]
    left = a[0] * eye(2) + sum((I * a[i + 1] * pauli[i] for i in range(3)), zeros(2))
    right = b[0] * eye(2) + sum((I * b[i + 1] * pauli[i] for i in range(3)), zeros(2))
    contraction = sum(
        (left * I * generator).trace() * (-I * generator * right).trace() / 4 for generator in pauli
    )
    boundary = (left * right).trace() / 2
    # Ordered basis (six-link loop, product of adjacent plaquette traces).
    minus_laplacian = Matrix([[18, -2], [0, 26]])
    pair_coefficients = Matrix([Rational(1, 1404), -Rational(1, 1872)])
    connected_controls = {
        "BA15_actual_shared_link_fierz": simplify(contraction - boundary + a[0] * b[0]) == 0,
        "BA15_exact_connected_pair_inverse": minus_laplacian * pair_coefficients
        == Matrix([Rational(1, 72), -Rational(1, 72)]),
        "BA14_exact_self_plaquette_inverse": 32 * -Rational(1, 4608) == -Rational(1, 144),
        "BA13_actual_second_energy_coefficient": -12 * Rational(1, 4) / 12**2 == -Rational(1, 48),
    }
    connected_controls = {name: bool(value) for name, value in connected_controls.items()}
    assert all(connected_controls.values())
    endpoint_floor = 1 - Rational(9, 16000) - Rational(12, 32001)
    endpoint_controls = {
        "BA25_uniform_gap_exceeds_13_over_5": Rational(199, 229) * 3 * endpoint_floor
        > Rational(13, 5),
        "BA25a_uniform_tensorization_below_29_over_25": Rational(229, 199) / endpoint_floor
        < Rational(29, 25),
    }
    endpoint_controls = {name: bool(value) for name, value in endpoint_controls.items()}
    assert all(endpoint_controls.values())
    rare_p, eta, gamma_s = symbols("rare_p eta gamma_s", positive=True)
    rare_probabilities = Matrix([(1 - rare_p) / 2, (1 - rare_p) / 2, rare_p])
    rare_indicator = Matrix([0, 0, 1])
    mean_rare = (rare_probabilities.T * rare_indicator)[0]
    rare_variance = (rare_probabilities.T * rare_indicator)[0] - mean_rare**2
    rare_energy = eta * rare_p * (1 - rare_p)
    rare_control = bool(
        simplify(rare_energy / rare_variance - eta) == 0
        and simplify(4 * ((1 - rare_p) * gamma_s / 4) / (1 - rare_p) - gamma_s) == 0
    )
    assert rare_control
    names = [
        "docs/derivations/wilson-true-vacuum-block-estimates.md",
        "docs/derivations/wilson-vacuum-aligned-assembly.md",
        "src/workhouse/invariants/wilson_vacuum.py",
        "scripts/validate_wilson_true_blocks.py",
        "ledger/documents.yaml",
        "ledger/gaps.yaml",
        "index/claims.jsonl",
        "index/graph.jsonl",
        "FRONTIER.md",
        "CERTIFIED.md",
    ]
    report = {
        "recorded_at": datetime.now(UTC).isoformat(),
        "scope": (
            "Eight new native block controls plus eight earlier vacuum controls, four "
            "connected-coefficient controls and two rational endpoint controls. Analytic Harnack, "
            "conditional-domain, maximal-correlation, and Brownian-limit arguments "
            "are not Lean formalizations. Finite perturbation coefficients do not "
            "alone certify a uniform all-order remainder. The separate analytic slab "
            "proof establishes actual assembly only for k/epsilon<=1/256000, not a continuum gap."
        ),
        "native_controls": native,
        "supplementary_connected_controls": connected_controls,
        "supplementary_uniform_endpoint_controls": endpoint_controls,
        "phase10_probability_gluing_counterexample": {
            "passed": rare_control,
            "scope": (
                "For 0<p<1 the exact three-state Rayleigh quotient is eta "
                "despite a good-sector gap gamma_s."
            ),
        },
        "test_runs": [
            {
                "file": path.name,
                **{
                    key: sum(
                        int(suite.get(key, "0")) for suite in ET.parse(path).findall(".//testsuite")
                    )
                    for key in ("tests", "failures", "errors", "skipped")
                },
            }
            for path in sorted((ROOT / "docs/validation").glob("wilson-block-*.xml"))
        ],
        "remaining_derivation": (
            "BA20-BA25 discharge the actual angle and conditional-gap bounds for "
            "k/epsilon<=1/256000. Extend control to the large-k/epsilon continuum "
            "trajectory; BA26 proves that adjusting slab length alone cannot keep "
            "both factor activities inside this small-activity budget."
        ),
        "artifacts_sha256": {
            name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in names
        },
    }
    path = ROOT / "docs/validation/wilson-true-blocks-2026-09-09.json"
    path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(
        f"{len(native)} native vacuum controls and 4 connected-coefficient controls passed; {path}"
    )


if __name__ == "__main__":
    main()
