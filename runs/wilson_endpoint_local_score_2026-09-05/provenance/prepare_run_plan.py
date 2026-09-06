"""Inventory immutable originals and proposed narrow evidence supports."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
PUB = HERE.parent
BASE = PUB.parent
ROOT = next(p for p in HERE.parents if (p / "pyproject.toml").is_file())


def hashed(path: Path) -> dict:
    return {"source": path.relative_to(ROOT).as_posix(),
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}


def main() -> None:
    families = [
        ("endpoint", "next_full_window_comparison", "check_literal_endpoint_window.py",
         "literal_endpoint_window_controls_frozen.json", "controls"),
        ("localized_score", "next_energy_local_score", "check_localized_true_ground_score.py",
         "localized_true_ground_score_controls.json", "controls"),
        ("local_gradient", "next_local_gradient_tensorization", "check_local_gradient_tensorization.py",
         "local_gradient_tensorization_controls_final.json", "top-level-without-source_sha256"),
        ("covariant_path", "next_covariant_block_sources", "check_covariant_path_sources.py",
         "covariant_path_source_controls.json", "controls"),
        ("fourier_alias", "next_covariant_block_sources", "check_fourier_alias_independent.py",
         "fourier_alias_independent_controls_frozen.json", "controls"),
    ]
    entries = []
    for key, directory, script, report, payload in families:
        folder = BASE / directory
        document = json.loads((folder / report).read_text(encoding="utf-8"))
        pins = document.get("source_sha256", {})
        if "script_sha256" in document:
            pins = {script: document["script_sha256"]}
        observed = []
        for relative, expected in pins.items():
            source = ROOT / relative if "/" in relative else folder / relative
            record = hashed(source)
            if record["sha256"] != expected:
                raise ValueError(f"An original report pin changed: {source}")
            observed.append(record)
        entries.append({"family": key, "script": hashed(folder / script),
                        "report": hashed(folder / report), "payload": payload,
                        "verified_declared_pins": observed})
    extras = [
        "next_full_window_comparison/LITERAL_ENDPOINT_COMPLETE_WINDOW.md",
        "next_full_window_comparison/replay_literal_endpoint_window.py",
        "next_full_window_comparison/INDEPENDENT_ENDPOINT_WINDOW_AUDIT.md",
        "next_energy_local_score/TRUE_GROUND_LOCALIZED_WILSON_SCORE.md",
        "next_energy_local_score/INDEPENDENT_LOCAL_SCORE_AUDIT.md",
        "next_energy_local_score/LOCALIZED_SCORE_REVIEW.md",
        "next_energy_local_score/LOCALIZED_SCORE_VALIDATION.json",
        "next_local_gradient_tensorization/LOCAL_GRADIENT_EXCITATION_SUPPORT.md",
        "next_covariant_block_sources/LOCAL_COVARIANT_AVERAGED_PATH_SOURCES.md",
        "next_covariant_block_sources/INDEPENDENT_FOURIER_ALIAS_AUDIT.md",
        "next_covariant_block_sources/COMPACT_MATRIX_GROUP_CHART_AUDIT.md",
        "next_covariant_block_sources/COVARIANT_PATH_VALIDATION.json",
        "next_endpoint_publication/INDEPENDENT_NATIVE_API_REVIEW.md",
        "next_endpoint_publication/staged_docs/CANDIDATE_COPY_AUDIT.json",
        "next_endpoint_publication/CANONICAL_DOCS_APPLIED.json",
    ]
    report = {"run": "wilson_endpoint_local_score_2026-09-05", "families": entries,
              "extra_evidence": [hashed(BASE / relative) for relative in extras],
              "declared_original_pin_count": sum(len(row["verified_declared_pins"]) for row in entries),
              "native_handoff": "await final NATIVE_CANDIDATE_HANDOFF.json; expected 15 sources/8 modules/10 checks"}
    (HERE / "ORIGINAL_INPUT_INVENTORY.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8", newline="\n")
    validation = json.loads((PUB / "STAGED_NATIVE_VALIDATION_V2.json").read_text(encoding="utf-8"))
    checks = validation["checks"]
    if len(checks) != 10:
        raise ValueError("Expected the final ten scoped finite checks")
    indices = {"LITERAL_ENDPOINT_SPECTRAL_COMPARISON": [0, 1, 2, 3],
               "WILSON_ENDPOINT_COMPLETE_CLUSTER": [0],
               "LOCAL_GRADIENT_EXCITATION_SUPPORT": [6, 7],
               "WILSON_LOCALIZED_TRUE_GROUND_SCORE": [4, 5],
               "WILSON_COVARIANT_BLOCK_SOURCES": [8, 9]}
    mapping = {}
    for suffix, selected in indices.items():
        supports = [{"target": checks[index]["id"], "scope": checks[index]["scope"]} for index in selected]
        if suffix == "WILSON_ENDPOINT_COMPLETE_CLUSTER":
            supports[0]["scope"] += (
                " This is only the finite complete-cluster mechanism; actual Wilson localization, "
                "its fixed-SU(N) thresholds and finite/countable-copy uniformity are analytic."
            )
        supports.append({"target": "RUN:wilson_endpoint_local_score_2026-09-05",
                         "scope": "Four pinned analytic proofs and five original finite control families with ten native exact checks, source-preserving cold replay and negative controls. Closed spectral domains, actual Wilson limiting/derivative estimates, all-size geometry and full Fock consequences remain analytic; no new Lean theorem certifies those full results."})
        mapping["RESULT:" + suffix] = supports
    (HERE / "RESULT_SUPPORT_MAPPING.json").write_text(json.dumps(mapping, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"original_families": len(entries), "original_declared_pins": report["declared_original_pin_count"],
                      "results": len(mapping), "check_edges": sum(len(x) - 1 for x in mapping.values()),
                      "unique_checks": len(checks)}))


if __name__ == "__main__":
    main()
