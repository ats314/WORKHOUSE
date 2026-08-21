# The matrix hinge and the “massive Maxwell” mechanism (fixed cutoff)

This note extracts and consolidates the project’s most structurally *leveraged* local estimate:
a **localized Bakry–Émery curvature lower bound** that splits into

- a **uniform Haar/Ricci mass** coming from the compact group geometry, and
- a **structured Maxwell–type PSD operator** coming from the Wilson action Hessian at the vacuum.

This is the analytic “hinge” that later converts into
(1) uniform functional inequalities on a small-field region and
(2) a concrete *massive* Green’s function controlling correlations.

---

## 1. Configuration manifold and Gibbs geometry

For a finite periodic lattice \(\Lambda\), the configuration space is the product Lie group
\[
M_\Lambda := G^{E(\Lambda)},
\]
equipped with the product bi-invariant Riemannian metric \(g_\Lambda\).

The Wilson Euclidean Gibbs measure has smooth density
\[
d\mu_{\Lambda,\beta}(U) = Z_{\Lambda,\beta}^{-1}\,e^{-S_W(U)}\,d\mathrm{vol}_{g_\Lambda}(U),
\]
so the reversible generator is
\[
L_\Lambda = \Delta_\Lambda - \langle \nabla S_W,\nabla \cdot\rangle_{g_\Lambda}.
\]

The Bakry–Émery tensor for \(\mu_{\Lambda,\beta}\) is the **curvature matrix**
\[
\mathrm{Ric}_{\mu_{\Lambda,\beta}}
:= \mathrm{Ric}_{g_\Lambda} + \nabla^2 S_W.
\]

The project’s Bochner–Bakry–Émery identity (with drift) reads on the localized region
\[
\Gamma_{2}(f)
= \|\nabla^2 f\|_{\mathrm{HS}}^2
+ \mathrm{Ric}_{\mu_{\Lambda,\beta}}(\nabla f,\nabla f),
\]
so a pointwise **matrix lower bound** on \(\mathrm{Ric}_{\mu_{\Lambda,\beta}}\) implies a local \(CD(\rho,\infty)\) condition and hence local Poincaré/LSI bounds.

---

## 2. Vacuum Hessian = discrete Maxwell operator

Let \(U^{(0)}\) be the vacuum configuration (all links equal to \(\mathbf 1\)).
The project computes the exact quadratic form of the Wilson Hessian at \(U^{(0)}\) as
\[
\nabla^2 S_W(U^{(0)}) \;=\; \frac{\beta}{n\lambda_\rho}\,d_1^\* d_1
\quad\text{on }\mathcal C^1(\Lambda;\mathfrak g).
\]

Equivalently,
\[
\nabla^2 S_W(U^{(0)})[X,X]
= \frac{\beta}{n\lambda_\rho}\,\|d_1 X\|_{\mathcal C^2}^2 \ge 0.
\]

This isolates the *structured* part of curvature: it is exactly the discrete Maxwell operator on \(1\)-cochains.

Gauge symmetry produces unavoidable kernel directions:
\(\mathrm{im}(d_0)\subseteq \ker(d_1)\), and even on the horizontal space
\(\ker(d_0^\*)\) there are harmonic zero-modes in finite volume.

---

## 3. Canonical small-field region and stability of the Hessian

The project defines a canonical small-field region \(K_\Lambda(r)\) (radius \(r\) below injectivity scale) such that:

1. every link admits uniform exponential coordinates in \(\mathfrak g\), and
2. the *nonlinear* Hessian \(\nabla^2 S_W(U)\) is a controlled perturbation of its vacuum value.

Using a uniform third-derivative constant \(M_3(r_\star)\) for a single plaquette functional and bounded overlap \(\nu\),
the global Hessian perturbation is bounded by
\[
\nabla^2 S_W(U) \;\succeq\; \nabla^2 S_W(U^{(0)}) \;-\; R_W(r)\,I,
\qquad
R_W(r) := \Big(\frac{\beta}{n}\Big)(2\nu M_3(r_\star))\,r.
\]

Crucially: **bounded overlap** prevents the constant from scaling like \(|P(\Lambda)|\).

---

## 4. The localized matrix hinge inequality

On \(K_\Lambda(r)\), the Bochner tensor admits the “hinge” decomposition
\[
\mathrm{Ric}_{\mu_{\Lambda,\beta}}(U)
\;\succeq\;
\big(c_H - R_W(r)\big)\,I
+ \frac{\beta}{n\lambda_\rho}\,d_1^\* d_1.
\]

Here \(c_H>0\) is a uniform lower bound coming from the Ricci curvature of the compact group factors (a “Haar/Ricci mass”).

Choosing \(r\) so that \(R_W(r)\le c_H/2\) gives the clean, \(U\)-independent operator bound
\[
\mathrm{Ric}_{\mu_{\Lambda,\beta}}(U)
\;\succeq\;
m^2 I + \alpha\,d_1^\*d_1
\quad\text{on }K_\Lambda(r),
\]
with the parameters
\[
m^2 := \frac{c_H}{2},
\qquad
\alpha := \frac{\beta}{n\lambda_\rho}.
\]

---

## 5. Interpretation: an emergent Proca operator on \(1\)-cochains

Define the **massive Maxwell operator**
\[
M := m^2 I + \alpha\,d_1^\* d_1
\quad\text{on }\mathcal C^1(\Lambda;\mathfrak g),
\]
and its restriction \(M_H\) to the vacuum horizontal sector \(H^{(0)}=\ker(d_0^\*)\).

What is conceptually interesting here is *where the mass comes from*:

- \(m^2\) is **geometric** (Haar/Ricci curvature of a compact group),
- the Maxwell stiffness \(\alpha\) is **dynamical** (Wilson coupling),
- and the decomposition is **operator-valued**, preserving link geometry and gauge structure.

This is precisely the sort of “structured coercivity” that is often lost when one scalarizes or uses coarse inequalities early.

---

## 6. Where this can go next (research directions)

1. **Optimize the hinge**: sharpen \(R_W(r)\) via finer overlap bookkeeping, or by choosing a better small-field region than the raw injectivity ball (e.g. plaquette-based rather than link-based).

2. **Group dependence**: compute or bound \(c_H\) explicitly for \(SU(N)\) under the chosen bi-invariant metric normalization, and track how \(m^2\) scales with \(N\).

3. **Anisotropic metrics**: a time/space anisotropic product metric could produce a *direction-dependent* hinge, matching Euclidean-time clustering more directly.

4. **Continuum scaling**: the project later connects \(\eta(a)\) and the OS gap to \(m^2,\alpha\). A refined hinge might improve how the physical gap survives along RG trajectories.

