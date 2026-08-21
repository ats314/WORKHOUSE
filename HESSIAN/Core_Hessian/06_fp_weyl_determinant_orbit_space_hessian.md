---
title: "Orbit-space Jacobians as geometric convexity sources: FP/Gram determinants and Weyl denominators on the irreducible lattice orbit space"
date: "2025-12-29"
project: "SIMULATIONS"
status: "working note / attempt"
---

> **Goal.** Identify the *natural* Jacobian/determinant that lives on the **principal (irreducible) stratum** of the lattice gauge-orbit space under a gauge-equivariant coarse-graining/smoothing semigroup, and isolate a piece whose **Hessian is a Laplacian** (hence nonnegative) with an **explicit, scale-free positive lower bound**.
>
> **Punchline.** There are (at least) two closely related candidates:
>
> 1. **Orbit-volume / FP determinant** coming from the Riemannian quotient \(\mathcal C/\mathcal G\):
>    \(\Delta_{\mathrm{FP}}(U)=\det(D_U^*D_U)\) on the principal stratum.
> 2. **Weyl-denominator determinant** that appears whenever coarse variables are **conjugacy classes of holonomies** (block plaquettes/loops): \(|\Delta(t)|^2\).  Its Hessian in eigenangle coordinates is a **weighted complete-graph Laplacian** with a **uniform positive bound** \(\ge N/4\) on the \(SU(N)\) constraint hyperplane.
>
> These two are not enemies: (2) is essentially the “diagonalized/class-function shadow” of (1) once you reduce to conjugacy-class variables.


## 0. Context from Pillar L

The project already exploits one Weyl-type determinant: the **Jacobian of the exponential map** for Haar measure on each link,
\[
J(A)=\det_{\mathfrak g}\!\Big(\frac{\sinh(\operatorname{ad}_{iagA}/2)}{\operatorname{ad}_{iagA}/2}\Big),\qquad S_{\mathrm{Haar}}=-\log J,
\]
which yields a **positive quadratic “Haar mass”** (finite-cutoff convexity seed) and leads to a global horizontal Hessian lower bound via a decomposition
\[
\mathrm{Hess}\,S_{\mathrm{eff}}(U)=\beta\,\Delta_{\mathrm{latt}}-\beta V(U)+c_0 I\quad\Rightarrow\quad
\mathrm{Hess}^{\perp}S_{\mathrm{eff}}\ \ge\ (c_0-\beta C_V)I
\]
on horizontal directions, at fixed cutoff.  (This is the “Laplacian + bounded potential + positive constant” template.)

The catch, emphasized in the project notes, is that the explicit Haar mass scales like \(a^2\) and dies as \(a\to 0\).  So we want a *different* geometric source term that can plausibly survive coarse-graining.


## 1. The object that *must* appear on the orbit space: orbit-volume / FP determinant

### 1.1 Configuration space, gauge group, principal stratum

Let
\[
\mathcal C_\Lambda = G^{|B|},\qquad G=SU(N),
\]
with product bi-invariant metric. The lattice gauge group is
\[
\mathcal G_\Lambda = G^{|V|},
\]
acting by \((g\cdot U)_{xy} = g_x\,U_{xy}\,g_y^{-1}.\)

On the **principal stratum** \(\mathcal C_{\Lambda}^{\mathrm{irr}}\) (irreducible configurations), the stabilizer is discrete (center), so the action is infinitesimally free and the quotient
\[
\mathcal O_{\Lambda}^{\mathrm{irr}} := \mathcal C_{\Lambda}^{\mathrm{irr}}/\mathcal G_\Lambda
\]
is a smooth orbifold/manifold.

### 1.2 The Riemannian Jacobian of the quotient map

Let \(\pi:\mathcal C^{\mathrm{irr}}\to\mathcal O^{\mathrm{irr}}\) be the quotient map.
For an isometric group action, there is a canonical decomposition
\[
T_U\mathcal C = V_U\oplus H_U
\]
into vertical (orbit) and horizontal (orthogonal complement) subspaces.

