# Exact physical operator for the adjacent two-square SU(2) Wilson strip

Date: 2026-09-09. Scope: the actual seven-edge strip, with a common edge and
simultaneous Gauss invariance. The interacting vacuum below is the ground of
this coupled operator; it is not replaced by a product vacuum or a classical
Gibbs density.

## 1. Link metric and complete physical quotient

Use the conventions of
`WORKHOUSE-flat-holonomy-20260907/paper/research_notes/G19_WILSON_BLOCK_SCORE_AND_FIBER_OBSTRUCTION_20260905.md`,
section 6.1: the based face loops are `U1=s b1`, `U2=b2 s^-1`, the Lie basis
is `T_a=i sigma_a/2`, and the exact electric generator is

\[
\Delta_{\rm link}=3(\Delta_1+\Delta_2)+\sum_a(L_{1a}-R_{2a})^2.
\tag{A1}
\]

Write
\[
U_1=xI+i\mathbf a\cdot\sigma,\qquad
U_2=yI+i\mathbf b\cdot\sigma,\qquad
z=\tfrac12\operatorname{Tr}(U_1U_2)=xy-\mathbf a\cdot\mathbf b.
\]
The triple `(x,y,z)` is a complete set of simultaneous-conjugation invariants:
the Gram matrix of two vectors determines their SO(3) orbit. Its domain is
\[
\mathcal D=\{(x,y,z)\in[-1,1]^3:
\mathscr D=1-x^2-y^2-z^2+2xyz\ge0\}.
\tag{A2}
\]
The product Haar pushforward is **constant**, `(2/pi^2) dx dy dz` on this
domain. Indeed each scalar quaternion coordinate has density
`(2/pi) sqrt(1-x^2)`, and the angle cosine between the two vector parts is
uniform on `[-1,1]`. Changing this cosine to `z` cancels the two square roots.

For fixed `z`, the fiber is the ellipse
\[
E_z=\{(x,y):x^2-2zxy+y^2\le1-z^2\},
\qquad |E_z|=\pi\sqrt{1-z^2}.
\tag{A3}
\]
Consequently the literal coarse holonomy `U=U1 U2` has the ordinary SU(2)
Haar scalar density `(2/pi) sqrt(1-z^2)` before ground weighting.

## 2. Explicit coupled second-order operator

Let `Gamma(f,h)` be the sum of products of derivatives in (A1). Its physical
cometric is
\[
G=\begin{pmatrix}
1-x^2 &(z-xy)/4&3(y-xz)/4\\
(z-xy)/4&1-y^2&3(x-yz)/4\\
3(y-xz)/4&3(x-yz)/4&3(1-z^2)/2
\end{pmatrix}.
\tag{A4}
\]
Thus, exactly,
\[
\begin{aligned}
\Delta_{\rm link} f={}&(1-x^2)f_{xx}+(1-y^2)f_{yy}
+\tfrac32(1-z^2)f_{zz}\\
&+\tfrac12(z-xy)f_{xy}
+\tfrac32(y-xz)f_{xz}+\tfrac32(x-yz)f_{yz}\\
&-3xf_x-3yf_y-\tfrac92zf_z.
\end{aligned}
\tag{A5}
\]
It is in divergence form `div(G grad f)` for the constant quotient Haar
density. Its determinant is
\[
\det G=\frac3{32}\mathscr D
\bigl(16-6x^2-3xyz-6y^2-z^2\bigr).
\tag{A6}
\]
The physically specified self-adjoint realization is inherited from smooth
simultaneous-conjugation-invariant functions on `SU(2)^2`. Artificial
Dirichlet boundary conditions on the singular quotient boundary would give
a different operator.

With `u=g^-4` and `v(U)=2-Re Tr U`, the actual strip Hamiltonian is
\[
H_u=-\tfrac12\Delta_{\rm link}+4u(2-x-y).
\tag{A7}
\]
This retains all seven electric edge derivatives. The shared derivative
annihilates the coarse trace exactly:
\[
(L_{1a}-R_{2a})z=0.
\tag{A8}
\]
That cancellation does not remove its contribution to the interacting
ground or to fast functions.

## 3. Exact true-ground source formula

