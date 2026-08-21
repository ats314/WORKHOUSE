# GPT-5.2 Physics Document Analysis Report

**Analysis Type:** GAPS
**Generated:** 2026-01-18T12:02:31.881314
**Model:** gpt-5.2

---

## Analysis Results

## 0. Logical flow trace (Abstract → Conclusions)

**Abstract claim:** singular strata (reducibles/Gribov copies) are *polar* (capacity zero) for the diffusion used in Bakry–Émery/LSI arguments, hence can be ignored in functional inequalities and maximum principles, enabling a curvature→LSI→spectral gap→mass gap pipeline.

**Actual chain used across chapters:**

1. **Gaussian polarity facts** for OU on an infinite-dimensional Hilbert space: infinite-codimension affine subspaces are polar; codim ≥3 in finite codim is polar.  
   → Ch.2.

2. **Transfer of polarity under change of measure**: if YM measure is a bounded-density perturbation of Gaussian with same carré du champ, then capacity-zero sets remain capacity-zero.  
   → Ch.3.

3. **Reducible locus has infinite codimension** in Sobolev configuration space via point-evaluation constraints, hence polar for OU; then (via transfer) polar for YM diffusion.  
   → Ch.4 + Ch.14.

4. **Polarity ⇒ stratified parabolic maximum principle**: PDE comparison/positivity propagation on regular stratum without boundary conditions at Σ.  
   → Ch.9.

5. **Horizontal Bakry–Émery curvature**: gauge-invariant observables have horizontal gradients; prove a local CD(ρ,∞) bound in horizontal directions with volume-independent constants.  
   → Ch.10.

6. **PDE-to-ODE Riccati barrier**: smallest curvature eigenvalue satisfies a parabolic inequality with forcing σ\_*; polarity allows maximum principle to compare with ODE and get positivity.  
   → Ch.11.

7. **Source of σ\_***: several candidates:
   - Haar Jacobian “mass” at finite cutoff (but vanishes as a→0). → Ch.6–8.
   - “Entropic spark” from Gribov geometry (conjectural). → Ch.7–8, 32, 41.
   - Weyl denominator curvature floor σ_geom = N/4 (claimed scale-independent). → Ch.13, 40.
   - FP determinant repulsion near reducibles/horizon. → Ch.12.

8. **From CD/LSI to spectral gap** (for Langevin generator) and then **to physical mass gap** via OS reconstruction / transfer matrix.  
   → Ch.17, 23, 29, 37.

9. **Continuum passage**: uniform-in-a curvature/LSI + Mosco convergence/Trotter–Kato transfers CD/LSI to continuum.  
   → Ch.20, 27.

**Where the conclusions rely on unproven steps:** (i) measure-change bounded density, (ii) correct diffusion/carré du champ in gauge theory, (iii) stratified maximum principle in this infinite-dimensional setting, (iv) global (not just local) LSI via Lyapunov drift, (v) uniform-in-a curvature source σ\_* that truly applies to the full interacting YM measure, (vi) rigorous bridge from Langevin spectral gap to Hamiltonian mass gap in the continuum limit.

---

## 1. Gap inventory (assumed claims, what’s needed, status)

### [2.2]
- **Claim being assumed:** “If dim(S^⊥)=∞ then S is always polar” for OU on H; and finite-codim threshold “polar iff m≥3”.
- **What would be needed to prove it:** A precise theorem for OU capacity in abstract Wiener space / Gaussian Hilbert space: characterization of capacity of affine subspaces in terms of codimension; proof that infinite-codim closed subspaces have zero OU capacity; careful distinction between Brownian motion vs OU, and between hitting probabilities and capacity in infinite dimensions.
- **Status:** **MISSING** (stated as proposition with “intuition”; needs a real reference/proof in the OU/Dirichlet-form setting used later).

