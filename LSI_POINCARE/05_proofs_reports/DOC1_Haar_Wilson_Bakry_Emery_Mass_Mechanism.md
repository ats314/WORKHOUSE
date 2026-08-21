# Haar–Wilson Bakry–Émery Mass Mechanism on the Lattice

## Abstract

On a finite lattice, the Yang–Mills configuration space is a compact Lie-group product
\[
\mathscr A \;=\; G^{E},\qquad G=\mathrm{SU}(N),
\]
equipped with the product (right-invariant) Haar metric \(g\) and Gibbs measure
\[
d\mu_\beta(U)\;=\;Z^{-1}e^{-S_\beta(U)}\,d\mathrm{vol}_g(U),
\]
where \(S_\beta\) is the Wilson action.  
This note isolates a geometric mechanism that yields a *positive* Bakry–Émery curvature lower bound on the **physical (horizontal)** directions near the identity sector:
\[
\mathrm{Ric}_{\mu_\beta}\big|_{\mathcal H_U}\;\ge\;(\kappa+\beta c_W)\,g\big|_{\mathcal H_U},
\]
with \(\kappa>0\) coming from the Ricci curvature of \(\mathrm{SU}(N)\) (Haar geometry) and \(c_W>0\) coming from the spectral gap of the Wilson Hessian on horizontals.  
Via Bakry–Émery \(\Gamma_2\)-calculus, this yields local Poincaré/log-Sobolev constants of order \(1/(\kappa+\beta c_W)\) and motivates an “effective mass scale” \(m_{\mathrm{eff}}^2\sim \kappa+\beta c_W\).

---

## 1. Lattice configuration space and Gibbs measure

Let \(\Lambda\) be a finite lattice (graph) with oriented edges \(E\) and oriented plaquettes \(P\).
Fix \(G=\mathrm{SU}(N)\) with Lie algebra \(\mathfrak g=\mathfrak{su}(N)\) and inner product
\[
\langle X,Y\rangle := -\mathrm{Tr}(XY).
\]

### 1.1 Configuration space and metric

A lattice gauge field is a map \(U:E\to G\). The configuration space is the compact manifold
\[
\mathscr A := G^E .
\]

Write a tangent vector at \(U\in \mathscr A\) in right-invariant coordinates:
\[
\delta U_e = U_e X_e,\qquad X_e\in\mathfrak g.
\]
Define the product right-invariant metric
\[
g_U(X,Y):=\sum_{e\in E}\langle X_e,Y_e\rangle .
\]

### 1.2 Wilson action and Gibbs measure

For each plaquette \(p\in P\) let \(U_p=\prod_{e\in\partial p}U_e^{\sigma_{p,e}}\) with \(\sigma_{p,e}\in\{\pm1,0\}\).
The Wilson action is
\[
S_\beta(U):=\beta\sum_{p\in P}\Bigl(N-\mathrm{Re}\,\mathrm{Tr}(U_p)\Bigr).
\]
The associated Gibbs measure is
\[
d\mu_\beta(U)=Z^{-1}e^{-S_\beta(U)}\,d\mathrm{vol}_g(U).
\]

The diffusion generator symmetric in \(L^2(\mu_\beta)\) is
\[
L=\Delta_g-\nabla S_\beta\cdot \nabla .
\]

---

## 2. Bakry–Émery tensor on \(\mathscr A\)

The Bakry–Émery tensor of \((\mathscr A,g,\mu_\beta)\) is
\[
\mathrm{Ric}_{\mu_\beta} \;:=\; \mathrm{Ric}_g+\nabla^2 S_\beta.
\]

### 2.1 Haar geometry supplies a positive baseline \(\kappa\)

For a compact simple Lie group \(G\) with a bi-invariant metric, the Ricci tensor is a positive multiple of the metric:
\[
\mathrm{Ric}_G = \kappa\, g_G,\qquad \kappa>0.
\]
For \(\mathrm{SU}(N)\) in the standard normalization, \(\kappa\) is proportional to the adjoint quadratic Casimir.

Since \(\mathscr A=G^E\) is a Riemannian product with the product Haar metric,
\[
\mathrm{Ric}_g=\kappa\, g
\]
(with the same \(\kappa\)).

---

## 3. Wilson Hessian as a Gram operator

### 3.1 Small-angle coordinates and linearization

Near the identity sector, write \(U_e=\exp(\theta_e)\) with \(\theta_e\in\mathfrak g\) small.
For a plaquette \(p\),
\[
U_p=\exp(\theta_p),\qquad \theta_p=\sum_{e\in\partial p}\sigma_{p,e}\theta_e + O(\|\theta\|^2).
\]

Let \(X=(X_e)_{e\in E}\in T_U\mathscr A\). The first variation of \(\theta_p\) defines a linear map
\[
C:\;T_U\mathscr A\to \mathfrak g^{P},\qquad (CX)_p:=\theta_p'(X),
\]
which is the discrete “curl” operator \(d_1\) up to Ad-transport corrections.

### 3.2 Second variation of the Wilson action

