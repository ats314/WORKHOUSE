---
title: "The OS/Configuration Gap Fault Line and a One-Step Bridge (Extracted + Proposed Lemmas)"
author: "Project extraction (Parts 16–18, 20) + chat-derived lemmas"
date: "2025-12-28"
---

## Scope and status

This note extracts the project’s **most conceptually sharp reduction**:

- the configuration-space diffusion spectral gap and the OS Hamiltonian spectral gap are *not the same object*;
- nonetheless, Part 18 isolates a **single, finite-volume inequality** that would bridge them.

I then append two *proposed* lemmas (C.2–C.3) that provide a concrete route to proving the bridge
for the Wilson action, while keeping all objects finite-dimensional.

---

## 1. Two different semigroups, two different gaps

### Configuration-space diffusion (fictitious time)

On a finite spatial lattice $\Lambda$ at fixed spacing $a$:

- configuration manifold: $M_\Lambda = G^{E(\Lambda)}$,
- Gibbs measure: $d\mu_{\Lambda,a}\propto e^{-S_{\Lambda,a}}\,d\mathrm{vol}$,
- generator on gauge-invariants: $L^{\mathrm{inv}}_{\Lambda,a}$.

The **configuration spectral gap** is
\[
\lambda^{\mathrm{conf}}_1(\Lambda,a)
:= \inf\Big\{\frac{\mathcal E_{\Lambda,a}(f,f)}{\mathrm{Var}_{\mu_{\Lambda,a}}(f)}:
f\in \mathcal A^{\mathrm{inv}}_\Lambda,\ f\not\equiv \mathrm{const}\Big\},
\]
where $\mathcal E_{\Lambda,a}(f,f)=\int \Gamma(f)\,d\mu_{\Lambda,a}$ is the Dirichlet form.

### OS Hamiltonian (Euclidean time)

From the full **space–time** lattice Euclidean measure (reflection positive),
OS reconstruction produces a Hilbert space $\mathcal H_{\Lambda,a}$ and a positive
self-adjoint Hamiltonian $H_{\Lambda,a}$ with semigroup $e^{-tH_{\Lambda,a}}$.

The **OS mass gap** is
\[
\Delta_{\Lambda,a}
:= \inf\big(\sigma(H_{\Lambda,a})\setminus\{0\}\big).
\]

These objects live in different Hilbert spaces and encode different dynamics.
There is no automatic intertwining.

---

## 2. The “one-step bridge” formulation (Part 18)

Part 18 introduces a time-slice transfer operator $T_{\Lambda,a}$ acting on
time-slice observables (functions on $M_\Lambda$) induced by integrating out one Euclidean time step.

Define the OS quadratic form
\[
\mathcal Q_{\Lambda,a}(f,f) := \langle f,\ (I-T_{\Lambda,a})f\rangle_{L^2(\mu_{\Lambda,a})}.
\]

### Hypothesis/Target inequality (the missing bridge)

A sufficient comparison statement is:

\[
\boxed{
\mathcal Q_{\Lambda,a}(f,f)\ \ge\ c\ \mathcal E_{\Lambda,a}(f,f)
\qquad\forall f\in \mathcal A^{\mathrm{inv}}_\Lambda
}
\tag{$\star$}
\]

with a constant $c>0$ independent of $\Lambda$ (and ideally stable in $a$ under scaling).

### Theorem 2.1 (Extracted: “bridge + Poincaré ⇒ OS gap”)

Assume:

1. a Poincaré inequality in configuration space:
   $\mathrm{Var}_{\mu_{\Lambda,a}}(f)\le C_P\,\mathcal E_{\Lambda,a}(f,f)$
   (equivalently $\lambda_1^{\mathrm{conf}}(\Lambda,a)\ge 1/C_P$);
2. the one-step bridge $(\star)$ with constant $c$.

Then the OS mass gap satisfies a finite-volume lower bound
\[
\Delta_{\Lambda,a} \ \ge\ c\,\lambda_1^{\mathrm{conf}}(\Lambda,a).
\]

*Interpretation.* The entire OS-to-diffusion comparison problem is compressed into $(\star)$.

---

## 3. Proposed Lemma C.2: Wilson-action one-step expansion (finite lattice)

**Status:** proposed (not claimed proved in the current draft).

### Setup

Work on a $(d+1)$-dimensional space–time lattice with time step $a_t$ (possibly $a_t=a$),
and spatial slice $\Lambda$.
Let the space–time action be the Wilson action $S_W$ (plus any local gauge-invariant add-ons
satisfying a uniform Hessian lower bound).

Let $T_{\Lambda,a_t}$ be the reflection-positive one-step transfer operator
acting on time-slice observables $f(M_\Lambda)\to f(M_\Lambda)$.

### Lemma C.2 (Wilson one-step Dirichlet-form expansion; form version)

