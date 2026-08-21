# M4 T_C asymptotics — exact closed form, the log law, and the (S)-interface (June 12, 2026, late pass)

Resolves the last open computational item of `NOTE_OP1_m4_harmonic_decomp_2026-06-12.md` ("T_C beyond ×3 refinement — no limit claim"). **First pass executed under DECISIONS #009** (agents do the mathematics); every claim below carries its grounds label. Conventions: α_W = β/6 (Casimir row, `theory/DOC_GOV_conventions.md`), v₀ = 1 unless stated, anchor a = 1 at β₀ = 5.6, physical diagonal L = 4s, m₀² = 0.5/s², β(s) = 5.6 + 2c_af ln s, c_af = 11N/48π².

## 1. Closed form for the coexact budget [derived + machine-verified]

On the flat 4-torus the link complex diagonalizes in momentum space: with g(k)_μ = e^{ik_μ}−1, λ(k) = Σ_ν 4sin²(k_ν/2), the transverse (= im P, k ≠ 0) projector is P_T(k) = I − g g†/λ, the four k = 0 modes are exactly the harmonic sector of the DECOMP note, and Δ₁ = λ(k)·I₄ componentwise so Δ₁up|_T = λ(k)I. For the source link b = (0, μ): T_C(μ) = (1/Ns)Σ_{k≠0}(P_T)_{μμ}/(m₀²+αλ)². Coordinate-permutation symmetry makes this μ-independent, and tr P_T = 3 exactly, so

**T_C = (3/4)·S₂,  S₂ = (1/Ns) Σ_{k≠0} (m₀² + α_W λ(k))⁻²,  T_H = 1/(m₀⁴Ns),  T_full = T_H + T_C.**

No CG solves, no sparse matrices: T_C at any (L, m₀², β) is an exact lattice sum. Independent route (same engine): S₂ = ∫₀^∞ t e^{−m₀²t}(q(α_W t)⁴ − 1/Ns)dt with q(u) = (1/L)Σ_n e^{−4u sin²(πn/L)}.

**Verification (all hard-gated, `ENGINE_OP1_m4_tc_fourier.py` + `ENGINE_OP1_m4_tc_realspace_check.py`):** F1 per-μ identity on full 4D grids (≤1e-12, L=4,6); F2 all 10 `CERT_OP1_kernel_consts.json` anchors reproduced at **2.0e-15** — the formula *is* the June-11 kernel, exactly; F3 all 17 deposited DECOMP rows at ≤1.5e-5 — **attribution corrected same day (parallel closed-form review, confirmed independently here): this is NOT CG noise but a β-rounding generation mix in the DECOMP json** (13 rows computed at the 4-decimal-rounded β incl. the four s=1 ties where both readings coincide, 4 rows at exact β(s); max cross-reading 1.54e-5 at (4, s=3); no integer radius affected; CG at these tolerances is actually exact to ≤1e-9, cf. the L=16/24 cross-check below at 1e-15 — see `NOTE_OP1_m4_tc_closed_form_2026-06-12.md` §2 and finding F027); F4 k-sum vs t-integral ≤2e-15 at every L ≤ 256; F5 quadrature self-refinement ≤1e-9. **Real-space cross-verification** at the new sizes by an end-to-end independent algorithm (vectorized sparse complex gated *exactly* against `R.lattice(8)`; kron-built L1up gated exactly against d₁ᵀd₁ at L=8,16; Hodge-projected CG, residual-gated): (L=16, s=4) four directions + the unsplit full-solve identity G3/G4; (L=24, s=6) two directions; **Fourier-vs-CG deviation ≤ 6.8e-15**, direction spread ≤ 4.4e-15. Cold reruns of both engines to fresh state paths reproduce **bit-identically** (worst rel dev 0.00e+00; integer certificates identical).

## 2. The diagonal to s = 128: a clean log law, no saturation [computed fact + derived asymptote]

Diagonal extended ×42 beyond the morning grid (s = 1 → 128, L = 4 → 512; k-sum exact to L = 256, gated quadrature beyond):

| s | L | β | T_C | α²T_C | N\* | N\*_C | N\*_split |
|---|---|---|---|---|---|---|---|
| 1 | 4 | 5.600 | 0.018838 | 0.016410 | 29 | 53 | 30 |
| 3 | 12 | 5.7531 | 0.030757 | 0.028277 | 21 | 32 | 30 |
| 6 | 24 | 5.8496 | 0.036982 | 0.035151 | 19 | 27 | 26 |
| 16 | 64 | 5.9863 | 0.044815 | 0.044610 | 16 | 22 | 22 |
| 48 | 192 | 6.1393 | 0.052640 | 0.055113 | 14 | 18 | 18 |
| 128 | 512 | 6.2760 | 0.058930 | 0.064475 | 13 | 16 | 16 |

(full 16-row table: `CERT_OP1_m4_tc_fourier.json`). Findings:

