# Part II — Lattice Yang–Mills as a Curvature–Controlled Gibbs Measure  
## Section 4 — Hessian of the Wilson Action and Physical Positivity Near the Identity

In this section we analyze the **second variation** (Hessian) of the Wilson action \(S_W\) at the **trivial configuration** \(U_\ell = \mathbf{1}_G\) for all edges \(\ell\in E(\Lambda)\), and we express it in terms of discrete cochain operators on the lattice.

The goals are:

1. To obtain an explicit quadratic form representing the Hessian \(\nabla^2 S_W\) at the identity,
2. To show that this Hessian is **nonnegative**, with a kernel precisely corresponding to discrete closed 1-forms,
3. To identify the **physical subspace** on which \(\nabla^2 S_W\) is strictly positive (modulo harmonic modes), as preparation for combining it later with the Haar curvature and gauge-fixing contributions.

We work throughout in a sufficiently small neighborhood of the identity in the **right-invariant exponential coordinates** described below, and we restrict attention to the linearized theory.

---

## 4.1. Right-invariant exponential coordinates on the configuration manifold

We first fix local coordinates around the identity in \(G\) and hence around the trivial configuration in \(M_\Lambda\).

### 4.1.1. Exponential map on a compact Lie group

Let \(\exp_G : \mathfrak{g}\to G\) be the Lie group exponential map. Since \(G\) is compact and connected, there exists a neighborhood \(\mathcal{U}_0 \subset \mathfrak{g}\) of \(0\) such that
\[
\exp_G : \mathcal{U}_0 \to \exp_G(\mathcal{U}_0)
\]
is a diffeomorphism onto an open neighborhood of the identity element \(e\in G\).

We fix such a neighborhood and write \(U = \exp_G(X)\) for \(X\in\mathcal{U}_0\). We identify \(T_e G \cong \mathfrak{g}\) via the chosen inner product \(\langle\cdot,\cdot\rangle_G\).

### 4.1.2. Link coordinates

On the configuration manifold \(M_\Lambda = G^{E(\Lambda)}\), take the trivial configuration
\[
U^{(0)} = (U^{(0)}_\ell)_{\ell\in E(\Lambda)}, \quad U^{(0)}_\ell = e \ \forall \ell.
\]

For configurations in a small neighborhood of \(U^{(0)}\), we can write each link variable as
\[
U_\ell = \exp_G(X_\ell),\quad X_\ell \in \mathcal{U}_0 \subset \mathfrak{g}.
\]

Thus we can use the vector \(X = (X_\ell)_{\ell\in E(\Lambda)}\in \mathfrak{g}^{E(\Lambda)}\) as local coordinates on \(M_\Lambda\) near \(U^{(0)}\). The origin \(X=0\) corresponds to \(U^{(0)}\).

### 4.1.3. Inner product and norm in coordinates

Using right-invariance and the product metric \(g_\Lambda\), the norm of a tangent vector at \(U^{(0)}\) corresponding to \(X\in\mathfrak{g}^{E(\Lambda)}\) is
\[
\|X\|^2 := \sum_{\ell\in E(\Lambda)} |X_\ell|_G^2,
\]
with \(|X_\ell|_G^2 = \langle X_\ell,X_\ell\rangle_G\).

The identification
\[
T_{U^{(0)}} M_\Lambda \cong \mathfrak{g}^{E(\Lambda)}
\]
is thus isometric with respect to \(g_\Lambda\).

---

## 4.2. Linearized plaquette holonomy and second-order expansion of the Wilson term

We now express the plaquette holonomies \(U_p(U)\) in terms of the coordinates \(X_\ell\) and expand the Wilson action to second order around \(X=0\).

### 4.2.1. Linearized plaquette holonomy

Fix a plaquette \(p = (x;\mu,\nu)\) with basepoint \(x\) and directions \(1\le\mu<\nu\le d\). In terms of link variables, we recall:
\[
U_p(U)
= U_{x,\mu}\, U_{x+\hat\mu,\nu}\, U_{x+\hat\nu,\mu}^{-1}\, U_{x,\nu}^{-1}.
\]

