# Strongest Novel Derivations in `SIMULATIONS/`

**Assembled 8 August 2026.** Every constant below was re-derived from the source
files, not transcribed. Where a result did not survive independent checking, it is
recorded in §6 rather than omitted.

---

## Summary

The defensible novel content of this corpus is concentrated in **one** thread: the
exact strong-coupling expansion of the SU(3) glueball band in the Kogut–Susskind
Hamiltonian (`y4_*.py`, `su3_*.py`, `tromino_*.py`, `ENGINE_FLUX_cls_flat_band_certificate.py`,
`ENGINE_FLUX_glueball_band_certificate_v2.py`).

That thread produces a genuine, self-contained theorem with a clean mechanism:

> **The C-odd (1⁺⁻, T₁) one-flux glueball band of SU(3) lattice gauge theory is
> exactly flat through O(y³), for a homological reason (∂∂ = 0), and first
> acquires dispersion at O(y⁴) with exact bandwidth 132329431693349/275331901291200 ≈ 0.4806 y⁴.**

The whole chain runs in exact rational arithmetic (`fractions.Fraction`,
`sympy.Rational`) with hard assertion gates, and terminates in an interval-arithmetic
branch-and-bound certificate for the global band edges. It reproduces from a clean
directory in ~10 minutes.

Four results are presented below in descending order of how well they would survive
review. §5 lists the load-bearing assumptions honestly. §6 lists what did not hold up.

---

## 1. The O(y²) flat band and its Gauss-law mechanism

*Sources: `ENGINE_FLUX_cls_flat_band_certificate.py` (13/13 gates), `ENGINE_FLUX_glueball_band_certificate_v2.py` (35 gates).*
**This is the strongest single item in the corpus.**

### Setup

Kogut–Susskind Hamiltonian on a 3D spatial cubic lattice, gauge group SU(3):

    H = H₀ − y W,     W = Σ_p ( Tr U_p + Tr U_p† )

with `y` the dimensionless magnetic coupling (`y ∝ 1/g⁴`; `y → 0` is strong coupling).
In units where a fundamental link costs E_link = ½C₂(3) = 2/3, a single excited
plaquette costs **E₀ = 8/3** — the leading mass gap.

The model space P is the **one-flux sector**: a single excited plaquette, three
orientations (xy, xz, yz) per site. Degenerate perturbation theory gives a three-band
Bloch problem; splitting by charge conjugation yields a C-even sector (0⁺⁺ A₁, 2⁺⁺ E)
and a C-odd sector (1⁺⁻ T₁). The C-odd branch is *the band*.

### Result

    m₊(k) = 8/3 − y + y² [ 223/1020 − (11/306) λ(k) ],   λ(k) ∈ [−4, 12]

    m₋(k) = 8/3 + y + y² [ 7/102  + (5/612)  μ(k) ],     μ(k) ∈ [−4,  8]

and the lowest C-odd branch has **μ(k) = −4 identically in k**, so

    m₋ = 8/3 + y + (11/306) y²     for every k.

The band is exactly flat — zero bandwidth at O(y²), not merely small.

The coefficient **11/306** closes an interval left open as `[−3/102, 17/102]` in the
prior Theorem 6.3 of this program. That is the sharpest novelty claim in the file, and
it is a *closure*, not a re-derivation.

### Mechanism — why it is flat

This is the part worth publishing. Let `S(k)` be the signed shared-link adjacency
symbol of the plaquette hopping. Then, exactly:

    S(k) + 4I  =  B(k) B(k)†

where `B(k)` is the **plaquette-to-link boundary symbol** — each plaquette feeds signed
amplitude into its four boundary links, with incidence signs σ ∈ {±1}. Two consequences
follow immediately:

1. `S(k) ⪰ −4I` as an operator — the spectrum is bounded below by −4;
2. the flat band **is** `ker B(k)†`, i.e. the states with zero net signed flux into
   every link channel.

And `ker B†` is spanned by the consistently (Levi-Civita) oriented **boundary of a
single elementary cube** — six faces, amplitudes ±1. These are compact localized
states: strictly zero outside one cube. They are annihilated because every cube edge is
shared by exactly two faces with opposite induced orientation.

