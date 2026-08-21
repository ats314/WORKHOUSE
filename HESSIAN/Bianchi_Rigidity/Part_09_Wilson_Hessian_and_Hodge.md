# Part 9 — Wilson Hessian, Discrete Hodge Decomposition, and Physical Positivity

In Parts 6–8 we built the configuration–space geometry for lattice Yang–Mills: the product Lie-group manifold
\(M_\Lambda = G^{E(\Lambda)}\), the Haar volume, the gauge group action, and the Wilson plaquette action as a local,
gauge-invariant potential. Part 9 zooms in on the **second variation** of the Wilson action at the trivial connection
and explains how it acts on the different types of tangent directions: pure gauge, harmonic, and co-exact (physical)
modes.

Concretely, we will:

1. Identify the tangent space at the trivial configuration with the space of \(\mathfrak{g}\)-valued lattice 1‑cochains.
2. Expand the Wilson action to second order and show that its Hessian is a discrete Maxwell operator
   \(2 c_W\, d_1^* d_1\) on 1‑cochains.fileciteturn6file9
3. Use **discrete Hodge theory** to decompose 1‑cochains into pure gauge, harmonic, and co-exact pieces and to
   understand the kernel and positive directions of the Hessian.fileciteturn6file0
4. Isolate the **physical positivity** statement: on the co-exact (physical) part of the horizontal subspace the Wilson
   Hessian is strictly positive, while gauge directions remain flat.fileciteturn4file3
5. Preview how adding the Haar “mass” from Part 6 turns this into a **uniformly positive** Hessian on all horizontal
   directions once we include the Haar curvature term.fileciteturn5file3turn4file13turn5file0

This is the “linearized Yang–Mills = discrete Maxwell + Haar mass” chapter.


---

## 9.1. Tangent 1‑cochains at the trivial configuration

### 9.1.1. Configuration manifold and metric

For a finite hypercubic lattice \(\Lambda \subset \mathbb{Z}^d\) with oriented edge set \(E(\Lambda)\), the configuration
manifold is
\[
M_\Lambda := G^{E(\Lambda)}, \qquad U = (U_\ell)_{\ell \in E(\Lambda)},
\]
equipped with the product Riemannian metric
\[
g_\Lambda(U)(V,W)
  := \sum_{\ell \in E(\Lambda)} g_G(U_\ell)(V_\ell, W_\ell),
\]
where \((G,g_G)\) is the compact Lie group with a fixed bi-invariant metric (for example \(G = \mathrm{SU}(N)\)).fileciteturn6file3

We single out the **trivial configuration**
\[
U^{(0)} = (U_\ell^{(0)})_{\ell\in E(\Lambda)}, \qquad U_\ell^{(0)} = e \ \ \forall \ell,
\]
where \(e\) is the identity of \(G\).

### 9.1.2. Exponential coordinates and 1‑cochains

For configurations in a small neighborhood of \(U^{(0)}\), each link variable can be written in exponential coordinates
\[
U_\ell = \exp_G(X_\ell), \qquad X_\ell \in U_0 \subset \mathfrak{g},
\]
where \(U_0\) is a small neighborhood of \(0 \in \mathfrak{g}\). Thus a configuration near \(U^{(0)}\) is described by a
collection
\[
X = (X_\ell)_{\ell \in E(\Lambda)} \in \mathfrak{g}^{E(\Lambda)}.
\]

We regard this as a \(\mathfrak{g}\)-valued **1‑cochain** on the lattice and write
\[
\mathcal{C}^1(\Lambda;\mathfrak{g}) := \{ X = (X_\ell)_{\ell\in E(\Lambda)} : X_\ell \in \mathfrak{g} \}.
\]

Using right-invariant identifications \(T_{U_\ell}G \cong \mathfrak{g}\), the metric \(g_\Lambda\) at \(U^{(0)}\) induces the
standard product inner product on \(\mathcal{C}^1(\Lambda;\mathfrak{g})\):
\[
\langle X, Y\rangle_{\mathcal{C}^1}
  := \sum_{\ell\in E(\Lambda)} \langle X_\ell, Y_\ell\rangle_G,
  \qquad
  |X|_{\mathcal{C}^1}^2 = \sum_{\ell\in E(\Lambda)} |X_\ell|_G^2.
\]fileciteturn6file3

