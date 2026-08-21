<!-- THEORY root index. If you are lost, start here. Live status = STATE.md. Rules = CLAUDE.md. -->

# INDEX — the map of `C:\THEORY`

**What this file is:** the one place that tells you *where everything lives* in this working home and
*where to look* for a given topic. It is navigation only — no status claims live here.
For **status** read `STATE.md`; for **rules** read `CLAUDE.md` → `GUARDRAILS.md` → `AGENT_PROTOCOL.md`;
for **what this project is** read `CHARTER.md`.

> Maintenance rule (project rule "index as you go"): when you add, move, or retire a directory,
> update the matching row here and in the affected layer's `README.md`. Last built: 2026-06-15.

---

## 1. Root map — every top-level entry

| Entry | What it is |
|---|---|
| `CHARTER.md` | What THEORY is and is **not** (the north star; wins all conflicts). |
| `CLAUDE.md` | Agent rules, layout, working conventions. Read after CHARTER. |
| `GUARDRAILS.md` | Anti-patterns learned the hard way. |
| `AGENT_PROTOCOL.md` | How to run one session; the claim-tier (T1/T2/T3) definitions. |
| `STATE.md` | **Living status — single source of truth.** Reverse-chronological; newest entry = current. |
| `INDEX.md` | This file — the tree map + topic router. |
| `SOURCES.md` | Map into the big read-only archives (`E:\YANG`, the other drives). |
| `DECISIONS.md` | Numbered log of *why* things are the way they are. |
| `theory/` | **Layer 1 — the mathematical object:** proof chain, open problems, conjectures, citation-safety maps. |
| `programs/` | **Layer 2 — active campaigns,** each with its own README/milestones. |
| `numerics/` | **Layer 3 — engines + data** that re-verify the computational claims. |
| `papers/` | **Layer 4 — manuscripts in flight.** |
| `records/` | **Layer 5 — the running log + the review campaign** (findings F001–F043). |
| `ZIP ARCHIVES/` | Release/source bundles (`.zip`) — the deliverable drop; also a user mount. Not a code layer. |
| `_QUARANTINE_DELETE_ME_2026-06-14/` | Inert cruft (pyc caches, verified-duplicate strays). Safe to delete; `rm` is blocked on this mount so it is parked here. |

---

## 2. The five layers in detail

### `theory/` — the mathematical object
| Path | Purpose |
|---|---|
| `DOC_GOV_open_problems.md` | **The only live problem list.** |
| `DOC_GOV_proof_chain.md` | Live copy of the proof map (P01–P20 + Clay chain). |
| `DOC_GOV_chain_status_map.md` | **Citation safety:** which archive docs may be quoted, through which review filter. Read before citing anything. |
| `DOC_GOV_conventions.md` | Metric conventions, Mode A/B bookkeeping, the citable-constants table (the factor-2 trap). |
| `conjectures/` | Canonical statements: CONJ_A (log-forest UV), CONJ_B (anomaly source — the bottleneck), CONJ_C, CONJ_D, CONJ_IR. |
| `under_review/` | **QUARANTINE — recovered, NOT validated, NOT citable:** PROOF_13/14/15. |

### `programs/` — active campaigns
| Path | Purpose | Sub-index |
|---|---|---|
| `op1_defect_sparsity/` | **Lead result.** Birman–Schwinger uniform θ<1; deterministic side solved (M1/M2), stochastic sparsity lemma (S) is the open piece. | `PLAN_OP1_unif_closure.md` |
| `one_plaquette/` | Flat-band glueball spectroscopy; rest-mass series q₂…m₆, string tension σ₂…σ₆, band-shape theorem. | **`PLAN_Y6_program_index.md` (authoritative file map — read first)** |
| `pmbsf/` | Projected Maxwell Birman–Schwinger Firewall (analytic sparsity; Lemma Q / Z.A+Z.B). | its `README.md` |
| `rooted_capacity_program/` | Rooted projected-capacity / source-stability line. | its `README.md` |

`op1_defect_sparsity/` subdirs: `defect_gas_docs/` (WILSON-era ancestry), `za_cap_geometry/` (Z.A LCI cap geometry), `farsource_gpu/` (open Z.B far-source decay engine), `red_davies_toolkit/` (precision extracts).

