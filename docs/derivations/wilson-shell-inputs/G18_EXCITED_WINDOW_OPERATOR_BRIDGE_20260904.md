# From a source-visible window to operator-level isolation

WORKHOUSE continuation. Base notes: 4 September 2026.
Repository reference read in this session: `d2f46c586d76d000c07369c6e83ae218bf897734`.
No remote changes. No native G18/G19 status changes.

## 0. What is established here

This note takes the calibrated Wilson free kinetic window from
`UNIFORM_WILSON_WINDOW.md` as a premise, and retains the ACTUAL positive
Wilson transfer rather than replacing its logarithm by an auxiliary Hamiltonian.

The new results are:

1. The time block that maximizes the separation guaranteed by the physical
   free-window theorem is explicit. At its ideal duration, the shell and the
   upper bound for the rest of the odd transfer spectrum are `(4/5)^4` and
   `(4/5)^5`. Their difference is `256/3125`. Temporal rounding retains an
   explicit common lower bound `1024/15625`.
2. At each fixed finite spatial volume, the actual, untruncated Wilson transfer
   has an isolated complete plaquette shell and an invertible literal-source
   frame for an explicit, temporal-mesh-uniform small coupling interval.
   The interval shrinks with volume and is not a thermodynamic theorem.
3. An explicit local vacuum rotation makes the FIRST derivative of the actual
   normalized block transfer bounded in full Hilbert-space operator norm,
   independently of volume and of the representation cutoff (there is none).
4. A general all-orders theorem converts a norm on locally vacuum-annihilating
   transfer activities into a full Hilbert-space perturbation bound. It
   includes every input state, not just the states detected by three sources.
   Constructing and bounding those activities for the fully dressed Wilson
   operator remains open.
5. A source/complement criterion proves isolation AND completeness when its
   full-complement upper bound is available. An exact moment identity measures
   leakage out of the source span, and an exact Schur complement retains its
   propagation through the remaining excitation space.

The existing source-correlation results are not reinterpreted as a proof of
excited-band isolation. The full thermodynamic Wilson shell, its sharp
spatially weighted spectral projection, and its complete source frame remain
unproved in this continuation. The new numerical tests are finite-model
checks, not interval certificates for the untruncated lattice.

## 1. Keep the two time scales separate

Let

\[
 \gamma=C_F/2,\quad E_s=4\gamma=2C_F,\quad
 T_{\epsilon,L}(u)=e^{\tau uV_L/2}e^{-\tau K_{\epsilon,L}}e^{\tau uV_L/2},
 \qquad \tau=\tau_F(\epsilon).
\]

The previous free theorem gives, in the neutral physical charge-odd space,

\[
 K_{\epsilon,L}P_0=4\gamma P_0,\qquad
 K_{\epsilon,L}|_{P_0^\perp}\ge5\gamma,
 \qquad \operatorname{rank}P_0=3L^3.
\]

The vacuum is absent from this odd space. On the full kinematic space the
one-link gap is exactly gamma. These statements hold for sufficiently small
epsilon uniformly in periodic L >= 3. The epsilon threshold remains
existential, inherited from the all-representation kinetic estimate.

The long block used in the previous vacuum expansion makes its one-link
kernel nearly Haar. Its spectral projectors and its Perron vector are the
same as those of every other positive integer power of T. Thus there is no
reason to use that long block in the excited spectral estimate.

### Proposition 1: spectrally optimal block

A physical-time block of duration s has shell eigenvalue
`c(s)=exp(-4 gamma s)` and an upper bound `d(s)=exp(-5 gamma s)` on the
remaining odd spectrum. The guaranteed separation

\[
 g(s)=e^{-4\gamma s}(1-e^{-\gamma s})
\]

is maximal at

\[
 \boxed{s_{\rm sp}=\gamma^{-1}\log(5/4).}
\]

At this time,

\[
 \delta=e^{-\gamma s_{\rm sp}}=4/5,\qquad
 c=256/625,\qquad d=1024/3125,\qquad
 \boxed{g=256/3125.}
\]

This optimizes the separation guaranteed by the WINDOW LOWER BOUND. It does
not assert that an eigenvalue at `5 gamma` is attained in the physical sector.

Proof: set x = exp(-gamma s). Then g = x^4(1-x), whose derivative in x is
x^3(4-5x). Its unique interior maximum on [0,1] is x=4/5.

For a genuine integer block use

