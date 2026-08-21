# shell6_o2 — second-order O(y²) attack on the shell-6 C-odd glueballs

Created June 13, 2026. Follows the uploaded first-order note
(`NOTE_SHELL6_first_order_codd_result_2026-06-13.md`): the exotic C-odd channels
(0⁻⁻, 3⁺⁻, 2⁻⁻, 2⁺⁻) are degenerate at O(y); ordering them is an O(y²) effect.
This directory attacks that O(y²) computation.

**Read `NOTE_SHELL6_o2_result_2026-06-13.md` first** — it states what is settled
(gate-backed), what is corrected, and what the full ordering computation requires.

## What this pass established (gate-backed)

1. **Symmetry skeleton** — the ordering question reduces to **three multiplicity-1,
   purely-hexagonal channels** (0⁻⁻ = A₁⁻⁻, 3⁺⁻ = A₂⁺⁻, 2⁻⁻ = E⁻⁻ and T₂⁻⁻); each
   O(y²) energy is a single number set by the **off-diagonal** H². The 2⁺⁻ mixes
   hexagon+rectangle (mult 2); the excited 1⁺⁻ is mult 3.
2. **First-order correction** — the corner-push matrix element is exactly 1/3 (Haar),
   so the excited 1⁺⁻ splits **±2√2/3 y**, not the uploaded script's ±√2/3 (a factor-2
   slip from hardcoding hop = 1/6 instead of the matrix element 1/3). Exotic channels
   stay degenerate at O(y) — qualitative conclusion unchanged.
3. **Exact SU(3) Haar engine** validated (multi-link, ε-baryon-aware) + a link-variable
   word calculus whose H₀ reproduces the certified vacuum self-energy e₂ = −3/4.

## Why the ordering itself is staged, not asserted

A Wilson-loop-intermediate engine provably cannot resolve C-even vs C-odd: on the
certified shell-4 neighbour hop it returns −1/12 for both, vs the certified
−481/612 (even) and 5/612 (odd). The C-parity-flip amplitude is carried by
**disconnected/two-loop and higher-irrep intermediates** that simple-loop enumeration
drops. The exact computation needs the full word calculus (su3_domino machinery)
extended to the hexagon basis — the staged next step.

## Canonical files

| file | role | gates |
|---|---|---|
| `NOTE_SHELL6_o2_result_2026-06-13.md` | the writeup (read first) | — |
| `ENGINE_SHELL6_o2_skeleton.py` | O_h×C decomposition of the 44-loop shell | 13 ✓ |
| `ENGINE_SHELL6_firstorder_corrected.py` | corrected first-order spectrum (±2√2/3) | 8 ✓ |
| `ENGINE_FLUX_shell6_o2_engine2.py` | exact multi-link SU(3) Haar engine + shell-4 calibration | diagnostic |
| `ENGINE_SHELL6_link_calculus_validate.py` | link-variable word calculus; H₀ validated (e₂ = −3/4) | partial |

**Superseded / do not use:** `ENGINE_SHELL6_o2.py` (truncated by a stale-mount write),
`ENGINE_SHELL6_haar_loops.py` (folded into `ENGINE_FLUX_shell6_o2_engine2.py`).

## Provenance

All engines build on the certified `../ENGINE_FLUX_su3_moments_ext.py` (27 gates) and
`../ENGINE_FLUX_su3_domino_d3.py` (251 gates). MD5s of this directory recorded in
`../../../records/SESSION_LOG.md` (2026-06-13 entry).
