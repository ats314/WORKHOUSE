# Fixed-observable Wilson expansion, complete shell, and carrier transport

8 September 2026. Analytic continuation at fixed spatial spacing, for SU(3).

This note completes the temporal marked-shell route under the calibrated
kinetic-window and Hamiltonian G18 hypotheses stated below. It combines the
actual Wilson creator/activity/source constructions already present in the
September 5 worktree with two further arguments: the anchored operator bound
holds at complex coupling, and finite propagation of Taylor coefficients turns
a uniform Hilbert-space analytic bound into the required spatially weighted
bound. It then sums the existing coefficientwise matching theorem.

The main checkout's earlier [WT-6](wilson-marked-transfer.md) did not include
those September 5 constructions. Their imported, unchanged proof sources and
original commit/file hashes are recorded in
[the input manifest](wilson-shell-inputs/manifest.json). They are analytic
inputs, not newly discovered results. The new full theorem is an analytic
derivation; the accompanying exact checks and Lean lemmas certify only their
stated finite algebra and scalar inequalities. The spatial continuum problem
G19 remains open.

## 1. Operators, inputs and common domain

Put gamma=C_F/2=2/3, J=6, and keep the fundamental-character clock

\[
 \tau=-2\log\lambda_F(\epsilon)/C_F,\qquad
 T_{\epsilon,\Lambda}(u)
 =e^{\tau uV_\Lambda/2}e^{-\tau K_{\epsilon,\Lambda}}
 e^{\tau uV_\Lambda/2},\qquad \beta_s=2Nu\tau.
\]

The link generators are nonnegative, annihilate their Haar vacua, and have
excited gap at least gamma. The calibrated physical neutral charge-odd
free shell has energy 4 gamma, is spanned by the normalized odd plaquette
characters, and its entire complement has energy at least 5 gamma. This is
the representation-uniform window premise of
[the existing window theorem](../../paper/research_notes/G19_UNIFORM_WILSON_WINDOW_20260904.md),
on its admitted temporal meshes and periodic L>=3. No representation cutoff
is imposed. The Hamiltonian complete-band, analytic-symbol and coefficient
identities are the G18 inputs to
[the relative-gap theorem](../../paper/research_notes/G18_RELATIVE_GAP_BRIDGE_20260904.tex).

Choose

\[
 s_0=\gamma^{-1}\log(5/4),\quad 0<\tau\le\tau_0\le s_0/4,
 \quad m=\lceil s_0/\tau\rceil,\quad s=m\tau\in[s_0,s_1],
 \quad s_1=s_0+\tau_0.
\]

Use a creator weight a>=max(gamma tau0/2, log(2)+gamma tau0/4), and set

\[
 u_* = \min\{9\gamma/(309680Je^{4a}),\ 9/(8450\tau_0Je^{4a})\},
 \quad u_0=u_*/1252800000,\quad u_1=u_0/(8N),\quad N=3.
 \tag{S1}
\]

The supplied proofs are:

| Input | Exact role in this continuation |
|---|---|
| [Rooted contraction](wilson-shell-inputs/G18_ROOTED_WILSON_CONTRACTION_20260905.md), §§4–7 | Nonzero scalar normalization, actual endpoint eigenpair, full resolvent restoring the moving support weight. |
| [Creator limit](wilson-shell-inputs/G18_WILSON_CREATOR_THERMODYNAMIC_LIMIT_20260905.md), §§2–4; [symmetric creators](wilson-shell-inputs/G18_WILSON_CREATOR_PARENT_AND_SPECTRAL_FLOW_20260905.md), §1 | Connected coefficient witnesses, local limits, actual symmetric vacuum creators. Only §1 of the parent note is needed for the creator estimate here. |
| [Cardinality chart](wilson-shell-inputs/G18_WILSON_CARDINALITY_UNITARY_CHART_20260905.md), §§2–5 | Exact vacuum-line unitary V on real coupling, its doubled holomorphic continuation, component factorization and local source transport. |
| [Activity extraction](wilson-shell-inputs/G18_WILSON_ACTIVITY_EXTRACTION_20260905.md), §2; [weighted activities](wilson-shell-inputs/G18_WILSON_WEIGHTED_ACTIVITY_BOUND_20260905.md), §§2–5 | Partition inversion, the actual Perron normalizer, ordered connected contour, and the full operator activity bound. The V chart is used throughout. |
| [Complete physical band](wilson-shell-inputs/G18_WILSON_INFINITE_VOLUME_PHYSICAL_BAND_20260905.md), §§2–8 | Strong actual-transfer limit, tagged synthesis estimate, onto projection argument, and inclusion of the entire band in the Wilson OS representation. |
| Window theorem, §8 | At every fixed magnetic order, matching of the compatible energy, Gram and source coefficients in the spatially weighted norm. |

