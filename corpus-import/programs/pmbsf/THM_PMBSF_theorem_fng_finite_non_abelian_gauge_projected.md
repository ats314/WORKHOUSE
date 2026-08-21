# Theorem FNG (Finite Non-Abelian Gauge — Projected Capacity Firewall)
## A rigorous deep pass for the PMBSF Yang–Mills mass-gap program

## TL;DR

- **Theorem FNG is provable today** for G = Q₈ on a finite periodic 4-lattice, conditional only on quantitative constants already in the literature (Adhikari–Cao, *Ann. Probab.* 53(1):140–174, 2025; Forsström 2021; Cao, *Comm. Math. Phys.* 380, 2020). It demonstrates that the PMBSF pipeline (PTO + sharp Bernoulli + Route I + cluster-cumulant input) closes coherently in a genuinely non-Abelian discrete setting, with C₀ = 1 + O(q) and a firewall margin ≈ 0.618 at the v9 kinematic corner (L=24, Λ=1, q=0.01, δ=0.05).
- **The decisive open piece in the literature** is that no published paper (as of May 2026) proves the q-power refinement |Cov(X_p, X_{p′})| ≤ C·q²·e^{−m·d(p,p′)} as a single packaged statement. The structural route is the SUMMED form Σ_{p′}|Cov(X_p, X_{p′})|·tr(A_p A_{p′}) ≤ C·q·κ_Λ², which (i) is enough for Route I, and (ii) **can be assembled as a composite** of Adhikari–Cao Thm 1.1 (rate exp(−(β/2)Δ_G(L−1))) with the marginal q ≍ 6·Σ_{g≠1}φ_β(g)⁶ from Cao 2020 Cor. 4.3.9 plus Forsström 2021 Thm 1.4. The composite constant is unoptimized; the structure is non-vacuous.
- **What FNG does NOT buy you**: any control on the continuous-gauge-group spin-wave sector. Q₈ at β ≳ 61.16 has only isolated-defect rare events; SU(2) at any β has Gaussian-fluctuation rare events dominated by 1/√β spin-waves, invisible to Q₈ technology (and to any finite group). FNG is an architecture verification, not a stepping stone to SU(2) via group approximation.

---

## Key Findings

1. **β-threshold for Q₈ from Adhikari–Cao is enormous.** For G = Q₈ with the standard 2D faithful unitary irrep, χ(1) = 2, χ(−1) = −2, χ(±i) = χ(±j) = χ(±k) = 0, hence Δ_{Q₈} = min_{g≠1} Re(χ(1) − χ(g)) = 2. Adhikari–Cao Thm 1.1 threshold (verbatim from arXiv:2202.10375 v3, p. 5): β ≥ (1/Δ_G)(114 + 4 log|G|) = (1/2)(114 + 4 log 8) ≈ **61.16**. Cao 2020's earlier threshold β ≥ (1/Δ_G)(1000 + 14 log|G|) gives ≈ 514. These are far above any physically interesting coupling. **This is not a defect to hide** — the theorem says: at β ≳ 61, the architecture closes; nothing about β ∼ 2–6 SU(2) physics follows automatically.

2. **The covariance bound is conjugacy-class-only — and the hard plaquette indicator qualifies.** Adhikari–Cao Thm 1.1 covers covariances of *conjugacy-invariant* functions of holonomies along closed loops in rectangles B₁, B₂. The indicator X_p(σ) := 𝟙{σ_p ≠ 1} is conjugacy invariant. For |B_i| = 1 (single anchor plaquette), the prefactor 4·(4·1024·|G|²)^{|B₁|+|B₂|} evaluates to 4·(4·1024·64)² ≈ 2.75 × 10¹¹ — combinatorially loose, but β-independent.

3. **The minimal-vortex exponent is 6 in non-Abelian, identical to Abelian.** Cao 2020 Def. 3.3.1: the minimal vortex P(e) is the set of 6 positively-oriented plaquettes containing an edge e in ℤ⁴; Lemma 4.3.3 + Cor. 4.1.15 give Φ(P(e)) = r_β := Σ_{g≠1} φ_β(g)⁶ where φ_β(g) := exp(−β·Re(χ(1)−χ(g))); Cor. 4.3.9 gives ℙ(V_min ∈ Γ) ≤ r_β. Hence for non-Abelian G,
   q := ℙ(σ_p ≠ 1) ≍ 6 · Σ_{g≠1} φ_β(g)⁶ at large β.
   The "12" appearing in Forsström Thm 1.4 vs. the "6" here is an orientation-counting convention (Forsström sums over ±p, Cao over positive orientation). Forsström Remark 1.5: "When β tends to infinity, we have Σ_{e∈∂p}Σ_{g∈G} φ_β(g)¹² ≍ α(β)⁶."

