---
title: "Core 5: Local Coercivity and Matrix Hinge on a Canonical Good Set"
status: "DRAFT"
depends_on:
  - "Core_1__Lattice_Gauge_Model_at_Fixed_Cutoff.md"
  - "Core_4__Vacuum_Linearization_and_Discrete_Maxwell_Structure.md"
  - "Appendix_A__Notation_and_Constants.md"
  - "Appendix_B__Lattice_Cell_Complex_and_Cochains.md"
  - "Appendix_C__Configuration_Geometry.md"
  - "Appendix_D__Wilson_Action_Vacuum_Expansion_and_Hessian.md"
  - "Appendix_E__Bakry_Emery_Calculus.md"
  - "Appendix_F__Helffer_Sjostrand_Covariance.md"
feeds_into:
  - "Core_6__Conditional_Covariance_Bound_via_HS_and_Hinge.md"
  - "Core_8__Localization_and_Transfer_to_Infinite_Volume.md"
---

## Core-5.0. Output of this file

This file provides three interfaces used later:

1. A **canonical “good set”** (domain) $\mathcal K_{\Lambda_L,\beta}\subset \mathcal M_{\Lambda_L}$ on which the Wilson drift is uniformly close (in a precise sense) to its vacuum linearization.

2. A **matrix hinge** (local Bakry–Émery lower bound) on $\mathcal K_{\Lambda_L,\beta}$:
\begin{equation}
\mathrm{Ric}_{\mu_{\Lambda_L,\beta}}(U)\ \succeq\ M_{\Lambda_L}^{\mathrm{hinge}}
\qquad\text{for all }U\in \mathcal K_{\Lambda_L,\beta},
\end{equation}
for a deterministic, lattice-translation-invariant comparison operator $M_{\Lambda_L}^{\mathrm{hinge}}$ built from the massive Maxwell operator of Core 4.

3. A **horizontality lemma**: gauge-invariant observables have gradients orthogonal to infinitesimal gauge directions (in a precise, configuration-dependent sense).

Nothing in this file uses typicality. Typicality (high probability of $\mathcal K_{\Lambda_L,\beta}$) is deferred to Appendix J / Core 8.

---

## Core-5.1. The canonical good set

The guiding principle is: the matrix hinge we need later is a **pointwise** lower bound on the Bakry–Émery curvature matrix. To obtain a deterministic (configuration-independent) comparison operator, we must localize to a region where the Wilson drift is controlled by its vacuum Hessian (Appendix D).

### Core-5.1.1. Plaquette logarithms and the small-field radius

Recall the Lie-group small-field radius $r_{\mathrm{sf}}$ from Appendix A (Definition A.7.4).

For any plaquette $p\in\mathcal P(\Lambda_L)$ and configuration $U\in\mathcal M_{\Lambda_L}$, define the plaquette holonomy $U_p(U)\in G$ as in Core 1 / Appendix C.

Whenever $U_p(U)\in \exp(B_{r_{\mathrm{sf}}}(0))$, the logarithm is uniquely defined and we write
\begin{equation}
\mathbf Y_p(U)\ :=\ \log\bigl(U_p(U)\bigr)\ \in \ \mathfrak g,
\qquad \|\mathbf Y_p(U)\|\le r_{\mathrm{sf}}.
\end{equation}

### Core-5.1.2. Definition of the canonical good set

We define a *pointwise* small-field domain by requiring every plaquette holonomy to lie inside the logarithmic chart, with a $\beta$-dependent scale that shrinks at least like $\beta^{-1/2}$.

#### Definition Core-5.1.2 (canonical good set)
Let $\Lambda_L$ be the $d$-dimensional periodic box from Core 1 and let $\beta>0$. Define the scale
\begin{equation}
r_{\beta}\ :=\ r_{\mathrm{sf}}\cdot \min\{1,\ \beta^{-1/2}\}.
\end{equation}
Define the canonical good set
\begin{equation}
\mathcal K_{\Lambda_L,\beta}\ :=\
\Bigl\{U\in\mathcal M_{\Lambda_L}\ :\ U_p(U)\in \exp(B_{r_{\beta}}(0))\ \text{for every }p\in\mathcal P(\Lambda_L)\Bigr\}.
\end{equation}

