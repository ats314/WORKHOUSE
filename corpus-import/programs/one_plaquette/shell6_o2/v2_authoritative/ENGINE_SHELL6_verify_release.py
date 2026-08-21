#!/usr/bin/env python3
from __future__ import annotations
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

EXPECTED = {
    "CERT_SHELL6_o2_representatives_v2.json":
        "b4f83612999ea658803689c49cf35a980a4c0f5950e4c94eee1bcd1c9ee6d4c0",
    "CERT_SHELL6_o2_matrix_v2.json":
        "ebd4bb69ccc909146bf60b14931a3ba6445f1a2b5edabbbb7532b4713aa5407c",
    "shell6_o2_analysis_v2.json":
        "631644769c488b8c42b46f4fd491cb9fea59181843eaa580ae21794ef49b4469",
}

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()

def gate(name: str, condition: bool, detail: str = "") -> None:
    print(("PASS" if condition else "FAIL"), name, detail)
    if not condition:
        raise RuntimeError(name)

for name, digest in EXPECTED.items():
    path = ROOT / name
    gate(f"{name} exists", path.exists())
    gate(f"{name} byte-identical hash", sha256(path) == digest, sha256(path))

channels = json.loads(
    (ROOT / "CERT_SHELL6_o2_exact_channel_certificate_v2.json").read_text()
)
coupling = json.loads(
    (ROOT / "CERT_SHELL6_shell46_t1_coupling_certificate_v1.json").read_text()
)

gate(
    "3+- lies below 0-- at O(u^2)",
    channels["ordering"]["three_plus_minus_below_zero_minus"] is True,
)
gate(
    "exact 3+- minus 0-- coefficient",
    channels["ordering"]["E_3+-_minus_E_0--_coefficient"]
    == "-1107923/959310",
)
gate("total shell4-shell6 g^2", coupling["total_g_squared"] == "16/9")
gate(
    "unfolded shell4 m2",
    coupling["shell4"]["unfolded_m2"] == "419/306",
)
gate(
    "branch coupling strengths",
    [row["g_squared"] for row in coupling["branches"]]
    == ["4/9", "8/9", "4/9"],
)

print("ALL RELEASE VERIFICATION GATES PASS")
