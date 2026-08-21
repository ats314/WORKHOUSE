# Flat-band glueball paper — **v1.1 current** (June 15, 2026); earlier versions retained below

**Current version: `PAPER_FLUX_glueball_flat_band_v1_1.tex` + `.pdf`** (2026-06-15, 27 pp, pdflatex ×3 clean, 0 undefined refs).
v1.1 promotes **σ₅ from native-reproduced (13-sig-fig float) to EXACT and INDEPENDENTLY RECONSTRUCTED**:
computed in exact finite-field arithmetic modulo **seven** independent primes (189-bit combined modulus), then
CRT-combined and rational-reconstructed **with no literature input** → σ₅ = 137767222189182735950309/2009803206414863779920000
(unique; coincides with the historical KPS value, used only as a post-hoc check). Enabled by a **weight-blocked
GF(p) determinant-sector engine** (`ftw.py`) that builds the m=7 (dim-2187) singlet projector inside the SU(3)
weight-zero block (dim 240). The appendix table + §ratio + verification
paragraph are updated accordingly; engine + certificate `CERT_STRING_sigma5_exact_certificate.json` live at
`../../programs/one_plaquette/su3_string_tension_native_o5/`. Referee polish: title trimmed to a clean
main+subtitle over SU(N≥3); the version-history author footnote replaced by a clean submission footnote.
v1.0 retained byte-identical for provenance.

**Prior — v1.0** (`glueball_flat_band_paper_v1_0.tex` + `.pdf`, 2026-06-15, 27 pp, pdflatex ×2 clean, 0 undefined refs).
v1.0 adds, over v0.9: **three figures** (`PAPER_FLUX_fig_bands.pdf` — the exactly-flat T₁⁺⁻ branch at 11/306 along Γ-X-M-R-Γ; `PAPER_FLUX_fig_c4.pdf` — the O(y⁴) lifting with Γ minimum / R maximum / ΔW₄≈0.4806; `PAPER_SUN_fig_largen.pdf` — the 1/N² mass extrapolation), and **promotes σ₅ from a historical KPS target to native-reproduced** via a new from-scratch exact SU(3) torelon engine that resolves the determinant/ε (triality) sector (new verification appendix `app:nativesigma`; σ₂,σ₃ exact-native, σ₄,σ₅ to ~13 sig figs vs KPS). Engine + certificate: `../../programs/one_plaquette/su3_string_tension_native_o5/`. v0.9 retained byte-identical.

**Prior — v0.9** (`glueball_flat_band_paper_v0_9.tex` + `.pdf`, 2026-06-14, 24 pp, compiles clean).
v0.9 is the **most complete form** — it folds every verified result into one paper. Over v0.8a it adds:
the **SU(2) exclusion theorem** (C is a gauge transformation in SU(2) ⟹ no T₁⁺⁻ branch; N≥3 maximal); the
**SU(3) fifth-order band** (Theorem: c₅=q₅+(A₅Q+B₅R)/2S, A₅=313/240, B₅>0; rest-mass series through y⁵); the
**scale-matched m/√σ ratio** with the project-native string tension (bridge σ(y)=½W(2y), σ₅ reconciled negative);
the **m₆ state** (local layer cleared, global open); the **determinant offsets** Δq₄,Δq₆; the **§11 corrected
fixed-rank wording**; and a **physical-interpretation section** — the continuum diagnostic (series alone can't reach
the continuum) and the **1/N² held-out glueball-mass prediction** (m/√σ→6.15 vs 6.065(40); ≈3.0 GeV), honestly
labeled as a lattice-data extrapolation, not a from-series result. Carries the y=β/6 normalization. All new content
is machine-verified (T1); none promoted to "established". Built in /tmp and copied back md5-verified.
- Retained for provenance: **v0.8a** (normalization erratum only), **v0.8** (byte-identical to the archive bundle), **v0.1**.
- Companion: `THM_Y5_fourth_order_t1pm_band_theorem_v0_8.md` (the theorem blueprint v0.9 implements),
  `AUDIT_FLUX_normalization_erratum_2026-06-14.md`.

("Gauss-law protection and exact fourth-order lifting of a flat band ... and a scale-matched glueball-mass estimate",
Alexander Smith, Independent Researcher, June 14, 2026).
Intaken from the 2026-06-14 ZIP-ARCHIVES drop (`GLUEBALL_FLAT_BAND_SOURCE_RELEASE_V0_8.zip`, md5
`0f40513795f5c3bce2440f14e290e14e`). v0.1 files are kept for history but are **superseded**.

**What v0.8 adds over v0.1 (changelog `DOC_FLUX_glueball_flat_band_paper_v0_8_changelog.md`):** it embeds the
**fourth-order SU(N) band-shape theorem, promoted from N≥7 to every integer N≥3** (SU(2) separate):
reduced \(B_N=P_{17}(N^2)/(N R_{20}(N^2))\); large-N series \(q_N=-227/N^5+\dots\), \(A_N=640/N^7+\dots\),
\(\Delta c_{4,N}=\tfrac{11930}{9}N^{-7}+\dots\); exceptional-rank determinant analysis (SU4 ΔA=ΔB=0; SU5 none;
SU6 absent-from-target). The SU(3) theorem, real-space SOS identity, exact kernel and lower-order
coefficients are unchanged from the certified v0.1 chain.