Let `Omega_u(x,y,z)>0` be the normalized ground of (A7), with energy `E_u`.
The ground transform on `d nu_u=(2/pi^2) Omega_u^2 dx dy dz` is
\[
\mathcal H_u=\Omega_u^{-1}(H_u-E_u)\Omega_u
=-\tfrac12\Delta_{\rm link}-\Gamma(\log\Omega_u,\cdot).
\tag{A9}
\]
Its quadratic form is `(1/2) integral Gamma(f,f) d nu_u`. Define the literal
coarse conditional expectation `P_u f=E_nu[f|z]` and `Q_u=1-P_u`. The actual
conditional law and marginal are
\[
\rho_{u,z}(x,y)=\frac{\Omega_u(x,y,z)^2}
 {\int_{E_z}\Omega_u(x',y',z)^2dx'dy'},\qquad
\mu_u(z)=\frac2{\pi^2}\int_{E_z}\Omega_u^2dxdy.
\tag{A10}
\]
Set
\[
\tau_u=\Gamma(\log\Omega_u,z)
=\frac34\left[(y-xz)\partial_x\log\Omega_u
+(x-yz)\partial_y\log\Omega_u
+2(1-z^2)\partial_z\log\Omega_u\right].
\tag{A11}
\]
For every smooth physical retained source `p(z)`, the complete off-diagonal
coupling is
\[
\boxed{Q_u\mathcal H_u P_u p
=-\bigl(\tau_u-E[\tau_u\mid z]\bigr)p'(z).}
\tag{A12}
\]
**Derivation.** Equation (A5) gives
\[
\mathcal H_u p=-\tfrac34(1-z^2)p''
+\bigl(\tfrac94z-\tau_u\bigr)p'.
\]
Both the `p''` coefficient and the vacuum-independent part of the `p'`
coefficient depend only on `z`, so `Q_u` removes them identically. There are
no omitted product-vacuum, Haar, or shared-edge terms in (A12).

The retained quadratic form is explicitly
\[
a_c[p]=\frac34\int_{-1}^1(1-z^2)|p'(z)|^2\mu_u(z)dz,
\tag{A13}
\]
and
\[
P_u\mathcal H_uP_u p
=-\frac{3}{4\mu_u}\partial_z\bigl(\mu_u(1-z^2)p'\bigr).
\tag{A14}
\]
Equating the two retained expressions also gives
\[
E[\tau_u\mid z]
=\tfrac34z+\tfrac34(1-z^2)\partial_z\log\mu_u.
\tag{A15}
\]
As a consistency check, the Haar vacuum `Omega=1` makes both sides zero.

If the full fast restriction `F_u=Q_u mathcal H_u Q_u` has a positive
inverse, positivity of the full quadratic form gives the exact Schur bound
\[
\langle Q_u\mathcal H_uP_up,F_u^{-1}Q_u\mathcal H_uP_up\rangle
\le a_c[p].
\tag{A16}
\]
The same statement holds in the energy-dual generalized-inverse sense
without presupposing a uniform spectral gap. This is an exact bound with
no small factor claimed. It identifies the actual interacting quantity to
estimate using (A11), instead of replacing it by a local classical score.

## 4. Physical inversion parity and the first jet

Simultaneous inversion sends `(mathbf a,mathbf b)` to
`(-mathbf a,-mathbf b)` and fixes **all three** invariants `x,y,z`. This can
also be seen by a pi rotation about an axis perpendicular to their span.
Therefore every physical two-loop SU(2) function satisfies
\[
f(U_1^{-1},U_2^{-1})=f(U_1,U_2).
\tag{A17}
\]
In weak-field pair coordinates `U1=exp(g X)`, `U2=exp(g Y)`, the quotient
pullback is even in `g`. The pulled-back physical operator, its true ground,
and the literal scalar coarse map are also even. On fixed local charts,
the positive Jacobian transport and vacuum multiplication inherit this
parity. Consequently, **if the W6 identification uses this parity-compatible
transport and the first derivative exists**, its physical first jet is
\[
W_1=\partial_g\widehat H_g\big|_{g=0}=0,
\qquad t_1=QW_1J=0.
\tag{A18}
\]
This does not say that the finite-`g` coupling (A12) vanishes. It says that
the first nonzero physical correction is of even order in this two-loop
SU(2) chart. An arbitrary `g`-dependent unitary transport can manufacture
an odd commutator jet, so (A18) must not be transferred without checking
the literal transport convention. With three independent Lie vectors the
scalar triple product is a physical inversion-odd invariant; (A17) then
fails and a nonzero physical first-jet mechanism can occur.

## 5. Verification

`verify_operator.py` starts from quaternion left/right vector fields and
the actual seven-edge metric (A1). It checks all six cometric entries,
all three drift coefficients, all three flat-density divergence
coefficients, the shared-edge cancellation, inversion parity, and the
determinant. Result: **15/15 exact polynomial checks** in
`operator_checks.json`. These are algebra checks of the exact finite
operator, not a computation of its interacting ground or an estimate of
an infinite-lattice residual.
