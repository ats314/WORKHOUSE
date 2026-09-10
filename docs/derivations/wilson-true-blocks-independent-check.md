# Independent check of the BA20-BA26 true-vacuum block estimates

9 September 2026. An independent re-derivation of
`wilson-true-vacuum-block-estimates.md`, read against VA12, VA14 and VA19 in
`wilson-vacuum-aligned-assembly.md`. The audited file is unmodified; its
SHA-256 as checked is the one recorded in
`docs/validation/wilson-true-blocks-2026-09-09.json`, and that record still
matches for the derivation, its validation script and the invariants module.

The verdict is that BA20-BA26 do what they claim. Nothing fatal or major was
found. Every defect located runs in the direction of under-claiming, and two
of them are recorded below as strengthenings. This is a different outcome from
the September 9 GPU run audited in `yangmills-gpu-resolution-audit.md`, and the
difference is structural rather than a matter of degree: that run inserted the
constants it needed, and this derivation constructs them.

## CB1. What was re-derived independently

The rational envelope reproduces. With alpha=1/32000, D=84 and
x=alpha e^2<x_star=8alpha=1/4000, the pinned sum satisfies
A(x)=x/(1-4Dx)<A_star=x_star/(1-4D x_star)=1/3664.
The equalities concern this rational upper envelope, not A(x):
(D+1)A_star=85/3664<1; 160*3*A_star=480/3664=30/229 exactly; and

    (199/229)*3*(1-9/16000-12/32001)=2.6045428798946513>13/5,
    (229/199)exp(9/16000)(32001/31999)^6=1.15183...<29/25.

The BA21 majorant is valid with room: e^-9(1541/6859)=2.7726*10^-5 dominates
the true sup|p_4-1|, whose leading term is 4e^-12=2.4577*10^-5. The incidence
combinatorics are machine-checked on an explicit side-3 three-slab lattice in
`src/workhouse/invariants/wilson_vacuum.py`: endpoint multiplicity 10, bridge
multiplicity 4, factor degree at most 84, at most 15 time-zero factors per
three-link block. These are the 8*9+4*3=84 and the 5r of BA20 and BA23.

The BA3 reduction was checked line by line rather than accepted. The collapse

    p_b(x,y)/(p_B(x)p_C(y))
       = integral [cross-ratio][p_b(x,y')p_b(x',y)/(p_B(x)p_C(y))]dx'dy'

is an identity because the second bracket integrates to 1 in (x',y'): its two
partial integrals are exactly the two marginals. The cross-ratio is at least
exp(-D_BC) pointwise, so p_b>=exp(-D_BC)p_B p_C. The remainder has mass
1-exp(-D_BC) and, after normalization, exactly the original marginals, which is
what makes the Cauchy--Schwarz step give |Cov(f,g)|<=(1-exp(-D_BC))||f|| ||g||
for centered block functions. BA7 is therefore a theorem about the object VA5
defines, not an analogy to it.

BA1 is a genuine partition of every link with covering multiplicity one: each
positively oriented link has a unique tail, 3 links per vertex times ell^3
vertices gives r=3ell^3, and (L/ell)^3 blocks recover all 3L^3 links. BA8 may
therefore drop the 1/m_* of VA19. The document also meets VA19's explicit
warning head-on rather than around it, in its own words: neighboring blocks
have neighboring link supports even though their centers are ell units apart.
Substituting center separation for link-support separation is precisely the
step that invalidated the block argument in GA9.

## CB2. The single-link partition is stronger, and closes VA12 directly

BA23's counting is generic in r: at most 5r time-zero factors touch a block,
which for a single link is one temporal factor plus the four plaquette factors
of the four plaquettes containing it. Taking each link as its own block gives
r=1 and p_B=4, so the BA2 exponent 4 k p_B t at t=4/epsilon is 64lambda rather
than 144lambda, and the density ratio is squared 2r=2 times rather than six.
The same machinery then yields

    kappa_single-link <=160A_star=10/229,
    gap_phys(H_Lambda) >=(219/229)3epsilon exp(-64lambda)(31999/32001)^2
                       >(2.8679)epsilon,
    0<=lambda<=1/256000, L>=3.                       (CB1)

This is strictly better than the ell=1 block result 30/229 and 2.6045 epsilon,
and it is a bound on the original single-link row sum. VA12, not only its
block variant VA19, therefore closes in this window. The document records only
the block instance and does not claim the sharper one.

## CB3. The angle budget is not graded in lambda

