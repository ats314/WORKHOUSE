# The strongest current theory of the WORKHOUSE carrier

**Session:** theory mode, repository read-only. No repository file was created, edited,
staged, or committed; `git status --short` is empty. This document is an external artifact.
**Repo state:** `bcddd4a` — 140/140 checks, 28 Lean theorems, 0 `sorry`, 1 open
contradiction (C2), 21 open gaps.
**Inputs audited:** the five Lean files (`CarrierAtom`, `Flatness`, `FiberGap`, `Incidence`,
`Spectrum`, `CarrierAtomGap{,_2}`); `FIXED_TO_CONTINUUM_MASTER_CHAIN_20260822.md` (**A**);
`carrier_atom_lean_audit.md` (**B**); `KEY_DERIVATIONS_20260823.md` (**C**);
`gemini_chat.txt` (**D**); `LEAN_EXPERIMENT_FINDINGS_20260823.md` (**E**).

**Tier discipline.** Every claim below is tagged. `[T0]` Lean-proved in the repo.
`[T1*]` exact symbolic re-derivation run in this session — *not a registered invariant*,
so it carries no repo tier. `[T3]` asserted. Nothing here is promoted by being written down.

---

## 0. The one-paragraph version

The corpus already contains, in separate places, every ingredient of a much stronger
statement than any of the five documents makes. The carrier is not a Bloch band with an
awkward singularity at Γ — it is a **flat band whose singular point carries the second
homology of the torus**, and that reading closes three things at once: it identifies the
rank-3 rest fiber the continuum chain needs and could not get, it discharges a hypothesis
the corpus explicitly assumes, and it makes the isolation gap of that fiber an **exact
rational that is provably independent of the one open contradiction**. Separately, and
more consequentially for the near-term research program: **C_shp is exactly the Γ-point
curvature anisotropy of the fourth-order band**, which means C2 is adjudicable from
near-Γ data — contradicting a belief the repository states in five places and uses to
narrow G3's scope.

---

## 1. The five results

| # | Result | Status | Bears on |
|---|---|---|---|
| **R1** | The "+2" in `dim Z₂ = L³+2` *is* the corank jump of the Bloch incidence at its unique zero: `rank B(k) = 2` off Γ, `0` at Γ, so `Σ_k dim ker B(k)† = (L³−1)·1 + 3`. | `[T1*]` **re-reading**, not a new result — the count is corpus prior art | G14, U1 |
| **R2** | The rank-3 rest fiber is `H₂(T³) = ker B(Γ)† ≅ ℂ³`, an **irreducible T₁g** of O_h (χ = (3,0,−1,1,−1), Σ|χ|²·size = 24). Schur ⟹ any O_h-covariant operator is scalar on it. | `[T1*]` — **discharges** MASTER_THEORY §5.2's assumed `H₄(Γ) = s₄I₃` | A/Step C, §5.2 |
| **R3** | `min_{k≠Γ} λ₄(k) = α·sin²(π/L) = (5/12)·sin²(π/L)`, attained on exactly the 6 axial momenta, **independent of β** — hence exactly C2-free. | `[T1*]` verified L=3…8, both branches | C2, G3, A/Steps C–E |
| **R4** | `λ₄/q_a = A + C_shp·Ψ`, `Ψ := 4e₂/q_a²` degree-0 homogeneous with range `[0, 4/3]`. Hence `C_shp` **is** the Γ-curvature anisotropy, and the near-Γ observable `Δ(L) = (4/3)C_shp + 4(B+D/9)sin²(π/L)` adjudicates C2. | `[T1*]` exact | **C2, G3, G14, G11** |
| **R4b** | The three lowest alias levels are `(5/12)s`, `(5+48C_shp)s/6`, `(5+64C_shp)s/4` with `s = sin²(π/L)`. Their **ratios are independent of L and of u**: `ρ₂ = 2 + (96/5)C_shp`, `ρ₃ = 3 + (192/5)C_shp`, and `ρ₃ = 2ρ₂ − 1` identically — a built-in blind holdout. | `[T1*]` exact, verified L=4,5,6,8 | **the sharpest C2 adjudicator available** |
| **R5** | `ε_mix` is not a dynamical quantity. Fine-lattice translation covariance makes the exact blocked Hamiltonian block-diagonal across aliases; the continuum requirement is a **Euclidean-time window** `τ ≳ 1/g(b) ~ 12b²/(5π²u⁴)`, not an unproven coupling bound. | `[T3]` structural argument, stated with its decisive assumption | A/Step C–E, D's "entirely a G17 statement" |

---

## 2. Setting the coordinates straight

Everything below lives in one equation. The corpus writes the fourth-order carrier band
two ways — as a generalized Hodge pencil (§5.2) and as a four-shape expansion (§5.1) —
and never puts them in the same line. Doing so is the whole trick.

With `Xᵢ = 1 − cos kᵢ = aᵢ/2`, `aᵢ = 4sin²(kᵢ/2)`, and

```
𝖰 = Σ Xᵢ²      𝖱 = Σ_{i<j} XᵢXⱼ      𝖲 = Σ Xᵢ
q_a = Σ aᵢ     e₂ = Σ_{i<j} aᵢaⱼ     e₃ = a₁a₂a₃
```

the pencil is `λ₄ = (α𝖰 + β𝖱)/(2𝖲)` (§5.2) and the shape form is
`ε₄ = c₀ + A·q_a + B·e₂ + C·(4e₂/q_a) + D·(e₃/q_a)` (§5.1).

Using `𝖰 = 𝖲² − 2𝖱` and the repo's own `C_shp = (β − 2α)/16` `[T0: C_from_beta]`:

```
λ₄ = α𝖲/2 + (β − 2α)·𝖱/(2𝖲)  =  (α/4)·q_a  +  C_shp·(4e₂/q_a)        [T1*]
```

So **`A = α/4`** — which is the repo's `[T0] alphaPen_three_eq_four_A` (`α₃ = 4A_shp`,
`A_shp = 5/48`) — and **`B = D = 0`** is exactly the tier collapse (G14). Everything
C2-dependent in the entire fourth-order band is the single term `C_shp·Φ_C`, with
`Φ_C = 4e₂/q_a` the repo's own crosswalk kernel.

