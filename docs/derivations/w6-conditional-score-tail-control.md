# Actual compact-square conditional-score tail bound

10 September 2026. Portable integrated successor of the [standalone analysis](../../runs/w6_bg_budget_2026-09-10/sources/campaign/bg_analysis.md). The [intake manifest](../../runs/w6_bg_budget_2026-09-10/source_manifest.json) preserves its original path and bytes. The endpoint, Gaussian inference obstruction and local repair below are new campaign arguments; the source criterion, actual-ground estimates and subdivision theorem are prior project results.

## Target and present checkpoint

This note attacks the scalar Hardy tail-resistance constant in
[the prior source-energy criterion](../../runs/recent_research_integration_2026-09-09/sources/w6_compact_continuation_20260909/quantile_source_weight.md),
equations W4-W5. Denote that scalar by `H_g` here, to distinguish it from
the operator forcing also called `B_g` in `quantile_scale.md`, Q9.

For the actual normalized ground of the fixed twelve-edge compact square,

\[
\mathsf H_g=g^2T+g^{-2}V,\quad d\mu_g=\Psi_g^2dU,\quad
w=\tfrac12\operatorname{Tr}(U_2U_3),\quad d\nu_g=\rho_g(w)dw,
\]


Here T includes one half of the original-edge T_op used in the companion note, so both notes use the same compact Hamiltonian normalization.

The source energy and conditional score variance are

\[
b_g[f]=g^2\int(1-w^2)|f'(w)|^2d\nu_g,
\quad K_g(w)=\operatorname{Var}_{\mu_g}\!\left(
\frac{\partial_g\Psi_g+D\Psi_g/g}{\Psi_g}\,\middle|\,w\right).
\]

The target is

\[
\sup_{0<g<g_*}\max\left\{
\sup_{m_g<x<1}\left(\int_x^1K_gd\nu_g\right)
 \left(\int_{m_g}^x\frac{dw}{g^2(1-w^2)\rho_g(w)}\right),
\sup_{-1<x<m_g}\left(\int_{-1}^xK_gd\nu_g\right)
 \left(\int_x^{m_g}\frac{dw}{g^2(1-w^2)\rho_g(w)}\right)
\right\}<\infty.
\]

The existing source proves the actual fixed-square quantum gap, bounded
mean conditional variance, and the sufficient all-source inequality

\[
\int K_g|f-\nu_gf|^2d\nu_g
\le(8H_g+4\overline K_g/\gamma)b_g[f].
\]

Section 6 additionally proves a uniform actual all-source potential moment, and reduces the remaining Hardy bound to the explicit score-versus-conditional-potential estimate M10. The uniform tail product itself is not already proved by these statements.
The ongoing calculation must use the actual marginal and score, including
rare coarse configurations. A global ground-norm estimate alone cannot
replace this task. A resulting first source derivative bound into L2
will also remain separate from the full energy-space operator derivatives
through order three required by the complete residual theorem.

## Sources inspected before deriving

- [quantile_source_weight.md](../../runs/recent_research_integration_2026-09-09/sources/w6_compact_continuation_20260909/quantile_source_weight.md): W1-W8, sharpness, and Gaussian multiplier example.
- [quantile_scale.md](../../runs/recent_research_integration_2026-09-09/sources/w6_compact_continuation_20260909/quantile_scale.md): exact moments Q1-Q5, full compact dilation Q8,
  actual renormalized derivative Q9-Q14.
- [compact_residual.md](../../runs/recent_research_integration_2026-09-09/sources/w6_compact_continuation_20260909/compact_residual.md): complete positive-reference transport and C7-C10
  spatial conditional moments, derivative constants and complete residual.
- The existing workspace and repository exact-name search returned the
  September 9 criterion and its integration records, with no located
  earlier uniform `H_g` closure.

## 1. What the actual compact endpoints do prove

For every fixed positive coupling the scalar `H_g` is finite. This is an
actual compact-square statement, not a Gaussian assertion. In product
coordinates `(U0,U1,U2,Q=U2U3)`, positivity and smoothness of the true
ground on the compact group imply smooth positive coarse density factor
`h_g(Q)=integral Psi_g^2` and a smooth conditional second moment for the
renormalized score. Physical invariance makes these class functions of Q.
They therefore have smooth expansions in `w=Tr(Q)/2` at both endpoints.
Writing `c=2/pi`,

\[
\rho_g(w)=c\,h_g(w)\sqrt{1-w^2},\qquad h_g(\pm1)>0,
\quad K_g\in C^\infty([-1,1]).
\]

For `s=1-x` and fixed g, direct integration gives

