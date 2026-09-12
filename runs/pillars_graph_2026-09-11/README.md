# Review-derived spectral budgets and preserved Gemini intake

The Gemini synthesis and first Codex review are retained verbatim under
received/. Their absolute paths and local links describe the historical
workstation context, not portable instructions. The earlier 611/611 and 13/13
receipts apply to b9651be, not to this integration.

The maintained [derivation](../../docs/derivations/review-derived-spectral-budgets.md)
corrects Q4 and proves a finite-family, time-amplified extension of MT4.
The [registered controls](../../src/workhouse/invariants/spectral_budgets.py)
can be rerun with workhouse verify --only multichannel and --only "assembled Q4".
[Independent tests](../../tests/test_spectral_budgets.py) optimize a separate
piecewise-linear envelope, including invalid-hypothesis and zero-rate examples.

The [task record](../../graph-tasks/2026-09-11-pillars-graph.md) retains
graph and execution provenance. The original review's G18/SC17 corrections
remain scoped source review; they are not new physical-construction proofs.
New statements and actual dependencies are in the native theory graph.
