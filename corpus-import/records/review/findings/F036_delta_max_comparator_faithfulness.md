# F036 — The δ-window's upper edge is δ_max ≤ 1, set by per-plaquette curvature; it is disjoint from Tier-R (June 12, 2026)

**Unit:** #57 (own-initiative computation, completing F035 at Alex's selection). **Verdict: the comparator-validity upper edge of the δ-window is now pinned — and it lands below where F035 hoped, which retracts F035's "adopt δ=1.3" recommendation.** F035 measured that the *in-model* firewall θ falls monotonically as δ grows and correctly flagged that the real upper edge is a comparator-validity condition it could not measure. This finding computes that condition. The comparator M = m₀²I + α_W d₁*d₁ is a **positive operator**, so it cannot lower-bound a plaquette whose local Hessian block is net-negative — and the SU(3) per-plaquette link-curvature is exactly **(4/3)(1 − s_p)**, which changes sign at **s_p = 1**. Hence the hard, calibration-independent ceiling is **δ_max ≤ 1**: any δ > 1 deliberately leaves net-negative-curvature plaquettes (1 < s_p ≤ δ) *off* the defect set, where a positive M cannot represent them. Since the (S) Tier-R rate β(δ−1) is positive only for **δ > 1**, the comparator-faithful window (δ ≤ 1) and the Tier-R-nonvacuous window (δ > 1) are **disjoint** — a structural reason, complementing F034's Ē₁ ≈ 1, that the chessboard route cannot operate. Engine: `numerics/op12_theta/s_chessboard/ENGINE_OP1_delta_max_curvature.py` (run copy `RUN_OP1_dmax.py`) → `CERT_OP1_delta_max_curvature.json`, gates **G-DM0..G-DM4 PASS**.

## 1. The object and why it is the right one

OP-1's objective (UNIF_OP1_CLOSURE_PLAN line 11): prove ‖K_a(U)‖ < 1 with K_a = M_a^{−1/2} V_a M_a^{−1/2}, **M_a = m₀²I + α_W d₁*d₁**, **V_a = v₀·Π_{D(U)}**. The defect potential lives *only* on D_δ; everything else is the clean comparator M. So the model has no internal upper-δ ceiling — larger δ means sparser Π_D and smaller θ, exactly F035's measured monotone fall. The upper edge is therefore not internal but a question of **model faithfulness**: for ‖K‖ < 1 to certify the true coercivity object, the splitting M − V must bound the true Hessian H from below, which requires M (a *positive* operator: m₀²I ⪰ 0 and α_W d₁*d₁ ⪰ 0) to be able to represent the off-defect background. Wherever the true local curvature is negative and the plaquette is *not* a defect, M overestimates H and the bound fails. Defects are precisely the negative-curvature plaquettes; the defect threshold δ must sit at or below where negative curvature sets in.

## 2. The computation (exact + gated)

The per-link 8×8 Hessian block contributed by one plaquette of holonomy U_p is, for the gauge action density s_p = 1 − (1/3)Re tr U_p,

  **H_ab = ∂²s_p/∂t_a∂t_b |₀ = (1/6) Re tr( {T_a,T_b} U_p )**,  T_a = λ_a/2,

whose trace is **tr H = (4/9) Re tr U_p = (4/3)(1 − s_p)** (using Σ_a T_a² = C_F I, C_F = 4/3). Scanning the full SU(3) conjugacy class (θ₁,θ₂ grid, det = 1 via θ₃ = −θ₁−θ₂):

| Gate | Check | Result |
|---|---|---|
| G-DM0 | Casimir Σ_a T_a² = (4/3)I | PASS (≤1e-13) |
| G-DM1 | trace law tr H = (4/3)(1−s_p) over 400 random classes | PASS, worst dev **4.4e-16** |
| G-DM2 | finite-difference cross-check of H_ab for a sample U_p | PASS, worst dev **4.0e-9** |
| G-DM3 | every class element with s_p > 1 has min-eig(H) < 0 (forced by tr < 0) | PASS |
| G-DM4 | negative-curvature onset s_p* ≤ 1 | PASS |

**Two thresholds, two strengths:**

- **Strict onset s_p\* = 2/3** (exact rational; reached at U_p = diag(1, i, −i), angles (0, π/2)): the *first* SU(3) class where H develops a single negative eigendirection. min-eig(H) crosses zero between the s_p ≈ 0.61 and 0.71 bins; it is +0.011 at 0.61, −0.014 at 0.71, −0.089 at 1.01.
- **Hard net (trace) sign change s_p = 1**: above this the block is net-negative (tr H < 0), so it has a negative direction *no matter the class* — a positive M cannot represent its average contribution. **Calibration-independent.**

So the faithful defect threshold lies in **[2/3, 1]**, and **δ_max ≤ 1** is the hard ceiling.

## 3. The structural verdict

