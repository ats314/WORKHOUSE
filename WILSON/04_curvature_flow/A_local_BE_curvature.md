# Local Bakry–Émery curvature for lattice Yang–Mills near the vacuum

This note isolates (with full proofs and explicit constants) a *local* Bakry–Émery curvature lower bound for the lattice Yang–Mills Gibbs measure on a finite lattice. The bound is uniform in the lattice volume. The mechanism is:

* product-group Ricci curvature from the Haar geometry, plus  
* a uniform small-field control of the Wilson action Hessian via locality and bounded third derivatives.

No global concentration is proved here; the result is a local (small-field) curvature bound.

---

## 1. Lattice, configuration manifold, and metric

Let \(\Lambda\subset\mathbb Z^d\) be a finite hypercubic region, \(d\ge 2\).

* \(E(\Lambda)\): oriented nearest-neighbor edges (links).  
* \(P(\Lambda)\): oriented plaquettes (choose one orientation per geometric plaquette).

Let \(G\) be a compact, connected Lie group, and let \(\mathfrak g=\mathrm{Lie}(G)\).
Fix an \(\mathrm{Ad}\)-invariant inner product \(\langle\cdot,\cdot\rangle_{\mathfrak g}\) on \(\mathfrak g\).
Equip \(G\) with the induced bi-invariant Riemannian metric \(g_G\), and equip the product manifold
\[
M_\Lambda := G^{E(\Lambda)}
\]
with the product metric \(g_\Lambda\). Denote the corresponding Riemannian volume form by \(\mathrm{vol}_{g_\Lambda}\); this equals product Haar volume on \(G^{E(\Lambda)}\).

Let \(U^{(0)}\in M_\Lambda\) be the vacuum configuration \(U^{(0)}_\ell=e\) for all links \(\ell\).

---

## 2. Generator, carré du champ, and Bakry–Émery tensor

Let \(S_\Lambda:M_\Lambda\to\mathbb R\) be a \(C^2\) action functional. Define the Gibbs measure
\[
\mu_\Lambda(\mathrm dU) = Z_\Lambda^{-1} e^{-S_\Lambda(U)}\,\mathrm{vol}_{g_\Lambda}(\mathrm dU),
\qquad
Z_\Lambda=\int_{M_\Lambda} e^{-S_\Lambda}\,\mathrm{vol}_{g_\Lambda}.
\]

Let \(\Delta_\Lambda\) be the Laplace–Beltrami operator on \((M_\Lambda,g_\Lambda)\), and \(\nabla\) the Riemannian gradient.
Define the reversible diffusion generator
\[
L_\Lambda f := \Delta_\Lambda f - \langle \nabla S_\Lambda, \nabla f\rangle_{g_\Lambda}.
\]
The associated carré du champ is
\[
\Gamma_\Lambda(f,g):=\frac12\big(L_\Lambda(fg)-fL_\Lambda g-gL_\Lambda f\big),
\qquad
\Gamma_\Lambda(f):=\Gamma_\Lambda(f,f).
\]
For the gradient diffusion above,
\[
\Gamma_\Lambda(f,g)=\langle \nabla f,\nabla g\rangle_{g_\Lambda},
\qquad
\Gamma_\Lambda(f)=|\nabla f|^2.
\]

The Bakry–Émery (BE) tensor of \(\mu_\Lambda\) is
\[
\mathrm{Ric}_{\mu_\Lambda}:=\mathrm{Ric}_{g_\Lambda}+\nabla^2 S_\Lambda,
\]
where \(\mathrm{Ric}_{g_\Lambda}\) is the Ricci tensor of \(g_\Lambda\) and \(\nabla^2 S_\Lambda\) is the Riemannian Hessian.

A key identity (Bochner–Bakry–Émery) states that for smooth \(f\),
\[
\Gamma_{2,\Lambda}(f)
:=\frac12\big(L_\Lambda\Gamma_\Lambda(f)-2\Gamma_\Lambda(f,L_\Lambda f)\big)
=
\|\nabla^2 f\|_{\mathrm{HS}}^2 + \mathrm{Ric}_{\mu_\Lambda}(\nabla f,\nabla f).
\]
In particular, if \(\mathrm{Ric}_{\mu_\Lambda}\ge \rho\, g_\Lambda\) as quadratic forms, then
\[
\Gamma_{2,\Lambda}(f)\ge \rho\,\Gamma_\Lambda(f),
\]
i.e. the curvature-dimension condition \(CD(\rho,\infty)\).

