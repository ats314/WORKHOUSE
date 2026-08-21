# GPT-5.2 Physics Document Analysis Report

**Analysis Type:** REDUNDANCY
**Generated:** 2026-01-18T12:07:57.733255
**Model:** gpt-5.2

---

## Analysis Results

# Redundancy & Consolidation Report — *Synthesis 15: Polarity and Gribov Horizon Mechanisms*

This report flags repeated mathematical content (same lemmas/equations/derivations) and recommends concrete consolidations. I organize it as:

1) **Per-chapter key mathematical concepts** (what each chapter *mathematically* contributes)  
2) **Major overlap clusters** (where the same theorem/equation/explanation reappears)  
3) **Specific consolidation edits** (what to merge, what to keep once, where to cross-reference)  
4) **Special checks**: repeated theorem statements, repeated derivations, Schur complement / Riccati repetition

---

## 1) Key mathematical concepts by chapter (math-only extraction)

### Ch.1 — Singular strata problem statement
- Stratified configuration/orbit space; reducibles vs irreducibles; Gribov copies.
- Motivation for ignoring singular sets in PDE/functional inequality arguments.

### Ch.2 — Gaussian polarity threshold (OU capacity)
- OU Dirichlet form: \(\mathcal E_0(f,f)=\int\|\nabla f\|^2\,d\mu_0\).
- Polarity definition via hitting probability / capacity zero.
- Threshold: finite codim \(m\): polar iff \(m\ge 3\); infinite codim ⇒ polar.
- Closure under affine translate + countable unions.

### Ch.3 — Capacity transfer under bounded density change
- Measure change \(d\mu=\rho\,d\mu_0\), \(c_1\le\rho\le c_2\).
- Capacity comparison: \(c_1\mathrm{Cap}_{\mu_0}(E)\le \mathrm{Cap}_\mu(E)\le c_2\mathrm{Cap}_{\mu_0}(E)\).
- Equivalence of capacity-zero sets under bounded perturbations.

### Ch.4 — Reducibles are polar (Sobolev setting)
- Reducible condition \(D_A\xi=0\).
- Linear constraint \(T_\xi(a)=[a,\xi]=b_\xi\).
- Infinite rank lemma for \(T_\xi\) ⇒ solution set is affine infinite-codim ⇒ polar.
- Countable union argument via dense \(\{\xi_j\}\).

### Ch.5 — Consequences for mass gap pipeline
- “Polarity buys”: no boundary terms, max principle, spectral analysis, clean Dirichlet form domain.
- Pipeline: curvature → LSI → spectral gap → mass gap.

### Ch.6 — Haar Jacobian “geometric mass” at finite cutoff
- Haar Jacobian determinant formula in exponential coordinates.
- Small-field expansion: \(S_{\rm Haar}(A)=\frac{c_0}{2}a^2g^2\|A\|^2+O(a^4g^4\|A\|^4)\).
- Hessian at 0: \(\mathrm{Hess}\,S_{\rm Haar}(0)=c_0a^2g^2 I\).
- Gribov region/horizon via \(\lambda_{\min}\) of horizontal Hessian; \(\rho_*(a,g,\beta)\).
- Continuum issue: \(c_0a^2g_0^2(a)\to 0\).

### Ch.7 — Entropic Spark conjecture (Prékopa–Leindler route)
- Fiber volume \(\mathrm{Vol}(Y)\) and \(V_{\rm eff}(Y)=E(Y)-\log\mathrm{Vol}(Y)\).
- Spark target: \(\nabla^2 V_{\rm eff}(0)\succeq c\gamma^2 I\).
- Prékopa–Leindler: convex \(\Lambda\) + linear projection ⇒ slice volume log-concave ⇒ \(-\log\mathrm{Vol}\) convex.

### Ch.8 — Two routes to continuum mass gap
- Comparison table: Haar mass fails in continuum; entropic \(\gamma^2\) conjectured.
- Additive decomposition of curvature source: \(\sigma=\sigma_{\rm Haar}(a)+\sigma_{\rm entropic}\).

