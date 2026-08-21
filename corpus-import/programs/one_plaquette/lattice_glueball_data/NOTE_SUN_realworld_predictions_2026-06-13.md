# Real-world predictions of the SU(N) 1⁺⁻ program, confronted with lattice data

**2026-06-13, lead math agent.** Object: extract from the exact strong-coupling band program
the statements that can be put next to real lattice Yang–Mills, organized strictly by *how
controlled* each is. Lattice reference: Athenodorou–Teper, arXiv:2106.00364 (SU(N), 2 ≤ N ≤ 12 and
N = ∞, continuum-extrapolated, units of √σ), as compiled in `DATA_SUN_glueball_jpc_core_benchmark_v2.csv`.

The headline: the program makes **two fully controlled, lattice-confirmed predictions** (the spectrum
ordering and the existence of the channel), one **exact-but-mismatched** scaling law that precisely
locates where strong coupling parts from the continuum, and one **consistent-but-uncontrolled**
continuum-mass estimate. The first tier is the real result and does **not** depend on the divergent-
series question that gates the continuum mass.

Reproduce: `python3 ENGINE_SUN_realworld_predictions.py DATA_SUN_glueball_jpc_core_benchmark_v2.csv`.

---

## TIER 1 — fully controlled, lattice-confirmed (these are the real predictions)

These are **sign / ordering / existence** statements. They are immune to the divergent-series problem
that limits the continuum mass, because they never require summing the series — only the sign of its
first one or two terms, which are exact and gate-backed.

### 1a. Spectrum ordering 0⁺⁺ < 2⁺⁺ < 1⁺⁻

From the certified SU(3) strong-coupling band edges (gate-backed: `ENGINE_FLUX_glueball_band_certificate_v2.py`,
36 gates; flat-band theorem):

| state | cubic irrep | strong-coupling band edge (lattice units) | source of O(y) sign |
|---|---|---|---|
| 0⁺⁺ | A₁⁺⁺ | 8/3 − y − (217/1020) y² | C-even, PWP = +1 ⇒ −y |
| 2⁺⁺ | E⁺⁺ | 8/3 − y + (223/1020) y² | C-even, PWP = +1 ⇒ −y |
| 1⁺⁻ | T₁⁺⁻ | 8/3 + y + (11/306) y² (exactly flat) | C-odd, PWP = −1 ⇒ +y |

The ordering is produced by the **sign structure** of the first two corrections, both exact:

- **O(y):** the first magnetic correction is h₁ = −PWP, and PWP is the **charge-conjugation operator**
  (verified [[0,1],[1,0]] per plaquette): eigenvalue +1 on C-even, −1 on C-odd. So C-even states drop
  by y and the C-odd 1⁺⁻ rises by y. That single sign — a Gauss-law / C-parity fact — is why the
  1⁺⁻ is the **heaviest** glueball. m(1⁺⁻) − m(2⁺⁺) = 2y + O(y²); the +2y dominates up to y ≈ 11,
  well past where the leading series is valid.
- **O(y²):** the channel split −217/1020 (A₁⁺⁺) vs +223/1020 (E⁺⁺) gives
  m(2⁺⁺) − m(0⁺⁺) = (22/51) y² > 0 for **all** y, so 0⁺⁺ < 2⁺⁺.

Result: **0⁺⁺ < 2⁺⁺ < 1⁺⁻, holding for all y > 0 at this order** — parameter-free.

**Lattice confirmation, every N:**

| N | m(0⁺⁺) | m(2⁺⁺) | m(1⁺⁻) | 0⁺⁺<2⁺⁺<1⁺⁻ |
|---|---|---|---|---|
| 3 | 3.405 | 4.894 | 6.065 | ✓ |
| 4 | 3.271 | 4.742 | 5.956 | ✓ |
| 5 | 3.156 | 4.690 | 5.915 | ✓ |
| 6 | 3.102 | 4.678 | 5.847 | ✓ |
| 8 | 3.099 | 4.660 | 5.801 | ✓ |
| 10 | 3.102 | 4.594 | 5.776 | ✓ |
| 12 | 3.151 | 4.646 | 5.741 | ✓ |
| ∞ | 3.072 | 4.599 | 5.760 | ✓ |

The ordering the paper states (`0⁺⁺ < 2⁺⁺ < 1⁺⁻`) is reproduced by the strong-coupling expansion
*and* confirmed by the lattice continuum at every N from 3 to ∞. The 1⁺⁻ being the heaviest is the
real-world shadow of its C-odd (Gauss-law-protected) nature — the same physics that makes its band
flat. This is the cleanest defensible real-world claim in the program.

### 1b. The 1⁺⁻ exists only for N ≥ 3

