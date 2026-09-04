"""The fourth-order cumulants of the beta_N assembly by resolvent channel, over Q(N).

    python channels.py > console.log

Every three-cluster cumulant of the assembly -- the two-hop weight u on the
coplanar, bent and in-plane L chains, the single-contact and fan dressings of
the coplanar and the perpendicular pair, and the corner dressing -- split by
channel with workhouse.symbolic_rank.channels: the direct term tagged by the
labels of its three intermediate states and the fold terms by the labels of
their two, a label being (extra fundamental links, irreps of the links carrying
more), read off each component's per-link energies. Every channel is one
rational function of N in each C-parity sector; the labels are rank-free by
construction.

Writes certificate.json: per cluster, per channel, the C-odd and C-even forms
as integer coefficient lists and factored strings.
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))

from sympy import factor  # noqa: E402

from workhouse import loopcalc as L  # noqa: E402
from workhouse import symbolic_rank as SR  # noqa: E402

P = ((0, 1), (0, 0, 0))
Q_COP = ((0, 1), (1, 0, 0))
Q_PERP = ((0, 2), (0, 0, 0))
CLUSTERS = {
    "u_coplanar": ([P, Q_COP, ((0, 1), (2, 0, 0))], 1),
    "u_bent": ([P, Q_PERP, ((0, 1), (0, 0, 1))], 1),
    "u_L": ([P, Q_COP, ((0, 1), (1, 1, 0))], 1),
    "single_perp": ([P, ((0, 1), (1, 0, 0)), Q_PERP], 1),
    "single_cop": ([P, ((0, 1), (2, 0, 0)), Q_COP], 1),
    "fan_perp": ([P, ((0, 1), (0, -1, 0)), Q_PERP], 1),
    "fan_cop": ([P, ((1, 2), (1, 0, 0)), Q_COP], 1),
    "corner": ([P, ((1, 2), (1, 0, 0)), Q_PERP], 1),
}

T0 = time.time()
out = {"schema": "channels_symbolic_rank/v1", "field": "Q(N)", "clusters": {}}
with SR.Symbolic() as S:
    for name, (faces, x_index) in CLUSTERS.items():
        t = time.time()
        ch = SR.channels(faces, x_index)
        rows = {}
        odd_total, even_total = SR.RF(0), SR.RF(0)
        for key in sorted(ch, key=SR.label_text):
            odd, even = SR.blocks(ch[key])
            odd_total, even_total = odd_total + odd, even_total + even
            rows[SR.label_text(key)] = {
                "key": repr(key),
                "odd": {"factored": str(factor(odd.to_sympy())), **odd.coefficient_lists()},
                "even": {"factored": str(factor(even.to_sympy())), **even.coefficient_lists()},
            }
        n_odd = sum(1 for r in rows.values() if r["odd"]["num"] != [0])
        n_even = sum(1 for r in rows.values() if r["even"]["num"] != [0])
        out["clusters"][name] = {
            "faces": [list(map(list, f)) for f in faces],
            "x_index": x_index,
            "channels": rows,
            "nonzero_odd": n_odd,
            "nonzero_even": n_even,
            "sum_odd": str(factor(odd_total.to_sympy())),
            "sum_even": str(factor(even_total.to_sympy())),
            "seconds": round(time.time() - t, 1),
        }
        print(
            f"[{time.time() - T0:7.1f}s] {name}: {len(rows)} channels ({n_odd} nonzero C-odd, "
            f"{n_even} nonzero C-even) in {time.time() - t:.1f}s; C-odd sum {out['clusters'][name]['sum_odd']}",
            flush=True,
        )
    out["audit"] = {k: v for k, v in S.stats.items() if k in ("components_verified", "max_weingarten_n", "max_charge")}
L.set_rank(3)
out["seconds"] = round(time.time() - T0, 1)
(HERE / "certificate.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8", newline="\n")
print("audit:", out["audit"])
print("wrote certificate.json in", out["seconds"], "s")