\[
 m_\epsilon=\lceil s_{\rm sp}/\tau\rceil,\qquad
 s_\epsilon=m_\epsilon\tau.
\]

Require `tau <= tau_0 <= s_sp/4`. Then

\[
 s_{\rm sp}\le s_\epsilon\le s_{\rm sp}+\tau_0,
 \qquad \delta_\epsilon=e^{-\gamma s_\epsilon}\le4/5,
\]

and

\[
 \boxed{g(s_\epsilon)\ge g_*:=1024/15625.}
\]

Indeed the first exponential in g loses at most a factor
`exp(-4 gamma tau_0) >= 4/5`, while the second factor increases. The shell
itself stays at least `(4/5)^5` away from zero.

For SU(3), gamma=2/3 and
`s_sp=(3/2) log(5/4)`, approximately 0.334715 in electric time units.
This is a temporal analysis scale, not a gauge coupling or physical
anisotropy calibration.

## 2. A cutoff-free finite-volume theorem for the actual transfer

Put P = 3L^3 (the number of spatial plaquettes), J=2N,
`s_1=s_sp+tau_0`, and `g_v=1/5`. Let B(u)=T(u)^m and B_0=exp(-s K).
All factors are bounded except K, which enters only through contraction
semigroups. Expanding the magnetic factors and telescoping the kinetic
products gives, for complex u,

\[
 \boxed{\|B(u)-B_0\|\le r(u):=e^{s_1JP|u|}-1.}
 \tag{1}
\]

This is uniform in epsilon on the chosen mesh interval and uses no
representation cutoff. It is extensive in P.

Define

\[
 r_L=\min\left\{g_*/100,\ g_v/(64N\sqrt P),\ 1/5\right\},
 \qquad
 u_L=\frac{\log(1+r_L)}{s_1JP}.
 \tag{2}
\]

### Theorem 2: finite-volume isolation and complete literal-source frame

For every fixed periodic L >= 3, every allowed sufficiently fine epsilon,
and every real |u| < u_L, the normalized actual block transfer
`D(u)=B(u)/b_0(u)` has, in the neutral physical odd sector, an isolated
spectral cluster of rank exactly P. It descends from the free plaquette
shell. The P normalized literal plaquette sources, projected onto this
cluster, form a basis. In coefficient normalization, their Gram matrix
is bounded below by `9/16 I`.

These are finite-volume statements with a common epsilon interval.
Equation (2) is not volume-uniform: its source bound can decrease as
`P^(-3/2)`. No thermodynamic closure follows from this theorem alone.

Proof. The full kinematic free block has a simple vacuum eigenvalue 1 and
rest at most 4/5. For r <= r_L its Perron eigenvalue satisfies
`|b_0-1| <= r`, remains simple, and is the branch from the free vacuum.
For real u this also follows from the strictly positive kernel. Consequently

\[
 \|D(u)-B_0\|\le\eta_L:=\frac{2r}{1-r}
 \le \frac52 r\le g_*/40.
 \tag{3}
\]

On the odd sector use the circle with center c(s_epsilon) and radius
`g_*/3`. The free distance to spectrum on this circle is at least that
radius. The resolvent Neumann series is valid by (3). Rank continues along
the real path from 0 to u, and the Riesz projection Pi obeys

\[
 \|\Pi-P_0\|\le
 \frac{\eta_L}{g_*/3-\eta_L}\le3/37.
 \tag{4}
\]

The contour defines a finite-rank projection because B is compact and the
circle is bounded away from zero. All gauge, one-form and charge symmetries
are preserved. The complete odd cluster has transfer eigenvalues in
`[c-eta_L,c+eta_L]`; all other odd eigenvalues are at most `d+eta_L`.
Thus its energy separation is at least
`log((c-eta_L)/(d+eta_L))/s_epsilon > 0`.

For source completeness let Omega be the aligned normalized Perron vector,
Omega_0 the free vacuum. Project its eigenvalue equation onto the free
vacuum complement. Since b_0 >= 1-r and the complementary compression of
B is at most 4/5+r,

\[
 \|\Omega-\Omega_0\|\le
 \sqrt2\,\frac{r}{g_v-2r}\le\frac{2\sqrt2 r}{g_v}.
 \tag{5}
\]

