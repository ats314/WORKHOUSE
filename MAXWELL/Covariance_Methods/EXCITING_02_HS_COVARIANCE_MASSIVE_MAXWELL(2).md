# Exciting Extract 02: Helffer–Sjöstrand covariance control and the matrix Brascamp–Lieb bound on a good set

This note extracts the analytic bridge

\[
\text{matrix curvature lower bound}\quad\Longrightarrow\quad
\text{covariance bound via an inverse “massive Maxwell” operator}.
\]

It is the point where the manuscript’s insistence on **matrix** inequalities (rather than scalar curvature bounds) pays off.

---

## 1. Reversible generator, carré du champ, and Witten Laplacian

Let \((M,g)\) be a compact Riemannian manifold and let \(\mu\) be a probability measure of the form
\[
d\mu = Z^{-1}e^{-S}\,d\mathrm{vol}_g,
\]
with \(S\in C^2(M)\). The reversible diffusion generator is
\[
L := \Delta_g - \langle \nabla S,\nabla(\cdot)\rangle_g,
\]
self-adjoint on \(L^2(\mu)\).

The carré du champ is
\[
\Gamma(f,g):=\langle \nabla f,\nabla g\rangle_g,\qquad \Gamma(f):=\Gamma(f,f).
\]

### 1.1 Bochner–Weitzenböck / Bakry–Émery curvature matrix

Define the Bakry–Émery curvature matrix
\[
\mathrm{Ric}_\mu := \mathrm{Ric}_g + \nabla^2 S,
\]
a symmetric endomorphism of \(TM\).

The associated Witten Laplacian on 1-forms (equivalently on vector fields) is the self-adjoint operator \(\mathcal L^{(1)}\) characterized by the commutation identity
\[
\nabla(-Lu)=\mathcal L^{(1)}(\nabla u),
\]
and admitting the decomposition
\[
\mathcal L^{(1)} = (-L)\otimes I + \mathrm{Ric}_\mu.
\tag{1.1}
\]
Because \((-L)\otimes I\succeq 0\) on \(L^2(\mu;TM)\), we have the basic domination
\[
\mathcal L^{(1)}\ \succeq\ \mathrm{Ric}_\mu.
\tag{1.2}
\]

---

## 2. Helffer–Sjöstrand representation of covariance

Let \(F,G\in C^1(M)\) be centered as needed (e.g. \(\mu(G)=0\)). Let \(u\) solve the Poisson equation
\[
-Lu = G,\qquad \mu(u)=0.
\]
Existence/uniqueness holds because \(M\) is compact and \(L\) is elliptic with constants in the kernel.

Using \(\mu\)-symmetry (integration by parts),
\[
\mathrm{Cov}_\mu(F,G)
= \int (F-\mu F)\,G\,d\mu
= \int (F-\mu F)(-Lu)\,d\mu
= \int \langle \nabla F,\nabla u\rangle_g\,d\mu.
\tag{2.1}
\]

Now apply the commutation identity \(\nabla(-Lu)=\mathcal L^{(1)}(\nabla u)\):
since \(-Lu=G\), we have
\[
\mathcal L^{(1)}(\nabla u)=\nabla G,
\qquad\text{so}\qquad
\nabla u = (\mathcal L^{(1)})^{-1}\nabla G
\]
(on the orthocomplement of the kernel). Substituting into (2.1) yields the HS identity:
\[
\mathrm{Cov}_\mu(F,G)
=
\int \Big\langle \nabla F,\ (\mathcal L^{(1)})^{-1}\nabla G\Big\rangle_g\,d\mu.
\tag{2.2}
\]

This is a **matrix** representation: covariances are controlled by an inverse operator on vector fields.

---

## 3. From a pointwise hinge to a massive Maxwell inverse on a good set

In the lattice gauge application, \(M=M_\Lambda\), \(\mu=\mu_{\Lambda,\beta}\), and Part 5 provides a *localized matrix hinge inequality* on a small-field region \(K\subset M\):
\[
\mathrm{Ric}_\mu(U)\ \succeq\ M_0
\qquad (U\in K),
\tag{3.1}
\]
where \(M_0\) is a fixed, \(U\)-independent positive operator on \(\mathcal C^1(\Lambda;\mathfrak g)\) of the form
\[
M_0 = m^2 I + \alpha\,d_1^\*d_1.
\tag{3.2}
\]

### 3.1 Localized/reflected dynamics (conditioning)

To use (3.1) rigorously in the HS representation, we work with a localized dynamics on \(K\):
- either the **conditioned measure** \(\mu^K=\mu(\cdot\mid K)\),
- or equivalently a **reflecting/Neumann** generator \(L^K\) on \(K\) reversible w.r.t. \(\mu^K\).

Let \(\mathcal L^{(1)}_K\) be the corresponding Witten Laplacian.