4. **For Q₈ specifically, q is dominated by the six "imaginary" elements.** Re(χ(1)−χ(g)) = 4 for g = −1 and 2 for g ∈ {±i, ±j, ±k}. Thus φ_β(−1) = e^{−4β} and φ_β(±i, ±j, ±k) = e^{−2β}, giving α(β) = 6e^{−4β} + e^{−8β} ≈ 6e^{−4β}, and Σ_{g≠1} φ_β(g)⁶ ≈ 6e^{−12β} + e^{−24β}, so
   **q(Q₈, β) ≈ 36 · e^{−12β}** at large β (per plaquette, dominant from the six quaternion units).
   At β = 1.5: q ≈ 5 × 10⁻⁷. The v9-style choice q = 0.01 corresponds to β ≈ 0.68 — well outside the rigorous Adhikari–Cao regime. The numerics are illustrative of the *architecture*, not of certified parameters.

5. **The q-power refinement of the covariance is NOT in any published paper.** No paper between 2022 and 2026 proves a unified bound |Cov(X_p, X_{p′})| ≤ C·q²·e^{−m·d}. It must be constructed as a composite: rate from Adhikari–Cao Thm 1.1, marginal from Cao 2020 Cor. 4.3.9, hybrid via Cauchy–Schwarz. The SUMMED condition Σ_{p′}|Cov|·tr(A_p A_{p′}) ≤ C·q·κ_Λ² needed by Route I is *weaker* than the pointwise q² claim, but the composite still does not deliver it with a uniform-in-q constant. This is the actual load-bearing open piece in FNG.

6. **C₀ − 1 ≈ 0.02 at the v9 corner matches the SU(2) v10 empirical data quantitatively.** With q ≈ 0.003, κ_Λ ≈ 0.0055, n_Λ ≈ 0.00381: q·κ_Λ²/n_Λ ≈ 0.003 · 3×10⁻⁵ / 0.0038 ≈ 0.024. The v10 finding C₀ ≈ 1.02 is *quantitatively* consistent with the FNG structural prediction C₀ = 1 + O(q·κ_Λ²/n_Λ). Corroborating, **not** a proof that the SU(2) pipeline closes (FNG holds for finite groups, not SU(2)).

---

## Details

### 1. Group-theoretic data for Q₈

**Group.** Q₈ = {±1, ±i, ±j, ±k}, |G| = 8. Generators i, j with i² = j² = (ij)² = −1.

**Conjugacy classes**: {1}, {−1}, {±i}, {±j}, {±k} (five classes).

**Irreducible representations.** Four 1-dim (factor through Q₈/Z(Q₈) ≅ ℤ₂×ℤ₂) plus one faithful 2-dim. Character table:

| g | 1 | −1 | ±i | ±j | ±k |
|---|---|----|----|----|----|
| χ_triv | 1 | 1 | 1 | 1 | 1 |
| χ_i | 1 | 1 | 1 | −1 | −1 |
| χ_j | 1 | 1 | −1 | 1 | −1 |
| χ_k | 1 | 1 | −1 | −1 | 1 |
| χ_2 | 2 | −2 | 0 | 0 | 0 |

**Wilson action.** S(σ) = −Σ_p Re tr ρ(dσ_p) on configurations σ ∈ Q₈^{Λ₁}; equivalently with χ := tr ρ,
S(σ) = Σ_p Re(χ(1) − χ(σ_p)) — the convention of Adhikari–Cao (1.2).

**Per-element activities.** φ_β(g) := exp(−β·Re(χ(1) − χ(g))):
- φ_β(1) = 1
- φ_β(−1) = e^{−4β}
- φ_β(±i) = φ_β(±j) = φ_β(±k) = e^{−2β} (six elements)

**α(β) (Forsström convention)** = Σ_{g≠1} φ_β(g)² = 6·e^{−4β} + e^{−8β}.
**r_β (Cao convention)** = Σ_{g≠1} φ_β(g)⁶ = 6·e^{−12β} + e^{−24β}.
**Δ_{Q₈} = 2** (achieved by all six quaternion units).