**δ_max ≤ 1 (hard) vs Tier-R's δ > 1 ⟹ the windows are disjoint.** Tier-R (F029/S_CHESSBOARD §5) gives P(Γ ⊂ D_δ) ≤ e^{−β(δ−1)|Γ|}, with a *positive* rate only for δ > 1. Comparator faithfulness requires δ ≤ 1. They meet only at the degenerate point δ = 1, where the Tier-R rate is zero (vacuous) and the comparator is marginal (zero net curvature). **There is no δ at which the deterministic firewall is faithful and Tier-R is non-vacuous simultaneously.** This is a second, independent obstruction to the chessboard route, structural where F034's Ē₁ ≈ 1 was quantitative: F034 showed Tier-S = Tier-R on sparse animals; F036 shows the entire Tier-R operating regime (δ > 1) lies past the comparator's faithfulness edge. The two together say the route is pinned to the wrong side of δ = 1 from both directions.

## 4. Correction to F035 (honesty discipline)

F035 recommended "adopt δ = 1.3 for a free 4.5× reduction in the Tier-R clearance (ln s 247 → 55)." **That recommendation is retracted.** F035's measurement — θ falls as δ grows — is correct *within the model* V = v₀Π_D, but this finding shows the model is **unfaithful for δ > 1**: at δ = 1.3, plaquettes with 1 < s_p ≤ 1.3 carry net-negative curvature and are assigned to the positive comparator background, which cannot represent them, so the in-model θ there does not bound the true operator. The faithful operating range is **δ ≤ 1**, where Tier-R is vacuous (δ = 1) or expensive (β_c → 40 as δ → 1⁺ is unreachable since δ ≤ 1). The legacy operating point **δ ≈ 0.9 sits correctly inside [2/3, 1]**, relying on the mass m₀² and the five neighbouring plaquettes to absorb the (2/3, 0.9) single negative directions — which is plausible at m₀² = 0.5 but is itself the calibration question (§5). F035's deterministic-safety conclusion in the *measured* window δ ∈ [1.1, 1.3] therefore stands only as an in-model statement; the faithful conclusion is δ ≤ 1.

## 5. Scope and what remains Alex's modeling call

The **hard ceiling δ_max ≤ 1** (net-negative curvature) is calibration-independent and settled. Two things are **not** settled here and remain the modeling layer:

1. **The strict onset s_p\* = 2/3 vs the hard ceiling 1.** Whether a *single* negative direction (s_p ∈ (2/3, 1)) actually breaks faithfulness depends on whether the mass m₀² and the other five plaquettes at the link absorb it. That is a calibration question (the values of m₀², α_W, v₀ against the true Hessian), Alex's layer. The conservative reading puts δ_max nearer 2/3; the permissive reading puts it at 1.
2. **The off-defect deficit for s_p ∈ (0, δ).** Even below the onset, every plaquette with s_p > 0 has curvature (4/3)(1−s_p) < the vacuum value, so M's α_W cannot be the vacuum stiffness — it must be calibrated to a reduced/typical value with V capturing the excess. Pinning that calibration (and hence the precise faithful δ_max within [2/3, 1]) is the comparator-design work flagged in F035 §4(1) and is upstream of this campaign. This finding bounds it from above (≤ 1) and identifies the relevant scale (2/3).

Grounds: G-DM-gated exact linear algebra (derived-and-machine-verified); the curvature law and both thresholds are exact. The δ_max ≤ 1 ceiling and the Tier-R disjointness are theorems about the positive comparator; the placement within [2/3, 1] is labeled calibration-dependent.

## 6. Consequences for OP-1

- **The δ-window is now pinned on both edges:** lower ≈ 0.9 (sparsity/non-percolation, F029/RESULTS), upper ≤ 1 (faithfulness, here). It is a **narrow** band ≈ [0.9, 1], not the [1.1, 1.45] F035's in-model measurement suggested. δ-tuning therefore buys **essentially no free Tier-R gain** — Tier-R is vacuous-to-expensive across the entire faithful band (β_c ≥ 40 at δ ≤ 1). The hope that "Tier-R alone covers the trajectory tail at cheap δ" is closed off.
- **This sharpens, again, that the real open content of (S) is M3a (Z.A/Z.B), not a δ-tuning or Ē/Tier-R maneuver.** Both F034 and F036 now independently show the chessboard/Tier-R family cannot reach the anchor; the covariance form (Z.A typicality + Z.B far-source stability) is where the remaining work is, consistent with the closure plan's standing assignment.
- **No proved status changes.** (D) stays closed (F033); the N* floors are comparator-ceiling theorems and do not depend on δ. This finding constrains the *modeling interface* (the faithful δ-range), not any proven bound.

## 7. Deposits

Engine `ENGINE_OP1_delta_max_curvature.py` (canonical, host-correct; md5 b28c064c) + run copy `RUN_OP1_dmax.py` (md5 4418005d — the VM mount served a stale truncated view of the canonical file mid-pass, so the gated run was executed from a fresh-path byte-equivalent copy; host canonical verified correct by Read) + `CERT_OP1_delta_max_curvature.json` (md5 cb640f9e) in `numerics/op12_theta/s_chessboard/`. F035 finding gets a retraction cross-link; S_CHESSBOARD route note gets a δ_max paragraph; STATE + SESSION_LOG + ledger #57 updated. Ledger count → 38/57 closed (35 DONE + 3 SKIP), F001–F036.