In right-invariant exponential coordinates, write
\[
U_{x,\mu} = \exp_G(X_{x,\mu}),
\quad U_{x+\hat\mu,\nu} = \exp_G(X_{x+\hat\mu,\nu}),
\quad U_{x+\hat\nu,\mu} = \exp_G(X_{x+\hat\nu,\mu}),
\quad U_{x,\nu} = \exp_G(X_{x,\nu}).
\]

Let us denote, for simplicity,
\[
X_1 := X_{x,\mu},\quad
X_2 := X_{x+\hat\mu,\nu},\quad
X_3 := X_{x+\hat\nu,\mu},\quad
X_4 := X_{x,\nu}.
\]

Then
\[
U_p(U) = \exp_G(X_1)\, \exp_G(X_2)\, \exp_G(-X_3)\, \exp_G(-X_4).
\]

Using the Baker–Campbell–Hausdorff (BCH) formula, there exists a (smooth) map \(\Phi : \mathfrak{g}^4 \to \mathfrak{g}\) such that
\[
U_p(U) = \exp_G\big(\Phi(X_1,X_2,-X_3,-X_4)\big),
\]
and \(\Phi\) has an expansion
\[
\Phi(X_1,X_2,-X_3,-X_4)
= X_1 + X_2 - X_3 - X_4 + \mathcal{O}(\|X\|^2).
\]

To second order in the \(X_i\), the linear term is simply
\[
A_p(X) := X_1 + X_2 - X_3 - X_4.
\]

The quadratic and higher-order corrections in \(\Phi\) contribute only to order \(\mathcal{O}(\|X\|^2)\) or higher in the Wilson action; for the Hessian, we only need the quadratic term of \(S_W\), which is determined entirely by the **linear** part \(A_p(X)\).

Thus, to compute the Hessian at \(X=0\), we may replace \(U_p(U)\) by \(\exp_G(A_p(X))\) at the level of second-order Taylor expansions.

### 4.2.2. Second-order expansion of the Wilson plaquette term

For \(G = SU(N)\), we recall
\[
S_p(U)
= \beta \left(1 - \frac{1}{N} \Re \operatorname{Tr} U_p(U)\right).
\]

At the identity, \(U_p(U^{(0)}) = \mathbf{1}\), and
\[
\frac{1}{N} \Re \operatorname{Tr} \mathbf{1} = 1,
\quad S_p(U^{(0)}) = 0.
\]

For small \(Y\in\mathfrak{su}(N)\), we have the Taylor expansion
\[
\frac{1}{N} \Re \operatorname{Tr} \exp_G(Y)
= 1 + \frac{1}{2N} \Re\operatorname{Tr}(Y^2) + \mathcal{O}(\|Y\|^3),
\]
using that \(\operatorname{Tr}(Y) = 0\) and that \(\Re\operatorname{Tr}(Y^2)\) is real and typically negative for anti-Hermitian \(Y\). In particular, there exists a positive constant \(c_{\mathrm{HS}}>0\), depending only on the chosen inner product on \(\mathfrak{su}(N)\), such that
\[
-\Re\operatorname{Tr}(Y^2) = c_{\mathrm{HS}}\,\|Y\|_G^2,
\]
where \(\|\cdot\|_G\) is the norm induced by \(\langle\cdot,\cdot\rangle_G\).

Thus, to second order,
\[
\begin{aligned}
S_p(U)
&= \beta\left(1 - \frac{1}{N} \Re \operatorname{Tr} \exp_G(A_p(X))\right) \\
&= \beta\left(1 - \left[1 + \frac{1}{2N}\Re\operatorname{Tr}(A_p(X)^2) + \mathcal{O}(\|X\|^3)\right]\right) \\
&= -\frac{\beta}{2N}\Re\operatorname{Tr}(A_p(X)^2) + \mathcal{O}(\|X\|^3) \\
&= \frac{\beta c_{\mathrm{HS}}}{2N}\,\|A_p(X)\|_G^2 + \mathcal{O}(\|X\|^3).
\end{aligned}
\]

