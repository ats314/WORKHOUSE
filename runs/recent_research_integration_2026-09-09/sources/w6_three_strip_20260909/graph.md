# Complete Gaussian reference graph for the three-plaquette strip

9 September 2026. Exact finite-cell Gaussian calculation and an independent
audit of the complete physical first-jet cancellation.

## Reference and invariant Gram form

In the wavefunction convention,

\[
H_0=-\tfrac12\sum_{ij}C_{ij}\nabla_i\cdot\nabla_j
       +\tfrac12\sum_i|X_i|^2,
\quad
C=\begin{pmatrix}4&-1&0\\-1&4&-1\\0&-1&4\end{pmatrix}.
\]

Put \(B=C^{1/2}\), \(\Sigma=B/2\), \(s=(1,1,1)^T\),
\(Y=\sum_iX_i\) and \(v=s^T\Sigma s\). The true reference ground is
\(\Omega_0\propto\exp(-X^TC^{-1/2}X/2)\). In its probability,
each color has covariance \(\Sigma\); the three colors are independent.
The ground-transformed generator is

\[
L_0=-\tfrac12 C:\nabla^2+(BX)\cdot\nabla.
\]

The physical invariant second Gaussian chaos consists of

\[
f_M=\sum_{ij}M_{ij}X_i\cdot X_j-3\operatorname{tr}(M\Sigma),
\qquad M=M^T\in\mathbb R^{3\times3}.
\]

Its exact Gram and generator formulas are

\[
\langle f_M,f_N\rangle=6\operatorname{tr}(M\Sigma N\Sigma),
\qquad L_0f_M=f_{BM+MB}.
\tag{G1}
\]

The literal Gaussian retained projection is conditioning on \(Y\).
On this chaos it has rank one:

\[
P_0f_M=\frac{s^T\Sigma M\Sigma s}{v^2}\,p,
\qquad p=|Y|^2-3v.
\tag{G2}
\]

It does not reduce \(L_0\). In particular, \(s\) is not an eigenvector
of \(B\). This calculation retains the resulting fast graph correction.

## Exact graph on the first retained excitation

Let \(N_z\) be the symmetric solution of

\[
BN_z+N_zB-zN_z=ss^T,
\qquad
\beta(z)=\frac{s^T\Sigma N_z\Sigma s}{v^2}.
\]

Then, for real \(z<2\sqrt{4-\sqrt2}\),

\[
\boxed{J_zp=f_{N_z/\beta(z)}.}
\tag{G3}
\]

Indeed \(P_0J_zp=p\), while
\((L_0-z)J_zp=p/\beta(z)\) lies in the retained space. Thus
\(Q_0(L_0-z)J_zp=0\), the defining reference graph equation.
The corresponding Schur eigenvalue is \(\beta(z)^{-1}\).

The normalized mode vectors, in frequency order, are

\[
u_-=(1,\sqrt2,1)^T/2,\quad
u_0=(1,0,-1)^T/\sqrt2,\quad
u_+=(1,-\sqrt2,1)^T/2,
\]

with frequencies \(a=\sqrt{4-\sqrt2}\), \(2\), and
\(b=\sqrt{4+\sqrt2}\). Put \(h_-=1+1/\sqrt2\),
\(h_+=1-1/\sqrt2\). In these modes,

\[
(N_z)_{ij}^{\rm mode}=\frac{h_i h_j}{\omega_i+\omega_j-z},
\quad h_0=0,\quad
v=\tfrac12(ah_-^2+bh_+^2).
\tag{G4}
\]

At \(z=0\):

| Quantity | Value |
|---|---:|
| \(v\) | 2.4428891037758432544 |
| \(\beta(0)\) | 0.30632592593159566355 |
| \(\|p\|^2\) | 35.806243040080456039 |
| \(\|Q_0J_0p\|^2\) | 0.094246891895676892429 |
| \(\langle p,L_0p\rangle=48v\) | 117.25867698124047621 |
| \(\langle J_0p,L_0J_0p\rangle=6v^2/\beta(0)\) | 116.88936524450821543 |

The positive fast-graph norm explicitly verifies nonreduction.

