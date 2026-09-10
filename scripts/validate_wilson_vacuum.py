"""Provenance and scoped exact controls for the actual vacuum assembly continuation."""

from __future__ import annotations

import hashlib
import json
import math
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    from workhouse.invariants.wilson_vacuum import vacuum
    from workhouse.invariants.yangmills_gpu_audit import audit

    checks = [vars(item) for item in vacuum.run() + audit.run()]
    assert all(item["passed"] for item in checks)
    from sympy import Rational, diff, factorial, simplify, symbols

    a, momentum = symbols("a momentum", positive=True)
    smearing_controls = {
        "inserted_mass_cancels_spacing_in_filter": simplify(
            (momentum / a) ** 2 / (2 * (Rational(6, 5) / a) ** 2)
            - momentum**2 / (2 * Rational(6, 5) ** 2)
        )
        == 0,
        "L8_uniform_85_percent_claim_fails_rational_majorant": 1 / (1 + Rational(25, 128))
        == Rational(128, 153)
        < Rational(17, 20),
    }
    smearing_controls = {name: bool(value) for name, value in smearing_controls.items()}
    assert all(smearing_controls.values())
    q = symbols("q")
    block_controls = {
        "VA18_shell_series": simplify(diff(q * diff(q / (1 - q), q), q) - (1 + q) / (1 - q) ** 3)
        == 0,
        "GA14_exponent_exceeds_five_halves": (2 * Rational(21939, 10000)) ** 2
        > 3 * Rational(5, 2) ** 2,
        "GA14_exp_five_halves_exceeds_twelve": sum(
            Rational(5, 2) ** j / factorial(j) for j in range(9)
        )
        > 12,
        "GA14_exact_infinite_scalar_budget": Rational(1, 2) * (Rational(13, 11) ** 3 - 1)
        == Rational(433, 1331)
        < 1,
    }
    block_controls = {name: bool(value) for name, value in block_controls.items()}
    assert all(block_controls.values())
    phase8_root = ROOT / "runs/gpu_yangmills_millennium_resolutions_2026-09-09"
    phase8_files = {
        name: (phase8_root / name).read_bytes()
        for name in ("phase8_approximate_tensorization_va12.py", "phase8_va12_results.json")
    }
    phase8 = json.loads(phase8_files["phase8_va12_results.json"])
    phase8_replays = []
    for half_size in (2, 4, 8, 16, 32, 50):
        counts = Counter(
            i * i + j * j + k * k
            for i in range(-half_size, half_size + 1)
            for j in range(-half_size, half_size + 1)
            for k in range(-half_size, half_size + 1)
            if i or j or k
        )
        for mass, suffix in ((2.1939, "phys"), (1.5515, "b1"), (0.8, "cons")):
            value = math.fsum(
                count * 0.5 * math.exp(-2 * mass * math.sqrt(n2)) for n2, count in counts.items()
            )
            if half_size == 50:
                expected = phase8["part3_block_tensorization"][f"kappa_block_inf_{suffix}"]
            else:
                expected = next(
                    row["kappa_block"]
                    for row in phase8["part3_block_tensorization"]["scans"]
                    if row["Nb"] == 2 * half_size and row["M"] == mass
                )
            error = abs(value - expected)
            assert error < 1e-10
            phase8_replays.append(dict(half_size=half_size, M=mass, value=value, error=error))
    source_root = Path("C:/WORKHOUSE/WORKHOUSE-autonomous-20260905/paper/research_notes")
    sources = [
        "G19_GROUND_MARGINAL_SCHUR_SCORE_20260905.md",
        "G19_TRUE_GROUND_LOCALIZED_WILSON_SCORE_20260905.md",
        "G19_TRUE_GROUND_CENTER_SCORE_OBSTRUCTION_20260905.md",
    ]
    artifacts = [
        "docs/derivations/wilson-vacuum-aligned-assembly.md",
        "docs/derivations/yangmills-gpu-resolution-audit.md",
        "docs/derivations/wilson-weighted-repair-and-rotor-gap.md",
        "docs/derivations/yangmills-resolvent-localization-and-dirichlet-gap.md",
        "src/workhouse/invariants/wilson_vacuum.py",
        "src/workhouse/invariants/yangmills_gpu_audit.py",
        "src/workhouse/invariants/__init__.py",
        "scripts/validate_wilson_vacuum.py",
        "scripts/validate_yangmills_gpu_audit.py",
        "docs/validation/yangmills-gpu-audit-2026-09-09.json",
        "lean/Workhouse/Basic.lean",
        "ledger/theorems.yaml",
        "ledger/documents.yaml",
        "ledger/gaps.yaml",
        "runs/index.yaml",
        "FRONTIER.md",
        "CERTIFIED.md",
        "index/claims.jsonl",
        "index/graph.jsonl",
    ]
    tests = []
    for path in sorted((ROOT / "docs/validation").glob("wilson-vacuum-*.xml")):
        suites = ET.parse(path).findall(".//testsuite")
        tests.append(
            dict(
                file=path.name,
                **{
                    key: sum(int(suite.get(key, "0")) for suite in suites)
                    for key in ("tests", "failures", "errors", "skipped")
                },
            )
        )
    lean_log = ROOT / "docs/validation/wilson-vacuum-lean-2026-09-09.txt"
    report = {
        "recorded_at": datetime.now(UTC).isoformat(),
        "analytic_progress": [
            "VA1-VA4: actual true-ground local density comparison independent of volume",
            "VA5-VA8: literal WR26 comparison is negative at large connected physical volume",
            "VA9-VA11: exact vacuum conditional projections with uniform local Poincare floor",
            "VA12-VA19: assembly criterion, quantitative decay budget, block repair and clock loss",
            "GA1-GA10: source-identified scalar theorems and archived operator discrepancies",
            "GA11: supplied Lean eigenvector identity does not assert F=E0-sum e_*=0",
        ],
        "proof_boundary": (
            "VA14 physical approximate tensorization for the true coupled vacuum with "
            "a volume-independent constant, plus improved local or physical-block coercivity: "
            "VA17 shows the present VA10 floor vanishes on the stated logarithmic trajectory. "
            "One sufficient assembly path is a strict summable physical "
            "projection-angle budget. Complete shell, source matching and observable "
            "transport remain conditional on their actual interacting hypotheses."
        ),
        "scope": (
            "Analytic semigroup, domain, full-volume and spectral arguments are not Lean "
            "formalizations. The exact controls below verify their stated finite identities. "
            "The GPU replay is separately labelled T2. No Yang-Mills continuum closure."
        ),
        "checks": checks,
        "supplementary_phase6_exact_controls": smearing_controls,
        "supplementary_block_exact_controls": block_controls,
        "phase8_source_and_scalar_replay": {
            "scope": (
                "Eighteen finite scalar kernel sums replayed; GA14 separately bounds the "
                "infinite sum. No physical conditional-angle or block-gap identification. "
                "Part 1 random binning was source-audited, not replayed."
            ),
            "files_sha256": {
                name: hashlib.sha256(data).hexdigest() for name, data in phase8_files.items()
            },
            "scalar_comparisons": phase8_replays,
        },
        "existing_source_provenance": {
            "checkout": str(source_root.parent.parent),
            "source_commit": "4bf812428e0af51d1ffcda299b0d97b38b644926",
            "files_sha256": {
                name: hashlib.sha256((source_root / name).read_bytes()).hexdigest()
                for name in sources
            },
            "use": "Existing exact ground-score theorem and localized score scope; not new results",
        },
        "test_runs": tests,
        "lean_diagnostic": lean_log.read_text(encoding="utf-8") if lean_log.exists() else "pending",
        "artifacts_sha256": {
            name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in artifacts
        },
        "guidance_pdf": {
            "sha256": "3558403ca14c11e382f73a09e548222708540bfdf478cf96aa11c52d43e23e09",
            "page": 11,
            "section": "6.5",
            "quote": (
                "One must then verify the existence of limits of appropriate expectations "
                "of gauge-invariant observables as the lattice spacing tends to zero "
                "and as the volume tends to infinity."
            ),
        },
    }
    target = ROOT / "docs/validation/wilson-vacuum-2026-09-09.json"
    target.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"{len(checks)} exact scoped controls passed; {target}")


if __name__ == "__main__":
    main()