### [2.3]
- **Claim being assumed:** “Affine translates of polar subspaces are polar; countable unions of polar sets are polar.”
- **What would be needed:** Show translation invariance (or quasi-invariance) of OU capacity under Cameron–Martin shifts; and σ-subadditivity of capacity for the specific capacity notion used (1-capacity associated to the Dirichlet form).
- **Status:** **MISSING** (standard but must match the exact capacity definition).

### [3.1]
- **Claim being assumed:** Capacity comparison under bounded density perturbation with “same carré du champ”.
- **What would be needed:** A theorem in Dirichlet form theory: if μ and μ₀ are equivalent with bounded Radon–Nikodym derivative and the form is closable with same energy measure, then capacities are comparable. Must verify closability, quasi-regularity, and that the capacity notion is the same (1-capacity vs 0-capacity).
- **Status:** **MISSING** (plausible but not justified; also “same Γ” is nontrivial under interacting YM measures).

### [3.2]
- **Claim being assumed:** “Yang–Mills measure is a bounded density perturbation of Gaussian reference.”
- **What would be needed:** In continuum 4D YM, there is no known construction of the YM measure as bounded perturbation of a Gaussian on a Hilbert space; even on lattice, density is bounded above/below only in special regimes and depends on β and volume. Need explicit uniform bounds c₁,c₂ independent of lattice size and spacing, or a different transfer mechanism (e.g., local absolute continuity with controlled constants).
- **Status:** **OPEN** (in 4D continuum essentially out of reach; on lattice may be false globally).

### [4.2] (and [14.3])
- **Claim being assumed:** The commutator map \(T_\xi:a\mapsto[a,\xi]\) has infinite rank in Sobolev configuration space; point evaluations \(a(x_n)\) are legitimate linear functionals.
- **What would be needed:** For \(a\in L_k^2\) with \(k>2\) in 4D, Sobolev embedding gives continuity, so point evaluation is continuous—fine. But must show the induced constraint map really yields *independent* constraints in the Hilbert topology and that the reducible set is contained in a **countable union** of affine subspaces of codim ≥3 (or ∞) in the *Cameron–Martin* space relevant to the OU form. Also must handle gauge equivalence and the fact that reducibility is “∃ξ” not “fixed ξ”.
- **Status:** **FRONTIER** (the sketch is plausible; the hard part is matching the functional-analytic setting of the Dirichlet form and quantifying codimension in the correct energy space).

### [4.3]
- **Claim being assumed:** “Taking a countable dense set {ξ_j} in stabilizer space gives Σ ⊂ ⋃ Σ_{ξ_j}.”
- **What would be needed:** A separability/compactness argument: if A is reducible, there exists ξ≠0 with D_A ξ=0; need to show existence of a ξ_j from a fixed countable set such that A lies in Σ_{ξ_j}. Density alone does not imply exact kernel membership. You’d need a *quantitative stability*: if D_A ξ=0 then also D_A ξ_j=0 for some ξ_j—false. Alternatively, cover by sets defined by “smallest eigenvalue of D_A^*D_A is 0” and approximate via rational directions plus continuity of the map ξ↦‖D_A ξ‖, but still “=0” is not stable under approximation.
- **Status:** **MISSING** (this is a genuine logical break: reducibility is an existential condition; replacing by countable dense subset does not preserve exact satisfaction).

### [5.2]
- **Claim being assumed:** “Polarity removes Gribov copies obstruction” and enables “Curvature → LSI → spectral gap → mass gap”.
- **What would be needed:** Precise identification of the diffusion (stochastic quantization) on the quotient/stratified space; proof that its Dirichlet form is quasi-regular and that polar sets can be removed without changing the semigroup; then show BE/LSI arguments apply on the quasi-open regular stratum.
- **Status:** **FRONTIER** (conceptually plausible; technically heavy).