**Verification this session (T1, cold-reproduced + independent cross-check).** The load-bearing new
content — the SU(N) band-shape theorem — was cold-run in a clean sandbox: `ENGINE_Y4_sun_all_n_ge3_band_shape_verify.py`,
`ENGINE_Y4_sun_symbolic_qab_verify.py`, `ENGINE_Y4_sun_largen_asymptotic_verify.py` **all gates pass**; and I independently
re-derived \(A_N=640/(N(N^2-1)^3)\) + \(B_N>0\) + bandwidth\(>0\) for N=7..18 from the separate independent-rerun
kernels. Distilled into `../../programs/one_plaquette/sun_band_shape/` (see its README). The v0.8 release also
ships its own independent symbolic audit (`AUDIT_FLUX_full_symbolic_independent_2026-06-14.md`, copied here) and
verification logs (in the source bundle). Status: machine-gated T1; not yet T2 (line-by-line) / T3 (referee).

**Consolidated theorem companion:** `THM_Y5_fourth_order_t1pm_band_theorem_v0_8.md` (Alex, 2026-06-14) — the
single best statement of the whole theorem behind the paper: SU(2) exclusion (§2), rank-complete fourth-order
band for all N≥3 (§§3–7), large-N flattening (§8), SU(3) fifth order + scale-matched ratio with the corrected
σ(u)=½W(2u) normalization and the σ₅-sign reconciliation (§9), m₆ state (§9.5), the corrected fixed-rank
verification scope (§11), and an honest proved/open status table (§13). Its §13 flags the very coupling-variable
fix now applied in v0.8a. Cross-refs: `../../programs/one_plaquette/{sun_band_shape,su3_y5_fifth_order,su3_o5_consolidated_y6,glueball_mass_prediction}/`.

---

## v0.1 (complete June 13, 2026) — retained for history

Standalone theory paper (`glueball_flat_band_paper_v0_1.tex` + compiled `.pdf`, 10 pp). All claims rest on the certified chain in `../../programs/one_plaquette/`.

**Status: complete and submittable.** Authorship filled June 13 — **Alexander Smith (Independent Researcher)**; recompiled clean (10 pp). (Optional, → v0.2: the O(y⁴) tromino-weight criterion computation.)

## June 13, 2026 hardening (THEORY, under AGENT_PROTOCOL)

- **Full cited certificate chain reproduced cold, in-store = 387 hard gates**, all passing: `ENGINE_FLUX_su3_moments_ext.py` 27, `ENGINE_FLUX_su3_domino_d3.py` 251 (regenerated `RUN_TROM_d3_results.json` byte-identical to the E: archive, sha256 d2d653b4…), `ENGINE_FLUX_glueball_band_certificate_v2.py` 35, `ENGINE_TROM_tromino_contract_independent_check.py` 19, `ENGINE_TROM_tromino_candidate_closed_form_check.py` 1 (+ a 40-point numerical battery), `ENGINE_FLUX_cls_flat_band_certificate_v1_1.py` 14, `ENGINE_FLUX_master_v2_regression_certificate.py` 40.
- **CLS v1.1 reconstructed** (`../../programs/one_plaquette/ENGINE_FLUX_cls_flat_band_certificate_v1_1.py` + `NOTE_FLUX_cls_flat_band_results_v1_1.md`). The v1.1 cited in App. A was lost (F015; the file re-uploaded was byte-identical v1.0). Rebuilt from v1.0 + the master-doc v2.6 changelog: G10 edge-count now gated (a Python operator-precedence bug bypassed it in v1.0), the G09 k=0 span overclaim removed, **new G09b** certifies torus completeness dim ker(Ñ+4I)=L³+2=29=26+3 at L=3, G11 reworded. 14/14 cold. **Agent reconstruction, labeled as such** — a machine-gated (T1) artifact, not claimed byte-identical to the lost original.
- **`ENGINE_FLUX_master_v2_regression_certificate.py`** (40 gates) was absent from C:\ALL THEORY → copied in from `E:\YANG ORGANIZED/12_ONE_PLAQUETTE/domino_certificates/` so the cited document-level regression reproduces in-store.
- **Gate counts corrected in the paper**: "more than 400 hard gates" → 387 (abstract, intro, App. A); the glueball band certificate 36 → 35 (the script's own counter prints "ALL 35 GATES PASSED").
- **Bibliography verified** against journal records (all entries). Two title/ref mismatches corrected: Banks et al. → "Strong-coupling calculations of the hadron spectrum of quantum chromodynamics" (PRD 15 (1977) 1111); Athenodorou–Teper → "The glueball spectrum of SU(3) gauge theory in 3+1 dimensions" (JHEP 11 (2020) 172).
- **The "towers certified separately" (c2/n7 N-generalization) claim was trimmed** to what reproduces (the within-plaquette towers used here are gated within `ENGINE_FLUX_su3_domino_d3.py`). The c2/n7 certs remain lost (F015); the paper no longer relies on them.
- **Authorship filled** (Alexander Smith, Independent Researcher) and PDF recompiled clean (pdflatex, 10 pp). Rendered PDF re-checked for all fixes + author.

Source of record: this directory. Archive original: `E:\YANG ORGANIZED/12_ONE_PLAQUETTE/theory_paper/`.

**Reproduce the chain:** run the seven certificates in `../../programs/one_plaquette/` (and `tromino_o3/`). One path caveat: `ENGINE_FLUX_su3_domino_d3.py` and `ENGINE_TROM_tromino_contract_independent_check.py` reference an authoring path `/home/claude/review/` for a JSON write / weight-cards read — run from a dir where that resolves or patch locally; gates are unaffected.