In particular, we obtain an isometric identification
\[
T_{U^{(0)}} M_\Lambda \;\cong\; \mathcal{C}^1(\Lambda;\mathfrak{g}),
\]
and we will freely identify tangent vectors at \(U^{(0)}\) with 1‑cochains in what follows.

---

## 9.2. Plaquette holonomy and the discrete exterior derivative

We now express the plaquette holonomy in these exponential coordinates and identify its linearization as a discrete curl.

### 9.2.1. Plaquettes and holonomy

Fix a plaquette
\[
p = (x;\mu,\nu),
\]
with basepoint \(x\in \Lambda\) and oriented directions \(1\le \mu < \nu\le d\). Its holonomy is the ordered product of
link variables around the plaquette:
\[
U_p(U)
  = U_{x,\mu}\, U_{x+\hat\mu,\nu}\, U_{x+\hat\nu,\mu}^{-1}\, U_{x,\nu}^{-1}.
\]fileciteturn6file3

In exponential coordinates
\[
U_{x,\mu} = \exp_G(X_{x,\mu}), \quad
U_{x+\hat\mu,\nu} = \exp_G(X_{x+\hat\mu,\nu}), \quad
U_{x+\hat\nu,\mu} = \exp_G(X_{x+\hat\nu,\mu}), \quad
U_{x,\nu} = \exp_G(X_{x,\nu}),
\]
so \(U_p\) is a product of exponentials of small Lie-algebra elements.fileciteturn6file3

### 9.2.2. The discrete exterior derivative \(d_1\)

We define the **discrete exterior derivative** (or discrete curl)
\[
d_1 : \mathcal{C}^1(\Lambda;\mathfrak{g}) \longrightarrow \mathcal{C}^2(\Lambda;\mathfrak{g})
\]
by
\[
(d_1 X)_p
  := X_{x,\mu}
     + X_{x+\hat\mu,\nu}
     - X_{x+\hat\nu,\mu}
     - X_{x,\nu},
\]
for the plaquette \(p = (x;\mu,\nu)\) with the above orientation. This is the standard coboundary from edge
cochains to plaquette cochains; for different orientations, signs are adjusted in the usual way.

Thus \(d_1 X\) is a \(\mathfrak{g}\)-valued 2‑cochain, which we denote by \(\mathcal{C}^2(\Lambda;\mathfrak{g})\). Equipped
with the product inner product
\[
\langle Y, Z\rangle_{\mathcal{C}^2}
  := \sum_{p\in P(\Lambda)} \langle Y_p, Z_p\rangle_G,
\]
we obtain a Hilbert space structure on plaquette cochains as well.

### 9.2.3. Linearized holonomy

Using the Baker–Campbell–Hausdorff expansion and the smallness of \(X\), one checks that the plaquette holonomy
admits an expansion of the form
\[
U_p(U) = \exp_G\big( (d_1 X)_p + \mathcal{O}(|X|^2)\big),
\]
uniformly for all plaquettes \(p\) in a small neighborhood of the origin \(X=0\). The linear term in the exponent is
exactly the discrete curvature \(d_1 X\); higher-order terms involve commutators of the \(X_\ell\) and are quadratic or
higher in \(X\).

This is the discrete analogue of \(F = dA + A\wedge A\) in the continuum: at quadratic order, only the linear \(dA\)
term matters.

---

## 9.3. Quadratic expansion of the Wilson action

### 9.3.1. The Wilson action in exponential coordinates

Recall that the Wilson plaquette action is
\[
S_W(U)
  = \frac{\beta}{N} \sum_{p\subset \Lambda} \mathrm{Re}\,\mathrm{Tr}\big( I - U_p(U) \big),
\]
where \(U_p(U)\) is the plaquette holonomy and \(\beta = \frac{2N}{g_0^2}\). For \(U\) close to the trivial configuration
\(U^{(0)}\), we write \(U = \exp(X)\) in exponential coordinates as above.

Expanding \(U_p(U)\) using the BCH formula and the linearization from §9.2, one finds that
\[
S_W(U) = S_W(U^{(0)}) + S_W^{(2)}(X) + \mathcal{O}(|X|^3),
\]
where the quadratic term can be written as
\[
S_W^{(2)}(X)
  = \frac{\beta c_{HS}}{N} \sum_{p\in P(\Lambda)} \big| (d_1 X)_p \big|_G^2
  = \frac{\beta c_{HS}}{N}\, \|d_1 X\|_{\mathcal{C}^2}^2
\]
for some universal constant \(c_{HS}>0\) depending only on the choice of inner product and trace normalization on
\(\mathfrak{g}\).fileciteturn6file9