Each literal source `O_p=(chi_p-bar chi_p)/sqrt2` has norm at most
`sqrt2 N`. If J(u) maps a plaquette coefficient vector to
`sum_p a_p O_p Omega`, the elementary Hilbert-Schmidt column bound gives

\[
 \|J(u)-J(0)\|\le
 \sqrt P\sqrt2 N\|\Omega-\Omega_0\|
 \le4N\sqrt P r/g_v\le1/16.
\]

J(0) is an isometry onto Ran P_0. Therefore

\[
 \|\Pi J(u)a\|\ge
 (1-3/37-1/16)\|a\|>\tfrac34\|a\|.
\]

Its range has dimension P and lies in the rank-P spectral range, so it is
onto. Squaring proves the Gram bound. This also proves completeness: no
additional, source-invisible state occurs in that particular isolated
finite-volume cluster. QED.

## 3. Why the raw norm estimate cannot supply a common volume domain

Write `d_tau(E)=tau/2 coth(tau E/2)` and c=exp(-s E_s).
At u=0, direct differentiation of the integer power gives

\[
 B'(0)\Omega_0=d_\tau(E_s)(1-c)V_L\Omega_0.
\]

The different plaquette characters are orthogonal and
`||V_L Omega_0||^2=2P`. Hence

\[
 \boxed{\|B'(0)\Omega_0\|
 =\sqrt{2P}\,d_\tau(E_s)(1-c).}
 \tag{6}
\]

The vacuum eigenvalue derivative is zero. Subtracting a vacuum energy
therefore does not remove this growth.

The problem also appears inside the odd space: a fixed odd plaquette can
be accompanied by an even excitation on any of the P-13 link-disjoint
plaquettes. Their orthogonal contributions give a lower bound
`c d_tau(E_s)(1-c) sqrt(2(P-13))` when P>13. The offending term is not a
new low-energy particle. It is the extensive change of the background
vacuum in a fixed reference basis.

## 4. An explicit first-order local vacuum rotation removes that growth

For one plaquette p let P_p^vac be the rank-one product-Haar vacuum
projection on its four links. Set

\[
 S_p=d_\tau(E_s)(v_pP_p^{\rm vac}-P_p^{\rm vac}v_p),\qquad
 S_L=\sum_p S_p,\qquad U_L(u)=e^{uS_L}.
 \tag{7}
\]

Each S_p is bounded and anti-Hermitian. It is gauge invariant, charge even,
and commutes with the one-form symmetries. The extensive finite-volume
exponential is a legitimate unitary. Define

\[
 \widetilde D_L(u)=U_L(u)^* B_L(u)U_L(u)/b_{0,L}(u).
\]

This is a FIRST-ORDER vacuum chart, not an exact finite-u vacuum chart.

### Lemma 3: the differentiated local term annihilates the local vacuum on both sides

At u=0,

\[
 \widetilde D_L'(0)
 =\sum_p F_p\otimes e^{-sK_{p^c}},\qquad
 F_p=B_p'(0)+[e^{-sK_p},S_p].
 \tag{8}
\]

Here B_p'(0) means that only the insertion on plaquette p is differentiated.
Then

\[
 F_pP_p^{\rm vac}=P_p^{\rm vac}F_p=0,\qquad
 \|F_p\|\le f:=J(s+2d_\tau(E_s)).
 \tag{9}
\]

Proof. The free character v_p Omega_p lies exactly at E_s. The differentiated
local block sends its vacuum to
`d_tau(E_s)(1-exp(-sE_s)) v_p Omega_p`. The commutator in (8) gives the
negative of this vector. F_p is self-adjoint, so its adjoint vacuum action
also vanishes. A differentiated fine product contributes at most sJ in
norm; the commutator at most 2J d_tau(E_s). QED.

### Theorem 4: volume- and representation-uniform full operator bound

If `exp(-gamma s) <= 4/5`, then

\[
 \boxed{\sup_L\|\widetilde D_L'(0)\|
 \le16J(s+2d_\tau(E_s)).}
 \tag{10}
\]

This is an operator bound on the FULL kinematic Hilbert space. It is not
restricted to a reachable low-representation sector. It remains valid after
physical/odd restriction.

Proof. Put Q_p=1-P_p^vac. The order inequalities
`-f Q_p <= F_p <= f Q_p` and positivity of the unaffected free factors give

\[
 -f A_L\le\widetilde D_L'(0)\le f A_L,
 \quad A_L=\sum_p Q_p\otimes e^{-sK_{p^c}}.
\]

