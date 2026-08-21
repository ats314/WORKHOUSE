---
title: "Candidate Theorem: Global Wilson Hessian Bound for SU(3) Wilson Plaquette Action"
date: "2026-01-01"
---

## 1. Status statement

This document assembles the **project’s most crucial analytic bottleneck** into a single place:

> A global, explicit upper bound for the Wilson action Hessian, uniform in lattice volume, in a small-field region.

The project uses this as the “curvature erosion bound” needed for convexity and restoration arguments.

**Important:** The statement below is a *candidate theorem/proof skeleton*.  
It is written in a theorem-proof style, but it requires a careful audit of:

- the chosen norms,
- the exact identification of link variables vs exponential coordinates,
- the product rule bookkeeping for the plaquette holonomy,
- and uniformity in lattice size.

---

## 2. Setup and notation

Let \(L\in\mathbb{N}\), dimension \(d=4\), and consider link fields
\[
  A = \{A_\ell\}_{\ell\in \mathcal{E}},\qquad A_\ell\in\mathfrak{su}(3).
\]
Set
\[
  U_\ell = e^{A_\ell}\in SU(3),
\]
and for each plaquette \(p=(\ell_1,\ell_2,\ell_3,\ell_4)\) define
\[
  U_p := U_{\ell_1}U_{\ell_2}U_{\ell_3}^{-1}U_{\ell_4}^{-1}.
\]
The Wilson plaquette action is
\[
  S_W(A) := \beta\sum_{p} \left(1-\frac{1}{3}\operatorname{ReTr}(U_p)\right).
\]

Let \(H\) denote a tangent vector \(H=\{H_\ell\}\) with \(H_\ell\in\mathfrak{su}(3)\).
Write \(D^2 S_W(A)[H,H]\) for the quadratic form, and \(\|\nabla^2 S_W(A)\|_{\mathrm{op}}\) for the induced operator norm in the Euclidean structure \(\sum_\ell \|H_\ell\|_F^2\).

Assume the small-field uniform bound
\[
  \|A_\ell\|_F \le \rho \qquad \forall \ell,
\]
for some \(\rho\le 1\) (the project constants are computed for \(\rho=1\)).

---

## 3. Analytic lemmas: commutators and exponential derivatives

### Lemma 3.1 (Adjoint action and commutator bounds)

For \(X,Y\in\mathfrak{su}(3)\),
\[
  \|[X,Y]\|_F \le 2 \|X\|_F \|Y\|_F.
\]
Consequently, for the adjoint action \(\mathrm{Ad}_{e^X}(Y)=e^X Y e^{-X}\),
\[
  \|\mathrm{Ad}_{e^X}(Y)\|_F \le e^{2\|X\|_F}\,\|Y\|_F.
\]

### Lemma 3.2 (Fréchet derivative bounds for \(e^A\))

Let \(f(A)=e^A\). For \(\|A\|_F\le \rho\),
\[
  \|D e^A[H]\|_F \le e^{\rho}\,\|H\|_F,
\]
\[
  \|D^2 e^A[H,K]\|_F \le e^{2\rho}\,\|H\|_F\,\|K\|_F.
\]
(Variants in the project include a more conservative bound \(e^{4\rho}\|H\|\|K\|\) depending on how adjoint rotations are handled.)

---

## 4. Candidate theorem statement (project form)

### Theorem 4.1 (Global Wilson Hessian erosion bound; project version)

There exists a constant \(C_{SU(3)}<\infty\) (explicit) such that for all lattices \(L^4\) and all link configurations \(A\) with \(\|A_\ell\|_F\le \rho\),
\[
  \|\nabla^2 S_W(A)\|_{\mathrm{op}}
  \;\le\;
  C_{SU(3)}\,\beta\,\rho^2.
\]
Equivalently, for all tangent vectors \(H\),
\[
  |D^2 S_W(A)[H,H]|
  \;\le\;
  C_{SU(3)}\,\beta\,\rho^2\,\sum_{\ell}\|H_\ell\|_F^2.
\]

#### Explicit constant as given in the project notes

The project decomposes the plaquette-level bound into three contributions:

- \(C_1\): local second derivatives on one link exponential
- \(C_2\): mixed first-derivative products within the plaquette
- \(C_3\): nested commutator (“backreaction”) terms

and states for \(\rho=1\):
\[
  C_1 = e^7,\qquad
  C_2 = 12 e^3,\qquad
  C_3 = 2 e^3,
\]
so that
\[
  C_p := C_1 + C_2 + C_3 \lesssim 3\times 10^3.
\]
Using that each link participates in \(6\) plaquettes in \(d=4\), the global constant is taken as
\[
  C_{SU(3)} := 6 C_p \approx 2\times 10^4.
\]

---

## 5. Proof skeleton (what must be checked)

1. **Differentiate one plaquette term.**  
   Write \(F_p(A)=\operatorname{ReTr}(U_p)\). Then \(D^2 F_p\) is a sum of terms obtained by product differentiation of \(U_{\ell_1}U_{\ell_2}U_{\ell_3}^{-1}U_{\ell_4}^{-1}\).

2. **Bound each term by derivative norms.**  
   Use Lemma 3.2 to control \(D e^{A_\ell}\) and \(D^2 e^{A_\ell}\), plus adjoint bounds to control conjugations.

3. **Convert plaquette bounds to global bounds.**  
   Use locality (each link appears in finitely many plaquettes, independent of \(L\)) and a block Gershgorin / operator-norm estimate to lift the plaquette bound to \(\|\nabla^2 S_W(A)\|_{\mathrm{op}}\).

4. **Track dependence on \(\rho\).**  
   If the derivative bounds give factors \(e^{c\rho}\), the constant can be stated explicitly as \(C_{SU(3)}(\rho)\).

---

## 6. Why this theorem is central

The project’s remaining chain (dynamic restoration, LSI, clustering, OS reconstruction) is designed to become rigorous **once** a theorem of the form Theorem 4.1 is made fully correct with explicit constants.

---

## 7. Minimum audit checklist

To promote Theorem 4.1 to a reliable theorem, the following must be fixed/verified:

- consistent norm choice (Frobenius vs operator norm) at every step,
- a clean definition of the coordinate patch and how \(\rho\) relates to group distance,
- exact handling of \(U^{-1}\) variations and their derivatives,
- a fully explicit plaquette Hessian expansion with term-by-term bounds,
- a precise “local-to-global” operator-norm lemma for the lattice Hessian as a sparse block matrix.
