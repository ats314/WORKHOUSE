---
title: "Polarity and Capacity of Reducible Strata in Gauge Field Space (Project Extract)"
date: "2026-01-01"
---

## 1. Purpose

Gauge theories have singular orbit structure:

- reducible connections,
- stabilizer jumps,
- nongeneric strata.

This project proposes handling these singular sets using **Gaussian polarity/capacity** arguments:

> If reducible strata are polar (capacity zero) in an appropriate infinite-dimensional measure class, they are negligible for functional inequalities and typical-path arguments.

This is presented as a *structural mechanism* intended to support gauge-invariant steps without needing to excise singular sets manually.

---

## 2. Project’s main structural claim (as recorded)

In an infinite-dimensional Gaussian setting (abstract Wiener space), the project claims:

- Any affine subspace of codimension \(\ge 2\) is polar (capacity zero).
- Reducible strata in gauge field space can be modeled as a countable union of such “thin” sets, hence polar.

This suggests:

\[
  \mathrm{Cap}(\text{reducible set}) = 0
\]
for the capacity associated with the relevant Dirichlet form / Sobolev structure.

---

## 3. Why this is potentially powerful

If correct and implemented in the lattice-to-continuum pipeline, this provides:

- a way to argue that “generic” configurations dominate estimates,
- compatibility with LSI / spectral gap methods that are stable under removal of capacity-zero sets,
- a measure-theoretic bypass for orbit-type singularities.

This is not the standard approach in constructive gauge theory, which tends to choose gauges or control orbit-space singularities directly.

---

## 4. What must be made precise

To make this usable in a proof, the following must be formalized:

1. **Exact measure class** (finite lattice Haar vs continuum Gaussian, and how limits are taken).
2. **Exact capacity** (which Dirichlet form, which Sobolev index).
3. **Modeling reducible strata** as a countable union of submanifolds or subspaces with controlled codimension in the relevant topology.
4. **Stability of inequalities** (e.g., LSI) under removing capacity-zero sets in the precise setting used.

---

## 5. Status

This document is a *structural extraction*.

- It looks like a plausible and possibly novel supporting mechanism.
- It is not yet a complete theorem chain in the lattice Yang–Mills context, because the Gaussian/infinite-dimensional framework must be connected rigorously to the finite-lattice Haar theory used elsewhere in the project.

---

## 6. Suggested next derivation (internal)

The minimal upgrade path is to prove a lemma of the form:

> For the finite-lattice gauge field configuration space with Haar product measure, the reducible set has exponentially small measure as \(L\to\infty\), and in the continuum limit its capacity vanishes with respect to the limiting Dirichlet form.

This would bridge the current polarity intuition to the actual measure sequence in Yang–Mills.
