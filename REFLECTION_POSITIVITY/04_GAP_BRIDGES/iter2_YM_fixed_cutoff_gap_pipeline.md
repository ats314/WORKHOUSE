# Fixed-Cutoff Lattice Yang–Mills: A Coercivity-to-Gap Pipeline via Bakry–Émery and OS

\newcommand{\dd}{\mathrm{d}}
\newcommand{\Id}{\mathrm{Id}}
\newcommand{\Cov}{\mathrm{Cov}}
\newcommand{\EE}{\mathbb{E}}
\newcommand{\RR}{\mathbb{R}}
\newcommand{\CC}{\mathbb{C}}

## Abstract

This document isolates a **potentially theory-developing** technical spine: a route from a *local curvature/convexity inequality* (a “matrix hinge” lower bound on Bakry–Émery curvature) to *Euclidean-time exponential decay* of correlations, and then—via Osterwalder–Schrader (OS) reconstruction—to a **spectral gap** of a reconstructed Hamiltonian at fixed lattice cutoff.

What is distinctive here is the strict separation of three interfaces:

1. **Deterministic pointwise coercivity** on a canonical “good set” $\mathcal K$ (no probability).
2. **Conditional covariance representation and kernel decay** under $\mu(\cdot\mid\mathcal K)$ (geometry + analysis).
3. **Localization + typicality** to pass from conditional to unconditional covariances, entering only as an additive $O(\mu(\mathcal K^c))$ error—never as a subtraction in the coercivity inequality.

The final OS gap extraction requires only Euclidean-time decay of centered OS correlations; no lattice geometry enters at that final step.

This document is self-contained; where existence of certain reflecting diffusions or OS reconstruction is required, it is stated as an explicit external analytic input.

---

## 1. Lattice, gauge group, and configuration space

### 1.1 Periodic 4D lattice

Fix a 4D periodic box
\[
\Lambda_L := \prod_{\mu=0}^3 (\mathbb{Z}/L_\mu\mathbb{Z}),
\qquad L_\mu\ge 2.
\]
The distinguished Euclidean time direction is $\mu=0$.

A positively oriented link is a pair $b=(x,\mu)$ representing the directed edge $x\to x+\hat e_\mu$ (addition mod $L$). Let $E(\Lambda_L)$ be the set of positively oriented links, and let $P(\Lambda_L)$ be the set of oriented plaquettes $p=(x;\mu,\nu)$ with $\mu<\nu$.

### 1.2 Gauge group and representation

Let $G$ be a compact Lie group with a fixed faithful unitary representation $\rho:G\to U(n)$. We use $\Re\mathrm{Tr}$ in this representation. Equip $G$ with a bi-invariant Riemannian metric induced from the trace form on $\mathfrak g$.

### 1.3 Configuration manifold

The configuration space is the compact manifold
\[
M_{\Lambda_L} := G^{E(\Lambda_L)}
\]
with product Riemannian metric $g_{\Lambda_L}=\oplus_{b\in E}g_G$ and volume form $\mathrm{vol}_{g_{\Lambda_L}}$.

A configuration is $U=(U_b)_{b\in E}\in M_{\Lambda_L}$.

---

## 2. Wilson action and Gibbs measure

### 2.1 Plaquette holonomy

For $p=(x;\mu,\nu)$ define the plaquette holonomy
\[
U_p(U) := U_{x,\mu}\,U_{x+\hat e_\mu,\nu}\,U_{x+\hat e_\nu,\mu}^{-1}\,U_{x,\nu}^{-1}\in G.
\]

### 2.2 Single-plaquette potential and Wilson action

Fix $\beta>0$ and define
\[
\Phi_\beta(V) := \beta\left(1-\frac{1}{n}\Re\mathrm{Tr}(V)\right),\qquad V\in G.
\]
Then the Wilson action is
\[
S_{\Lambda_L,\beta}(U) := \sum_{p\in P(\Lambda_L)} \Phi_\beta(U_p(U)).
\]

### 2.3 Gibbs measure

Define the Gibbs probability measure
\[
\mu_{\Lambda_L,\beta}(\dd U) := Z^{-1}e^{-S_{\Lambda_L,\beta}(U)}\,\mathrm{vol}_{g_{\Lambda_L}}(\dd U).
\]
For an observable $F$, write $\EE[F]=\int F\,\dd\mu$ and
\[
\Cov_\mu(F,G):=\EE[FG]-\EE[F]\EE[G].
\]

---

## 3. Differential calculus as cochains (right-trivialization)

### 3.1 Right-trivialization

