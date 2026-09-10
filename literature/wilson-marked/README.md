# Wilson marked-transfer continuation

The [derivation](../../docs/derivations/wilson-marked-transfer.md) constructs exact physical-time blocks of the symmetric Wilson transfer. It derives an all-orders block activity bound and a uniform vacuum polymer expansion. The remaining complete-shell coefficient estimate is stated explicitly in WT-6.

[theory_graph.yaml](theory_graph.yaml) adds six source-located native study nodes. Analytic statements retain their T3 study tier; separate check and Lean nodes identify the exact verified parts. G19 has a completed vacuum-block route and a live complete-shell route, without changing the gap's open status.

[sources.json](sources.json) pins three acquired papers and their extraction hashes: 53 additional PDF pages in total, with selected reading scopes recorded. Their working PDFs and extracted text live in the ignored `literature/inbox/WILSON_MARKED_20260908/` directory. The original Kotecky-Preiss article remains metadata-only; the convergence criterion actually inspected is Ueltschi's Theorem 1.

```text
workhouse why STUDY:YM:wilson-vacuum-majorant
workhouse why STUDY:YM:wilson-complete-shell
workhouse why STUDY:YM:wilson-carrier-transport
workhouse verify --only "Wilson complete finite configuration sum"
workhouse verify --only "Wilson activated-block majorant"
```

The exact suite is [wilson_marked.py](../../src/workhouse/invariants/wilson_marked.py). The [validation record](../../docs/validation/wilson-marked-2026-09-08.json) records the final verification results and open obligations.
