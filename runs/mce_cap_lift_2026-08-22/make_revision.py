#!/usr/bin/env python3
"""Regenerate the cap-lifted MCE engine revision from the pinned original.

The revision is NOT vendored: it is a 288 KB near-duplicate of an immutable
corpus file, and duplicating the corpus to change three bytes is how a fork
silently becomes a second source of truth. This script reproduces it
byte-for-byte instead, and refuses to write anything if either hash is wrong.

    python3 runs/mce_cap_lift_2026-08-22/make_revision.py

Writes build/mce_cap_lift/DATA_SU3_Exact_MarkedCluster_m4_Colab_capfix.py
(gitignored: it lives outside the run directory because tests/test_runs.py pins
every entry of a run dir by digest, and a nested directory has no digest).

What changes, and why it is not a mathematical change: the engine's H0-closure
BFS carries an operational cap, `closure(seed_state, max_states=100)`. The guard
never truncates -- it either returns the complete finite orbit or raises
ExactEngineError -- so raising the cap can only convert an abort into the
complete orbit. It cannot change any value the engine computes. The first
production cluster demands 216 states (measured), so the shipped cap of 100
fail-closes the sweep before it starts.
"""

import hashlib
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]

ORIGINAL = (
    REPO
    / "corpus-import/programs/hodge_o4_adjudication/src"
    / "DATA_SU3_Exact_MarkedCluster_m4_Colab.py"
)
ORIGINAL_SHA = "be9d77f5b245715ed6e4fe6dc9178a56ddfa5c68efe697eaa7cf4bb6adae27ad"
REVISION_SHA = "9af3708e81a4a246130e50614dbe305341a3aaf3d726877a18205bb1ad1b11c0"

OLD = b"def closure(seed_state: State, max_states: int = 100) -> list[State]:"
NEW = b"def closure(seed_state: State, max_states: int = 100000) -> list[State]:"

OUT = REPO / "build" / "mce_cap_lift" / "DATA_SU3_Exact_MarkedCluster_m4_Colab_capfix.py"


def main() -> int:
    original = ORIGINAL.read_bytes()
    got = hashlib.sha256(original).hexdigest()
    if got != ORIGINAL_SHA:
        print(f"[FAIL] pinned original has moved: {got} != {ORIGINAL_SHA}")
        return 1
    if original.count(OLD) != 1:
        print(f"[FAIL] closure signature appears {original.count(OLD)} times, expected 1")
        return 1
    revision = original.replace(OLD, NEW, 1)
    got = hashlib.sha256(revision).hexdigest()
    if got != REVISION_SHA:
        print(f"[FAIL] revision hash mismatch: {got} != {REVISION_SHA}")
        return 1
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes(revision)
    print(f"[PASS] original  sha256 {ORIGINAL_SHA}")
    print(f"[PASS] revision  sha256 {REVISION_SHA}  ({len(revision) - len(original)} bytes added)")
    print(f"[PASS] wrote {OUT.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
