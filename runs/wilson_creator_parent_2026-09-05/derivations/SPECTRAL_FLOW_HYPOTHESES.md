# Spectral flow for the Wilson-vacuum parent family

Independent primary-source audit and application argument, 5 September 2026.
Draft only. The creator estimates and parent gap below are WORKHOUSE inputs;
the application and boundary comparison are spelled out separately from the
external theorem statements.

## 1. Exact primary-source locators and the on-site dimension issue

**BMNS:** Bachmann, Michalakis, Nachtergaele, Sims,
[arXiv:1102.0842v2](https://arxiv.org/pdf/1102.0842v2).
Assumption 2.1 and Proposition 2.4, printed pages 3-5, give finite-volume
spectral transport for a self-adjoint path with bounded derivative and an
isolated spectral interval with uniform separation; Hilbert-space dimension
is unrestricted. However, Section 5, printed pages 21-22, explicitly
restricts its thermodynamic Theorems 5.2 and 5.5 to finite-dimensional
on-site spaces. The abstract alone therefore does not justify applying
those thermodynamic theorems directly to Wilson rotors.

**NSY:** Nachtergaele, Sims, Young,
[arXiv:1810.02428](https://arxiv.org/pdf/1810.02428).
Section 3.1.1 allows general on-site Hilbert spaces. Assumption 6.12,
printed page 78, requires self-adjoint strongly C1 interactions satisfying

    sum_{Z contains x,y}(||Phi_Z(s)||+|Z| ||Phi'_Z(s)||)
        <= C(s) F(d(x,y)),                              (SF)

with bounded measurable C and F(r)=exp(-g(r))/(1+r)^xi.
Theorem 6.14, printed page 81, assumes g(r)>=b r^theta, b>0,
0<theta<=1, and establishes the thermodynamic spectral flow; equation
(6.122) gives its norm limit on local observables. Theorem 6.3 gives exact
spectral transport. Theorem 7.4, printed page 85, transports selected limit
states. Definition 3.7 and Theorem 3.8 give interaction/dynamics continuity;
Section 7.1, printed page 84, explicitly discusses volume-dependent
interactions converging locally uniformly in this norm. Consistent normal
product-state expectations are used in Section 4 and equations (6.117)-(6.118).

These are the relevant references, rather than a finite-spin theorem
informally extrapolated to an infinite-dimensional link space.

## 2. WORKHOUSE input to be recorded explicitly

Fix a real coupling u in a strict subdisk of the common Wilson creator
domain, for example |u|<=u_star/8 once the weighted estimates below have
been proved there. Parameterize the path by u(s)=s u, 0<=s<=1. Work on
the cubic lattice of links with a fixed finite-range graph metric d.
The number of links in a radius-r ball is O((1+r)^3).

The parent construction supplies actual symmetric-vacuum creators
w_X^Lambda(u), their compatible limit w_X^infinity(u), and:

1. A support weight mu>=log(2) and rooted norm at most 1/8, uniformly in
   finite volume and along the real path. The creators vanish at u=0.
2. Holomorphy on a strictly larger complex coupling disk.
3. Exact coefficient locality: a nonzero degree-n coefficient has a
   connected active-plaquette cover of at most n faces; coefficients in an
   interior neighborhood agree once the requisite cluster fits.
4. Consequently, after reducing the coupling disk, exponential decay in
   the minimum connected-face cover, including a positive decay margin;
   the same holds for the derivative in s by Cauchy estimates on a larger
   disk. Differences between finite-volume and infinite-volume coefficients
   obey the corresponding locally uniform decay estimate.
5. The exact finite-volume parent gap is at least 247/256, and its unique
   ground vector is the actual finite-volume Wilson Perron vacuum.

Item 4 has the following direct quantitative proof from items 1-3. Put
a=1/8, r=u_star/2, beta_plus=log(5/2), and
z=exp(beta_plus)|u|/r<=5/8. Cauchy gives
||w_n||_mu<=a r^(-n), and a degree-n coefficient has cover number at most n.
Consequently, with M0(mu,beta;w) denoting the rooted sum weighted by
exp(mu|X|+beta rho(X)),

    sup_{0<=s<=1} M0(mu,beta_plus;w(su))
        <= a z/(1-z) <= 5/24,
    sup_{0<=s<=1} M0(mu,beta_plus;partial_s w(su))
        <= a sum_{n>=1} n z^n = a z/(1-z)^2 <= 5/9.      (0)

Their sum is at most 55/72. The stronger cover weight leaves a margin
beta_plus-log(2)=log(5/4)>0, and retaining support weight mu/2 leaves
another positive margin mu/2. These larger cover-weight sums do not
replace the original support-only bound a=1/8 used in the gap estimate.

Here differentiation of (su)^n contributes n u^n s^(n-1), and
s^(n-1)<=1, including n=1 at s=0. Uniform convergence of the differentiated
series justifies this calculation. For two volume/root families agreeing
through degree N, the corresponding weighted tails are bounded by

    2a z^(N+1)/(1-z),
    2a z^(N+1)((N+1)-N z)/(1-z)^2,

respectively. These bounds decay exponentially in the distance from the
root to the boundary, or the injectivity scale for a torus, since every
witness through an order proportional to that distance fits. They are
uniform in s. For a periodic system, cover number and diameter are
intrinsic torus quantities; see Section 5a before comparing them with
the fixed infinite-lattice metric. A weighted difference of periodic and
infinite families is compared on a fixed embedded neighborhood, where
the metrics and cover numbers agree for large L; exterior terms are
estimated separately in their own intrinsic metrics. No whole-family
ambient cover-weight difference bound is asserted for a cut-open torus.

A bound only on exp(mu|X|) would not control the diameter of a disconnected
exact support X. The connected-cover statement is the mathematical step
that repairs that specific issue.

## 3. One consistent infinite-volume interaction

Let a_X(s)=|w_X^infinity(su)><Omega_X|, embedded by the identity. Define a
self-adjoint interaction on finite link sets by

    Phi_Z(s) = 1_{Z={i}} q_i - |Z|(a_Z(s)+a_Z(s)^*)
             + sum_{X union Y=Z} |X intersection Y| a_X(s)^* a_Y(s).
                                                               (1)

The singleton term means q_i if Z is the singleton {i}, and zero
otherwise. Terms with empty intersection have zero coefficient. The
quadratic sum is self-adjoint because exchanging X,Y takes adjoints.
At each finite Z, (1) is a finite sum of bounded operators.

For every finite link set Lambda, summing (1) over Z subset Lambda gives

    Hhat_Lambda(s)
      = sum_{i in Lambda}(q_i-Ahat_i,Lambda(s))^*
                            (q_i-Ahat_i,Lambda(s)),
    Ahat_i,Lambda(s)=sum_{X subset Lambda, X contains i} a_X(s).
                                                               (2)

This is exactly the parent of the truncated infinite creator family.
Indeed q_i a_X=a_X and a_X^*q_i=a_X^* when i belongs to X, and counting
the admissible i gives |X| and |X intersection Y| in (1). Thus the
finite-volume Hamiltonians in (2) are restrictions of ONE interaction;
they are not merely a collection of unrelated parents.

Restriction cannot increase the rooted norm. The generic parent-gap
proof therefore applies to every Hhat_Lambda along the whole real path:
its zero space is one-dimensional and its gap is at least 247/256.
Its ground vector need not equal the actual finite-Lambda Wilson vacuum.
That comparison is handled in Section 5 below.

One may set the fixed on-site Hamiltonians in the spectral-flow framework
equal to zero and include q_i in Phi. In particular, no unbounded Wilson
electric generator is being differentiated or conjugated in this use of
spectral flow. All local parent terms and their path derivatives are bounded.

## 4. Checking the interaction norm rather than assuming it

Write rho(X) for the minimum number of faces in a connected cover of X.
Choose a harmless convention for singletons. Only two geometric facts
are needed: diam(X)<=c0+c1 rho(X), and, whenever X intersects Y,
rho(X union Y)<=rho(X)+rho(Y). The union of connected face covers sharing
a link is again connected in the shared-link face graph.

Equation (0) gives eta=mu>=log(2), beta=beta_plus, and B<=55/72 with

    sup_s sup_i sum_{X contains i}
        exp(eta|X|+beta rho(X))
        (||w_X(su)||+||partial_s w_X(su)||) <= B.         (3)

Use retained weights eta=mu/2 and beta=log(2) when estimating the
interaction. The discarded positive margins absorb any fixed polynomial
in support or cover sizes. For the quadratic terms in
(1), use ||a_X^*a_Y||<=||w_X|| ||w_Y|| and write the overlap count as
sum_i 1_{i in X intersection Y}. To sum terms whose union contains a root
x, distinguish x in X and x in Y. For example,

    sum_{X contains x} b_X sum_{Y intersects X}|X intersection Y| b_Y
      = sum_{X contains x} b_X sum_{i in X} sum_{Y contains i} b_Y
      <= (sup_i sum_{Y contains i}b_Y)
                            sum_{X contains x}|X|b_X.   (4)

Exactly the same counting works with the exponential cover weight, by
the two subadditivity inequalities for a union. Derivatives replace one
factor b by its derivative bound. The additional |Z| in (SF), as well as
the linear prefactor |Z| and overlap counts, are absorbed by the positive
support-weight margin in (3). Thus, for some k>0 and C0<infinity,

    sup_s sup_x sum_{Z contains x} exp(k diam(Z))
           (||Phi_Z(s)||+|Z| ||partial_s Phi_Z(s)||) <= C0.
                                                               (5)

This yields a pair bound C0 exp(-k d(x,y)). Choose, for example,

    F(r)=exp(-k r/2)/(1+r)^5.

The remaining factor (1+r)^5 exp(-k r/2) is bounded. The cubic-link
geometry has growth exponent 3, so this F has the required summability
and convolution properties. Equation (SF) follows with a finite constant.
Norm differentiability of each Phi_Z is stronger than strong C1.

For open boxes the same fixed-metric estimates hold uniformly for the
interaction Phi^Lambda built from actual w^Lambda. For periodic boxes
they hold in the intrinsic periodic metric, with the same constants;
they do NOT imply a uniform ambient F-norm after a wrapping interaction
has been embedded into a fundamental domain. On every fixed interior
set of link labels, both
Phi^Lambda and its derivative converge uniformly in s to Phi. There are
only finitely many subsets in such a fixed set, and the positive decay
margin controls the remaining tails. This verifies the local interaction
convergence needed for the open-box comparison. The periodic comparison
requires the extra intrinsic-metric argument in Section 5a.

## 5. Comparing actual finite-volume parents with restrictions

The finite-volume Wilson parents have Phi^Lambda in place of Phi. Their
spectral-flow parameter can use a single gap cutoff smaller than 247/256,
for example gamma_flow=1/2. Choose the same filter and the same normal
product-state conditional expectations for all volumes.

For open boxes, here is the local-limit argument behind using the volume-dependent
version, rather than claiming Phi^Lambda is literally a restriction:

* Uniform interaction bounds give uniform Lieb-Robinson estimates for
  the physical-time dynamics of all these bounded parent Hamiltonians.
  On any local observable, the dynamics for Phi^Lambda and restrictions
  of Phi have the same limit, uniformly for s and bounded time intervals:
  first restrict to a large fixed neighborhood, then use local interaction
  convergence there; the exterior error is uniformly small by locality.
* The spectral-flow generator is a filtered time integral of evolved
  derivative terms. For a fixed local derivative term, truncate its time
  integral to [-T,T]. The omitted norm is bounded by its norm times the
  L1 tail of the common filter. The remaining integral converges by the
  preceding dynamics comparison and local derivative convergence.
* Decompose these filtered terms with the common product-state conditional
  expectations into successively enlarged supports. Their uniform
  locality estimates have summable moments after spectral filtering;
  the original exponential decay is sufficient for this. Truncating this
  support decomposition and the original derivative-support tail leaves
  finitely many local comparisons. Sending Lambda to infinity, then the
  support and time truncations to infinity, shows that both constructions
  have the same local limit for the spectral-flow interaction.
* Applying the local dynamics comparison to the two spectral-flow
  interactions gives the same quasi-local automorphism alpha_s. The
  comparison is uniform on the unit ball of every fixed local observable
  algebra and uniform in s. Reverse flows converge as well, so the limit
  is an automorphism, not just an endomorphism.

This uses local convergence with uniform tails, never the false assertion
that zero-extended finite boxes converge globally in a supremum over all
roots. Boundary-dependent terms need not be globally small.

### 5a. Periodic boxes: use their intrinsic metric before taking the local limit

Take centered cubic tori of side L tending to infinity, with L>=3.
Use their link graph in which two links are adjacent if one plaquette
contains both. A wrapping plaquette has intrinsic diameter one even if
its chosen fundamental-domain representatives are O(L) apart. Accordingly
the periodic interaction is not declared to have uniform F-norm in the
ambient metric. The following comparison avoids that false inference.

The torus graph balls obey |B_L(x,R)|<=C(1+R)^3 with C independent of L.
For R below a fixed fraction of L, they are quotients of balls of the
infinite cubic-link graph; for larger R, the bound follows from the total
number 3L^3 of links. Uniform polynomial growth implies uniformly bounded
sums of F0(r)=(1+r)^(-5). The convolution constant is uniform as well:
for each intermediate z, either d_L(x,z)>=d_L(x,y)/2 or
d_L(z,y)>=d_L(x,y)/2. Combine that dichotomy with the triangle inequality
for the exponential factors in F(r)=exp(-b r)F0(r), then sum the other
factor. This bounds the convolution by a fixed multiple of F(d_L(x,y)).
All finite-volume Lieb-Robinson constants therefore use the same data.

For any fixed finite observable support S and radius R, the intrinsic
R-neighborhood of S embeds isometrically into the infinite lattice once
L is sufficiently large. In that neighborhood the local creator
coefficients and derivatives have the same stabilized Taylor terms.
The remainder bounds in Section 2 are uniform and decay with L.

First compare the physical-time parent evolutions. Restrict the torus
parent Hamiltonian to terms wholly supported in this embedded neighborhood.
For times |t|<=T, the uniform Lieb-Robinson restriction estimate bounds
the change on an observable B in A_S by

    C_T ||B|| sum_{x in S} sum_{y outside B_L(S,R)} F(d_L(x,y)),

with C_T independent of L. Uniform growth and summability make this
small as R increases, uniformly in L. On the fixed neighborhood, the
interaction and derivative coefficients converge in norm, so its
dynamics converge to the corresponding infinite-lattice restricted
dynamics. The analogous restriction error on the infinite lattice is
also small. Thus the full torus dynamics converge on A_S, uniformly
on its unit ball, in s, and for bounded time intervals. The order of
limits is: fix R,T; let L tend to infinity; then increase R,T as needed.

Next use the same spectral filter on all tori and the infinite lattice.
Its time tail is uniformly integrable. For a derivative term with fixed
local support, truncate the filter integral at T and use the preceding
dynamics convergence. The finite-volume conditional expectations are
formed with the same normal product vacuum state; on an embedded
neighborhood they agree with the infinite-system conditional expectations.
The filtered-term localization estimates depend only on the uniform
metric growth, F constants and filter. They therefore have the same
summable tails on every torus. Split their support expansions into a
fixed-radius interior part and the remaining tail. The interior part
converges termwise; the tail is uniformly small. This proves local
convergence of the torus spectral-flow interactions to the same
infinite-lattice interaction as in the open-box construction.

Finally repeat the first restriction/dynamics argument for these
spectral-flow interactions, using their summable, generally slower
decay function instead of the original exponential F. It follows that
the torus spectral flows converge to alpha_s uniformly on the unit ball
of every fixed A_S and uniformly in s. Reverse flows obey the same
argument. Wrapping terms have been controlled through intrinsic
distance to the fixed root, never through a nonexistent uniform
ambient interaction norm.

Consequently both open-box exhaustions and centered periodic exhaustions
select the same local automorphism and state. This extra argument is
what makes the periodic application precise; a bare citation of a
fixed-metric local-convergence theorem would omit it.

## 6. The selected actual Wilson state and its GNS representation

Use the convention alpha_Lambda,s(B)=U_Lambda(s)^* B U_Lambda(s), with
U_Lambda transporting the free parent ground projection to the ground
projection at s. The actual finite-volume parent ground projection is
the actual Wilson vacuum projection. For every local bounded observable B,

    omega_W,Lambda(su)(B) = omega_0(alpha_Lambda,s(B)).

Section 5 therefore gives the full, rather than subsequential, selected
local limit

    omega_W(su)(B) = omega_0(alpha_s(B)).                 (6)

The limit is independent of the compared admissible exhaustions. The
product vacuum omega_0 is pure, and an automorphism preserves purity;
thus this selected state is pure on the full quasi-local link algebra.
This does not claim uniqueness among every abstract state satisfying
some different infinite-volume boundary condition or representation.

There is no residual local-normality problem. Restricted to a fixed
finite local algebra B(H_X), the right side of (6) is the functional-norm
limit of restrictions of finite-volume normal states, because the flow
comparison is uniform on that local unit ball. Normal functionals form
a norm-closed predual. Hence omega_W is locally normal, even though H_X
is infinite dimensional. Mere pointwise weak-star convergence would not
have been enough for this inference.

Let (H_W,pi_W,Omega_W) be its GNS representation and
(H_0,pi_0,Omega_0) the product state's representation. The map

    pi_W(B)Omega_W  |->  pi_0(alpha_s(B))Omega_0          (7)

preserves inner products by (6), has dense range because alpha_s is onto,
and extends to a unitary. Thus pi_W is unitarily equivalent to
pi_0 composed with alpha_s. Equation (7) is the precise automorphic GNS
equivalence. It does NOT assert that alpha_s is implemented by a unitary
inside the original free infinite tensor-product representation, nor
that the untransformed representations pi_W and pi_0 are equivalent.

If the already constructed physical Wilson state is defined by these
same finite-volume Perron expectations on the same bounded local
observable algebra, (6) identifies it directly with this state; uniqueness
of the local limit supplies the identification. If a prior Euclidean
construction has so far only specified a smaller commuting time-zero
algebra, its extension to the present noncommutative observable algebra
must be explicitly matched. Equality on a smaller commuting algebra alone
does not identify every electric or time-dependent observable.

When the parent family is covariant under the retained gauge and global
symmetries, the common spectral filter and invariant product reference
state make alpha_s symmetry-covariant. It then restricts to the invariant
observable algebra. This uses the actual covariance of the creator
family; it is not obtained by assuming a tensor decomposition of the
gauge-constrained Hilbert space.

## 7. What is obtained and what must not be conflated with it

Under the explicit creator norm, holomorphy, connected-cover decay and
local coefficient comparison in Section 2, every spectral-flow assumption
for the bounded parent family is met. Standard spectral flow plus the
local comparison in Section 5 therefore gives a quasi-local realization
of the selected actual Wilson vacuum state, with (6)-(7) providing its
state/GNS meaning. Infinite-dimensional link spaces cause no remaining
domain problem for this bounded parent construction.

The explicit choice |u|<=u_star/8 and estimate (0) supply the positive
weights and local derivative comparison used in (3)-(5). These calculations
should be copied into the canonical application with the independently
proved symmetric-creator coefficient estimates as their stated inputs.

The following conclusions remain outside this argument:

* The quasi-local spectral-flow automorphism need not have strictly
  exponential decay; spectral filtering generally loses some decay.
* It need not equal the old ordered unitary-generator product.
* The parent gap is not a gap theorem for the interacting Wilson transfer
  or its logarithm. Matching the excited operator still requires its own
  full-operator estimates, spectral-range identification, and source bounds.
* No bounded global creator exponential or free-representation implementing
  unitary was introduced in proving the local-limit result.

The specific task remaining before identifying a pre-existing full
Euclidean representation is therefore the explicitly checkable
source-algebra and transfer-representation identification, if it was not
already part of that construction. The selected bounded-local-operator
state itself is uniquely determined by (6). There is no need to assume a
finite representation cutoff or infer a small global similarity condition
number.
