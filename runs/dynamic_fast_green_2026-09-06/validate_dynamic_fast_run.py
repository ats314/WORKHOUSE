"""Validate a fresh run by cold replay, corruption and source-read guards."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def snapshot(root):
    return {
        path.relative_to(root).as_posix(): sha(path) for path in root.rglob("*") if path.is_file()
    }


def main():
    if sys.flags.optimize:
        raise RuntimeError("Run validation rejects optimized execution")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", type=Path, required=True)
    parser.add_argument("--checkout", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    require(not args.output.exists(), "validation output must be fresh")
    run, checkout = args.run.resolve(), args.checkout.resolve()
    original = snapshot(run)
    events = []
    results = []
    with tempfile.TemporaryDirectory(prefix="workhouse-dynamic-fast-cold-") as temporary:
        cold = Path(temporary) / "evidence"
        shutil.copytree(run, cold)
        # Importing SymPy from the installed .venv is permitted. Every other
        # checkout read is forbidden, including an editable source package.
        bootstrap = r"""
import os,runpy,sys
sys.dont_write_bytecode=True
cold=os.path.realpath(sys.argv.pop(1))
checkout=os.path.realpath(sys.argv.pop(1))
runtime=os.path.join(checkout,'.venv')
def within(value,root):
    try:return os.path.commonpath([value,root])==root
    except ValueError:return False
def audit(event,args):
    if event=='open' and isinstance(args[0],(str,bytes,os.PathLike)):
        value=os.path.realpath(os.fsdecode(args[0]))
        if within(value,checkout) and not within(value,runtime) and not within(value,cold):
            raise PermissionError('source checkout reads forbidden')
sys.addaudithook(audit)
try:
    open(os.path.join(checkout,'README.md'),'rb')
except PermissionError:pass
else:raise RuntimeError('checkout-read guard not active')
script=sys.argv.pop(1)
sys.argv[0]=script
runpy.run_path(script,run_name='__main__')
"""

        def call(script, arguments, success, label, optimized=False):
            command = [sys.executable]
            if optimized:
                command.append("-O")
            command += [
                "-B",
                "-c",
                bootstrap,
                str(cold),
                str(checkout),
                str(script),
                *map(str, arguments),
            ]
            environment = os.environ.copy()
            environment["PYTHONDONTWRITEBYTECODE"] = "1"
            result = subprocess.run(
                command, cwd=cold, env=environment, capture_output=True, text=True, check=False
            )
            require(
                (result.returncode == 0) == success,
                f"{label}: unexpected exit {result.returncode}: {result.stdout}\n{result.stderr}",
            )
            events.append(label)
            return result

        replay = cold / "replay_frozen.py"
        full = call(
            replay,
            ["--negative-controls"],
            True,
            "cold four-family replay with checkout reads and numerical imports blocked",
        )
        results.append(json.loads(full.stdout.strip().splitlines()[-1]))
        require(results[-1]["corruption_rejections"] == 8, "eight complete report/source negatives")
        call(replay, [], False, "optimized frozen acceptance rejected", optimized=True)
        cases = json.loads((cold / "INPUTS.json").read_text(encoding="utf-8"))["cases"]
        for case in cases:
            call(
                cold / case["checker"],
                ["--output", cold / case["report"]],
                False,
                "overwrite rejected: " + case["checker"],
            )
        # A new file is rejected before loading any model. No scientific input
        # is mutated, and cleanup occurs only in the resolved temporary tree.
        unexpected = cold / "UNPINNED.txt"
        unexpected.write_text("deliberate manifest negative\n", encoding="utf-8")
        call(replay, [], False, "unmanifested file rejected")
        unexpected.unlink()
        victim = cold / cases[0]["checker"]
        saved = victim.read_bytes()
        victim.write_bytes(saved + b"\n# deliberate pin corruption\n")
        call(replay, [], False, "mutated frozen checker rejected")
        victim.write_bytes(saved)
        require(
            snapshot(cold) == original, "cold replay and corruption cleanup preserve exact bytes"
        )
    require(snapshot(run) == original, "original run bytes unchanged by validation")
    payload = {
        "passed": True,
        "checks": events,
        "cold_replay": results,
        "original_file_count": len(original),
        "read_boundaries": (
            "All checkout reads blocked except installed .venv; "
            "all originals replay from relocated run."
        ),
        "scope": "Finite exact replay and sealing guards; no full analytic theorem certification.",
    }
    with args.output.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(payload, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(
        json.dumps(
            {
                "passed": True,
                "checks": len(events),
                "families": 4,
                "mathematical_and_source_corruption_rejections": 8,
            }
        )
    )


if __name__ == "__main__":
    main()
