<!-- THEORY > numerics > op12_theta | Live status: STATE.md | Problems: theory/DOC_GOV_open_problems.md (OP-1, OP-7, OP-12) -->

# op12_theta — Direct Birman–Schwinger θ Computation (OP-12): engines + data, working home

**This is the working copy:** `E:\YANG\ORGANIZED\04_SIMULATIONS\op12_theta_scan\` copied MD5-verified June 12, 2026 (archive-deposit inventory: `MAN_FLUX_manifest.md`), **plus** `op12_state/` MC states rescued the same day from temporary session outputs — every certificate is reproducible from this directory alone. Smoke-tested cold June 12: GATE-TR / GATE-NSTAR / GATE-VALID pass, certificates byte-reproduce. **Run engines from THIS directory** (they expect `ENGINE_OP1_op12_runner.py`, `CERT_OP1_kernel_consts.json`, `op12_state/` in CWD). Known wart: the M2 engines resolve the `m2_kernel/` tensor cache relative to CWD — a June-12 run from here left a stray partial cache at this level (removed after an array-identity check against the canonical `m2_certificates/m2_kernel/`).

**What it does:** the direct numerical test of whether the Birman–Schwinger framework (OP-1) closes. SU(3) Wilson MC along β = 5.6–7.2 at L = 4, 6; defect sets seeded by bad plaquettes at Peierls-calibrated thresholds; θ = v₀·λmax(Π_D P M⁻¹ P Π_D) computed exactly per configuration with hard gates (chain-complex identity, projector idempotence, [M,P] = 0, CG residuals).

**Headline (June 11):** θ < 1 with margin in the sparse-defect regime (δ ≥ 0.9), monotone decreasing in β, stable L = 4 → 6; firewall fails only at near-percolating δ = 0.7, β = 5.6. **Evidence and calibration, not closure** — caveats in `NOTE_OP1_results_2026-06-11.md`.

| File | Purpose |
|---|---|
| `ENGINE_OP1_op12_runner.py` | Deadline-chunked runner: MC + incidence operators + Hodge projector + θ power iteration; checkpointed, resumable; prints ALL_WORK_DONE |
| `op12_state/` | MC checkpoint states + per-(L,β) meta/results (provenance: rescued June 12 — see its README) |
| `NOTE_OP1_results_2026-06-11.md` / `CERT_OP1_op12_summary.json` / `DATA_OP1_op12_theta_vs_beta.png` / `results/` | June-11 scan: results note, machine-readable summary (24 rows), plot, per-configuration data |
| `NOTE_OP1_kchain_ledger_2026-06-11.md` + `ENGINE_OP1_kchain_ledger.py/.json` | Slack decomposition of the OP-7 chain (where it loses ~10⁶) + exact ‖K‖_HS via defect-basis Gram on stored configs |
| `ENGINE_OP1_kernel_consts.py/.json` | Exact configuration-independent G_P = PM⁻¹P constants: g_diag, T_full, c = √T_full, N\* per (L, β) — the probability-free certificate θ < 1 for \|D\| ≤ N\* |
| `m2_certificates/` | **M2 (June 12):** exact pair-level certificate engine (translation-lookup tensors), stored-state + fresh-ensemble certifications with defect sets stored, L=8 constants, W(r) shells. Canonical results: `m2_certificates/NOTE_OP1_m2_results_2026-06-12.md` |
| `m4_scaling/` | M4 physical-units scaling tables (precomputed June 12; consumers blocked on M3) |
| `ENGINE_OP1_red_davies_kchain.py/.json` + `NOTE_OP1_red_davies_results_2026-06-12.md` | **#10d/F020 (June 12):** the kchain re-run with red_propositions Davies rates — chain bounds ×133–172 tighter, row-sum constants vacuous here, N\* certificate unchanged |

Reproduce: `python3 ENGINE_OP1_op12_runner.py --deadline 600` repeatedly until ALL_WORK_DONE (numpy + scipy, `pip install --break-system-packages`; ~5 min laptop-class). Extend (L = 8, longer therm, m₀²(a)): edit SCHEDULE/M2 atop the runner.