Hence the **quadratic approximation** to the plaquette term is
\[
S_p^{(2)}(X) := \frac{\beta c_{\mathrm{HS}}}{2N}\,\|A_p(X)\|_G^2.
\]

Summing over plaquettes,
\[
S_W^{(2)}(X) := \sum_{p\in P(\Lambda)} S_p^{(2)}(X)
= \frac{\beta c_{\mathrm{HS}}}{2N} \sum_{p\in P(\Lambda)} \|A_p(X)\|_G^2.
\]

By definition of the Hessian at \(X=0\),
\[
\frac{1}{2} \langle X, \nabla^2 S_W(U^{(0)}) X \rangle
= S_W^{(2)}(X).
\]

We now recast this quadratic form in a more geometric discrete-operator language.

---

## 4.3. Discrete cochains and the operator \(d_1^* d_1\)

The structure \(A_p(X) = X_1 + X_2 - X_3 - X_4\) is exactly the **discrete exterior derivative** of a 1-cochain evaluated on a plaquette.

### 4.3.1. Discrete cochain spaces

Let us define:

- \(\mathcal{C}^0(\Lambda;\mathfrak{g}) := \mathfrak{g}^{V(\Lambda)}\): 0-cochains (site fields),
- \(\mathcal{C}^1(\Lambda;\mathfrak{g}) := \mathfrak{g}^{E(\Lambda)}\): 1-cochains (edge/link fields),
- \(\mathcal{C}^2(\Lambda;\mathfrak{g}) := \mathfrak{g}^{P(\Lambda)}\): 2-cochains (plaquette fields),

each endowed with the product inner product induced from \(\langle\cdot,\cdot\rangle_G\) on \(\mathfrak{g}\). For example, for \(X,Y\in\mathcal{C}^1\),
\[
\langle X,Y\rangle_1 = \sum_{\ell\in E(\Lambda)} \langle X_\ell,Y_\ell\rangle_G,
\]
and analogously for \(\mathcal{C}^0\) and \(\mathcal{C}^2\).

### 4.3.2. Discrete exterior derivative \(d_1 : \mathcal{C}^1 \to \mathcal{C}^2\)

Define the operator
\[
d_1 : \mathcal{C}^1(\Lambda;\mathfrak{g}) \to \mathcal{C}^2(\Lambda;\mathfrak{g})
\]
by
\[
(d_1 X)_p := \sum_{\ell\in \partial p} \epsilon_{p,\ell} X_\ell,
\]
where:

- \(\partial p\) is the oriented boundary of plaquette \(p\),
- \(\epsilon_{p,\ell} = +1\) if \(\ell\) appears in \(\partial p\) with the same orientation as in \(E(\Lambda)\), and \(-1\) if it appears with opposite orientation.

For the plaquette \(p = (x;\mu,\nu)\) with our fixed orientation convention, the boundary consists of edges
\[
(x,\mu),\ (x+\hat\mu,\nu),\ (x+\hat\nu,\mu)^{-1},\ (x,\nu)^{-1},
\]
and we indeed have
\[
(d_1 X)_p = X_{x,\mu} + X_{x+\hat\mu,\nu} - X_{x+\hat\nu,\mu} - X_{x,\nu} = A_p(X).
\]

Thus the linearization of the plaquette holonomy logarithm is precisely the cochain derivative:
\[
A_p(X) = (d_1 X)_p.
\]

### 4.3.3. Quadratic form and \(d_1^* d_1\)

Let \(d_1^* : \mathcal{C}^2 \to \mathcal{C}^1\) be the adjoint of \(d_1\) with respect to the inner products \(\langle\cdot,\cdot\rangle_1\) and \(\langle\cdot,\cdot\rangle_2\). Then for all \(X\in\mathcal{C}^1\), \(Y\in\mathcal{C}^2\),
\[
\langle d_1 X, Y\rangle_2 = \langle X,d_1^* Y\rangle_1.
\]

