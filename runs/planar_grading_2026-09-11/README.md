# The single-face planar grading law over ℚ(N): orders eight and ten, and the irrep channels — 2026-09-11

ADR 0046 conjectured that the order-`2k` band coefficient is `N^-(4k-1)` while
its channels are `N^-(2k-1)`, verified it at `k = 1, 2`, and recorded that a
per-channel label rule fails on 47 of its 1,772 channel forms. The **G9 suite**
("G9 direct sixth order on one face and the shared-link pairs, any rank",
`runs/g9_direct_h6_pair_2026-09-11`) then settled the one-face `k = 3` case
exactly over ℚ(N), including the `N^-11` order-six C-parity splitting.

**Correction kept on the record.** An earlier version of this run claimed
`k = 3` as new, said ADR 0046's named test had not been reached, and reported
`c_6 = -1748/3` as a recognition of a numerical limit. All three were wrong: the
G9 suite had reached `k = 3` exactly, and the ℚ(N) engine returns `c_6` in
closed form. The run was rebuilt on the exact footing; what follows is what
survives.

## The object

    S_m(N) = odd_m - even_m = -2 K_m[0][1],

the C-parity splitting of the one-plaquette diagonal, as an exact rational
function of N from the rank-generic character engine
`sixth_order_characters.bloch_series` (states are pairs of partitions,
`V = chi_F + chi_F-bar` by the Pieri rule, `H0 = 2 C_2` on four private links).
It is **not** the cluster cumulant `beta_N`.

## What is computed

`derive.py` writes `certificate.json`. Exact rational functions of N
throughout; the only floating point is the independent cross-check.

1. The exponent and the planar coefficient at even orders 2 through 10.
2. The `tau`-normalised coefficients `b_m = c_m/2^m` implied by `u = N^2 tau/2`.
3. An exact decomposition of `S_m` by the intermediate state — the parts are
   asserted to sum to `S_m` over ℚ(N) — and the leading coefficient of each.
4. An independent integer-rank cross-check with the unrelated one-plaquette
   engine of ADR 0047 at `N = 60..200`, Richardson-extrapolated in `1/N^2`.

## Result

| order m | k | exponent | `c_m` | `b_m = c_m/2^m` |
|---|---|---|---|---|
| 2 | 1 | −3 | −4 | **−1** |
| 4 | 2 | −7 | −32 | **−2** |
| 6 | 3 | −11 | −1748/3 | −437/48 |
| 8 | 4 | −15 | −123332/9 | −30833/576 |
| 10 | 5 | −19 | −49593808/135 | −3099613/8640 |

Orders eight and ten are new; `k = 3` is the G9 suite's. Because
`u = N^2 tau/2`, every even order carries the same single power of N — the
single-face band **per unit N** is a function of `tau` alone.

The irrep channels of the splitting, in units of `s = 2^(m/2-2)`:

| channel | coefficient | m = 4 | m = 6 | m = 8 | m = 10 |
|---|---|---|---|---|---|
| singlet `((), ())` | `-4s` | −4 | −8 | −16 | −32 |
| adjoint `((1,), (1,))` | `+2s` | +2 | +4 | +8 | +16 |
| `((2,), ())` | `+1s` | +1 | +2 | +4 | +8 |
| `((1,1), ())` | `+1s` | +1 | +2 | +4 | +8 |
| **sum** | **0** | 0 | 0 | 0 | 0 |

At `m = 2` only the singlet and the adjoint exist, at `-2` and `+2`. Every
channel is `O(N^-(m-1))`, so the suppression to `N^-(2m-1)` is carried entirely
by the relative coefficients: the cancellation is **between channels of equal
order**, which is why ADR 0046's per-channel label rule could not see it. This
is a different decomposition from the word-formula pieces of (F6).

Independent cross-check (ADR 0047 engine, extrapolated): −4.000000004,
−31.999990, −582.664862, −13703.363230 against the exact −4, −32, −1748/3,
−123332/9 — relative gaps 9.5e-10, 3.0e-7, 3.1e-6, 1.4e-5, degrading with order
as the extrapolation does.

## Scope

The one-plaquette diagonal at even orders `m <= 10`. ADR 0046's cluster
conjecture is **not** discharged; the shared-link pair route carries the
multi-face statement, and G16's overlap theorem is untouched. Each order is an
exact computation at that order, so the general-`m` law remains a conjecture,
now verified at `k = 1..5` on this channel.

## Reproduce

    python runs/planar_grading_2026-09-11/derive.py     # about 4 minutes
    workhouse verify --only 'one face over Q(N): the C-parity'

The suite "the single-face planar grading law through tenth order (G16)" has
three T1 checks (the law and coefficients at m = 2..8, the `tau`-normalisation,
and the channel decomposition, all re-derived live over ℚ(N)) and one T2 (the
integer-rank cross-check, a tolerance on an extrapolated value). Order 10 is
pinned from the certificate because its Bloch series costs about a minute.