### Ch.9 — Stratified parabolic maximum principle
- Parabolic comparison theorem on \(M_{\rm reg}\) with polar singular set \(\Sigma\).
- Feynman–Kac + avoidance of \(\Sigma\) ⇒ positivity propagation.

### Ch.10 — Horizontal Bakry–Émery curvature
- Lemma: gauge-invariant \(f\) has \(\nabla f\in H_U\).
- \(\Gamma_2\) identity; \(\mathrm{Ric}_{\mu}=\mathrm{Ric}_g+\nabla^2 S\).
- Local horizontal CD theorem: \(\mathrm{Ric}_{\mu_\Lambda}(v,v)\ge \rho_{\rm loc}|v|^2\) for \(v\in H_U\).
- Volume-independent constants.

### Ch.11 — PDE-to-ODE reduction; Riccati barrier
- Riccati-type inequality for smallest eigenvalue \(\lambda\):
  \(\partial_t\lambda\ge L\lambda-2\lambda^2+\sigma_*\).
- ODE comparison: \(\dot{\underline\lambda}=-2\underline\lambda^2+\sigma_*\).
- Fixed point \(\sqrt{\sigma_*/2}\).

### Ch.12 — FP determinant as orbit-volume Jacobian
- \(M_U=D_U^*D_U\), \(\Delta_{\rm FP}=\det M_U\).
- Reducibles ↔ \(\ker D_U\neq 0\) ↔ \(\Delta_{\rm FP}\to 0\).
- \(S_{\rm FP}=-\frac12\log\Delta_{\rm FP}\to+\infty\).
- Hessian formula with nonnegative “trace of square” term.

### Ch.13 — Weyl denominator curvature floor \(\sigma_{\rm geom}=N/4\)
- Weyl denominator \(|\Delta|^2=\prod_{i<j}4\sin^2((\theta_i-\theta_j)/2)\).
- \(S_{\rm Weyl}=-\log|\Delta|^2\).
- Hessian is weighted complete-graph Laplacian; lower bound on \(\sum x_i=0\):
  \(\nabla^2 S_{\rm Weyl}\ge \frac{N}{4}I\).
- Scale independence vs Haar.

### Ch.14 — Infinite codimension proof (point evaluation trick)
- Re-derives \(\Sigma_\xi=\{A:[a,\xi]=\cdots\}\).
- Constructs countably many point-evaluation constraints \(T_n(a)=[a(x_n),\xi(x_n)]\).
- Shows infinite rank ⇒ infinite codim ⇒ polar; countable union.

### Ch.15 — PBH flow and persistence theorem
- Hessian flow PDE: \(\partial_t h_t=\Delta_H h_t-2\nabla_{V_t}h_t-2h_t^2+S_{\rm anom}+\mathfrak G\).
- Scalar inequality for \(\lambda_{\min}\):
  \(\partial_t\lambda_{\min}\ge -2\lambda_{\min}^2+\sigma_A-C_1 g(t)^2H_{\rm Tr}\).
- Asymptotic freedom makes error vanish; persistence to positive equilibrium.

### Ch.16 — Anomaly source positivity (three prongs)
- Prong A: gauge-fixing/FP gives small-field quadratic term \(c_{\rm FP}\|A\|^2\) (with \(c_{\rm FP}\sim Ng_0^2a^2/12\)).
- Prong B: perturbative UV: \(\sigma_A(k)=2\beta_0 g(k)^2 k^2\).
- Prong C: BE curvature: \(\mathrm{Hess}(V)\ge \rho I\Rightarrow CD(\rho,\infty)\Rightarrow\) Poincaré gap.

### Ch.17 — Uniform spectral gap dichotomy
- “Uniform lattice gap as \(a\to 0\)” dichotomy.
- Pipeline summary referencing Ch.6–7,10–11,13,15–16.