From the expression for \(S_W^{(2)}\) and the identification \(A_p(X) = (d_1 X)_p\), we may write
\[
S_W^{(2)}(X)
= c_W \sum_{p\in P(\Lambda)} \|(d_1 X)_p\|_G^2
= c_W \,\langle d_1 X, d_1 X\rangle_2,
\]
with
\[
c_W := \frac{\beta c_{\mathrm{HS}}}{2N} > 0.
\]

Equivalently,
\[
S_W^{(2)}(X)
= c_W\, \langle X, d_1^* d_1 X\rangle_1.
\]

Comparing with
\[
\frac{1}{2} \langle X,\nabla^2 S_W(U^{(0)})X\rangle = S_W^{(2)}(X),
\]
we obtain the explicit expression for the Hessian at the trivial configuration:

> **Proposition 4.1 (Hessian of the Wilson action at the identity).**  
> In the right-invariant exponential coordinates \(X\in\mathcal{C}^1(\Lambda;\mathfrak{g})\) around the trivial configuration \(U^{(0)}\), the Hessian of the Wilson action at \(U^{(0)}\) is
> \[
> \nabla^2 S_W(U^{(0)}) = 2 c_W\, d_1^* d_1,
> \]
> where \(c_W>0\) depends only on \(\beta\), \(N\), and the normalization of the inner product on \(\mathfrak{g}\).

In particular, \(\nabla^2 S_W(U^{(0)})\) is a **self-adjoint, nonnegative operator** on \(\mathcal{C}^1(\Lambda;\mathfrak{g})\).

---

## 4.4. Nonnegativity and characterization of the kernel

We now analyze the spectral properties of \(d_1^* d_1\) on the 1-cochain space \(\mathcal{C}^1(\Lambda;\mathfrak{g})\).

### 4.4.1. Nonnegativity

For any \(X\in \mathcal{C}^1(\Lambda;\mathfrak{g})\),
\[
\langle X, d_1^* d_1 X\rangle_1
= \langle d_1 X, d_1 X\rangle_2
= \sum_{p\in P(\Lambda)} \|(d_1 X)_p\|_G^2
\ge 0.
\]

Consequently,
\[
\langle X, \nabla^2 S_W(U^{(0)}) X\rangle
= \beta\kappa\, \langle X,d_1^* d_1 X\rangle_1
\ge 0.
\]

Thus \(\nabla^2 S_W(U^{(0)})\) is positive semidefinite.

### 4.4.2. Kernel of \(d_1^* d_1\)

From the above expression, we see that
\[
\langle X, d_1^* d_1 X\rangle_1 = 0
\quad\Longleftrightarrow\quad
d_1 X = 0.
\]

Thus
\[
\ker(d_1^* d_1) = \ker(d_1) = \{ X\in \mathcal{C}^1(\Lambda;\mathfrak{g}) : d_1 X = 0\},
\]
i.e. the space of **discrete closed 1-forms** (1-cochains with vanishing discrete curl).

In terms of the Wilson action, these are precisely the directions along which the plaquette curvature remains zero to first order, and the quadratic Wilson cost vanishes.

---

## 4.5. Relation to gauge directions and harmonic modes (discrete Hodge decomposition)

To interpret the kernel, we recall the standard discrete Hodge decomposition on a finite cell complex.

### 4.5.1. Discrete gradient and Laplacian

Define the discrete gradient (0-to-1 cochain map)
\[
d_0 : \mathcal{C}^0(\Lambda;\mathfrak{g}) \to \mathcal{C}^1(\Lambda;\mathfrak{g}),
\]
by
\[
(d_0 \phi)_{x,\mu} := \phi_{x+\hat\mu} - \phi_x
\]
for a 0-cochain \(\phi \in \mathcal{C}^0(\Lambda;\mathfrak{g})\).

