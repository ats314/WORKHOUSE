# Strong-coupling → continuum extrapolation of the 1(+-) glueball mass
**2026-06-13 — bold attempt, honest reporting.** Object: turn the exact strong-coupling series
for the flat C-odd (T1^{+-}) band into a number we can put next to the lattice continuum mass.

## Target
Lattice continuum (Athenodorou–Teper SU(3)):  **m(1^{+-})/√σ = 6.065(40)**.

## Input series (lattice / Kogut–Susskind units)
m_-(y) = 8/3 + y + (11/306)y² − (109151/249696)y³ + c4 y⁴ + …
with **c4 = −4555981615057344457/1812647572150615200 ≈ −2.5134**, the rigid O(y⁴) component
from the (independently re-verified) breaking calculation — so this is a genuine **5-term** series,
not 3. Coefficients: 2.667, 1, 0.036, −0.437, −2.513 → magnitudes grow ⇒ **divergent/asymptotic**
(as a strong-coupling series must be).

String tension at leading order: σa² = 2/3 (one fundamental link's electric energy per unit length).
⇒ exact leading ratio **m(1^{+-})/√σ |₀ = (8/3)/√(2/3) = 3.266 = 54% of the lattice value.**

## What each method gives
- **Truncation:** dead. O(y²) at y≈2 peaks near 5.9, but O(y³) and O(y⁴) terms crash it (−12, −48).
- **Padé of m_-(y), y→∞:** nonsense (−7.5, 0, +∞) — the coefficient pattern defeats it.
- **Borel–Padé (5 terms), evaluated vs y:**
  | approx | y=1 | 1.5 | 2.0 | 2.5 |
  |---|---|---|---|---|
  | [2/1] | 4.50 | 5.11 | **5.73** | 6.34 |
  | [1/1] | 4.54 | 5.21 | **5.91** | 6.65 |
  | [1/2] | 4.09 | 4.14 | 4.09 | 3.98 |
  | [1/3] | 3.87 | 3.74 | 3.54 | 3.33 |
  | [2/2] | 4.75 | 5.91 | 11.3 | 9.97 |
  | [3/1] | 4.72 | 10.9 | 6.51 | 7.52 |
  The two stable (near-diagonal) approximants [1/1],[2/1] **pass through 6.07 at y≈2.1–2.3**, which
  is the coupling region of SU(3)'s strong-to-weak crossover. The finite-limit approximants saturate
  low (~3.3–4.1); [2/2]/[3/1] have spurious poles.

## Verdict
**Consistent and encouraging, not controlled.** The lattice 6.07 lies inside the resummation
scatter (~3.3–11) and the *stable* Borel–Padé hits it at the physically relevant coupling. With a
divergent 5-term series this is a consistency check, not a prediction. It did **not** cleanly fail.

## Direction (working back from here)
1. **σ(y) series — highest value.** Only the leading 2/3 is used. Magnetic corrections lower σ ⇒
   raise m/√σ ⇒ every number above is a **floor**; including σ(y) moves the stable estimates up
   toward / past 6.07. This is the decisive missing input and is computable in the same framework.
2. **More mass orders (O(y⁵), O(y⁶)).** Tests whether Borel–Padé converges to 6.07 or to ~4. The
   O(y⁴) engine already exists; extending it is the natural next computation.
3. **y ↔ continuum-coupling map.** Pin which y the lattice crossover/continuum corresponds to, so the
   "crosses at y≈2.2" statement becomes quantitative rather than suggestive.

## Honest scope for the paper
This belongs in the paper as a **consistency remark**, not a theorem: *the resummed strong-coupling
series for the flat C-odd band is consistent with the measured continuum 1^{+-} glueball mass, with a
controlled prediction pending σ(y) and higher orders.* Do not state a single extrapolated number as
"the prediction" until (1)–(2) are done.
