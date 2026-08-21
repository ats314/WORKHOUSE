
## 0. Lattice Pillar Summary: Polarity, Haar Mass, and Hessian Gap

In the lattice module we now have three rigorous finite-cutoff pillars:

1. **Polarity of reducible configurations (finite-cutoff \(C_{\text{cutoff}}\)).**  
   On any finite lattice \(\Lambda\), the set of reducible configurations \(\Sigma_\Lambda\) is polar for both:
   - The Haar-OU Dirichlet form \((\mathcal{E}_0,\mu_H)\) associated with product Brownian motion on \(SU(N)^{\mathcal{B}}\), and
   - The lattice YM Dirichlet form \((\mathcal{E}_{\mathrm{YM}},\mu_{\Lambda,\mathrm{YM}})\) associated with the Wilson action.

   Thus, the corresponding diffusions almost surely never visit \(\Sigma_\Lambda\), and all spectral/functional-inequality arguments can be formulated on the irreducible sector without boundary conditions at \(\Sigma_\Lambda\). A detailed proof is given in
   `Rigorous Proof_ Polarity of Reducible Connections in Lattice Yang-Mills.md`.

2. **Mass from Haar measure with explicit coefficient.**  
   In exponential coordinates \(U_b = \exp(iagA_b)\), the Haar measure on each link yields a Jacobian
   \[
   J(A_b) = \det_{\mathfrak{g}}\Big(\frac{\sinh(\mathrm{ad}_{iagA_b}/2)}{\mathrm{ad}_{iagA_b}/2}\Big),
   \]
   and the measure action \(S_{\mathrm{Haar}}:=-\log J\) has expansion
   \[
   S_{\mathrm{Haar}}(A_b) = \frac{c_0}{2}\operatorname{Tr}(A_b^2) + O(a^4\|A_b\|^4),
   \quad c_0 = \frac{N^2-1}{2N},
   \]
   for \(SU(N)\). This supplies a strictly positive quadratic term in the effective action, a “mass from geometry” independent of the Wilson coupling. The derivation and representation-theoretic details are in
   `Package 2_ Lattice Foundation - Complete Summary.md`.

3. **Hessian structure and eigenvalue gap (Riccati prototype).**  
   Combining the Wilson action with the Haar-induced term, the effective lattice action \(S_{\mathrm{eff}}\) admits a Hessian decomposition of the form
   \[
   \mathrm{Hess}\,S_{\mathrm{eff}}(U)
   = \beta \Delta_{\text{lattice}} - \beta V(U) + c_0 I,
   \]
   where \(\Delta_{\text{lattice}}\) is a discrete Laplacian on link variables, \(V(U)\) is a bounded interaction operator, and \(c_0>0\) is as above. One obtains a uniform lower bound on the smallest horizontal eigenvalue
   \[
   \lambda_{\min}(U) \ge c_0
   \]
   across all configurations. Under suitable Langevin or RG evolution, these eigenvalues satisfy a Riccati-type inequality
   \[
   \frac{d\lambda}{dt} \gtrsim -\alpha \lambda^2 + c_0,
   \]
   providing a concrete finite-dimensional realization of the anomaly-supported curvature-flow mechanism invoked in the continuum MFIP. The detailed derivation is in
   `Rigorous Derivation_ Lattice Hessian Formula and Eigenvalue Analysis.md`.

Taken together, these results show that at finite lattice spacing:

- Reducible configurations are dynamically negligible (polar sets),
- The Haar measure supplies a strictly positive mass scale \(c_0\) in the Hessian,
- The Hessian flow obeys a Riccati-type inequality with a strictly positive source term, leading to sector-wise spectral gaps \(\Delta^\pm(a)\) bounded below by constants of order \(\sqrt{c_0}/a\).

This “Pillar L” is the lattice analogue of the continuum conjectures C (polarity) and B (anomaly-driven curvature source) and provides a concrete testbed for the MFIP ideas developed in the dynamic YM documents.

---

# Constructive Lattice Yang–Mills: Polarity Sectors and Mass from the Haar Measure

_Derived from the master white paper on Yang–Mills mass gap (v3.6)._  


## Context

## Executive Summary

This white paper lays out a **dynamic and constructive program** for the Yang–Mills Existence and Mass Gap problem, combining:

- A **convex scalar prototype** (lattice \(\phi^4_4\)) where the Bakry–\u00c9mery curvature condition yields a uniform log–Sobolev inequality and spectral gap, providing a fully rigorous test case for the dynamic route.
- A **stochastic/dynamic formulation** of Yang–Mills via Langevin (stochastic quantization), focusing on **spectral gaps of the generator** and their relation to the physical mass gap.
- A **UV “Log–Forest” hypothesis** for gradient norms of gauge-invariant observables (Wilson loops), ensuring that the Dirichlet form is not destroyed by uncontrolled UV roughness.
- A **toy RG–Hessian / curvature-flow picture**, where the trace anomaly acts as a positive curvature source in a viscous Hamilton–Jacobi flow for the effective action.
- A **stratified Sobolev framework** on the singular gauge quotient \(\mathcal{A}/\mathcal{G}\), including a rigorous definition of \(W^{1,2}(\mathcal{A}/\mathcal{G})\) and a Gaussian-reference polarity theorem (plus Conjecture C for the full YM measure) showing that reducible strata can be treated as capacity-zero.
- A **constructive lattice YM component** (in the spirit of Faria da Veiga & O’Carroll) where:
  - the Hilbert space is rigorously decomposed into **charge-conjugation (“polarity”) sectors** \(\mathcal{H} = \mathcal{H}^+ \oplus \mathcal{H}^-\) for \(SU(N>2)\),
  - the **Haar measure** is shown to generate an effective local mass term (“mass from geometry”),
  - and **two positive mass gaps** \(\Delta^\pm\) are established at finite lattice spacing.

The program does **not** claim a full Clay-level proof. Instead it:

1. Makes explicit which steps are **formal** and which are **conjectural**.  
2. Identifies a precise **local-sector spectral gap** that should correspond to the physical mass gap, separating it from ultra-slow topological modes.  
3. States a set of named conjectures (A, B, C, IR–1/2, D) whose resolution would turn this architecture into a rigorous solution.

---



# Part VI – Constructive Lattice Yang–Mills: Polarity and Mass from the Haar Measure

This part distills the constructive lattice YM perspective inspired by Faria da Veiga and O’Carroll (F&O), focusing on:

- OS-compatible lattice construction,
- Charge-conjugation “polarity” sectors,
- Haar-measure induced mass terms,
- Two-sector mass gaps at finite lattice spacing.

## 6.1. Lattice Formalism and Transfer Matrix

On a finite Euclidean lattice \(\Lambda\) with periodic boundary conditions:

- Variables: \(U_b\in SU(N)\) on bonds \(b\).
- Action: Wilson action
  \[
  S_W(U) = \frac{1}{g^2}\sum_{p\subset\Lambda}\mathrm{Re\,Tr}(I-U_p).
  \]
- Measure: product Haar measure
  \[
  Z_\Lambda = \int \prod_{b\in\Lambda} d\mu(U_b)\,e^{-S_W(U)}.
  \]

The transfer matrix \(T\) is defined by slicing the lattice in Euclidean time and integrating over one time step. Osterwalder–Schrader reconstruction yields:

- A Hilbert space \(\mathcal{H}\),
- A vacuum \(\Omega\) corresponding to the largest eigenvalue \(\lambda_{\max}\) of \(T\),
- A Hamiltonian \(H\) via \(T = e^{-aH}\).

The **mass gap** at finite lattice spacing is
\[
\Delta(a) = -\frac{1}{a} \log\left(\frac{\lambda_1}{\lambda_{\max}}\right),
\]
where \(\lambda_1\) is the next eigenvalue above \(\lambda_{\max}\).

## 6.2. Charge Conjugation and Polarity Sectors

Define charge conjugation \(\mathcal{C}\) on bond variables by complex conjugation:
\[
\mathcal{C}: U_b \mapsto U_b^*.
\]

For \(SU(N)\):

- The Wilson action is invariant under \(\mathcal{C}\).
- \(\mathcal{C}\) is an involution: \(\mathcal{C}^2 = I\).

The effect on the lattice Hilbert space depends on \(N\):

- **\(SU(2)\):** The fundamental representation is pseudo-real; characters are real-valued. Charge conjugation acts trivially on gauge-invariant observables (Wilson loops). The Hilbert space \(\mathcal{H}\) has a **single sector** under \(\mathcal{C}\).

- **\(SU(N>2)\):** The fundamental representation is complex; characters are generically complex. \(\mathcal{C}\) is a nontrivial involution with eigenvalues \(\pm 1\).

  Hence
  \[
  \mathcal{H} = \mathcal{H}^+ \oplus \mathcal{H}^-,
  \]
  where \(\mathcal{H}^\pm\) are the \(\pm 1\)-eigenspaces of \(\mathcal{C}\).

Because \(H\) commutes with \(\mathcal{C}\), it preserves these sectors. This yields a **polarity decomposition** of the spectrum:

