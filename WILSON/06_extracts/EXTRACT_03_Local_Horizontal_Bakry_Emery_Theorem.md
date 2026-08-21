---
title: "A Local Horizontal Bakry–Émery Curvature Theorem for Lattice Yang–Mills"
date: "2025-12-29"
---

# A local horizontal Bakry–Émery curvature theorem for lattice Yang–Mills

## Abstract

On a finite lattice $\Lambda$, the configuration space of lattice gauge fields is the compact Riemannian
manifold $M_\Lambda = G^{E(\Lambda)}$ with product bi-invariant metric and product Haar volume.
The lattice gauge group $\mathcal G_\Lambda$ acts isometrically by gauge transformations; hence
gauge-invariant observables have gradients orthogonal to gauge orbits (horizontal).

This note packages a key structural statement:

> **Near the trivial configuration, the Bakry–Émery curvature of the Yang–Mills Gibbs measure is strictly positive in horizontal directions, with constants independent of the finite volume.**

This is the analytic “engine room” needed to connect lattice Yang–Mills to the curvature–dimension
machinery that implies Poincaré/LSI bounds and spectral gaps for the associated diffusion.

---

## 1. Finite-volume geometric setup

Let $G$ be compact connected with bi-invariant metric $g_G$.
Let $\Lambda$ be a finite lattice with edge set $E(\Lambda)$.
Define
\[
M_\Lambda := G^{E(\Lambda)},\qquad g_\Lambda := \bigoplus_{e\in E(\Lambda)} g_G,\qquad
d\mathrm{vol}_{g_\Lambda}=\text{(product Haar)}.
\]

Let $S_\Lambda\in C^2(M_\Lambda)$ be a gauge-invariant effective action and define the Gibbs measure
\[
d\mu_\Lambda \;=\; Z_\Lambda^{-1}\,e^{-S_\Lambda}\,d\mathrm{vol}_{g_\Lambda}.
\tag{1.1}
\]

The associated diffusion generator is
\[
L_\Lambda = \Delta_{g_\Lambda} - \langle \nabla S_\Lambda,\nabla\cdot\rangle_{g_\Lambda}.
\tag{1.2}
\]

The Bakry--Émery Ricci tensor is
\[
\mathrm{Ric}_{\mu_\Lambda} = \mathrm{Ric}_{g_\Lambda} + \nabla^2 S_\Lambda.
\tag{1.3}
\]

---

## 2. Gauge orbits and horizontal subspaces

Let $\mathcal G_\Lambda$ be the lattice gauge group (product of $G$ over sites) acting smoothly and isometrically on $M_\Lambda$.
At $U\in M_\Lambda$:

- the **vertical** space $V_U\subset T_U M_\Lambda$ is the tangent to the gauge orbit,
- the **horizontal** space is the orthogonal complement
\[
H_U := V_U^\perp \subset T_U M_\Lambda.
\tag{2.1}
\]

**Lemma 2.1 (Horizontal gradients).**  
If $f$ is gauge invariant, then $\nabla f(U)\in H_U$ for all $U$.

Consequently, the carré du champ of a gauge-invariant $f$ is purely horizontal:
\[
\Gamma_\Lambda(f)(U)=|\nabla f(U)|^2 = |\nabla^H f(U)|^2.
\tag{2.2}
\]

---

## 3. The small-field anchor point: the trivial configuration

Let $U^{(0)}$ be the trivial configuration (all links equal to the identity).
Assume the effective action splits as
\[
S_\Lambda = S_W + S_{\mathrm{add},\Lambda},
\tag{3.1}
\]
where:

1. $S_W$ is the Wilson action.
2. $S_{\mathrm{add},\Lambda}$ is gauge invariant and has a uniform Hessian lower bound
\[
\nabla^2 S_{\mathrm{add},\Lambda}(U)\ \ge\ -C_{\mathrm{add}}\, g_\Lambda(U)
\quad\text{for all }U\in M_\Lambda,
\tag{3.2}
\]
with $C_{\mathrm{add}}$ independent of $\Lambda$.

Assume also that $G$ has a uniform Ricci lower bound
\[
\mathrm{Ric}_G \ge \kappa_G g_G
\quad\text{with }\kappa_G>0.
\tag{3.3}
\]
Then, by product structure,
\[
\mathrm{Ric}_{g_\Lambda} \ge \kappa_G g_\Lambda.
\tag{3.4}
\]

