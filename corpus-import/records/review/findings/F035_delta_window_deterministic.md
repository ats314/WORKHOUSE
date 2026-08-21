# F035 — The δ-window is one-sided on the deterministic side: the firewall only *strengthens* as δ grows (June 12, 2026)

> **⚠ PARTIAL RETRACTION (F036, same day).** The recommendation below to "adopt δ = 1.3" is **withdrawn**. F035's measured result — the *in-model* firewall θ falls monotonically as δ grows — is correct, but F036 computes the comparator-validity upper edge F035 left to "Alex's call" and finds it is **δ_max ≤ 1** (the comparator M = m₀²I + α_W d₁*d₁ is a positive operator and cannot represent a plaquette whose per-plaquette curvature tr H = (4/3)(1−s_p) has gone net-negative, i.e. s_p > 1; strict onset of a negative direction at s_p\* = 2/3). So the model V = v₀Π_D is **unfaithful for δ > 1**, and δ = 1.3 is not a valid operating point. The faithful range is δ ≤ 1 (legacy δ ≈ 0.9 sits correctly inside [2/3, 1]); the δ-window is a narrow band ≈ [0.9, 1], and δ-tuning buys no free Tier-R gain. The in-model conclusions below (θ falls, monotone, G-DW gates) stand as in-model statements. See `F036_delta_max_comparator_faithfulness.md`.

**Unit:** #56 (own-initiative computation, the cheapest of F034's three ranked redirects — the "δ-window" option). **Verdict: a clean POSITIVE result for the (D) side, with one honest limit.** The F034 redirect asked whether the **deterministic firewall θ < 1 survives in the larger-δ window** where the (S) chessboard Tier-R rate β(δ−1) clears the rooted threshold at much lower β (β_c = 39.96 → 8.88 as δ = 1.10 → 1.45). Direct re-measurement on the deposited thermalized MC states gives an unambiguous answer for the part that is measurable: **θ falls monotonically as δ grows** — at the anchor (β = 5.6) θ_max goes 0.31 → 0.18 → 0.16 across δ = 1.1 → 1.2 → 1.3 — so the deterministic side imposes **no upper θ-ceiling** on δ; raising δ only buys margin. The single honest limit: above δ ≈ 1.35 defects that deep simply do not occur on L ≤ 6, so the firewall there is **statistically untestable on these volumes** (θ = 0 trivially, no defects to test), not proven-safe. **Net: δ ∈ [1.1, 1.3] is deterministically safe AND well-tested; adopting δ = 1.3 cuts the (S) Tier-R clearance distance from ln s ≈ 247 to ln s ≈ 55 — a 4.5× reduction, deterministically free.** The remaining upper edge of the window is a *comparator-validity* question (analytic, Alex), not a measured-θ obstruction. Engine: `numerics/op12_theta/s_chessboard/ENGINE_OP1_op12_delta_window.py` → `CERT_OP1_delta_window_summary.json` + `DATA_OP1_delta_window.png`; gates **G-DW1..G-DW6 PASS** (incl. G-DW5 δ=1.10 reproduction of the deposited scan, G-DW6 monotonicity).

## 1. The question and why this is the right object

OP-1's defect threshold δ is a parameter we choose: D_δ = {links bordering a plaquette with s_p = 1 − Re tr U_p/3 > δ}. The two halves of OP-1 both depend on it, in *opposite-looking* directions that turn out to align:

- **(S) chessboard side (F029, S_CHESSBOARD_ROUTE §5):** Tier-R gives P(Γ ⊂ D_δ) ≤ e^{−β(δ−1)|Γ|}, rooted-summable for β(δ−1) > log μ̄ = 3.996. Larger δ ⟹ larger rate ⟹ lower β_c. The table: β_c = 39.96 (δ=1.10), 19.98 (1.20), 13.32 (1.30), 9.99 (1.40), 8.88 (1.45); equivalently the trajectory must run to ln s ≈ 247, 103, 55, 32, 24 from the anchor before Tier-R alone covers it. **(S) wants δ large.**
- **(D) deterministic side (this finding):** larger δ ⟹ sparser D_δ ⟹ smaller θ = v₀·λmax(Π_D P M⁻¹ P Π_D). **(D) also likes δ large** — *provided the comparator M still controls the sub-δ plaquettes excluded from D_δ.*

