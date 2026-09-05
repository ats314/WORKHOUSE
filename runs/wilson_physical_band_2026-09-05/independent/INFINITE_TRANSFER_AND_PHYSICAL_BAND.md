# The actual infinite-volume Wilson transfer and its physical isolated band

5 September 2026. Independent continuation from the frozen cardinality
chart and weighted-activity theorems. The literal-source frame estimate is
the parallel input in `LITERAL_SOURCE_FRAME.md`; its precise use below is
stated separately from the operator construction.

Fix an admitted calibrated temporal mesh tau, its spectral block power m,
and s=m tau. Let

    eta=1/2500,  epsilon=1/998,  delta=4/5,
    g_star=1024/15625.

Use a real coupling in the proved weighted-activity interval, or its
smaller source-frame interval when invoking that frame theorem. All
kinetic, plaquette-incidence and physical free-window hypotheses remain
as in the two frozen proofs.

## 1. The product Hilbert space and its free transfer

Let H_0 be the incomplete tensor product of the countable link Hilbert
spaces with their unit Haar vacua. Equivalently,

    H_0 = C Omega direct-sum
          direct-sum_{finite nonempty I} tensor_{i in I} H'_i.

For a finite link set S, let H_S denote its full tensor Hilbert space
with the vacuum outside S, embedded in H_0. The union of the H_S is
dense; each H_S may be infinite dimensional.

Write D_i=P_i+d_i for the free blocked link kernel, with 0<=d_i<=
delta(1-P_i). The incomplete product D_infinity is the direct sum of
tensor_{i in I}d_i over exact supports I, with value one on Omega.
It is a positive contraction. Its norm on the nonvacuum space is at
most delta. Products D_{S complement} are defined in the same way and
commute with operators supported in S.

## 2. Exact ambient independence of open induced activities

For each finite X in the infinite lattice, construct its own induced
Wilson model, new creator-velocity unitary V_X, normalized blocked
transfer G_X, and partition activity F_X. The induced model retains
exactly the plaquettes fully contained in X. Thus F_X is a single
bounded operator attached to X, independent of any larger ambient box.
This is exact, not merely stabilization of Taylor coefficients.

The frozen weighted theorem gives

    F_X*=F_X,  F_X P_X=P_X F_X=0,
    sup_i sum_{X contains i} 2^|X| ||F_X|| <= eta,                (1)

and F_X=0 unless X is a connected plaquette footprint. On every finite
Gamma its partition expansion reconstructs its actual normalized transfer

    G_Gamma = V_Gamma^* T_Gamma^m V_Gamma / b_Gamma.

In particular G_Gamma is a positive contraction fixing the product
vacuum. This uses the ACTUAL Perron normalization, not an auxiliary
parent energy.

## 3. Strong limit, with a quantitative local Hilbert-space bound

For a finite family C of pairwise disjoint activity supports define on
H_0

    Theta_C = (tensor_{X in C} F_X) tensor D_{(union C) complement}.

The empty family gives D_infinity. If psi belongs to H_S, every nonzero
Theta_C psi has X intersect S nonempty for every X in C. Otherwise that
factor acts on its local vacuum and vanishes, irrespective of the
other, disjoint activities. In particular at most |S| activities survive
in one family. Put

    a(S)=sum_{X intersects S}||F_X|| <= |S| eta.

Dropping disjointness in the positive majorant gives

    sum_{C nonempty} ||Theta_C psi||
       <= (exp(a(S))-1)||psi||.                                (2)

Hence D_infinity psi plus this activity series converges absolutely and
uniformly on the unit ball of every H_S. It defines a linear operator
on the dense union of those subspaces.

For an open finite volume Gamma put

    A_Gamma = G_Gamma tensor D_{Gamma complement}.

Its activity expansion is exactly the preceding series restricted to
X subset Gamma. If S subset Gamma, the omitted part is bounded by

    ||(G_infinity-A_Gamma)psi||
       <= exp(a(S)) a_out(S,Gamma)||psi||,
    a_out(S,Gamma)=sum_{X intersects S, X not subset Gamma}||F_X||. (3)

Indeed mark one omitted activity and bound the remaining nonnegative
family sum by exp(a(S)). For a box containing the radius-R link-graph
neighborhood of S, connectedness forces every omitted support to have
at least R links, and (1) gives the convenient bound

    a_out(S,Gamma)<=|S| eta 2^(-R).                              (4)

The deliberately weaker exponent avoids a boundary convention for
whether the outer layer has radius R or R+1.