### Ch.18 — Curvature-RG budget (Schur complement + discrete Riccati)
- Block Hessian bound: \(A,B,C\) ⇒ coarse Hessian \(\succeq (\alpha-M^2/\gamma)I\).
- Discrete recursion: \(\rho_{k+1}\ge \rho_k-\frac{M_k^2}{\rho_k}\).
- Squared budget: \(\rho_k^2\ge \rho_0^2-2\sum M_j^2\).
- Strong-coupling convexity window via \(\rho_*(a,g)\).

### Ch.19 — Engineering checklist (status)
- Repeats key inequalities: Haar Hessian, Wilson increment, polarity status, Lyapunov drift.
- Project management framing, not new math.

### Ch.20 — Mosco convergence and curvature lifting
- Mosco convergence definition (liminf + recovery).
- Uniform lattice CD bound transfers to continuum via Trotter–Kato.
- Equivalent gradient contraction inequality.

### Ch.21 — 3D compact QED sanity anchor
- Sine-Gordon dual action; cosine expansion gives spark curvature \(\zeta\).
- Mass scale \(m^2\sim \zeta e^2\).

### Ch.22 — Lyapunov drift local-to-global upgrade
- Drift condition \(LW\le -\alpha W+b1_K\).
- Local LSI + Lyapunov ⇒ global LSI with \(\rho\gtrsim \min(\rho_K,\alpha/b)\).

### Ch.23 — OS reconstruction bridge
- OS positivity + tightness + reconstruction yields Hamiltonian and mass gap.
- Relates diffusion spectral gap to physical gap.

### Ch.24 — Gribov region vs horizon; polarity comparison
- Defines \(\Omega\) via positive horizontal Hessian; horizon \(\partial\Omega\) via \(\lambda_{\min}=0\).
- Table: reducibles polar (codim ∞) vs horizon not polar (codim 1).
- Repeats horizontal gradient lemma.

### Ch.25 — Schur complement and RG convexity stability (again)
- Repeats block Hessian, Schur complement, convexity loss \(M^2/\gamma\).
- Repeats discrete Riccati recursion and squared budget.
- Adds interpretation and “why this matters for polarity” (but math is Ch.18).

### Ch.26 — Helffer–Sjöstrand and Green’s function decay
- HS covariance identity with \(M^{-1}\).
- Witten Laplacian on 1-forms: \(\mathcal L^{(1)}=(-L)+\nabla^2S+\mathrm{Ric}\).
- Bochner identity \(\nabla(-Lf)=\mathcal L^{(1)}(\nabla f)\).
- Exponential decay of Green’s function for massive operator; horizontal reduction.

### Ch.27 — Tightness and compactness lever
- Repeats CD→LSI→concentration→moments→tightness pipeline.
- Prokhorov theorem; tightness in \(H^{-s}\) via Sobolev embedding.
- Overlaps with Ch.20 and Ch.23.

### Ch.28 — Reflection positivity permanence and RG no-go
- Reflection positivity definition and permanence under equivariant pushforwards/projective limits.
- No-go theorem for exact reflection-equivariant Markov RG in nonabelian case.

### Ch.29 — One-step gap bridge and transfer matrix
- Strong-coupling transfer matrix gap estimate; Hamiltonian gap lower bound.
- “Two gap witnesses” framing.

### Ch.30 — Tubular neighborhood reduction
- Program: uniform tubular neighborhood of flat stratum in orbit space.
- Riemannian submersion geometry; uniform Jacobian/curvature bounds.

### Ch.31 — Simulation targets
- Numerical diagnostics; not mathematical derivations.

### Ch.32 — Entropic Spark conjecture (again)
- Restates spark mechanism and Riccati fixed point \(\dot\lambda=-2\lambda^2+\sigma\).
- Frames as “soul of mass gap”; overlaps with Ch.7–8 and Ch.11.

### Ch.33 — PBH flow as viscous HJ (again)
- vHJ equation \(\partial_t S_t=\Delta_H S_t-|\nabla_H S_t|^2+J_t\).
- Defines anomaly tensor \(S_{\rm anom}=\nabla_H^2J_t\) and uniform positivity.
- Differentiation gives Hessian evolution with \(-2H_t^2\).
- Overlaps heavily with Ch.15–16.

