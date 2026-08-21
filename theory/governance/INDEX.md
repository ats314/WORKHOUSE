# INDEX — tree map + topic router

**Rebuilt and refreshed August 20, 2026** against the actual filesystem after the reorganization and v4.3 corpus promotion (DECISIONS #012 and #016). The June 15 version is byte-preserved at `records/governance_archive/INDEX_2026-06-15_ORIGINAL.md`.

Use this whenever you are unsure **where something is** or **where something belongs**. If you cannot place a file from this document, that is a gap in this document.

---

## 1. The tree

```
ALL THEORY/
├── README.md CLAUDE.md INDEX.md STATE.md SOURCES.md DECISIONS.md
│   NAMING_CONVENTION.md      how every filename is structured — read before adding files
│
├── corpus/                    ** SCIENTIFIC AUTHORITY — read first **
│     MASTER_THEORY_UNIFIED_2026-08-20_v4_3.md                 scientific + status authority
│     GLUEBALL_DETAILED_FORMULA_DOCUMENT_2026-08-20_v3_1.md   coefficient-level technical appendix
│     GLUEBALL_SOURCE_CONSOLIDATION_GUIDE_2026-08-20_v4_3.md  navigation / return guide
│     GLUEBALL_CANONICAL_SOURCE_MANIFEST_2026-08-20_v4_3.csv  byte-level provenance record
│
├── export/                    frozen handoff to github.com/ats314/WORKHOUSE
│
├── theory/                    the mathematical object
│   ├── DOC_GOV_open_problems.md       the live problem list
│   ├── DOC_GOV_proof_chain.md         proof map P01–P20 (legacy Clay chain = provenance only)
│   ├── DOC_GOV_chain_status_map.md    citation-safety layer  ← consult before quoting archive docs
│   ├── DOC_GOV_conventions.md         metric conventions, Mode A/B, citable-constants table
│   ├── conjectures/           CONJ_A–D, CONJ_IR
│   ├── theorems/              standalone theorem statements (8)
│   ├── notes/                 mathematical notes not yet promoted (15)
│   └── under_review/          PROOF_13/14/15 — recovered, NOT validated
│
├── programs/                  active campaigns
│   ├── hodge_o4_adjudication/   ** LIVE FRONT ** notebooks/ src/ data/
│   ├── one_plaquette/           flat-band spectroscopy — see its PLAN_Y6_program_index.md
│   ├── y4_allrank/              Y4 stage0→stage3h symbolic pipeline — src/ data/
│   ├── hodge_haar_krylov/       Haar-electric resolvent / Krylov / Feshbach line
│   ├── op1_defect_sparsity/     Birman–Schwinger defect sparsity (M1–M2 done; (S) open)
│   ├── pmbsf/                   analytic sparsity (Lemma Q / Z.A + Z.B)
│   └── rooted_capacity_program/ rooted projected-capacity source stability
│
├── numerics/                  engines + data that re-verify claims
│   ├── engines/  notebooks/  certificates/  results/  data/
│   ├── op12_theta/            θ-scan, kernel constants, M2 pair certificates, MC states
│   ├── clay_verify/  cw_extractor/  scratch_tmp/
│
├── papers/                    manuscripts in flight
│   ├── flat_band/                        v1.1 current
│   ├── gauge_constrained_spectral_geometry/  v1.4 current
│   ├── source_docx/  pmbsf_su2/  pmbsf_su3/
│
├── literature/                external papers + novelty/priors checks
│
├── records/                   append-only history
│   ├── SESSION_LOG.md         the one running log
│   ├── review/                REVIEW_LEDGER + findings F001–F043
│   ├── audits/                the 00–10 audit series, docx render audit, review reports
│   ├── runs/                  raw .log files from executions
│   ├── transcripts/           session + run transcripts (incl. the 15-hour run)
│   ├── governance_archive/    June 15 originals, byte-preserved + MD5
│   ├── REORG_MANIFEST_2026-08-20.tsv       every Aug-20 move, with MD5
│   ├── REORG_PLAN_2026-08-20_PREMOVE.tsv   the plan as computed before execution
│   └── CORPUS_PROMOTION_2026-08-20_V43.tsv v3→v4.3 promotion ledger
│
├── archive/                   bulk material
│   ├── zips/                  68 release/source bundles
│   ├── simulations/           SU(2)/q-6j/TRG experiment archive (322 files)
│   ├── bundles/               pentagonal_verification, SU5_COMPLETE_FOURTH_ORDER
│   └── MAN_FLUX_manifest.md            Y4 Final Archive manifest
│
├── GITHUB/                    flat mirror for upload — regenerated, not authored
│   ├── _READ_ME_FIRST.md      briefing for the agent who reorganizes the upload
│   └── _MANIFEST.tsv          flat name → original path, class, topic, md5, title
│
└── QUARANTINE/                moved out — nothing deleted
    ├── RESTORE_MANIFEST.tsv   quarantined path → original path, reason, size, MD5
    ├── unrelated/             not mathematics (installers, game assets, IECC docx, …)
    ├── duplicates_exact/      byte-identical copies; canonical retained in-tree
    ├── superseded/            older versions of documents whose successor is in-tree
    └── process_docs/          retired agent-process docs (CHARTER, GUARDRAILS, AGENT_PROTOCOL)
```

The three prefixed v3 authority predecessors are retained in `QUARANTINE/superseded/`; their original locations, sizes, and MD5 values are recorded in `QUARANTINE/RESTORE_MANIFEST.tsv`.

---

## 2. Topic → location router

| If you want… | Go to |
|---|---|
| **The current scientific statement of the whole program** | `corpus/MASTER_THEORY_UNIFIED_2026-08-20_v4_3.md` |
| A specific coefficient, stencil weight, or polynomial | `corpus/GLUEBALL_DETAILED_FORMULA_DOCUMENT_2026-08-20_v3_1.md` (`P₁₇` is in its Appendix A) |
| Which archived file a number came from | `corpus/GLUEBALL_CANONICAL_SOURCE_MANIFEST_2026-08-20_v4_3.csv` |
| Where the exact local copy lives—or whether it is absent by hash | `records/MAN_GOV_all_theory_local_path_index_v4_3.csv` |
| **Whether a claim may be cited, and at what status** | `theory/DOC_GOV_chain_status_map.md`, then corpus §13 ledger |
| The `u` vs `β_lat` vs `Y` vs `β_loc` normalization | `theory/DOC_GOV_conventions.md` + corpus §2 + errata §14 |
| The open problem list | `theory/DOC_GOV_open_problems.md` |
| **The fourth-order `C⁽⁴⁾` dispute** (the live front) | corpus §7 and §10; runs in `programs/hodge_o4_adjudication/` |
| The eleven freeze conditions for the decisive run | corpus §15.1 / detailed doc §18.1 |
| Incidence factorization, Betti counts, `dim ker ∂₂` | corpus §3; `theory/theorems/THM_FLUX_centered_double_incidence_theorem_2026-08-08.md` |
| The all-rank second-order law `t_N` | corpus §4.1 |
| The SU(3) `O(u³)` factorization | corpus §4.3 |
| The generalized Hodge pencil `Q₄φ = λ₄Gφ` | corpus §5.2 |
| The historical 189-record kernel, α/β, 25-point stencil | corpus §6 |
| The all-rank family `α_N`, `β_N`, `P₁₇`, `R₂₀` | corpus §8 + appendix A |
| Temporal histories / linked-cluster discipline | corpus §9; `theory/notes/THM_FLUX_hodge_cellular_circuit_mobility_theorem.md` |
| The exact isotropic pentagonal fourth-order cap hop | corpus §9.3; `archive/zips/pentagonal_o4_dual_cold_verification_bundle.zip` |
| The pentagonal O4 raw frontier and falsified zero backend | corpus §9.4; `numerics/engines/ENGINE_PENT_pentagonal_o4_minimal_representation_frontier.py` and `ENGINE_FLUX_audit_stranded_zero_backend.py` |
| The pentagonal direct O5 fraction and why it is not a theorem | corpus §9.5; `records/transcripts/pentagonal_prism_O5_decisive_resolvent_results.txt` — **prose-only** |
| The improved charge-odd source `O₃^imp` | corpus §10.1 |
| Monte Carlo record (`CERT_O4_next14.json`), σ, `aM(T₁⁺⁻)` | corpus §10.2; `programs/hodge_o4_adjudication/data/CERT_O4_next14.json` |
| The weak-well / local class-Hamiltonian gap | corpus §10.3 |
| Fifth order, string tension, `m₆` | corpus §11; `programs/one_plaquette/su3_y5_fifth_order/`, `su3_y6_m6/` |
| The infinite-volume / continuum firewall | corpus §12 (read before any continuum claim) |
| The flat-band manuscript | `papers/flat_band/PAPER_FLUX_glueball_flat_band_v1_1.tex/.pdf` |
| The unified spectral-geometry manuscript | `papers/gauge_constrained_spectral_geometry/` (v1.4) |
| Birman–Schwinger / OP-1 / lemma (S) | `programs/op1_defect_sparsity/`, `numerics/op12_theta/` |
| PMBSF / Lemma Q | `programs/pmbsf/`, `papers/pmbsf_su2/`, `papers/pmbsf_su3/` |
| Rooted projected capacity | `programs/rooted_capacity_program/` |
| A raw run log or a session transcript | `records/runs/`, `records/transcripts/` |
| The 15-hour August run (controls the numerical adjudication) | `records/transcripts/15 hour RUN.txt` + `15 hour RUN. results.txt` |
| Where a file went in the Aug-20 reorganization | `records/REORG_MANIFEST_2026-08-20.tsv` |
| What changed in the v4.3 authority promotion | `records/CORPUS_PROMOTION_2026-08-20_V43.tsv`, DECISIONS #016 |
| Something you think was wrongly removed | `QUARANTINE/RESTORE_MANIFEST.tsv` |
| Material in the wider archive (E:\YANG etc.) | `SOURCES.md` |

---

## 3. Where new files go

| Kind of thing you just made | Put it in |
|---|---|
| A revision of an authority document | `corpus/` — and move the old one to `QUARANTINE/superseded/` |
| A theorem statement meant to be cited | `theory/theorems/` |
| A derivation not yet promoted | `theory/notes/` |
| Campaign work (code + its results together) | the matching `programs/<campaign>/` |
| A reusable engine or verifier script | `numerics/engines/` |
| A JSON certificate emitted by a gate | `numerics/certificates/` |
| A computed result write-up | `numerics/results/` |
| A notebook not tied to one campaign | `numerics/notebooks/` |
| Manuscript source | `papers/<manuscript>/` |
| A run log | `records/runs/` |
| A session/run transcript | `records/transcripts/` |
| An audit or review write-up | `records/audits/` (findings → `records/review/`) |
| A release bundle (.zip) | `archive/zips/` |
| **Anything at all** | **not the tree root** |


