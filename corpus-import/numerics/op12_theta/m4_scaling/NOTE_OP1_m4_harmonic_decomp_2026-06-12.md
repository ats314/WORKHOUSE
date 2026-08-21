# M4 harmonic/coexact decomposition — the scaling instability is exactly the 4 harmonic modes (June 12, 2026)

Resolves the open diagnostic of `NOTE_OP1_m4_scaling_2026-06-12.md`. Engine: `ENGINE_OP1_m4_harmonic_decomposition.py` → `CERT_OP1_m4_harmonic_decomposition.json` (17 rows: L ∈ {4,6,8} × s ∈ {1, 1.25, 1.5, 2, 3} + L=12 at s ∈ {1, 3}; resumable, state-file, deadline-aware). Conventions: α_W = β/6 (Casimir row of `theory/DOC_GOV_conventions.md`), v₀ = 1.

## Exact structure (gated, not assumed)

im P = H ⊕ C orthogonally with dim H = 4: the constant-direction 1-forms h_μ satisfy L₁up h_μ = 0, d₀ᵀh_μ = 0, P h_μ = h_μ (GATE G1, ≤1e-12). Hence M h_μ = m₀² h_μ and G_P = G_H + G_C with G_H G_C = 0, giving **exactly**

T_full(b) = T_H + T_C(b),  **T_H = 1/(m₀⁴·L⁴)**,  g_H = 1/(m₀²·L⁴)  (closed form).

On the physical diagonal (m₀² = m̄²a², L = ℓ/a): m₀⁴L⁴ = m̄⁴ℓ⁴ ⇒ **T_H is exactly constant along the diagonal** (0.015625 in anchor units at every point). Verified per-row: numeric harmonic projection vs closed form ≤1e-10 (G4); T_C computed two independent ways — direct CG on the harmonic-deflated source vs subtraction — agreeing ≤1e-8, cross term <1e-10 (G3); anchors reproduce `CERT_OP1_kernel_consts.json` at (4,6.4),(6,7.2),(4,5.6),(6,5.6) rtol 1e-6 (G2/G2b).

## Findings (computed facts)

**1. The fixed-L collapse is entirely harmonic.** At (L=4, s=3): T_H/T_full = 98%; N\* collapses 29→0 while N\*_C stays 53→44. The m₀²→0 explosion is the rank-4 sector where M⁻¹ = 1/m₀².

**2. The coexact remainder is scaling-stable to ×1.63.** T_C across the entire 17-row grid sits in **[0.0188, 0.0308]** while T_full spans ×59.

**3. Physical diagonal (the meaningful trajectory):**

| (L, s) | β | T_full | T_H (exact const) | T_C | N\* | N\*_C | **N\*_split** |
|---|---|---|---|---|---|---|---|
| (4, 1.0) | 5.600 | 0.034463 | 0.015625 | 0.018838 | 29 | 53 | **30** |
| (6, 1.5) | 5.657 | 0.039208 | 0.015625 | 0.023583 | 25 | 42 | **33** |
| (8, 2.0) | 5.697 | 0.042330 | 0.015625 | 0.026705 | 23 | 37 | **32** |
| (12, 3.0) | 5.753 | 0.046382 | 0.015625 | 0.030757 | 21 | 32 | **30** |

T_C grows slowly (+25%/+13%/+15% per refinement step — **not saturated in three steps; no limit claim**). N\*_C erodes 53→32; plain N\* erodes 29→21.

**4. Split certificate (sharper than pure HS, same probability-free character).** The harmonic block of Π_D G_P Π_D is rank ≤ 4 with **exact** norm: its 4×4 Gram is diagonal, λ_H = max_μ |D_μ|/(m₀²L⁴) (|D_μ| = defects of orientation μ; engine uses worst case |D_μ| = |D|). The coexact block keeps the HS bound. So

θ ≤ v₀·[ |D|/(m₀²L⁴) + √(|D|·T_C) ],  N\*_split = max |D| with RHS < 1.

N\*_split is **nearly flat along the diagonal: 30→33→32→30**, vs N\* 29→25→23→21 (+43% at the finest point). The per-defect harmonic coefficient on the diagonal is 1/(m₀²L⁴) = a²/(m̄²ℓ⁴) → 0 like a²: the harmonic term costs nothing in the continuum direction; the certificate's scaling fate rests on T_C alone.

## Consequence for M4 assembly (and what stays open)

The comparator's scaling instability is isolated in a finite-dimensional, explicitly diagonalized sector that the split certificate handles **exactly** — the M4 closure note can target (S) against the near-constant coexact budget (N\*_C ≈ 32–53 at these volumes) plus an a²-vanishing harmonic term, instead of the collapsing single-HS budget. What this does NOT do: it is finite-L computation (L ≤ 12, three refinement steps); the T_C diagonal growth is unresolved beyond ×3 refinement; v₀'s physical scaling remains a modeling input for Alex's sign-off; whether the split form is the right interface for (S)/M3a is Alex's determination.

**RESOLVED June 12 (same day, late pass, under DECISIONS #009):** T_C is now exact at every (L, m₀², β) via the momentum-space closed form, and the diagonal is computed to s = 128 — **logarithmic growth, no saturation**, with the (S)-side consequence (closure condition q + c_af·κ > 2) quantified. See `NOTE_OP1_m4_tc_asymptotics_2026-06-12.md`; its json supersedes this note's diagonal values (which carry ≤1.5e-5 CG noise). The v₀ sign-off item is upgraded there from "modeling input" to the decisive M4 input.

## Run record + data integrity

ALL GATES PASSED, 17/17 rows (first run June 12, 2026, ~10 s total; L=12 row Nl=82,944 ≈ 1 s/solve). Cold rerun to a fresh state file: 17/17 rows reproduce, integer certificates (N\*, N\*_C, N\*_split) **identical**, worst float rel dev 1.5e-5 ~~(CG path noise; within gate tolerances)~~. **[Attribution corrected later June 12 (closed-form review, F027): the 1.5e-5 is a β-rounding generation mix, not CG noise — 13 of this json's rows were computed at the 4-decimal-rounded β (carried over from the scaling-state era of the chunked run) and 4 fresh rows (s=1.25 ×3, (12,3)) at exact β(s); the cold rerun used exact β throughout, so the mixed rows show the cross-reading offset ≤1.5e-5. CG itself is exact to ≤1e-9 here. No integer certificate is affected under either reading. Exact regeneration: `ENGINE_OP1_m4_tc_closed_form.py` / `ENGINE_OP1_m4_tc_fourier.py`.]** **Data-integrity note:** `CERT_OP1_m4_scaling_tables.json` is missing its s=1.0/1.25 rows — `ENGINE_OP1_m4_scaling_tables.py` overwrites rather than accumulates across chunked invocations; the values its NOTE quotes are nevertheless correct (this engine reproduces them independently). This engine is self-contained (recomputes the full AF ladder) and supersedes that json as the M4 data source.
