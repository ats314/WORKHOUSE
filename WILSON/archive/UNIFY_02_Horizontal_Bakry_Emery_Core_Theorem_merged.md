# UNIFY 02 — The Core “Horizontal Bakry–Émery Curvature” Mechanism for Lattice Gauge Theory

## Purpose of this extract

This note extracts the project’s **central geometric move**:

> Instead of demanding Bakry–Émery curvature positivity in *all* directions on \(M_\Lambda\),
> impose it only on the **horizontal (physical)** directions, and only where it can be proven (a small-field region).
> For **gauge-invariant observables**, this is enough because their gradients are automatically horizontal.

This is the bridge that turns local geometric convexity (Haar + Wilson) into a **local curvature–dimension condition** \(CD(\rho_{\mathrm{loc}},\infty)\) *in the gauge-invariant sector*.

---

## 1. Configuration space, gauge action, and the horizontal bundle

Let \(M_\Lambda = G^{E(\Lambda)}\) with product bi-invariant metric \(g_\Lambda\).
The lattice gauge group is \(\mathcal{G}_\Lambda = G^{V(\Lambda)}\), acting by
\[
(g\cdot U)_\ell = g_{x}\,U_\ell\,g_{y}^{-1}
\quad \text{for } \ell=(x\to y).
\]

For \(U\in M_\Lambda\), the orbit \(\mathcal O_U=\mathcal G_\Lambda\cdot U\) has tangent space
\[
V_U := T_U \mathcal O_U \subset T_UM_\Lambda,
\]
the **vertical space** (pure-gauge directions). Define the **horizontal space**
\[
H_U := V_U^\perp \subset T_UM_\Lambda
\]
with respect to \(g_\Lambda\), so that
\[
T_UM_\Lambda = H_U \oplus V_U.
\]

---

## 2. Gauge-invariant observables have horizontal gradients

Let
\[
\mathcal A_\Lambda^{\mathrm{inv}} := \{ f\in C^\infty(M_\Lambda)\;:\; f(g\cdot U)=f(U)\ \forall g\in\mathcal G_\Lambda\}.
\]

If \(f\in\mathcal A_\Lambda^{\mathrm{inv}}\), then \(df_U\) annihilates vertical vectors, hence
\[
\nabla f(U)\in H_U
\quad\forall U.
\]
Equivalently, the carré du champ for gauge-invariant \(f\) only sees horizontal derivatives:
\[
\Gamma_\Lambda(f)(U)=|\nabla f(U)|^2 = |\nabla^H f(U)|^2.
\]

This single fact is what makes a *horizontal-only* curvature bound meaningful for physics.

---

## 3. Bakry–Émery curvature, but restricted to horizontals

Let \(\mu_\Lambda\) be the Gibbs measure
\[
d\mu_\Lambda(U) = Z_\Lambda^{-1}\,e^{-S_\Lambda(U)}\,d\mathrm{vol}_{g_\Lambda}(U),
\]
with generator
\[
L_\Lambda f = \Delta_{g_\Lambda} f - \langle \nabla S_\Lambda,\nabla f\rangle.
\]

The Bochner–Bakry–Émery identity gives
\[
\Gamma_{2,\Lambda}(f)
= \|\nabla^2 f\|_{\mathrm{HS}}^2 + \mathrm{Ric}_{\mu_\Lambda}(\nabla f,\nabla f),
\qquad
\mathrm{Ric}_{\mu_\Lambda}:=\mathrm{Ric}_{g_\Lambda}+\nabla^2 S_\Lambda.
\]

### Horizontal curvature condition

Fix an open region \(\Omega\subset M_\Lambda\). We say \(\mu_\Lambda\) has **horizontal Bakry–Émery curvature \(\ge \rho\) on \(\Omega\)** if
\[
\mathrm{Ric}_{\mu_\Lambda}(U)(W,W)\ \ge\ \rho\,|W|^2
\quad \forall U\in \Omega,\ \forall W\in H_U.
\]

### Consequence for gauge-invariant observables

