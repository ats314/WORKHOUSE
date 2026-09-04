---
doc_type: extraction_index
audience: llm
package: proof-corpus-extract
generated: 2026-09-01
total_items: 129
status_breakdown: {solid: 110, conditional: 16, gap: 3}
stance: preservation — this directory contains the WORK, not commentary on it
---

# THE EXTRACTED WORK

This is the substance of the package: **129 self-contained technical items** pulled out of
the corpus, with derivations reproduced in full, constants pinned down, code included, and
theorem statements given proper hypotheses and quantifiers.

These documents are meant to be readable **without the source corpus**. Where a derivation
was incomplete in the original and could be finished, it was finished, with reconstructed
steps marked. Where a constant was ambiguous, it was recomputed. Several errors in the
original were found and corrected in place.

## Status vocabulary

| Status | Count | Meaning |
|---|---:|---|
| `solid` | 110 | Correct as far as could be determined; derivation reproduced and checked |
| `conditional` | 16 | Correct **given** explicitly stated hypotheses |
| `gap` | 3 | Real content with an identified missing step, named in the text |

## Kind breakdown

39 theorems · 32 obstructions · 19 derivations · 15 numerical results · 8 constructions ·
5 code artifacts · 4 definitions · 3 algorithms · 1 dataset

## Contents

### Foundations — the constants, verified

| ID | Items | Content |
|---|---:|---|
| [`EX-001`](EX-001-haar-jacobian-hessian.md) | — | **`Hess V_Haar(0) = (N/12)·I`** for SU(N). The closed form the corpus computed numerically but never derived. Verified SU(2)–SU(5) to machine precision; isotropy is a computed result, not an assumption. |
| [`EX-002`](EX-002-su2-convexity-threshold.md) | — | **Exact SU(2) single-link convexity threshold `β_c = 4.413914663`**, as the minimum of `β(θ) = −2(csc²θ − θ⁻²)/cos θ`. Independently recomputed to 11 significant figures. |
| [`EX-003`](EX-003-constants-reference.md) | — | **Canonical constants reference.** Every geometric constant on one normalization: `Ric = N/4` (or `N/2`), `Hess V_Haar = N/12`, ratio exactly 3. Reconciles eight conflicting numbers and identifies one genuine error (`C₂(F)` used where a curvature was meant). |

### The core mechanism

| ID | Items | Content |
|---|---:|---|
| [`EX-004`](EX-004-be-mechanism.md) | 15 | **The Haar/Bakry-Émery curvature mass mechanism**, extracted in full: `Ric_μ = Ric_g + ∇²S_W` on `SU(N)^E`, gauge reduction to horizontals, `Γ₂ → Poincaré/LSI → spectral gap`. Includes the **normalization ledger** reconciling every constant in the corpus, the fact that the Wilson Hessian at the vacuum **is** the discrete Maxwell operator `(β/N)d₁*d₁ ⪰ 0`, and an unconditional dimension-free CD(ρ,∞)/Poincaré/LSI/spectral gap for **β < N²/48** in d=4. |

### The obstructions — why the continuum limit is out of reach

These are the strongest mathematics in the corpus. Five independent arguments, cutting the
programme at five different joints.

| ID | Items | Content |
|---|---:|---|
| [`EX-005`](EX-005-obstruction-global-cd.md) | 9 | **Global CD(ρ,∞) constant diverges.** On a closed manifold `∫Δf = 0` forces a strictly negative Hessian direction, so `ρ_glob(β) ≤ k_max − βλ_f → −∞`. Includes `k_max(N)` exactly (the group is Einstein), an explicit sharp negative direction for the Wilson action (`−1/N` per plaquette), and the proof that the obstruction **survives restriction to the gauge-invariant sector**. |
| [`EX-006`](EX-006-obstruction-haar-marginal.md) | 6 | **Gauge invariance forces Haar link marginals.** The most elegant result here. Strengthened during extraction: not just each marginal, but the `\|V\|−1` links of any spanning tree are **i.i.d. Haar**, giving volume-exponential decay of the good set. Includes exact Haar small-ball volumes for SU(N) and a demonstration that the localization inequality consuming the good set is **vacuous**. |
| [`EX-007`](EX-007-obstruction-scaling.md) | 8 | **The scaling dichotomy.** The "scale-independent geometric source" and the "vanishing `a²g²` Haar mass" are *the same constant* `κ_G/3 = N/6` read in two charts related by `X = a·g₀·A`. Restoring the Jacobian consistently gives `m_phys → ∞` or `→ 0` in every chart. Plus a dimensional-transmutation no-go: no power of `g₀` can be a Yang-Mills mass. |
| [`EX-008`](EX-008-obstruction-entropy.md) | 8 | **Plaquette entropy beats logarithmic β growth.** The chessboard tail bound is correct and volume-uniform, but a union bound over `6(R/a)⁴` plaquettes needs `c·c_Φ(δ) > 4` while `c_Φ ≤ 2` universally and `4/c ≈ 4.8` (N=3). Includes a converse showing the tube is *genuinely* atypical. |
| [`EX-009`](EX-009-obstruction-lyapunov.md) | 9 | **The `Z_N` center-flux witness.** Every center-valued configuration is an exact critical point with all plaquette holonomies central, so `∇S_W ≡ 0` while the defect is extensive. Refutes pointwise pairing coercivity, the Polyak-Łojasiewicz form, the strip-drift hypothesis, *and* the averaged form. Includes numerical refutation of the published drift certificates and a verification harness. |