---

## 3. The product-group Ricci term (“Haar mass”)

Assume \(G\) has a uniform Ricci lower bound:
\[
\mathrm{Ric}_G \ge \kappa_G\, g_G
\qquad\text{for some }\kappa_G>0.
\tag{3.1}
\]
(This holds for many compact Lie groups equipped with appropriate bi-invariant metrics; here it is taken as a fixed geometric input.)

### Lemma 3.1 (Product Ricci bound)

On \(M_\Lambda=G^{E(\Lambda)}\) with the product metric \(g_\Lambda\),
\[
\mathrm{Ric}_{g_\Lambda} \ge \kappa_G\, g_\Lambda.
\tag{3.2}
\]

**Proof.**
For a Riemannian product \(M=\prod_{i=1}^n M_i\) with product metric, the Levi–Civita connection splits and the Ricci tensor is the direct sum of the Ricci tensors on each factor. Concretely, for a tangent vector \(v=(v_1,\dots,v_n)\),
\[
\mathrm{Ric}_M(v,v)=\sum_{i=1}^n \mathrm{Ric}_{M_i}(v_i,v_i).
\]
Applying (3.1) to each copy of \(G\) yields
\[
\mathrm{Ric}_{g_\Lambda}(v,v)\ge \kappa_G \sum_i |v_i|^2 = \kappa_G |v|^2_{g_\Lambda}.
\]
∎

---

## 4. Wilson plaquette action and its Hessian at the vacuum

Specialize to \(G=\mathrm{SU}(N)\). Define oriented plaquette holonomy for a plaquette \(p=(x;\mu,\nu)\) (\(\mu<\nu\)) by
\[
U_p(U) := U_{x,\mu}\,U_{x+\hat\mu,\nu}\,U_{x+\hat\nu,\mu}^{-1}\,U_{x,\nu}^{-1}\in \mathrm{SU}(N).
\]
Define the Wilson single-plaquette potential
\[
\Phi(U) := \frac{\beta}{N}\,\mathrm{Re}\,\mathrm{Tr}(I-U),
\qquad U\in \mathrm{SU}(N),
\]
and the Wilson action
\[
S_W(U):=\sum_{p\in P(\Lambda)}\Phi(U_p(U)).
\]

We identify the tangent space at the vacuum as
\[
T_{U^{(0)}}M_\Lambda \cong \mathcal C^1(\Lambda;\mathfrak{su}(N)):=\mathfrak{su}(N)^{E(\Lambda)}.
\]
Given \(X=(X_\ell)_{\ell\in E(\Lambda)}\), define the geodesic through the vacuum by
\[
U_\ell(t)=\exp(tX_\ell),\qquad U(t):=(U_\ell(t))_{\ell\in E(\Lambda)}.
\tag{4.1}
\]

Define the discrete coboundary \(d_1:\mathcal C^1\to\mathcal C^2\) (“curl”) by the oriented sum around a plaquette:
\[
(d_1 X)_p := X_{x,\mu}+X_{x+\hat\mu,\nu}-X_{x+\hat\nu,\mu}-X_{x,\nu}\in\mathfrak{su}(N).
\tag{4.2}
\]
Let \(d_1^*\) be its adjoint in the \(\ell^2\) inner product on cochains.

### Lemma 4.1 (Second-order Taylor of \(\mathrm{ReTr}(I-e^Y)\))

For \(Y\in\mathfrak{su}(N)\) small,
\[
\mathrm{Re}\,\mathrm{Tr}(I-e^Y)= -\frac12\,\mathrm{Tr}(Y^2)+O(|Y|^3).
\tag{4.3}
\]

**Proof.**
Use \(e^Y=I+Y+\frac12Y^2+O(|Y|^3)\). Since \(Y\in\mathfrak{su}(N)\) has \(\mathrm{Tr}(Y)=0\), the linear term vanishes in the trace. Also \(\mathrm{Tr}(Y^2)\in\mathbb R\) for anti-Hermitian \(Y\). Hence
\[
\mathrm{Re}\,\mathrm{Tr}(e^Y)=N+\frac12\mathrm{Tr}(Y^2)+O(|Y|^3),
\]
and subtracting from \(\mathrm{Re}\,\mathrm{Tr}(I)=N\) yields (4.3). ∎

### Lemma 4.2 (Plaquette holonomy linearization)