At each link factor, right-trivialize tangent vectors by the map
\[
\omega_{U_b}^R:T_{U_b}G\to\mathfrak g,\qquad \omega_{U_b}^R(v)=(\dd R_{U_b^{-1}})_{U_b}v.
\]
On the product manifold, this identifies
\[
T_U M_{\Lambda_L}\cong \mathfrak g^{E(\Lambda_L)}=:\mathcal C^1(\Lambda_L;\mathfrak g)
\]
(the space of $\mathfrak g$-valued 1-cochains).

Under this identification, gradients $\nabla F(U)$ can be viewed as 1-cochains $\nabla^R F(U)\in \mathcal C^1$.

### 3.2 Discrete coboundary operators

Define the coboundary $d_1:\mathcal C^1\to\mathcal C^2$ by
\[
(d_1X)_p := \sum_{b\in E}\sigma_{p,b}X_b,
\]
where $\sigma_{p,b}\in\{-1,0,+1\}$ are incidence coefficients from the oriented boundary of $p$. The adjoint $d_1^*:\mathcal C^2\to\mathcal C^1$ is defined by the $\ell^2$ inner products. The discrete Maxwell operator is
\[
\mathsf M_1 := d_1^*d_1\ \succeq\ 0.
\]

---

## 4. Vacuum linearization: why the Hessian is Maxwell

### 4.1 Vacuum configuration

Let $U^{(0)}\in M_{\Lambda_L}$ be the vacuum configuration $U^{(0)}_b=\mathbf 1$ for all links.

### 4.2 Linearization of plaquette holonomy at the vacuum

Consider the curve $U(t)$ defined by linkwise exponentials
\[
U_b(t):=\exp(tX_b),
\qquad X\in\mathcal C^1(\Lambda_L;\mathfrak g).
\]
Differentiate the plaquette holonomy at $t=0$. Since all factors equal identity at $0$,
\[
\left.\frac{\dd}{\dd t}\right|_{t=0}U_p(U(t))
=
X_{x,\mu}+X_{x+\hat e_\mu,\nu}-X_{x+\hat e_\nu,\mu}-X_{x,\nu}
=
(d_1X)_p.
\]
Thus the differential of the holonomy map at the vacuum is exactly $d_1$.

### 4.3 Hessian of the Wilson action at the vacuum

Because $\nabla\Phi_\beta(\mathbf 1)=0$, the vacuum is a critical point:
\[
\nabla S_{\Lambda_L,\beta}(U^{(0)})=0.
\]
The second derivative arises from composing the holonomy linearization with the Hessian of $\Phi_\beta$ at identity. Along a group geodesic $\exp(tY)$ one finds
\[
\left.\frac{\dd^2}{\dd t^2}\right|_{t=0}\Phi_\beta(\exp(tY))
=
\alpha_W\,|Y|_{\mathfrak g}^2,
\qquad \alpha_W:=\beta/n>0.
\]
Combining with the chain rule and the identity in §4.2 yields the operator identity on cochains:
\[
\boxed{
\nabla^2 S_{\Lambda_L,\beta}(U^{(0)}) = \alpha_W\,d_1^*d_1 = \alpha_W\,\mathsf M_1.
}
\tag{4.1}
\]

This is the key “Maxwell emerges from Wilson vacuum” statement.

---

## 5. Bakry–Émery curvature and the matrix hinge on a good set

### 5.1 Gibbs generator and Bakry–Émery curvature

Let $\mathcal L$ be the symmetric diffusion generator for $\mu$:
\[
\mathcal L := \Delta_{g_{\Lambda_L}} - \langle \nabla S, \nabla(\cdot)\rangle.
\]
Bakry–Émery theory associates the curvature endomorphism
\[
\mathrm{Ric}_\mu(U) := \mathrm{Ric}_{g_{\Lambda_L}}(U) + \nabla^2 S(U),
\]
acting on $T_U M_{\Lambda_L}$.

Because $g_{\Lambda_L}$ is a product of a compact group metric, $\mathrm{Ric}_{g_{\Lambda_L}}$ has a uniform positive lower bound:
\[
\mathrm{Ric}_{g_{\Lambda_L}}(U)\ \succeq\ \kappa_G\,\Id
\quad\text{for all }U.
\]
Define the mass parameter
\[
m_H^2 := \kappa_G/3>0.
\]

### 5.2 Canonical good set \(\mathcal K\)

Fix a small-field radius $r_{\mathrm{sf}}>0$ so that the logarithm chart $\log$ is unique on $\exp(B_{r_{\mathrm{sf}}}(0))\subset G$.

Define
\[
r_\beta := r_{\mathrm{sf}}\min\{1,\beta^{-1/2}\}.
\]
Define the canonical good set
\[
\mathcal K_{\Lambda_L,\beta}:=\left\{U:\ U_p(U)\in \exp(B_{r_\beta}(0))\ \text{for all plaquettes }p\right\}.
\]
Equivalently all plaquette logs exist and satisfy $\sup_p \|\log U_p\|\le r_\beta$.