If \(f\in \mathcal A_\Lambda^{\mathrm{inv}}\) then \(\nabla f(U)\in H_U\), hence on \(\Omega\)
\[
\Gamma_{2,\Lambda}(f)(U)
\ge \mathrm{Ric}_{\mu_\Lambda}(U)(\nabla f(U),\nabla f(U))
\ge \rho\,\Gamma_\Lambda(f)(U).
\]
So a horizontal curvature bound implies the **local curvature–dimension condition**
\(CD(\rho,\infty)\) *when tested on gauge-invariant observables*.

---

## 4. The core local theorem near the vacuum

Let \(U^{(0)}\) be the trivial configuration. Consider a small metric ball
\[
B_r(U^{(0)}) := \{U: d_{g_\Lambda}(U,U^{(0)})\le r\}.
\]

### Key input A: group Ricci curvature

If \(\mathrm{Ric}_G\ge \kappa_G g_G\) on the single-link group \((G,g_G)\) with \(\kappa_G>0\), then the product metric gives
\[
\mathrm{Ric}_{g_\Lambda} \ge \kappa_G\, g_\Lambda
\]
(pointwise, as quadratic forms), uniformly in \(\Lambda\).

### Key input B: Wilson Hessian is nonnegative on physical directions at the vacuum

At \(U^{(0)}\), the Wilson action has Hessian \(2c_W d_1^*d_1\ge 0\), hence in particular
\[
\nabla^2 S_W(U^{(0)})(W,W)\ge 0
\quad \forall W\in T_{U^{(0)}}M_\Lambda.
\]

After projecting away gauge directions, the remaining degeneracies correspond to harmonic \(1\)-forms; this is the motivation for pairing Wilson with the compact-group curvature.

### Key input C: other action terms are a controlled perturbation

If the “additional” part of the action satisfies a lower Hessian bound
\[
\nabla^2 S_{\mathrm{add}}(U)(W,W)\ \ge\ -C_{\mathrm{add}}\,|W|^2,
\]
then at \(U^{(0)}\)
\[
\mathrm{Ric}_{\mu_\Lambda}(U^{(0)})(W,W)
\ge (\kappa_G - C_{\mathrm{add}})\,|W|^2
\qquad \forall W\in T_{U^{(0)}}M_\Lambda.
\]

### Continuity upgrade to a small-field ball

Because \(\mathrm{Ric}_{\mu_\Lambda}\) varies continuously with \(U\), the strict positivity at \(U^{(0)}\) extends to a small ball:

> **Local Horizontal Curvature Theorem (schematic form).**  
> If \(\kappa_G>C_{\mathrm{add}}\), then there exist \(r>0\) and \(\rho_{\mathrm{loc}}>0\), independent of \(\Lambda\), such that on \(B_r(U^{(0)})\)
> \[
> \mathrm{Ric}_{\mu_\Lambda}(U)(W,W)\ge \rho_{\mathrm{loc}}\,|W|^2
> \quad \forall W\in H_U.
> \]
> Consequently, \(CD(\rho_{\mathrm{loc}},\infty)\) holds on \(B_r(U^{(0)})\) for all gauge-invariant observables.

Uniformity in \(\Lambda\) is plausible because:

- the Ricci term is a product-group constant,
- Wilson’s Hessian is local (each link appears in finitely many plaquettes),
- the perturbation bound is assumed uniform.

---

## 5. Why this is the “high-leverage” idea in the project

The horizontal restriction does two conceptual jobs at once:

1. **It matches the quotient geometry.**  
   Gauge-invariant observables are functions on the orbit space \(M_\Lambda/\mathcal G_\Lambda\) (at least on the regular set), and their gradients live in the horizontal bundle. A horizontal Bakry–Émery bound is exactly the curvature condition relevant to that quotient Dirichlet form.

2. **It avoids fighting gauge degeneracy head-on.**  
   The Wilson action *must* be flat along gauge orbits, so a full-space Hessian lower bound is impossible. The “horizontal-only” move is the correct geometric way to respect the symmetry.

From a theory-building point of view, this is the cleanest candidate for a general principle:

> **Curvature–dimension on symmetry-reduced directions is the right analytic object for gauge-invariant physics.**

The next step (UNIFY 03) is to upgrade this *local* \(CD\) control into *global* functional inequalities via Lyapunov drift.