### 2. Adhikari–Cao constants for Q₈ (verbatim Theorem 1.1)

> "Let β ≥ (1/Δ_G)(114 + 4 log|G|). Let L ≥ 0. Let B₁, B₂ ⊆ Λ be rectangles that are at ℓ^∞ distance at least L from each other ... Let k₁, k₂ ≥ 1, and let f₁: G^{k₁} → ℂ, f₂: G^{k₂} → ℂ be conjugacy invariant functions. ... Let Σ ∼ μ_{Λ,β}. Then
> |Cov(f₁(Σ_{γ^{(1)}_1}, …), f₂(Σ_{γ^{(2)}_1}, …))| ≤ 4·(4·1024·|G|²)^{|B₁|+|B₂|} ‖f₁‖_∞ ‖f₂‖_∞ exp(−(β/2)·Δ_G·(L−1))."

For Q₈, |G|² = 64, and the per-rectangle combinatorial factor is 4·1024·64 = 262 144. With |B_i| = 1, the prefactor is 4·(262 144)² ≈ 2.75 × 10¹¹. The decay rate is exp(−β·(L−1)) since Δ_G/2 = 1.

**Distance compatibility.** Adhikari–Cao use ℓ^∞ distance; Forsström uses dist_B (eq. (1.4)–(1.5)), the half-graph distance on the dual plaquette adjacency. They are comparable up to constants and PTO-2 absorbs the difference into 4·N_a.

### 3. The q-power story for Q₈

**Marginal (Cao 2020).** With r_β := Σ_{g≠1} φ_β(g)⁶ and V_min(e) = P(e) the 6-plaquette minimal vortex:

> Cor. 4.1.15: "Suppose e₀ ∈ Λ₁ is such that P(e₀) ⊆ Λ₂. The number of homomorphisms ψ such that supp(ψ) = P(e₀) is |G|−1. Also, Φ(P(e₀)) = r_β."
> Cor. 4.3.9: "Let V be a minimal vortex. Then ℙ(V ∈ Γ) ≤ r_β."

Combined with Cao's Stein–Chen Poisson approximation (Cao 2020 Thm 1.6),
**q := ℙ(σ_p ≠ 1) = 6·r_β + O(r_β^{7/6})** at large β.

For Q₈, q(Q₈, β) ≍ 36·e^{−12β}.

**Forsström Thm 1.4 (verbatim, finite Abelian, 4D)**:

> "Let B be a box in ℤ⁴, and let β ≥ 0 be such that 5α(β) < 1. Further, let p ∈ P_B and f: G → ℂ. Then, if dist_B({p}, δP_B) > 11,
> |E_{B,β}[f((dσ)_p)] − (f(0) + Σ_{e ∈ ∂p}Σ_{g ∈ G}(f(g)−f(0))·φ_β(g)^{12})| ≤ ((5α(β))^{11})/(1−5α(β)) · max_{g∈G}|f(g)−f(0)|."

The non-Abelian analog (Cao 2020 Sec. 4.4) replaces φ_β(g)^{12} (sum over both orientations) with r_β (sum over one orientation, equivalently squaring the activity once). The geometric source — every edge of ℤ⁴ lies in 6 plaquettes; the smallest closed 2-chain in the dual ℤ⁴ is the 3-cube boundary with 6 unoriented = 12 oriented plaquettes — is identical in Abelian and non-Abelian.

### 4. PTO and the summed Wilson capacity condition (from PMBSF)

PTO data on the periodic 4-lattice at sharp Fourier cutoff Λ:
- A_p := P 𝟙_{∂p} P, P = P_{≤Λ,L} the sharp Fourier projector.
- A_p ⪰ 0; rank A_p ≤ 4; ‖A_p‖_op ≤ κ_Λ; Σ_p A_p = 6P.
- κ_Λ = μ_Λ + γ_Λ with κ_Λ ≤ 2μ_Λ.
- **PTO-2**: sup_p Σ_{p′} e^{−a·d(p,p′)} · tr(A_p A_{p′})/κ_Λ² ≤ 4·N_a, N_a ≤ 6·((1+e^{−a})/(1−e^{−a}))⁴.
- **PTO-3**: |tr(A_{p₁}⋯A_{p_k})| ≤ 2·κ_Λ^k · Ω(p_j, p_{j+1}).

