# MCE cap-lift — blessed revision and cost measurement, 2026-08-22

The `run` stage of the frozen protocol fail-closed in
`runs/mce_freeze_and_first_run_2026-08-22/`: the engine's H0-closure BFS
carries an operational cap, `closure(seed_state, max_states=100)`, and the
first production cluster of 609 demands 216 states. Alex blessed the cap
lift on 2026-08-22. This directory is that blessing, and the measurement
Alex asked for before anyone commits to the sweep.

## Why the lift is not a mathematical change

The guard never truncates. It either returns the complete finite H0 orbit or
raises `ExactEngineError`:

```python
if len(states) > max_states:
    raise ExactEngineError("unexpectedly large H0 closure")
```

So raising the cap can only convert an abort into the complete orbit. It
cannot change any value the engine computes — only whether the sweep can
start. The measured demand, 216 states, is finite and barely 2x the cap: an
operational miscalibration inherited unchanged from the v06c electric-resolvent
lineage, never exercised at production size.

## The revision is regenerated, never vendored

`make_revision.py` reproduces it byte-for-byte from the pinned original and
refuses to write anything if either hash is wrong:

```
$ python3 runs/mce_cap_lift_2026-08-22/make_revision.py
[PASS] original  sha256 be9d77f5b245715ed6e4fe6dc9178a56ddfa5c68efe697eaa7cf4bb6adae27ad
[PASS] revision  sha256 9af3708e81a4a246130e50614dbe305341a3aaf3d726877a18205bb1ad1b11c0  (3 bytes added)
[PASS] wrote build/mce_cap_lift/DATA_SU3_Exact_MarkedCluster_m4_Colab_capfix.py
```

A 288 KB near-duplicate of an immutable corpus file is how a fork quietly
becomes a second source of truth, so the revision is not committed. It lands
under `build/` rather than in this directory because `tests/test_runs.py`
pins every entry of a run directory by digest, and a nested directory has no
digest. The corpus engine itself is untouched and still reads `max_states=100`;
`workhouse verify --only 'the blessed cap-lift revision reproduces byte-for-byte
from the pinned engine'` re-establishes the whole chain in about a second.

## Freeze against the revision

| Stage | Result |
|---|---|
| contamination scan | **clean** — engine source free of every quarantined constant |
| engine self-test | **47/47** exact Phase-2/Phase-3 gates |
| geometry preflight | **609** evaluations sealed, coverage SHA matches, zero physics |
| `FREEZE.json` | engine sha256 `9af3708e81a4a246…`, preflight `576a4a3f…`, manifest `40b8bcc7…` |

Both preflight pins reproduce the values the unmodified engine produced, which
is the point: the lift changed nothing the freeze stage can see.

## What this does NOT settle

Scoping protocol item 7 the same day changed the picture more than the cap lift
did. The Stage-3H leg is **not an unrun stage that hardware would clear — it is
an unwritten one.** The only Stage-3H-aware code in the corpus is
`_require_stage3h_sealed_out()`, which refuses to certify a run *unless*
Stage-3H was excluded. See the registered FINDING:

```bash
workhouse verify --only 'FINDING: G3 protocol item 7 has no implementation — only a guard that seals Stage-3H OUT'
```

So the 609-cluster sweep yields a **scalar-only (m4)** certificate. `C_shp` —
and with it C2, the one genuinely open item — needs item 7 as well. The sweep's
affordability and its sufficiency are now separate questions, and item 7 is the
binding one.

## Files

| File | What it is |
|---|---|
| `make_revision.py` | regenerates the blessed revision from the pinned original, verifying both hashes |
| `FREEZE.json` | the harness's freeze record for the revision |
| `freeze_console.log` | console transcript of the freeze stage |
| `harness_selftest.log` | engine self-test, 47/47 gates |
| `harness_manifest.log` | engine fail-closed manifest |
| `harness_preflight.log` | geometry preflight, 609 evaluations, zero physics |

`SHA256SUMS` pins everything above; `tests/test_runs.py` verifies it.