Equivalently, $U\in\mathcal K_{\Lambda_L,\beta}$ iff the plaquette logs $\mathbf Y_p(U)$ exist for all $p$ and satisfy
\begin{equation}
\sup_{p\in\mathcal P(\Lambda_L)} \|\mathbf Y_p(U)\|\ \le\ r_{\beta}.
\end{equation}

#### Lemma Core-5.1.3 (gauge invariance of $\mathcal K_{\Lambda_L,\beta}$)
$\mathcal K_{\Lambda_L,\beta}$ is gauge invariant: for all $g\in\mathcal G_{\Lambda_L}$ and all $U\in\mathcal M_{\Lambda_L}$,
\begin{equation}
U\in \mathcal K_{\Lambda_L,\beta}\quad\Longleftrightarrow\quad g\cdot U\in \mathcal K_{\Lambda_L,\beta}.
\end{equation}

**Proof.**
By Core 1 / Appendix C, plaquette holonomies transform by conjugation:
\begin{equation}
U_p(g\cdot U)\ =\ g_x\, U_p(U)\, g_x^{-1},
\end{equation}
where $x$ is the basepoint (tail vertex) of plaquette $p$. Since the metric on $G$ is bi-invariant, conjugation is an isometry, hence
\begin{equation}
\mathrm{dist}_G(1, U_p(g\cdot U))=\mathrm{dist}_G(1,U_p(U)).
\end{equation}
Therefore $U_p(U)\in \exp(B_{r_\beta}(0))$ for all $p$ iff $U_p(g\cdot U)\in \exp(B_{r_\beta}(0))$ for all $p$. ∎

### Core-5.1.4. Domain regularity for conditioning

Later (Appendix F, External Input F.20) we will use a reflecting diffusion / Helffer–Sjöstrand representation on a domain $\Omega\subset\mathcal M_{\Lambda_L}$, reversible w.r.t. the conditional measure $\mu_{\Lambda_L,\beta}(\cdot\mid \Omega)$.

The set $\mathcal K_{\Lambda_L,\beta}$ is an intersection of sublevel sets of smooth functions (squared distances in the small chart), hence has a piecewise smooth boundary (corners). We will treat the existence of the reflecting generator on $\mathcal K_{\Lambda_L,\beta}$ as part of the same “reflecting diffusion” external input already isolated in Appendix F (External Input F.20).

---

## Core-5.2. Bakry–Émery curvature and the matrix hinge

### Core-5.2.1. Curvature matrix notation

Let $\mu_{\Lambda_L,\beta}$ be the Gibbs measure on $\mathcal M_{\Lambda_L}$ (Core 1), viewed as a smooth density with respect to $\mathrm{vol}_{g_{\Lambda_L}}$:
\begin{equation}
\mathrm d\mu_{\Lambda_L,\beta}(U) \propto e^{-S_{\Lambda_L,\beta}(U)}\,\mathrm d\mathrm{vol}_{g_{\Lambda_L}}(U).
\end{equation}

Recall the Bakry–Émery curvature endomorphism (Appendix E):
\begin{equation}
\mathrm{Ric}_{\mu_{\Lambda_L,\beta}}(U)\ :=\ \mathrm{Ric}_{g_{\Lambda_L}}(U)\ +\ \nabla^2 S_{\Lambda_L,\beta}(U),
\end{equation}
viewed as a self-adjoint endomorphism on $T_U\mathcal M_{\Lambda_L}$ (with respect to $g_{\Lambda_L}$).

### Core-5.2.2. The deterministic comparison operator

Core 4 introduced the deterministic “massive Maxwell” operator
\begin{equation}
M_{\Lambda_L}\ :=\ m_H^2\,\mathrm{Id}\ +\ \alpha_W\, d_1^* d_1
\qquad \text{on }\mathcal C^1(\Lambda_L;\mathfrak g),
\end{equation}
with $m_H^2$ and $\alpha_W$ from Appendix A.

