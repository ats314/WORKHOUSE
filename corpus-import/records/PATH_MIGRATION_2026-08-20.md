# PATH MIGRATION — August 20, 2026

Older documents in this tree, and every document in the read-only archives, refer to paths that changed in the reorganization (DECISIONS #012). This page resolves them.

**Historical documents were deliberately *not* rewritten.** `records/SESSION_LOG.md`, `records/STATE_ARCHIVE_2026-06-15.md`, `records/review/findings/`, the `DECISIONS.md` entries, and everything under `records/governance_archive/` and `QUARANTINE/` are append-only history; silently editing them would destroy the provenance they exist to preserve. Live navigation documents (`CHARTER`, `GUARDRAILS`, `AGENT_PROTOCOL`, `SOURCES`, the `programs/` and `papers/` READMEs, `PLAN_Y6_program_index.md`) **were** updated in place — 18 references across 12 files.

`corpus/` documents were **not touched at all**: they are the frozen authority consumed by WORKHOUSE, and their hashes are pinned in `export/MAN_GOV_export_manifest.csv`.

## The moves

| Old path | New path |
|---|---|
| `C:\THEORY\` | `C:\ALL THEORY\` |
| `ZIP ARCHIVES/` | `archive/zips/` |
| `SIMULATIONS/` | `archive/simulations/` |
| `pentagonal_verification_bundle/` | `archive/bundles/pentagonal_verification_bundle/` |
| `SU5_COMPLETE_FOURTH_ORDER_BUNDLE/` | `archive/bundles/SU5_COMPLETE_FOURTH_ORDER_BUNDLE/` |
| `_audit_su_n_docx_af3a56e7/` | `records/audits/su_n_docx_render_audit/` |
| `tmp/` | `numerics/scratch_tmp/` |
| `<root>/*.ipynb` | `numerics/notebooks/` or the owning `programs/` campaign |
| `<root>/*.py` | `numerics/engines/` or the owning `programs/` campaign |
| `<root>/*.json` | `numerics/certificates/` or the owning campaign's `data/` |
| `<root>/*.zip` | `archive/zips/` |
| `<root>/*.log` | `records/runs/` |
| `<root>/*.txt` (transcripts) | `records/transcripts/` |
| `<root>/*.pdf` (third-party) | `literature/` |
| `<root>/*.docx` | `papers/source_docx/` |
| `<root>/Hodge_v10a*`, `Hodge_O4_*`, `*MarkedCluster*` | `programs/hodge_o4_adjudication/` |
| `<root>/y4_stage*`, `y4_sun_*`, `y4_su[46]*` | `programs/y4_allrank/` |
| `<root>/Hodge_Haar*`, `*Krylov*`, `*Feshbach*` | `programs/hodge_haar_krylov/` |
| `<root>/AGENTS.md` | `QUARANTINE/unrelated/` — orphaned, misleading; see `QUARANTINE/README.md` |
| `<root>/README.md` (Y6 Stage-0 package readme) | `records/audits/README_Y6_STAGE0_external_memory_pipeline.md` |

## Resolving any individual file

Every one of the 621 moves is recorded with its original path, new path, reason, size, and MD5:

```bash
grep -i "<filename>" "C:/ALL THEORY/records/REORG_MANIFEST_2026-08-20.tsv"
```

For something that was moved *out* of the tree:

```bash
grep -i "<filename>" "C:/ALL THEORY/QUARANTINE/RESTORE_MANIFEST.tsv"
```

The plan as computed before execution is preserved separately at `records/REORG_PLAN_2026-08-20_PREMOVE.tsv`, so the intended and actual outcomes can be compared.

## Caveat

Notebooks and scripts that hard-code absolute paths were **not** edited — only documents were. A `programs/` or `numerics/` script that opens `C:\THEORY\...` or a bare relative path from the old root will fail until its path is updated. Fix those as you encounter them, in the pass that encounters them.
