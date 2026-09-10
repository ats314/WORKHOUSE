# The complete infinite-volume physical Wilson band and literal-source frame

5 September 2026. Comprehensive analytic continuation from the established
actual creator chart and weighted operator activities. The result concerns
the selected actual Wilson transfer at fixed spatial lattice spacing,
uniformly over the admitted volumes and temporal meshes. It is not a
statement about the auxiliary creator-parent excitation spectrum.

## 1. Established inputs and theorem

Use the exact hypotheses and constants of
[the rooted Wilson contraction](G18_ROOTED_WILSON_CONTRACTION_20260905.md),
[the actual symmetric creators](G18_WILSON_CREATOR_PARENT_AND_SPECTRAL_FLOW_20260905.md),
[the cardinality unitary chart](G18_WILSON_CARDINALITY_UNITARY_CHART_20260905.md),
and [the actual weighted activities](G18_WILSON_WEIGHTED_ACTIVITY_BOUND_20260905.md).
In particular, retain four distinct links per plaquette, at most four
plaquettes per link and twelve overlap neighbors per plaquette, bounded
magnetic terms of norm at most J, additive link kinetic gap gamma, and
the compact, self-adjoint, positivity-improving real Wilson-kernel premise.
The physical free plaquette shell additionally uses the full calibrated
window in [the Wilson-window theorem](G19_UNIFORM_WILSON_WINDOW_20260904.md).
For this physical specialization set gamma=C_F/2=(N^2-1)/(4N), the
exact calibrated fundamental-link energy. The free odd plaquette shell
then has energy 4gamma and its complement has energy at least 5gamma.
An arbitrary smaller additive-gap lower bound does not identify this
shell center and cannot replace the calibrated window premise.

For fixed N>=3 put

```text
mu >= max(gamma tau0/2,log(2)+gamma tau0/4),
u_star=min(9 gamma/(309680 J exp(4mu)),
           9/(8450 tau0 J exp(4mu))),
s_sp=log(5/4)/gamma,
0<tau<=tau0<=s_sp/4,
m=ceil(s_sp/tau),  s=m tau<=s1=s_sp+tau0,
u0=u_star/1252800000,
u1=u0/(8N),  |u|<=u1,
eta_act=1/2500,  epsilon=1/998,
g_star=1024/15625,  q0=4/5+1/998<1.
```

Keep the calibrated representation-uniform kinetic-window mesh premise;
its N-dependent admissible temporal threshold remains the established one.
All estimates below are uniform in volume and in meshes satisfying these
premises. The common coupling interval depends on fixed N and is nonzero.
The new creator-velocity unitary is denoted V; it is not identified with
the earlier common-filter spectral-flow unitary.

**Theorem.** There is a selected positive self-adjoint contraction
G_infinity on the product-vacuum Hilbert space, obtained strongly from
the ACTUAL Perron-normalized blocked Wilson transfers in the V chart.
Open boxes and centered periodic exhaustions give the same limit, and

```text
G_infinity Omega=Omega,
||G_infinity-D_infinity||<=epsilon,
||G_infinity|Omega^perp||<=q0<1.
```

Its complete physical neutral charge-odd plaquette island has an
orthogonal Riesz projection Pi. If P0 is the complete free shell,

```text
||Pi-P0||<=epsilon/(g_star-epsilon)<=1/9.
```

For the literal normalized odd plaquette multiplication sources
O_p=(chi_p-chi_bar_p)/sqrt(2), the full synthesis operator
J a=sum_p a_p alpha(O_p)Omega is bounded and obeys ||J-J0||<1/8,
where J0 is the free plaquette isometry. The projected map Pi J is a
bounded bijection from ell^2(Z^3) tensor C^3 ONTO Ran Pi, with

```text
(312481/419904) I <= J*Pi J <= (81/64) I,
312481/419904 > 9/16,
||(Pi J)^(-1)||<=648/559<6/5.
```

The corresponding orthonormalization is a unitary onto the complete
band and intertwines translations. The same band and literal-source
frame occur in the selected full physical quantum GNS representation
and in the reflection-positive Euclidean multiplication-history
reconstruction. No equality between their entire high-energy Hilbert
spaces is needed or inferred.

