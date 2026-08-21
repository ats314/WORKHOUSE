# UNIFY 01 — Wilson Hessian as a Discrete Hodge Laplacian, and the “Haar Mass” Quadratic Form

## Purpose of this extract

This note distills (and slightly re-packages) two linked derivations from the project:

1. **Small-field expansion of the Wilson action** and identification of its Hessian at the trivial configuration with the discrete Hodge operator \(d_1^* d_1\) on lattice \(1\)-forms.
2. **Small-field expansion of Haar volume in exponential coordinates**, yielding a strictly convex quadratic term whose Hessian is proportional to the group Ricci tensor—an effect informally dubbed the “Haar mass”.

The *combination* is the interesting part: the Wilson Hessian controls **curvature (field strength)**, while the Haar contribution supplies a **uniform on-site convexity** that survives in directions where the Wilson quadratic form is degenerate.

---

## 1. Lattice gauge configuration manifold and exponential coordinates

Let \(\Lambda\) be a finite periodic hypercubic lattice. Let \(G\) be a compact connected Lie group with Lie algebra \(\mathfrak g\), equipped with a bi-invariant metric \(\langle\cdot,\cdot\rangle_G\).

The configuration manifold is the finite product
\[
M_\Lambda := G^{E(\Lambda)},
\]
one copy of \(G\) per oriented edge \(\ell\in E(\Lambda)\). For the small-field analysis we work near the *trivial configuration*
\[
U^{(0)} := (e,e,\dots,e)\in M_\Lambda.
\]

In a neighborhood of \(e\in G\), we use exponential coordinates:
\[
U_\ell = \exp_G(X_\ell), \qquad X_\ell\in \mathfrak g.
\]
Thus a small neighborhood of \(U^{(0)}\) is parametrized by \(X=(X_\ell)_{\ell\in E(\Lambda)}\in \mathfrak g^{E(\Lambda)}\).

---

## 2. Wilson action quadraticization and the operator \(d_1^*d_1\)

### 2.1 Wilson action

Write the oriented plaquette holonomy as \(U_p\), and take (for concreteness) the \(SU(N)\) Wilson action
\[
S_W(U) \;=\; \frac{\beta}{N}\sum_{p\in P(\Lambda)} \Big( N - \Re \mathrm{Tr}(U_p)\Big).
\]
Near \(U_p=e\), the class function \(U\mapsto N-\Re\mathrm{Tr}(U)\) has a second-order Taylor expansion
\[
N-\Re\mathrm{Tr}(\exp X) \;=\; \frac12 \langle X, H_0 X\rangle_G + O(|X|^3),
\]
so the Wilson action admits a small-field quadratic approximation in terms of \(\log U_p\).

### 2.2 Discrete cochain operators

Let \(C^k(\Lambda;\mathfrak g)\) be \(\mathfrak g\)-valued \(k\)-cochains.
Define the coboundaries
\[
d_0 : C^0 \to C^1,\qquad d_1 : C^1 \to C^2.
\]
In particular, for a \(1\)-cochain \(X\in C^1\), \((d_1 X)_p\) is the signed sum of link variables around plaquette \(p\).

Equip cochains with the Euclidean inner products induced from \(\langle\cdot,\cdot\rangle_G\) and counting measure. Let \(d_1^*\) denote the adjoint.

### 2.3 Linearization of plaquettes

For a plaquette \(p\) with oriented boundary \(\partial p=\ell_1+\ell_2-\ell_3-\ell_4\),
\[
U_p \;=\; U_{\ell_1}U_{\ell_2}U_{\ell_3}^{-1}U_{\ell_4}^{-1}.
\]
If \(U_\ell=\exp(X_\ell)\) with all \(X_\ell\) small, then the Baker–Campbell–Hausdorff expansion gives
\[
\log(U_p) \;=\; (d_1 X)_p \;+\; O(|X|^2),
\]
where \(O(|X|^2)\) consists of Lie bracket terms.

### 2.4 Hessian at the vacuum

Inserting the previous expansion into \(S_W\) yields the leading quadratic form
\[
S_W(U) \;=\; c_W \sum_{p\in P(\Lambda)} \big\|(d_1 X)_p\big\|_G^2 \;+\; O(|X|^3),
\qquad c_W:=\frac{\beta}{2N}.
\]
Therefore, at \(U^{(0)}\) the Hessian of \(S_W\) is the operator
\[
\nabla^2 S_W\big(U^{(0)}\big) \;=\; 2c_W\, d_1^*d_1
\quad \text{on } \mathfrak g^{E(\Lambda)}\simeq C^1(\Lambda;\mathfrak g).
\]
In particular \(d_1^*d_1\ge 0\), hence the Wilson Hessian is positive semidefinite.

### 2.5 Degeneracy: closed 1-forms, gauge modes, and harmonic modes

The kernel is
\[
\ker(d_1^*d_1) = \ker(d_1),
\]
i.e. the \(\mathfrak g\)-valued **closed** \(1\)-cochains. On a periodic lattice, \(\ker(d_1)\) contains:

- **Exact** modes \(\mathrm{im}(d_0)\), corresponding to infinitesimal gauge transformations.
- **Harmonic** modes \(\ker(\Delta_1)\) (lattice “torons”), i.e. global flat directions on the torus.

A discrete Hodge decomposition gives
\[
C^1(\Lambda;\mathfrak g)
= \mathrm{im}(d_0)\;\oplus\;\ker(\Delta_1)\;\oplus\;\mathrm{im}(d_1^*),
\qquad \Delta_1:=d_0d_0^*+d_1^*d_1.
\]
On \(\mathrm{im}(d_1^*)\) (coexact 1-forms), \(d_1^*d_1\) is strictly positive; the degeneracy lives entirely in \(\mathrm{im}(d_0)\oplus\ker(\Delta_1)\).

---

## 3. Haar volume in exponential coordinates and the “Haar mass”

### 3.1 Volume density expansion on a Riemannian manifold

In geodesic normal coordinates \(\theta\) around a point \(x_0\) on a Riemannian manifold \((M,g)\), the volume density satisfies
\[
\sqrt{\det g_{ij}(\theta)}
= 1 - \frac16 \mathrm{Ric}_{ij}(x_0)\,\theta^i\theta^j + O(|\theta|^3).
\]

### 3.2 Application to compact Lie groups

For \((G,g_G)\) bi-invariant and \(x_0=e\), exponential coordinates are geodesic normal coordinates. Writing \(X=\sum_i \theta^i e_i\),
\[
d\mathrm{vol}_{g_G}(U)
= J_G(\theta)\,d\theta,\qquad U=\exp_G(X),
\]
and the expansion gives
\[
J_G(\theta) = 1 - \frac16 \mathrm{Ric}_{ij}(e)\,\theta^i\theta^j + O(|\theta|^3).
\]

Define the **Haar potential**
\[
S_H(\theta) := -\log J_G(\theta).
\]
Then
\[
\nabla^2 S_H(0)(X,X) \;=\; \frac13\,\mathrm{Ric}_G(X,X).
\]

If \(\mathrm{Ric}_G \ge \kappa_G g_G\) for some \(\kappa_G>0\) (true for compact simple groups with the usual normalization), then
\[
\nabla^2 S_H(0) \;\ge\; c_H\,\mathrm{Id},
\qquad c_H:=\kappa_G/3.
\]

This is the “Haar mass”: in exponential coordinates, **the log-density of Haar measure is locally strictly convex**, with curvature controlled by the group Ricci tensor.

### 3.3 Product Haar measure on \(M_\Lambda\)

On \(M_\Lambda = G^{E(\Lambda)}\), the Riemannian volume is the product Haar volume. In exponential coordinates
\(U_\ell=\exp(X_\ell)\) it yields a sum of single-link Haar potentials:
\[
S_{H,\Lambda}(X)=\sum_{\ell\in E(\Lambda)} S_H(X_\ell),
\]
so the Hessian at \(0\) satisfies
\[
\nabla^2 S_{H,\Lambda}(0) \;\ge\; c_H\,\mathrm{Id}
\quad \text{on } \mathfrak g^{E(\Lambda)}.
\]

---

## 4. Combined quadratic form: Wilson curvature + Haar on-site convexity

In exponential coordinates near \(U^{(0)}\), the “effective” small-field quadratic form (Haar + Wilson) is
\[
S_{\mathrm{eff},\Lambda}^{(2)}(X)
:= S_{H,\Lambda}^{(2)}(X) + S_W^{(2)}(X)
\;\approx\;
\frac12 \langle X,\,(c_H\,\mathrm{Id} + 2c_W d_1^*d_1)\,X\rangle.
\]

Key structural consequences:

1. **Coexact modes \(\mathrm{im}(d_1^*)\)**: both terms contribute, giving robust convexity tied to curvature energy.
2. **Harmonic modes \(\ker(\Delta_1)\)**: Wilson contributes nothing, but Haar still gives a strictly positive quadratic form.
3. **Exact modes \(\mathrm{im}(d_0)\)**: Wilson contributes nothing (gauge symmetry), but Haar remains strictly convex; these are ultimately removed/quotiented when restricting to gauge-invariant observables.

Thus, even though the Wilson quadratic form is degenerate, the compact-group geometry injects a uniform, local convexity that can be exploited in Bakry–Émery curvature bounds once one projects to physical (horizontal) directions.

---

## 5. Why this is “potentially new theory” material

None of the ingredients alone are new (Wilson quadraticization, Hodge theory, normal-coordinate volume expansion). What *is* potentially generative is the synthesis:

- **Use the group’s intrinsic Ricci curvature as an analytic “mass scale”** in the functional-inequality/semigroup sense (not a particle mass, but a uniform spectral-gap seed).
- **Treat the Wilson action Hessian as a discrete geometric operator** \(d_1^*d_1\), making the physical positivity and the exact/harmonic/coexact split transparent.
- **Set up a clean interface to horizontal Bakry–Émery curvature** (see UNIFY 02), which is a natural entry point for dimension-free Poincaré/LSI and local-to-global upgrades.