The **induced measure** on the orbit space (pushforward of Haar/Riemannian volume) differs from the quotient Riemannian volume by an **orbit-volume density**. Concretely, pick an orthonormal basis \(\{\xi^{(a)}\}\) of \(\mathrm{Lie}(\mathcal G)\). The corresponding Killing vector fields \(K_a(U)\in V_U\) have a Gram matrix
\[
M_U := \big(\langle K_a(U),K_b(U)\rangle\big)_{ab}.
\]
Then the orbit-volume factor is
\[
\mathrm{vol}(\mathcal G\cdot U) \propto \sqrt{\det M_U}.
\]
This is the *coordinate-free* origin of an FP-type determinant on the orbit space.

### 1.3 Identifying \(M_U\) as a covariant graph Laplacian

Infinitesimally, a gauge parameter \(\xi=\{\xi_x\}_{x\in V}\) (with \(\xi_x\in\mathfrak{su}(N)\)) generates a vertical variation on a link \(b=(x\to y)\):
\[
\delta U_b \sim \xi_x\,U_b - U_b\,\xi_y.
\]
Using bi-invariance, the squared norm of this variation is equivalent to
\[
\|\delta U_b\|^2 \simeq \|\xi_x - \operatorname{Ad}_{U_b}\xi_y\|^2.
\]
Define the **lattice covariant derivative**
\[
(D_U\xi)_b := \xi_x - \operatorname{Ad}_{U_b}\xi_y\qquad (b:x\to y).
\]
Then the orbit metric is
\[
\|\delta U\|^2_{\mathrm{vert}} = \sum_{b\in B}\|(D_U\xi)_b\|^2
= \langle \xi,\ (D_U^*D_U)\,\xi\rangle.
\]
So (up to harmless constants)
\[
M_U = D_U^*D_U,\qquad \Delta_{\mathrm{FP}}(U):=\det(D_U^*D_U).
\]

### 1.4 Why this is naturally tied to the principal stratum

- \(D_U\) has a nontrivial kernel iff there exists a nonzero covariantly constant adjoint field
  \(\xi\) with \(\xi_x = \operatorname{Ad}_{U_b}\xi_y\) along every link.
  That is exactly a **reducibility** condition.

- Hence on \(\mathcal C^{\mathrm{irr}}\), \(D_U\) is injective and \(D_U^*D_U\) is strictly positive.
  So \(\Delta_{\mathrm{FP}}(U)>0\) is a smooth positive function on the principal stratum.

- On the reducible set \(\Sigma\), \(\Delta_{\mathrm{FP}}\to 0\). Thus
  \(S_{\mathrm{FP}}:=-\frac12\log\Delta_{\mathrm{FP}}\to +\infty\), giving a natural “repulsive wall” at the singular strata.

This meshes beautifully with the project’s **polarity-of-reducibles** theme: if reducibles are polar for the horizontal Dirichlet form, you can treat the orbit space as “analytically equivalent” to its principal stratum.


## 2. Hessian of the FP/Gram determinant: a sum-of-squares structure (near-Laplacian)

Define the geometric potential induced by orbit volume:
\[
S_{\mathrm{orb}}(U):=-\log \mathrm{vol}(\mathcal G\cdot U)
\;\equiv\; -\tfrac12\log\det(D_U^*D_U).
\]

Let \(M(U)=D_U^*D_U\). On the principal stratum, \(M(U)\) is positive definite.
Use the standard matrix calculus identities:
\[
\delta\log\det M = \mathrm{Tr}(M^{-1}\delta M),
\]
\[
\delta^2\log\det M
= \mathrm{Tr}(M^{-1}\delta^2 M) - \mathrm{Tr}(M^{-1}\delta M\,M^{-1}\delta M).
\]
Therefore
\[
\delta^2 S_{\mathrm{orb}}(U)
= -\tfrac12\mathrm{Tr}(M^{-1}\delta^2 M)
+\tfrac12\mathrm{Tr}(M^{-1}\delta M\,M^{-1}\delta M).
\]
The second term is manifestly **nonnegative**: it is a trace of a square.

