---
title: "A Smooth Fundamental-Character Lyapunov Atom on SU(N) Lattices"
subtitle: "Exact affine Laplacian drift for the plaquette proxy"
status: "Reusable analytic lemma"
date: "2025-12-31"
---

# 0. Summary

Distance-squared on a compact Lie group has global nonsmoothness (cut locus).
A globally smooth replacement is the fundamental-character proxy
\[
\widetilde z(U):=1-\frac1N\Re\mathrm{Tr}(U),\qquad U\in \mathrm{SU}(N).
\]

On a lattice, the averaged plaquette proxy produces an **exact affine Laplacian identity**
with **volume-uniform constants**. This is a clean “Lyapunov atom” for drift patching.

---

# 1. Group input: fundamental character is a Laplacian eigenfunction

Let $G=\mathrm{SU}(N)$ with a fixed bi-invariant Riemannian metric, and let $\Delta_G$ be the corresponding Laplace–Beltrami operator.

Assume the representation-theoretic eigenfunction identity
\[
\Delta_G\,\Re\mathrm{Tr}(U)=-\lambda_{\mathrm{fund}}\ \Re\mathrm{Tr}(U),
\qquad \lambda_{\mathrm{fund}}>0.
\tag{1.1}
\]

Define
\[
\widetilde z(U):=1-\frac1N\Re\mathrm{Tr}(U).
\tag{1.2}
\]
Then by linearity,
\[
\Delta_G \widetilde z(U)= -\lambda_{\mathrm{fund}}\widetilde z(U)+\lambda_{\mathrm{fund}}.
\tag{1.3}
\]

---

# 2. Lattice setup

Let $\Lambda$ be a finite 4D lattice region (torus or box).

- Configuration manifold: $M_\Lambda := G^{E(\Lambda)}$.
- Product Laplacian: $\Delta_\Lambda := \sum_{\ell\in E(\Lambda)}\Delta_\ell$,
  where $\Delta_\ell$ acts as $\Delta_G$ on the $\ell$-th link variable.

For plaquette $p$, let $U_p(U)$ denote the plaquette holonomy and define the plaquette proxy
\[
\widetilde z_p(U) := \widetilde z\!\big(U_p(U)\big).
\tag{2.1}
\]

Define the averaged proxy and its affine shift:
\[
\overline z_\Lambda(U):=\frac{1}{|P(\Lambda)|}\sum_{p}\widetilde z_p(U),
\qquad
\overline V_\Lambda(U):=1+\overline z_\Lambda(U).
\tag{2.2}
\]

---

# 3. Lemma: exact affine Laplacian identity

## Lemma 3.1 (Exact Laplacian drift for $\overline V_\Lambda$)

Assume (1.1). Then
\[
\boxed{
\Delta_\Lambda \overline V_\Lambda
=
-\lambda\,\overline V_\Lambda + b,
\qquad
\lambda:=4\lambda_{\mathrm{fund}},
\qquad
b:=2\lambda.
}
\tag{3.1}
\]

### Proof

Fix a plaquette $p$ with boundary links $\partial p=\{\ell_1,\ell_2,\ell_3,\ell_4\}$.
Freeze all links except $U_{\ell}$ for one $\ell\in\partial p$. Then $U_p(U)$ becomes a function of $U_\ell$ alone:
\[
U_p(U)=A\,U_\ell\,B \quad\text{or}\quad U_p(U)=A\,U_\ell^{-1}\,B
\]
for some fixed $A,B\in G$.

Because the metric is bi-invariant, left and right translations are isometries, so they preserve the Laplacian.
Inversion is also an isometry. Therefore, as a function of $U_\ell$,
\[
\Delta_\ell \Re\mathrm{Tr}(U_p(U))
=
-\lambda_{\mathrm{fund}}\ \Re\mathrm{Tr}(U_p(U)).
\]
By linearity (using (1.2)),
\[
\Delta_\ell \widetilde z_p(U)= -\lambda_{\mathrm{fund}}\widetilde z_p(U)+\lambda_{\mathrm{fund}}.
\]

Summing over the four boundary links,
\[
\Delta_\Lambda \widetilde z_p
=
\sum_{\ell\in\partial p}\Delta_\ell \widetilde z_p
=
-4\lambda_{\mathrm{fund}}\widetilde z_p + 4\lambda_{\mathrm{fund}}.
\]
Average over $p$ and use that $\Delta_\Lambda 1=0$:
\[
\Delta_\Lambda \overline V_\Lambda
=
\Delta_\Lambda\!\left(1+\frac{1}{|P|}\sum_p\widetilde z_p\right)
=
-4\lambda_{\mathrm{fund}}\cdot \frac{1}{|P|}\sum_p \widetilde z_p
+4\lambda_{\mathrm{fund}}.
\]
Since $\frac{1}{|P|}\sum_p\widetilde z_p = \overline V_\Lambda-1$, we obtain
\[
\Delta_\Lambda \overline V_\Lambda
=
-4\lambda_{\mathrm{fund}}(\overline V_\Lambda-1)+4\lambda_{\mathrm{fund}}
=
-\lambda \overline V_\Lambda + 2\lambda,
\]
i.e. (3.1). $\square$

---

# 4. Corollary: a uniform affine Lyapunov drift bound for Langevin dynamics

For the Langevin generator
\[
L = \Delta_\Lambda - \langle\nabla S,\nabla(\cdot)\rangle,
\]
one immediately has
\[
L\overline V_\Lambda
=
\Delta_\Lambda \overline V_\Lambda - \langle\nabla S,\nabla \overline V_\Lambda\rangle
\ \le\
\Delta_\Lambda \overline V_\Lambda
=
-\lambda \overline V_\Lambda + b,
\]
provided the pairing term is nonnegative (as occurs for Wilson-type actions aligned with the same plaquette proxy).

The constants $(\lambda,b)$ are **independent of volume**.

---

# 5. Metric normalization: explicit $\lambda_{\mathrm{fund}}$ via Casimir

Under the common convention $\Delta_G = -\sum_a X_a^2$ with $\{X_a\}$ orthonormal,
Laplacian eigenvalues coincide with quadratic Casimir values.

If (as in SU(2) Laplacian checks) $\lambda_{\mathrm{fund}} = 4C_2(\mathrm{fund})$, then
\[
\lambda_{\mathrm{fund}}=\frac{2(N^2-1)}{N},
\qquad
\lambda=\frac{8(N^2-1)}{N},
\qquad
b=\frac{16(N^2-1)}{N}.
\]

This pins the constants for SU(2) and SU(3) once the metric normalization is fixed.

---

# 6. Why this lemma is useful

- It removes cut-locus nonsmoothness from naive distance-squared Lyapunov candidates.
- It yields an **exact** affine structure (not “$\lesssim$”) with explicit constants.
- It is immediately compatible with local-to-global Poincaré/LSI patching via Lyapunov drift.

This is a high-leverage “atom” for the global functional inequality engine.
