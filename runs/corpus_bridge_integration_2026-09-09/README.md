# Full-root corpus bridge into the canonical checkout

This September 9 integration connects the preserved September 7 full-root audit to the current `REPO` checkout. It adds the exact [12,108-content notes manifest](../../notes/WORKHOUSE_FULL_2026-09-07.jsonl), [coverage verifier](../../scripts/verify_full_corpus_coverage.py), [scope document](../../docs/corpus_coverage.md), and archive declaration. The older [audit run](../full_corpus_coverage_2026-09-07/README.md) remains byte-identical to its source.

All 265 preexisting review verdicts and reasons remain unchanged. The notes queue reuses reviews only for an identical content digest, preserving the original archive/verdict/scope. The full-root queue has 0 own reviews, 229 reused scoped reviews and 11,879 pending contents. A renamed exact copy can reuse a review; a changed file with the same name, even if indexed, remains pending.

## Preserved provenance and fresh verification

- [SOURCE_MANIFEST.json](SOURCE_MANIFEST.json) records original source paths, bytes and SHA-256 digests: 73 frozen-run files, four active copies and five preserved source/baseline files.
- [NOTES_MERGE.json](NOTES_MERGE.json) records the three-way review for `notes.py`, its tests and intake README. GitHub and the common ancestor agree on these files; the source-only change was brought across without dropping remote behavior. Before-edit GitHub working files also remain in `C:/WORKHOUSE/navigation/reconciliation/2026-09-09/github-snapshot`.
- [COLLECTION_MATRIX.json](COLLECTION_MATRIX.json) holds the existing navigation/corpus metadata join, verified local entry paths, source-input hashes and bounded next queues. It is a snapshot, not a fresh recursive scan. The navigation snapshot predates `REPO` creation.
- [VALIDATION.json](VALIDATION.json) records fresh portable coverage replay, current thirty-six duplicate-pair hash checks, focused regressions and unchanged original review records. No full mathematical collector or Lean build was run for this intake.
- `SHA256SUMS` pins every nested file in this package, except the checksum file itself.

From the repository root, replay the frozen eligible content/path union without mounting the corpus:

```powershell
python scripts/verify_full_corpus_coverage.py --manifest notes/WORKHOUSE_FULL_2026-09-07.jsonl --run runs/full_corpus_coverage_2026-09-07
python -m pytest tests/test_full_corpus_coverage.py tests/test_notes.py
```

To additionally check the thirty-six historical retained/quarantine byte pairs, append `--workspace-root C:/WORKHOUSE` to the verifier command. This is a read-only check, not a request to repeat the old moves. Original corpus documents, full extracted text and original worktrees remain local and intact.

## Collection roles and finite next queues

`C:/WORKHOUSE` is the encompassing historical research workspace. `REPO` is the current executable verifier checkout. `ALL THEORY` is a separate source collection retaining an earlier checkout. The numbered collections, publication bundles, standalone projects, simulation families and dated campaigns keep their original identities. `organized_pdfs` and `organized_proofs` are intentional recovery redirects, and `quarantine` records provenance rather than scientific rejection.

The matrix distinguishes September 9 path counts from September 7 distinct eligible loose-content hashes. Copies count as separate paths but not separate scientific origins; per-area hash sets overlap and must not be summed. An older source's local filesystem timestamp is not its scientific date. The [current research map](../../docs/current_research.md), result register and `workhouse why <id>` establish the live route before a new source review.

1. Recover and compare the five SHA-identified denominator/CRT Lean files (three modules, two wrappers), compile with the current toolchain and audit axioms. Existing full source reads and integer checks are historical records; they are not a new T0 result. Completeness of physical denominator lists remains a premise.
2. Read at most 150 new lines in each of seven specified synthesis files, using the recorded unread ranges. Across all nineteen syntheses the existing audit read 4,896 of 26,730 lines; it fully read two documents and partially read seventeen. New intake must retain the rest as pending.
3. Map four already identified original-source arguments to live results: smooth-proxy volume repair, deterministic action flow, tightness versus Cauchy, and the conditional continuum extension. Keep surviving mechanisms, failed steps and explicit hypotheses.
4. Resolve the next ten relevant exact source identities from the fifty-eight unresolved entries in the 148-row historical manifest audit. Ninety identities are already recovered. Search preserved metadata first.

The detailed local collection map is `C:/WORKHOUSE/navigation/reconciliation/2026-09-09/corpus_bridge.md`; its full structured content is pinned here in the matrix. The previous source reviews, findings and failed routes remain explicitly dated historical evidence. This operational bridge does not perform full semantic review or promote a mathematical claim.
