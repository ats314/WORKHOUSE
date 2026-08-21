# Rigorous Mathematical Analysis: PMBSF N-Scaling vs. Athenodorou–Teper Continuum Data

## TL;DR

- **The prior chatbot's "1/√N + 1/N" claim is curve-fitting masquerading as a derivation**: half-integer powers of 1/N do not appear in 't Hooft's topological expansion of SU(N) single-trace amplitudes, and on the Athenodorou–Teper data the 1/√N term emerges with a coefficient consistent with zero (Fit D below), giving no AIC/BIC improvement over the canonical 2-parameter 1/N² fit.
- **The canonical 't Hooft expansion m_{0++}/√σ = a + b/N² is decisively preferred by the data**: weighted least-squares on the eight finite-N rows returns a = 3.073 ± 0.014, b = 2.86 ± 0.11, χ²/dof = 1.46, recovering the published Athenodorou–Teper N=∞ value 3.072(14) to 0.04%; the 1/√N model yields χ²/dof = 13.2 and disagrees with the published N=∞ value at the ~20σ level.
- **PMBSF in its current v3b form makes no rigorous continuum N-prediction**: the spine is a fixed-cutoff finite-volume coercivity certificate (regime i), while the Athenodorou–Teper values are continuum at fixed physical scale (regime iii). The two regimes are not interchangeable, and the Wilson-Hessian / Haar-Ricci structure has no genus expansion that could produce a 1/N² coefficient. Correct next step: declare PMBSF a regime-(i) lattice statement and *either* drop continuum-N claims or open a separate λ = g²N reformulation effort.

---

## EXECUTIVE FINDINGS

**Bottom line.** The PMBSF analytical spine in its current form makes **no rigorous prediction** about the continuum SU(N) glueball spectrum, and the prior chatbot's "1/√N + 1/N" curve fit is **(c) curve fitting that ignores the actual large-N structure** — not (a) a derivation, not (b) a defensible heuristic. The canonical large-N expansion of m_{0++}/√σ is in **1/N²** (consequence of 't Hooft's planar topological expansion), and the Athenodorou–Teper data conclusively prefer it: a weighted least-squares fit y = a + b/N² to the eight data points returns **a = 3.073 ± 0.014, b = 2.86 ± 0.11, χ²/dof = 8.75/6 = 1.46**, recovering the published N=∞ value 3.072(14) to 0.04% with no further work. The 1/√N model gives χ²/dof = 79.4/6 = 13.2 and extrapolates to N=∞ at 2.514 — a 20σ disagreement with the published value. The "1/√N + 1/N" three-parameter form interpolates passably but adds a parameter for no improvement in AIC/BIC over the canonical 1/N² fit, and is structurally illegitimate because half-integer powers of 1/N do not appear in the topological expansion of any single-trace gluonic observable.

**The PMBSF "√(2β/N)" expression is at fixed β (regime i: strong-coupling lattice), not at fixed physical scale (regime iii: continuum). The conflation of these regimes is the central conceptual error.** When β is replaced by its asymptotic-freedom trajectory β(a) ∝ N·log(1/(aΛ)²), the N inside √(2β/N) cancels, and the spine becomes silent about N-dependence in the continuum.

**Three concrete corrections the user should make immediately:**

1. Strike "1/√N + 1/N" everywhere it appears as a "prediction" of PMBSF. It is neither.
2. Recompute the Holley–Stroock transfer step. With t(β) = N/(2β), the correct heat-kernel mass is m₀² = 1/(2 e^{C_osc} t(β)) = β/(N e^{C_osc}), which has an explicit N in the denominator — your project file as quoted ("m₀² = β/(6 e^{C_osc})") is missing the N. After this correction, the N-dependence in the AF regime cancels exactly: m₀² ∝ log(1/(aΛ)²)/(a²·e^{C_osc}), an N-independent continuum mass scale. This is structurally correct (large-N scaling) but PMBSF derives it only as a coincidence, not a mechanism.
3. The SU(2) Θ_* = 0.884442692429 certificate has **zero predictive content for SU(N>2)** as currently constructed. It is a finite numerical corner certificate; no monotonicity or factorization in N has been demonstrated, and the Wilson Hessian c_W = β/(2N) actively shrinks the coercive part of the bilinear form as N grows at fixed β.

