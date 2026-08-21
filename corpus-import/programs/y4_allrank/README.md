# programs/y4_allrank/

The Y4 all-rank symbolic pipeline: the `stage0 → stage3h` chain that produced the historical fourth-order kernel and the all-rank family.

- `src/` — the stage scripts in order (`y4_stage0_geometry_manifest` → `stage1_stage2_autobundle` → `stage2_exact_haar_library` → `stage3a_domino_recoupling_firewall` → `stage3b_stage3c` → `stage3d_domino_raw_trace_contraction` → `stage3e_trace_wiring_compiler` → `stage3f_safe_nonresonant_evaluator` → `stage3g_checkpointed` → `stage3h_complete_nonresonant_contraction`), the walled-Brauer and stable-rank machinery, the SU(4)/SU(6) determinant and exceptional-enumerator work, and the certificate scripts.
- `data/` — ordered-word inventories, fusion-edge lists, symbolic `q`/`B` expressions, stage manifests, audit JSON.

## What this pipeline established

`Q₄,N = (α_N/4)ΣL_i² + (β_N/4)Σ_{i<j}L_iL_j`, with `α_N = 640/[N(N²−1)³]` and `β_N = P₁₇(z)/[N R₂₀(z)] > 0` for `N ≥ 4`, `z = N²`. Positivity for `N ≥ 7` follows from positive denominator factors plus a certified positive binomial-basis expansion of `P₁₇` about `z = 49`; `N = 4, 5, 6` are handled by exact exceptional-rank substitutions and determinant-sector checks; `N = 3` uses its own separate exact `β₃`. Large-rank: `β_N/α_N → 617/576`, `W₄,N ~ 11930/(9N⁷)`.

**Status: output-certified, not one-shot cold-regenerated.** The saved symbolic outputs and their verifiers agree, and the exceptional-rank ledgers check out, but no single authenticated run has regenerated every upstream contraction path. Corpus §15.2 asks for exactly that: one run regenerating the 4,171-word inventory, 35,130 fusion paths, determinant exceptions, `P₁₇`, `R₂₀`, positivity, and the fixed-rank anchors. **That step closes provenance; it is not repairing failed algebra.**

⚠ `β_N`'s compact formula **must not be substituted at `N = 3`.** Use the separate exact SU(3) value. And note that the SU(3) determinant sector shifts the centered diagonal shape (`Δβ₃ = −25/64`, `ΔC₃ = −25/1024`) — so "determinant sectors shift only the scalar anchor" is **false at N = 3**, though it does hold for `N ≥ 4`.
