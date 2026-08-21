---
title: "EXTRACT 05 — Conjecture D: From Euclidean Spectral Gap to Physical Mass Gap via OS Reconstruction"
project: "SWIM2"
source_files:
  - "SYNTH_CONJ_D_spectral_to_mass.md"
  - "SYNTH_P03_transfer_matrix_gap.md"
  - "SYNTH_P15_dichotomy_theorem.md"
status: "extracted synthesis"
---

# Conjecture D: From Euclidean Spectral Gap to Physical Mass Gap via OS Reconstruction

## Abstract

The project’s “last bridge” is conceptually standard but technically delicate in gauge theory:

> A Euclidean **spectral gap** (Poincaré/LSI constant) for the relevant Markov generator on *local gauge-invariant observables* should imply exponential decay of Euclidean correlators, and hence a **mass gap** in the reconstructed Minkowski theory via Osterwalder–Schrader (OS) reconstruction.

This note extracts the conjecture in its cleanest form and flags the genuinely hard part: **local-sector isolation** (separating local observables from global/topological/gauge modes so that a spectral gap is the right object).

---

## 1. Two different “gaps”

### (A) Spectral gap (Euclidean / Markov / Dirichlet form)

Given a probability measure \(\mu\) and a Dirichlet form \(\mathcal{E}\), a Poincaré inequality
\[
\mathrm{Var}_\mu(f) \le \frac{1}{\lambda}\,\mathcal{E}(f,f)
\]
means the generator \(L\) has a spectral gap \(\lambda\) in \(L^2(\mu)\).

### (B) Mass gap (Minkowski / Hamiltonian)

After OS reconstruction one has a Hilbert space \(\mathcal{H}\) and Hamiltonian \(H\ge 0\), and a mass gap is
\[
\sigma(H)=\{0\}\cup[\Delta,\infty),\qquad \Delta>0.
\]

Conjecture D is the claim that (A) implies (B), provided the right sector is used.

---

## 2. Why “local sector” matters

Gauge theories have “soft” directions that can destroy global gaps without affecting local physics:

- gauge directions (must be quotiented/projected out),
- torons / harmonic modes on periodic lattices (topological/global),
- possible IR sector issues in the continuum.

The project’s Conjecture D explicitly restricts to a **local-observable sector**, i.e. to test functions \(f\) depending on finitely many links/plaquettes (or their continuum analogues).

The expected logic is:

1. Prove a uniform Poincaré/LSI constant \(\lambda_{\mathrm{loc}}>0\) for local observables.
2. Use OS reflection positivity and transfer matrix technology to identify exponential time-decay of local correlators with a gap in the Hamiltonian spectrum.

---

## 3. The heuristic scaling \(m \sim \sqrt{\lambda}\)

In simple Gaussian/Ornstein–Uhlenbeck settings, the Poincaré constant is literally the smallest eigenvalue of the Hessian (a “mass-squared”), so \(m\sim \sqrt{\lambda}\).

The project uses this as a scaling guide:
\[
m \ge c\,\sqrt{\lambda_{\mathrm{loc}}}.
\]

One should treat the constant \(c\) as scheme-dependent; the robust claim is “\(\lambda_{\mathrm{loc}}>0\) forces exponential clustering”.

---

## 4. Lattice support: transfer matrix gap

On the lattice, reflection positivity implies existence of a transfer matrix \(T_a=e^{-aH_a}\). A spectral gap in \(H_a\) is equivalent to exponential decay of correlation functions in Euclidean time.

Thus, a plausible lattice route is:

- show that the spectral gap for a suitable Markov generator (stochastic quantization / Langevin) implies exponential decay of Euclidean two-point functions for local observables,
- then use reflection positivity / transfer matrix to turn that decay into a Hamiltonian mass gap.

---

## 5. What remains hard (and is not “just standard OS”)

1. **Prove the spectral gap uniformly in the continuum limit** (as \(a\to 0\)).  
   Many inequalities degrade with dimension/cutoff unless you have scale-robust curvature/convexity input.

2. **Justify restriction to local observables** and control the complement sector.  
   Without this, topological/zero modes can fake “gaplessness” at the level of the global generator.

3. **Handle gauge fixing/projectors cleanly** while preserving reflection positivity.

---

## 6. A sharp, operational formulation

A version of Conjecture D that could be attacked systematically:

> **Conjecture D′ (Uniform local Poincaré \(\Rightarrow\) mass gap).**  
> Consider Wilson SU(\(N\)) lattice gauge theory with spacing \(a\) and reflection-positive measure. Suppose there exists \(\lambda_{\mathrm{loc}}>0\), independent of \(a\), such that for every local gauge-invariant observable \(f\),
> \[
> \mathrm{Var}_{\mu_a}(f)\le \frac{1}{\lambda_{\mathrm{loc}}}\,\mathcal{E}_a(f,f).
> \]
> Then the transfer-matrix Hamiltonian \(H_a\) has a spectral gap \(\Delta_a\ge c\sqrt{\lambda_{\mathrm{loc}}}\), and in the continuum limit the reconstructed theory has \(\Delta>0\).

---

## 7. Why this is still “exciting” (even if the ingredients are classical)

Because it converts the Clay-style “mass gap” statement into a functional-inequality target:

- If you can build a **scale-robust** Poincaré/LSI inequality on the local sector (via curvature floors and RG stability), the rest is (in principle) operator-theoretic.

This is precisely the kind of “modularization” that makes a hard QFT problem attackable.

