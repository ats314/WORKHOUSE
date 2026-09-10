# Actual compact-square conditional-score tail bound

10 September 2026. Standalone continuation; source files are unchanged.

## Target and present checkpoint

This note attacks the scalar Hardy tail-resistance constant in
`C:/WORKHOUSE/REPO/runs/recent_research_integration_2026-09-09/sources/w6_compact_continuation_20260909/quantile_source_weight.md`,
equations W4-W5. Denote that scalar by `H_g` here, to distinguish it from
the operator forcing also called `B_g` in `quantile_scale.md`, Q9.

For the actual normalized ground of the fixed twelve-edge compact square,

\[
\mathsf H_g=g^2T+g^{-2}V,\quad d\mu_g=\Psi_g^2dU,\quad
w=\tfrac12\operatorname{Tr}(U_2U_3),\quad d\nu_g=\rho_g(w)dw,
\]

the source energy and conditional score variance are

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

The uniform tail product is not already proved by these statements.
The ongoing calculation must use the actual marginal and score, including
rare coarse configurations. A global ground-norm estimate alone cannot
replace this task. A resulting first source derivative bound into L2
will also remain separate from the full energy-space operator derivatives
through order three required by the complete residual theorem.

## Sources inspected before deriving

- `quantile_source_weight.md`: W1-W8, sharpness, and Gaussian multiplier example.
- `quantile_scale.md`: exact moments Q1-Q5, full compact dilation Q8,
  actual renormalized derivative Q9-Q14.
- `compact_residual.md`: complete positive-reference transport and C7-C10
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
`../w6_square_block_20260909/source.md`, section 6. At coupling g the
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

`bg_gaussian_cutoff_check.py` passed four exact SymPy checks on this date:
the conditional variance coefficient, exact quantitative rare-tail product,
the asymptotic coefficient, and the actual compact endpoint coefficient.
`bg_gaussian_cutoff_checks.json` records this scope explicitly. The bump
construction, interval lower bounds, endpoint regularity and coordinate
repair are analytic arguments in this note; the script does not formalize
their integration or differential-geometric steps.

An independent review of the companion `residual_analysis.md`, R3-R12,
checked the ground-energy derivative identity including its third-order
normalization term and its energy-space generator/Leibniz constants. No
missing term was found. That companion supplies new actual untransported
derivative scaling; its remaining transport-energy estimate is not supplied
by the present H_g analysis.

A targeted primary-source literature search located Barry Simon's
1983 nondegenerate-minimum analysis and Bernard Helffer's WKB lecture
notes. These were not used as a proved pointwise conditional expansion for
the compact square: an eigenvalue/quasimode expansion is not automatically
the relative, parameter-differentiated conditional estimate needed in B6-B8.
The exact arguments B1-B5a do not rely on those literature results.

The supplied worktree note
`C:/WORKHOUSE/worktrees/w6-energy-form-20260910/docs/research/w6-subdivided-compact-transport-2026-09-10.md`
was read after discovery. It already removes the extra `c1<4` condition
by subdividing the complete compact-reference approximation, conditional on
the actual derivative scaling. It does not supply the missing H_g estimate.
