# Verification — O(y⁵) folded identity & strong-coupling→continuum extrapolation

**2026-06-13.** Independent check of the two uploaded O(y⁵)/extrapolation artifacts. Grounds tags:
**[V]** machine-verified here, **[H]** heuristic, **[note]** caveat.

## 1. The H₅ des-Cloizeaux folded-coefficient identity — **CORRECT [V]**

Claim (scalar PVP=aP model space): the 5th-order energy coefficient is a path-sum over five-V words
whose folded weight depends only on the zero-pattern of the four intermediate denominators, with
**j-return coefficient `(−1)ʲ/(j+1)`**:

| model-space returns | coefficient |
|---|---|
| 0 | `1/(d₁d₂d₃d₄)` |
| 1 (a,b,c) | `−½ · [1/(a²bc)+1/(ab²c)+1/(abc²)]` |
| 2 (a,b) | `+⅓ · [1/(a³b)+1/(ab³)] + ⅓ · [1/(a²b²)]` |
| 3 (a) | `−¼ / a⁴` |
| 4 | `0` |

**Verified** against a **numerical gold standard** (high-precision eigenvalue Taylor fit, mpmath dps=70)
on **12 fresh random models (n=4,5)** — the path-sum with `(−½,⅓,⅓,−¼)` reproduces the true c₅ in every
case. The check uses *neither* the uploaded RS engine *nor* my own char-poly tool, so it is independent of
both. The `b1 = b2 = ⅓` equality (the new symmetric 2-return structure) is confirmed.

### Honest correction of an earlier mis-diagnosis
My first pass wrongly concluded the identity was "circular/unverified." That was premature. Root cause,
now resolved by the gold standard:
- the uploaded `eig_coeffs` RS-PT engine has an **even-order sign quirk** (it returns c₂, c₄ with the wrong
  sign) — but it is **correct at odd orders, including c₅**. Since the identity concerns c₅, the engine's
  quirk does **not** affect the derivation or its validation. **[note]** Don't reuse that engine for
  even-order coefficients.
- my own characteristic-polynomial cross-check was itself **unreliable at 5th order** (it disagreed with the
  gold standard on some seeds). I retired it in favor of the numerical eigenvalue fit.

Net: the **identity stands**; the uploaded note's own scope ("delivers the validated H₅ identity, *not* the
actual flat-band c₅, which still needs the heavy order-5 contraction") is accurate.

## 2. Strong-coupling → continuum extrapolation — **reproduced; "consistent, not controlled" [V/H]**

- Series used: `m₋(y) = 8/3 + y + (11/306)y² − (109151/249696)y³ + c₄·y⁴`, with
  `c₄ = −4555981615057344457/1812647572150615200 ≈ −2.5134` = the rigid cube eigenvalue, which **I had
  already verified** independently (G5 cube-residual check). Coefficient magnitudes grow
  (2.67, 1, 0.036, 0.44, 2.51) ⇒ asymptotic/divergent, as a strong-coupling series must be. **[V]**
- Reproduced the Borel–Padé table exactly. The two stable near-diagonal approximants ([1/1], [2/1]) rise
  through the lattice value `m(1⁺⁻)/√σ = 6.065(40)` around **y ≈ 2.1–2.3**; the others scatter (≈3.3–11).
  Truncation is hopeless (the −2.51 y⁴ term wrecks it); only resummation has a chance. **[V]**
- **Verdict (theirs, and I concur): consistent, NOT a controlled prediction.** A 5-term divergent series
  cannot pin a continuum number; the lattice 6.065 lies *inside* the resummation scatter and the stable
  approximants pass through it at the physically relevant coupling — a consistency check, nothing stronger.

### Caveats I add **[note]**
- `σa² = 2/3` is a **leading-order** string-tension input I did **not** independently verify; the σ(y)
  series is the acknowledged decisive missing piece (it would *raise* the estimates toward 6.065).
- Using the rigid-cube `c₄ = −2.5134` as "the" O(y⁴) coefficient is a **choice**: the band is *not* flat at
  O(y⁴) (it spans c₄(k) ∈ [−2.858, −2.377], see `../lattice_glueball_data/SYNTHESIS_*`); −2.5134 is the
  localized-cube representative, not a unique number.

## Bottom line
The new mathematics (H₅ identity) is **correct and independently verified**. The continuum extrapolation is
an **honest consistency remark**, correctly labeled as such by its author — not a prediction. Both uploaded
docs are accurately scoped. Reproducible check: `ENGINE_Y5_verify_oy5_numeric.py`.