Its actual blocked and fine-time vacuum correlations have an
electric-time exponential gap at least

```text
Delta_el >= -log(q0)/s1 > 0.
```

The inequality is a transfer-gap statement and requires no assertion
that G_infinity is injective on its entire high-energy complement.
On the isolated band, G is bounded away from zero, so -(1/s)log G is
a bounded self-adjoint band-energy operator. Its band is nonzero in the
Euclidean reconstruction because the literal projected frame is onto
and bounded below.

The proof now supplies the operator limit, physical free-window passage,
whole-family source bound, infinite-dimensional onto argument, and
joint-time/Euclidean identification in that order.


## 2. The product space and actual transfer limit

Let H_0 be the incomplete tensor product of the countable link Hilbert
spaces with their unit Haar vacua. Equivalently,

    H_0 = C Omega direct-sum
          direct-sum_{finite nonempty I} tensor_{i in I} H'_i.

For a finite link set S, let H_S denote its full tensor Hilbert space
with the vacuum outside S, embedded in H_0. The union of the H_S is
dense; each H_S may be infinite dimensional.

Write D_i=P_i+d_i for the free blocked link kernel, with
0<=d_i<=delta_kin(1-P_i) and delta_kin=exp(-gamma s)<=4/5.
The incomplete product D_infinity is the direct sum of
tensor_{i in I}d_i over exact supports I, with value one on Omega.
It is a positive contraction. Its norm on the nonvacuum space is at
most delta_kin. Products D_{S complement} are defined in the same way and
commute with operators supported in S.

### 2.1. Exact ambient independence of induced activities

For each finite X in the infinite lattice, construct its own induced
Wilson model, new creator-velocity unitary V_X, normalized blocked
transfer G_X, and partition activity F_X. The induced model retains
exactly the plaquettes fully contained in X. Thus F_X is a single
bounded operator attached to X, independent of any larger ambient box.
This is exact, not merely stabilization of Taylor coefficients.

The frozen weighted theorem gives

    F_X*=F_X,  F_X P_X=P_X F_X=0,
    sup_i sum_{X contains i} 2^|X| ||F_X|| <= eta_act,

and F_X=0 unless X is a connected plaquette footprint. On every finite
Gamma its partition expansion reconstructs its actual normalized transfer

    G_Gamma = V_Gamma^* T_Gamma^m V_Gamma / b_Gamma.

In particular G_Gamma is a positive contraction fixing the product
vacuum. This uses the ACTUAL Perron normalization, not an auxiliary
parent energy.

### 2.2. Strong limit with a local Hilbert-space bound

For a finite family C of pairwise disjoint activity supports define on
H_0

    Theta_C = (tensor_{X in C} F_X) tensor D_{(union C) complement}.

The empty family gives D_infinity. If psi belongs to H_S, every nonzero
Theta_C psi has X intersect S nonempty for every X in C. Otherwise that
factor acts on its local vacuum and vanishes, irrespective of the
other, disjoint activities. In particular at most |S| activities survive
in one family. Put

    a(S)=sum_{X intersects S}||F_X|| <= |S| eta_act.

Dropping disjointness in the positive majorant gives

    sum_{C nonempty} ||Theta_C psi||
       <= (exp(a(S))-1)||psi||.

Hence D_infinity psi plus this activity series converges absolutely and
uniformly on the unit ball of every H_S. It defines a linear operator
on the dense union of those subspaces.

For an open finite volume Gamma put

    A_Gamma = G_Gamma tensor D_{Gamma complement}.

Its activity expansion is exactly the preceding series restricted to
X subset Gamma. If S subset Gamma, the omitted part is bounded by

    ||(G_infinity-A_Gamma)psi||
       <= exp(a(S)) a_out(S,Gamma)||psi||,
    a_out(S,Gamma)=sum_{X intersects S, X not subset Gamma}||F_X||.