**Flatness is the statement ∂∂ = 0.** The band is flat because the boundary of a
boundary is zero. That is a homological protection mechanism, not a numerical
coincidence, and it is what makes the result robust rather than accidental.

The explicit flat Bloch vector, with `u_j = 1 − e^{ik_j}`:

    w(k) = ( ū₃ , −ū₂ , ū₁ )

### The sharp all-orders criterion (gate T4)

The mechanism generalizes into a criterion that does real work downstream:

> Any effective hopping correction whose symbol has the **link-mediated form**
> `B(k) M(k) B(k)†`, with M an arbitrary Hermitian symbol, annihilates the flat-band
> subspace *exactly*. The band stays flat with unshifted hopping energy; only
> diagonal, k-independent constants can move it.

So the entire question "does the band survive at higher order?" collapses to a single
scalar test:

    flat at O(y⁴)   ⟺   u(k)† H₄(k) v(k) = 0

Companion gate G12 shows the criterion is **sharp**: corner-sharing symbols, which are
*not* of the form BMB†, do lift the band. So the criterion is not vacuous.

This is a clean, short, hand-checkable piece of lattice homology plus spectral theory.
It would survive review essentially as written.

---

## 2. The O(y³) tromino-vanishing lemma

*Sources: `ENGINE_FLUX_su3_domino_d3.py` (251 gates), `ENGINE_TROM_tromino_contract_independent_check.py` (16 gates).*

At third order the band **still** does not disperse. It shifts rigidly:

    b₃          =  1975/124848
    leak₃(odd)  = −12331/249696
    d₃ = 7/32 + 12·leak₃ − 4·b₃ = **−109151/249696** ≈ −0.4371355568

    m₋(k) = 8/3 + y + (11/306) y² + (−109151/249696) y³     for ALL k.

*(Verified: `7/32 + 12·(−12331/249696) − 4·(1975/124848) == −109151/249696` exactly.)*

### The bare-link lemma — a genuine group-theory argument

Why do the O(y³) "tromino" geometries (three-plaquette, two-hop paths `p → q → r`)
vanish? Not numerically — structurally:

> Every three-distinct-plaquette two-hop geometry leaves the middle plaquette with **at
> least two links touched by nothing else**. A single χ_q insertion therefore deposits
> unremovable fundamental flux on a bare link, and the amplitude vanishes **by
> triality**.

This kills all 32 five-trace O(y³) numerators exactly. It is a selection rule from the
center ℤ₃ of SU(3), not a cancellation that happens to occur.

### Independent second leg

The same conclusion is reached through a symbolic geometry contract, which is a useful
cross-check because it is mechanically unrelated:

    B_backtrack = 12 I
    B_samelink  = 2 S
    B_corner    = −2 S⊥
    B_path₊ + B_path₋ + B_corner = S² − 12I − 2S

Equal lifter weights therefore act as a constant on the flat line, and the corner class
alone is what provably lifts (0 at X versus 16 at R).

---

## 3. The O(y⁴) dispersion and the global band-edge certificate

*Sources: stages `y4_stage0` → `y4_stage3j`, `y4_band_curvature_exact.py`,
`y4_global_band_edge_certificate_final.py`.*

Ten stages — geometry enumeration → SU(3) channels and denominators → exact Haar
projectors → fusion-tree tensors → trace wiring → global contraction → des-Cloizeaux
folding — produce a 189-record real-space H₄ kernel. The verdict:

    cube_boundary_residual_nonzero : true
    flat_through_order_y4          : false
    first_nonzero_bandwidth_order  : y^4

    exact bandwidth = 132329431693349 / 275331901291200 = 0.48061786909826

Band edges, all exact rationals (computed, not inserted):

| point | c₄ (exact) | decimal |
|---|---|---|
| Γ | −20721577909065127111 / 7250590288602460800 | −2.8579159881 |
| X | −17700498622147435111 / 7250590288602460800 | −2.4412493214 |
| M | −4367164159624988707 / 1812647572150615200 | −2.4092737202 |
| R | −3447362930970494909 / 1450118057720492160 | −2.3772981190 |

*(Verified: c₄(R) − c₄(Γ) equals the stated bandwidth exactly.)*

### Closed-form band curvature

