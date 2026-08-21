# Exact real-space sum-of-squares theorem for the SU(3) fourth-order lift

**Status:** PASS  
**Kernel records:** 189  
**Semantic kernel SHA-256:** `48a422a517c7c1e70b84fd88a0773943f81ae3f9bfafadbe2304f8eb7d2e9b77`

Let \(C=\partial_3\) be the cell/origin-gauge cube-boundary map with symbol

\[
\psi(k)=\bigl(e^{ik_2}-1,-(e^{ik_1}-1),e^{ik_0}-1\bigr)^T.
\]

For the complete fourth-order plaquette kernel \(H_4\),

\[
q=-20721577909065127111/7250590288602460800,\qquad A=5/12,\qquad B=17607806155349/275331901291200,
\]

and exact rational Laurent arithmetic proves

\[
\boxed{
C^\dagger(H_4-qI)C
=\frac{A}4\sum_i L_i^2
+\frac{B}4\sum_{i<j}L_iL_j
},
\qquad
L_i=(T_i-I)^\dagger(T_i-I).
\]

Equivalently,

\[
C^\dagger(H_4-qI)C
=\frac{5}{48}\sum_i L_i^2
+\frac{17607806155349}{1101327605164800}
\sum_{i<j}(\nabla_i\nabla_j)^\dagger(\nabla_i\nabla_j).
\]

This is a manifest local sum of squares.  In real space it is the 25-point stencil

\[
(Q\phi)_x=w_0\phi_x+w_1\sum_i(\phi_{x+e_i}+\phi_{x-e_i})
+w_2\sum_i(\phi_{x+2e_i}+\phi_{x-2e_i})
+w_d\sum_{i<j}\sum_{\sigma,\tau=\pm1}
\phi_{x+\sigma e_i+\tau e_j},
\]

with

\[
w_0=189690244462349/91777300430400,\quad
w_1=-132329431693349/275331901291200,\quad
w_2=5/48,\quad
w_d=17607806155349/1101327605164800,
\]

and \(w_0+6w_1+6w_2+12w_d=0\).

The cube-boundary states are not orthonormal. Their Gram operator is

\[
G=C^\dagger C=\sum_iL_i,
\]

so the physical fourth-order lift is the generalized eigenproblem

\[
Q\phi=\lambda G\phi,
\qquad
\lambda(k)=
\frac{A\sum_iX_i^2+B\sum_{i<j}X_iX_j}
{2\sum_iX_i},
\quad X_i=1-\cos k_i.
\]

The exact high-symmetry lifts are

\[
\lambda_X=A=5/12,\qquad
\lambda_M=A+\frac B2=247051057231349/550663802582400,\qquad
\lambda_R=A+B=132329431693349/275331901291200.
\]
