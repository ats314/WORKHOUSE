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

Register it on a suite in `invariants.py`, cite the corpus section *and the
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
- `invariants.py` — every T1/T2 check, grouped in suites
- `frontier.py` — computes `FRONTIER.md`; do not hand-write what it derives
- `ledger.py` — loads and structurally validates the three registers
- `graph.py` — computes `index/graph.jsonl`, every recorded edge between claims
- `navigator.py` — `workhouse why`: one id's whole evidence neighborhood
- `corpus_index.py` — exact rationals in code, certificates, notebooks
- `corpus_registry.py` — near-miss, multiple, and coverage sweeps over the whole corpus
- `tier_collapse.py`, `near_gamma.py`, `settlement.py` — one investigation each
- `triage.py` — read-only survey of an unpinned archive
