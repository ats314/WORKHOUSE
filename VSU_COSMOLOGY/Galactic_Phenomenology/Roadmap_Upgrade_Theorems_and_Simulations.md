---
title: "Upgrade Roadmap"
subtitle: "What the existing work unlocks, and what must be proved / simulated next"
status: "Forward-looking; explicitly separates proved components from required upgrades"
---

# Upgrade Roadmap
## Turning the best current results into publishable papers (and eventually bigger claims)

This document is intentionally pragmatic. It lists:
- what in the project is already “theorem-shaped,”
- what is *one paper away* from theorem-shaped,
- and what are the unavoidable “hard upgrades” if you want to level up the claims.

---

# A. Constructive mass-gap program (lattice gauge theory)

## A1. What is already structurally complete at fixed cutoff
From the appendices, the following chain is internally coherent:

1. **Local coercivity via a matrix hinge inequality**  
   (Wilson action linearization \(\Rightarrow\) massive Maxwell-type control in the good region).

2. **Lyapunov drift \(\Rightarrow\) uniform-in-volume functional inequalities**  
   (Poincaré / Log–Sobolev).

3. **Helffer–Sjöstrand covariance representation**  
   (correlations = resolvent of a Witten-type operator).

4. **Combes–Thomas inverse decay**  
   (exponential off-diagonal decay of the resolvent).

5. **Localization + typicality**  
   (remove conditioning, get unconditional exponential clustering with exponentially small finite-volume corrections).

6. **OS reconstruction + gap extraction**  
   (exponential time clustering \(\Rightarrow\) Hamiltonian spectral gap).

These pieces are already “paper modular”: you can publish subchains as independent results if you choose scope carefully.

## A2. Theorems you must still prove to upgrade from “fixed cutoff” to “real mass gap”
The project explicitly points at the necessary permanence upgrades:

### (1) Thermodynamic limit + permanence of OS structure
You need:
- existence of infinite-volume limit points \(\mu_\infty\) of \(\mu_\Lambda\),
- and that OS reflection positivity / translation invariance persist under \(|\Lambda|\to\infty\).

### (2) Reflection-positivity permanence under RG / coarse graining
You need a theorem of the form:

> If \(\mu\) is reflection positive and the coarse-graining map \(\mathcal R\) is reflection-equivariant,
> then \(\mathcal R_\*\mu\) remains reflection positive.

And similarly for projective limits on the cylinder observable algebras.

### (3) Continuum limit control
Even with (1) and (2), the actual Clay-style Yang–Mills statement requires:
- uniform control as \(a\to 0\),
- renormalization handled in a way compatible with the OS axioms,
- and persistence of a nonzero gap in the limit.

The correct “honest framing” is: the current appendices give a *serious fixed-cutoff constructive gap machine*, and the continuum limit is the deep remaining mountain.

---

# B. Vacuum stiffness theory (IR modified gravity / scalar sector)

## B1. What is already strong and publishable
1. **Clean variational principle for the AQUAL-type PDE** with an explicit constitutive law \(\mu(s)=1-e^{-s}\).  
2. **Hyperbolicity / stability analysis** in the covariant completion (no-ghost, positive sound speed, principal symbol).  
3. **Intrinsic screening via operator saturation** (high-acceleration recovery of Poisson/GR).  
4. **A concrete, reproducible cluster solver** (Coma) demonstrating that scalar self-energy contributions can be order-unity relative to gas mass at \(R_{500}\) for plausible central parameters.  
5. **A signed, explicit linear-order mapping for \(S_8\)** with an integral \(I(0)\) that can be computed and checked independently.

Those are all “referee-safe” provided the claims are scoped properly (IR effective theory; controlled regimes; clear perturbative approximations).

## B2. Simulations needed to move from “toy cosmology” to “precision cosmology”
This is where you move from paper-writing to HPC.

### (1) Modified Boltzmann code (CLASS/CAMB)
You need to implement the modified linear sector:
- background \(H(a)\) (if unchanged, simplest),
- modified Poisson relation / slip (if any),
- and the scale/time-dependent \(G_{\rm eff}(k,a)\) (or \(\alpha(k,a)\)).

Deliverables:
- CMB TT/TE/EE spectra,
- lensing \(C_\ell^{\kappa\kappa}\),
- matter power \(P(k,z)\),
- derived parameters (\(S_8\), \(f\sigma_8\), etc).

### (2) Nonlinear structure formation (N-body)
Because intrinsic screening is nonlinear, you ultimately need:
- N-body with the quasilinear elliptic solver for \(\Phi\),
- environment-dependent effects (EFE) and halo bias predictions,
- cluster mass calibration against lensing.

### (3) Cluster + galaxy forward modeling
Your Coma solver is a great “unit test.” Turning it into a paper means:
- a sample of clusters, not one,
- explicit priors for \(T(r)\), non-thermal pressure, and hydrostatic bias,
- and a consistent mapping to observable X-ray profiles.

---

# C. A “bigger theory” connection that is actually honest

If you want a unifying narrative without overreach:

- The **mass-gap program** is about *constructive control of infrared behavior* (exponential clustering \(\leftrightarrow\) gapped spectrum).
- The **vacuum stiffness theory** is about *phenomenological infrared modification* encoded by a constitutive law \(\mu\).

A serious, testable bridge between these two worlds would look like:
- an RG mechanism where a microscopic measure (possibly gauge-theoretic) flows to an effective IR stiffness functional,
- with reflection positivity / OS axioms preserved along the flow,
- and with a demonstrable gap setting a correlation length that shows up as an IR scale.

That’s a real research program. It’s also exactly the sort of thing worth splitting into multiple papers, because each “bridge segment” is a nontrivial theorem/simulation.

---

# Dependencies in the project
This roadmap is grounded in:
- Appendix L’s OS reconstruction + permanence discussion,
- Appendix K’s reflection positivity setup,
- the VSU action / stability / screening files (`01.x`, `05.1`),
- the linear cosmology + weak lensing files (`03.5`, `04.2`).
