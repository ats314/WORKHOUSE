#!/usr/bin/env python3
"""Parallel G3 cluster sweep, for running on a real desktop.

It lives in scripts/ and not in settlement/ deliberately: settlement/ is
received evidence, pinned by its own manifest, and tests/test_settlement.py
holds it to an exact file list. This is repo-authored tooling, so putting it
there would have misclassified a diagnostic as evidence -- which is precisely
what that test caught.

WHAT THIS IS NOT
----------------
This is **not** the sealed adjudication path and it does not produce a G3
certificate. ``mce_adjudication_harness.py`` is that path: it runs the engine
from a sealed file descriptor under an authenticated context, which is what
makes its output tamper-evident. This script imports the engine as a module
and lifts one guard, so its output is a **diagnostic ledger** -- useful for
measuring cost, finding the clusters that fail, and seeing the coefficient
take shape, and worth nothing as evidence. Do not cite it as a G3 result.

WHY IT EXISTS
-------------
Two measurements from 2026-08-28 (both registered as checks):

* the engine's ``closure()`` caps at ``max_states=100``, but fourth order is
  insertion depth four and the H0 closure there is 160 -- the cap is a
  third-order scaffold, short by 1.6x, and the sealed run fail-closes on
  cluster 1 of 609 because of it;
* the closure walk itself costs under a second, so the cap is not why the
  sweep is slow. The cost is downstream, in the exact Haar contractions and
  resolvent inversions.

That second point is why this is parallel. The 609 clusters are independent,
so the sweep is embarrassingly parallel across cores, and exact rational
arithmetic is the one workload a GPU cannot help with -- it is bignum-bound,
branchy, and allocation-heavy. Cores and cache are the lever.

The 609 break down by support size as {1: 3, 2: 36, 3: 474, 4: 60, 5: 30,
6: 6}, and cost grows steeply with support, so work is issued smallest-first:
a partial run still tells you the shape of the cost curve.

USAGE
-----
    python3 scripts/g3_local_sweep.py --workers 8
    python3 scripts/g3_local_sweep.py --workers 8 --max-support 3
    python3 scripts/g3_local_sweep.py --resume        # skips completed rows

Results append to ``g3_sweep_results.jsonl`` one row per cluster, so the run is
resumable and survives being interrupted.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import sys
import time
from multiprocessing import Pool
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENGINE = (
    ROOT
    / "corpus-import"
    / "programs"
    / "hodge_o4_adjudication"
    / "src"
    / "DATA_SU3_Exact_MarkedCluster_m4_Colab.py"
)
RESULTS = Path("g3_sweep_results.jsonl")

#: Depth-4 closures measure 160; 100 is the shipped third-order scaffold. This
#: is generous headroom for depth 5 (the curve is 1, 2, 8, 32, 160, so roughly
#: x4-5 per insertion) without being unbounded -- a runaway should still stop.
CLOSURE_CAP = 4096

_ENGINE = None


def _engine():
    """Import the engine once per worker process, with the cap lifted."""
    global _ENGINE
    if _ENGINE is None:
        spec = importlib.util.spec_from_file_location("mce_engine", ENGINE)
        engine = importlib.util.module_from_spec(spec)
        sys.modules["mce_engine"] = engine
        # The engine lives in pinned corpus, and importing would write a
        # __pycache__ beside it that no manifest covers.
        previously = sys.dont_write_bytecode
        sys.dont_write_bytecode = True
        try:
            spec.loader.exec_module(engine)
        finally:
            sys.dont_write_bytecode = previously
        original = engine.closure
        engine.closure = lambda seed, max_states=CLOSURE_CAP: original(seed, max_states)
        _ENGINE = engine
    return _ENGINE


def clusters():
    """The 609 canonical clusters as (polarization, root, sorted support)."""
    engine = _engine()
    patch, roots, coverages, _candidate = engine.build_o4_triality_candidate_full_t1_coverage()
    out = []
    for pol in sorted(coverages):
        root = roots[pol]
        for embedding in coverages[pol].embeddings:
            support = tuple(sorted(int(f) for f in embedding.canonical_support))
            if root in support:
                out.append((pol, root, support))
    return out


def evaluate(task):
    pol, root, support = task
    engine = _engine()
    patch, _roots, _cov, _cand = engine.build_o4_triality_candidate_full_t1_coverage()
    builder = engine.ExactFaceInsertionBuilder(patch)
    cluster = engine.RootedOpenCluster(patch, root, frozenset(support))
    started = time.time()
    try:
        engine.evaluate_exact_endpoint_marked_vacuum_cluster(builder, cluster)
        return {
            "polarization": pol,
            "root": root,
            "support": list(support),
            "size": len(support),
            "seconds": round(time.time() - started, 3),
            "status": "ok",
        }
    except Exception as exc:  # noqa: BLE001 - a failing cluster is data, not a crash
        return {
            "polarization": pol,
            "root": root,
            "support": list(support),
            "size": len(support),
            "seconds": round(time.time() - started, 3),
            "status": f"{type(exc).__name__}: {exc}",
        }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workers", type=int, default=os.cpu_count() or 1)
    parser.add_argument("--max-support", type=int, default=6)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()

    tasks = [t for t in clusters() if t[2].__len__() <= args.max_support]
    tasks.sort(key=lambda t: (len(t[2]), t[0], t[2]))

    done = set()
    if args.resume and RESULTS.exists():
        for line in RESULTS.read_text().splitlines():
            if line.strip():
                row = json.loads(line)
                done.add((row["polarization"], row["root"], tuple(row["support"])))
        tasks = [t for t in tasks if t not in done]
        print(f"resuming: {len(done)} already recorded, {len(tasks)} remaining")

    if args.limit:
        tasks = tasks[: args.limit]

    print(f"{len(tasks)} clusters, {args.workers} workers, closure cap {CLOSURE_CAP}")
    print("NOT a sealed run: this is a diagnostic ledger, not a G3 certificate.\n")
    print(f"{'#':>5} {'size':>5} {'sec':>9}  status", flush=True)

    started = time.time()
    completed = 0
    with Pool(args.workers) as pool, RESULTS.open("a") as sink:
        for row in pool.imap_unordered(evaluate, tasks, chunksize=1):
            completed += 1
            sink.write(json.dumps(row, sort_keys=True) + "\n")
            sink.flush()
            elapsed = time.time() - started
            rate = completed / elapsed if elapsed else 0
            eta = (len(tasks) - completed) / rate if rate else float("inf")
            print(
                f"{completed:5d} {row['size']:5d} {row['seconds']:9.2f}  "
                f"{row['status'][:44]}   eta {eta / 60:.1f}m",
                flush=True,
            )

    print(f"\n{completed} clusters in {(time.time() - started) / 60:.1f} min -> {RESULTS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
