"""Replay the exact PBH proposal tests and record the final graph evidence."""

from __future__ import annotations

import hashlib
import json
import xml.etree.ElementTree as ET
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    from workhouse.invariants.ym_pbh import pbh

    checks = [vars(result) for result in pbh.run()]
    if not all(check["passed"] for check in checks):
        raise ValueError(checks)
    artifacts = (
        "docs/derivations/yangmills-pbh-wilson-test.md",
        "docs/derivations/yangmills-weighted-curvature.md",
        "src/workhouse/invariants/ym_pbh.py",
        "src/workhouse/invariants/__init__.py",
        "scripts/validate_pbh_wilson.py",
        "ledger/documents.yaml",
        "ledger/gaps.yaml",
        "index/claims.jsonl",
        "index/graph.jsonl",
        "FRONTIER.md",
        "CERTIFIED.md",
    )
    tests = []
    for path in sorted((ROOT / "docs/validation").glob("pbh-wilson-*.xml")):
        suites = ET.parse(path).findall(".//testsuite")
        tests.append(
            {
                "file": path.name,
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                **{
                    key: sum(int(suite.get(key, "0")) for suite in suites)
                    for key in ("tests", "failures", "errors", "skipped")
                },
            }
        )
    report = {
        "recorded_at": datetime.now(UTC).isoformat(),
        "scope": (
            "Five exact finite/differential controls. The finite SU2 lattice "
            "horizontal-geodesic argument PBH-5 is an analytic proof. No full "
            "manifold theorem is claimed machine-formalized."
        ),
        "verdict": (
            "The proposed classical Wilson weight cannot maintain globally "
            "positive pointwise orbit curvature at all large beta in the stated "
            "regularization. This does not refute other LSI or true-ground curvature "
            "methods. W6 remains open; no continuum Yang-Mills proof is claimed."
        ),
        "checks": checks,
        "test_runs": tests,
        "artifacts": {
            name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in artifacts
        },
        "primary_sources": [
            {
                "url": "https://www.sfb1283.uni-bielefeld.de/preprints/sfb22100.pdf",
                "locator": "Assumption 1.1, Theorems 1.2 and 1.4; Section 4.3",
                "scope": "Strong-coupling infinite-volume uniqueness, LSI and clustering",
            },
            {
                "url": "https://arxiv.org/abs/1101.0963",
                "scope": "Perturbative gradient-flow finiteness after underlying renormalization",
            },
            {
                "url": "https://arxiv.org/abs/1809.06318",
                "scope": "Ground-state weighted curvature; conventions pinned in GST derivation",
            },
        ],
    }
    output = ROOT / "docs/validation/pbh-wilson-2026-09-08.json"
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"{len(checks)}/{len(checks)} exact controls passed; {output}")


if __name__ == "__main__":
    main()