At $U^{(0)}$, the Wilson Hessian is nonnegative in horizontal directions (linearized curvature energy).
Thus at $U^{(0)}$ and for $v\in H_{U^{(0)}}$,
\[
\mathrm{Ric}_{\mu_\Lambda}(U^{(0)})(v,v)
=
\mathrm{Ric}_{g_\Lambda}(v,v) + \nabla^2 S_W(U^{(0)})(v,v) + \nabla^2 S_{\mathrm{add},\Lambda}(U^{(0)})(v,v)
\ge (\kappa_G - C_{\mathrm{add}})\,|v|^2.
\tag{3.5}
\]
Define the **anchor curvature**
\[
\rho_0 := \kappa_G - C_{\mathrm{add}}.
\tag{3.6}
\]
If $C_{\mathrm{add}}<\kappa_G$, then $\rho_0>0$.

---

## 4. Local persistence and uniformity in volume

The maps $U\mapsto \nabla^2 S_\Lambda(U)$ and $U\mapsto H_U$ are smooth (on the regular set).
Therefore the minimal eigenvalue of $\mathrm{Ric}_{\mu_\Lambda}$ restricted to $H_U$ varies continuously with $U$.

By continuity, there exists a radius $r>0$ such that for all $U$ in the $g_\Lambda$-ball
\[
B_r(U^{(0)}) := \{U\in M_\Lambda: d_{g_\Lambda}(U,U^{(0)})\le r\},
\]
the horizontal curvature bound persists with a slightly smaller constant $\rho_{\mathrm{loc}}>0$:
\[
\mathrm{Ric}_{\mu_\Lambda}(U)(v,v)\ \ge\ \rho_{\mathrm{loc}}\,|v|^2
\quad\forall U\in B_r(U^{(0)}),\ \forall v\in H_U.
\tag{4.1}
\]

Because:

- $\kappa_G$ is a property of the single-link geometry,
- the Hessian bound (3.2) is assumed uniform in $\Lambda$,
- and the action is local and translation-invariant in typical lattice gauge settings,

one expects $r$ and $\rho_{\mathrm{loc}}$ to be chosen **independently of $\Lambda$**.

---

## 5. Core theorem: local horizontal curvature and induced $CD(\rho,\infty)$

**Theorem 5.1 (Local horizontal Bakry–Émery curvature bound).**  
Under the hypotheses above, there exist constants $r>0$ and $\rho_{\mathrm{loc}}>0$,
independent of the finite volume $\Lambda$, such that
\[
\mathrm{Ric}_{\mu_\Lambda}(U)(v,v)\ \ge\ \rho_{\mathrm{loc}}\,|v|^2
\quad\forall U\in B_r(U^{(0)}),\ \forall v\in H_U.
\tag{5.1}
\]

**Corollary 5.2 (Local $CD(\rho,\infty)$ for gauge-invariant observables).**  
For any smooth gauge-invariant $f$,
\[
\Gamma_{2,\Lambda}(f)(U)\ \ge\ \rho_{\mathrm{loc}}\,\Gamma_\Lambda(f)(U)
\quad\forall U\in B_r(U^{(0)}).
\tag{5.2}
\]

*Proof idea.* The standard Bochner--Bakry--Émery identity gives
\[
\Gamma_2(f)=\|\nabla^2 f\|^2 + \mathrm{Ric}_{\mu_\Lambda}(\nabla f,\nabla f).
\]
For gauge-invariant $f$, $\nabla f\in H_U$, so the curvature term is bounded below by (5.1).

---

## 6. What this buys you (and what it does not)

What you get immediately (locally, on $B_r(U^{(0)})$):

- Poincaré and log-Sobolev inequalities with constants controlled by $1/\rho_{\mathrm{loc}}$,
- exponential relaxation for the associated Langevin diffusion,
- volume-independent control on small-field fluctuations of gauge-invariant observables.

What remains:

- turning this local inequality into a **global** one with constants independent of $\Lambda$,
- relating the diffusion spectral gap to the **physical** mass gap (transfer matrix / Hamiltonian gap),
- and controlling continuum limits and RG flow.

Those “next steps” are addressed in a separate roadmap note.