Each A_Gamma is a positive contraction. Consequently the densely
defined limit extends to a positive self-adjoint contraction G_infinity
on H_0, and A_Gamma converges strongly to it. Positivity and
self-adjointness follow from bounded strong convergence of the quadratic
forms. Equations (3)-(4) are stronger than pointwise convergence: they
are uniform on the local Hilbert-space unit ball, without a finite
representation cutoff.

The frozen finite-volume norm theorem gives

    ||A_Gamma-D_infinity||
       =||(G_Gamma-D_Gamma) tensor D_{Gamma complement}||
       <= epsilon.

Passing to the strong limit proves

    G_infinity Omega=Omega,
    ||G_infinity-D_infinity||<=epsilon.                         (5)

The ordinary embeddings G_Gamma tensor I have the same strong limit:
on any fixed H_S they agree with A_Gamma once Gamma contains S, and all
are contractions. Norm convergence on the entire H_0 is not asserted.

### Centered periodic volumes

Embed a centered torus's link factors into a centered cube of H_0. On
any fixed faithful interior neighborhood its induced activities agree
EXACTLY with the open-lattice F_X, since no wrapping plaquette is
retained there. All remaining activities that can act on H_S must both
meet S and exit that neighborhood. Their intrinsic torus connected
support cardinalities are therefore at least the neighborhood radius.
Apply (3)-(4) separately to the torus and open tails. This proves the
same local Hilbert-space limit, with at most twice the displayed tail
bound. It does not give a false ambient diameter estimate for wrapping
plaquettes. Free factors are identical under the link-factor embedding.

## 4. Physical symmetry reduction and complete odd projection

The canonical infinite activities are covariant under translations and
the retained gauge, charge-conjugation and center symmetries. This follows
from the unique induced creator solution and unique velocity inversion.
Thus G_infinity and D_infinity commute with these symmetries.

Let H_phys be the product-vacuum physical neutral sector, and restrict
further to its charge-odd subspace H_-. The finite-support gauge-invariant
vectors are dense in this sector: projection onto the vacuum outside
larger finite link sets converges strongly to I and commutes with the
gauge transformations. Such a finite support embeds inside a sufficiently
large periodic lattice without winding. Its physical neutral free
window is therefore the calibrated finite-volume window. Passing its
quadratic-form inequality to the closure gives

    D_infinity P_0=c P_0,  D_infinity|_(H_- minus P_0)<=d,
    c=exp(-4 gamma s),  d=exp(-5 gamma s),  c-d>=g_star.          (6)

Here P_0 is the COMPLETE free odd plaquette shell, the closure of its
orthonormal translated plaquette vectors. It is naturally isomorphic to
ell^2(Z^3) tensor C^3. In particular the hypothesis is the full physical
window, not just a one-link kinetic gap.

Let Pi be the Riesz projection of G_infinity|H_- on the circle centered
at c with radius g_star/2. Equation (5), the resolvent identity and the
free gap imply

    ||Pi-P_0|| <= 2 epsilon/(g_star-2 epsilon) < 1/4.             (7)

The projection is orthogonal, and its range is the entire spectrum in
this island, including any vector invisible to a preselected source.
The remainder lies below c-g_star/2; no odd spectral component lies above
the circle. This follows from the self-adjoint spectral inclusion under
a norm-epsilon perturbation of (6).

There is also a genuine infinite-volume vacuum transfer gap: (5) and
vacuum anchoring give ||G_infinity|Omega^perp||<=delta+epsilon<1.
No global logarithmic Hamiltonian is needed for any of these assertions.
On Ran Pi the transfer is bounded away from zero, so its logarithm is
a bounded self-adjoint band-energy operator in the actual electric-time
normalization. This statement does not require injectivity of G on its
entire high-energy complement.

## 5. Identification with the selected full quantum GNS transfer

Use the new-chart automorphism alpha, with finite convention
alpha_Gamma(O)=V_Gamma^* O V_Gamma. The established local operator-norm
limit gives the selected actual vacuum state

    omega_W(O)=<Omega,alpha(O)Omega>.

For its full local-quantum GNS representation the map

    W: pi_W(O)Omega_W -> alpha(O)Omega                          (8)

extends to a unitary onto H_0. Isometry follows from the state identity;
density follows from the automorphism property and product-state
cyclicity for the full quasi-local algebra. The same statement restricts
to the physical invariant observable algebra and its vacuum-cyclic
physical sector. A finite gauge-invariant vector can be produced from
Omega by its bounded local invariant rank-one creator, giving the
required physical density in this full-quantum statement.

Define the actual blocked GNS transfer as W^* G_infinity W. This is more
than an operator sharing the vacuum. For any fixed bounded local
operators O_j and nonnegative integer powers n_j, the exact finite
Wilson vacuum expectation equals

    <Omega,alpha_Gamma(O_0) G_Gamma^n_1 alpha_Gamma(O_1)
                ... G_Gamma^n_k alpha_Gamma(O_k)Omega>.

