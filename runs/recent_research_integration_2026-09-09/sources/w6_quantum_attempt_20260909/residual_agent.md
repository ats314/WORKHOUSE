# Full transported residual: exact source jet and an all-energy obstruction

9 September 2026. Independent analytic continuation for the W6 quantum attempt.
The exact model below refutes an abstract sufficient estimate, not Wilson W6.

## 1. The actual requested force is not the cubic alone

The local source record `wilson-spatial-schur-excess.md`, SP10, SP16 and
SP17-SP18, specifies

\[
t_1=QW_1J_z,
\quad W_1=H_1-e_1+[H_0,K_1^{\rm src}],
\quad J_zp=(p,-(F_0-z)^{-1}B_0^*p).
\]

Thus the fast block of the first jet already contributes
\(-f_1(F_0-z)^{-1}B_0^*p\). Both that inverse and the true conditional
projection can spread local support. Locality of the bare magnetic cubic
does not establish bounded overlap of the complete residual.

The exact literal isometry is
\[
J_g^{\rm lit}f=\Psi_g
 [\mu_0/\mu_g]^{1/2}(y_g)f(y_g).
\]
Write \(\Psi_g=\Psi_0(1+gp_1+O(g^2))\),
\(y_g=y_0+gY_1+O(g^2)\), and
\(\mu_g=\mu_0(1+gm_1+O(g^2))\). Its **complete first derivative** is
\[
\boxed{(J_g^{\rm lit})'_0 f
=\Psi_0\left[Y_1\cdot\nabla f+
 (p_1-\tfrac12m_1(y_0))f\right],}
\]
where SP17 gives
\[
m_1(y)=2\mathbb E_0[p_1\mid y]
-\mu_0(y)^{-1}\operatorname{div}_y
   \bigl(\mu_0(y)\mathbb E_0[Y_1\mid y]\bigr).
\]
This derivation differentiates the actual quantum marginal normalization;
it is valid on the specified smooth chart/core. In particular the transport
contains retained derivatives, which cannot be treated as bounded operators
on all retained \(L^2\). The source isometry fixes the transport only on its
retained range. A full unitary extension, its action on Q, and estimates on
its generator are additional data needed to evaluate SP16 and the complete
residual. The source formula alone does not fix the Q-to-Q block.

## 2. A smooth local exact quantum model disproves the proposed fast-gradient estimate

Use the two-torus with normalized Haar measure, coordinates \(y,k\), and
\[
H_g=-\partial_k^2-(1+g\cos k)\partial_y^2,
\qquad |g|<1/2.
\]
Its closed form is
\[
h_g[f]=\int\bigl(|\partial_kf|^2+
 (1+g\cos k)|\partial_yf|^2\bigr).
\]
The true normalized ground is exactly 1 with energy zero. The actual source
projection is \(P=\mathbb E_k\), independent of g, so both the full source
and vacuum transports are the identity. There are no discarded potential,
Haar, source or vacuum terms: the complete first jet is
\(W_1=(\cos k)N_y\), \(N_y=-\partial_y^2\), and all higher jets vanish.
The reference source space reduces H0, so \(J_0p=p\). Set z=0.

The actual conditional measure is uniform on the fast circle, its vertical
operator is \(D=-\partial_k^2\) on conditional mean-zero functions, and
\(D\ge I\). Also, with \(A_g=QH_gQ\),
\[
A_g\ge(1-|g|)A_0\ge(1-|g|)D.
\]
This is an actual quantum ground conditional, with uniform smooth elliptic
metric coefficients. The retained source energy is exactly
\(b[p]=\|\partial_yp\|^2\), independent of g. Its static Schur energy is
between \((1-|g|)b[p]\) and \(b[p]\): the lower bound follows by minimizing
\(h_g[p+q]\ge(1-|g|)h_0[p+q]\), and the upper by q=0. Thus b is comparable
to the actual coarse energy, not an artificially strengthened Sobolev norm.

For \(p_n=e^{iny}\), \(n\ge1\), direct differentiation gives
\[
\begin{split}
b[p_n]&=n^2,\\
t_1p_n&=n^2\cos k\,p_n,\\
u_{0,n}=A_0^{-1}t_1p_n
 &=\frac{n^2}{n^2+1}\cos k\,p_n,\\
\rho_n=(A_g-A_0)u_{0,n}
 &=\frac{g n^4}{2(n^2+1)}\cos(2k)\,p_n.
\end{split}
\]
The conditional projection in the last line removes the constant part of
\(\cos^2k=(1+\cos2k)/2\). The Gaussian synthesis bound holds uniformly:
\[
\frac{\langle t_1p_n,A_0^{-1}t_1p_n\rangle}{b[p_n]}
=\frac{n^2}{2(n^2+1)}\le\frac12.
\]
For a sum of retained Fourier modes the same bound follows by orthogonality.
The exact selected Gaussian diagonal defect is zero because
\(\int\cos^3k\,dk=0\).

