---
title: "Wilson Hessian as a Discrete Hodge Laplacian"
subtitle: "Linearized Yang–Mills on the lattice and positivity on physical modes"
author: "Extracted and restructured from the project draft"
date: "2025-12-28"
---

## 0. Why this module is interesting

Near the vacuum \(U_\ell=\mathbf{1}\), the Wilson plaquette action becomes a quadratic form on Lie-algebra edge fields. The key structural identity is:

\[
\nabla^2 S_W(U^{(0)}) \;\;=\;\; 2c_W\, d_1^\ast d_1,
\]
where \(d_1\) is the discrete exterior derivative (edge \(\to\) plaquette).

This is the lattice avatar of “linearized Yang–Mills = Maxwell”:
- \(d_1 X\) is the linearized curvature,
- \(d_1^\ast d_1\) is a discrete Hodge Laplacian on 1-cochains.

The kernel analysis cleanly separates:
- pure gauge modes,
- harmonic (topological / toron) modes,
- co-exact (physical) modes.

This decomposition is the algebraic backbone for later curvature and Bakry–Émery arguments.

---

## 1. Lattice cochain notation

Let \(\Lambda\) be a finite lattice with:

- vertices \(V(\Lambda)\),
- oriented edges \(E(\Lambda)\),
- oriented plaquettes \(P(\Lambda)\).

Let \(\mathfrak g\) be the Lie algebra of a compact Lie group \(G\) with inner product \(\langle\cdot,\cdot\rangle\).

Define cochain spaces:
\[
\mathcal C^0(\Lambda;\mathfrak g)\cong \mathfrak g^{V(\Lambda)},\qquad
\mathcal C^1(\Lambda;\mathfrak g)\cong \mathfrak g^{E(\Lambda)},\qquad
\mathcal C^2(\Lambda;\mathfrak g)\cong \mathfrak g^{P(\Lambda)}.
\]
Equip each with the natural \(\ell^2\) inner product induced by \(\langle\cdot,\cdot\rangle\).

### 1.1 Discrete exterior derivative \(d_1\)

Define \(d_1:\mathcal C^1\to \mathcal C^2\) by the oriented sum around plaquettes: for a plaquette \(p=(x;\mu,\nu)\),
\[
(d_1 X)_p := X_{x,\mu} + X_{x+\hat\mu,\nu} - X_{x+\hat\nu,\mu} - X_{x,\nu}.
\]
This is the discrete curl.

Its adjoint \(d_1^\ast:\mathcal C^2\to \mathcal C^1\) satisfies
\[
\langle d_1 X, Y\rangle_2 = \langle X, d_1^\ast Y\rangle_1.
\]

---

## 2. Wilson action and expansion near the vacuum

Let \(U=(U_\ell)_{\ell\in E(\Lambda)}\in G^{E(\Lambda)}\) be link variables.

For each oriented plaquette \(p\), let \(U_p\) be the plaquette holonomy, i.e. the ordered product of link matrices around \(p\).

The Wilson action is
\[
S_W(U) = \beta \sum_{p\in P(\Lambda)}\Big(1 - \frac1N \Re\mathrm{Tr}(U_p)\Big)
\]
(for \(G=SU(N)\); other compact groups use the analogous class function).

Let \(U^{(0)}\) be the trivial configuration \(U_\ell=\mathbf 1\).

### 2.1 Exponential coordinates around \(U^{(0)}\)

Write
\[
U_\ell = \exp(X_\ell),\qquad X_\ell\in \mathfrak g,
\]
with \(X\in \mathcal C^1(\Lambda;\mathfrak g)\) small.

For small \(X\), the Baker–Campbell–Hausdorff expansion yields:
- the plaquette holonomy is
  \[
  U_p = \exp\big((d_1 X)_p + O(|X|^2)\big),
  \]
- hence the Wilson action expands as
  \[
  S_W(U^{(0)}\exp X)
  = S_W(U^{(0)}) + c_W \sum_{p}\|(d_1 X)_p\|^2 + O(\|X\|^3),
  \]
for some constant \(c_W>0\) depending on \(\beta\) and normalization.

---

## 3. The Hessian identity

**Proposition 3.1 (Wilson Hessian at the vacuum).**  
Identifying \(T_{U^{(0)}}(G^{E(\Lambda)})\simeq \mathcal C^1(\Lambda;\mathfrak g)\), the Hessian of the Wilson action satisfies
\[
\nabla^2 S_W(U^{(0)}) = 2c_W\, d_1^\ast d_1.
\]