A free configuration with n excited links intersects at most 4n plaquettes.
At least max(n-4,0) excited links are outside any one p. The associated
eigenvalue of A_L is therefore at most

\[
 4n\delta^{\max(n-4,0)},\qquad \delta=e^{-\gamma s}\le4/5.
\]

This is at most 16: for n<=4 it is immediate, at n=5 equality is possible
at delta=4/5, and thereafter the ratio of consecutive bounds is at most
`(n+1)(4/5)/n < 1`. Thus ||A_L||<=16. QED.

The factor 16 comes from four links per plaquette and four plaquettes per
link, not from a representation dimension. The scale maximizing the
certified free spectral gap is also exactly the endpoint of this elementary
support-count bound.

## 5. An all-orders operator theorem for locally vacuum-annihilating activities

The following theorem states a SU(N)-independent operator mechanism. It is
NOT yet a statement that the fully dressed Wilson operator has the required
activities or their norm bound.

Let every site have a unit vector Omega_i, and let
`D_i=P_i+d_i`, with P_i its vacuum projection, `0<=d_i<=delta(1-P_i)` and
0<delta<1. For nonempty finite supports X suppose a self-adjoint bounded
operator F_X on those sites satisfies

\[
 F_XP_X=P_XF_X=0,\qquad P_X=\bigotimes_{i\in X}P_i.
 \tag{11}
\]

Assume the transfer has the exact finite-volume expansion

\[
 \mathcal D_\Lambda=
 \sum_{\{X_1,\ldots,X_r\}\ \mathrm{pairwise\ disjoint}}
 \left(\bigotimes_{j=1}^rF_{X_j}\right)
 \otimes\left(\bigotimes_{i\notin\cup_jX_j}D_i\right),
 \tag{12}
\]

where the empty family is D_0. It is enough to have bounds a_X>=||F_X||
with

\[
 \eta=\sup_i\sum_{X\ni i}\delta^{-|X|}a_X
 <\log(1/\delta).
 \tag{13}
\]

### Theorem 5: an all-orders volume-independent norm estimate

\[
 \boxed{\|\mathcal D_\Lambda-D_0\|
 \le \sup_{n\ge1}\delta^n(e^{n\eta}-1)
 \le\frac{\eta}{e[\log(1/\delta)-\eta]}.}
 \tag{14}
\]

The estimate holds independently of the number and dimensions of the sites.

Proof. On disjoint supports the operators commute and tensorize. With
Q_X=1-P_X, the absolute quadratic form of a nonempty-family term in (12)
is bounded by its product of a_X times the positive diagonal operator
`(product Q_X) tensor D_outside`. On a configuration with excited-site set I,
this vanishes unless EVERY X meets I. The unaffected part is at most
`delta^(|I|-|union X|)`. Drop disjointness only in this positive upper sum.
The exponential bound for collections then gives

\[
 \delta^{|I|}\left[
 \exp\left(\sum_{X:X\cap I\ne\varnothing}a_X\delta^{-|X|}\right)-1
 \right]\le\delta^n(e^{n\eta}-1).
\]

This bounds the whole self-adjoint quadratic form, not individual selected
matrix elements. Finally `e^(n eta)-1 <= n eta e^(n eta)` and
`sup_(x>=0) x exp(-a x)=1/(e a)` prove (14). QED.

### A concrete sufficient threshold at the spectral block

Use the uniform bound delta=4/5, including rounded blocks. If

\[
 \boxed{\eta\le1/400,}
\]

then `log(5/4)>=1/5` and e>=2 give

\[
 \|\mathcal D_\Lambda-D_0\|\le1/158<g_*/10.
 \tag{15}
\]

A circle of radius g_*/2 around the free odd shell therefore has a convergent
resolvent Neumann series. Its projection differs from the free one by less
than 1/4, and finite-volume rank is exactly 3L^3. All odd eigenvalues outside
that cluster lie below the circle. The estimate controls source-invisible
states because it is a full operator estimate.

For an infinite-volume conclusion one must ALSO supply the compatible
thermodynamic vacuum chart / Hilbert-space identification and local limits.
For spatially weighted sharp-shell matching one must control the spatial
extent of the F_X and the source transformations, not merely (13).

### What remains physical rather than abstract