### What this buys you

- If you can bound the “bad” term \(\mathrm{Tr}(M^{-1}\delta^2 M)\) above by \(C\|\delta U\|^2\), then you get a lower bound
  \[
  \mathrm{Hess}\,S_{\mathrm{orb}}\ \ge\ -C\,I \ + \ (\text{positive semidefinite}).
  \]
  This is exactly the same *shape* as the project’s Hessian decomposition \(\Delta- V + c_0 I\), except now the positive part is not a constant mass but a sum-of-squares term tied to \(M^{-1}\delta M\).

- Near reducibles, \(M^{-1}\) becomes large and the positive term \(\mathrm{Tr}(M^{-1}\delta M M^{-1}\delta M)\) typically blows up. So the orbit-volume wall is not just repulsive—it is *strongly* convex near the singular strata.

- Under a gauge-equivariant smoothing semigroup (heat-kernel convolution / Wilson flow / Langevin), the quotient Jacobian term is unavoidable because it is built into the quotient geometry.

This is a convincing route to “Hessian has Laplacian structure”: \(M=D_U^*D_U\) **is** a covariant graph Laplacian, and the convex part of \(\mathrm{Hess}\,S_{\mathrm{orb}}\) is literally a **sum of squares** of Laplacian-resolvent-weighted variations.


## 3. The *clean* Laplacian Hessian you can compute exactly: Weyl denominators of coarse holonomies

The FP/Gram determinant story is the invariant, coordinate-free one—but it can be abstract.
There is a simpler lens where you can see the Laplacian Hessian **in closed form**.

### 3.1 Coarse variables: conjugacy classes of holonomies

Many coarse-graining schemes (block-spin, TRG/HOTRG-inspired effective variables, heat-kernel projection) end up promoting **block holonomies** as slow variables:
\[
U_{\square}^{(\ell)}\in G\quad\text{(holonomy around an \(\ell\times\ell\) block plaquette/loop)}.
\]
Gauge transformations act on each such holonomy by **conjugation** at a basepoint,
\(U\mapsto g U g^{-1}\), so the gauge-invariant content is the **conjugacy class**.

Whenever your effective description depends on these variables through **class functions** of \(U\) (e.g. Wilson terms, heat kernels, character expansions), the measure reduction to conjugacy classes inevitably drags in the Weyl denominator.

### 3.2 Weyl denominator and its geometric potential

For a single \(G=SU(N)\) element with eigenangles \(\theta_1,\dots,\theta_N\) (\(\sum_i\theta_i=0\)), Weyl’s integration formula implies a density
\[
|\Delta(e^{i\theta})|^2
= \prod_{i<j}4\sin^2\!\Big(\frac{\theta_i-\theta_j}{2}\Big).
\]
Define
\[
S_{\mathrm{Weyl}}(\theta):=-\log|\Delta(e^{i\theta})|^2
= -\sum_{i<j}\log\Big(4\sin^2\!\frac{\theta_i-\theta_j}{2}\Big).
\]
The singular set (eigenvalue collisions) is exactly the non-regular / reducible locus.

### 3.3 Exact Hessian = weighted complete-graph Laplacian

Let
\[
w_{ij}(\theta):=\csc^2\!\Big(\frac{\theta_i-\theta_j}{2}\Big)\ge 1.
\]
A direct derivative computation yields
\[
\frac{\partial^2 S_{\mathrm{Weyl}}}{\partial\theta_i\partial\theta_j}=-\tfrac12 w_{ij}\ (i\ne j),\qquad
\frac{\partial^2 S_{\mathrm{Weyl}}}{\partial\theta_i^2}=\tfrac12\sum_{k\ne i}w_{ik}.
\]
So
\[
\nabla^2 S_{\mathrm{Weyl}}(\theta)=\tfrac12 L_{w(\theta)},
\]
where \(L_{w(\theta)}\) is the weighted Laplacian of the **complete graph** on \(\{1,\dots,N\}\).
Equivalently
\[
x^\top\nabla^2 S_{\mathrm{Weyl}}(\theta)x
=\tfrac14\sum_{i<j}w_{ij}(\theta)(x_i-x_j)^2.
\]