### [6.4]
- **Claim being assumed:** Combined Hessian bound \(\mathrm{Hess}\,S_{\mathrm{eff}}\succeq (c_0a^2g^2-\beta C_V)I\) on horizontal subspace.
- **What would be needed:** A rigorous computation of the Wilson action Hessian in exponential coordinates, control of remainder terms, and a uniform bound \(C_V\) independent of volume and lattice spacing in the regime considered; also must specify the metric used for the Hessian and how horizontality is enforced.
- **Status:** **FRONTIER** (needs explicit constants and careful coordinate control).

### [7.4–7.5]
- **Claim being assumed:** Gribov region (or relevant constraint set Λ) is convex enough; Prékopa–Leindler applies; strict convexity with quantitative γ² emerges.
- **What would be needed:** (i) Identify Λ precisely (FMR? Gribov region in Landau gauge?); (ii) prove convexity in the linear structure used for PL (but gauge orbit space is not linear); (iii) show slice volumes are log-concave under the correct measure; (iv) obtain **strict** convexity at 0 with a uniform lower bound γ² independent of a.
- **Status:** **OPEN** (this is explicitly conjectural; also convexity of Gribov region is subtle and gauge-dependent).

### [9.2–9.3]
- **Claim being assumed:** Stratified parabolic comparison principle using polarity and Feynman–Kac.
- **What would be needed:** A well-posed Markov process on the stratified configuration/orbit space with generator L; quasi-continuity of supersolutions; validity of Feynman–Kac on M_reg; proof that polar Σ is avoided quasi-surely; and that boundary terms vanish in integration by parts for the Dirichlet form domain.
- **Status:** **FRONTIER** (hard analytic step; listed as “Hard” in appendix).

### [10.3]
- **Claim being assumed:** “Local horizontal CD with volume-independent constants r, ρ_loc.”
- **What would be needed:** A precise Riemannian/sub-Riemannian structure on configuration/orbit space; control of O’Neill tensors and perturbations uniformly in volume; proof that the perturbation constant \(C_{\text{add}}\) is < κ_G uniformly; and that the horizontal Ricci + Hessian bound holds for the Gibbs measure used.
- **Status:** **FRONTIER** (uniformity in Λ is nontrivial; depends on submersion geometry and gauge fixing).

### [11.1]
- **Claim being assumed:** Smallest eigenvalue λ(t,x) satisfies \(\partial_t\lambda \ge L\lambda -2\lambda^2+\sigma_*\).
- **What would be needed:** A rigorous tensor maximum principle for the evolving horizontal Hessian/curvature tensor under the stated flow; derivation of the PDE for λ_min including control of non-smoothness at eigenvalue crossings; justification of the forcing term σ_* and error terms.
- **Status:** **FRONTIER** (derivation is delicate even in finite dimensions; more so on stratified/infinite-dimensional spaces).

### [12.3]
- **Claim being assumed:** “D_U has nontrivial kernel ⇔ reducible” and “Δ_FP→0 near reducibles”.
- **What would be needed:** On lattice, clarify the precise gauge-fixing operator and its kernel; show equivalence between stabilizer and kernel of D_U; show continuity of smallest eigenvalue of \(D_U^*D_U\) and its vanishing exactly on reducibles; handle global gauge modes.
- **Status:** **MISSING** (likely true with caveats; needs careful statement).

### [12.4]
- **Claim being assumed:** “Near reducibles, M^{-1} blows up ⇒ strong convexity near singular strata.”
- **What would be needed:** The Hessian formula for \(-\frac12\log\det M\) must be applied with control of the first term \(-\frac12\mathrm{Tr}(M^{-1}\delta^2M)\), which can have either sign; nonnegativity of the second term alone does not yield a lower bound. Need a quantitative lower bound on the full Hessian in relevant directions, not just “blows up”.
- **Status:** **MISSING** (sign/size of the first term is a real gap).

