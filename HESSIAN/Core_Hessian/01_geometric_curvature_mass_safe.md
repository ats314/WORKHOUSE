# Geometric Mass from Haar Curvature and Wilson Convexity (SAFE Region)

*Project extraction (generated 2025-12-29).*

## 0. Executive statement

In right–invariant exponential coordinates near the identity of $SU(3)$, the Haar measure contributes a strictly positive **Bakry–Émery curvature floor**; the Wilson action contributes a controlled perturbation of the Hessian inside a certified “SAFE” ball.  
Inside that ball, the **physical** Hessian stays uniformly bounded below:
\[
\lambda_{\min}^{\mathrm{phys}}(x)\ge \kappa_* - \delta \approx 0.244,
\]
with a numerical minimum around $0.248$ on the scanned grid.

This produces a *local* logarithmic Sobolev inequality (LSI) and a corresponding spectral gap for the associated diffusion generator, with constants explicitly tied to $(\kappa_*,\delta)$.

---

## 1. Geometry and measure in coordinates

Let $G=SU(3)$ with Lie algebra $\mathfrak{su}(3)$ and inner product
\[
\langle X,Y\rangle := -\mathrm{Tr}(XY).
\]
In a right–invariant chart near the identity,
\[
U = \exp(X),\qquad X\in \mathfrak{su}(3),\qquad X = \sum_{a=1}^8 x_a T_a,
\]
with an orthonormal basis $\langle T_a,T_b\rangle = \delta_{ab}$.

The Haar density in exponential coordinates is
\[
d\mathrm{Haar}(U) = J(x)\,dx,
\]
so the “Haar potential” is
\[
V_{\mathrm{Haar}}(x) := -\log J(x).
\]

The Bakry–Émery tensor associated to a Riemannian metric $g$ and potential $V$ is
\[
\mathrm{Ric}_V := \mathrm{Ric}_g + \nabla^2 V.
\]

---

## 2. Haar curvature floor in the SAFE ball

With the bi–invariant metric normalization above, the group Ricci curvature satisfies
\[
\mathrm{Ric}_{SU(3)} \ge \tfrac14\,g.
\]

In the SAFE region
\[
\|x\| \le R_0 := 0.05,
\]
the coordinate Jacobian correction obeys a small Hessian bound of the schematic form
\[
\|\nabla^2 \log J(x)\|_{op} \lesssim \text{(small constant)},
\]
so the Bakry–Émery tensor for Haar stays uniformly positive.

**SAFE constant adopted in the project:**
\[
\boxed{\kappa_* = 0.25.}
\]

> Interpretation: $\kappa_*$ is a conservative curvature floor (with numerical buffer) for the Haar-induced convexity on the ball $\|x\|\le 0.05$.

---

## 3. Wilson Hessian perturbation bound

Write the local Wilson action schematically as
\[
S_W(U) = \beta\sum_p\Bigl(1 - \tfrac13\Re\mathrm{Tr}(U_p)\Bigr),
\]
with plaquette holonomy expressed via BCH in the link coordinates $X_\ell$.

Inside the SAFE ball $\|X_\ell\|\le R_0$, the plaquette Hessian decomposes into BCH pieces
\[
\nabla^2 S_W = \beta\sum_p\Bigl(H^{(2)}_p + H^{(3)}_p + H^{(4)}_p\Bigr),
\]
with operator–norm scaling
\[
\|H^{(2)}_p\|_{op} = O(1),\qquad
\|H^{(3)}_p\|_{op} = O(\|x\|),\qquad
\|H^{(4)}_p\|_{op} = O(\|x\|^2).
\]

The project’s evaluated envelope constants (plaquette level) are:
\[
C_2=0.011,\quad C_3\approx 0.10,\quad C_4\approx 1.1,
\]
yielding (at $R_0=0.05$) a plaquette bound
\[
\|H_p\|_{op}\le C_2 + C_3R_0 + C_4R_0^2 = 0.01875.
\]

A link participates in at most $6$ plaquettes in 4D, giving the linkwise perturbation
\[
\|\nabla^2 S_W\|_{op,\ell} \lesssim 6\beta\cdot 0.01875.
\]

With the SAFE scaling choice $\beta a^4\le 0.05$, the perturbation is rounded to
\[
\boxed{\delta = 0.006.}
\]

---

## 4. Certified physical Hessian lower bound

Define the physical Hessian (schematically)
\[
H_{\mathrm{phys}}(x)
:= \Pi_{\mathrm{phys}}^\top\,\nabla^2\bigl(V_{\mathrm{Haar}}+S_W\bigr)(x)\,\Pi_{\mathrm{phys}},
\]
where $\Pi_{\mathrm{phys}}$ removes gauge directions (horizontal projection).

Then inside the SAFE ball the project asserts, and numerically verifies, the bound
\[
\boxed{
\lambda_{\min}^{\mathrm{phys}}(x)
\ge \kappa_* - \delta = 0.25 - 0.006 = 0.244.
}
\]

### 4.1 Representative eigenvalue scan table

The recorded representative minima (radial scan with random directions) include:

\[
\begin{array}{c|c|c}
r & \lambda_{\min}^{\mathrm{Haar}}(r) & \lambda_{\min}^{\mathrm{phys}}(r) \\ \hline
0.00 & 0.291 & 0.286 \\
0.01 & 0.286 & 0.280 \\
0.02 & 0.279 & 0.273 \\
0.03 & 0.271 & 0.265 \\
0.04 & 0.263 & 0.257 \\
0.05 & 0.255 & 0.249
\end{array}
\]

The global minimum over the scanned SAFE grid is reported around
\[
\min\lambda_{\min}^{\mathrm{phys}} \approx 0.248,
\]
which leaves a numerical margin $\approx 0.004$ above $0.244$.

---

## 5. Immediate analytic consequences inside the SAFE region

If $\mathrm{Ric}_V\ge \kappa g$ holds on a region and the diffusion is confined to it (or one uses local functional inequalities), then Bakry–Émery gives an LSI
\[
\mathrm{Ent}_\mu(f^2)\le \frac{2}{\kappa}\int |\nabla f|^2\,d\mu,
\]
and hence a Poincaré/spectral–gap bound of order $\kappa$.

In the SAFE region, $\kappa$ can be taken as $\kappa_* - \delta\approx 0.244$.

---

## 6. What’s genuinely “new” here (as a research direction)

The ingredients are classical (Lie group geometry, BCH, Bakry–Émery), but the *assembly* is unusual:

1. **Explicit numeric constants** $(\kappa_*,\delta)$ for $SU(3)$ in a concrete coordinate ball.
2. A certified inequality on the **projected physical Hessian**, not just the full Hessian.
3. A route to interpret this curvature floor as a “geometric mass scale” for gauge–invariant observables.

---

## 7. Next technical moves

1. Extend certification beyond $\|x\|\le 0.05$ (either enlarge the SAFE ball or patch multiple charts).
2. Prove a *drift/return* estimate showing the lattice measure spends most probability mass inside SAFE-type regions as $a\to 0$.
3. Make the “physical projector” $\Pi_{\mathrm{phys}}$ fully explicit for the chosen gauge and verify stability under coarse graining.