`one_plaquette/` subdirs: `su3_y5_fifth_order/` (q₅), `su3_y6_m6/` (m₆ pipeline), `y4_o3_flatband_verification/` (q₄ / 189-record H₄ kernel — *relocated from root 2026-06-15*), `lattice_glueball_data/` (real-world lattice comparison — *relocated from root 2026-06-15*), `su3_string_tension_native_o5/` (σ₂–σ₅ native), `su3_string_tension/` (σ through O(y⁶)), `sun_band_shape/` (SU(N) 4th-order band-shape theorem), `su3_o5_consolidated_y6/`, `shell6_o2/`, `tromino_o3/`, `glueball_mass_prediction/`.

### `numerics/` — engines + data
| Path | Purpose |
|---|---|
| `op12_theta/` | The OP-12 θ-scan: exact kernel constants (M1), pair certificates (M2 in `m2_certificates/`), scaling tables (`m4_scaling/`), the (S) chessboard engine (`s_chessboard/`), MC states, per-config results. |
| `clay_verify/` | The Clay submission's CODE/VERIFY scripts, run and recorded (archive working copies). |
| `cw_extractor/` | Recovered authoring notebook for the c_W constant. |

### `papers/` — manuscripts in flight
| Path | Purpose |
|---|---|
| `flat_band/` | Flat-band glueball paper — **v1.1 current** (27 pp). |
| `pmbsf_su2/` | Pointer to the SU(2) conditional-firewall manuscript (lives in `programs/pmbsf/`). |
| `pmbsf_su3/` | Pointer to the SU(3)/SU(N) paper line (lives in `programs/pmbsf/`). |

### `records/` — log + review
| Path | Purpose |
|---|---|
| `SESSION_LOG.md` | **The one running log** — one entry per pass. |
| `review/REVIEW_LEDGER.md` | **The index of findings** — one row per Fnnn. |
| `review/findings/` | `F001`–`F043`, one file per finding. |
| `review/manifests/` | MD5 manifests of external stores at survey time. |

---

## 3. Topic → where to look

| If you want… | Go to |
|---|---|
| Current status / what's proven, conditional, open | `STATE.md` (newest entry) + `theory/DOC_GOV_open_problems.md` |
| Whether a result may be cited, and how | `theory/DOC_GOV_chain_status_map.md` |
| A constant's value / metric convention | `theory/DOC_GOV_conventions.md`; one-plaquette values: `programs/one_plaquette/PLAN_Y6_program_index.md` §1 |
| The lead result (uniform Birman–Schwinger θ<1) | `programs/op1_defect_sparsity/PLAN_OP1_unif_closure.md` |
| θ-scan numbers, kernel constants, M2 certificates | `numerics/op12_theta/` |
| The open sparsity lemma (S) / chessboard route | `numerics/op12_theta/s_chessboard/` + `programs/op1_defect_sparsity/NOTE_FLUX_s_chessboard_route_2026-06-12.md` |
| Glueball rest-mass coefficients q₄ / q₅ / m₆ | `programs/one_plaquette/{y4_o3_flatband_verification, su3_y5_fifth_order, su3_y6_m6}/`; values in `PLAN_Y6_program_index.md` §1 |
| String tension σ₂…σ₆ | `programs/one_plaquette/{su3_string_tension_native_o5, su3_string_tension}/` |
| SU(N) band-shape theorem | `programs/one_plaquette/sun_band_shape/` |
| Lattice-QCD comparison / real-world glueball data | `programs/one_plaquette/lattice_glueball_data/` |
| The flat-band manuscript | `papers/flat_band/` (v1.1) |
| The PMBSF firewall program / its papers | `programs/pmbsf/`; `papers/pmbsf_su2/`, `papers/pmbsf_su3/` |
| Proof chain P01–P20 / conjectures | `theory/DOC_GOV_proof_chain.md`; `theory/conjectures/` |
| A specific review finding (F0nn) | `records/review/REVIEW_LEDGER.md` → `records/review/findings/F0nn_*.md` |
| What happened in a past session | `records/SESSION_LOG.md` |
| Where something lives in the big archive | `SOURCES.md` |
| Why a decision was made | `DECISIONS.md` |

---

## 4. Sub-indexes (don't duplicate — point)

- **One-plaquette program:** `programs/one_plaquette/PLAN_Y6_program_index.md` — every file across Downloads / ZIP ARCHIVES / THEORY, canonical results, pipeline stages, release version-chains, known-missing list.
- **Review campaign:** `records/review/REVIEW_LEDGER.md` is the findings index (no second index is kept).
- **Archive map:** `SOURCES.md` routes into `E:\YANG` (≈8,100 organized files + 43K-file proof workspace) and the other drives.
