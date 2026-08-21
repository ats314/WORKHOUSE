# F009 — Second Lean project (F:\STORAGE\yang_mills_lean) + STORAGE inventory

**Date:** June 12, 2026. Triggered by Alex's screenshots. Amends/extends F008.

## Corrected chronology (per file dates + Alex's second screenshot)

**synthesis10** (the F008 audit subject): Jan 2–4, 2026, original home `F:\E\lean_projects\synthesis10_lean\` (outside current mounts; archived copy incl. .git in `DELETE/originals/lean_projects/synthesis10_lean/`). **yang_mills_lean**: Jan 15, 2026, `F:\STORAGE\yang_mills_lean\` — the *matured successor*, and it was **in no archive until today** (now `ORGANIZED/05_LEAN/yang_mills_lean_jan2026/`, 315 files, MD5 spot-checked).

## What the successor project is

110 modules / 12,205 lines / **zero sorries** / Duper + LeanAide in deps. Same scalar genre as synthesis10 but materially more mature:

1. **MasterTheorem.lean (765 lines):** the full chain *composed* — 8 stages (curvature sources → positivity → hand-off → Riccati → Schur RG → transfer gap → clustering → OS/physical mass), with genuine Riccati attraction/Lyapunov lemmas (beyond F008's static algebra). Crown theorem `yang_mills_mass_gap_from_first_principles`: constructs m from σ = weyl_floor + anomaly_source with m² ≥ N/4, β < 0, and `∃ H : SpectralHamiltonian, H.gap = m` — **where SpectralHamiltonian is a two-field record (gap, gap_pos), i.e., a witness construction, not an operator statement.** Still scalar-level; honestly so.
2. **Stubs/ = labeled axioms:** e.g. "STRUCTURAL AXIOM: projective limit RP", "NUMERICAL AXIOM: m₀ ≥ 1.48". The open continuum inputs are axiomatized *and marked*.
3. **tools/CheckAxioms.lean:** `#print axioms` on the crown theorem — the project ships with its own conditionality made machine-enumerable. This is the right architecture for honest conditional formalization.
4. **YangMillsFromAxioms.lean:** real group-theory micro-layer (su(N) dims, Casimirs, Killing normalization, Weyl roots).

**Revised Lean-layer verdict (F008+F009):** two generations, both zero-sorry, both scalar-shadow in content; the Jan-15 project adds composition + an explicit, introspectable axiom boundary. Neither touches operator/measure content. **M5 should be built on the yang_mills_lean architecture** (add the M2 rational-kernel certificate as a new module contributing *zero* new axioms — making it the first load-bearing content inside an already-honest conditional frame, with CheckAxioms attesting the boundary).

## STORAGE mount accounted

`yang_mills_lean/` (deposited), `ai_proof_tools/` = LeanAide-main external tool (144K files — SKIP, same copy archived in DELETE), `lattice_qcd/` = one script `SU2_Lambda_QCD_Extraction.py` (deposited → `04_SIMULATIONS/utilities/`).

## Note on F:\E\

Alex's screenshot shows `F:\E\lean_projects\` — a drive area outside current mounts. Its synthesis10 copy is archived (DELETE), but **if `F:\E\` holds other unarchived trees, it needs a mount + sweep** — queued as a question for Alex / future unit.