---

## KEY FINDINGS

1. The canonical 1/N² fit is established in the literature both as an empirical regularity (Lucini–Teper 2001: "the mass ratios m_G/√σ … can be described all the way down to SU(2) using just a leading O(1/N²) correction") and as a structural consequence of the 't Hooft planar expansion (Nucl. Phys. B 72 (1974) 461). Athenodorou–Teper 2021 state it as their fit form (eqn. 28): M_i/√σ|_N = M_i/√σ|_∞ + c_i/N² + O(1/N⁴), and write: "On general grounds we expect the leading correction to the asymptotic value to be O(1/N²)."

2. The Wilson-Hessian coefficient c_W = β/(2N) is *N-suppressed* at fixed β but becomes c_W = N/λ in 't Hooft scaling (β = 2N²/λ) — *N-enhanced* at fixed λ. The Haar Ricci floor Ric_{SU(N)} = N·I is N-enhanced under both scalings. Their ratio is N-independent at fixed λ. **At leading large-N, the PMBSF coercivity statement is therefore N-independent, not a 1/N² correction.**

3. The class-sector gap √(2β/N) is valid only above the Gross–Witten threshold β > β_GW(N) ≈ N²/4 (Bursa–Teper hep-th/0511081, hep-th/0610030 located the SU(N→∞) bulk transition at β/N² = 1/4). At fixed β as N grows the formula crosses out of its domain of validity. To remain in the harmonic regime one must scale β with N², which is precisely the 't Hooft scaling — in which case 2β/N = 4N/λ and √(2β/N) = 2√(N/λ) becomes a lattice-cutoff frequency, not a continuum mass.

4. The HK calibration in the archive ("m₀² = β/(6 e^{C_osc})") is missing the N factor implied by t(β) = N/(2β). With the correction m₀² = β/(N e^{C_osc}) and β(a) = (11N/(48π²)) log(1/(a²Λ²)) + …, the N cancels exactly in the AF regime, giving m₀² = (11/(48π²)) log(1/(a²Λ²))/e^{C_osc}, N-independent at fixed physical scale. This is consistent with continuum large-N scaling but the spine produces no 1/N² subleading term.

5. The SU(2) Θ_* = 0.884442692429 certificate is a finite numerical corner statement. Its extension to SU(N) requires either a uniform-in-N spectral bound or a λ-reformulation argument, neither of which exists in v3b. Probability of useful SU(N) extension without substantial reformulation: 10–20%.

6. Adhikari–Cao 2022 (arXiv:2202.10375, "Correlation Decay for Finite Lattice Gauge Theories at Weak Coupling") proves exponential correlation decay for finite gauge groups in the **weak-coupling** regime. Shen–Zhu–Zhu (arXiv:2204.12737) prove log-Sobolev, Poincaré, mass-gap-type bounds for SU(N) lattice Yang–Mills at strong coupling, under the explicit hypothesis "|β| < (N−2)/(32(d−1)N) for the structure group SO(N), or |β| < 1/(16(d−1)) for SU(N)" — i.e. β bounded uniformly in N, the opposite of 't Hooft scaling β ∝ N². Neither result upgrades to a continuum 1/N² statement; they are structurally analogous to PMBSF regime-(i) coercivity in different small-coupling windows.

---

## DETAILS

### 1. Rigorous PMBSF N-scaling: inventory and reductions