This is already the discrete Maxwell energy: it is the \(L^2\)-norm of the lattice curvature \(d_1 X\).

### 9.3.2. Hessian from the quadratic form

By definition of the Hessian,
\[
S_W^{(2)}(X) = \frac{1}{2} \big\langle X, \nabla^2 S_W(U^{(0)}) X\big\rangle_{\mathcal{C}^1}.
\]
Comparing this with the expression above and using the adjoint \(d_1^* : \mathcal{C}^2 \to \mathcal{C}^1\), characterized by
\[
\langle d_1 X, Y\rangle_{\mathcal{C}^2} = \langle X, d_1^* Y\rangle_{\mathcal{C}^1},
\]
we obtain
\[
S_W^{(2)}(X)
  = \frac{\beta c_{HS}}{N}\, \langle d_1 X, d_1 X\rangle_{\mathcal{C}^2}
  = \frac{\beta c_{HS}}{N}\, \langle X, d_1^* d_1 X\rangle_{\mathcal{C}^1}.
\]

On the other hand,
\[
S_W^{(2)}(X)
  = \frac{1}{2} \langle X, \nabla^2 S_W(U^{(0)}) X\rangle_{\mathcal{C}^1}.
\]
Since these two quadratic forms agree for all \(X\), we deduce the **operator identity**
\[
\nabla^2 S_W(U^{(0)}) = 2 c_W\, d_1^* d_1,
\qquad
c_W := \frac{\beta c_{HS}}{N} > 0.
\]fileciteturn6file9

This is the central algebraic fact of this part: the Wilson Hessian at the trivial configuration is a positive scalar
multiple of the **discrete 1‑form Laplacian** \(d_1^* d_1\).

> **Proposition 9.1 (Wilson Hessian as discrete Maxwell operator).**  
> At the trivial configuration \(U^{(0)}\), the Hessian of the Wilson action acts on
> \(\mathcal{C}^1(\Lambda;\mathfrak{g})\) as
> \[
> \nabla^2 S_W(U^{(0)}) = 2 c_W\, d_1^* d_1,
> \]
> a positive scalar multiple of the discrete Maxwell operator on 1‑cochains.

---

## 9.4. Nonnegativity and kernel: closed forms as zero modes

From the representation
\[
\nabla^2 S_W(U^{(0)}) = 2 c_W\, d_1^* d_1,
\]
the basic spectral properties are immediate:

1. \(\nabla^2 S_W(U^{(0)})\) is **self-adjoint** on \(\mathcal{C}^1(\Lambda;\mathfrak{g})\).
2. \(\nabla^2 S_W(U^{(0)})\) is **nonnegative**:
   \[
   \big\langle X, \nabla^2 S_W(U^{(0)}) X\big\rangle_{\mathcal{C}^1}
     = 2 c_W\, \|d_1 X\|_{\mathcal{C}^2}^2 \ge 0.
   \]
3. Its kernel is the space of 1‑cochains annihilated by \(d_1\):
   \[
   \ker\big(\nabla^2 S_W(U^{(0)})\big)
     = \{ X \in \mathcal{C}^1 : d_1 X = 0\}
     =: \ker d_1.
   \]fileciteturn6file2

We interpret \(\ker d_1\) as the space of **discrete closed 1‑forms**: those whose lattice curl vanishes around every
plaquette. In continuum language, these are connections with vanishing linearized field strength.

> **Corollary 9.2 (Nonnegativity and closed-form kernel).**  
> The Hessian \(\nabla^2 S_W(U^{(0)})\) is self-adjoint and nonnegative on
> \(\mathcal{C}^1(\Lambda;\mathfrak{g})\), with kernel equal to the space of discrete closed 1‑forms
> \(\ker d_1\).

This matches the physical picture: the quadratic energy cost for small fluctuations depends only on their discrete
field strength. If \(d_1 X = 0\), the quadratic Wilson energy vanishes; such directions are flat at quadratic order and
must be understood via the gauge geometry and Haar mass.

To refine this picture, we now bring in the discrete Hodge decomposition.

---

## 9.5. Discrete gradient, Laplacians, and Hodge decomposition

### 9.5.1. The discrete gradient \(d_0\) and adjoints

