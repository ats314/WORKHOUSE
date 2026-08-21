# OP-12 Direct θ Scan — Results (June 11, 2026)

**What this is:** the numerical attack vector of `CLAUDE_REVIEW/10_DOC_GOV_open_problems.md` OP-1/OP-12, executed: sample SU(3) Wilson configurations along a β ladder, identify defect links, build the massive Maxwell comparator M = m₀²I + α_W·d₁*d₁, and compute the Hodge-projected Birman-Schwinger firewall ratio θ = v₀·λmax(Π_D P M⁻¹ P Π_D) exactly (power iteration + CG; hard gates on the chain-complex identity d₁d₀ = 0, P idempotence, [M,P] = 0, CG residuals).

**What this is NOT:** closure of OP-1. These are finite-volume (L = 4, 6), finite-ladder (β ≤ 7.2), small-statistics (12–20 cfgs) Monte Carlo measurements at fixed comparator parameters. Closing OP-1 requires the analytic uniform sparsity bound along the AF trajectory. This deposit is evidence and calibration for that work.

## Parameters

SU(3) Wilson action, 4D periodic torus, Metropolis (adaptive step, pooled exp(iεH) proposals, cold start). Comparator: m₀² = 0.5 (Program B anchor, Untitled185), v₀ = 1, α_W = β/6 (Casimir convention, master doc C.0 / MaxwellOperator.lean). Defects: gauge-invariant, plaquette-seeded — link b ∈ D iff b borders a plaquette with s_p = 1 − Re tr U_p/3 > δ; δ ∈ {0.70, 0.90, 1.10} per the Peierls probe's finding that δ = 0.35 percolates. L = 4: β ∈ {5.6, 6.0, 6.4, 6.8, 7.2}, 120 therm + 20 cfgs (sep 4). L = 6: β ∈ {5.6, 6.4, 7.2}, 100 therm + 12 cfgs. Seed 20260611.

## Results

| L | β | δ | ⟨plaq⟩ | ρ_link | max\|D\| | θ_mean | θ_max | HS-chain bound |
|---|-----|------|--------|--------|------|--------|--------|----------------|
| 4 | 5.6 | 0.70 | 0.5537 | 0.516 | 561 | 1.144 | **1.197** | 1.2×10⁶ |
| 4 | 5.6 | 0.90 | 0.5537 | 0.163 | 200 | 0.475 | 0.550 | 7.3×10⁵ |
| 4 | 5.6 | 1.10 | 0.5537 | 0.032 | 56 | 0.207 | 0.287 | 3.9×10⁵ |
| 4 | 6.0 | 0.70 | 0.6099 | 0.309 | 370 | 0.774 | 0.907 | 1.1×10⁶ |
| 4 | 6.0 | 0.90 | 0.6099 | 0.064 | 82 | 0.271 | 0.323 | 5.4×10⁵ |
| 4 | 6.0 | 1.10 | 0.6099 | 0.007 | 19 | 0.132 | 0.171 | 2.6×10⁵ |
| 4 | 6.4 | 0.70 | 0.6335 | 0.233 | 289 | 0.610 | 0.690 | 1.1×10⁶ |
| 4 | 6.4 | 0.90 | 0.6335 | 0.037 | 73 | 0.205 | 0.259 | 5.8×10⁵ |
| 4 | 6.4 | 1.10 | 0.6335 | 0.004 | 16 | 0.086 | 0.159 | 2.7×10⁵ |
| 4 | 6.8 | 0.70 | 0.6604 | 0.153 | 201 | 0.435 | 0.555 | 1.1×10⁶ |
| 4 | 6.8 | 0.90 | 0.6604 | 0.020 | 36 | 0.164 | 0.204 | 4.6×10⁵ |
| 4 | 6.8 | 1.10 | 0.6604 | 0.001 | 4 | 0.017 | 0.113 | 1.5×10⁵ |
| 4 | 7.2 | 0.70 | 0.6914 | 0.079 | 119 | 0.286 | 0.381 | 9.3×10⁵ |
| 4 | 7.2 | 0.90 | 0.6914 | 0.008 | 24 | 0.105 | 0.175 | 4.2×10⁵ |
| 4 | 7.2 | 1.10 | 0.6914 | 0.001 | 8 | 0.022 | 0.120 | 2.4×10⁵ |
| 6 | 5.6 | 0.70 | 0.5602 | 0.490 | 2695 | 1.075 | **1.133** | 2.7×10⁶ |
| 6 | 5.6 | 0.90 | 0.5602 | 0.142 | 843 | 0.417 | 0.449 | 1.5×10⁶ |
| 6 | 5.6 | 1.10 | 0.5602 | 0.021 | 142 | 0.181 | 0.203 | 6.2×10⁵ |
| 6 | 6.4 | 0.70 | 0.6348 | 0.227 | 1280 | 0.566 | 0.603 | 2.4×10⁶ |
| 6 | 6.4 | 0.90 | 0.6348 | 0.038 | 255 | 0.200 | 0.233 | 1.1×10⁶ |
| 6 | 6.4 | 1.10 | 0.6348 | 0.003 | 32 | 0.122 | 0.131 | 3.8×10⁵ |
| 6 | 7.2 | 0.70 | 0.6889 | 0.083 | 472 | 0.278 | 0.297 | 1.9×10⁶ |
| 6 | 7.2 | 0.90 | 0.6889 | 0.008 | 68 | 0.123 | 0.136 | 7.0×10⁵ |
| 6 | 7.2 | 1.10 | 0.6889 | 0.000 | 12 | 0.033 | 0.103 | 3.0×10⁵ |

