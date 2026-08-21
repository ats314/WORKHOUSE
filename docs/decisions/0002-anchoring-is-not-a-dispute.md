# 2. q_band and m_Gamma are anchors, not competing estimates

Date: 2026-08-21

## Status

Accepted. Amends ADR 0001, which treated C1 and C2 as a single dispute.

## Context

The contradiction register recorded C1 as a conflict between two values of the
fourth-order rest scalar: an exact rational `-2.857915988114559` and a float
`-0.7751458630189173`, differing by `Delta_Gamma = 2.0827701250956417`.

Read as two estimates of one quantity, that is a glaring disagreement. Read
correctly, it is not a disagreement at all. The two numbers are differently
anchored coordinates:

- `q_band^(4)` — a band-kernel anchor
- `m_Gamma^(4)` — a vacuum-subtracted physical Gamma-point coefficient

They are related by a translation-local scalar shift. If
`H_4_mass(k) = H_4_band(k) + Delta_Gamma * I`, then
`H_4_mass(k) - m_Gamma^(4) I = H_4_band(k) - q_band^(4) I` identically, so the
centered operator, its eigenvectors, the SOS factorization, the mobility
coefficients and the bandwidth are all untouched.

The conflict was manufactured entirely by calling both quantities `m_4`.

## Decision

1. C1 is **resolved** as an anchoring distinction, not adjudicated as a dispute.
2. The names `q_band^(4)` and `m_Gamma^(4)` are mandatory. Writing "two `m_4`
   values" is forbidden, and `tests/test_ledger.py` enforces that the register
   keeps saying so — the false contradiction otherwise regenerates on every
   re-reading.
3. C2 remains open, and the crosswalk explains why it must:

   ```
   c_4_new(k) = c_4_old(k) + Delta_Gamma + Delta_C * Phi_C(k)
   Phi_C(k)   = 4 * e_2(k) / Q(k)
   ```

   With `e_2 = O(|k|^4)` and `Q = O(|k|^2)`, `Phi_C = O(|k|^2)` and
   `Phi_C(0) = 0`. A Gamma-point scalar therefore fixes `Delta_Gamma` and
   constrains `Delta_C` not at all. `Phi_C` also vanishes on every axial cut,
   which is exactly why the axial data agree while M and R split by
   `8*Delta_C` and `16*Delta_C`.

4. Two claims about the run are kept apart, because conflating them is how C22
   arose:
   - the oracle value is an independent blind reconstruction, matching Hamer's
     `a_4` to `5.2e-13` with no historical target in its data flow —
     **substantive**;
   - the final assembled rest value is forced to equal that oracle by
     `local_shift = M4_ORACLE - ax_rest` — **true by construction**, and it
     validates neither the off-axis C-row nor the 189-entry ledger.

## Consequences

G3's scope narrows: it no longer needs to adjudicate a scalar. What it must
settle is `C_shp`, and `Phi_C(0) = 0` proves no amount of Gamma-point precision
can substitute for that.

The defensible status is now: the blind linked-cluster calculation reproduces
Hamer's fourth-order Gamma-point coefficient; the earlier scalar is a
differently anchored band-kernel coordinate related by a shift that leaves the
centered Hodge/SOS mobility structure unchanged; and the cold and historical
off-axis C-shape coefficients still differ, so the complete momentum-resolved
fourth-order kernel is not yet independently sealed.
