
# Haar measure and gauge fixing: making the FP→Haar link explicit

## Why you care

The curvature floor argument leans hard on “Haar geometry is really there in the measure you’re using.”

That is not automatic once you gauge-fix. Gauge fixing rewrites the path integral measure as
\[
\mathcal{D}A \;=\; \mathcal{D}A\;\delta(G[A])\,\Delta_{\rm FP}[A]\;\mathcal{D}g,
\]
and the question is:

> Does the resulting reduced measure on the gauge-fixed variables carry the same Haar/Vandermonde geometry (at least locally, in the SAFE chart)?

If yes, then your local Haar curvature estimates apply to the gauge-fixed measure (modulo technicalities like Gribov copies and boundaries of the gauge slice).

---

## 1. The core mechanism in one line

On a compact gauge group \(G\), when you diagonalize a group element (or a Lie-algebra element in a Cartan subalgebra), the Jacobian for “eigenvalues + angles” is a **Vandermonde determinant**. Squared Vandermonde factors are exactly the density of Haar measure restricted to the maximal torus (with Weyl quotient).

That Vandermonde factor is precisely what a Faddeev–Popov determinant computes when the gauge condition is “diagonalize \(A_0\)” (Polyakov gauge) or “fix to Cartan”.

---

## 2. A canonical example: Polyakov gauge (continuum)

In Polyakov gauge one chooses a gauge transformation that makes \(A_0\) time-independent and diagonal in the Cartan subalgebra:
\[
A_0 = \frac{2\pi}{\beta}\,\mathrm{diag}(\rho_1,\rho_2,\rho_3),\qquad \sum_i \rho_i = 0.
\]

The Faddeev–Popov determinant for this gauge choice produces a factor of the form
\[
\Delta_{\rm FP}(\rho)\propto \prod_{i<j}\sin^2\big(\pi(\rho_i-\rho_j)\big),
\]
which is the reduced Haar measure (the SU(3) Vandermonde density) on the maximal torus.

This is the cleanest “physics” justification that gauge-fixing does not erase Haar geometry; it **recreates it** as the FP Jacobian.

---

## 3. What changes on the lattice

On the lattice, each link variable \(U_\ell\in G\) is integrated against Haar measure by definition.
If you introduce a gauge condition that fixes a representative in each gauge orbit, you pick up an FP determinant that is the Jacobian of the orbit-to-slice map.

Locally (in a sufficiently small chart around the identity and away from Gribov horizons):

- The gauge slice can be parameterized smoothly.
- The FP determinant is smooth and nonzero.
- The induced measure on physical variables inherits the same local differential geometry, up to bounded distortions.

This is exactly the regime in which a local curvature certificate is meaningful.

---

## 4. The real caveats that must be stated

If you want this piece to be rigorous (not “physicist-rigorous”), you must declare what you assume about:

1. **Gribov copies**: the gauge condition might intersect a gauge orbit more than once.
2. **Boundary / singular sets**: places where the FP determinant vanishes (gauge slice tangent to orbit).
3. **Topological sectors / holonomies**: residual degrees that cannot be gauged away on a periodic lattice.

The SAFE analysis typically lives in a neighborhood where these pathologies are absent or controlled.

---

## 5. What you can safely claim

A rigorously defensible statement (and the one you should write) is:

> In a neighborhood of the identity configuration (or more generally, inside a gauge slice where the FP determinant is bounded away from zero and infinity), the gauge-fixed measure is absolutely continuous with respect to the product Haar measure, with a smooth density. Therefore, the local Haar geometric curvature estimates apply (up to an explicit distortion term).

That is strong enough to justify using Haar curvature as the baseline in the SAFE region.

