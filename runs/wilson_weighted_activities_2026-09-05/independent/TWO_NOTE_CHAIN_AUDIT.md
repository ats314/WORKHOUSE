# Independent review of the two-note weighted-activity proof

5 September 2026. Read in full:

* `paper/research_notes/G18_WILSON_CARDINALITY_UNITARY_CHART_20260905.md`
* `paper/research_notes/G18_WILSON_WEIGHTED_ACTIVITY_BOUND_20260905.md`

Final audited SHA256 values:

```text
G18_WILSON_CARDINALITY_UNITARY_CHART_20260905.md
15ae9409d96220d41c6cf9c77ce7a294bc2760a586d2e0a245235fd02e6e908f

G18_WILSON_WEIGHTED_ACTIVITY_BOUND_20260905.md
45458b4e3666f82563c05c797271e546defe3407ab2e3e16c8620c6b97bdfbb0
```

Verdict: ACCEPTED. The derivation establishes the claimed weighted
activity bound for the replacement creator-velocity chart under the
displayed Wilson, incidence and calibrated-kinetic inputs. The companion
chart theorem, its analytic-coefficient and witness-count premises, the
Perron scalar estimate and all inputs to the contour theorem were checked
in this final review. The conditions listed as application inputs in the
earlier independent contour draft are supplied by this audited chain;
they are not left as additional conjectures. No substantive unresolved
step was found. The general contour lemma now explicitly requires
kappa>=0; this correction was confirmed in equation (12).

## 1. Creator chart

The lowering monomial has one exact output support, including for
entangled creator vectors. Its cardinality equals total left/right
creator cardinality minus the lowering support cardinality. Creators
disjoint from the lowerer cancel as operators. Pointing the output root
at one surviving creator input gives the stated factor two, touching
exponential and M1(w;nu), without an output-projection multiplicity.

T_w is conjugate-linear in the velocity and is inverted on the real
Banach space. The doubled conjugate-Hilbert-space equations are genuinely
holomorphic; they do not continue an adjoint holomorphically. Their
off-diagonal norm bound, real-slice uniqueness and coefficient estimates
were checked. The scalar equation in the transported vector is correct
including its possible phase.

The polydisk proof uses a maximum coupling norm, so it preserves the
rooted contraction constants. The Cauchy circle for t->w(tz) remains
strictly inside the available polydisk. M1<=9/64, theta<=3/16<=1/4 and
||b||<=1/6 are consistent conservative bounds.

Every application of T adds positive coupling degree and joins touching
active witnesses. Finite-order induction therefore gives connected
assigned footprints and exact induced-subsystem coefficient compatibility.
Cauchy on the rooted coefficient family in the minimal active subsystem
gives ||S_alpha||<=|Y_alpha|r^(-n)/3. The conjugate coefficient family has
the same witness property. Assigned footprints, rather than only exact
excited supports, are essential here and are explicitly retained.

The deterministic spanning-tree walk records its visited plaquette set,
so the 144^(k-1) count is valid. Root-face choices and positive
multiplicities give 4*145^(n-1), including repeated marks and periodic
geometries with the stated degree bound.

## 2. Perron scalar and contour

Only creator supports contained in p survive <Omega,v_p exp(A)Omega>.
Their total norm is at most 4R; hence the local bound r J e is valid.
At multiindex alpha, only its active p variables contribute, at most n.
Integrating m times over tau costs m tau<=s1. This verifies the scalar
coefficient n s1 J e r r^(-n), its connected additivity and its convergence.
The exact endpoint normalizer identifies the scalar branch with the
actual Perron eigenvalue on the stated real interval.

A scalar identity may carry a larger named support specifying where its
active variables are retained. This is a support assignment, not a claim
of operator linear independence. It is compatible with induced systems
and with the contour overlap grouping.

Free kinetic factors tensorize. On one connected component, free factors
at insertion times belonging to other components telescope; their full
component contour leaves exactly D_i on each unoccupied link. Time-order
shuffles factor disjoint components and retain the original order within
each component. Thus no overlapping operators are commuted. Absolute
positive bounds justify the regrouping with countably many primitive
coefficient labels at finite volume.

The connected-word 1/n! factor, marked-root 1/(n-1)! factor and rooted
tree recursion are consistent. The supersolution b_Y exp(h|Y|) gives the
same root constant E, not an additional denominator. The independent
replay tests these factors through order seven with repeated support
labels. The final activities equal the induced partition activities by
uniqueness. Consequently self-adjointness and vacuum annihilation hold
after the full connected sum; neither is incorrectly imposed on each
primitive magnetic/unitary/scalar insertion.

## 3. Constants and consequences

The unitary, scalar and magnetic sums were independently recomputed.
Factoring 4 exp(rho)/145, their upper sum is

    q + (e+8/3) q/(1-q)^2,

using s1 J r<=1. At q<=1/2 it is bounded overall by (568/145)q.
For rho=1+log(2), exp(3rho)<216 and u0=u_star/1252800000 give
q<=1/10000. Thus 568/1450000<1/2500 as asserted.

The independent exact rational replay also bounds the primitive total
more sharply by 1999940003/18121375181250 and verifies a positive margin
to 1/2500. Both derivations agree. The transfer perturbation consequence
is exactly

    (1/2500)/(2(1/5-1/2500))=1/998<g_star/10.

The uniform full-operator bound legitimately restricts to the retained
physical neutral odd sector because the new velocity equation and its
unique inverse preserve the stated symmetries. The calibrated free
window then gives the complete isolated finite-volume shell of rank
3L^3 on its periodic lattices. This uses full operator norms and is not
restricted to source-detected states.

## 4. Local sources and scope

The source commutator estimate has two root cases. The decreasing support
weight cancels the term containing M1(A); the stronger generator weight
controls M1(S). This verifies the displayed exponential source factor.
The inverse endpoint unitary is obtained by the time-reversed generator
-S(1-s), so the same bound applies to both conjugations.

Assigned supports retain the original source support even when actual
operator cancellations shrink it. Their rooted estimate at any source
link therefore controls the entire source series. Connected footprints
give the stated spatial factor. Uniform tails and coefficient locality
yield norm limits on local observables, and the inverse limits extend to
inverse automorphisms. This does not require a unitary implementation in
the original infinite product representation.

The notes correctly distinguish V from the old common-filter U and do
not transfer a bound on one set of activities to the other. They also
leave the thermodynamic Riesz range, literal-source frame invertibility
and totality, sharp-shell matching and continuum hypotheses separate.
No global G18/G19 closure follows solely from this result.

## 5. Independent artifacts

* `INDEPENDENT_CREATOR_VELOCITY_AUDIT.md`: tangent estimate and exact
  scalar/phase and component equations.
* `INDEPENDENT_CONTOUR_POLYMER_BOUND.md`: full dimension-independent
  contour theorem and primitive cost audit.
* `check_contour_tree_majorant.py`: passed exact rational replay of 28
  root/order tree comparisons and the displayed smallness constants.

These controls verify their finite combinatorial and scalar statements.
The Hilbert-space, convergence and full operator estimates are the
analytic proofs audited above, not conclusions inferred from sampling.
