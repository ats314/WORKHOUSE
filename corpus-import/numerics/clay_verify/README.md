# clay_verify — the Clay submission's CODE/VERIFY scripts, run and recorded (June 12, 2026, #8b/F022)

Working copies of `E:\YANG\ORGANIZED\01_PROOFS\clay_submission\CODE\` (read-only archive), run here for the first recorded time. Canonical output: `NOTE_SU2_run_output_2026-06-12.txt`.

| MD5 | File | What it actually is |
|---|---|---|
| 333c4874f61a0a83f1b2369ab48aecd7 | ENGINE_SU2_verify_01_heat_kernel_stability.py | SU(2) heat-kernel estimate scan: κ(t) = ρ − 12·M₂(t) (Bakry–Émery route) and Dobrushin α(t) = 48·M₂(t), t ∈ [0.1, 2.0], with the script's own β ↔ t map β = 1/t (SU(2)) |
| 041b3200d5dac76ae972c88366211bb3 | ENGINE_FLUX_verify_02_anomaly_shield.py | Toy Legendre/dual-Hessian probe on 1D model potentials — a CONJ_B "shielding" illustration, no lattice content |
| cffab9237ab19c02baf9d32f214f8577 | ENGINE_FLUX_verify_03_continuum_scaling.py | SU(2) L=8 **Gaussian-approximation** configs (not MC), ⟨\|∇W\|²⟩/⟨W²⟩ vs β ∈ [2, 4]; **unseeded RNG — nondeterministic across runs** |

**Run findings (descriptive; June 12, 2026):**

1. **No gates anywhere** — zero `assert` statements across all three scripts; every script exits 0 regardless of what it prints. These are demos/diagnostics, not verifications in the rule-4 (hard-gate) sense.
2. **VERIFY_01's own table shows its κ-positivity criterion failing except deep in strong coupling:** κ > 0 only for t ≥ 1.7, i.e. β = 1/t ≲ 0.59; for all β ≳ 0.6 the printed Bakry–Émery κ is negative under this heat-kernel estimate. The stricter Dobrushin route (α < 1) fails at every scanned t (α = 1.44 even at t = 2.0) and its print line is commented out in the source as "usually too strict." Output columns are mislabeled: the column headed "Route A" prints σ_geom = 4t/3 (the P04 geometric bound under the script's map), and the column headed "Route B" prints Route A's pass flag (κ > 0).
3. **VERIFY_02** prints a `nan` suppression factor in its central "Shielded (Massive)" case (the mass term degenerates the double well; barrier −0.000000).
4. **VERIFY_03's printed values trend opposite to its own legend:** the ratio *decreases* 29.26 → 22.38 as β goes 2.0 → 4.0 while every row is labeled "(Expected Log Growth)" unconditionally (log β increases on that range). No test enforces the stated hypothesis.
5. **Convention exhibit (live factor trap):** VERIFY_01's header comments deliberate over the source paper's constants — "The paper normalization is g = −Killing = 2N(−Tr) … This means their metric is scaled. We will use the PAPER'S CONSTANTS exactly" — a third metric normalization in the corpus (see DOC_GOV_conventions.md §1 note). With it: ρ = 1 for SU(2); numerically coincides with PROOF_04's κ = ¼C_adj = 1 at SU(2).

None of these run-level facts are recorded in the submission's own documents (the April deep-read did not execute CODE). Finding: `records/review/findings/F022_clay_remainder_proof04_reviews_code.md`. House note: scripts kept verbatim (archive copies); do NOT add gates here — write new gated engines in numerics/ if any of these estimates are ever load-bearing.
