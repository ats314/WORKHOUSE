# Selection Report: “Most Novel / Most Theory-Pregnant” Derivations in the Project Files
*(Why these were chosen, what they connect to, and how to push them into publishable territory.)*

## Executive summary

The project contains a coherent, repeating motif that is genuinely fertile:

> **Phase isolation:** rewrite θ-term partition functions as a positive-coefficient generating function in \(z=e^{i\theta}\), so that all local tensor entries remain real and non-negative and complex phases appear only in a final boundary sum/evaluation.

This is implemented cleanly for the 1D rotor, plausibly extendable to interacting rotors (with a polynomial transfer matrix), and explicitly proposed (but not yet engineered) for 2D U(1) Villain gauge theory. The same motif then hits a wall in the SU(2) fusion basis, producing a useful negative result: strict local positivity is obstructed by 6j / q-6j sign/phase structure, pushing the computational strategy toward complex-tensor TRG.

Those are the “best” pieces because they are:
- structurally general (not just model-specific),
- falsifiable (have explicit error bounds / convergence levers),
- expandable into a broader framework (“how to defang θ-terms with TNs”).

---

## What I selected (and why)

### 1) Phase-Isolation Principle (general theory doc)

**Why selected:**  
It unifies the project’s rotor and U(1) gauge constructions under a single conceptual mechanism: compute non-negative sector weights \(Z_Q^{(0)}\) and evaluate \(Z(\theta)=\sum_Q e^{i\theta Q}Z_Q^{(0)}\). This is “theory-shaped” and points to general conditions (integer additive charge + θ=0 positivity).

**What to expand next:**  
Formulate a general theorem with explicit sufficient conditions for existence of a positive-coefficient generating function \(P(z)\), including bounds on truncation error in \(Q\).

---

### 2) 1D rotor: boundary-only θ + Gaussian truncation bound

**Why selected:**  
This is the most complete proof package in the project. It contains a clean error bound:

\[
|Z_{\mathrm{TN}}-Z|\le 4Z\,\exp\!\left(-\frac{2\pi^2K_{\max}^2}{\beta}\right),
\]
implying \(K_{\max}\sim \sqrt{\beta\ln(1/\varepsilon)}\) and (critically) showing the exponent is independent of Trotter slice count \(N\). The archive also records a “dead end” correction: earlier \(N\)-dependent truncation exponents were unphysical and fixed.

**What to expand next:**  
- Formalize the reflection-principle argument in a rigorous measure-theoretic way (or at least in a careful discrete-time path measure).
- Benchmark the bound against numerical tail estimates to see how sharp constants are.

---

### 3) Interacting rotor: polynomial transfer matrix + cost scaling

**Why selected:**  
It preserves strict positivity in the presence of interactions (via Trotter splitting) and introduces a computationally powerful representation:

\[
W(X)=\sum_{\Delta k} W^{(\Delta k)}X^{\Delta k},\quad W^{(\Delta k)}\ge 0.
\]

This is the first step toward a reusable “θ-term TN design pattern” for interacting systems.

**What to expand next:**  
- Implement the interacting TN and do convergence scans in \(N,M,K_{\max}\).
- Resolve the project’s internal log-factor bookkeeping discrepancy in the complexity estimate by measuring effective scaling numerically.
- Explore FFT-based evaluation of \(W(X)^N\) on roots of unity to amortize many θ values.

---

### 4) 2D U(1) Villain: validated non-negative TN + proposed strict θ-sector decomposition

**Why selected:**  
The θ=0 site tensor is validated and already used in a successful TRG run. The flux truncation bound is explicit and Gaussian in \(N_{\max}^2\). The proposed strict θ-sector design is an obvious and exciting next engineering target:

\[
Z(\beta,\theta)=\sum_Q e^{i\theta Q} Z_Q^{(0)}(\beta),
\qquad Z_Q^{(0)}\ge 0.
\]

This is the cleanest on-ramp from “one model solved” to “methodology”.

**What to expand next:**  
- Build the charge accumulator / polynomial TN and verify it reproduces the existing complex-phase implementation.
- Study how \(Q\)-tails scale with volume in practice (critical for setting \(Q_{\max}\)).

---

### 5) SU(2) θ attempts: obstruction + algorithmic salvage

**Why selected (despite being a “no”):**  
The roadmap’s conclusion—that strict local positivity is impossible in the fusion/irrep basis because 6j symbols oscillate in sign and q-6j are complex—saves a lot of wasted effort. The discussion then pivots toward an actionable strategy: deterministic TRG with complex tensors, supported by q-6j caching + symmetry reduction.

**What to expand next:**  
- Make the obstruction statement more rigorous (e.g., by proving that no local basis change within the fusion category can make all intertwiner coefficients non-negative while preserving fusion rules).
- If pursuing SU(2) anyway: implement an optimized q-6j table with canonicalization under symmetries and test realistic \(J_{\max}\).

---

## The bigger theory these connect to

The project is inching toward a general framework:

> **Topological-term TN framework:**  
> Represent \(Z(\theta)\) as evaluation of a positive generating function \(P(z)\) (or a polynomial transfer operator), where coefficients are θ=0 sector weights for an additive integer topological charge.

This smells like a bridge between:
- tensor networks as *deterministic partition-function evaluators*,
- topological charge distributions as *Fourier coefficients*,
- and “sign problems” as *a failure to find a positive-coefficient representation in the chosen variables*.

The U(1) cases strongly support this framework.
The SU(2) fusion-basis obstruction suggests that in non-Abelian cases, the existence of such a representation may depend on deeper categorical structures or on moving to dual variables (loops/surfaces) where an additive integer charge is explicit.

---

## Concrete “next steps” that would produce publishable results

1. **2D U(1) strict sector TN demo** on small lattices, then scaling to larger volumes (this would already be a nice methods paper).
2. **Interacting rotor benchmark paper**: TN vs exact diagonalization for grids of \((\beta,\lambda,\theta)\), with controlled errors and scaling plots.
3. **General theorem note**: sufficient conditions for phase isolation (positive-coefficient generating function) + explicit truncation bounds.
4. **SU(2) feasibility study**: implement q-6j caching + complex-TNR contraction; publish as “what works and what provably can’t” for θ-term SU(2) in fusion basis.
5. **Periodic θ-observable extraction**: standardize Fourier-fitting + susceptibility extraction; propagate errors; prevent polynomial-fit artifacts.

---

## Files produced in this extraction set

- `LATTICE_QCD_phase_isolation_principle.md`
- `LATTICE_QCD_1D_rotor_boundary_phase_and_error_bounds.md`
- `LATTICE_QCD_interacting_rotor_polynomial_TN_and_complexity.md`
- `LATTICE_QCD_2D_U1_theta_sector_design.md`
- `LATTICE_QCD_SU2_theta_obstruction_and_q6j_caching.md`
- `LATTICE_QCD_periodic_theta_fitting_and_susceptibility.md`

