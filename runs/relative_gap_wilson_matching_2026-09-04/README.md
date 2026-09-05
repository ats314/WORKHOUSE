# Relative gap and temporal Wilson matching run

Reference: `31255abac3829cb0cc1ce7c36c1852db8cdafbea`.

New derivations are in `paper/research_notes/G18_RELATIVE_GAP_BRIDGE_20260904.tex` and
`paper/research_notes/G19_TEMPORAL_WILSON_MATCHING_20260904.md`. The former is not
automatically input by the main manuscript. The original relative-gap Markdown
is retained in the companion download; its digest is in SOURCE_MANIFEST.json.

Executed: 12 prior relative-gap checks, 11 Wilson matching checks, and nine
exact algebra unit tests. Full WORKHOUSE CI was not run. Numerical diagnostics
need NumPy, SciPy, SymPy, separately listed in requirements.txt; core project
dependencies are unchanged.

From the repository root:

```bash
python -m pytest tests/test_temporal_matching_algebra.py
python runs/relative_gap_wilson_matching_2026-09-04/wilson_clock.py --output /tmp/wilson_check.json
python runs/relative_gap_wilson_matching_2026-09-04/verify_relative_gap_bridge.py --output /tmp/relative_check.json
```

The character tests are one-link SU(3) Weyl integration and a finite
21-character one-plaquette truncation. They do not establish an infinite-volume
Wilson carrier band. The G18 relative-gap theorem inherits the existing exact
weighted-symbol premises. The matching implication retains its unproved
physical weighted-band/source hypotheses. No G18/G19 closure is declared.

`graph_integration_proposal.json` is a staged proposal, not a native ledger
update. Register this run and refresh generated graph views only after the
repository-level checks and proof-dependency review. This additive patch does
not change immutable theory, numerical comparator constants, native gap
statuses, or the main manuscript.