### Ch.34 — Hessian spectrum and curvature propagation
- Empirical/diagnostic: Wilson Hessian spectrum at identity; coarse-graining.
- Riccati-type decay estimate \(m_\ell \gtrsim \frac{m_0}{1+cm_0\ell}\).
- Repeats “source term ⇒ fixed point” narrative.

### Ch.35 — Multiscale recursion blueprint (again)
- Generic recursion \(\rho_{j+1}\ge K\rho_j-\varepsilon_j+\sigma_*\).
- Repeats PDE Riccati inequality and fixed point \(\sqrt{\sigma_*/2}\).
- Decomposes tasks: prove \(\sigma_*>0\), control \(\sum\varepsilon_j\).

### Ch.36 — Correlation decay and confinement physics
- Convexity floor ⇒ Poincaré/LSI ⇒ spectral gap ⇒ correlation decay rate \(\sim \sqrt{\kappa_*}\).
- Repeats QED3 spark and general pipeline.

### Ch.37 — Bochner identity and spectral gap theorem (again)
- Bochner–Weitzenböck identity for \(\Gamma_2\).
- Horizontal specialization; \(\Gamma_2\ge \rho\Gamma\).
- Poincaré/spectral gap theorem; overlaps with Ch.10 and Ch.26.

### Ch.38 — O’Neill formula and submersion geometry
- Riemannian submersion \(\pi:C_a\to M_a\).
- O’Neill formula: \(K_B=K_E+\frac34\|[X,Y]_V\|^2\); with \(K_E=0\).
- Curvature scaling \(\sim g^2\); near-flat stratum boundedness.

### Ch.39 — Strong–weak coupling crossover
- Repeats strong coupling gap; uniformity obstruction as \(g(a)\to 0\).
- Strategy list; overlaps with Ch.17, Ch.29.

### Ch.40 — Heat kernel semigroup and Weyl freezing
- Heat kernel semigroup on compact group; convolution smoothing.
- “Weyl factor frozen” under convolution; scale-independent geometric source.
- Repeats \(\sigma_{\rm geom}=N/4\) motivation.

### Ch.41 — Monopole spark and IR effective potential (again)
- Repeats QED3 dual action and spark curvature.
- Restates entropic Gribov spark conjecture; locality argument.

---

## 2) Chapters with significant overlap (concept clusters)

### Cluster A — **Polarity of reducibles via infinite codimension**
- **Ch.2** (general OU polarity threshold)
- **Ch.4** (reducibles polar via infinite rank)
- **Ch.14** (point-evaluation infinite codimension proof; repeats Ch.4 + Ch.2)
- **Ch.24** (table: reducibles polar; horizon not polar; repeats polarity facts)

**Redundancy type:** same proposition (“codim ∞ ⇒ polar”), same reducible constraint equation \(D_A\xi=0\) → \([a,\xi]=b\), same countable union argument.

### Cluster B — **Capacity transfer / “ignore Cap=0 sets” enabling PDE**
- **Ch.3** (capacity transfer lemma)
- **Ch.5** (consequences: ignore Σ)
- **Ch.9** (stratified parabolic max principle using polarity)
- **Ch.11** (PDE-to-ODE comparison explicitly assumes Σ polar)
- **Ch.24** (repeats “polarity makes Σ invisible”)

**Redundancy type:** repeated explanation that polarity removes boundary terms / allows max principle / diffusion avoids Σ.

### Cluster C — **Horizontal gradient lemma + horizontal-only BE curvature**
- **Ch.10** (lemma: gauge-invariant ⇒ horizontal gradient; local horizontal CD)
- **Ch.24** (re-states the same lemma verbatim as Prop 2.1)
- **Ch.37** (repeats horizontal specialization of Bochner/BE to get Poincaré gap)
- **Ch.26** (Witten Laplacian/Bochner identity overlaps conceptually with Ch.37)

**Redundancy type:** same lemma statement and proof sketch appears at least twice; BE→Poincaré/spectral gap appears multiple times.

