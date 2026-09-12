# 48. The single-face planar grading law at k = 4 and k = 5, and the irrep channels that carry the cancellation

Date: 2026-09-11. Status: accepted. Bears on G16, G14, G9; changes no claim's
status. Source: `paper/research_notes/PLANAR_GRADING_SINGLE_FACE_20260911.md`.
Run: `runs/planar_grading_2026-09-11`.

## Context, and what was already established

Three results of 2026-09-11 bear on the same N-grading of the strong-coupling
band.

- **ADR 0046** showed every fourth-order cumulant is `O(N⁻⁷)` while its 1,772
  resolvent channels are `O(N⁻³)`, conjectured the law `N⁻⁽⁴ᵏ⁻¹⁾` at order `2k`
  with `N⁻⁽²ᵏ⁻¹⁾` channel content, and verified it at `k = 1, 2`. It recorded a
  negative: a per-channel label rule fails on 47 of the 1,772 forms, so "the
  cancellation of the two higher orders is not a per-label statement".
- **ADR 0047** proved, from Z_N link-flux quantization, that the odd orders are
  determinant families: none at even N, none below order `N − 2` at odd N.
- **The G9 suite** "G9 direct sixth order on one face and the shared-link
  pairs, any rank" (`runs/g9_direct_h6_pair_2026-09-11`) already established,
  **exactly over ℚ(N)**, the one-face case at `k = 3` — including that the
  order-six C-parity splitting is `N⁻¹¹` — and that the seven word-formula
  pieces of (F6) are each `O(N⁻⁵)`, so three orders cancel between channel
  content and cumulant. It also did the shared-link pairs at `k = 1, 2, 3`.

**A correction to an earlier draft of this ADR, kept on the record.** That
draft claimed `k = 3` as new and stated that ADR 0046's named test had not been
reached. Both are false: the G9 suite reached it, exactly, and by a better
route than the numerical extrapolation the draft used. The draft also recorded
`c₆ = −1748/3` as a "recognition of a numerical limit"; the ℚ(N) engine returns
it exactly. The error was caught by the repository's own full test run, which
printed the G9 check's name. What survives is stated below.

## What was computed

The C-parity splitting of the one-plaquette diagonal,
`S_m(N) = odd_m − even_m = −2·K_m[0][1]`, in the rank-generic character engine
`sixth_order_characters.bloch_series` over ℚ(N), at even orders 2 through 10.
Exact rational functions of N throughout. An independent integer-rank
cross-check uses the unrelated one-plaquette engine of ADR 0047 at `N ≤ 200`.

## Decision: record three facts and one reading

1. **The law at k = 4 and k = 5, exactly.** For even `m ≤ 10`,
   `S_m(N) = c_m N⁻⁽²ᵐ⁻¹⁾(1 + O(N⁻²))`; with `m = 2k` that is `N⁻⁽⁴ᵏ⁻¹⁾`.
   Orders **eight and ten are new** — nothing in the corpus had gone past order
   six on this object, and `k = 5` confirms a prediction the earlier draft made
   before it could test it.

2. **The planar coefficients of the splitting, and their τ-normalization.**

   | order m | k | exponent | `c_m` | `b_m = c_m/2ᵐ` |
   |---|---|---|---|---|
   | 2 | 1 | −3 | −4 | **−1** |
   | 4 | 2 | −7 | −32 | **−2** |
   | 6 | 3 | −11 | −1748/3 | −437/48 |
   | 8 | 4 | −15 | −123332/9 | −30833/576 |
   | 10 | 5 | −19 | −49593808/135 | −3099613/8640 |

   With the canonical `u = β_N/(2N)` and `τ = β/N³`, so `u = N²τ/2`, the
   order-`m` term is `(c_m/2ᵐ)·N·τᵐ`: **every even order carries the same single
   power of N**, so the single-face band per unit N is a function of `τ` alone.
   `b₂ = −1` and `b₄ = −2` exactly.

3. **The irrep channels, and where the cancellation lives.** Split `S_m` by the
   intermediate state of the perturbed vector — an exact decomposition, asserted
   against `S_m` in the run. At every even `m` from 4 to 10 exactly **four**
   channels contribute: the singlet `((), ())`, the adjoint `((1,), (1,))`, and
   the two two-box states `((2,), ())` and `((1,1), ())`. **Each is of order
   `N⁻⁽ᵐ⁻¹⁾`**, with leading coefficients, in units of `s = 2^(m/2−2)`:

   | singlet | adjoint | `((2,), ())` | `((1,1), ())` | sum |
   |---|---|---|---|---|
   | `−4s` | `+2s` | `+1s` | `+1s` | **0** |

   At `m = 2` only the singlet and adjoint exist, at `−2` and `+2`. This is a
   different decomposition from the word-formula pieces of (F6) that the G9
   suite bounds.

4. **The reading.** The suppression is a cancellation **between channels of
   equal order**, carried entirely by their relative coefficients and graded by
   the irrep content of the intermediate state. That explains ADR 0046's
   negative directly: no rule assigning an order to each channel separately can
   reproduce the cancellation, because every channel has the *same* order. The
   47 forms its label rule failed on are not exceptions to a rule; there is no
   per-channel rule of that kind to be had.

   Both band laws are then faces of one Z_N flux grading. Unbalanced class
   (ADR 0047): some link carries flux `≥ N`, so `m + 2 ≥ N` — the determinant
   families. Balanced class (here): all channels sit at `N⁻⁽ᵐ⁻¹⁾` and their
   irrep-graded coefficients cancel through `m − 1` orders.

## Consequences

- G16 gains the one-face exponent law at two further orders, with the exact
  planar coefficients of the splitting and the `τ`-normalization in which the
  first two are `−1` and `−2`.
- ADR 0046's conjecture is **not** discharged for cluster cumulants. The object
  here is the one-plaquette diagonal. G9's shared-link pair route carries the
  multi-face statement, and G16's overlap theorem is untouched.
- **Falsifier for the mechanism:** regrouping ADR 0046's 1,772 fourth-order
  channel forms by the irrep content of the intermediate state should make
  their orders uniform at `N⁻³` and their leading coefficients sum to zero. If
  they do not, the identification of the two cancellations is wrong. That test
  uses a computation that already exists.
- Order 12 (`k = 6`) was computed separately and **does** give `N⁻²³`, with
  `c₁₂ = −21582705596/2025` and `b₁₂ = −5395676399/2073600`. That value is
  deliberately **not** certified here — folding it in means rebuilding the run
  and rerunning the whole regeneration and verification chain — so it is
  recorded as an observed next rung, to be certified when this run is next
  touched. Order 14 is then the one after.