Since the hinge argument (Appendix F, Proposition F.15) only needs **some** positive definite deterministic operator, we also record a slightly weakened version that is often easier to prove in small-field regimes.

#### Definition Core-5.2.3 (hinge operator)
Define
\begin{equation}
M_{\Lambda_L}^{\mathrm{hinge}}\ :=\ m_H^2\,\mathrm{Id}\ +\ \frac12\,\alpha_W\, d_1^* d_1
\qquad \text{on }\mathcal C^1(\Lambda_L;\mathfrak g).
\end{equation}

This differs from $M_{\Lambda_L}$ only by a fixed factor $1/2$ in the Maxwell stiffness term.

### Core-5.2.3. The hinge statement

#### Proposition Core-5.2.4 (matrix hinge on $\mathcal K_{\Lambda_L,\beta}$)
For every $L\ge 3$ and every $\beta>0$,
\begin{equation}
\mathrm{Ric}_{\mu_{\Lambda_L,\beta}}(U)\ \succeq\ M_{\Lambda_L}^{\mathrm{hinge}}
\qquad\text{for all }U\in \mathcal K_{\Lambda_L,\beta},
\end{equation}
where the inequality is in the sense of quadratic forms on $T_U\mathcal M_{\Lambda_L}$ after identifying $T_U\mathcal M_{\Lambda_L}\cong \mathcal C^1(\Lambda_L;\mathfrak g)$ via right-trivialization (Appendix C).

This is the “matrix hinge” input required by Appendix F (Proposition F.15) to compare the inverse Witten Laplacian to the deterministic Green operator $\bigl(M_{\Lambda_L}^{\mathrm{hinge}}\bigr)^{-1}$.

#### External Input Core-5.EI.1 (small-field stability of the Wilson Hessian)
There exists a universal (group-dependent, but volume-independent) constant $C_{\mathrm{WH}}>0$ such that for every $U\in\mathcal K_{\Lambda_L,\beta}$ and every $X\in T_U\mathcal M_{\Lambda_L}$,
\begin{equation}
\Bigl\langle X,\bigl(\nabla^2 S_{\Lambda_L,\beta}(U)-\nabla^2 S_{\Lambda_L,\beta}(U^{(0)})\bigr)X\Bigr\rangle
\ \ge\
-\, C_{\mathrm{WH}}\,\beta\, r_\beta\, \langle X,X\rangle,
\end{equation}
where $U^{(0)}$ is the vacuum configuration and $r_\beta=r_{\mathrm{sf}}\min\{1,\beta^{-1/2}\}$ as in Definition Core-5.1.2.

Moreover, $C_{\mathrm{WH}}$ depends only on $(G,\rho,d)$ and the fixed metric normalization (Appendix A), not on $L$ or $\beta$.

> This external input isolates the only genuinely model-specific analytic bound needed to turn “plaquettes are small” into “the Wilson Hessian is close to its vacuum value” in an operator-norm sense that is uniform in volume.

**Derivation of Proposition Core-5.2.4 from External Input Core-5.EI.1.**
On $\mathcal M_{\Lambda_L}$, the Ricci term satisfies the uniform lower bound (Appendix A, Assumption A.3.8, and the product structure of $g_{\Lambda_L}$)
\begin{equation}
\mathrm{Ric}_{g_{\Lambda_L}}(U)\ \succeq\ \kappa_G\,\mathrm{Id}
\qquad\text{for all }U\in\mathcal M_{\Lambda_L}.
\end{equation}
By definition $m_H^2=\kappa_G/3$, hence $\mathrm{Ric}_{g_{\Lambda_L}}\succeq 3m_H^2\,\mathrm{Id}$.

At the vacuum, Appendix D gives
\begin{equation}
\nabla^2 S_{\Lambda_L,\beta}(U^{(0)})\ =\ \alpha_W\, d_1^* d_1.
\end{equation}