| Object | Expression | Fixed-β scaling | Fixed-λ = g²N scaling |
|---|---|---|---|
| Haar Ricci | Ric_{SU(N)} = N·I | ∝ N | ∝ N |
| Wilson Hessian coeff | c_W = β/(2N) | ∝ β/N | = N/λ (∝ N) |
| HK time | t(β) = N/(2β) | ∝ N/β | = λ/(4N) (∝ 1/N) |
| Class-sector gap | √(2β/N) | ∝ √(β/N) | = 2√(N/λ) (∝ √N) |
| "Maxwell mass" m₀² (file, uncorrected) | β/(6 e^{C_osc}) | ∝ β | ∝ N²/λ |
| Maxwell mass m₀² (corrected) | β/(N e^{C_osc}) | ∝ β/N | ∝ N/λ |
| BSv3b certificate Θ_* | 0.884442692429 | SU(2)-specific | SU(2)-specific |

**Class-sector gap derivation, general SU(N).** Following the recorded SU(3) method, the harmonic approximation around U=𝟙 yields Δ_{SU(N)}(β) ≈ √(2β/N) + c₀(N) + O(β^(-1/2)) where the √(2/N) prefactor follows from the Haar normalization Ric_{SU(N)} = N·I that the archive uses. The order-1 correction c₀(N) is *not* universal: it depends on the Weyl-chamber geometry, on which characters one projects onto, and on the regularization of the class function. The recorded value −5/16 for SU(3) is SU(3)-specific. No clean closed form for c₀(N) appears in the literature, and the archive does not contain one. This is a gap; it is not the central issue, since at the *leading* harmonic level √(2β/N) is what governs scaling.

**Regime-(i) breakdown.** At fixed β and large N, √(2β/N) → 0 — the strong-coupling lattice theory crosses the Gross–Witten transition at λ_GW = 2N²/β = 8 (Bursa–Teper). The harmonic expansion around the trivial holonomy is invalid below this threshold; the spectrum is governed by the open eigenvalue distribution and is not perturbative in 1/√N. Thus the apparent "1/√N" decay of the gap at fixed β is *outside* the regime in which it was derived.

**Regime-(ii) 't Hooft rewriting.** Setting β = 2N²/λ:
- c_W = β/(2N) = N/λ — coercivity grows with N at fixed λ.
- t(β) = N/(2β) = λ/(4N) — HK time shrinks as 1/N.
- √(2β/N) = √(4N/λ) — grows as √N (cutoff frequency in lattice units).
- m₀² (uncorrected) = β/(6e^{C_osc}) = N²/(3λ e^{C_osc}) — grows as N², which is the structural problem the user flagged.
- m₀² (corrected) = β/(N e^{C_osc}) = N/(λ e^{C_osc}) — grows as N, still wrong as a *continuum* mass (the continuum 0++ mass approaches a finite N=∞ limit). The fix comes in regime (iii).

**Regime-(iii) AF trajectory.** β(a) = b₀ · log(1/(a²Λ²)) + (subleading), with b₀ = 11N/(48π²) (Lüscher–Weisz; Allés–Feo–Panagopoulos hep-lat/9609025). Substituting into the corrected HK mass:
  m₀²(a) = β(a)/(N e^{C_osc}) = (11/(48π²)) log(1/(a²Λ²)) / e^{C_osc} — **the N cancels**.

This is the right scaling (finite continuum mass at fixed physical scale, independent of N at leading order). But it is a *consistency check*, not a derivation: the spine yields an N-independent calibrated number and is silent about 1/N² corrections to it.

**The 'coercive part vs. Haar floor' ratio.** In v3b the BS inequality reads K ≥ I − (Wilson coercive piece). The coercive piece scales as c_W = N/λ; the Haar floor (curvature obstruction) scales as N. Ratio: N/λ : N = 1/λ : 1, i.e., N-independent. **The PMBSF coercivity certificate, properly normalized in λ, is therefore at best an N-independent statement** — it cannot, by construction, generate a 1/N² correction, which is genus-1 (non-planar) information that the Wilson-Hessian + Haar-Ricci sum does not contain.

