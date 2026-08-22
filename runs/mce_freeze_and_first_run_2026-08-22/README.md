# MCE frozen-protocol attempt — 2026-08-22

The first execution of the settlement harness's `freeze` and `run` stages
anywhere: the engine the settlement package records as absent is in
`corpus-import/` under the import pipeline's rename (see the
`the engine the harness drives IS in the repository` check), so the
frozen protocol of GLUEBALL §18.1 became executable in this repository.

Everything here was produced by the pinned harness
(`settlement/mce_adjudication_harness.py`, unmodified) driving the pinned
engine (`corpus-import/programs/hodge_o4_adjudication/src/DATA_SU3_Exact_MarkedCluster_m4_Colab.py`,
unmodified), on this repository's container (Linux, CPython 3.11.15,
sympy 1.14.0, single core).

## What happened

| Stage | Result |
|---|---|
| `freeze` | **PASS** — contamination scan clean, self-test 47/47, geometry preflight 609 evaluations with both SHA256 pins matching (`FREEZE.json`) |
| `run` | **FAIL-CLOSED on cluster 1 of 609** — `ExactEngineError: unexpectedly large H0 closure` (`harness_production.log`) |

The failure is deterministic exact arithmetic over the engine's own sealed
candidate inventory: the identical failure occurs on any machine, including
the production box the settlement package deferred to. The `run` stage was
never executable as received.

## The mechanism

`closure(seed_state, max_states=100)` caps the BFS enumeration of a seed
state's H0 orbit. The guard never truncates — it either returns the complete
finite orbit or aborts — so the cap is operational, not mathematical. It was
inherited unchanged from the electric-resolvent lineage
(`corpus-import/programs/hodge_haar_krylov/NB_HAAR_hodge_electric_resolvent_v06c.ipynb`,
same `max_states=100`), and no pre-production path exercises it at
production size: the self-test deliberately contracts no real half-history,
the geometry preflight runs zero physics, and the upstream sandbox record
says the first cluster evaluation was *started*, not finished. The first
production cluster of polarization 0 has **support size 1** — the failure is
not a large-cluster corner case; it is the first R2-stage resolvent of the
sweep.

Measured demand (diagnostic probe, engine unmodified, module-global
`closure` wrapped with a 10^6 cap and size recording — `probe_closure.py`,
transcript `probe_console.log`): the first oversize orbit is **216 states**
— finite, barely 2x the cap; an operational miscalibration, not an
explosion. The probe was terminated at session budget before the 1-face
cluster's full evaluation completed (~13.5 CPU-minutes single-core at
termination), so per-cluster wall cost is bounded below, not measured:
even the smallest of the 609 clusters costs >13 CPU-minutes, and 474 of
them are 3-face. A support-size census of the sealed coverage:
each polarization has sizes {1: 1, 2: 12, 3: 158, 4: 20, 5: 10, 6: 2}.

A cap-lifted single-line fork (100 -> 100000, sha256 9af3708e81a4a246...)
passes the full freeze stage — contamination scan, self-test 47/47, both
preflight pins — so the protocol becomes startable the moment the cap is
raised; whether it is affordable is the open cost question. The fork was
not run and is not vendored: the fix belongs upstream, where the pinned
engine hash changes deliberately.

## Reproduction

```bash
cd $(mktemp -d)
python3 /path/to/repo/settlement/mce_adjudication_harness.py \
  --engine /path/to/repo/corpus-import/programs/hodge_o4_adjudication/src/DATA_SU3_Exact_MarkedCluster_m4_Colab.py \
  freeze   # minutes; passes
python3 /path/to/repo/settlement/mce_adjudication_harness.py \
  --engine ... run   # fail-closes on cluster 1
```

## Files

| File | What it is |
|---|---|
| `FREEZE.json` | the harness's freeze record: engine SHA-256, self-test tally, preflight pins |
| `freeze_console.log` | console transcript of the freeze stage |
| `harness_selftest.log` | engine self-test, 47/47 gates |
| `harness_manifest.log` | engine fail-closed manifest |
| `harness_preflight.log` | geometry preflight, 609 evaluations, zero physics |
| `run_console.log` | console transcript of the run stage, with the harness [FAIL] |
| `harness_production.log` | the sealed subprocess's log: one progress line, then the traceback |
| `probe_closure.py` | the diagnostic probe (engine file untouched; module-global `closure` wrapped) |
| `probe_console.log` | probe transcript: the 216-state measurement, and the termination note |

Not vendored: `RESUME_SECRET.json` (run credentials), the sqlite checkpoint
(empty — no cluster ever completed), the `.status` file (ephemeral).
`SHA256SUMS` pins everything above; `tests/test_runs.py` verifies it.
