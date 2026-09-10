"""Replay the background exact controls and record their limited proof scope."""

from __future__ import annotations

import hashlib
import json
import xml.etree.ElementTree as ET
from datetime import UTC, datetime
from pathlib import Path

from workhouse.invariants.wilson_background import background

ROOT = Path(__file__).resolve().parents[1]


def main():
    controls = [vars(result) for result in background.run()]
    assert len(controls) == 7 and all(result["passed"] for result in controls)
    names = [
        "docs/derivations/wilson-background-covariance-continuation.md",
        "docs/validation/wilson-background-independent-review.md",
        "src/workhouse/invariants/wilson_background.py",
        "src/workhouse/invariants/__init__.py",
        "scripts/validate_wilson_background.py",
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
            "Seven exact finite controls. The all-coupling magnetic comparison and charged "
            "parabolic bounds have analytic proofs; the controls do not formalize their "
            "operator domains, gauge disintegration, or Markov evolution in Lean. "
            "No spatial decay, full quantum fast comparison, or continuum mass gap is certified."
        ),
        "controls": controls,
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
            for path in sorted((ROOT / "docs/validation").glob("wilson-background-*.xml"))
        ],
        "remaining_derivation": (
            "SC17: spatial decay of R_xy(F_e tensor V_f+V_e tensor F_f)+F_e tensor F_f. "
            "The actual uniform time/volume bound 18lambda^2 has no distance factor. "
            "BF6 is a small-field affine-slice comparison; its extension to the actual "
            "quantum fast restriction still needs excluded-field coupling, vacuum subtraction, "
            "literal source fibers and retained Schur control."
        ),
        "artifacts_sha256": {
            name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in names
        },
    }
    target = ROOT / "docs/validation/wilson-background-2026-09-09.json"
    target.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"{len(controls)} exact controls passed; {target}")


if __name__ == "__main__":
    main()
