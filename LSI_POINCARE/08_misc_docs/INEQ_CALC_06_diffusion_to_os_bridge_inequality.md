---
title: "Diffusion → OS Bridge Inequality"
subtitle: "A one-step Dirichlet comparison as the missing theorem"
status: "Open interface (precise target statement + proof plan)"
date: "2025-12-31"
---

# 0. Why this matters

Two spectral gaps appear in lattice gauge theory:

1. **Configuration diffusion gap** (Poincaré/LSI constant) controlling relaxation of Langevin dynamics on $M_\Lambda$.
2. **OS mass gap** of the Hamiltonian reconstructed from reflection positivity and Euclidean time translations.

A single explicit inequality comparing one time-step of the transfer operator to a diffusion Dirichlet form
would bridge them. This note isolates that inequality.

---

# 1. Two semigroups, two quadratic forms

Assume finite-volume OS reconstruction holds:

- a Hilbert space $\mathcal H_\Lambda$ with vacuum $\Omega_\Lambda$,
- a transfer operator $T_\Lambda=e^{-aH_\Lambda}$ acting as Euclidean time translation.

Let $\mathcal A_+$ be the positive-time observable algebra (time-zero-supported suffices).

For $F\in\mathcal A_+$ with $\langle F,\Omega_\Lambda\rangle=0$ and $\|F\|_{\mathcal H_\Lambda}=1$, define
\[
\mathcal Q_\Lambda(F):=\langle F,(I-T_\Lambda)F\rangle_{\mathcal H_\Lambda}.
\tag{1.1}
\]

On the configuration side, let $L_\Lambda$ be the Langevin generator on $M_\Lambda$ with invariant measure $\mu_\Lambda$,
with Dirichlet form
\[
\mathcal E_{\mathrm{conf}}(f,f):=\int_{M_\Lambda}|\nabla f|^2\,d\mu_\Lambda.
\tag{1.2}
\]
Let $\mathcal E_{\mathrm{conf},\partial}$ denote a boundary-restricted version (depending on the chosen slab disintegration).

---

# 2. The bridge inequality (target)

## Hypothesis 2.1 (One-step bridge)

There exists a constant $c_\star>0$ independent of $\Lambda$ such that for all normalized mean-zero $F\in\mathcal A_+$,
\[
\boxed{
\langle F,(I-T_\Lambda)F\rangle_{\mathcal H_\Lambda}
\ \ge\
c_\star\,\mathcal E_{\mathrm{conf},\partial}(F,F).
}
\tag{2.1}
\]

Interpretation: one Euclidean time step has at least a fixed fraction of the dissipativity
of the configuration diffusion at the boundary.

---

# 3. Consequence: diffusion gap transfers to OS mass gap

Let $\lambda_{\mathrm{conf}}$ be the configuration diffusion spectral gap:
\[
\mathrm{Var}_{\mu_\Lambda}(f)\le \frac{1}{\lambda_{\mathrm{conf}}}\mathcal E_{\mathrm{conf}}(f,f).
\]

If $\lambda_{\mathrm{conf}}\ge \lambda_\star>0$ uniformly in $\Lambda$, and if (2.1) holds, then
\[
1-e^{-a\Delta_\Lambda}
=
\inf_{\substack{F\in\mathcal A_+\\ \|F\|=1,\ \langle F,\Omega\rangle=0}}
\langle F,(I-T_\Lambda)F\rangle
\ \ge\
c_\star\lambda_\star,
\]
and hence (using $1-e^{-x}\le x$),
\[
\boxed{
\Delta_\Lambda \ \ge\ \frac{c_\star}{a}\,\lambda_\star.
}
\tag{3.1}
\]

Thus a *uniform diffusion gap* implies a *uniform OS mass gap* once the bridge constant $c_\star$ is controlled.

---

# 4. Proof strategy sketch: slab locality across the reflection plane

A plausible route to (2.1) uses only locality and reflection positivity:

1. **Disintegrate the slab measure.**  
   Condition on boundary configurations at times $0$ and $a$, integrate over the interior slab.

2. **Identify the effective boundary kernel $K_a$.**  
   This is a Markov kernel from boundary-at-time-0 to boundary-at-time-$a$ induced by the slab.

3. **Compare quadratic forms.**  
   Show the quadratic form induced by $I-K_a$ dominates a boundary gradient energy:
   \[
   \langle f,(I-K_a)f\rangle_{L^2(\nu)}
   \ \ge\
   c_\star\,\mathcal E_{\mathrm{conf},\partial}(f,f).
   \]

4. **Lift to OS Hilbert space.**  
   Use reflection positivity to identify the OS quadratic form with a boundary kernel quadratic form.

The locality heuristic: only plaquettes crossing the reflection plane contribute to the one-step energy.

---

# 5. Relation to the cone–hyperbolicity calculus

In the calculus language:

- The transfer step $(I-T_\Lambda)$ defines a quadratic form on $\mathfrak A_+$.
- The boundary diffusion Dirichlet form is another quadratic form.
- The bridge inequality is a **cone-dominance statement**: the transfer quadratic form dominates the diffusion quadratic form on the admissible cone of test vectors.

If proved, (2.1) becomes the missing structural theorem that turns diffusion certificates into OS mass gaps.
