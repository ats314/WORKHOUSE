# The Feshbach channel of the plaquette Hodge algebra

**Date** 2026-09-08. **Bears on** G14 (mechanism of the tier collapse), U2, U3,
C2. **Machine certification** the statements below marked *checked* are T1 in
the suite `the Feshbach channel of the plaquette Hodge algebra`
(`src/workhouse/invariants/hodge_feshbach.py`), exact Laurent identities over
the whole Brillouin zone with no tolerance. Everything else is stated as
conjecture or prediction and marked so.

## The question this answers

G14 asked why the degree-3 part of `d^dagger H_4 d` vanishes when the two-hop
enumeration produces it. ADR 0019 reduced that to the Hodge form

    H4 = -nu~ (L_up - 2) + u S^2 - pi~ S + sigma~ I - 2 C_shp R,

with `S = L_down - 4I` and `R` the cross-plane half of `S`, and observed that
"on the carrier every term but the last is a scalar". That is an observation
about one kernel. U3 asks for the statement one level up: a single fact about
the Feshbach projection `Q` that specializes to the cubic tier collapse and to
the pentagonal proper-return vanishing, in two unrelated geometries.

## The splitting (checked)

At each Bloch point the plaquette fibre is three-dimensional and

    L_down + L_up = q I   per plane component,   L_down L_up = 0,

so `L_up = q I - L_down` on the fibre and the two kernels are complementary:

    C psi  (+)  psi^perp  =  ker L_down  (+)  ker L_up.

`psi` is the cube-boundary carrier, `L_down psi = 0` is homological protection.
Therefore **the Feshbach complement is a Hodge summand**: `Q` is exactly the
orthogonal projector onto `ker L_up`. This is the structural fact everything
below rests on, and it is the reason the Feshbach problem for this geometry is
solvable in closed form rather than order by order.

Two immediate corollaries, both checked:

- `Q L_down psi = Q L_up psi = Q S psi = 0`. Neither Hodge generator leaves the
  retained sector. The Hodge algebra generates **no Feshbach coupling at all**
  — no resolvent, no intermediate state, nothing to expand.
- `R` does leave it, and its excitation `phi = Q R psi` satisfies
  `L_up phi = 0` identically. Every excursion off the retained sector in this
  geometry is an `R` insertion, and it lands in the up-harmonic summand.

## The word calculus (checked)

Write `sigma(W) = psi^dagger W psi` for a word `W` in the generators
`(S, U, R)` with `U = L_up`, and call `sigma(W) - q prod_g eps(g)` the word's
*Feshbach defect*, where `eps(g) = sigma(g)/q`. A zero defect means the word
never actually leaves the carrier and its value is the product of its letters'
carrier eigenvalues.

Of the 39 words of length at most three, exactly seven have nonzero defect:
`RR, RRR, RRS, RRU, RSR, SRR, URR`. The selection rule is exact and is not
"two R's":

> a word has nonzero Feshbach defect **iff** it contains two `R` insertions
> with no `U` between them.

`RUR` factorizes and `RSR` does not, because the intermediate letter acts on
`phi`, and `L_up phi = 0` while `S phi` does not vanish. The defect of `RUR` is
`phi^dagger U phi = 0`; the defect of `RSR` is `phi^dagger S phi != 0`.

Every word with at most one `R` has the closed-form carrier symbol

    sigma(W) = (-4)^#S (-2)^#R q^(#U + 1 - #R) e_2^#R,

verified word by word. The monomials reached are `q^n` and `q^n e_2 / q`: the
`c_0`, `A` and `4C` tiers of the shape ansatz. **Neither `q e_2` nor `e_3` is
populated at R-degree one or zero.**

## The mechanism of the tier collapse (checked)

The recorded fourth-order kernel is linear in `R`, with coefficient
`-2 C_shp`. With the previous paragraph that is the whole mechanism:

> `B_shp = D_shp = 0` because the fourth-order kernel enters the Feshbach
> channel exactly once, and one entry reaches only `e_2`.

There is nothing to cancel, at any rank, and the statement is a property of the
operator algebra rather than of the 189 records or of the six-orbit structure.
It supersedes nothing in ADR 0019 — it explains it.

It also says something about C2 that was not visible before: **`C_shp` is the
amplitude of the unique generator of the Feshbach channel.** The disputed
coefficient and the tier collapse are the same structural fact seen twice, and
the dispute's two branches are two values for how strongly the retained sector
couples to its own complement. Nothing here adjudicates them, and nothing here
changes the standing of either recorded value.

## What two insertions unlock (checked identity, conjectural relevance)

`sigma(RR) = q e_2 + 3 e_3` exactly. So the `R^2` channel carries the
B-monomial and the D-monomial **locked at 1 : 3**: any order whose degree-3
tier is carried by `R^2` alone has `D = 3 B`, and a measured departure
localizes the other defective words rather than being a free fit parameter.

`sigma(RUR) = 4 e_2^2`, with zero defect. Its shape symbol `4 e_2^2 / q` is
**outside** the span of the ansatz's cleared monomials `{q, q^2, e_2, q e_2,
e_3}` — an exact rank test, recorded as a `FINDING:` check. U2 says the
obstruction space is spanned by elementary symmetric polynomials in the `a_i`
and nothing else appears; the algebra that produced the fourth-order kernel
contains a word whose carrier symbol the four-shape ansatz cannot hold at all,
however its coefficients are fitted.

**This is a prediction, not a result.** Whether the sixth-order dynamics
populates `RUR`, `RSR` or `R^3` is open (G9, G10). ADR 0005 is why that
sentence is written twice: a degree bound was once read off a vertex count,
predicted the `L^-4` tier first at sixth order, and was retracted. The
statements here are Laurent identities of the recorded operators; the only
thing they say about order six is conditional on which words it turns on.

## The general form, offered as U7

The cubic half of U3 is now derived rather than observed. The general
statement it suggests:

> Let the retained sector be the line spanned by `psi`, where `psi` spans
> `ker L_down` and is an eigenvector of `L_up`. Then the Feshbach complement is
> a Hodge summand, every history whose operator is a word in the Hodge algebra
> is scalar on the retained sector and shape-inert, and all shape dispersion is
> carried by non-Hodge insertions.

**That hypothesis is the corrected one, and the correction matters.** The first
draft asked for `L_down + L_up` to be a scalar — link regularity — because that
is what the cubic lattice does. The pentagonal prism refutes it: five links on
a cap, four on a side, so the sum is `diag(6, 6, 5, 5, 5, 5, 5)`. Had the
over-strong version stood it would have excluded the very geometry U3 is about.
The weaker hypothesis is checked in all three (`L_up psi = 4 psi` on the
tetrahedron, `7 psi` on the prism, `q psi` on the cubic lattice), and it is
enough: a word in the two Laplacians ending in `L_down` annihilates the
carrier, one ending in `L_up` rescales it.

Under it the "two vanishings" of U3 are two specializations: the cubic tier
collapse is R-degree one, and the pentagonal proper-return vanishing is that
proper returns are Hodge words. The tetrahedral data point already recorded —
primitive proper returns are exactly scalar on the face space, so their
traceless compression is zero — is the same statement in the geometry where
the Hodge algebra is one-dimensional.

Its falsifier is stated in `ledger/gaps.yaml` under `U7`, and it is not
satisfied by anything in this note: the pentagonal and tetrahedral halves are
not computed here. What this note establishes is the cubic half, exactly.
