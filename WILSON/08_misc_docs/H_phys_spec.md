# Code-level definition of \(H_{\rm phys}\)

This note pins down what the draft currently calls “\(\Pi_{\rm phys}\)” and “\(H_{\rm phys}\)” in an algorithmic, reproducible way.

## 1. Cluster degrees of freedom

Choose a finite oriented cluster graph
\[
\mathcal C=(V_{\mathcal C},E_{\mathcal C}),
\]
with \(|V_{\mathcal C}|=n_V\) vertices and \(|E_{\mathcal C}|=n_E\) oriented edges (links).

A cluster configuration is
\[
U=(U_e)_{e\in E_{\mathcal C}}\in \mathrm{SU}(3)^{n_E}.
\]

In right–invariant exponential coordinates, each link is
\[
U_e=\exp(X_e),\qquad X_e=\sum_{a=1}^8 x_{e,a}T_a\in\mathfrak{su}(3),
\]
where \(\{T_a\}_{a=1}^8\) is an orthonormal anti-Hermitian basis.

The flattened coordinate vector is
\[
x = (x_{e,a}) \in \mathbb R^{8n_E}.
\]

## 2. Vertical (gauge) tangent directions \( \mathrm{Im}\,D_0(U)\)

A (site) gauge parameter is
\[
\phi=(\phi_v)_{v\in V_{\mathcal C}} \in \mathfrak{su}(3)^{n_V}.
\]

The derivative of the gauge action gives a linear map
\[
D_0(U):\ \mathfrak{su}(3)^{n_V}\to \mathfrak{su}(3)^{n_E}
\]
defined on each oriented edge \(e=(v\to w)\) by
\[
(D_0(U)\phi)_e = \phi_v - \mathrm{Ad}_{U_e}\phi_w.
\]

In a fixed orthonormal basis, \(D_0(U)\) is a real matrix of shape \((8n_E)\times(8n_V)\) with block row for edge \(e\):
- an \(+I_8\) block in the columns of \(v=\mathrm{tail}(e)\),
- a \(-\mathrm{Ad}_{U_e}\) block in the columns of \(w=\mathrm{head}(e)\).

The vertical subspace is \(\mathrm{Im}\,D_0(U)\).

## 3. Horizontal (physical) subspace and projector \( \Pi_{\rm phys}(x)\)

With the product Haar metric and an orthonormal basis, the horizontal subspace is the orthogonal complement of the vertical:
\[
H_U \;:=\; \bigl(\mathrm{Im}\,D_0(U)\bigr)^\perp \;=\; \ker D_0(U)^\top .
\]

Algorithmically:
1. Build \(U(x)\) from \(x\) via matrix exponentials.
2. Build the real matrix \(D_0(U(x))\).
3. Compute an orthonormal basis \(Q(x)\) for \(\ker D_0(U(x))^\top\) via SVD.
4. Set
\[
\Pi_{\rm phys}(x) := Q(x).
\]

So \(\Pi_{\rm phys}(x)\) is a tall matrix of shape \((8n_E)\times m\) with orthonormal columns spanning \(H_U\).

> If you are already parametrizing in \(\mathfrak{su}(3)\), “projected to the traceless tangent subspace” is automatic.

## 4. Physical Hessian \(H_{\rm phys}\)

Let \(V_{\rm tot}(x)\) be the scalar potential whose curvature you want to scan (e.g. Haar chart potential + Wilson action, or Bakry–Émery tensor contracted against the metric).

Compute the full Hessian
\[
H_{\rm tot}(x) := \nabla^2 V_{\rm tot}(x)\in\mathbb R^{8n_E\times 8n_E}.
\]

Then the projected (physical) Hessian is
\[
H_{\rm phys}(x) := \Pi_{\rm phys}(x)^\top\, H_{\rm tot}(x)\,\Pi_{\rm phys}(x).
\]

The scan target is
\[
\lambda_{\min}^{\rm phys}(x) = \lambda_{\min}\bigl(H_{\rm phys}(x)\bigr).
\]

## 5. Optional: Schur complement (marginalization / “effective single-link” Hessian)

If your scan uses an *effective* Hessian after eliminating internal/fast variables \(y\) from a multi-link cluster, then in a quadratic approximation you use the Schur complement.

Partition the flattened variables as \((x_{\rm keep},x_{\rm drop})\) and block the Hessian as
\[
H_{\rm tot}=\begin{pmatrix}A&B\\B^\top&C\end{pmatrix}.
\]

Define
\[
H_{\rm eff} := A - B\,C^{+}\,B^\top,
\]
with \(C^{+}\) the pseudoinverse (or inverse after gauge-fixing).

Then project:
\[
H_{\rm phys,eff} := \Pi_{\rm phys,keep}^\top H_{\rm eff}\,\Pi_{\rm phys,keep}.
\]

## 6. Reference implementation

See `h_phys_tools.py` for:
- \(D_0(U)\) construction (gauge vertical operator),
- \(\Pi_{\rm phys}\) as a nullspace basis for \(D_0(U)^\top\),
- projection \(H\mapsto \Pi^\top H\Pi\),
- Schur complement helper.
