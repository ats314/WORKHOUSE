# F020 — Unit #10d: red Davies propositions × exact-kernel ledger (OP-7 slack)

**Date:** 2026-06-12 · **Unit:** `02_APPENDICES/red_propositions/` (Props 9.X/9.X′/9.X″ + Defs) cross-read against `numerics/op12_theta/` June-11 kchain accounting. Method: mechanical insertion — the June-11 chain (`Ξ(q) = 8((1+q²)/(1−q²))⁴`, `HS ≤ (2v₀/m²)√(|D|Ξ)`) kept identical, only the decay constant swapped per the propositions. Engine: `numerics/op12_theta/ENGINE_OP1_red_davies_kchain.py` — **35 hard gate checks across 7 families (G1–G7), all pass** (incl. byte-level recomputation of the stored June-11 bounds, G3); rerun-deterministic (JSON byte-identical on cold rerun).

## 1. Computed outcomes (facts, not claims)

1. **Row-sum refinements are vacuous for this comparator.** C₀(Δ₁) = C_∂(Δ₁) = D_E = 18 exactly, at L = 4 and L = 6 (every off-diagonal entry of d₁ᵀd₁ has magnitude 1; the worst row crosses distance level sets at all 18 neighbors). Props 9.X′/9.X″ give nothing here. Red-006's "your diagnostics show a smaller C₀" reflects its own lower-dimensional example (C₀ = 6 is the 2D value); recorded so nobody re-tries this expecting a constant-level win in 4D.
2. **The Davies functional swap alone is worth ×133–172 on the chain bound.** η: 0.0115–0.0148 (CT) → 0.152–0.172 (arcosh form) — the m-vs-m² small-mass scaling realized at x = m²/(2αD_E) ≈ 0.015. On the four stored cases: bound 1.2×10⁶/7.2×10⁵/3.7×10⁵/1.7×10⁵ → 9.2×10³/5.4×10³/2.4×10³/9.9×10². S_kernel: 3.2–9.0×10⁵ → **2.4–5.2×10³**.
3. **Per-√|D| chain constant vs exact:** (2v₀/m²)√Ξ = 5.2–8.5×10⁴ (CT) → **389–497** (Davies) vs exact c = √T_full = 0.127–0.186. Residual analytic-chain slack: **2.1–3.9×10³** — this is what any sharper argument (e.g. the W(r)-weighted pair sums of ledger §4) still has to explain.
4. **Validity spot-check:** the pointwise Davies bound (2/m²)e^(−η·dist) dominates exact M⁻¹ columns (all 4 orientation orbits, CG 1e-12) with max ratio 0.153 (L=4, β=5.6) / 0.150 (L=6, β=6.4) — ≈6.5× pointwise headroom at the sharpest admissible rate.
5. **Chain-level certification stays vacuous at these parameters:** bound < 1 would require |D| ≲ 10⁻⁵. The Davies chain's value is structural (rate scaling), not certificate-grade; the exact-kernel N\* certificate remains the sharp instrument (M5 Lean target unaffected).

## 2. Era/status notes

Red INDEX: `Source: chat_export.md` — these are chat-extract precision items, **no status headers** of their own. Red-001 (tubular neighborhood) is a different topic (orbit-space geometry, OP-5-adjacent) with an explicit honesty section ("the weakest link is uniform control of curvature bounds… as a→0") — architecture, not Davies material. Red-002 defines Δ₁ = d₁ᵀd₁ + d₀d₀ᵀ (full Hodge incl. gauge term) while the OP-12 comparator uses m²I + αd₁ᵀd₁ — definitional mismatch flagged, not reconciled.

## 3. Carried caveat (not resolved here)

The propositions bound **M⁻¹ entries**; the chain applies the bound to the projected kernel G_P = PM⁻¹P exactly as the June-11 ledger did. Gate G6 confirms the resulting bounds dominate measured HS norms on all stored cases, but whether the P-transfer is provable is OP-7-write-up content — Alex's domain.

## 4. Consequence for OP-7 (decision left to Alex)

Re-pointing candidate: the analytic/Lean chain target could swap CT → Davies (Prop 9.X form) for a ~10² gain at unchanged structure, still ~10³ from exact. OPEN_PROBLEMS OP-7 addendum updated with these numbers.

## 5. Deposits

`numerics/op12_theta/ENGINE_OP1_red_davies_kchain.py` + `.json` + `NOTE_OP1_red_davies_results_2026-06-12.md`; `programs/op1_defect_sparsity/red_davies_toolkit/` (9 files, MD5-verified copy of the red extracts + README with provenance and outcome); OPEN_PROBLEMS OP-7 addendum 2; CHAIN_STATUS_MAP §2c (02_APPENDICES consumption row, joint with F019); ledger #10d → DONE.
