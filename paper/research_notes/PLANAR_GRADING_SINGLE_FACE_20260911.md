# The single-face planar grading law: orders eight and ten, and the irrep channels that carry the cancellation

2026-09-11. Bears on G16, G14, G9. Run: `runs/planar_grading_2026-09-11`.
Suite: "the single-face planar grading law through tenth order (G16)".
Sources: ADR 0046, ADR 0047, ADR 0048, the G9 suite
(`runs/g9_direct_h6_pair_2026-09-11`), ADR 0029.

## What was already known

ADR 0046 conjectured that the order-`2k` band coefficient is `N^-(4k-1)` while
its resolvent channels are `N^-(2k-1)`, verified it at `k = 1, 2` on the
fourth-order cluster cumulants, and recorded a negative: a per-channel label
rule fails on 47 of its 1,772 channel forms, so the cancellation "is not a
per-label statement".

ADR 0047 proved the odd orders are determinant families, from Z_N link-flux
quantization.

**The G9 suite** — "G9 direct sixth order on one face and the shared-link
pairs, any rank" — then established the one-face case at `k = 3` **exactly over
ℚ(N)**, including that the order-six C-parity splitting is `N^-11`, and that the
seven word-formula pieces of (F6) are each `O(N^-5)`.

An earlier draft of this note claimed `k = 3` as new and reported `c_6` as a
recognition of a numerical limit. Both were wrong, and the correction is kept
on the record: the G9 suite had already reached `k = 3`, exactly, and the ℚ(N)
engine returns `c_6 = -1748/3` in closed form. What follows is what survives,
recomputed on the exact footing.

## The object

On one plaquette the model space is the two face words `F` and `F-bar`. In the
rank-generic character engine (`sixth_order_characters.bloch_series`, states
labelled by a pair of partitions `(lambda, mu)`, `V = chi_F + chi_F-bar` by the
Pieri rule, `H0 = 2 C_2` on four private links), the C-parity splitting of the
one-plaquette diagonal is the off-diagonal Bloch element

    S_m(N) = odd_m - even_m = -2 K_m[0][1],

an exact rational function of N at each fixed order. It is **not** the cluster
cumulant `beta_N` of ADR 0046; it is the one-face object whose `k = 3` case the
G9 suite settled.

## Result 1 — the law at k = 4 and k = 5

For even `m <= 10`, exactly over ℚ(N),

    S_m(N) = c_m N^-(2m-1) (1 + O(N^-2)),

which with `m = 2k` is ADR 0046's `N^-(4k-1)`. Orders **eight and ten are
new**: nothing in the corpus had gone past order six on this object.

| order m | k | exponent | `c_m` | `b_m = c_m/2^m` |
|---|---|---|---|---|
| 2 | 1 | −3 | −4 | **−1** |
| 4 | 2 | −7 | −32 | **−2** |
| 6 | 3 | −11 | −1748/3 | −437/48 |
| 8 | 4 | −15 | −123332/9 | −30833/576 |
| 10 | 5 | −19 | −49593808/135 | −3099613/8640 |

`k = 5` confirms the prediction the earlier draft made before it could test it.

## Result 2 — the tau-normalization in which the law is an identity

With the canonical `u = beta_N/(2N)` and `tau = beta/N^3`, so `u = N^2 tau/2`,

    S_m u^m = (c_m / 2^m) N tau^m.

**Every even order carries the same single power of N.** So `S(u)/N` is a
function of `tau` alone, with rank-independent coefficients:

    S(u)/N = -tau^2 - 2 tau^4 - (437/48) tau^6 - (30833/576) tau^8
             - (3099613/8640) tau^10 - ...

`b_2 = -1` and `b_4 = -2` exactly. This is the precise sense in which the
exponent law is not a coincidence about powers: it says the single-face band,
**per unit N**, is a function of `tau` alone — the matched-scaling structure of
NOTE_O4 section 11, made exact five orders deep on this channel.

## Result 3 — where the cancellation lives

Split `S_m` by the intermediate state of the perturbed vector. This is an exact
decomposition; the run asserts the parts sum to `S_m` over ℚ(N).

