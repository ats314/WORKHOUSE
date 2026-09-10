# Actual compact-square source moment and conditional-score reduction

10 September 2026. New analytic consequence of the existing twelve-edge
Wilson square, its actual quantum ground, and its established physical gap.
This proves a uniform all-source potential-moment estimate. The additional
conditional-score inequality identified below remains unproved.

## 1. Exact original operator and source normalization

Use the original-edge convention of
[geometry.md](../../REPO/runs/recent_research_integration_2026-09-09/sources/w6_square_block_20260909/geometry.md),
its exact tree geometry and S3-S4, and
[quantile_scale.md](../../REPO/runs/recent_research_integration_2026-09-09/sources/w6_compact_continuation_20260909/quantile_scale.md),
Q1-Q14:

\[
T=-\tfrac12\sum_{e,a}(E_e^a)^2,\quad
\mathsf H_g=g^2T+g^{-2}V,\quad
\mathsf H_g\Psi_g=e_g\Psi_g,\quad \|\Psi_g\|_2=1.
\tag{M1}
\]

The four based group variables are U0,U1,U2,U3. Set

\[
F_1=U_2U_0^{-1},\quad F_2=U_0,\quad
F_3=U_3U_1^{-1},\quad F_4=U_1.
\]

These are the four face holonomies, in an order in which

\[
Q=U_2U_3=F_1F_2F_3F_4,\qquad
w=\tfrac12\operatorname{Tr}Q,\qquad
V=4\sum_{i=1}^4(1-\tfrac12\operatorname{Tr}F_i).
\tag{M2}
\]

All Ui and Fi transform by simultaneous conjugation under the remaining
gauge action. Consequently w, V and every f(w) are physical functions.
The true positive ground is physical by invariance and uniqueness.

Only eight original boundary edges differentiate w. The four interior
edges annihilate it, as recorded in the original-edge table of geometry.md.
For clarity, write an SU(2) matrix as `Q=w I+i r.sigma` and use
`T_a=i sigma_a/2`. Then the trace derivative under one left multiplication
is `Tr(T_a Q)/2=-r_a/2`. Right multiplication, an orientation reversal or
an adjoint rotation gives the same sum of squared derivatives. Thus each
boundary edge contributes `(1-w^2)/4`, and the eight edges give

\[
\Gamma(w,w):=\sum_{e,a}|E_e^a w|^2=2(1-w^2),\qquad
\sum_{e,a}(E_e^a)^2w=-6w.
\tag{M3}
\]

The second identity is eight copies of the fundamental Casimir `-3w/4`.
In particular no factor of two is hidden in the retained energy. With
`dmu_g=Psi_g^2 dU` and its literal trace marginal `dnu_g`,

\[
b_g[f]=\frac{g^2}{2}\int\Gamma(f(w),f(w))d\mu_g
=g^2\int(1-w^2)|f'(w)|^2d\nu_g(w).
\tag{M4}
\]

This is exactly C11 in
[compact_residual.md](../../REPO/runs/recent_research_integration_2026-09-09/sources/w6_compact_continuation_20260909/compact_residual.md).

## 2. Global noncommuting holonomy inequality

For a two-dimensional SU(2) matrix F the Frobenius norm obeys

\[
\|I-F\|_{\rm F}^2=4(1-\tfrac12\operatorname{Tr}F).
\]

The exact telescoping identity, with products in their actual order, is

\[
I-F_1F_2F_3F_4
=\sum_{i=1}^4F_1\cdots F_{i-1}(I-F_i).
\]

Unitary invariance of the Frobenius norm and Cauchy-Schwarz for four
summands imply

\[
4(1-w)=\|I-Q\|_{\rm F}^2
\le4\sum_{i=1}^4\|I-F_i\|_{\rm F}^2=4V.
\]

Hence, globally on the actual compact configuration space,

\[
\boxed{0\le1-w\le V.}\tag{M5}
\]

This uses no commutation of the face holonomies and no small-field chart.
The constant one cannot be reduced uniformly: for four equal face
holonomies `F_i=exp(t T_3)`, the ratio `(1-w)/V` tends to one as t tends
to zero. Those face values are realized by
`U0=U1=exp(t T_3)`, `U2=U3=exp(2t T_3)`.

## 3. Uniform actual all-source potential moment

For any source f in the actual compact retained form domain, the exact
ground-state identity is

\[
\mathsf H_g[\Psi_g f(w)]
=e_g\|f\|_{L^2(\nu_g)}^2+b_g[f].
\tag{M6}
\]

On a smooth core this follows by expanding the original-edge derivatives
of `Psi_g f(w)` and integrating their cross term by parts against the
ground equation. Complex f uses the real part of the cross term. Form
closure extends the identity. Since T and V are nonnegative, M5-M6 give

\[
\boxed{
g^{-2}\int(1-w)|f|^2d\nu_g
\le g^{-2}\int V|f(w)|^2d\mu_g
\le b_g[f]+e_g\|f\|_{L^2(\nu_g)}^2.}
\tag{M7}
\]

The actual fixed-square prior results give `e_g<=E` and physical gap
`gamma>0` uniformly on a sufficiently small interval `0<g<g_*`.
For centered f, `nu_g f=0`, the physical gap supplies
`||f||^2<=b_g[f]/gamma`. Therefore

