# Part I — Curvature–Controlled Gibbs Measures  
## Section 3 — From \(CD(\rho,\infty)\) to Poincaré and Log-Sobolev Inequalities

We continue in the setting of Sections&nbsp;1–2:

- \((M,g)\) is a smooth, connected, complete Riemannian manifold (finite-dimensional),
- \(S\in C^2(M)\) is a potential and \(\mu \propto e^{-S} d\mathrm{vol}_g\) is the associated Gibbs measure,
- \(L = \Delta_g - \langle \nabla S,\nabla\cdot\rangle\) is the diffusion generator,
- \(\Gamma,\Gamma_2\) are the carré du champ operators,

and we assume throughout this section that the **curvature–dimension condition** holds:

> \[
> CD(\rho,\infty) \quad\text{for some } \rho>0,
> \]
> i.e.
> \[
> \Gamma_2(f) \ge \rho\, \Gamma(f) \quad \text{for all smooth } f.
> \]

Our goal is to derive, in a finite-dimensional and self-contained way:

1. A **Poincaré inequality** (spectral gap) with constant \(1/\rho\),
2. A **logarithmic Sobolev inequality** with constant \(2/\rho\).

---

## 3.1. Spectral decomposition and Dirichlet form

We recall some basic properties of the self-adjoint operator \(-L\) associated with the Dirichlet form
\[
\mathcal{E}(f,g) = \int_M \Gamma(f,g)\,d\mu
= \int_M \langle \nabla f,\nabla g\rangle\,d\mu.
\]

### 3.1.1. Self-adjoint operator and spectrum

As in Section&nbsp;1:

- The symmetric bilinear form \((\mathcal{E},\mathcal{D}(\mathcal{E}))\) is closed and Markovian.
- There exists a unique nonnegative self-adjoint operator \(-L\) on \(L^2(\mu)\) such that
  \[
    \mathcal{E}(f,g) = \langle f,-Lg\rangle_{L^2(\mu)}
    \quad
    \forall f\in \mathcal{D}(\mathcal{E}),\ \forall g\in\mathcal{D}(-L).
  \]

Because \(M\) is finite-dimensional and \(\mu\) has a smooth, strictly positive density, standard elliptic theory implies (under mild additional confining assumptions on \(S\)) that \(L\) has **purely discrete spectrum** in \(L^2(\mu)\). In particular, there exists an orthonormal basis \((\varphi_k)_{k\ge 0}\) of \(L^2(\mu)\) with
\[
L\varphi_k = -\lambda_k \varphi_k,\quad
0 = \lambda_0 < \lambda_1 \le \lambda_2 \le \cdots,
\]
and \(\varphi_0\) is constant (equal to \(1\), up to normalization).

For any \(f\in L^2(\mu)\) we can expand
\[
f = \sum_{k=0}^\infty c_k \varphi_k,\quad
c_k = \langle f,\varphi_k\rangle_{L^2(\mu)}.
\]

### 3.1.2. Dirichlet form in eigenbasis

Using the eigen-basis:

- The \(L^2(\mu)\)-norm is
  \[
  \|f\|_{L^2(\mu)}^2 = \sum_{k=0}^\infty |c_k|^2.
  \]

- The Dirichlet form is
  \[
  \mathcal{E}(f,f)
  = \langle f,-Lf\rangle
  = \sum_{k=0}^\infty \lambda_k |c_k|^2.
  \]

- The variance is
  \[
  \operatorname{Var}_\mu(f)
  = \|f - \mu(f)\|_{L^2(\mu)}^2
  = \sum_{k\ge 1} |c_k|^2,
  \]
  since \(\varphi_0\) is constant and \(\mu(f) = c_0\).

A **Poincaré inequality** with constant \(1/\lambda\) is equivalent to
\[
\operatorname{Var}_\mu(f) \le \frac{1}{\lambda}\mathcal{E}(f,f),
\]
which in the eigenbasis becomes
\[
\sum_{k\ge 1} |c_k|^2 \;\le\; \frac{1}{\lambda}\sum_{k\ge 1}\lambda_k |c_k|^2.
\]