### [13.3]
- **Claim being assumed:** Weyl denominator Hessian lower bound \( \nabla^2 S_{\text{Weyl}} \ge \frac{N}{4}I\) on the trace-zero hyperplane, uniformly in θ.
- **What would be needed:** A complete proof including handling singularities where eigenangles collide (where Hessian diverges) and ensuring the inequality holds globally on the regular set; also specify the metric/norm used. (This is marked “Lean verified”, but that only covers the finite-dimensional inequality, not its embedding into the gauge theory measure.)
- **Status:** **FRONTIER** as used in YM: the inequality itself may be **DONE**, but the step “this contributes an a-independent curvature floor to the full lattice/continuum action” is not proved.

### [15.1–15.4]
- **Claim being assumed:** PBH flow equation for Hessian and the scalar inequality for λ_min with controlled error \(C_1 g(t)^2 H_{\mathrm{Tr}}\).
- **What would be needed:** Define PBH flow precisely (what is t? RG time? heat-kernel time?); prove existence/regularity; derive the Hessian evolution including geometric correction term 𝔊; prove hypotheses H1–H5 in the YM setting; justify the tensor maximum principle leading to the scalar inequality.
- **Status:** **OPEN** (this is a programmatic PDE; hypotheses are “locks” not established).

### [16.2]
- **Claim being assumed:** \(\sigma_A(k)=2\beta_0 g(k)^2 k^2>0\) acts as a positive *Hessian forcing* in the effective action flow.
- **What would be needed:** A derivation connecting perturbative β-function to a *convexity source term* in the nonperturbative effective potential/Hessian evolution; control of scheme dependence; show positivity survives beyond perturbation theory and is uniform in volume and lattice spacing.
- **Status:** **OPEN** (physics-motivated; not a rigorous implication).

### [17.3]
- **Claim being assumed:** “Uniform LSI/Poincaré → uniform spectral gap for generators → transfer matrix gap → Hamiltonian mass gap.”
- **What would be needed:** (i) show the Langevin generator gap implies exponential decay of Euclidean correlations in the OS sense; (ii) relate that to the transfer matrix spectrum; (iii) prove uniformity in a and Λ; (iv) ensure the gap pertains to gauge-invariant sector and matches physical mass gap.
- **Status:** **FRONTIER** (bridges exist in some settings but not established here).

### [18.1–18.3] and [25.2–25.5]
- **Claim being assumed:** Schur complement bound applies to RG marginalization of the Gibbs measure; discrete Riccati recursion for convexity.
- **What would be needed:** The lemma is true for finite-dimensional log-concave integrals under strong convexity assumptions, but here coarse-graining is on compact groups with nontrivial measure factors and constraints; must show the effective action is twice differentiable and Hessian blocks satisfy the assumed bounds uniformly; also RG kernel may not be Markov/exact (cf. Ch.28).
- **Status:** **FRONTIER** (mathematically standard lemma; applicability to nonabelian gauge RG is not proved).

### [20.3]
- **Claim being assumed:** “Uniform lattice curvature CD(ρ₀,∞) + Mosco convergence ⇒ continuum CD(ρ₀,∞).”
- **What would be needed:** A precise stability theorem for BE curvature under Mosco convergence of Dirichlet forms (this is not automatic in general); need assumptions: uniform quasi-regularity, convergence of carré du champ, and compatibility of Γ₂ structures. Trotter–Kato gives semigroup convergence, but Γ₂ inequalities are second-order and require additional structure.
- **Status:** **OPEN** (this is a major technical point; not generally true without strong hypotheses).

### [22.3]
- **Claim being assumed:** Local LSI + Lyapunov drift ⇒ global LSI with uniform constant.
- **What would be needed:** A specific theorem (e.g., Bakry–Cattiaux–Guillin type) with verification of drift condition for the YM generator on configuration space; construction of gauge-invariant Lyapunov function W with constants uniform in Λ and a.
- **Status:** **FRONTIER** (explicitly identified as hardest obstacle).