1. **No saturation.** The saturating fit c₀ − c₁/s through s ∈ [2,6] (the best one could do with the morning's data) predicts T_C(128) ≤ 0.0412; actual is 0.0589 — **43% above the predicted ceiling**.
2. **The law.** IR analysis of the explicit sum (4D density of states k³dk against (m₀²+αk²)²; on the diagonal the mass and volume cutoffs lock, m₀²L²/α = 8/α) gives α²T_C = (3/64π²)(2 ln s + ln α + C) + O(s⁻²). Measured: local slopes d(α²T_C)/d ln s decrease **monotonically** 0.01122 → 0.009543 (s: 1→128) toward the derived **3/32π² = 0.0094989** (+0.47% at the last step); the two-parameter fit on s ≥ 8 returns coefficient **0.9955 × (3/64π²)**, C = 3.890, residual rms 1.2e-5. Grounds: the sum is exact; the asymptote is a standard IR estimate of that sum, confirmed by the data at the half-percent level. [derived-unverified beyond this window: the O(s⁻²) tail shape]
3. **Certificate erosion is logarithmic with computed coefficient.** N\*_split ≈ 64π²α²/(3(2 ln s + ln α + C)): erodes 30 → 16 over a ×128 refinement. The harmonic per-defect cost dies as a² (m₀²L⁴ = 128s² on the diagonal) — T_C alone owns the asymptotics, as the DECOMP note anticipated.
4. **Curiosity, not load-bearing:** with AF running, the fitted law peaks at ln s ≈ 36.2 (s ~ 5×10¹⁵, T_C ≈ 0.116) and then decays ∝ 1/ln s; N\* eventually *regrows* ∝ α²/ln s. Unreachable physically; recorded because it is the exact asymptotic shape of the comparator object. [derived from the fitted law + AF running]

## 3. The (S)-interface: what the log law demands, and what the MC data say [computed; consequences labeled]

Split-certificate algebra with v₀ = c_v a^q and a Peierls ansatz ρ_P(β; δ) ~ e^{−κ(δ)β} for fixed-threshold defects, along the diagonal (E[#bad plaquettes] = 6L⁴ρ_P = 1536 s⁴ρ_P, hence E|D| ≤ 4·that = 6144 s⁴ρ_P — *prefactor display corrected June 12 late; exponents and all conclusions unaffected*):

**θ_HS ~ s^{2−q−c_af·κ}·√(ln s)  ⇒  closure condition q + c_af·κ > 2.**

- **q = 0 (v₀ fixed, the current normalization) requires κ > 2/c_af = 32π²/11 = 28.712.** Measured from the stored OP-12 ensembles (8 ensembles, L=4/6, β=5.6–7.2; count-weighted WLS, volume-stability z ≤ 2.5 gated): **κ̂ = 1.24±0.01 (δ=0.7), 1.85±0.03 (δ=0.9), 2.57±0.15 (δ=1.1)** — 4–9% of required. Worse, structurally: the Wilson action cost of a single plaquette is ≤ 2β, capping κ(δ) at O(2–4) for *every* fixed δ ≤ 2. **The q = 0 route is closed — not empirically short, unreachable.** [measurement + heuristic ceiling argument; ceiling labeled heuristic]
- **q = 2 (v₀ carries the canonical a² of the comparator's other dimensionful couplings): ANY exponential sparsity closes the diagonal** — θ ~ s^{−c_af·κ}√(ln s) → 0; at the measured κ̂ the exponents are −0.087/−0.129/−0.179 (slow but strictly closing).
- **Breakeven: q\*(δ) = 2 − c_af·κ̂(δ) = 1.91 / 1.87 / 1.82.** Anything ≥ ~1.9 closes at every measured threshold.

**Consequence (the load-bearing sentence): the v₀ physical-scaling sign-off flagged in the morning notes is not a refinement — M4's diagonal viability is equivalent to it.** With q = 0 the conditional closure note cannot be assembled (defect proliferation s^{3.6–3.8} beats a 1/ln s budget); with q = 2 it goes through with margin for any exponential Peierls bound, i.e. (S) could even be weakened. This also sharpens what M3a must deliver: not raw κ size, but (i) any strictly positive exponential rate, plus (ii) the concentration/tail layer (the E-level condition above is necessary, not sufficient — P(|D| > budget) summability is still (S)'s job, with the W(r)/ρ₂ pair structure unchanged as the sharper interface).

Honest caveats: κ̂ from a narrow β window (5.6–7.2), volumes L = 4/6, 12–20 correlated configs (Poisson SEs indicative); fixed-δ defect family only (the δ(a) ↑ family is capped by s_p ≤ 2 and cannot rescue q = 0); all statements are about the comparator certificate chain, not directly about YM dynamics; v₀'s q is a modeling/normalization decision = **Alex's**, now with its consequences computed on both branches.

## 4. Artifacts, reproduction, incidents

`ENGINE_OP1_m4_tc_fourier.py` → `CERT_OP1_m4_tc_fourier.json` (16 diagonal rows + gates F1–F5 + analysis block; ~30 s single pass, resumable, L=256 row chunk-safe). `ENGINE_OP1_m4_tc_realspace_check.py` → `CERT_OP1_m4_tc_realspace_check.json` (+ `opcache/` — regenerable sparse-operator cache for L=8/16/24, ~73 MB compressed, safe to delete). `ENGINE_OP1_m4_sparsity_interface.py` → `CERT_OP1_m4_sparsity_interface.json` (gates D1–D4). Cold reruns: bit-identical (§1). **Incident (mount-cache hazard, new failure mode):** the VM mount served a stale-truncated view of `ENGINE_OP1_m4_sparsity_interface.py` that was *syntactically valid* (ended at a bare `print`) and silently executed partially; the Windows-side file was verified complete via direct read, and the run was completed from a /tmp copy. Guard adopted: engines end with a terminal sentinel print (`wrote <json>` / `ALL GATES PASSED`) — **treat any engine output lacking its sentinel as a partial run.** Also repaired in passing: an earlier tail-splice in that file from editing against the stale view (full rewrite deposited; no other file affected).