The decomposition (1.1) holds on \(K\) for the reflected dynamics, hence
\[
\mathcal L^{(1)}_K \succeq \mathrm{Ric}_\mu\qquad\text{on }K,
\]
and by (3.1),
\[
\mathcal L^{(1)}_K\ \succeq\ M_0.
\tag{3.3}
\]

### 3.2 Inverse order reversal

**Lemma 3.1 (inverse monotonicity).**  
If \(A,B\) are self-adjoint and \(A\succeq B\succ0\), then
\[
A^{-1}\ \preceq\ B^{-1}.
\]

*Proof.* Conjugate by \(B^{-1/2}\) to get \(B^{-1/2}AB^{-1/2}\succeq I\), hence its inverse is \(\preceq I\). Conjugate back. \(\square\)

Apply Lemma 3.1 to (3.3) to obtain
\[
(\mathcal L^{(1)}_K)^{-1}\ \preceq\ M_0^{-1}.
\tag{3.4}
\]

### 3.3 Conditional matrix Brascamp–Lieb bound

Insert (3.4) into the HS identity on \(K\):

**Proposition 3.2 (conditional covariance bound on \(K\)).**  
For \(F,G\in C^1(M)\) with \(\mu^K(G)=0\),
\[
\mathrm{Cov}_{\mu^K}(F,G)
=
\int_{K}\Big\langle \nabla F,\ (\mathcal L^{(1)}_K)^{-1}\nabla G\Big\rangle\,d\mu^K
\ \le\
\int_{K}\Big\langle \nabla F,\ M_0^{-1}\nabla G\Big\rangle\,d\mu^K.
\tag{3.5}
\]

This is the sought “matrix Brascamp–Lieb” inequality: the covariance is bounded by the inverse of a fixed operator.

---

## 4. Horizontal restriction for gauge-invariant observables

On the lattice gauge manifold, there is a gauge-orbit foliation. Gauge-invariant observables have gradients orthogonal to gauge directions (they are **horizontal**).

At the vacuum, the horizontal subspace is
\[
H^{(0)} := \ker(d_0^\*)\subset \mathcal C^1(\Lambda;\mathfrak g).
\]

Because \(d_1d_0=0\), one has \(d_0^\*d_1^\*=0\), hence
\[
d_1^\*d_1(\mathcal C^1)\subset \ker(d_0^\*),
\]
so \(H^{(0)}\) is invariant under \(d_1^\*d_1\), and therefore under \(M_0=m^2I+\alpha d_1^\*d_1\).

Define the restricted operator
\[
(M_0)_H := M_0|_{H^{(0)}}.
\]
For \(\xi,\eta\in H^{(0)}\),
\[
\langle \xi, M_0^{-1}\eta\rangle_{\mathcal C^1}
=
\langle \xi,(M_0)_H^{-1}\eta\rangle_{\mathcal C^1}.
\tag{4.1}
\]

Thus for gauge-invariant \(F,G\), the physically relevant object is \((M_0)_H^{-1}\).

---

## 5. Kernel notation and the road to exponential clustering

Write the (horizontal) Green kernel in link indices:
for \(b,b'\in E(\Lambda)\),
\[
\big((M_0)_H^{-1}\eta\big)_b = \sum_{b'} \big((M_0)_H^{-1}\big)_{b,b'}\,\eta_{b'}.
\]
Define the operator norm of the block
\[
\Big|\big((M_0)_H^{-1}\big)_{b,b'}\Big|_{\mathrm{op}}
:=\sup_{|v|_{\mathfrak g}=1}\Big|\big((M_0)_H^{-1}\big)_{b,b'}v\Big|_{\mathfrak g}.
\]

Let \(\mathrm{dist}_E\) be the graph distance on links induced by **plaquette adjacency**:
\(b\sim b'\) iff a plaquette boundary contains both \(b\) and \(b'\).

The analytic target (proved later via Combes–Thomas) is:
\[
\Big|\big((M_0)_H^{-1}\big)_{b,b'}\Big|_{\mathrm{op}}
\ \le\ C\,e^{-\eta\,\mathrm{dist}_E(b,b')}.
\tag{5.1}
\]

Once (5.1) is known, the conditional covariance bound (3.5) becomes an exponential-in-distance bound whenever the supports of \(\nabla F\) and \(\nabla G\) are separated in \(\mathrm{dist}_E\).

---

## 6. What could be developed further

The HS + hinge mechanism is modular. If one can produce a comparable matrix lower bound for the curvature matrix \(\mathrm{Ric}_\mu\) for other lattice field theories (spin systems with internal symmetry, sigma models, or improved gauge actions), then the same chain applies:

\[
\text{matrix hinge} \Rightarrow \text{HS covariance bound} \Rightarrow
\text{finite-range inverse decay} \Rightarrow \text{exponential clustering}.
\]

The challenging parts are not HS or Combes–Thomas; they are:
- producing the hinge in the right sector (horizontal/gauge-invariant),
- and globalizing (localization / typicality) so that the good set \(K\) has high \(\mu\)-probability.