\[
\boxed{
g^{-2}\int(1-w)|f|^2d\nu_g
\le (1+E/\gamma)b_g[f].}
\tag{M8}
\]

For the exact rescaled literal variable `a_g=4(1-w)/g^2`, this is

\[
\boxed{\int a_g|f|^2d\nu_g
\le4(1+E/\gamma)b_g[f].}\tag{M9}
\]

These estimates cover every actual centered finite-energy source, including
sources concentrated on rare coarse fibers. They use the true compact
quantum measure, not its Gaussian approximation.

## 4. The precise remaining conditional-score inequality

Retain the actual score and the specified compact dilation of Q8:

\[
\sigma_g=(\partial_g\Psi_g+D\Psi_g/g)/\Psi_g,\quad
K_g(w)=\operatorname{Var}_{\mu_g}(\sigma_g\mid w),\quad
W_g(w)=g^{-2}\mathbb E_{\mu_g}(V\mid w).
\]

A sufficient additional actual-model estimate is

\[
\boxed{K_g(w)\le C_0+C_1W_g(w)}
\quad\nu_g\text{-a.e.},\quad 0<g<g_*,
\tag{M10, OPEN}
\]

with constants independent of g. The stronger inequality
`K_g(w)<=C0+C1(1-w)/g^2` would also suffice by M5. This is a conditional
score-versus-potential estimate; it is not supplied by the already bounded
average of K_g. The score definition includes the actual ground derivative,
Haar divergence of D, and all compact corrections.

If M10 is proved, M7 immediately gives, for every source f,

\[
\int K_g|f|^2d\nu_g
\le C_1b_g[f]+(C_0+C_1e_g)\|f\|^2.
\tag{M11}
\]

For centered f, this yields the uniform full-source estimate

\[
\boxed{\int K_g|f|^2d\nu_g
\le\left[C_1+\frac{C_0+C_1E}{\gamma}\right]b_g[f].}
\tag{M12, CONDITIONAL ON M10}
\]

This route uses the original positive quantum form to bound the source
moment; it does not require separately matching exponential upper and lower
estimates for the coarse marginal density.

## 5. Exact anchored Hardy constant, retaining the uncentered term

Let `m_g` be a median of the actual trace law. Take h on one half-interval,
with h(m_g)=0, and extend it by zero to the other half. Its support has
probability at most one half, so

\[
|\nu_g h|^2\le\tfrac12\|h\|^2,\qquad
\operatorname{Var}_{\nu_g}(h)\ge\tfrac12\|h\|^2.
\]

The physical gap applies to `h-nu_g h`; its energy is `b_g[h]`. Thus

\[
\|h\|^2\le2b_g[h]/\gamma.
\tag{M13}
\]

Applying M11, including its `e_g ||h||^2` term, proves

\[
\int K_g|h|^2d\nu_g
\le C_H b_g[h],\qquad
C_H=C_1+\frac{2(C_0+C_1E)}{\gamma}.
\tag{M14, CONDITIONAL ON M10}
\]

Write `v_g=g^2(1-w^2)rho_g(w)` as in W2 of
[quantile_source_weight.md](../../REPO/runs/recent_research_integration_2026-09-09/sources/w6_compact_continuation_20260909/quantile_source_weight.md).
For the right half let
`R(x)=integral_[m_g,x] dw/v_g(w)` and
`Q(x)=integral_[x,1] K_g dnu_g`. The admissible test
`h_t(x)=R(min(x,t))`, extended by zero to the left, has energy R(t)
and weighted norm at least `Q(t)R(t)^2`. Its constant tail is finite;
smooth form-core approximation handles its corner at t. M14 gives
`Q(t)R(t)<=C_H`. The identical left-half argument proves

\[
\boxed{\mathfrak B_g\le
C_1+\frac{2(C_0+C_1E)}{\gamma}.}
\tag{M15, CONDITIONAL ON M10}
\]

Here `mathfrak B_g` is precisely the maximum of the two scalar
tail-resistance suprema W4-W5. The factor two in M15 comes from the
half-source centering argument; it does not discard the vacuum-energy
term in M7. M15 supplies the uniform Hardy criterion once M10 is proved.

## 6. Established consequence and stopping point

M5 and M7-M9 are new actual compact-square inequalities derived here from
the existing operator and physical gap. They discharge the source
potential-moment part uniformly at small coupling. M10 remains the smallest
explicit additional score inequality supplied by this route. M11-M15 are
proved consequences of M10, not a proof of it.

The original Q10-Q14 controls the actual renormalized ground derivative in
global Hilbert/quantum energy norms and its averaged conditional variance.
It does not bound the conditional multiplier K_g by W_g. The local Morse
repair in `bg_analysis.md` also requires chart-complement and
conditional-mean control before it can address M10 on every coarse fiber.
No actual-model obstruction to M10 was proved in this bounded pass.

Every result here is for the fixed twelve-edge square. The factor four in
the telescoping argument counts its four faces; an enlarged loop changes
that count. The fixed-square E and gamma are not asserted uniform over
coupled growing grids. No continuum transport or full moving-source
operator derivative estimate is inferred from the source moment theorem.
