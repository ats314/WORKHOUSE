Document 1 — Scalar Prototype: Uniform Convexity and Bakry–Émery Gap

# Document 1: Scalar Prototype — Uniform Convexity and Bakry–Émery Mass Gap

## 1. Model

Let \(\Lambda_L \subset \mathbb{Z}^4\) be a finite periodic lattice. A scalar field configuration is
\[
  \phi = (\phi_x)_{x \in \Lambda_L} \in \mathbb{R}^{|\Lambda_L|}.
\]

**Definition 1.1 (Scalar Action).**  
Given parameters \(m_0^2>0\), \(\lambda>0\), \(\kappa\ge0\), define
\[
  S_\Lambda(\phi)
  = \sum_{x\in\Lambda_L} \Big(
      \frac{m_0^2}{2}\phi_x^2 + \frac{\lambda}{4}\phi_x^4
    \Big)
    + \frac{\kappa}{2}\sum_{\langle x,y\rangle}(\phi_x - \phi_y)^2,
\]
where \(\langle x,y\rangle\) are nearest-neighbor pairs. The Gibbs measure is
\[
  d\mu_\Lambda(\phi) = Z_\Lambda^{-1} e^{-S_\Lambda(\phi)}
  \prod_{x\in\Lambda_L} d\phi_x.
\]

Let \(\nabla^2 S_\Lambda(\phi)\) denote the Hessian, acting on vectors
\(v=(v_x)_{x\in\Lambda_L}\in\mathbb{R}^{|\Lambda_L|}\).

## 2. Uniform Convexity

**Lemma 2.1 (Uniform Hessian Lower Bound).**  
For all configurations \(\phi\) and all \(v\),
\[
  \langle v,\nabla^2 S_\Lambda(\phi) v\rangle
  \;\ge\; \rho_* \|v\|^2,
  \qquad \rho_* = m_0^2.
\]

*Proof.*  
The action is a sum of onsite potentials plus nearest-neighbor couplings.

1. Onsite potential at \(x\):
   \[
     V(\phi_x)=\frac{m_0^2}{2}\phi_x^2 + \frac{\lambda}{4}\phi_x^4,
   \]
   with
   \[
     V''(\phi_x) = m_0^2 + 3\lambda \phi_x^2 \ge m_0^2.
   \]

2. Coupling:
   \[
     K(\phi)=\frac{\kappa}{2}\sum_{\langle x,y\rangle}(\phi_x - \phi_y)^2.
   \]
   Its Hessian corresponds to a discrete Laplacian. For any \(v\),
   \[
     \langle v, \nabla^2 K v\rangle
     = \kappa \sum_{\langle x,y\rangle} (v_x - v_y)^2 \ge 0.
   \]

Thus
\[
  \langle v, \nabla^2 S_\Lambda(\phi) v\rangle
  = \sum_x (m_0^2 + 3\lambda\phi_x^2) v_x^2
    + \kappa\sum_{\langle x,y\rangle} (v_x - v_y)^2
  \ge m_0^2\sum_x v_x^2
  = m_0^2 \|v\|^2.
\]
So we may take \(\rho_* = m_0^2\), independent of the volume. ∎

## 3. Bakry–Émery and Functional Inequalities

Consider Langevin dynamics with generator
\[
  L_\Lambda f = \Delta f - \nabla S_\Lambda \cdot \nabla f
\]
on \(\mathbb{R}^{|\Lambda_L|}\), reversible w.r.t. \(\mu_\Lambda\).

Define the carré du champ and its iterated version:
\[
  \Gamma(f) = \|\nabla f\|^2,\qquad
  \Gamma_2(f) = \frac{1}{2}L_\Lambda \Gamma(f) - \Gamma(f,L_\Lambda f).
\]

In Euclidean space, Bochner’s identity gives
\[
  \Gamma_2(f)
  = \|\nabla^2 f\|_{\mathrm{HS}}^2
    + \langle \nabla^2 S_\Lambda \nabla f,\nabla f\rangle.
\]

**Proposition 3.1 (Bakry–Émery \(\mathrm{CD}(\rho_*,\infty)\)).**  
For the scalar model above,
\[
  \Gamma_2(f) \;\ge\; \rho_*\,\Gamma(f),
  \qquad \rho_* = m_0^2.
\]

*Proof.*  
Using Bochner:
\[
  \Gamma_2(f)
  = \|\nabla^2 f\|_{\mathrm{HS}}^2
    + \langle \nabla^2 S_\Lambda \nabla f,\nabla f\rangle
  \ge \langle \nabla^2 S_\Lambda \nabla f,\nabla f\rangle.
\]
Apply Lemma 2.1 with \(v = \nabla f\):
\[
  \langle \nabla^2 S_\Lambda \nabla f,\nabla f\rangle
  \ge \rho_* \|\nabla f\|^2
  = \rho_* \Gamma(f).
\]
∎

The Bakry–Émery condition implies Poincaré and log-Sobolev inequalities:

**Theorem 3.2 (Poincaré & Log-Sobolev).**  
For all smooth \(f\),
\[
  \mathrm{Var}_{\mu_\Lambda}(f)
  \le \frac{1}{\rho_*}\int \|\nabla f\|^2\,d\mu_\Lambda,
\]
\[
  \mathrm{Ent}_{\mu_\Lambda}(f^2)
  \le \frac{2}{\rho_*}\int \|\nabla f\|^2\,d\mu_\Lambda.
\]

*Sketch.* Standard Bakry–Émery theory: \(\mathrm{CD}(\rho_*,\infty)\) implies exponential decay of the Dirichlet form along the semigroup \(P_t = e^{tL_\Lambda}\), which integrates to Poincaré and log-Sobolev bounds via Grönwall-type arguments.

## 4. Dynamic Mass Gap

Let \(H = -L_\Lambda\) on \(L^2(\mu_\Lambda)\). By the Rayleigh–Ritz principle, the smallest nonzero eigenvalue \(\lambda_1\) satisfies
\[
  \lambda_1 = \inf_{f\perp 1}
  \frac{\int \|\nabla f\|^2 d\mu_\Lambda}{\mathrm{Var}_{\mu_\Lambda}(f)}.
\]
Combining with the Poincaré inequality,
\[
  \lambda_1 \;\ge\; \rho_* = m_0^2.
\]

So the scalar model has a strictly positive spectral gap (a “mass gap”), **uniform in the volume**. This will be our template for the gauge theory: get a **uniform Hessian lower bound** → Bakry–Émery → spectral gap.


⸻