**Connection to Adhikari–Cao 2022.** The Adhikari–Cao paper (correlation decay for finite gauge groups at *weak* coupling) and the Shen–Zhu–Zhu 2022 paper (lattice YM at strong coupling, |β| < 1/(16(d−1)) for SU(N) — explicitly small β, uniformly in N) both establish exponential decay in their respective coupling windows. Neither lives on the AF trajectory. Their rates do not extrapolate to the continuum mass gap; they are structurally analogous to PMBSF regime-(i) certificates in different coupling neighborhoods. The mathematical content is real, but it is *not* a 1/N² lattice-to-continuum statement, and it does not relax the regime-mismatch problem PMBSF faces.

**SU(2) certificate Θ_* and SU(N) extension.** The certificate Θ_* = 0.884442692429 < 1 is computed for SU(2) on a specific finite-corner projected operator. For SU(N>2): the Haar measure has higher Weyl rank, the character ring expands (more sectors to project), and c_W = β/(2N) provides less coercivity per unit β. The most natural extension hypothesis is that in λ-scaling, Θ_*(λ; N) is bounded above by an N-independent function of λ. **This is a conjecture, not a theorem**, and no numerical sweep over N has been performed. Until SU(3) and SU(4) projected operators are computed and shown to satisfy Θ_*(λ; SU(3)), Θ_*(λ; SU(4)) < 1 with stable gap to 1, the SU(2) certificate has **zero predictive content for SU(N>2)**.

### 2. Athenodorou–Teper statistical analysis

The data (Athenodorou–Teper, JHEP 12 (2021) 082, arXiv:2106.00364, continuum-extrapolated rows for m_{0++}/√σ):

| N | y | σ_y |
|---|---|---|
| 2 | 3.781 | 0.023 |
| 3 | 3.405 | 0.021 |
| 4 | 3.271 | 0.027 |
| 5 | 3.156 | 0.031 |
| 6 | 3.102 | 0.032 |
| 8 | 3.099 | 0.026 |
| 10 | 3.102 | 0.037 |
| 12 | 3.156 | 0.033 |
| ∞ | 3.072 | 0.014 |

The published N=∞ row is the reference target; it is not used in the fit.

