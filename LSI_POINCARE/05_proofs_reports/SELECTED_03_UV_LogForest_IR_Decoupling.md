\
---
title: "UV log-forest control and IR topology decoupling for local observables"
date: 2025-12-29
format: markdown+latex
---

## Abstract

Two related ideas appear repeatedly across the project notes:

1. **UV log-forest control:** for local observables, gradient energies blow up at most polylogarithmically as the lattice spacing $a\to 0$.
2. **IR topology decoupling:** slow global/topological modes should not control the relaxation of **local gauge-invariant observables**.

This note packages these ideas into a coherent (but explicitly conditional) argument chain for a **uniform local spectral gap**.

---

## 1. Local observables and tangent-space splitting

Let $F$ be a gauge-invariant observable supported in a fixed physical region $B_R\subset\mathbb{R}^4$.

On the (regular stratum of the) gauge quotient, the project uses a schematic decomposition
\[
T_A(\mathcal{A}/\mathcal{G})
=
T_A^{\mathrm{loc}}\oplus T_A^{\mathrm{gauge}}\oplus T_A^{\mathrm{top}},
\]
where:

- $T^{\mathrm{loc}}$ are variations supported in (or strongly localized to) $B_R$,
- $T^{\mathrm{top}}$ are global/topological variations,
- $T^{\mathrm{gauge}}$ are pure gauge directions.

For local gauge-invariant $F$, one expects
\[
\nabla F(A)\in T_A^{\mathrm{loc}}.
\]

---

## 2. Assumption A: UV log-forest control (polylog gradient bound)

### Assumption A (polylog gradient energy)

There exist constants $C(F)>0$ and $p<\infty$ such that, under the lattice measures $\mu_a$,
\[
\mathbb{E}_{\mu_a}\bigl[\|\nabla F\|^2\bigr] \le C(F)\,(1+\log(1/a))^p.
\]

**Interpretation.** The continuum limit does not “strip away” the Dirichlet-form domain for local observables; the UV cost grows slowly enough (polylog) to remain controllable.

---

## 3. Local–topological mixing bound (the key decoupling estimate)

### Lemma 3.1 (Off-diagonal Hessian mixing is polylog)

Let $H(A)=\mathrm{Hess}_A S$ denote the physical Hessian of the effective action. For $X\in T_A^{\mathrm{loc}}$ and $Y\in T_A^{\mathrm{top}}$,
\[
|\langle X, H(A)Y\rangle|
\le
C_R\,(1+\log(1/a))^p\,\|X\|\,\|Y\|.
\]

*Mechanism (as stated in the project notes).* The Hessian is a sum of local plaquette terms; only plaquettes intersecting $B_R$ can contribute. The restriction of a topological mode to $B_R$ is controlled by Sobolev embedding plus the UV log-forest bound.

**Conditionality.** The lemma is only as strong as (i) the exact norm control on restricted topological modes and (ii) the UV bound used to control those restrictions.

---

## 4. PBH flow invariance of the local block (a Schur complement argument)

Let $\Pi_{\mathrm{loc}}$ be projection onto the local block and write (schematically)
\[
H=
\begin{pmatrix}
H_{\mathrm{loc}} & B \\
B^\ast & H_{\mathrm{top}}
\end{pmatrix}.
\]

Using the mixing bound, the off-diagonal block $B$ is small (polylog). One then expects:

### Lemma 4.1 (Projected evolution with controlled error)

If the full Hessian evolves as
\[
\partial_t H = -2H^2 + \mathcal{R}(t),
\]
then
\[
\partial_t H_{\mathrm{loc}}
\succeq
-2H_{\mathrm{loc}}^2
+ \Pi_{\mathrm{loc}}\,\mathcal{R}(t)\,\Pi_{\mathrm{loc}}
-\varepsilon(a,R)\,I,
\]
where $\varepsilon(a,R)$ is controlled by $\|B\|^2$ and hence is polylog in $1/a$.

---

## 5. Local Riccati inequality and a protected local gap

Let $\lambda_{\mathrm{loc}}(t)=\inf\sigma(H_{\mathrm{loc}}(t))$.

Assume the project’s lattice-scale geometric floor provides
\[
H_{\mathrm{loc}}(0)\succeq c_0 I
\qquad (c_0>0),
\]
and assume the projected source is positive:
\[
\Pi_{\mathrm{loc}}\,\mathcal{R}(t)\,\Pi_{\mathrm{loc}} \succeq c_0 I.
\]

Then combining Lemma 4.1 with the operator-Riccati comparison yields
\[
\dot\lambda_{\mathrm{loc}}(t)
\ge
-2\lambda_{\mathrm{loc}}(t)^2 + c_0-\varepsilon(a,R).
\]

If $a$ is small enough that $\varepsilon(a,R)\le c_0/2$, then the forcing term remains strictly positive and one obtains a uniform floor:
\[
\lambda_{\mathrm{loc}}(t)\ge \rho_0:=\sqrt{\frac{c_0/2}{2}} = \sqrt{\frac{c_0}{4}}
\quad\text{for all }t\ge 0.
\]

---

## 6. Conclusion: local Poincaré inequality / local mass

A uniform lower bound on the local Hessian yields, via standard Bakry–Émery arguments, a Poincaré inequality for local observables:
\[
\mathrm{Var}_{\mu}(F) \le \frac{1}{\rho_0}\,\mathcal{E}(F,F).
\]

**Physical reading.** Global topological slow modes (instantons, winding sectors) may remain slow, but *local physics* relaxes at a rate bounded below by $\rho_0$, producing a robust **local mass scale**.

---

## 7. Why this is interesting (and what to prove next)

The novelty is the proposed *engineering separation principle*:

- locality + polylog UV control ⇒ small off-diagonal mixing,
- small mixing + operator Riccati ⇒ protected local eigenvalue floor,
- protected floor ⇒ local spectral gap ⇒ local mass.

To make it publishable, the key tasks are:

1. Replace Assumption A by an actual bound derived from a concrete RG/flow scheme.
2. Make the local/topological splitting precise in a Sobolev framework.
3. Prove the Schur complement / block-evolution estimate in the exact model.

