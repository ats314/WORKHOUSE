# (S) via the Wilson-action large-deviation route: reflection positivity + chessboard

**Date:** June 12, 2026
**Author:** session agent (lead math agent per DECISIONS #009), for Alex
**Engine:** `ENGINE_OP1_s_chessboard_rate.py` → `CERT_OP1_s_chessboard_rate.json` (all gates hard asserts)
**Context:** OP-1's own attack list names "(Analytic) Peierls estimate for |D(U)| using the Wilson action's large-deviation rate function" as the analytic vector; only a numerical probe is deposited. The four recorded failed routes (A′ budget, trace-weighted, HB-q² Matrix-Stein, edge-Bernoulli) do **not** include this one. The corpus records RP as known for the Wilson action (OPEN_PROBLEMS OP-5). This note executes the route to the extent provable in one pass, with every step labeled.

**Status labels:**
- §2 Lemma A (animal growth): **PROVED here** (complete proof), enumeration-gated (G-S4).
- §3 one-plaquette layer: **EXACT** (Weyl quadrature, machine-gated G-S1/G-S2).
- §4 Lemma P (positivity) and §5 Theorem S-LB (Tier-R Peierls bound): **CONDITIONAL on a cited-standard package** (OS reflection positivity for Wilson SU(3) on the even torus + FILS multi-event chessboard); the dissemination bookkeeping and the F/ΘF decomposition are written out below but **flagged for Alex's verification** — they are standard manipulations, not new mathematics, but this note does not claim them as independently re-proved.
- §6 Tier-S sharp rate: **TARGET** (one provable inequality away), with the exact proxy computed.
- §7 calibration vs deposited ensembles: **MC EVIDENCE**, hard-gated where the bound applies (G-S3, 8/8).
- §8 consequences: labeled GATE-BACKED / CONDITIONAL / OPINION per item.
- **Honest headline:** Tier-R does **not** cover the anchor (β, δ) = (5.6, 1.1). It gives the first nonvacuous proven-modulo-cited-package regime of the (S) display, with the correct uniformity structure along the trajectory, and it localizes the remaining gap in a single expectation bound (§6).

---

## 1. Setup and target

Wilson SU(3) on Λ = (ℤ/Lℤ)⁴, L even: P_β(dU) = Z⁻¹ e^{−β Σ_p φ_p} dU_Haar, φ_p = 1 − (1/3)Re tr U_p ∈ [0, 3/2] (max 3/2 at the order-3 center-like classes; grid value 1.499999, G-S1 run). Defect plaquettes D_δ = {p : φ_p ≥ δ}. The canonical (S) display (UNIF_OP1_CLOSURE_PLAN §2):

  P(Γ ⊂ D_δ) ≤ K₀^{|Γ|} exp(−α β δ |Γ|),  with rate > log μ_animal + margin, uniformly along β(a).

The rooted-capacity chain (M3 Addendum 2) consumes exactly this through the rooted sum Σ_{Γ∋p₀} e^{a|Γ| + sΘ(Γ)} P(Γ ⊂ D_δ).

## 2. Lemma A — the animal constant, pinned

**Lemma A.** Let G be any graph of maximum degree Δ, v a fixed vertex. The number a_n of connected vertex sets S ∋ v with |S| = n satisfies a_n ≤ e·(eΔ)^{n−1}. For the plaquette-adjacency graph of ℤ⁴ (plaquettes adjacent iff they share a link), Δ = 20, hence

  a_n ≤ e·μ̄^{n−1},  μ̄ := eΔ = 54.37,  **log μ̄ = 1 + log 20 = 3.9957.**

*Proof.* Each plaquette has 4 links; each link lies in 2(d−1) = 6 plaquettes; two distinct plaquettes share at most one link (two unit squares sharing two edges coincide), so the 4·5 = 20 neighbors are distinct: Δ = 20. For the count: each connected S has a canonical (BFS-lexicographic) spanning tree T rooted at v. T is reconstructed from the data: for each vertex u in BFS order, the subset c_u of u's ≤ Δ neighbor-slots that are tree-children. Hence a_n is at most the number of sequences of subsets with Σ|c_u| = n−1 drawn from n blocks of Δ slots, which is ≤ C(Δn, n−1) ≤ (eΔn/(n−1))^{n−1} ≤ e·(eΔ)^{n−1}, using C(m,k) ≤ (em/k)^k and (n/(n−1))^{n−1} ≤ e. ∎

**Exact small-n counts (engine, gate G-S4):** a₁..a₄ = 1, 20, 458, 11132; per-step growth a_n^{1/(n−1)} = 20.0, 21.4, 22.3 — comfortably below μ̄, and indicating the *true* plaquette-animal connective constant is ≈ 25–35 (log ≈ 3.2–3.6), so log μ̄ = 3.996 is a safe, provable, but not sharp threshold. All thresholds below use the proved 3.996.

## 3. The exact one-plaquette layer (Weyl quadrature; machine-gated)

By Weyl integration, for class functions: ∫f dU = (6(2π)²)⁻¹ ∬ f(θ)·Π_{i<j} 4sin²((θ_i−θ_j)/2) dθ₁dθ₂, θ₃ = −θ₁−θ₂. Gates: Haar normalization 0 to machine, E Re tr U = 8·10⁻¹⁷, E|tr U|² − 1 = −2·10⁻¹⁶ (G-S1/G-S2). Computed exactly (engine §B):

| β | z(β) = E e^{−βφ} | f₁ = −log z | ⟨φ⟩₁pl | r₁(δ=1.1) | r₁(δ=1.3) |
|---|---|---|---|---|---|
| 5.6 | 1.0804·10⁻² | 4.528 | 0.6040 | 3.132 | 5.696 |
| 6.0 | 8.5305·10⁻³ | 4.764 | 0.5775 | 3.372 | 5.992 |
| 6.4 | 6.8057·10⁻³ | 4.990 | 0.5522 | 3.622 | 6.298 |
| 6.8 | 5.4835·10⁻³ | 5.206 | 0.5282 | 3.881 | 6.613 |
| 7.2 | 4.4595·10⁻³ | 5.413 | 0.5055 | 4.148 | 6.938 |

r₁(β,δ) := −log P_one-plaquette(φ ≥ δ) is the exactly solvable independent-plaquette benchmark rate. Note **r₁ crosses log μ̄ = 3.996 at β ≈ 7.0 for δ = 1.1** — the benchmark rate clears the rooted threshold just above the anchor window.

## 4. Lemma P — positivity of the orientation-removed plaquette expectation

Fix an orientation class o = (μν) and let Z′ be the Wilson model with all o-plaquette couplings removed (the other 5L⁴ plaquette terms intact, same links, same Haar). The removed class is invariant under lattice reflections, so Z′ inherits reflection positivity wrt link-midplane reflections (OS for Wilson actions; corpus baseline OP-5 "known for Wilson action").

**Lemma P (flagged for verification).** E_{Z′}[Re tr U_p] ≥ 0 for every o-plaquette p; hence E_{Z′} φ_p ≤ 1.

*Argument.* Let Θ be the link-reflection through the midplane perpendicular to μ bisecting p. Writing the plaquette holonomy as the pairing of the half-plaquette path F with its reflection, tr U_p = Σ_{ab} F_{ab} (ΘF)̄_{ab} = ⟨F, ΘF⟩, the OS form gives E_{Z′}⟨F, ΘF⟩ ≥ 0 because the Z′ action is Θ-symmetric (the removed orientation class maps to itself, and p is bisected by the plane). This is the standard infrared-bound manipulation; the precise half-path definition and the gauge of the shared links are the bookkeeping flagged for review. ∎(mod flags)

**Consequence (Jensen).** Z = Z′·E_{Z′}[e^{−β Σ_{p∈o} φ_p}] ≥ Z′·exp(−β Σ_{p∈o} E_{Z′}φ_p) ≥ Z′·e^{−βL⁴}, by convexity, translation invariance of Z′, and Lemma P. So **Z′/Z ≤ e^{βL⁴}.**

## 5. Theorem S-LB — the Tier-R Peierls display

**Chessboard input (cited-standard, flagged).** For the RP measure on the even torus with events A_t supported on unit cells (a plaquette (x, μν) is supported on the closed unit cell at x), the multi-event chessboard estimate (FILS) gives P(∩_{t∈T} A_t) ≤ Π_{t∈T} P(A_t disseminated to every cell)^{1/L⁴}. Disseminating a single bad o-plaquette event yields the all-cells, same-orientation event.

**All-bad-one-orientation bound.** Z_{o-bad} = ∫ Π_{p∈o} 1{φ_p ≥ δ} e^{−βS} ≤ e^{−βδL⁴} ∫ e^{−βS_rest} = e^{−βδL⁴} Z′. With §4: P(disseminated) = Z_{o-bad}/Z ≤ e^{−βδL⁴}·e^{βL⁴} = e^{−β(δ−1)L⁴}.

**Theorem S-LB (conditional on the cited package).** For every finite set Γ of plaquettes on the even torus, every δ ∈ (1, 3/2], every β > 0:

  **P(Γ ⊂ D_δ) ≤ exp(−β(δ−1)·|Γ|).**

*Proof.* Apply the multi-event chessboard with one event per element of Γ; each factor is bounded by the all-bad-one-orientation dissemination above, contributing e^{−β(δ−1)} per element. K₀ = 1 in this accounting; any cell/reflection bookkeeping correction is expected to cost only a benign K₀^{|Γ|} = e^{O(|Γ|)} without touching the β-linear rate (flagged). ∎(mod flags)

**Remarks.** (i) Γ is arbitrary, not just connected — stronger than the display needs. (ii) Rate monotone increasing in β and in δ ⇒ once the threshold is cleared at some β₀ it is cleared along the entire upper trajectory: **the uniformity-in-cutoff structure the closure plan demands is automatic on this route.** (iii) Link-marked transfer: a link defect requires one of its 6 plaquettes bad, so P(Γ_L ⊂ D^link) ≤ 6^{|Γ_L|} e^{−r⌈|Γ_L|/4⌉}, i.e. rate_link ≥ r/4 − log 6 — remark-grade, the rooted chain is stated on plaquettes.

**Corollary (rooted summability, Tier-R).** With Lemma A and capacity weights e^{a|Γ| + sΘ(Γ)}, Θ(Γ) ≤ θ̄|Γ|:

  Σ_{Γ∋p₀} e^{a|Γ|+sΘ(Γ)} P(Γ⊂D_δ) ≤ e·Σ_{n≥1} μ̄^{n−1} e^{(a+sθ̄)n} e^{−β(δ−1)n} < ∞ ⟺ **β(δ−1) > log μ̄ + a + sθ̄ = 3.996 + a + sθ̄.**

**Tier-R thresholds (a = sθ̄ = 0), engine §C:**

| δ | β_c (Tier-R) | ln s to reach from anchor |
|---|---|---|
| 1.10 | 39.96 | 246.6 |
| 1.20 | 19.98 | 103.2 |
| 1.30 | 13.32 | 55.4 |
| 1.40 | 9.99 | 31.5 |
| 1.45 | 8.88 | 23.5 |

**Honest verdict:** Tier-R is nonvacuous only for δ > 1 and covers β ≥ β_c(δ) ∈ [8.9, 40]. The anchor (5.6, 1.1) is **not covered**. δ → 3/2 gives the floor β_c → 8.0.

## 6. Tier-S — where the remaining factor lives

The single lossy step is Jensen with E_{Z′}φ_p ≤ 1 (Lemma P's free consequence). Any proved bound E_{Z′}φ_p ≤ Ē(β) upgrades the rate to **r_S = β(δ − Ē(β))** with everything else unchanged. Calibration of how much that buys:

- Exact one-plaquette proxy: Ē ≈ ⟨φ⟩₁pl(β) (table §3): r_S(5.6, 1.1) = 5.6·(1.1−0.604) = 2.78; r_S clears log μ̄ at **β ≈ 6.9 for δ = 1.1**.
- Measured full-Wilson ⟨φ⟩ (deposited ensembles, §7): 0.446 at β = 5.6 → 0.309 at 7.2 — *below* the one-plaquette value, as interaction orders the system; if Ē could be pushed to the measured scale, r_S(5.6, 1.1) ≈ 5.6·0.654 = 3.66, and ≈ 4.0 by β ≈ 5.9.
- Candidate proofs of Ē < 1 (ranked): (1) chessboard/infrared bound on ⟨φ_p⟩_{Z′} itself (the same machinery, applied to the observable instead of the indicator — the classical Gaussian-domination estimate gives ⟨Re tr U_p⟩ ≥ c(β) > 0 at large β); (2) a one-plaquette comparison inequality conditioning on the star of p (the project's one-plaquette program owns the exact conditional laws — the domino/tromino weight cards are precisely conditional one-plaquette objects); (3) strong-coupling/character expansion at small β for a complementary regime. Each unit of improvement in (1−Ē) buys rate β·(improvement); the entire distance from Tier-R to the anchor is Ē: 1 → ≈ 0.3.

## 7. Calibration against the deposited ensembles (MC evidence; hard gate where applicable)

Engine §D, all 8 ensembles (L = 4: β = 5.6–7.2; L = 6: β = 5.6, 6.4, 7.2), per-config `rhoP_dδ` means:

| L | β | ⟨φ⟩ meas | ρ_P(0.7) | ρ_P(0.9) | ρ_P(1.1) | −ln ρ_P(1.1) |
|---|---|---|---|---|---|---|
| 4 | 5.6 | 0.4463 | 1.20·10⁻¹ | 3.06·10⁻² | 5.53·10⁻³ | 5.20 |
| 4 | 6.0 | 0.3901 | 6.24·10⁻² | 1.11·10⁻² | 1.24·10⁻³ | 6.69 |
| 4 | 6.4 | 0.3665 | 4.49·10⁻² | 6.38·10⁻³ | 5.86·10⁻⁴ | 7.44 |
| 4 | 6.8 | 0.3396 | 2.82·10⁻² | 3.29·10⁻³ | 9.77·10⁻⁵ | 9.23 |
| 4 | 7.2 | 0.3086 | 1.41·10⁻² | 1.27·10⁻³ | 1.63·10⁻⁴ | 8.72 |
| 6 | 5.6 | 0.4398 | 1.11·10⁻¹ | 2.58·10⁻² | 3.49·10⁻³ | 5.66 |
| 6 | 6.4 | 0.3652 | 4.35·10⁻² | 6.47·10⁻³ | 5.47·10⁻⁴ | 7.51 |
| 6 | 7.2 | 0.3111 | 1.47·10⁻² | 1.33·10⁻³ | 6.43·10⁻⁵ | 9.65 |

**G-S3 (hard, falsifiable, PASSED 8/8):** measured ρ_P(δ) ≤ e^{−β(δ−1)} for every ensemble at δ = 1.1 — the Tier-R inequality at |Γ| = 1 holds in the data with large margin. **MC observations (evidence, not proof):** the true rate −ln ρ_P(1.1) is 5.2 at the anchor and exceeds log μ̄ = 3.996 already at β = 5.6, reaching ~9 by β = 7.2 — the rooted threshold is empirically cleared *at and beyond the anchor*; the entire deficit is in what is provable. The benchmark r₁ tracks the measured rate from below (3.13 vs 5.20 at the anchor), consistent with interactions suppressing defects beyond the independent-plaquette level.

## 8. What this changes (labeled)

**[GATE-BACKED]** (1) μ_animal — named but never pinned in the corpus — is now a proved explicit constant: log μ̄ = 3.9957 (Lemma A), with exact counts a₂..a₄ = 20, 458, 11132 showing the true constant is ≈ 25–35. (2) The exact one-plaquette layer (z, f₁, ⟨φ⟩, tails) is deposited as gated reference data; r₁ crosses the rooted threshold at β ≈ 7.0 (δ = 1.1). (3) The Tier-R single-plaquette inequality holds in all deposited ensembles with large margin.

**[CONDITIONAL — cited package, flagged steps]** (4) Theorem S-LB: the (S) Peierls display holds with rate β(δ−1), K₀ = 1, for arbitrary Γ, δ > 1, on the even torus — the first nonvacuous proven-modulo-citations regime of the display, with uniformity along the trajectory automatic (rate monotone in β). Rooted summability for β(δ−1) > 3.996 + a + sθ̄.

**[OPINION, per DECISIONS #009]** (5) This route complements Z.A/Z.B rather than replacing them: it owns the large-(β,δ) regime unconditionally-in-structure, while Z.A/Z.B target the covariance form at the anchor. (6) The remaining distance to the anchor is now a *single expectation bound* — E_{Z′}φ_p ≤ Ē with Ē pushed from 1 toward ≈ 0.5–0.6 — and route (1) of §6 (infrared bound on the plaquette expectation) uses machinery already in play here; I'd rate it the highest-value/effort analytic target currently visible on the (S) side, and it is exactly the kind of estimate the closure plan predicted would be needed ("Wilson-action large-deviation route"). (7) δ is a parameter we choose; the δ-window question (does the gap-protection side tolerate δ = 1.3–1.45, where β_c drops to 9–13?) should be settled against `NOTE_OP1_unif_gap_protection_factorization.md` — if yes, Tier-R alone covers the trajectory tail from ln s ≈ 24–55 and Tier-S would need far less.

**Scope honesty:** nothing here proves (S) at the anchor; nothing touches Z.A/Z.B, CONJ_B, or the continuum. The chessboard and RP inputs are standard and corpus-consistent but are *cited*, not re-proved; the flagged bookkeeping (cell geometry, F/ΘF decomposition, dissemination constants) is Alex-verification work before any status upgrade.

## 9. Files, gates, reproduction

`ENGINE_OP1_s_chessboard_rate.py` (this engine; gates G-S1 Haar normalization, G-S2 Haar moments, G-S3 ensemble Tier-R checks 8/8, G-S4 animal counts vs Lemma A), `CERT_OP1_s_chessboard_rate.json` (all tables). Reproduce: `python3 ENGINE_OP1_s_chessboard_rate.py`. Dependencies: numpy. MD5s in the session message; record in ledger on deposit.

Suggested STATE.md line (owner to paste):
> (S)/M3 — chessboard route opened (NOTE_FLUX_s_chessboard_route_2026-06-12.md): Lemma A pins log μ_animal ≤ 3.9957 (PROVED, enumeration-gated); Tier-R Peierls display P(Γ⊂D_δ) ≤ e^{−β(δ−1)|Γ|} conditional on cited OS-RP+chessboard package (flags listed); rooted summability for β(δ−1) > 3.996; anchor NOT covered — remaining gap localized to one expectation bound E_{Z′}φ_p ≤ Ē (§6); exact one-plaquette layer deposited; ensembles clear the rooted threshold empirically at β ≥ 5.6 (MC evidence).
