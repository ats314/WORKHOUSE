# Haar Mass and the Core Curvature Theorem (Horizontal Bakry–Émery Positivity)

## 0. What is extracted here

This document collects the most “structural” geometric input in the project:

- a first-principles Ricci-curvature computation for compact Lie groups with bi-invariant metrics,
- the way this becomes a **uniform positive term** (“Haar mass”) on the configuration manifold \(M_\Lambda=G^{E(\Lambda)}\),
- and the core theorem: **on a small-field region near the vacuum, the Bakry–Émery tensor is uniformly positive on the physical (horizontal) directions**, independent of volume.

This is the part that makes the later Helffer–Sjőstrand / Green-function machinery behave like a *massive* operator rather than a massless one.

---

## 1. Ricci curvature of a compact Lie group with a bi-invariant metric

Let \(G\) be a compact connected Lie group with Lie algebra \(\mathfrak g\), and let \(\langle\cdot,\cdot\rangle\) be an \(\mathrm{Ad}\)-invariant inner product on \(\mathfrak g\). This defines a bi-invariant Riemannian metric \(g_G\) on \(G\).

### 1.1 Levi–Civita connection (bi-invariant case)

If \(X^L,Y^L\) are left-invariant vector fields, then
\[
\nabla_{X^L}Y^L = \tfrac12 [X,Y]^L.
\]

### 1.2 Curvature and Ricci (explicit formula)

Using the above,
\[
R(X^L,Y^L)Z^L = -\tfrac14 [[X,Y],Z]^L.
\]

Let \(\{e_i\}_{i=1}^{\dim\mathfrak g}\) be an orthonormal basis of \(\mathfrak g\). Then
\[
\mathrm{Ric}_G(X,X)
=
\sum_i \langle R(X^L,e_i^L)e_i^L,X^L\rangle
=
\tfrac14\sum_i \|[X,e_i]\|^2
\ \ge\ 0.
\]

Thus bi-invariant metrics have nonnegative Ricci curvature, and they have a **strictly positive** lower bound iff there are no abelian (flat torus) factors.

### 1.3 Strict positivity constant (semisimple case)

If \(G\) is compact semisimple, then the quadratic form
\[
X\mapsto \sum_i \|[X,e_i]\|^2
\]
is comparable to \(\|X\|^2\) (it is the adjoint-Casimir). Hence
\[
\mathrm{Ric}_G \ge \kappa_G\, g_G
\quad\text{for some }\kappa_G>0
\]
with \(\kappa_G\) depending only on \((G,g_G)\).

For \(G=\mathrm{SU}(N)\) with the conventional normalization \(\langle X,Y\rangle=-\mathrm{Tr}(XY)\), one can make \(\kappa_G\) fully explicit in terms of the Casimir eigenvalue (project notes keep it symbolic to avoid normalization traps).

---

## 2. Product geometry: the configuration manifold

For a finite lattice \(\Lambda\), define
\[
M_\Lambda := G^{E(\Lambda)}
\]
with product metric \(g_\Lambda=\bigoplus_{\ell\in E(\Lambda)} g_G\).

Because Ricci curvature is additive across Riemannian products,
\[
\mathrm{Ric}_{g_\Lambda}(v,v) = \sum_{\ell\in E(\Lambda)} \mathrm{Ric}_G(v_\ell,v_\ell)
\ge
\kappa_G \sum_{\ell}\|v_\ell\|^2
=
\kappa_G \|v\|_{g_\Lambda}^2.
\]
So:
\[
\boxed{
\mathrm{Ric}_{g_\Lambda} \ge \kappa_G g_\Lambda
\quad\text{uniformly in }\Lambda.
}
\]

This is the geometric origin of “Haar mass.”

---

## 3. Bakry–Émery tensor for the Gibbs law

Let the Gibbs measure be
\[
\mu_\Lambda(dU)=Z_\Lambda^{-1}e^{-S_\Lambda(U)}\,d\mathrm{vol}_{g_\Lambda}(U),
\]
and let \(L_\Lambda=\Delta_\Lambda-\langle\nabla S_\Lambda,\nabla\cdot\rangle\).

The Bakry–Émery tensor is
\[
\mathrm{Ric}_{\mu_\Lambda}
:=
\mathrm{Ric}_{g_\Lambda} + \nabla^2 S_\Lambda.
\]