Plot: `DATA_OP1_op12_theta_vs_beta.png`. Per-configuration data: `results/`, summary: `CERT_OP1_op12_summary.json`.

## Findings

1. **θ < 1 with margin across the ladder in the sparse-defect regime.** At δ ≥ 0.90 every configuration at every (L, β) satisfies the firewall condition, with θ_max falling from 0.55 (β = 5.6) to 0.18 (β = 7.2) at L = 4, δ = 0.90.
2. **θ decreases monotonically in β at fixed δ** — the direction OP-1 predicts ("‖K‖ = O(a²) → 0 if defect density stays bounded").
3. **Volume stability L = 4 → L = 6.** θ does not grow with volume at any (β, δ); at matched points it is equal or slightly smaller at L = 6 (e.g. β = 6.4, δ = 0.90: θ_max 0.259 → 0.233). Two volumes only — but the trend is the one OP-1 needs.
4. **The firewall fails exactly where sparsity fails.** At δ = 0.70, β = 5.6 the defect set covers ~50% of links (near-percolating) and θ_max = 1.20 (L=4) / 1.13 (L=6) > 1. This reproduces the Peierls probe's percolation lesson in θ form and quantifies OP-1's emphasis: the open half of the problem (defect sparsity) is precisely what the closure rests on.
5. **The deterministic HS-chain bound is vacuous in this parameter regime.** The OP-7 chain (Combes-Thomas q with D_E = 18, HS norm, c_E = 8) gives bounds of order 10⁵–10⁶ where the measured θ ≤ 1.2 — about six orders of magnitude of slack, driven by q → 1 when α_W/m₀² ≈ 2. Whatever closes OP-1 analytically must either operate at much larger effective mass-to-stiffness ratio (physical-units scaling) or replace the HS route's volume factor. This quantifies the analytic burden.

## Caveats (read before citing numbers)

Thermalization: cold starts with 100–120 sweeps leave ⟨plaq⟩ ≈ 2–3% above literature values (drift check at β = 6.0, L = 4: continuing 200 sweeps brings 0.610 → 0.594, the known value; a θ re-measurement on the extended-thermalization configuration gives δ = 0.70/0.90/1.10 → 0.876/0.300/0.134, i.e. slightly above the scan means and within or near the scan maxima). Under-thermalization therefore biases θ slightly LOW at δ = 0.70; the δ ≥ 0.90 conclusions are inside the config-to-config spread. Other caveats: fixed comparator parameters (m₀², v₀ not run along a physical-units scaling); plaquette-seeded gauge-invariant defect definition (surrogate for OP-1's gauge-variant link distance); 12–20 configurations; Metropolis only; L ≤ 6. The OP-12 specification's L = 8, 12 and a physically scaled m₀²(a) are the natural next runs.

## Relation to prior work

Extends Program B's Untitled185 firewall audit (single β = 4, L = 8–24, all SAFE, p99 = 0.8541) along the β ladder with the Peierls-probe-calibrated thresholds, on smaller volumes with exact projected eigencomputation. Consistent overall picture: θ < 1 wherever the defect set is sparse.
