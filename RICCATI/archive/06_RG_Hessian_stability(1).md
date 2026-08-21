Document 6 — RG Hessian Inequality and Strong-Coupling Stability

# Document 6: RG Hessian Inequality and Strong-Coupling Stability

This document formalizes how convexity behaves under coarse-graining, using a block-matrix Hessian decomposition and a functional inequality (a Brascamp–Lieb / Poincaré type bound). The goal: identify a **subwindow** in strong coupling where convexity is **stable under one RG step**.

## 1. Block Decomposition of the Hessian

Split the horizontal degrees of freedom into coarse and fine blocks:
\[
  x \in \mathbb{R}^m \quad(\text{coarse}),\qquad
  y \in \mathbb{R}^n \quad(\text{fine}).
\]
The full action \(S(x,y)\) has Hessian
\[
  \nabla^2 S(x,y)
  = \begin{pmatrix}
      A(x,y) & B(x,y)\\
      B(x,y)^\top & C(x,y)
    \end{pmatrix},
\]
where:

- \(A\) is the coarse–coarse block;
- \(C\) is the fine–fine block;
- \(B\) couples coarse and fine directions.

Assume uniform bounds:
\[
  A(x,y) \succeq \alpha I_m,\quad
  C(x,y)\succeq \gamma I_n,\quad
  \|B(x,y)\|_{\mathrm{op}} \le M
\]
for all \((x,y)\). Here \(\alpha,\gamma>0\) and \(M\ge0\).

Define the coarse effective action by integrating out \(y\):
\[
  e^{-S_{\mathrm{eff}}(x)}
  := \int_{\mathbb{R}^n} e^{-S(x,y)}\,dy.
\]

## 2. Hessian of the Coarse Effective Action

Let \(E_x[\cdot]\) and \(\mathrm{Cov}_x\) denote expectation and covariance w.r.t. the conditional measure
\[
  d\mu_x(y) = Z(x)^{-1} e^{-S(x,y)}dy.
\]

Then
\[
  \nabla_x^2 S_{\mathrm{eff}}(x)
  = E_x[A(x,Y)] - \mathrm{Cov}_x(\nabla_x S(x,Y)).
\]

For any unit vector \(v\in\mathbb{R}^m\),
\[
  v^\top \nabla_x^2 S_{\mathrm{eff}}(x)\,v
  = E_x[v^\top A v] - \mathrm{Var}_x\big( v^\top \nabla_x S(x,Y)\big).
\]

The first term is bounded below by \(\alpha\). For the second term, use a Poincaré-type inequality in the \(y\)-variables: since \(C\succeq \gamma I_n\), the conditional measure \(\mu_x\) is \(\gamma\)-strongly log-concave in \(y\), and for any centered \(f\),
\[
  \mathrm{Var}_x(f(Y)) \le \frac{1}{\gamma} E_x[\|\nabla_y f(Y)\|^2].
\]

Apply this to \(f(y) = v^\top \nabla_x S(x,y)\). Then
\[
  \nabla_y f(y) = B(x,y)^\top v,
\]
so
\[
  \|\nabla_y f(y)\|^2 = \|B(x,y)^\top v\|^2 \le M^2.
\]
Hence
\[
  \mathrm{Var}_x\big(v^\top \nabla_x S(x,Y)\big)
  \le \frac{M^2}{\gamma}.
\]

Putting it together,
\[
  v^\top \nabla_x^2 S_{\mathrm{eff}}(x)\,v
  \ge \alpha - \frac{M^2}{\gamma}.
\]
Since this holds for all unit vectors \(v\), we obtain:

**Theorem 2.1 (Block RG Convexity Bound).**  
If \(A\succeq \alpha I_m\), \(C\succeq \gamma I_n\), and \(\|B\|_{\mathrm{op}}\le M\) uniformly, then
\[
  \nabla_x^2 S_{\mathrm{eff}}(x)
  \succeq \left(\alpha - \frac{M^2}{\gamma}\right) I_m.
\]
In particular, if \(M^2 < \alpha\gamma\), the coarse effective action remains uniformly convex with curvature
\[
  \rho_{\mathrm{new}} = \alpha - \frac{M^2}{\gamma} > 0.
\]