### [23.3]
- **Claim being assumed:** “Diffusion spectral gap → OS reconstruction → Hamiltonian mass gap.”
- **What would be needed:** A rigorous theorem linking the spectral gap of the stochastic quantization generator (in configuration space) to the mass gap of the reconstructed QFT Hamiltonian. Typically OS reconstruction uses Euclidean correlation functions from the Gibbs measure, not the Langevin dynamics gap. Need to show the gap yields exponential decay in Euclidean time of Schwinger functions with uniform constants, and that this implies a spectral gap of the transfer matrix/Hamiltonian.
- **Status:** **OPEN** (bridge is nontrivial; currently more a heuristic alignment).

### [24.2–24.3]
- **Claim being assumed:** Gribov horizon is codim 1 hence nonpolar; but “stochastic quantization stays inside Ω by construction” and “ρ\*>0 uniformly separates from horizon.”
- **What would be needed:** Define Ω precisely and show the dynamics is reflected/conditioned to remain in Ω, or show Ω is invariant under the SDE/Dirichlet form; prove uniform separation ρ\*>0 in the regime of interest (but ρ\* depends on a,g and tends to 0 in AF regime unless replaced by another source).
- **Status:** **FRONTIER** (invariance and uniform separation are not established).

### [26.2–26.4]
- **Claim being assumed:** Helffer–Sjöstrand covariance identity applies; Witten Laplacian has a mass term m² from convexity; Green’s function decays exponentially on horizontal sector.
- **What would be needed:** Establish the HS identity for the non-Euclidean compact-group configuration manifold with gauge constraints; show uniform ellipticity and a spectral gap for the Witten Laplacian on 1-forms; justify reduction to scalar massive Laplacian on horizontals (kernel of d₀* etc.) with controlled constants.
- **Status:** **FRONTIER** (powerful but requires heavy geometric analysis).

### [27.3]
- **Claim being assumed:** Uniform LSI ⇒ tightness in H^{-s} via Sobolev embedding.
- **What would be needed:** Identify the field space and topology; show Lipschitz observables control the relevant Sobolev norms; verify uniform integrability and that the embedding constants behave correctly as a→0 and volume→∞.
- **Status:** **FRONTIER** (standard in SPDE contexts but not automatic for YM).

### [29.1–29.4]
- **Claim being assumed:** “One-step gap bridge” comparing transfer matrix dissipation to Dirichlet form; and that strong-coupling transfer matrix gap is a “mass gap witness” compatible with the diffusion gap.
- **What would be needed:** A precise inequality relating the two operators (transfer matrix vs Langevin generator) or at least relating their gaps; show the strong-coupling expansion bounds persist under the limits needed; and connect to isotropic continuum scaling (β→∞).
- **Status:** **MISSING/FRONTIER** (strong coupling gap is known; the bridge to the curvature method is not proved).

### [30.3]
- **Claim being assumed:** Existence of tubular neighborhood of flat stratum in orbit space with uniform-in-a geometry bounds.
- **What would be needed:** Uniform control of injectivity radius, second fundamental form, and O’Neill tensors for the quotient \(C_a/G_a\) as the lattice refines; handle emergence of near-reducibles and shrinking directions; prove constants do not deteriorate with number of edges/vertices.
- **Status:** **OPEN** (this is essentially the “uniform geometry as a→0” problem).

### [37.2–37.4]
- **Claim being assumed:** Horizontal BE curvature bound implies Poincaré/LSI and spectral gap “restricted to gauge invariants” with constant ρ_BE = ρ₀+ρ\*.
- **What would be needed:** A rigorous “horizontal Γ₂ calculus” on the quotient/stratified space; show the generator restricted to gauge-invariant functions is symmetric and satisfies BE; verify domain issues and that horizontality is preserved under the semigroup.
- **Status:** **FRONTIER**.

### [38.4–38.6]
- **Claim being assumed:** Vertical bracket scales like g and curvature like g²; bounded near flat stratum.
- **What would be needed:** A rigorous identification of the horizontal distribution and its dependence on A; bounds on \(DP_V(A)\) in operator norm uniformly in lattice refinement; and a proof that near vacuum these bounds are uniform in a.
- **Status:** **FRONTIER/OPEN** (ties directly to the continuum uniformity problem).

