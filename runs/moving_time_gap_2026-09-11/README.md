# Moving-time spectral gap derivation evidence

The mathematical source is
[moving-time-spectral-gap.md](../../docs/derivations/moving-time-spectral-gap.md).
The pinned summary is
[MOVING_TIME_SPECTRAL_GAP_20260911.md](../../paper/research_notes/MOVING_TIME_SPECTRAL_GAP_20260911.md).

`start.json` is the retained saved briefing at base
`7cf8a646521259a34a772d65c8740ef7597f0265`; freshness was unknown in the
new worktree and no Python checks executed for that saved request.
`start-fresh.json` preserves an unsuccessful fresh attempt: the new source
file had been created while the inventory was not yet registered. Its
explicit error is an inventory mismatch. It is not passing fresh evidence.
The source was subsequently registered and both native loaders validated.

The [task record](../../graph-tasks/2026-09-11-moving-time-gap.md) retains
the final commands, current validation results, end briefing, and landing
state. `source-manifest.json` identifies the reviewed premises and resulting
source bytes. Graph-task evidence remains outside scientific input scope so
recording execution observations does not change scientific input fingerprints.

Reproduce the four exact mathematical controls:

```text
workhouse verify --only moving-time
pytest -q tests/test_moving_time_gap.py
```

Full theorem status is proven with analytic evidence. The measure-limit,
spectral identification and density arguments have no whole-statement
Lean certificate. The T1 controls certify only their named finite or symbolic
identities; no Wilson trajectory bound or continuum mass gap was measured.