This is true for all \(f\) if and only if
\[
\lambda \le \lambda_1,
\]
and the **optimal** Poincaré constant is precisely \(\lambda_1\).

Thus to prove a Poincaré inequality with constant \(1/\rho\), it suffices to show
\[
\lambda_1 \ge \rho.
\]

We will now use the \(CD(\rho,\infty)\) condition to prove exactly this.

---

## 3.2. Poincaré inequality from \(CD(\rho,\infty)\)

We relate \(\Gamma_2\) to the eigenvalues of \(-L\).

### 3.2.1. \(\Gamma_2\) integrated against an eigenfunction

Let \(\varphi\in \mathcal{D}(-L)\) be a nonconstant eigenfunction:
\[
L\varphi = -\lambda \varphi,\qquad \lambda>0.
\]

We first compute the integral of \(\Gamma_2(\varphi)\) with respect to \(\mu\).

From the definition,
\[
\Gamma_2(\varphi)
= \frac{1}{2}\big(L\Gamma(\varphi) - 2\Gamma(\varphi,L\varphi)\big).
\]

Integrate both sides over \(M\) with respect to \(\mu\):

- Since \(L\) is symmetric and \(\mu\)-invariant, \(\int L h\,d\mu = 0\) for any smooth \(h\), so
  \[
    \int L\Gamma(\varphi)\,d\mu = 0.
  \]

- Therefore,
  \[
  \int \Gamma_2(\varphi)\,d\mu
   = - \int \Gamma(\varphi,L\varphi)\,d\mu.
  \]

Now use the eigenfunction relation \(L\varphi = -\lambda \varphi\) and bilinearity of \(\Gamma\):
\[
\Gamma(\varphi,L\varphi)
= \Gamma(\varphi,-\lambda \varphi)
= -\lambda\,\Gamma(\varphi,\varphi)
= -\lambda\,\Gamma(\varphi).
\]

Hence
\[
\int \Gamma_2(\varphi)\,d\mu
= -\int \Gamma(\varphi,L\varphi)\,d\mu
= \lambda \int \Gamma(\varphi)\,d\mu.
\]

### 3.2.2. Application of \(CD(\rho,\infty)\)

By the \(CD(\rho,\infty)\) condition,
\[
\Gamma_2(\varphi) \ge \rho\,\Gamma(\varphi) \quad\text{pointwise},
\]
and hence, integrating,
\[
\int \Gamma_2(\varphi)\,d\mu
\ge \rho \int \Gamma(\varphi)\,d\mu.
\]

Combining with the relation above, we obtain
\[
\lambda \int \Gamma(\varphi)\,d\mu
= \int \Gamma_2(\varphi)\,d\mu
\ge \rho \int \Gamma(\varphi)\,d\mu.
\]

If \(\varphi\) is nonconstant, \(\Gamma(\varphi)\) is not identically zero, hence
\[
\int \Gamma(\varphi)\,d\mu > 0,
\]
and we can divide by it to conclude
\[
\lambda \ge \rho.
\]

This holds for every nonconstant eigenfunction, so in particular
\[
\lambda_1 \ge \rho.
\]

### 3.2.3. Poincaré inequality and spectral gap

As observed in Section&nbsp;3.1,

- The optimal Poincaré constant is \(\lambda_1\),
- We have just shown \(\lambda_1 \ge \rho\).

Therefore:

> **Theorem 3.1 (Poincaré inequality from \(CD(\rho,\infty)\)).**  
> Suppose that \(L\) satisfies \(CD(\rho,\infty)\) with \(\rho>0\). Then for all \(f\in\mathcal{D}(\mathcal{E})\),
> \[
> \operatorname{Var}_\mu(f)
> \le \frac{1}{\rho}\,\mathcal{E}(f,f)
> = \frac{1}{\rho}\int_M \Gamma(f)\,d\mu.
> \]
> Equivalently, the spectral gap of \(-L\) satisfies
> \[
> \lambda_1 \ge \rho.
> \]