## Exact graph on every retained radial chaos

Let \(p_n\) be any nonzero retained radial Hermite polynomial of total
degree \(2n\), equivalently a radial Laguerre polynomial in
\(|Y|^2/(2v)\), with \(n\ge1\). Its normalization is immaterial.
Define

\[
w_- = \frac{ah_-^2}{ah_-^2+bh_+^2},\qquad w_+=1-w_-,
\]

and

\[
\alpha_n(z)=\sum_{k=0}^{2n}
\binom{2n}{k}
\frac{w_-^k w_+^{2n-k}}
{ka+(2n-k)b-z}.
\tag{G5}
\]

Then the full Gaussian graph and Schur operator satisfy

\[
\boxed{
J_zp_n=\frac{(L_0-z)^{-1}p_n}{\alpha_n(z)},
\qquad S_0(z)p_n=\alpha_n(z)^{-1}p_n.
}
\tag{G6}
\]

Here the inverse in (G6) acts on the positive-degree chaos; it causes
no vacuum ambiguity at \(z=0\). Formula (G5) follows directly from
second quantization: the normalized retained one-particle vector has
squared mode components \(w_-,w_+\); its radial \(2n\)-particle
tensor has the binomial spectral measure displayed. Equivalently,

\[
\frac{\langle p_n,e^{-tL_0}p_n\rangle}{\|p_n\|^2}
=(w_-e^{-at}+w_+e^{-bt})^{2n}.
\]

Integrating against \(e^{tz}\) gives (G5). Different chaos degrees
are orthogonal and preserved by both the generator and conditioning,
so these formulas specify the graph on the full radial polynomial core.
They also give

\[
\frac{\|J_zp_n\|^2}{\|p_n\|^2}
=\frac{\alpha_n'(z)}{\alpha_n(z)^2}.
\tag{G7}
\]

## Complete first-jet cancellation on this nonreducing graph

The geometric and source calculations supply the actual first jet and
the literal-source-compatible unitary generator

\[
\begin{split}
H_1={}&\tfrac12(X_0+3X_1)\cdot(\nabla_0\times\nabla_1)
+\tfrac12(X_1+3X_2)\cdot(\nabla_1\times\nabla_2)\\
&+X_2\cdot(\nabla_0\times\nabla_2),\\
K={}&-\tfrac12(X_0\times X_1)\cdot\nabla_0.
\end{split}
\]

Direct calculation, independent of a test-state truncation, yields

\[
\boxed{
W_1=H_1+[H_0,K]
=-\left(\nabla_0+\tfrac32\nabla_1-\tfrac12\nabla_2\right)
\cdot\mathcal J,
\quad
\mathcal J=\sum_i X_i\times\nabla_i.
}
\tag{G8}
\]

Physical scalar functions satisfy \(\mathcal Jf=0\); this includes
\(\Omega_0f\), every physical reference graph vector, and the invariant
odd cubic \(T=X_0\cdot(X_1\times X_2)\). Therefore

\[
\boxed{t_1=Q_0W_1J_z=0}
\]

on the entire physical source polynomial core, despite nonreduction.
Its inverse energy and the first residual coefficient
\(Q_0W_1(F_0-z)^{-1}t_1\) are consequently zero. This is a complete
first-coefficient identity; it does not assert that the next even
coefficient or the finite-coupling off-diagonal source vanishes.

For later use the sole invariant cubic has exact data

\[
L_0T=(a+2+b)T,\quad
\|T\|^2=6\det\Sigma=\tfrac32\sqrt{14}.
\]

## Verification

[verify_graph.py](verify_graph.py) gives **22 passing exact controls** in
[graph_checks.json](graph_checks.json). The commutator and Ward
factorization are each checked on all 55 Cartesian monomials of degree
at most two. Since both identities concern differential operators of
order at most two, these tests determine every coefficient. Additional
controls evaluate invariant states of degrees three through six,
the Gaussian Sylvester inverse, source normalization and graph norm.
The all-chaos formula (G5) is the analytic second-quantization argument
above, with its first-chaos instance independently checked by the exact
matrix calculation. No Lean certification is claimed.