The Bochner–Bakry–Émery identity gives, for smooth \(f\),
\[
\Gamma_{2,\Lambda}(f)
=
\|\nabla^2 f\|_{\mathrm{HS}}^2
+
\mathrm{Ric}_{\mu_\Lambda}(\nabla f,\nabla f).
\]

Hence any lower bound
\(\mathrm{Ric}_{\mu_\Lambda}\ge \rho g_\Lambda\)
implies the curvature-dimension inequality \(CD(\rho,\infty)\) pointwise.

---

## 4. Gauge invariance forces horizontality

Let \(\mathcal G_\Lambda=G^{V(\Lambda)}\) act by lattice gauge transformations.
Tangent vectors to gauge orbits define the **vertical** directions; their orthogonal complement defines the **horizontal** directions \(H_U\subset T_U M_\Lambda\).

If \(f\) is gauge-invariant, then
\[
df(U)[v]=0\quad\forall v\in T_U(\mathcal G_\Lambda\cdot U),
\]
so \(\nabla f(U)\in H_U\). This is the reason all curvature estimates can (and should) be proved only on the horizontal sector: it is the physically relevant one for gauge-invariant observables.

---

## 5. The core curvature theorem (local, volume-uniform)

Write the action as
\[
S_\Lambda = S_W + S_{\mathrm{add},\Lambda},
\]
where:

- \(S_W\) is the Wilson plaquette action,
- \(S_{\mathrm{add},\Lambda}\) is a gauge-invariant stabilizer.

Assume:

1. (Uniform lower bound on the stabilizer Hessian)  
   \[
   \nabla^2 S_{\mathrm{add},\Lambda}(U)\ \ge\ -C_{\mathrm{add}}\, g_\Lambda(U)
   \quad\text{for all }U,
   \]
   with \(C_{\mathrm{add}}\) independent of \(\Lambda\).

2. \(C_{\mathrm{add}}<\kappa_G\).

Then the project proves a local theorem of the following form:

### Theorem (Core curvature theorem, local horizontal positivity)

There exist constants \(r>0\), \(\rho_{\mathrm{loc}}>0\) depending only on \(\kappa_G\) and \(C_{\mathrm{add}}\) (and local lattice geometry) such that, for every finite \(\Lambda\),

\[
\mathrm{Ric}_{\mu_\Lambda}(U)(v,v)\ \ge\ \rho_{\mathrm{loc}}\|v\|^2
\quad\text{for all }U\in B_r(U^{(0)}),\ v\in H_U.
\]

Equivalently, gauge-invariant observables satisfy \(CD(\rho_{\mathrm{loc}},\infty)\) on the small-field ball \(B_r(U^{(0)})\).

### Where the Wilson action enters

- At the vacuum, the Wilson Hessian linearizes to a multiple of \(d_1^\ast d_1\), hence is nonnegative.
- Locality + continuity implies the Wilson Hessian has no large negative part on a sufficiently small neighborhood.

So the negative part comes only from the stabilizer, and the Haar Ricci term \(\kappa_G g_\Lambda\) dominates it as long as \(C_{\mathrm{add}}<\kappa_G\).

---

## 6. Optional extension: heat-kernel lattice actions (global CD mechanism)

The notes also record a separate “UNIFIED” mechanism:

- For actions built from heat-kernel potentials \(V_t(g)=-\log K_t(g)\),
  one can bound \(\|\nabla^2 V_t\|_\infty\) explicitly by a quantity \(M_2(t)\).
- Locality then gives a global Hessian lower bound \(\nabla^2 S\ge -(\nu M_2(t))g_\Lambda\).
- Therefore
  \[
  \mathrm{Ric}_{\mu_\Lambda}\ge (\kappa_G-\nu M_2(t))g_\Lambda,
  \]
  yielding a global \(CD(\rho,\infty)\) whenever \(\kappa_G>\nu M_2(t)\).

This is mathematically clean because it trades “small-field” restrictions for parameter tuning.

---

## 7. Why this is exciting

The usual lattice YM intuition treats “mass” as a dynamical effect of nonlinearity and confinement. Here, there is a distinct geometric contribution:

- The compact-group *reference geometry* contributes a strictly positive term to the Bochner tensor, which behaves like a mass in the effective operator controlling gradients.

This is not the whole mass gap story (nonabelian dynamics still matters), but it provides a rigorous mass-like baseline that makes operator inverses exponentially decaying once you project to the physical sector.