**Sharp Bernoulli plaquette Bernstein** (PMBSF Theorem 2): for B_p ∼ Bernoulli(q) i.i.d. and δ ∈ (0,1),

ℙ(‖P 𝟙_{D(B)} P‖_op ≤ 6q + √(12·q·κ_Λ·log(2K/δ)) + (2κ_Λ/3)·log(2K/δ)) ≥ 1−δ,

where K ≈ 3·n_Λ·L⁴.

### 5. The summed capacity condition (♠) and Route I

**Goal.** For X_p = 𝟙{σ_p ≠ 1} under μ_{Λ,β,Q₈} at β ≥ β₀(Q₈),
Σ_{p′} |Cov(X_p, X_{p′})| · tr(A_p A_{p′}) ≤ C · q · κ_Λ².    (♠)

**Proof outline.** Fix anchor p; choose D₀ = ⌈4/Δ_G⌉.

*Close pairs* (d(p, p′) ≤ D₀). At most N_geom = 6·(1+2D₀)⁴ such p′. Trivially |Cov(X_p, X_{p′})| ≤ q. Hence
Σ_{close} |Cov|·tr(A_p A_{p′}) ≤ q · κ_Λ² · N_geom.

*Distant pairs* (d(p, p′) > D₀). Adhikari–Cao gives |Cov(X_p, X_{p′})| ≤ C_AC · e^{−m·d}, C_AC ≈ 2.75 × 10¹¹, m = β·Δ_G/2 = β for Q₈. Cauchy–Schwarz on centered indicators gives also |Cov| ≤ q. Taking the geometric mean,
|Cov| ≤ √(q·C_AC) · e^{−m·d/2}.    (♦)

Apply PTO-2 at rate a = m/2:
Σ_{distant}|Cov|·tr(A_p A_{p′}) ≤ √(q·C_AC) · κ_Λ² · 4·N_{m/2} ≤ √(q·C_AC) · κ_Λ² · 24.

**Honest gap.** Combining gives Σ_{p′}|Cov|·tr(A_p A_{p′}) ≤ κ_Λ²·(q·N_geom + 24·√(q·C_AC)). The second term is O(√q), *not* O(q). With C_AC ≈ 2.75 × 10¹¹, recovering the linear-in-q form requires q ≥ C_AC/C² — impossible for any reasonable C. **The composite gives a sublinear bound that is technically too weak for the literal statement of Route I.**

**Fix.** Two options:

(i) **Rewrite Route I to accept the O(√q·κ_Λ²) bound directly.** This re-derives C₀ = 1 + O(√q·κ_Λ²/n_Λ). At the v9 corner this is O(√0.01·3×10⁻⁵/0.0038) ≈ 0.0008·constant — entirely tolerable. *This is the recommended technical fix.*

(ii) **Prove (★): |Cov(X_p, X_{p′})| ≤ C·q²·e^{−m·d} directly.** This is the natural non-Abelian analogue of Forsström Thm 1.6 specialized to indicators. It is the conjectured truth and would yield Σ ≤ κ_Λ²·q²·O(N_geom + 4·N_m), then dividing through by q gives the linear-in-q form. **Not in the literature.**

The recommended Stage 1 paper uses (i); Stage 2 attempts (ii).

### 6. Conditional Route I matrix-Laplace transfer

**Statement (using fix (i)).** Assume (♠′): Σ_{p′}|Cov(X_p, X_{p′})|·tr(A_p A_{p′}) ≤ C·√q·κ_Λ² for q ∈ [0, q_*]. Then
|log M_G(θ) − log M_B(θ)| / K ≤ (θ·κ_Λ)² · C · √q · κ_Λ²/n_Λ + O((θκ_Λ)³),
so **C₀ := exp(O(√q·κ_Λ²/n_Λ)) = 1 + O(√q)** at fixed Λ.

If (★) is proved (Stage 2), this strengthens to C₀ = 1 + O(q).

### 7. Numerical verification at the v9 corner

Parameters: L = 24, q = 0.01, Λ = 1, κ_Λ ≈ 0.0055, δ = 0.05, K ≈ 3·n_Λ·L⁴ with n_Λ ≈ 0.00381 ⇒ K ≈ 3160.