There exist constants $a_0>0$ and $C<\infty$ (depending on $G$, the plaquette geometry, and local bounds
on the add-on terms, but **not** on $\Lambda$) such that for all $a_t\in(0,a_0)$ and all
gauge-invariant $f\in C^\infty(M_\Lambda)$,
\[
\mathcal Q_{\Lambda,a_t}(f,f)
=
a_t\,\mathcal E_{\Lambda,a_t}(f,f)\ +\ R_{\Lambda,a_t}(f),
\]
where the remainder satisfies the **quadratic error bound**
\[
|R_{\Lambda,a_t}(f)| \ \le\ C\,a_t^2\,
\Big(\mathcal E_{\Lambda,a_t}(f,f) + \|f\|_{L^2(\mu_{\Lambda,a_t})}^2\Big).
\]

*Heuristic proof sketch (what one would make rigorous).*  
The transfer operator kernel is an $a_t$-step Gibbs kernel in Euclidean time. For small $a_t$,
one expects a Trotter-type expansion
\[
T_{\Lambda,a_t} \approx I - a_t\,(-L^{\mathrm{inv}}_{\Lambda,a_t}) + O(a_t^2)
\]
in a suitable quadratic-form topology, with $-L^{\mathrm{inv}}$ the symmetric generator
with Dirichlet form $\mathcal E$.

The proof would be a careful expansion of the time-like plaquette contributions in the Wilson action,
using:

- locality (only time-like plaquettes couple consecutive slices),
- smoothness and bounded geometry of $M_\Lambda$,
- uniform control of third derivatives on the chosen small-field region (or global bounds from compactness),
- and gauge invariance (so only horizontal/physical derivatives matter).

---

## 4. Lemma C.3: Error absorption via the configuration spectral gap

This lemma is clean, general, and is exactly the mechanism you want referees to see.

### Lemma C.3 (Error absorption)

Let $\mu$ be a probability measure on a compact manifold $M$, and let
$\mathcal E$ be a Dirichlet form satisfying a Poincaré inequality with spectral gap $\lambda>0$:
\[
\mathrm{Var}_\mu(f)\le \frac{1}{\lambda}\,\mathcal E(f,f).
\]

Suppose a quadratic form $\mathcal Q$ satisfies the **defective comparison**
\[
\mathcal Q(f,f)\ \ge\ c\,\mathcal E(f,f)\ -\ \varepsilon\,\mathrm{Var}_\mu(f)
\qquad\forall f\in\mathcal D,
\]
for some $c>0$ and $\varepsilon\ge 0$.

Then
\[
\mathcal Q(f,f)\ \ge\ \Big(c - \frac{\varepsilon}{\lambda}\Big)\,\mathcal E(f,f)
\qquad\forall f\in\mathcal D.
\]

In particular, if $\varepsilon < c\lambda$, then $\mathcal Q\ge c'\mathcal E$ with $c'=c-\varepsilon/\lambda>0$.

*Proof.* By Poincaré, $\mathrm{Var}_\mu(f)\le \mathcal E(f,f)/\lambda$, so
\[
\mathcal Q(f,f)\ge c\,\mathcal E(f,f)-\varepsilon\,\frac{1}{\lambda}\mathcal E(f,f)
=\Big(c-\frac{\varepsilon}{\lambda}\Big)\mathcal E(f,f).
\quad\square
\]

---

## 5. How C.2 + C.3 would prove the bridge $(\star)$

If Lemma C.2 holds, then for small $a_t$:
\[
\mathcal Q_{\Lambda,a_t}(f,f)
\ge a_t\,\mathcal E_{\Lambda,a_t}(f,f)\ -\ C a_t^2\,\|f-\mu(f)\|_{L^2}^2.
\]

But $\|f-\mu(f)\|_{L^2}^2=\mathrm{Var}_\mu(f)\le \mathcal E(f,f)/\lambda^{\mathrm{conf}}_1$,
so Lemma C.3 yields
\[
\mathcal Q_{\Lambda,a_t}(f,f)\ \ge\
\Big(a_t - \frac{C a_t^2}{\lambda_1^{\mathrm{conf}}(\Lambda,a_t)}\Big)\,
\mathcal E_{\Lambda,a_t}(f,f).
\]

Thus, as soon as $\lambda_1^{\mathrm{conf}}(\Lambda,a_t)$ has a volume-uniform positive lower bound
and $a_t$ is small enough in relation to it, we obtain the desired bridge $(\star)$
with an explicit constant.

This turns the OS comparison into a *controlled small-step expansion problem* plus
a *configuration-space gap input*.

---

## 6. Continuum-limit passage (what convergence would be assumed)

A clean way to keep everything airtight is:

1. Prove $(\star)$ uniformly in $\Lambda$ at fixed cutoff $a$.
2. Prove a volume-uniform OS gap at fixed $a$:
   $\Delta_\infty(a):=\liminf_{L\to\infty}\Delta_{\Lambda_L,a}>0$.
3. Assume OS convergence of the continuum limit along a scaling trajectory $a\to 0$
   (tightness of Schwinger functions, existence of a reflection-positive limit).
4. Assume **gap persistence in physical units**:
   \[
   \liminf_{a\to 0}\ \frac{\Delta_\infty(a)}{a}\ >\ 0.
   \]

These are explicit, checkable (if hard) stability hypotheses.
They prevent any reliance on informal infinite-dimensional “Laplacians”.

