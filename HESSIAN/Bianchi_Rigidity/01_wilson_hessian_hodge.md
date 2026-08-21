# Wilson Hessian at the vacuum = discrete Maxwell operator (and why this is the right “matrix object”)

This note extracts the cleanest “hard algebra” fact in the project: **the quadratic form of the Wilson action at the trivial connection is exactly the discrete Maxwell operator** \(d_1^\ast d_1\) on 1‑cochains.  

That identity is what makes the later “matrix hinge” approach plausible: you keep the *signed incidence structure* of \(d_1\) instead of destroying it with absolute‑value bounds.

---

## 1. Lattice cochains and coboundaries

Let \(\Lambda\subset\mathbb Z^d\) be a finite lattice complex with

- vertices \(V(\Lambda)\),
- oriented edges (links) \(E(\Lambda)\),
- oriented plaquettes \(P(\Lambda)\).

Let \(G\) be a compact Lie group with Lie algebra \(\mathfrak g\). Fix an \(\mathrm{Ad}\)-invariant inner product \(\langle\cdot,\cdot\rangle_{\mathfrak g}\) on \(\mathfrak g\) and use it linkwise/plaquettewise to define \(\ell^2\) inner products on cochains.

Define the cochain spaces
\[
\mathcal C^0 := \{ \phi:V(\Lambda)\to\mathfrak g\},\qquad
\mathcal C^1 := \{ X:E(\Lambda)\to\mathfrak g\},\qquad
\mathcal C^2 := \{ \omega:P(\Lambda)\to\mathfrak g\}.
\]

### 1.1 Coboundary \(d_0:\mathcal C^0\to\mathcal C^1\)

For an oriented edge \(e=(x\to y)\),
\[
(d_0\phi)_e := \phi_y-\phi_x.
\]

### 1.2 Coboundary \(d_1:\mathcal C^1\to\mathcal C^2\) (discrete curl)

For an oriented plaquette \(p\) with oriented boundary edges \(\partial p=(e_1,e_2,e_3,e_4)\) and signs \(\sigma_i\in\{\pm1\}\) matching the orientation convention,
\[
(d_1 X)_p := \sum_{i=1}^4 \sigma_i\, X_{e_i}.
\]

Let \(d_0^\ast,d_1^\ast\) denote the adjoints with respect to the \(\ell^2\) inner products. Then \(d_1^\ast d_1\succeq 0\) is a self-adjoint operator on \(\mathcal C^1\).

---

## 2. Configuration manifold and the vacuum tangent identification

Define the configuration manifold
\[
M_\Lambda := G^{E(\Lambda)}.
\]

Let \(U^{(0)}\in M_\Lambda\) be the trivial configuration \(U^{(0)}_e=e\) for all edges \(e\).  

Equip each \(G\)-factor with its bi-invariant Riemannian metric induced by \(\langle\cdot,\cdot\rangle_{\mathfrak g}\), and \(M_\Lambda\) with the product metric.

Right-invariant trivialization gives an identification
\[
T_{U^{(0)}}M_\Lambda \cong \mathcal C^1(\Lambda;\mathfrak g),
\]
by mapping \(X=(X_e)_{e\in E(\Lambda)}\) to the geodesic
\[
U_e(t) = \exp(tX_e).
\]

---

## 3. Linearization of plaquette holonomy = \(d_1\)

For a plaquette \(p\in P(\Lambda)\) with ordered boundary edges \(e_1,e_2,e_3,e_4\), define the plaquette holonomy
\[
U_p := U_{e_1}\,U_{e_2}\,U_{e_3}^{-1}\,U_{e_4}^{-1}.
\]

### Lemma 3.1 (Plaquette holonomy linearization)
Let \(U(t)=\exp(tX)\) with \(X\in\mathcal C^1(\Lambda;\mathfrak g)\). Then for each plaquette \(p\),
\[
U_p(t)=\exp\!\Big(t(d_1X)_p + t^2 R_p(t)\Big),
\]
where \(R_p(t)\in\mathfrak g\) is smooth and satisfies \(\|R_p(t)\|\le C\|X\|_\infty^2\) for \(|t|\le t_0\) (constants depend on \(G\) but not on \(\Lambda\)).

**Proof.**
Write \(U_p(t)=\exp(tX_{e_1})\exp(tX_{e_2})\exp(-tX_{e_3})\exp(-tX_{e_4})\).
Iteratively apply the Baker–Campbell–Hausdorff expansion
\[
\exp(A)\exp(B)=\exp\big(A+B+\mathcal O(\|A\|\|B\|)\big),
\]
with \(A,B=\mathcal O(t\|X\|_\infty)\). The first-order term is the signed sum of the four edge components, i.e. \((d_1X)_p\).  \(\square\)

---

## 4. Wilson plaquette action and its second variation at \(U^{(0)}\)

Specialize to \(G=\mathrm{SU}(N)\) with the inner product \(\langle A,B\rangle=-\mathrm{Tr}(AB)\) on \(\mathfrak{su}(N)\) (anti-Hermitian traceless matrices).

Define the single-plaquette potential
\[
\Phi(U):=\frac{\beta}{N}\,\mathrm{Re}\,\mathrm{Tr}(I-U),
\qquad U\in \mathrm{SU}(N),
\]
and the Wilson action
\[
S_W(U):=\sum_{p\in P(\Lambda)} \Phi(U_p).
\]

### Lemma 4.1 (Single-plaquette Taylor coefficient)
Let \(A\in\mathfrak{su}(N)\). Then
\[
\Phi(\exp(tA))
= \frac{\beta}{2N}\, t^2\, \|A\|^2 + \mathcal O(t^3\|A\|^3),
\qquad
\|A\|^2:=-\mathrm{Tr}(A^2).
\]

