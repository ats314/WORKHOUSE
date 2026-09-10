# All-retained-energy inverse synthesis audit

Date: 2026-09-09. This independently audits the complete second-order source
coefficient computed in the adjacent-strip calculation. It proves an
inverse-energy estimate for every radial retained state of finite reference
form energy, not only the first retained polynomial excitation.

## Input coefficient and exact inverse sector

Let `s,t` be independent three-dimensional centered Gaussian vectors with
covariance matrices `sigma_s I`, `sigma_t I`, where
\[
\sigma_s=\sqrt3/2,\qquad \sigma_t=\sqrt5/2.
\]
These symbols denote **variances**, not standard deviations. Let
\[
L_0=L_s+L_t=\sqrt3 N_s+\sqrt5 N_t,
\quad a=|s|^2,\quad
B=|t|^2-3\sigma_t,\quad C=(s\cdot t)^2-\sigma_t a,
\quad k=\frac{3(\sqrt5-\sqrt3)}{160}.
\]
The actual complete coefficient supplied by the strip calculation is
\[
t_2\varphi=k[-11aB+6C]\varphi'(a).
\tag{I1}
\]
It lies entirely in fast Hermite degree two. Consequently its full
reference inverse is exactly
\[
A_0^{-1}\big|_{\operatorname{ran}t_2}
=(L_s+2\sqrt5)^{-1}\otimes I.
\tag{I2}
\]
The retained contribution `L_s` is present throughout the estimate.

## Tensor factorization

Put
\[
Q_{ij}=t_it_j-\sigma_t\delta_{ij},\quad
R_{ij}\varphi=s_i\partial_j\varphi,\quad
M_{ij}\varphi=6s_i\partial_j\varphi
-11\delta_{ij}\sum_\ell s_\ell\partial_\ell\varphi.
\]
For a radial `varphi(a)`, `partial_j varphi=2s_j varphi'(a)`, so exactly
\[
t_2\varphi=\frac{k}{2}\sum_{i,j}Q_{ij}M_{ij}\varphi.
\tag{I3}
\]
The covariance is
\[
E[Q_{ij}Q_{k\ell}]
=\sigma_t^2(\delta_{ik}\delta_{j\ell}
+\delta_{i\ell}\delta_{jk}).
\]
Since `M` is symmetric for radial input, with `A_s=L_s+2sqrt5`,
\[
\langle t_2\varphi,A_0^{-1}t_2\varphi\rangle
=\frac{k^2\sigma_t^2}{2}
\sum_{i,j}\|A_s^{-1/2}M_{ij}\varphi\|^2.
\tag{I4}
\]
For nonsymmetric matrix inputs the same right side is an upper bound,
because symmetrization is an orthogonal projection.

The matrix map `R -> 6R-11(tr R)I` has Frobenius operator norm **27**:
it is multiplication by `-27` on scalar matrices and by `6` on trace-free
matrices. This remains true for matrices with Hilbert-space entries.
Hence
\[
\sum_{i,j}\|A_s^{-1/2}M_{ij}\varphi\|^2
\le729\sum_{i,j}\|A_s^{-1/2}s_i\partial_j\varphi\|^2.
\tag{I5}
\]

## Uniform multiplication estimate with the full denominator

In normalized Gaussian Hermite coordinates,
\[
s_i=\sqrt{\sigma_s}(a_i+a_i^*),\qquad
A_s=\sqrt3(N_s+c),\qquad c=2\sqrt5/\sqrt3>1.
\]
For a Hermite multi-index `n`, the squared ladder coefficients after left
multiplication by `(N_s+c)^(-1/2)` are
\[
\frac{n_i}{|n|-1+c}\le1\quad(n_i\ge1),
\qquad
\frac{n_i+1}{|n|+1+c}\le1.
\]
Each shift sends distinct input basis vectors to distinct output basis
vectors. These inequalities therefore establish actual operator norms,
not just individual diagonal matrix elements. The triangle inequality gives
\[
\|A_s^{-1/2}s_i\|
\le2\sqrt{\sigma_s/\sqrt3}=\sqrt2.
\tag{I6}
\]
It follows that
\[
\sum_{i,j}\|A_s^{-1/2}s_i\partial_j\varphi\|^2
\le6\|\nabla_s\varphi\|^2.
\tag{I7}
\]
Combining (I4)--(I7) and using the exact retained reference form
\[
b[\varphi]=\langle\varphi,L_s\varphi\rangle
=\frac32\|\nabla_s\varphi\|^2
\]
proves
\[
\boxed{\langle t_2\varphi,A_0^{-1}t_2\varphi\rangle
\le K\,b[\varphi],\qquad
K=\frac{3645}{2}k^2
=\frac{6561(4-\sqrt{15})}{5120}.}
\tag{I8}
\]
The denominator in the simplified constant is `5120`, not `2560`.

## Spectral shifts and domains

The same constant works for real spectral shifts
\[
z\le2\sqrt5-\sqrt3,
\]
provided the inverse is understood on this fast-degree-two source sector:
replace `c` above by `(2sqrt5-z)/sqrt3`, which remains at least one.
Positivity or invertibility on other fast sectors is a separate condition
if one writes the inverse as that of the entire fast operator.

First prove the displayed identities on finite Gaussian polynomials.
Radial Gaussian polynomials are a form core for radial finite-energy
states (radial Hermite/Laguerre spectral truncation proves this).
Equation (I8) then extends `t2` continuously from the retained form domain
into the **full inverse-energy dual**. It does not require that every
finite-energy state's polynomially weighted residual belongs to ordinary
`L2`. This is precisely the denominator-preserving extension needed here.

This is an all-retained-source theorem for the computed second-order
coefficient on the actual adjacent strip. No finite-g remainder,
interacting-resolvent comparison, or volume-uniform interface estimate is
assumed or inferred.
