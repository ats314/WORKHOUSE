# W6 conditional transport: exact score, rare-fiber obstruction and synchronized repair

10 September 2026. Successor of the [M10 source-score target](w6-conditional-score-tail-control.md).

**Outcome.** The Q8 specification admits smooth compact radial transports for
which M10 is false in the actual four-face SU(2) ground law. This does not
refute M10 for every possible transport. An explicit synchronized choice
removes the identified normal drift; its full uniform M10 estimate remains
open. The actual counterexample uses a finite-flow argument and ordinary
relative one-well asymptotics, not differentiation of a formal WKB series.

The established source-potential estimates M7-M9 and the implications
M11-M15 retain their original scopes. None is withdrawn or re-proved as new.

## S1 Exact conditional score

Use the original twelve-edge square with four faces and

\[
 H_g=-\frac{g^2}{2}\sum_j E_j^2+g^{-2}V,\qquad
 V=4\left[4-\frac{\operatorname{tr}U_0}{2}
 -\frac{\operatorname{tr}U_1}{2}
 -\frac{\operatorname{tr}(U_2U_0^{-1})}{2}
 -\frac{\operatorname{tr}(U_3U_1^{-1})}{2}\right].
\]

Here the sum includes every original edge and all three Lie directions;
the [original geometry](../../runs/recent_research_integration_2026-09-09/sources/w6_square_block_20260909/geometry.md)
specifies its fields. In particular `0 <= V <= 32`. Let `Psi_g` be the
normalized positive actual ground. Put `Q=U2 U3`, `y=(U0,U1,U2)` and
`w=tr(Q)/2`. Product Haar is exactly `dy dQ` in these coordinates.

The [prior Q8 construction](../../runs/recent_research_integration_2026-09-09/sources/w6_compact_continuation_20260909/quantile_scale.md)
chooses radial vector fields on the four product factors. It requires
Euler behavior near the identity and zero near the antipode but does not
specify the four cutoff profiles or require synchronization. Write
`Z=Z_y+Z_Q`, with `Z_Q` independent of y, and `D=Z+(div Z)/2`.
For `U=cos(r)I+i sin(r)n.sigma`, a radial speed `z(r)` has Haar divergence

\[
 \operatorname{div}Z=z'(r)+2\cot(r)z(r).                 \tag{S1}
\]

The expression extends smoothly for the prescribed endpoint behaviors.
Define the actual conditional density and continuity residual

\[
 h_g(Q)=\int\Psi_g(y,Q)^2dy,\qquad p_g(y\mid Q)=\Psi_g(y,Q)^2/h_g(Q),
\]
\[
 r_g=\partial_gp_g+g^{-1}Z_Qp_g+g^{-1}\operatorname{div}_y(p_gZ_y).
\]

All quantities are smooth at positive g. Compact fiber integration gives
`integral r_g dy=0`. Substitution into the specified renormalized score gives

\[
 \boxed{2\bigl(\sigma_g-\mathbb E(\sigma_g\mid Q)\bigr)=r_g/p_g,
 \qquad K_g(Q)=\frac14\int\frac{r_g^2}{p_g}\,dy.}       \tag{S2}
\]

Indeed, twice the score is
`(partial_g+Z/g)log(h_g p_g)+(div Z)/g`. The terms containing only h_g
and the coarse divergence disappear under conditional centering; the
remaining expression is r_g/p_g and already has mean zero. This proves S2
with the conditional normalization, Haar divergence and coarse motion kept.

Simultaneous conjugation invariance of the ground and equivariance of Z
make both conditional score moments constant on the conjugacy class of Q.
The law of total variance therefore gives exactly `K_g(Q)=K_g(w)`.
Conditioning on full Q has not replaced the source or the variance in M10.

## S2 Exact constrained geometry

Let `theta=acos(w)`, `0<=theta<=pi`. The actual constrained potential is

\[
 \boxed{\min_{U_2U_3=Q}V=16[1-\cos(\theta/4)]=:v_*(\theta).} \tag{S3}
\]