**Proof.**
Use \(\exp(tA)=I+tA+\tfrac12 t^2 A^2+\mathcal O(t^3)\) and \(\mathrm{Tr}(A)=0\). Then
\[
\mathrm{Re}\,\mathrm{Tr}(I-\exp(tA))
= -\tfrac12 t^2\,\mathrm{Re}\,\mathrm{Tr}(A^2) + \mathcal O(t^3\|A\|^3)
= \tfrac12 t^2 \|A\|^2 + \mathcal O(t^3\|A\|^3).
\]
Multiply by \(\beta/N\). \(\square\)

### Proposition 4.2 (Vacuum Hessian of the Wilson action)
At the trivial configuration \(U^{(0)}\),
\[
\nabla^2 S_W(U^{(0)}) \;=\; \frac{\beta}{N}\, d_1^\ast d_1
\quad\text{as an operator on }\mathcal C^1(\Lambda;\mathfrak{su}(N)).
\]

Equivalently, for \(X\in\mathcal C^1\),
\[
\frac{d^2}{dt^2}\Big|_{t=0} S_W(\exp(tX))
= \frac{\beta}{N}\,\|d_1X\|_{\mathcal C^2}^2.
\]

**Proof.**
By Lemma 3.1, \(U_p(t)=\exp(t(d_1X)_p + \mathcal O(t^2))\).  
Apply Lemma 4.1 plaquettewise and sum:
\[
S_W(\exp(tX))
= \sum_p \Big(\frac{\beta}{2N}t^2\|(d_1X)_p\|^2 + \mathcal O(t^3\|X\|_\infty^3)\Big)
= \frac{\beta}{2N}t^2\|d_1X\|^2 + \mathcal O(t^3).
\]
Thus the quadratic form is \(\frac{\beta}{2N}\|d_1X\|^2=\frac12\langle X,(\frac{\beta}{N}d_1^\ast d_1)X\rangle\), hence the Hessian is \((\beta/N)d_1^\ast d_1\). \(\square\)

---

## 5. Discrete Hodge decomposition and “physical” positivity

The operator \(d_1^\ast d_1\) is positive semidefinite but has a large kernel. The kernel has a clean geometric meaning.

### Lemma 5.1 (Gauge directions lie in \(\ker(d_1)\))
For all \(\phi\in\mathcal C^0\),
\[
d_1(d_0\phi)=0.
\]

**Proof.**
This is the cochain identity \(d_1\circ d_0=0\), i.e. “curl grad \(=0\)”.  \(\square\)

So \(\mathrm{Im}(d_0)\subset \ker(d_1)\subset\ker(d_1^\ast d_1)\). These are the infinitesimal gauge directions at the vacuum.

### Lemma 5.2 (Orthogonal Hodge splitting at the vacuum)
Assume \(\Lambda\) is a finite cell complex with the \(\ell^2\) inner products above. Then
\[
\mathcal C^1 \;=\; \mathrm{Im}(d_0)\ \oplus\ \ker(\Delta_1)\ \oplus\ \mathrm{Im}(d_1^\ast),
\qquad
\Delta_1:=d_0d_0^\ast + d_1^\ast d_1,
\]
an orthogonal decomposition. Moreover,
\[
\ker(d_1^\ast d_1)=\mathrm{Im}(d_0)\oplus \ker(\Delta_1).
\]

**Proof.**
Standard finite-dimensional Hodge theory: \(\Delta_1\) is self-adjoint, \(\mathrm{Im}(d_0)\perp \mathrm{Im}(d_1^\ast)\), and \(\ker(\Delta_1)=\ker(d_0^\ast)\cap\ker(d_1)\). Orthogonal complements give the decomposition. \(\square\)

### Corollary 5.3 (Positivity on the coexact sector)
On \(\mathrm{Im}(d_1^\ast)\) one has strict positivity:
\[
\langle X, d_1^\ast d_1 X\rangle >0
\quad\forall X\in \mathrm{Im}(d_1^\ast)\setminus\{0\}.
\]

**Proof.**
If \(X=d_1^\ast\omega\neq 0\), then \(\langle X,d_1^\ast d_1 X\rangle=\|d_1X\|^2=\|d_1d_1^\ast\omega\|^2>0\) unless \(d_1^\ast\omega\in\ker d_1\), which would force \(\omega\) harmonic on 2-cochains; in finite volume \(\mathrm{Im}(d_1^\ast)\cap\ker(d_1)=\{0\}\). \(\square\)

### Definition 5.4 (Horizontal subspace at the vacuum)
Define the vacuum horizontal (divergence-free) subspace
\[
H_{U^{(0)}} := \ker(d_0^\ast)\subset \mathcal C^1.
\]
Then
\[
H_{U^{(0)}} \;=\; \ker(\Delta_1)\ \oplus\ \mathrm{Im}(d_1^\ast).
\]

So: **the Wilson Hessian is strictly coercive on the coexact part of the horizontal space**.

---

## 6. Appendix: numerical sanity check (abelian \(U(1)\))

On a 2D periodic \(L\times L\) lattice for \(U(1)\) gauge theory, the Wilson action is
\[
S(\theta)=\beta\sum_{p}(1-\cos((d_1\theta)_p)),
\]
and the exact vacuum Hessian is \(H=\beta\, d_1^\top d_1\).

A short numerical check (see `A1_u1_numerical_sanity_check.md`) verifies:

- finite-difference Hessian at \(\theta=0\) matches \(\beta\,d_1^\top d_1\) to \(\sim 10^{-8}\) relative error;
- \(\dim\ker(d_1^\top d_1)=(|V|-1)+\dim H^1(\text{torus})\), i.e. gauge modes + harmonic modes.

---