\[
\int_x^1K_g\rho_g\,dw
=\tfrac23c h_g(1)\sqrt2 K_g(1)s^{3/2}+o(s^{3/2}),
\]
\[
\int_{m_g}^x\frac{dw}{g^2(1-w^2)\rho_g(w)}
=\frac{s^{-1/2}}{g^2 c h_g(1)\sqrt2}+O_g(1).
\]

The tail product consequently is

\[
\frac{2K_g(1)}{3g^2}(1-x)+o_g(1-x)\longrightarrow0.
\tag{B1}
\]

At the other endpoint it is `2 K_g(-1)(1+x)/(3g^2)+o_g(1+x)`.
Interior continuity, positivity of the density and finiteness of the
interior median resistance complete the proof. All quantities depend
continuously on g on a closed interval `[a,b]` with `a>0`; the same argument
with compact-uniform smooth bounds proves `sup_[a,b] H_g<infinity`.

This discharges endpoint integrability and every closed positive-coupling
interval. It does not discharge the moving-boundary-layer limit `g -> 0`.

## 2. Exact obstruction to inferring uniformity from averaged ground control

There is a precise source-preserving dilation sensitivity already in the
square's actual Gaussian reference. This does not claim a counterexample
for the full compact Hamiltonian or for a suitably repaired dilation.

Use the independently Gaussian physical modes `(q,u,s,v)` of
[the square Gaussian source derivation](../../runs/recent_research_integration_2026-09-09/sources/w6_square_block_20260909/source.md), section 6. At coupling g the
variance of each component of u is `g^2/2`; for `a=|q|^2`, the coarse law is
Gamma(shape `3/2`, scale `theta g^2`), `theta=2 sqrt(2)`, and

\[
b_g^{\rm Gauss}[f]=8g^2\int_0^\infty a|f'(a)|^2d\nu_g(a).
\tag{B2}
\]

Let `D0` be the exact twelve-dimensional skew dilation. For its normalized
Gaussian ground, `(partial_g+D0/g)Psi_g=0`. Choose a smooth bump chi of a
supported away from zero and equal to one in an interval containing a fixed
number `A>0`. The complete vector field

\[
Y=\chi(|q|^2)q\cdot\nabla_u,\qquad D=D0+Y
\tag{B3}
\]

has zero divergence in its additional term, commutes with simultaneous
rotations and preserves the full q source algebra. It agrees with D0 on
an open neighborhood of the well. Its flow is complete. The renormalized
conditional score is exactly

\[
\sigma_g=-\frac{\chi(a)q\cdot u}{g^3},\qquad
K_g(a)=\frac{\chi(a)^2a}{2g^4}.
\tag{B4}
\]

Its average tends to zero faster than every power of g, because the bump
is supported on a fixed rare coarse annulus. The same is true of the
ground-weighted quantum energy of the modified renormalized derivative:
each derivative adds only a fixed polynomial in `g^-1` and Gaussian
coordinates on that annulus. Thus the global Q12/Q14-type bounds survive,
as does every near-well asymptotic coefficient.

Nevertheless the actual radial Hardy tail product at A diverges. If
`rho_g(a)=c_g a^(1/2) exp(-a/(theta g^2))`, Laplace integration at the
endpoint A gives

\[
\int_A^\infty K_g\rho_g\,da
\sim\theta g^2 K_g(A)\rho_g(A),\qquad
\int_{m_g}^{A}\frac{da}{8g^2a\rho_g(a)}
\sim\frac{\theta}{8A\rho_g(A)}.
\]

Here the first formula holds because chi is one in a neighborhood of A;
the fixed upper cutoff contributes an exponentially smaller term. The
second holds because `m_g` is `g^2` times the fixed Gamma median. Multiplying,

\[
H_g\ge\frac{\theta^2}{16g^2}(1+o(1))
=\frac1{2g^2}(1+o(1)).
\tag{B5}
\]

There is an elementary quantitative version that needs no asymptotic
theorem. Put `h=theta g^2`, and assume chi is one on `[A,A+delta]`.
For `h<=min(A/4,delta)`, Markov's inequality puts the median below
`3h<=A-h`, since the Gamma mean is `3h/2`. Integrate the first tail
only over `[A,A+h]` and the resistance only over `[A-h,A]`. Since
`rho_g=c_g a^(1/2)e^(-a/h)`,

\[
\int_A^{A+h}K_g\rho_g\,da
\ge\frac{c_g h A^{3/2}}{2g^4}e^{-A/h-1},\qquad
\int_{A-h}^{A}\frac{da}{8g^2a\rho_g(a)}
\ge\frac{h}{8g^2c_g A^{3/2}}e^{A/h-1}.
\]

Consequently the exact bound is