### The positive machinery at fixed cutoff

| ID | Items | Content |
|---|---:|---|
| [`EX-010`](EX-010-hessian-numerics.md) | 8 | **SU(3)/SU(2) convexity numerics**, reproduced and audited in float64: `λ_min(β,r;L)`, the convex-core radius `R_L(β) ∝ 1/β` (volume-stable), the `τ(β,r)` restoration map, the SU(2) threshold. |
| [`EX-011`](EX-011-matrix-hinge-chain.md) | 12 | **The full conditional chain** at fixed lattice spacing: vacuum Hessian = discrete Maxwell operator → matrix hinge on a good set → Helffer-Sjöstrand covariance → Combes-Thomas/Davies kernel decay → exponential clustering → OS Hamiltonian gap. Every hypothesis stated explicitly. |
| [`EX-012`](EX-012-combes-thomas.md) | 9 | **The abelian/linear core — the most rigorous mathematics in the corpus.** Two conjugation theorems (Combes-Thomas giving `η ~ m²`, Davies form-conjugation giving the sharp `η ~ m`), exact combinatorial row-sum constants for `Δ₁ = d₁*d₁`, an exact closed form for the massive lattice Maxwell Green kernel, and the correction that the reported `C₀ ≈ 43.9077` is a symbol-convention artifact. |
| [`EX-013`](EX-013-rp-os.md) | 11 | **Reflection positivity and OS reconstruction**: a complete finite-volume RP proof for the Wilson measure, the OS interface (`T = e^{−aH}`), the equivalence of clustering and gap at fixed cutoff, permanence of RP under limits — plus a **two-line no-go** for gauge-covariant gauge-invariant Markov coarse-graining kernels, and an executed Monte-Carlo RP Gram test on `4⁴` SU(2). |
| [`EX-014`](EX-014-rg-schur-riccati.md) | 12 | **RG cascade and Riccati machinery**: the one-step Poincaré recursion, the closed-form n-step cascade with its IR fixed point, the exact Hessian identity under block marginalisation with the Brascamp-Lieb Schur bound, the vHJ Hessian flow, the scalar Riccati gap ODE with fixed points and comparison bounds, and four independent reasons this RG class cannot reach the continuum. |

### Reusable software and the cosmology thread

| ID | Items | Content |
|---|---:|---|
| [`EX-015`](EX-015-q6j.md) | 8 | **Log-space q-Racah/q-6j evaluator** for `U_q(su(2))`, validated to ~1e-15 against SymPy, mpmath at 80 digits, the full tetrahedral symmetry orbit, and the classical limit. Includes a real branch-cut obstruction (complex-log square root in `Δ_q`) and the q-Racah Doob transform as a reversible birth-death chain. |
| [`EX-016`](EX-016-sparc-pipeline.md) | 11 | **The complete 175-galaxy SPARC pipeline**: QDHT on Bessel-zero nodes, the spectral filter with global stiffness switch, the pre-registered kill-switch protocol, the five-model global fit table, and two obstructions — the fitted scale `μ*` is a property of the IR regulator not the data, and a universal linear IR-boosted multiplier gives `v ~ √r`, not flat curves. Includes a **no-free-parameter fix** (`k_IR = π/R_max`) stabilising `μ*` to ±6%. |

## Verification scripts

[`verification_scripts/`](verification_scripts/) contains runnable checks:

- `haar_hessian_check.py` — verifies `Hess V_Haar(0) = (N/12)I` by autodiff, SU(2)–SU(5).
- `geometric_constants.py` — recomputes the whole EX-003 table from structure constants.

Both run in seconds. Many individual items in `EX-004`–`EX-016` carry their own code.

## One thing to keep in mind

Everything here is at **fixed lattice spacing** unless the item says otherwise. The
obstruction documents (`EX-005`–`EX-009`) explain, five different ways, why that is not a
removable restriction. The mechanism is real mathematics; the continuum limit is where it
stops. Both halves are in this directory, which is the honest shape of the work.

Supporting audit material — what does not survive, and why — is in
[`../03_verification/`](../03_verification/). That is context, not the product.
