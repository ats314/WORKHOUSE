"""Equivalence + speed probe for the performance fork.

1. Imports BOTH the cap-lifted pristine engine and the perf fork as separate
   modules.
2. Cross-checks haar_inner exactly on a sample of basis-state pairs from the
   first production cluster's closure (fork vs pristine, Fraction equality).
3. Times the perf fork on full cluster evaluations of increasing support size
   (the sealed sweep's own entry point, outside the sealed authentication,
   which gates only the certificate, not the mathematics).
"""

import importlib.util
import json
import random
import sys
import time
from pathlib import Path

HERE = Path(__file__).parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


perf = load("mce_perf", HERE / "engine_perf.py")
prist = load("mce_pristine", HERE / "engine_caplifted.py")

t0 = time.time()
print("[PROBE] building sealed candidate coverage (perf fork)...", flush=True)
patch, roots, coverages, cert = perf.build_o4_triality_candidate_full_t1_coverage()
print(f"[PROBE] coverage built in {time.time()-t0:.1f}s", flush=True)

input_pol = 0
root = roots[input_pol]
coverage = coverages[input_pol]
supports = tuple(e.canonical_support for e in coverage.embeddings)
by_size = {}
for s in supports:
    by_size.setdefault(len(s), []).append(s)
print(f"[PROBE] support census: { {k: len(v) for k, v in sorted(by_size.items())} }",
      flush=True)

# --- equivalence: haar_inner on sampled pairs from the smallest closure ---
builder_p = perf.ExactFaceInsertionBuilder(patch)
seed_support = by_size[1][0]

# sample production-like states: closure of a two-face tensor product
t1 = time.time()
f0, f1 = patch.faces[0], patch.faces[1]
seed = perf.tensor_product(perf.trace_state(f0.steps), perf.trace_state(f1.steps))
factor, seed = perf.simplify_unitarity(seed)
basis_states = perf.closure(seed)
print(f"[PROBE] closure of two-face tensor: {len(basis_states)} states "
      f"({time.time()-t1:.1f}s)", flush=True)

rng = random.Random(20260828)
n = len(basis_states)
pairs = [(rng.randrange(n), rng.randrange(n)) for _ in range(60)]
t2 = time.time()
mismatch = 0
for i, j in pairs:
    a = perf.haar_inner(basis_states[i], basis_states[j])
    # translate State across modules via constructor fields
    li = prist.State(basis_states[i].occ, basis_states[i].part)
    rj = prist.State(basis_states[j].occ, basis_states[j].part)
    b = prist.haar_inner(li, rj)
    if a != b:
        mismatch += 1
        print(f"[PROBE][MISMATCH] pair ({i},{j}): fork {a} vs pristine {b}",
              flush=True)
print(f"[PROBE] haar_inner cross-check: {len(pairs)} pairs, "
      f"{mismatch} mismatches ({time.time()-t2:.1f}s)", flush=True)
if mismatch:
    sys.exit(1)

# --- speed: full cluster evaluations on the fork ---
results = {}
for size in sorted(by_size):
    support = by_size[size][0]
    cluster = perf.RootedOpenCluster(patch, root, support)
    t3 = time.time()
    print(f"[PROBE] evaluating one size-{size} cluster (perf fork)...", flush=True)
    ev = perf.evaluate_exact_endpoint_marked_vacuum_cluster(builder_p, cluster)
    dt = time.time() - t3
    results[size] = dt
    print(f"[PROBE] size {size}: {dt:.1f}s; contract cache "
          f"{len(perf._CONTRACT_CACHE)} entries; haar cache "
          f"{len(perf._HAAR_CACHE)} entries", flush=True)
    if size >= 3:
        break  # sizes 1..3 cover 171/203 supports; enough to extrapolate

census = {k: len(v) for k, v in sorted(by_size.items())}
Path(HERE / "probe_perf_result.json").write_text(json.dumps(
    {"seconds_by_size": results, "census": census}, indent=2))
print("[PROBE] DONE", flush=True)