- States in \(\mathcal{H}^+\): “even under \(\mathcal{C}\)” (positive polarity),
- States in \(\mathcal{H}^-\): “odd under \(\mathcal{C}\)” (negative polarity).

This is the rigorous content of the **Polarity Note** for constructive YM: for \(N>2\), the physical Hilbert space splits into two orthogonal charge-conjugation sectors.

## 6.3. Mass from the Haar Measure

In the classical continuum action, there is no local mass term. F&O highlight that the lattice path integral includes the Haar measure, which induces an **effective local mass** when expressed in Lie-algebra variables.

Parameterize
\[
U_b = e^{iagA_b}, \quad A_b \in \mathfrak{su}(N).
\]

The Haar measure induces a nontrivial Jacobian:
\[
  \int d\mu(U)\,f(U)
  = \int dA\,
ho(A)\,f(e^{iA}),
\]
where, in a neighbourhood of the identity, the density can be written in terms of the adjoint action as
\[
  
ho(A)
  = \det_{\mathrm{ad}}\Bigg(
      
rac{\sin(\mathrm{ad}_A/2)}{\mathrm{ad}_A/2}
    \Bigg),
\]
and
\[
  S_{\mathrm{measure}}(A)
  := -\log 
ho(A).
\]
Expanding near \(A=0\) using
\[
  
rac{\sin x/2}{x/2}
  = 1 - 
rac{x^2}{24} + O(x^4),
\]
one finds
\[
  S_{\mathrm{measure}}(A)
  = 
rac{1}{24}\,\mathrm{Tr}_{\mathrm{ad}}ig((\mathrm{ad}_A)^2ig)
    + O(\|A\|^4).
\]
Using the Killing form \(K(A,B) = -\mathrm{Tr}_{\mathrm{ad}}(\mathrm{ad}_A\mathrm{ad}_B)\), this can be rewritten as
\[
  S_{\mathrm{measure}}(A)
  = c_N\,K(A,A) + O(\|A\|^4),
\]
for some constant \(c_N>0\) depending only on \(N\). In the standard normalization \(K(A,A)=2N\,\mathrm{Tr}(A^2)\) for \(SU(N)\), this gives a **positive definite quadratic term**
\[
  S_{\mathrm{measure}}(A)
  pprox c'_N\,\mathrm{Tr}(A^2),
  \qquad c'_N>0,
\]
and therefore a strictly positive Hessian at the origin,
\[
  
abla^2 S_{\mathrm{measure}}(0) \;\ge\; c''_N\,I \;>\; 0.
\]
In other words, the Haar measure contributes a genuine Bakry–Émery curvature term at the lattice (UV) scale. In a combined action
\[
  S_{\mathrm{latt}}(A)
  = S_W(A) + S_{\mathrm{measure}}(A),
\]
where \(S_W(A)\) has kinetic and interaction terms but no local quadratic mass, the term \(S_{\mathrm{measure}}\) adds a gauge-invariant quadratic contribution and provides a geometric source of curvature.


This provides a **geometric origin** for a mass scale:

- The compactness and curvature of \(SU(N)\) are encoded in \(\rho(A)\).
- This yields a local “mass from geometry”
  \[
  m_{\text{measure}}^2 \sim g^2 C_2(N),
  \]
  which survives in the strong-coupling regime and contributes to the lattice mass gap.

Standard perturbative treatments often linearize the measure and drop \(S_{\mathrm{measure}}\), thereby **losing** this mechanism.

## 6.4. Two-Sector Mass Gaps and Correlation Functions

Define plaquette operators \(F_p(x)\) and their \(\mathcal{C}\)-even/odd parts:
\[
F_p^\pm(x) = F_p(x) \pm \mathcal{C}F_p(x).
\]

- \(F_p^+(x)\) creates states in \(\mathcal{H}^+\),
- \(F_p^-(x)\) in \(\mathcal{H}^-\).

One then shows (at finite lattice spacing \(a\)) that:

- The 2-point functions
  \[
  \langle F_p^\pm(x) F_p^\pm(y)\rangle
  \sim e^{-m^\pm |x-y|}
  \]
  define **two positive masses** \(m^\pm(a) > 0\), corresponding to the lowest excitations in each polarity sector.

In the strong-coupling regime, F&O obtain asymptotic formulas:
\[
m^\pm(\beta)
\approx \frac{-4\ln\beta}{a} + r^\pm(\beta),
\]
where \(\beta\sim 1/g^2\) and \(r^\pm(\beta)\) are analytic corrections. To leading order, \(m^+\approx m^-\), but higher orders split the two sectors.

This gives a **two-mass-gap structure** at finite lattice spacing for \(SU(N>2)\):

