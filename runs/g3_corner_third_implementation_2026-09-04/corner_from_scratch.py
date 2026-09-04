"""The corner cluster from a third implementation, every dressing of the three
shared-link pairs, the cube completion in both bases, and the historical
pipeline's own ledger read by cluster -- the G3 route closed (ADR 0024).

    python corner_from_scratch.py > console.log

Writes certificate.json beside itself. Reads: workhouse.loopcalc (the third
engine), workhouse.stage3i (the pinned Stage-3I fixture), workhouse.cellular
(the multi-loop cube completion), and, for comparison only, the registered
constants and the 2026-09-02 run's certificate.
"""

from __future__ import annotations

import json
import sys
import time
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))

from workhouse import cellular as CEL  # noqa: E402
from workhouse import constants as K  # noqa: E402
from workhouse import loopcalc as L  # noqa: E402
from workhouse import stage3i as S  # noqa: E402
from workhouse.payloads import kernel_records  # noqa: E402

T0 = time.time()


def log(msg):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


def fr(x):
    return str(x)


cert = {"schema": "g3_corner_third_implementation/v1"}

# ---- second order and the chain amplitude
single = L.Cluster([((0, 1), (0, 0, 0))])
pair = L.Cluster([((0, 1), (0, 0, 0)), ((0, 1), (1, 0, 0))])
perp = L.Cluster([((0, 1), (0, 0, 0)), ((0, 2), (0, 0, 0))])
h2s, _ = single.second_order()
h2, _ = pair.second_order()
h2p, _ = perp.second_order()
cert["second_order"] = {
    "coplanar_hop": fr(L.codd(h2, 0, 1)),
    "perpendicular_hop_(0,2)": fr(L.codd(h2p, 0, 1)),
    "c_even_hop": fr(L.ceven(h2, 0, 1)),
    "leakage": fr(L.codd(h2, 0, 0) - L.codd(h2s, 0, 0) + F(3, 4)),
}
log("second order: " + json.dumps(cert["second_order"]))

CHAINS = {
    "coplanar-coplanar": [((0, 1), (0, 0, 0)), ((0, 1), (1, 0, 0)), ((0, 1), (2, 0, 0))],
    "coplanar-perpendicular": [((0, 1), (0, 0, 0)), ((0, 1), (1, 0, 0)), ((1, 2), (2, 0, 0))],
    "perpendicular-perpendicular": [((0, 1), (0, 0, 0)), ((0, 2), (0, 0, 0)), ((0, 1), (0, 0, 1))],
}
cert["chains"] = {}
for name, faces in CHAINS.items():
    w = L.cumulant(faces, 1)
    cert["chains"][name] = {"codd": fr(L.block_odd(w)), "ceven": fr(L.block_even(w))}
    log(f"chain {name}: " + json.dumps(cert["chains"][name]))

# ---- every dressing of the three pairs, in the kernel's own basis
PAIRS = {
    "coplanar": (((0, 1), (0, 0, 0)), ((0, 1), (1, 0, 0))),
    "normal": (((0, 1), (0, 0, 0)), ((0, 1), (0, 0, 1))),
    "perpendicular": (((0, 1), (0, 0, 0)), ((0, 2), (0, 0, 0))),
}
cert["pairs"] = {}
for name, (P, Q) in PAIRS.items():
    xs = L.plaquettes_sharing_a_link([P, Q])
    dressings = {}
    for X in xs:
        w = L.cumulant([P, X, Q], 1)
        dressings[str(X)] = {"codd": fr(L.block_odd(w)), "ceven": fr(L.block_even(w))}
    far = L.cumulant([P, ((0, 1), (5, 0, 0)), Q], 1)
    entry = {
        "faces": [list(P), list(Q)],
        "dressings": dressings,
        "dressing_sum_codd": fr(sum(F(d["codd"]) for d in dressings.values())),
        "dressing_sum_ceven": fr(sum(F(d["ceven"]) for d in dressings.values())),
        "far_X_gate_all_zero": all(v == 0 for v in far.values()),
    }
    cert["pairs"][name] = entry
    log(
        f"pair {name}: {len(xs)} dressings, sum C-odd {entry['dressing_sum_codd']}, "
        f"far gate zero: {entry['far_X_gate_all_zero']}"
    )

# ---- the cube completion from the third engine, both bases
P = ((0, 1), (0, 0, 0))
others_perp = [((0, 1), (0, 0, 1)), ((0, 2), (0, 1, 0)), ((1, 2), (0, 0, 0)), ((1, 2), (1, 0, 0))]
others_norm = [((0, 2), (0, 0, 0)), ((0, 2), (0, 1, 0)), ((1, 2), (0, 0, 0)), ((1, 2), (1, 0, 0))]
cubes = {}
for name, Q, others in (
    ("normal", ((0, 1), (0, 0, 1)), others_norm),
    ("perpendicular_(2,0)", ((2, 0), (0, 0, 0)), others_perp),
    ("perpendicular_(0,2)", ((0, 2), (0, 0, 0)), others_perp),
):
    w = L.cube_completion(P, Q, others)
    cubes[name] = {
        "W": {str(k): fr(v) for k, v in w.items()},
        "codd": fr(L.block_odd(w)),
        "ceven": fr(L.block_even(w)),
    }
    log(f"cube {name}: C-odd {cubes[name]['codd']} C-even {cubes[name]['ceven']}")