This is the Bakry–Émery version of the classical Lichnerowicz estimate.

---

## 3.3. Logarithmic Sobolev inequality from \(CD(\rho,\infty)\)

We now turn to the **logarithmic Sobolev inequality** (LSI), which controls entropy by energy.

The statement we aim for is:

> **Theorem 3.2 (Log-Sobolev inequality from \(CD(\rho,\infty)\)).**  
> Suppose \(L\) satisfies \(CD(\rho,\infty)\) with \(\rho>0\). Then for every smooth \(f\),
> \[
> \operatorname{Ent}_\mu(f^2)
> \;\le\; \frac{2}{\rho}\,\mathcal{E}(f,f)
> = \frac{2}{\rho}\int_M |\nabla f|^2\,d\mu.
> \]

We give the standard semigroup-based derivation due to Bakry and Émery.

### 3.3.1. Entropy along the diffusion semigroup

Let \(P_t = e^{tL}\) be the Markov semigroup generated by \(L\). Fix a function \(f\ge 0\) with sufficient regularity and define
\[
g_t := P_t f, \quad t\ge 0.
\]

Note:

- \(g_t \ge 0\) since \(P_t\) is positivity-preserving,
- \(\int g_t\,d\mu = \int f\,d\mu\) is constant in \(t\) (invariance of \(\mu\)),
- \(g_t\) solves the PDE
  \[
  \partial_t g_t = L g_t.
  \]

Define the entropy functional
\[
\Phi(t) := \operatorname{Ent}_\mu(g_t)
= \int_M g_t \log g_t \, d\mu
 - \bigg(\int_M g_t \, d\mu\bigg)\log\bigg(\int_M g_t \, d\mu\bigg).
\]

Because \(\int g_t\,d\mu\) is constant in \(t\), the second term is constant; therefore
\[
\Phi'(t) = \frac{d}{dt}\int_M g_t \log g_t \, d\mu
= \int_M \partial_t g_t \cdot \log g_t \, d\mu
  + \int_M \partial_t g_t \, d\mu.
\]

The second integral vanishes (again by invariance of \(\mu\)), so
\[
\Phi'(t) = \int_M L g_t \cdot \log g_t \, d\mu.
\]

Using symmetry of \(L\) and the definition of \(\Gamma\), we have the integration by parts identity
\[
\int_M L h \cdot \psi \, d\mu
= -\int_M \Gamma(h,\psi) \, d\mu
\]
for smooth \(h,\psi\). Applying this with \(h = g_t\), \(\psi = \log g_t\), we obtain
\[
\Phi'(t)
= - \int_M \Gamma(g_t,\log g_t) \, d\mu.
\]

Using the chain rule \(\nabla(\log g_t) = \nabla g_t / g_t\), we have
\[
\Gamma(g_t,\log g_t) = \langle \nabla g_t,\nabla\log g_t\rangle = \frac{|\nabla g_t|^2}{g_t},
\]
so we may also write
\[
\Phi'(t)
= -\int_M \frac{|\nabla g_t|^2}{g_t} \, d\mu.
\]

