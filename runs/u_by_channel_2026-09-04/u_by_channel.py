"""The two-hop weight u by irrep-labelled channel, on three chain types, N = 3..30.

    python u_by_channel.py > console.log

Writes certificate.json beside itself: for each chain (coplanar P-Q-R in one
plane; bent, with P and R on opposite faces of a cube through a side face; the
in-plane L, with the connector's two shared links adjacent), and each rank, the
C-odd contribution of every channel, labelled by the irreps of the doubled
links at each of the three intermediate states (direct term) or the two
resolvents (fold term). Nothing here reads a kernel or the engine.
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))

from workhouse import chain_channels as CC  # noqa: E402

CHAINS = {
    "coplanar": CC.COPLANAR,
    "bent": CC.BENT,
    "L": (((0, 1), (0, 0, 0)), ((0, 1), (1, 0, 0)), ((0, 1), (1, 1, 0))),
}
T0 = time.time()
cert = {"schema": "u_by_channel/v1", "chains": {k: [list(f) for f in v] for k, v in CHAINS.items()}, "ranks": {}}
for n in range(3, 31):
    row = {}
    for name, chain in CHAINS.items():
        t0 = time.time()
        d = CC.decompose(chain, n)
        row[name] = {"channels": {str(k): str(v) for k, v in sorted(d.items(), key=str)}, "u": str(sum(d.values()))}
        print(
            f"[{time.time() - T0:7.1f}s] N={n} {name}: {len(d)} channels, u = {row[name]['u']} ({time.time() - t0:.1f}s)",
            flush=True,
        )
    cert["ranks"][str(n)] = row
    (HERE / "certificate.json").write_text(json.dumps(cert, indent=1) + "\n", encoding="utf-8", newline="\n")
cert["seconds"] = round(time.time() - T0, 1)
(HERE / "certificate.json").write_text(json.dumps(cert, indent=1) + "\n", encoding="utf-8", newline="\n")
print("wrote certificate.json")