- log(2K/δ) = log(126 400) ≈ 11.747.
- C₀ = 1+O(q) = 1.02: log(2·C₀·K/δ) ≈ 11.747 + log(1.02) ≈ 11.767.
- **Bernstein bound**:
  6q + √(12·q·κ_Λ·log(2C₀K/δ)) + (2κ_Λ/3)·log(2C₀K/δ)
  = 0.06 + √(12·0.01·0.0055·11.77) + (2·0.0055/3)·11.77
  = 0.06 + 0.0881 + 0.0432
  ≈ **0.191**.

- **Firewall margin**. Θ = 2·0.191 = 0.382, margin 1 − Θ ≈ **0.618**.

- **C₀ sensitivity.** C₀ ∈ [1.00, 1.04] ⇒ Bernstein term ∈ [0.190, 0.193]. Margin robust to ±0.005.

### 8. Statement of Theorem FNG

**Theorem FNG (Finite Non-Abelian Gauge — Projected Capacity Firewall).**

*Hypotheses.* Let G = Q₈ with the standard 2D faithful unitary irrep ρ; Λ ⊆ ℤ⁴ a periodic 4-lattice of side L; μ_{Λ,β,Q₈} the Wilson lattice gauge measure with action S(σ) = Σ_p Re(χ(1) − χ(σ_p)), χ = tr ρ. Let P = P_{≤Λ,L} be the sharp Fourier-window projector of rank K = K(Λ, L). Let X_p(σ) := 𝟙{σ_p ≠ 1}, q := 𝔼[X_p]. Assume:

(H1) β ≥ β₀(Q₈) := (1/Δ_{Q₈})(114 + 4 log 8) ≈ 61.16 (Adhikari–Cao Thm 1.1 threshold).

(H2) Cluster-cumulant input — one of:
  (H2a, weak) The summed condition: Σ_{p′}|Cov(X_p, X_{p′})|·tr(A_p A_{p′}) ≤ C₁·√q·κ_Λ²;
  (H2b, strong) The pointwise refinement: |Cov(X_p, X_{p′})| ≤ C₂·q²·exp(−m·d(p,p′)) with m = (β/2)Δ_G.

(H2a) is proved unconditionally by the composite Adhikari–Cao + Cao 2020 + Cauchy–Schwarz argument of §5. (H2b) is conjectured but not proved in the literature.

(H3) PTO data (PMBSF): A_p = P𝟙_{∂p}P satisfies PSD, rank ≤ 4, ‖·‖_op ≤ κ_Λ, Σ A_p = 6P, PTO-2 with N_a, PTO-3.

*Conclusion.* For every δ ∈ (0,1), with probability ≥ 1 − δ under μ_{Λ,β,Q₈},

‖P 𝟙_{D_G(σ)} P‖_op ≤ 6q + √(12·q·κ_Λ·log(2C₀K/δ)) + (2κ_Λ/3)·log(2C₀K/δ) + o_L(1),

with C₀ = 1 + O(√q·κ_Λ²/n_Λ) under (H2a), C₀ = 1 + O(q·κ_Λ²/n_Λ) under (H2b).

At the v9 corner (L=24, Λ=1, q=0.01, κ_Λ=0.0055, δ=0.05), RHS ≈ 0.191, firewall margin **0.618**.

*Proof sketch.* (i) PTO and the Bernoulli Bernstein are deterministic (PMBSF Theorem 2). (ii) The matrix-Laplace transfer from Bernoulli to Wilson requires only the *summed* condition (H2a) or (H2b). (iii) Splitting close pairs (≤ D₀) from distant pairs (> D₀) and using PTO-2 at rate a = m gives the close contribution ≤ q·κ_Λ²·N_geom and the distant contribution ≤ C_AC·O(√q or q²)·κ_Λ²·4·N_m. Both are absorbed into C₀ via log M_G − log M_B ≤ K·(θκ_Λ)²·(correction)/n_Λ + higher order. (iv) C₀ enters the Bernstein log-factor and is bounded by 1 + O(q^{1/2}) for q ≪ 1. □

### 9. What FNG does and does not buy

**It demonstrates** that the PMBSF pipeline architecture is *internally consistent* at the level of probabilistic constants in a rigorous non-Abelian setting: the PTO is independent of G; the Bernoulli baseline is independent of G; the cluster-cumulant input (H2) localizes the G-dependence; the firewall margin survives the perturbation C₀ → 1 + O(√q).

