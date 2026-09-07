"""Read-only acceptance of four original dynamic/full-fast control families."""

from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
if sys.flags.optimize:
    raise RuntimeError("Frozen acceptance rejects optimized Python execution")
ROOT = Path(__file__).resolve().parent


class BlockNumerics:
    def find_spec(self, fullname, path=None, target=None):
        if fullname.split(".")[0] in {"numpy", "scipy"}:
            raise ImportError("Numerical proposal imports are forbidden in acceptance")
        return None


sys.meta_path.insert(0, BlockNumerics())


def require(condition, message):
    if not condition:
        raise ValueError(message)


def path(relative):
    result = (ROOT / relative).resolve()
    require(result != ROOT and result.is_relative_to(ROOT), "run path escapes its root")
    return result


def sha(file):
    return hashlib.sha256(file.read_bytes()).hexdigest()


def manifest():
    hashes = {}
    for line in path("SHA256SUMS").read_text(encoding="utf-8").splitlines():
        digest, relative = line.split("  ", 1)
        require(relative not in hashes, "duplicate manifest path")
        require(len(digest) == 64 and sha(path(relative)) == digest, "manifest pin: " + relative)
        hashes[relative] = digest
    actual = {
        file.relative_to(ROOT).as_posix()
        for file in ROOT.rglob("*")
        if file.is_file() and file != ROOT / "SHA256SUMS"
    }
    require(actual == set(hashes), "manifest file set is incomplete")
    require(
        not any("__pycache__" in name or name.endswith((".pyc", ".pyo")) for name in actual),
        "bytecode is forbidden in sealed evidence",
    )
    return hashes


def compute(case, module):
    mode = case["api"]
    if mode == "dynamic_named_functions":
        payload = {
            "dynamic_spectral_island": module.dynamic_functional_calculus_control(),
            "full_complement_not_fiber_inverse": module.compressed_full_inverse_control(),
            "two_time_connected_Lie_cubic": module.lie_cubic_two_time_control(),
        }
        result = {
            "passed": True,
            "controls": payload,
            "source_sha256": {name: sha(path(name)) for name in case["embedded_pins"]},
        }
    elif mode == "witness_controls":
        result = {
            "passed": True,
            "controls": module.controls(),
            "source_sha256": {name: sha(path(name)) for name in case["embedded_pins"]},
        }
    elif mode == "derive":
        result = module.derive()
    elif mode == "independent_polynomial_derive":
        result = module.derive()
        result["review_script_sha256"] = sha(path(case["checker"]))
    else:
        raise ValueError("unknown frozen family API")
    return json.loads(json.dumps(result))


def check_case(saved, case, expected):
    require(saved == expected, "complete mathematical report differs")
    require(
        all(sha(path(name)) == digest for name, digest in case["original_pins"].items()),
        "original external source pin differs",
    )


def validate_copies(inputs):
    records = json.loads(path("provenance/CANONICAL_COPY_AUDIT.json").read_text(encoding="utf-8"))
    reconstructed = []
    for record in records:
        source = path(Path(record["source"]).name)
        target = path("source/" + record["target"])
        require(sha(source) == record["source_sha256"], "original copy source pin")
        require(sha(target) == record["canonical_sha256"], "canonical copy pin")
        body = source.read_text(encoding="utf-8")
        for old, new in record["replacements"]:
            require(body.count(old) == 1, "canonical replacement count")
            body = body.replace(old, new)
        canonical = target.read_text(encoding="utf-8")
        prefix, separator, appendix = canonical.partition("\n## Repository provenance\n")
        require(
            separator != "" and prefix.rstrip() == body.rstrip(), "canonical body reconstruction"
        )
        require("sealed reproduction run" in appendix, "canonical provenance appendix")
        reconstructed.append(record["target"])
    require(
        set(inputs["canonical_pins"]) == {"source/" + name for name in reconstructed},
        "canonical inventory matches copy audit",
    )
    return reconstructed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--negative-controls", action="store_true")
    args = parser.parse_args()
    before = manifest()
    inputs = json.loads(path("INPUTS.json").read_text(encoding="utf-8"))
    require(
        all(sha(path(name)) == digest for name, digest in inputs["canonical_pins"].items()),
        "canonical source mirrors changed",
    )
    copies = validate_copies(inputs)
    negatives = 0
    for index, case in enumerate(inputs["cases"]):
        spec = importlib.util.spec_from_file_location(
            "frozen_original_" + str(index), path(case["checker"])
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        expected = compute(case, module)
        saved = json.loads(path(case["report"]).read_text(encoding="utf-8"))
        check_case(saved, case, expected)
        if args.negative_controls:
            corrupt = copy.deepcopy(saved)
            owner = corrupt
            for key in case["corrupt_path"][:-1]:
                owner = owner[key]
            owner[case["corrupt_path"][-1]] = "CORRUPTED_EXACT_VALUE"
            try:
                check_case(corrupt, case, expected)
            except ValueError:
                negatives += 1
            else:
                raise ValueError("mathematical corruption accepted")
            wrong_pins = copy.deepcopy(case)
            wrong_pins["original_pins"][case["checker"]] = "0" * 64
            try:
                check_case(saved, wrong_pins, expected)
            except ValueError:
                negatives += 1
            else:
                raise ValueError("original source corruption accepted")
    require(manifest() == before, "frozen bytes changed during replay")
    print(
        json.dumps(
            {
                "passed": True,
                "original_families": len(inputs["cases"]),
                "canonical_proofs": len(copies),
                "manifest_files": len(before),
                "numerical_imports_blocked": True,
                "corruption_rejections": negatives,
                "read_only": True,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