This set is gauge invariant because conjugation is an isometry of $G$.

### 5.3 Small-field stability of the Wilson Hessian (analytic input)

**External analytic input (Hessian stability).**
There exists a constant $C_{\mathrm{WH}}>0$ such that for all $U\in\mathcal K_{\Lambda_L,\beta}$ and all tangent vectors $X$,
\[
\langle X,(\nabla^2S(U)-\nabla^2S(U^{(0)}))X\rangle
\ge -C_{\mathrm{WH}}\,\beta\,r_\beta\,\langle X,X\rangle.
\tag{5.1}
\]
This is the only genuinely model-specific control required: it upgrades “plaquettes are small” into “the drift Hessian is close to its vacuum value”.

### 5.4 The matrix hinge

Using (4.1), (5.1), and $\mathrm{Ric}_{g_{\Lambda_L}}\succeq 3m_H^2\Id$,
\[
\mathrm{Ric}_\mu(U)
=
\mathrm{Ric}_{g_{\Lambda_L}}(U)+\nabla^2S(U)
\succeq
3m_H^2\Id + \alpha_W\mathsf M_1 - C_{\mathrm{WH}}\beta r_\beta\,\Id.
\]
If the small-field scale is chosen so that $C_{\mathrm{WH}}\beta r_\beta\le 2m_H^2$, then for all $U\in\mathcal K$,
\[
\boxed{
\mathrm{Ric}_\mu(U)\ \succeq\ m_H^2\Id + \tfrac12\alpha_W \mathsf M_1.
}
\tag{5.2}
\]
Define the deterministic comparison operator
\[
M^{\mathrm{hinge}} := m_H^2\Id + \tfrac12\alpha_W d_1^*d_1.
\]

**Crucial interface point:** (5.2) is deterministic and pointwise *on* $\mathcal K$; probability enters later, not here.

---

## 6. Conditional covariance via Helffer–Sjöstrand (HS)

### 6.1 HS representation (analytic input)

On a domain with reflecting boundary (here, $\mathcal K$ has piecewise smooth boundary), there exists a reflecting diffusion reversible w.r.t. $\mu(\cdot\mid \mathcal K)$ with generator $\mathcal L_{\mathcal K}$. A Helffer–Sjöstrand representation gives, for sufficiently smooth observables $F,G$,
\[
\boxed{
\Cov_{\mu(\cdot\mid\mathcal K)}(F,G)
=
\left\langle \nabla F,\ (\mathcal L_{\mathcal K}^{(1)})^{-1}\nabla G\right\rangle_{L^2(\mu\mid\mathcal K)},
}
\tag{6.1}
\]
where $\mathcal L^{(1)}$ is the Witten Laplacian on 1-forms associated to $\mathcal L$.

### 6.2 Using the hinge: operator comparison

Bakry–Émery calculus yields a quadratic-form lower bound for $\mathcal L^{(1)}$ in terms of $\mathrm{Ric}_\mu$. In particular, the matrix hinge (5.2) implies
\[
\mathcal L_{\mathcal K}^{(1)} \ \succeq\ M^{\mathrm{hinge}}
\quad\Rightarrow\quad
(\mathcal L_{\mathcal K}^{(1)})^{-1}\ \preceq\ (M^{\mathrm{hinge}})^{-1}.
\tag{6.2}
\]
Insert (6.2) into (6.1) to reduce covariance bounds to kernel bounds for $(M^{\mathrm{hinge}})^{-1}$.

---

## 7. Exponential clustering under \(\mu(\cdot\mid\mathcal K)\) from finite range

The operator $d_1^*d_1$ has finite range on links: it couples only links sharing plaquettes. Therefore $M^{\mathrm{hinge}}$ is a massive finite-range operator.

A standard Combes–Thomas/finite-range inverse-decay argument implies its Green kernel decays exponentially in link-graph distance:
\[
|(M^{\mathrm{hinge}})^{-1}(b,b')|\ \le\ C\,e^{-\eta\,\mathrm{dist}_E(b,b')}.
\tag{7.1}
\]
If $F$ and $G$ are cylinder observables supported on link sets separated by distance $\ge n$ in the time direction, their gradients are supported near the same sets, and (6.1)–(7.1) imply
\[
\boxed{
|\Cov_{\mu(\cdot\mid\mathcal K)}(F,\tau_{n\hat e_0}G)| \le C_{F,G}\,e^{-\eta n}.
}
\tag{7.2}
\]

This is **conditional exponential clustering**.

---

## 8. Localization algebra: from conditional to unconditional covariances

Let $\mathcal K$ be any event with $0<\mu(\mathcal K)<1$. Define conditional measures $\mu_{\mathcal K}:=\mu(\cdot\mid\mathcal K)$ and $\mu_{\mathcal K^c}:=\mu(\cdot\mid\mathcal K^c)$.