Near Γ, `c₄(k) ≈ c₄(Γ) + ½ κ_d |k|²` with exact directional curvatures

    κ[100] = **5/24**  = 0.2083333…
    κ[110] = 247051057231349 / 2202655210329600 ≈ 0.1121606
    κ[111] = 132329431693349 / 1651991407747200 ≈ 0.0801031

all positive, confirming Γ is the minimum. The quartic form
`T₄ = A Σᵢ kᵢ⁴ + B Σᵢ<ⱼ kᵢ²kⱼ²` has

    A = **5/48**,     B = 17607806155349 / 1101327605164800

and satisfies the two independent consistency identities exactly:

    A = ½ κ[100]        ✓
    A + B/2 = κ[110]    ✓

`κ[100] = 5/24` and `A = 5/48` are strikingly clean numbers sitting on top of a very
large computation — that is weak evidence the tower is not corrupted, though not proof.

### The certificate

The global minimization over the Brillouin zone is a real computer-assisted proof:
`mpmath.iv` interval arithmetic at 45 dps, branch-and-bound, with exact sympy Taylor
remainder bounds and a factor-2 safety margin.

    GLOBAL MINIMUM AT Γ: proved=true, processed_boxes=1590, unresolved_boxes=0
    GLOBAL MAXIMUM AT R: proved=true, processed_boxes=76,   unresolved_boxes=0

The local certificates are clean: `λ = min(A, (A+B)/3)` is the exactly correct minimum
of the cubic quartic form on the unit sphere, and the remainders `Σ|a_r||r|⁴/4!` and
`Σ|a_r||r|⁶/6!` are correct cosine Taylor bounds in exact rationals.

---

## 4. Two reusable exact tools

### 4a. The SU(3) Haar moment engine — `ENGINE_FLUX_su3_moments_ext.py` (27 gates)

Exact rational U(3) Weingarten calculus for p = q ≤ 3, plus a generic projector block
for |p − q| = 3 built from ε-matching invariant tensors, with a pseudo-inverse Gram via
kernel completion:

    K = (G + N Nᵀ)⁻¹ − N (Nᵀ N)⁻² Nᵀ

Every block is validated against a fully independent oracle: Weyl integration on the
SU(3) maximal torus as an exact Laurent constant-term extraction. Sample results:

    ∫ (tr U)⁴ tr(Ū) dU = 3
    Inv(V⊗⁴ ⊗ V̄) has rank 3, not 4   (Schouten relation)

Not novel mathematics, but a correct, exact, reusable engine — worth releasing as a
standalone utility.

### 4b. The order-5 folded des Cloizeaux identity — `folded5_derivation.py`

Exact fifth-order folded scalar coefficients, by zero-count:

    0-zero : 1/(d₁d₂d₃d₄)
    1-zero : −½ [ 1/(a²bc) + 1/(ab²c) + 1/(abc²) ]
    2-zero :  ⅓ [ 1/(a³b) + 1/(ab³) ] + ⅓ [ 1/(a²b²) ]
    3-zero : −¼ / a⁴
    4-zero :  0

The order-4 analogue drives the pipeline. Caveat in §5.

---

## 5. Load-bearing assumptions (state these before publishing)

These are real and a referee will find them. None is currently fatal; all are unclosed.

1. **`PVP = aP` is assumed, never verified in code.** Physically plausible — a single
   plaquette operator should not hop within the one-flux sector — but it is an
   unchecked structural input to the *entire* O(y⁴) result. Closing this is cheap and
   should be done first.

2. **The folded formula is regression-tested only in the non-degenerate case.** The
   validation solves `det(h₀ + yV − E(y)I) = 0` order by order, i.e. a **1-dimensional**
   model space. The object actually computed is an *operator* on a large degenerate
   model space, and its off-diagonal hopping structure is exactly what sets the
   bandwidth. That structure is never regression-tested. `folded5_derivation.py`
   additionally *fits* its coefficients from a 4×4 system on 4 random models and then
   validates on 14 more — persuasive, but a fit plus spot-check, not a derivation.

