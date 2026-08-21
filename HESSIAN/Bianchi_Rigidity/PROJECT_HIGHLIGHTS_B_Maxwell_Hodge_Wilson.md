# Project Highlight B: Lattice cochains, gauge directions, the horizontal sector, and the Wilson Hessian

This document extracts the “symbolic backbone” used everywhere later:
\[
d_0,\ d_1,\ d_0^\*,\ d_1^\*,\quad \ker d_0^\*,\quad d_1^\*d_1,
\]
and the key quadratic identity at the vacuum:
\[
\nabla^2 S_W(U^{(0)})=\frac{\beta}{N}\,d_1^\*d_1.
\]

---

## B.1. Lattice cells and cochains

Let \(\Lambda\subset\mathbb Z^d\) be a finite region.

* \(V(\Lambda)\): vertices (sites).
* \(E(\Lambda)\): oriented nearest-neighbor edges (links).
* \(P(\Lambda)\): oriented plaquettes (2-cells).  

Fix a compact Lie group \(G\) with Lie algebra \(\mathfrak g\) and an \(\mathrm{Ad}\)-invariant inner product
\[
\langle\cdot,\cdot\rangle_{\mathfrak g} \quad\text{on }\mathfrak g.
\]

Define \(k\)-cochains with values in \(\mathfrak g\):
\[
\mathcal C^0(\Lambda;\mathfrak g):=\{\,\varphi:V(\Lambda)\to\mathfrak g\,\},\qquad
\mathcal C^1(\Lambda;\mathfrak g):=\{\,X:E(\Lambda)\to\mathfrak g\,\},\qquad
\mathcal C^2(\Lambda;\mathfrak g):=\{\,Y:P(\Lambda)\to\mathfrak g\,\}.
\]

Equip \(\mathcal C^k\) with the standard \(\ell^2\) inner product induced by \(\langle\cdot,\cdot\rangle_{\mathfrak g}\):
\[
\langle X,X'\rangle_{\mathcal C^1}
:=\sum_{e\in E(\Lambda)}\langle X_e,X'_e\rangle_{\mathfrak g},
\quad
\langle Y,Y'\rangle_{\mathcal C^2}
:=\sum_{p\in P(\Lambda)}\langle Y_p,Y'_p\rangle_{\mathfrak g},
\quad\text{etc.}
\]

---

## B.2. Gauge action and the discrete differential \(d_0\)

The configuration manifold is
\[
M_\Lambda := G^{E(\Lambda)}.
\]
A gauge transformation \(g\in G^{V(\Lambda)}\) acts on \(U\in M_\Lambda\) by
\[
(g\cdot U)_{x,\mu} := g_x\,U_{x,\mu}\,g_{x+\hat\mu}^{-1}.
\]

Linearize at the vacuum configuration \(U^{(0)}\) with \(U^{(0)}_e=e\).  
Identify the tangent space
\[
T_{U^{(0)}}M_\Lambda \cong \mathcal C^1(\Lambda;\mathfrak g)
\]
via linkwise exponential paths
\[
U(t)_e=\exp(tX_e),\qquad X\in\mathcal C^1(\Lambda;\mathfrak g).
\]

The infinitesimal gauge action at the vacuum is the map
\[
d_0:\mathcal C^0(\Lambda;\mathfrak g)\to\mathcal C^1(\Lambda;\mathfrak g),
\qquad (d_0\varphi)_{x,\mu}:=\varphi_x-\varphi_{x+\hat\mu}.
\]
(With the convention that edges are oriented from \(x\) to \(x+\hat\mu\).)

Thus the **vertical** (gauge) subspace at \(U^{(0)}\) is
\[
V_{U^{(0)}} := \mathrm{im}(d_0)\subset \mathcal C^1(\Lambda;\mathfrak g).
\]

---

## B.3. The discrete curl \(d_1\) and cochain identity \(d_1d_0=0\)

Define
\[
d_1:\mathcal C^1(\Lambda;\mathfrak g)\to\mathcal C^2(\Lambda;\mathfrak g)
\]
by signed summation around a plaquette. For an oriented plaquette \(p=(x;\mu,\nu)\) (with \(\mu<\nu\)),
\[
(d_1X)_{x;\mu,\nu}
:= X_{x,\mu}+X_{x+\hat\mu,\nu}-X_{x+\hat\nu,\mu}-X_{x,\nu}.
\]
This is the lattice “curl”.

A direct cancellation check yields the cochain-complex identity
\[
d_1d_0 = 0.
\]
Hence every infinitesimal gauge direction is curl-free at the vacuum:
\[
\mathrm{im}(d_0)\subset \ker(d_1).
\]

---

## B.4. Adjoints and the horizontal sector \(\ker d_0^\*\)

Let \(d_0^\*,d_1^\*\) denote the adjoints with respect to the \(\ell^2\) inner products:
\[
\langle d_0\varphi, X\rangle_{\mathcal C^1}=\langle\varphi, d_0^\*X\rangle_{\mathcal C^0},
\qquad
\langle d_1X, Y\rangle_{\mathcal C^2}=\langle X, d_1^\*Y\rangle_{\mathcal C^1}.
\]