The long vacuum block of WT-1–WT-4 and the shorter spectral block above are
powers of the same positive transfer. They have the same vacuum and spectral
subspaces. All quantitative domains used together may be intersected; each
is nonempty and independent of spatial volume and temporal mesh.

## 2. The expansion with a fixed observable

For a bounded local O and integers a,b>=0, insert exp(zO) at a block boundary:

\[
 Z_{a,b}(z)=\langle\Omega_0,B^a e^{zO}B^b\Omega_0\rangle,
 \qquad B=T^m.
\]

The coefficient linear in z of log Z is

\[
 [z]\log Z_{a,b}(z)
 =\frac{\langle\Omega_0,B^a O B^b\Omega_0\rangle}
 {\langle\Omega_0,B^{a+b}\Omega_0\rangle}.                 \tag{S2}
\]

Expand the magnetic half and full factors in their actual time order,
retaining all intervening kinetic contractions. For a set I of activated
plaquettes the inclusion-exclusion block of WT-2 satisfies

\[
 \|C_I\|\le\prod_{p\in I}(e^{s|u|\|V_p\|}-1).             \tag{S3}
\]

Resolve inactive links into their vacuum and excited projectors as in WT-3.
Compatible space-time components factor, including components separated by
an explicit rank-one vacuum reset on a reused link. A disconnected spectator
has Z(z)=Z_A(z)Z_C and therefore contributes nothing to [z] log Z. The
multivariate identity gives this cancellation coefficient by coefficient,
before taking absolute values. Two distinct source derivatives of log Z
retain clusters joining both marks. For a disconnected spatial support of O,
assign a fixed connected hull to its mark; this costs only a fixed support
constant. Repeated magnetic insertions are already summed in (S3).

WT-4 bounds this scalar marked series on its stated common domain. For the
operator continuation use the exact analytic vacuum chart and the induced
Perron normalizer instead of a scalar amplitude bound. On every induced
finite link set X define

\[
 G_X(u)=b_X(u)^{-1}V_X(u)^{-1}T_X(u)^m V_X(u),\qquad
 D_X=e^{-sK_X},\quad b_X=\lambda_X^m.                      \tag{S4}
\]

At real coupling V is unitary and b_X is the actual Perron eigenvalue.
At complex coupling inverse means the holomorphic inverse, never the adjoint
at the same complex argument. The doubled chart supplies it. Its identity
V(\bar u)^*=V(u)^{-1} follows from the real identity and holomorphy.

Partition inversion on induced link subsets gives the exact expansion

\[
 G_\Lambda=D_\Lambda+
 \sum_{\varnothing\ne\mathcal A\ {m disjoint}}
   \bigotimes_{X\in\mathcal A}F_X\ \otimes D_{\Lambda\setminus\cup\mathcal A},
 \quad F_XP_X=P_XF_X=0.                                  \tag{S5}
\]

Both vacuum legs vanish at complex u as well: each is a holomorphic operator
identity vanishing on a real interval. This is stronger than subtracting an
extensive vacuum-energy scalar in an unchanged free basis.

The weighted-activity proof represents (S4) by an ordered contour with two
chart legs, magnetic slots of total duration s, and the scalar log b leg.
For primitive costs a_Y=integral ||J_Y(t)||dt, the rooted tree estimate is

\[
 E=\sup_i\sum_{Y\ni i}e^{(\kappa+h)|Y|}a_Y\le h
 \quad\Longrightarrow\quad
 \sup_i\sum_{X\ni i}e^{\kappa|X|}\|F_X\|\le E.           \tag{S6}
\]