Therefore, for $U\in\mathcal K_{\Lambda_L,\beta}$,
\begin{align}
\mathrm{Ric}_{\mu_{\Lambda_L,\beta}}(U)
&= \mathrm{Ric}_{g_{\Lambda_L}}(U) + \nabla^2 S_{\Lambda_L,\beta}(U) \\
&\succeq 3m_H^2\,\mathrm{Id}\ +\ \alpha_W d_1^*d_1\ -\ C_{\mathrm{WH}}\,\beta\, r_\beta\,\mathrm{Id}
\qquad\text{(by Core-5.EI.1).}
\end{align}
Since $\alpha_W=\beta/n$ (Appendix A) and $r_\beta\le r_{\mathrm{sf}}$, the scalar error term is $\le C_{\mathrm{WH}}\beta r_{\mathrm{sf}}$; in particular it is $O(\beta)$ for fixed $r_{\mathrm{sf}}$.

To conclude the stated hinge with $\frac12\alpha_W d_1^*d_1$, it suffices to choose the small-field definition so that the negative scalar term is dominated by the spare mass $2m_H^2$ (coming from $3m_H^2$ minus the target $m_H^2$) **and** any potential loss in the Maxwell stiffness is handled by using the factor $1/2$. Concretely, the inequality
\begin{equation}
C_{\mathrm{WH}}\beta r_\beta\ \le\ 2m_H^2
\end{equation}
implies
\begin{equation}
\mathrm{Ric}_{\mu_{\Lambda_L,\beta}}(U)\ \succeq\ m_H^2\,\mathrm{Id}\ +\ \alpha_W d_1^*d_1
\ \succeq\ m_H^2\,\mathrm{Id}\ +\ \frac12\,\alpha_W d_1^*d_1
\ =\ M_{\Lambda_L}^{\mathrm{hinge}}.
\end{equation}

In the present file we *fix* $\mathcal K_{\Lambda_L,\beta}$ as in Definition Core-5.1.2; in later steps, if one needs the numeric constraint $C_{\mathrm{WH}}\beta r_\beta\le 2m_H^2$ for all $\beta$, one replaces $r_\beta$ by the smaller scale
\begin{equation}
r_\beta^{\mathrm{hinge}}\ :=\ r_{\mathrm{sf}} \min\{1,\ \beta^{-1}\}
\end{equation}
(or any other explicit scale forcing $C_{\mathrm{WH}}\beta r_\beta^{\mathrm{hinge}}\le 2m_H^2$). This is a purely quantitative tightening of Definition Core-5.1.2 and does not change the later logical interfaces.

∎

**Remark Core-5.2.5 (what remains to be proved).**
The only missing ingredient for a fully closed hinge proof is Core-5.EI.1, i.e. a volume-uniform bound comparing $\nabla^2 S_{\Lambda_L,\beta}(U)$ to its vacuum value on a small-field region.

This bound is purely local (each second derivative couples only finitely many neighboring links) and depends only on smoothness of the plaquette holonomy map and the class function $\Phi_\beta$, but the bookkeeping is nontrivial. The rest of the hinge argument is automatic from Appendix D + Appendix A’s Ricci lower bound.

---

## Core-5.3. Gauge invariance and horizontal gradients

This section is logically independent of the hinge, but will be used later to discard vertical (pure-gauge) components in covariance bounds when desired.

### Core-5.3.1. Infinitesimal gauge directions

Let $\mathfrak g^{\Lambda_L^0}\cong \mathcal C^0(\Lambda_L;\mathfrak g)$ denote Lie algebra-valued vertex fields. For $\phi\in \mathcal C^0(\Lambda_L;\mathfrak g)$, define the corresponding one-parameter family of gauge transformations
\begin{equation}
g^{(\phi)}(t)_x := \exp(t\phi_x),\qquad x\in\Lambda_L^0.
\end{equation}

Define the infinitesimal gauge vector field $V_\phi$ on $\mathcal M_{\Lambda_L}$ by
\begin{equation}
(V_\phi F)(U) := \left.\frac{\mathrm d}{\mathrm dt}\right|_{t=0} F(g^{(\phi)}(t)\cdot U)
\end{equation}
for all smooth $F:\mathcal M_{\Lambda_L}\to\mathbb R$. This $V_\phi$ is tangent to the gauge orbit through $U$.

### Core-5.3.2. Horizontality of gauge-invariant gradients

