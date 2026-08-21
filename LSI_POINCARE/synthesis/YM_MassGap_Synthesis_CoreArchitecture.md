# Yang–Mills Mass Gap: Core Architecture (Synthesis)

> **Purpose.** This document is a *clean, portable spine* of the project: definitions, the core chain of implications, and the minimal set of conjectural “bridges” that remain if the finite-dimensional lattice pieces are accepted.

---

## 1. The object we want

Let \(G=\mathrm{SU}(N)\). A **mass gap** \(\Delta>0\) means that connected Euclidean correlation functions of gauge-invariant local observables (e.g. plaquette operators) decay exponentially in separation:
\[
\langle \mathcal{O}(x)\mathcal{O}(0)\rangle_c \;\sim\; e^{-\Delta |x|}\quad (|x|\to\infty),
\]
equivalently that the reconstructed Hamiltonian has a strictly positive spectral gap above the vacuum.

On the lattice (spacing \(a\)), this is encoded by the **transfer matrix** \(T\) (Osterwalder–Schrader framework). Writing
\[
T = e^{-a H_T},
\]
the physical gap is \(\Delta = E_1 - E_0\), with \(E_0\) the ground state.

---

## 2. The project’s “one-line mechanism”

The mechanism is a chain:

\[
\boxed{
\text{Compact gauge group} \Rightarrow \text{Haar Jacobian curvature} \Rightarrow 
\lambda_{\min}(\nabla^2 S_{\mathrm{eff}})\ge c_0>0 \Rightarrow
\text{spectral gap} \Rightarrow \Delta>0.
}
\]

The new-ish claim is that **compactness/topology of \(G\)** injects a **strictly positive quadratic term** into the effective action coming from the Haar measure, producing a uniform “curvature floor” \(c_0\) (no tunable mass parameter).

---

## 3. The lattice layer (finite-dimensional)

### 3.1 Configuration space, measure, and effective action
For a finite lattice, the link configuration space is
\[
\mathcal{C} = G^{|B|},
\]
with product Haar measure \(\mu_{\mathrm{Haar}}\). With Wilson action \(S_W(U)\) and \(\beta\) the usual coupling parameter, the lattice YM measure is
\[
d\mu_{\mathrm{YM}}(U) \propto e^{-S_W(U)}\, d\mu_{\mathrm{Haar}}(U).
\]

Introduce exponential coordinates on each link \(U_\ell=\exp(i A_\ell)\) near the identity. The Haar volume element becomes
\[
d\mu_{\mathrm{Haar}}(U) = J(A)\, dA,
\qquad
S_{\mathrm{Haar}}(A):= -\log J(A).
\]

### 3.2 Haar mass coefficient (local quadratic term)
The central coefficient is asserted to be
\[
S_{\mathrm{Haar}}(A) = \frac{c_0}{2}\mathrm{Tr}(A^2) + O(A^4),
\qquad
c_0 = \frac{N^2-1}{2N}.
\]
The interpretation is **“mass from geometry”**: a strictly convex quadratic term produced by the Jacobian.

### 3.3 Lattice Hessian structure and lower bound
For the effective action
\[
S_{\mathrm{eff}} = S_W + S_{\mathrm{Haar}},
\]
the project asserts a structural decomposition of the Hessian
\[
H(U)=\nabla^2 S_{\mathrm{eff}}(U)
= \beta\,\Delta_{\mathrm{lattice}} - \beta V(U) + c_0 I,
\]
and a uniform **horizontal** lower bound
\[
\lambda_{\min}(U)\;\ge\;c_0.
\]

### 3.4 Gap consequence (finite \(a\))
Combining the curvature floor with transfer-matrix technology yields a lattice spacing bound of the form
\[
\Delta \;\gtrsim\; \frac{\sqrt{c_0/2}}{a},
\]
with explicit numerical constants quoted in the project for SU(2), SU(3), etc.

> **Important caution.** This is a *finite lattice-spacing* bound. The continuum limit \(a\to 0\) requires renormalization control and a physical identification of the limiting Hamiltonian gap.

---

## 4. The singular-set layer (polarity + stratified analysis)

The configuration/orbit space has a singular set \(\Sigma\) (reducible connections / non-free gauge orbits). The mechanism wants to run PDE/Dirichlet-form arguments on the **regular stratum** while ensuring \(\Sigma\) does not act like a boundary.

### 4.1 Polarity target
Show \(\Sigma\) is **polar** (capacity zero) for the relevant diffusion:
\[
\mathrm{Cap}_{\mu}(\Sigma)=0.
\]
Intuition: the stochastic/Langevin dynamics almost surely never hit \(\Sigma\), so maximum principles and integration-by-parts effectively ignore it.

### 4.2 Gaussian reference and change-of-measure bridge
A key strategy is:
1. Prove polarity for a Gaussian reference measure \(\mu_0\) on a linearized configuration space.
2. Transfer polarity to \(\mu_{\mathrm{YM}}\) using an \(L^p\) density condition for \(d\mu_{\mathrm{YM}}/d\mu_0\).

---

## 5. The dynamic layer (Bakry–Émery + Riccati)

A second, “flow” version of the mechanism uses:
- **Bakry–Émery curvature**: a lower bound on \(\nabla^2 V\) implies a Poincaré inequality and thus a spectral gap for the associated Markov generator.
- **Riccati-type evolution** for the smallest curvature eigenvalue:
\[
\frac{d\lambda}{dt} \;\gtrsim\; -\alpha \lambda^2 + \sigma_{\mathrm{eff}}(t),
\]
where \(\sigma_{\mathrm{eff}}\) collects *positive sources* (Haar + anomaly) and *corrections*.
If \(\sigma_{\mathrm{eff}}(t)\ge \sigma_{\min}>0\), then \(\lambda(t)\) converges to a positive fixed point \(\sim\sqrt{\sigma_{\min}/\alpha}\).

---

## 6. What remains genuinely nontrivial

The project’s own “bottlenecks” can be stated cleanly:

1. **Continuum UV control**: show a renormalized analogue of the curvature floor survives (the “log-forest” / UV control conjecture).
2. **Continuum polarity**: show \(\mathrm{Cap}_{\mu_{\mathrm{YM}}}(\Sigma)=0\) in the infinite-dimensional limit.
3. **Bridge to the physical mass gap**: show the relevant spectral gap (Dirichlet-form / Langevin generator / transfer-matrix gap) matches the mass gap definition used in the Clay problem.

---

## 7. What this synthesis is *for*

If you start a new chat, this file should let you say:

- “Here is the single intended causal chain.”
- “Here are the two bridge lemmas (polarity transfer, curvature-to-gap).”
- “Here is exactly what needs to be made airtight in the continuum.”

No extra directions. Just the spine.