Define the **horizontal** subspace at the vacuum:
\[
H_{U^{(0)}} := V_{U^{(0)}}^\perp = \ker(d_0^\*).
\]
This is the standard Coulomb-like gauge-fixing subspace in the cochain language.

---

## B.5. Hodge decomposition on \(\mathcal C^1\)

Define the degree-1 Hodge Laplacian
\[
\Delta_1 := d_0d_0^\* + d_1^\*d_1.
\]
On a finite complex, standard linear algebra yields an orthogonal decomposition
\[
\mathcal C^1(\Lambda;\mathfrak g)
=
\mathrm{im}(d_0)\ \oplus\ \ker(\Delta_1)\ \oplus\ \mathrm{im}(d_1^\*),
\]
and
\[
\ker(d_0^\*) = \ker(\Delta_1)\oplus \mathrm{im}(d_1^\*).
\]
If boundary conditions kill harmonic 1-forms (e.g. contractible box with suitable boundary), then \(\ker(\Delta_1)=\{0\}\) and
\[
\ker(d_0^\*) = \mathrm{im}(d_1^\*).
\]

This is precisely the sector in which the Maxwell operator \(d_1^\*d_1\) is strictly positive (modulo boundary effects).

---

## B.6. Wilson plaquette holonomy and the linearization \(d_1\)

For a plaquette \(p=(x;\mu,\nu)\), define its holonomy
\[
U_p := U_{x,\mu}\,U_{x+\hat\mu,\nu}\,U_{x+\hat\nu,\mu}^{-1}\,U_{x,\nu}^{-1}.
\]

Let \(U(t)=\exp(tX)\) linkwise, with \(X\in\mathcal C^1(\Lambda;\mathfrak g)\).  
A first-order Baker–Campbell–Hausdorff expansion gives

**Lemma B.1 (Plaquette linearization).**
\[
U_p(t) = \exp\!\big(t(d_1X)_p + O(t^2)\big),\qquad t\to 0,
\]
uniformly for \(X\) in bounded sets.

---

## B.7. Wilson action and its Hessian at the vacuum

For \(G=\mathrm{SU}(N)\) define the Wilson plaquette potential
\[
\Phi(U) := \frac{\beta}{N}\,\mathrm{Re}\,\mathrm{Tr}(I-U),
\]
and the finite-volume Wilson action
\[
S_W(U) := \sum_{p\in P(\Lambda)} \Phi(U_p).
\]

Let the Lie algebra norm be
\[
|A|_{\mathfrak g}^2 := \langle A,A\rangle_{\mathfrak g}.
\]
In the \(\mathrm{SU}(N)\) specialization used in the project, the inner product is taken as
\[
\langle A,B\rangle_{\mathfrak g} := -\mathrm{Tr}(AB)
\qquad (A,B\in\mathfrak{su}(N)\text{ anti-Hermitian}).
\]

**Lemma B.2 (Quadratic expansion of \(\Phi\) at the identity).**  
For \(A\in\mathfrak{su}(N)\) with \(|A|\to 0\),
\[
\mathrm{Re}\,\mathrm{Tr}(I-e^A)
=\frac12\,|A|_{\mathfrak g}^2 + O(|A|^3).
\]
Consequently,
\[
\Phi(e^A)=\frac{\beta}{2N}\,|A|_{\mathfrak g}^2+O(|A|^3).
\]

Combine Lemma B.1 with Lemma B.2 to obtain the quadratic expansion of \(S_W\) at \(U^{(0)}\):

**Proposition B.3 (Wilson quadratic form).** For \(X\in\mathcal C^1(\Lambda;\mathfrak g)\),
\[
S_W(\exp(tX))
=
S_W(U^{(0)}) + \frac{\beta}{2N}\,t^2\,\|d_1X\|_{\mathcal C^2}^2 + O(t^3).
\]

Therefore the Hessian at the vacuum is exactly the lattice Maxwell operator:

**Theorem B.4 (Wilson Hessian \(=\frac{\beta}{N}d_1^\*d_1\)).**
As an operator on \(\mathcal C^1(\Lambda;\mathfrak g)\cong T_{U^{(0)}}M_\Lambda\),
\[
\nabla^2 S_W(U^{(0)})=\frac{\beta}{N}\,d_1^\*d_1.
\]
In particular for \(G=\mathrm{SU}(3)\),
\[
\nabla^2 S_W(U^{(0)})=\frac{\beta}{3}\,d_1^\*d_1.
\]

**Corollary B.5 (Kernel and gauge directions).**
\[
\ker\big(\nabla^2 S_W(U^{(0)})\big)=\ker(d_1)\supset \mathrm{im}(d_0).
\]
Hence infinitesimal gauge directions are always zero-modes of the Wilson Hessian at the vacuum; this is why later arguments project to \(H_{U^{(0)}}=\ker d_0^\*\).

---

## B.8. Why this matters downstream

1. The operator \(d_1^\*d_1\) is **positive semidefinite** and sparse (local stencil). This is the algebraic source of “PSD not adversarial” upgrades.
2. On \(\ker d_0^\*\), the Fourier symbol becomes “transverse Maxwell”, and the Green’s function estimates become close to plug-and-play.
3. The Wilson part alone has small eigenvalues on large tori (near-zero modes), so it cannot give volume-uniform coercivity; this is repaired by adding the Haar mass term (Highlight C).