A direct identity gives
\[
\Cov_\mu(F,G)
=
\mu(\mathcal K)\Cov_{\mu_{\mathcal K}}(F,G)
+
\mu(\mathcal K^c)\Cov_{\mu_{\mathcal K^c}}(F,G)
+
\mu(\mathcal K)\mu(\mathcal K^c)\Delta_{\mathcal K}F\,\Delta_{\mathcal K}G,
\tag{8.1}
\]
where $\Delta_{\mathcal K}F := \mu_{\mathcal K}(F)-\mu_{\mathcal K^c}(F)$.

For bounded $F,G$ one has universal bounds
\[
|\Cov_{\nu}(F,G)|\le 4\|F\|_\infty\|G\|_\infty,
\qquad
|\Delta_{\mathcal K}F|\le 2\|F\|_\infty.
\]
Therefore
\[
\boxed{
|\Cov_\mu(F,G)|
\le
|\Cov_{\mu_{\mathcal K}}(F,G)|
+
8\|F\|_\infty\|G\|_\infty\,\mu(\mathcal K^c).
}
\tag{8.2}
\]

**This is the only place probability enters:** through the additive tail $\mu(\mathcal K^c)$.

### 8.1 Typicality input

A typicality mechanism aims to show
\[
\boxed{\mu(\mathcal K^c)\le e^{-c|P(\Lambda_L)|}}
\tag{8.3}
\]
so the “bad set” probability is exponentially small in volume (or in the number of plaquettes).

Combining (7.2), (8.2), and (8.3) yields unconditional Euclidean-time exponential decay for centered correlations, up to an $n$-independent exponentially small error.

---

## 9. OS reconstruction and gap extraction

### 9.1 OS data and transfer operator (analytic input)

Assume the measure $\mu$ is translation invariant and reflection positive with respect to time reflection $\Theta$. Let $\mathcal A_+$ be the positive-time algebra of bounded observables supported at nonnegative times. Define the OS sesquilinear form
\[
\langle F,G\rangle_{\mathrm{OS}} := \mu((\theta F)G),\qquad (\theta F)(U)=\overline{F(\Theta U)}.
\]
Reflection positivity implies $\langle F,F\rangle_{\mathrm{OS}}\ge 0$.

OS reconstruction provides a Hilbert space $\mathcal H_{\mathrm{OS}}$ and a positive self-adjoint contraction $T$ such that
\[
\langle[F],T^n[G]\rangle_{\mathrm{OS}} = \mu((\theta F)\,\tau_{n\hat e_0}G).
\tag{9.1}
\]
Functional calculus yields $T=e^{-a_{\lat}H}$ for a self-adjoint $H\ge 0$.

### 9.2 Euclidean decay implies spectral gap

Let $\psi=[F]$ be a centered vector ($\mu(F)=0$). Then (9.1) expresses a time-separated centered correlation as a matrix element of $T^n=e^{-na_{\lat}H}$:
\[
\langle\psi,e^{-na_{\lat}H}\psi\rangle = \Cov_\mu(F,\tau_{n\hat e_0}F).
\]
If
\[
|\Cov_\mu(F,\tau_{n\hat e_0}F)| \le C\,e^{-\eta n}
\quad\text{for all }n\ge n_0,
\tag{9.2}
\]
a spectral-measure argument implies the spectral support of $\psi$ lies in $[\eta/a_{\lat},\infty)$, hence the Hamiltonian has a gap at least $\eta/a_{\lat}$ on the cyclic subspace generated by $\mathcal A_+$.

Under standard cyclicity assumptions, this yields
\[
\boxed{\mathrm{gap}(H)\ \ge\ \eta/a_{\lat}.}
\tag{9.3}
\]

**Key point:** OS gap extraction needs only the Euclidean-time decay input (9.2); it is agnostic about how (9.2) was proved.

---

## 10. Why this pipeline is a promising “new theory” direction

The novelty is not any one inequality; it is the *modular composability*:

- A local deterministic inequality (matrix hinge) controls a global observable (mass gap).
- Probability (typicality) enters only as a small additive correction in a localization identity.
- OS reconstruction turns a Euclidean statement into a Hamiltonian spectral statement with no further structure.

This architecture suggests a potentially general template for proving gaps in other lattice field theories: identify a vacuum Hessian with a finite-range massive operator; prove small-field stability to create a deterministic hinge; bound conditional covariances by an inverse kernel; then lift to the full measure and apply OS.

The main expansion tasks are to (i) prove the Hessian stability input (5.1) with explicit group constants, and (ii) establish typicality (8.3) in the regime of interest (large $\beta$ or scaling trajectories).
