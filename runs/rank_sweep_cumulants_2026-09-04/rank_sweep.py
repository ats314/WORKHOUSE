"""The fourth-order cluster cumulants at every rank N = 3..40, from the third engine.

    python rank_sweep.py > console.log

Writes certificate.json beside itself: per rank, the second-order hop in both
sectors and both raw leakages, the two-hop weight u in both sectors, and the
three dressing classes of the perpendicular pair (single contact, shared-link
fan, corner) in both sectors, all in the kernel's (0,2) basis. Nothing here
reads the engine, a kernel, or the corpus; the all-rank second-order formulas
are compared afterwards by the checks, not here.
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))

from workhouse import loopcalc as L  # noqa: E402

P, Q02, X = ((0, 1), (0, 0, 0)), ((0, 2), (0, 0, 0)), ((1, 2), (1, 0, 0))
results = {"schema": "rank_sweep_cumulants/v1", "basis": "(0,2) x-then-z, the kernel's", "ranks": {}}
T0 = time.time()
for n in range(3, 71):
    L.set_rank(n)
    t0 = time.time()
    single = L.Cluster([P])
    pair = L.Cluster([P, ((0, 1), (1, 0, 0))])
    perp = L.Cluster([P, Q02])
    h2s, _ = single.second_order()
    h2, _ = pair.second_order()
    h2p, _ = perp.second_order()
    wu = L.cumulant([P, ((0, 1), (1, 0, 0)), ((0, 1), (2, 0, 0))], 1)
    wc = L.cumulant([P, X, Q02], 1)
    wd = L.cumulant([P, ((0, 1), (1, 0, 0)), Q02], 1)
    ws = L.cumulant([P, ((0, 1), (0, -1, 0)), Q02], 1)
    r = {
        "hop_odd": str(L.codd(h2, 0, 1)),
        "hop_perp_odd": str(L.codd(h2p, 0, 1)),
        "hop_even": str(L.ceven(h2, 0, 1)),
        "leak_odd_raw": str(L.codd(h2, 0, 0) - L.codd(h2s, 0, 0)),
        "leak_even_raw": str(L.ceven(h2, 0, 0) - L.ceven(h2s, 0, 0)),
        "u_odd": str(L.block_odd(wu)),
        "u_even": str(L.block_even(wu)),
        "corner_odd": str(L.block_odd(wc)),
        "corner_even": str(L.block_even(wc)),
        "single_odd": str(L.block_odd(wd)),
        "single_even": str(L.block_even(wd)),
        "fan_odd": str(L.block_odd(ws)),
        "fan_even": str(L.block_even(ws)),
        "seconds": round(time.time() - t0, 1),
    }
    results["ranks"][str(n)] = r
    print(f"[{time.time() - T0:7.1f}s] N={n}: " + json.dumps(r), flush=True)
L.set_rank(3)
results["seconds"] = round(time.time() - T0, 1)
(HERE / "certificate.json").write_text(json.dumps(results, indent=1) + "\n", encoding="utf-8", newline="\n")
print("wrote certificate.json")
