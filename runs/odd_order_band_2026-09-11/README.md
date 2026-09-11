# The odd orders of the band are determinant families: the third order at N = 3..7 and over ℚ(N) — 2026-09-11

ADR 0046 gave the even orders of the strong-coupling band their large-N law
and left the odd orders alone. The corpus has a full third order at SU(3)
(`B_3 = 1975/124848`, `t_3+ = −6335/249696`, `leak_3 = −12331/249696`, the
towers `7/32` and `101/200`, `d_3 = −109151/249696`; MASTER_THEORY §4.4, the
domino engine) and nothing at any other rank. This run builds the third-order
des Cloizeaux operator in the third engine (`loopcalc`) for the first time and
evaluates it at N = 3, 4, 5, 6, 7 and over ℚ(N). The theorem it tests is in
`paper/research_notes/ODD_ORDER_CENTRE_PARITY_20260911.md` (ADR 0047).

## What is computed

`derive.py` writes `certificate.json`. All arithmetic is exact.

1. For N = 3, 4, 6, 7, on the single plaquette and on the coplanar and
   perpendicular shared-link pairs: the towers (one-plaquette diagonal), hops
   (pair off-diagonal) and leakages (pair diagonal minus tower) at orders 1,
   2, 3 in both C-parity sectors (`workhouse.invariants.odd_order.band_numbers`),
   with

       H_1 = −P W P,  H_2 = P W R W P,  H_3 = −(P W R W R W P − ½{P W R² W P, P W P}),

   `V = −u W`, `u = β_N/(2N)`, plus the one-plaquette vacuum energies
   `⟨1|H_2|1⟩` and `⟨1|H_3|1⟩` (E₀ = 0).
2. At N = 5, where a one-plaquette history with five words of one face is a
   (5,0) determinant family on four links and the word engine's ε-contractions
   are too expensive: the pair hops and the X-touched leakages by `loopcalc`
   (`pair_third_cheap`, which never meets those families), and the towers and
   vacuum by a one-plaquette character engine (`towers`: Pieri rule for
   `χ_F` and `χ_F̄`, `H0 = 2 C₂`, Rayleigh–Schrödinger series per C-parity
   sector). The character engine is also run at N = 3..11 through seventh
   order and agrees with `loopcalc` on every tower and vacuum at N = 3, 4, 6, 7.
3. The eight third-order pair elements over ℚ(N) in the symbolic engine of
   ADR 0029, where only balanced Haar families exist.
4. The closed form of the first odd-order vertex `−(N/(N+1))^{N−3}/((N−3)!)²`
   at odd N ≤ 13, the centre-parity link set T checked on blocks up to 6³,
   and the theorem's criterion tabulated.

## Result

| N | first order | third-order towers (odd, even) | third-order hops | third-order leakages | vacuum ⟨1\|H₃\|1⟩ |
|---|---|---|---|---|---|
| 3 | ±1 | −1/16, 179/800 (7/32, 101/200 after vacuum subtraction) | −B₃ coplanar, +B₃ perpendicular; t₃⁺ both | −41279/124848 odd, −38281/124848 even (leak₃ = −12331/249696 after vacuum subtraction) | −9/32 |
| 4 | 0 | 0, 0 | 0 | 0 | 0 |
| 5 | 0 | +25/144, −25/144 (characters) | 0 | 0 (X-touched) | 0 |
| 6 | 0 | 0, 0 | 0 | 0 | 0 |
| 7 | 0 | 0, 0 | 0 | 0 | 0 |

Over ℚ(N) all eight third-order pair elements are 0.

- **N = 3 is reproduced in full**, every number a (3,0) determinant family:
  the domino diagonals `−24541/62424` (C-odd) and `−517313/6242400` (C-even)
  are tower + leakage; the corpus's vacuum-subtracted towers and leakage are
  tower − (−9/32) and leakage − (−9/32); `d_3 = 7/32 + 12 leak_3 − 4 B_3`.
  The second order agrees too: `⟨1|H_2|1⟩ = −3/4`, tower₂ − vac₂ = 1/2, hop₂ =
  −5/612 coplanar.
- **Even N has no odd order** (Theorem A of the note): N = 4 and 6, every
  first- and third-order element in both sectors, zero.
- **Odd N has its first odd order at m = N − 2** (Theorem B): at N = 5 the
  third order is the single five-word vertex ±25/144 = ±(5/6)²/(2!)², the
  one path F → Λ² → Λ³ → F̄, and at N = 7 the third order is empty. By
  characters through seventh order: N = 4, 6, 8, 10 have no odd order; N = 7
  and 9 have their first at orders 5 and 7 with the closed-form vertex.
- **No balanced family reaches the third order**: the symbolic engine returns
  0 identically, so every nonzero odd-order number of the corpus is a
  determinant-family number.

## Consequence for G16

The band's τ-series of ADR 0046 has no odd terms in the planar limit at any
fixed order; for odd N the first odd term is the baryonic vertex at order
N − 2, of relative size `(e²τ/2)ᴺ` up to a power of N.

## Reproduce

    python runs/odd_order_band_2026-09-11/derive.py
    workhouse verify --only 'determinant families'

The suite "the odd orders of the band are determinant families (G16)" (seven
T1 checks) recomputes N = 3 (single plaquette and coplanar pair) and N = 4 in
`loopcalc`, the character towers, the N = 5 cheap elements and the symbolic
hops live, and reads the rest from the certificate. Timings are in
`certificate.json`; the N = 3 determinant families dominate.