Indeed mark one omitted activity and bound the remaining nonnegative
family sum by exp(a(S)). For a box containing the radius-R link-graph
neighborhood of S, connectedness forces every omitted support to have
at least R links, and the primitive majorant gives the convenient bound

    a_out(S,Gamma)<=|S| eta_act 2^(-R).

The deliberately weaker exponent avoids a boundary convention for
whether the outer layer has radius R or R+1.

Each A_Gamma is a positive contraction. Consequently the densely
defined limit extends to a positive self-adjoint contraction G_infinity
on H_0, and A_Gamma converges strongly to it. Positivity and
self-adjointness follow from bounded strong convergence of the quadratic
forms. The preceding tail bounds are stronger than pointwise convergence: they
are uniform on the local Hilbert-space unit ball, without a finite
representation cutoff.

The frozen finite-volume norm theorem gives

    ||A_Gamma-D_infinity||
       =||(G_Gamma-D_Gamma) tensor D_{Gamma complement}||
       <= epsilon.

Passing to the strong limit proves

    G_infinity Omega=Omega,
    ||G_infinity-D_infinity||<=epsilon.

The ordinary embeddings G_Gamma tensor I have the same strong limit:
on any fixed H_S they agree with A_Gamma once Gamma contains S, and all
are contractions. Norm convergence on the entire H_0 is not asserted.

### 2.3. Centered periodic volumes

Embed a centered torus's link factors into a centered cube of H_0. On
any fixed faithful interior neighborhood its induced activities agree
EXACTLY with the open-lattice F_X, since no wrapping plaquette is
retained there. All remaining activities that can act on H_S must both
meet S and exit that neighborhood. Their intrinsic torus connected
support cardinalities are therefore at least the neighborhood radius.
Apply the preceding marked-family tail bound separately to the torus
and open tails. This proves the
same local Hilbert-space limit, with at most twice the displayed tail
bound. It does not give a false ambient diameter estimate for wrapping
plaquettes. Free factors are identical under the link-factor embedding.

## 3. Physical free window and complete close projection

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
    c=exp(-4 gamma s),  d=exp(-5 gamma s),  c-d>=g_star.

Here P_0 is the COMPLETE free odd plaquette shell, the closure of its
orthonormal translated plaquette vectors. It is naturally isomorphic to
ell^2(Z^3) tensor C^3. In particular the hypothesis is the full physical
window, not just a one-link kinetic gap.

Let H be a Hilbert space, P0 an orthogonal projection, Q0=I-P0, and

    D = c P0 + D_Q,   D_Q=Q0 D Q0 <= (c-g) Q0,   g>0.

Here D and G are bounded self-adjoint operators and ||G-D||<=epsilon<g/2.
Positivity is useful for the eventual transfer interpretation but is not
needed for this lemma. Work inside the physical odd Hilbert space, so that
no vacuum eigenvalue above the free plaquette shell is present.

The self-adjoint resolvent Neumann bound puts the spectrum of G inside

    (-infinity,c-g+epsilon] union [c-epsilon,c+epsilon].

Let P=1_(c-g/2,infinity)(G), Q=I-P. The same P is the Riesz projection
around c of radius g/2. Then

    delta=||P-P0|| <= epsilon/(g-epsilon) < 1.

Proof without a finite-rank assumption: put E=G-D, G_P=G restricted to
Ran P and G_Q=G restricted to Ran Q. For X=Q0 P and Y=Q P0,

    D_Q X - X G_P = -Q0 E P,
    G_Q Y - Y c = Q E P0.

Since sup spectrum(D_Q)<=c-g and inf spectrum(G_P)>=c-epsilon,

    X = integral_0^infinity exp(t(D_Q-(c-g)))
                 Q0 E P exp(-t(G_P-(c-g))) dt.

The integral converges in operator norm and has norm at most
epsilon/(g-epsilon). It solves the Sylvester equation; uniqueness follows
by applying the same exponentially decaying conjugation to a homogeneous
solution. Similarly

    Y = -integral_0^infinity exp(t(G_Q-c)) Q E P0 dt

has that bound. Finally ||P-P0||=max(||Q0P||,||QP0||), proving the claim.
This also establishes the needed bound on both defect spaces; no dimension
comparison is hidden in the argument.