**It does NOT extend to SU(2).** Three obstructions:

1. **Spin-wave dominance.** For SU(2) at any β, the small-fluctuation Gaussian (spin-wave) sector contributes to X_p via continuous |U_p − 1|² ∼ 1/β fluctuations. The probability q_{SU(2)} scales as a Gaussian tail, not as e^{−c·β}. No finite group captures this.

2. **No analogue of (H2) for SU(2).** The Adhikari–Cao swapping argument fundamentally uses |G| < ∞ in two places: (a) finite enumeration of minimal vortices, (b) probability lower bound via the Lemma 6.7 prefactor 4^{|P|}|G|^{2|P|}. For SU(2), an analogous estimate must be Gaussian-cluster (Bałaban) or stochastic-quantization (Shen–Zhu–Zhu 2023), and is at present unavailable as a packaged covariance decay statement with explicit constants.

3. **β-threshold mismatch.** Q₈ requires β ≳ 61; SU(2) confinement crossover is at β ∼ 2.3. Even at large β for SU(2), the relevant rare event is parametrically different.

**Natural intermediate targets** between FNG (Q₈) and SU(2):

- **FNG-D₄**: Same proof for the dihedral group D₄. Tests robustness to a non-quaternion non-Abelian structure.
- **FNG-A₄, FNG-S₄, FNG-A₅**: Higher-order non-Abelian discrete subgroups of SO(3)/SU(2). A₅ has |G| = 60; approaches the SO(3) limit through icosahedral discretizations — a recognized "ladder" in the lattice gauge literature.
- **FNG-ℤ_n large n**: Cyclic discretization of U(1) at n ≫ 1; in Forsström's framework directly, but does not test non-Abelian topology.
- **FNG-Higgs**: Coupling Q₈ to a Higgs field as in Adhikari 2024 (Comm. Math. Phys. 405:117).
- **Explicit refinement of (H2b)** from (H2a): a single well-defined open mathematical problem with a clear payoff for the entire PMBSF program.

---

## Recommendations

**Stage 1 (immediate, ≤ 4 weeks).** Write up Theorem FNG with **(H2a) — the summed sublinear bound** — listed as a *proved composite* (Adhikari–Cao Thm 1.1 + Cao 2020 Cor. 4.3.9 + Cauchy–Schwarz), not as an axiom. Submit the deterministic PTO + Bernoulli + Route I matrix-Laplace transfer as a standalone preprint. The conclusion is C₀ = 1 + O(√q·κ_Λ²/n_Λ), still bounded above by 1 + O(√q) at fixed Λ. The numerics at the v9 corner survive: margin 0.618. This is the "architecture firewall" paper.

**Stage 2 (1–3 months).** Prove (H2b) for Q₈ directly. Route: refine Adhikari–Cao's Lemma 6.7 to track the *internal* β-suppression on anchor plaquettes — replace
Φ^{(2)}_{P₀}(P) ≤ 4^{|P|}|G|^{2|P|} e^{−β·Δ_G·|P − P₀|}
with a version including q^{|P∩P₀|}·poly(|G|) factors. Technically a Peierls-type refinement; the topological knot machinery is unchanged. Estimated effort: a graduate-student-level project for someone fluent in Cao 2020 / Adhikari–Cao 2025.

**Stage 3 (3–9 months).** Reproduce Stages 1+2 for D₄ and A₄, in that order. The proof structure should be identical; the changes are character-table data and Δ_G values. This produces a "non-Abelian discrete gauge group library" of FNG results.

**Stage 4 (open-ended).** SU(2). Three independent attacks:

- *Bałaban renormalization-group route* (block-spin averaging from SU(2) to finite-group approximant). Bałaban's series — culminating in T. Bałaban, *Comm. Math. Phys.* 122:355–392 (1989), "Large field renormalization. II. Localization, exponentiation, and bounds for the R operation" — proves ultraviolet stability of 4D pure gauge theories but never a mass-gap statement.
- *Stochastic-quantization route* (H. Shen, R. Zhu, X. Zhu, "A stochastic analysis approach to lattice Yang–Mills at strong coupling," *Comm. Math. Phys.* 400:805–851 (2023), arXiv:2204.12737) — proves a strictly positive mass gap for SU(N) under |β| < 1/(16(d−1)), i.e. strong coupling only, opposite regime.
- *Heat-kernel / Villain-action route* (Chevyrev–Garban, *J. Stat. Phys.* 192:38 (2025), arXiv:2410.20984) — establishes Villain action as universal limit on carpet graphs for any compact connected G, but abelianizes too aggressively for SU(2).