cert["cube_completion_third_engine"] = cubes

amp_opp, _ = CEL.c_full(CEL.CUBE, 0, 1)
amp_adj, rows = CEL.c_full(CEL.CUBE, 0, 2)
cert["cube_completion_multiloop"] = {
    "opposite": str(amp_opp),
    "adjacent": str(amp_adj),
    "adjacent_at_3": fr(F(str(amp_adj.subs(CEL.N, 3)))),
    "single_loop_histories": sum(1 for r in rows if all(n == 1 for n in r[2])),
    "multi_loop_histories": sum(1 for r in rows if not all(n == 1 for n in r[2])),
}
log("multi-loop cube completion: " + json.dumps(cert["cube_completion_multiloop"]))

# ---- the historical pipeline's own ledger, by cluster
full = S.build_full_kernel(S.build_root_kernel(S.load_words()))
cert["stage3i"] = {
    "fixture_sha256_gz": S.STAGE3I_SHA,
    "words": len(S.load_words()),
    "reassembly_equals_pinned_kernel": full == dict(kernel_records()),
}
hist = {}
for sector in ("odd", "even"):
    classes = S.cluster_classes(S.ROTATION_OUTPUT, sector)
    hist[sector] = {
        c: {
            "sum": fr(v["sum"]),
            "supports": v["supports"],
            "values": sorted({fr(x) for x in v["values"]}),
        }
        for c, v in classes.items()
    }
cert["stage3i"]["rotation_record_by_cluster"] = hist
cube_hist = S.cube_words(S.ROTATION_OUTPUT)
cert["stage3i"]["rotation_cube_words"] = [{"id": i, "codd": fr(v)} for i, _ins, v in cube_hist]
log(f"stage-3I reassembly == pinned kernel: {cert['stage3i']['reassembly_equals_pinned_kernel']}")
log(
    "historical rotation record by cluster (C-odd): "
    + json.dumps({c: v["sum"] for c, v in hist["odd"].items()})
)

# ---- the rotation element in the kernel's basis, assembled and historical
run = json.loads(
    (
        ROOT / "runs" / "g3_shared_link_pair_2026-09-02" / "shared_link_pair_certificate.json"
    ).read_text(encoding="utf-8")
)
pair_cluster = F(
    run["pairs"]["perpendicular"]["pair_cluster_codd"]
)  # the one piece not recomputed here
dress = sum(F(d["codd"]) for d in cert["pairs"]["perpendicular"]["dressings"].values())
cube_full = F(cubes["perpendicular_(0,2)"]["codd"])
non_cube = -pair_cluster + dress  # the (0,2) basis: every C-odd element of the (2,0) run flips
rho_asm = non_cube + cube_full
rho_hist = F(K.RHO_ORBIT.p, K.RHO_ORBIT.q)
cube_hist_sum = F(hist["odd"]["cube(six faces once each)"]["sum"])
u = F(K.X_QUANTUM.p, K.X_QUANTUM.q)
pi = F(K.PI_ORBIT.p, K.PI_ORBIT.q)
c_hist = F(K.C_SHP_HISTORICAL.p, K.C_SHP_HISTORICAL.q)
c_asm = F(-5, 96) - u - (rho_asm + pi) / 2
cert["rotation_element_kernel_basis"] = {
    "pair_cluster_codd_(0,2)": fr(-pair_cluster),
    "dressing_sum_codd_(0,2)": fr(dress),
    "non_cube_part": fr(non_cube),
    "cube_full": fr(cube_full),
    "cube_historical": fr(cube_hist_sum),
    "rho_assembled": fr(rho_asm),
    "rho_historical": fr(rho_hist),
    "rho_historical_minus_assembled": fr(rho_hist - rho_asm),
    "C_shp_assembled": fr(c_asm),
    "C_shp_historical": fr(c_hist),
    "C_shp_assembled_minus_historical": fr(c_asm - c_hist),
    "equals_C_SHP_CONTINUATION_SHIFTED": c_asm
    == F(K.C_SHP_CONTINUATION_SHIFTED.p, K.C_SHP_CONTINUATION_SHIFTED.q),
    "rho_historical_equals_non_cube_plus_historical_cube": rho_hist == non_cube + cube_hist_sum,
}
log(
    f"kernel basis: rho_asm {rho_asm} = {float(rho_asm):.10f}, rho_hist {rho_hist} = "
    f"{float(rho_hist):.10f}, difference {rho_hist - rho_asm}"
)
log(
    f"C_shp assembled {c_asm} = {float(c_asm):.12f}; equals C_SHP_CONTINUATION_SHIFTED: "
    f"{cert['rotation_element_kernel_basis']['equals_C_SHP_CONTINUATION_SHIFTED']}"
)
cert["seconds"] = round(time.time() - T0, 1)
(HERE / "certificate.json").write_text(json.dumps(cert, indent=1) + "\n", encoding="utf-8")
log("wrote certificate.json")
