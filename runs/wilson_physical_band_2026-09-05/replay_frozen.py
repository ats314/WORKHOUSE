"""Replay pinned finite controls without importing the installed workhouse package."""
import hashlib
import importlib.util
import json
import sys
import types
from pathlib import Path

sys.dont_write_bytecode = True
if sys.flags.optimize:
    raise RuntimeError("Assertions must be enabled")
root = Path(__file__).resolve().parent
report = json.loads((root / "certificate.json").read_text(encoding="utf-8"))
for name, expected in report["sources"].items():
    actual = hashlib.sha256((root / "source" / name).read_bytes()).hexdigest()
    if actual != expected:
        raise RuntimeError(f"Frozen source digest mismatch: {name}")

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

package = types.ModuleType("workhouse")
package.__path__ = []
sys.modules["workhouse"] = package
package.wilson_activity_extraction = load(
    "workhouse.wilson_activity_extraction",
    root / "source/src/workhouse/wilson_activity_extraction.py",
)
band = load("frozen_physical_band", root / "source/src/workhouse/wilson_physical_band.py")
if band.exact_controls() != report["finite_controls"]:
    raise RuntimeError("Frozen finite-control replay differs from certificate")
print("PASS: all eight source hashes and exact finite-control payload match")
print("Scope: finite projection, tagged Gram, activity exhaustion, counterexamples and rational margins")
print("The complete infinite-volume and OS theorem is the separately pinned analytic proof")