This is a quantitative version of the principle “strong log-concavity is stable under marginalization”.

## 3. Application to Lattice Yang–Mills

For the lattice Yang–Mills effective action \(S_{\mathrm{eff}}\) (restricted to horizontals), assume we’re in the convexity window of Document 5:
\[
  \mathrm{Hess}_{\mathrm{hor}} S_{\mathrm{eff}}(U)
  \succeq \rho_*(a) I,
  \qquad
  \rho_*(a) = c_0 a^2 g^2 - \frac{12}{g^2} > 0.
\]

Split the horizontal directions into coarse and fine bonds. Because the Hessian is bounded below by \(\rho_*(a)\) uniformly, we can take
\[
  \alpha = \gamma = \rho_*(a).
\]

The mixed block \(B\) is dominated by the off-diagonal couplings coming from the Wilson action. From Document 4,
\[
  \|\mathrm{Hess} S_W(U)\|_{\mathrm{op}}\le C_V(N)=\frac{6}{N}.
\]
Thus the full Wilson contribution at coupling \(\beta\) satisfies
\[
  \|\beta\,\mathrm{Hess} S_W(U)\|_{\mathrm{op}}
  \le \beta C_V(N) = \frac{12}{g^2}.
\]
We can safely set
\[
  M = \frac{12}{g^2}.
\]

Applying Theorem 2.1, after integrating out the fine bonds we get a coarse effective action with curvature
\[
  \rho_{\mathrm{new}}(a)
  \ge \rho_*(a) - \frac{M^2}{\rho_*(a)}
  = \rho_*(a) - \frac{144}{g^4\,\rho_*(a)}.
\]

To guarantee \(\rho_{\mathrm{new}}(a) > 0\), it suffices that
\[
  \rho_*(a)^2 > \frac{144}{g^4}
  \quad\Longleftrightarrow\quad
  \rho_*(a) > \frac{12}{g^2}.
\]

Substitute \(\rho_*(a) = c_0 a^2 g^2 - 12/g^2\):
\[
  c_0 a^2 g^2 - \frac{12}{g^2} > \frac{12}{g^2}
  \quad\Longleftrightarrow\quad
  c_0 a^2 g^2 > \frac{24}{g^2}
  \quad\Longleftrightarrow\quad
  g^4 > \frac{24}{c_0 a^2}.
\]

**Theorem 3.1 (RG-Stable Strong-Coupling Subwindow).**  
Fix lattice spacing \(a>0\). If
\[
  g^4 > \frac{24}{c_0 a^2},
\]
then:

1. The bare effective action \(S_{\mathrm{eff}}\) is uniformly convex along horizontals (finite-cutoff mass gap regime).
2. After integrating out a block of fine bonds in one RG step, the coarse effective action remains uniformly convex with curvature \(\rho_{\mathrm{new}}(a) > 0\).

Thus for sufficiently strong coupling, convexity is **not only present but stable under coarse-graining**, at least for one blocking step. This is a nontrivial constraint that goes beyond a single-scale argument.

## 4. Comment: Continuum vHJ vs Lattice RG

In continuum flat space, applying the vHJ/Riccati machinery (Document 2) to a Gaussian action shows that Hessian eigenvalues \(\lambda_i(t)\) under heat-flow RG decay like
\[
  \lambda_i(t) = \frac{\lambda_i(0)}{1 + 2t\,\lambda_i(0)} \to 0
\]
as \(t\to\infty\): convexity **collapses**.

The lattice result here is qualitatively different: the compact group geometry and the discrete structure allow a regime where convexity is preserved under coarse-graining, thanks to the Haar mass and the boundedness of Wilson couplings.

This is one of the hints behind the **Geometric–Spectral Stability** conjecture for the continuum limit.


⸻
