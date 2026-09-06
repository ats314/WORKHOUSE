"""Independent complete replay and rejection controls; writes fresh audit only."""

import copy
import hashlib
import importlib.abc
import json
import runpy
import subprocess
import sys
from pathlib import Path

if sys.flags.optimize:
    raise RuntimeError("Independent acceptance requires assertions enabled")
sys.dont_write_bytecode = True


class BlockNumerics(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname.split(".")[0] in {"numpy", "scipy"}:
            raise ImportError("Independent replay blocks numerical proposal libraries")


sys.meta_path.insert(0, BlockNumerics())
base = Path(__file__).resolve().parent
checker = base / "check_cubic_ground_transfer.py"
proof = base / "CUBIC_GROUND_TRANSFER.md"
report_path = base / "cubic_ground_controls_frozen.json"
output = base / "CUBIC_INDEPENDENT_REPLAY_VALIDATION.json"
if output.exists():
    raise FileExistsError(output)
files = [checker, proof, report_path]
before = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
module = runpy.run_path(str(checker), run_name="independent_cubic_model")
expected = json.loads(json.dumps(module["controls"]()))
source_pins = {p.name: before[p.name] for p in [checker, proof]}


def replay(report):
    if report.get("schema") != "wilson-cubic-ground-controls/v1":
        raise ValueError("schema differs")
    if report.get("passed") is not True:
        raise ValueError("success status differs")
    if report.get("controls") != expected:
        raise ValueError("complete independently recomputed payload differs")
    if report.get("sources") != source_pins:
        raise ValueError("actual source hashes differ")


saved = json.loads(report_path.read_text(encoding="utf-8"))
replay(saved)
negatives = []
for label, field, value in [
    ("corrupted rank", "exterior_rank2", 1),
    ("corrupted moving source", "moving_source_density_term", "0"),
]:
    corrupt = copy.deepcopy(saved)
    corrupt["controls"][field] = value
    try:
        replay(corrupt)
    except ValueError:
        negatives.append(label)
    else:
        raise ValueError("corruption accepted")
corrupt = copy.deepcopy(saved)
corrupt["sources"][proof.name] = "0" * 64
try:
    replay(corrupt)
except ValueError:
    negatives.append("corrupted proof hash")
else:
    raise ValueError("corrupted hash accepted")
optimized_output = base / "FORBIDDEN_OPTIMIZED_REPORT.json"
if optimized_output.exists():
    raise FileExistsError(optimized_output)
optimized = subprocess.run(
    [sys.executable, "-B", "-O", str(checker), "--output", str(optimized_output)],
    capture_output=True, text=True, check=False,
)
if optimized.returncode == 0 or optimized_output.exists():
    raise ValueError("optimized execution accepted")
overwrite = subprocess.run(
    [sys.executable, "-B", str(checker), "--output", str(report_path)],
    capture_output=True, text=True, check=False,
)
if overwrite.returncode == 0:
    raise ValueError("overwrite accepted")
after = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
if after != before:
    raise ValueError("frozen evidence changed")
result = {
    "passed": True, "complete_payload_replay": True,
    "numerical_imports_blocked": True, "sources_unchanged": True,
    "sources": before, "corruption_rejections": negatives,
    "optimized_rejected": optimized.returncode,
    "overwrite_rejected": overwrite.returncode,
}
with output.open("x", encoding="utf-8", newline="\n") as stream:
    json.dump(result, stream, indent=2, sort_keys=True)
    stream.write("\n")
print(json.dumps(result, sort_keys=True))
