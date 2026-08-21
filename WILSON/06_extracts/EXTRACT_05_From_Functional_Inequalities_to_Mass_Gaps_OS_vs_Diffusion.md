---
title: "From Functional Inequalities to Mass Gaps"
subtitle: "A comparison program between stochastic quantization (configuration diffusion) and OS Hamiltonians"
author: "Extracted and restructured from the project draft"
date: "2025-12-28"
---

## 0. Why this module is interesting

The project develops strong tools for the **configuration-space diffusion**
\[
P_t = e^{tL},\qquad L=\Delta_g-\langle\nabla S,\nabla\cdot\rangle,
\]
which is (up to conventions) the generator of **stochastic quantization**.

The **physical mass gap**, however, is defined via the spectrum of a different object:
the Osterwalder–Schrader reconstructed Hamiltonian \(H\) acting on the OS Hilbert space \(\mathcal H\).

These two operators are not the same, and there is no general theorem that a spectral gap for \(-L\) implies a spectral gap for \(H\). Bridging them is one of the most “new-physics-meets-new-analysis” parts of the program.

This module extracts and sharpens the project’s comparison idea into a small set of explicit conjectures and *conditional* lemmas that could become a publishable research direction even if the full Yang–Mills mass-gap goal remains distant.

---

## 1. Two gaps, two worlds

### 1.1 Configuration diffusion gap

Let \((M_\Lambda,g_\Lambda,\mu_\Lambda)\) be a finite-volume lattice gauge model (configuration manifold, metric, Gibbs measure). Let \(L_\Lambda\) be the associated diffusion generator on \(L^2(\mu_\Lambda)\). Restrict to gauge-invariant observables and let \(-L_\Lambda^{\mathrm{inv}}\) have spectral gap
\[
\lambda_1^{\mathrm{conf}}(\Lambda) > 0.
\]

Equivalently, a Poincaré inequality holds:
\[
\mathrm{Var}_{\mu_\Lambda}(f)\le \frac1{\lambda_1^{\mathrm{conf}}(\Lambda)}\int |\nabla f|^2\,d\mu_\Lambda,
\qquad f\in\mathcal A_\Lambda^{\mathrm{inv}}.
\]

### 1.2 OS Hamiltonian gap (finite-volume mass gap)

Assume the Euclidean lattice measure satisfies reflection positivity and the OS axioms. Then OS reconstruction yields a Hilbert space \(\mathcal H_\Lambda\), a vacuum \(\Omega_\Lambda\), and a self-adjoint Hamiltonian \(H_\Lambda\ge 0\). Let its spectral gap be
\[
\Delta_\Lambda := \inf\big(\sigma(H_\Lambda)\cap(0,\infty)\big).
\]
This controls Euclidean-time correlation decay:
\[
\langle \Omega_\Lambda, \mathcal O\, e^{-tH_\Lambda}\,\mathcal O\,\Omega_\Lambda\rangle
= \sum_{n\ge 1}|a_n|^2 e^{-E_n t},
\qquad \Delta_\Lambda = E_1.
\]

---

## 2. The conceptual bridge: stochastic quantization vs Euclidean time

The diffusion semigroup \(e^{tL}\) evolves in an *auxiliary* time (Langevin time). The OS semigroup \(e^{-tH}\) evolves in **Euclidean physical time**.

Nevertheless, both are built from the *same Euclidean action*. This raises an enticing possibility:

> Strong functional inequalities for stochastic quantization might constrain the low-energy spectrum of the OS Hamiltonian.

This is reminiscent of (and potentially connected to):
- Nelson’s ideas about Euclidean field theory,
- the Parisi–Wu stochastic quantization program,
- and Dirichlet-form comparisons in constructive field theory.

But to make it quantitative one needs an inequality comparing two different Dirichlet forms.

---

## 3. A precise finite-volume conjecture

**Conjecture 3.1 (Dirichlet-form comparison for time-slice observables).**  
Let \(\mathcal A_{0,\Lambda}^{\mathrm{inv}}\) be the algebra of gauge-invariant observables supported on a fixed time slice (say \(x_0=0\)). Let
\[
\iota:\mathcal A_{0,\Lambda}^{\mathrm{inv}} \to \mathcal H_\Lambda,
\qquad f\mapsto [f],
\]
be the OS map sending a time-slice observable to its equivalence class in \(\mathcal H_\Lambda\).

There exists a constant \(c>0\), independent of \(\Lambda\), such that
\[
\langle [f], H_\Lambda [f]\rangle_{\mathcal H_\Lambda}
\;\ge\;
c\,\int_{M_\Lambda} |\nabla f|_{g_\Lambda}^2\, d\mu_\Lambda,
\qquad \forall f\in \mathcal A_{0,\Lambda}^{\mathrm{inv}},
\]
after matching normalizations.