Let \(\mathcal{C}^0(\Lambda;\mathfrak{g})\) denote the space of \(\mathfrak{g}\)-valued vertex fields
\(\varphi = (\varphi_x)_{x\in V(\Lambda)}\). The **discrete gradient**
\[
d_0 : \mathcal{C}^0(\Lambda;\mathfrak{g}) \to \mathcal{C}^1(\Lambda;\mathfrak{g})
\]
is the coboundary operator from vertices to edges, defined on an oriented edge \((x,\mu)\) by
\[
(d_0 \varphi)_{x,\mu} := \varphi_{x+\hat\mu} - \varphi_x.
\]fileciteturn6file0

We equip \(\mathcal{C}^0(\Lambda;\mathfrak{g})\) with the standard product inner product
\[
\langle \varphi,\psi\rangle_{\mathcal{C}^0} := \sum_{x\in V(\Lambda)} \langle \varphi_x,\psi_x\rangle_G.
\]
With the inner products on \(\mathcal{C}^0,\mathcal{C}^1,\mathcal{C}^2\) specified, we denote by
\[
d_0^* : \mathcal{C}^1 \to \mathcal{C}^0, \qquad d_1^* : \mathcal{C}^2 \to \mathcal{C}^1
\]
the Hilbert adjoints of \(d_0\) and \(d_1\), characterized by
\[
\langle d_0 \varphi, X\rangle_{\mathcal{C}^1} = \langle \varphi, d_0^* X\rangle_{\mathcal{C}^0},
\quad
\langle d_1 X, Y\rangle_{\mathcal{C}^2} = \langle X, d_1^* Y\rangle_{\mathcal{C}^1}.
\]

### 9.5.2. Hodge Laplacians and harmonic forms

The **discrete Hodge Laplacians** are then defined by
\[
\Delta_0 := d_0^* d_0 : \mathcal{C}^0 \to \mathcal{C}^0,
\qquad
\Delta_1 := d_0 d_0^* + d_1^* d_1 : \mathcal{C}^1 \to \mathcal{C}^1.
\]fileciteturn6file0

The operator \(\Delta_1\) is self-adjoint and nonnegative, and its kernel consists of **harmonic 1‑forms**:
\[
\ker(\Delta_1)
  = \{ X\in \mathcal{C}^1 : d_1 X = 0,\ d_0^* X = 0\}.
\]fileciteturn6file0

These are precisely those closed 1‑forms that are also co-closed. On a simply connected finite lattice (e.g. a box
with periodic or Dirichlet boundary conditions), \(\ker(\Delta_1)\) is finite-dimensional and encodes global
“toron-like” modes (constant fluxes around noncontractible cycles); in a strictly contractible region it may be trivial.

### 9.5.3. The discrete Hodge decomposition

Standard finite-dimensional Hodge theory on cell complexes yields an orthogonal decomposition
\[
\mathcal{C}^1(\Lambda;\mathfrak{g})
  = \mathrm{im}(d_0)
    \;\oplus\;
    \ker(\Delta_1)
    \;\oplus\;
    \mathrm{im}(d_1^*),
\]
with all three summands pairwise orthogonal with respect to \(\langle \cdot,\cdot\rangle_{\mathcal{C}^1}\).

Concretely:

- \(\mathrm{im}(d_0)\) consists of **exact** 1‑forms, i.e. discrete gradients of vertex fields. These will turn out to be
  **pure gauge** directions.
- \(\ker(\Delta_1)\) consists of **harmonic** 1‑forms, closed and co-closed.
- \(\mathrm{im}(d_1^*)\) consists of **co-exact** 1‑forms, i.e. co-differentials of plaquette fields, which will be the
  strictly **physical** modes.

Because
\[
\ker(d_1) = \{ X : d_1 X = 0\},
\]
and
\[
\ker(d_1) = \mathrm{im}(d_0) \oplus \ker(\Delta_1),
\]
we see that the kernel of the Wilson Hessian consists of the sum of exact and harmonic 1‑forms; the co-exact part
\(\mathrm{im}(d_1^*)\) is the locus of strict positivity.

---

## 9.6. Gauge directions, horizontal subspace, and physical modes

We now tie the Hodge decomposition back to the geometry of gauge orbits developed in Parts 6–8.

### 9.6.1. Vertical directions and pure gauge modes

