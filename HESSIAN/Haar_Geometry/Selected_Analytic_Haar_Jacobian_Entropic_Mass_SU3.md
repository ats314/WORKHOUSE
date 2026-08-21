---
title: "Haar Jacobian Mass Term as an Entropic Stabilizer (SU(3) Lattice Coordinates)"
date: "2026-01-01"
---

## 1. Purpose

This document isolates the project’s central **structural idea**:

> In exponential coordinates \(U=\exp(A)\) on \(SU(3)\), the Haar measure contributes a **local Jacobian factor** \(J(A)\).
> Expanding \(-\log J(A)\) at small \(A\) yields a positive quadratic term that behaves like an **entropic mass** and seeds a convex core.

This is used throughout the project as a hard stabilizer term:
\[
  S_\beta(A) \;=\; S_{\mathrm{W}}(A) \;+\; S_{\mathrm{Haar}}(A),\qquad
  S_{\mathrm{Haar}}(A)\approx c_0\sum_\ell \|A_\ell\|^2,
\]
with \(c_0=0.125\) in the adopted normalization.

---

## 2. Haar Jacobian in exponential coordinates

Let \(G=SU(N)\), \(\mathfrak{g}=\mathfrak{su}(N)\), and \(U=\exp(A)\) with \(A\in\mathfrak{g}\).
In exponential coordinates, Haar measure locally takes the form
\[
  d\mu_{\mathrm{Haar}}(U) = J(A)\, dA,
\]
where the Jacobian can be expressed via the adjoint map:
\[
  J(A) \;=\; \det\!\left(\frac{\sinh(\operatorname{ad}_A/2)}{\operatorname{ad}_A/2}\right).
\]
Hence the induced “Haar action” is
\[
  S_{\mathrm{Haar}}(A) = -\log J(A) = -\mathrm{Tr}\,\log\!\left(\frac{\sinh(\operatorname{ad}_A/2)}{\operatorname{ad}_A/2}\right).
\]

---

## 3. Small-field expansion and the quadratic “mass” term

Using the Taylor expansion
\[
  \log\left(\frac{\sinh x}{x}\right) = \frac{x^2}{6} - \frac{x^4}{180} + O(x^6),
\]
one obtains, for small \(\|A\|\),
\[
  S_{\mathrm{Haar}}(A)
  \;=\;
  \frac{1}{24}\,\mathrm{Tr}\big(\operatorname{ad}_A^2\big)
  \;+\;
  O(\|A\|^4).
\]
The quadratic term is positive because \(\operatorname{ad}_A\) is skew-adjoint with respect to the Killing form / Frobenius pairing, so \(\mathrm{Tr}(\operatorname{ad}_A^2)\le 0\) and the sign is handled by conventions.

In the project’s concrete coordinate convention for \(SU(3)\),
this quadratic term is represented numerically as:
\[
  S_{\mathrm{Haar}}(A)\approx c_0 \|A\|_F^2,
  \qquad c_0=\frac{3}{24}=0.125,
\]
and is implemented as a linkwise Frobenius norm penalty.

---

## 4. Convexity seed

A key consequence (local) is:

\[
  \nabla^2 S_{\mathrm{Haar}}(A) \succeq c_0 I
\]
in the flat coordinate system on Lie algebra variables (to leading order; in the project it is treated as an exact quadratic term).

This provides a **positive uniform floor** for the total action’s Hessian near the identity.

---

## 5. Why this matters in the project pipeline

The project’s proposed mass-gap mechanism uses the Haar term as the source of **uniform convexity in a small ball**, while the Wilson term provides a negative “curvature erosion” that grows with \(\beta\) and amplitude \(r\).

The key objects \(R(\beta)\) and \(\tau(\beta,r)\) are defined relative to the competition:

\[
  \lambda_{\min}(\nabla^2 S_\beta(A))
  \approx
  c_0 - (\text{Wilson erosion}),
\]
and “Wilson erosion” is then bounded (analytically, in the project plan) by a quadratic form in the small field region.

---

## 6. Caveats

- The exact form of \(J(A)\) is standard; what is nonstandard here is treating its quadratic expansion as a *primary stabilizing term* in a constructive mass-gap pipeline and attempting to propagate it by a flow argument.
- Any continuum argument must control the coordinate patch and gauge issues; this document only explains the entropic stabilization mechanism at the level of local coordinates.
