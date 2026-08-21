# Haar Geometry, Jacobians, and an “Emergent Mass” from Curvature

**Purpose.** Extract the project’s “Haar mass mechanism” idea:  
even before dynamics, the **geometry of compact gauge groups** and the **Jacobian of the exponential map** can act like a built-in confining quadratic potential—i.e. a **mass-like curvature floor**—which can be upgraded into functional inequalities (Poincaré/LSI) via Bakry–Émery.

This combines content from `SYNTH_P04_haar_geometry_supplement.md`, `SYNTH_P10_log_sobolev.md`, and `UNIF_HAAR_SPECTRAL_SYNTHESIS.md`, plus the lattice geometric setup in Part II.

---

## 1. Configuration geometry is already curved

On a finite lattice with link variables \(U_e\in SU(N)\), the configuration manifold is
\[
\mathscr{A} = SU(N)^{E},
\]
with product bi-invariant metric. Compact simple Lie groups with bi-invariant metrics are Einstein:
\[
\mathrm{Ric}_G = \kappa\, g_G,\qquad \kappa>0.
\]
Hence on the product
\[
\mathrm{Ric}_{\mathscr{A}} = \kappa\, g_{\mathscr{A}}.
\]

**Meaning.** Even the “free” Haar measure lives on a positively curved space.  
Positive Ricci curvature is exactly what Bakry–Émery needs to produce functional inequalities.

---

## 2. The exponential Jacobian behaves like a quadratic potential

Near identity \(U=\exp(X)\) with \(X\in\mathfrak{su}(N)\), Haar measure can be written as
\[
d\mu_{\mathrm{Haar}}(\exp X) = J(X)\, dX,
\]
with Jacobian
\[
J(X)=\det\!\left(\frac{\sinh(\mathrm{ad}_X/2)}{\mathrm{ad}_X/2}\right).
\]
Expanding at \(X=0\),
\[
\log J(X)
=
- c_H\,\|X\|^2 + O(\|X\|^4),
\qquad c_H>0,
\]
with a group-dependent \(c_H\) (normalization-dependent; the project quotes a coefficient proportional to \(N/12\) in a common convention).

**Interpretation.** In local coordinates, Haar measure looks like
\[
d\mu_{\mathrm{Haar}}(\exp X) \approx \exp(-c_H\|X\|^2)\, dX.
\]
That is a Gaussian-like weight: **pure measure geometry is already “massive.”**

---

## 3. Wilson action Hessian: positivity on physical (horizontal) modes

For Wilson action
\[
S_W(U) = \beta\sum_{p}\left(N-\Re\mathrm{Tr}(U_p)\right),
\]
expand near identity. Writing \(U_e=\exp(X_e)\) and the plaquette angles \(\theta_p\) as a discrete curvature,
\[
S_W \approx \frac{\beta}{2}\sum_p \|\theta_p\|^2 + O(\|X\|^3).
\]

At the quadratic level,
\[
\theta = d_1 X
\quad\Rightarrow\quad
S_W^{(2)}(X) = \frac{\beta}{2}\langle d_1 X, d_1 X\rangle
= \frac{\beta}{2}\langle X, d_1^\ast d_1 X\rangle.
\]

Gauge directions are (linearized) coboundaries \(X=d_0\phi\), and \(d_1d_0=0\), so gauge directions sit in \(\ker(d_1)\).  
On the orthogonal complement (horizontal/physical modes), and after dealing with harmonic/toroidal zero-modes appropriately, one expects a spectral gap:
\[
\langle X, d_1^\ast d_1 X\rangle \ge c_W \|X\|^2
\quad \text{for }X\in (\mathrm{im}\,d_0)^\perp.
\]

**Meaning.** Wilson’s action is *flat* along gauge directions (as it must be), but **strictly convex in physical directions** near the identity sector.

---

## 4. Bakry–Émery curvature: add geometry + convexity

For a Gibbs measure
\[
d\mu \propto e^{-S}\,d\mathrm{vol}_{g},
\]
the Bakry–Émery tensor is
\[
\mathrm{Ric}_\mu := \mathrm{Ric}_g + \nabla^2 S.
\]

In the present setting:
- \(\mathrm{Ric}_g\) contributes \(\kappa g\) from Haar geometry,
- \(\nabla^2 S_W\) contributes \(\beta c_W g\) on physical directions (near identity),
- the exponential Jacobian picture suggests an additional effective quadratic concentration near the identity in coordinate descriptions.

So the “mass from curvature” slogan is:
\[
\mathrm{Ric}_\mu\vert_{\mathrm{phys}}
\gtrsim
(\kappa + \beta c_W)\,g.
\]

Once you have \(\mathrm{Ric}_\mu\ge\rho g\), Bakry–Émery \(\Gamma_2\) theory gives:

- Poincaré inequality with constant \(1/\rho\),
- log-Sobolev inequality with constant \(2/\rho\),
- spectral gap \(\lambda_1\ge \rho\) for the associated diffusion generator.

This is the project’s route from **group geometry** to **uniform functional inequalities**.

---

## 5. Why this is potentially bigger than YM

This “Haar/Jacobian \(\to\) quadratic confinement” idea generalizes:

- any compact gauge group (or even compact homogeneous spaces) has a built-in curvature scale;
- local coordinate Jacobians encode “entropic potentials”;
- combining geometric curvature and action convexity is exactly the Bakry–Émery playbook.

So this part of the project might seed a larger theory:

> **Entropic mass generation from group geometry + convexity, formalized via curvature-dimension bounds.**

That’s a lovely intersection of:
- stochastic analysis (diffusions and functional inequalities),
- differential geometry (Ricci curvature, Jacobians),
- lattice gauge theory (Wilson action and discrete Hodge theory).

---

## 6. Technical pressure points (to strengthen the claim)

1. Track normalization conventions carefully (the coefficient in \(\log J(X)\) is metric-dependent).
2. Make the “positive on horizontals” statement uniform and global (not just near identity).
3. Handle torons/harmonic 1-forms cleanly in periodic volumes (global gauge fixing or quotienting).
4. Clarify the relation between:
   - positivity from \(\mathrm{Ric}_g\) (intrinsic curvature),
   - and positivity from coordinate Jacobians (entropic weight).

Those are fixable, and tightening them would make the “Haar mass mechanism” a robust, reusable lemma.