The lattice gauge group \(\mathcal{G}_\Lambda = G^{V(\Lambda)}\) acts on configurations by
\[
(g\cdot U)_{x,\mu} = g_x\, U_{x,\mu}\, g_{x+\hat\mu}^{-1}.
\]
The **vertical subspace** \(V_U \subset T_U M_\Lambda\) is, by definition, the tangent space to the gauge orbit
\(\mathcal{O}_U := \{g\cdot U: g\in\mathcal{G}_\Lambda\}\).fileciteturn5file12

At the trivial configuration \(U^{(0)}\), a gauge variation generated by a vertex field
\(\varphi \in \mathcal{C}^0(\Lambda;\mathfrak{g})\) is
\[
g_x(t) = \exp_G(t\varphi_x),
\quad
U_{x,\mu}(t)
  = g_x(t)\, U_{x,\mu}^{(0)}\, g_{x+\hat\mu}(t)^{-1}
  = \exp_G\big( t(\varphi_{x+\hat\mu} - \varphi_x)\big) + \mathcal{O}(t^2).
\]
Thus the tangent variation at \(t=0\) is
\[
\left.\frac{d}{dt}\right|_{t=0} U_{x,\mu}(t)
  = \varphi_{x+\hat\mu} - \varphi_x
  = (d_0 \varphi)_{x,\mu}.
\]

Under the identification \(T_{U^{(0)}}M_\Lambda \cong \mathcal{C}^1(\Lambda;\mathfrak{g})\), this shows that
\[
V_{U^{(0)}} = \mathrm{im}(d_0) \subset \mathcal{C}^1(\Lambda;\mathfrak{g}).
\]

So the exact 1‑forms are precisely the **vertical (pure gauge)** tangent directions.

### 9.6.2. Horizontal subspace and its Hodge description

By definition (see Part 6), the **horizontal subspace** at \(U\) is the orthogonal complement of the vertical space:
\[
H_U := V_U^\perp \subset T_U M_\Lambda.
\]fileciteturn5file12

At the trivial configuration, the orthogonal complement of \(\mathrm{im}(d_0)\) is
\[
H_{U^{(0)}} = \big(\mathrm{im}(d_0)\big)^\perp = \ker(d_0^*) \subset \mathcal{C}^1(\Lambda;\mathfrak{g}).
\]

Combining this with the Hodge decomposition, we get
\[
H_{U^{(0)}}
  = \ker(d_0^*)
  = \ker(\Delta_1) \oplus \mathrm{im}(d_1^*).
\]

Thus the horizontal tangent space at the vacuum decomposes as
\[
\underbrace{\ker(\Delta_1)}_{\text{harmonic (global)}} \;\oplus\;
\underbrace{\mathrm{im}(d_1^*)}_{\text{co-exact (physical)}}.
\]

From the perspective of gauge-invariant observables \(f\), we know that \(\nabla f(U)\in H_U\) for all \(U\), and in
particular \(\nabla f(U^{(0)}) \in H_{U^{(0)}}\).fileciteturn5file12 Hence only harmonic and co-exact directions are
relevant for physical gradients; the pure gauge directions never appear in the gradient of gauge-invariant functions.

---

## 9.7. Physical positivity of the Wilson Hessian

We now combine the Hessian formula and the Hodge decomposition to isolate the physically relevant positivity
properties of \(\nabla^2 S_W(U^{(0)})\).

### 9.7.1. Action on the Hodge components

Recall that
\[
\nabla^2 S_W(U^{(0)}) = 2 c_W\, d_1^* d_1,
\]
and that
\[
\mathcal{C}^1
  = \mathrm{im}(d_0) \oplus \ker(\Delta_1) \oplus \mathrm{im}(d_1^*).
\]

On each component we have:

1. If \(X = d_0 \varphi\) is **pure gauge**, then \(d_1 X = d_1 d_0 \varphi = 0\) (since \(d_1 d_0 = 0\)), and hence
   \[
   \nabla^2 S_W(U^{(0)}) X = 0.
   \]
   Pure gauge directions are flat directions of the Wilson quadratic form.

2. If \(X\in \ker(\Delta_1)\) is **harmonic**, then in particular \(d_1 X = 0\), so again
   \[
   \nabla^2 S_W(U^{(0)}) X = 0.
   \]

