"""Replay exact controls and a separately labelled rotor spectral diagnostic."""

from __future__ import annotations

import hashlib
import json
import math
import xml.etree.ElementTree as ET
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def conditional_barrier_controls() -> dict[str, bool]:
    """Supplementary exact algebra; spectral and direct-integral proofs are analytic."""
    from sympy import I, Matrix, Rational, eye, simplify, sqrt, symbols

    a, b, c, d = symbols("a b c d", real=True)
    quaternion = Matrix([[a + I * d, c + I * b], [-c + I * b, a - I * d]])
    gram = (quaternion.conjugate().T * quaternion).applyfunc(simplify)
    threshold = sqrt(32) / 2 - 3 / sqrt(2)
    r, eigenvalue = symbols("r eigenvalue", real=True)
    p1 = Matrix([[1, 0], [0, 0]])
    vector = Matrix([r, sqrt(1 - r**2)])
    p2 = vector * vector.T
    assembly = 2 * eye(2) - p1 - p2
    return {
        "staple_quaternion_gram": gram == (a**2 + b**2 + c**2 + d**2) * eye(2),
        "threshold_32_bad_region": simplify(threshold - 1 / sqrt(2)) == 0,
        "bad_region_exceeds_good_gap": simplify(threshold - 1 / (16 * sqrt(2)))
        == 15 * sqrt(2) / 32
        > 0,
        "plaquette_four_edge_allocation": 4 * Rational(1, 4) == 1,
        "projection_assembly_requires_geometry": simplify(
            (assembly - eigenvalue * eye(2)).det() - ((eigenvalue - 1) ** 2 - r**2)
        )
        == 0,
    }


def rotor_spectrum(k: float, size: int) -> dict[str, float]:
    """Rayleigh--Ritz in full angular sectors using Gegenbauer recurrences.

    Individual truncated eigenvalues are variational upper estimates; their
    difference is NOT a certified bound on the true gap. This is a diagnostic.
    """
    levels = []
    for ell in (0, 1):
        diagonal = [(n + ell) * (n + ell + 2) + k for n in range(size)]
        off_diagonal = [
            -k * math.sqrt((j + 1) * (j + 2 * ell + 2) / ((j + ell + 1) * (j + ell + 2))) / 2
            for j in range(size - 1)
        ]
        # Gershgorin brackets and the exact tridiagonal LDL Sturm recurrence.
        radii = [
            (abs(off_diagonal[j - 1]) if j else 0) + (abs(off_diagonal[j]) if j < size - 1 else 0)
            for j in range(size)
        ]
        lower = min(d - r for d, r in zip(diagonal, radii, strict=True)) - 1
        upper = max(d + r for d, r in zip(diagonal, radii, strict=True)) + 1

        def below(value: float, diagonal=diagonal, off_diagonal=off_diagonal) -> int:
            pivot = diagonal[0] - value
            count = int(pivot < 0)
            for j in range(1, size):
                if abs(pivot) < 1e-100:
                    pivot = -1e-100
                pivot = diagonal[j] - value - off_diagonal[j - 1] ** 2 / pivot
                count += int(pivot < 0)
            return count

        eigenvalues = []
        for index in (0, 1):
            left, right = lower, upper
            for _ in range(100):
                middle = (left + right) / 2
                if below(middle) <= index:
                    left = middle
                else:
                    right = middle
            eigenvalues.append((left + right) / 2)
        levels.append(eigenvalues)
    return {
        "ground": float(levels[0][0]),
        "radial_first": float(levels[0][1]),
        "angular_first": float(levels[1][0]),
        "gap_diagnostic": float(min(levels[0][1], levels[1][0]) - levels[0][0]),
    }