Expanding \(N-\mathrm{ReTr}(e^{\theta_p})=\frac12\|\theta_p\|^2+O(\|\theta_p\|^3)\), the leading term of the second variation is
\[
\delta^2 S_\beta[X]
=
\nabla^2 S_\beta(X,X)
=
\beta\sum_{p\in P}\langle \theta_p'(X),\theta_p'(X)\rangle
+O(\|\theta\|\cdot\|X\|^2).
\]
Ignoring higher-order corrections in a sufficiently small-angle region, this is the Gram form
\[
\nabla^2 S_\beta(X,X)\approx \beta\langle CX,CX\rangle
=
\beta\langle X,C^\ast C X\rangle.
\]
Hence the **Wilson Hessian** is the positive semidefinite operator
\[
\mathcal H_W := C^\ast C \ge 0.
\]

---

## 4. Gauge directions, horizontals, and a spectral gap \(c_W\)

### 4.1 Vertical (gauge) directions lie in \(\ker \mathcal H_W\)

Infinitesimal gauge transformations are vertex fields \(\phi:V\to\mathfrak g\) acting as
\[
X = d_0\phi,\qquad X_e=\phi(t(e))-\phi(s(e))
\]
(in the linearization near identity).  
By the lattice Bianchi identity,
\[
C(d_0\phi)=0.
\]
Therefore vertical directions belong to \(\ker(C)\subseteq \ker(\mathcal H_W)\).

### 4.2 Horizontal subspace and the gap on physical modes

Decompose orthogonally
\[
T_U\mathscr A = \mathcal V_U\oplus \mathcal H_U,
\]
where \(\mathcal V_U\) is the tangent to the gauge orbit and \(\mathcal H_U=\mathcal V_U^\perp\) is the horizontal (physical) subspace.
Let \(P_0\) denote the orthogonal projector onto \(\mathcal H_U\).

Assuming boundary/gauge-fixing conditions that eliminate cohomological zero-modes in the horizontal sector, the restriction of \(\mathcal H_W\) to \(\mathcal H_U\) has a strictly positive spectral gap:
\[
\exists\,c_W>0:\qquad
\langle X_{\mathrm{hor}},\mathcal H_W X_{\mathrm{hor}}\rangle
\ge c_W\|X_{\mathrm{hor}}\|^2
\quad \forall\,X_{\mathrm{hor}}\in\mathcal H_U.
\]
Equivalently,
\[
P_0^\top \mathcal H_W P_0 \;\ge\; c_W P_0.
\]

---

## 5. Main bound: Bakry–Émery curvature is positive on horizontals

### Theorem (Haar–Wilson Bakry–Émery lower bound; local/horizontal)

There exists a small-angle neighborhood \(\mathcal N_{\theta_0}\subset \mathscr A\) such that for all \(U\in\mathcal N_{\theta_0}\) and all horizontal \(X\in \mathcal H_U\),
\[
\nabla^2 S_\beta(U)[X,X]\;\ge\;\beta c_W\|X\|^2.
\]
Consequently, on \(\mathcal H_U\),
\[
\mathrm{Ric}_{\mu_\beta}(U)[X,X]
=
\mathrm{Ric}_g(U)[X,X]+\nabla^2 S_\beta(U)[X,X]
\;\ge\;(\kappa+\beta c_W)\|X\|^2.
\]
Equivalently,
\[
\mathrm{Ric}_{\mu_\beta}\big|_{\mathcal H_U}
\;\ge\;
(\kappa+\beta c_W)\,g\big|_{\mathcal H_U}.
\]

### Proof sketch

1. Haar geometry gives \(\mathrm{Ric}_g=\kappa g\).  
2. In \(\mathcal N_{\theta_0}\), higher-order corrections \(O(\|\theta\|\|X\|^2)\) are absorbed by shrinking \(\theta_0\).  
3. The spectral gap of \(\mathcal H_W\) on \(\mathcal H_U\) yields \(\nabla^2 S_\beta\ge \beta c_W\) on horizontals.  
4. Summing gives the bound.

---

## 6. Consequences: local Poincaré/LSI and “effective mass”

A Bakry–Émery curvature lower bound \(\mathrm{Ric}_{\mu_\beta}\ge \rho g\) with \(\rho>0\) implies (under standard smoothness assumptions) Poincaré and log-Sobolev inequalities with constants \(1/\rho\) and \(2/\rho\), respectively.

In the present setting, on the small-angle tube \(\mathcal N_{\theta_0}\) and on horizontal observables, the natural scale is
\[
\rho=\kappa+\beta c_W>0.
\]
This motivates interpreting
\[
m_{\mathrm{eff}}^2\;\sim\;\kappa+\beta c_W
\]
as an “effective mass squared” for physical fluctuations at the lattice scale.

---

## 7. Why this is interesting (and what is still missing)

- The sign of the Bakry–Émery tensor is fixed **geometrically**: Haar Ricci curvature contributes \(\kappa>0\), and the Wilson Hessian contributes \(\beta c_W>0\) on physical modes.
- This is a clean bridge between:
  - Lie group geometry (Ricci curvature of \(\mathrm{SU}(N)\)),
  - discrete Hodge theory (gap of \(d_1^\ast d_1\) on horizontals),
  - functional inequalities (Poincaré/LSI) and spectral gap.

Open ends for upgrading “local/horizontal” to “uniform/nonperturbative” include:
1. Control of large-angle configurations and global convexity failures.
2. Volume-uniformity: behavior of \(c_W\) under increasing lattice size and boundary conditions.
3. Compatibility with the full gauge orbit geometry (Gribov issues, reducibles).
