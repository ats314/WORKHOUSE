"""Read-only exact replay and negative CLI controls, without NumPy or SciPy."""

from __future__ import annotations

import hashlib
import importlib.abc
import importlib.util
import json
import subprocess
import sys
from pathlib import Path


class BlockNumericalImports(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname.split(".", 1)[0] in {"numpy", "scipy"}:
            raise ImportError(f"Numerical dependency deliberately blocked: {fullname}")
        return None


def main() -> None:
    if not __debug__:
        raise RuntimeError("Optimized Python is rejected for exact verification.")
    sys.dont_write_bytecode = True
    sys.meta_path.insert(0, BlockNumericalImports())
    here = Path(__file__).resolve().parent
    script = here / "check_global_wilson_vertical_barrier.py"
    certificate = here / "check_global_wilson_vertical_barrier.json"
    spec = importlib.util.spec_from_file_location("global_vertical_control", script)
    if spec is None or spec.loader is None:
        raise RuntimeError("Cannot load the original exact control.")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    before = certificate.read_bytes()
    report = json.loads(before)
    module.require(module.source_hashes() == report["sources"], "all current source pins")
    module.require(module.controls() == report["controls"], "exact saved payload replay")
    collision = subprocess.run(
        [sys.executable, str(script), "--output", str(certificate)],
        capture_output=True,
        text=True,
        check=False,
    )
    module.require(
        collision.returncode != 0 and "Refusing to overwrite" in collision.stderr,
        "existing output is rejected",
    )
    forbidden = here / "optimized_output_must_not_exist.json"
    module.require(not forbidden.exists(), "fresh optimized negative-control path")
    optimized = subprocess.run(
        [sys.executable, "-O", str(script), "--output", str(forbidden)],
        capture_output=True,
        text=True,
        check=False,
    )
    module.require(
        optimized.returncode != 0 and "Optimized Python is rejected" in optimized.stderr,
        "optimized verification is rejected",
    )
    module.require(not forbidden.exists(), "optimized run produced no output")
    module.require(certificate.read_bytes() == before, "read-only certificate replay")
    module.require(not {"numpy", "scipy"}.intersection(sys.modules), "no numerical import")
    print(
        json.dumps(
            {
                "passed": True,
                "source_pins": len(report["sources"]),
                "exact_families": list(report["controls"]),
                "numpy_scipy_blocked": True,
                "overwrite_rejected": True,
                "optimized_rejected": True,
                "certificate_sha256": hashlib.sha256(before).hexdigest(),
                "scope": (
                    "Read-only exact finite payload replay "
                    "and verification-runner negative controls."
                ),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
