---
title: "Matrix Hinge → Functional Inequalities → Kernel Decay → OS Mass Gap"
subtitle: "A closed constructive pipeline at fixed cutoff"
status: "Paper-ready architecture (proved modules + explicit open interfaces)"
date: "2025-12-31"
---

# 0. Goal and setting

Fix a finite lattice region $\Lambda$ and compact gauge group $G=\mathrm{SU}(N)$.
Let $M_\Lambda=G^{E(\Lambda)}$ and $\mu_\Lambda\propto e^{-S_\Lambda}d\mathrm{vol}$ be the Wilson measure.

The objective at **fixed cutoff** is:

1. **Exponential clustering** of Euclidean correlations, and hence
2. a **positive mass gap** for the OS reconstructed Hamiltonian.

This note isolates a modular chain of implications that reduces the workload
to a small set of explicit “interfaces” (places where new lemmas are required).

---

# 1. Local matrix coercivity: the hinge inequality

## 1.1 Bakry–Émery curvature matrix

For the Langevin generator
\[
L=\Delta-\langle\nabla S,\nabla(\cdot)\rangle,
\]
define
\[
\mathrm{Ric}_\mu := \mathrm{Ric}_g + \nabla^2 S.
\]

A pointwise lower bound
\[
\mathrm{Ric}_\mu(U)\succeq \rho\,\mathrm{Id}
\]
on a region $\Omega$ implies a local $CD(\rho,\infty)$ inequality:
\[
\Gamma_2(f)\ge \rho\,\Gamma(f)\quad\text{on }\Omega.
\]

## 1.2 Matrix hinge form (gauge theory)

Near the vacuum (or on a small-field good set $K_\Lambda(r)$) the project’s key move is to keep coercivity **matrix-valued**:
\[
\mathrm{Ric}_\mu(U)\ \succeq\ m_H^2\,\mathrm{Id} + \alpha\,d_1^\*d_1 - \mathrm{Err}(r),
\qquad U\in K_\Lambda(r),
\]
where:

- $m_H^2>0$ is the “Haar mass” curvature contribution,
- $\alpha d_1^\*d_1$ is the lattice Maxwell stiffness operator on $1$-cochains,
- $\mathrm{Err}(r)$ is a controllable remainder small for small $r$.

This is the *local coercivity module*.

---

# 2. Global functional inequalities via Lyapunov drift

Local $CD(\rho,\infty)$ on $K_\Lambda(r)$ is not enough: $\mu_\Lambda$ lives on all of $M_\Lambda$.

A Lyapunov function $W\ge 1$ and constants $\alpha>0,\beta\ge 0$ are used to control excursions:
\[
LW \le -\alpha W + \beta\,\mathbf 1_{K_\Lambda(r)}.
\]

A general local-to-global engine then yields:

- global **Poincaré** inequality (spectral gap for $-L$),
- and, under stronger inputs, global **log-Sobolev** inequality (hypercontractivity).

All constants can be made volume-uniform if the drift constants are volume-uniform
and the local geometry on the core is uniform.

A clean, explicit Lyapunov candidate is the smooth fundamental-character proxy
$\overline V_\Lambda=1+\overline z_\Lambda$ (see the separate lemma note).

---

# 3. Helffer–Sjöstrand covariance representation

Assuming a Poincaré/LSI framework and solvability of the Poisson equation on mean-zero functions,
one obtains a covariance formula of the form
\[
\mathrm{Cov}_{\mu_\Lambda}(F,G)
=
\int \left\langle \nabla F,\ \big(\mathcal L^{(1)}\big)^{-1}\nabla G\right\rangle\,d\mu_\Lambda,
\]
where $\mathcal L^{(1)}$ is a drifted connection Laplacian on vector fields:
\[
\mathcal L^{(1)} = ((-L)\otimes I)+\mathrm{Ric}_\mu.
\]

If $\mathrm{Ric}_\mu\succeq M$ on the good set, then
\[
(\mathcal L^{(1)})^{-1}\preceq M^{-1}
\quad\text{(as quadratic forms on the supported sector)}.
\]

Thus covariance control reduces to **deterministic inverse bounds** for a finite-range operator $M$.

---

# 4. Deterministic inverse decay: Combes–Thomas / Davies

For a positive finite-range operator on a graph,
\[
M = m^2 I + \alpha\,d_1^\*d_1
\]
acting on link fields, Combes–Thomas / Davies arguments yield exponential off-diagonal decay:
\[
\|(M^{-1})_{xy}\| \ \le\ C\,e^{-\eta\,\mathrm{dist}(x,y)},
\]
with explicit $\eta=\eta(m^2,\alpha,\text{geometry})$.

This produces exponential clustering bounds on $\mathrm{Cov}_{\mu_\Lambda}(F,G)$ for local observables.

---

# 5. Conditional → unconditional: localization + typicality

The hinge inequality (and hence the Maxwell dominator) is often proved only on a good set $K_\Lambda(r)$.

A localization algebra gives an exact decomposition:
\[
\mathrm{Cov}_\mu(F,G)
=
\mu(K)\,\mathrm{Cov}_{\mu_K}(F,G)
+\mu(K^c)\,\mathrm{Cov}_{\mu_{K^c}}(F,G)
+\mu(K)\mu(K^c)\,\Delta_K F\,\Delta_K G.
\]

If typicality gives $\mu(K^c)\le e^{-c|P(\Lambda)|}$, then conditional clustering on $K$
upgrades to unconditional clustering.

---

# 6. Reflection positivity and OS gap extraction

For the Wilson measure, finite-volume **reflection positivity** implies OS reconstruction:
a Hilbert space $\mathcal H$, transfer operator $T=e^{-aH}$, and Hamiltonian $H\ge 0$.

A standard spectral lemma: exponential decay of Euclidean-time correlations implies a mass gap:
\[
|\langle \Omega,\,F\,T^n\,F\,\Omega\rangle - \langle\Omega,F\Omega\rangle^2|
\le C e^{-mn}
\quad\Rightarrow\quad
\mathrm{gap}(H)\ge m/a.
\]

---

# 7. The explicit open interfaces (where new work is needed)

The pipeline is “closed” modulo a small number of interfaces:

1. **Hinge lower bound on a good set:** $\mathrm{Ric}_\mu\succeq m^2I+\alpha d_1^\*d_1$.
2. **Volume-uniform Lyapunov drift:** $LW\le -\alpha W+\beta\mathbf 1_K$ with $\alpha,\beta$ independent of $|\Lambda|$.
3. **Typicality of the good set:** $\mu(K^c)$ exponentially small in $|P(\Lambda)|$.
4. **Diffusion-to-OS bridge (optional but powerful):** a one-step quadratic form comparison linking diffusion contraction to transfer contraction.

Everything else is either classical or already modularized.

This is the project’s “constructive fixed-cutoff mass gap” spine.