Disconnected ordered shuffles factor; overlapping insertion order is kept.
The positive rooted-tree recursion is T_Y=b_Y exp(sum_{Z intersect Y}T_Z),
with b_Y=e^{kappa|Y|}a_Y and supersolution b_Y exp(h|Y|). This bounds all
orders and arbitrary Hilbert-space coefficients. The coefficients of both
holomorphic chart legs were bounded separately in the input proof, so the
same majorant applies at complex coupling. With kappa=log 2 and h=1 it gives

\[
 \sup_{\Lambda,\epsilon,i}\sum_{X\ni i}2^{|X|}\|F_X(u)\|
 \le 1/2500\qquad (|u|\le u_0).                         \tag{S7}
\]

There is no division by tau in (S3), (S6) or (S7). The kinetic factors enter
only as contractions. The count of connected degree-n primitive monomials
through a link is at most 4*145^(n-1), also on wrapping periodic supports.
The nonzero normalizer and its connected log are retained in this count.
The same estimates hold for independent plaquette variables with their maximum
modulus in the stated disc; translation invariance is not needed for the
primitive counts or the operator estimate. This multivariate version will be
used only to establish coefficient support.

## 3. Complex anchored operator bound

Here is the additional operator lemma. Self-adjointness of the F_X is
unnecessary in the all-orders norm estimate of the excited-window bridge.
Suppose D_i=P_i+d_i, 0<=d_i<=delta(1-P_i), 0<delta<1, and (S5) holds with
F_X=Q_X F_X Q_X, Q_X=1-P_X. Write a_X>=||F_X|| and

\[
 \eta=\sup_i\sum_{X\ni i}\delta^{-|X|}a_X<\log(1/\delta).
\]

For each nonempty disjoint family A put

\[
 C_A=\prod_{X\in A}a_X\,
       \bigotimes_{X\in A}Q_X\otimes D_{\Lambda\setminus\cup A}.
\]

By inserting the square root of the positive spectator D, the corresponding
operator term L_A satisfies, for arbitrary vectors phi,psi,

\[
 |\langle\phi,L_A\psi\rangle|
 \le\langle\phi,C_A\phi\rangle^{1/2}
      \langle\psi,C_A\psi\rangle^{1/2}.
\]

Cauchy–Schwarz over families bounds the sum by the same expression with
C=sum_A C_A. This argument is valid for nonnormal F_X. In an exact excited
support I of size n, C is zero unless each activity meets I. Dropping
disjointness only in the positive majorant gives

\[
 \|G_\Lambda-D_\Lambda\|
 \le\|C\|\le\sup_{n\ge1}\delta^n(e^{n\eta}-1)
 \le\frac{\eta}{e(\log(1/\delta)-\eta)}.                 \tag{S8}
\]

Take the common envelope delta=4/5, not the smaller mesh-dependent actual
one-link norm. Equation (S7) implies eta<=1/2500 since (5/4)^|X|<=2^|X|.
Using log(5/4)>=1/5 and e>=2 proves the complex uniform bound

\[
 \|G_\Lambda(u)-D_\Lambda\|\le e_0:=1/998.                \tag{S9}
\]

This controls every input excitation support, including arbitrarily high
representations. It avoids a global norm estimate for V or V^{-1}.

## 4. Actual complete shell and a holomorphic literal-source frame

In the physical odd sector write c=exp(-4 gamma s), g_*=1024/15625, and
use the circle C_s: |w-c|=r_c with r_c=g_*/2. Its free spectral clearance
is at least r_c. Equation (S9) yields the Neumann resolvent and full Riesz
projection P(u), with

\[
 \|P(u)-P_0\|\le e_0/(r_c-e_0)<1/9.                     \tag{S10}
\]

The last strict inequality follows from 20/998<g_*. The complex projection
need not be orthogonal. At real u it is the orthogonal projection of the
actual normalized transfer; its range is the complete continued shell.

For O_p=(chi_p-bar chi_p)/sqrt(2), let

\[
 J(u)e_p=V(u)^{-1}O_pV(u)\Omega_0,\qquad
 J^\sharp(u)=J(\bar u)^*.
\]

The source estimate in the complete-band proof keeps every plaquette tag,
uses charge-odd zero expectation term by term, and uses disjoint-support
orthogonality to bound the entire synthesis map. Its proof uses absolute
generator norms and thus also applies to the holomorphic chart. On |u|<=u1,

