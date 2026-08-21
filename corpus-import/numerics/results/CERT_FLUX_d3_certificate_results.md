# O(y³) Glueball Band Coefficients: Exact d₃ and a Correction to Theorem 6.2

**Status: machine-certified, exact rational arithmetic throughout. 251 gates in
`ENGINE_FLUX_su3_domino_d3.py` + 27 gates in `ENGINE_FLUX_su3_moments_ext.py`, all passing.**
Results JSON: `RUN_TROM_d3_results.json`.

---

## 1. Headline result: the C-odd flat band through O(y³)

The T₁⁺⁻ (C-odd) glueball band of the SU(3) one-plaquette-class lattice
Hamiltonian is exactly flat through third order, with

> **m₋(k) = 8/3 + y + (11/306) y² − (109151/249696) y³  for all k.**

Numerically: 11/306 ≈ 0.035948 and 109151/249696 ≈ 0.437135.

The mechanism for persistent flatness is the previously certified theorem that
all O(y³) tromino weights vanish (bare-link lemma: trominoes activate only at
O(y⁴)). Consequently the third-order lattice effective Hamiltonian in the
C-odd sector has the *same* signed-adjacency structure as at second order —
verified here by the σ-covariance gate T₃(s) = −T₃(−s) — and the signed
adjacency possesses an exactly flat band at μ ≡ −4 for every k. The flat-band
coefficient is then the same uniform contraction as at O(y²):

    d₃ = 7/32 + 12·leak₃ − 4·b₃
       = 7/32 + 12·(−12331/249696) − 4·(1975/124848)
       = −109151/249696,

with machine-exact ingredients

    b₃   = T₃ᵒ(s=+1)            =  1975/124848      (per-neighbor C-odd hop)
    D₃ᵒ  =                       −24541/62424        (domino C-odd diagonal)
    e₃ᵛᵃᶜ(domino) = −9/16  (= 2·(−9/32); no connected 3rd-order vacuum piece)
    leak₃ᵒ = (D₃ᵒ − e₃ᵛᵃᶜ) − 7/32 = −12331/249696   (per-neighbor leakage)

The dispersive C-odd band **top** (μ = 8) through O(y³):
m₋ᵗᵒᵖ = 8/3 + y + (41/306) y² − (61751/249696) y³.

The assembly contraction itself is validated by a gate showing the *identical*
formula at second order reproduces the known flat-band constant:
1/2 + 12·(−11/306) − 4·(5/612) = 11/306.

## 2. Correction to Theorem 6.2 (C-even lattice hopping)

The abstract-domino computation shows the C-even per-neighbor hopping at
second order is

> **t₊ = −11/306 = −481/612 + 3/4,**

not −481/612 as used in the paper's Theorem 6.2. The +3/4 is the
vacuum-mediated route ⟨e_r|W|0⟩⟨0|W|e_i⟩/(8/3 − 0) = (√2·√2)·(3/8), which is
absent for C-odd states (⟨o|W|0⟩ = 0, so Theorem 6.3 is untouched) but present
for C-even ones. The paper's channel sum
(1/9)(−3/4) + (8/9)(−6/17) + (1/3)(−1/2) + (2/3)(−1/3) = −481/612 is correct
*as a channel sum*; the omission is the |0⟩-intermediate route. Decisively,
the paper's own §7 domino diagonalization numbers discriminate between the two
values: the C-even domino gap levels are diag-gap ± |t₊| with diag-gap
1879/3060, and {1769/3060, 13/20} forces |t₊| = 110/3060 = 11/306, not
481/612. Our pipeline reproduces both paper level sets exactly:

    C-even domino levels: {1769/3060, 13/20}     [gate PASS]
    C-odd  domino levels: {31/68, 17/36}         [gate PASS]
    t⁻(s) = 5s/612                               [gate PASS]

Consistency check on distant (non-interacting) pairs: there the channel route
is the free two-flux sum 2·(8/3 − 16/3)⁻¹ = −3/4, and the vacuum route +3/4
cancels it exactly — recovering the established result that distant-pair
hopping vanishes. The adjacent-pair value −11/306 is the partial version of
the same cancellation.

Corrected second-order C-even constants (λ_S(k) ∈ [−4, 12], λ_S(0) = 12):

    m₊(k) = 8/3 − y + [ 13/20 − (11/306)(12 + λ_S(k)) ] y² + O(y³)

    A₁⁺⁺ at k = 0 (band minimum, location unchanged):  −217/1020   (≈ −0.2127)
        — replaces the paper's −9397/1020 (≈ −9.213)
    band top (λ_S = −4):                                1109/3060
    curvature near k = 0:                            +(22/459)|k|²  (was 481/459)
    full C-even bandwidth 16|t₊|:                        88/153     (was 1924/153)
    E⁺⁺ at k = 0:                                       223/1020    (UNCHANGED)

Because t₊ keeps its sign, the band minimum remains at k = 0; only the
magnitude of all hopping-derived quantities shrinks by the factor
(11/306)/(481/612) = 22/481.

## 3. New: the C-even channel at O(y³)

With the same pipeline (T₃ᵉ verified s-independent):

    T₃ᵉ = −6335/249696,   D₃ᵉ = −517313/6242400,
    leak₃ᵉ = (D₃ᵉ − e₃ᵛᵃᶜ) − 101/200 = −6335/249696.

