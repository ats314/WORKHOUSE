# Riccati–Flux Derivation of Exponential Kernel Decay

## Purpose and scope

This module gives an analytic derivation of exponential off-diagonal decay for resolvents (and inverse operators) associated with local, uniformly positive operators. The proof route is **flux-based** and reduces the decay mechanism to a one-dimensional **Riccati inequality**, providing an independent alternative to:

- Combes–Thomas resolvent conjugation plus Schur bounds,
- Davies-type semigroup (heat kernel) conjugation.

The method is especially useful when a geometry-of-level-sets argument is natural (continuous setting) or when one can replace level sets by discrete shells (graph/lattice setting).

---

## Operator setting

Let \( (X,d) \) be a metric space (e.g., \(\mathbb R^d\) or a lattice/graph). Let \(H\) be a self-adjoint operator on a Hilbert space \(\mathcal H\) of functions over \(X\), and assume:

1. **Uniform positivity (spectral floor).** There exists \(m^2>0\) such that
   \[
   \langle u,Hu\rangle \ge m^2\,\|u\|^2
   \quad\text{for all }u\in\mathrm{Dom}(H).
   \]

2. **Locality.** \(H\) is local with respect to \(d\) (finite range on a lattice/graph, or a local elliptic operator in the continuum). This enters only through the coercivity estimate for exponential conjugation below.

Fix \(E<m^2\) and consider
\[
(H-E)u=f,
\]
with \(f\) compactly supported.

---

## Exponential conjugation

Fix a “source” set \(B\subset X\) and define
\[
\phi(x):=d(x,B).
\]
For \(\alpha>0\), define
\[
w(x):=e^{\alpha\phi(x)}u(x),
\]
so \(u=e^{-\alpha\phi}w\). The conjugated operator is
\[
H_\alpha := e^{\alpha\phi} H e^{-\alpha\phi},
\]
and the equation becomes
\[
(H_\alpha-E)w = e^{\alpha\phi} f.
\]

---

## Coercivity of the conjugated operator

There exists a constant \(C>0\) (depending only on the locality constants of \(H\)) such that
\[
\langle w,(H_\alpha-E)w\rangle
\ge (m^2-E-C\alpha^2)\,\|w\|^2.
\]
In particular, for
\[
\alpha < \sqrt{\frac{m^2-E}{C}},
\]
the operator \(H_\alpha-E\) is strictly positive.

*Remark.* In the continuum, this is the standard estimate that arises from commuting \(H\) with the weight \(e^{\alpha\phi}\) and controlling the induced first-order drift terms. On graphs/lattices, it follows from finite-range locality and weighted discrete integration by parts.

---

## Flux identity (continuous formulation)

For clarity, assume here that \(X\) is a smooth Riemannian manifold and \(H\) is a second-order elliptic operator. The lattice version replaces integrals by sums over distance shells.

Let level sets of \(\phi\) be denoted \(S_r:=\{x: \phi(x)=r\}\). Define the surface energy
\[
\mathcal E(r):=\int_{S_r}|w|^2\,d\sigma,
\]
and the outward flux
\[
\mathcal F(r):=\int_{S_r} \Re(\overline{w}\,\partial_n w)\,d\sigma,
\]
where \(\partial_n\) is the outward normal derivative.

A Rellich/coarea computation yields
\[
\frac{d}{dr}\mathcal E(r)=2\,\mathcal F(r)
\]
for \(r\) outside singular radii (the cut locus can be treated by standard smoothing/approximation; on graphs, the identity is exact on shells).

---

## Riccati inequality

Define the logarithmic slope
\[
g(r):=\frac{d}{dr}\log\sqrt{\mathcal E(r)}=\frac{\mathcal F(r)}{\mathcal E(r)}.
\]
Using the coercivity estimate for \(H_\alpha-E\) and integration by parts on the exterior region where \(f=0\), one obtains the differential inequality
\[
g'(r)+g(r)^2 \ge \alpha^2
\]
for \(r\) beyond the support of \(f\).

This is the key reduction: decay becomes a one-dimensional comparison problem.

---

## Riccati comparison and exponential decay

Consider the equality ODE
\[
h'(r)+h(r)^2=\alpha^2,
\]
whose stable constant solution is \(h\equiv\alpha\). A standard comparison argument implies that once \(r\) is beyond the source region,
\[
g(r)\ge \alpha,
\]
and therefore
\[
\mathcal E(r)\le \mathcal E(r_0)\,e^{-2\alpha(r-r_0)}.
\]

Undoing the conjugation yields pointwise (or operator-norm) exponential decay. In operator form, for measurable sets \(A,B\),
\[
\|\mathbf 1_A (H-E)^{-1} \mathbf 1_B\|
\le C_E\,e^{-\alpha\,d(A,B)},
\]
for some \(C_E\) depending on \(m^2-E\) and the locality constants of \(H\).

---

## How this complements Combes–Thomas and Davies

- **Combes–Thomas** typically proves resolvent decay by bounding \(\|H_\alpha-H\|\) and then using a Neumann-series argument for \((H_\alpha-E)^{-1}\). The Riccati–flux method instead derives decay from a flux monotonicity inequality.

- **Davies** gives heat-kernel decay and converts to resolvent decay via Laplace transform. Riccati–flux stays at the resolvent level and can be sharper when resolvent coercivity is natural.

---

## Consequences and usage

This module provides a third, independent exponential-decay engine. In a proof architecture that relies on inverse-kernel decay (e.g., exponential clustering, mass-gap transfer, or deterministic inverse bounds), having multiple logically independent routes significantly strengthens robustness to technical assumptions.
