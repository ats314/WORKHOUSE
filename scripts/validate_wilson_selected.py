"""Replay the selected-inverse controls and verify exact input provenance."""

from __future__ import annotations

import json
import xml.etree.ElementTree as ET
from datetime import UTC, datetime
from pathlib import Path

from validate_wilson_spatial import committed, sha

ROOT = Path(__file__).resolve().parents[1]
CHECKOUT = Path("C:/WORKHOUSE/WORKHOUSE-autonomous-20260905")
COMMIT = "4bf812428e0af51d1ffcda299b0d97b38b644926"
PDF = Path(
    "C:/Users/Alex/.codex/codex-remote-attachments/"
    "01a082e4-6acd-7fb3-9b51-19444da9ee6b/"
    "7CB6AE9F-52F3-4247-B1C0-B94760FF97DD/1-yangmills.pdf"
)
PDF_SHA = "3558403ca14c11e382f73a09e548222708540bfdf478cf96aa11c52d43e23e09"
INPUT_NAMES = (
    "G19_TRUE_GROUND_LOCALIZED_WILSON_SCORE_20260905.md",
    "G19_LOCAL_GRADIENT_EXCITATION_SUPPORT_20260905.md",
    "G19_GROUND_MARGINAL_SCHUR_SCORE_20260905.md",
)


def main() -> None:
    if sha(PDF.read_bytes()) != PDF_SHA:
        raise ValueError("The supplied Yang-Mills guidance PDF has changed")
    inputs = []
    for name in INPUT_NAMES:
        path = CHECKOUT / "paper/research_notes" / name
        payload = path.read_bytes()
        blob = committed(CHECKOUT, COMMIT, name)
        if payload.replace(b"\r\n", b"\n") != blob.replace(b"\r\n", b"\n"):
            raise ValueError(f"Input differs from its recorded commit: {path}")
        inputs.append(
            {
                "source": str(path),
                "commit": COMMIT,
                "sha256": sha(payload),
                "git_blob_sha256": sha(blob),
                "matches_commit_after_lf_normalization": True,
            }
        )

    from workhouse.invariants.wilson_selected import selected

    results = [vars(result) for result in selected.run()]
    if not all(result["passed"] for result in results):
        raise ValueError(results)
    artifacts = (
        "docs/derivations/wilson-selected-inverse-wall.md",
        "src/workhouse/invariants/wilson_selected.py",
        "src/workhouse/invariants/__init__.py",
        "scripts/validate_wilson_selected.py",
        "scripts/validate_wilson_spatial.py",
        "docs/research/spatial-continuum-passage-2026-09-08.md",
        "ledger/documents.yaml",
        "ledger/gaps.yaml",
        "index/claims.jsonl",
        "index/symbols.jsonl",
        "index/graph.jsonl",
        "FRONTIER.md",
        "CERTIFIED.md",
    )
    catalogue = [
        json.loads(line)
        for line in (ROOT / "index/claims.jsonl").read_text(encoding="utf-8").splitlines()
    ]
    native = [claim for claim in catalogue if claim["kind"] == "check"]
    graph_record = {
        "claim_records": len(catalogue),
        "edge_records": len((ROOT / "index/graph.jsonl").read_text(encoding="utf-8").splitlines()),
        "native_checks": len(native),
        "native_checks_passing": sum(claim["status"] == "passing" for claim in native),
        "lean_records": sum(claim["id"].startswith("LEAN:") for claim in catalogue),
        "g19_routes": [
            {key: claim[key] for key in ("id", "statement", "status", "related")}
            for claim in catalogue
            if claim["id"].startswith("ROUTE:G19:")
        ],
    }
    reports = []
    for path in sorted((ROOT / "docs/validation").glob("wilson-selected-*.xml")):
        suites = ET.parse(path).findall(".//testsuite")
        reports.append(
            {
                "file": path.name,
                "sha256": sha(path.read_bytes()),
                **{
                    key: sum(int(suite.get(key, "0")) for suite in suites)
                    for key in ("tests", "failures", "errors", "skipped")
                },
            }
        )
    report = {
        "recorded_at": datetime.now(UTC).isoformat(),
        "analytic_scope": (
            "Compact SU2 min-max obstruction after finite-rank Gaussian retention; "
            "conditional selected-resolvent Schur remainder; exact method counterexamples"
        ),
        "open_estimate": (
            "W6: uniform interacting signed fast-form pairing on both inverse images "
            "of the complete graph force; actual fast floor and direct/source remainders "
            "are also unproved. No continuum construction is claimed."
        ),
        "guidance_pdf": {"path": str(PDF), "sha256": PDF_SHA, "quoted_pages": [11, 12]},
        "input_pins": inputs,
        "checks": results,
        "artifacts": {name: sha((ROOT / name).read_bytes()) for name in artifacts},
        "test_runs": reports,
        "generated_graph": graph_record,
        "execution_note": (
            "Initial sandbox execution could not load pyflint or run ruff (access denied); "
            "normal host execution is used for validation. No full pytest pass is claimed."
        ),
    }
    output = ROOT / "docs/validation/wilson-selected-2026-09-08.json"
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"{len(results)}/{len(results)} exact controls; {len(inputs)} commit pins; {output}")


if __name__ == "__main__":
    main()
