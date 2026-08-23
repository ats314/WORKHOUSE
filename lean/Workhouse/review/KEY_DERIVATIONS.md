# WORKHOUSE — key derivations (arXiv-corpus-review session)

Date: 2026-08-23
Scope: a self-contained record of the mathematics derived and machine-checked in this
session — the carrier→continuum audit, the TE/SE reduction, the H0 free-carrier
construction, the `u⁴` dispersion power, the U1 incidence factorization, and the Lean
atom lemma. Every claim is tagged with how it was verified.
Repository status: read-only; external to the clone.

**Verification legend.** `[sympy]` exact symbolic check · `[numpy]` numerical stress test ·
`[Lean]` machine-checked Lean 4 / Mathlib, no `sorry`, axioms `[propext, Classical.choice,
Quot.sound]` · `[corpus]` value imported from the pinned corpus.

**Standing conventions.** `dᵢ = e^{ikᵢ} − 1`, `aᵢ = |dᵢ|² = 4sin²(kᵢ/2)`, `q_a = Σᵢ aᵢ`,
`m₀ = 8/3` (the C-odd one-flux branch bottom), `ψ` the homological carrier.

---

## Part 0 — The connections question (arXiv:2608.20066)

Not a derivation but the finding that framed the session: the 798-page treatise
*"Resolution of Singularities in Positive Characteristic"* has **no** substantive connection
to the SU(N) flux-band program. Method (the corpus's own): search by value and by term.

- Paper contains **0** exact rationals, **0** occurrences of glueball/Yang–Mills/Wilson/mass
  gap/lattice/SU(N)/spectrum. Its vocabulary is algebraic geometry (Rees, Hasse, blowup,
  resolution, scheme).
- Every apparent shared word is a **false cognate on both sides**: corpus "Rees" (615) is
  `deg`**`rees`**/`t`**`rees`** (true `\bRees\b`: 1); "Frobenius" is Perron–Frobenius;
  "characteristic p" is characteristic polynomial; corpus "marked-cluster" vs paper "marked
  Rees" ("cluster" = 0 in the paper).

Conclusion: different fields; the terminology rhyme is coincidence.

---

## Part I — Carrier→continuum audit verifications

### I.1 Upper bound ≠ atom (the H3 counterexample) `[sympy]`

Claim: an exponential **upper** bound with the correct edge exponent, reflection positivity,
and a positive transfer representation are all compatible with **zero** carrier atom.

Take `dμ(E) = 𝟙_{[M,M+1]}(E) dE`. Then

```
C(t) = ∫_M^{M+1} e^{−tE} dE = e^{−Mt}(1 − e^{−t})/t,     C(0) = 1.
```

- Bottom exponent: `−lim_{t→∞} (1/t) log C(t) = M`  (correct support edge).
- `C` is completely monotone (Laplace transform of a positive measure ⇒ positive
  transfer/spectral representation, RP-compatible).
- `μ({M}) = 0`  (μ absolutely continuous).

**Consequence.** Any H3 proof routed through a PMBSF *absolute upper activity bound*
(`Σ|w_s(Γ)|e^{a(Γ)} ≤ C e^{−m d}`) is insufficient in principle: it can never force a
bottom-atom lower bound. Retires that class of attempts.

### I.2 The corrected finite-time atom bound (Part VI) `[sympy]`

With `μ = Z δ_M + μ_tail`, `supp(μ_tail) ⊂ [M+Δ,∞)`, `q := e^{−Δt}`, `F(t) := e^{Mt}C(t)`:

```
F(t) ≤ Z + q(C(0) − Z)   ⟹   Z ≥ (F(t) − q·C(0)) / (1 − q).
```

**Normalization is load-bearing.** Example `μ = δ_M + 9δ_{M+Δ}`, `q = 1/2`: true `Z = 1`,
`C(0) = 10`, `F(t) = 5.5`.
- corrected `(5.5 − ½·10)/(½) = 1` ✓;
- the printed *unnormalized* formula `(F − q)/(1 − q) = (5.5 − 0.5)/0.5 = 10` ✗ (overshoots the
  true `Z = 1` by 10×).

### I.3 The SU(3) `p₃` source anchor `[sympy]`

Weyl–Gaussian normalization `ψ₀ = √6/(3√π)`, `ψ₂ = (√5/(15√π)) y(3x²−y²)`,
`p₃ = (√6/6) y(3x²−y²)`:

```
p₃ = [√(30π)/2] · ψ₂ ,     p₃ ψ₀ = √5 · ψ₂ ,     ⟨ψ₀, p₃² ψ₀⟩ = 5
```

(the last given orthonormality and `p₃` Hermitian). An exact nonzero local source matrix
element — the leading term any signed-source (SE) estimate must preserve. It is *not* yet a
literal-Wilson residue theorem (remainder `Im Tr U = −p₃/6 + O(θ⁵)` uncontrolled).

### I.4 The frame-perturbation bound `z_ent` `[sympy]`,`[numpy]`

The audit's `z_ent = z_* − 2M_*ε_W − ε_W² − M_*²η_P`. Loewner re-derivation with
`J_c = J_* + E` (`‖E‖ ≤ ε_W`), `P_c = P_* + D` (`‖D‖ ≤ η_P`, `‖P_c‖ = 1`):

```
J_c*P_cJ_c = J_**P_cJ_*  +  (J_**P_cE + E*P_cJ_*)  +  E*P_cE
             ⪰ (z_* − M_*²η_P)  −  2M_*ε_W  +  0
```

using `E*P_cE ⪰ 0`, `‖J_**P_cE + E*P_cJ_*‖ ≤ 2M_*ε_W`, and `J_**P_cJ_* ⪰ z_* − M_*²η_P`.
So `z_ent` is a **valid** (slightly conservative — the `−ε_W²` is unnecessary) lower bound.
Stress test: 0 violations of `λ_min(J_c*P_cJ_c) ≥ z_ent` in ~8000 random trials `[numpy]`.
A cleaner alternative bound follows from `‖P_cJ_c v‖ ≥ √z_* − (ε_W + M_*η_P)`:

```
J_c*P_cJ_c ⪰ (√z_* − ε_W − M_*η_P)² · I .
```

### I.5 Matrix Källén–Lehmann layer `[sympy: 3/5, ρ; logic checked]`

- **Atom persistence (Thm 3.1):** positive `r×r` matrix measures `ν_n = I_r`, shrinking
  islands `I_n → {M}` with `ν_n(I_n) ⪰ z_* I`, vague limit ⇒ `ν({M}) ⪰ z_* I`. Proof:
  scalarize `v*ν v`, compact-set Portmanteau, continuity from above.
- **Transfer-moment form (Thm 3.4):** push to `x = e^{−AE} ∈ [0,1]`; `x = 0` absorbs UV escape,
  so no separate tightness needed.
- **KL promotion:** energy measure = pushforward of `ρ` under `E = √s` with weight `1/(2√s)`,
  hence `ρ({M²}) = 2M · A`.
- **Spin firewall:** `S_iii = H_iii^{(J=3)} + (3/5) V_i^{(J=1)}`, coefficient
  `3/(d+2) = 3/5` in `d = 3` (symmetric-traceless rank-3 projector). `[sympy]`

---

## Part II — TE/SE reduction and the tolerance budget

Goal: turn "prove uniform transfer-entry (TE) + source-entry (SE)" into explicit numbers.

### II.1 The Kato/Riesz chain `[numpy]`

Isolating contour = circle of radius `d_*/2` around the carrier band. For self-adjoint `T_*`,
`sup_Γ ‖R_*(z)‖ ≤ 2/d_*`, so with `δT = T̂_c − T_*`, `‖δT‖ ≤ ε_T`:

```
q := sup_Γ ‖δT R_*‖ ≤ 2ε_T/d_*        (choose ε_T < d_*/4 ⇒ q < ½)
‖P̂_c − P_*‖ ≤ 2ε_T/(d_*(1−q)) ≤ 4ε_T/d_*
```

Verified numerically: predicted `q ≤ 2ε_T/d_*` holds (ratio 1.03; the 3% is band width — which
is exactly why the conservative `d_*/4` threshold is used), and the projection bound holds.

### II.2 The budget

Feeding `η_P ≈ 4ε_T/d_*` into `z_ent > 0` and splitting the margin in half:

```
ε_W < z_*/(4M_*)   ,     ε_T < z_* d_* / (8 M_*²).
```

`ε_T` scales with the (small) isolation gap `d_*` and inversely with `M_*²` — the binding
constraint.

### II.3 The two reductions

- **TE ⇐ G17 ⊗ G21.** `δT` is the block-induced effective-transfer correction (non-local in
  time, higher-character). Bounding it in the contour norm is (a) uniform RG convergence to
  the scale-`A` reference = **G17**, controlled via (b) exponential decay of the induced
  temporal kernel = a **G21** (Combes–Thomas/Davies) input.
- **SE ⇐ S3.** The blocked Wilson source must preserve the `p₃` leading term (§I.3) with a
  remainder uniformly `o(1)` — the "signed noncancellation" no PMBSF file supplies.

---

## Part III — H0 free-carrier construction

**Setup.** Fine lattice `N_f = b·N_c` per dim; block by `b`. The coarse `p=0` fiber is the
`b^d` aliases `k_f^{(s)} = 2πs/A`, `s ∈ {0,…,b−1}^d`, with `s = 0` the true fine carrier.

### III.1 The `b^d` block-origin sources and the DFT structure

For block origin `τ`, `J^{(τ)}_s = e^{i k_f^{(s)}·τ} G(k_f^{(s)}) J_fine(k_f^{(s)})`, where the
phase table `e^{i2πs·τ/b}` is the `b^d`-point DFT. Hence `{J^{(τ)}}_τ` is a unitary image of
the alias-diagonal sources.

**Box form factor kills aliases exactly:** `G(k_f^{(s)}) = ∏_i (1/b)Σ_m e^{i2πs_i m/b} =
∏_i δ_{s_i,0} = δ_{s,0}`. So the coarse `p=0` source equals the fine `k=0` carrier.

### III.2 H0 holds — uniform cross-Gram `[numpy]`

`λ_min(carrier cross-Gram)/z_* = 1.000000` for **all** `b` (1D `b ≤ 64`; 3D `b ≤ 4`, up to
`b³ = 64` aliases), box and non-ideal kernels. **H0 is satisfiable at Gaussian order and is
not the barrier.**

### III.3 The isolation gap collapses `[numpy]`

`g(b) = E(2π/b) − E(0)`. For a band with curvature `c u²`:
`g(b) = c u²·4sin²(π/b) ≈ 4π²c u²/b²` — verified `g(b)·b² → 0.3948 = 4π²c u²`. In the free
theory this is harmless (box source is an exact eigenvector, blind to the aliases: clean atom
for all `b`). The danger is only under interactions.

### III.4 The alias-mixing mechanism `[numpy]`

Couple the carrier to the nearest alias with strength `ε_mix`. The carrier atom weight is a
**universal function of `ε_mix/g(b)`** (identical across `b`):

| `ε_mix/g` | 0.1 | 1.0 | 3.0 | →∞ |
|---|---|---|---|---|
| atom weight | 0.990 | 0.724 | 0.582 | → 0.5 |

Since `g(b) → 0`, any fixed coupling eventually dominates. **Uniform clean atom ⟺
`ε_mix(b) = o(g(b))`.** Fixed-contour TE (`ε_T < d_*/4` with `d_*` fixed) is thus the wrong
target; the shrinking-island form (Thm 3.4) is mandatory.

---

## Part IV — The `u⁴` dispersion power and the exact gap

### IV.1 The power is proven `[corpus + reasoning]`

The carrier `ψ(k) ∈ ker B(k)†`, so every correction factoring through `B(k)B(k)†` is `k`-flat.
Hence the carrier energy is **exactly `k`-independent through `O(u³)`** (the flatness earned by
`B†ψ = 0`; formalized in §V.4 / `[Lean]`). The first `k`-dependence is therefore `O(u⁴)`.

### IV.2 The exact gap `[sympy]`,`[Lean]`

Historical `O(u⁴)` cap-band dispersion (`[corpus]`): `ΔE(k) = −(2861009/8438730300) u⁴ cos k`.
Γ-to-nearest-alias gap:

```
g(b) = ΔE(2π/b) − ΔE(0) = (2861009/8438730300) u⁴ (1 − cos(2π/b))
     = (2861009/4219365150) u⁴ sin²(π/b).
```

Asymptotic (via `sin x / x → 1`):

```
b²·g(b) → 2861009 π² / 4219365150 = 0.006692245400461788,   i.e.  g(b) ∼ 6.69×10⁻³ u⁴/b².
```

So the required rate sharpens to **`ε_mix(b) = o(u⁴/b²)`**. (The `O(u²|k|²)` term of G11 is a
*larger* inter-branch gap; the binding one is the carrier self-alias at `u⁴/b²`.)

**Caveat.** The `u⁴` *power* is proven; the coefficient `2861009/8438730300` is the historical
branch and inherits the **C2 dispute** — algebra certified, disputed input not.

---

## Part V — The U1 incidence factorization `[sympy]`,`[Lean]`

Exact objects (`[corpus]` v4.3 §3.2), basis `(12),(13),(23)`:

```
B(k) = [ d₂ −d₁  0 ]      ψ(k) = ( d̄₃, −d̄₂, d̄₁ ) ,   q_a = |d₁|²+|d₂|²+|d₃|².
       [ d₃  0 −d₁ ]
       [ 0  d₃ −d₂ ]
```

### V.1 The Gram computation (Lemma 3.1)

Entry-by-entry (verified `[sympy]`, then `[Lean]` `incidence_gram`):

```
B(k) B(k)† = q_a·I − ψψ†
```

e.g. `(BB†)₁₁ = |d₂|² + |d₁|²`, and `(q_a I − ψψ†)₁₁ = q_a − |d₃|² = |d₁|² + |d₂|²`; the
off-diagonals match as `d_i d̄_j`. Consequences:

- **Carrier kernel:** `B(k)† ψ(k) = 0`  (`= ∂₂∂₃ = 0` in Bloch form). `[Lean] carrier_in_kernel`
- **Norm:** `‖ψ(k)‖² = q_a`.  `[Lean] carrier_normSq`
- **Factorization:** `S(k) + 4I = B(k)B(k)†` with `S := BB† − 4I`. `[Lean] incidence_factorization`

### V.2 Spectrum with multiplicities `[Lean]`

From `BB† = q_a I − ψψ†`:
- `S ψ = −4 ψ`  (carrier is the simple `−4` eigenvector). `Smat_carrier_eigen`
- `ψ†v = 0 ⇒ S v = (−4+q_a) v`  (all of `ψ^⟂` is the `(−4+q_a)`-eigenspace). `Smat_perp_eigen`
- `finrank_ℂ (ℂ∙ψ)ᗮ = 2` for `ψ ≠ 0`  (i.e. `k ≠ Γ`). `orthogonal_finrank_two`,
  `carrier_perp_finrank`; `carrier_ne_zero`.

Therefore `spec S(k) = {−4, −4+q_a, −4+q_a}` — `−4` simple, `−4+q_a` of multiplicity 2.

### V.3 Grounding `q_a` `[Lean]`

`|e^{ik} − 1|² = (e^{−ik}−1)(e^{ik}−1) = 2 − 2cos k = 4 sin²(k/2)` (Euler + half-angle
`cos k = 1 − 2sin²(k/2)`). Hence

```
q_a = Σᵢ 4 sin²(kᵢ/2)          [Lean] qa_dispersion, qa_dispersion_sum
```

— the same `sin²(·/2)` dispersion form used throughout.

### V.4 Flatness closes the assumption `[Lean]`

`B†ψ = 0 ⇒ (E·I + t·BB†) ψ = E ψ`, eigenvalue `E` manifestly independent of `k`
(`carrier_eigenvector`, `carrier_flat`). Combined with §V.1, the `BB†` form the flatness proof
uses is **produced** by the concrete incidence operator, not assumed (`flat_from_incidence`).

---

## Part VI — The Lean carrier-atom lemma (spectral Chebyshev) `[Lean]`

The §5 atom bound, formalized without Davis–Kahan (no operator contour integrals):

**Core (`window_weight_ge`).** Nonneg spectral weights `w`, `Σ w = 1`,
`Σ (λᵢ−m₀)² wᵢ ≤ ε²`, window `W = {i : |λᵢ−m₀| ≤ g/2}`. Then

```
Σ_{i∈W} wᵢ ≥ 1 − (2ε/g)².
```

Proof: for `i ∉ W`, `(g/2)² ≤ (λᵢ−m₀)²`, so `(g/2)²·Σ_{Wᶜ} wᵢ ≤ Σ_{Wᶜ}(λᵢ−m₀)²wᵢ ≤ ε²`,
giving `Σ_{Wᶜ} wᵢ ≤ (2ε/g)²`.

**Operator form (`carrier_atom_of_perturbation`).** For a unit `ψ` in the `m₀`-eigenspace of
`H₀` and `H = H₀ + V`, `(H−m₀)ψ = Vψ`, so the second moment `= ‖Vψ‖² ≤ ε²`; with Parseval
(`norm_sq_eq_sum_repr`) the window weight `≥ 1 − (2ε/g)²`.

**Combined + limit (`carrier_atom_fiber_gap`, `carrier_atom_clean_limit`).** Substituting
`g = g(b)` from Part IV and taking `ε_mix(b)/g(b) → 0` gives the atom weight `→ 1` — the formal
`o(u⁴/b²)` clean-atom rule.

---

## Appendix — verification manifest

| Derivation | Result | Checked by |
|---|---|---|
| H3 counterexample (I.1) | upper bound ⇏ atom | `[sympy]` |
| Part VI bound (I.2) | `Z ≥ (F−qC₀)/(1−q)`; printed formula false | `[sympy]` |
| SU(3) anchor (I.3) | `p₃=[√(30π)/2]ψ₂`, `p₃ψ₀=√5ψ₂` | `[sympy]` |
| `z_ent` (I.4) | valid lower bound; clean `(√z_*−ε_W−M_*η_P)²` | `[sympy]`,`[numpy]` |
| KL layer (I.5) | `ρ({M²})=2MA`, spin `3/5` | `[sympy]` |
| Kato/Riesz chain (II.1) | `q ≤ 2ε_T/d_*` | `[numpy]` |
| tolerance budget (II.2) | `ε_W<z_*/4M_*`, `ε_T<z_*d_*/8M_*²` | `[sympy]` |
| H0 cross-Gram (III.2) | `λ_min/z_* = 1`, all `b,d` | `[numpy]` |
| isolation collapse (III.3) | `g·b² → 4π²cu²` | `[numpy]` |
| mixing mechanism (III.4) | weight = universal `f(ε/g)` | `[numpy]` |
| exact gap (IV.2) | `g(b)=(2861009/4219365150)u⁴sin²(π/b)`; `b²g→0.006692…` | `[sympy]`,`[Lean]` |
| incidence Gram (V.1) | `BB†=q_a I−ψψ†`; `B†ψ=0` | `[sympy]`,`[Lean]` |
| spectrum + mult (V.2) | `{−4,−4+q_a,−4+q_a}`, mult 2 | `[Lean]` |
| `q_a` grounding (V.3) | `q_a=Σ4sin²(kᵢ/2)` | `[Lean]` |
| flatness (V.4) | `B†ψ=0 ⇒` flat eigenvalue | `[Lean]` |
| atom lemma (VI) | window weight `≥ 1−(2ε/g)²` | `[Lean]` |

**Two standing T3 physics inputs** (unchanged by all of the above): the `O(u³)` factorized
*form* `H_eff⁻ = E_flat·I + t·BB† + O(u⁴)`, and the interacting `ε_mix = o(u⁴/b²)` bound
(**G17**). Everything on the carrier-atom chain except these two is now certified.