\[
 \|J-J_0\|<1/8,\quad \|J^\sharp-J_0^*\|<1/8,
 \quad \|J\|,\|J^\sharp\|\le9/8.                        \tag{S11}
\]

Explicitly, its tagged remainder has norm
D<=640 e^2 sqrt(2)N G_int exp(2G_int), synthesis norm <=D/8, and
G_int<=1/(20000N). These are uniform complex estimates as well as real ones.
Adjoint reflection in J^sharp, rather than adjoint at u, preserves holomorphy.

Define the absolute projected-source Gram and its binomial functions by

\[
 A=J^\sharp PJ,\qquad A(0)=I,\quad S=A^{1/2},\quad C=A^{-1/2}.
\]

Equations (S10)–(S11) give

\[
 \|A-I\|\le (1/9)(9/8)^2+2/8+1/64=13/32<1/2.           \tag{S12}
\]

The binomial series therefore define bounded holomorphic S,C on a common
disc, with ||S||<2 and ||C||<2. Put W=PJC and W^sharp=CJ^sharp P; then
W^sharp W=I. At real coupling the direct-rotation/Neumann argument of the
complete-band theorem proves W is onto Ran P, including in infinite volume.
A lower bound alone is not being used to infer infinite-dimensional onto.
Its quantitative real source frame obeys

\[
 9I/16\prec A\preceq81I/64.                              \tag{S13}
\]

The contour lies in the open right half plane and away from zero. Let

\[
 L(u)=\frac1{2\pi i}\oint_{C_s}\log w\,(w-G(u))^{-1}dw,
 \qquad h(u)=-s^{-1}C J^\sharp L(u)J C.                  \tag{S14}
\]

The logarithm is the branch real on positive w. On the real shell, h is
exactly the vacuum-subtracted physical generator in the orthonormal literal
source frame. Since s=m tau and G is normalized by lambda^m, it is the
generator of the original fine transfer in the same energy units.
In this frame S is precisely the projected literal-source synthesis matrix.

For example set c_min=(4/5)^5, L_log=-log(c_min-r_c)+pi and
M_op=max(2,6 L_log/s0). The contour resolvent and (S11)–(S12) give

\[
 \sup_{\epsilon,\Lambda,|u|<u_1}
   \max(\|h(u)\|,\|A(u)\|,\|S(u)\|)\le M_{\rm op}.    \tag{S15}
\]

The numerical constants are loose; the relevant facts are a positive common
disc and no volume, mesh or representation-dimension factor.

The input complete-band proof realizes the thermodynamic G strongly on the
product-vacuum tensor space and the local source chart in operator norm.
Its joint-time limit identifies the actual Wilson correlations, not only
the equal-time state. The OS history subspace reduces G and contains every
projected literal source. Since PJ is onto, it contains all of Ran P. Thus
the complete shell in (S14) is present in the physical Wilson reconstruction.
Complex full-space thermodynamic holomorphy need not be assumed: the kernel
limits and their holomorphy follow directly from the coefficients below.

## 5. From finite-order locality to a uniform weighted Taylor bound

Use a common coefficient convention indexed by three plaquette orientations
at each lattice point. For Phi in {h,A,S}, write Phi=sum_n u^n Phi_n.
Choose R0=u1/2. Cauchy's operator estimate from (S15) gives

\[
 \|\Phi_{\epsilon,\Lambda,n}\|\le M_{\rm op}R_0^{-n}.    \tag{S16}
\]

**Support lemma.** For n>=1, a matrix entry between source anchors p,q
vanishes if their periodic base-point l1 distance exceeds 12n. The same
statement holds on the infinite lattice.

To prove it, first use independent plaquette couplings. Every degree-n
chart/activity coefficient is assigned to the footprint of at most n
active plaquettes. With these variables alone switched on, distinct
link-connected components tensorize, the normalized transfer fixes the
vacuum on an unused component, and the source remains odd on its own
component. Hence a spectator component without a mark drops out exactly,
and two components each carrying one odd mark have zero cross entry.
This factorization takes place in the kinematic link tensor space. One does
not assume that a Gauss-constrained Hilbert space tensorizes across components
sharing a vertex. Physical source-generated cyclic subspaces are invariant
under the actual self-adjoint transfer; spectral functions on those vectors
retain the same spectator-vacuum and component-parity identities. Equivalently,
use polynomial approximation on the physical transfer spectrum and then
analytic continuation of its matrix elements.
A nonzero coefficient of J^sharp P J or J^sharp L J therefore has a
connected witness joining the two marked plaquettes, with at most n+2
plaquettes in all. The spectral functions do not add spatial support:
in the factorized model they preserve the component parity and act on a
spectator vacuum of normalized eigenvalue one. This also proves cancellation
for diagonal entries with remote spectator variables.

