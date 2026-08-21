# Glueball physical-mass prediction + continuum diagnostic — intake (2026-06-14)

**What this is.** The physics payoff line of the one-plaquette program: turning the exact
strong-coupling glueball spectroscopy into a statement about the **physical SU(3) 1⁺⁻ glueball
mass**, plus an honest diagnostic of how far the strong-coupling series alone can be pushed toward
the continuum. Two Alex-uploaded reports, intaken with the verification I could do.

## 1. Blind held-out lattice prediction across gauge rank (`AUDIT_SU3_glueball_mass_prediction_report_v1.md`)

A 1/N² fit `m_{1⁺⁻}(N)/√σ = m_∞ + c/N²` to **lattice** continuum values at N=4,5,6,8,10,12 (the SU(3)
datum withheld) gives the **blind prediction**
\[ m_{1⁺⁻}(SU(3))/\sqrt\sigma = 6.151 \pm 0.266 \quad(\sigma_{fit}=0.079,\ \sigma_{model}=0.254,\ \chi^2/dof=0.677/4). \]
Unblinding against the modern benchmark **6.065 ± 0.040** → blind error **+0.086 (0.32σ)**. With the historical
scale r₀⁻¹=410(20) MeV and r₀√σ=1.19, this is **m_{1⁺⁻} ≈ 3.00 ± 0.20 GeV**. An independent Hamiltonian-limit
datum (r₀m=7.17(17) ⟹ 6.025±0.143) is consistent. (Also: the often-cited 8.31 is the 1⁻⁻ ground state, not 1⁺⁻.)

**Honest scope (the doc's own).** This is a genuine held-out **lattice-data extrapolation across rank**, motivated
by the exact theorem (which supplies the 1/N² correction and identifies the channel) — it is **NOT** an analytic
continuation of the strong-coupling y-series. The remaining goal is a same-normalization string-tension bridge that
predicts the continuum mass *from the series itself*.

## 2. Why the series alone can't yet reach the continuum (`NOTE_SU3_glueball_ratio_continuum_diagnostic_2026-06-14.md`)

Scale-matched ratio (corrected normalization, u=β/6): `m/√σ = √6 Σ rₙ yⁿ`, anchor **R(0)=4√6/3 ≈ 3.266**. The exact
4th-order polynomial peaks at y\*≈0.469 with **R₄≈3.730 — 38.5% below the continuum 6.065** (and R₄(y)=6.065 has no
positive root). All near-diagonal **Padé, Dlog-Padé, Borel-Padé fail** (positive-axis poles / wrong asymptotic limit).
Conclusion: the 4th-order series is internally stable only at small coupling and **cannot be extrapolated to the
continuum**; the minimum next requirement is the **5th/6th-order ratio coefficients** (→ needs m₅ [have], m₆ [open],
native σ₅,σ₆) plus finite-coupling Hamiltonian anchors, and **shell-six mixing** before the isolated one-plaquette
branch is the physical lowest 1⁺⁻ state.

## 3. The 1/N² extrapolation + high-N predictions (`NOTE_FLUX_glueball_highn_predictions_2026-06-14.md` + plot)

The fuller version of the prediction (the plot Alex shared). Weighted fit to Athenodorou–Teper continuum
data, **1/N² form supplied by the exact theory, values by the lattice**:
\[ m_{1⁺⁻}/\sqrt\sigma(N) = 5.759(25) + 2.91(46)/N^2. \]
Strongest internal check: the fit's **N→∞ intercept 5.759(25) matches the lattice's independently-measured
N=∞ datum 5.760(25) to 0.02σ** (and that datum was *not* used in the fit). Leave-one-out RMS = 0.045 (~ the
lattice error bars), so the 1/N² form is genuinely predictive across rank. SU(3) is the least-controlled point
(most-extrapolated): held-out 6.151 vs measured 6.065(40) — ~2σ on the tight error, 0.3σ on the conservative.
**Falsifiable forward predictions** (interpolations between N=12 and N=∞): N=14→5.774, 16→5.771, 20→5.767,
24→5.764 (±0.051); the ratio has effectively converged to its large-N limit by N≈14 (finite-N correction <0.3%
beyond) — a future SU(14)/SU(16) lattice run ≠ 5.77 would falsify it.

**Independent cross-check (mine):** I re-did the weighted 1/N² fit from the plotted AT points and got
**intercept 5.757, slope 2.94, held-out SU(3) 6.148** — reproducing the doc's 5.759 / 2.91 / 6.151 to
plot-reading precision. Forward-prediction arithmetic (5.759+2.91/N²) reproduces the table exactly.

## Verification this session (grounds)
- **R(0)=4√6/3** confirmed (sympy); the ratio normalization is the corrected u=β/6 / σ(u)=½W(2u) one (consistent with
  `../su3_o5_consolidated_y6/`). The 1/N² lattice fit and Padé/Borel diagnostics are **reports of data analysis** — I
  did not re-run the multi-rank fit (input lattice table not all in-bundle); intaken as **documented diagnostics**, not
  machine-reproduced here. Honestly: the blind 0.32σ agreement is striking but is a lattice-data extrapolation, T0/doc-grade,
  **not** a from-series or proven result. No continuum claim is asserted.

## Provenance
Sources (Alex uploads 2026-06-14): `AUDIT_SU3_glueball_mass_prediction_report_v1.md`, `NOTE_SU3_glueball_ratio_continuum_diagnostic_2026-06-14.md`.
Per-file MD5 in `MAN_SUN_md5sums.txt`. Related: `../su3_o5_consolidated_y6/` (ratio coefficients, normalization), `../../../papers/flat_band/` (the paper).

## Open / next
- 5th/6th-order **ratio** coefficients into a continuation (needs m₆ + native σ₅,σ₆).
- shell-six mixing before the one-plaquette branch = physical lowest 1⁺⁻.
- a same-normalization string-tension bridge for a from-series continuum mass.