3. **Incomplete independent regression.** Stage 3H independently recomputes 1,478 of
   3,895 topologies. The 2,417 mixed/all-resonant (folded) topologies have **no**
   independent recomputation. Also, the one-command endgame bundle silently omits
   stages 3F and 3H — running it as documented reports
   `stage3h_topologies_regressed: 0`. They must be run manually.

4. **A normalization caveat is quietly dropped.** Stages 3F and 3H both exclude "any
   convention-dependent magnetic-operator prefactor not already absorbed into the
   project's y-normalization." By 3I/3J the sentence disappears with no gate resolving
   it. If such a prefactor exists, every O(y⁴) number is off by a global factor.

5. **Interval-arithmetic leaks (small but real).** Three places in
   `y4_global_band_edge_certificate_final.py` compute in plain `mp.mpf` and then wrap
   the *point* result in an interval (`theta`, `delta`, and `plo/phi` in
   `interval_direct`). `initial_boxes` also tiles with the rounded `mp.pi`, leaving a
   ~10⁻⁴⁵-wide uncovered sliver at the zone boundary. At 45 dps against margins of
   ~10⁻⁶ nothing is wrong in practice, but as written the certificate is not fully
   rigorous. Fixing it is mechanical.

6. **Perturbation theory degenerates where the minimum is claimed.** At k → Γ the flat
   band *touches* the two dispersive branches (‖u(k)‖² = Σ sin²(kⱼ/2) → 0), so the
   O(y²) level spacing ~y²|k|² drops below the O(y⁴) perturbation once |k| ≲ y. Γ itself
   is handled correctly (H₄(Γ) is gated scalar), but "the minimum sits at Γ" is asserted
   precisely where the expansion is least controlled.

7. **No data files ship with the code.** `DATA_Y4_full_real_space_h4_kernel.json.gz` — which
   every endgame script consumes — is absent, and no reference SHA is stored. Anyone
   auditing must regenerate it. Add the file and its hash to the repository.

8. **The series is divergent.** `sc_extrap2.py` says so itself. Coefficient magnitudes
   2.667, 1.000, 0.036, 0.437, 2.513 are growing; Borel–Padé estimates from 5 terms
   cluster in 4–6, straddling but not converging to the lattice value 6.07. The file's
   own verdict — "consistent, not controlled" — is the right one.

9. **Scope, in the code's own words:** *"This is an order-by-order strong-coupling
   statement. It is not a continuum Yang–Mills claim."* Explicitly not claimed:
   all-orders behavior, continuum glueball bandwidth, continuum Yang–Mills mass gap.
   Keep that sentence in any abstract.

10. **One downstream inconsistency.** `sc_extrap2.py` feeds the *rigid component*
    (−2.5134, the CLS diagonal matrix element) into the mass-gap series;
    `ENGINE_SUN_realworld_predictions.py` correctly uses the band minimum c₄(Γ) = −2.857916.
    The older file was never updated.

---

## 6. What did not survive checking

Recorded so the effort is not repeated. All three findings come from independent
re-implementation, not from reading the notebooks' own verdicts.

### "Theorem B" (~43 notebooks) — the claim is not supported

`ρ_eff ≥ N/2 − M²/γ` is asserted in markdown and never proved, derived, or given
hypotheses anywhere in 43 notebooks. Numerically:

- **The Schur bound's precondition fails.** It requires `H_ηη ≻ 0`. Under the
  notebooks' own formula, at β = 0, `λ_min(H_ηη) < 0` for **100.0%** of 4000 Haar links
  (SU(3), SU(4), SU(5)); at β = 5.5 it fails 1.5–12.9%, rising with N. When γ < 0 the
  term −M²/γ becomes *positive* and inflates ρ_eff. The famous "σ_θ ≈ N/2" is a sign
  artifact of dividing by a negative γ.
- **The Hessian is unbounded below, so no Bakry–Émery constant exists to measure.** The
  Haar potential's Hessian diverges as −1/φ² at eigenangle collisions — analytic, not
  noise: λ_min = −5.86, −220, −3761, −2771419 as the angle gap goes 1.0 → 0.2 → 0.04 →
  0.002. `GAMMA_FLOOR` and `median` are censoring an infinite tail, not adding
  robustness. The theorem needs an infimum; the code reports a median.