3. If \(X \in \mathrm{im}(d_1^*)\) is **co-exact**, we can write \(X = d_1^* Y\) for some \(Y\in\mathcal{C}^2\). Then
   \[
   \nabla^2 S_W(U^{(0)}) X
     = 2 c_W d_1^* d_1 (d_1^* Y)
     = 2 c_W d_1^* \big( d_1 d_1^* Y \big).
   \]
   Here \(d_1 d_1^*\) is the plaquette Laplacian on 2‑cochains. On a finite lattice with suitable boundary conditions
   (e.g. a periodic box or a contractible region), discrete Hodge theory ensures that there are **no harmonic 2‑forms**
   in the co-exact 1‑form sector, so \(d_1 d_1^*\) is strictly positive on \(\mathrm{im}(d_1)\). Consequently, the only way
   for \(\nabla^2 S_W(U^{(0)}) X\) to vanish with \(X\in \mathrm{im}(d_1^*)\) is for \(X=0\).

Formally, the restriction of \(d_1^* d_1\) to \(\mathrm{im}(d_1^*)\) has a **strictly positive spectral gap**:
\[
\exists\,\lambda_{\min} > 0 \text{ such that }
  \langle X, d_1^* d_1 X\rangle_{\mathcal{C}^1}
    \ge \lambda_{\min} \, |X|_{\mathcal{C}^1}^2
  \quad\forall X\in \mathrm{im}(d_1^*).
\]

> **Theorem 9.3 (Physical positivity of the Wilson Hessian).**  
> On the Hodge decomposition of \(\mathcal{C}^1(\Lambda;\mathfrak{g})\),
> \[
> \mathcal{C}^1 = \mathrm{im}(d_0) \oplus \ker(\Delta_1) \oplus \mathrm{im}(d_1^*),
> \]
> the Wilson Hessian \(\nabla^2 S_W(U^{(0)})\) satisfies:
> 
> 1. \(\nabla^2 S_W(U^{(0)})\) vanishes on the pure gauge and harmonic subspaces:
>    \[
>    \nabla^2 S_W(U^{(0)})|_{\mathrm{im}(d_0) \oplus \ker(\Delta_1)} = 0.
>    \]
> 2. \(\nabla^2 S_W(U^{(0)})\) is **strictly positive definite** on the co-exact subspace \(\mathrm{im}(d_1^*)\):
>    \[
>    \big\langle X, \nabla^2 S_W(U^{(0)}) X\big\rangle_{\mathcal{C}^1}
>      \ge 2 c_W \lambda_{\min} |X|_{\mathcal{C}^1}^2
>      \quad\forall X\in \mathrm{im}(d_1^*),
>    \]
>    for some \(\lambda_{\min} > 0\) depending only on the lattice geometry and \(G\).

In particular, on the **horizontal subspace**
\[
H_{U^{(0)}}
  = \ker(\Delta_1) \oplus \mathrm{im}(d_1^*),
\]
the Hessian is nonnegative, with kernel equal to the harmonic sector and strictly positive on the co-exact part.fileciteturn4file3turn5file3

This is exactly the statement that the Wilson action provides a **quadratic confinement** for physical (co-exact)
fluctuations near the trivial configuration, while leaving gauge and global modes flat.

### 9.7.2. Relation to the “physical” Hessian in P‑language

In the proof file language of P09, the restriction of the Hessian to the physical subspace
\(H_{U^{(0)}} = \ker(\Delta_1)\oplus\mathrm{im}(d_1^*)\) is written as
\[
H_W|_{\mathrm{phys}} = \beta\, M,
\]
where \(M\) is precisely the lattice 1‑form Laplacian restricted to the physical modes, and one proves
\[
H_W|_{\mathrm{phys}} \ge \beta \lambda_{\min}(M) > 0.
\]fileciteturn5file3

Our discrete Hodge formulation re-packages this as the positivity of \(d_1^* d_1\) on the co-exact subspace and
the identification of the physical subspace \(H_{U^{(0)}}\) with harmonic \(\oplus\) co-exact 1‑forms.

---

## 9.8. Adding Haar mass: towards full horizontal positivity

So far we have analyzed only the Wilson action. Part 6 showed that the Haar geometry of \(G\) already provides a
“mass-like” quadratic form, via either the Ricci curvature of \((M_\Lambda,g_\Lambda)\) or, in exponential
coordinates, a product Haar potential with strictly positive Hessian at the identity.fileciteturn6file11turn5file6

