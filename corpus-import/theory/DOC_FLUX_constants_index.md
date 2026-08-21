# CONSTANTS INDEX — every exact rational in the corpus

**Generated** by `export/index/ENGINE_GOV_build_constants_index.py`. Regenerate after any corpus edit; do not hand-edit.

Scanned **398** prose files (`.md` + `.tex`, excluding `archive/`). **205** distinct non-trivial exact rationals live in the tree across **1049** occurrences; **9** more appear only in `QUARANTINE/`.

## Why this file exists

The join keys of this corpus are exact rationals, not concepts. `109151/249696` appears in dozens of separate files; so does `20721577909065127111/7250590288602460800`. No semantic search will ever retrieve those from a natural-language query, so an exact index is the primary retrieval surface — and until this file, nothing in the tree listed them. `theory/DOC_GOV_conventions.md` §3 is the designated citable-constants table but covers only the June Birman–Schwinger era (κ, ceiling-law, Lemma A/B); this file covers the flux-band program.

**Reading the columns.** *Symbol* is recovered mechanically from the most authoritative occurrence that assigns the value to a name — a strong hint, **not a definition**; verify against the source before citing. *Cited* counts live occurrences and distinct live files. *Tiers* lists the document classes carrying the constant, so you can see whether it is vouched for by the authority stack or only by a manuscript. A constant carried by `manuscript` but not `authority` is a candidate for exactly the kind of drift this corpus has a documented history of.

> **Before quoting any row:** pin the convention via `theory/DOC_GOV_conventions.md`, then check `export/index/CERT_GOV_constant_ratio_classifications.json`. Four constants here stand in exact 2× or 4× relationships with another. Three are legitimate convention (real-space `β/4` vs symbol `β`; `τ₄` vs `2τ₄`); the fourth is a **live symbol collision** — `κ` denotes `2a(n)` in `corpus/` and `a(n)` in flat-band manuscript v1.1. Neither is wrong; anyone quoting across them would be.

---

## Cited constants (187)

