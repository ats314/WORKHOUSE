# 23. The swap-odd domino state derives leak = hop, and the vacuum route is not why

Date: 2026-09-03. Status: accepted — U4 refuted on its own second falsifier,
the equality it named promoted from observed to derived.

## Context

Asked to use the theory graph to find a novel path, the session ranked the
graph's own residue rather than the prose: gaps with no route and no check,
unifying candidates with one edge, values shared by nodes with no edge
between them. U4 stood out — a `conjectured` candidate with exactly one
edge, a falsifier with two clauses, and an equality nobody had derived:
the domino engine finds the C-even per-neighbour leakage and the C-even
hopping equal at both orders it computes, `-11/306` and `-6335/249696`, and
the corpus explains it as "the diagonal's +3/4 (vacuum-energy bookkeeping)
and the hop's +3/4 (the |0⟩ route) are distinct mechanisms with equal
value". U4 sharpened that into a mechanism — one vacuum-mediated route
entering both, at every order — and the charge-even suite, rightly, verified
the equality and refused to assert a cause.

The engine's definitions are the whole key. On the domino's C-even manifold
`span{e_1, e_2}`, `e_i = χ_i + χ̄_i`, it sets `t_k = ⟨e_1|h_k|e_2⟩` and
`leak_k = (⟨e_1|h_k|e_1⟩ − vac_k^domino) − gap_k^single`. So

    leak_k − t_k = E_k(ψ_A) − vac_k^domino − gap_k^single,   ψ_A = e_1 − e_2,

and the identity is a statement about the **swap-odd** C-even state: its
energy is the domino vacuum plus one free single-plaquette excitation.

## What was derived

Two facts about `ψ_A`, each machine-checked in
`src/workhouse/invariants/swap_odd.py`, engine-free.

1. **The swap-odd lemma.** Class functions multiply commutatively, so
   `W ψ_A = (χ_1+χ̄_1)² − (χ_2+χ̄_2)²`: the mixed products cancel identically
   and the two vacuum overlaps are the same number. `W ψ_A` has no
   two-plaquette image and no vacuum image. `H_0 = 2Cas⁽¹⁾ + 2Cas⁽²⁾ + cross`
   conserves each plaquette's isotypic content, so through third order no
   two-plaquette intermediate can return to that image. Hence `E_k(ψ_A)`
   for `k ≤ 3` is the single-plaquette rotor energy computed with the vacuum
   removed from its intermediates. For the C-odd state `o_1 − o_2` the lemma
   fails in exactly one place: the pair `χ_1χ̄_2, χ̄_1χ_2` survives.

2. **The |0⟩ route is minus the vacuum energy.** An engine-free SU(3) rotor
   — irreps `(p,q)`, `E = 2C_2`, multiplicity-free fusion, des Cloizeaux to
   third order — reproduces the engine's spectral gates: vacuum
   `(0, −3/4, −9/32)`, towers `13/20, 1/2, 101/200, 7/32`. The vacuum's share
   of the excited C-even energy is `3/4 = 1/C_F` at order 2 and `9/32` at
   order 3: the same matrix element `⟨0|W|e⟩ = |e|²` over `2C_F`, with the
   sign of the denominator flipped. Two names, one number.

Together: `E_k(ψ_A) = E_k^exc − route_k = E_k^exc + vac_k`, and with
`vac_k^domino = 2 vac_k` (no connected vacuum diagram below fourth order)
that is `leak_k = t_k`. The third check reads the domino's registered
third-order numbers through `ψ_A`: `D3_even − T3_even = −23/400`, the
vacuum-free rotor energy, a prediction the engine never gated in that form
and meets with numbers computed for other gates.

The same bookkeeping in the other sector is the control. The C-odd rotor
has no vacuum share at any order (`⟨0|W|o⟩ = 0`), and its swap-odd state
keeps the like-family pair, so `leak_(2,−) − t_(2,−) = 2A_N + 1/C_F`:
`−3/68` at `N = 3`, the registered value, and not `2B_N + 1/C_F = −1/36`.
That decides which family the surviving pair carries, and it is why the
C-odd sector separates while the C-even one does not.

## Decision

U4 is `refuted` on the second clause of its falsifier — a derivation for a
reason that does not involve the vacuum route. The vacuum does not enter
`ψ_A` at all; it cancels out of it. The equality stands, both rationals
keep their registered values, and it moves from observed to derived.

What stays open is the all-orders half, and the derivation says where it
stops. The lemma keeps two-plaquette intermediates out of `E(ψ_A)` only
while a walk cannot excite the inert plaquette and de-excite it again,
which takes four insertions; the domino vacuum acquires its first connected
diagram at the same order. So

    leak_(4,+) − t_(4,+) = [connected (excited, fluctuating-neighbour) diagram]
                         − [connected domino vacuum diagram],

two quantities no symmetry relates. That difference is the sharpened
falsifier, recorded on U4: zero would be a cancellation this derivation
does not predict, nonzero ends the identity at the first order the mechanism
cannot reach. It is not a byproduct of G3 — G3's weight cards are the cubic
fourth-order kernel on three-plaquette lattice clusters, while this needs the
two-plaquette domino at order four, past the pinned engine's degree-four
word basis. It is costed as an untried route on G25.

## Consequences

- `ledger/gaps.yaml`: U4 `status: refuted`, with the derivation and the
  fourth-order falsifier; `constants.py` and the charge-even check's detail
  stop calling the mechanism the vacuum route.
- Four T1 checks, suite "the swap-odd domino state", yielding
  `E_VAC_SINGLE_2 = −3/4`, `E_VAC_SINGLE_3 = −9/32`, `E_PSI_A_3 = −23/400`,
  `ODD_SWAP_GAP_2 = −3/68`. The four tower coefficients the coupling and su3
  suites carry as literals are now derived from the irrep ladder.
- The graph found this one. The candidate had been sitting with one edge
  since 2026-08-28; the two files that decide it, the engine's definitions
  and the corpus's "distinct mechanisms" sentence, were never read together.

## Addendum, 2026-09-03: the disconnected half of the fourth-order falsifier

The G25 route's cheap part ran the same day. Within one C-parity sector the
rotor's excited level is nondegenerate, so Rayleigh–Schrödinger reaches
fifth order in exact rationals, agreeing with the des Cloizeaux blocks
through third. Two of its fourth-order numbers already existed in the corpus
by other routes and match to the digit: the one-face vacuum `−39/1280` the
v10a.7 Hodge engine gates as a float, and the size-1 cluster row `143/8960`
of `m_Γ⁽⁴⁾`. Both are now T1.

The number that matters is new. The vacuum's share of the excited C-even
energy plus the vacuum energy is `0, 0, 0` at orders one to three — that is
the identity — and `−63/800` at order four. So the disconnected half of the
falsifier does not vanish:

    leak_(4,+) − t_(4,+) = 63/800 + conn_A − conn_vac.

The corpus already holds `conn_vac`: the v10a.7 engine gates the two-face
vacuum linked `O(u⁴)` weight `ω₄ = −327/83776`, the same for coplanar and
perpendicular pairs, with zero linked `O(u²)` and `O(u³)` — exactly the
"no connected vacuum diagram below fourth order" the derivation assumed.
It is a float gate at a stated tolerance with rational recognition, T3
here. Taken as read, U4's all-orders equality survives fourth order if and
only if the connected swap-odd excited diagram is

    conn_A = ω₄ − 63/800 = −173109/2094400.

Nothing in the corpus computes that number. It is the one remaining
quantity, and it needs SU(3) recoupling between two-plaquette states or the
engine's word calculus at letter degree five. The route stays `live` on G25
with that target written down.