### [40.3–40.4]
- **Claim being assumed:** Under heat-kernel convolution coarse-graining, “Weyl factor is frozen” and yields a block-diagonal curvature floor N/4 that is scale-independent and relevant to the full theory.
- **What would be needed:** Specify the RG map (convolution on links? plaquettes?); prove the induced measure factorization and that the Weyl Jacobian appears additively in the effective action at each scale; show it contributes to the **horizontal** Hessian in the interacting measure, not just in eigenangle coordinates for a single group element.
- **Status:** **OPEN** (key conceptual leap; not established).

---

## 2. Dependency chain (who depends on what; where it breaks)

I’ll write “A → B” meaning B uses A.

### Polarity branch
- **[2.2,2.3] Gaussian polarity theorems**  
  → **[4.2,14.3] infinite codimension ⇒ polar Σ_ξ**  
  → **[4.3] countable union ⇒ polar Σ**  
  → **[9.2] stratified max principle**  
  → **[11.2] PDE-to-ODE comparison for λ_min**  
  → supports **[5.1] “ignore Σ”** and later curvature propagation arguments.

**Breaks:**
- At **[4.3]** (countable dense ξ_j does not cover reducibles).  
- At **[3.2]** if you need polarity under YM measure rather than OU.  
- At **[9.2]** (stratified max principle not proved in this setting).

### Curvature/source → LSI → spectral gap branch
- **[10.1] horizontal gradient lemma**  
  → **[10.3] local horizontal CD(ρ_loc)**  
  → **[22.3] local-to-global via Lyapunov drift**  
  → **[37.4] Poincaré/LSI ⇒ spectral gap λ₁ ≥ ρ**  
  → **[27] tightness** and **[17] uniform gap dichotomy**.

**Breaks:**
- At **[10.3]** (uniform, volume-independent local CD not established).  
- At **[22.3]** (Lyapunov drift is explicitly frontier).  
- At **[37]** (horizontal Γ₂ calculus on quotient/stratified space).

### Riccati forcing/source term branch
- **[11.1] λ_min PDE inequality with σ\_***  
  + **[11.3] ODE fixed point**  
  → **[15.3] persistence under PBH flow**  
  → **[17.3] uniform spectral gap**.

**Breaks:**
- At **[11.1]** (derivation of λ inequality).  
- At identification/positivity/uniformity of **σ\_***:
  - Haar mass dies as a→0 (**acknowledged**).
  - Entropic spark is conjectural (**[7],[32],[41] OPEN**).
  - Weyl σ_geom=N/4: inequality proven, but embedding into YM effective action as a uniform forcing is **[40] OPEN**.
  - β-function forcing: **[16.2] OPEN**.

### Lattice → continuum branch
- **[37] uniform lattice CD/LSI**  
  → **[20] Mosco convergence**  
  → **continuum CD/LSI**  
  → **[23] OS reconstruction mass gap**.

**Breaks:**
- At **uniformity in a** (core unsolved).  
- At **[20.3]** (stability of Γ₂ under Mosco is not automatic).  
- At **[23.3]** (diffusion gap to Hamiltonian gap bridge is not proved).

---

## 3. Focused gap notes (requested emphasis)

### A) Lattice → continuum steps
1. **[20.3] Mosco + Trotter–Kato ⇒ curvature transfers.**  
   - **Gap:** semigroup convergence does not by itself preserve Γ₂ inequalities; need a dedicated stability theorem with strong hypotheses (convergence of carré du champ, uniform integrability, etc.).  
   - **Status:** **OPEN**.

2. **[27.3] Uniform LSI ⇒ tightness in H^{-s}.**  
   - **Gap:** must control how Lipschitz constants and Sobolev embeddings scale with lattice refinement; also identify the correct continuum field topology.  
   - **Status:** **FRONTIER**.