**Exact identity (gated): leak_nᵉ = T_nᵉ at n = 2 and n = 3.** Both quantities
equal "channel sum + 3/4-type vacuum term," the diagonal's 3/4 arising from
vacuum-energy bookkeeping and the hop's 3/4 from the |0⟩ route; the identity
makes the A₁⁺⁺ correction at k = 0 equal to within-tower + 24·T_nᵉ per order.

    m₊(k) at O(y³) = 101/200 + 12·leak₃ᵉ + T₃ᵉ·λ_S(k):
      k = 0 (A₁⁺⁺):     −54049/520200   (≈ −0.1039)
      λ_S = −4:          471353/1560600 (≈ +0.3020)

Combined corrected scalar channel through third order:

> **m₊(k=0) = 8/3 − y − (217/1020) y² − (54049/520200) y³.**

## 4. Verification architecture (what guarantees these numbers)

Layer 0 — independent oracle. Weyl integration on the SU(3) torus: exact
Laurent constant-term over rationals with measure (1/6)Π|z_i − z_j|²,
z₃ = 1/(z₁z₂). No Weingarten input.

Layer 1 — moment engine (`ENGINE_FLUX_su3_moments_ext.py`, 27 gates). U(3) Weingarten for
balanced moments p = q ≤ 3; generic ε-matching projector blocks for charge
p − q = ±3 built from spanning tensors with an exact rational pseudo-inverse
of the brute-force Gram (internal asserts GKG = G, KGK = K). Battery includes
∫(trU)⁴ tr Ū = 3 with Inv(V⁴⊗V̄) rank 3 (one Schouten relation), the (1,4)
mirror, and (5,2). (6,0) is intentionally unsupported with a hard-fail guard;
a degree census shows per-closure Grams in this pipeline cap at (4,1)/(3,3).

Layer 2 — canonical word calculus. Two independent Haar matrices; SU(3)
Cayley–Hamilton rewrites g² = χg − χ̄ + g⁻¹ (and inverse) drive every trace
word to an alternating canonical form of non-increasing letter degree; H₀ acts
by exact Fierz surgery (½(SWAP − ⅓𝟙𝟙)) with side/sign insertion rules derived
from right/left translation derivatives, including the shared-link sign s.
Structural gates: H₀χ₁² = (20/3)χ₁² − 4χ̄₁ (3̄/6 split), H₀χ₁χ̄₁ = 6χ₁χ̄₁ − 6
(1/8 split), Tr g³ = χ³ − 3χχ̄ + 3, and the four shared-link channel 2×2
blocks reproducing Lemma 6.1 energies {4, 11/2, 14/3, 17/3} with the correct
s ↔ like/mixed assignment for both s = ±1.

Layer 3 — resolvent solves. Q-projection by exact overlaps; H₀-closure of each
vector (sizes 8 and 36); stacked rational solve with appended ⟨f_m|y⟩ = 0
rows. Per-solve gates: consistency, coefficient-level residual ≡ 0 (which is a
function identity), and every kernel vector of the stacked system is the zero
*function* (Gram norm 0) — so R is well defined without assuming basis
independence.

Layer 4 — des Cloizeaux to third order, two independent implementations.
H⁽¹⁾ = −PWP, H⁽²⁾ = +PWRWP, H⁽³⁾ = −PWRWRWP + ½{PWR²WP, PWP}. The word
calculus and a fully independent spectral implementation (irrep basis with
exact Schur characters via Jacobi–Trudi on the torus) both reproduce the
strong-coupling Bridge towers: vacuum (−3/4, −9/32), level shifts
(−1/10, −1/4), gaps {13/20, 1/2} and {101/200, 7/32}.

Layer 5 — domino gates. Vacuum e₂ = −3/2 and e₃ = −9/16 (predicted: no
connected third-order vacuum diagram); manifold orthonormality; h₁, h₂, h₃
Hermitian, C-block-diagonal, swap-symmetric at both s; order-2 reproduction of
every §7 number; order-3 σ-covariance (T₃ odd in s) and s-independence of T₃ᵉ,
D₃ᵒ, D₃ᵉ — nontrivial cancellations across distinct Fierz insertion patterns.

Layer 6 — assembly. The d₃ contraction is the same one gated against the known
O(y²) flat-band constant, with certificate locks pinning every exact rational.

## 5. What changes in the paper, and what does not

Changes: Theorem 6.2's hopping constant (−481/612 → −11/306) and every number
derived from it (the −9397/1020 scalar coefficient, curvature, bandwidth).
Suggested fix: add the vacuum-route lemma ⟨e_r|W R W|e_i⟩ ⊃ +3/4 for adjacent
and distant pairs alike, then restate the corrected constants of §2 above.

Unchanged: Lemma 6.1; the channel sum −481/612 *as a channel sum*; Theorem 6.3
and the C-odd sector entirely; all §7 domino diagonalization numbers (they
were correct and are what diagnose the issue); E⁺⁺ at k = 0 = 223/1020.

New theorems available: (i) m₋ flat through O(y³) with d₃ = −109151/249696;
(ii) corrected-and-extended scalar channel m₊(k=0) through O(y³); (iii) the
leakᵉ = Tᵉ identity at orders 2–3.

## 6. Reproduction

    python3 ENGINE_FLUX_su3_moments_ext.py    # 27 gates: moment engine vs torus oracle
    python3 ENGINE_FLUX_su3_domino_d3.py      # 251 gates: full pipeline -> RUN_TROM_d3_results.json

Both scripts are pure Python 3 standard library (fractions, itertools); no
external dependencies; every printed constant is an exact rational.