\[
\boxed{H_g\ge\frac{e^{-2}}{2g^2}}
\quad\text{if}\quad\theta g^2\le\min(A/4,\delta).
\tag{B5a}
\]

Every median and normalization constant has been retained. This proves
divergence without numerical quadrature or a formal expansion.

This proves an actual limitation of the inference, with the original
square reference's normalizations: bounded averaged score and its quantum
energy, even together with all near-well jets, do not control the all-source
Hardy quantity. The rare-source tail must be estimated, and the global
choice of source-preserving dilation matters.

The source Q8 only fixes its compact dilation near the well and near the
antipode. B3 is not the identical product-radial choice written there, so
B5 does not establish failure of that particular compact construction.
It establishes that source-algebra preservation and near-well correctness
alone cannot justify changing global dilation choices without a new bound.

## 3. A concrete phase-adapted repair of the dangerous direction

This lemma gives a constructive repair target, with its still-unproved
actual-model inputs explicit. It is not a declaration that the actual
compact-square phase estimates have already been obtained.

Suppose a smooth, g-independent local ground phase S in coordinates `(q,y)`
has, for each coarse q, a unique nondegenerate conditional minimum `y_*(q)`.
Choose a g-independent parametric Morse coordinate `eta=Phi(q,y)`; it gives

\[
S(q,y)=I(q)+\tfrac12|\eta|^2,\qquad \Phi(q,y_*(q))=0.
\tag{B6}
\]

Choose the coarse radial velocity z(q), and define a full source-preserving
vector field by the explicit coordinate formula

\[
Z_q=z(q),\qquad
Z_y=(D_y\Phi)^{-1}\big(\Phi-D_q\Phi\,z(q)\big).
\tag{B7}
\]

It sends `eta` to `eta`, is tangent to the conditional minimizer section,
and obeys

\[
ZS=z\cdot\nabla I+|\eta|^2,\qquad
2S-ZS=2I-z\cdot\nabla I.
\tag{B8}
\]

Thus the entire `g^-3` contribution to the renormalized score of
`Psi_g=A_g exp(-S/g^2)` is a function of the retained variable. Conditional
centering removes it exactly. This directly repairs the g^-4 variance
mechanism in B3-B5; it does not try to bound that direction by a global
ground average.

More precisely, in half-density coordinates, first restrict to the
normalized conditional law on a fixed chart where B6 holds. Denote its
variance by `Var_chart` and its score variance by `K_g^chart(q)`. Suppose
these chart-restricted conditional laws have a Poincare bound
`Var_chart(F|q)<=C g^2 E_chart[|partial_eta F|^2|q]`, and the eta derivatives
of the amplitude contribution
`r_g=partial_g log A_g+g^-1 Z log A_g` are bounded by `C'/g`.
The divergence correction is included in the half-density amplitude;
its q-only part has zero conditional variance. Equations B6-B8 then prove
`K_g^chart(q)<=C(C')^2`, uniformly in g. The phase, coordinate change and
chart are g-independent here; a moving phase or chart would generate
additional parameter derivatives which must be included.

This is a bound on the normalized chart-restricted variance. It controls
the full `K_g(q)` only if the chart covers the full conditional support,
or if the complementary-tail variance and the difference of conditional
means are also controlled. A local Morse chart does not by itself cover
the whole compact fiber. This is a direct proved implication with a
specific vector field, not an assumption that the desired whole-fiber
variance bound holds.

Multiplying Z by a cutoff depending only on q preserves its tangency at
the conditional minimum. Where that cutoff differs from one, the remaining
quadratic fast phase contributes chart-restricted variance of order `g^-2`,
rather than `g^-4`, provided explicitly that
`Var_chart(|eta|^2|q)<=C_2 g^4`. For example the preceding conditional
Poincare estimate and `E_chart(|eta|^2|q)<=C_3 g^2` imply this fourth-order
variance bound by differentiating `|eta|^2`. Matching it to zero away from
the well is therefore structurally preferable to an arbitrary product-radial
cutoff. A uniform global Hardy estimate must still control chart-complement
tails, glue conditional means and variances, and compare the resulting
whole-fiber variance with the actual coarse resistance; it does not follow
from this local construction alone.

## 4. Current mathematical stopping point

The actual square's B1 endpoint theorem is proved above. The exact Gaussian
obstruction B2-B5 and the constructive phase-tangent repair B6-B8 are also
derived here. No uniform all-source compact-square H_g estimate is claimed.
To prove it by this repair one must construct the actual conditional phase
and amplitude bounds, show the corrected vector field has the stated global
smooth equivariance/source properties, and control the rare coarse fibers
including any conditional minimizer degeneracies. Those inputs are not
contained in the existing global quantum moment and first-jet bounds.