3. **[30.3] Uniform tubular neighborhood geometry as a→0.**  
   - **Gap:** uniform injectivity radius/curvature bounds on orbit space as dimension explodes; near-reducibles proliferate.  
   - **Status:** **OPEN**.

### B) Spectral gap → mass gap steps
1. **[23.3] Langevin spectral gap ⇒ Hamiltonian mass gap.**  
   - **Gap:** OS reconstruction uses Euclidean time correlations; Langevin time is auxiliary. Need a theorem connecting relaxation in stochastic quantization to exponential decay of Schwinger functions in Euclidean time, uniformly in a, and then to transfer matrix spectrum.  
   - **Status:** **OPEN**.

2. **[17.3] “Uniform spectral gap for generators → transfer matrix gap”.**  
   - **Gap:** these are different operators; equivalence is not established. At best, both imply clustering but with different notions of time.  
   - **Status:** **MISSING/OPEN**.

### C) Uniform bound claims
1. **[10.3] volume-independent ρ_loc.**  
   - **Gap:** must bound geometric terms (Ricci, O’Neill tensors, perturbations) uniformly in number of lattice sites/links; nontrivial.  
   - **Status:** **FRONTIER**.

2. **[6.4]/[24.3] uniform separation from Gribov horizon via ρ\*(a,g)>0.**  
   - **Gap:** ρ\* depends on a²g² and vanishes in AF regime; so cannot be uniform unless replaced by a different source (Weyl/entropic).  
   - **Status:** **MISSING** as a continuum-uniform statement.

3. **[13→40] Weyl σ_geom=N/4 gives a-independent curvature floor for the *full* theory.**  
   - **Gap:** showing this term persists under RG/coarse-graining and contributes to the relevant Hessian/Γ₂ for gauge-invariant observables is not proved.  
   - **Status:** **OPEN**.

4. **[3.2] bounded density perturbation for YM measure.**  
   - **Gap:** essentially false/unknown in 4D continuum; even lattice bounds won’t be uniform in volume/β.  
   - **Status:** **OPEN**.

---

## 4. Highest-impact chain breaks (summary)

1. **Countable union step for reducibles** fails as stated:  
   - **Location:** [4.3]  
   - **Issue:** density of {ξ_j} does not imply Σ ⊂ ⋃ Σ_{ξ_j}.  
   - **Fix needed:** replace with a *countable family of conditions* that exactly characterize reducibility (e.g., vanishing of lowest FP eigenvalue) and show each condition defines a polar set, or use analytic set/capacity arguments (Choquet capacitability) to handle uncountable unions.

2. **Transfer of polarity to YM measure** is not justified:  
   - **Location:** [3.2]  
   - **Issue:** bounded density perturbation is not available.  
   - **Fix needed:** either (i) prove polarity directly for the interacting Dirichlet form, or (ii) use local absolute continuity with quantitative capacity comparison, or (iii) work with reference Gaussian only for the diffusion actually used.

3. **Stratified maximum principle and λ_min PDE inequality** are major analytic gaps:  
   - **Locations:** [9.2], [11.1]  
   - **Fix needed:** full Dirichlet-form/quasi-regular framework on stratified orbit space; tensor maximum principle for Hessian flow.

4. **Uniform global LSI via Lyapunov drift** is explicitly missing and is essential for thermodynamic/continuum limits:  
   - **Location:** [22.3]  
   - **Fix needed:** construct gauge-invariant Lyapunov function with uniform drift constants.

5. **Spectral gap (Langevin) → physical mass gap** bridge is not proved:  
   - **Location:** [23.3]  
   - **Fix needed:** a rigorous theorem connecting stochastic quantization gap to Euclidean-time clustering/transfer matrix spectrum, or bypass Langevin and prove transfer matrix gap uniformly.

---

If you want, I can reorganize the gap list into a minimal “critical path” (smallest set of missing lemmas whose proof would make the main theorem go through) versus “supporting gaps” that improve robustness but aren’t strictly necessary.

---

*Report generated by GPT-5.2 Physics RAG Analyzer*
