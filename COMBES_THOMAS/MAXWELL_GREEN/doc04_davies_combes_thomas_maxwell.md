# Davies / Combes–Thomas Decay for the Massive Maxwell Green Kernel

*This note collects the finite-range inverse-decay machinery (Part 9) in a single place, emphasizing the dependence of constants on “row-sum” parameters and boundary effects. This is the piece that upgrades operator positivity \(M\succeq m^2I\) into **exponential spatial decay** of \(M^{-1}\).*

---

## 1. The operator

Let \(\Lambda\) be a finite \(4\)D lattice (torus or box). Let \(E(\Lambda)\) be the set of oriented links, equipped with the link-adjacency graph distance \(\mathrm{dist}_E\).

Consider the operator on \(1\)-cochains (link fields)
\[
M := m^2 I + \alpha\, d_1^\*d_1
\quad\text{on}\quad
\mathsf H:=\ell^2(E(\Lambda);\mathfrak g).
\]

Basic properties (uniform in \(|\Lambda|\)):
- \(M\succeq m^2 I\) (uniform positivity).
- \(M\) has **finite range** with respect to \(\mathrm{dist}_E\): \(M_{bb'}=0\) if \(\mathrm{dist}_E(b,b')>1\).

---

## 2. Abstract finite-range inverse decay via Combes–Thomas conjugation

Let \(A\) be a self-adjoint operator on \(\ell^2(V)\) with:
- \(A\succeq a_0 I\),
- finite range \(R\),
- row-sum bound \(B\) on off-diagonal couplings.

Combes–Thomas uses the conjugation
\[
A_\theta := e^{\theta \phi}\,A\,e^{-\theta \phi},
\]
with \(\phi\) a 1-Lipschitz “distance to a set” function, and chooses \(\theta\) so that \(A_\theta\) remains invertible with controlled norm. This yields the standard exponential off-diagonal inverse bound:
\[
|(A^{-1})_{xy}|\ \lesssim\ e^{-c\,\mathrm{dist}(x,y)}.
\]

The project extracts a clean, volume-uniform version specialized to the link graph, with explicit bookkeeping for the parameters \((a_0,B,R)\).

---

## 3. Row-sum constants and why they matter

The decay exponent depends on the competition between:
- the **spectral floor** \(a_0=m^2\), and
- the amount of off-diagonal coupling (measured by \(B\)).

For the Maxwell operator on the link graph in \(d=4\), bounded overlap of plaquettes implies a uniform degree bound, hence a uniform row-sum bound:
\[
B\ \le\ \alpha\,C_B,\qquad C_B\le 18.
\]

Boundary conditions affect \(B\) only through a localized modification of adjacency near the boundary; the project introduces “partial” row-sum constants \(C_{\partial}\) to isolate that effect cleanly.

---

## 4. Davies-type decay for the Maxwell Green kernel

Let \(G:=M^{-1}\). The key output is a Davies-type bound of the form
\[
\|G_{b,b'}\|\ \le\ C\,e^{-\gamma\,\mathrm{dist}_E(b,b')}
\qquad (b,b'\in E(\Lambda)),
\]
with constants \((C,\gamma)\) depending only on \((m^2,\alpha,C_B)\) (and the boundary row-sum constant, if needed), **not** on \(|\Lambda|\).

The project records:
- a baseline proposition with a global row-sum constant \(B\),
- a refined proposition replacing \(B\) by a boundary-aware constant \(C_0\),
- and a corollary using a partially localized constant \(C_{\partial}\) to sharpen the exponent.

These refinements are important because they prevent the decay rate from being polluted by a pessimistic global bound when only a thin boundary layer is “worse.”

---

## 5. Why this is a “bridge theorem” in the mass-gap proof

This module sits exactly at the junction:
\[
\text{(local curvature / Poincaré)}\ \Rightarrow\ 
\text{(covariance resolvent)}\ \Rightarrow\ 
\text{(kernel decay)}\ \Rightarrow\ 
\text{(exponential clustering)}.
\]

It is robust because it is:
- purely finite-dimensional,
- purely operator-theoretic,
- insensitive to nonabelian gauge complications once \(M\) is identified.

---

## 6. Next steps / possible extensions

1. **Optimize constants**: sharpen the dependence of \(\gamma\) on \((m,\alpha)\) and on the local degree bound (using exact lattice geometry instead of \(C_B\le 18\)).
2. **Random-operator connection**: interpret the Maxwell kernel as a deterministic “reference resolvent,” then treat fluctuations of the curvature matrix as a perturbation. This frames the Yang–Mills problem in language familiar from random Schrödinger operators, but with a *geometrically controlled* perturbation.
3. **Continuum scaling**: express the decay exponent in physical units and isolate what must stay uniform along \(a\downarrow 0\).

---

## Sources inside this project

- Abstract Combes–Thomas framework: `### 9.1 Abstract finite-range inverse decay lemma via Combes–Thomas conjugation.txt`
- Davies decay statements:  
  `003_Proposition_9_X_Davies_type_decay_for_the_massive_Maxwell_Green_kernel.md`  
  `006_Proposition_9_X_Davies_decay_with_C_0_in_place_of_D_E.md`  
  `008_Corollary_9_X_Davies_decay_with_C_partial.md`
- Row-sum constant bookkeeping: `005_Definition_row_sum_constants_for_Delta_1.md`, `007_Definition_boundary_row_sum_constant.md`