The simpler circular-contour bound is
2epsilon/(g-2epsilon). The Sylvester bound uses the one-sided free complement and
is stronger. Apply this with g=g_star and epsilon=1/998<g_star/10. Therefore delta<=1/9 for the complete actual physical odd projection Pi=P.

## 4. Uniform tagged literal-source control

In this section the path parameter t runs from zero to one, independently
of the blocked electric time s. Let S(t) be the V-chart generator,
rho_plus=1+log(2), and

```text
g(t)=sup_i sum_(Y contains i) exp(rho_plus|Y|)||S_Y(t)||,
G_int=integral_0^1 g(t)dt,
r=u_star/4,
q=145 exp(3rho_plus)|u|/r.
```

The established primitive majorant gives G_int<=E<=(568/145)q and
q<=1/10000 on |u|<=u0. Each assigned coefficient preserves the physical
symmetries and is charge even. The literal sources satisfy

```text
O_p=(chi_p-chi_bar_p)/sqrt(2),
||O_p||<=sqrt(2)N=:c_N,
e_p=O_p Omega.
```

By the retained physical free-window theorem the e_p are orthonormal
and span Ran P0. Thus J0 a=sum_p a_p e_p is the isometry from the full
plaquette coefficient space. The actual transported literal synthesis
is J a=sum_p a_p alpha(O_p)Omega, initially on finite sequences. The
following estimate proves its bounded extension, not merely bounds on
individual source columns.

Keep the source label `p` throughout the commutator expansion. Assign its
initial operator to its four-link plaquette. Every later commutator with
`S_X` is assigned to the union of intersecting input supports. Thus

```text
V* O_p V-O_p = sum_(Y contains p) A_(p,Y),
|Y|>=4,
```

where `Y contains p` means that `Y` contains all four anchor links.
Retain separate labels even when several terms have the same support.
For a tagged family `A`, use

```text
||A||_rho^tag
 =sup_i sum_p sum_(Y contains i) exp(rho|Y|)||A_(p,Y)||.
```

All terms have the same odd charge-conjugation character as `O_p`,
because each local generator coefficient is even. Hence

```text
<Omega_Y,A_(p,Y)Omega_Y>=0.
```

This zero expectation holds term by term. Subtracting the expectation
of the total dressed source alone would not justify the disjoint-support
orthogonality used below.

We prove the required norm estimate for the forward source evolution
`C'= [S,C]`. The inverse conjugation uses the time-reversed generator
`-S(1-t)` and has the same integrated norm. Write

```text
C(0)=C0,  (C0)_(p,Y)=O_p if Y=p and zero otherwise,
A(t)=C(t)-C0,
rho0=log(2)+1/2,
rho(t)=rho0-2 integral_0^t g(v)dv.
```

At most four plaquettes contain a link, so

```text
||C0||_(rho0)^tag <=4 exp(4rho0)c_N=64 e^2 c_N=:C_*.
```

The exact inhomogeneous equation is

```text
A'=[S,A]+[S,C0],  A(0)=0.
```

As in the chart's source theorem, the decreasing support weight cancels
the moment in which the root lies in the source support. Since
`rho_plus-rho(t)>=1/2`,

```text
M1(S;rho(t)) <= (2/e)g(t) <=g(t).
```

The remaining homogeneous contribution to the upper Dini derivative is
at most `2g(t)||A||^tag`. For the inhomogeneous term, each initial
source has cardinality four, and therefore

```text
||[S,C0]||_(rho(t))^tag
 <=2g(t)M1(C0;rho(t))+2M1(S;rho(t))||C0||_(rho(t))^tag
 <=(8+4/e)g(t)C_* <=10g(t)C_*.
```

The same pointed-support inequality holds with source tags because all
their sums are nonnegative and the tag is unchanged by a commutator.
Integrating the scalar inequality gives

```text
||A(1)||_(rho0-2G_int)^tag
 <=5 C_* (exp(2G_int)-1)
 <=10 G_int exp(2G_int) C_*.
```

If `G_int<=1/4`, weakening the final weight to `log(2)` yields