The heat-completed embeddings A_Gamma give the same expression when all
local operators are contained in Gamma. The operators alpha_Gamma(O_j)
converge in norm and the uniformly bounded A_Gamma converge strongly.
Finite products therefore converge to the identical expression with
alpha and G_infinity. This proves the joint selected actual-transfer
identification, including noncommuting bounded local quantum operators.

### Fine temporal steps from the positive block root

No separate activity estimate is required to recover the fine step.
For fixed tau and its fixed integer m, functional calculus gives

    A_Gamma^(1/m)
      = (V_Gamma^* T_Gamma V_Gamma/lambda_Gamma)
                       tensor exp(-tau K_(Gamma complement)).

The function x->x^(1/m) is continuous on [0,1]. Uniform boundedness and
polynomial approximation imply strong convergence of these roots to
G_fine=G_infinity^(1/m). Hence G_fine^m=G_infinity, and all finite fine-time
correlation products have their corresponding limits. This is at each
admitted fixed temporal mesh; no interchange with a mesh limit is used.

## 6. Euclidean reconstruction and the exact cyclicity needed for the band

For the physical Wilson interpretation use the algebra M of bounded
local gauge-invariant neutral multiplication sources. On this algebra
the finite kinematic vacuum correlations equal the gauge-projected
Wilson correlations, because the vacuum and all intermediate vectors
remain gauge invariant. Gauge-variant time histories are not needed.

Let a positive-time multiplication history F have factors f_0,...,f_k
and time increments n_1,...,n_k. Associate the vector

    v_F=alpha(f_0) G_fine^n_1 alpha(f_1)
                     ... G_fine^n_k alpha(f_k)Omega.              (9)

Products at the reflection slice combine in the commuting algebra
alpha(M). The exact finite transfer identity identifies
<v_F,v_H> with the limit of the reflection-positive Wilson form
<Theta F H>. Section 5 proves existence of all these limits. Thus the
OS quotient by its zero-norm histories, followed by completion, is
unitarily represented onto

    K=closure span{v_F} subset H_phys.                           (10)

This explicitly constructs the physical Euclidean transfer representation;
it does not infer it merely from equality of time-zero states. The
transfer reconstructed by one fine time step is G_fine restricted to K.
The subspace K is invariant under G_fine, by adding an initial identity
source and time step to a history. Since G_fine is bounded self-adjoint,
K is reducing. It is also invariant under charge conjugation, so its
odd part reduces the odd blocked transfer.

At this point one need not assume that M alone is cyclic in the entire
full-quantum GNS Hilbert space. The following stronger-for-the-target
statement is enough and is provable. Let J_p=alpha(O_p)Omega be the
literal odd plaquette source vectors. Each J_p belongs to K. On H_-,
the isolated projection Pi is a uniform limit of polynomials in the
blocked transfer: choose a continuous function equal to one on the
island and zero on the remaining odd spectrum, and use polynomial
approximation on [0,1]. Consequently

    Pi J_p belongs to K for every p.                            (11)

If the parallel literal-source frame theorem proves that the bounded
synthesis Pi J maps ell^2(Z^3) tensor C^3 ONTO Ran Pi, then (11) and
closedness imply Ran Pi subset K. Therefore the entire full-quantum
physical band is present in the OS representation, with no omitted
source-invisible band state. Conversely K reduces G, so its spectral
projection on the island is precisely the restriction of Pi. Hence

    OS isolated band = Ran Pi,                                  (12)

unitarily, with the actual transfer and all projected source vectors
intertwined. The same band is already represented in the full physical
GNS space by (8).

This proves selective source cyclicity on the COMPLETE isolated band.
It neither assumes nor needs K=H_phys, or cyclicity of only equal-time
multiplication operators on every high-energy quantum state. Those
global equalities are not prerequisites for (12). The literal frame
surjectivity is the substantive input that rules out a hidden band
complement; a lower frame bound alone would not suffice at infinite rank.

## 7. Scope and remaining use

The strong transfer limit, joint actual-GNS identification, complete
isolated infinite-volume odd projection and OS realization are analytic
consequences of the established weighted activities and chart. With the
parallel onto-frame estimate they give the complete infinite-volume
physical Wilson band and literal-source frame in the stated small
coupling regime. The operator limits work for open boxes and centered
periodic exhaustions and have no representation cutoff.

This does not equate the Wilson band-energy kernel with its Hamiltonian
counterpart, establish a spatial continuum limit, or prove global
injectivity of the transfer merely from its norm perturbation bound.
Those statements are unnecessary to the complete band and selective
Euclidean/GNS identification proved here.
