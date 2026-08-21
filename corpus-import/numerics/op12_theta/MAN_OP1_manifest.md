# 04_SIMULATIONS / op12_theta_scan — MANIFEST

**Generated:** June 11, 2026 (updated June 12: M2 pair-certificate suite added; June 12 evening: m4_scaling/ M4-precompute suite; June 12 late: T_C asymptotics suite — closed form, log law, (S)-interface; June 12 late evening: s_chessboard/ route engine + M5.1/M5.3 notebooks + F029/F030 audit suite; June 12 late night: **Lemma-B proof certificate** + session-P M5 audit engines + M5.4–M5.8 notebook, F031; June 12 latest: z_prime_mc Ē₁ engine (F034) + **op12_delta_window δ-window scan (F035)** + **delta_max_curvature δ_max comparator-faithfulness (F036)** in s_chessboard/)
**Total Files:** 94+ (10 root + 8 per-configuration results + 26 in m2_certificates/ + 38 in m4_scaling/ + 11 in s_chessboard/ [README, ENGINE_OP1_s_chessboard_rate.py/.json, ENGINE_OP1_z_prime_mc.py/.json, ENGINE_OP1_op12_delta_window.py, CERT_OP1_delta_window_summary.json, DATA_OP1_delta_window.png, ENGINE_OP1_delta_max_curvature.py, RUN_OP1_dmax.py, CERT_OP1_delta_max_curvature.json] + dw_state/ (24, resumable scan state) + this file; excludes m4_scaling/opcache/ — 12 regenerable .npz operator caches, ~73 MB, safe to delete)

| File | Type | Purpose |
|---|---|---|
| README.md | md | Directory overview, headline, reproduce instructions |
| NOTE_OP1_results_2026-06-11.md | md | Results table (24 rows), findings 1–5, caveats, relation to Program B |
| ENGINE_OP1_op12_runner.py | py | Deadline-chunked MC + θ runner (hard gates; checkpointing; schedule embedded) |
| CERT_OP1_op12_summary.json | json | Aggregated summary per (L, β, δ) |
| DATA_OP1_op12_theta_vs_beta.png | png | θ_max/θ_mean vs β, L = 4/6, δ = 0.7/0.9/1.1 |
| NOTE_OP1_kchain_ledger_2026-06-11.md | md | Slack decomposition of the OP-7 chain; exact kernel constants; N\* certificate + validation |
| ENGINE_OP1_kchain_ledger.py | py | Exact HS-norm (defect-basis Gram) vs θ_op vs chain bound on stored configs |
| CERT_OP1_kchain_ledger.json | json | Ledger data (S_int, S_kernel per case) |
| ENGINE_OP1_kernel_consts.py | py | Exact G_P constants per orientation orbit: g_diag, T_full, c, N\* |
| CERT_OP1_kernel_consts.json | json | Kernel constant tables, L = 4 and 6, β = 5.6–7.2 |
| m2_certificates/NOTE_OP1_m2_results_2026-06-12.md | md | M2 results: gates, certify-rates (δ=1.1: 91%), L=8 constants, structural limits |
| m2_certificates/ENGINE_OP1_m2_pair_certificates.py | py | Engine: kernel tensor (4 solves/(L,β)), translation-lookup exact certs, 3 hard gates |
| m2_certificates/ENGINE_OP1_m2_ensemble.py | py | Chunked fresh-ensemble runner; stores defect sets per config |
| m2_certificates/ENGINE_OP1_m2_l8_shells.py | py | L=8 constants + W(r) distance-shell tables |
| m2_certificates/m2_certs_L{4,6}.json | json | Stored-state certificates, all δ |
| m2_certificates/CERT_OP1_m2_l8_shells.json | json | L=8 constants; shell tables L=6/8 |
| m2_certificates/m2_kernel/ (10 npz) | npz | Cached kernel tensors (certs reproducible without solves) |
| m2_certificates/m2_ens