# A contour-to-activity theorem with an explicit rooted tree bound

5 September 2026. Independent analytic derivation for the weighted-activity
continuation. This note concerns a replacement creator-velocity unitary,
not the previously fixed common-filter spectral-flow gauge.

## 1. Precise contour hypotheses

Let Lambda be finite, with arbitrary site Hilbert spaces. The free contour
propagator is a tensor product of contraction cocycles R_i(t,s), on a
finite ordered contour 0<=s<=t<=T. Thus

    R_i(t,r) R_i(r,s)=R_i(t,s),  ||R_i(t,s)||<=1.

Identity segments and positive-time kinetic heat segments are permitted.
Unbounded kinetic generators enter only through these bounded contraction
propagators. Put D_i=R_i(T,0).

Specify a subsystem-consistent collection of bounded insertion operators
J_A(t) supported in finite nonempty A. On a subsystem Gamma retain exactly
the terms whose named supports A lie inside Gamma. Named supports can be
larger than the smallest operator support; this allows a scalar multiple
of the identity to carry its connected active-plaquette witness. Multiple
primitive terms with the same named support may be combined or retained
as separate labels. Assume measurability sufficient for the norm bounds
and Dyson integrals below, and define

    a_A = integral_0^T ||J_A(t)|| dt.

This consistency assumption is essential. A bound on the generators of
separately constructed finite systems is not by itself a bound on such a
common interaction family. For the proposed replacement chart, connected
multivariate coefficients and their named active supports are how this
hypothesis is to be established.

Let G_Gamma be the free-contour Dyson evolution with those insertions.
For finite Gamma the series converges absolutely whenever sum_{A subset
Gamma} a_A<infinity. The rooted hypothesis below implies this condition.

## 2. Exact connected operator activities

For an ordered word of insertions A_1,...,A_n, join distinct insertion
vertices j,k when A_j intersects A_k. Repeated supports are allowed and
are distinct vertices of this graph. Define F_X by summing all nonempty
Dyson words whose graph is connected and whose union of named supports
is exactly X. On the sites of X include their entire free-contour
propagation before, between and after the insertions.

Then

    G_Gamma = sum_{C a family of pairwise disjoint nonempty subsets of Gamma}
                (tensor_{X in C} F_X) tensor
                (tensor_{i in Gamma outside union C} D_i).          (1)

The empty family gives the free product. The justification is exact:
every insertion word has a unique partition into overlap-connected
components, whose support unions are disjoint. Operators belonging to
different components commute as tensor factors. Free propagation on one
component telescopes across insertion times belonging to another, by the
cocycle law. Summing all time-order shuffles of the component words fills
the product of their individual ordered integration domains. This gives
their tensor product, with no additional factorial. Repeated insertions
and noncommuting operators within a component are retained in their
original time order.

Absolute finite-volume convergence justifies this regrouping. Taking
norms only after preserving that order gives

    ||F_X|| <= sum_{n>=1} 1/n!
                 sum_{A_1,...,A_n: union A_j=X, overlap graph connected}
                    product_{j=1}^n a_{A_j}.                        (2)

To see the factor 1/n!, sum the positive scalar ordered-integral bounds
over every support word. The connectedness and union restrictions are
invariant under simultaneously permuting the integration variables and
support labels. Hence the full cube integral is n! times the ordered
one, and its scalar integrand factorizes into the integrated costs a_A.
This step never rearranges a noncommuting operator product.

## 3. Rooted tree majorant

Let kappa>=0, h>0, and suppose

    epsilon = sup_i sum_{A contains i} exp((kappa+h)|A|) a_A <= h.   (3)

Then the exact activities satisfy

    sup_i sum_{X contains i} exp(kappa |X|) ||F_X|| <= epsilon.      (4)

In particular one may use h=1 and epsilon<=1. If epsilon<=1/400, this
meets the basic excited-window threshold whenever kappa>=log(5/4).

### Proof

Write b_A=exp(kappa|A|) a_A. The factor exp(kappa|union A_j|) is at most
product_j exp(kappa|A_j|). To bound the rooted sum in (2), mark one
insertion support containing i. This can only overcount it, and replaces
1/n! by 1/(n-1)! after designating that insertion as vertex 1. For a
connected overlap graph, the number of its spanning trees is at least
one. Thus the marked positive sum is bounded by the corresponding sum
over rooted labelled trees with overlapping supports along every edge.

Let T_A denote this rooted-tree sum with root support A. In formal
nonnegative series, or by successively bounding trees of increasing
height, its recursion is

    T_A = b_A exp(sum_{B: B intersects A} T_B).                    (5)

The exponential counts the unordered collection of rooted child trees;
its child factorials are exactly the labelled-tree 1/(n-1)! convention
above. It includes arbitrarily many repeated support labels.

The nonnegative family t_A=b_A exp(h|A|) is a supersolution, since

    sum_{B intersects A} t_B
       <= sum_{j in A} sum_{B contains j} exp((kappa+h)|B|) a_B
       <= |A| epsilon <= h|A|.

Starting the height recursion at zero proves T_A<=t_A for every finite
height; monotone convergence proves it for all rooted trees. Therefore

    sum_{A contains i} T_A
       <= sum_{A contains i} exp((kappa+h)|A|)a_A <= epsilon,

