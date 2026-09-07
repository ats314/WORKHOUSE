"""Read-only replay, cold relocation and mathematical corruption controls."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import runpy
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    if sys.flags.optimize:
        raise RuntimeError("Validation rejects optimized execution")
    sys.dont_write_bytecode = True
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    require(not args.output.exists(), "validation output must be fresh")
    base = Path(__file__).resolve().parent
    checker = base / "check_local_plaquette_fast_obstruction.py"
    proof = base / "LOCAL_PLAQUETTE_HARMONIC_FAST_OBSTRUCTION.md"
    report = base / "local_plaquette_fast_obstruction_controls_final.json"
    sources = (checker, proof, report)
    hashes = {path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in sources}
    module = runpy.run_path(str(checker))
    expected = json.loads(report.read_text(encoding="utf-8"))
    require(module["controls"]() == expected["controls"], "whole original payload replay")
    events = ["whole original payload replay"]
    for period in (2, 3, 5):
        try:
            module["geometry"](period)
        except ValueError:
            events.append(f"unsupported period {period} rejected")
        else:
            raise ValueError("invalid geometry accepted")
    with tempfile.TemporaryDirectory(prefix="workhouse-plaquette-fast-") as temporary:
        directory = Path(temporary)
        for path in sources:
            shutil.copyfile(path, directory / path.name)
        cold_checker = directory / checker.name
        cold_report = directory / report.name
        bootstrap = (
            "import sys,runpy;sys.dont_write_bytecode=True;"
            "sys.meta_path.insert(0,type('Block',(),{'find_spec':lambda self,name,*args: "
            "(_ for _ in ()).throw(ImportError('blocked numerical dependency')) "
            "if name.split('.')[0] in ('numpy','scipy') else None})());"
            "script=sys.argv.pop(1);sys.argv[0]=script;runpy.run_path(script,run_name='__main__')"
        )

        def invoke(arguments, success, label, optimized=False):
            command = [sys.executable]
            if optimized:
                command.append("-O")
            command += ["-c", bootstrap, str(cold_checker), *map(str, arguments)]
            result = subprocess.run(
                command, cwd=directory, capture_output=True, text=True, check=False
            )
            require(
                (result.returncode == 0) == success,
                f"{label}: unexpected exit {result.returncode}: {result.stderr}",
            )
            events.append(label)

        invoke(["--replay", cold_report], True, "cold full replay with NumPy/SciPy blocked")
        fresh = directory / "fresh.json"
        invoke(["--output", fresh], True, "fresh cold output")
        require(
            json.loads(fresh.read_text(encoding="utf-8")) == expected, "cold certificate equality"
        )
        invoke(["--output", fresh], False, "overwrite rejected")
        invoke(["--replay", cold_report], False, "optimized replay rejected", optimized=True)
        invoke(
            ["--output", directory / "optimized.json"],
            False,
            "optimized output rejected",
            optimized=True,
        )
        corrupted = copy.deepcopy(expected)
        corrupted["controls"]["physical_harmonic_fast_energy"]["SU2_color_tensor_norm_squared"] = 3
        altered = directory / "wrong_norm.json"
        altered.write_text(json.dumps(corrupted), encoding="utf-8")
        invoke(["--replay", altered], False, "wrong color normalization rejected")
        corrupted = copy.deepcopy(expected)
        corrupted["controls"]["actual_path_geometry"][0]["plaquette_sign_sum"] = 64
        altered = directory / "wrong_sum.json"
        altered.write_text(json.dumps(corrupted), encoding="utf-8")
        invoke(["--replay", altered], False, "omitted spatial cancellation rejected")
        corrupted = copy.deepcopy(expected)
        corrupted["source_sha256"][proof.name] = "0" * 64
        altered = directory / "wrong_pin.json"
        altered.write_text(json.dumps(corrupted), encoding="utf-8")
        invoke(["--replay", altered], False, "wrong proof pin rejected")
    require(
        hashes == {path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in sources},
        "original evidence bytes unchanged",
    )
    with args.output.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(
            {"passed": True, "checks": events, "source_sha256": hashes},
            stream,
            indent=2,
            sort_keys=True,
        )
        stream.write("\n")
    print(f"PASS: {len(events)} exact replay, domain, cold and rejection checks")


if __name__ == "__main__":
    main()
