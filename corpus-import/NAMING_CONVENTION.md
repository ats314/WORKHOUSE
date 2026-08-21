# NAMING CONVENTION

**Purpose: a filename should tell an agent what a file *is* before the file is opened.** `ls` and `grep` are the primary retrieval surface for a corpus this size, so every character in a name should carry information.

---

## 1. The pattern

```
CLASS_TOPIC_descriptor[_vN][_YYYY-MM-DD].ext
```

| Field | Case | Required | Meaning |
|---|---|---|---|
| `CLASS` | UPPER | yes | What kind of artifact this is. Closed vocabulary, §2. |
| `TOPIC` | UPPER | yes | Which program or object it belongs to. Closed vocabulary, §3. |
| `descriptor` | lower_snake | yes | What it says or does. Free text, 2–6 words. |
| `vN` | lower | no | Version. `v1`, `v2`, `v10a24c`. Use when a lineage exists. |
| `YYYY-MM-DD` | — | no | ISO date. Use for dated reports, runs, and audits. |

Parsing is unambiguous because `CLASS` and `TOPIC` are uppercase closed vocabularies and the descriptor is lowercase:

```
THM_O4_hodge_pencil_positivity_v2_2026-08-08.md
CERT_Y5_sigma5_exact_2026-06-14.json
ENGINE_Y4_stage3h_nonresonant_contraction.py
RUN_O4_marked_cluster_production_15h_2026-08-19.txt
PAPER_FLUX_flat_band_v1_1.tex
AUDIT_GOV_coupling_normalization_2026-06-14.md
DATA_SUN_glueball_jpc_benchmark_v2.csv
```

An agent gets four facts from `ls` alone, and these become real queries:

```bash
ls THM_*                 # every theorem statement
ls *_O4_*                # everything about the fourth-order adjudication
ls CERT_*_2026-08-*      # certificates emitted in August
ls PAPER_*               # manuscript sources
```

---

## 2. CLASS vocabulary

| CLASS | Use for |
|---|---|
| `DOC` | Governance and navigation: charters, indexes, READMEs, maps. |
| `THM` | A theorem statement meant to be cited. |
| `LEM` | A lemma, usually supporting a `THM`. |
| `NOTE` | A derivation or note not yet promoted to `THM`. |
| `PLAN` | A campaign plan, milestone ladder, or closure route. |
| `AUDIT` | An audit, review, reconciliation, or forensic report. |
| `CERT` | A machine-emitted certificate from a gate run. |
| `ENGINE` | A reusable computation or verification script. |
| `NB` | A notebook. |
| `RUN` | A run log or a session/run transcript. |
| `PAPER` | Manuscript source or output. |
| `DATA` | A data table, array, or figure. |
| `LIT` | External or third-party literature. |
| `IDX` | A generated index — regenerable, never hand-edited. |
| `MAN` | A manifest or provenance table. |

## 3. TOPIC vocabulary

| TOPIC | Use for |
|---|---|
| `FLUX` | The one-plaquette flux band generally. |
| `O2` `O3` `O4` `O5` `O6` | Order-specific work. `O4` is the live front. |
| `Y4` `Y5` `Y6` | The Y-order symbolic pipelines. |
| `SUN` | All-rank SU(N) results. |
| `SU2` `SU3` `SU4` `SU5` `SU6` | Rank-specific. |
| `OP1` | Birman–Schwinger defect sparsity. |
| `PMBSF` | The PMBSF / Lemma Q program. |
| `RCAP` | Rooted projected capacity. |
| `STRING` | String tension. |
| `SHELL6` | Shell-6 work. |
| `PENT` | The pentagonal-prism model. |
| `HAAR` | Haar-electric resolvent, Krylov, Feshbach. |
| `MC` | Monte Carlo. |
| `TROM` | Tromino. |
| `GOV` | Governance, process, meta. |
| `MISC` | Genuinely cross-cutting. Use sparingly — it carries no information. |

