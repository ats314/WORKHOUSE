# Sharp inverse-energy theorem for the complete first square-block force

Date: 2026-09-09. This is an all-source estimate for the actual first
transported coefficient, with the full Gaussian inverse retained.

The original-edge calculation and complete ground/source transport give

\[
t_1\varphi=\frac{\sqrt2-4}{7}(T_{023}+T_{123})\varphi'(a),
\quad a=\frac{|X_2+X_3|^2}{2},\quad
T_{ijk}=X_i\cdot(X_j\times X_k).
\tag{S1}
\]

Introduce independent three-dimensional Gaussian vectors

\[
q=\frac{X_2+X_3}{\sqrt2},\quad
u=\frac{X_0+X_1}{\sqrt2}-\frac q2,\quad
s=\frac{X_2-X_3}{\sqrt2},\quad
v=\frac{X_0-X_1}{\sqrt2}-\frac s2.
\]

Their variances per component are respectively
\(\sqrt2,1/2,2,\sqrt6/4\), and their OU frequencies are
\(\sqrt2,2,2,\sqrt6\). In particular

\[
L_0=\sqrt2 N_q+2N_u+2N_s+\sqrt6 N_v,
\qquad b[\varphi]=2\|\nabla_q\varphi\|^2.
\tag{S2}
\]

The retained physical space consists of radial functions of \(q\).
It reduces \(L_0\), so the reference graph lift is the retained inclusion.
Set \(\gamma=(4\sqrt2-2)/7\). The force factors exactly as

\[
t_1\varphi=\gamma u\cdot(q\times s)\varphi'(|q|^2)
=\frac\gamma2(s\times u)\cdot\nabla_q\varphi.
\tag{S3}
\]

The fast vector \(s\times u\) has mean zero, covariance \(2I_3\),
and exact fast excitation energy \(4\). Consequently the **full**
inverse gives the identity

\[
\boxed{
\langle t_1\varphi,F_0^{-1}t_1\varphi\rangle
=\frac{\gamma^2}{2}\sum_{i=1}^3
\langle\partial_i\varphi,(L_q+4)^{-1}\partial_i\varphi\rangle.}
\tag{S4}
\]

Every derivative of a radial function is odd in \(q\), so its
\(L_q\)-spectral support is at least \(\sqrt2\). Hence

\[
\boxed{
\langle t_1\varphi,F_0^{-1}t_1\varphi\rangle
\le K\,b[\varphi],\qquad
K=\frac{\gamma^2}{4(4+\sqrt2)}
=\frac{(4-\sqrt2)^3}{1372}
=0.0126015465607472649853611980973\ldots .}
\tag{S5}
\]

This constant is sharp. The first retained excitation
\(\varphi_1=a-3\sqrt2\) has \(b[\varphi_1]=24\sqrt2\) and

\[
\langle t_1\varphi_1,F_0^{-1}t_1\varphi_1\rangle
=\frac{528\sqrt2-600}{343}
=K\,24\sqrt2.
\tag{S6}
\]

More precisely, on the radial Hermite level of total degree \(2n\),
\(n\ge1\), the energy ratio is exactly

\[
K_n=\frac{\gamma^2}{4[4+\sqrt2(2n-1)]}.
\tag{S7}
\]

Orthogonality of different Hermite levels proves the same bound for their
arbitrary superpositions. First establish the identity on radial Gaussian
polynomials, then use radial spectral truncation as a form core. The bound
extends the force continuously from the retained form domain into the
inverse-energy dual; ordinary unweighted residual \(L^2\) membership is
unnecessary.

The same proof gives \(K(z)=\gamma^2/[4(4+\sqrt2-z)]\) for real
\(z<4+\sqrt2\), when the inverse is restricted to this force sector.
Writing it as the inverse of the entire fast operator additionally requires
that the entire fast operator be invertible at that shift.

## Consequence for the next W6 calculation

The coefficient is nonzero, its inverse image is explicit, and its
all-source inverse-energy norm is now controlled. The next insertion is
the complete transported defect acting on that image:
\(\rho_1=QW_1F_0^{-1}t_1\). The calculation of that insertion must retain
the ground correction, source transport, fast projection and every
resulting chaos sector. Equation (S5) establishes the input bound for this
step; it does not replace the insertion by a derivative seminorm.