Nevertheless the proposed local derivative norm is
\[
\boxed{
\frac{\ell[\rho_n]}{g^2b[p_n]}
=\frac{n^6}{2(n^2+1)^2}\longrightarrow\infty,
\qquad \ell[f]=\|\partial_kf\|^2.}
\]
All quantities are smooth vectors in the relevant domains. Equivalently,
replace p_n by p_n/n to satisfy b=1. This failure occurs at one fixed
finite configuration space; volume growth is unnecessary. The residual
has one local differentiated profile \(\cos 2k\), but its retained
coefficient has no uniform bound by b. Bounded overlap of profiles does not
control that coefficient.

This example violates the special extra hypothesis that the horizontal
cometric depends only on y used in the ground-marginal-score theorem. It
does **not** prove that Wilson's actual complete residual violates the
estimate. It proves that quantum conditional coercivity, smooth local metric
coefficients and Gaussian inverse synthesis alone do not imply it. Any
Wilson proof must use additional structural cancellation or a weaker norm.

## 3. The weak residual norm preserves the needed retained-energy denominator

In the same example the correct dual quantity remains uniformly small:
\[
\frac{\langle\rho_n,A_0^{-1}\rho_n\rangle}{b[p_n]}
=\frac{g^2 n^6}{8(n^2+1)^2(n^2+4)}\le\frac{g^2}{8}.
\]
Inverse order and the zero diagonal defect therefore prove
\[
0\le\frac{\langle t_1p_n,(A_g^{-1}-A_0^{-1})t_1p_n\rangle}{b[p_n]}
\le\frac{g^2}{8(1-|g|)}.
\]
Fourier orthogonality first proves this for finite Fourier sums, and
continuity extends the estimate to the b-form domain. In that extension
the force is understood as a form-dual source when it is not an L2 vector.
W6 therefore holds in this model, while the proposed sufficient
fast-gradient bound is false. Replacing A0 by D in the residual inverse
throws away the n-dependent horizontal energy denominator. This is precisely
the information needed at high retained energy.

There is also a less sharp direct form-dual proof which never differentiates
the residual. For q in Q,
\[
\rho_p(q)=g\int\cos k\,\partial_yu_0\,
 \overline{\partial_yq}.
\]
The Fourier expression gives
\(\|\partial_yu_0\|^2\le b[p]/2\). Since
\(\|\partial_yq\|^2\le h_g[q]/(1-|g|)\),
\[
|\rho_p(q)|\le
\frac{|g|}{\sqrt{2(1-|g|)}}\sqrt{b[p]}\sqrt{h_g[q]}.
\]
This identifies a viable corrected proof architecture: retain the full fast
form, including its horizontal derivatives, in the local weak residual
factorization. A norm of a differentiated residual is stronger than is needed
by the exact variational identity.

On the cutoff \(n^2\le E\), the discarded gradient route does give the
rigorous bound \(\ell[\rho_p]\le(g^2E/2)b[p]\). Its growth with E states
exactly why that window calculation cannot be promoted to the complete
retained domain without separate high-energy control.

## 4. Specific Wilson stopping point

The recorded SP16-SP18 formulas determine local jets conditional on the
source extension and actual ground expansion. They do not supply volume-
uniform weighted derivatives of that extension, nor an all-energy local
factorization of \((F_g-F_0)(F_0-z)^{-1}QW_1J_zp\). The complete Wilson
operator is not evaluated by the scalar example above.

The useful next theorem is to construct a full-form weak factorization
\[
\rho_p(q)=g\langle Y_gq,K_gX_0p\rangle,
\quad\|Y_gq\|^2\le a_g[q],
\quad\|K_gX_0p\|^2\le Cb[p],
\]
with actual vacuum and source transport, local coefficient summability and
the physical coarse energy b. Here the derivative fields Y_g must retain
horizontal directions when they are needed for high-energy compensation.
This is an explicit unproved Wilson target, not a theorem established by
rewriting the desired norm. No all-volume Wilson residual estimate or W6
proof is claimed by this note.

## 5. Exact controls

`verify_residual_agent.py` checks rational versions of the displayed norm
identities, the high-energy lower witness and the polynomial identity behind
the dual estimate at selected integers. The trigonometric differential and
all-mode proofs above are analytic. These controls do not formalize or prove
the Wilson application.