```text
D:=||A(1)||_(log(2))^tag
 <=640 e^2 c_N G_int exp(2G_int).
```

The estimate is on the whole tagged family. Bounding each source
individually would not control synthesis from arbitrary square-summable
plaquette coefficients.

### 4.1. From source bounds to a synthesis operator

Set

```text
f_(p,Y)=A_(p,Y)Omega,
F_p=sum_Y f_(p,Y)=(V* O_p V-O_p)Omega.
```

Each term belongs to the tensor factor on `Y`, with vacuum spectators,
and has zero local vacuum expectation by charge oddness. Consequently

```text
<f_(p,Y),f_(q,Z)>=0 when Y and Z are disjoint.
```

All assigned supports have cardinality at least four. The tagged norm gives

```text
sup_i sum_q sum_(Z contains i) ||f_(q,Z)|| <=D/16,
```

because `2^(-|Z|)<=1/16`. For each fixed `p`, choose any one anchor link
`i in p`; every `Y` of that source contains `i`. Since
`n 2^(-n)<=1/4` for integers `n>=4`,

```text
sum_Y |Y| ||f_(p,Y)|| <=D/4.
```

The disjointness and preceding moment bounds give the absolute Gram row bound

```text
sum_q |<F_p,F_q>|
 <=sum_Y ||f_(p,Y)||
      sum_(q,Z: Z intersects Y) ||f_(q,Z)||
 <=(D/16) sum_Y |Y|||f_(p,Y)||
 <=D^2/64.
```

The Gram matrix is Hermitian, so its column sum has the same bound.
The Schur estimate proves that `a ->sum_p a_p F_p` extends from finite
sequences to an operator of norm at most `D/8`. Together with the tagged norm estimate,

```text
||J-J0|| <=80 e^2 sqrt(2) N G_int exp(2G_int).
```

This proof needs no finite-rank dimension estimate. It works directly
on an infinite plaquette index set once the local source limits exist.
Alternatively, apply it to arbitrary finite coefficient sets and pass
their columns to the locally convergent infinite-volume source chart.
Uniformity preserves the Gram and synthesis bounds. Zero extensions at moving boundaries
are not claimed to converge in the global rooted supremum norm.

### 4.2. The common source interval

On `|u|<=u1=u0/(8N)`, the linear relation defining `q` and the primitive majorant give

```text
q<=1/(80000N),
G_int <=(568/145)/(80000N)=71/(1450000N) <=1/(20000N).
```

Use `e^2<9`, `sqrt(2)<3/2`, and `exp(2G_int)<2`, valid here since
`G_int<=1/4`. Then the synthesis bound implies

```text
||J-J0|| <=2160 N G_int <=2160/20000=27/250<1/8.
```

The additional reduction depends on fixed rank `N` but is independent
of spatial volume and temporal mesh. It is strictly positive for every
fixed `N>=3`. No claim of a rank-uniform interval is made.

## 5. Direct rotation and complete source-frame range

For arbitrary orthogonal P,P0 with delta<1, define

    K=P-P0,
    R=P P0+(I-P)(I-P0),
    S=(I-K^2)^(1/2),
    U=R S^(-1).

Exact multiplication gives

    R*R=RR*=I-K^2,
    R P0=P R,
    [S,P]=[S,P0]=0.

Thus U is a unitary, U P0=P U, and it maps Ran P0 onto Ran P. This is a
direct rotation, not merely an isometric embedding. It also obeys

    U+U*=2S,
    ||U-I||=sqrt(2(1-sqrt(1-delta^2))) <= sqrt(2) delta.

Let E be a coefficient Hilbert space and J0:E->H an isometry onto Ran P0.
Then A0=P J0 has the exact factorization

    A0=U S J0.

Consequently A0 is a bounded bijection E->Ran P, with

    A0^(-1)=J0* S^(-1) U* restricted to Ran P,
    sqrt(1-delta^2)||f|| <= ||A0f|| <= ||f||.

This proves surjectivity in infinite dimension. The lower bound alone
would not prove it.

### 5.1. Perturbed sources and complete range

