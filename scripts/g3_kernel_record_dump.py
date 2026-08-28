#!/usr/bin/env python3
"""Rerun the v10a.26 kernel leg and dump the 189 records it never wrote down.

WHAT THIS IS NOT
----------------
Not sealed evidence and not a G3 certificate. It executes the imported
v10a.26 script (pinned by digest in ledger/notes.yaml) up to — and NOT
including — the rooted finite-cluster oracle leg, then writes the folded
axial kernel's nonzero records to JSON. The output is a diagnostic ledger:
useful for the block-structure comparison G3 step 2 names, worth nothing
until checks re-derive what it claims.

WHY IT EXISTS
-------------
The 15-hour transcript (notes/imported/HODGE_RUNS_2026-08-28/15_hour_RUN.txt)
proves the cold kernel had 189 anchored records, prints its shape fit
(A = 5/48 shared with the historical side, C = -0.020213328886166577), and
never dumps the records: K4_mass_cols existed only in the dead A100
process's memory. The kernel leg is the cheap leg — the 15 hours were the
oracle leg, which the C question does not need. Cutting before that leg
reruns only the kernel construction.

The records map to displacements trivially: faces[f] = (v, a, b) with v the
lattice vertex and (a, b) the polarization, and the anchor column index is
itself a T1 polarization. That is everything a block decomposition needs.

USAGE
-----
    python3 scripts/g3_kernel_record_dump.py            # CPU, default L
    V10_DUMP_OUT=out.json python3 scripts/g3_kernel_record_dump.py
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT / "notes" / "imported" / "HODGE_RUNS_2026-08-28" / "HODGE_v10a26_factor52_comp_script.txt"
)
#: ledger/notes.yaml digest for the imported script — refuse to run drift.
SCRIPT_SHA256 = "c123287ae7a38a327275557825d6f750bd15f38734a213d10c55842f7939819d"
#: Everything after this marker is the rooted oracle leg (the 15-hour half).
CUT_MARKER = "# HODGE v10a.24c — INDEPENDENT ROOTED FINITE-CLUSTER LINKED-GAP ORACLE"
OUT = Path(os.environ.get("V10_DUMP_OUT", "g3_kernel_records.json"))


def main() -> int:
    raw = SCRIPT.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != SCRIPT_SHA256:
        print(f"[FAIL] script digest {digest[:16]}... != pinned {SCRIPT_SHA256[:16]}...")
        return 1
    text = raw.decode("utf-8", errors="replace")
    cut = text.find(CUT_MARKER)
    if cut < 0:
        print("[FAIL] oracle-leg cut marker not found")
        return 1
    # The imported file opens with a markdown preamble; code begins at the
    # first import. The script sets PREFER_GPU=1 itself, so the CPU override
    # is applied to the body, not the environment — a config patch, no math.
    start = text.index("import os")
    body = text[start:cut].replace(
        'os.environ["PREFER_GPU"] = "1"', 'os.environ["PREFER_GPU"] = "0"', 1
    )

    sys.dont_write_bytecode = True  # the source lives in a pinned import dir

    print(
        f"[DUMP] executing kernel leg: {len(body.splitlines()):,} of "
        f"{len(text.splitlines()):,} lines, cut before the oracle leg",
        flush=True,
    )
    started = time.time()
    namespace: dict = {"__name__": "__main__", "__file__": str(SCRIPT)}
    exec(compile(body, str(SCRIPT), "exec"), namespace)  # noqa: S102 - pinned source
    elapsed = time.time() - started
    print(f"[DUMP] kernel leg complete in {elapsed / 60:.1f} min", flush=True)

    cols = namespace["V23_AXIAL_H4_COLS"]
    faces = namespace["faces"]
    t1_pols = namespace["T1_POLS"]
    tol = float(namespace["V23_RECORD_TOL"])
    shape = namespace["V23_AXIAL_SHAPE"]

    import numpy as np

    records = []
    for f in range(cols.shape[0]):
        v, a, b = faces[f]
        for col in range(cols.shape[1]):
            value = complex(cols[f, col])
            if abs(value) > tol:
                records.append(
                    {
                        "displacement": [int(x) for x in v],
                        "row_pol": [int(a), int(b)],
                        "anchor_pol": [int(x) for x in t1_pols[col]],
                        "re": float(np.real(value)),
                        "im": float(np.imag(value)),
                    }
                )
    payload = {
        "source": str(SCRIPT.relative_to(ROOT)),
        "source_sha256": digest,
        "cut_marker": CUT_MARKER,
        "record_tol": tol,
        "record_count": len(records),
        "shape": {
            k: (float(vv) if isinstance(vv, (int, float)) else str(vv))
            for k, vv in shape.items()
            if not isinstance(vv, (tuple, list))
        },
        "elapsed_minutes": elapsed / 60,
        "records": records,
    }
    OUT.write_text(json.dumps(payload, indent=1))
    print(f"[DUMP] {len(records)} records -> {OUT}", flush=True)
    print(f"[DUMP] shape: A={shape['A']!r} C_direct={shape['C_direct']!r}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