Let \(S_{H,\Lambda}\) denote this Haar potential in exponential coordinates, and write
\[
S_{\text{eff},\Lambda} = S_W + S_{H,\Lambda}
\]
for the combined potential with respect to the flat reference measure in those coordinates. At the trivial
configuration, we have
\[
\nabla^2 S_{H,\Lambda}(U^{(0)}) = c_0\, \mathrm{Id}
\]
for some constant \(c_0>0\) depending only on \(G\) (e.g. \(c_0 = \frac{N^2-1}{2N}\) for \(\mathrm{SU}(N)\)).fileciteturn4file13turn5file0

On the physical subspace \(H_{U^{(0)}}\), the **effective Hessian** is therefore
\[
\nabla^2 S_{\text{eff},\Lambda}(U^{(0)})|_{H_{U^{(0)}}}
  = \nabla^2 S_W(U^{(0)})|_{H_{U^{(0)}}}
    + c_0\, \mathrm{Id}_{H_{U^{(0)}}}.
\]

Since \(\nabla^2 S_W(U^{(0)})\) is nonnegative on \(H_{U^{(0)}}\) and strictly positive on the co-exact part, we obtain:

> **Corollary 9.4 (Effective physical Hessian with Haar mass).**  
> On the physical horizontal subspace \(H_{U^{(0)}}\),
> \[
> \nabla^2 S_{\text{eff},\Lambda}(U^{(0)})|_{H_{U^{(0)}}}
>   \ge c_0\, \mathrm{Id}_{H_{U^{(0)}}},
> \]
> i.e. the effective Hessian is **strictly positive definite** on all physical modes (harmonic and co-exact), with a
> spectral gap at least \(c_0>0\) which is independent of the lattice volume.fileciteturn5file3turn5file0

In the P‑file notation this is exactly the statement
\[
H_{\mathrm{eff}}|_{\mathrm{phys}} = H_W|_{\mathrm{phys}} + c_0 I \ge c_0 I,
\]
which is the key input for the lattice log–Sobolev inequality of P10 and for the horizontal Bakry–Émery curvature
bounds in Part 10.fileciteturn5file0turn4file3

---

## 9.9. Summary and role in the overall program

Let us collect the main outputs of this part:

1. **Linearization:** The tangent space at the trivial configuration is the 1‑cochain space
   \(\mathcal{C}^1(\Lambda;\mathfrak{g})\) with the product inner product.fileciteturn6file3

2. **Hessian = discrete Maxwell:** The Hessian of the Wilson action at \(U^{(0)}\) is
   \[
   \nabla^2 S_W(U^{(0)}) = 2 c_W\, d_1^* d_1,
   \]
   a positive scalar multiple of the discrete 1‑form Laplacian.fileciteturn6file9

3. **Kernel = closed forms:** The kernel consists of discrete closed 1‑forms \(\ker(d_1)\).fileciteturn6file2

4. **Hodge decomposition and gauge geometry:** Using discrete Hodge theory and the gauge group action, we identify
   \[
   \mathcal{C}^1
     = \underbrace{\mathrm{im}(d_0)}_{\text{vertical / pure gauge}}
       \oplus
       \underbrace{\ker(\Delta_1)}_{\text{harmonic}}
       \oplus
       \underbrace{\mathrm{im}(d_1^*)}_{\text{co-exact (physical)}},
   \]
   and the horizontal physical subspace at the vacuum as
   \[
   H_{U^{(0)}} = \ker(\Delta_1) \oplus \mathrm{im}(d_1^*).fileciteturn6file0turn5file12turn4file3
   \]

5. **Physical positivity:** The Wilson Hessian is nonnegative on \(H_{U^{(0)}}\), with kernel equal to the harmonic
   sector and strictly positive definite on the co-exact physical sector. This is the rigorous form of “quadratic
   confinement” for small physical fluctuations.

6. **Effective mass from Haar:** Adding the Haar mass term gives an effective Hessian on \(H_{U^{(0)}}\) bounded below
   by \(c_0 I\), with \(c_0>0\) independent of \(\Lambda\). This is the key ingredient for the local horizontal Bakry–Émery
   curvature bound in Part 10 and the lattice log–Sobolev inequality in P10.fileciteturn4file13turn5file0turn4file3

In the global 20‑part structure, Part 9 is where the abstract curvature machinery of Parts 1–5 meets the concrete
lattice Yang–Mills interaction in its **quadratic, physical** incarnation. After this, Part 10 will combine Haar curvature
and the Wilson Hessian into a local horizontal Bakry–Émery curvature bound, and Part 11 will package Parts 6–10
into the “core curvature theorem” that feeds directly into the analytic interface of Part 5.