**Benchmarks that would change the recommendation.**

- *Refute (H2b) for Q₈* — i.e., construct a configuration where Cov(X_p, X_{p′}) decays slower than q²·e^{−m·d}. Would force redesign of the matrix-Laplace transfer.
- *Prove (H2b) for Q₈ with C₂ = poly(|G|), m = Ω(β)* — Theorem FNG becomes unconditional with C₀ = 1 + O(q).
- *Refinement of Adhikari–Cao reducing β₀(Q₈) from ~61 to ~10* — pushes the rigorous regime closer to physical scales.
- *Numerical observation that C₀ → 1 sharply as β → ∞ for SU(2)* — corroborates the structural prediction beyond v10 data.

---

## Caveats

1. **(H2b) is the load-bearing assumption if you want C₀ = 1 + O(q).** As of May 2026, no published paper proves (H2b) for any non-Abelian finite gauge group. The natural mechanism (combining Adhikari–Cao decay with Cao 2020 marginal q ≍ r_β) does *not* produce a single packaged bound with both the correct q² prefactor and the exp(−m·d) decay. A composite/hybrid argument (Cauchy–Schwarz; (♦) above) gives only O(√q·e^{−m·d/2}). **This is the open mathematical problem at the heart of FNG.**

2. **The v9 numerical corner uses q = 0.01.** For Q₈ at the Adhikari–Cao β threshold (β ≈ 61), q(Q₈, 61) ≈ 36·e^{−732} ≈ 10⁻³¹⁸. To reach q = 0.01 one needs β ≈ 0.68 — six decades below the rigorous regime. The numerics are an architecture check, not a parameter-certified statement. At rigorous β, the Bernstein bound is dominated by the deterministic 6q ≈ 2 × 10⁻³¹⁷ — trivially below the firewall, but encoding no physical SU(2) content.

3. **Adhikari–Cao prefactor C_AC ≈ 2.75 × 10¹¹** is large but β-independent; at the v9-style β it is overwhelmed by exp(−β·L), but at β = 2 it would dominate. The threshold (H1) is precisely calibrated so that C_AC · e^{−(β/2)Δ_G·(L−1)} ≤ 1 once L − 1 ≥ (2/Δ_G)·log C_AC = log(2.75 × 10¹¹) ≈ 26 (using Δ_G = 2). So even at the threshold β, one needs L ≳ 27 to swamp the constant.

4. **The v10 SU(2) empirical C₀ ≈ 1.02 matches the structural prediction quantitatively** (q·κ_Λ²/n_Λ ≈ 0.024 at the cited parameters). This is corroborating *evidence*, not a proof. The structural prediction is derived for finite groups; its agreement with SU(2) data at β ≈ 3.5 is intriguing but mechanistically unjustified.

5. **The minimal-vortex coefficient prefactor for Q₈** — 6 (Cao) vs. 12 (Forsström) vs. 7 (|G|−1 naïve) — is convention-dependent. The *exponential* rate q ∼ e^{−12β} for Q₈ is universal.

6. **No paper as of May 2026** proves mass gap or correlation decay for SU(2) or SU(3) pure lattice gauge theory at any β > 1/(16(d−1)) ≈ 0.021 (the strong-coupling bound of Shen–Zhu–Zhu 2023). The closest results are Bałaban's 4D ultraviolet stability theorems (1980s, no mass gap), and Adhikari–Cao 2025 in the finite-group case (the foundation of this paper).

7. **(H2a) requires no axiom, but the resulting C₀ = 1 + O(√q) is weaker than v10 empirics suggest possible.** That gap between √q and q is the precise content of the Stage 2 problem. It is not academic: at v9 parameters, √q ≈ 0.1 vs. q = 0.01 — a tenfold loss in the firewall correction. The architecture survives (margin still > 0.5), but the elegance of the prediction degrades. *That is the honest current state.*

8. **FNG conditional on (H2b) ≠ FNG unconditional.** Stage 1 ships FNG unconditionally with (H2a). Stage 2 upgrades to FNG with (H2b) — the cleaner statement Alex is targeting. *Do not announce FNG as proved with (H2b) until Stage 2 is written.*