- **Same run, both verdicts.** Median: `ρ = +24`, printed as `THEOREM B SUPPORTED`.
  Mean: `−7.9 × 10³⁴`.
- **ρ_eff carries no information beyond the plaquette.** With U ≈ I, `H_W ≈ β·3·plaq·I`
  → 13.695 predicted vs 12.951 measured (SU(3)). The `haar_weight = 0.00` control —
  Haar term *off*, i.e. the alleged source of the gap removed — is the only setting
  giving a clean positive answer with zero failures: `13.331 ± 0.011, 0.0% neg`.
- **"Linear growth in N" is imposed.** β = 5.5·N/3, so β ∝ N, so ρ ∝ N automatically.
  At fixed β it is flat. This is 't Hooft coupling scaling restated.
- **It fails where the answer is known.** At β → 0, where SZZ23 *proves* a gap:
  `ρ_eff mean = −inf` → `✗ FAIL: Something wrong`. Volume scaling: L = 6,8,10,12 all
  give `−inf ± nan`.
- Wrong coupling regime (β_std ≈ 16.5–30, plaquette 0.83, vs real SU(3) at β_std ≈
  5.7–6.5, plaquette ≈ 0.5–0.6); not the lattice Hessian (8×8 single-link with
  neighbours frozen — the off-diagonal link–link blocks, where a spectral gap would
  live, are never computed); and no mass gap, correlator, string tension, or continuum
  limit is ever measured.
- The headline result originated on a lattice that was **never thermalized**
  (plaquette ≈ 0, i.e. Haar-random links, where σ_θ ≈ N/2 is a trivial property of
  random SU(3) matrices) and evaporated the moment the staple and action bugs were
  fixed — σ_θ jumped to 13.865 against a "theory" of 1.5. From v12.14 the notebooks stop
  reporting that ratio.

**Salvageable, and genuinely worth a short technical note:** the *analytical Wilson +
Haar Hessian* is correct. Verified independently against finite differences at β = 0
(the regime the notebooks never validated, since their β = 5.5 check is swamped by the
~30× larger Wilson term):

    SU(3): corr = 1.00000000, max|diff| = 9.40e-06, median rel err = 9.14e-08
    SU(4): corr = 1.00000000, max|diff| = 1.93e-06, median rel err = 1.26e-07

Both pieces hold: `H_W[a,b] = (β/2) Re Tr({T_a,T_b} U V)`, and the non-obvious
second-order eigenangle correction

    ∂²θ_k/∂ω_a∂ω_b = Σ_{j≠k} cot(φ_kj/2) Re(R_aj R̄_bj)