For \(U(t)\) as in (4.1), each plaquette holonomy satisfies
\[
U_p(t)=\exp\!\big(t(d_1X)_p + t^2 R_p(t)\big),
\tag{4.4}
\]
where \(R_p(t)\in\mathfrak{su}(N)\) is smooth in \(t\) and \(|R_p(t)|\le C|X|_\infty^2\) for \(|t|\le t_0\), with \(C,t_0\) depending only on \(G\) (not on \(\Lambda\)).

**Proof.**
Write \(U_p(t)\) as a product of four exponentials \(\exp(\pm tX_{\ell_i})\). Apply the Baker–Campbell–Hausdorff (BCH) formula iteratively. The linear term is the signed sum of the four \(X_{\ell_i}\), which is \((d_1X)_p\). Commutator contributions enter at order \(t^2\) and are bounded by \(C|X|_\infty^2\). ∎

### Proposition 4.3 (Wilson Hessian at the vacuum is \(d_1^*d_1\))

Along the geodesic \(U(t)=\exp(tX)\),
\[
S_W(U(t))
=
S_W(U^{(0)}) + \frac{t^2}{2}\,\frac{\beta}{N}\,\|d_1X\|_{\mathcal C^2}^2 + O(t^3|X|_\infty^3).
\tag{4.5}
\]
Equivalently, as a quadratic form on \(\mathcal C^1(\Lambda;\mathfrak{su}(N))\),
\[
\nabla^2 S_W(U^{(0)})(X,X)=\frac{\beta}{N}\,\langle X, d_1^*d_1 X\rangle_{\mathcal C^1}.
\tag{4.6}
\]

**Proof.**
Insert Lemma 4.2 into \(\Phi(U_p(t))=\frac{\beta}{N}\mathrm{ReTr}(I-\exp(Y_p(t)))\) with \(Y_p(t)=t(d_1X)_p+t^2R_p(t)\). Apply Lemma 4.1: the leading term is \(\frac{\beta}{N}\cdot \frac12|(d_1X)_p|^2 t^2\). Summing over plaquettes yields (4.5). The Hessian equals the second derivative at \(t=0\) along the geodesic, giving (4.6). ∎

---

## 5. Local curvature bound via a uniform Hessian modulus

Let the full action be
\[
S_\Lambda = S_W + S_{\mathrm{add},\Lambda},
\]
where \(S_{\mathrm{add},\Lambda}\) is any additional smooth gauge-invariant local term.

Assume a uniform lower Hessian bound for the additional term:
\[
\nabla^2 S_{\mathrm{add},\Lambda}(U) \ge -C_{\mathrm{add}}\, g_\Lambda(U)
\qquad\text{for all }U\in M_\Lambda,
\tag{5.1}
\]
with \(C_{\mathrm{add}}\) independent of \(\Lambda\).
Assume also
\[
C_{\mathrm{add}}<\kappa_G,
\tag{5.2}
\]
and define
\[
\rho_0 := \kappa_G - C_{\mathrm{add}} > 0.
\tag{5.3}
\]

### Proposition 5.1 (Curvature at the vacuum)

At \(U^{(0)}\),
\[
\mathrm{Ric}_{\mu_\Lambda}(U^{(0)})(v,v)\ge \rho_0\,|v|_{g_\Lambda}^2
\qquad\forall v\in T_{U^{(0)}}M_\Lambda.
\tag{5.4}
\]

**Proof.**
At \(U^{(0)}\),
\[
\mathrm{Ric}_{\mu_\Lambda}
=
\mathrm{Ric}_{g_\Lambda}+\nabla^2 S_W+\nabla^2 S_{\mathrm{add},\Lambda}.
\]
Apply Lemma 3.1, \(\nabla^2 S_W(U^{(0)})\ge 0\) from (4.6), and (5.1). ∎

The next step is to extend (5.4) to a *ball* around \(U^{(0)}\) with radius independent of \(\Lambda\). This requires a uniform Lipschitz bound on \(\nabla^2 S_W\) near \(U^{(0)}\).

Let \(\nu\) be the maximal number of plaquettes incident to a given edge (a purely local combinatorial constant; on the \(d=4\) hypercubic lattice, \(\nu=6\)).

### Lemma 5.2 (Uniform third derivative bound for \(S_W\))

There exists a constant \(C_W^{(3)}<\infty\), depending only on \(G\) and \(\Phi\) (not on \(\Lambda\)), such that for all \(U\in M_\Lambda\) and all tangent vectors \(\eta,v,w\in T_U M_\Lambda\),
\[
|\nabla^3 S_W(U)(\eta,v,w)|\le C_W^{(3)}\,\nu^{3/2}\,|\eta|\,|v|\,|w|.
\tag{5.5}
\]