### Cluster D — **Riccati mechanism (continuous) and “fixed point = √(σ/2)”**
- **Ch.11** (core Riccati PDE→ODE and fixed point)
- **Ch.15** (scalar inequality with \(-2\lambda^2+\sigma_A-\text{error}\))
- **Ch.32** (restates Riccati and fixed point as central)
- **Ch.33** (derives Hessian evolution with \(-2H^2\))
- **Ch.34** (Riccati propagation narrative)
- **Ch.35** (repeats PDE inequality and fixed point)
- **Summary blocks** also repeat \(\lambda_*=\sqrt{\sigma/2}\).

**Redundancy type:** same equation \(\dot\lambda=-2\lambda^2+\sigma\) and same attractor value repeated many times.

### Cluster E — **Schur complement / RG convexity budget (discrete Riccati)**
- **Ch.18** (block marginalization lemma + recursion + squared budget)
- **Ch.25** (repeats essentially all of Ch.18 with slightly different framing)

**Redundancy type:** near-duplicate lemma and recursion; this is the clearest “merge these” case.

### Cluster F — **Haar mass vs continuum failure; Gribov region/horizon**
- **Ch.6** (Haar Jacobian expansion; \(\rho_*\); Gribov region/horizon; Haar mass vanishes)
- **Ch.8** (table repeating Haar fails / entropic spark)
- **Ch.24** (Gribov region vs horizon definitions; separation condition \(\rho_*>0\))
- **Ch.39** (repeats “asymptotic freedom kills \(a^2g^2\)” obstruction)

**Redundancy type:** same narrative and same inequality \(\mathrm{Hess}\,S_{\rm eff}\succeq \rho_* I\) and “\(a^2g^2\to 0\)” repeated.

### Cluster G — **Weyl denominator curvature floor \(N/4\)**
- **Ch.13** (full derivation and bound)
- **Ch.40** (re-motivates and reasserts “Weyl factor frozen” and “source \(N/4\)”)
- **Global summaries** repeat \(\sigma_{\rm geom}=N/4\).

**Redundancy type:** repeated statement of the same key bound; Ch.40 adds a *new* angle (heat kernel convolution) but repeats the conclusion.

### Cluster H — **Tightness / Mosco / OS reconstruction pipeline**
- **Ch.20** (Mosco + curvature lifting)
- **Ch.23** (OS reconstruction checklist; gap bridge)
- **Ch.27** (tightness pipeline CD→LSI→tightness; overlaps with Ch.20 and Ch.23)

**Redundancy type:** repeated pipeline narrative; Ch.27 largely re-summarizes.

### Cluster I — **QED3 “spark” worked example**
- **Ch.21** (worked example)
- **Ch.41** (repeats same equations and spark expansion)
- **Ch.36** (repeats again at narrative level)

**Redundancy type:** same sine-Gordon action and cosine expansion repeated.

---

## 3) Specific consolidation recommendations (actionable edits)

### 3.1 Merge Ch.18 and Ch.25 (Schur complement / discrete Riccati)
**Recommendation:** Keep **one** chapter as the canonical “RG convexity stability via Schur complement” chapter.

- **Keep:** Ch.18 as the main technical statement (it already has lemma + recursion + squared budget + window).
- **Fold Ch.25 into Ch.18** as:
  - a short “Interpretation” subsection (convexity loss per step \(M^2/\gamma\)),
  - and a short “Connection to polarity” remark (if truly needed).
- **Replace Ch.25** with a 1–2 paragraph cross-reference: “See Ch.18 for Schur complement and discrete Riccati budget.”

This removes a near-duplicate derivation and satisfies your “Schur complement appearing repeatedly” check.

---

### 3.2 Consolidate polarity proofs: Ch.4 + Ch.14 (+ parts of Ch.2)
**Recommendation:** Make **one** place where the reducible set polarity proof lives, and one place where the general OU polarity theorem lives.

- **Keep Ch.2** as the general OU polarity/capacity theorem (codim threshold, affine/union closure).
- **Make Ch.4** the *application* to reducibles, but **move the point-evaluation infinite rank proof from Ch.14 into Ch.4** as the proof of the “Infinite Rank” lemma.
- **Convert Ch.14** into either:
  - an appendix (“Technical proof: point-evaluation infinite rank”), or
  - a short “Proof details” subsection inside Ch.4.