Suppose the actual source synthesis J:E->H is bounded and

    ||J-J0|| <= eta < sqrt(1-delta^2).

This is the norm of the entire synthesis operator, not a bound
on each source column separately. Set A=PJ. On the coefficient space,

    A = A0 (I+B),
    B=A0^(-1) P(J-J0),
    ||B|| <= eta/sqrt(1-delta^2) < 1.

The convergent operator-norm Neumann series for (I+B)^(-1) proves A is a
bounded bijection onto the complete spectral range Ran P. In particular

    (sqrt(1-delta^2)-eta)^2 I <= J*P J <= (1+eta)^2 I,
    ||A^(-1)|| <= 1/(sqrt(1-delta^2)-eta).

Its polar normalization W=A(A*A)^(-1/2) is a unitary E->Ran P. If P,J0,J
intertwine translations, so do the inverse, Gram normalization and W.
With E=ell^2(Z^3) tensor C^3 this identifies the complete band as a
three-component translation representation. Exponential decay of the
orthonormalized band kernel needs a weighted kernel estimate in addition
to the plain operator-norm statement here.

Convenient exact sufficient constants are

    epsilon<=g/10,   delta<=1/9,   eta<=1/8.

Since sqrt(1-delta^2)>=1-delta^2>=80/81,

    ||Af|| >= (559/648)||f|| > (3/4)||f||,
    A*A >= (559/648)^2 I > (9/16) I,
    ||A^(-1)|| <= 648/559 < 6/5.

No finite-volume rank argument, source-by-source extrapolation, or
infinite-dimensional compactness is needed in this onto argument.

## 6. Actual GNS and fine-time transfer identification

Use the new-chart automorphism alpha, with finite convention
alpha_Gamma(O)=V_Gamma^* O V_Gamma. The established local operator-norm
limit gives the selected actual vacuum state

    omega_W(O)=<Omega,alpha(O)Omega>.

For its full local-quantum GNS representation the map

    W: pi_W(O)Omega_W -> alpha(O)Omega

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

### 6.1. Fine temporal steps from the positive block root

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

## 7. Euclidean reconstruction and complete band cyclicity

For the physical Wilson interpretation use the algebra M of bounded
local gauge-invariant neutral multiplication sources. On this algebra
the finite kinematic vacuum correlations equal the gauge-projected
Wilson correlations, because the vacuum and all intermediate vectors
remain gauge invariant. Gauge-variant time histories are not needed.

Let a positive-time multiplication history F have factors f_0,...,f_k
and time increments n_1,...,n_k. Associate the vector

    v_F=alpha(f_0) G_fine^n_1 alpha(f_1)
                     ... G_fine^n_k alpha(f_k)Omega.

Products at the reflection slice combine in the commuting algebra
alpha(M). The exact finite transfer identity identifies
<v_F,v_H> with the limit of the reflection-positive Wilson form
<Theta F H>. The preceding joint-time limit proves existence of all these limits. Thus the
OS quotient by its zero-norm histories, followed by completion, is
unitarily represented onto

    K=closure span{v_F} subset H_phys.

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

    Pi J_p belongs to K for every p.

The source and direct-rotation arguments above prove that Pi J maps
ell^2(Z^3) tensor C^3 ONTO Ran Pi. Consequently the projected-history
identity and closedness imply Ran Pi subset K. Therefore the entire full-quantum
physical band is present in the OS representation, with no omitted
source-invisible band state. Conversely K reduces G, so its spectral
projection on the island is precisely the restriction of Pi. Hence

    OS isolated band = Ran Pi,

unitarily, with the actual transfer and all projected source vectors
intertwined. In the full physical GNS space the band is
W^*(Ran Pi), and its projection is W^* Pi W.

This proves selective source cyclicity on the COMPLETE isolated band.
It neither assumes nor needs K=H_phys, or cyclicity of only equal-time
multiplication operators on every high-energy quantum state. Those
global equalities are not prerequisites for this band identification. The proved literal frame
surjectivity is the substantive input that rules out a hidden band
complement; a lower frame bound alone would not suffice at infinite rank.

