# M4 prep — physical-scaling kernel tables (June 12, 2026)

Exact T_full/N\* under AF scaling: β(a) = (11N/48π²)log(1/(aΛ)²), m₀²(a) = m̄²a² (anchored m₀²=0.5 at β=5.6), α_W = β/6, v₀ = 1. GATE-REF passes (anchors reproduce `CERT_OP1_kernel_consts.json`). Data: `CERT_OP1_m4_scaling_tables.json`; engine: `ENGINE_OP1_m4_scaling_tables.py` (scale factors s = 1/a ratio: 1, 1.25, 1.5, 2, 3).

## The two readings

**Fixed L (wrong diagonal, shown for contrast):** N\* collapses fast as a→0 (L=4: 29 → 17 → 9 → 3 → 0) — β grows only logarithmically while m₀² ∝ a² kills the comparator mass.

**Fixed physical volume (L ∝ 1/a — the meaningful diagonal):**

| trajectory point | (L, s) | T_full | N\* |
|---|---|---|---|
| start | (4, 1.0) | 0.0345 | 29 |
| ×1.5 finer | (6, 1.5) | 0.0392 | 25 |
| ×2 finer | (8, 2.0) | 0.0423 | 23 |

T_full grows **slowly** along the physical diagonal (~+10% per refinement step shown) rather than exploding — the volume trend (T_full ↓ in L) partially cancels the mass trend (T_full ↑ as m₀²↓). N\* erodes mildly: 29 → 25 → 23.

## Honest read + open diagnostic

This is a *two-step, small-L* diagonal at v₀ = 1 — not a limit statement. The mild erosion means (S)/Lemma Q must supply defect-density decay along the trajectory at least matching it (consistent with the dossier's structural finding; quantitatively gentler on the physical diagonal than the fixed-L collapse suggests). **Open diagnostic (next session):** decompose T_full's m₀²→0 growth into harmonic-sector (the 4 torus zero-modes of L₁up, where M⁻¹ = 1/m₀²) vs coexact contributions — if growth localizes in the 4 harmonic modes, the comparator can treat them separately (finite-dimensional sector) and the coexact T_full may be scaling-stable. Back-of-envelope harmonic estimates conflict with the measured values, so the decomposition needs computing, not estimating. Also: v₀'s physical scaling (defect potential strength vs a) is a modeling input for M4 proper — flagged for Alex's sign-off at assembly time.

**RESOLVED June 12 (same day, evening pass):** the decomposition is computed and gated — see `NOTE_OP1_m4_harmonic_decomp_2026-06-12.md`. Outcome: T_H = 1/(m₀⁴L⁴) exactly (constant on the physical diagonal); the fixed-L collapse is entirely harmonic (98% at (4,3)); T_C is scaling-stable to ×1.63 across the full grid; the rank-4-exact + coexact-HS **split certificate** holds N\*_split ≈ 30 flat along the diagonal. The "conflict" above dissolved: the closed form reproduces all measured rows once the cross-term-free orthogonal split is used. v₀ sign-off item unchanged.