| Symbol | Value | Cited | Tiers | Defined in |
|---|---|---:|---|---|
| `d_3` | `109151/249696` | 73 / 39f | authority, theorem, manuscript, campaign, numerics, note, record, other, +quarantine | `corpus/GLUEBALL_SOURCE_CONSOLIDATION_GUIDE_2026-08-20_v3.md`:183 |
| `B_3` | `17607806155349/275331901291200` | 44 / 25f | authority, theorem, manuscript, campaign, numerics, note, record, other, +quarantine | `theory/theorems/THM_FLUX_strongest_formula_resolved_cellular_mobility_2026-08-20.md`:179 |
| `q` | `20721577909065127111/7250590288602460800` | 34 / 20f | authority, manuscript, campaign, numerics, note, other, +quarantine | `papers/flat_band/PAPER_FLUX_glueball_flat_band_v0_9_2_normalization.tex`:66 |
| `w_1` | `132329431693349/275331901291200` | 28 / 19f | authority, theorem, manuscript, campaign, numerics, note, other, +quarantine | `corpus/GLUEBALL_DETAILED_FORMULA_DOCUMENT_2026-08-20_v3_1.md`:770 |
| `b_3` | `1975/124848` | 28 / 20f | authority, theorem, manuscript, campaign, numerics, note, record, other, +quarantine | `corpus/GLUEBALL_DETAILED_FORMULA_DOCUMENT_2026-08-20_v3_1.md`:360 |
| `w_d` | `17607806155349/1101327605164800` | 23 / 13f | authority, theorem, manuscript, numerics, note, other, +quarantine | `corpus/GLUEBALL_DETAILED_FORMULA_DOCUMENT_2026-08-20_v3_1.md`:778 |
| `q_4` | `304746539168/160249753125` | 23 / 18f | theorem, manuscript, campaign, note, record, other, +quarantine | `theory/theorems/THM_O4_universal_fourth_order_mobility_theorem_v2_2026-08-08.md`:99 |
| — | `1769/3060` | 17 / 10f | manuscript, campaign, numerics, note, record, +quarantine | `papers/flat_band/PAPER_FLUX_glueball_flat_band_v0_9_2_normalization.tex`:384 |
| — | `9397/1020` | 16 / 6f | campaign, numerics, note, record, +quarantine | `programs/one_plaquette/NOTE_FLUX_glueball_band_results_v2.md`:66 |
| — | `223/1020` | 15 / 7f | authority, manuscript, campaign, numerics, other, +quarantine | `corpus/GLUEBALL_DETAILED_FORMULA_DOCUMENT_2026-08-20_v3_1.md`:302 |
| `d_3` | `-109151/249696` | 14 / 10f | manuscript, campaign, numerics, note, record, +quarantine | `programs/one_plaquette/PAPER_FLUX_manuscript_section6_patch.tex`:310 |
| `leak_3` | `12331/249696` | 14 / 12f | authority, manuscript, campaign, numerics, note, other, +quarantine | `corpus/GLUEBALL_DETAILED_FORMULA_DOCUMENT_2026-08-20_v3_1.md`:362 |
| — | `21281/1530` | 14 / 8f | campaign, note, record, other, +quarantine | `programs/one_plaquette/shell6_o2/NOTE_SHELL6_o2_result_2026-06-13.md`:4 |
| — | `132329431693349/3303982815494400` | 13 / 6f | manuscript, campaign, numerics, note, other, +quarantine | `papers/flat_band/PAPER_FLUX_glueball_flat_band_v0_9_2_normalization.tex`:934 |
| `\sigma_5` | `137767222189182735950309/2009803206414863779…` | 13 / 11f | manuscript, campaign, record, other, +quarantine | `papers/flat_band/THM_Y5_fourth_order_t1pm_band_theorem_v0_8.md`:572 |
| `\sigma_4` | `737327120374220449/7250590288602460800` | 13 / 12f | manuscript, campaign, note, +quarantine | `programs/one_plaquette/su3_o5_consolidated_y6/AUDIT_STRING_m6_sigma56_execution_report_2026-06-14.md`:131 |
| `c4` | `-20721577909065127111/7250590288602460800` | 11 / 9f | manuscript, campaign, numerics, note, +quarantine | `programs/one_plaquette/y4_o3_flatband_verification/CERT_Y4_global_band_edge_certificate.md`:10 |
| — | `1109/3060` | 11 / 8f | manuscript, campaign, numerics, note, +quarantine | `papers/flat_band/PAPER_FLUX_glueball_flat_band_v0_9_2_normalization.tex`:542 |
| `diag` | `1879/3060` | 11 / 7f | manuscript, campaign, numerics, note, +quarantine | `papers/flat_band/PAPER_FLUX_glueball_flat_band_v0_9_2_normalization.tex`:385 |
| — | `217/1020` | 11 / 4f | manuscript, campaign, numerics, +quarantine | `papers/flat_band/PAPER_FLUX_glueball_flat_band_v0_9_2_normalization.tex`:539 |
| — | `5665/110592` | 11 / 4f | authority, manuscript, campaign, note, +quarantine | `corpus/MASTER_THEORY_UNIFIED_2026-08-20_v3.md`:1499 |
| — | `54049/520200` | 10 / 7f | manuscript, campaign, numerics, note, +quarantine | `papers/flat_band/PAPER_FLUX_glueball_flat_band_v0_9_2_normalization.tex`:603 |
| `q_5` | `866236750503342026253096691057/1169668083793…` | 10 / 8f | manuscript, campaign, +quarantine | `papers/flat_band/PAPER_FLUX_glueball_flat_band_v1_1.tex`:1270 |
| — | `471353/1560600` | 9 / 8f | manuscript, campaign, numerics, note, +quarantine | `papers/flat_band/PAPER_FLUX_glueball_flat_band_v0_9_2_normalization.tex`:605 |
| — | `6117632/479655` | 9 / 8f | campaign, note, record, other, +quarantine | `programs/one_plaquette/shell6_o2/NOTE_SHELL6_o2_result_2026-06-13.md`:5 |
| — | `6277517/479655` | 9 / 8f | campaign, note, record, other, +quarantine | `programs/one_plaquette/shell6_o2/NOTE_SHELL6_o2_result_2026-06-13.md`:5 |
| — | `6597287/479655` | 9 / 8f | campaign, note, record, other, +quarantine | `programs/one_plaquette/shell6_o2/NOTE_SHELL6_o2_result_2026-06-13.md`:5 |
| `c_3` | `7559/499392` | 9 / 9f | authority, manuscript, campaign, note, +quarantine | `papers/flat_band/PAPER_FLUX_glueball_flat_band_v1_1.tex`:1328 |
| `c4` | `-3447362930970494909/1450118057720492160` | 8 / 7f | manuscript, campaign, numerics, note, +quarantine | `programs/one_plaquette/y4_o3_flatband_verification/CERT_Y4_global_band_edge_certificate.md`:13 |
| `\kappa_{111}` | `132329431693349/1651991407747200` | 8 / 7f | authority, manuscript, campaign, note, +quarantine | `papers/gauge_constrained_spectral_geometry/PAPER_FLUX_gauge_constrained_spectral_geometry_unified_v1_4_2026-08-08.md`:505 |
| — | `17700498622147435111/7250590288602460800` | 8 / 8f | manuscript, campaign, numerics, note, +quarantine | `papers/flat_band/PAPER_FLUX_glueball_flat_band_v0_9_2_normalization.tex`:917 |
| `\kappa_{110}` | `247051057231349/2202655210329600` | 8 / 8f | authority, manuscript, campaign, note, other, +quarantine | `papers/gauge_constrained_spectral_geometry/PAPER_FLUX_gauge_constrained_spectral_geometry_unified_v1_4_2026-08-08.md`:503 |
| — | `3447362930970494909/1450118057720492160` | 8 / 8f | manuscript, campaign, numerics, note, +quarantine | `papers/flat_band/PAPER_FLUX_glueball_flat_band_v0_9_2_normalization.tex`:919 |
| `e}` | `52163/260100` | 8 / 5f | manuscript, campaign, numerics, note, +quarantine | `papers/flat_band/PAPER_FLUX_glueball_flat_band_v0_9_2_normalization.tex`:611 |
| — | `61751/249696` | 8 / 8f | manuscript, campaign, numerics, note, record, +quarantine | `papers/flat_band/PAPER_FLUX_glueball_flat_band_v0_9_2_normalization.tex`:601 |
| `c4` | `-17700498622147435111/7250590288602460800` | 7 / 7f | manuscript, campaign, numerics, note, +quarantine | `programs/one_plaquette/y4_o3_flatband_verification/CERT_Y4_global_band_edge_certificate.md`:11 |
| `q_4` | `-304746539168/160249753125` | 7 / 6f | manuscript, campaign, note, record, +quarantine | `papers/flat_band/PAPER_FLUX_glueball_flat_band_v1_1.tex`:1247 |
| `c4` | `-4367164159624988707/1812647572150615200` | 7 / 7f | manuscript, campaign, numerics, note, +quarantine | `programs/one_plaquette/y4_o3_flatband_verification/CERT_Y4_global_band_edge_certificate.md`:12 |
| — | `1107923/959310` | 7 / 5f | campaign, note, +quarantine | `programs/one_plaquette/shell6_o2/NOTE_SHELL6_o2_result_2026-06-13.md`:6 |
| — | `13271/50176` | 7 / 2f | campaign, note, +quarantine | `programs/one_plaquette/NOTE_FLUX_master_one_plaquette_program_v2_7.md`:16 |
| — | `15699837076521691751589626260152540589721150…` | 7 / 7f | campaign, record, other | `programs/one_plaquette/PLAN_Y6_program_index.md`:27 |
| `c_4` | `15752822901180179/12642703205932800` | 7 / 7f | manuscript, campaign, note, +quarantine | `papers/flat_band/PAPER_FLUX_glueball_flat_band_v1_1.tex`:1329 |
| `w_0` | `189690244462349/91777300430400` | 7 / 7f | authority, manuscript, numerics, note, +quarantine | `corpus/GLUEBALL_DETAILED_FORMULA_DOCUMENT_2026-08-20_v3_1.md`:768 |
| — | `4367164159624988707/1812647572150615200` | 7 / 7f | manuscript, campaign, numerics, note, +quarantine | `papers/flat_band/PAPER_FLUX_glueball_flat_band_v0_9_2_normalization.tex`:918 |
| — | `-54049/520200` | 6 / 6f | manuscript, campaign, numerics, note, +quarantine | `papers/flat_band/PAPER_FLUX_glueball_flat_band_v0_9_2_normalization.tex`:1340 |
| — | `-61751/249696` | 6 / 6f | manuscript, campaign, numerics, note, +quarantine | `papers/flat_band/PAPER_FLUX_glueball_flat_band_v0_9_2_normalization.tex`:1337 |
| — | `-9397/1020` | 6 / 5f | manuscript, campaign, numerics, note, +quarantine | `papers/flat_band/PAPER_FLUX_glueball_flat_band_v0_9_2_normalization.tex`:380 |
| `B_5` | `1881863087742908605903793/165293224897596718…` | 6 / 6f | manuscript, campaign, +quarantine | `papers/flat_band/PAPER_FLUX_glueball_flat_band_v1_1.tex`:1267 |
| `old}` | `211835444920651/4405310420659200` | 6 / 6f | authority, manuscript, campaign, note, other, +quarantine | `corpus/GLUEBALL_DETAILED_FORMULA_DOCUMENT_2026-08-20_v3_1.md`:961 |
| `E(k)` | `2861009/8438730300` | 6 / 6f | authority, note, other, +quarantine | `corpus/GLUEBALL_SOURCE_CONSOLIDATION_GUIDE_2026-08-20_v3.md`:281 |
| `B_5` | `4037562229115732471176793/165293224897596718…` | 6 / 6f | manuscript, campaign, +quarantine | `papers/flat_band/PAPER_FLUX_glueball_flat_band_v1_1.tex`:1277 |
| `c_4` | `4555981615057344457/1812647572150615200` | 6 / 5f | campaign, note, +quarantine | `programs/one_plaquette/y4_o3_flatband_verification/THM_Y4_theorem_flat_band_breaking_2026-06-13.md`:35 |
| — | `6953/36864` | 6 / 2f | campaign, note, +quarantine | `programs/one_plaquette/NOTE_FLUX_master_one_plaquette_program_v2_7.md`:16 |
| `q_6` | `1/2160` | 5 / 2f | manuscript, +quarantine | `papers/THM_SUN_su_n_class_function_theorem_v2_alt.tex`:317 |
| — | `13029053/959310` | 5 / 3f | campaign, note, +quarantine | `programs/one_plaquette/shell6_o2/v2_authoritative/README.md`:46 |
| — | `13127/50176` | 5 / 3f | campaign, note, record, +quarantine | `programs/one_plaquette/NOTE_FLUX_master_one_plaquette_program_v2_7.md`:16 |
| `tr(T^{(3)})^3` | `175/13824` | 5 / 4f | manuscript, campaign, +quarantine | `programs/pmbsf/NOTE_PMBSF_su3_su_n_wilson_merged_draft_2026-05-30.md`:627 |
| — | `1980693/2048` | 5 / 5f | campaign, note, record, other | `programs/one_plaquette/su3_y6_m6/NOTE_Y6_m6_result_2026-06-15.md`:35 |
| — | `25/294912` | 5 / 4f | manuscript, campaign, +quarantine | `papers/gauge_constrained_spectral_geometry/PAPER_FLUX_gauge_constrained_spectral_geometry_unified_v1_4_2026-08-08.md`:167 |
| `\tau_4` | `2861009/16877460600` | 5 / 5f | authority, note, other, +quarantine | `corpus/GLUEBALL_DETAILED_FORMULA_DOCUMENT_2026-08-20_v3_1.md`:1361 |
| `h_{4,side}` | `2861009/84387303000` | 5 / 5f | authority, note, other, +quarantine | `corpus/GLUEBALL_SOURCE_CONSOLIDATION_GUIDE_2026-08-20_v3.md`:274 |
| — | `3125/13824` | 5 / 3f | theorem, campaign, note | `theory/theorems/LEM_O4_lemma_b_review_2026-06-12.md`:62 |
| `\,y^3` | `6335/187272` | 5 / 5f | manuscript, campaign, numerics, note, +quarantine | `papers/flat_band/PAPER_FLUX_glueball_flat_band_v0_9_2_normalization.tex`:613 |
| `\alpha_6` | `64/25725` | 5 / 3f | theorem, manuscript, +quarantine | `theory/theorems/THM_O4_universal_fourth_order_mobility_theorem_v2_2026-08-08.md`:48 |
| — | `-132329431693349/3303982815494400` | 4 / 4f | manuscript, numerics, note, +quarantine | `papers/flat_band/PAPER_FLUX_glueball_flat_band_v0_9_2_normalization.tex`:1377 |
| — | `1193/16384` | 4 / 2f | campaign, note, +quarantine | `programs/one_plaquette/NOTE_FLUX_master_one_plaquette_program_v2_7.md`:168 |
| — | `12075379/959310` | 4 / 3f | campaign, note, record | `programs/one_plaquette/shell6_o2/NOTE_SHELL6_o2_result_2026-06-13.md`:178 |
| — | `12714919/959310` | 4 / 3f | campaign, note, record | `programs/one_plaquette/shell6_o2/NOTE_SHELL6_o2_result_2026-06-13.md`:179 |
| — | `13034689/959310` | 4 / 3f | campaign, note, record | `programs/one_plaquette/shell6_o2/NOTE_SHELL6_o2_result_2026-06-13.md`:180 |
| — | `13674229/959310` | 4 / 3f | campaign, note, record | `programs/one_plaquette/shell6_o2/NOTE_SHELL6_o2_result_2026-06-13.md`:220 |
| `bal}` | `15644916262153/34416487661400` | 4 / 4f | theorem, manuscript, campaign, note, +quarantine | `papers/flat_band/THM_Y5_fourth_order_t1pm_band_theorem_v0_8.md`:185 |
| `q_3` | `16863189551/76406976000` | 4 / 4f | theorem, manuscript, campaign, note, +quarantine | `theory/theorems/THM_SUN_unified_nality_theorem_corrected_2026-06-14.md`:126 |
| `q_6` | `19/1244160` | 4 / 1f | manuscript | `papers/THM_SUN_su_n_class_function_theorem_v2_alt.tex`:62 |
| `B2` | `247051057231349/550663802582400` | 4 / 4f | manuscript, campaign, numerics, note, +quarantine | `numerics/scratch_tmp/y4_sos_repro/Y4_REAL_SPACE_SOS_PACKAGE/THM_Y4_real_space_sos_theorem.md`:81 |
| `\beta_4^{pen}` | `3601925923737103752887/704816967203594963437…` | 4 / 3f | manuscript, campaign, +quarantine | `papers/gauge_constrained_spectral_geometry/PAPER_FLUX_gauge_constrained_spectral_geometry_unified_v1_4_2026-08-08.md`:468 |
| — | `6335/249696` | 4 / 3f | campaign, numerics, note, +quarantine | `programs/one_plaquette/NOTE_FLUX_master_one_plaquette_program_v2_7.md`:429 |
| — | `633904/479655` | 4 / 3f | campaign, note | `programs/one_plaquette/shell6_o2/NOTE_SHELL6_o2_result_2026-06-13.md`:7 |
| — | `-12331/249696` | 3 / 3f | campaign, note, +quarantine | `programs/one_plaquette/NOTE_FLUX_run_log_2026-06-11.md`:29 |
| `VLINK_EX` | `-1474623/1675520` | 3 / 3f | note, record, +quarantine | `records/audits/07-denominator-lift.md`:38 |
| `diagonal` | `-21281/1530` | 3 / 3f | campaign, note, record | `programs/one_plaquette/shell6_o2/NOTE_SHELL6_o2_result_2026-06-13.md`:297 |
| — | `-6335/249696` | 3 / 2f | campaign, note | `programs/one_plaquette/NOTE_FLUX_run_log_2026-06-11.md`:25 |
| — | `-737327120374220449/7250590288602460800` | 3 / 3f | manuscript, campaign, note, +quarantine | `papers/flat_band/PAPER_FLUX_glueball_flat_band_v1_1.tex`:1789 |
| `\boxed{q_5` | `-866236750503342026253096691057/116966808379…` | 3 / 3f | manuscript, campaign, +quarantine | `programs/one_plaquette/su3_o5_consolidated_y6/sources/THM_Y5_su3_fifth_order_theorem.md`:14 |
| — | `101/2700` | 3 / 3f | manuscript, numerics, +quarantine | `papers/flat_band/PAPER_FLUX_glueball_flat_band_v0_9_2_normalization.tex`:299 |
| — | `10433/4800` | 3 / 3f | note | `theory/DOC_FLUX_constants_index.md`:105 |
| — | `1145/13601` | 3 / 3f | manuscript, note, +quarantine | `papers/flat_band/PAPER_FLUX_glueball_flat_band_v0_9_2_normalization.tex`:1079 |
| `K` | `11816469772330068287291692098025623610692788…` | 3 / 3f | manuscript, campaign, +quarantine | `programs/one_plaquette/su3_o5_consolidated_y6/AUDIT_STRING_m6_sigma56_execution_report_2026-06-14.md`:151 |
| `c_M` | `13250388338835740713398569140103/11696680837…` | 3 / 3f | manuscript, campaign, +quarantine | `papers/flat_band/THM_Y5_fourth_order_t1pm_band_theorem_v0_8.md`:500 |
| — | `13348823/959310` | 3 / 2f | campaign, note, +quarantine | `programs/one_plaquette/shell6_o2/v2_authoritative/THM_SHELL6_shell46_theorem_v2.md`:130 |
| `q_4` | `162485785670299274695454289332603/1212946071…` | 3 / 3f | manuscript, campaign, +quarantine | `papers/flat_band/THM_Y5_fourth_order_t1pm_band_theorem_v0_8.md`:242 |
| — | `23081/65536` | 3 / 2f | campaign, note, +quarantine | `programs/one_plaquette/NOTE_FLUX_master_one_plaquette_program_v2_7.md`:16 |
| `B_4` | `2314426811641505637629/234938989067864987812…` | 3 / 3f | campaign, note, +quarantine | `programs/one_plaquette/sun_band_shape/completion_2026-06-14/THM_SU4_determinant_theorem.md`:38 |
| `c_{5,\det}^{SU(3)}` | `235424477177/407461473619200` | 3 / 2f | theorem, note, +quarantine | `theory/theorems/THM_FLUX_strongest_formula_resolved_cellular_mobility_2026-08-20.md`:219 |
| — | `24541/62424` | 3 / 3f | campaign, numerics, note, +quarantine | `programs/one_plaquette/NOTE_FLUX_master_one_plaquette_program_v2_7.md`:430 |
| `C_3` | `25/1024` | 3 / 3f | authority, manuscript, other, +quarantine | `corpus/MASTER_THEORY_UNIFIED_2026-08-20_v3.md`:967 |
| — | `281257/4608000` | 3 / 3f | note | `theory/DOC_FLUX_constants_index.md`:116 |
| — | `2873/19200` | 3 / 3f | note | `theory/DOC_FLUX_constants_index.md`:117 |
| — | `42703538244288992007864271915574871272499717…` | 3 / 3f | campaign, record | `programs/one_plaquette/PLAN_Y6_program_index.md`:39 |
| — | `43579/8640000` | 3 / 3f | theorem, campaign, note | `theory/theorems/LEM_O4_lemma_b_review_2026-06-12.md`:62 |
| `c_R` | `475012476694676416524425923/2790771339458416…` | 3 / 3f | manuscript, campaign, +quarantine | `papers/flat_band/THM_Y5_fourth_order_t1pm_band_theorem_v0_8.md`:503 |
| — | `517313/6242400` | 3 / 3f | campaign, numerics, note, +quarantine | `programs/one_plaquette/NOTE_FLUX_master_one_plaquette_program_v2_7.md`:430 |
| — | `52959/3553` | 3 / 3f | campaign, note, +quarantine | `programs/one_plaquette/shell6_o2/v2_authoritative/README.md`:48 |
| — | `55053/262144` | 3 / 2f | campaign, note, +quarantine | `programs/one_plaquette/NOTE_FLUX_master_one_plaquette_program_v2_7.md`:14 |
| — | `60219/102400` | 3 / 2f | campaign, note, +quarantine | `programs/one_plaquette/NOTE_FLUX_master_one_plaquette_program_v2_7.md`:14 |
| `c_X` | `659205375444420345742539899543/1169668083793…` | 3 / 3f | manuscript, campaign, +quarantine | `papers/flat_band/THM_Y5_fourth_order_t1pm_band_theorem_v0_8.md`:498 |
| — | `72099/262144` | 3 / 2f | campaign, note, +quarantine | `programs/one_plaquette/NOTE_FLUX_master_one_plaquette_program_v2_7.md`:14 |
| — | `-10670728893034386567182468628311/4678672335` | 2 / 1f | note | `theory/DOC_FLUX_constants_index.md`:127 |
| `\sqrt\sigma}` | `-10670728893034386567182468628311/4678672335…` | 2 / 2f | campaign | `programs/one_plaquette/su3_o5_consolidated_y6/sources/THM_Y5_su3_fifth_order_theorem.md`:97 |
| — | `-109151/15980544` | 2 / 2f | campaign, note, +quarantine | `programs/one_plaquette/su3_o5_consolidated_y6/AUDIT_SU3_glueball_coupling_normalization_2026-06-14.md`:116 |
| `\boxed{\sigma_6` | `-1313066166103419077293595934881644464980071…` | 2 / 2f | campaign, +quarantine | `programs/one_plaquette/su3_o5_consolidated_y6/sources/THM_STRING_su3_tension_o4_theorem_normalized_v2.md`:59 |
| `w_1` | `-132329431693349/275331901291200` | 2 / 2f | numerics, note | `numerics/scratch_tmp/y4_sos_repro/Y4_REAL_SPACE_SOS_PACKAGE/THM_Y4_real_space_sos_theorem.md`:53 |
| — | `-137767222189182735950309/200980320641486377` | 2 / 1f | note | `theory/DOC_FLUX_constants_index.md`:132 |
| `\boxed{\sigma_5` | `-137767222189182735950309/200980320641486377…` | 2 / 2f | campaign, +quarantine | `programs/one_plaquette/su3_o5_consolidated_y6/sources/THM_STRING_su3_tension_o4_theorem_normalized_v2.md`:57 |
| — | `-137767222189182735950309/205803848336882051` | 2 / 1f | note | `theory/DOC_FLUX_constants_index.md`:134 |
| `c_4` | `-15752822901180179/12642703205932800` | 2 / 2f | campaign, note, +quarantine | `programs/one_plaquette/su3_o5_consolidated_y6/AUDIT_SU3_glueball_coupling_normalization_2026-06-14.md`:183 |
| `M4_EXACT` | `-160506019419340168451/14501180577204921600` | 2 / 2f | note, record | `records/audits/08-rooted-adjudication.md`:54 |
| — | `-162485785670299274695454289332603/121294607` | 2 / 1f | note | `theory/DOC_FLUX_constants_index.md`:137 |
| — | `-1781/55296` | 2 / 2f | manuscript, note, +quarantine | `papers/gauge_constrained_spectral_geometry/PAPER_FLUX_gauge_constrained_spectral_geometry_unified_v1_4_2026-08-08.md`:146 |
| — | `-1960/1` | 2 / 1f | manuscript | `papers/THM_SUN_su_n_class_function_theorem_v2_alt.tex`:539 |
| — | `-1975/124848` | 2 / 2f | note, record | `theory/DOC_FLUX_constants_index.md`:140 |
| — | `-20721577909065127111/1856151113882229964800` | 2 / 2f | campaign, note, +quarantine | `programs/one_plaquette/su3_o5_consolidated_y6/AUDIT_SU3_glueball_coupling_normalization_2026-06-14.md`:117 |
| — | `-24541/62424` | 2 / 2f | campaign, note | `programs/one_plaquette/NOTE_FLUX_run_log_2026-06-11.md`:26 |
| — | `-2649605075224534084759/18561511138822299648` | 2 / 1f | note | `theory/DOC_FLUX_constants_index.md`:143 |
| `D_EXACT` | `-361008126292641364183/7250590288602460800` | 2 / 2f | note, record | `records/audits/08-rooted-adjudication.md`:53 |
| — | `-48945521/25468992` | 2 / 2f | note, record | `theory/DOC_FLUX_constants_index.md`:145 |
| — | `-517313/6242400` | 2 / 2f | campaign, note | `programs/one_plaquette/NOTE_FLUX_run_log_2026-06-11.md`:27 |
| — | `-55954617740619111266546735567327219227/2665` | 2 / 1f | note | `theory/DOC_FLUX_constants_index.md`:147 |
| — | `-5665/110592` | 2 / 2f | manuscript, note, +quarantine | `papers/gauge_constrained_spectral_geometry/PAPER_FLUX_gauge_constrained_spectral_geometry_unified_v1_4_2026-08-08.md`:660 |
| — | `-5871724573605720944161941470537/62078801439` | 2 / 1f | note | `theory/DOC_FLUX_constants_index.md`:149 |
| — | `-68773336105372320795886362345421433/1403601` | 2 / 1f | note | `theory/DOC_FLUX_constants_index.md`:150 |
| — | `-737327120374220449/1856151113882229964800` | 2 / 2f | campaign, note, +quarantine | `programs/one_plaquette/su3_o5_consolidated_y6/AUDIT_SU3_glueball_coupling_normalization_2026-06-14.md`:150 |
| `c_3` | `-7559/499392` | 2 / 2f | campaign, note, +quarantine | `programs/one_plaquette/su3_o5_consolidated_y6/AUDIT_SU3_glueball_coupling_normalization_2026-06-14.md`:182 |
| — | `-781009569168365268247626732239/648447459458` | 2 / 1f | note | `theory/DOC_FLUX_constants_index.md`:153 |
| — | `-850411/3995136` | 2 / 2f | campaign, note | `programs/one_plaquette/su3_string_tension/README.md`:41 |
| — | `-866236750503342026253096691057/116966808379` | 2 / 1f | note | `theory/DOC_FLUX_constants_index.md`:103 |
| — | `1014252151151/865945728` | 2 / 2f | campaign, note, +quarantine | `programs/one_plaquette/su3_y5_fifth_order/THM_Y5_su3_m5_theorem_2026-06-14.md`:121 |
| — | `10670728893034386567182468628311/46786723351` | 2 / 1f | note | `theory/DOC_FLUX_constants_index.md`:157 |
| `c_5` | `10670728893034386567182468628311/46786723351…` | 2 / 2f | manuscript, +quarantine | `papers/flat_band/PAPER_FLUX_glueball_flat_band_v1_1.tex`:1330 |
| — | `108889196164826769179507/7656393167294719161` | 2 / 1f | note | `theory/DOC_FLUX_constants_index.md`:159 |
| — | `111910685208057689/3107395837972483200` | 2 / 2f | note | `theory/DOC_FLUX_constants_index.md`:160 |
| — | `1193/8192` | 2 / 2f | campaign, note, +quarantine | `programs/one_plaquette/NOTE_FLUX_master_one_plaquette_program_v2_7.md`:220 |
| `c_{4,N}` | `11930/9` | 2 / 2f | manuscript, campaign | `papers/flat_band/README.md`:40 |
| — | `126537112003083861011/1271689472003172306084` | 2 / 1f | note | `theory/DOC_FLUX_constants_index.md`:163 |
| — | `13250388338835740713398569140103/11696680837` | 2 / 1f | note | `theory/DOC_FLUX_constants_index.md`:108 |
| — | `137767222189182735950309/2009803206414863779` | 2 / 1f | note | `theory/DOC_FLUX_constants_index.md`:35 |
| — | `162485785670299274695454289332603/1212946071` | 2 / 1f | note | `theory/DOC_FLUX_constants_index.md`:110 |
| — | `1657/567000` | 2 / 2f | campaign, note, +quarantine | `programs/one_plaquette/NOTE_FLUX_master_one_plaquette_program_v2_7.md`:104 |
| — | `165983/10659` | 2 / 2f | campaign, note, +quarantine | `programs/one_plaquette/shell6_o2/v2_authoritative/THM_SHELL6_shell46_theorem_v2.md`:133 |
| — | `17607806155349/4405310420659200` | 2 / 2f | campaign, note | `programs/one_plaquette/y4_o3_flatband_verification/NOTE_Y4_summary.md`:36 |
| — | `17700498622147435111/87007083463229529600` | 2 / 2f | campaign, note | `programs/one_plaquette/y4_o3_flatband_verification/NOTE_Y4_summary.md`:34 |
| — | `180411173111623579/3107395837972483200` | 2 / 2f | note | `theory/DOC_FLUX_constants_index.md`:171 |
| — | `1881863087742908605903793/165293224897596718` | 2 / 1f | note | `theory/DOC_FLUX_constants_index.md`:68 |
| — | `1975/62424` | 2 / 2f | note, record | `theory/DOC_FLUX_constants_index.md`:173 |
| — | `2025/2026` | 2 / 2f | note, record | `theory/DOC_FLUX_constants_index.md`:174 |
| — | `2055143/1600300800` | 2 / 2f | campaign, note, +quarantine | `programs/one_plaquette/NOTE_FLUX_master_one_plaquette_program_v2_7.md`:107 |
| — | `2167017157/800150400000` | 2 / 2f | campaign, note, +quarantine | `programs/one_plaquette/NOTE_FLUX_master_one_plaquette_program_v2_7.md`:105 |
| — | `2314426811641505637629/234938989067864987812` | 2 / 1f | note | `theory/DOC_FLUX_constants_index.md`:112 |
| — | `235401086266217267636986869176/8815920161561` | 2 / 1f | note | `theory/DOC_FLUX_constants_index.md`:178 |
| `\boxed{B_6` | `235401086266217267636986869176/8815920161561…` | 2 / 2f | campaign, +quarantine | `programs/one_plaquette/sun_band_shape/completion_2026-06-14/THM_SU6_determinant_theorem.md`:106 |
| — | `27013849/1918620` | 2 / 2f | campaign, note, +quarantine | `programs/one_plaquette/shell6_o2/v2_authoritative/THM_SHELL6_shell46_theorem_v2.md`:34 |
| — | `291/1637` | 2 / 2f | manuscript, +quarantine | `papers/flat_band/PAPER_FLUX_glueball_flat_band_v0_9_2_normalization.tex`:1081 |
| — | `3265/26136` | 2 / 2f | note, record | `theory/DOC_FLUX_constants_index.md`:182 |
| — | `32657/7620480` | 2 / 2f | campaign, note, +quarantine | `programs/one_plaquette/NOTE_FLUX_master_one_plaquette_program_v2_7.md`:104 |
| — | `33554467/33554393` | 2 / 2f | note, record | `theory/DOC_FLUX_constants_index.md`:184 |
| — | `3356317/1769472` | 2 / 2f | campaign, note, +quarantine | `programs/one_plaquette/NOTE_FLUX_master_one_plaquette_program_v2_7.md`:14 |
| — | `34705471293352429373/174014166926459059200` | 2 / 2f | campaign, note | `programs/one_plaquette/y4_o3_flatband_verification/NOTE_Y4_summary.md`:35 |
| — | `34877/15240960` | 2 / 2f | campaign, note, +quarantine | `programs/one_plaquette/NOTE_FLUX_master_one_plaquette_program_v2_7.md`:106 |
| — | `3601925923737103752887/704816967203594963437` | 2 / 1f | note | `theory/DOC_FLUX_constants_index.md`:95 |
| — | `367979177879/1344252672000000` | 2 / 2f | campaign, note, +quarantine | `programs/one_plaquette/NOTE_FLUX_master_one_plaquette_program_v2_7.md`:109 |
| `c_5` | `37373840041427/407461473619200` | 2 / 2f | theorem, note, +quarantine | `theory/theorems/THM_FLUX_strongest_formula_resolved_cellular_mobility_2026-08-20.md`:228 |
| `b8` | `38764675528307/83642388480000000` | 2 / 2f | campaign, note, +quarantine | `programs/one_plaquette/NOTE_FLUX_master_one_plaquette_program_v2_7.md`:109 |
| — | `4037562229115732471176793/165293224897596718` | 2 / 1f | note | `theory/DOC_FLUX_constants_index.md`:71 |
| — | `454728157341029756849050509176/8815920161561` | 2 / 1f | note | `theory/DOC_FLUX_constants_index.md`:193 |
| `B_6` | `454728157341029756849050509176/8815920161561…` | 2 / 2f | campaign, +quarantine | `programs/one_plaquette/sun_band_shape/completion_2026-06-14/THM_SU6_determinant_theorem.md`:112 |
| — | `475012476694676416524425923/2790771339458416` | 2 / 1f | note | `theory/DOC_FLUX_constants_index.md`:120 |
| — | `511051/124848` | 2 / 2f | note, record | `theory/DOC_FLUX_constants_index.md`:196 |
| `name{tr}\bigl(T^{(3)}\bigr)^4` | `5125/32768` | 2 / 2f | campaign, note | `programs/pmbsf/NOTE_PMBSF_su3_su_n_wilson_merged_draft_2026-05-30.md`:625 |
| `FOLD_EX` | `5315003/140454` | 2 / 2f | note, record | `records/audits/07-denominator-lift.md`:38 |
| — | `55954617740619111266546735567327219227/26657` | 2 / 1f | note | `theory/DOC_FLUX_constants_index.md`:199 |
| `q_6` | `55954617740619111266546735567327219227/26657…` | 2 / 2f | manuscript, campaign, +quarantine | `papers/flat_band/THM_Y5_fourth_order_t1pm_band_theorem_v0_8.md`:251 |
| — | `56673445/1528823808` | 2 / 2f | campaign, note, +quarantine | `programs/one_plaquette/NOTE_FLUX_master_one_plaquette_program_v2_7.md`:66 |
| — | `659205375444420345742539899543/1169668083793` | 2 / 1f | note | `theory/DOC_FLUX_constants_index.md`:125 |
| — | `781009569168365268247626732239/6484474594581` | 2 / 1f | note | `theory/DOC_FLUX_constants_index.md`:203 |
| `q_5` | `781009569168365268247626732239/6484474594581…` | 2 / 2f | manuscript, campaign, +quarantine | `papers/flat_band/THM_Y5_fourth_order_t1pm_band_theorem_v0_8.md`:246 |
| — | `7903/221184` | 2 / 2f | manuscript, note, +quarantine | `papers/gauge_constrained_spectral_geometry/PAPER_FLUX_gauge_constrained_spectral_geometry_unified_v1_4_2026-08-08.md`:563 |
| — | `81428712396187592747/4238964906677241020280` | 2 / 2f | campaign, note | `programs/one_plaquette/sun_band_shape/CERT_Y4_sun_all_n_ge_3_band_shape_2026-06-14.md`:41 |
| — | `866236750503342026253096691057/1169668083793` | 2 / 1f | note | `theory/DOC_FLUX_constants_index.md`:43 |

