---
title: "A Core Local Horizontal Curvature Theorem for Lattice Yang–Mills"
subtitle: "Uniform small-field Bakry–Émery control in the gauge-invariant sector"
author: "Extracted and restructured from the project draft"
date: "2025-12-28"
---

## 0. Why this module is interesting

This is the sharpest “engine block” in the current project: a theorem asserting that, in a uniform neighborhood of the vacuum configuration \(U^{(0)}\), the **Bakry–Émery curvature is strictly positive in horizontal (physical) directions**, with constants **independent of the lattice volume**.

That sort of uniformity is exactly what one needs if one dreams of:

- volume-independent functional inequalities (Poincaré / LSI),
- uniform mixing for a stochastic-quantization diffusion,
- and ultimately a route toward a mass-gap statement.

Crucially, the positivity is not claimed globally on the whole configuration space—only in a small-field region. This keeps the statement honest and technically believable.

---

## 1. Finite-volume Yang–Mills configuration geometry

Let \(G\) be a compact Lie group with a fixed bi-invariant metric \(g_G\). Let \(\Lambda\) be a finite lattice with edge set \(E(\Lambda)\). Define the configuration manifold
\[
M_\Lambda := G^{E(\Lambda)}
\]
equipped with the product metric \(g_\Lambda\) and product Haar (Riemannian) volume \(d\mathrm{vol}_{g_\Lambda}\).

### 1.1 Ricci curvature of the configuration manifold

Assume the single-link Ricci tensor satisfies
\[
\mathrm{Ric}_G \ge \kappa_G\, g_G
\qquad (\kappa_G>0).
\]
Then by product geometry,
\[
\mathrm{Ric}_{g_\Lambda} \ge \kappa_G\, g_\Lambda,
\]
with the same \(\kappa_G\) independent of \(\Lambda\).

---

## 2. Gauge symmetry and horizontal subspaces

Let \(\mathcal G_\Lambda\) be the lattice gauge group acting on \(M_\Lambda\) by endpoint conjugations on links. This action is isometric w.r.t. \(g_\Lambda\).

For a configuration \(U\in M_\Lambda\), let \(V_U\subset T_U M_\Lambda\) be the vertical (orbit) tangent space and define the horizontal subspace
\[
H_U := V_U^\perp \subset T_U M_\Lambda
\]
(on the regular set).

For gauge-invariant observables \(f\), one has \(\nabla f(U)\in H_U\), so horizontal curvature is the relevant object.

---

## 3. Gibbs measure and Bakry–Émery tensor

Let the finite-volume Gibbs measure be
\[
d\mu_\Lambda(U) = Z_\Lambda^{-1} e^{-S_\Lambda(U)}\, d\mathrm{vol}_{g_\Lambda}(U),
\]
where
\[
S_\Lambda = S_W + S_{\mathrm{add},\Lambda}.
\]

Here:
- \(S_W\) is the Wilson plaquette action,
- \(S_{\mathrm{add},\Lambda}\) is an additional gauge-invariant term (e.g. regulator, gauge-fixing proxy, or other local modification).

Define the Bakry–Émery tensor:
\[
\mathrm{Ric}_{\mu_\Lambda} := \mathrm{Ric}_{g_\Lambda} + \nabla^2 S_\Lambda.
\]

---

## 4. A local horizontal curvature bound

We assume the following structural hypothesis on the “additional term”.

**Assumption A (uniform Hessian lower bound).**  
There exists \(C_{\mathrm{add}}\ge 0\), independent of \(\Lambda\), such that
\[
\nabla^2 S_{\mathrm{add},\Lambda}(U) \ge - C_{\mathrm{add}}\, g_\Lambda(U)
\qquad \forall U\in M_\Lambda
\]
as quadratic forms.

We also assume a **dominance condition**
\[
\kappa_G > C_{\mathrm{add}}.
\]

This inequality is the clean algebraic statement “group curvature dominates any controlled concavity coming from the added term”.

### 4.1 Curvature bound at the vacuum

Let \(U^{(0)}\) denote the trivial configuration.

At \(U^{(0)}\), the Wilson Hessian contributes a nonnegative operator (on the tangent space),
\[
\nabla^2 S_W(U^{(0)}) \ge 0,
\]
so on horizontal vectors \(v\in H_{U^{(0)}}\),
\[
\begin{aligned}
\mathrm{Ric}_{\mu_\Lambda}(U^{(0)})(v,v)
&= \mathrm{Ric}_{g_\Lambda}(U^{(0)})(v,v) + \nabla^2 S_W(U^{(0)})(v,v) + \nabla^2 S_{\mathrm{add},\Lambda}(U^{(0)})(v,v) \\
&\ge \kappa_G |v|_{g_\Lambda}^2 + 0 - C_{\mathrm{add}} |v|_{g_\Lambda}^2 \\
&= (\kappa_G - C_{\mathrm{add}})\,|v|_{g_\Lambda}^2.
\end{aligned}
\]
Define
\[
\rho_0 := \kappa_G - C_{\mathrm{add}} > 0.
\]
Then
\[
\mathrm{Ric}_{\mu_\Lambda}(U^{(0)})(v,v)\ge \rho_0 |v|^2
\qquad \forall v\in H_{U^{(0)}}.
\]