So the naive worry — that the (S) side's appetite for large δ fights a (D)-side θ-ceiling — is **false in the measured regime**: both sides improve together. The genuine upper constraint is elsewhere (§4).

## 2. The measurement (MC evidence; same gated θ machinery as the deposited scan)

Method: load each deposited thermalized state (`op12_state/state_*.npz`, therm_done = 120/100, i.e. well past equilibration), continue the chain (8 re-equilibration sweeps + 16 configs × 4-sweep separation), and compute the **identical** Hodge-projected Birman–Schwinger ratio θ on the extended grid δ ∈ {1.10, 1.20, 1.30, 1.40, 1.45}. Comparator unchanged: m₀² = 0.5, v₀ = 1, α_W = β/6. Hard gates carried over: d₁d₀ = 0 (G-DW1), P² = P (G-DW2), [M,P] = 0 (G-DW3), CG convergence (G-DW4). **G-DW5 (consistency):** the δ = 1.10 column overlaps the deposited June-11 scan and reproduces it within the MC band at all 8 (L, β) — e.g. anchor mean 0.202 vs deposited 0.207; L6 b5.6 0.187 vs 0.181. **G-DW6:** θ monotone non-increasing in δ at every (L, β).

**θ_max over the ensemble:**

| L | β | δ=1.10 | 1.20 | 1.30 | 1.40 | 1.45 |
|---|---|---|---|---|---|---|
| 4 | 5.6 | 0.308 | 0.181 | 0.156 | — | — |
| 4 | 6.0 | 0.180 | 0.125 | — | — | — |
| 4 | 6.4 | 0.155 | — | — | — | — |
| 4 | 6.8 | 0.113 | 0.113 | — | — | — |
| 4 | 7.2 | 0.108 | — | — | — | — |
| 6 | 5.6 | 0.207 | 0.172 | 0.140 | — | — |
| 6 | 6.4 | 0.150 | 0.117 | — | — | — |
| 6 | 7.2 | 0.106 | 0.099 | 0.099 | — | — |

(— = no defects of that depth occurred in any of the 16 configs ⟹ θ = 0 trivially, **untested**, not safe-by-margin. Max defect-link counts: at the anchor max|D| = 65 → 24 → 8 → 0 → 0 across the grid for L=4; 170 → 62 → 8 → 0 → 0 for L=6.)

The **tested** window is δ ∈ [1.1, 1.3]: there the firewall is genuinely exercised (defects present in 31–100% of configs at the anchor) and θ_max ≤ 0.156 — a factor ≳ 6 below the θ = 1 threshold, with the margin *growing* in δ. Above δ ≈ 1.35 the test goes dark on L ≤ 6.

## 3. The deterministic verdict

**On the (D) side the δ-window is one-sided: it has a lower edge (sparsity — δ ≳ 0.9, below which D_δ percolates and θ > 1, the F029/RESULTS percolation lesson) and, in the measured regime, NO upper edge.** Raising δ from the legacy 1.10 to 1.30 leaves the firewall strictly safer (θ_max 0.16 vs 0.31 at the anchor) while handing the (S) side a 4.5× shorter clearance run (ln s 247 → 55). That trade is **deterministically free** and should be taken: δ = 1.3 (not 1.1) is the natural operating threshold for the joint (D)×(S) accounting. δ = 1.45 (β_c = 8.9, ln s ≈ 24) would be better still for (S), but the (D) side cannot *confirm* safety there on L ≤ 6 — see §4.

## 4. The real upper edge — and what it is (the remaining Alex input)