## Single-citation constants (18)

Cited exactly once in the live tree. Either genuinely one-off, or a constant that lost its cross-references — worth knowing which.

| Value | Symbol | Where |
|---|---|---|
| `-1313066166103419077293595934881644464980071…` | — | `programs/one_plaquette/su3_o5_consolidated_y6/AUDIT_SU3_glueball_coupling_normalization_2026-06-14.md`:152 |
| `-137767222189182735950309/205803848336882051…` | — | `programs/one_plaquette/su3_o5_consolidated_y6/AUDIT_SU3_glueball_coupling_normalization_2026-06-14.md`:151 |
| `-162485785670299274695454289332603/121294607…` | `q_4` | `programs/one_plaquette/sun_band_shape/completion_2026-06-14/THM_SU4_determinant_theorem.md`:32 |
| `-2649605075224534084759/18561511138822299648…` | — | `programs/one_plaquette/su3_string_tension/README.md`:41 |
| `-521965902/593076541` | — | `theory/DOC_FLUX_constants_index.md`:212 |
| `-55954617740619111266546735567327219227/2665…` | `q_6` | `programs/one_plaquette/sun_band_shape/completion_2026-06-14/THM_SU6_determinant_theorem.md`:94 |
| `-5871724573605720944161941470537/62078801439…` | — | `programs/one_plaquette/su3_y5_fifth_order/THM_Y5_su3_m5_theorem_2026-06-14.md`:109 |
| `-68773336105372320795886362345421433/1403601…` | — | `programs/one_plaquette/su3_y5_fifth_order/THM_Y5_su3_m5_theorem_2026-06-14.md`:115 |
| `-781009569168365268247626732239/648447459458…` | — | `papers/flat_band/THM_Y5_fourth_order_t1pm_band_theorem_v0_8.md`:70 |
| `108889196164826769179507/7656393167294719161…` | — | `programs/one_plaquette/su3_o5_consolidated_y6/AUDIT_SU3_glueball_coupling_normalization_2026-06-14.md`:187 |
| `126537112003083861011/1271689472003172306084…` | — | `programs/one_plaquette/sun_band_shape/CERT_Y4_sun_all_n_ge_3_band_shape_2026-06-14.md`:41 |
| `13130661661034190772935959348816444649800714…` | `\,t_6` | `programs/one_plaquette/su3_string_tension/AUDIT_STRING_batch_verification_sigma_reconciliation_2026-06-14.md`:65 |
| `1474623/1675520` | — | `theory/DOC_FLUX_constants_index.md`:220 |
| `160506019419340168451/14501180577204921600` | — | `theory/DOC_FLUX_constants_index.md`:221 |
| `175/4608` | `name{tr}\bigl(T^{(3)}\bigr)^3` | `programs/pmbsf/NOTE_PMBSF_su3_su_n_wilson_merged_draft_2026-05-30.md`:623 |
| `3125/648` | — | `theory/theorems/LEM_O4_lemma_b_review_2026-06-12.md`:55 |
| `54321/837760` | `e_4(C)` | `theory/DOC_FLUX_constants_index.md`:224 |
| `6170/9` | `\(B_N` | `programs/one_plaquette/sun_band_shape/README.md`:26 |

