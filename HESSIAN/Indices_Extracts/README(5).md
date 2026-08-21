# Novel extracts: what to save and why

This folder contains the **most “theory-creating”** pieces in the current project corpus: arguments that are either (i) genuinely geometric in flavor, (ii) capable of scaling into a new analytic framework for Yang–Mills, or (iii) contain a mechanism that is *not* just a repackaging of standard textbook material.

## Included documents

### `Haar_Curvature_and_Geometric_Mass.md`
Core idea: **positive Ricci curvature of the compact gauge group** provides a baseline Bakry–Émery curvature floor on \(G^E\), which can be interpreted as a **mass-like scale** via Poincaré/LSI.

### `Riccati_Barrier_and_Geometric_RG.md`
Core idea: the minimal eigenvalue of a projected Hessian/curvature tensor satisfies a **Riccati-type inequality** with **positive forcing**, giving a simple, robust **barrier mechanism** for keeping the IR eigenvalue strictly positive. Includes a small runnable ODE simulation snippet.

### `Infinite_Codimension_and_Gaussian_Polarity.md`
Core idea: reducible connections satisfy **infinitely many independent constraints**, hence the reducible locus has **infinite codimension**, making it a natural candidate for **polarity/capacity-zero** under Gaussian/OU Dirichlet forms.

### `Stratified_Parabolic_Maximum_Principle.md`
Core idea: on stratified spaces, a **polar singular set** should not spoil parabolic comparison; this enables a PDE-to-ODE comparison principle for curvature positivity evolution.

## What is *not* included
- Purely standard background (definitions of Poincaré inequality, basic Bakry–Émery, etc.) unless it is directly used in the extracted mechanisms.
- Conjecture-analysis files whose main content is external review rather than an internal derivation.

## Suggested next expansion route
A coherent “new theory” arc would connect the four documents into a single pipeline:

1. Haar curvature provides a baseline convexity floor.
2. A projected Hessian/curvature flow satisfies a Riccati barrier inequality with forcing.
3. Polarity removes the reducible singular set from the functional-analytic dynamics.
4. Stratified comparison preserves positivity in the presence of singular strata.

The main missing technical bridge is proving the *correct projected PDE/inequality* for the eigenvalue \(\lambda(t,x)\) with a forcing term whose sign is fully controlled.
