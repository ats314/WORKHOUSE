# Wilson vacuum expansion \(\Rightarrow\) discrete Maxwell stiffness

\begin{center}
\textbf{Extracted from the lattice gauge appendices: vacuum linearization, Hessian identification, and discrete cochain operators.}
\end{center}

## 1. Configuration manifold and Wilson action

On a finite periodic lattice \(\Lambda_L\), a (link) gauge field is a point
\[
U = (U_b)_{b\in E(\Lambda_L)} \in M_{\Lambda_L} := G^{E(\Lambda_L)}
\]
with product Riemannian metric induced from a bi-invariant metric on the compact Lie group \(G\).

For an oriented plaquette \(p=(x;\mu,\nu)\), \(\mu<\nu\), the plaquette holonomy is
\[
U_p(U) := U_{x,\mu}\,U_{x+\hat e_\mu,\nu}\,U_{x+\hat e_\nu,\mu}^{-1}\,U_{x,\nu}^{-1} \in G.
\]
The (finite-volume) Wilson action is
\[
S_{\Lambda_L,\beta}(U) := \sum_{p\in P(\Lambda_L)} \Phi_\beta\big(U_p(U)\big),
\qquad
\Phi_\beta(V) := \beta\Bigl(1-\tfrac1n\Re\mathrm{Tr}(V)\Bigr).
\]
The vacuum configuration is \(U^{(0)}\) with \(U_b^{(0)}=\mathbf 1\) for all links \(b\).

The main point of this extract is that the quadratic expansion of \(S_{\Lambda_L,\beta}\) at \(U^{(0)}\) is exactly a discrete Maxwell energy.

---

## 2. A geodesic chart through the vacuum

Right-trivialize tangent vectors at the vacuum:
\[
T_{U^{(0)}}M_{\Lambda_L} \simeq \mathfrak g^{E(\Lambda_L)} \equiv \mathcal C^1(\Lambda_L;\mathfrak g).
\]
Given a \(1\)-cochain \(X=(X_b)_{b\in E}\in\mathcal C^1\), consider the linkwise exponential curve
\[
(\gamma_X(t))_b := \exp(tX_b).
\]
Because each component \(t\mapsto\exp(tX_b)\) is a one-parameter subgroup in a bi-invariant metric, \(\gamma_X\) is a product geodesic with
\(
\dot\gamma_X(0)\leftrightarrow X.
\)

---

## 3. Linearization of plaquette holonomy

Define the discrete coboundary \(d_1:\mathcal C^1\to\mathcal C^2\) using the oriented plaquette boundary
\(
\partial p = (x,\mu)+(x+\hat e_\mu,\nu)-(x+\hat e_\nu,\mu)-(x,\nu)
\)
so that
\[
(d_1X)_p = X_{x,\mu}+X_{x+\hat e_\mu,\nu}-X_{x+\hat e_\nu,\mu}-X_{x,\nu}.
\]

**Key linearization.** Along the vacuum geodesic \(\gamma_X(t)\),
\[
\left.\frac{d}{dt}\right|_{t=0} U_p(\gamma_X(t)) = (d_1X)_p \in \mathfrak g.
\]
*Reason:* differentiate the product defining \(U_p\) at \(t=0\); each factor is the identity at \(0\), so the derivative is a signed sum of the link velocities, with minus signs for inverted links.

---

## 4. Hessian of the single-plaquette potential at the identity

Let \(Y\in\mathfrak g\) and \(\eta_Y(t)=\exp(tY)\) (a geodesic in \(G\)). The Riemannian Hessian at \(\mathbf 1\) is
\[
\nabla^2\Phi_\beta(\mathbf 1)[Y,Y]=\left.\frac{d^2}{dt^2}\right|_{t=0}\Phi_\beta\big(\exp(tY)\big).
\]
Using the Taylor expansion of \(\Re\mathrm{Tr}(\exp(tA))\) for \(A=d\rho(Y)\in\mathfrak u(n)\) and the metric normalization
\(
|Y|_{\mathfrak g}^2 = -\Re\mathrm{Tr}(A^2),
\)
one finds
\[
\nabla\Phi_\beta(\mathbf 1)=0,
\qquad
\nabla^2\Phi_\beta(\mathbf 1)[Y,Z] = \alpha_W\langle Y,Z\rangle_{\mathfrak g},
\qquad
\alpha_W:=\beta/n.
\]

---

## 5. The vacuum Hessian is the Maxwell operator

Differentiate the full action twice along \(\gamma_X(t)\):
\[
\nabla^2 S_{\Lambda_L,\beta}(U^{(0)})[X,X]
=\left.\frac{d^2}{dt^2}\right|_{t=0} \sum_{p}\Phi_\beta\big(U_p(\gamma_X(t))\big).
\]
Because \(\nabla\Phi_\beta(\mathbf 1)=0\), only the Hessian term contributes, giving
\[
\nabla^2 S_{\Lambda_L,\beta}(U^{(0)})[X,X]
=\sum_p \nabla^2\Phi_\beta(\mathbf 1)\big[(d_1X)_p,(d_1X)_p\big]
=\alpha_W\,\|d_1X\|_{\mathcal C^2}^2.
\]
Equivalently, as an operator on \(\mathcal C^1\),
\[
\boxed{\quad \nabla^2 S_{\Lambda_L,\beta}(U^{(0)}) = \alpha_W\,d_1^*d_1\quad}
\]
where \(d_1^*\) is the \(\ell^2\)-adjoint. The operator \(\mathsf M_1:=d_1^*d_1\) is the discrete Maxwell operator on 1-cochains.

---

## 6. Why this matters (in one paragraph)

Near the vacuum, the Wilson measure looks (to second order) like a Gaussian measure on 1-cochains with stiffness \(\alpha_W d_1^*d_1\). This is the exact point where gauge theory becomes "linear electromagnetism on a lattice"—and it is the backbone for turning geometric/functional inequalities into quantitative correlation decay: once you can replace the true (nonlinear) curvature/Hessian by a massive Maxwell operator on a high-probability good set, you can import sharp deterministic Green-kernel decay estimates.