Right now Ch.14 re-derives the same constraint structure and repeats the codimension→polarity logic already in Ch.2/Ch.4.

---

### 3.3 Unify “polarity enables max principle / PDE arguments” (Ch.5 + Ch.9 + Ch.11)
**Recommendation:** Create a single “Polarity as analytic enabler” chapter/section.

- **Keep Ch.9** as the canonical theorem statement (stratified parabolic comparison).
- **Move Ch.5.1** (“What polarity buys”) into the introduction of Ch.9 (or immediately after the theorem as “Corollaries/Consequences”).
- **In Ch.11**, avoid re-explaining polarity; just state: “Assume Σ polar (Ch.9), then PDE-to-ODE comparison applies.”

This reduces repeated prose about “diffusion never hits Σ” and “no boundary terms”.

---

### 3.4 Deduplicate the horizontal gradient lemma (Ch.10 vs Ch.24)
**Recommendation:** State and prove the lemma **once**.

- **Keep the lemma + proof in Ch.10** (it’s foundational for horizontal BE).
- **In Ch.24**, replace the repeated proof with: “By Ch.10.1, gauge-invariant gradients are horizontal.”

Ch.24 can keep the *new* content: “horizon not polar (codim 1)” and “separation from horizon via \(\rho_*>0\)”.

---

### 3.5 Consolidate Bakry–Émery → Poincaré/spectral gap (Ch.10 vs Ch.37)
**Recommendation:** Avoid re-proving the BE engine twice.

- **Option A (preferred):** Keep Ch.10 as the BE curvature chapter, and make Ch.37 a short “Theorem (Spectral gap from CD)” with a reference to standard BE theory + a pointer back to Ch.10 for hypotheses.
- **Option B:** Merge Ch.37 into Ch.10 as a final subsection “From CD to Poincaré/LSI and spectral gap”.

Ch.37 currently repeats the Bochner identity and the CD→gap pipeline already implicit in Ch.10 and also overlaps with Ch.26’s Bochner/Witten Laplacian discussion.

---

### 3.6 Centralize the Riccati story (Ch.11, Ch.15, Ch.32, Ch.33, Ch.35, Ch.34)
**Recommendation:** Choose **one** canonical Riccati section and treat the rest as applications.

- **Keep Ch.11** as the canonical “Riccati barrier: PDE→ODE→fixed point” chapter.
- **Keep Ch.15** as the PBH-flow-specific inequality (it’s a distinct model equation with error term).
- **Merge Ch.33 into Ch.15** (since Ch.33 is essentially the derivation/context for PBH/vHJ and anomaly tensor).
- **Convert Ch.32 and Ch.35** into short “Program summaries” that *reference* Ch.11/Ch.15 rather than restating \(\dot\lambda=-2\lambda^2+\sigma\) and \(\lambda_*=\sqrt{\sigma/2}\).
- **Ch.34** should either:
  - focus purely on the empirical/spectral diagnostics (SU(2) Hessian spectrum, Lanczos), or
  - be folded into an “Experiments/Diagnostics” appendix; remove repeated Riccati narrative.

This addresses your “Riccati appearing repeatedly” check: it appears in at least 5 chapters plus summaries.

---

### 3.7 Reduce repetition around Haar mass failure / two routes (Ch.6, Ch.8, Ch.39)
**Recommendation:** Keep the technical derivation once, summarize elsewhere.

- **Keep Ch.6** as the technical Haar Jacobian expansion + \(\rho_*\) + horizon definitions.
- **Fold Ch.8** into the end of Ch.6 as a short “Continuum implication: Haar mass vanishes; need replacement source”.
- **In Ch.39**, avoid re-stating the same “\(a^2g^2\to 0\)” argument; just cite Ch.6 and focus Ch.39 on the *crossover framing* and strategy list.

---

