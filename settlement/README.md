# Settlement package

Received artifacts, not repository code. They are pinned by `SHA256SUMS` and
treated the same way as `theory/`: evidence to be checked, never edited to make
a check pass.

| File | What it is |
|---|---|
| `SETTLEMENT.md` | the package's own account of what settles what |
| `cold_rerun_pentagonal_frontier.txt` | cold rerun, pentagonal O(4) minimal representation frontier, 8/8 |
| `cold_rerun_stranded_flux_audit.txt` | cold rerun, stranded-flux zero audit, 8/8, `ZERO_BACKEND_FALSIFIED` |
| `mce_adjudication_harness.py` | frozen-protocol driver for the marked-cluster engine (GLUEBALL §18.1) |

## On the harness

`mce_adjudication_harness.py` is vendored **as received**. It is the thing that
would actually decide C2, and it is verified upstream through contamination
scan, engine self-test (47/47), geometry preflight (609 evaluations, zero
physics), sealed-memfd launch, and interrupt/resume. What remains is the `run`
stage on production hardware.

Do not patch it here. `src/workhouse/settlement.py` reads it and
`invariants.py` records what the audit found; fixes belong upstream, and the
pinned hash then changes deliberately. The audit currently records that the
target-blindness scan has gaps — see the `FINDING:` checks.

## The engine is absent

The harness drives `Hodge_SU3_Exact_MarkedCluster_m4_Colab.py`, which is not in
this repository. Nothing here can run the `freeze`, `run` or `adjudicate`
stages; the checks below are static analysis of the harness source only.
