# export/ — the WORKHOUSE handoff layer

`ALL THEORY` is the **upstream corpus**. [github.com/ats314/WORKHOUSE](https://github.com/ats314/WORKHOUSE) is the downstream **machine verifier**: it re-derives the corpus's exact claims from their stated definitions and reports, mechanically, where a printed number and its own definition disagree. It does not restate the theory, and it is not a mirror of this tree.

This directory is the contract between the two.

## What is frozen

`MAN_GOV_export_manifest.csv` lists every corpus document that WORKHOUSE is entitled to consume, with its size, SHA-256, MD5, and freeze date.

| File | Role |
|---|---|
| `corpus/MASTER_THEORY_UNIFIED_2026-08-20_v3.md` | scientific and status authority |
| `corpus/GLUEBALL_DETAILED_FORMULA_DOCUMENT_2026-08-20_v3_1.md` | coefficient-level technical appendix |
| `corpus/GLUEBALL_SOURCE_CONSOLIDATION_GUIDE_2026-08-20_v3.md` | navigation and return guide |
| `corpus/GLUEBALL_CANONICAL_SOURCE_MANIFEST_2026-08-20_v3.csv` | byte-level provenance record |

The manifest holds hashes rather than copies. There is exactly one canonical body of each document, in `corpus/`; duplicating it here would recreate the version-drift problem this reorganization exists to end.

## Direction of flow

```
   ALL THEORY/corpus/   ──freeze──►   export/MAN_GOV_export_manifest.csv   ──consume──►   WORKHOUSE
        (authoring)                        (contract)                          (verification)

   WORKHOUSE findings  ──────────────────────────────────────────►  records/review/  +  STATE.md
```

One direction for documents, the other for verdicts. **WORKHOUSE never writes into `corpus/`**, and a WORKHOUSE finding does not silently change a claim's status here — it becomes a review finding, and `STATE.md` is updated by a human-directed pass.

## Verifying the contract

```bash
python -c "import hashlib,csv,os; [print(('OK ' if hashlib.sha256(open(os.path.join(r'C:\ALL THEORY',r['file'].replace('/',os.sep)),'rb').read()).hexdigest()==r['sha256'] else 'DRIFT ')+r['file']) for r in csv.DictReader(open(r'C:\ALL THEORY\export\MAN_GOV_export_manifest.csv',encoding='utf-8'))]"
```

A `DRIFT` line means a corpus document changed without the manifest being refreshed. **That is a bug, not a fact** — either the edit was unintended, or the freeze step was skipped. Resolve it before running WORKHOUSE against this tree, because WORKHOUSE's constants registry is keyed to the frozen content.

## Index tooling

- `DOC_GOV_index_design_2026-08-20.md` — design proposal for a claims index and retrieval layer over the corpus, with the measurements that motivate it and a GitHub build plan. Nothing beyond step 1 is built.
- `ENGINE_GOV_constant_index.py` — step 1, working. Builds the exact-rational index (174 distinct constants, 863 occurrences across 320 prose files) and lints for the 2×/4× signature shared by the `Y = 4u` label erratum and the factor-2 metric trap. `--check` is CI mode: it exits 1 on any unclassified pair.
- `CERT_GOV_constant_ratio_classifications.json` — the four currently-known 2×/4× relationships and why each is legitimate. Three are convention (real-space `β/4` vs symbol `β`; `τ₄` vs `2τ₄`); the fourth is a **symbol collision** — `κ` denotes `2a(n)` in the corpus and `a(n)` in flat-band manuscript v1.1. Neither document is wrong; anyone quoting across them would be.

```bash
python export/ENGINE_GOV_constant_index.py --check
```

## Publishing a revision

1. Write the new version into `corpus/` with an incremented version marker.
2. Move the superseded version to `QUARANTINE/superseded/`.
3. Regenerate `MAN_GOV_export_manifest.csv`.
4. Record the change in `STATE.md` and `records/SESSION_LOG.md` in the same pass.
5. Only then re-point WORKHOUSE.

## What WORKHOUSE is currently expected to find

The corpus does not claim internal consistency it has not earned. The known live discrepancy — and the thing a mechanical verifier should reproduce rather than smooth over — is the fourth-order off-axis coefficient `C⁽⁴⁾`: `C_old = −0.04808638318135875…` (exact, historical 189-record kernel) against `C_new = −0.020213328886166577` (numerical, August linked marked-cluster run), with the axial coefficient agreeing to numerical tolerance. **A verifier that reports these as reconciled is wrong.** See `corpus/` §7 and §10, and Appendix B on why no scalar shift closes the gap.
