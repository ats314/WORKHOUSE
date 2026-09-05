# Uniform Wilson kinetic window and the second-order shell at finite temporal step — 2026-09-04

Third package from a parallel GPT session, prepared against `31255ab` and
reviewed here before integration. It continues the temporal matching of
`runs/relative_gap_wilson_matching_2026-09-04`: the same positive Wilson transfer
family, the clock calibrated on the fundamental character, now with the high
irreps controlled all at once and the actual transfer generator's second-order
shell written down at finite temporal step.

## What it establishes, and how far

- **Uniform exclusion of high irreps (analytic).** A pointwise comparison of the
  Wilson density with a narrower heat kernel gives `k_ε(R) ≥ c_N min(C_R, 1/ε)`
  for every irrep, so no representation can enter a fixed low-energy window as
  `ε → 0`, uniformly in the spatial volume. With Revision 6's support census
  the free physical spectrum below `5C_F/2` is exactly `{0, 2C_F}`, the vacuum
  and the fundamental plaquette shell, for every periodic `L ≥ 3` once `ε` is
  below an existential `ε₀(N)`. A research-note proof; not machine-checked.
- **The finite-step reduced resolvent (derived identity).** For the symmetric
  transfer `e^{τuV/2} e^{-τK} e^{τuV/2}` the second-order effective generator
  carries `d_τ(Δ) = (τ/2) coth(τΔ/2)` in place of `1/Δ`.
- **The second-order C-odd shell at finite step (exact algebra, re-derived here).**
  With the exact SU(3) multipliers from Cartan Gaussian moments,
  `λ₃ = 1 − 2ε/3 + ε²/36 + 13ε³/648`, `λ₈ = 1 − 3ε/2 + 11ε²/16 + ε³/96`,
  `λ₆ = 1 − 5ε/3 + 65ε²/72 − 55ε³/1296`, the shell is again `t_W` times the
  signed incidence adjacency with
  `t_W = 5/612 + 175/280908 ε² + O(ε³)`, `s_{2,W} = 11/306 − 89159/2247264 ε²`,
  and the first literal-source Gram coefficient `−2 d_τ(E_F) = −3/4 − 4ε²/9`.
  The suite "the Wilson transfer matrix at finite temporal step"
  (`src/workhouse/invariants/wilson_step.py`) re-derives all of this from the
  stated definitions, and checks on the way that the four channel weights
  reproduce `t_N` at every rank in the Hamiltonian limit.
- **Fixed-order weighted matching (analytic).** Energy, Gram and source kernels of
  the transfer and the Hamiltonian differ by `O(ε²)` in the spatially weighted
  norm at every fixed magnetic order, with order-dependent constants. Not a
  bound on the summed series.
- **Conditional (G18).** For SU(3) the auxiliary family `K_ε − uV` shares the
  vacuum, symmetries, onsite gap and a common kinematic contour, so the G18
  construction runs uniformly for it; the note is explicit that this is not
  the logarithm of the symmetric transfer operator.
- **Open.** The summed matching for the actual Wilson transfer operator is
  reduced to a uniform discrete-time marked-cluster majorant (Section 10 of the
  note). Nothing here changes a gap's status.

## Files

Pinned as received, checksums in `PACKAGE_SHA256SUMS` (three entries there refer
to files moved or renamed: the two notes now live in `paper/research_notes/` as
`G19_UNIFORM_WILSON_WINDOW_20260904.md` and
`G19_WILSON_KINETIC_WINDOW_INSERT_20260904.tex`, and the package's README is
`PACKAGE_README.md`).

| File | What it is |
|---|---|
| `exact_su3_laplace.py` | the exact Cartan Gaussian-moment derivation of the multipliers (sympy only; replayed here, identical output) |
| `exact_laplace_certificate.json` | its output as received |
| `verify_kinetic_window_and_shell.py`, `wilson_clock.py` | the 23 checks, including the 231-irrep scans and the two negative controls; need NumPy, SciPy, mpmath; pinned only |
| `window_shell_certificate.json`, `checks.log` | the recorded results of that execution |
| `graph_integration_proposal.json` | the session's proposed claim connections; not applied |
| `source_manifest.json`, `requirements.txt`, `PACKAGE_README.md`, `PACKAGE_SHA256SUMS` | provenance |
| `SHA256SUMS` | the pin of this directory |