The scalar activities in the preceding vacuum note are functions of paths.
The F_X in (12) are operators after an EXACT vacuum dressing. The former
must not simply be relabeled as the latter. The new physical target is to
construct an exact, symmetry-preserving vacuum chart and prove (13), with
spatially rooted refinements, for its normalized Wilson transfer. Equation
(10) establishes the first derivative of such a construction directly;
it does not supply the full F_X at nonzero u.

There is a possible nonunitary alternative: the finite-volume Doob operator
`P f=(b_0 Omega)^(-1) B(Omega f)` has P1=1 exactly and is self-adjoint in
L2(Omega^2 dHaar). A linked bound for its action on exact-support functions
could avoid constructing an all-orders unitary. An L-infinity or coefficient
space resolvent must still be connected to the physical Hilbert spectrum
and to source totality. That operator norm bridge is not asserted here.

## 6. An exact completeness test using the full complement

Let D be a positive self-adjoint contraction in an odd momentum fiber, and
let J:C^r -> H be an injective source synthesis map (r=3 for the desired
lattice triplet). Define

\[
 G=J^*J,\quad W=JG^{-1/2},\quad P=WW^*,\quad Q=1-P,
\]

and the exact blocks

\[
 A=W^*DW,\qquad R=QDW,\qquad D_Q=QDQ|_{QH}.
 \tag{16}
\]

### Theorem 6: source-span/complement separation implies completeness

If

\[
 \boxed{A\succeq aI_r,\qquad D_Q\preceq bI_Q,\qquad b<a,}
 \tag{17}
\]

then D has exactly r eigenvalues above b, all at least a, and no spectrum in
(b,a). Its high spectral range is r-dimensional and is spanned by the
projected sources. This holds even when QH is infinite dimensional.

Proof. For real lambda in (b,a), D_Q-lambda is negative and boundedly
invertible. The Schur complement is

\[
 A-\lambda+R^*(\lambda-D_Q)^{-1}R\succeq(a-\lambda)I_r>0.
\]

Block factorization therefore makes D-lambda invertible. Its positive
inertia is exactly r. Equivalently min-max gives at least r eigenvalues
at or above a from P, and at most r above b from the codimension-r subspace Q.
Finite-rank coupling to Q cannot introduce essential spectrum above b.
To prove projected-source completeness, if a vector in P were orthogonal
to the high spectral range, its Rayleigh quotient would be at most b,
contradicting the lower bound a on P. Thus the projection restricted to P
is injective, and dimensions give surjectivity. QED.

This is an application of elementary Schur-complement spectral theory. The
primary methodological source read here is Dusson--Sigal--Stamm,
arXiv:2105.02058, Theorem 1.2 and equations (1.10)--(1.16). No priority claim
is made for Schur reduction or min-max.

If Pi is the high spectral projection, the Sylvester equation on its range
also gives

\[
 \|\Pi-P\|\le\frac{\|R\|}{a-b}.
 \tag{18}
\]

Indeed, with X=Q|Ran Pi and Y=P|Ran Pi,
`D_Q X-X D_high=-RY`. Its solution is a convergent integral with norm at
most `||R||/(a-b)`. The equal finite ranks make `||Q Pi||=||Pi-P||`.
When the right side is below one, this gives a quantitative source-frame
lower bound; mere completeness in Theorem 6 does not need that extra bound.

The ONE genuinely spectral input in (17) is the bound on the ENTIRE Q
space. It cannot be estimated from a three-source correlator alone.

## 7. Source moments isolate irreducible leakage exactly

Let `C_j=J^*D^jJ`, j=0,1,2, so G=C_0. Then

\[
 \boxed{R^*R=
 G^{-1/2}(C_2-C_1G^{-1}C_1)G^{-1/2}\succeq0.}
 \tag{19}
\]

Unlike the previous variance around a fixed scalar c, this removes ALL
motion internal to the source span. Explicitly,

\[
 G^{-1/2}(C_2-2cC_1+c^2G)G^{-1/2}
 =(A-cI)^2+R^*R.
 \tag{20}
\]

Thus one can distinguish a shifted/split source block from genuine leakage
out of that block without assuming a mass or fitting a one-pole correlator.
This is useful whether or not (17) has been proved.

For complex z off the complementary spectrum the exact source resolvent is

\[
 W^*(z-D)^{-1}W=
 [z-A-\Sigma(z)]^{-1},\qquad
 \Sigma(z)=R^*(z-D_Q)^{-1}R.
 \tag{21}
\]