For fixed U2 of angle a, quaternion scalar-product maximization gives
`max_U0 [tr(U0)/2+tr(U2 U0^-1)/2]=2 cos(a/2)`. Apply the same identity
to U1,U3, with b the angle of U3. The SU(2) geodesic triangle inequality
gives `a+b>=theta`. Concavity and monotonicity yield
`2cos(a/2)+2cos(b/2)<=4cos((a+b)/4)<=4cos(theta/4)`.
For regular Q, equality has the unique configuration

\[
 U_0=U_1=e^{i\theta n\cdot\sigma/4},\quad
 U_2=U_3=e^{i\theta n\cdot\sigma/2},\quad Q=e^{i\theta n\cdot\sigma}. \tag{S4}
\]

At `Q=-I` this configuration has the full two-sphere of axes n. In
particular S3 recovers the prior antipodal value `16-8 sqrt(2)`.

This configuration also minimizes the *Agmon action for the actual
electric metric*. Write `Gamma(f,f)=sum_j(E_j f)^2` and let G be its inverse
metric. The established original-edge identity is
`Gamma(w,w)=2(1-w^2)`, hence `Gamma(theta,theta)=2` on regular fibers.
Every curve c from the unique well consequently satisfies

\[
 \int\sqrt{2V(c)}\,|c'|_G
 \ \ge\int\sqrt{v_*(\theta(c))}\,|\theta(c)'|
 \ \ge I(\theta(c_{\rm end})),
\]
\[
 \boxed{I(\theta)=32\sqrt2[1-\cos(\theta/8)],\qquad
 I'(\theta)^2=v_*(\theta).}                            \tag{S5}
\]

The path S4 attains equality. At commuting configurations its longitudinal
cometric in angle coordinates is `C/4`, where C is the established four-loop
electric matrix. With `b=(0,0,1,1)`,
`(C/4)b=(1/2,1/2,1,1)` and the S4 velocity is half this gradient.
Its full squared metric speed is `1/2`; transverse derivatives of theta
vanish there. This verifies the sharp metric factor, not just a restricted
potential calculation. Equality in both bounds forces the minimizing
configuration S4 at a fixed regular Q. One may equivalently use the smooth
local Agmon phase near the nondegenerate well, which suffices below.

In Lie-vector convention `Q=exp(i q.sigma/2)`, the minimum graph in
`(log U0,log U1,log U2)` is

\[
 \boxed{m(q)=(q/4,q/4,q/2).}                            \tag{S6}
\]

For deviations `(a,b,c)` at fixed q, the known Gaussian phase has

\[
 S_2-\min S_2=\frac{|a+b|^2}{4}+\frac{|c|^2}{4}
                  +\frac{\sqrt6}{12}|a-b-c|^2.          \tag{S7}
\]

This is strictly positive in all nine conditional directions. Thus the
conditional Hessian B(q) of the smooth local Agmon phase stays positive
for sufficiently small q. The exact coefficient is
`m(q)^T B(0)m(q)=(6+sqrt(6))|q|^2/24`.

## S3 Actual conditional concentration

**Statement.** For each sufficiently small fixed nonzero q, the actual
conditional measures `p_g(y|Q)dy` tend weakly to the point mass at S6 as
`g -> 0`. The conditional normalization is essential: the fiber is rare.

The external analytic input is the scalar specialization of the local
one-well WKB comparison theorem: Klein and Rosenberger,
[*The Tunneling Effect for Schroedinger operators on a vector bundle*](https://arxiv.org/html/2005.13852#S6),
Hypotheses 1.1 and 6.1, Theorem 6.5, especially (6.9) and the spatial
derivative bootstrap immediately following its proof. It supplies weighted
comparison with the **actual Dirichlet eigenfunction**, rather than only
a formal quasimode. This classical theorem is an explicitly named input;
the finite script accompanying this note does not machine-prove it.

Here is its application and the passage to the actual compact ground.

1. Put `h=g^2` and `P_h=h H_g=h^2 T+V`. On the compact smooth manifold
   `SU(2)^4`, T is elliptic: the four non-tree horizontal edge fields alone
   span its tangent space. Its principal symbol is `Gamma/2`. Conjugation
   from Haar measure to the volume of that principal metric preserves
   scalar Laplace type and adds only smooth lower-order terms in T.
   Those terms are multiplied by h squared; none changes the eikonal phase.
2. V has one zero, all four U_i equal to I, and its Hessian is positive
   (the established M matrix). The oscillator ground is simple. Apply the
   comparison theorem with ambient manifold a sufficiently small open
   conjugation-invariant well chart, and with a smooth Dirichlet domain
   compactly contained in that chart. In the single-well specialization
   the interwell separation in Hypothesis 3.2 is infinite; choose any small
   admissible Agmon ball inside the Dirichlet domain. The local outgoing
   Agmon graph and a backward-invariant smaller sublevel satisfy Hypothesis
   6.1. Restricting the ambient chart excludes returning global trajectories;
   we do not assert that the full unstable manifold on the original compact
   space has no other branches above the chart. No smooth phase at the
   antipode or global noncaustic hypothesis is used.
3. The comparison theorem on this Dirichlet neighborhood gives its true
   positive ground in the form `h^-3 exp(-S/h)(a0+O(sqrt(h)))` on a smaller
   neighborhood, with positive smooth a0 there and relative spatial
   remainder estimates. The phase S is the actual Agmon distance locally,
   has the Gaussian Hessian and the constrained minimum S5-S6.
4. First identify its eigenvalue with the actual compact ground branch.
   If xi is a physical cutoff equal to one near the well and supported in
   the Dirichlet domain, the exact ground-transform Rayleigh identity is
   `R_P[xi Psi_g]=h e_g+(h^2/2) integral Gamma(xi,xi)Psi_g^2/||xi Psi_g||^2`.
   Q5 makes the correction exponentially small. Dirichlet min-max gives
   `h e_g<=lambda_D<=R_P[xi Psi_g]`. Thus lambda_D is exponentially close
   to the compact ground energy, and the existing physical gap separates
   it from all other physical eigenvalues by at least `h gamma/2`.
   Now cut off the **exact Dirichlet ground** on a fixed positive-action
   shell. Its residual is exponentially small by the Agmon energy estimate;
   commutator and fixed Sobolev derivatives lose only powers of h. The
   cutoff and ground are physical by conjugation invariance and positive
   simplicity. Spectral projection, positive sign and the identified gap
   give an exponentially small L2 difference from the actual ground.
   Local elliptic estimates upgrade the difference to C0 with polynomial
   h losses. Consequently both grounds have the same relative expansion
   where S is less than a sufficiently small fixed exponent. An algebraic
   **unweighted** quasimode remainder would not justify this step; cutting
   off an exact Dirichlet eigenfunction avoids that problem.
5. Outside a fixed smaller well neighborhood, the previously proved quantum
   exponential moment Q5 and cutoff elliptic estimates bound the actual
   ground pointwise by `h^-N exp(-c/h)` for some c>0. Choose |q| sufficiently
   small that `I(|q|/2)<c/2` and also below the comparison exponent in step 4.
   The local conditional Laplace integral has leading normalization
   `h^-3/2 exp(-2I/h)` times a positive constant. Outside the local chart the
   exponential gap survives this normalization. Inside, S7 and uniqueness
   yield concentration at m(q), by the ordinary finite-dimensional Laplace
   estimate. This proves the statement for the **full actual fiber**.

No derivative in g of a WKB remainder is used. All choices of q here are
fixed before sending g to zero; this is not the ordinary `q=O(g)` oscillator
scaling. This distinction is what makes the result useful for rare fibers.

## S4 A transport obstruction

**Theorem.** There is a smooth, complete, conjugation-equivariant radial
product field satisfying every Q8 requirement for which no finite
nonnegative constants C0,C1 can satisfy M10 on a small interval `0<g<g_*`.
This is an existence counterexample within Q8, not a refutation of every
possible synchronized choice.

Choose r0>0 sufficiently small for S3 and a smooth profile chi with
`chi(r)=1` for `r<=3r0/5` and `chi(r)=0` for `r>=4r0/5`.
On **each** product factor, in Lie-vector logarithms x, use
`Z_factor=chi(|x|) x.partial_x`, extended by zero outside the identity
chart. This is smooth, physical and complete, agrees with Euler near the
well, and vanishes near the antipode. Its Q flow is radial and normalizes
the entire trace algebra, as required by Q8.

Fix |q|=r0. On a neighborhood of the conditional minimum,

\[
 Z_Q=0,\qquad Z_y=y,\qquad Z_y(m(q))=m(q)\ne0.         \tag{S8}
\]

Let `v_g(y)=Psi_g(y,Q)/sqrt(h_g(Q))`, a unit vector in the fixed compact
fiber Haar space, and let `D_y=Z_y+(div_y Z_y)/2`. Since Z_Q vanishes on a
neighborhood of this Q, S2 is equivalently

\[
 v'_g+D_yv_g/g=(\sigma_g-\mathbb E(\sigma_g\mid Q))v_g,
 \qquad\|v'_g+D_yv_g/g\|^2=K_g(Q).                    \tag{S9}
\]

There is no factor two in this normalized-vector speed. Let
`U_t=exp(t D_y)`. Its half-density pullback is
`U_t f=Jac(Phi_t)^(1/2) f o Phi_t`, so it transports concentration from m
to `Phi_-t(m)`. For every sufficiently small fixed t>0 those points differ.
By S3 the endpoint vectors `v_g` and `U_t v_(exp(t)g)` therefore satisfy

\[
 \langle v_g,U_t v_{e^tg}\rangle\longrightarrow0,
 \qquad \|v_g-U_tv_{e^tg}\|\longrightarrow\sqrt2.       \tag{S10}
\]

To check the overlap assertion, split its integral into a neighborhood of m
disjoint from `Phi_-t(m)` and its complement. Cauchy-Schwarz bounds it by
two square roots of probabilities tending to zero.

The curve `s -> U_log(s/g) v_s`, `g<=s<=exp(t)g`, has speed `sqrt(K_s)`.
If M10 held, `V<=32` would imply `K_s<=C0+32 C1/s^2`. Hence

\[
 \|v_g-U_tv_{e^tg}\|
 \le\int_g^{e^tg}\sqrt{K_s}\,ds
 \le\sqrt{C_0}(e^t-1)g+\sqrt{32C_1}\,t.              \tag{S11}
\]

Choose t>0 so small that the second term is strictly less than sqrt(2),
then let g tend to zero. Equations S10-S11 contradict each other. This
proves the theorem without asserting an unproved score power law.
For each positive g both conditional moments are continuous at regular w;
an almost-everywhere M10 therefore extends to this chosen w. There is no
exceptional-fiber loophole.

The earlier bounded global score moment Q14 remains valid: it averages
against an exponentially small marginal on these rare fibers. This theorem
does not retract that averaged bound or the earlier fixed-block gap.

For interpretation only, a differentiated relative WKB/Laplace hypothesis
would sharpen this example to `g^4 K_g(q)->m(q)^T B(q)m(q)/2`, whose
quadratic small-q coefficient is `(6+sqrt(6))|q|^2/48`. That rate is a
conditional refinement, not used or claimed as an actual-model theorem here.

## S5 Synchronized tangency

For a projectable Z and a smooth phase with minimum graph m(q), differentiate
`S_y(m(q),q)=0`. The exact normal phase derivative is

\[
 \partial_y(2S-ZS)|_{m(q)}
 =-B(q)\,[Z_y(m(q),q)-Dm(q)Z_q(q)].                    \tag{S12}
\]

This isolates the failure in S8. In angle convention `U=exp(i r n.sigma)`,
choose one smooth cutoff chi, constant one near zero and identically zero
for `r>=theta_a<pi`. Extend it by zero beyond its support and choose

\[
 \boxed{z_0(r)=z_1(r)=r\chi(4r),\quad
 z_2(r)=r\chi(2r),\quad z_Q(r)=r\chi(r).}              \tag{S13}
\]

These radial fields satisfy Q8 and keep the Haar divergence S1. At S4 their
speeds are respectively `theta chi(theta)/4`, the same, half, and the full
`theta chi(theta)`. They preserve the whole conditional minimum curve,
so the bracket and the dangerous linear phase term S12 vanish exactly.
This is an explicit new selection/repair of the previously unspecified
cutoffs, not an identification with the counterexample field.

One identical radial speed on all four factors cannot satisfy this tangency
for every theta: `z(theta)=4z(theta/4)` iterated into the Euler region forces
`z(theta)=theta` for every theta<pi, incompatible with the antipodal cutoff.
This algebraic fact alone is not a proof of failure for every identical
cutoff: the actual counterexample S4 uses the local concentration regime.

## S6 Remaining all-fiber estimate

The synchronized **actual** M10 target is still open. Tangency is necessary
for the identified mechanism but is not the entire score estimate. A useful
precise sufficient implication, proved here, is the following.

On a tube about S6 write the true ground as
`Psi_g=g^-6 A_g(q,eta) exp(-S(q,eta)/g^2)`, with the actual Haar correction
retained. This defines A_g; it does not automatically bound it. Assume the
conditional tube moments satisfy `E|eta|^(2j)<=c_(2j)g^(2j)` for j=1,2,3,
and the fast derivative of
`a_g=partial_g log A_g+g^-1[Z log A_g+(div Z)/2-6]`
is bounded by `c_a/g`. Uniform differentiated relative-amplitude control,
not just the undifferentiated comparison in S3, is needed for this premise.

Let `F=2S-ZS`. The synchronized tangency and the oscillator quadratic jet
give, near the well,
`|F(q,eta)-F(q,0)|<=c_F(|q||eta|^2+|eta|^3)`.
Taylor expansion in eta proves this: its linear term vanishes by S12,
its fast Hessian at q=0 vanishes by Euler cancellation, and its third fast
derivatives are bounded. A compact source annulus within a smooth phase
tube can be included if its phase derivatives and tube bounds are uniform,
by enlarging the constant. Set `beta_g(q)=F(q,0)/g^3+a_g(q,0)`. Then

\[
 \mathbb E_{\rm tube}|\sigma_g-\beta_g|^2
 \le4c_F^2(c_4|q|^2/g^2+c_6)+2c_a^2c_2.              \tag{S14}
\]

Here q uses Lie-vector convention, so `|q|=2theta`. Since
`v_*(theta)>=2theta^2/pi^2`, the q term is bounded by
`2 pi^2 g^-2 E(V|Q)`. The full conditional variance obeys, with p the
actual conditional tube probability,

\[
 K_g(Q)\le p\,\mathbb E_{\rm tube}|\sigma_g-\beta_g|^2
       +\mathbb E[1_{\rm outside}|\sigma_g-\beta_g|^2\mid Q]. \tag{S15}
\]

The common reference beta retains conditional-mean differences; exponentially
small unconditioned mass does not replace the second term.

For a fixed `theta_b>theta_a`, Z vanishes on a uniform tube about the
minimizing configurations with `theta>=theta_b`. On that tube it suffices
to bound the conditional ordinary-score variance by `C/g^2`, because
v_*(theta) is bounded below; S15 must still bound the complement with the
full transported score and retain the conditional-mean difference.
The antipodal limiting minimizers form a
two-sphere: a uniform positive nine-dimensional conditional Hessian must not
be assumed. A degeneration-uniform actual score estimate and its conditional
complement bound remain to be proved.

**Consequence.** The arbitrary-cutoff route is ruled out by an actual-model
counterexample; the exact center geometry supplies a synchronized transport
and a concrete remaining tail/amplitude problem. M11-M15 become applicable
only after M10 for that fully specified transport is proved. Complete R10
energy jets, interacting-volume constants and continuum transport remain
separate obligations.

## Verification and attribution

The square geometry, source-potential estimates, quantum moment bounds and
physical gap are prior project results. This note adds S2-S15 with the scopes
above and uses the explicitly cited one-well comparison theorem in S3.
The companion [exact check](../../scripts/check_m10_transport.py) verifies
finite symbolic identities: metric calibration, Gaussian conditional
Hessian/coefficient, Haar divergence and score normalization arithmetic.
It does not certify the external analytic theorem, compact elliptic
estimates, weak-concentration limit or the complete all-fiber M10 claim.