Cross-check against the repo's recorded crosswalk values, reproduced exactly:
`Φ_C(X) = 0`, `Φ_C(M) = 8`, `Φ_C(P) = 16/3`, `Φ_C(R) = 16` — matching
`invariants.py:455` `want = {"X": 0, "M": 8, "P": Rational(16,3), "R": 16}`. `[T1*]`

**The two C2 branches differ only in β**, verified by inverting the v10a.26 branch from
its *recorded bandwidth alone* and recovering its *recorded* `C_shp`:

```
α       = 5/12 = 0.4166666666666667                      (both branches)
β_old   = 17607806155349/275331901291200 = 0.06395120243159332
β_new   = W₄_new − α                     = 0.5099200711546681
(β_new − 2α)/16  = −0.02021332888616658
recorded v10a.26  = −0.020213328886166577      difference −3.47e−18      [T1*]
```

---

## 3. R1 — the rank jump *is* the harmonic triplet

The corpus proves `dim Z₂ = L³ + 2` homologically (§3.3: `#C₃ = L³`, `b₂ = 3`, `b₃ = 1`,
`rank ∂₃ = L³ − 1`, "three wrapping sheets complete the carrier"), and separately gives the
Bloch incidence `B(k) = ∂₂(k)†` with `spec S(k) = {−4, −4+q_a, −4+q_a}` (§3.2). These are
two descriptions of one object, and the bridge is a rank count:

```
det B(k) ≡ 0  for all k                                   [T1*]
rank B(k) = 2  for every k ≠ Γ  (verified exactly at (1,0,0),(0,1,0),(1,1,0),
                                 (1,1,1),(3,0,0),(3,3,3),(2,4,5) mod 2π/6)
rank B(Γ) = 0  (all dᵢ = 0)
⟹ dim ker B(k)† = 1 off Γ,  = 3 at Γ
⟹ Σ_k dim ker B(k)† = (L³ − 1)·1 + 3 = L³ + 2 = dim Z₂    [T1*]
```

Verified at L = 3,4,5,6 → 29, 66, 127, 218, matching the repo's passing check
`dim Z_2 at L = 3, 4, 5` → `{3: 29, 4: 66, 5: 127}`.

