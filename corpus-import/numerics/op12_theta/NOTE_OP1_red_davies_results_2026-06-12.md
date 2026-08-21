# Red Davies Insertion — Results (June 12, 2026, review unit #10d / F020)

**What this is:** the June-11 kchain accounting re-run with the Davies-type decay rates from `E:\YANG\ORGANIZED\02_APPENDICES\red_propositions\` (Prop 9.X; Defs C₀/C_∂; Prop 9.X′; Cor 9.X″) in place of Combes–Thomas. Chain structure (Ξ shell sum, prefactor, |D| factor) byte-identical to `ENGINE_OP1_kchain_ledger.py` — gate G3 recomputes the stored June-11 bounds to 1e-9 relative. Engine: `ENGINE_OP1_red_davies_kchain.py` (35 hard gate checks across 7 families G1–G7, all pass, 1.6 s; JSON byte-identical on cold rerun); data: `CERT_OP1_red_davies_kchain.json`. Working copies of the propositions with provenance: `programs/op1_defect_sparsity/red_davies_toolkit/`.

## Row-sum constants (exact, configuration-independent)

C₀(Δ₁) = C_∂(Δ₁) = D_E = **18** at L = 4 and L = 6 (all off-diagonal entries of d₁ᵀd₁ have magnitude 1; worst row crosses level sets at every neighbor). **Props 9.X′/9.X″ buy nothing for this comparator** — the entire effect below is Prop 9.X's arcosh (Davies) rate vs the log (CT) rate.

## Chain bounds on the stored cases (m₀² = 0.5, α_W = β/6, v₀ = 1)

| L | β | δ | \|D\| | HS_meas | bound CT | bound Davies | tighter × | S_kernel CT → Davies |
|---|-----|-----|------|---------|----------|--------------|-----------|----------------------|
| 4 | 5.6 | 0.7 | 561 | 3.888 | 1.23×10⁶ | 9.21×10³ | 133 | 3.2×10⁵ → 2.4×10³ |
| 4 | 5.6 | 0.9 | 192 | 1.824 | 7.19×10⁵ | 5.39×10³ | 133 | 3.9×10⁵ → 3.0×10³ |
| 4 | 6.4 | 0.9 | 30 | 0.591 | 3.70×10⁵ | 2.43×10³ | 153 | 6.3×10⁵ → 4.1×10³ |
| 4 | 7.2 | 0.9 | 4 | 0.191 | 1.71×10⁵ | 9.95×10² | 172 | 9.0×10⁵ → 5.2×10³ |

Per-√|D| chain constant: 5.2–8.5×10⁴ (CT) → **389–497** (Davies) vs exact c = √T_full = 0.127–0.186 ⇒ residual analytic slack **2.1–3.9×10³** across the full (L, β) grid.

## Validity checks

Pointwise Davies bound (2/m²)e^(−η·dist) dominates exact M⁻¹ columns at the sharpest admissible η on all orientation orbits: max measured/bound = 0.153 (L=4, β=5.6), 0.150 (L=6, β=6.4). All Davies bounds dominate measured HS norms on stored cases (G6). Red-006's printed sanity numbers reproduced (G1).

## Caveats

(i) The propositions bound M⁻¹ entries; the chain applies them to G_P = PM⁻¹P exactly as the June-11 ledger did — the P-transfer step is OP-7-write-up content, not established here. (ii) Chain-level certification remains vacuous at these parameters (bound < 1 needs |D| ≲ 10⁻⁵): the Davies form matters for the analytic/asymptotic chain, not as a finite certificate — the exact-kernel N\* route (KCHAIN_LEDGER §3) remains the certificate. (iii) Fixed comparator parameters as in the June-11 ledger; η values are parameter-relative.
