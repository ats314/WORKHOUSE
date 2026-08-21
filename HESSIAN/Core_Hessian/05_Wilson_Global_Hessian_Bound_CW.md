# A clean global Wilson Hessian bound and an explicit \(C_W\)

This note is a **repair**: it replaces “hand-wavy BCH growth bounds” with a direct, global operator-norm bound for the Wilson Hessian in exponential coordinates.

The key observation is almost embarrassingly simple:

> For \(A\in\mathfrak{su}(3)\), \(e^A\) is unitary, and the Fréchet derivatives of the exponential are uniformly bounded in unitarily-invariant norms.

So the Hessian of each plaquette term is uniformly bounded, and the full Wilson Hessian is bounded by a constant depending only on **local lattice connectivity**.

This gives a *global polynomial bound* (in fact, a constant) of the form
\[
\|\nabla^2 S_W(A)\| \le C_W\,\beta
\quad\text{for all configurations }A.
\]

---

## 1. Setup

- Gauge group: \(G=SU(3)\).
- Exponential coordinates on each link:
  \[
  U_\ell = e^{A_\ell},\qquad A_\ell\in\mathfrak{su}(3).
  \]
- Wilson plaquette action:
  \[
  S_W(U)=\beta\sum_{p}\left(1-\frac{1}{3}\mathrm{Re}\,\mathrm{Tr}(U_p)\right),
  \qquad U_p=U_{\ell_1}U_{\ell_2}U_{\ell_3}U_{\ell_4}.
  \]

Define the single-plaquette function on \(G^4\):
\[
f_p(X_1,X_2,X_3,X_4)=
-\frac{\beta}{3}\,\mathrm{Re}\,\mathrm{Tr}(X_1X_2X_3X_4).
\]

---

## 2. Uniform derivative bounds on \(f_p\)

Because \(G^4\) is compact and multiplication/trace are smooth, the first and second derivatives of \(f_p\) are uniformly bounded.

A crude explicit bound (sufficient for a clean \(C_W\)) is:

- For each \(i\),
  \[
  |D_{X_i} f_p[X](H_i)| \le \frac{\beta}{3}\,\|H_i\|.
  \]
- For each \(i,j\),
  \[
  |D^2_{X_i,X_j} f_p[X](H_i,H_j)| \le \frac{\beta}{3}\,\|H_i\|\,\|H_j\|.
  \]

These follow from \(|\mathrm{ReTr}(AB)|\le \|A\|_{\mathrm{HS}}\|B\|_{\mathrm{HS}}\) and unitarity of the other factors.

---

## 3. Uniform derivative bounds on \(A\mapsto e^A\) for \(A^\dagger=-A\)

### 3.1 First derivative bound

The Duhamel formula:
\[
D e^A[H]=\int_0^1 e^{(1-s)A}H e^{sA}\,ds.
\]
For \(A\in\mathfrak{su}(3)\), all \(e^{tA}\) are unitary. Since the Hilbert–Schmidt norm is unitarily invariant,
\[
\|e^{(1-s)A}H e^{sA}\|_{\mathrm{HS}}=\|H\|_{\mathrm{HS}}.
\]
Thus
\[
\boxed{\ \|D e^A\|_{\mathrm{op}}\le 1\quad \text{(HS\(\to\)HS)}\ }.
\]

### 3.2 Second derivative bound

One convenient integral representation is:
\[
D^2 e^A[H,K]
=
\int_0^1\!\!\int_0^s e^{(1-s)A}H e^{(s-u)A}K e^{uA}\,du\,ds
+
\int_0^1\!\!\int_0^s e^{(1-s)A}K e^{(s-u)A}H e^{uA}\,du\,ds.
\]

Again, each unitary conjugation is an isometry in HS norm, and the integrals have total mass \(1/2\) each. Therefore
\[
\|D^2 e^A[H,K]\|_{\mathrm{HS}}
\le
\left(\int_0^1\!\!\int_0^s du\,ds\right)\|H\|\,\|K\|
+
\left(\int_0^1\!\!\int_0^s du\,ds\right)\|K\|\,\|H\|
=
\|H\|\,\|K\|.
\]