Two plaquettes sharing a link have base-point l1 distance at most two.
The connected witness has at most n+1 adjacency edges along a simple path
between its marks, giving distance <=2(n+1). The looser 12n bound for n>=1
leaves ample endpoint allowance. The degree-zero matrices are scalar and
diagonal. Products and the formal binomial series for A^{+/-1/2} concatenate
such paths; since their positive degrees sum to n, the 12n bound survives.
This proves it for h and S as well. On a torus paths are measured intrinsically;
wrapping does not invalidate the bound. Once L>4(n+2), the primitive
coefficients have faithful infinite-lattice lifts as in the window proof.
Products inherit coefficient stabilization by finite convolution.

For scalar orientation entries define the weighted row/column Schur norm

\[
 \|K\|_{\mu,\sharp}=
 \max\{\sup_p\sum_q e^{\mu d(p,q)}|K_{pq}|,
         \sup_q\sum_p e^{\mu d(p,q)}|K_{pq}|\}.
\]

For translation kernels this is the usual weighted orientation row/column
norm, using base-point displacement. Intrinsic torus distance is used in
finite volume. Any fixed mu>0 is allowed at the cost of shrinking the
coupling radius. A radius-12n row has at most 3(24n+1)^3 entries, including
on a torus. Each entry is bounded by (S16). Since n^3<=4*2^n for n>=1,

\[
 \boxed{\ \|\Phi_{\epsilon,\Lambda,n}\|_{\mu,\sharp}
 \le M R^{-n},\quad
 M=187500M_{\rm op},\quad R=R_0/(2e^{12\mu}).\ }         \tag{S17}
\]

The same constants cover n=0. The inequality n^3<=4*2^n follows by checking
n=1,...,4 and inducting from n=4, since ((n+1)/n)^3<=125/64<2.
This is the requested all-order weighted majorant. It bounds the energy,
Gram and source kernels on one common disc. Finite order has finite range;
its row count, rather than a volume count, is what upgrades (S16).

Coefficient stabilization plus the geometric tail in (S17) now gives
limiting translation kernels in the weighted Banach space. For real u they
agree, by entrywise local/strong convergence and uniqueness, with the actual
complete-band kernels in §4. This proves both convergence and identification.
It does not assert that moving-box zero extensions converge in a global
rooted supremum norm.

## 6. Sum the matching and transport the carrier

Choose 0<mu<=mu_H, where mu_H is an exponent supplied by the Hamiltonian
G18 theorem, and take a smaller common radius if needed to include its weighted
majorant. The window theorem §8 applies in the same literal-source polar
frame on both sides. The choice is intrinsic: unitary vacuum charts cancel
from real physical matrix elements, hence from their analytic continuations.
No equality between the excited actions of different vacuum charts is needed.

For each Phi in {h,A,S}, at |u|<R and any integer M0>=0,

\[
 \|\Phi^W_\epsilon(u)-\Phi^H(u)\|_{\mu,\sharp}
 \le\epsilon^2\sum_{n=0}^{M_0}A_{n,\mu}|u|^n
  +\frac{2M(|u|/R)^{M_0+1}}{1-|u|/R}.                  \tag{S18}
\]

First epsilon tends to zero at fixed M0, then M0 tends to infinity.
The convergence is uniform on each smaller closed coupling disc. No summed
O(epsilon^2) rate is inferred without a bound on the growth of A_{n,mu}.

There is a useful stronger uniformity at u=0. The exact complete second-order
formula in the window note gives h^W_0=h^H_0=(8/3)I and
h^W_1=h^H_1=I in this frame. Consequently

\[
 \Xi_\epsilon(u)=\frac{h^W_\epsilon(u)-h^H(u)}{u^2}
\]