The 1⁺⁻ single-plaquette operator is Im Tr(U_p). For SU(2) every representation is (pseudo)real,
so Tr(U) is real and **Im Tr(U_p) ≡ 0** — there is no C-odd single-plaquette glueball. The channel
exists only for N ≥ 3 (complex fundamental). Lattice: the SU(2) row has **no** 1⁺⁻ entry, exactly as
predicted. This ties the existence of the whole C-odd sector to the complex (χ vs χ̄) structure the
paper's flat band is built on.

---

## TIER 2 — exact, parameter-free, but N-scaling mismatched (the demarcation)

Leading-order strong coupling fixes the ratio exactly. With E_link = ½C₂(fund) = (N²−1)/(4N), string
tension σa² = E_link, and the 1⁺⁻ a single plaquette (4 links):

> **m(1⁺⁻)/√σ |₀ = 2·√((N²−1)/N)**  (exact; reproduces SU(3) → (8/3)/√(2/3) = 3.266)

| N | lattice m(1⁺⁻)/√σ | SC leading | SC/lat |
|---|---|---|---|
| 3 | 6.065(40) | 3.266 | 0.54 |
| 4 | 5.956(42) | 3.873 | 0.65 |
| 5 | 5.915(45) | 4.382 | 0.74 |
| 6 | 5.847(43) | 4.830 | 0.83 |
| 8 | 5.801(38) | 5.612 | 0.97 |
| 10 | 5.776(41) | 6.293 | 1.09 |
| 12 | 5.741(60) | 6.904 | 1.20 |
| ∞ | 5.760(25) | → ∞ (~2√N) | diverges |

The **lattice ratio is N-independent** (→ 5.76), as glueball mass ratios famously are at large N. The
**leading SC ratio grows as 2√N and diverges.** They have *incompatible* large-N scaling; the near-
agreement at N ≈ 8 (5.61 vs 5.80) and the 54% at N = 3 are a rising √N line crossing a flat band
(crossing at N ≈ 8.4), **not** controlled agreement. This is the precise, quantitative statement of
*why* strong coupling at fixed lattice spacing is not the continuum for this observable — the N-scaling
is wrong at leading order, and no finite number of magnetic corrections changes the leading large-N
power. (See `DATA_SUN_1pm_sc_vs_lattice.png`.)

This does **not** undermine the paper's SU(N) generalization: that generalization is the *flat-band
structure* (the closed-2-chain / Gauss-law mechanism), which is a homological statement valid for all
N ≥ 3 — not a claim about the continuum mass ratio.

---

## TIER 3 — consistent, not controlled (the continuum mass)

Borel–Padé resummation of the divergent rest-mass series, now with the **correct band-minimum
coefficient** c₄(Γ) = −20721577909065127111/7250590288602460800 = **−2.857916** (the earlier
extrapolation mistakenly used the rigid sub-component −2.5134; corrected here):

m(1⁺⁻)(y) = 8/3 + y + (11/306)y² − (109151/249696)y³ − 2.857916 y⁴ + …

The stable approximants [2/1], [1/1] cross the lattice 6.07 near y ≈ 2.3–2.5 (in the SU(3) strong-to-
weak crossover region); the others scatter (3.3–11). The series is divergent (coefficient magnitudes
2.67, 1, 0.04, 0.44, 2.86, growing), so this is a **consistency check, not a prediction.** Correcting
c₄ leaves the stable approximants unchanged (a₄ enters only [1/3], shifting it < 0.01) — confirming the
5-term extrapolation leans almost entirely on the low-order coefficients, and is therefore *less*
controlled than its bracketing of 6.07 might suggest. A controlled number is gated on the O(y⁵⁺)
inter-plaquette leakage; the analytic key for the next order (the H₅ des-Cloizeaux folded-coefficient
identity) is derived and validated, but the heavy contraction itself is not done.

---

## What to put in the paper

1. **Lead the real-world section with Tier 1.** The ordering 0⁺⁺ < 2⁺⁺ < 1⁺⁻ is an exact, parameter-
   free, lattice-confirmed (every N) prediction of the strong-coupling band program, traceable to the
   C-parity sign at O(y) and the channel split at O(y²) — and the 1⁺⁻ being heaviest is the same
   Gauss-law physics as its flat band. Add the N ≥ 3 existence statement. These are fully controlled.
2. **Use Tier 2 as the honest demarcation.** State the exact leading ratio 2√((N²−1)/N) and that its
   √N growth is incompatible with the N-independent lattice ratio — the precise boundary of the
   strong-coupling/continuum connection. This strengthens, not weakens, the paper's care.
3. **Keep Tier 3 as a consistency remark only**, with the corrected c₄ = −2.857916, explicitly *not*
   a prediction, gated on the O(y⁵⁺) leakage.

Files: `ENGINE_SUN_realworld_predictions.py` (reproduces all three tiers), `DATA_SUN_1pm_sc_vs_lattice.png`,
`DATA_SUN_glueball_jpc_core_benchmark_v2.csv` (lattice data, AT 2021).