## 8. The actual electric-time vacuum gap

The vacuum line is fixed and its orthogonal complement reduces
G_infinity. From its full-space norm bound and D_infinity|Omega^perp<=4/5,

```text
||G_infinity|Omega^perp||<=q0=4/5+1/998<1.
```

Thus the vacuum eigenvalue one is simple, and for centered vectors xi,eta
and integer block time n,

```text
|<xi,G_infinity^n eta>|<=q0^n ||xi||||eta||
 <=exp(-n s[-log(q0)/s1])||xi||||eta||.
```

The same inequality holds in the full physical GNS and OS spaces by the
unitary identifications and reducing restriction. This is a genuine
positive mass lower bound in the fixed lattice's calibrated electric-time
units, independent of admitted volume and mesh. The positivity of the
fine transfer root gives, for every integer n>=0,

```text
||G_fine^n|Omega^perp||<=q0^(n/m)
 <=exp(-n tau[-log(q0)/s1]).
```

The nonzero
isolated odd band has a complete literal-source frame and a bounded
band logarithm, so this is not only a vacuum clustering assertion.

## 9. Exact contribution to the Yang-Mills continuum objective

The result establishes an actual infinite-volume Wilson transfer gap,
a complete physical excitation band, and nonvanishing total literal
sources at fixed spatial lattice spacing. It also identifies that band
inside Euclidean reconstruction. These are concrete operators and
spectral subspaces available for temporal Hamiltonian matching and
renormalization arguments. No source-visible pole is being substituted
for a complete spectral range.

It does not yet construct a four-dimensional continuum Yang-Mills
field theory or a continuum mass gap. The project's existing
[continuum bridge](G19_CONTINUUM_BRIDGE_INSERT.tex) distinguishes the
necessary next scale statements:

* The proved interval is the small magnetic-coordinate regime. In the
  Hamiltonian coordinate u=g_H^(-4), an asymptotically free trajectory
  has u(a)->infinity as the spatial lattice spacing a tends to zero.
  Its tail is outside this fixed strong-coupling interval. A controlled
  continuation or renormalization/coarse-graining theorem must relate
  these regimes; the present estimate does not extrapolate between them.
* To obtain a finite positive physical gap one must control the physical
  electric-energy prefactor, temporal/spatial anisotropy and the coupling
  scheme along that scale trajectory, and prove uniform bounds for the
  corresponding renormalized spectral measure. The positive number
  -log(q0)/s1 is in calibrated lattice electric-time units; it is not
  automatically a scale-uniform physical mass after a->0.
* A continuum limit must retain gauge invariance, reflection positivity,
  nontriviality and the regularity/covariance properties needed for the
  continuum reconstruction. The established finite/thermodynamic OS
  transfer and band are inputs to those limiting arguments, not their
  conclusion. The project separately records which blocking and
  reflection-factorization hypotheses remain to be proved.
* The physical shell and normalized character sources used here are the
  established SU(N), N>=3 inputs. The abstract creator, contour and
  close-projection lemmas are dimension independent, but a claim for
  every compact simple gauge group requires that group's calibrated
  physical free window, source normalization and corresponding
  representation/center-sector analysis. In particular an SU(2) charge-
  odd fundamental-character difference is identically zero, so it cannot
  be obtained by silently reusing this source choice.

These are explicit downstream hypotheses. They do not undo the fixed-
spacing actual Wilson theorem proved here, and they locate its exact
contribution to the larger continuum goal.

## 10. Evidence and provenance

The analytic inputs are the pinned rooted-contraction, symmetric-creator,
cardinality-chart and weighted-activity proofs linked above, together
with the calibrated physical kinetic window. This note consolidates the
independent actual operator/OS construction, the tagged source synthesis
bound and the Sylvester/direct-rotation onto argument. Exact finite
controls test the rational constants, projection identities, Gram
certificates and counterexamples to weaker totality criteria. They do
not substitute for the infinite-dimensional operator proofs here.

The theorem uses the new V chart throughout. The common-filter chart's
excited action and activity norm are not identified with it. No spatial
continuum or all-compact-simple-group completion is claimed.
