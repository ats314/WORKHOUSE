"""Replay frozen controls without importing the installed workhouse package."""
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

if sys.flags.optimize:
    raise RuntimeError("Frozen controls require assertions enabled")
root = Path(__file__).resolve().parent
certificate = json.loads((root / "certificate.json").read_text(encoding="utf-8"))
for name, expected in certificate["sources"].items():
    actual = hashlib.sha256((root / "source" / name).read_bytes()).hexdigest()
    if actual != expected:
        raise RuntimeError(f"Frozen source digest mismatch: {name}")

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

velocity = load("frozen_velocity", root / "source/src/workhouse/wilson_creator_velocity.py")
trees = load("frozen_trees", root / "source/src/workhouse/wilson_contour_trees.py")
if velocity.exact_controls() != certificate["finite_controls"]:
    raise RuntimeError("Frozen velocity/control replay differs from certificate")
if trees.exact_tree_control() != certificate["finite_tree_control"]:
    raise RuntimeError("Frozen marked-tree replay differs from certificate")
print("PASS: frozen source hashes, velocity/phase/contour/scalar controls and 20 tree coefficients")
print("Scope: exact finite controls; complete analytic theorems are the separately pinned proofs")
