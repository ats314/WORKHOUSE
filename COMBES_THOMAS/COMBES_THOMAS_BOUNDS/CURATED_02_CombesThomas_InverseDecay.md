# Combes–Thomas inverse decay for massive finite-range operators on bounded-degree graphs

## Purpose

This note records a self-contained Combes–Thomas type estimate in the form needed for lattice Yang–Mills covariance bounds:

> A positive “mass” on the diagonal plus finite-range off-diagonal couplings imply that the inverse matrix (Green’s function) decays exponentially in graph distance.

The statement is formulated for **matrix-valued** kernels (operators acting on vector fields on edges).

---

## 1. Graph and operator model

Let \((\mathcal X,d)\) be a countable graph metric space (in applications: \(\mathcal X=E(\Lambda)\), the set of oriented links, with graph distance \(d_E\)).
Assume bounded degree, so that the size of balls grows at most exponentially.

Fix a finite-dimensional real inner product space \(V\cong\mathbb R^q\), and consider the Hilbert space
\[
\mathcal H := \ell^2(\mathcal X;V).
\]

Let \(A:\mathcal H\to\mathcal H\) be a bounded self-adjoint operator with kernel \(A_{xy}\in\operatorname{End}(V)\).
Assume **finite range**: there is \(R\in\mathbb N\) such that
\[
A_{xy}=0\qquad\text{whenever } d(x,y)>R.
\]

Define the uniform off-diagonal row-sum bound
\[
B\ :=\ \sup_{x\in\mathcal X}\ \sum_{y\neq x}\ \|A_{xy}\|_{\mathrm{op}}.
\]

Assume a strict diagonal positivity (“mass”)
\[
A\ \succeq\ a_0\,I
\quad\text{as an operator on }\mathcal H,
\qquad a_0>0.
\]

---

## 2. The estimate

### Theorem (Combes–Thomas decay)

Under the assumptions above, for all \(x,y\in\mathcal X\),
\[
\boxed{
\bigl\| (A^{-1})_{xy}\bigr\|_{\mathrm{op}}
\ \le\
\frac{2}{a_0}\ \exp\!\Bigl(-m\, d(x,y)\Bigr),
}
\]
where one may take
\[
m\ :=\ \frac1R\ \log\!\Bigl(1+\frac{a_0}{2B}\Bigr).
\]

---

## 3. Proof

Fix a basepoint \(x_0\in\mathcal X\).
For \(t\ge 0\), define the multiplication operator \(W_t:\mathcal H\to\mathcal H\) by
\[
(W_t f)(x) := e^{t\,d(x,x_0)} f(x).
\]
Conjugate \(A\) by \(W_t\):
\[
A_t := W_t\,A\,W_t^{-1}.
\]
The kernel satisfies
\[
(A_t)_{xy}
=
e^{t(d(x,x_0)-d(y,x_0))}\,A_{xy}.
\]
By the triangle inequality,
\[
|d(x,x_0)-d(y,x_0)|\le d(x,y),
\]
so for \(d(x,y)\le R\) we have
\[
\bigl\|(A_t)_{xy}\bigr\|_{\mathrm{op}}
\le e^{tR}\,\|A_{xy}\|_{\mathrm{op}}.
\]

### Step 1: estimate the conjugation error

Write
\[
A_t = A + K_t,
\qquad
(K_t)_{xy}
=
\Bigl(e^{t(d(x,x_0)-d(y,x_0))}-1\Bigr)A_{xy}.
\]
For \(x\neq y\) with \(d(x,y)\le R\),
\[
\|(K_t)_{xy}\|_{\mathrm{op}}
\le (e^{tR}-1)\,\|A_{xy}\|_{\mathrm{op}},
\]
and \((K_t)_{xx}=0\).
Therefore, by the Schur test,
\[
\|K_t\|_{\mathrm{op}}
\le
\sup_x\sum_{y\neq x}\|(K_t)_{xy}\|_{\mathrm{op}}
\le
(e^{tR}-1)\,B.
\tag{3.1}
\]

### Step 2: choose \(t\) so that \(A_t\) stays invertible

Since \(A\succeq a_0 I\), we have \(\|A^{-1}\|_{\mathrm{op}}\le a_0^{-1}\).
If \( \|K_t\|_{\mathrm{op}} \le a_0/2\), then \(A_t=A(I+A^{-1}K_t)\) is invertible and
\[
\|A_t^{-1}\|_{\mathrm{op}}
\le
\frac{1}{a_0-\|K_t\|_{\mathrm{op}}}
\le
\frac{2}{a_0}.
\tag{3.2}
\]
By (3.1), it suffices that
\[
(e^{tR}-1)B\ \le\ \frac{a_0}{2}.
\]
One convenient choice is
\[
t := \frac1R\log\!\Bigl(1+\frac{a_0}{2B}\Bigr).
\tag{3.3}
\]

### Step 3: convert the weighted bound into an off-diagonal decay

Let \(\delta_x\in\ell^2(\mathcal X;V)\) be a unit vector supported at \(x\).
Then
\[
(A^{-1})_{xy}
=
\langle \delta_x, A^{-1}\delta_y\rangle_V
=
\langle W_t^{-1}\delta_x,\ A_t^{-1}\, W_t\delta_y\rangle_V.
\]
Hence
\[
\|(A^{-1})_{xy}\|_{\mathrm{op}}
\le
\|W_t^{-1}\delta_x\|\ \|A_t^{-1}\|_{\mathrm{op}}\ \|W_t\delta_y\|
=
e^{-t d(x,x_0)}\ \|A_t^{-1}\|_{\mathrm{op}}\ e^{t d(y,x_0)}.
\]
Choose \(x_0=x\). Then \(d(x,x_0)=0\) and \(d(y,x_0)=d(x,y)\), giving
\[
\|(A^{-1})_{xy}\|_{\mathrm{op}}
\le
\|A_t^{-1}\|_{\mathrm{op}}\ e^{-t d(x,y)}.
\]
Using (3.2) and the value of \(t\) from (3.3) yields the stated estimate with decay rate \(m=t\).
\(\square\)

---

## 4. Remarks for the gauge-theory application

1. **What plays the role of \(A\)?**  
   In the Helffer–Sjöstrand representation, \(A\) is the Bakry–Émery curvature matrix \(\mathcal H_\Lambda(U)\) acting on gradients (edge fields).

2. **Where does \(a_0\) come from?**  
   The matrix hinge inequality provides \(a_0=m_{\mathrm H}^2\), a uniform “Haar mass” floor.

3. **Why finite range?**  
   \(\mathcal H_\Lambda(U)\) inherits locality from the Wilson action: each link interacts only with a bounded number of nearby links (sharing a plaquette). Hence \(R\) is a lattice constant.

4. **Volume-uniform decay.**  
   Since all constants are independent of \(|\Lambda|\), the resulting decay bounds are suitable for thermodynamic limits.
