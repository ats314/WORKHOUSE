# G9 sixth-order combination evidence

Source base: fa1bbadddd52955cb6517a0d7af5b59c086c40df (live main matched at start).

The [derivation](../../paper/research_notes/G9_SIXTH_ORDER_COMBINED_20260911.md)
and [task record](../../graph-tasks/2026-09-11-g9-sixth-combined.md) state hypotheses and scope.
`source-manifest.json` pins the preserved merged census script, tests and note.
`report.json` records every folded word, all 25 mixing pairs, exact one-face
coefficients and representation supports. An unknown direct multi-face H6 is
explicitly recorded as unknown. The initial check checkpoint is `validation.md`; final check results are retained
with the [task validation](../../graph-tasks/evidence/2026-09-11-g9-sixth-combined/validation.md)
outside the scientific input trees, so recording test outcomes does not invalidate the graph.

Reproduce with `python scripts/g9_sixth_order_rur_census.py --json --out NEW_REPORT.json`
and `pytest -q tests/test_sixth_order.py tests/test_g9_rur_dynamics.py`.
The original source snapshots are historical evidence, not runnable current claims.