### 3.4 Uniform positive lower bound (the explicit \(\sigma_{\mathrm{geom}}\))

On the \(SU(N)\) tangent constraint \(\sum_i x_i=0\), using \(w_{ij}\ge 1\), we get
\[
 x^\top\nabla^2 S_{\mathrm{Weyl}}(\theta)x
\ge \tfrac14\sum_{i<j}(x_i-x_j)^2
= \tfrac{N}{4}\,\|x\|^2.
\]
Thus on the regular set,
\[
\boxed{\ \nabla^2 S_{\mathrm{Weyl}}\big|_{\sum x_i=0}\ \ge\ \frac{N}{4}\,I\ }
\]
with an \(a\)-independent constant.

### 3.5 Lattice consequence

If your coarse-graining semigroup produces an effective description in terms of a collection of coarse holonomies
\(\{U_{\square}^{(\ell)}\}\), then the total geometric potential includes
\[
S_{\mathrm{geom}}^{(\ell)}\ \supset\ \sum_{\square}\,S_{\mathrm{Weyl}}\big(\theta(U_{\square}^{(\ell)})\big),
\]
and its Hessian contains a **block-diagonal sum of complete-graph Laplacians**, each with the explicit lower bound \(N/4\) on the appropriate constraint hyperplane.

That is the cleanest candidate for an \(a\)-independent **positive source term** in the Riccati picture.


## 4. How this plugs into the “Riccati attractor” mass-gap story

- The finite-cutoff Haar mass term is a beautiful *starter motor* (it directly produces a constant \(+c_0 I\) piece in the horizontal Hessian), but it scales away with \(a\).

- The orbit-space determinants above are different: they come from **quotient geometry** (orbit-volume collapse near reducibles / eigenvalue collisions) and are naturally **dimensionless**.

- If the effective action under your smoothing/RG semigroup includes
  \(S_{\mathrm{eff}} = S_{\mathrm{phys}} + S_{\mathrm{geom}}\) with
  \(\nabla^2 S_{\mathrm{geom}}\ge \sigma_{\mathrm{geom}} I\) on the principal stratum (in the relevant coordinates), then the Riccati mechanism can plausibly stabilize a strictly positive convexity eigenvalue even as explicit UV “mass seeds” disappear.


## 5. What to do next (to turn this from “pretty” into “useful”)

1. **Choose the semigroup precisely.** Heat-kernel convolution on links, Wilson flow, or an explicit TRG/HOTRG-induced Markov kernel. You want a map that commutes with gauge action so the quotient story is clean.

2. **Prove that the coarse variables include regular holonomies with Weyl density.** Make precise the pushforward of Haar measure to conjugacy classes of coarse holonomies, and identify the Weyl denominator factor.

3. **Show uniformity on the principal stratum.** Use polarity/capacity-zero arguments to ignore reducibles; then show the remaining contributions to the Hessian are bounded below by \(-\beta C\) as in the project’s Hessian decomposition.

4. **Riccati extraction.** Combine the explicit \(\sigma_{\mathrm{geom}}=N/4\) coming from Weyl denominators with the \(-2H^2\) nonlinearity in the Hessian evolution under the chosen smoothing flow.


## 6. Tiny moral

The Weyl denominator is the universe’s way of saying:

> “If you try to make eigenvalues collide (i.e. drift toward reducibility), I will punish you with infinite action curvature.”

That punishment is a weighted Laplacian.
And weighted Laplacians are exactly the kind of objects spectral-gap proofs like to eat for breakfast.