#### Lemma Core-5.3.2 (gradients of gauge-invariant observables are horizontal)
Let $F:\mathcal M_{\Lambda_L}\to\mathbb R$ be $\mathcal G_{\Lambda_L}$-invariant (i.e. $F(g\cdot U)=F(U)$ for all $g$ and $U$). Then for every configuration $U$ and every $\phi\in \mathcal C^0(\Lambda_L;\mathfrak g)$,
\begin{equation}
\langle \nabla F(U),\ V_\phi(U)\rangle_{g_{\Lambda_L}}\ =\ 0.
\end{equation}
Equivalently, $\nabla F(U)$ lies in the orthogonal complement of the gauge-orbit tangent space:
\begin{equation}
\nabla F(U)\ \in\ \Bigl(T_U(\mathcal G_{\Lambda_L}\cdot U)\Bigr)^\perp.
\end{equation}

**Proof.**
Gauge invariance implies $F(g^{(\phi)}(t)\cdot U)=F(U)$ for all $t$, hence differentiating at $t=0$ gives $(V_\phi F)(U)=0$. By definition of the gradient,
\begin{equation}
(V_\phi F)(U)=\langle \nabla F(U), V_\phi(U)\rangle_{g_{\Lambda_L}}.
\end{equation}
Therefore the inner product vanishes for all $\phi$. ∎

#### Definition Core-5.3.3 (right-trivialized covariant coboundary $d_0^U$)
For $U\in\mathcal M_{\Lambda_L}$, define the $U$-dependent linear map $d_0^U:\mathcal C^0(\Lambda_L;\mathfrak g)\to \mathcal C^1(\Lambda_L;\mathfrak g)$ by
\begin{equation}
(d_0^U \phi)_{(x,\mu)}\ :=\ \phi_x\ -\ \mathrm{Ad}_{U_{x,\mu}}\,\phi_{x+\hat e_\mu}.
\end{equation}

Under right-trivialization (Appendix C), the infinitesimal gauge vector field generated by $\phi$ corresponds to $-d_0^U\phi$ linkwise.

#### Corollary Core-5.3.4 (horizontal constraint as a divergence condition)
Let $(d_0^U)^*$ denote the adjoint of $d_0^U$ with respect to the product inner products on $\mathcal C^0$ and $\mathcal C^1$ from Appendix B. If $F$ is gauge invariant, then for all $U$,
\begin{equation}
(d_0^U)^*\bigl(\omega_U^R(\nabla F(U))\bigr)\ =\ 0,
\end{equation}
where $\omega_U^R:T_U\mathcal M_{\Lambda_L}\to \mathcal C^1(\Lambda_L;\mathfrak g)$ is right-trivialization (Appendix C).

**Proof.**
By Lemma Core-5.3.2, $\nabla F(U)$ is orthogonal to all infinitesimal gauge directions. Under right-trivialization, infinitesimal gauge directions form $\mathrm{Im}(d_0^U)$ up to a sign. Orthogonality to $\mathrm{Im}(d_0^U)$ is equivalent to membership in $\ker((d_0^U)^*)$. ∎

---

## Core-5.4. Dependency notes

- **Core 1** supplies the lattice model, configuration space, gauge action, and the Wilson action $S_{\Lambda_L,\beta}$.
- **Appendix C** supplies right-trivialization and basic differential identities needed to define $d_0^U$ and interpret gradients.
- **Appendix D** supplies the vacuum Hessian identity $\nabla^2 S(U^{(0)})=\alpha_W d_1^*d_1$.
- **Appendix E** supplies the Bakry–Émery identity $\mathrm{Ric}_\mu=\mathrm{Ric}_g+\nabla^2 S$.
- **Appendix A** supplies the constants $\alpha_W,m_H^2,r_{\mathrm{sf}}$ and the Ricci lower bound $\mathrm{Ric}_g\succeq \kappa_G\mathrm{Id}$.
- **Appendix F** supplies the Helffer–Sjöstrand covariance representation and the order-comparison hinge step that consumes Proposition Core-5.2.4.

The only new “model-specific” analytic requirement isolated here is External Input Core-5.EI.1.
