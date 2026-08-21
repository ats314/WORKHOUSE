# SU(3) O(u⁶) glueball rest mass m₆ — pipeline validation (degree-8 Haar tensor compiler)

**Created 2026-06-15 (this session).** Target: `m₆ = ⅓ tr H₆(0)`, the sixth-order rest energy
of the $T_1^{+-}$ glueball band, `u=β/6=1/g_H⁴` (the single open coefficient in the flat-band paper).

## Status (honest)

| component | status |
|---|---|
| Stage-0 connected six-insertion **geometry census** (247,326,161 supports → 21,175 triality survivors → ~1.22M ordered transition words → 2,870 final local signatures) | **DONE by Alex (Colab), integrity-verified here (SHA-256 ✓)** |
| **E₆ scalar fold identity** (32 monomials; only new moment `S11111=⟨0|VRVRVRVRVRV|0⟩`) | **VALIDATED** (`ENGINE_Y6_su3_scalar_fold_formula.py`, 12 matrix models) |
| encoding decode (`<7I4Q` records; plaquette dec/enc; per-link token = ext·inc·sg; 256-bit triality mask) | **DONE** (from the C++/Python source) |
| **degree-8 Haar tensor compiler** (per-link SU(3) singlet projectors + Casimir resolvent histories) | **BUILT + VALIDATED** (22 gates, this dir) |
| global folded contraction → moments → m₆ | **HPC / external-memory — NOT done; no m₆ value claimed** |

## The validated advance: degree-8 Haar tensor compiler

The weight-blocked GF(p) singlet projector (`ftw.py`, this session's σ₅ engine) is the "degree-eight
Haar tensor compiler" the launch bundle flags as the next stage. `ENGINE_HAAR_m6_compiler_certificate.py`
cross-checks it against the bundle's **independent fusion-tree census** (`ENGINE_Y6_su3_local_channel_census.py`):

- **singlet color multiplicity** for every triality family through degree 8 — (1,1),(3,0),(0,3),(2,2),
  (4,1),(1,4),(6,0),(0,6),(3,3),(5,2),(2,5),(7,1),(1,7),(4,4) — all match (incl. every determinant/ε sector);
- **cumulative-Casimir resolvent histories** (the energy denominators feeding the fold) — full multiset
  agreement on representative tokens through degree 8 (incl. (4,4) 23-channel and (7,1) 21-channel).

**22/22 gates pass, cold-reproduced.** This validates the per-link layer of the m₆ contraction.

## What remains (the HPC step)

`m₆ = E₆` via the fold needs the **chain moments** `S` — global contractions summing, over the
~1.22M ordered six-insertion geometries, the product of per-link Haar tensors (now validated) weighted by
the resolvent denominators `∏ 1/(E₀−E_cut)`, plus all lower moments. This is external-memory scale (the
bundle defers it). The per-link inputs are ready; the global sum is not attempted in-sandbox. **No m₆
value is fabricated.** The natural validation when it is run: reproduce q₄, q₅ (known from the paper's
independent 189-record kernel) through the same fold before trusting q₆.

## Files

- `ftw.py` — weight-blocked GF(p) engine (the Haar compiler core; copy of the σ₅ engine).
- `ENGINE_Y6_su3_local_channel_census.py`, `ENGINE_Y6_su3_scalar_fold_formula.py` — bundle reference code (fusion-tree census + E₆ fold), copied for reproducibility.
- `ENGINE_HAAR_m6_compiler_certificate.py` — 22-gate certificate runner (this dir; local imports).
- `ENGINE_HAAR_validate.py`, `ENGINE_Y6_energy_validate.py` — the two cross-checks.
- `CERT_HAAR_m6_compiler_certificate.json` — gate results.

## Provenance (uploaded bundles; bulk data NOT copied into THEORY per rule 8)

- `SU3_Y6_STAGE0_ESSENTIAL_RESULTS.zip` sha256 `4360b13079b942738408161fa8f45f80e449d2c2e7b670277449cb45ef4ac5db`
  - `final/y6_triality_survivors.tsv` sha256 `57e988a02424cd2731685704227b16cd56702c9bd20af2e583f88a894cfb0cf6` (21,175 rows)
  - `final/y6_ordered_transition_words.tsv` sha256 `aa951806f830718e4a9c53b2542c26669bcde2770b0e335739a8e5370b389db4` (371 MB; ~3.1M rows)
- `SU3_Y6_STAGE0_LAUNCH_BUNDLE_2026-06-14.zip` sha256 `5a33bd828287f654adecf9b2655bebc0e94eb81847eb0a89f10c5bc90ef4aa06` (census C++/launcher + y5 seed)
- Bulk census data lives in the uploaded bundles / the archive, not here.

## Addendum 2026-06-15 (cont.) — corrected notebook + contraction reference located

- **`NB_Y6_su3_m6_pipeline_corrected.ipynb`** — Colab notebook of the pipeline. Fixes a boundary-sign
  edit that appeared in an uploaded copy: `boundary()` MUST return oriented-square signs
  `(+1,+1,-1,-1)` (per `su3_y6_stage0_census.cpp` / `postprocess.py`); the uploaded copy had
  `(+1,+1,+1,-1)`. The error does not affect `selftest` or `compile-haar` (neither calls
  `boundary()`), only `contract`.
- **Contraction reference for `contract`:** the order-4 glueball contraction that produced q4 is the
  in-tree Stage 0–3J chain — `../y4_o3_flatband_verification/`:
  `NB_Y4_d3_vertex_singlet_dictionary_generator.ipynb` (vertex-singlet layer), `CERT_Y4_stage3j_verdict.json`
  (gates: 4221 ordered words → 189-record H4 kernel), `CERT_Y4_full_real_space_h4_kernel.json` (q4 = H4(0) trace).
  Completing m6 = extending that multi-stage chain (vertex singlets + des-Cloizeaux fold + assembly +
  Γ-trace) to order 6 and validating it against q4/q5 before emitting q6. The per-link Haar layer and the
  E6 fold are already validated here; the multi-stage color/Γ assembly is the remaining work.
