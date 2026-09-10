"""Replay scoped Wilson controls and verify the unchanged analytic-input bytes.

Run from the repository with PYTHONPATH=src. This does not certify the full
analytic theorem or replace pytest and the recorded Lean build.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import xml.etree.ElementTree as ET
from datetime import UTC, datetime
from pathlib import Path

from workhouse.invariants.wilson_marked import marked
from workhouse.invariants.wilson_shell import shell

ROOT = Path(__file__).resolve().parents[1]
INPUTS = ROOT / "docs/derivations/wilson-shell-inputs"
OUTPUT = ROOT / "docs/validation/wilson-shell-2026-09-08.json"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    manifest = json.loads((INPUTS / "manifest.json").read_text(encoding="utf-8-sig"))
    pins = []
    for entry in manifest["files"]:
        payload = (INPUTS / entry["name"]).read_bytes()
        assert sha(payload) == entry["sha256"], entry["name"]
        committed = subprocess.run(
            [
                "git",
                "-c",
                f"safe.directory={Path(manifest['source_checkout']).as_posix()}",
                "-C",
                manifest["source_checkout"],
                "show",
                f"{entry['source_commit']}:paper/research_notes/{entry['name']}",
            ],
            check=True,
            capture_output=True,
        ).stdout
        # Git and the Windows checkout can differ only in text line endings.
        assert payload.replace(b"\r\n", b"\n") == committed.replace(b"\r\n", b"\n"), entry["name"]
        pins.append(
            {
                "file": entry["name"],
                "sha256": sha(payload),
                "git_blob_content_sha256": sha(committed),
                "matches_recorded_commit_after_lf_normalization": True,
            }
        )
    results = [vars(result) for suite in (marked, shell) for result in suite.run()]
    assert all(result["passed"] for result in results), results
    artifacts = [
        "docs/derivations/wilson-marked-shell-transport.md",
        "src/workhouse/invariants/wilson_shell.py",
        "src/workhouse/ledger.py",
        "tests/test_ledger.py",
        "lean/Workhouse/Basic.lean",
        "ledger/theorems.yaml",
        "ledger/documents.yaml",
        "ledger/gaps.yaml",
        "literature/wilson-marked/theory_graph.yaml",
        "paper/research_notes/G19_UNIFORM_WILSON_WINDOW_20260904.md",
        "paper/research_notes/G18_RELATIVE_GAP_BRIDGE_20260904.tex",
        "paper/research_notes/G18_FIXED_SPACING_CARRIER_BRIDGE_INSERT.tex",
        "paper/research_notes/G18_INTERNAL_BBDAGGER_SHEET_CLOSURE_20260830.tex",
    ]
    junit = ROOT / "docs/validation/wilson-shell-tests-2026-09-08.xml"
    pytest_summary = None
    if junit.exists():
        tree = ET.parse(junit)
        pytest_summary = {
            key: sum(int(suite.get(key, "0")) for suite in tree.findall(".//testsuite"))
            for key in ("tests", "failures", "errors", "skipped")
        }
        pytest_summary["sha256"] = sha(junit.read_bytes())
        failed = {
            (case.get("classname"), case.get("name"))
            for case in tree.findall(".//testcase")
            if case.find("failure") is not None or case.find("error") is not None
        }
        observed = {
            (case.get("classname"), case.get("name")) for case in tree.findall(".//testcase")
        }
        retried_passes = set()
        retries = []
        retry_specs = (
            (
                "wilson-shell-hook-retry-2026-09-08.xml",
                "Git Bash before the WindowsApps WSL bash launcher on PATH",
                False,
            ),
            (
                "wilson-shell-ledger-retry-2026-09-08.xml",
                "Accept registered CITE/LEAN closers; reject missing or unresolved references",
                True,
            ),
        )
        for filename, reason, code_changed in retry_specs:
            retry_junit = junit.parent / filename
            if not retry_junit.exists():
                continue
            retry_tree = ET.parse(retry_junit)
            passed = {
                (case.get("classname"), case.get("name"))
                for case in retry_tree.findall(".//testcase")
                if all(case.find(tag) is None for tag in ("failure", "error", "skipped"))
            }
            retried_passes.update(passed)
            observed.update(passed)
            retries.append(
                {
                    "file": retry_junit.name,
                    "sha256": sha(retry_junit.read_bytes()),
                    "passed_testcases": sorted(passed),
                    "reason": reason,
                    "repository_code_changed_for_retry": code_changed,
                }
            )
        pytest_summary["retries"] = retries
        pytest_summary["effective_unique_testcases"] = len(observed)
        pytest_summary["unresolved_failed_testcases"] = sorted(failed - retried_passes)
        assert not pytest_summary["unresolved_failed_testcases"], pytest_summary
    axiom_file = ROOT / "docs/validation/wilson-shell-axioms-2026-09-08.txt"
    axioms = axiom_file.read_text(encoding="utf-8-sig") if axiom_file.exists() else None
    report = {
        "schema": "wilson-shell-validation/v1",
        "validated_at": datetime.now(UTC).isoformat(),
        "scope": {
            "mathematical_status": "proven under the explicit calibrated-window and G18 inputs",
            "evidence": "analytic",
            "full_theorem_machine_tier": (
                "T3; only the separately named finite/scalar controls are T1/T0"
            ),
            "step_1": "The normalized marked expansion cancels disconnected vacuum components.",
            "step_2": (
                "Actual complete Wilson shell and onto source frame; "
                "common complex weighted Taylor majorant."
            ),
            "step_3": "Summed temporal matching, relative carrier gap and positive source overlap.",
            "specific_WT6_rooted_operator_norm_proved": False,
            "sufficient_alternative": (
                "Full Hilbert-space complex anchored estimate plus finite-order kernel locality."
            ),
            "spatial_continuum_proved": False,
            "summed_epsilon_squared_rate_proved": False,
        },
        "unchanged_analytic_inputs": pins,
        "direct_checks_passed": sum(result["passed"] for result in results),
        "direct_checks_total": len(results),
        "direct_checks": results,
        "artifact_sha256": {path: sha((ROOT / path).read_bytes()) for path in artifacts},
        "other_validation": {
            "lean": "lake build --wfail; new axioms: wilson-shell-axioms-2026-09-08.txt",
            "new_lemma_axioms": axioms,
            "pytest": pytest_summary,
        },
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"Verified {len(pins)} input pins and {len(results)}/{len(results)} exact controls.")
    print(OUTPUT)


if __name__ == "__main__":
    main()