## Constants appearing only in QUARANTINE (9)

These occur in **no live document**. Each is either a value that was corrected — in which case the correction should be traceable — or a result that was dropped without a successor. Both are worth knowing; neither is citable.

| Value | Symbol | Where | Occ |
|---|---|---|---:|
| `1021/256` | — | `QUARANTINE/superseded/MASTER_THEORY.md`:58 | 2 |
| `26775/2` | `P_5` | `QUARANTINE/superseded/MASTER_THEORY.md`:295 | 1 |
| `1785/16` | `Im\,Tr\,e^{iX}` | `QUARANTINE/superseded/MASTER_THEORY.md`:295 | 1 |
| `65/1728` | — | `QUARANTINE/superseded/MASTER_THEORY.md`:458 | 1 |
| `119/1536` | — | `QUARANTINE/superseded/MASTER_THEORY.md`:458 | 1 |
| `551/13824` | — | `QUARANTINE/superseded/MASTER_THEORY.md`:458 | 1 |
| `309/1280` | `D` | `QUARANTINE/superseded/MASTER_THEORY.md`:568 | 1 |
| `39/1280` | `e_4` | `QUARANTINE/superseded/MASTER_THEORY.md`:568 | 1 |
| `327/83776` | `\omega_4` | `QUARANTINE/superseded/MASTER_THEORY.md`:568 | 1 |