**Proof.**
Write \(S_W=\sum_{p} S_{W,p}\) with \(S_{W,p}(U)=\Phi(U_p(U))\). Each \(S_{W,p}\) depends only on the four links in \(\partial p\). Since \(\Phi\) and the holonomy map are smooth on compact sets, \(\nabla^3 S_{W,p}\) is uniformly bounded by a constant \(K_3\) depending only on \(G,\Phi\). Summing over \(p\) and using the incidence bound \(\#\{p:\ell\in\partial p\}\le \nu\) plus a triple Cauchy–Schwarz yields the factor \(\nu^{3/2}\). ∎

### Corollary 5.3 (Uniform Lipschitz continuity of \(\nabla^2 S_W\))

Let
\[
L_W := C_W^{(3)}\,\nu^{3/2}.
\tag{5.6}
\]
Then for any \(U\in M_\Lambda\),
\[
\|\nabla^2 S_W(U)-\nabla^2 S_W(U^{(0)})\|_{\mathrm{op}}
\le L_W\, d_{g_\Lambda}(U,U^{(0)}).
\tag{5.7}
\]

**Proof.**
Integrate \(\nabla^3 S_W\) along a minimizing geodesic \(\gamma\) from \(U^{(0)}\) to \(U\), apply Lemma 5.2, and use \(|\dot\gamma|=d_{g_\Lambda}(U,U^{(0)})\). ∎

### Theorem 5.4 (Uniform local BE curvature bound on a small-field ball)

Define
\[
r := \min\left\{1,\frac{\rho_0}{2L_W}\right\},
\qquad
\rho_{\mathrm{loc}} := \frac{\rho_0}{2}=\frac{\kappa_G-C_{\mathrm{add}}}{2}.
\tag{5.8}
\]
Then for every lattice \(\Lambda\), every \(U\in M_\Lambda\) with \(d_{g_\Lambda}(U,U^{(0)})\le r\), and every \(v\in T_U M_\Lambda\),
\[
\mathrm{Ric}_{\mu_\Lambda}(U)(v,v)\ge \rho_{\mathrm{loc}}\,|v|_{g_\Lambda}^2.
\tag{5.9}
\]
Consequently, on the same ball and for every smooth \(f\),
\[
\Gamma_{2,\Lambda}(f)(U)\ge \rho_{\mathrm{loc}}\,\Gamma_\Lambda(f)(U).
\tag{5.10}
\]

**Proof.**
Fix \(U\in B_r(U^{(0)})\). Decompose
\[
\mathrm{Ric}_{\mu_\Lambda}(U)
=
\mathrm{Ric}_{g_\Lambda}(U)+\nabla^2S_{\mathrm{add},\Lambda}(U)+\nabla^2S_W(U).
\]
The first two terms satisfy \(\mathrm{Ric}_{g_\Lambda}\ge \kappa_G g_\Lambda\) and \(\nabla^2S_{\mathrm{add},\Lambda}\ge -C_{\mathrm{add}}g_\Lambda\). For the Wilson term,
\[
\nabla^2 S_W(U)\ge \nabla^2 S_W(U^{(0)}) - \|\nabla^2 S_W(U)-\nabla^2S_W(U^{(0)})\|_{\mathrm{op}}\,g_\Lambda
\ge -L_W r\,g_\Lambda,
\]
because \(\nabla^2S_W(U^{(0)})\ge 0\). With the choice of \(r\), \(L_W r\le \rho_0/2\). Summing gives
\[
\mathrm{Ric}_{\mu_\Lambda}(U)\ge (\kappa_G-C_{\mathrm{add}}-\rho_0/2)\,g_\Lambda = \rho_0/2\,g_\Lambda=\rho_{\mathrm{loc}}\,g_\Lambda.
\]
This proves (5.9). The inequality (5.10) follows from the Bochner–Bakry–Émery identity and \(\|\nabla^2 f\|_{\mathrm{HS}}^2\ge 0\). ∎

---

## 6. Interpretation and interface

* The curvature lower bound is **local** (only on \(B_r(U^{(0)})\)).  
* The constants \(r,\rho_{\mathrm{loc}}\) are **uniform in \(\Lambda\)** because \(L_W\) depends only on local incidence \(\nu\) and bounded derivatives of \(\Phi\) and \(G\)-geometry.

This is the precise small-field geometric input used by local-to-global functional inequality “assembly” theorems.