For |z|>||D_Q|| its expansion starts with `R^*R/z`. The three source moments
therefore give the leading coefficient of the exact memory term, but not
its analytic continuation or the spectrum of D_Q. A state orthogonal to
all sources and R can be completely absent from Sigma while still belonging
to the physical window. The complement test explicitly detects this case.

## 8. Tests and falsification controls

`verify_excited_window.py` passed 33 checks. The core SU(3) quadrature
primitive is copied, with its digest, from the preceding deliverable;
this is reuse, not another independent microscopic engine.

The new tests include:

* exact optimal-block and rounded-margin arithmetic;
* direct finite-time local derivative and cancellation of both vacuum legs;
* overlapping four-site supports with the uniform factor-16 bound;
* an exact, all-orders sum over 198 disjoint families in a six-site anchored
  operator model (the actual executed family count is recorded in the JSON);
* exact source-moment, Schur-complement, rank, and angle identities in a
  complete finite triplet-plus-complement model;
* a dark-state negative control: source moments are unchanged, but the
  full-complement test rejects the claimed rank;
* a product-system negative control demonstrating that a first-order vacuum
  rotation is not an all-orders, volume-uniform chart;
* the actual symmetric SU(3) transfer on one closed plaquette in the declared
  p+q<=5 character truncation: 21 total states, all 9 odd states tested.

The Weyl diagnostic used 384-by-384 and 768-by-768 grids; their largest
discrepancy in electric-energy units was about 9.66e-14. Agreement under
refinement is not a validated quadrature enclosure.

The last diagnostic checks the FULL COMPLEMENT OF THE RETAINED MATRIX. It
does not bound representations outside that retained matrix. The cutoff-free
finite-volume conclusion instead rests on Theorem 2's proof.

At u=0.05 and epsilon=0.00625, the diagnostic gives approximately

\[
 a=0.3989127474,\quad b=0.1049284456,\quad
 \|R\|=0.0019073927,
\]

an energy-gap lower bound `log(a/b)/s=3.94971662` against the retained model's
actual gap `3.95015718`, and projector error 0.00648764 against bound
0.00648808. The source Gram in the one-dimensional upper window is about
0.96211111 in the stated normalization. These are floating-point
computations, not validated interval enclosures and not 3+1D glueball data.

### Why first-order success does not establish the nonlinear chart

For independent two-level sites, the first rotation cancels the linear
vacuum creation, but a nonzero quadratic creation term remains. Its action
on an n-site vacuum has norm proportional to sqrt(n). At fixed nonzero u,
the residual product-vacuum overlap can go to zero as n grows. The test
uses the exact product formula and never constructs a 2^n-dimensional
matrix. It prevents (10) from being silently extrapolated to all orders.

## 9. Next precise physical operation

The missing object is now specified at operator level:

1. Construct a symmetry-preserving exact vacuum chart for the Wilson block,
   or its Doob coefficient-space alternative, with linked spatial estimates.
2. Generate the locally vacuum-annihilating operator activities and bound
   their weighted sum. At the short spectral block, eta<=1/400 is one
   explicit sufficient full-Hilbert-space criterion.
3. Establish the thermodynamic range/source identification and spatially
   rooted contour limits. Then use sharp projected-kernel matching and the
   relative-q theorem already derived in the earlier continuation.

No additional computation of C_shp or rest-frame Taylor coefficient supplies
this missing activity bound. Conversely, the sufficient operator criterion
is not tied to any disputed fourth-order value.

## Sources and scope

* `UNIFORM_WILSON_WINDOW.md`: calibrated kinetic free window, positivity,
  all-irrep exclusion, and uniform one-link gap (upstream premises).
* `DISCRETE_TIME_VACUUM_AND_WINDOW.md`: exact positive-power blocking,
  actual Perron vacuum, full source correlations, and the distinction
  between a populated Borel window and a complete Riesz band.
* Revision 6, Theorem 1, Eqs. (2)--(4), and its degree/plaquette counts:
  retained physical shell, source normalization, and link geometry.
* G. Dusson, I. M. Sigal, B. Stamm, *The Feshbach-Schur map and perturbation
  theory*, arXiv:2105.02058v1, Theorem 1.2: external spectral-method context.

The broad thermodynamic Wilson isolation theorem is not claimed. No spatial
continuum limit, physical anisotropy matching, or spin-one identification
is proved. No exhaustive novelty assertion is made.