Its adjoint
\[
d_0^* : \mathcal{C}^1 \to \mathcal{C}^0
\]
is the discrete divergence, and the discrete Laplacians
\[
\Delta_0 := d_0^* d_0 : \mathcal{C}^0 \to \mathcal{C}^0,
\quad
\Delta_1 := d_1^* d_1 + d_0 d_0^* : \mathcal{C}^1 \to \mathcal{C}^1
\]
appear in the standard combinatorial Hodge theory.

### 4.5.2. Hodge decomposition on a finite complex

On a finite lattice \(\Lambda\) with appropriate boundary conditions (e.g. periodic), one has a finite-dimensional Hodge decomposition:
\[
\mathcal{C}^1
= \mathrm{im}(d_0) \oplus \ker(\Delta_1) \oplus \mathrm{im}(d_1^*).
\]

Intuitively:

- \(\mathrm{im}(d_0)\) are **pure gauge directions** (gradients of 0-cochains),
- \(\ker(\Delta_1)\) are **harmonic 1-forms** (torons),
- \(\mathrm{im}(d_1^*)\) are **co-exact 1-forms** corresponding to physical fluctuations of the field strength.

Since \(d_1\circ d_0 = 0\), we have \(\mathrm{im}(d_0)\subset\ker(d_1)\). Also, \(\ker(d_1) = \mathrm{im}(d_0)\oplus \ker(\Delta_1)\). Therefore,
\[
\ker(d_1^* d_1) = \ker(d_1) = \mathrm{im}(d_0)\oplus \ker(\Delta_1),
\]
i.e. the kernel consists precisely of the **gauge plus harmonic** modes.

### 4.5.3. Positivity on the co-exact (physical) subspace

On the co-exact subspace
\[
\mathcal{C}^1_{\mathrm{coex}} := \mathrm{im}(d_1^*) \subset \mathcal{C}^1,
\]
we have \(d_1\) injective (no nontrivial co-exact 1-form can be closed), hence
\[
d_1^* d_1 X = 0 \quad\Longrightarrow\quad X=0
\]
for \(X\in \mathcal{C}^1_{\mathrm{coex}}\). Thus \(d_1^* d_1\) is **strictly positive** on \(\mathcal{C}^1_{\mathrm{coex}}\).

Equivalently:

> **Proposition 4.2 (Wilson Hessian positivity on co-exact modes).**  
> Restrict the Hessian \(\nabla^2 S_W(U^{(0)}) = \beta\kappa d_1^* d_1\) to the co-exact subspace \(\mathcal{C}^1_{\mathrm{coex}} = \mathrm{im}(d_1^*) \subset \mathcal{C}^1(\Lambda;\mathfrak{g})\). Then:
> 1. \(\nabla^2 S_W(U^{(0)})\big|_{\mathcal{C}^1_{\mathrm{coex}}}\) is positive definite,
> 2. Its spectrum on \(\mathcal{C}^1_{\mathrm{coex}}\) consists of finitely many strictly positive eigenvalues,
> 3. In particular, there exists \(\lambda_{\min}(\Lambda) > 0\) (depending on \(\Lambda\)) such that
>    \[
>    \langle X, \nabla^2 S_W(U^{(0)}) X\rangle
>    \ge \beta\kappa\, \lambda_{\min}(\Lambda) \|X\|^2
>    \quad \forall X\in \mathcal{C}^1_{\mathrm{coex}}.
>    \]

The constant \(\lambda_{\min}(\Lambda)\) is the lowest nonzero eigenvalue of \(d_1^* d_1\) on the co-exact 1-forms. It depends on the lattice geometry and volume; we do **not** claim any uniform lower bound in \(\Lambda\) here. Uniformity will rely on additional geometric or probabilistic input and (if needed) will be treated separately.

---

## 4.6. Connection with horizontal (physical) directions

Recall from Section&nbsp;3 that the **vertical subspace** \(V_U\) consists of gauge directions, and the **horizontal subspace** \(H_U = V_U^\perp\) is defined as their orthogonal complement with respect to the product metric \(g_\Lambda\).