At lambda=0 the ground is constant, mu is product Haar, and every mixed
oscillation D_BC vanishes identically. BA23 nevertheless returns 30/229. The
mechanism is visible in BA21: the two activities enter through a single
envelope alpha=max(sup|a|,sup|b|), and sup|a|<=2.7726*10^-5 is a property of
the free heat kernel at tau=4, independent of lambda, while sup|b|<=8lambda
tends to zero. The budget is therefore pinned by free-kernel bookkeeping and
cannot degenerate to the exact free answer. This is a looseness, not an error;
a two-species activity majorant that keeps the temporal and magnetic factors
separate would grade the bound in lambda and is the natural sharpening.

## CB4. The BA26 wall is more robust than its own derivation

BA26 assumes both factor suprema stay below the same alpha. That hypothesis is
stated, and it reads like a soft spot. It is not one. Relaxing it to separate
budgets alpha_a for the temporal factors and alpha_b for the magnetic factors
gives lambda<=3[-log(1-alpha_b)]/[2log(4/alpha_a)], and the Kotecky--Preiss
criterion itself caps both: (D+1)x/(1-4Dx)<1 with x=alpha e^2 and D=84 forces
alpha<3.2147*10^-4. Maximizing the ceiling over that admissible region gives

    lambda <=5.11*10^-5,                             (CB2)

against 3.986*10^-6 at the document's own alpha=1/32000. A factor of thirteen,
and still finite. Excluding lambda tending to infinity does not depend on the
equal-budget simplification. Two further remarks belong with BA26. First, the
achieved window 1/256000=3.906*10^-6 sits within two percent of the ceiling at
its own alpha, so the window is essentially saturated at that budget, though
alpha is a free parameter and the route's ceiling is an order of magnitude
higher. Second, what BA26 excludes is a uniform sup-norm activity budget, not
the Feynman--Kac polymer route as such; activities controlled in a moment norm
rather than a supremum are untested by it. The document hedges correctly on
this point and names the three alternatives.

## CB5. The two boxed constants must not be chained

BA25 derives the gap directly as gamma_B(1-kappa_blocks) with the exact factor
199/229. Chaining the two boxed results instead gives

    3epsilon(1-9/16000-12/32001)/(29/25)=2.5838epsilon<(13/5)epsilon,

so the gap statement does not follow from the rounded C_AT<29/25. The document
is correct because BA25 does not take that route, but a summary that presents
the pair as a consequence chain invites the wrong inference. The margin on the
gap is 0.175 percent, and it survives only because the rationals are exact.

## CB6. Repairs, all editorial

None of the following changes an estimate. They are recorded so the file can be
tightened without re-auditing it.

1. BA3, after the Cauchy--Schwarz step: "centered" and "their L2 norms" are
   unqualified. Both are taken in the marginals p_B,p_C at the same fixed b,
   not in L2(mu).
2. BA3 reuses p_B for the block link count and for a marginal density. Rename
   the marginals.
3. BA7's disintegration to the maximal correlation, and the gauge-restriction
   step, are asserted in one sentence each; the latter uses the block analogue
   of VA4 without citing it at the point of use.
4. BA20's bridge construction stops at the dyadic skeleton and is not extended
   to the path functional that b actually integrates. One line of Kolmogorov
   continuity closes it.
5. BA20 asserts positivity of the heat transition densities at small dyadic
   times; VA3 supplies this only at tau of order one. The general fact is
   standard for a bi-invariant metric on a compact connected group.
6. BA20's "endpoint variables at times 1,...,N" should read "at the slab
   boundaries j=1,...,N, i.e. times 4,...,4N". Both tau=1 and tau=4 are live in
   this document, so the slip is worth fixing.
7. BA23 never states the premise its cancellation rests on: the expansion is of
   log Zhat, not Zhat, so a cluster touching only one block contributes a term
   depending on one block alone and is killed by the mixed second difference.
8. BA23's ground limit uses uniqueness and positivity of Omega at fixed finite
   volume. That is VA1; cite it at the point of use. The limit itself is sound:
   log Zhat_(4N)(U)=-4N E_0/epsilon+log<Omega,1>+log Omega(U)+o(1), and the
   mixed second difference annihilates both constants.
9. BA25a's full-space C_AT needs the unrestricted row sum, while BA24 states
   the physical one. BA3 proves the pre-restriction bound; record it alongside.

## CB7. What remains open is unchanged

The wall is BA26 and it is correctly placed. Under the VA17 coefficients
k/epsilon=(c_B/c_E)g^-4 tends to infinity, and CB2 shows no redistribution of
the activity budget reaches that regime. The continuum carrier and the
observable-overlap transport of Jaffe--Witten section 6.5 remain unproved, and
the document says so without hedging in the other direction. What BA20-BA25 do
establish, and what VA16 and VA18 both failed to supply, is a strict summable
physical angle budget and a true conditional block floor for the actual vacuum
mu=Omega^2 dU, with constants independent of volume and of the slab count, in
an explicit finite-spacing window.