- The lightest glueball in \(\mathcal{H}^+\) (scalar-like \(0^{++}\) state),
- A heavier partner in \(\mathcal{H}^-\) (odd polarity).

## 6.5. Elitzur’s Theorem and Sector Decoupling

Elitzur’s Theorem states that a local gauge symmetry cannot be spontaneously broken: the expectation value of any gauge non-invariant local operator is zero.

F&O combine this with \(\mathcal{C}\)-invariance of the vacuum to show:

- Cross correlators between \(\mathcal{H}^+\) and \(\mathcal{H}^-\) vanish:
  \[
  \langle F_p^+(x) F_p^-(y) \rangle = 0.
  \]
- Hence the two sectors are **exactly decoupled** in the spectrum; there are no mixed-polarity glueballs.

This rigorous decoupling justifies treating the mass gap problem as a **two-channel spectral problem**, one per polarity sector.

## 6.6. Stability Bounds and Continuum Limit Status

F&O further establish:

- **Thermodynamic stability:** free energy density and correlation functions have well-defined infinite-volume limits (\(L\to\infty\)).
- **UV stability:** generating functionals remain bounded as \(a\to 0\) with appropriately scaled couplings, reflecting asymptotic freedom and the stabilizing role of the Haar measure.

However, the final Clay-level step remains open:

- For each fixed \(a>0\), there are positive mass gaps \(m^\pm(a)\).
- One must show that along an appropriate RG trajectory \(g(a)\), the continuum limit
  \[
  \lim_{a\to 0} m^\pm(a) = m^\pm_{\mathrm{phys}} > 0
  \]
  exists and yields a nonzero physical mass gap.

The constructive lattice program provides a **strong base**: it shows that YM with compact gauge group and Haar measure is a well-defined, massive theory at each finite \(a\), with rich polarity structure. Connecting this to a continuum, OS/Wightman-compatible mass gap is the remaining challenge.

---


## 6.7. Strong-Coupling Transfer Matrix Spectral Gap

In addition to the Haar-induced mass and Hessian gap, we have a direct transfer matrix spectral-gap result at finite cutoff, valid in the strong-coupling regime.

Consider an anisotropic lattice with spatial and temporal couplings \(\beta_s,\beta_t\) and time spacing \(a\). Let \(T\) be the Osterwalder–Schrader transfer matrix acting on the physical Hilbert space \(\mathcal{H}\), defined by slicing the Euclidean lattice in the time direction and integrating over temporal links. As recalled in §6.1, \(T\) is a positive self-adjoint operator with
\[
T = e^{-aH},\qquad H\ge 0,
\]
and the vacuum vector \(\Omega\) corresponds to the maximal eigenvalue \(\lambda_0>0\).

The strong-coupling analysis in `Rigorous Derivation_ Transfer Matrix Spectral Gap in Lattice Yang-Mills.md` shows that:

- There exists a critical temporal coupling \(\beta_c>0\), depending on \(G\) and the spatial volume, such that for \(0<\beta_t<\beta_c\) the transfer matrix has a **simple** maximal eigenvalue \(\lambda_0\) (vacuum), and the remainder of the spectrum is strictly separated:
  \[
  0<\lambda_1 \le \lambda_2 \le \cdots < \lambda_0.
  \]
- The ratio \(\lambda_1/\lambda_0\) admits an explicit upper bound of the form
  \[
  \frac{\lambda_1}{\lambda_0} \le (c\,\beta_t)^L < 1,
  \]
  where \(c>0\) is a constant and \(L\) is the length of the shortest non-contractible spatial loop (e.g. the spatial extent of the lattice). The first excited state can be identified with a non-contractible Wilson loop (flux tube) wrapping once around the spatial torus.

In particular, the **finite-lattice mass gap**,
\[
\Delta(a) = -\frac{1}{a}\log\left(\frac{\lambda_1}{\lambda_0}\right),
\]
is strictly positive and satisfies a lower bound of the schematic form
\[
\Delta(a) \ge \frac{L}{a}\,|\log(c\beta_t)|,
\]
for \(\beta_t\) in the strong-coupling region \(0<\beta_t<\beta_c\).

This provides a fourth, fully rigorous pillar at finite cutoff:

4. A transfer-matrix-level mass gap \(\Delta(a)>0\) in the strong-coupling regime, with the first excited state represented by a non-contractible Wilson loop in the physical Hilbert space.

Combined with the polarity of reducible configurations (§0), the Haar-induced mass term (§6.3), and the Hessian/eigenvalue gap (§6.6), this shows that on each finite lattice the SU(N) Yang–Mills transfer matrix is genuinely gapped in a regime where constructive control is available.

