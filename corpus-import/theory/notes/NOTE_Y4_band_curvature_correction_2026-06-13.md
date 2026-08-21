# Correction: O(y⁴) 1⁺⁻ band-edge curvatures are anisotropic (not isotropic)

**2026-06-13.** Correcting NOTE_Y4_synthesis_band_vs_lattice.md §1 ("band-edge effective masses
(isotropic, by cubic symmetry): +0.104 at Γ, −0.036 at R") and falsifiable-prediction point 4.

## The error
The SYNTHESIS reports a single isotropic curvature at each edge, justified "by cubic symmetry."
That justification fails: at Γ the three coordinate-plane one-flux states are **triply degenerate**
(this is exactly the statement H₄(0) = c₄(Γ)·I). The effective-mass tensor of a band emerging from a
degenerate (T₁) edge carries cubic **warping** — the cubic group relates equivalent directions but does
**not** force [100] = [110] = [111]. Direct computation confirms the band is anisotropic at both edges;
the quoted "+0.104" is essentially the [110] value and "−0.036" is exactly the [100] value, i.e. single
directions misreported as the isotropic curvature.

## The exact corrected curvatures (d²c₄/d|k|², from the verified H₄ kernel)
Along the high-symmetry directions the C-odd vector w(k) is a genuine eigenvector, so these are **exact**,
not finite-difference estimates:

| direction | Γ (band bottom) | R (band top) |
|---|---|---|
| [100] | **5/24** = +0.20833 | −111910685208057689/3107395837972483200 = −0.03601 |
| [110] | 247051057231349/2202655210329600 = +0.11216 | −180411173111623579/3107395837972483200 = −0.05806 |
| [111] | **+ΔW₄/6** = +0.08010 | **−ΔW₄/6** = −0.08010 |

with ΔW₄ = 132329431693349/275331901291200 ≈ 0.48062 the exact bandwidth.

Two clean exact facts worth keeping:
- **Γ [100] curvature = 5/24** exactly.
- **Body-diagonal curvatures = ±ΔW₄/6**: Γ[111] = +ΔW₄/6 and R[111] = −ΔW₄/6 exactly — an internal
  consistency tie between the band-edge curvature and the bandwidth.

Anisotropy ratio: ~2.6× at Γ (0.208 → 0.080) and ~2.2× at R (0.036 → 0.080). Not isotropic by any reading.

## Corrected falsifiable-prediction point 4
Replace "band isotropic at Γ with bottom curvature +0.104·y⁴ and top curvature −0.036·y⁴" with:

> 4. band **anisotropic** at both edges (cubic warping from the triply-degenerate edge). Exact O(y⁴)
>    curvatures d²m/d|k|²: at Γ, +(5/24)y⁴ along [100], +(ΔW₄/6)y⁴ along [111]; at R, −(ΔW₄/6)y⁴ along
>    [111], ≈−0.036·y⁴ along [100]. A measurement must resolve the **direction dependence**; an isotropic
>    fit would misrepresent the kernel.

This matters operationally: feeding a tensor-network / exact-diagonalization test the wrong *isotropic*
curvatures would spuriously falsify (or falsely confirm) the correct kernel. Everything else in the
prediction is unaffected — Γ-min/R-max, flat through O(y³), and the exact bandwidth 0.48062·y⁴ all stand.
