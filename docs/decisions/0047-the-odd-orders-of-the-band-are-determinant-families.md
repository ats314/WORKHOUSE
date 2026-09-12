# 47. The odd orders of the band are determinant families: none for even N, none below order N − 2 for odd N

Date: 2026-09-11. Status: accepted. Bears on G16, G14, G6; changes no claim's
status. Source: `paper/research_notes/ODD_ORDER_CENTRE_PARITY_20260911.md`,
registered as `RESULT:ODD_ORDER_CENTRE_PARITY`.

## Context

ADR 0046 established that the order-2k band coefficient is N⁻⁽⁴ᵏ⁻¹⁾ for
k = 1, 2 and wrote the band, relative to the plaquette energy, as a series in
τ² = (β/N³)² with N-independent limits. It said nothing about odd orders. The
corpus holds a full third order at SU(3) — `B_3 = 1975/124848`, `t_3+`,
`leak_3`, the towers `7/32` and `101/200`, `d_3 = −109151/249696` (MASTER
§4.4, the domino engine's 251 gates) — and a first-order `+u`, and the
symbolic-N engine of ADR 0029 had never been asked about an odd order. The
question was whether the odd orders obey an N-power law of their own.

## What was derived

They obey something sharper. Every Haar integral of the strong-coupling
expansion needs net flux `0 mod N` on every link. The link set T (x-links at
even y, y-links at even z, z-links at even x) meets every plaquette of Z³ an
odd number of times, so summing the link fluxes over T modulo 2 counts the
face words of a history modulo 2. Hence:

1. **Even N: no odd order, ever.** For even N every link flux is even, so
   every surviving history has an even number of face words; an order-m
   element has m + 2 words and every fold term contains an odd-order factor.
   Every odd-order element of the des Cloizeaux operator vanishes
   identically, on every cluster, in both C-parity sectors, at every order.
2. **Odd N: nothing below order N − 2.** An odd-word history has a link of
   odd flux, so of |flux| ≥ N, so touched by at least N words: `m + 2 ≥ N`.
   At `m = N − 2` all N words traverse that link the same way and, because
   two plaquettes through a link meet only there, they are all one face's:
   the only surviving element is the one-plaquette vertex between a face and
   its conjugate.
3. **The vertex in closed form.** On one plaquette the states are characters
   and W adds or removes a box; the only path from F to F̄ = Λᴺ⁻¹ in N − 2
   steps is through the columns Λᵏ, so with `E_k − E_0 = (k−1)(N−k−1)(N+1)/N`

   `H_{N−2}(F̄, F) = −(N/(N+1))^{N−3} / ((N−3)!)²`,

   which is −1 at N = 3 (the first-order vertex, `+u` C-odd) and −25/144 at
   N = 5.

## What the third engine confirms

`runs/odd_order_band_2026-09-11`; suite "the odd orders of the band are
determinant families (G16)", seven T1 checks. The third-order des Cloizeaux
operator, built in `loopcalc` for the first time, reproduces at N = 3 the
entire SU(3) third-order ledger from an engine independent of the domino
engine in every primitive, with the vacuum route `⟨1|H₃|1⟩ = −9/32` supplying
the corpus's vacuum subtraction exactly. At N = 4 and 6 every first- and
third-order element is zero; at N = 7 everything is zero; over ℚ(N) the eight
third-order pair elements are identically zero, so the third order has no
balanced-family content at any rank. A second, one-plaquette character engine
(Pieri rule, Rayleigh–Schrödinger series per C-parity sector) agrees with
`loopcalc` on every tower and vacuum energy at N = 3, 4, 6, 7, gives the
N = 5 split ±25/144 where the word engine's five-box determinant families are
too expensive, and confirms the vertex at N = 7 and 9 (orders 5 and 7) with
every lower odd order zero; the word engine's N = 5 hops and X-touched
leakages are zero.

## Decision

Record the theorem and the vertex, and read the corpus's third order as
what it is: an SU(3) determinant-family effect, not the odd member of a
rank-uniform series. For G16 this makes the absence of odd τ-terms exact at
every fixed order in the planar limit. The first odd term of odd N sits at
order N − 2, and with `u = N²τ/2` its size relative to the plaquette energy
is `(e²τ/2)ᴺ` up to a power of N — exponentially small below τ = 2/e² ≈ 0.27
and exponentially large above it. That threshold is an observation about one
term, not a convergence statement about the series.

## Consequences

- G16's detail records that the strong-coupling band is an even series in u
  for even N, and through order N − 3 for odd N; the even orders' N⁻⁽⁴ᵏ⁻¹⁾
  law and the overlap theorem are untouched.
- The fourth-order exceptional-rank treatment of N = 4, 5, 6 in the corpus
  (GLUEBALL v3.1 §4) is the even-order face of the same counting: a
  determinant family at order m needs N ≤ m + 2.
- G9's sixth-order clusters carry no odd-order contamination at any even N,
  and none at odd N ≥ 9.
- `loopcalc` now has the third order; `odd_order.effective` returns H₁, H₂,
  H₃ on any cluster at any rank, and its N = 3 values are a third,
  independent certification of `B_3`, `T3_EVEN`, `LEAK_3`, `D_3` and the
  domino diagonals.
