# SU(3) one-plaquette / glueball / Y6–m₆ / string-tension — MASTER FILE INDEX

**Authoritative map of where every file in this program lives, what it is, and its status.**
Maintained by the lead agent; update it whenever files are added/moved (project rule: index as you go).
Last built: 2026-06-15. Convention everywhere: `u = β/6 = 1/g_H⁴`.

## 0. Drive map (where to look)

| Location | Role |
|---|---|
| `C:\Users\Alex\Downloads` | **LIVE / newest.** Working area; the most recent versions land here first (e.g. m₆ driver V4). Search here FIRST. |
| `C:\ALL THEORY\programs\one_plaquette\` | Distilled working copies + this-session deposits (`su3_y6_m6`, `su3_string_tension_native_o5`, `sun_band_shape`, `su3_o5_consolidated_y6`, …). |
| `C:\ALL THEORY\ZIP ARCHIVES\` and the `ZIP ARCHIVES` mount | Archived bundles (releases, source zips). |
| `C:\ALL THEORY\papers\flat_band\` | The manuscript (`PAPER_FLUX_glueball_flat_band_v1_1.tex/.pdf`) + figures. |
| `E:\YANG`, `E:\…` | Archive-of-record (read-only). |

## 1. Canonical results (coefficient → value → authoritative file → status)

Rest-mass series `m₁₊₋(u) = 8/3 + u + (11/306)u² − (109151/249696)u³ + q₄u⁴ + q₅u⁵ + m₆u⁶ + O(u⁷)`:

| coeff | value | authoritative file | status |
|---|---|---|---|
| O(u²) | 11/306 | paper §5; `ENGINE_FLUX_glueball_band_certificate_v2.py` | PROVEN |
| O(u³) | −109151/249696 | paper §6 | PROVEN |
| q₄ | −20721577909065127111/7250590288602460800 | `y4_extracted_sources/stage3j.py` → 189-kernel | EXACT (reproduced from scratch this session) |
| q₅ | −866236750503342026253096691057/1169668083793811403447133488000 | `su3_y5_fifth_order/`; `SU3_Y5_M5_COMPLETE_*` | EXACT |
| **m₆** | −156998370765216917515896262601525405897211506214753116643443873 / 4880681791275629050759264798095652027950878794719744000000 (≈ −32167.30) | `SU3_Y6_M6_EXACT_INTERNAL_V1_RELEASE.zip` → `certificates/Y6_M6_EXACT_CERTIFICATE.json` | **PROVISIONAL** (exact-internal; color+fold primitives independently verified; order-6 census not independently re-derived) |

String tension `σ(u) = 2/3 − (22/153)u² − (61/408)u³ − …` (bridge σ=½W(2u)):

| coeff | value | authoritative file | status |
|---|---|---|---|
| σ₂ | −22/153 | `su3_string_tension_native_o5/` (`ENGINE_STRING_su3_torelon.py`) | EXACT (rational) |
| σ₃ | 61/408 | same | EXACT (rational, determinant sector) |
| σ₄ | −737327120374220449/7250590288602460800 | `su3_string_tension_native_o5/ftw.py` | EXACT (mod-p, 3 primes) |
| σ₅ | 137767222189182735950309/2009803206414863779920000 | `su3_string_tension_native_o5/{ftw.py, CERT_STRING_sigma5_exact_certificate.json}` | EXACT (7-prime CRT reconstruction, this session) |
| σ₆ | (KPS table value) | `su3_string_tension/` | historical KPS target (not native) |

Ratio `m₁₊₋/√σ = √6 Σ cₙuⁿ`: c₆ = −4270353824428899200786427191557487127249971701568661364147801/265509089445394220361304005016403470320527806432754073600 (PROVISIONAL, from m₆).

## 2. The computation pipeline (stage → implementing files, by order)

Same five-stage shape at every order n (ROOT + n insertions + output, C-odd, Γ/k=0):

| stage | what | order-4 file | order-6 file(s) | independent (mine) |
|---|---|---|---|---|
| 0 geometry census | enumerate connected supports; triality; canonical ordered words | `y4_extracted_sources/stage0.py` | `SU3_Y6_STAGE0_RESUMABLE_V2/*.cpp` (v2 launcher; wrote the `.tsv`s) | `stage0.py` rerun in-sandbox (q₄ geom) |
| 1 local Haar / singlet | per-link SU(3) singlet projectors (color basis) + Casimir histories | `stage1.py`→`stage3c.py` | `SU3_Y6_STAGE1_LOCAL_EXACT_V1/` (`Y6_LOCAL_EXACT_PATH_LIBRARY.json.gz`); `ENGINE_Y6_su3_local_channel_census.py` | **`su3_y6_m6/ftw.py`** weight-blocked Haar — matches projectors matrix-exactly |
| 3e/3i fold | des-Cloizeaux folded weights (incl. resonances) | `stage3e.py`,`stage3i.py` | `y6_folded_weight_catalog.py`; `su3_o5_consolidated_y6/ENGINE_Y6_folded_descloizeaux_preflight.py` | **`y6_folded_descloizeaux_preflight.folded_coefficient`** — matches on 500 vectors + anchor |
| 3g color contraction | tensor-network contract path tensors via topology wiring | `stage3g.py` | `Y6_M6_EXACT_INTERNAL_V1/source/y6_batched_contraction_core.py` | covered by the projector match (contraction deterministic) |
| 3j Γ-reduction + assembly | cubic-stabilizer reduction → kernel / coefficient | `stage3j.py` → 189-kernel, q₄ | `…/y6_gamma_contraction_batched_resumable.py` → m₆ | reused (color-independent symmetry) |

Order-4 reference pipeline source: `archive/zips/y4_extracted_sources.zip` (stage0…stage3j; runs from ROOT, no external input; ~minutes in-sandbox). Loose copies of individual y4 stages also in `Downloads/y4_stage3*.py`.

## 3. Release / bundle catalog (m₆ packaging chain — newest first)

All in `Downloads/`. The m₆ VALUE is identical across V1→V4; later ones are packaging convenience.

| package | role | status |
|---|---|---|
| `NB_Y6_su3_m6_self_contained_v4.ipynb` (21M, 14:05) | **latest.** Notebook with the whole bundle embedded; run top-to-bottom, no uploads. | recommended runner |
| `SU3_Y6_M6_ALL_IN_ONE_V3.zip` (16M, 13:59) | Stage-0 essential + Stage-1 local + EXACT_INTERNAL_V1 + driver + README_FIRST. | superseded by V4 |
| `SU3_Y6_M6_COMPLETE_DRIVER_V2.zip` (20K, 13:44) | `su3_y6_m6_pipeline_complete.py` + notebook (no embedded data). | superseded by V3/V4 |
| `SU3_Y6_M6_EXACT_INTERNAL_V1_RELEASE.zip` (52K, 12:54) | **canonical result + full contraction source + 14 certificates + verifiers.** | authoritative for m₆ value |

Stage releases (Downloads/):
- `SU3_Y6_STAGE0_ESSENTIAL_RESULTS.zip` (19M) — geometry OUTPUT: `final/y6_triality_survivors.tsv`, `final/y6_ordered_transition_words.tsv`, logs, run_state. (**Does NOT contain** `SIGNATURES/su3_y6_final_ordered_signatures.bin` — that dir was omitted by its zip step.)
- `SU3_Y6_STAGE0_LAUNCH_BUNDLE_2026-06-14.zip` (21M) — v1 launcher code + y5 seed (`y5_connected_supports.bin.gz`). (v1 `enc`; the `.tsv`s were written by v2 — different encoding.)
- `SU3_Y6_STAGE0_RESUMABLE_V2_RELEASE.zip` (44K) — **v2 launcher that wrote the essential-results `.tsv`s** (`su3_y6_stage0_launcher_v2.py`, the `y6_*.cpp` shards).
- `SU3_Y6_STAGE1_LOCAL_EXACT_V1_RELEASE.zip` (60K) — order-6 local layer: `Y6_LOCAL_EXACT_PATH_LIBRARY.json.gz`, `Y6_LOCAL_TOKEN_SIGNATURE_CATALOG.tsv`, census `.cpp`.
- `SU3_Y6_STAGE0_EXTERNAL_MEMORY_V1_RELEASE.zip` (36K) — sharded external-memory census variant + evidence.
- `SU3_Y6_STAGE0_COMPLETE_2026-06-15.tar.zst` (0 bytes — empty/failed export).
- Audits: `SU3_Y6_{LOCAL_INPUTS,STAGE0_VALIDATION}_AUDIT_2026-06-14.zip`.

Y5 / lower order:
- `SU3_Y5_COMPLETE_FIFTH_ORDER_BUNDLE.zip` (19M), `SU3_Y5_M5_COMPLETE_{CERTIFICATE.json,THEOREM.md}`, `ENGINE_Y6_su3_y5_historical_recovery_r2.py`, the `SU3_Y5_Y6_HISTORICAL_RECOVERY*` notebooks/results.
- `SU3_O5_CONSOLIDATED_AND_Y6_PREFLIGHT_2026-06-14.zip` (folded-weight preflight + y6 local fusion preflight).

String tension / SU(N) / paper:
- `SU3_STRING_TENSION_PHYSICAL_O6_RELEASE_V2.zip`, `SU3_STRING_TENSION_O4_COMPLETE_BUNDLE.zip`, `GLUEBALL_STRING_NORMALIZATION_CORRECTION_V2.zip`.
- `SU_N_{STAGE3G_WIRING,WALLED_BRAUER_STAGE2A}_BUNDLE.zip`, `SU6_DETERMINANT_STAGE0_BUNDLE.zip` (in ZIP ARCHIVES).
- `GLUEBALL_FLAT_BAND_SOURCE_RELEASE_V0_7/V0_8.zip`; paper history `glueball_flat_band_paper_v0_1..v0_9*` (Downloads); current = `THEORY/papers/flat_band/glueball_flat_band_paper_v1_1.*`.
- `MASTER_one_plaquette_program*.md` (v2_1…v2_7; current v2_7 in `THEORY/programs/one_plaquette/`).

## 4. KNOWN-MISSING (do not ask the user to upload — these are the facts)

- `su3_y6_final_ordered_signatures.bin`: **not in any uploaded zip** (omitted from ESSENTIAL_RESULTS). Equivalent order-6 local data IS in `SU3_Y6_STAGE1_LOCAL_EXACT_V1` (`Y6_LOCAL_EXACT_PATH_LIBRARY.json.gz`). Otherwise on the Colab VM at `SU3_Y6_RUN/SIGNATURES/`, or regenerable by the v2 signature census.
- The **five large order-6 intermediates** for a full independent re-contraction (`Y6_GAMMA_TOPOLOGY_BLOCKS.tsv`, `Y6_CLASS_ENERGY_SPECTRA.bin`, `Y6_EXACT_LOCAL_PATH_TENSORS.json.gz`, `Y6_ENERGY_CLASSES.tsv`, `Y6_GLOBAL_FOLDED_WEIGHT_CATALOG.tsv`): **not in any upload** (HPC-scale). SHA-256s are in `Y6_M6_EXACT_CERTIFICATE.json`.

## 5. This session's deposits (`THEORY/programs/one_plaquette/`)

- `su3_string_tension_native_o5/`: `ftw.py` (weight-blocked GF(p) engine), σ₅ certificates/reconstruction, README.
- `su3_y6_m6/`: `ENGINE_Y6_su3_m6_pipeline.py` + `ENGINE_Y6_su3_m6_colab.py` (selftest/compile-haar runner), `ENGINE_HAAR_m6_compiler_certificate.py` (22-gate degree-8 Haar validation), `ENGINE_Y6_m6_independent_fold_check.py`, `NOTE_Y6_m6_result_2026-06-15.md`, `NOTE_Y6_m6_independent_verification_2026-06-15.md`, `DATA_Y6_y4_reference_local_path_tensors.json.gz`.
- `papers/flat_band/glueball_flat_band_paper_v1_1.*`: current manuscript (σ₅ exact; provisional m₆ in §6).
- **Relocated into this program from the THEORY root (2026-06-15 cleanup):** `y4_o3_flatband_verification/` (the order-4 reference: Stage 0–3J chain, 189-record H₄ kernel, q₄ = H₄(0) trace — the contraction reference cited in §2) and `lattice_glueball_data/` (real-world lattice glueball spectrum + SU(N) predictions; the band-vs-lattice synthesis). They were loose at root; now siblings here, their mutual `../`-links intact.

## 6. Status summary

- Proven/exact through q₅ and σ₅. m₆ provisional (exact-internal; color+fold independently verified; order-6 census is the open gap). σ₆ = KPS target.
- Open: independent order-6 geometry census (the anomalous m₆ magnitude lives there).