In particular, \(\Phi'(t) \le 0\); entropy is non-increasing along the flow.

### 3.3.2. Second derivative and \(\Gamma_2\)

To exploit the curvature condition, we need a formula for \(\Phi''(t)\) in terms of \(\Gamma_2\).

Define \(h_t := \log g_t\). Then \(g_t = e^{h_t}\) and \(\nabla h_t = \nabla g_t / g_t\). A standard computation in the Bakry–Émery calculus gives:
\[
\Phi''(t) = 2\int_M \Gamma_2(h_t)\, g_t \, d\mu.
\]

We briefly sketch the derivation.

**Sketch of proof.**  
Write
\[
\Phi'(t) = -\int_M g_t \,\Gamma(h_t)\,d\mu,
\]
using \(\Gamma(g_t,\log g_t) = g_t \Gamma(h_t)\). Differentiating,
\[
\Phi''(t)
= -\int_M \partial_t g_t \,\Gamma(h_t)\,d\mu
  - \int_M g_t \,\partial_t\Gamma(h_t)\,d\mu.
\]

- Use \(\partial_t g_t = L g_t\),
- Use the identity \(\partial_t \Gamma(h_t) = 2\Gamma(h_t,L h_t) + 2\Gamma_2(h_t)\),
- Use repeated integration by parts and the symmetry of \(L\) with respect to \(\mu\).

After cancellations, the mixed term involving \(\Gamma(h_t,L h_t)\) disappears, and one is left with
\[
\Phi''(t) = 2\int_M \Gamma_2(h_t)\, g_t\,d\mu.
\]
This is the standard Bakry–Émery entropy second derivative formula. \(\square\)

### 3.3.3. Application of \(CD(\rho,\infty)\) and differential inequality

We now apply the curvature–dimension condition to \(h_t = \log g_t\). Since \(CD(\rho,\infty)\) holds for all smooth functions,
\[
\Gamma_2(h_t) \ge \rho\,\Gamma(h_t)
\quad\text{for all } t\ge 0.
\]

Multiplying by \(g_t\) and integrating,
\[
\int_M \Gamma_2(h_t)\,g_t\,d\mu
\ge \rho \int_M \Gamma(h_t)\,g_t\,d\mu.
\]

Recall from above that
\[
\Phi'(t)
= -\int_M g_t \Gamma(h_t)\,d\mu,
\]
so
\[
\int_M \Gamma(h_t)\,g_t\,d\mu = -\Phi'(t).
\]

Therefore
\[
\Phi''(t)
= 2\int_M \Gamma_2(h_t)\,g_t\,d\mu
\ge 2\rho \int_M \Gamma(h_t)\,g_t\,d\mu
= -2\rho\,\Phi'(t).
\]

We have obtained the differential inequality
\[
\Phi''(t) + 2\rho\,\Phi'(t) \ge 0.
\]

Since \(\Phi'(t)\le 0\), this implies that \(\Phi\) is convex and decreasing, and we can use a simple ODE comparison argument to deduce exponential decay.

### 3.3.4. Exponential decay of entropy

Define
\[
\Psi(t) := -\Phi'(t) \ge 0.
\]

The inequality \(\Phi''(t) + 2\rho\,\Phi'(t) \ge 0\) becomes
\[
\Psi'(t) + 2\rho\,\Psi(t) \le 0.
\]

This is a linear differential inequality. Writing it as
\[
\frac{d}{dt}\big(e^{2\rho t}\Psi(t)\big) \le 0,
\]
we deduce that \(e^{2\rho t}\Psi(t)\) is non-increasing. In particular,
\[
\Psi(t) \le e^{-2\rho t}\Psi(0).
\]

Now integrate \(\Psi\) from \(0\) to \(t\):
\[
\Phi(0) - \Phi(t)
= \int_0^t \Psi(s)\,ds
\le \int_0^t e^{-2\rho s}\Psi(0)\,ds
= \frac{1 - e^{-2\rho t}}{2\rho}\,\Psi(0).
\]

As \(t\to\infty\), \(g_t = P_t f\) converges to the constant function \(\int f\,d\mu\), so \(\Phi(t)\to 0\). Thus taking the limit \(t\to\infty\) yields
\[
\Phi(0)
\le \frac{1}{2\rho}\,\Psi(0).
\]

But \(\Phi(0) = \operatorname{Ent}_\mu(f)\), and
\[
\Psi(0) = -\Phi'(0)
= \int_M \Gamma(f,\log f)\,d\mu
= \int_M \frac{|\nabla f|^2}{f} \, d\mu.
\]

We have therefore obtained the (non-symmetric) log-Sobolev inequality
\[
\operatorname{Ent}_\mu(f)
\le \frac{1}{2\rho} \int_M \frac{|\nabla f|^2}{f}\,d\mu,
\quad \text{for } f\ge 0.
\]

### 3.3.5. Symmetric LSI for \(f^2\)

To obtain the more convenient LSI in terms of \(f^2\), we apply the previous inequality to \(f = g^2\) with \(g\) arbitrary. Then
\[
\operatorname{Ent}_\mu(g^2)
\le \frac{1}{2\rho} \int_M \frac{|\nabla(g^2)|^2}{g^2}\,d\mu
= \frac{1}{2\rho} \int_M \frac{(2g|\nabla g|)^2}{g^2}\,d\mu
= \frac{2}{\rho} \int_M |\nabla g|^2\,d\mu.
\]

Renaming \(g\) as \(f\), we obtain the desired inequality:

> **Theorem 3.2 (Log-Sobolev inequality from \(CD(\rho,\infty)\), symmetric form).**  
> Suppose \(CD(\rho,\infty)\) holds with \(\rho>0\). Then for all smooth \(f\),
> \[
> \operatorname{Ent}_\mu(f^2)
> \le \frac{2}{\rho} \int_M |\nabla f|^2\,d\mu
> = \frac{2}{\rho}\,\mathcal{E}(f,f).
> \]

---

## 3.4. Summary of Section 3 — Functional Inequalities from Curvature

Under the curvature–dimension condition \(CD(\rho,\infty)\) with \(\rho>0\), we have established:

1. **Poincaré inequality (spectral gap).**  
   For all \(f\in\mathcal{D}(\mathcal{E})\),
   \[
   \operatorname{Var}_\mu(f)
   \le \frac{1}{\rho}\,\mathcal{E}(f,f),
   \]
   and the spectral gap of \(-L\) satisfies \(\lambda_1 \ge \rho\).

2. **Logarithmic Sobolev inequality (LSI).**  
   For all smooth \(f\),
   \[
   \operatorname{Ent}_\mu(f^2)
   \le \frac{2}{\rho}\,\mathcal{E}(f,f).
   \]

These inequalities are **dimension-free** in the sense that the constants \(1/\rho\) and \(2/\rho\) depend only on the curvature lower bound \(\rho\) and not on the dimension \(n\) or the volume of \(M\).

In **Section 4**, we will apply this abstract machinery to an explicit finite lattice scalar field model, where the curvature lower bound \(\rho\) can be computed directly from the Hessian of the potential. This will serve as a concrete prototype for the more complex Yang–Mills applications developed in later parts of the project.

## 3.5. Lyapunov conditions and local-to-global principles

In many applications, including lattice Yang–Mills, one does **not** have a global curvature–dimension bound \(CD(\rho,\infty)\) on all of \(M\). Instead, one has:

- A **local curvature bound** \(CD(\rho_{\mathrm{loc}},\infty)\) on a ball \(B_r(x_0)\subset M\), and
- A **Lyapunov drift condition** that controls the tails of the invariant measure outside \(B_r(x_0)\).

In this subsection we recall the abstract Lyapunov framework that will be used in Part&nbsp;II. We work in the same general setting as above, but we **do not** assume global \(CD(\rho,\infty)\).

### 3.5.1. Lyapunov functions and drift

Let \(L\) be the symmetric diffusion generator associated with \(\mu\), as in Sections&nbsp;1–2.  

A **Lyapunov function** for \((L,\mu)\) is a function \(W\colon M\to[1,\infty)\), sufficiently regular (e.g. \(C^2\)), such that there exist constants \(\lambda>0\), \(b\ge 0\), and a relatively compact set \(K\subset M\) with
\[
L W \;\le\; -\lambda W + b\,\mathbf{1}_K
\quad\text{(pointwise on }M\text{).}
\]

This inequality expresses that, away from the “small” region \(K\), the dynamics generated by \(L\) has a **drift towards regions where \(W\) is small**. Under mild additional hypotheses, such a drift condition enforces the existence of a spectral gap and, with stronger growth of \(W\), a log-Sobolev inequality.

We will use the following two standard results (we state them without proof; proofs can be found in the functional-inequality literature).

### 3.5.2. Lyapunov + local Poincaré \(\Rightarrow\) global Poincaré

Let \(K\subset M\) be a relatively compact set (for example a geodesic ball \(B_r(x_0)\)). Assume:

1. (**Lyapunov drift**)  
   There exist \(W\ge 1\), \(\lambda>0\), \(b\ge 0\), and \(K\subset M\) such that
   \[
   L W \;\le\; -\lambda W + b\,\mathbf{1}_K.
   \]

2. (**Local Poincaré on \(K\)**)  
   There exists \(C_K>0\) such that for all smooth \(f\),
   \[
   \int_K \big(f - f_K\big)^2\,d\mu
   \;\le\; C_K \int_K \Gamma(f)\,d\mu,
   \]
   where \(f_K := \mu_K(f)\) is the average of \(f\) with respect to \(\mu\) conditioned on \(K\).

Then there exists a constant \(C_{\mathrm{P}}>0\), depending only on \(\lambda,b,C_K\) and \(\mu(K)\), such that the **global Poincaré inequality**
\[
\operatorname{Var}_\mu(f)
\;\le\; C_{\mathrm{P}} \int_M \Gamma(f)\,d\mu
\]
holds for all \(f\) in the domain of the Dirichlet form.

In particular, the spectral gap of \(-L\) satisfies \(\lambda_1 \ge C_{\mathrm{P}}^{-1} >0\).

This result shows that a **local control of oscillations** on a set \(K\) combined with a **global Lyapunov drift** is sufficient to obtain a global, volume-independent spectral gap, even when no global curvature bound is available.

### 3.5.3. Lyapunov + local super-Poincaré \(\Rightarrow\) log-Sobolev

There is a parallel result for **log-Sobolev inequalities**, using a stronger local functional inequality.

Assume again that \(W\) satisfies the Lyapunov drift condition above, and that on \(K\) one has a **local super-Poincaré inequality**
\[
\int_K f^2\,d\mu
\;\le\; s \int_K \Gamma(f)\,d\mu + \beta_K(s)\,\Big(\int_K |f|\,d\mu\Big)^2
\quad\text{for all }s>0,
\]
with some function \(\beta_K(s)\). Under suitable growth conditions on \(W\) at infinity (typically, one assumes that \(W\) dominates a convex function of a control distance), one can deduce from these hypotheses a **global super-Poincaré inequality** for \(\mu\), and hence a logarithmic Sobolev inequality
\[
\operatorname{Ent}_\mu(f^2)
\;\le\; C_{\mathrm{LSI}} \int_M \Gamma(f)\,d\mu
\]
with some finite constant \(C_{\mathrm{LSI}}>0\).

We will not need the full general statement here; the key point for later use is that:

- A **local curvature lower bound** (e.g. \(CD(\rho_{\mathrm{loc}},\infty)\) on a ball \(K=B_r(x_0)\)) implies local Poincaré and local super-Poincaré inequalities on \(K\) with constants depending only on \(\rho_{\mathrm{loc}}\) and the geometry of \(K\);
- A **Lyapunov drift condition** provides the mechanism to propagate these local inequalities to the whole manifold.

In the lattice Yang–Mills setting of Part&nbsp;II, Theorem 6.1 will verify a local curvature condition for the horizontal Bakry–Émery tensor on a small ball \(K=B_r(U^{(0)})\), uniformly in the lattice volume \(\Lambda\). The construction of suitable Lyapunov functions for the corresponding Langevin generators \(L_\Lambda\) and the verification of local Poincaré/super-Poincaré inequalities on \(K\) will then allow us to obtain global, volume-independent Poincaré and log-Sobolev inequalities for the gauge-invariant Gibbs measures.

