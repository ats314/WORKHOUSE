# Three-folder source review and graph integration

This September 10 intake covers every file in the requested archived
`docs/derivations`, `docs/research` and `docs/validation` folders. The starting
GitHub main revision was `42b0762e4ce382efa153a969e8bb44bb77537844`.
The original folders remain unchanged.

| Requested folder | Files | Intake comparison with GitHub main |
| --- | ---: | --- |
| derivations | 42 | 41 identical; one maintained SC17 successor |
| research | 3 | two identical; one maintained U7 source-status correction |
| validation | 69 | 39 identical; 30 differing only by line endings |
| Total | 114 | Every file was already tracked; 36 validation logs lacked direct citation nodes |

The [independent source census](source_inventory.json) and
[reviewed inventory](inventory.json) account for all 2,020,424 received bytes.
The complete [source snapshot](sources/docs/) retains exact archive bytes,
including failed runs and earlier versions. Line-ending equivalence is recorded
separately from byte identity. The two maintained successors stay in the live
documentation; their archive predecessors are preserved here.

## What was extracted and connected

- Six analytic results now have stable RESULT identities: common-space
  contractive map/observable drift, projective-source martingale convergence,
  reverse-martingale blocking, predictable source drift with conditional
  variance control, uniform marked clustering, and full source/complement
  spectral-window completeness. Their hypotheses and source sections are
  recorded in [the result ledger](../../ledger/results.yaml).
- Eighteen nested input sources connect to their byte-identical canonical
  sources and existing analytic results. Existing results are reused, with
  the new complete-window theorem extracted separately.
- All 36 previously unaliased TXT/XML execution artifacts receive native
  citation nodes with historical outcomes and scoped source links. Failed
  reports and their later successful retries remain distinguishable.
- Three stale G14/G22/U3 interpretations and the G14 support route are
  corrected against existing checked results. Original interpretations remain
  in explicit historical fields. The actual fourth-order support replaces
  the falsified R-degree-only dependency; no gap state is changed by intake.

Detailed source reviews are in [derivations](derivations_review.md),
[research](research_review.md) and [validation](validation_review.md), with
corresponding JSON records. They inspect statements, proof interfaces,
hypotheses, finite controls, historical outcomes and existing formal coverage.
They are not a fresh independent reconstruction of every analytic proof.
The original source authors' work and prior checks retain their provenance;
the contributions of this intake are extraction, scoped review and routing.

## Verification and application boundary

```text
uv run --no-sync python scripts/verify_folder_evidence.py
uv run --no-sync workhouse why RESULT:COMMON_SPACE_CONTRACTIVE_DRIFT
uv run --no-sync workhouse why RESULT:PROJECTIVE_SOURCE_MARTINGALE
uv run --no-sync workhouse why RESULT:SOURCE_COMPLEMENT_COMPLETE_WINDOW
uv run --no-sync workhouse verify
```

The first command checks exact received bytes, independent census coverage,
scoped dispositions and generated graph connections. Tests reject omitted
sources, duplicate rows, changed hashes, missing citations, missing claim
edges and absent scope. These are provenance/retrieval checks, not an extra
mathematical verification tier. The six extracted results are `proven` with
`analytic` evidence and remain T3 for machine certification. No new Lean
theorem or actual Wilson cross-cutoff realization is asserted by this intake.

The source/complement criterion requires the bound on the **entire**
complement. Convergence criteria require actual common spaces or laws,
normalized observables, and the specified drift/variance bounds. Marked
clustering requires the stated physical norm and source normalization.
Supplying these hypotheses for a continuum Wilson trajectory remains distinct
from having proved the reusable criteria.

Fresh execution details are in [local_validation.json](local_validation.json):
562/562 mathematical checks passed. The full regression collection plus an
exact rerun of the 181 cases affected by a missing temporary-directory parent
accounts for 1,347 passes and one Windows symlink skip out of 1,348 cases.
Both the initial error report and corrected rerun are retained. The earlier
[integration checkpoint](validation.json) records its then-pending work;
GitHub CI and merge status are recorded by the publishing pull request.
The [PR 119 reconciliation](reconciliation_pr119.json) records the subsequent
literature-only upstream merge and regeneration of the combined graph. It
preserves both integrations and does not alter the requested source snapshots.
`SHA256SUMS` pins this run. Maintained navigation was preserved separately
under the workstation's `navigation/preserved/2026-09-10-folder-evidence-integration/`;
those navigation backups are not scientific evidence.