The existing uniform Gaussian grid floor is separate from all of these
fixed-square estimates. No interacting growing-grid floor or continuum
transport is inferred here.

## 5. Verification and precise attribution

[bg_gaussian_cutoff_check.py](../../runs/w6_bg_budget_2026-09-10/sources/campaign/bg_gaussian_cutoff_check.py) passed four exact SymPy checks on this date:
the conditional variance coefficient, exact quantitative rare-tail product,
the asymptotic coefficient, and the actual compact endpoint coefficient.
[bg_gaussian_cutoff_checks.json](../../runs/w6_bg_budget_2026-09-10/sources/campaign/bg_gaussian_cutoff_checks.json) records this scope explicitly. The bump
construction, interval lower bounds, endpoint regularity and coordinate
repair are analytic arguments in this note; the script does not formalize
their integration or differential-geometric steps.

An independent review of the companion [the ground-jet and transport-budget companion](w6-ground-jets-and-transport-budget.md), R3-R12,
checked the ground-energy derivative identity including its third-order
normalization term and its energy-space generator/Leibniz constants. No
missing term was found. That companion supplies new actual untransported
derivative scaling; its remaining transport-energy estimate is not supplied
by the present H_g analysis.

The supplied worktree note
[the preserved prior subdivision note](../../runs/w6_bg_budget_2026-09-10/sources/prior_subdivision/docs/research/w6-subdivided-compact-transport-2026-09-10.md)
was read after discovery. It already removes the extra `c1<4` condition
by subdividing the complete compact-reference approximation, conditional on
the actual derivative scaling. It does not supply the missing H_g estimate.

The uncited external-literature search paragraph in the received note was not a proof input and is omitted from this integrated successor; its exact text remains in the preserved source.

## 6. Uniform actual source potential moment and sharper score criterion

This additional new actual theorem is preserved in [actual_potential_moment.md](../../runs/w6_bg_budget_2026-09-10/sources/campaign/actual_potential_moment.md). Its source potential-moment conclusion is uniform at small coupling on the fixed square; its score-to-potential hypothesis M10 remains open.

### M.1. Exact original operator and source normalization

Use the original-edge convention of
[geometry.md](../../runs/recent_research_integration_2026-09-09/sources/w6_square_block_20260909/geometry.md),
its exact tree geometry and S3-S4, and
[quantile_scale.md](../../runs/recent_research_integration_2026-09-09/sources/w6_compact_continuation_20260909/quantile_scale.md),
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
[compact_residual.md](../../runs/recent_research_integration_2026-09-09/sources/w6_compact_continuation_20260909/compact_residual.md).

### M.2. Global noncommuting holonomy inequality

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

### M.3. Uniform actual all-source potential moment

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

### M.4. The precise remaining conditional-score inequality

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

with finite nonnegative constants `C0,C1>=0` independent of g. The stronger inequality
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

### M.5. Exact anchored Hardy constant, retaining the uncentered term

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
[quantile_source_weight.md](../../runs/recent_research_integration_2026-09-09/sources/w6_compact_continuation_20260909/quantile_source_weight.md).
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

### M.6. Established consequence and stopping point

M5 and M7-M9 are new actual compact-square inequalities derived here from
the existing operator and physical gap. They discharge the source
potential-moment part uniformly at small coupling. M10 remains the smallest
explicit additional score inequality supplied by this route. M11-M15 are
proved consequences of M10, not a proof of it.

The original Q10-Q14 controls the actual renormalized ground derivative in
global Hilbert/quantum energy norms and its averaged conditional variance.
It does not bound the conditional multiplier K_g by W_g. The local Morse
repair in the phase-adapted analysis in section 3 above also requires chart-complement and
conditional-mean control before it can address M10 on every coarse fiber.
No actual-model obstruction to M10 was proved in this bounded pass.

Every result here is for the fixed twelve-edge square. The factor four in
the telescoping argument counts its four faces; an enlarged loop changes
that count. The fixed-square E and gamma are not asserted uniform over
coupled growing grids. No continuum transport or full moving-source
operator derivative estimate is inferred from the source moment theorem.

The [five exact source-moment controls](../../runs/w6_bg_budget_2026-09-10/sources/campaign/bg_actual_potential_check.py) and their [record](../../runs/w6_bg_budget_2026-09-10/sources/campaign/bg_actual_potential_checks.json) verify two SU(2) word/norm examples, the eight-edge normalization, and the centered/anchored budget constants. The general holonomy inequality and actual source theorem remain analytic proofs. Independent review checked M2-M15, including the nonnegative score constants and the uncentered vacuum-energy term.
