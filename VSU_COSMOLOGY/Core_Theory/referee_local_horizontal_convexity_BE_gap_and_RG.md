# Local horizontal convexity at fixed cutoff: Haar mass \(\oplus\) Wilson Hessian bound \(\Rightarrow\) Bakry–Émery gap (and one-step RG stability)

## What this document establishes

A precise fixed-cutoff statement of the project’s **curvature \(\Rightarrow\) spectral-gap** mechanism:

1. a *uniform* lower bound on the **horizontal Hessian** of an effective lattice action,
2. a Bakry–Émery curvature-dimension condition on gauge-invariant functions, yielding a volume-uniform Poincaré/spectral gap for the Langevin generator,
3. a standard block-Hessian inequality showing that uniform convexity survives at least one RG blocking step under stronger coupling.

This is a fixed-cutoff mechanism only; it does not solve the \(a\to 0\) problem.

---

## 0. Setup

Configuration manifold \(\mathcal C_\Lambda = SU(N)^{|B|}\) with product bi-invariant metric.

Let \(S_{\mathrm{eff}} = \beta S_W + S_{\mathrm{Haar}}\) with:
- Wilson action \(S_W\) (plaquette sum),
- a linkwise Jacobian action \(S_{\mathrm{Haar}}\) coming from the Haar measure in exponential coordinates,
- \(\beta = 2N/g^2\) (project convention).

Let \(H_U\subset T_U\mathcal C_\Lambda\) be the **horizontal** subspace (orthogonal to gauge orbits).
For gauge-invariant \(f\), \(\nabla f\) is horizontal.

---

## 1. Input A (Haar mass): local uniform convexity on each link

On a normal neighborhood of the identity in each link,
\[
S_{\mathrm{Haar}}(A) = \frac{c_0}{2}\,a^2 g^2 \sum_{b\in B}\|A_b\|^2 + O(a^4 g^4 \|A\|^4),
\]
and hence (by continuity) there is a neighborhood in which
\[
\mathrm{Hess}\,S_{\mathrm{Haar}} \ \succeq\ c_0 a^2 g^2\, I
\]
as a quadratic form on link tangent vectors.

**Status.** Standard Taylor expansion + compactness/continuity; the constant \(c_0>0\) is local and depends on the chosen normal neighborhood.

---

## 2. Input B (Wilson Hessian bound): uniform operator-norm control

There is a volume-uniform constant \(C_V(N)\) such that for every configuration \(U\) and every link tangent vector \(X\),
\[
\big|\langle X,\ \mathrm{Hess}\,S_W(U)\, X\rangle\big|
\ \le\ C_V(N)\,\|X\|^2.
\]

In the project normalization,
\[
C_V(N)=\frac{6}{N},
\]
coming from: each link participates in 6 plaquettes in \(d=4\), and each plaquette contribution has second derivative bounded in operator norm by \(1/N\).

**Status.** This is an explicit uniform bound; the method is standard (trace inequalities + counting plaquettes). The numerical value depends on metric/normalization conventions but the **existence** of such a uniform constant is not in doubt.

---

## 3. Main fixed-cutoff bound: horizontal convexity window

Combine the two inputs on horizontal directions:
\[
\mathrm{Hess}_{\mathrm{hor}}\,S_{\mathrm{eff}}(U)
\ \succeq\ \rho_*(a,g)\,I,
\qquad
\rho_*(a,g) := c_0 a^2 g^2 - \beta C_V(N).
\]

With \(\beta=2N/g^2\) and \(C_V(N)=6/N\),
\[
\rho_*(a,g)= c_0 a^2 g^2 - \frac{12}{g^2}.
\]

Hence \(\rho_*>0\) holds in the strong coupling window
\[
g^4 > \frac{12}{c_0 a^2}.
\]

**Status.** Given Inputs A–B, this is immediate algebra. The restriction to *horizontal directions* is essential.

---

## 4. Bakry–Émery on the physical sector \(\Rightarrow\) Poincaré and spectral gap

On a compact Riemannian manifold, the Bochner identity gives (schematically)
\[
\Gamma_2(f) = \|\nabla^2 f\|^2 + \langle(\mathrm{Ric}+\nabla^2 S)\nabla f,\nabla f\rangle.
\]

For gauge-invariant \(f\), \(\nabla f\in H_U\), so the horizontal lower bound yields
\[
\langle(\mathrm{Ric}+\nabla^2 S)\nabla f,\nabla f\rangle
\ \ge\ (\rho_0 + \rho_*)\,\|\nabla f\|^2,
\]
where \(\rho_0>0\) is the (bi-invariant) Ricci lower bound on \(SU(N)\) (volume-independent on the product).

Thus, on gauge-invariant functions,
\[
\Gamma_2 \ge \rho_{\mathrm{BE}}\,\Gamma,
\qquad
\rho_{\mathrm{BE}} := \rho_0 + \rho_* >0.
\]

Consequences:
- Poincaré inequality with constant \(1/\rho_{\mathrm{BE}}\),
- spectral gap \(\ge \rho_{\mathrm{BE}}\) for the Langevin generator restricted to gauge-invariant functions.

**Status.** Standard Bakry–Émery, with the *only project-specific input* being the horizontal Hessian bound.

---

## 5. One-step RG stability via a block Hessian inequality

Let \((x,y)\) be a fine/coarse split and consider a smooth function \(S(x,y)\) with block Hessian
\[
\nabla^2 S =
\begin{pmatrix}
A & B\\
B^\top & C
\end{pmatrix}.
\]

If \(A\succeq \alpha I\), \(C\succeq \gamma I\), and \(\|B\|\le M\), then the Schur complement yields a lower bound for the coarse effective action (after integrating out \(y\)):
\[
\mathrm{Hess}\,S_{\mathrm{coarse}}(x)\ \succeq\ \alpha - \frac{M^2}{\gamma}.
\]

Applied with \(\alpha=\gamma=\rho_*\) and \(M\sim \beta C_V(N)\), one gets a sufficient condition for one-step preservation of convexity:
\[
\rho_*^2 > M^2
\quad\Longrightarrow\quad
g^4 > \frac{24}{c_0 a^2}
\]
(in the project’s algebraic simplification).

**Status.** The inequality itself is standard; what is nontrivial is tying the constants \(\alpha,\gamma,M\) to lattice gauge-theory structure in a way uniform in volume.

---

## 6. Referee assessment: what is genuinely structural here

- The “Haar mass \(\oplus\) bounded Wilson Hessian \(\Rightarrow\) horizontal convexity” is a clean fixed-cutoff coercivity mechanism.
- The restriction to horizontality is essential and is explicitly used to avoid gauge directions.
- The RG step is a correct quantitative template but currently only a one-step and only in a very-strong-coupling subwindow.

**Non-negotiable limitation.**
As \(a\to 0\), the Haar seed scales like \(a^2 g(a)^2\) while \(\beta\sim g(a)^{-2}\) diverges. Absent an additional \(a\)-independent positive source term, \(\rho_*\) becomes negative. This is not an “artifact”; it is the main obstruction the project acknowledges and tries to address elsewhere (Riccati spine / orbit-space Jacobians).

---

## Internal sources in this project

Primary modules:
- `lemma_unity_curvature_rg_mass_gap.md`
- `UNIFY_01_Wilson_Hessian_and_Haar_Mass.md`
- `Extract_04_Core_Local_Horizontal_Curvature_Theorem_for_Lattice_Yang_Mills.md`
- `A_local_BE_curvature.md`
- `lemma_unity_stitched_curvature_rg.md` / `01_curvature_rg_riccati_hotrg.md` (for RG framing)