which proves (4). No division by 1-epsilon and no Hilbert dimension occur.

## 4. Why anchoring and self-adjointness can be imposed afterwards

Suppose additionally that every full subsystem transfer G_Gamma is
self-adjoint and fixes its product vacuum, each D_i fixes its vacuum,
and G_i=D_i. Then the F_X extracted by the contour equal the activities
from the established induced-subsystem partition extraction theorem.
Indeed (1) recursively determines F_Gamma from G_Gamma and proper
subsystems, and F_i=G_i-D_i=0.

Induction gives self-adjointness because the subtracted proper-family
terms are tensor products on disjoint supports. Applied to the product
vacuum, every nonempty proper-family term vanishes inductively; the
remaining G_Gamma and free product both fix the vacuum. Thus

    F_X P_X=P_X F_X=0.

The separate magnetic, unitary and scalar-counterterm contour pieces
need not have locally anchored activities individually. The exact vacuum
condition of their full normalized product provides that cancellation.
This avoids imposing an unjustified termwise anchoring hypothesis on
the unexpanded contour.

For the Wilson application, the contour consists of the two inverse
unitary legs, the magnetic pulses of the actual integer block, its free
kinetic heat segments, and the scalar Perron normalization. The full
product is V_Lambda^* T_Lambda^m V_Lambda/b_Lambda. Here V is the new
creator-velocity unitary. Its excited-space action need not equal that
of the previously fixed common-filter unitary U.

## 5. Independent audit of the proposed primitive costs

Assume the new-chart construction supplies the following coefficient
facts on a common polydisk of radius r=u_star/4:

* Its generator coefficient at a connected active-plaquette multiindex
  alpha of degree n has operator norm at most |Y_alpha| r^(-n)/3,
  with named support |Y_alpha|<=3n+1.
* At a fixed link, the number of such rooted degree-n multiindices is at
  most 4*145^(n-1).
* The scalar logarithmic Perron normalization has coefficient bound
  |ell_alpha|<=n s_1 J e r r^(-n).

These are inputs to this particular numerical substitution, not premises
needed for the general contour theorem. Put rho=kappa+1 and

    q=145 exp(3rho) |u|/r < 1.

The two unitary legs then have total primitive norm at most

    [8 exp(rho)/435] q(4-q)/(1-q)^2.                             (6)

This follows by summing (2/3)*4*145^(n-1)*(3n+1)
exp(rho(3n+1))(|u|/r)^n. The two legs account for the leading factor 2.
The scalar primitive norm is at most

    [4 exp(rho)/145] s_1 J e r q/(1-q)^2,                        (7)

and the magnetic pulses contribute at most

    4 exp(4rho) s_1 J |u|.                                     (8)

The scalar coefficient bound has a direct check. In the endpoint magnetic
creator flow,

    c_p=z_p <Omega, v_p exp(W) Omega>.

Every right creator in a surviving term lies inside p; otherwise an
excited link outside p survives the vacuum bra. The total norm of those
creators is at most 4R, with R=1/4. Hence |c_p|<=r J exp(4R)=rJe.
Only p in the active multiindex can contribute to its coefficient, giving
at most n such terms. Integrating over m magnetic intervals costs
m tau<=s_1. This proves the stated n s_1 J e r coefficient bound by
polydisk Cauchy, assuming the common analytic flow and connected
coefficient locality supplied by the construction.

At rho=1+log(2), use e<3 and |u|<=u_star/1,252,800,000. Then
|u|/r<=1/313,200,000 and q<=1/10,000. If s_1 J r<=1, (6) is below
4.5e-5, (7) below 5e-5, and (8) below 1.7e-5. Their sum is safely below
1/2500. All three expressions are monotone in the indicated positive
parameters. The condition s_1 J r<=1 follows very conservatively from
the first branch of u_star and s_1 gamma<1 at the rounded spectral block.

Consequently, once the listed analytic-coefficient inputs are proved,
the contour theorem gives the stronger bound

    sup_i sum_{X contains i} 2^|X| ||F_X|| <= 1/2500 < 1/400.

This implies the required (5/4)^|X| bound for the NEW chart. It cannot be
reported as a bound for the previously fixed common-filter activities.

## 6. Evidence scope

Sections 1-4 give the analytic contour theorem under explicit consistency
and primitive-norm hypotheses. Section 5 independently checks the scalar
normalizer estimate and sums the proposed primitive majorants. No
representation truncation, selected-matrix-element bound or assumption
that overlapping operators commute is used. The remaining application
inputs are the common-polydisk creator-velocity construction, its
connected coefficient locality and the stated rooted multiindex count.

The companion `check_contour_tree_majorant.py` uses exact rational
arithmetic to compare the connected-word and rooted-tree coefficients
through order seven on a three-support overlap chain, including repeated
supports (28 root/order comparisons). It also checks the conservative
numerical primitive bound exactly:

    total <= 1999940003/18121375181250 < 1/2500.

Both controls passed. They check the combinatorial normalization and
scalar arithmetic; the general operator and infinite-tree statements
are the analytic arguments above.