has a removable singularity at zero and converges to zero in the weighted
norm uniformly on every smaller closed disc, by (S17) applied to the shifted
series and fixed-order matching starting at degree two. Put
xi_epsilon=sup_{|u|<=r}||Xi_epsilon(u)||_(mu,sharp), where r<R is also
inside the Hamiltonian carrier domain.

Cubic covariance and scalar inversion at Gamma give scalar h(0,u) and
zero first momentum derivative in the common frame. The existing centering
theorem, gamma_mu=pi^2/(2e^2 mu^2), therefore gives the matched centered error
at momentum k at most gamma_mu xi_epsilon u^2 q(k), where
q(k)=4 sum_j sin^2(k_j/2). Choose the Hamiltonian domain so that its internal
gap is at least (t3/2)u^2 q(k), t3=5/612. For all sufficiently small admitted
epsilon, independently of 0<|u|<=r, arrange xi_epsilon<t3/(8 gamma_mu).
Weyl's two eigenvalue errors then give

\[
 \boxed{E_1^W(k,u)-E_0^W(k,u)
 \ge [t_3/2-2\gamma_\mu\xi_\epsilon]u^2q(k)
 > (t_3/4)u^2q(k),\quad k\ne0.}                         \tag{S19}
\]

This uses one coupling interval and one sufficiently fine temporal threshold
for every nonzero momentum. Their existence is proved, not their optimal size.
The internal gap still closes at Gamma; the full shell remains isolated from
its external complement.

Let P_H(k,u),P_W(k,u) be the lowest rank-one projections in the common
three-dimensional coefficient frame. Projecting the perturbed eigenvector
equation onto the Hamiltonian complement gives the convenient bound

\[
 \|P_W-P_H\|\le
 d_\epsilon:={\gamma_\mu\xi_\epsilon\over
                   t_3/2-2\gamma_\mu\xi_\epsilon}\longrightarrow0.
 \tag{S20}
\]

After shrinking epsilon so that d_epsilon<1, projection and normalization
of the established Hamiltonian unit carrier section supplies the Wilson
section on the punctured zone. Its direct integral is reducing for the
actual Wilson energy and translations.

## 7. Observable overlap, with the quantifiers retained

For any unit carrier vector v_W in its fiber, the onto literal-source frame
already proves

\[
 \sum_{\alpha=1}^3|\langle v_W,S_W e_\alpha\rangle|^2
 \ge9/16.                                               \tag{S21}
\]

For a *specified* source combination a(k), ||a(k)||<=1, put
b_H(k,u)=||P_H S_H a|| and eta_S=||S_W-S_H||_(mu,sharp). Then

\[
 \boxed{\ \|P_W S_W a\|
 \ge b_H(k,u)-\eta_S-d_\epsilon\|S_Ha\|.\ }             \tag{S22}
\]

Thus every established positive overlap of that fixed observable survives
once its explicit amplitude exceeds the two errors. Uniform positivity on a
momentum set requires a positive Hamiltonian infimum there. A complete frame
does not mean every individual local observable couples to every fiber.
For the normalized cube-direction source one may instead use the existing
bound 1-||P_W-P_free||-||S_W-I|| after shrinking the common domains.
The literal unnormalized compact cube has coefficient w(k), of norm sqrt(q),
so its spectral weight retains the factor q and vanishes at Gamma.

For an arbitrary bounded local O outside the three-source span, §2 constructs
its marked expectation, but (S22) requires the corresponding established
source-synthesis matching. No overlap of an arbitrary observable is inferred
from its mere boundedness (the identity observable is an immediate example).

## 8. What is now established and what remains

The fixed-observable vacuum cancellation is exact. The actual holomorphic
anchored transfer has a uniform full-Hilbert-space bound. Its complete shell,
onto physical source frame and Wilson reconstruction are supplied by the
identified September 5 theorems; §§3–5 give their missing common weighted
Taylor majorant. Equations (S18)–(S22) then implement the existing matching
and relative-gap route, including the observable amplitude it actually
controls. The inputs and finite controls remain separately identified.

This advances the temporal part of G18/G19 at fixed spatial lattice spacing
and small magnetic coupling. A spatial scale theorem, the appropriate coupling
trajectory and physical normalization, and a continuum reconstruction remain
separate obligations. No finite-order numeric threshold is substituted for
the analytic coupling radius above.
