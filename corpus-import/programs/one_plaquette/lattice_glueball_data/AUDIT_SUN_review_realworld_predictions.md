# Review — SU(N) real-world predictions (`NOTE_SUN_realworld_predictions_2026-06-13.md`)

**2026-06-13.** Independent review. Grounds: **[V]** verified here, **[NV]** not independently verifiable
from the uploaded material, **[FLAG]** issue to fix.

## Overall: well-tiered and honest, with two items to flag.

The document's discipline is good — it separates **controlled** (Tier 1: ordering/existence),
**demarcation** (Tier 2: exact but N-mismatched), and **uncontrolled** (Tier 3: continuum mass), and it
corrects the earlier extrapolation to use the band-minimum `c₄(Γ)=−2.857916`. The headline Tier-2 result
is the strongest and it is correct.

## Verified [V]
- **Tier 2 leading formula & scaling (the real result).** `m(1⁺⁻)/√σ|₀ = 2√((N²−1)/N)` reproduces SU(3) →
  `3.266`; it grows as `~2√N → ∞`, while the lattice ratio is N-independent; they cross accidentally at
  **N ≈ 8.41**. The mismatch is *structural* — leading mass ∝ C₂ ∝ N and σ ∝ C₂ ⇒ `m/√σ ∝ √N` — so it is
  robust to the O(1) σ convention. This is a clean, honest demarcation of "strong coupling ≠ continuum."
- **Ordering arithmetic.** `m(2⁺⁺)−m(0⁺⁺) = (22/51)y² > 0`; `m(1⁺⁻)−m(2⁺⁺)=2y+O(y²)` with the `+2y`
  dominating to `y≈11`. The `1⁺⁻` O(y) coefficient `+1` matches my **independently verified** series
  `8/3+y+(11/306)y²`.
- **Tier 1b existence.** `1⁺⁻ ∝ Im Tr U_p ≡ 0` for SU(2) (pseudoreal) — correct; the channel needs N≥3.
- **Tier 3.** Borel–Padé reproduces; with the corrected `c₄` the stable `[2/1],[1/1]` approximants are
  **unchanged** (a₄ only moves `[1/3]`), confirming the doc's own point that the bracketing of 6.07 leans
  on low orders and is *consistency, not prediction*. Correctly labelled.

## Flags
- **[FLAG 1 — overstatement] "the 1⁺⁻ is the heaviest glueball."** This is true only among the **three
  single-plaquette ground states** the leading band program produces (`0⁺⁺, 2⁺⁺, 1⁺⁻`). It is **not** the
  heaviest glueball overall: the AT continuum tower (this folder's `DATA_FLUX_at_continuum_spectrum.csv`) has many
  heavier states — `1⁻⁻ (8.31√σ)`, `2⁻⁻ (8.08)`, `1⁻⁺ (8.48)`, `2⁺⁻ (8.74)`, plus radial excitations.
  Recommend rephrasing to "the heaviest of the three leading single-plaquette channels."
- **[FLAG 2 — unverified inputs] the `0⁺⁺/2⁺⁺` coefficients** `−217/1020`, `+223/1020` come from
  `ENGINE_FLUX_glueball_band_certificate_v2.py`, which is **not** in my independently-verified set (only the `1⁺⁻`
  series is). The *ordering* `0⁺⁺<2⁺⁺<1⁺⁻` is lattice-confirmed regardless, but the SC *explanation* of the
  `0⁺⁺/2⁺⁺` split rests on those unverified numbers. Worth a gate check.
- **[FLAG 3 — external data, recommend confirming] the SU(N≥4) lattice values** (and the `N=∞` `1⁺⁻ ≈
  5.76(25)`) live in `DATA_SUN_glueball_jpc_core_benchmark_v2.csv`, which was **not** uploaded. The SU(3) value
  `6.065` is independently verified (AT 2020); the *N-independence* of glueball ratios at large N is
  established lattice physics (Lucini–Teper–Wenger; AT). I could not re-extract the specific N=4..∞ numbers
  (the source arXiv:2106.00364 page was too heavy to render in-browser). The Tier-2 *conclusion* survives
  even if those numbers shift by their error bars (it needs only N-independence vs `√N`), but the table
  itself should be checked against the source before it goes in a paper.

## Net
The Tier-2 demarcation and the existence statement are solid and well-argued; the tiering is honest and the
`c₄` correction is right. Fix the "heaviest glueball" phrasing, gate the `0⁺⁺/2⁺⁺` coefficients, and confirm
the SU(N) lattice CSV against arXiv:2106.00364. Reproduction: `ENGINE_SUN_verify.py`.
