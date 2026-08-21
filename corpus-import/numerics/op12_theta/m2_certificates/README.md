# m2_certificates — M2: exact pair-level certificates (June 12, 2026)

Milestone M2 of `programs/op1_defect_sparsity/PLAN_OP1_unif_closure.md`: translation invariance ⇒ 4 projected solves per (L, β) determine the whole kernel G_P; per-configuration certificate = exact √(tr K²) by lookup. Canonical results + caveats: `NOTE_OP1_m2_results_2026-06-12.md`.

| File | Purpose |
|---|---|
| `ENGINE_OP1_m2_pair_certificates.py` | Certificate engine: builds/loads the lookup tensors, certifies stored-state configs; gates GATE-TR (lookup vs direct solve), GATE-NSTAR, GATE-VALID |
| `ENGINE_OP1_m2_ensemble.py` → `m2_ensemble/` | Fresh-ensemble certification (defect sets stored per config) |
| `ENGINE_OP1_m2_l8_shells.py` → `CERT_OP1_m2_l8_shells.json` | L = 8 kernel constants + W(r) shell tables (the ρ₂ interface for the open lemma (S)) |
| `CERT_OP1_m2_certs_l4.json` / `CERT_OP1_m2_certs_l6.json` | Stored-state certificates |
| `m2_kernel/` | Lookup tensor cache (regenerable — see its README; engines resolve this path relative to CWD) |

Run from `numerics/op12_theta/` (CWD requirement): `python3 m2_certificates/ENGINE_OP1_m2_pair_certificates.py …`