At every even `m` from 4 to 10 exactly **four** channels contribute: the
singlet `((), ())`, the adjoint `((1,), (1,))`, and the two two-box states
`((2,), ())` and `((1,1), ())`. **Each is of order `N^-(m-1)`** — the channel
content ADR 0046 predicted — with leading coefficients, in units of
`s = 2^(m/2-2)`:

| channel | leading coefficient | m = 4 | m = 6 | m = 8 | m = 10 |
|---|---|---|---|---|---|
| singlet `((), ())` | `-4s` | −4 | −8 | −16 | −32 |
| adjoint `((1,), (1,))` | `+2s` | +2 | +4 | +8 | +16 |
| `((2,), ())` | `+1s` | +1 | +2 | +4 | +8 |
| `((1,1), ())` | `+1s` | +1 | +2 | +4 | +8 |
| **sum** | **0** | 0 | 0 | 0 | 0 |

At `m = 2` only the singlet and adjoint exist, at `-2` and `+2`.

So the cancellation is **between channels of equal order, not inside any one of
them**, and it is graded by the irrep content of the intermediate state — the
singlet carrying twice the adjoint, the adjoint twice each two-box state. This
is a different decomposition from the word-formula pieces of (F6) that the G9
suite bounds, and it is the one that explains ADR 0046's negative: a label rule
assigning an order to each channel separately cannot see the cancellation,
because every channel has the *same* order and the suppression is carried
entirely by the relative coefficients. The 47 channel forms on which ADR 0046's
label rule failed are not exceptions to a rule; there is no per-channel rule of
that kind to be had.

## The grading, stated once

Grade each strong-coupling history by its Z_N link-flux class.

* **Unbalanced class** (ADR 0047): the class is nonzero only if some link
  carries flux `>= N`, hence `m + 2 >= N`. These are the determinant families —
  odd orders at odd N, the exceptional even ranks `N <= m + 2`. Their size
  relative to the plaquette energy is `(e^2 tau/2)^N` up to a power of N.
* **Balanced class** (here): the surviving channels all sit at `N^-(m-1)`, and
  their irrep-graded coefficients sum to zero through `m - 1` orders, leaving
  `N^-(2m-1)` — equivalently, `b_m tau^m` per unit N.

One grading, two regimes.

## Order twelve: observed, not certified

A separate exploratory computation (the same ℚ(N) engine at order 12, about
fourteen minutes to build the series) gives the exponent `-23` and

    c_12 = -21582705596/2025,   b_12 = -5395676399/2073600,

so the law holds at `k = 6` as well, confirming this note's own prediction.
**This is deliberately not in the certificate, the suite or the `RESULT:`.**
Folding it in would mean rebuilding the run and rerunning the whole
regeneration and verification chain; it is recorded here as an observed value
with its provenance, and it should be certified the next time this run is
touched.

## Falsifiable predictions

1. **Order 14 on one face: `N^-27`.** Order 12 is already observed above; the
   ℚ(N) series cost grows steeply (a minute at order 10, fourteen at order 12),
   so order 14 is the next rung and the next real test of the exponent law.
2. **The cluster-level regrouping — the falsifier for the mechanism.** If
   ADR 0046's 1,772 fourth-order channel forms are regrouped by the irrep
   content of the intermediate state rather than by "number of intermediate
   states carrying no irrep", their orders should become uniform at `N^-3` and
   their leading coefficients should sum to zero. If they do not, the
   identification of the two cancellations is wrong. This uses a computation
   that already exists.
3. **The shared-link pairs should show the same four-channel structure**, with
   coefficients summing to zero, at every even order the G9 pair route reaches.

## What this does and does not establish

* It **does** extend the one-face exponent law to `k = 4` and `k = 5`, exactly,
  and supply the exact planar coefficients of the splitting and their
  `tau`-normalization.
* It **does** exhibit the cancellation mechanism exactly over ℚ(N), and explain
  the failure of ADR 0046's label rule.
* It **does not** discharge the conjecture for cluster cumulants. The object is
  the one-plaquette diagonal. The G9 shared-link pair route carries the
  multi-face statement; G16's overlap theorem is untouched.
* It **does not** prove the law for all `m`. Each order is an exact computation
  at that order; the general statement remains ADR 0046's conjecture, now
  verified at `k = 1..5` on this channel.
