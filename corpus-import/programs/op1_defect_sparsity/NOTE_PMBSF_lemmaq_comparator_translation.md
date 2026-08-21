# Lemma Q ↔ OP-1 Comparator — Translation Note (M3 interface)

**Date:** June 12, 2026. **Status:** organizational mapping with verification flags — *no mathematical claims*; every correspondence marked (≈) needs analytic verification as part of M3b. **Decision context:** DECISIONS #007 — Lemma Q / (M′) is the canonical form of M3 (M3a); the comparator form is the interface this note specifies (M3b). **F007 refinement:** in the v3.4 architecture Lemma Q is *derived* (master Props Z.1+Z.2); the open analytic content is Theorems Z.A (LCI typicality) + Z.B (Bałaban far-source stability) — the dictionary below is unchanged, with Z.A/Z.B sitting one level above Lemma Q.
**Sources:** PMBSF pass-19 master §§0.5, 5–7, Appendix I (`programs/pmbsf/`); OP-1 dossier + M2 certificates (`PLAN_OP1_unif_closure.md`, `numerics/op12_theta/`).

## Object dictionary

| PMBSF (SU(2), pass 19) | OP-1 comparator (SU(3) Wilson, June campaign) | Status |
|---|---|---|
| Defect indicator X_p = 1{φ(U_p) ≥ δ_bond} (plaquette-marked; smoothed X_{p,η}) | Defect set D(U) = links of plaquettes with φ_p > δ (link-marked via `plinks`) | (≈) same object up to plaquette→link marking and δ-convention; reconcile δ_bond ↔ δ and η-smoothing |
| Source intensity q_η = E X_p | ρ₁ = E\|D\|/N_links | (≈) modulo marking multiplicity (≤ 4 links/plaquette) |
| Projected plaquette atoms A_p = P1_{∂p}P; trace overlaps tr(A_pA_p') | Kernel pair weights G_P(b,b')² (exact, translation-lookup); W(r) shell tables | (≈) both are the deterministic pair-weight layer; PMBSF bounds overlaps analytically (PTO-2), campaign computes them exactly |
| κ_Λ (closed form, plane-independent) | T_full = max_b Σ_{b'} G_P(b,b')² (exact; N\* = 1/T_full) | (≈) same role: per-defect deterministic capacity constant |
| **(M′) level (iii):** Σ_{p'}\|Cov(X_p,X_{p'})\| tr(A_pA_{p'}) ≤ Cq²κ_Λ² | **ρ-weighted kernel sum < 1:** v₀²Σ_{b,b'} ρ₂(b,b') G_P(b,b')² < 1 with ρ₂ ≤ ρ₁² + Cov-term | **(≈) the same inequality shape** — the load-bearing correspondence |
| Pass-10 minimal target: \|Cov_W(X_{p,η},X_{p',η})\| ≤ C q_η² e^{−m d(p,p')}, uniform in Λ | Dossier §3's ρ₂(β, dist) decay requirement; W(r) tables are its consumer | (≈) near-literal match; this is the single inequality both programs need |
| Lemma Q: conditional rare-source factorization, Z_A(ρ/q_η) ≤ e^{K\|A\|} (⇒ the moment/correlation bounds above) | (S): P(Γ ⊂ D_δ) ≤ K₀^{\|Γ\|}e^{−αβδ\|Γ\|} (Peierls-form inclusion bound) | (≈) Lemma Q is the conditional/cavity strengthening of (S)'s product form |
| Bernoulli–Bernstein comparator (§6): firewall under iid B_p ~ Bern(q), margin 0.615 at worst corner | Count-only certificate θ < 1 for \|D\| ≤ N\* (probability-free) | both unconditional baselines; different probability inputs (iid vs none) |
| Θ < 1 (projected-capacity firewall) | θ < 1 (Birman–Schwinger) | (≈) same role; operator conventions differ (their P_{≤Λ,L} spectral window vs Hodge P; reconcile in M3b) |
| Stage-B exact heat-bath diagnostics (vMF₄ law; Λ medians ≈ 1.016) | OP-12 θ-scan + Peierls probe calibration (δ-regimes) | both: numerical plausibility anchors, not proofs |

## Group/parameter gap to bridge in M3b

SU(2), β = 3.5, exact heat-bath, spectral window Λ ≈ 1.05 ↔ SU(3), β = 5.6–7.2, Wilson MC, Hodge projector, m₀² = 0.5. The lift has two independent steps: (i) SU(2) → SU(3)/SU(N) for the covariance bound (PMBSF's SU(3) sections + `Expanded_Derivations_PMBSF_LemmaQ_SU3` are the in-store starting points); (ii) spectral-window ↔ massive-comparator transfer (their P_{≤Λ} vs M_a^{−1/2}·Π_D·M_a^{−1/2}). Neither is done; both are bookkeeping-heavy rather than conceptually new *if* the SU(2) bound closes — per the pass-19 documents' own framing (verify).

## The assembly, once M3a closes (= M4's job)

Pass-10 bound (SU(3) version) ⇒ ρ₂(b,b') ≤ ρ₁²(1 + Ce^{−m·d}) ⇒ plug into the M2 exact pair sums: E tr K² ≤ v₀²[ρ₁ Σ_b G_P(b,b)² + Σ_{b≠b'} ρ₂ G_P²] with the W(r) tables — typical-θ < 1 follows wherever the numbers land below 1 (the dossier §3 targets quantify exactly where). Uniformity along β(a) enters through ρ₁(β) (Lemma Q's q_η scaling) and the computed T_full(β, L) trends.

## Convergence note (recorded, not asserted)

PMBSF's spectral-window direction conjectures a projected BE floor ρ\*(L) → κ_G (pass 16) — the **same geometric Ricci floor that anchors the main chain's P04 Haar curvature mechanism**. If that direction matures, the sparsity program and the curvature program meet at κ_G. Flagged for the review ledger when units #7 (P04) and #33+ are cross-read.

## Failed routes (carried over so nobody retries them silently)

Global HB-q² Matrix-Stein absorption (v15 audit: η_cov 0.40–1.23 vs target 0.25) — failed. Edge-Bernoulli comparator v6b (Wilson/edge ratio 1.23–1.55) — retired. A′ spike-residual budget — failed (Untitled193). Trace-weighted finite-rank — WEAK. (Dossier §5 updated.)
