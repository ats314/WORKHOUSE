---
title: "Selection F — OS Reconstruction vs Configuration Diffusion: the Bridge Inequality"
date: "2025-12-28"
---

# Abstract

The project contains a sharp conceptual move: it separates two *different* spectral gaps that are often conflated.

1. The **configuration diffusion gap** (Poincaré/LSI constant) controls relaxation of a Langevin-type Markov process on the configuration manifold.
2. The **Osterwalder–Schrader (OS) mass gap** is a spectral gap of the Hamiltonian reconstructed from reflection positivity and Euclidean time translations.

A single, explicit *one-step comparison inequality* would bridge them. This note isolates that inequality and shows how it would imply a volume-uniform mass gap once a volume-uniform Poincaré constant is available.

# 1. Two semigroups, two gaps

Let $\Lambda$ be a finite lattice with a chosen reflection plane and Euclidean time direction.
Let $\mu_\Lambda$ be the Euclidean Gibbs measure on configurations.

## 1.1 Configuration diffusion

Let $L_\Lambda$ be the reversible diffusion generator on $M_\Lambda$ with invariant measure $\mu_\Lambda$:
\[
L_\Lambda=\Delta-\langle \nabla S_\Lambda,\nabla(\cdot)\rangle.
\]
Its spectral gap $\lambda_{\mathrm{conf}}$ is the best constant in the Poincaré inequality
\[
\mathrm{Var}_{\mu_\Lambda}(f)\ \le\ \frac{1}{\lambda_{\mathrm{conf}}}\int \|\nabla f\|^2\,d\mu_\Lambda.
\]

## 1.2 OS reconstruction and transfer matrix

Assume reflection positivity, Euclidean invariance, and the OS axioms so that one reconstructs a Hilbert space $\mathcal H_\Lambda$,
a vacuum vector $\Omega_\Lambda$, and a self-adjoint Hamiltonian $H_\Lambda\ge0$ generating Euclidean time translations.
Let $a>0$ be the lattice time spacing and define the transfer operator
\[
T_\Lambda := e^{-aH_\Lambda}.
\]
The OS **mass gap** is
\[
\Delta_\Lambda := \inf\big(\mathrm{spec}(H_\Lambda)\setminus\{0\}\big).
\]

# 2. The bridge inequality (one-step Dirichlet comparison)

Let $\mathcal A_+$ denote the algebra of observables supported on the positive-time half-lattice (the OS “positive-time” algebra).
For $F\in\mathcal A_+$ with $\langle F,\Omega_\Lambda\rangle_{\mathcal H_\Lambda}=0$ and $\|F\|_{\mathcal H_\Lambda}=1$, define the one-step quadratic form
\[
\mathcal Q_\Lambda(F) := \langle F, (I-T_\Lambda)F\rangle_{\mathcal H_\Lambda}.
\]

On the other hand, for such $F$ viewed as a function of the boundary configuration, define a *configuration-space Dirichlet form*
$\mathcal E_{\mathrm{conf},\partial}(F,F)$ built from the boundary diffusion (or from the full diffusion restricted to $\mathcal A_+$, depending on implementation).

## Hypothesis 2.1 (Bridge inequality)

There exists a constant $c_\star>0$ independent of $\Lambda$ such that for all normalized mean-zero $F\in\mathcal A_+$,
\[
\langle F,(I-T_\Lambda)F\rangle_{\mathcal H_\Lambda}
\ \ge\
c_\star\,\mathcal E_{\mathrm{conf},\partial}(F,F).
\tag{$\star$}
\]

Interpretation: one Euclidean time step has at least as much dissipativity as a fixed fraction of the configuration diffusion energy.

# 3. Why ($\star$) would imply a volume-uniform mass gap

Assume:

- a volume-uniform configuration diffusion gap $\lambda_{\mathrm{conf}}\ge \lambda_\star>0$ (from curvature + Lyapunov),
- and the bridge inequality ($\star$) with volume-uniform $c_\star$.

## Proposition 3.1 (Bridge $\Rightarrow$ gap transfer)

Then the OS mass gap satisfies
\[
\Delta_\Lambda \ \ge\ \frac{c_\star}{a}\,\lambda_\star
\]
(up to the standard discrete-time conversion between $I-T$ and $H=-a^{-1}\log T$; the inequality above is the clean first-order bound).

### Proof sketch

By the variational principle,
\[
1-e^{-a\Delta_\Lambda}
=
\inf_{\substack{F\in\mathcal A_+\\ \|F\|=1,\ \langle F,\Omega\rangle=0}}
\langle F,(I-T_\Lambda)F\rangle.
\]
Apply ($\star$) to obtain
\[
1-e^{-a\Delta_\Lambda}
\ \ge\ c_\star\,
\inf_{\|F\|=1,\langle F,\Omega\rangle=0}\mathcal E_{\mathrm{conf},\partial}(F,F).
\]
The infimum of the Dirichlet form over unit vectors is the boundary diffusion gap, which is controlled below by $\lambda_\star$
(if boundary and bulk gaps are linked by standard comparison estimates on finite-volume reversible dynamics).
Thus $1-e^{-a\Delta_\Lambda}\ge c_\star \lambda_\star$, and hence $\Delta_\Lambda\ge \frac{c_\star}{a}\lambda_\star$ after elementary inequalities. ∎

# 4. How one might prove ($\star$): locality across the reflection plane

The project’s key idea is that **only plaquettes crossing the reflection plane** participate in the OS one-step energy.

Heuristically:

- $T_\Lambda$ is built from integrating out a single time-slab.
- The action is a sum of plaquette-local terms.
- Therefore $(I-T_\Lambda)$ should be comparable to a sum of *local* boundary Dirichlet forms coming from those crossing plaquettes.

A plausible proof structure:

1. **Disintegrate the slab measure**:
   condition on the boundary configurations at times $0$ and $a$, integrate over the interior of the slab.
2. **Identify the effective boundary kernel** $K_a$ (a Markov kernel from time $0$ boundary to time $a$ boundary).
3. Show that the quadratic form induced by $I-K_a$ dominates a boundary gradient energy.
4. Lift that domination to the OS Hilbert space quadratic form $\langle F,(I-T)F\rangle$ using reflection positivity.

# 5. Why this is genuinely new

Classical mass gap arguments (cluster expansions, strong coupling, reflection positivity estimates) do not typically route through a *configuration diffusion gap*.
Here the ambition is more geometric:

\[
\text{local horizontal curvature}
\ \Rightarrow\
\text{volume-uniform diffusion gap}
\ \overset{(\star)}{\Rightarrow}\
\text{OS mass gap}.
\]

If ($\star$) can be proved with a coupling/locality argument, it becomes a powerful template for other lattice QFTs where a diffusion exists but
OS reconstruction is hard to access directly.

# 6. Next technical targets

- Give a precise definition of $\mathcal E_{\mathrm{conf},\partial}$ and prove its comparison to the bulk Dirichlet form uniformly in volume.
- Construct the slab kernel $K_a$ explicitly and compute/estimate its coarse Ricci curvature (Ollivier–Ricci) to obtain a direct spectral gap.
- Prove ($\star$) by bounding the Radon–Nikodym derivative between the slab-induced boundary measure and the boundary diffusion measure.

