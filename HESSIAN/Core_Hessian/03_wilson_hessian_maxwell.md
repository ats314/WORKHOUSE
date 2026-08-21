# Wilson Hessian \(=\) discrete Maxwell operator and the physical Hodge split

## Scope

This note isolates the **second-variation spine** of the lattice Yang–Mills action around the trivial connection. The deliverable is a precise operator identity:
\[
\nabla^2 S_W(U^{(0)}) \;=\; 2c_W\,d_1^*d_1,
\]
together with the discrete Hodge decomposition that explains its kernel and where “physical positivity” lives.

---

## 1. Configuration manifold and tangent identification at the vacuum

Let \(G\) be compact with Lie algebra \(\mathfrak g\), fixed \(\mathrm{Ad}\)-invariant inner product \(\langle\cdot,\cdot\rangle_{\mathfrak g}\), and induced bi-invariant metric.

On a finite lattice \(\Lambda\), the configuration manifold is
\[
M_\Lambda := G^{E(\Lambda)}.
\]
At the trivial configuration \(U^{(0)}=(e)_{\ell\in E(\Lambda)}\),
\[
T_{U^{(0)}}M_\Lambda \;\cong\; \mathfrak g^{E(\Lambda)} \;=\; \mathcal C^1(\Lambda;\mathfrak g),
\]
with the \(\ell^2\)-product inner product.

---

## 2. Discrete cochain complex and Hodge Laplacian

Define cochains
\[
\mathcal C^0(\Lambda;\mathfrak g)=\mathfrak g^{V(\Lambda)},\quad
\mathcal C^1(\Lambda;\mathfrak g)=\mathfrak g^{E(\Lambda)},\quad
\mathcal C^2(\Lambda;\mathfrak g)=\mathfrak g^{P(\Lambda)}.
\]

Define the coboundary operators \(d_0:\mathcal C^0\to\mathcal C^1\) (discrete gradient) and \(d_1:\mathcal C^1\to\mathcal C^2\) (discrete curl) by the standard oriented-incidence formulas. One checks directly that
\[
d_1 d_0 = 0.
\tag{2.1}
\]

Let \(d_0^*,d_1^*\) denote adjoints w.r.t. the product inner products. Define the 1-form Hodge Laplacian
\[
\Delta_1 := d_0 d_0^* + d_1^* d_1.
\]

### Discrete Hodge decomposition (finite-dimensional linear algebra)

Because the complex is finite-dimensional, standard orthogonal decomposition yields
\[
\mathcal C^1
=
\mathrm{im}(d_0)\ \oplus\ \mathcal H^1\ \oplus\ \mathrm{im}(d_1^*),
\tag{2.2}
\]
where \(\mathcal H^1:=\ker(\Delta_1)=\ker(d_1)\cap\ker(d_0^*)\).

Interpretation:

* \(\mathrm{im}(d_0)\): exact 1-forms (infinitesimal gauge directions at the vacuum).
* \(\mathrm{im}(d_1^*)\): coexact 1-forms (transverse/physical sector).
* \(\mathcal H^1\): harmonic 1-forms (global/topological sector; depends on boundary conditions).

---

## 3. Linearization of plaquette holonomy

For a plaquette \(p\), the holonomy is
\[
U_p(U) := U_{\ell_1}U_{\ell_2}U_{\ell_3}^{-1}U_{\ell_4}^{-1}.
\]
In exponential coordinates \(U_\ell=\exp(X_\ell)\) near the vacuum,
\[
\log U_p(\exp X) = (d_1 X)_p + O(|X|^2).
\tag{3.1}
\]
This identifies the linearized curvature with the lattice curl \(d_1X\).

---

## 4. Quadratic expansion of the Wilson action

For \(G=\mathrm{SU}(N)\), the Wilson plaquette action has the form
\[
S_W(U)
=
\frac{\beta}{N}\sum_{p\in P(\Lambda)}\Re\operatorname{Tr}\big(I-U_p(U)\big).
\]
Using (3.1) and the Taylor expansion of \(\Re\operatorname{Tr}(I-\exp Y)\) at \(Y=0\),
\[
\Re\operatorname{Tr}(I-\exp Y)=\frac{c_{\mathrm{HS}}}{2}|Y|_{\mathfrak g}^2+O(|Y|^3),
\]
one obtains the quadratic expansion
\[
S_W(\exp X)
=
S_W(U^{(0)})
+
c_W\,|d_1 X|_{\mathcal C^2}^2
+
O(|X|_{\mathcal C^1}^3),
\qquad
c_W := \frac{\beta}{N}\cdot\frac{c_{\mathrm{HS}}}{2}.
\tag{4.1}
\]

### Proposition 4.1 (Wilson Hessian = discrete Maxwell operator)

By comparing (4.1) with the defining expansion
\[
S_W(\exp(tX))
=
S_W(U^{(0)})
+\frac{t^2}{2}\langle X,\nabla^2 S_W(U^{(0)})X\rangle_{\mathcal C^1}
+O(t^3),
\]
one identifies
\[
\nabla^2 S_W(U^{(0)}) = 2c_W\,d_1^*d_1
\quad\text{on }\mathcal C^1(\Lambda;\mathfrak g).
\tag{4.2}
\]

Immediate consequences:

* Nonnegativity:
  \(\langle X,\nabla^2 S_W(U^{(0)})X\rangle = 2c_W\,|d_1X|^2\ge 0\).
* Kernel:
  \(\ker(\nabla^2 S_W(U^{(0)}))=\ker(d_1)\) (closed 1-forms).

---

## 5. Where “physical positivity” lives

Restrict to the vacuum horizontal space \(H_{U^{(0)}}:=\ker(d_0^*)\). Then
\[
H_{U^{(0)}} = \mathcal H^1\oplus \mathrm{im}(d_1^*).
\tag{5.1}
\]
On \(\mathrm{im}(d_1^*)\) (coexact/transverse),
\[
d_1^*d_1 \text{ has a spectral gap (finite volume, once harmonic sector removed).}
\]
On \(\mathcal H^1\), \(d_1^*d_1\) vanishes.

Thus the Wilson quadratic form is strictly positive on the coexact sector (the “propagating modes”), and has zero-modes only in gauge and harmonic directions.

---

## 6. How the Haar/Ricci floor closes the remaining vacuum degeneracy

The project’s “Haar mass” mechanism supplies an additional volume-uniform quadratic form near the vacuum coming from Haar geometry:
\[
\nabla^2 S_{H,\Lambda}(0)\ \ge\ \frac{\kappa_G}{3}\,\mathrm{Id}.
\]
Adding this to (4.2) yields an effective Hessian on the horizontal sector of the schematic form
\[
\nabla^2 S_{\mathrm{eff}}(U^{(0)})\big|_{H_{U^{(0)}}}
\ \ge\
\frac{\kappa_G}{3}\,\mathrm{Id}_{H_{U^{(0)}}}
\;+\;
2c_W\,d_1^*d_1.
\tag{6.1}
\]
This is the operator that later appears as \(M\) in the Green’s-function/covariance step; it is invertible on \(H_{U^{(0)}}\) with a spectral gap bounded below by \(\kappa_G/3\).

---

## 7. Why this is “new” inside the project’s logic

Many approaches to lattice YM use scalar inequalities or absolute-value bounds that destroy the incidence-matrix structure and inflate constants with volume. The identity (4.2) is a matrix-level statement: it keeps the structured PSD operator \(d_1^*d_1\) intact, which is exactly what the later Helffer–Sjöstrand step needs in order to extract **exponential** Green’s-function decay.