*Proof (coordinate-level).*  
From the quadratic expansion,
\[
S_W(U^{(0)}\exp X) = S_W(U^{(0)}) + c_W \langle d_1 X, d_1 X\rangle_2 + O(\|X\|^3).
\]
Thus the quadratic form associated to the Hessian is
\[
\langle X, \nabla^2 S_W(U^{(0)})\,X\rangle_1 = 2c_W \langle d_1 X, d_1 X\rangle_2.
\]
Using the definition of adjoint,
\[
\langle d_1 X, d_1 X\rangle_2 = \langle X, d_1^\ast d_1 X\rangle_1,
\]
so the operator identity follows. ∎

### 3.2 Immediate consequences

- **Nonnegativity**
  \[
  \langle X, \nabla^2 S_W(U^{(0)})X\rangle_1 = 2c_W\|d_1 X\|_2^2\ge 0.
  \]
- **Kernel**
  \[
  \ker(\nabla^2 S_W(U^{(0)}))=\ker(d_1),
  \]
the space of discrete closed 1-forms.

---

## 4. Gauge directions and discrete Hodge decomposition

Define the discrete gradient \(d_0:\mathcal C^0\to \mathcal C^1\) by
\[
(d_0\phi)_{x,\mu} := \phi_{x+\hat\mu}-\phi_x.
\]
Then \(d_1d_0=0\), so \(\mathrm{im}(d_0)\subset \ker(d_1)\).

Define the 1-form Laplacian
\[
\Delta_1 := d_1^\ast d_1 + d_0 d_0^\ast.
\]

On a finite complex (with e.g. periodic boundary conditions), one has the finite-dimensional Hodge decomposition
\[
\mathcal C^1
= \mathrm{im}(d_0)\ \oplus\ \ker(\Delta_1)\ \oplus\ \mathrm{im}(d_1^\ast).
\]

Interpretation:

- \(\mathrm{im}(d_0)\): pure gauge directions (infinitesimal gauge transforms),
- \(\ker(\Delta_1)\): harmonic 1-forms (torons / global modes),
- \(\mathrm{im}(d_1^\ast)\): co-exact 1-forms (physical fluctuations).

From the decomposition,
\[
\ker(d_1)=\mathrm{im}(d_0)\oplus \ker(\Delta_1),
\]
so the Wilson Hessian vanishes precisely on **gauge + harmonic** modes.

---

## 5. Positivity on physical modes

Let
\[
\mathcal C^1_{\mathrm{coex}} := \mathrm{im}(d_1^\ast).
\]

**Proposition 5.1 (Strict positivity on co-exact modes).**  
On \(\mathcal C^1_{\mathrm{coex}}\),
\[
d_1^\ast d_1 \text{ is positive definite}.
\]
Equivalently, the Wilson Hessian is strictly positive on \(\mathrm{im}(d_1^\ast)\).

*Reason.*  
If \(X=d_1^\ast Y\) and \(d_1 X=0\), then \(d_1 d_1^\ast Y=0\). Under the Hodge decomposition, this forces \(X\) to be orthogonal to \(\mathrm{im}(d_1^\ast)\) unless \(X=0\). More concretely,
\[
\langle X, d_1^\ast d_1 X\rangle_1 = \|d_1 X\|_2^2,
\]
so vanishing implies \(d_1 X=0\), hence \(X\in \ker(d_1)\cap \mathrm{im}(d_1^\ast)=\{0\}\). ∎

---

## 6. What is potentially novel here?

The decomposition itself is standard. The “potentially new” angle comes from **how it is used** in the larger program:

1. It isolates exactly which directions the Wilson action controls quadratically near the vacuum (co-exact modes).
2. It cleanly separates modes that must be controlled by other mechanisms:
   - pure gauge directions (handled by invariance / quotienting),
   - harmonic modes (often lifted by boundary conditions, regulators, or geometric effects like Haar mass).
3. It plugs into the Bakry–Émery tensor
   \[
   \mathrm{Ric}_\mu = \mathrm{Ric}_g + \nabla^2 S,
   \]
   where \(\nabla^2 S_W\) contributes \(d_1^\ast d_1\)-type positivity on physical fluctuations.

So the novelty is not “discovering \(d_1^\ast d_1\)”, but embedding this discrete Hodge structure as a *curvature input* for functional inequalities in gauge theory.

---

## 7. Further work suggested by this module

1. **Uniform spectral estimates.**  
   The smallest nonzero eigenvalue of \(d_1^\ast d_1\) on co-exact modes depends on volume. Understanding how other terms (e.g. Haar mass) change this is critical.

2. **Harmonic modes and topology.**  
   On periodic lattices, torons can be genuine low-energy excitations. One needs a consistent treatment:
   - restrict sectors,
   - add gauge-invariant regulators,
   - or use probabilistic concentration to show their suppression in the measure.

3. **Nonlinear regime.**  
   The quadratic analysis is local. Extending control into a finite small-field neighborhood and quantifying higher-order errors is necessary for a robust curvature bound.

