"""Diagnostic probe for the MCE 'unexpectedly large H0 closure' failure.

Imports the engine UNMODIFIED, then monkey-patches the module-global
`closure` with a wrapper that calls the engine's own closure() with a large
cap and records the actual orbit sizes demanded. No mathematical change:
closure() either returns the complete unique H0 orbit or aborts — a larger
cap can only convert an abort into the complete orbit.

Runs the first production cluster of polarization 0 exactly as the sealed
sweep would (same builder, same root, same support), outside the sealed
authentication (which gates only the certificate, not the mathematics).
"""

import importlib.util
import json
import sys
import time
from pathlib import Path

ENGINE = Path(
    "/home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/src/"
    "DATA_SU3_Exact_MarkedCluster_m4_Colab.py"
)

spec = importlib.util.spec_from_file_location("mce_engine", ENGINE)
eng = importlib.util.module_from_spec(spec)
sys.modules["mce_engine"] = eng
spec.loader.exec_module(eng)

_original_closure = eng.closure
SIZES = []


def probing_closure(seed_state, max_states: int = 100):
    result = _original_closure(seed_state, max_states=10**6)
    SIZES.append(len(result))
    if len(result) > 100:
        print(f"[PROBE] closure size {len(result)} exceeds the shipped cap 100",
              flush=True)
    return result


eng.closure = probing_closure

t0 = time.time()
print("[PROBE] building sealed candidate coverage ...", flush=True)
patch, roots, coverages, candidate_certificate = (
    eng.build_o4_triality_candidate_full_t1_coverage()
)
print(f"[PROBE] coverage built in {time.time()-t0:.1f}s; "
      f"certificate {candidate_certificate['certificate_sha256'][:16]}...",
      flush=True)

input_pol = 0
root = roots[input_pol] if isinstance(roots, (tuple, list)) else roots[input_pol]
coverage = coverages[input_pol]
supports = tuple(e.canonical_support for e in coverage.embeddings)
print(f"[PROBE] pol {input_pol}: {len(supports)} clusters; "
      f"first support size {len(supports[0])}", flush=True)

builder = eng.ExactFaceInsertionBuilder(patch)
cluster = eng.RootedOpenCluster(patch, root, supports[0])

t1 = time.time()
print("[PROBE] evaluating first production cluster ...", flush=True)
evaluation = eng.evaluate_exact_endpoint_marked_vacuum_cluster(builder, cluster)
dt = time.time() - t1

print(f"[PROBE] first cluster complete in {dt:.1f}s", flush=True)
print(f"[PROBE] closure calls: {len(SIZES)}; max size {max(SIZES)}; "
      f"sizes>100: {sorted(s for s in SIZES if s > 100)}", flush=True)
print("[PROBE] gap rows by order:", flush=True)
for order, row in enumerate(evaluation.gap_rows_by_order, start=1):
    print(f"  order {order}: {[str(v) for v in row]}", flush=True)

out = {
    "first_cluster_seconds": dt,
    "closure_calls": len(SIZES),
    "max_closure_size": max(SIZES),
    "oversize_closures": sorted(s for s in SIZES if s > 100),
    "support": [str(s) for s in supports[0]],
}
Path("probe_result.json").write_text(json.dumps(out, indent=2))
print("[PROBE] DONE", flush=True)