def main() -> None:
    from workhouse.invariants.wilson_weighted import weighted

    checks = [vars(result) for result in weighted.run()]
    if not all(check["passed"] for check in checks):
        raise ValueError(checks)
    conditional = {name: bool(value) for name, value in conditional_barrier_controls().items()}
    if not all(conditional.values()):
        raise ValueError(conditional)
    diagnostics = []
    for k in (0.0, 0.01, 1.0, 2.5, 10.0, 64.0, 1000.0, 1000000.0):
        small, large = rotor_spectrum(k, 128), rotor_spectrum(k, 256)
        bound = max(0.5, k**0.5 / 16)
        drift = abs(small["gap_diagnostic"] - large["gap_diagnostic"])
        if drift > 0.000001 * max(1.0, abs(large["gap_diagnostic"])):
            raise ValueError(f"Unconverged diagnostic at k={k}: {drift}")
        if large["gap_diagnostic"] < bound:
            raise ValueError(f"Spectral diagnostic contradicts claimed bound at k={k}")
        diagnostics.append(
            {
                "c": 1,
                "k": k,
                "size_128": small,
                "size_256": large,
                "gap_drift": drift,
                "analytic_bound_WR11": bound,
            }
        )
    artifacts = (
        "docs/derivations/wilson-weighted-repair-and-rotor-gap.md",
        "src/workhouse/invariants/wilson_weighted.py",
        "src/workhouse/invariants/__init__.py",
        "scripts/validate_wilson_weighted.py",
        "ledger/documents.yaml",
        "ledger/gaps.yaml",
        "index/claims.jsonl",
        "index/graph.jsonl",
        "FRONTIER.md",
        "CERTIFIED.md",
    )
    tests = []
    for path in sorted((ROOT / "docs/validation").glob("wilson-weighted-*.xml")):
        suites = ET.parse(path).findall(".//testsuite")
        tests.append(
            {
                "file": path.name,
                **{
                    key: sum(int(suite.get(key, "0")) for suite in suites)
                    for key in ("tests", "failures", "errors", "skipped")
                },
            }
        )
    report = {
        "recorded_at": datetime.now(UTC).isoformat(),
        "analytic_scope": (
            "WR1-WR12: integrated Wilson class diffusion gap and explicit complete "
            "compact rotor gap. WR13-WR16: nonnegative trial residual for the actual "
            "overlapping lattice. WR20-WR21: exact true-ground boundary-form embedding. "
            "WR22-WR24: uniform actual-link fast barrier on the full compact boundary "
            "space, including cancellation of staples. WR25-WR26 retain the unresolved "
            "vacuum-frustration term in the actual link assembly. "
            "Analytic domain, eigenfunction and min-max arguments are not Lean-formalized."
        ),
        "unresolved": (
            "Uniform connected residual and selected-source assembly on the actual "
            "lattice with complete boundary retention, followed by spatial continuum "
            "and physical-clock transport. A fixed finite unreduced frame is insufficient."
        ),
        "checks": checks,
        "supplementary_exact_conditional_barrier_controls": conditional,
        "spectral_diagnostic_scope": (
            "Floating Rayleigh-Ritz consistency check, c=1 and eight k values; 128/256 "
            "basis sizes agree within relative tolerance 0.000001. Differences of "
            "variational upper eigenvalues are not certified true gap bounds."
        ),
        "spectral_diagnostics": diagnostics,
        "test_runs": tests,
        "artifacts": {
            name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in artifacts
        },
        "method_source": "https://arxiv.org/abs/1304.3595",
        "guidance_pdf_quote": {
            "page": 11,
            "section": "6.5",
            "text": (
                "One must then verify the existence of limits of appropriate expectations "
                "of gauge-invariant observables as the lattice spacing tends to zero "
                "and as the volume tends to infinity."
            ),
        },
    }
    output = ROOT / "docs/validation/wilson-weighted-2026-09-08.json"
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(
        f"{len(checks)} exact checks and {len(diagnostics)} spectral diagnostics passed; {output}"
    )


if __name__ == "__main__":
    main()