Interpretation:
- the OS energy of a time-slice excitation controls the configuration-space Dirichlet energy of the observable.

This is a strong statement; it will likely require additional structure (e.g. transfer matrix representation, locality, or comparison to a Markov chain generator).

---

## 4. A conditional lemma: if you have the comparison, you get a gap transfer

Assume additionally that the OS map \(\iota\) is compatible with variances in the sense that
\[
\|[f]\|_{\mathcal H_\Lambda}^2 = \langle [f],[f]\rangle
\asymp \mathrm{Var}_{\mu_\Lambda}(f)
\]
for a class of centered observables \(f\) (this is plausible for mean-zero time-slice observables under standard OS constructions, but it must be checked carefully).

Then one gets:

**Lemma 4.1 (Gap transfer, conditional).**  
If Conjecture 3.1 holds and \(\|[f]\|^2\simeq \mathrm{Var}_{\mu_\Lambda}(f)\) on a dense class, then
\[
\Delta_\Lambda \;\ge\; c\,\lambda_1^{\mathrm{conf}}(\Lambda)
\]
(up to the same convention constants), hence any volume-uniform lower bound on \(\lambda_1^{\mathrm{conf}}(\Lambda)\) yields a volume-uniform lower bound on \(\Delta_\Lambda\).

*Proof idea.*  
The spectral gap \(\Delta_\Lambda\) can be characterized variationally as
\[
\Delta_\Lambda
=\inf_{\Psi\perp\Omega_\Lambda}\frac{\langle \Psi,H_\Lambda\Psi\rangle}{\|\Psi\|^2}.
\]
Restrict the infimum to the subspace generated by \([f]\) with \(f\in\mathcal A_{0,\Lambda}^{\mathrm{inv}}\), \(f\) centered. Use Conjecture 3.1 in the numerator and the variance equivalence in the denominator, then apply the Poincaré inequality for \(\mu_\Lambda\). ∎

This lemma is simple but important: it isolates exactly what kind of comparison inequality would turn the project’s configuration-space gap into a physical mass gap.

---

## 5. How might one prove a comparison inequality?

Here are plausible routes, each requiring serious work.

### 5.1 Transfer matrix / heat-bath interpretation

If one can represent the time-slice dynamics by a Markov kernel \(K\) whose Dirichlet form is comparable to the diffusion Dirichlet form, and if the transfer matrix \(T=e^{-aH}\) is comparable to \(K\) on the OS Hilbert space, then \(H\) inherits a spectral gap.

This resembles:
- comparison of Metropolis/heat-bath chains with Langevin diffusions,
- spectral comparison theorems in Markov chain theory.

### 5.2 Reflection positivity + hypercontractivity

Log-Sobolev inequalities yield hypercontractivity for \(e^{tL}\). Reflection positivity yields positivity of \(e^{-tH}\). One can dream of a “mixed” inequality linking the two via common Euclidean correlation functionals, but this is currently speculative.

### 5.3 Stochastic quantization → Schwinger functions control

Stochastic quantization defines a Markov process whose stationary measure is the Euclidean field measure. If one can show that the process has a uniform mixing rate in Langevin time *and* that its finite-time distributions approximate the Euclidean-time Schwinger functions in a controlled way, then Euclidean-time decay might follow.

This is exactly where new theory could emerge: a quantitative bridge between auxiliary-time mixing and physical-time mass gaps.

---

## 6. Why this is worth extracting as “exciting work”

Even if one never closes the full Yang–Mills mass-gap proof, a careful investigation of the OS-vs-diffusion gap comparison would touch multiple deep areas:

- Dirichlet forms and Markov semigroups,
- reflection positivity and constructive QFT,
- stochastic quantization,
- functional inequalities and curvature methods.

It is “new theory adjacent”: you are trying to connect two *legitimate*, well-defined notions of spectral gap that live in different Hilbert spaces but arise from the same Euclidean action.

---

## 7. Concrete next steps

1. **Define the comparison map precisely.**  
   Write down the OS Hilbert space inner product for time-slice observables and compute \(\langle[f],H[f]\rangle\) in terms of Euclidean correlations.

2. **Identify a tractable subclass of observables.**  
   Start with cylindrical observables supported on one or two plaquettes and attempt explicit bounds.

3. **Test on simpler models.**  
   Before Yang–Mills, test the comparison on:
   - massive scalar lattice fields,
   - compact \(U(1)\) in strong coupling (where mass gap is known),
   - \(SU(2)\) in strong coupling.

4. **Look for known comparison principles.**  
   There may be existing inequalities in the literature comparing transfer matrices and Langevin generators in finite dimensions; adapt them.

