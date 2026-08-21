# The O(y⁵) folded-coefficient identity (H₅ des-Cloizeaux, scalar-PVP sector)

**2026-06-13.** Attacking the O(y⁵) inter-plaquette leakage — the one computation that gates
whether the strong-coupling series reaches the continuum 1⁺⁻ mass.

## Honest scope first
The **full** O(y⁵) leakage is a major computation the program has not done and cannot be completed
reliably in one session:
- Geometry enumeration runs 1, 6, 156, 5082, 182440 for orders 0–4 (≈36× per order) ⇒ order 5 is
  ≈6–7 million connected multisets.
- The trace wiring gains a 7th event (28 corner variables vs 24), pushing treewidth past 17; the
  worst order-4 blocks already sit at 3¹⁸ peak color states.
- The des-Cloizeaux folded coefficient is **order-specific**: the pipeline's
  `folded_coefficient_from_denominators` is exactly the H₄ Hermitian identity. Order 5 needs a **new**
  H₅ identity — which is the analytic bottleneck, and is what this note delivers.

## Delivered: the exact H₅ folded coefficient
Under PVP = aP scalar in the model space (the same assumption the O(y⁴) pipeline uses — i.e. the band
is flat at O(y)), the fifth-order Hermitian effective-Hamiltonian coefficient multiplying each raw
five-V ordered word depends only on its intermediate energy denominators (d₁,d₂,d₃,d₄), via:

| model-space returns (zero denominators) | coefficient (nonzero denominators shown) |
|---|---|
| 0 | 1/(d₁ d₂ d₃ d₄) |
| 1 (a,b,c) | **−½ · (ab+bc+ca)/(abc)²**  = −½[1/(a²bc)+1/(ab²c)+1/(abc²)] |
| 2 (a,b) | **+⅓ · (a²+ab+b²)/(ab)³**  = ⅓[1/(a³b)+1/(ab³)+1/(a²b²)] |
| 3 (a) | **−¼ / a⁴** |
| 4 | 0 |

Diagonal pattern: the j-return coefficient is **(−1)ʲ/(j+1)** (−½, +⅓, −¼), the harmonic folding
signature — and at order 5 the 2-return term carries the genuinely new symmetric structure
(both 1/(a³b)+1/(ab³) and 1/(a²b²) with equal weight ⅓).

## How it was derived and validated (`folded5_derivation.py`)
1. Exact eigenvalue coefficients c₁…c₅ for random rational scalar models via exact Rayleigh–Schrödinger
   recursion (the same exact-PT engine used for the within-plaquette tower).
2. The folded coefficient is parameterized by zero-pattern + symmetric functions of the nonzero
   denominators; the unknowns are fixed by a full-rank 4×4 linear match to exact c₅.
3. **Method cross-check:** the identical procedure at order 4 reproduces the pipeline's published
   coefficients (−½, ⅓) exactly.
4. **Validation:** path-sum with the solved H₅ coefficients equals exact c₅ on 14 fresh independent
   models (n = 4 and 5), every one matching.

## What this unblocks
This is the missing analytic kernel for an order-5 generalization of the pipeline's Stage 3I
(`folded_coefficient_from_denominators` → order 5). With it in hand, the remaining work to obtain the
actual flat-band c₅ is purely the heavy geometric/contraction lift (order-5 supports, 7-event trace
wiring, exact tensor contraction) — large, but now no longer blocked on new mathematics.

The actual numerical c₅ (and hence whether Borel–Padé converges to 6.07) still requires that
contraction; it is **not** delivered here. What is delivered is the exact, validated H₅ identity it
depends on.