### 3.8 Weyl \(N/4\) bound: keep derivation once (Ch.13) and reference elsewhere (Ch.40)
**Recommendation:** Ch.40 should not restate the bound; it should only add the “heat kernel convolution freezes Weyl factor” insight.

- **Keep Ch.13** as the sole derivation/proof of \(\nabla^2 S_{\rm Weyl}\ge N/4\).
- **In Ch.40**, replace repeated “therefore \(N/4\)” statements with a pointer: “Thus the geometric source from Ch.13 persists under heat-kernel smoothing.”

---

### 3.9 Tightness / Mosco / OS: merge Ch.27 into Ch.20+Ch.23
**Recommendation:** Ch.27 is mostly a re-summary of standard implications.

- **Keep Ch.20** for Mosco + curvature lifting (technical).
- **Keep Ch.23** for OS reconstruction checklist (physical bridge).
- **Replace Ch.27** with a short “Consequences” subsection split across:
  - end of Ch.20: “Uniform CD ⇒ uniform LSI ⇒ tightness”
  - end of Ch.23: “tightness is the compactness lever needed for OS limits”

---

### 3.10 QED3 spark repetition (Ch.21, Ch.41, Ch.36)
**Recommendation:** Keep one worked example.

- **Keep Ch.21** as the canonical worked example.
- **In Ch.41**, keep only what is *new* (e.g., locality/topology discussion) and replace the sine-Gordon equations with a reference to Ch.21.
- **In Ch.36**, remove the explicit QED3 equations entirely; just cite Ch.21.

---

## 4) Explicit redundancy checks requested

### A) Same theorem stated multiple times
- **Horizontal gradient lemma**: Ch.10.1 and Ch.24.4 (nearly verbatim).
- **CD/Bochner → Poincaré/spectral gap**: Ch.10 (CD theorem), Ch.37 (Theorem 4.1), and parts of Ch.16.3 (Prong C) restate the same implication chain.
- **Riccati fixed point** \(\lambda_*=\sqrt{\sigma/2}\): Ch.11, Ch.32, Ch.35, plus summaries.

### B) Same equation derived in different chapters
- **Schur complement bound** and **discrete Riccati recursion**: Ch.18 and Ch.25 duplicate.
- **Riccati inequality** (continuous): Ch.11 and again in Ch.35; PBH variant in Ch.15 and again contextualized in Ch.33.
- **QED3 cosine expansion spark**: Ch.21 and Ch.41 duplicate.

### C) Overlapping explanations of the same concept
- “Polarity means diffusion never hits Σ, so ignore boundary terms”: Ch.5, Ch.9, Ch.11, Ch.24, Ch.40.
- “Haar mass vanishes as \(a\to 0\)”: Ch.6, Ch.8, Ch.39.
- “Two gap witnesses (Langevin vs transfer matrix)”: Ch.29 and echoed in Ch.39.

### D) Schur complement / Riccati appearing repeatedly
- **Schur complement**: Ch.18 and Ch.25 (clear duplication).
- **Riccati**: Ch.11, Ch.15, Ch.32, Ch.33, Ch.34, Ch.35 (plus summaries). This is the largest repeated mathematical motif.

---

## High-impact consolidation plan (minimal disruption)

If you want the biggest redundancy reduction with minimal restructuring:

1) **Delete/replace Ch.25** with “See Ch.18” (largest near-duplicate).  
2) **Move Ch.14 into Ch.4** (or make it an appendix) and keep Ch.2 as the only general polarity theorem.  
3) **Remove the repeated horizontal gradient lemma proof from Ch.24** (reference Ch.10).  
4) **Merge Ch.33 into Ch.15** and make Ch.32/Ch.35 purely referential summaries (stop restating Riccati).  
5) **Drop explicit QED3 equations from Ch.41 and Ch.36** (reference Ch.21).  
6) **Fold Ch.8 into Ch.6** and trim Ch.39 to avoid re-deriving the same continuum obstruction.

These edits would substantially reduce repeated theorems/equations while preserving the narrative arc.

---

*Report generated by GPT-5.2 Physics RAG Analyzer*