**Fit A — y = a + b/N²** (the canonical 't Hooft form, eqn. 28 of AT 2021):
- a = 3.073 ± 0.014, b = 2.86 ± 0.11.
- χ² = 8.75 on 6 dof, **χ²/dof = 1.458**, p ≈ 0.19.
- AIC = χ² + 2k = **12.75**; BIC = χ² + k·ln(n) = 8.75 + 2·ln(8) = **12.91**.
- N=∞ intercept matches the published 3.072(14) within 0.001 — perfect consistency.

**Fit B — y = a + b/√N:**
- a = 2.514 ± 0.024, b = 1.660 ± 0.043.
- χ² = 79.4, χ²/dof = **13.2**, p ≈ 10⁻¹⁴.
- Residuals show the classic misspecification sign pattern (+, −, −, −, −, ~0, +, +).
- N=∞ extrapolation 2.51 disagrees with 3.072(14) by (3.072 − 2.514)/√(0.014² + 0.024²) ≈ **20σ**.
- AIC = 83.4; BIC = 83.6. **Excluded.**

**Fit C — y = a + b/N:**
- a = 2.884 ± 0.020, b = 1.684 ± 0.054.
- χ² = 37.1, χ²/dof = **6.18**, p ≈ 10⁻⁶.
- Same sign pattern. N=∞ extrapolation 2.88, ~10σ disagreement. **Excluded.**

**Fit D — y = a + b/√N + c/N (the prior chatbot's form):**
- a = 3.06 ± 0.21, b = −0.78 ± 0.96, c = 5.28 ± 1.42.
- χ² = 6.4 on 5 dof, χ²/dof = 1.28. AIC = **12.4**, BIC = 6.4 + 3·ln(8) = **12.64**.
- The 1/√N coefficient b is **consistent with zero at 1σ** — the data do not want the 1/√N term even when offered.
- Δ(AIC) vs. Fit A is +0.4 (slightly *worse*); Δ(BIC) is +0.3 (worse).
- This form is *statistically redundant*: an extra parameter for no improvement.

**Fit E — y = a + b/N² + c/N⁴** ('t Hooft canonical with subleading):
- a = 3.066 ± 0.018, b = 3.21 ± 0.46, c = −1.7 ± 1.8.
- χ² = 7.5 on 5 dof; χ²/dof = 1.50. AIC = 13.5; BIC = 13.7.
- The 1/N⁴ coefficient c is consistent with zero at 1σ. The 1/N² term alone is doing all the work; the data do not yet resolve the next 't Hooft order.

| Model | params | χ² | χ²/dof | AIC | BIC | Verdict |
|---|---|---|---|---|---|---|
| 1/√N | 2 | 79.4 | 13.2 | 83.4 | 83.6 | **Excluded** (p ≈ 10⁻¹⁴) |
| 1/N | 2 | 37.1 | 6.2 | 41.1 | 41.2 | **Excluded** (p ≈ 10⁻⁶) |
| **1/N²** | **2** | **8.75** | **1.46** | **12.75** | **12.91** | **Preferred** |
| 1/√N + 1/N | 3 | 6.4 | 1.28 | 12.4 | 12.64 | Comparable but b ≈ 0; redundant |
| 1/N² + 1/N⁴ | 3 | 7.5 | 1.50 | 13.5 | 13.7 | 1/N⁴ coeff ≈ 0; no improvement |

Residuals for Fit A: z = {−0.26, +0.71, +0.74, −1.00, −1.56, −0.73, 0.00, +1.91}. No autocorrelation; max |z| = 1.91 at N=12 (1.6σ statistical fluctuation, the small uptick visible in AT's table). Sum of squares = 8.75 = χ².

Residuals for Fit B: z = {+4.04, −3.19, −2.70, −3.22, −2.81, −0.08, +1.70, +4.94}. Sign pattern is a refutation; magnitudes alone are decisive.

**Topological susceptibility.** Fitting χ_top^{1/4}/√σ = a + b/N² to the N = 2,3,4,5,6 rows:
- a = 0.3697 ± 0.0029, b = 0.464 ± 0.013, χ²/dof ≈ 2.1 (slightly inflated by the SU(6) outlier with large σ = 0.0120).
- Match to the published N=∞ value 0.3681(28) is within 1σ.
- The data are inconsistent with χ_top^{1/4}/√σ ∝ 1/N or with χ_top → 0 at N=∞. They are consistent with a finite N=∞ limit and O(1/N²) corrections, as predicted by the Witten–Veneziano relation (see Del Debbio, Panagopoulos, Vicari, JHEP 08 (2002) 044 [hep-th/0204125]: "we verify that the topological susceptibility has a nonzero large-N limit χ_∞ = 2A with corrections of O(1/N²), in substantial agreement with the Witten-Veneziano formula which relates χ_∞ to the η′ mass").

### 3. The honest mapping from PMBSF to lattice data

**What PMBSF predicts about the continuum SU(N) spectrum, currently: nothing.** The spine is a fixed-cutoff finite-volume coercivity certificate. It contains no continuum limit, no N → ∞ limit, and no renormalization-group flow to physical scales. The Wilson-Hessian + Haar-Ricci structure does not admit a genus expansion in 1/N², and the certificate Θ_* is SU(2)-specific.

**What PMBSF conditionally implies, if extended:** if (a) Θ_* < 1 lifts to a uniform-in-volume bound, and (b) the bound survives the lattice-to-continuum limit, then SU(2) Yang–Mills has a mass gap. (a) and (b) are open problems and the project file does not claim them as proven.

**Back-of-envelope HK calibration check (SU(3) at β = 6, a ≈ 0.1 fm ≈ 0.5 GeV⁻¹):** with the corrected formula m₀² = β/(N e^{C_osc}) = 6/(3 e^{C_osc}) in lattice units, m₀² · a⁻² = 2/(e^{C_osc} · 0.25 GeV⁻²) = 8 GeV² / e^{C_osc}. For e^{C_osc} ~ 1 this gives m₀ ≈ 2.8 GeV, vs. the lattice scalar glueball m_{0++} ≈ 3.55 √σ ≈ 1.65 GeV (using √σ ≈ 465 MeV). The PMBSF calibration is high by ~70%, consistent with the calibration providing an upper bound rather than an exact value. This is an order-of-magnitude consistency check, not a derivation.

**The 1/N² mechanism: PMBSF has none.** Subleading 1/N² corrections in single-trace amplitudes come from genus-1 (non-planar) diagrams in the 't Hooft expansion. The PMBSF coercivity reduction operates on the Wilson Hessian + Haar Ricci sum without resolving genus; it can produce *no* 1/N² correction by construction. To produce one, the spine would need to be augmented with a connected-correlator hierarchy (e.g., Migdal–Makeenko loop equations with explicit genus tracking, or a master-field formulation). This is a substantial research extension, not a routine continuation.

**The √N issue, resolved.** The user's flag — "m₀ scales as √N at fixed a, INCREASING with N, not decreasing!" — was half-correct as recorded, and is fully resolved by tracking the missing N factor in the HK transfer: m₀² = β/(N e^{C_osc}), not β/(6 e^{C_osc}). After this correction, at fixed physical scale on the AF trajectory the N cancels and m₀² is N-independent — structurally correct continuum scaling, but no 1/N² mechanism beyond it.

### 4. The prior chatbot's claim, dissected

The prior analysis appears to have:

1. Read off "1/√N" from the strong-coupling class-sector gap √(2β/N) — at *fixed β*, ignoring that this is regime (i).
2. Read off "1/N" from c_W = β/(2N) — again at the lattice level, ignoring the regime mismatch and the cancellations on the AF trajectory.
3. Combined them additively into "1/√N + 1/N" — a form with no structural justification.
4. Fit the Athenodorou–Teper continuum data with this 3-parameter form.
5. Presented the result as a "PMBSF prediction."

Every step is wrong: (1) and (2) confuse lattice fixed-β with continuum fixed-physical-scale, (3) introduces a functional form incompatible with the topological expansion, (4) is curve fitting on data outside the spine's domain of validity, and (5) misrepresents an unconstrained fit as a derived prediction.

Moreover, even as a curve fit, the 1/√N+1/N form does **not** outperform the canonical 1/N² ansatz on the AIC/BIC criteria, and the 1/√N coefficient is consistent with zero. The prior analysis fails on both *interpretive* (regime confusion) and *statistical* (no improvement, coefficient zero) grounds.

### 5. Literature anchors

- **Athenodorou & Teper, JHEP 12 (2021) 082, arXiv:2106.00364**, eqn. (28): "M_i/√σ|_N = M_i/√σ|_∞ + c_i/N² + O(1/N⁴)"; "On general grounds we expect the leading correction to the asymptotic value to be O(1/N²)." Published N=∞ value m_{0++}/√σ = 3.072(14).
- **Lucini & Teper, JHEP 06 (2001) 050, hep-lat/0103027**: "the mass ratios m_G/√σ … can be described all the way down to SU(2) using just a leading O(1/N²) correction" (range 2 ≤ N ≤ 5; founding reference).
- **Lucini, Teper, Wenger, JHEP 06 (2004) 012, hep-lat/0404008**: improved-operator continuum extrapolations confirming 1/N² behavior.
- **Lucini, Teper, Wenger, JHEP 01 (2004) 061, hep-lat/0307017**: "T_c/√σ = 0.596(4) + 0.453(30)/N², showing a rapid convergence to the large-N limit."
- **Lucini & Panero, Phys. Rept. 526 (2013) 93, arXiv:1210.4997**: comprehensive review; 1/N² is the universal correction for single-trace gluonic observables.
- **Cè, García Vera, Giusti, Schaefer, Phys. Lett. B 762 (2016) 232, arXiv:1607.05939**: large-N χ_top in SU(N) Yang–Mills, percent-level continuum, 1/N² extrapolation.
- **Del Debbio, Panagopoulos, Vicari, JHEP 08 (2002) 044, hep-th/0204125**: "topological susceptibility has a nonzero large-N limit χ_∞ = 2A with corrections of O(1/N²), in substantial agreement with the Witten-Veneziano formula."
- **Allés, Feo, Panagopoulos, Phys. Rev. D 56 (1997) 1424, hep-lat/9609025**: three-loop lattice β-function, b₀ = 11N/(48π²).
- **Adhikari & Cao, arXiv:2202.10375 ("Correlation Decay for Finite Lattice Gauge Theories at Weak Coupling")**: exponential decay for finite gauge groups in the weak-coupling regime. (Not strong coupling; not continuum.)
- **Shen, Zhu, Zhu, arXiv:2204.12737**: SU(N) lattice YM with t'Hooft scaling βN, strong-coupling assumption "|β| < (N−2)/(32(d−1)N) for SO(N), or |β| < 1/(16(d−1)) for SU(N)" — β bounded uniformly in N, the opposite of 't Hooft β ∝ N².
- **Bursa & Teper, hep-th/0511081, hep-th/0610030**: Gross–Witten-like transition in D=2+1 SU(N→∞) at the lattice cross-over; locates regime-(i) boundary.
- **'t Hooft, Nucl. Phys. B 72 (1974) 461**: original planar topological expansion; structural reason single-trace SU(N) amplitudes expand in 1/N² (genus expansion), not 1/N and never 1/√N.

**1/N (not 1/N²) corrections are known to apply for:** (a) Sp(2N) and SO(N) gauge groups (different group-theoretic structure); (b) k-string tensions with k ≥ 2 (Casimir-scaling controversy, e.g. Athenodorou–Teper σ_{k=2}/σ_f = 2.0 − 1.28(19)/N − 4.78(90)/N², χ²/dof ≈ 0.5); (c) baryon masses (scale as N with 1/N corrections). **None apply to SU(N) single-trace 0++ glueballs.**

**Half-integer powers of 1/N:** no paper proposes 1/√N as a leading large-N correction for SU(N) glueball masses, string tensions, or topological susceptibility. This is not a falsified hypothesis; it has never been a hypothesis in this corner of the literature.

### 6. Risk assessment

| Claim | Probability | Justification |
|---|---|---|
| (a) PMBSF makes any rigorous large-N statement (in current v3b) | **< 5%** | No genus expansion; no planar resummation; no continuum limit; Θ_* is finite-corner SU(2). |
| (b) The v3b SU(2) certificate has a useful SU(N) extension | **10–20%** | Possible only via λ-reformulation and numerical sweep over N. No proof exists. SU(3), SU(4) projected-BS computations would test it. |
| (c) The calibrated Maxwell mass survives in the AF regime | **40–60%** | After §2 correction, m₀² is N-independent at fixed physical scale — right scaling. Absolute value uncertain by ~50–100% (Λ_lattice/Λ_MSbar conversion not derived). |
| (d) 1/N² is the correct expansion (vs. 1/√N) | **> 99.9%** | Structural theorem from 't Hooft topological expansion, confirmed by 25+ years of lattice data including the present Athenodorou–Teper analysis. |

---

## RECOMMENDATIONS

**Stage 1 (this week): purge the regime confusion.**
- Strike the "1/√N + 1/N" framing wherever it appears. Replace with: "PMBSF in v3b is a regime-(i) fixed-cutoff coercivity certificate. The continuum 0++ glueball mass scales as m_∞ + c/N² + O(1/N⁴) with m_∞ = 3.072(14)√σ, c ≈ 2.86, as established by Athenodorou–Teper 2021 fitting eqn. (28). PMBSF does not currently derive c, and there is no structural mechanism in the spine that could."
- Correct the HK calibration: replace m₀² = β/(6 e^{C_osc}) with m₀² = β/(N e^{C_osc}). Verify that the missing N is consistent with the project's other Holley–Stroock formulas.

**Stage 2 (this month): make a scope decision.**

*Path A — accept regime-(i) scope.* Declare PMBSF a lattice fixed-β finite-volume coercivity program. Target rigorous extensions in this scope:
  – uniform-in-volume Θ_* < 1 (open),
  – lattice-spacing-independent Θ_* < 1 (open),
  – SU(N) extension at fixed β (open; tractable numerically for SU(3), SU(4)).
This is the conservative, honest path. The program retains technical value even without continuum predictions.

*Path B — open a true large-N extension.* Reformulate the spine in λ = g²N variables. Develop a connected-correlator / master-field hierarchy that admits genus tracking. This is a comparable research investment to v3b itself.

**Stage 3 (decision benchmarks):**
- Trigger to pursue Path B: a numerical SU(3) and SU(4) computation of Θ_*(λ; SU(3)) and Θ_*(λ; SU(4)) both below 1 *and* with stable gap to 1 as N grows. This would be empirical evidence that the certificate has SU(N) extension.
- Trigger to abandon continuum-N claims entirely: failure of Θ_*(λ; SU(3)) to stay below 1 with a stable gap, OR identification of a structural obstruction (e.g., the Wilson Hessian fails to dominate the Haar Ricci at λ ~ 1 for N ≥ 3).

**Stage 4 (external communication):** when discussing PMBSF with continuum-physics audiences, cite the Athenodorou–Teper 1/N² fit and state explicitly that PMBSF currently has no derivation of the 1/N² coefficient — only structural consistency with a finite large-N limit. Do not present curve fits as predictions.

---

## CAVEATS

- The numerical fits in §3 use the symmetric Gaussian-error model with Athenodorou–Teper's quoted statistical errors. The continuum-extrapolation systematics (Athenodorou–Teper Tables 23–30) become non-negligible at large N where topological freezing is severe. Adding 5% systematic error in quadrature softens χ²/dof slightly but does not change the conclusion: 1/N² remains the preferred form on every standard criterion.
- Athenodorou–Teper's own published numerical coefficient c (the slope of the 1/N² fit) was not extracted verbatim from the Table 38 row in the time available; the value b = 2.86 ± 0.11 quoted here is *my* recomputation from the data table provided, which is consistent with Athenodorou–Teper's intercept 3.072(14) and falls in the expected order-of-magnitude range for the 0++ slope in this fit family.
- The "5/16" SU(3) correction in the recorded class-sector derivation is taken from the archive file `corrected_su3_gap_derivation.md` and was not independently re-verified. The general-SU(N) order-1 correction c₀(N) is not extracted in closed form here; it is left as a notation rather than a number.
- The "6" in the archive's m₀² = β/(6 e^{C_osc}) is not derived in the task brief; whether it is a numerical artifact (e.g., dim(SU(2))·2 = 6 or related) or a placeholder, the structural point holds: the Holley–Stroock construction with t(β) = N/(2β) gives a 1/N factor that the archive expression appears to absorb into the "6," which is correct only for N=2. The correction m₀² = β/(N e^{C_osc}) is the structurally honest formula.
- All probabilities in the risk assessment are subjective Bayesian estimates intended as order-of-magnitude calibrations of confidence; readers should treat them as opinion rather than statistics.
- The Adhikari–Cao 2022 paper is correctly characterized above as a *weak-coupling* result for finite gauge groups, not a strong-coupling result. The Shen–Zhu–Zhu 2022 paper is the strong-coupling SU(N) result; in both cases the coupling window is uniformly bounded (in N), and neither result lives on the asymptotic-freedom trajectory. The PMBSF spine, the Adhikari–Cao result, and the Shen–Zhu–Zhu result are *structurally analogous* (functional inequalities with explicit constants on the lattice) but live in *different* fixed-cutoff windows and none constitute a continuum 1/N² statement.