Hence we may take the **global constant**
\[
\boxed{\ \|D^2 e^A\|_{\mathrm{op}}\le 1\quad \text{(bilinear HS\(\times\)HS\(\to\)HS)}\ }.
\]

(If you want a safety margin, replace \(1\) by \(2\); it won’t change the logic.)

---

## 4. Single-plaquette Hessian bound

Consider a plaquette \(p\) with 4 links and variations \(H=(H_1,\dots,H_4)\), \(K=(K_1,\dots,K_4)\).

The second variation of \(S_p(A)=f_p(e^{A_{\ell_1}},\dots,e^{A_{\ell_4}})\) decomposes into:

- Type I terms: \(D^2 f_p\) acting on \(D e^{A_{\ell_i}}[H_i]\) and \(D e^{A_{\ell_j}}[K_j]\),
- Type II terms: \(D f_p\) acting on \(D^2 e^{A_{\ell_i}}[H_i,K_i]\).

Using the bounds above, one obtains
\[
|\langle H,\nabla^2 S_p(A)K\rangle|
\le
\beta\Big(
\frac{1}{3}\sum_{i\neq j}\|H_i\|\,\|K_j\|
+\frac{1}{3}\sum_i\|H_i\|\,\|K_i\|
\Big).
\]

A simple Cauchy–Schwarz estimate in \(\mathbb{R}^4\) yields
\[
\sum_{i,j}\|H_i\|\,\|K_j\|
\le
\left(\sum_i\|H_i\|\right)\left(\sum_j\|K_j\|\right)
\le 4\,\|H\|\,\|K\|,
\qquad
\sum_i\|H_i\|\,\|K_i\|\le \|H\|\,\|K\|.
\]

Therefore the operator norm on the 4-link block satisfies
\[
\boxed{
\|\nabla^2 S_p(A)\|_{\mathrm{op}}
\le
\beta\,C_p,
\qquad
C_p:=\frac{4}{3}+\frac{1}{3}=\frac{5}{3}.
}
\]

(If you used a larger constant for \(\|D^2 e^A\|\), \(C_p\) changes in the obvious way.)

---

## 5. Global bound on the full lattice and the constant \(C_W\)

Now sum over plaquettes:
\[
\nabla^2 S_W(A)=\sum_p \nabla^2 S_p(A).
\]

Let \(n_p\) be the maximum number of plaquettes containing any given link. In a 4D hypercubic lattice, \(n_p=6\).

A standard block-matrix estimate gives
\[
\|\nabla^2 S_W(A)\|_{\mathrm{op}}
\le
\sup_{\ell}\ \sum_{\ell'} \|(\nabla^2 S_W(A))_{\ell\ell'}\|.
\]

Each plaquette contributes to at most \(4\) blocks in the row corresponding to a given link \(\ell\), and there are at most \(n_p\) plaquettes containing \(\ell\). Each such block contribution is bounded by \(\beta C_p\).

Hence
\[
\sum_{\ell'} \|(\nabla^2 S_W(A))_{\ell\ell'}\|
\le
4\,n_p\,\beta C_p.
\]

Therefore we can take
\[
\boxed{
\|\nabla^2 S_W(A)\|_{\mathrm{op}}
\le
C_W\,\beta,
\qquad
C_W:=4n_p C_p.
}
\]

With \(n_p=6\) and \(C_p=5/3\), this gives the explicit constant
\[
\boxed{
C_W = 4\cdot 6\cdot \frac{5}{3} = 40.
}
\]

This bound is:

- global in configuration \(A\),
- independent of lattice volume,
- depends only on local geometry and group norms.

---

## 6. What this *does* and *does not* buy you

- It **does** give a clean, honest, volume-stable inequality you can cite without squirming.
- It **does not** (by itself) produce convexity at moderate/weak coupling, because combining with Haar curvature yields only:
  \[
  \nabla^2(S_{\mathrm{Haar}}+S_W)\succeq (c_0 - C_W\beta)\,I,
  \]
  which requires \(\beta<c_0/C_W\).

So this is a solid “strong coupling” convexity result, and a useful global control input for any dynamic-restoration mechanism.

The program then becomes: find an additional mechanism (flow, RG smoothing, concentration) that effectively reduces the Wilson Hessian *in the region where the measure lives*.