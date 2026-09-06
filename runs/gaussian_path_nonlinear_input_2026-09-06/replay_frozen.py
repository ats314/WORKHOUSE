"""Read-only replay of three original Gaussian/nonlinear-input control families."""

import argparse
import copy
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
if sys.flags.optimize:
    raise RuntimeError("Frozen acceptance requires assertions enabled")
ROOT = Path(__file__).resolve().parent


class BlockNumerics:
    def find_spec(self, fullname, path=None, target=None):
        if fullname.split(".")[0] in {"numpy", "scipy"}:
            raise ImportError("Numerical proposal imports are forbidden")
        return None


sys.meta_path.insert(0, BlockNumerics())


def path(relative):
    result = (ROOT / relative).resolve()
    if result == ROOT or not result.is_relative_to(ROOT):
        raise ValueError("Run-relative path escapes the frozen run")
    return result


def sha(file):
    return hashlib.sha256(file.read_bytes()).hexdigest()


def manifest():
    hashes = {}
    for line in path("SHA256SUMS").read_text(encoding="utf-8").splitlines():
        digest, relative = line.split("  ", 1)
        if relative in hashes or sha(path(relative)) != digest:
            raise ValueError("Invalid manifest pin: " + relative)
        hashes[relative] = digest
    actual = {
        file.relative_to(ROOT).as_posix()
        for file in ROOT.rglob("*")
        if file.is_file() and file.name != "SHA256SUMS"
    }
    if actual != set(hashes):
        raise ValueError("Incomplete manifest file set")
    if any("__pycache__" in name or name.endswith((".pyc", ".pyo")) for name in actual):
        raise ValueError("Bytecode is forbidden in sealed evidence")
    return hashes


def check_report(saved, case, expected):
    if saved.get(case["payload_key"]) != expected:
        raise ValueError("Complete mathematical payload differs")
    pins = saved.get(case["pin_key"])
    if not isinstance(pins, dict) or pins != {
        name: sha(path(name)) for name in case["original_pins"]
    }:
        raise ValueError("Original source pins differ")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--negative-controls", action="store_true")
    args = parser.parse_args()
    before = manifest()
    inputs = json.loads(path("INPUTS.json").read_text(encoding="utf-8"))
    for relative, digest in inputs["canonical_pins"].items():
        if sha(path(relative)) != digest:
            raise ValueError("Canonical source mirror differs")
    negatives = 0
    for index, case in enumerate(inputs["cases"]):
        spec = importlib.util.spec_from_file_location(
            "frozen_original_" + str(index), path(case["checker"])
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        expected = json.loads(json.dumps(module.controls()))
        saved = json.loads(path(case["report"]).read_text(encoding="utf-8"))
        check_report(saved, case, expected)
        if args.negative_controls:
            for field in [case["payload_key"], case["pin_key"]]:
                corrupt = copy.deepcopy(saved)
                corrupt[field] = {}
                try:
                    check_report(corrupt, case, expected)
                except ValueError:
                    negatives += 1
                else:
                    raise ValueError("Corrupted family accepted")
    if manifest() != before:
        raise ValueError("Frozen bytes changed during replay")
    print(
        json.dumps(
            {
                "passed": True,
                "original_families": len(inputs["cases"]),
                "canonical_proofs": len(inputs["canonical_pins"]),
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
