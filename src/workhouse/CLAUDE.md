# The checking layer

This is where a claim stops being prose. Everything here is about the
distinction between what the corpus says and what has been re-derived.

## Exact stays exact

Corpus rationals are `sympy.Rational`. Values the corpus records only as
floating point are Python floats named with a `_NUM` suffix. A float that reads
as exact is the most dangerous bug in this codebase, and
`tests/test_constants.py` guards the boundary.

Any function taking a rank or extent must `sympify()` its argument. `hopping(3)`
returning `0.00816...` instead of `5/612` is a bug this repository has already
shipped once.

## Adding an invariant

Register it on a suite in the module for its subject under `invariants/`,
cite the corpus section *and the
document*, and return `(passed, detail)` where `detail` carries the numbers a
reader needs to argue with you. `tests/test_invariants.py` picks it up with no
separate test to write.

A check whose detail line is a restatement of its name is documentation wearing
a check's clothes. `"close enough"` is not a finding; `3.0e-15 = 31 ulps` is.

## Never widen a tolerance

If a check fails, it found something. Three possibilities: a bug in the check, a
transcription slip in the registry, or a real discrepancy in the corpus. For the
third, add an explicit `FINDING:` check that *asserts* the discrepancy.

## Files

- `constants.py` — the curated registry, with provenance and corpus status
- `invariants/` — every T1/T2 check, one module per subject; `__init__` fixes
  the order the suites register in, `_core` holds the plumbing
- `frontier.py` — computes `FRONTIER.md`; do not hand-write what it derives
- `ledger.py` — loads and structurally validates the three registers
- `graph.py` — computes `index/graph.jsonl`, every recorded edge between claims
- `navigator.py` — `workhouse why`: one id's whole evidence neighborhood,
  its traversal, and the replay-status axis (orthogonal to tier and status)
- `render.py` — the colour decision and the JSON boundary, in one place
- `branches.py` — `workhouse branches`: each disagreement's sides, side by side
- `derive.py` — `workhouse derive`: recorded support, dependency-ordered
- `snapshot.py` — `workhouse drift`: live run versus the checked-in `index/`
- `atlas.py` — the graph as one self-contained HTML page; a view, never checked in
- `corpus_index.py` — exact rationals in code, certificates, notebooks
- `corpus_registry.py` — near-miss, multiple, and coverage sweeps over the whole corpus
- `tier_collapse.py`, `near_gamma.py`, `settlement.py`, `payloads.py` — one investigation each
- `even_sector.py` — the charge-even Bloch cubic, and the finite lattice it is checked against
- `rigor.py` — certified Arb enclosures for T2 comparisons (ADR 0010); the only sanctioned route to arb
- `triage.py` — read-only survey of an unpinned archive
- `notes.py` — the notes register: archive inventories, review verdicts, intake rules