The upper edge of the δ-window is **not** a measured-θ failure; it is a *comparator-validity* condition that small-lattice MC cannot see:

1. **Comparator domination of excluded plaquettes (analytic — Alex's modeling call).** The firewall argument splits the operator into a defect part (D_δ, handled by θ < 1) and a background folded into M = m₀²I + α_W d₁*d₁. As δ grows, plaquettes with s_p ∈ (s_min, δ] — carrying progressively *larger* local potential — are excluded from D_δ and assigned to the controlled background. Validity requires M to still dominate them: there is a δ_max(m₀², α_W) above which an excluded plaquette's potential exceeds the comparator's reach and the split is no longer faithful. Quantifying δ_max requires the comparator-design criterion (the per-plaquette potential vs the M-spectrum floor), which is part of the v₀-scaling / comparator modeling Alex owns — **this finding does not settle it**, but localizes the upper-edge question precisely here, and notes it is independent of the measured θ data.
2. **Finite-volume detectability (numerical — resolvable).** Deep defects (s_p > 1.35) are rare; populating them to test the firewall directly needs larger L (L = 8, 12 — already the RESULTS "natural next runs") or importance sampling on the defect depth. This is a tooling matter, not an obstruction in principle.

So the honest closure of the δ-window question is: **lower edge δ ≳ 0.9 (established, sparsity); interior [0.9, 1.3] deterministically safe and tested; operating point should move to δ = 1.3 (free 4.5× gain for (S)); upper edge δ_max set by comparator validity (analytic, Alex) and confirmable up to L≤6 only out to δ ≈ 1.3.**

## 5. Consequences for the (S) program

- **The F034 redirect's top option is now quantified and partly answered.** F034 made the δ-window "the highest-value (S) lever." This finding supplies its (D)-side half: the deterministic firewall does **not** obstruct δ = 1.2–1.3, so the (S) side may adopt δ = 1.3 and the Tier-R clearance drops to ln s ≈ 55 (β_c = 13.3). The remaining (S)-side question is whether the **gap-protection / comparator side** (not the firewall, which is fine) tolerates δ = 1.3–1.45 — that is the analytic call flagged in §4(1), and it is the genuine content of "δ-window vs gap-protection."
- **It sharpens, but does not close, the anchor gap.** The anchor is (β, δ) = (5.6, 1.1) by legacy convention. If the operating threshold moves to δ = 1.3, the relevant Tier-R floor is β_c = 13.3, and the trajectory covers ln s ≳ 55 unconditionally-in-structure (mod the cited chessboard package). The window β ∈ [5.6, 13.3] near the anchor still needs (S) by other means (Z.A/Z.B, M3a) — δ-tuning shrinks that window by ~4.5× in log-scale but does not eliminate it.
- **No proved status changes.** The deterministic side stays closed (F033); this is a parameter-robustness map of the *measured* firewall, refining the operating point. Grounds: G-DW-gated MC (evidence, not proof); the comparator-validity upper edge is identified as analytic and labeled Alex's call; the "adopt δ=1.3" recommendation is opinion (DECISIONS #009), well inside the data.

## 6. Status changes / deposits

(1) New engine + data + plot deposited in `numerics/op12_theta/s_chessboard/` (ENGINE_OP1_op12_delta_window.py, dw_state/, CERT_OP1_delta_window_summary.json, DATA_OP1_delta_window.png), MD5s in the SESSION_LOG entry. (2) `NOTE_FLUX_s_chessboard_route_2026-06-12.md` §8 (7) δ-window remark and F034 §4 option 1 are now **data-backed on the (D) side** — cross-link added. (3) The (S)-side open question is re-stated precisely: "does gap-protection/comparator validity tolerate δ up to 1.3–1.45?" (§4(1)) — Alex. (4) RESULTS "natural next runs" (L=8,12) gains a second motivation: confirming firewall safety at δ ≳ 1.35 where L≤6 is statistics-limited. (5) Ledger #56 closed.