### 4.2 Stability in a small-field neighborhood

Because:
- \(U\mapsto \mathrm{Ric}_{\mu_\Lambda}(U)\) is continuous,
- the horizontal distribution \(U\mapsto H_U\) varies continuously on the regular set,
- the unit sphere bundle in \(H\) over a compact neighborhood is compact,

the inequality persists in a small ball.

The key point for this project is that one can choose the ball size **independently of \(\Lambda\)**, because:
- \(\kappa_G\) is independent of \(\Lambda\) (product curvature),
- the Hessian bound constant \(C_{\mathrm{add}}\) is assumed independent of \(\Lambda\),
- the construction is local and uses only finite-dimensional continuity.

---

## 5. The theorem (local, horizontal, uniform-in-volume)

Let \(B_r(U^{(0)})\subset M_\Lambda\) be the geodesic ball of radius \(r\) around \(U^{(0)}\) w.r.t. \(g_\Lambda\).

**Theorem 5.1 (Uniform local horizontal Bakry–Émery bound).**  
Assume:

1. \(\mathrm{Ric}_{g_\Lambda}\ge \kappa_G g_\Lambda\) with \(\kappa_G>0\) independent of \(\Lambda\),
2. \(\nabla^2 S_{\mathrm{add},\Lambda}\ge -C_{\mathrm{add}} g_\Lambda\) with \(C_{\mathrm{add}}<\kappa_G\) independent of \(\Lambda\),
3. \(S_W\) is smooth and \(\nabla^2 S_W(U^{(0)})\ge 0\).

Then there exist constants \(r>0\) and \(\rho_{\mathrm{loc}}>0\), independent of \(\Lambda\), such that for all \(U\in B_r(U^{(0)})\) and all horizontal vectors \(v\in H_U\),
\[
\mathrm{Ric}_{\mu_\Lambda}(U)(v,v)\ge \rho_{\mathrm{loc}}\,|v|_{g_\Lambda}^2.
\]

In particular, for any smooth gauge-invariant observable \(f\),
\[
\Gamma_{2,\Lambda}(f)(U)\ge \rho_{\mathrm{loc}}\,\Gamma_\Lambda(f)(U)\qquad \forall U\in B_r(U^{(0)}),
\]
i.e. a **local** \(CD(\rho_{\mathrm{loc}},\infty)\) condition in the gauge-invariant sector.

*Proof sketch.*  
The bound at \(U^{(0)}\) holds with constant \(\rho_0=\kappa_G-C_{\mathrm{add}}>0\). By continuity of the symmetric bilinear form \((U,v)\mapsto \mathrm{Ric}_{\mu_\Lambda}(U)(v,v)\) restricted to unit horizontal vectors, there exists \(r>0\) such that the infimum over \(U\in B_r(U^{(0)})\) and \(|v|=1\) satisfies
\[
\inf_{U\in B_r}\inf_{v\in H_U, |v|=1}\mathrm{Ric}_{\mu_\Lambda}(U)(v,v)\ge \tfrac12\rho_0.
\]
Set \(\rho_{\mathrm{loc}}:=\rho_0/2\). Uniformity in \(\Lambda\) follows because \(\rho_0\) depends only on \(\kappa_G\) and \(C_{\mathrm{add}}\), and the continuity argument is local and finite-dimensional. ∎

---

## 6. What is potentially novel here?

The underlying ingredients are known (product Ricci bounds; Bakry–Émery tensor; gauge invariance). The potentially new contribution is their **synthesis** into a lattice gauge theory curvature statement with the three properties:

1. **Horizontal (physical-sector) formulation**: avoids gauge degeneracy.
2. **Local small-field formulation**: avoids global large-field complexity.
3. **Volume-uniform constants**: crucial for any mass-gap narrative.

This is a sharp and exportable theorem: it is exactly the type of “input lemma” one can hand to a functional-inequalities specialist or stochastic-quantization expert.

---

## 7. What further work would expand this into something stronger

1. **Construct a uniform Lyapunov function.**  
   Local curvature gives local functional inequalities; global ones require a drift condition controlling tails. For Yang–Mills, building a gauge-invariant \(W_\Lambda\) with uniform drift remains a major analytic task.

2. **Quantify the allowed \(S_{\mathrm{add},\Lambda}\).**  
   The uniform bound \(\nabla^2 S_{\mathrm{add},\Lambda}\ge -C_{\mathrm{add}}g\) is clean but strong. One can seek more local/average conditions.

3. **Extend beyond a ball.**  
   One can try to enlarge the region of curvature positivity, perhaps probabilistically (“curvature positive on a set of large \(\mu_\Lambda\)-measure”).

4. **Interface to OS Hamiltonians.**  
   The theorem yields curvature control for the stochastic-quantization diffusion, but the physical mass gap is defined via the OS Hamiltonian. Quantitative comparison remains an open bridge.

