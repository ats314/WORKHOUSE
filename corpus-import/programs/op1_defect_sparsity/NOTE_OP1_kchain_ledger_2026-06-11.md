# K-Chain Slack Ledger and Exact Kernel Constants (June 11, 2026)

**What this is:** a step-by-step audit of where the deterministic OP-7 chain (Combes-Thomas → HS norm → shell sum) loses its ~10⁶ factor against the measured Birman-Schwinger θ, followed by exact computation of the quantities the chain estimates. Companions: `ENGINE_OP1_kchain_ledger.py/.json` (slack decomposition on stored OP-12 configurations), `ENGINE_OP1_kernel_consts.py/.json` (exact configuration-independent kernel constants). Diagnostics and exact finite-lattice computations only — the stochastic content of OP-1 is untouched and open.

## 1. Slack decomposition (stored L = 4 final configurations, m₀² = 0.5, α_W = β/6, v₀ = 1)

| β | δ | \|D\| | θ_op (measured) | ‖K‖_HS (exact) | chain bound (q_CT) | S_int = HS/θ | S_kernel = bound/HS |
|-----|-----|------|--------|--------|------------|------|----------|
| 5.6 | 0.7 | 561 | 1.187 | 3.888 | 1.2×10⁶ | 3.3 | 3.2×10⁵ |
| 5.6 | 0.9 | 192 | 0.517 | 1.824 | 7.2×10⁵ | 3.5 | 3.9×10⁵ |
| 6.4 | 0.9 | 30 | 0.196 | 0.591 | 3.7×10⁵ | 3.0 | 6.3×10⁵ |
| 7.2 | 0.9 | 4 | 0.108 | 0.191 | 1.7×10⁵ | 1.8 | 8.9×10⁵ |

(‖K‖_HS computed exactly via the defect-basis Gram matrix — up to 561 projected CG solves per row; eigenvalues of the Gram reproduce θ_op, cross-validating the power iteration.)

**Reading:** the HS→operator-norm step costs only a factor 1.8–3.5. Essentially the entire 10⁵–10⁶ sits in the chain's *estimate of the HS norm itself* — the Combes-Thomas decay constant q_CT = (1 + m₀²/(2α_W·18))⁻¹ ≈ 0.985–0.989 feeds a shell sum Ξ₂,tot ≈ 10⁷–10⁸ where the true kernel mass is O(10⁻²). (A decay-*rate* measurement is not extractable at L = 4 — the link-adjacency graph has diameter ~2–3 — but it is also unnecessary, per §2.)

## 2. The kernel is configuration-independent — so compute it, don't bound it

M = m₀²I + α_W d₁*d₁ and the Hodge projector P depend only on the lattice, **not on U**. Hence in

    tr K² = v₀² Σ_{b,b' ∈ D(U)} G_P(b,b')²,    G_P = P M⁻¹ P,

the kernel G_P is a fixed, exactly computable object; only the index set D(U) is random. The chain's CT step is an *estimate* of G_P's row mass — replaced here by exact computation (translation invariance ⇒ 4 orientation orbits ⇒ 4 projected solves per (L, β)):

| L | β | g_diag = max G_P(b,b) | T_full = max_b Σ_{b'} G_P(b,b')² | c = √T_full | **N\* = ⌊1/(v₀²T_full)⌋** |
|---|-----|---------|----------|--------|------|
| 4 | 5.6 | 0.1153 | 0.03446 | 0.186 | 29 |
| 4 | 6.0 | 0.1088 | 0.03228 | 0.180 | 30 |
| 4 | 6.4 | 0.1030 | 0.03046 | 0.175 | 32 |
| 4 | 6.8 | 0.0978 | 0.02893 | 0.170 | 34 |
| 4 | 7.2 | 0.0931 | 0.02762 | 0.166 | 36 |
| 6 | 5.6 | 0.1111 | 0.02350 | 0.153 | 42 |
| 6 | 6.0 | 0.1044 | 0.02119 | 0.146 | 47 |
| 6 | 6.4 | 0.0985 | 0.01925 | 0.139 | 51 |
| 6 | 6.8 | 0.0933 | 0.01761 | 0.133 | 56 |
| 6 | 7.2 | 0.0886 | 0.01621 | 0.127 | 61 |

## 3. The probability-free certificate this yields

By the framework's own HS step with the kernel sum taken exactly (elementary: Σ_{b,b'∈D} G² ≤ |D|·max_b Σ_{b'} G²):

    ‖K‖_op ≤ ‖K‖_HS ≤ v₀ √( |D| · T_full )   ⟹   **θ < 1 whenever |D| ≤ N\*.**

No Combes-Thomas, no probability, no cluster expansion — a finite computation per (L, β). Against the chain's per-√|D| constant (2v₀/m₀²)√Ξ ≈ 5.6×10⁴, the exact constant is c ≈ 0.13–0.19: a ~3×10⁵ improvement, matching §1's S_kernel.

**Validation against the OP-12 scan:** every scan point with max|D| ≤ N\* indeed had θ_max < 1 (e.g. L=4, δ=1.1, β ≥ 6.0: |D| ≤ 19 ≤ 30 ✓; L=6, δ=1.1, β=7.2: |D|=12 ≤ 61 ✓). Points beyond N\* are simply *uncertified* by this route, not violated — e.g. L=4, β=5.6, δ=0.9 has |D|=192 > 29 yet measured θ = 0.52: the worst-case bound concedes a further ~(HS/θ)·(mixing of orbits) factor that a sharper deterministic argument could recover.

**Trends worth noting (computed facts, not claims):** T_full *decreases* with β at fixed L and *decreases* from L=4 to L=6 at fixed β — both in the direction OP-1 needs; N\* grows correspondingly. The scan's measured defect counts at δ = 1.1 (4–56 at L=4, 12–142 at L=6) straddle N\*: certification of typical configurations at fixed parameters is within reach of either slightly sharper kernel accounting (pair-distance-weighted sums instead of worst-case row mass) or slightly sparser defect regimes.

## 4. What remains open (unchanged)

The certificate converts OP-1's deterministic half into exact arithmetic, but the *stochastic* half — that D(U) is sparse, P-typically and uniformly along the AF trajectory (the Peierls inclusion bound the probe tests, with αβδ beating the animal-counting entropy) — is the open mathematical content, exactly as OP-1 states. The pair-correlation refinement (Σ_{b,b'∈D} weighted by inclusion probabilities ρ₁, ρ₂(dist)) would tighten |D|·T_full to ρ-weighted kernel sums; the inequality on ρ remains for analytic work.

## Caveats

Fixed comparator parameters (m₀² = 0.5, v₀ = 1, α_W = β/6); N\* is parameter-relative and L-relative (computed exactly at L = 4, 6; the L-trend is favorable but not a limit statement); T_full uses the worst orientation orbit; CG tolerance 1e-12 (gates as in ENGINE_OP1_op12_runner.py); the §1 table uses final-state configurations (thermalization caveat as in NOTE_OP1_results_2026-06-11.md).