At the trivial configuration \(U^{(0)}\), the vertical subspace \(V_{U^{(0)}}\) corresponds (in the right-invariant identification \(T_{U^{(0)}} M_\Lambda \cong \mathcal{C}^1(\Lambda;\mathfrak{g})\)) to \(\mathrm{im}(d_0)\). Thus, at \(U^{(0)}\),
\[
V_{U^{(0)}} \cong \mathrm{im}(d_0),
\quad
H_{U^{(0)}} \cong \big(\mathrm{im}(d_0)\big)^\perp.
\]

Using the Hodge decomposition, we may decompose
\[
H_{U^{(0)}} \cong \ker(\Delta_1) \oplus \mathrm{im}(d_1^*).
\]

- The component \(\ker(\Delta_1)\) consists of **harmonic 1-forms** (torons),
- The component \(\mathrm{im}(d_1^*)\) consists of **co-exact 1-forms**, which are the genuinely physical modes affected by the Wilson action to quadratic order.

The Hessian \(\nabla^2 S_W(U^{(0)})\):

- Vanishes on \(\ker(d_1) = \mathrm{im}(d_0) \oplus \ker(\Delta_1)\),
- Is strictly positive on \(\mathrm{im}(d_1^*)\).

Thus, modulo gauge and harmonic degeneracies, the Wilson action provides a **positive quadratic form** on the physical horizontal directions at the trivial configuration.

In later sections, when we incorporate:

- the **Haar/Jacobian contribution**,
- possible **gauge-fixing terms**,

these additional contributions will lift some of these degeneracies (including, in particular, toron modes) and furnish a **uniform positive lower bound** on the Hessian in the horizontal directions. That strengthened statement will realize the full Hypothesis H\(_{\mathrm{curv}}\) in the Yang–Mills context.

---

## 4.7. Summary of Section 4 — Linearized Wilson Hessian and Physical Positivity

We have obtained the following:

1. Using right-invariant exponential coordinates \(X\in \mathcal{C}^1(\Lambda;\mathfrak{g})\) around the trivial configuration, the Hessian of the Wilson action satisfies
   \[
   \nabla^2 S_W(U^{(0)}) = \beta\kappa\, d_1^* d_1,
   \]
   where \(d_1\) is the discrete exterior derivative mapping edge fields to plaquette fields.

2. The quadratic form is nonnegative:
   \[
   \langle X, \nabla^2 S_W(U^{(0)}) X\rangle
   = \frac{\beta\kappa}{2} \sum_{p\in P(\Lambda)} \|(d_1 X)_p\|_G^2 \ge 0.
   \]

3. The kernel is exactly the set of discrete **closed 1-forms**:
   \[
   \ker(\nabla^2 S_W(U^{(0)})) = \ker(d_1)
   = \mathrm{im}(d_0) \oplus \ker(\Delta_1),
   \]
   corresponding to pure gauge directions and harmonic 1-forms (torons).

4. On the **co-exact 1-form subspace** \(\mathrm{im}(d_1^*)\), the Hessian is strictly positive; the associated smallest eigenvalue \(\lambda_{\min}(\Lambda)>0\) depends on the lattice, but is bounded away from zero for each fixed finite \(\Lambda\).

5. At the trivial configuration, the horizontal (physical) tangent space \(H_{U^{(0)}}\) decomposes into harmonic plus co-exact components; the Wilson Hessian is strictly positive on the co-exact part, and vanishes on pure gauge + harmonic modes.

This local linearized analysis of the Wilson action provides the core algebraic structure needed in Part II:

- It identifies the **physical curvature operator** \(d_1^* d_1\),
- It shows that the Wilson action already drives positivity on co-exact modes,
- And it sets the stage for adding Haar and gauge-fixing contributions to obtain a **uniform horizontal Bakry–Émery curvature bound** in a neighborhood of the identity, as required by the abstract curvature hypothesis H\(_{\mathrm{curv}}\) from Part I.
