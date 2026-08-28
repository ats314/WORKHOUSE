"""Strong equivalence probe: fork vs pristine on REAL production state pairs.

Runs the perf fork through the full size-1 production cluster evaluation,
harvests every (left, right) state pair its _HAAR_CACHE exercised, then
recomputes a random sample of those inner products with the PRISTINE
cap-lifted engine and demands exact Fraction equality.

Also recomputes a sample of _CONTRACT_CACHE entries with the pristine
contract_link_partition and compares the full output dicts.
"""

import importlib.util
import json
import random
import sys
import time
from pathlib import Path

HERE = Path(__file__).parent
SAMPLE_INNER = 150
SAMPLE_CONTRACT = 300


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


perf = load("mce_perf", HERE / "engine_perf.py")
prist = load("mce_pristine", HERE / "engine_caplifted.py")

patch, roots, coverages, cert = perf.build_o4_triality_candidate_full_t1_coverage()
input_pol = 0
root = roots[input_pol]
supports = tuple(e.canonical_support for e in coverages[input_pol].embeddings)
support = min(supports, key=len)  # the size-1 cluster

builder = perf.ExactFaceInsertionBuilder(patch)
cluster = perf.RootedOpenCluster(patch, root, support)
t0 = time.time()
print(f"[EQ] evaluating size-{len(support)} cluster on fork...", flush=True)
ev = perf.evaluate_exact_endpoint_marked_vacuum_cluster(builder, cluster)
print(f"[EQ] fork evaluation: {time.time()-t0:.1f}s; "
      f"haar cache {len(perf._HAAR_CACHE)}, contract cache "
      f"{len(perf._CONTRACT_CACHE)}", flush=True)

rng = random.Random(20260828)

# --- haar_inner sample ---
keys = list(perf._HAAR_CACHE)
sample = rng.sample(keys, min(SAMPLE_INNER, len(keys)))
t1 = time.time()
bad = 0
for left, right in sample:
    a = perf._HAAR_CACHE[(left, right)]
    b = prist.haar_inner(prist.State(left.occ, left.part),
                         prist.State(right.occ, right.part))
    if a != b:
        bad += 1
        print(f"[EQ][MISMATCH] haar_inner {left} | {right}: {a} vs {b}",
              flush=True)
print(f"[EQ] haar_inner: {len(sample)} production pairs, {bad} mismatches "
      f"({time.time()-t1:.1f}s)", flush=True)

# --- contract_link_partition sample ---
ckeys = list(perf._CONTRACT_CACHE)
csample = rng.sample(ckeys, min(SAMPLE_CONTRACT, len(ckeys)))
t2 = time.time()
cbad = 0
for partition, u_occ, ubar_occ in csample:
    a = perf._CONTRACT_CACHE[(partition, u_occ, ubar_occ)]
    b = prist.contract_link_partition(partition, u_occ, ubar_occ)
    if a != b:
        cbad += 1
        print(f"[EQ][MISMATCH] contract {partition} {u_occ} {ubar_occ}",
              flush=True)
print(f"[EQ] contract_link_partition: {len(csample)} entries, {cbad} "
      f"mismatches ({time.time()-t2:.1f}s)", flush=True)

ok = bad == 0 and cbad == 0
Path(HERE / "probe_equiv_result.json").write_text(json.dumps({
    "haar_inner_pairs": len(sample), "haar_inner_mismatches": bad,
    "contract_entries": len(csample), "contract_mismatches": cbad,
    "verdict": "EXACT_AGREEMENT" if ok else "MISMATCH",
}, indent=2))
print(f"[EQ] {'PASS' if ok else 'FAIL'}", flush=True)
sys.exit(0 if ok else 1)