That correction is the mathematically interesting part and it is right. (Drop the
"100× faster" framing — the notebooks' own timing cells report 1× or slower at N = 3.)

### The 4D SU(2) θ-term / TRG thread — not yet started

- **No Wilson action.** The weight is `exp(−β j(j+1))` per *leg*, not
  `exp(β Re Tr U_p)` per plaquette. There is no plaquette anywhere; this is closer to a
  spin-foam state sum. The 6j argument pattern `(j₀,j₁,k,j₂,j₃,k)` is asserted, not
  derived. And `q = e^{iθ}` as "the θ-term" is a physics claim with no derivation
  (the q ↔ level relation lives in 3D Chern–Simons, not a 4D F∧F term).
- **No coarse-graining.** One implementation discards `U` from the SVD and strips one
  index per "step" (8 legs → 4); the other truncates a 16×16 matrix to bond dimension
  16, making `weave_step` the identity up to normalization. No lattice is ever doubled,
  so there is no thermodynamic limit and nothing that is meaningfully "4D."
- **θ is never implemented in the U(1) work.** `create_gauge_tensor_numpy(beta, theta,
  N_max)` accepts `theta` and never uses it — the comment says
  `# Villain weight (without theta term for now)`. The 25-point θ scan returns
  `F = 10.190587` at every θ; `ΔF = 0.000000`. A 150-simulation β×θ scan (236 s) was
  then run on identically-zero θ-dependence and concluded "✓ Stable numerical
  convergence across all θ values."
- **Nine mutually contradictory χ_top values**, both signs, two orders of magnitude —
  for a quantity that is non-negative by definition. The +1.30 result is
  `chi_top_estimate = max(0.5, Q_avg)` inserted and then recovered by a quadratic fit;
  `Q_avg` is the mean *array index*. The +1.46 result comes entirely from a
  divide-by-zero at θ = π, where `q = e^{iθ}` hits a root of unity and `[n]_q` vanishes.
- **The one validation that would have caught all of this was never run.**
  `trg_ising_colab.ipynb` never scans temperature; it reports `f = −0.000008` at
  β = 0.5 where Onsager gives −2.051586 — five orders of magnitude off — and prints
  "✓ System is near the critical point!". Two bugs: the free-energy normalization
  divides by `4**n_steps` instead of weighting each level by tensors remaining, and the
  tensor `T[i,j,k,l] = Σ_s exp(β·s·(i+j+k+l)/4)` is not the Ising tensor.
- Also: 3D SU(2) mass gap runs are unequilibrated (⟨P⟩ oscillates between −0.65 and
  +0.89); ν = −0.0407 is declared "≈ −1/2" by a one-sided test `nu_asym > -0.65`; the
  "area law" has area increasing 27× while Ω increases 1.18×, and is capped by the
  Lanczos iteration count (`m_steps=100` → 97–98 positive eigenvalues at every L).

**Salvageable:** the Levin–Nave `trg_step` kernel itself is correct. Fed a proper Ising
tensor (`W = sqrtm(M)`), the *unmodified* kernel gives rel. err 4.97e-04 against
Onsager at β = 0.5. The plumbing is fine; nothing built on it was ever validated.

### The q-Racah / Doob gap — correct, but a rediscovery

`Untitled100.ipynb` Cell 0 is the one clean implementation (correct symmetrization
`off = −sqrt(B[:-1]·D[1:])`, PSD with E₀ = 0 to 10⁻¹⁶). Its gap is **exactly
N-independent** — 8 identical digits over N = 20…200 — and obeys

    m_q(N) = (1/q − 1)(1 − αc/d)

verified to ≤ 5×10⁻¹⁶ across three parameter sets. This is the n = 1 case of the
standard Askey–Wilson / q-Racah eigenvalue `λₙ = (q⁻ⁿ − 1)(1 − dt·qⁿ)`. So it is
**correct but not new**, and the notebook misreads it: there is no finite-size scaling
to extract, because there is no finite-size dependence.

The sibling notebooks are wrong. `Untitled94.ipynb` builds a **non-symmetric** matrix
(`H[n,n+1] = −Aₙ` but `H[n+1,n] = −C_{n+1}`); `np.linalg.eigh` silently reads only the
lower triangle, so the birth rates never enter the spectrum. Its gap is 0.0762696 where
the correct value is 0.0011326 — **a factor of 67**. Its `m_inf ≈ 0.027` is a 1/N fit to
non-monotone, faster-than-1/N data (the true limit is 0: the gap at N = 200/400/800 is
1.23e-4 / 2.1e-5 / 4e-6). Its exponent `nu ≈ −1.043` has the sign inverted and R² = 0.31.

---

## 7. Recommended next steps

Ordered by return on effort.

1. **Close `PVP = aP` in code.** Cheapest way to remove the largest unchecked input.
2. **Commit the H₄ kernel and its SHA.** Currently nothing is reproducible without a
   10-minute rerun and there is no reference hash to check against.
3. **Fix the interval leaks** in `y4_global_band_edge_certificate_final.py` — enclose
   `theta`, `delta`, `plo/phi`, and tile with an outward-rounded π. Mechanical, and it
   turns "morally rigorous" into "rigorous."
4. **Regression-test the folded formula on a degenerate model space**, or state plainly
   that it is validated only in the non-degenerate case.
5. **Extend Stage 3H** to the 2,417 folded topologies, or scope the claim to what is
   independently regressed.
6. **Resolve the magnetic-prefactor normalization** with an explicit gate.
7. Write up §1 alone as a short paper. The flat band + Gauss-law factorization + T4
   criterion is self-contained, hand-checkable, and does not depend on the O(y⁴) tower
   or any of its caveats. It is publishable now.
8. Write up the analytical Wilson+Haar Hessian (§6) as a separate technical note,
   detached from Theorem B.