Add a TOPIC only when a real program exists for it, and record the addition here.

---

## 4. Character rules

Always, without exception:

- **ASCII only.** No en-dashes, em-dashes, or smart quotes. `HODGE–HAAR` (en-dash) is not `HODGE-HAAR`.
- **No spaces.** Use `_`.
- **No shell- or URL-hostile characters:** `# = ( ) { } [ ] , ' " ! $ & ; : @ + ~ \` ^ %`. A name containing `=` or `#` breaks shell globs, URLs, and some Git tooling.
- **No leading punctuation.** A leading `_` or `#` sorts unpredictably and hides files on some systems.
- **Lowercase extensions.** `.md` not `.MD`.
- **ISO dates only.** `2026-08-20`, never `20260820` or `Aug20`.
- **No `(1)` copy suffixes.** If a variant genuinely differs, name the difference (`_alt`, `_fixed`, `_resume`). If it does not differ, it is a duplicate and belongs in `QUARANTINE/duplicates_exact/`.
- **Under 80 characters** including the extension.

---

## 5. What the filename does NOT carry

**Status.** No `_PROVEN`, `_DISPUTED`, `_OPEN` suffixes, deliberately. Status changes — the fourth-order kernel went from "exact" to "disputed" without a single byte of the historical kernel changing — and a status baked into a filename goes stale silently while looking authoritative. That is the same failure mode as the "PROVEN" banners this corpus already has a documented problem with.

Status lives in `STATE.md`, the `corpus/` evidence ledger, and `theory/DOC_GOV_chain_status_map.md`. One source of truth.

The one exception is location, not naming: material under `QUARANTINE/superseded/` is superseded by virtue of where it sits.

---

## 6. Exemptions — files that must NOT be renamed

Renaming is not free here. A survey of the live tree found **756 of 982 files referenced by name, across 12,229 mentions**, so a name is often an identifier rather than a label.

**Never rename:**

1. **Python files imported as modules.** Seventeen are import targets (`su3_moments_ext`, `su3_domino_d3`, `shell6_o2_engine2`, `lci_typicality_diagnostic`, `fast_haar`, `link_o2_v2`, `su2hb_f041`, `su3_haar_tromino_primitives`, and others). `import ENGINE_FLUX_su3_moments_ext` breaks the moment the file moves.
2. **Any file named inside a certificate.** A certificate recording that `ENGINE_FLUX_su3_domino_d3.py` produced it is a *historical fact*. Renaming the script and rewriting the certificate makes the certificate lie about what ran. Provenance outranks tidiness.
3. **Governance files at the tree root.** `CLAUDE.md`, `README.md`, `INDEX.md`, `STATE.md`, `SOURCES.md`, `DECISIONS.md`, this file. Tools and agents expect these names.
4. **`corpus/` documents.** Their SHA-256 hashes are pinned in `export/MAN_GOV_export_manifest.csv` and consumed downstream by WORKHOUSE. Renaming requires a coordinated re-freeze.
5. **Anything under `QUARANTINE/` or `records/`.** Both are append-only history; the names are part of the record.

For exempt code, the information an agent needs lives in a generated map rather than in the filename.

---

## 7. Applying it

**New files:** use the convention from the start.

**Existing files:** three tiers, by whether the name is a label or an identifier.

| Tier | Applies to | Action |
|---|---|---|
| **A — full rename** | Documents in `theory/`, `papers/`, `literature/`, `programs/**/*.md` | Rename to `CLASS_TOPIC_descriptor`. References rewritten mechanically in the same pass. |
| **B — sanitize only** | Notebooks, logs, data, figures | Fix character rules and copy suffixes. Leave the descriptive stem alone. |
| **C — exempt** | Everything in §6 | Leave the name. Carry the metadata in a generated map instead. |

Every rename is recorded with old path, new path, size, and MD5, so the operation is reversible from the manifest.
