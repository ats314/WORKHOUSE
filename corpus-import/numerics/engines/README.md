# numerics/engines/

Reusable verifier and engine scripts, not tied to a single campaign. Campaign-specific code lives with its campaign under `programs/`.

- **`VERIFY_*.py`** — theorem verifiers: `VERIFY_CENTERED_DOUBLE_INCIDENCE`, `VERIFY_INCIDENCE_SYZYGY`, `VERIFY_DETERMINANT_TO_INCIDENCE_REDUCTION`, `VERIFY_THEOREM_ASSEMBLY`, and `VERIFY_ALL`. These pair with `theory/theorems/`.
- **Monte Carlo** — `SU3_T1pm_spatial_MC_HARDENED_v2`, `..._POLARIZATION_v3`, `..._nextrun`.
- **Generic machinery** — `ENGINE_STRING_generic_pt_core.py`, `ENGINE_STRING_generic_sigma.py`, `ENGINE_FLUX_gram_cold.py`.
- **Certificate producers** — the `m3a_stage_*`, `m5_*`, `shell6_*`, `tromino_*`, `su3_*`, `folded5_derivation`, `s_chessboard_rate`, `sc_extrap2` scripts.

**Gates hard-fail.** An engine ships with self-checking gates that raise via `assert` rather than warn, so a broken invariant stops the run instead of colouring an output. Note the limit of what a passing gate shows: on the corpus evidence scale it moves a result to `Cold-reproduced` at best, and a gate checking the same computation that produced the number is not independent of it.

Outputs go to `numerics/certificates/` (JSON) or `numerics/results/` (write-ups); raw logs go to `records/runs/`.
