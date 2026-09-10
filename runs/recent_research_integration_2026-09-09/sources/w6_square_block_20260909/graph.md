# Exact square-block Gaussian inverse and nonzero complete first force

9 September 2026. The actual twelve-edge, four-plaquette SU(2) block.

Use nested based holonomy variables \(X_0,X_1,X_2,X_3\), with
literal retained coordinate \(a=|X_2+X_3|^2/2\). The original-edge
geometry gives

\[
C=\begin{pmatrix}4&-1&3&-1\\-1&4&-1&3\\3&-1&6&-2\\-1&3&-2&6\end{pmatrix},
\qquad
V=\begin{pmatrix}2&0&-1&0\\0&2&0&-1\\-1&0&1&0\\0&-1&0&1\end{pmatrix}.
\]

The Gaussian Hamiltonian is \(H_0=-C:\nabla^2/2+X^TVX/2\).
Write \(D=(CV)^{1/2}\), \(A=C^{-1}D\) and
\(\Sigma=A^{-1}/2\). Then \(ACA=V\), and the true Gaussian ground
is \(\Omega_0\propto e^{-X^TAX/2}\). Each color has covariance
\(\Sigma\). The drift frequencies are \(\sqrt2,2,2,\sqrt6\).

## The literal outer source reduces this Gaussian reference

For \(s=(0,0,1,1)^T\), direct calculation gives

\[
D^Ts=\sqrt2s,\qquad s^T\Sigma s=2\sqrt2.
\]

Thus conditioning on \(Y=X_2+X_3\) reduces the full reference
generator. Its physical radial restriction, with \(q=Y/\sqrt2\), is

\[
L_q=-2\Delta_q+\sqrt2q\cdot\nabla_q,
\qquad
L_q\phi(a)=-8a\phi''+(2\sqrt2a-12)\phi'.
\]

Here \(a=|q|^2\), \(\mathbb E q_iq_j=\sqrt2\delta_{ij}\).
Consequently the exact Gaussian graph is \(J_z=P_0\) for this
source. This conclusion follows from the actual covariance and drift,
not from an assumed block decoupling.

## Four-dimensional physical cubic inverse

Use the oriented cubic basis

\[
T_i=(-1)^i\det(X_j:j\ne i),\qquad i=0,1,2,3,
\]

with the remaining rows in increasing order. There are exactly four
independent physical odd cubics. Their Gram matrix and generator are

\[
G=6\det(\Sigma)\Sigma^{-1}=6\sqrt3 A,
\qquad
L_0T=ET,\quad E=\operatorname{tr}(D)I-D^T.
\tag{Q1}
\]

For coefficient columns \(h\), the inverse acts by
\((E^T-z)^{-1}h\). Hence

\[
\langle h^TT,(F_0-z)^{-1}h^TT\rangle
=h^TG(E^T-z)^{-1}h.
\tag{Q2}
\]

All physical odd cubics have zero conditional expectation given \(Y\),
so this is the full fast inverse on the cubic sector.

## Complete true-ground and literal-source first force

The actual first ground correction is

\[
p_1=c(T_{012}+T_{013})+d(T_{023}+T_{123}),
\]

where \(T_{ijk}=X_i\cdot(X_j\times X_k)\), and

\[
c=-\frac18+\frac{\sqrt6}{24},\qquad
d=-\frac3{56}-\frac{\sqrt2}{56}+\frac{\sqrt6}{48}.
\]

The literal first observation and marginal jets both vanish, so
\(J_1^{\rm lit}\phi=\Omega_0p_1\phi\). Using this actual normalized
source jet, the true ground equation, and the full electric \(H_1\),

\[
\begin{split}
t_1\phi
&=Q_0\Omega_0^{-1}
  \big[H_1\Omega_0\phi+(H_0-e_0)\Omega_0p_1\phi
                   -\Omega_0p_1L_q\phi\big]\\
&=\boxed{\frac{\sqrt2-4}{7}(T_{023}+T_{123})\phi'(a).}
\tag{Q3}
\end{split}
\]

The would-be quintic term cancels by the full quantum ground equation.
The retained second derivative term is zero. Formula (Q3) holds for
every smooth radial source on the coefficient core, not only the first
excitation. The source and geometry agents computed (Q3) independently.

For \(\phi_1=a-3\sqrt2\), the cubic in (Q3) is a true Gaussian
eigenfunction with eigenvalue \(4+\sqrt2\). Therefore

\[
\boxed{
\langle t_1\phi_1,F_0^{-1}t_1\phi_1\rangle
=\frac{528\sqrt2-600}{343}
=0.427710673274035527018342992369\ldots.
}
\tag{Q4}
\]

The actual retained energy is \(b[\phi_1]=24\sqrt2\), so the exact
ratio is

\[
\frac{44-25\sqrt2}{686}
=0.0126015465607472649853611980973\ldots.
\tag{Q5}
\]

For spectral shift \(z<4+\sqrt2\), replace the cubic denominator
\(4+\sqrt2\) by \(4+\sqrt2-z\), with the whole fast inverse
defined on its separate resolvent domain.

The independent Gaussian variables

\[
q=(X_2+X_3)/\sqrt2,\quad
u=(X_0+X_1)/\sqrt2-q/2,\quad
s=(X_2-X_3)/\sqrt2,\quad
v=(X_0-X_1)/\sqrt2-s/2
\]

have component variances \(\sqrt2,1/2,2,\sqrt6/4\) and frequencies
\(\sqrt2,2,2,\sqrt6\), respectively. In these coordinates
\(T_{023}+T_{123}=\sqrt2 q\cdot(u\times s)\). This identifies the
complete force as retained degree one times fast degree two and allows
the full retained-energy inverse estimate to be proved directly.

## Verification and scope

[verify_graph.py](verify_graph.py) independently computes the Gaussian
ground, cubic ground correction, complete force and cubic inverse.
[graph_checks.json](graph_checks.json) records **10 passing exact
controls**. The script retains the actual shared-edge matrices and the
true quantum ground correction. These are complete first asymptotic
coefficients of this fixed Wilson block; finite-coupling remainder
bounds are separate questions.