**Reading, and its honest size.** The count itself is *not* new — it is in the corpus's
opening paragraph verbatim (`dim Z₂ = L³+2 = (L³−1)+3`, "the second is the harmonic plane
triplet") and it is a passing repo check. What R1 adds is only the **mechanism**: the split
is a corank jump of a single operator at the single point of the zone where that operator
vanishes. That is a re-reading, not a new result, and I am recording it only because it is
what makes R2 and §5's fiber count computable rather than asserted.

I verified the underlying Gram identity independently and exactly, matching
`Incidence.lean`'s `incidence_gram` and the repo's `tier_collapse.incidence_identity`:

```
B(k)B(k)† − (q_a·I − ψψ†) = 0     (3×3 zero matrix, symbolic in k₁,k₂,k₃)   [T1*]
B(k)†ψ(k) = 0 ,  ‖ψ(k)‖² = q_a
```

**Prior art, honestly.** The identity itself is *already a passing T1 check* —
`B B^dagger = q I - d conj(d)^T for the curl incidence` (UNIFIED §2.4), whose detail line
even records "the identity gives eigenvalues (0, q, q)". Document C Part V.1 and
`Incidence.lean` are therefore a **T1→T0 promotion of existing repo mathematics**, not new
mathematics — which is exactly what document E's own V5 pass concluded ("no genuinely new
mathematics"). The new content in R1 is the rank-count bridge to `dim Z₂`, nothing else.

---

## 4. R2 — the rank-3 rest fiber is topological, and Schur applies

Document A's Step C needs, and cannot get, this: *"the completed `p=0` fiber is exactly one
irreducible cubic `T1` copy of rank three and the transfer commutes with the cubic action.
Schur's lemma then makes the transfer scalar on that fiber."*

**The object exists and is already in the corpus.** It is `H₂(T_L³) = ker B(Γ)† ≅ ℂ³` — the
three wrapping sheets. Three facts, none of them an estimate:

1. **Rank 3 is topological.** `dim H₂ = b₂(T³) = 3` for every `L` and every block factor
   `b`, exactly. Not a bound, not a limit, not a fit.
2. **It is irreducible T₁g.** A 2-form in 3d is Hodge-dual to an axial vector, so the three
   coordinate 2-planes carry the axial-vector rep of O_h. Character on the rotation classes
   `χ(R) = 1 + 2cos θ`:

   | class | E | 8C₃ | 6C₂′ | 6C₄ | 3C₂ |
   |---|---|---|---|---|---|
   | χ | 3 | 0 | −1 | 1 | −1 |

   `Σ |class|·χ² = 9 + 0 + 6 + 6 + 3 = 24 = |O|` ⟹ **irreducible**. `[T1*]`
   Axial ⟹ parity-even ⟹ **T₁g**; with the C=− projection, **J^{PC} = 1^{+−}**.
3. **Therefore Schur applies**, and any O_h-covariant operator — the transfer included — is
   a scalar on this triplet.

**This discharges a stated corpus assumption.** MASTER_THEORY §5.2 says *"Assume the cubic
Γ-block is scalar, `H₄(Γ) = s₄I₃`, `s₄ = (1/3)tr H₄(Γ)`."* If the Γ block carries an
irreducible 3-dimensional cubic rep, Schur **forces** it to be scalar. The assumption is a
theorem, and the whole `𝒬₄φ = λ₄Gφ` construction rests on it.

**And it matches the corpus's own dictionary.** §3.3 line 445: *"The rest-frame axial `T₁`,
parity-even, charge-odd dictionary is an analytic assignment in the one-plaquette operator
space."* §3.1: *"For SU(2), complex conjugation is a gauge transformation, so the charge-odd
projector vanishes. The `T₁^{+−}` construction begins at N = 3."* §3.4 lists the four
possible fates and reaches the same place: *"harmonic annihilation — the band disperses but
`ℋ₂` stays pinned"*, *"cubic-symmetry breaking — only then can the `T₁` triplet split."*

**Prior art, honestly.** The T₁^{+−} assignment is corpus prior art (§3.3, §3.4) and the
repo flags it as *"not a measured physical overlap theorem"* — i.e. G18. What is not in the
corpus is the **derivation of the irreducibility from the Hodge duality**, and hence the
observation that §5.2's scalar-Γ-block assumption is not independent. That is R2's content.

**The obvious way to kill R2 is closed.** The natural objection is that the C=− projection
might annihilate the harmonic sector. It does not — the corpus's *opening paragraph* settles
it: *"The strongest coherent result in the archive is a finite-lattice, strong-coupling
theorem about the **charge-odd** one-plaquette flux sector... the cubic incidence complex
produces a singular homological carrier `Z₂ = ker ∂₂`... On the three-torus,
`dim Z₂ = L³+2 = (L³−1)+3`, where the first term is the space of cube boundaries and **the
second is the harmonic plane triplet**."* The triplet is inside the charge-odd carrier by
construction, not something the projection could remove.

**Where R2 can still die.** §3.4 is explicit and I will not paper over it: the pinning is
*"an all-orders theorem only within the boundary-factorized corner generated by the incidence
maps. The set `{BMB†}` is not a two-sided ideal of all endomorphisms of `C₂`, and topology
does not prove that every physical correction belongs to it."* R2 gives the **rank and the
irreducibility** unconditionally; it does **not** give the pinning unconditionally. A
correction outside the boundary-factorized corner — §3.4's outcome 4, cubic-symmetry
breaking — is the remaining route, and blocking by a cubic block does not supply one.

---

## 5. R3 — the isolation gap of that fiber is exactly C2-free

> **Theorem.** Let `λ₄(k) = (α𝖰 + β𝖱)/(2𝖲)` with `α > 0`, `β ≥ 0`. On `T_L³` (equivalently,
> on the alias set of a block of side `b`),
> ```
>     min_{k ≠ Γ} λ₄(k) = α·sin²(π/L)
> ```
> attained on exactly the six axial momenta `(±2π/L, 0, 0)` and permutations, and
> **independent of β**.
>
> **Corollary (SU(3)).** The isolation gap of the harmonic triplet from every other state in
> its own folded fiber is
> ```
>     g(L) = (5/12)·u⁴·sin²(π/L)  ~  (5π²/12)·u⁴/L²  ≈  4.112·u⁴/L²
> ```
> the *same exact rational* in the historical and v10a.26 kernels.

**Proof.** Write `Xᵢ = 2sin²(πnᵢ/L)`, `X₁ := 2sin²(π/L) = min{2sin²(πm/L) : 1 ≤ m ≤ L−1}`.
*(a)* On an axis `𝖱 = 0` identically, so `λ₄ = αX₁²/(2X₁) = α sin²(π/L)`.
*(b)* For any `n ≠ 0`, every nonzero `Xᵢ ≥ X₁`, so `Σ Xᵢ(Xᵢ − X₁) ≥ 0` termwise, i.e.
`𝖰 ≥ X₁𝖲`; with `β, 𝖱 ≥ 0`, `λ₄ ≥ α𝖰/(2𝖲) ≥ αX₁/2`.
*(c)* Equality forces `β𝖱 = 0` and `𝖰 = X₁𝖲`: for `β > 0`, at most one `Xⱼ ≠ 0` and then
`Xⱼ = X₁`, so `nⱼ ∈ {1, L−1}` — exactly six points.
*(d)* `λ₄ → 0` at Γ from every direction, consistent with §5.3's "minimum unique at Γ". ∎

Only *(a)* and *(d)* use `α`; *(b)* and *(c)* use only `β ≥ 0`. **Both the value and the
identification of which alias is nearest survive C2**, the latter because both branches have
`β > 0` (0.0640 and 0.5099).

**Verification.** Exhaustive symbolic minimum over the *entire* momentum set, exact
`Rational`, both branches:

```
L=3:   26 momenta  min = 0.3125          = α sin²(π/3)   exact ✓   6 argmins, all axial
L=4:   63          min = 0.2083333333    = α sin²(π/4)   exact ✓   6 argmins
L=5:  124          min = 0.1439547928    = α sin²(π/5)   exact ✓   6 argmins
L=6:  215          min = 0.1041666667    = α sin²(π/6)   exact ✓   6 argmins
L=7:  342          min = 0.07843962461   = α sin²(π/7)   exact ✓   6 argmins
L=8:  511          min = 0.06101942059   = α sin²(π/8)   exact ✓   6 argmins
```

**Consistency:** at `L = 2`, `g = α = 4A_shp = Δ_X`, which is the repo's own extraction
formula `A = Δ_X/4` and its check `X is blind to B, C, D — it fixes A alone`. R3 is the
one-parameter family through that point.

**The folded fiber, exactly.** Blocking by `b` gives a coarse `p=0` fiber of dimension
`3 + (b³ − 1) = b³ + 2`: the harmonic triplet at Γ, plus `b³−1` aliased Bloch carriers.
Levels (in units of `u⁴`, relative to the triplet):

| b | aliases | fiber dim | first excited level |
|---|---|---|---|
| 2 | 8 | 10 | `5/12` = 0.416667 |
| 3 | 27 | 29 | `5/16` = 0.312500 |
| 4 | 64 | 66 | `5/24` = 0.208333 |
| 6 | 216 | 218 | `5/48` = 0.104167 |
| 8 | 512 | 514 | `5/24 − 5√2/48` = 0.061019 |

**This corrects Step C.** *"Exactly one irreducible rank-three T1 copy"* is **true of the
harmonic triplet** and **false of the folded fiber** for every `b > 1` — the fiber has
dimension `b³ + 2`. But the correct replacement is *better* than the hedge document A offers
("prove a uniformly weighted sub-island whose diameter tends to zero"): the extra states are
a different kind of state, and they are separated from the triplet by an **exact rational
gap that does not wait on G3**. Schur does the work on the triplet; R3 does the work on the
separation.

**Prior art:** `workhouse search` returns **no claim** for "alias", "fiber", or "isolation
gap"; `invariants.py` contains no "isolation", "island", "nearest", or "minimum over".
The `4sin²(π/L)` in §3.3 is the *second-order* incidence level, a different quantity.

---

## 6. R4 — `C_shp` *is* the Γ-curvature anisotropy, so C2 is adjudicable near Γ

This is the result with the most immediate consequence for the research program.

### 6.1 The normalized band

From §2, dividing by `q_a`:

```
λ₄(k)/q_a(k) = A + C_shp·Ψ(k),      Ψ := 4e₂/q_a²          [T1*]  (exact, all k ≠ Γ)
```

`Ψ` is **degree-0 homogeneous** in the `aᵢ` — it depends only on the ratios `a₁:a₂:a₃`, not
on `|k|`. Its range on the simplex is exactly

```
Ψ = 0     ⟺ at most one aᵢ ≠ 0   (the three coordinate axes)
Ψ = 1     on a face diagonal a = (1,1,0)
Ψ = 8/9   at P = (π, π/2, 0)
Ψ = 4/3   ⟺ a₁ = a₂ = a₃          (maximum)
```

So `λ₄/q_a` is an **affine function of `C_shp` with slope `Ψ ∈ [0, 4/3]`**, and the entire
C2-dependence of the normalized band spans exactly `(4/3)·C_shp`.

### 6.2 Why this contradicts a stated belief

The repository states, in five places, that Γ-point data cannot constrain `Δ_C`:

| location | text |
|---|---|
| `FRONTIER.md:137`, `gaps.yaml:49` (G3) | "`Φ_C(0) = 0` makes **Gamma-point data structurally incapable** of constraining Delta_C" |
| `symbols.yaml:91` (`delta_c`) | "**Gamma-point data cannot constrain it**" |
| `symbols.yaml:104` (`phi_c`) | "`Φ_C(0)=0`, which is why the Gamma-point **scalar** places no constraint" |
| `constants.py:693` | "...why a Gamma-point **scalar** can pin the anchoring offset while leaving the off-axis kernel wholly unconstrained" |
| `contradictions.yaml:81` | "`Φ_C = O(\|k\|²)` and `Φ_C(0) = 0`. So Hamer's Gamma-point **scalar** pins Delta_Gamma and places NO constraint on..." |

The three that say **"scalar"** are correct and I am not disputing them. The two that say
**"data"** — including G3's own scope note — overstate. `Φ_C = O(|k|²)` kills the *value*;
it does not kill the *second-order jet*. `Φ_C/q_a = Ψ` is degree-0 and takes its full range
`[0, 4/3]` in **every** neighbourhood of Γ, however small.

Equivalently: the fourth-order band's touching at Γ is **isotropic iff `C_shp = 0`**. The
Γ-limit curvature along a unit direction `n̂` is exactly

```
K(n̂) = lim_{ρ→0} λ₄(ρn̂)/ρ² = A + 4·C_shp·P(n̂),     P(n̂) = Σ_{i<j} n̂ᵢ²n̂ⱼ² ∈ [0, 1/3]
```

so `C_shp` is precisely the coefficient of the cubic harmonic `P` in the Γ curvature.
Both branches have `C_shp ≠ 0`, so in both kernels the band is anisotropic at Γ.

### 6.3 The adjudication observable

Take the two smallest nonzero momenta on `T_L³` — one axial, one body-diagonal:

```
Δ(L) := (ε₄/q_a)|_{(2π/L)(1,1,1)} − (ε₄/q_a)|_{(2π/L)(1,0,0)}
      = (4/3)·C_shp + 4·(B_shp + D_shp/9)·sin²(π/L)              [T1*]  exact
```

Three things follow, all exact:

1. **In the tier-collapsed regime** (`B = D = 0`, which is what both recorded kernels
   have — `constants.py:158-159` `B_SHP_3 = Rational(0)`, `D_SHP_3 = Rational(0)`),
   `Δ(L) = (4/3)C_shp` **exactly at every L ≥ 3**.
2. **Without the tier collapse**, `Δ(L) → (4/3)C_shp` as `L → ∞`, so the adjudication is
   asymptotically independent of **G14** as well as of the collapse assumption. Better: the
   `sin²(π/L)` dependence means **two lattice sizes separate `C_shp` from `B + D/9`
   exactly** — the same measurement that adjudicates C2 also measures the tier-collapse
   combination that G14 is about.
3. **It is far cleaner than the zone-boundary extraction.** The same observable built from
   the frozen protocol's own points gives
   `(ε₄/q_a)|_R − (ε₄/q_a)|_X = (4/3)C_shp + 4(B + D/9)` — the `B,D` term at *full*
   strength, since `sin²(π/2) = 1`. Suppression factor of the near-Γ version:

   | L | 4 | 6 | 8 | 12 | 16 | 24 | 32 |
   |---|---|---|---|---|---|---|---|
   | `1/sin²(π/L)` | 2.0× | 4.0× | 6.8× | 14.9× | 26.3× | 58.7× | 104× |

**Decisiveness.**

```
historical  C_shp = −0.0480863832   →  (4/3)C_shp = −0.0641151776
v10a.26     C_shp = −0.0202133289   →  (4/3)C_shp = −0.0269511052
separation of the two predictions              =  0.0371640724   (ratio 2.379)
worst-case B,D contamination at L=4, using the recorded residuals
  B_shp = 3.55e−16, D_shp = 2.23e−13          =  5.03e−14
signal / contamination                         =  7.4e+11
```

**No competing O(u²) contamination.** This is the point where G11 would normally bite: near
Γ the `O(u²)` splitting `t(u)q_a(k)` is comparable to the `O(u⁴)` scale. But that splitting
separates the carrier from its **two partner branches**; the carrier's *own* energy is
`E_flat(u)` exactly through `O(u³)` (§4.3), so it does not enter `ε₄` at all. The
adjudication reads the carrier branch and is untouched by the orbital splitting.

**Prior art.** The repo has `Φ_C = 4e₂/q_a` (`constants.py:689`) and its high-symmetry
values, and the checks *"Phi_C vanishes on every axial cut"* and *"off-axis band splits are
8·Δ_C and 16·Δ_C"* at M and R. It does **not** have the scale-invariant normalization
`Ψ = 4e₂/q_a²`, its `[0, 4/3]` range, the Γ-curvature reading, or any near-Γ observable.
`workhouse search` returns **no match** for `−0.0641151776`, `−0.0269511052`, or
`0.0371640724`.

**Caveat on process.** G3's protocol is *frozen*, and target-blindness is the reason. R4 is
an **additional** extraction to run inside the same sealed run, not a replacement for the
frozen 11 items. Changing a frozen protocol is a reviewed event; adding a blind observable
computed from the same kernel is not.

---

## 6bis. R4b — a scale-free C2 adjudicator with its own blind holdout

R4 needs `q_a` normalization. This does not. It is the sharpest form I found.

### 6bis.1 The three lowest levels

Write `s = sin²(π/L)`. The three lowest alias levels above the harmonic triplet — the
axial, face-diagonal and body-diagonal momenta at the smallest nonzero `|n|` — are exactly

```
level-1  (2π/L)(1,0,0)  :  λ₄ = (5/12)·s                     C2-FREE          [T1*]
level-2  (2π/L)(1,1,0)  :  λ₄ = (5 + 48·C_shp)·s/6
level-3  (2π/L)(1,1,1)  :  λ₄ = (5 + 64·C_shp)·s/4
```

**`s` cancels in every ratio.** Therefore

```
ρ₂ := level-2/level-1 = 2 + (96/5)·C_shp        ⟺   C_shp = (5/96)·(ρ₂ − 2)
ρ₃ := level-3/level-1 = 3 + (192/5)·C_shp       ⟺   C_shp = (5/192)·(ρ₃ − 3)
```

both **independent of `L`, of `u`, of `E_flat`, and of any overall normalization**. Verified
exactly against the direct exhaustive minimum at L = 4, 5, 6, 8, both branches.

### 6bis.2 The predictions are far apart

| | `ρ₂` | `ρ₃` |
|---|---|---|
| historical (`C_shp = −0.0480863832`) | **1.0767414429** | **1.1534828858** |
| v10a.26 (`C_shp = −0.0202133289`) | **1.6119040854** | **2.2238081708** |
| separation | 0.535 | 1.070 |

A 50% and a 93% difference in a pure dimensionless ratio of two level spacings.

### 6bis.2b The level ordering is robust — its falsifier is closed

R4b assumes level-2 is the face diagonal `(2π/L)(1,1,0)` rather than the second axial
`(2π/L)(2,0,0)`. That is an inequality, and it holds with a wide margin:

```
face  =  (α + β/2)·s        second axial  =  4α·s·(1 − s)
face is lower  ⟺  β < 2α(3 − 4s)                              [T1*]
```

| L | 4 | 5 | 6 | 8 | 12 | 16 | 32 | →∞ |
|---|---|---|---|---|---|---|---|---|
| bound on β | 0.833 | 1.348 | 1.667 | 2.012 | 2.277 | 2.373 | 2.468 | `6α = 5/2` |

`β_old = 0.0640` and `β_new = 0.5099` are far inside at every L. In `C_shp` terms the
ordering fails only for `C_shp > α(2 − 4s)/8`, which at L=16 is `+0.0962`; **both branches
are negative**. Exhaustively confirmed at L = 3,4,5,6,7 in both kernels (L=3 is degenerate:
`n=2 ≡ −1 mod 3`, so the second axial coincides with the first and no new level appears).

### 6bis.3 It carries its own blind holdout

```
ρ₃ − (2ρ₂ − 1) = 0        identically in C_shp                [T1*]
```

This is the *same affine structure* as the repo's `[T0] blind_holdout`
(`lam α β 1 = 2·lam α β (1/2) − lam α β 0`) and as G3's frozen protocol item
*"direct X/M extraction with `λ_R = 2λ_M − λ_X` as blind holdout"*. So the near-Γ triple
is a **drop-in analogue of the zone-boundary triple X/M/R**: same three-point affine
extraction, same holdout identity, but evaluated at the smallest nonzero momenta instead of
the zone corners — where the `B_shp, D_shp` contamination is suppressed by `sin²(π/L)`
(26× at L=16, 104× at L=32; see §6.3).

### 6bis.4 What is C2-free and what is not — the exact boundary

| feature of the fourth-order band | C2-free? |
|---|---|
| **floor** of the alias island — `min_{k≠Γ} λ₄ = α sin²(π/L)` | **yes, exactly** (R3) |
| **ceiling** — `max λ₄ = λ₄(R) = α + β = W₄` | no — this *is* `W₄`, 0.4806 vs 0.9266 |
| **second** alias level | no — `(5+48C_shp)s/6`, 0.0657 vs 0.0984 at L=8 |
| **island width / level spacings** above the floor | no |
| value at any point on a coordinate axis | **yes** (`Φ_C = 0` there — repo prior art) |
| Γ-limit curvature along an axis | **yes** — `K = A` |
| Γ-limit curvature anisotropy | no — `4C_shp·P(n̂)` (R4) |

**The floor of the band is sealed; everything above it is disputed.** That is the exact
scope of what can be asserted before G3 runs — and it is what makes R3 usable now and the
island *diameter* of document A's Step E not usable now.

---

## 7. R5 — `ε_mix` is not a dynamical quantity

Documents A, C and D converge on one bottleneck. Document D states it most baldly:
*"The algebra is solved; what remains is entirely a G17 statement bounding the actual
interacting SU(3) cross-talk."* Document C III.4: *"Uniform clean atom ⟺
`ε_mix(b) = o(g(b))`."*

**The structural objection.** The exact fine lattice theory on `T_L³` (`L = b·N_c`) is
exactly invariant under the full fine translation group `ℤ_L³`. Fine momentum is therefore
an exact good quantum number and the exact fine Hamiltonian — interacting, all orders — is
**block-diagonal across distinct fine momenta**. The aliases `k_s` *are* distinct fine
momenta. Blocking restricts which **observables** are used; it does not break the
**dynamics'** symmetry. Document A's own Step B insists on the *exact* pushforward with no
projection back to a one-coupling Wilson ansatz, which closes the only loophole.

So `ε_mix` as defined — block-induced mixing between the carrier at Γ and the carrier at an
alias — **is zero**, and the nonzero quantity is the **alias content of the blocked source**.
That is a materially different object: a source with alias weights `c_s` produces

```
⟨J(τ)J(0)⟩ = Σ_s |c_s|² e^{−τ(E_flat + λ₄(k_s)u⁴)}
```

a **multi-exponential correlator with resolved components**, not a broadened or shifted
atom. Document C's own III.1 computes `G(k_s) = ∏ᵢ δ_{sᵢ,0}` — the box form factor kills
the aliases exactly — and III.2's `λ_min/z_* = 1.000000 for all b` is the same fact seen
numerically.

**The corrected requirement.** Since every alias sits *above* the triplet by at least
`g(b) = (5/12)u⁴sin²(π/b)` (R3), the atom is recovered by waiting:

```
τ ≳ 1/g(b) = 12b²/(5π²u⁴)          [T3, structural]
```

| u | b=2 | b=4 | b=8 | b=16 |
|---|---|---|---|---|
| 0.10 | 2.4e4 | 4.8e4 | 1.6e5 | 6.3e5 |
| 0.20 | 1.5e3 | 3.0e3 | 1.0e4 | 3.9e4 |

**Same `b²` scaling — but a statement about the measurement window rather than an unproven
bound on an interaction.** That is a different kind of obligation: a resource requirement,
checkable in advance, instead of an open estimate. And the table is itself a finding — at
`u = 0.1` the required separations are `10⁴`–`10⁶` lattice units, which no document states
and which bounds what any Monte Carlo can see.

**Status and the assumption that decides it.** `[T3]` — a structural argument, not a
theorem. It turns entirely on whether the exact blocked object is the *pushforward of the
fine system* (translation-covariant, `ε_mix = 0`) or an *approximate coarse Hamiltonian*
(not covariant, `ε_mix ≠ 0`). Document A demands the former; document C's III.4 model
assumes the latter. Both cannot be right, and **naming which one is meant is prerequisite
to any TE/SE estimate.** This is the single highest-value question I can point at.

---

## 8. Corrections to the input documents

### 8.1 The pentagonal transplant, now in its third document

Document C Part IV.2 repeats `FiberGap.lean`'s coefficient: `ΔE(k) = −(2861009/8438730300)
u⁴ cos k`, `g(b) = (2861009/4219365150)u⁴sin²(π/b)`, `b²g → 6.69e−3`. These constants are
`DELTA_E_CAP_4` and `PENT_BANDWIDTH_4` (`constants.py:479, 481`) — the **isotropic
pentagonal-prism cap band**, which MASTER_THEORY §9.3 calls *"a separate geometry and
retained sector"* that *"remains outside the cubic SU(3) kernel"*, and which the repo's own
passing T1 check `h_4^side and the cubic kernel share no denominator structure` separates
explicitly. Correct cubic value: `α = 5/12`. **Ratio 614.49**; corrected asymptotic
`4.112·u⁴/b²`, not `6.69e−3·u⁴/b²`.

Documents B and E already flag this; document C does not, and its Part IV.2 "Caveat"
(*"the coefficient ... inherits the C2 dispute"*) is wrong twice — the pentagonal
coefficient is neither side of C2 (`−0.04808638` / `−0.02021333`) and is not disputed at
all (§9.3: two independent exact backends, cold-regenerated end to end, 21/21 + 24/24 +
17/17×2 + 26/26 + 17/17 + 27/27 + 7/7 + 29/29, a deliberate one-row mutation rejected).

**Repetition is not independence.** Three documents now carry this, from **one** origin.

### 8.2 The `O(u²)` / `O(u⁴)` mismatch inside document C

Part III.3 gives an `O(u²)` gap (`g(b) = c u²·4sin²(π/b)`, `g·b² → 0.3948`); Part IV.2 gives
an `O(u⁴)` gap. These are **two different physical separations**, both real, both in the
corpus, and the document does not distinguish them:

| | separates | order | at the nearest axial alias |
|---|---|---|---|
| **orbital** | carrier from its two partner branches at the *same* k | O(u²) | `t(u)·q_a = 4t(u)sin²(π/b)` |
| **alias** | the triplet from carriers at *folded* momenta | O(u⁴) | `α u⁴ sin²(π/b)` |

with `t(u) = (5/612)u² + (1975/124848)u³`. The ratio is exact:

```
orbital / alias  =  4t(u)/(αu⁴)  =  (395u + 204)/(2601u²)                    [T1*]
crossing at       u* = (395 + √2278441)/5202 = 0.3660996851770081  (exact)
```

| u | 0.05 | 0.10 | 0.20 | 1/3 | 0.50 |
|---|---|---|---|---|---|
| orbital/alias | 34.41 | 9.36 | 2.72 | 1.16 | 0.62 |

**Correction to my own earlier audit.** Document B §8 said "the orbital gap dominates at
small u", which is true but ambiguous about which gap *binds*. Being precise: for
`u < u* ≈ 0.366` the orbital gap is the **larger** one, so the **alias gap is the smaller
and therefore the binding** separation. **Document C's parenthetical — *"the binding one is
the carrier self-alias at `u⁴/b²`"* — is correct throughout the strong-coupling regime**,
and my earlier framing understated it. `ledger/gaps.yaml:250` still uses the name "the
isolation gap" for the *orbital* one, so the two must be named apart; but the choice
document C made is the right one, for a reason it did not state and I can now supply.

### 8.3 The Gemini Lean code (document D)

Three specific defects in `carrier_mass_tends_to_one`, independent of whether it compiles:

1. **`window_mass` is inconsistent between drafts** — first `window_mass E dim basis ψ b (W b)`,
   later `window_mass b (W b)`. With section `variable`s these do not elaborate to the same
   term unless inclusion is forced.
2. **`IsLittleO.tendsto_div_nhds_zero` needs `g` eventually non-zero.** `valid_gap g` is
   assumed in the theorem but is **not threaded into `error_term_tends_to_zero`**, which
   takes only `h_atom`. The dependency is dangling.
3. **The theorem is close to vacuous as stated.** Nothing relates the spaces `E b` to each
   other, nothing constrains `m0 b`, and the window `W b` has half-width `g b / 2 → 0`.
   "The mass in `W b` tends to 1" with a shrinking window and an unrelated family of spaces
   asserts far less than the prose around it claims. Document E's own V5 pass reached the
   compatible conclusion for the existing files — `carrier_atom_clean_limit` "never
   references spectral mass, `gapfun`, or `carrier_atom_fiber_gap`" — and D's addition does
   not repair that; it formalizes the same decoupled limit arithmetic one level up.

Also: **`G17` is not what D says it is.** D calls it "bounding the actual interacting SU(3)
cross-talk". `ledger/gaps.yaml` G17 is *"PC-2 free-energy stability and the source-radius
reduction — the two named hypotheses gating EVERY infinite-volume statement: the
inhomogeneous Wilson free-energy bound with useful `log K_alpha`, and the source-radius
reduction."* Different object.

### 8.3bis Document C Parts I–II — three real errors

An independent adversarial re-derivation of every item in document C Parts I and II returned
mostly CONFIRMED, plus three genuine errors and one tier problem:

- **II.1 is wrong, and its own numbers say so.** `sup_Γ ‖R_*(z)‖ ≤ 2/d_*` is **false** for a
  band of nonzero width `w` on a circle of radius `d_*/2`; the correct bound is
  `2/(d_* − w)`. The document's own reported *"ratio 1.03; the 3% is band width — which is
  exactly why the conservative `d_*/4` threshold is used"* **is that violation**, reported as
  a confirmation. The Riesz algebra downstream is right; the corrected constant is
  `4(1 + w/d_*)·ε_T/d_*`.
- **I.4's aside is wrong.** *"slightly conservative — the `−ε_W²` is unnecessary"* fails under
  the hypotheses the document itself states; an explicit 2×2 case makes `−ε_W²` exactly tight.
  The main `z_ent` bound is valid (6000-trial stress test clean), and the alternative
  `(√z_* − ε_W − M_*η_P)²` is valid too — but it needs `P_c` to be an **orthogonal**
  projection, and it is stronger exactly when `z_* ≪ M_*²`.
- **I.3's normalization is unstated and non-standard.** The two coefficient identities
  (`p₃ = [√(30π)/2]ψ₂`, `p₃ψ₀ = √5 ψ₂`) are exact and measure-independent, but `ψ₀` and `ψ₂`
  are **not simultaneously orthonormal** under any single-parameter natural convention, so
  `⟨ψ₀, p₃²ψ₀⟩ = 5` rests on a measure the document does not give.
- **II.2**: the `ε_T` budget reproduces exactly; the `ε_W` budget is derived from the
  *tightened* bound rather than from `z_ent` as printed, and fails at its own boundary.
- **Tier inflation**: the appendix manifest marks every Part I/II item `[sympy]` or `[numpy]`,
  but none of these checks exists in the repository. In repo terms they are all T3.

Two of the document's criticisms also over-reach: I.1's counterexample refutes a narrower
class than *"any H3 proof routed through an absolute upper activity bound"*, and I.2's
*"the printed unnormalized formula is false"* is a strawman in the setting document A
actually uses. I.5 is otherwise clean — including the spin coefficient `3/(d+2) = 3/5`,
verified by explicit construction of the symmetric-traceless rank-3 projector in
`d = 2,3,4,5,6`. One refinement: `ρ({M²}) = 2MA` is correct but the factor is a
**KL-kernel convention, not a Jacobian**; read as a Jacobian it would be 1.

### 8.4 Document E is the strongest of the four

Its coefficient-inertness finding is right and useful: replacing the literal by a free symbol
`c` leaves `fiber_gap` valid, so the proof gives **zero bits** toward that number — only the
1:2 ratio between the two printed literals is machine-checked, and the sign is a hypothesis
(`0 < gapfun`), not a verified fact. Two consequences worth drawing out:

- **The fix is free.** Because the coefficient is inert, substituting `c := α/2 = 5/24` into
  `cos_gap` repairs `FiberGap.lean` with **no change to any proof**. `cos_gap` is already
  coefficient-agnostic.
- E's own V-passes are the right posture, and E still inherits the mis-attribution: it calls
  the coefficient "C2-disputed" in Engine C and in the tier table.

### 8.5 The Γ hypothesis, restated

The carrier-atom theorems assume `‖ψ‖ = 1` for a source on the `p=0` fiber, whose base point
is Γ — where `‖ψ(Γ)‖² = q_a(Γ) = 0` and §3.2 says the normalized vector *"has no continuous
extension to Γ"*. **R2 is the resolution**: at Γ the carrier is not a degenerate Bloch vector
but the 3-dimensional harmonic space `ker B(Γ)†`. The right hypothesis is not `k ≠ Γ`; it is
that the rest fiber is `H₂`, on which everything is well defined and Schur-scalar.

---

## 9. Falsifiers

Per `CLAUDE.md`, a candidate without one is an analogy.

| Result | Dies if |
|---|---|
| **R1** | `rank B(k) < 2` at some `k ≠ Γ` (would break the count), or `dim H₂ ≠ 3` |
| **R2** | ~~the C=− projection annihilates the harmonic sector~~ — **closed**: the corpus's opening paragraph puts the harmonic plane triplet *inside* the charge-odd carrier `Z₂`. Remaining routes: a corpus convention making the 2-planes polar rather than axial (T₁u not T₁g), or a physical correction outside the boundary-factorized corner (§3.4 outcome 4) |
| **R3** | a surviving kernel branch with `β < 0` (moves the minimum off-axis and re-couples the gap to C2 — and `β`'s sign is exactly what G3 determines, so this is a live falsifier, not a formality); or a fourth-order shape outside `span{q_a, e₂, 4e₂/q_a, e₃/q_a}` that is nonzero on a coordinate axis |
| **R4** | `B_shp + D_shp/9` not small at the L used (measurable, and the two-L fit detects it); or `ε₄` failing to be a function of the `aᵢ` alone; or an `O(u⁵)` term with its own Γ-anisotropy comparable to `u⁴C_shp` |
| **R4b** | the tier collapse failing at the L used — **detected by `ρ₃ ≠ 2ρ₂ − 1`**, which is the point of the holdout. (The level-crossing route is **closed**: level-2 is the face diagonal unless `β > 2α(3−4s)`, i.e. `C_shp > +0.0962` at L=16, and both branches are negative.) |
| **R5** | the exact blocked object is **not** the pushforward of a fine translation-invariant system — e.g. if the intended construction is an approximate coarse Hamiltonian. This is a definitional question about document A's Step B, answerable without any estimate |

---

## 10. What to do next, in cost order

1. **Answer R5's definitional question first.** It is free and it decides whether TE/SE is
   an estimate problem or a bookkeeping problem. Nothing downstream should be attempted
   before it is settled.
2. **Add the near-Γ triple to the G3 run — R4b first.** Three extra momenta,
   `(2π/L)(1,0,0)`, `(2π/L)(1,1,0)`, `(2π/L)(1,1,1)`, computed from the same sealed kernel.
   Blind, additive, does not touch the frozen 11 items, and it returns:
   - `C_shp` from `ρ₂ = 2 + (96/5)C_shp` — no normalization, no `u`, no `L` extrapolation;
   - its own consistency check `ρ₃ = 2ρ₂ − 1`, the same holdout structure the protocol
     already uses at X/M/R;
   - `B_shp + D_shp/9` from R4's `Δ(L)` at two lattice sizes — attacking **G14** for free;
   - all with the `B,D` contamination suppressed by `sin²(π/L)` rather than at full strength.
   This is the cheapest decisive step now available.
3. **Register R3 as an invariant, then promote to T0.** Pure rational algebra plus one
   termwise inequality plus a trig identity `cos_gap` already carries. It would be the first
   Lean statement in the repo *about the band* rather than about its coefficients.
4. **Fix `FiberGap.lean` by substitution.** `c := 5/24` into `cos_gap`. Free, by E's
   inertness result.
5. **Record the transplant as a `FINDING:` check**, per `CLAUDE.md`'s "when a check fails"
   step 4 — the honest record is that the discrepancy exists, not a silent correction.

---

## 11. Honest limits

- Everything marked `[T1*]` was computed in this session and is **not a registered
  invariant**. In this repository's own terms that makes it T3 until a check exists.
- **R2's most likely failure mode is now closed** (the corpus's opening paragraph puts the
  harmonic triplet inside the charge-odd carrier), but its *pinning* remains conditional on
  §3.4's boundary-factorized corner. R2 gives rank and irreducibility unconditionally and
  pinning only inside that corner.
- **R5 is a structural argument, not a theorem.** It is stated with the assumption that
  decides it precisely because I cannot close it.
- **None of this touches the mass gap.** R1–R4 are statements about a finite-dimensional
  effective Hamiltonian's fourth-order band. G18 (the spectral bridge) and G19 (the
  continuum limit) are untouched, and `AGENTS.md`'s firewall applies: *a theorem about a
  finite-dimensional effective Hamiltonian is not a theorem about a continuum field theory;
  a protected lattice excitation is not a particle.* Document E's closing line is the right
  one and I will repeat it: the T0 status is real, and none of it yet bears on the mass gap.
- The strongest thing here is **R4b**, and its strength is narrow and specific: it makes one
  open contradiction cheaply decidable from a dimensionless ratio, and shows a stated reason
  for its intractability to be too strong. That is worth one sealed run, not a claim.
- **R4/R4b assume the tier collapse holds where it is used.** In the recorded kernels it
  does (`B_SHP_3 = D_SHP_3 = 0` exactly, residuals 3.55e−16 and 2.23e−13), and the
  `ρ₃ = 2ρ₂ − 1` holdout detects failure — but a kernel with genuinely nonzero `B, D`
  shifts `ρ₂` and `ρ₃` and the inversion would need the two-L fit of R4 instead.

---

## 12. Reproduction

```bash
# repo facts
workhouse search '2861009/8438730300'; workhouse why C2; workhouse why G3; workhouse why G14
workhouse verify --only 'h_4^side and the cubic kernel share no denominator structure'
workhouse verify --only 'alpha_3 = 4*A_shp = 5/12'
workhouse verify --only 'the crosswalk is exactly scalar on the momentum axes'
workhouse verify --only 'dim Z_2 at L = 3, 4, 5'
sed -n '260,290p;415,500p' theory/MASTER_THEORY_UNIFIED_2026-08-20_v4_3.md   # §2.4 §3.3 §3.4
sed -n '640,790p'          theory/MASTER_THEORY_UNIFIED_2026-08-20_v4_3.md   # §5.1 §5.2 §5.3
sed -n '685,712p' src/workhouse/constants.py                                  # phi_c, crosswalk
```

```python
# R1: the rank jump is the harmonic triplet
from sympy import *
k1,k2,k3 = symbols('k1 k2 k3', real=True)
d1,d2,d3 = [exp(I*k)-1 for k in (k1,k2,k3)]
B = Matrix([[d2,-d1,0],[d3,0,-d1],[0,d3,-d2]])
psi = Matrix([conjugate(d3),-conjugate(d2),conjugate(d1)])
qa = sum(simplify(abs(x)**2) for x in (d1,d2,d3))
assert simplify(expand(B.det())) == 0
assert simplify(expand(B*B.conjugate().T - (qa*eye(3) - psi*psi.conjugate().T))) == zeros(3,3)
# rank 2 off Gamma, 0 at Gamma  ->  sum_k dim ker B^dag = (L^3-1) + 3 = L^3 + 2

# R3 + R4: the gap and the adjudication
A,B_,C,D,L = symbols('A_shp B_shp C_shp D_shp L', positive=True)
def norm4(k):
    a=[4*sin(x/2)**2 for x in k]
    q=sum(a); e2=a[0]*a[1]+a[0]*a[2]+a[1]*a[2]; e3=a[0]*a[1]*a[2]
    return simplify((A*q + B_*e2 + C*4*e2/q + D*e3/q)/q)
th = 2*pi/L
print(simplify(expand(trigsimp(norm4((th,th,th)) - norm4((th,0,0))))))
#  -> 4*B_shp*sin(pi/L)**2 + 4*C_shp/3 + 4*D_shp*sin(pi/L)**2/9
```

*Nothing in this document is authority. Only the checks are — and the `[T1*]` rows are not
checks yet.*
