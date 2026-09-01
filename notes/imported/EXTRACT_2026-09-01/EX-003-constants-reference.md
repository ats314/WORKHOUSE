---
id: EX-003
title: "Canonical constants reference: every geometric constant in the programme, on one normalization, verified"
kind: definition + derivation
status: solid
program: yang_mills
extracted_by: claude-opus-5, 2026-09-01
verification: all values computed independently from structure constants; exact agreement for SU(2..5)
purpose: the corpus quotes N/4, N/2, N/12, 1/6, 0.25, 0.125, (N^2-1)/(2N) and 0.2909 without a common convention; this reconciles them
reproduction: 02_extracted/verification_scripts/geometric_constants.py
related: EX-001, EX-002
---

# Canonical constants reference

The corpus uses at least eight different numerical constants for "the curvature" or "the
mass coefficient", in at least three metric normalizations, often without saying which.
Several apparent contradictions in the documents are pure normalization mismatches; at
least one is a genuine conflation of two different quantities.

**This table fixes a convention and puts everything on it.** Anyone continuing the work
should adopt it.

## The convention

Take `X, Y ∈ 𝔰𝔲(N)` anti-Hermitian and traceless. Two inner products appear:

| Label | Definition | Orthonormal basis |
|---|---|---|
| **(A)** *(recommended)* | `⟨X,Y⟩_A = 2 tr(X†Y) = −2 tr(XY)` | `T_a = (i/2)λ_a` |
| **(B)** | `⟨X,Y⟩_B = tr(X†Y) = −tr(XY)` | `√2·T_a` |

They differ by a factor of 2: `⟨·,·⟩_A = 2⟨·,·⟩_B`. Curvature *ratios* `Ric/g` therefore
differ by a factor of 2 between them, which is the source of the `N/4` vs `N/2` confusion.

Convention **(A)** is recommended because it makes `T_a = (i/2)λ_a` — the basis actually
used in the corpus's own code (`safe_scan_tracked_v2.py`, `su3_haar_hessian_scan.py`) —
orthonormal, so numerics and analysis agree without a hidden rescaling.

## The table

All values verified numerically for SU(2), SU(3), SU(4), SU(5) to machine precision.

| Quantity | Symbol | Convention (A) | Convention (B) | SU(2)ᴬ | SU(3)ᴬ |
|---|---|---|---|---|---|
| Ricci curvature of `SU(N)`, bi-invariant | `Ric = κ_G·g` | **`N/4`** | `N/2` | 0.5 | 0.75 |
| Haar Jacobian potential Hessian at `e` | `Hess V_Haar(0)` | **`N/12`** | `N/6` | 0.166667 | 0.25 |
| Ratio | `κ_G / Hess V_Haar` | **`3`** | `3` | 3 | 3 |
| Quadratic Casimir, fundamental | `C₂(F)` | `(N²−1)/(2N)` | — | 0.75 | 1.3333 |
| Quadratic Casimir, adjoint | `C₂(A)` | `N` | — | 2 | 3 |

`Ric` and `Hess V_Haar(0)` are both **isotropic** — proportional to the identity, with no
preferred subspace. This is a computed fact, not an assumption (min eigenvalue = max
eigenvalue to machine precision in every case).

The relation `κ_G = 3 · Hess V_Haar(0)` holds in **both** conventions, since it is a ratio.
It is exact and worth remembering: the group's own Ricci curvature is exactly three times
the curvature the Haar Jacobian contributes in the exponential chart.

## Mapping every constant the corpus quotes

| Corpus value | Where it appears | What it is | Correct? |
|---|---|---|---|
| `N/4` | `MasterTheorem.lean` (`weyl_floor`), "Weyl floor" docs | `Ric(SU(N))` in convention **(A)** | ✅ |
| `N/2` | `WILSON/03_decay_bounds/` ("`κ_G = N/2` for `⟨X,Y⟩ = −Tr XY`") | `Ric(SU(N))` in convention **(B)** | ✅ — same fact, other normalization |
| `0.25` | `su3_haar_hessian_scan_results.csv` at `r=0` | `Hess V_Haar` for SU(3), conv. (B) — equivalently `N/12`·2 | ✅ |
| `1/6` | "1/6 per link, exponential chart" | `Hess V_Haar` for SU(2), conv. (A) = `2/12` | ✅ |
| `0.290892665` | `safe_scan_results_scaled.csv` | a third rescaling; ratio to 0.25 is 1.1636 | ⚠️ normalization undocumented |
| `c₀ = 0.125` | `su3_haar_hessian_scan.py` convexity scan | an **added quadratic regulator** `c₀Σ‖A‖_F²`, *not* the Haar term | ⚠️ mislabeled `haar_mass` in code |
| `(N²−1)/(2N)` | `lean/YangMills/HaarMassCoeff.lean`, `MasterTheorem.lean` | `C₂(F)`, the fundamental Casimir | ❌ **not a curvature** — see below |
| `m_H² = N/4` | `MatrixHinge.lean` | `Ric`, conv. (A) | ✅ |

## The one genuine error

`lean/YangMills/HaarMassCoeff.lean` defines

```lean
def haar_mass_coeff (N : ℕ) : ℚ := (N^2 - 1) / (2 * N)
```

under the header "Formal proof of the Haar mass coefficient formula", and
`MasterTheorem.lean` uses it as `haar_mass_sq N a = haar_coeff N / a²`.

`(N²−1)/(2N)` is the **quadratic Casimir of the fundamental representation**, `C₂(F)`.
It is not the Haar Jacobian Hessian, which is `N/12` (conv. A). For SU(3):

$$ C_2(F) = 4/3 \approx 1.3333 \qquad\text{vs}\qquad \operatorname{Hess}V_{\rm Haar}(0) = 1/4 = 0.25 $$

a factor of **16/3 ≈ 5.33**. These are different quantities with different `N`-scaling
(`~N/2` versus `~N/12`), so no choice of normalization reconciles them.

Anywhere the Lean development's `haar_coeff` is used as the coefficient of a curvature or
mass term derived from the Haar measure, it is the wrong constant. Note this does not by
itself change any conclusion — the obstruction results are `N`-independent in form — but it
must be fixed before any quantitative statement is made.

## Derivations

**Ricci.** For a compact Lie group with bi-invariant metric and orthonormal basis `{e_a}`,
`Ric(X,X) = ¼ Σ_a ‖[X,e_a]‖²`. Equivalently `Ric = −¼B` with `B` the Killing form; for
`𝔰𝔲(N)`, `B(X,Y) = 2N tr(XY)`, giving `Ric(X,X) = (N/2)‖X‖²_HS`. In convention (A),
`g(X,X) = 2‖X‖²_HS`, so `Ric = (N/4)g`. In (B), `g = ‖X‖²_HS` and `Ric = (N/2)g`.

**Haar Hessian.** See `EX-001` for the full derivation:
`V_Haar(X) = (N/12)‖X‖²_HS + O(X³)`, giving `N/12` in convention (A).

**Ratio.** `Ric/Hess = (N/2)/(N/6) = 3` in HS terms — independent of `N` and of convention.

## Reproduction

`verification_scripts/geometric_constants.py` recomputes the whole table from structure
constants. `verification_scripts/haar_hessian_check.py` verifies the Haar Hessian by
autodiff. Both run in seconds and require only numpy (plus torch for the second).
