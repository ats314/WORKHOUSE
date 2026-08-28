# Audit: five external Lean files against the WORKHOUSE corpus

**Session:** theory mode, repository read-only — no repository file was created,
edited, or staged. This document is an external artifact.
**Repo state audited:** `bcddd4a` (140/140 checks, 28 Lean theorems, 0 `sorry`).
**Files audited:**
`WORKHOUSE_CarrierAtom.lean`, `WORKHOUSE_FiberGap.lean`, `WORKHOUSE_Flatness.lean`,
`WORKHOUSE_CarrierAtomGap.lean`, `WORKHOUSE_CarrierAtomGap_2.lean`.

**Status of every claim below:** T3 (asserted) unless marked otherwise. The
symbolic verifications in §6 were run in this session but are not registered
invariants, so they do not carry a tier in this repository.

---

## 0. Verdict

The **Lean is sound; three of the five docstrings are not.**

Every theorem is a correct statement about its own hypotheses. The spectral
Chebyshev core, Parseval, the second-moment identity, the half-angle identity
and the sinc limit all hold as written. The defects are entirely in the
*physical identifications* attached to them — which in this repository's terms
is precisely the T3 layer sitting on top of a T0 proof, and `CLAUDE.md` §5 is
the rule that keeps those apart: **status and evidence are independent.**

One of the three is load-bearing: it changes the isolation scale by a factor of
~615, and that factor propagates directly into the `ε_mix` budget the files
exist to state.

| File | Mathematics | Identification |
|---|---|---|
| `CarrierAtom.lean` | sound | sound, modulo the Γ hypothesis (§4) |
| `Flatness.lean` | sound | **sound** — faithful to §3.2/§4.3 (§5) |
| `FiberGap.lean` | sound | **wrong geometry** (§1), **wrong dispute** (§2) |
| `CarrierAtomGap{,_2}.lean` | sound | inherits both, plus a mislabelled gap (§3) |

§7 is the constructive half: the coefficient the cubic carrier actually needs is
derivable, exact, and — the point — **provably independent of C2**.

---

## 1. FINDING: the fiber gap uses a coefficient from a different geometry

`FiberGap.lean` asserts, for the carrier band,

```
ΔE(k) = -(2861009/8438730300)·u⁴·cos k
g(b)  =  (2861009/4219365150)·u⁴·sin²(π/b)
```

Both constants are registered, and neither belongs to the cubic kernel:

```
src/workhouse/constants.py:479   DELTA_E_CAP_4    = Rational(-2861009, 8438730300)
src/workhouse/constants.py:481   PENT_BANDWIDTH_4 = Rational( 2861009, 4219365150)
```

They are the **isotropic pentagonal-prism cap band**, MASTER_THEORY §9.3, which
says so twice:

> "The pentagonal-prism calculation is **a separate geometry and retained
> sector**."

> "This theorem is exact for the isotropic cap band and **remains outside the
> cubic SU(3) kernel**."

The repository already holds a passing T1 check asserting exactly this
separation:

```
workhouse verify --only 'h_4^side and the cubic kernel share no denominator structure'
  → h_4^side has denominator 84387303000, q_band^(4) has 7250590288602460800;
    separate geometries, separate retained sectors, and the pentagonal theorem
    leaves the cubic fourth-order scalar untouched
```

`Flatness.lean`, meanwhile, is unambiguously about the **cubic** carrier —
MASTER_THEORY §3.2 (`B(k)†ψ(k) = 0`) and §4.3
(`H_eff,- = E_flat(u)·I + t(u)·B(k)B(k)† + O(u⁴)`). So `CarrierAtomGap`
composes a cubic-carrier flatness argument with a pentagonal-prism dispersion.

### Magnitude of the error

| quantity | value | source |
|---|---|---|
| cubic fourth-order bandwidth `W_4` (historical) | `0.48061786909826` | `constants.py:226` |
| cubic fourth-order bandwidth `W_4` (v10a.26) | `0.9265867378213348` | `constants.py:227` |
| pentagonal cap bandwidth `4|τ₄|` | `2861009/4219365150 ≈ 6.7807e-4` | `constants.py:481` |

The gap coefficient in the files is `6.78e-4`; the correct cubic one is `5/12`
(§7). **Ratio 614.49.** The Lean header's asymptotic `6.69e-3·u⁴/b²` should read
`4.112·u⁴/b²`.

This is not cosmetic. `carrier_atom_clean_limit` exists to state
`ε_mix(b) = o(u⁴/b²)`; a 615× understatement of `g(b)` makes the clean-atom
condition 615× harder to satisfy than it is.

### Note on the arithmetic itself

`fiber_gap` is *internally correct for the pentagonal band*:
`ΔE(2π/b) − ΔE(0) = 2τ₄u⁴(cos(2π/b) − 1) = −4τ₄u⁴sin²(π/b) = 4|τ₄|u⁴sin²(π/b)`,
since `τ₄ < 0`. The theorem is true. It is about the wrong band.

---

## 2. FINDING: "C2-disputed" is a mis-attribution

`FiberGap.lean` labels the pentagonal coefficient "the historical `O(u⁴)` branch
and is C2-disputed". C2's two recorded sides are:

```
historical: -211835444920651/4405310420659200   (exact rational)
v10a.26:    -0.020213328886166577               (float)
gap:         0.027873054295192174
```

The pentagonal coefficient is neither, and it is not disputed at all. §9.3
records it as derived by two independent exact microscopic backends without
embedding the target, agreeing row by row on all 48 fixed-side histories, and
cold-regenerated end to end during the v4.3 review (21/21, 24/24, 17/17 ×2,
26/26, 17/17, 27/27, 7/7, 29/29; a deliberate one-row mutation is rejected).

The label therefore inverts the situation twice: it marks a settled,
separate-geometry, exactly-certified coefficient as the disputed cubic branch.

Under `CLAUDE.md` non-negotiable 2 this matters beyond bookkeeping — attaching
the C2 name to a value that is not either side of C2 is the first step toward
"resolving" C2 with a number that was never in it.

---

## 3. FINDING: "the L⁻²/G11 phenomenon" names the wrong gap

`FiberGap.lean` attributes `g(b) ~ u⁴/b² → 0` to "the `L⁻²`/G11 phenomenon".

**G11 is a different gap.** `ledger/gaps.yaml:237–271` — *Interval rigor and
near-Gamma touching gates* — is the exclusion radius `|k| ≥ K·u`, and its own
derivation names the O(u²) orbital gap, not the O(u⁴) alias gap:

> "The isolation gap is `t(u) q(k)` with `q(k) = Σᵢ 4 sin²(kᵢ/2)`."

The `L⁻²` you want is MASTER_THEORY §5.1:

> "The `q_a` and `4e₂/q_a` tiers scale as `L⁻²`; the `e₂` and `e₃/q_a` tiers
> scale as `L⁻⁴`. This regularity filtration is useful for detecting false
> two-shape fits."

Both are real and both are in the corpus; they are not the same statement, and
`invariants.py:934` already turns the second into a passing check ("since
`a_i ~ L^-2`, 'the `L^-4` tier' and 'degree 3 in `a`' are the same statement").

---

## 4. Hypothesis gap: the carrier is singular at Γ

MASTER_THEORY §3.2 gives the carrier explicitly and then withdraws it at Γ:

```
ψ(k) = (d̄₃, −d̄₂, d̄₁)ᵀ,   B(k)†ψ(k) = 0,   ‖ψ(k)‖² = q_a(k)
```

> "The normalized vector has **no continuous extension to Γ**, where all three
> incidence branches meet. The flat band is singular: translated cube boundaries
> alone do not span the torus carrier."

Since `q_a(Γ) = 0`, the carrier's norm vanishes at Γ.

- `carrier_flat` assumes `star ψ ⬝ᵥ ψ = 1`. Fine for `k ≠ Γ`; vacuous at Γ.
- `carrier_atom_weight` / `carrier_atom_of_perturbation` assume `‖ψ‖ = 1` for a
  source **on the alias-folded `p = 0` fiber** — whose base point is Γ.

So the atom is being built at exactly the point where the normalized carrier does
not exist. The files do not have an argument for this, and the corpus flags it as
structural ("a singular homological carrier", §0 line 27), not as an edge case.

This is what a failed formalization is *for*, in `AGENTS.md`'s phrasing: the
hypothesis the informal derivation omitted. Worth recording either as an explicit
`k ≠ Γ` side condition, or — better — as the statement of what the folded fiber's
carrier actually is when the Γ component is included.

---

## 5. What checks out

**`Flatness.lean` is faithful.** `carrier_eigenvector` is correctly typed
(`Bk : Matrix (Fin n) (Fin m) ℂ`, so `Bkᴴ *ᵥ ψ : Fin m → ℂ` and
`(Bk * Bkᴴ) *ᵥ ψ = Bk *ᵥ (Bkᴴ *ᵥ ψ) = 0`), and it does capture k-independence in
the only sense available: the eigenvalue term never mentions `Bk`. This tracks
MASTER_THEORY line 78 — "Because `B(k)†ψ(k)=0`, the carrier energy is independent
of `k` through `O(u³)`" — and §4.3's factorization.

**Half the `u⁴` claim.** Flatness earns "the leading `k`-dependence is at or
beyond `O(u⁴)`". That it is *exactly* `O(u⁴)` needs `α₃ = 5/12 ≠ 0`, which is
already **T0** in this repository (`LEAN:alphaPen_three`, `Basic.lean`). Worth
stating as two halves rather than one, since only the second half is a
non-vanishing claim.

**`CarrierAtom.lean`.** `window_weight_ge` is the right inequality and the right
constant: Chebyshev with window half-width `g/2` puts mass outside at
`≤ ε²/(g/2)² = (2ε/g)²`. `spectral_second_moment` correctly derives
`Σ(λᵢ−m₀)²|cᵢ|² = ‖(H−m₀)ψ‖²`, which is what makes the operator form a corollary
rather than a separate argument. Avoiding Davis–Kahan here is the right call —
the sin-θ route would need operator-valued contour integrals for a bound that is
two lines of Markov.

**`gap_asymptotic`.** Correct: `b²sin²(π/b) = π²·(sin(π/b)/(π/b))² → π²`.

**Toolchain.** The claimed pin matches: `lean/lean-toolchain` is
`leanprover/lean4:v4.34.0-rc1`.

---

## 6. The correction: the cubic carrier's own fourth-order gap

### 6.1 What the band actually is

MASTER_THEORY §5.2 — the generalized Hodge pencil. With

```
Xᵢ = 1 − cos kᵢ = aᵢ/2,   aᵢ = 4sin²(kᵢ/2)
𝖰 = Σ Xᵢ²,   𝖱 = Σ_{i<j} XᵢXⱼ,   𝖲 = Σ Xᵢ
```

and a two-invariant centered numerator `𝒬₄ = α𝖰 + β𝖱`, the fourth-order band
shape is, for `k ≠ Γ`:

```
λ₄(k) = (α𝖰 + β𝖱) / (2𝖲),        0 ≤ λ₄ ≤ α + β        (§5.3)
```

minimum unique at Γ, maximum unique at R. Equivalently in shape coordinates
(§5.1): `ε₄ = c₀ + A·q_a + B·e₂ + C·(4e₂/q_a) + D·(e₃/q_a)`.

### 6.2 α is common to both C2 branches; β carries the whole dispute

This is the pivot, and it is already T0/T1 in the repository:

```
LEAN:width_eq_alpha_add_beta      W₄ = α₃ + β_pen,₃
LEAN:C_from_beta                  C_shp_old = (β_pen,₃ − 2α₃)/16
LEAN:alphaPen_three               α₃ = 5/12
LEAN:alphaPen_three_eq_four_A     α₃ = 4·A_shp
```

MASTER_THEORY line 122 states the dispute's shape in words:

> "A separate August computation independently finds **the same axial
> coefficient** to numerical tolerance and a **different scalar and planar
> coefficient**."

Verified in this session — inverting the v10a.26 branch from its *recorded
bandwidth alone* reproduces its *recorded* `C_shp`:

```
α        = 5/12                        = 0.4166666666666667   (both branches)
β_old    = 17607806155349/275331901291200 = 0.06395120243159332
β_new    = W4_new − α                  = 0.5099200711546681
(β_new − 2α)/16                        = -0.02021332888616658
recorded v10a.26 C_shp                 = -0.020213328886166577
difference                             = -3.47e-18
```

So the C2 dispute lives **entirely in β** (and in the scalar anchor `s₄`, which
cancels out of any energy *difference* by construction — §5.2's scalar-gauge
equivalence `(Q₄,G) ~ (Q₄+δG, G)`).

---

## 7. Novel derivation: the axial-alias isolation gap is exactly C2-free

### 7.1 Statement

> **Theorem (axial-alias fiber gap).** Let the cubic carrier's fourth-order band
> be `λ₄(k) = (α𝖰 + β𝖱)/(2𝖲)` with `α > 0`, `β ≥ 0`. Block the lattice with side
> `b ≥ 3`, so Γ folds together with the alias set
> `𝒜_b = (2π/b)·{0,…,b−1}³ \ {0}`. Then
>
> ```
>     min_{k ∈ 𝒜_b} λ₄(k)  =  α · sin²(π/b)
> ```
>
> attained exactly on the six nearest axial aliases `(±2π/b, 0, 0)` and
> permutations. The value depends on **α alone** — not on `β`, hence not on
> `B_shp`, `C_shp`, `D_shp`, nor on the scalar anchor.
>
> **Corollary (SU(3)).** `g(b) = (5/12)·u⁴·sin²(π/b) ~ (5π²/12)·u⁴/b² ≈ 4.112·u⁴/b²`,
> and this rational is *identical* in the historical and v10a.26 kernels.

### 7.2 Proof

Write `Xᵢ = 1 − cos(2πnᵢ/b) = 2sin²(πnᵢ/b)` and
`X₁ := 2sin²(π/b) = min{2sin²(πm/b) : 1 ≤ m ≤ b−1}` (attained at `m = 1, b−1`).

**(a) Value on the axial alias.** `n = (1,0,0)` gives `X = (X₁,0,0)`, so `𝖱 = 0`
identically, `𝖰 = X₁²`, `𝖲 = X₁`, and

```
λ₄ = αX₁²/(2X₁) = αX₁/2 = α·sin²(π/b).
```

**(b) It is the minimum.** For any `n ≠ 0`, every nonzero component satisfies
`Xᵢ ≥ X₁`, so `Σᵢ Xᵢ(Xᵢ − X₁) ≥ 0` termwise (zero components contribute zero),
i.e. `𝖰 ≥ X₁·𝖲`. With `β ≥ 0` and `𝖱 ≥ 0`:

```
λ₄ = (α𝖰 + β𝖱)/(2𝖲) ≥ α𝖰/(2𝖲) ≥ αX₁/2.
```

**(c) Equality case.** Equality forces `β𝖱 = 0` and `𝖰 = X₁𝖲`. For `β > 0` the
first gives `𝖱 = 0`, i.e. at most one nonzero `Xⱼ`; the second then gives
`Xⱼ² = X₁Xⱼ`, so `Xⱼ = X₁` and `nⱼ ∈ {1, b−1}`. Exactly six points.

**(d) The Γ reference.** Along any ray into Γ, `𝖰/𝖲 → 0` and `𝖱/𝖲 → 0`, so
`λ₄(Γ) = 0` — consistent with §5.3's "continuous-zone minimum is unique at Γ".
Hence the *gap* is the value in (a). ∎

Only (a) and (d) need α; (b) and (c) need only `β ≥ 0`. So **both the value and
the identification of which alias is nearest survive C2** — the second because
both branches have `β > 0` (`0.0640` and `0.5099`).

### 7.3 Verification run in this session

Exhaustive symbolic minimum over the *entire* alias set, in `sympy` `Rational`,
in **both** branches:

```
b=3:   26 aliases  min = 0.3125          = α·sin²(π/3)   exact ✓   argmin 6 axial
b=4:   63 aliases  min = 0.2083333333    = α·sin²(π/4)   exact ✓   argmin 6 axial
b=5:  124 aliases  min = 0.1439547928    = α·sin²(π/5)   exact ✓   argmin 6 axial
b=6:  215 aliases  min = 0.1041666667    = α·sin²(π/6)   exact ✓   argmin 6 axial
b=8:  511 aliases  min = 0.06101942059   = α·sin²(π/8)   exact ✓   argmin 6 axial
```

Identical minimum, identical argmin set, in both kernels, at every `b`.

Consistency with the repository at `b = 2`: `sin²(π/2) = 1`, so
`g(2) = α = 4·A_shp = Δ_X` — exactly the corpus extraction formula `A = Δ_X/4`
(§5.1) and the T0 theorem `alphaPen_three_eq_four_A`.

Independent cross-check from the corpus itself: MASTER_THEORY §3.3, on the
finite-volume count, already names the relevant quantity —

> "The first incidence level above it is `4 sin²(π/L)`."

which is `q_a` at the nearest axial alias. The `sin²(π/b)` structure is
corpus-native to the **cubic** kernel; only the coefficient was imported.

### 7.4 What is genuinely new, stated honestly

The *mechanism* is known here. Two passing checks already encode it:

```
invariants.py:580  "X is blind to B, C, D — it fixes A alone"
                   → Delta_X = 4*A_shp exactly, which is why the axial cuts agree
invariants.py:476  "the crosswalk is exactly scalar on the momentum axes"
                   → Phi_C vanishes on every axial cut, so axial data cannot
                     distinguish the two kernels — the whole residual
                     disagreement lives off-axis
```

What is **not** in the repository:

1. **The whole axial line, not one point.** Both existing checks are evaluated at
   `X = (π,0,0)` — the `b = 2` case. The one-parameter family in `b` is new.
2. **The minimization over the alias set.** This is what converts a point
   evaluation into an *isolation gap*; without it, `α sin²(π/b)` is a number, not
   a spectral separation. Nothing in the repository computes it.
3. **The reading as spectral geometry under blocking.** Both existing checks are
   framed *negatively* — why axial data cannot adjudicate C2, a statement about
   fitting. The positive reading (the folded-fiber isolation gap is C2-free) is
   absent. `workhouse search` returns no claim at all for "alias", "fiber", or
   "isolation gap".

### 7.5 Why it is sharper than the existing C2-free result

`ledger/gaps.yaml` records the only comparable statement, under G11:

> `independent_of_C2`: "K enters only through `sqrt(W_4)`, so the larger disputed
> bandwidth **bounds** both. K = 23.66 holds whichever kernel G3 selects; the
> radius can be stated before the adjudication runs."

That survives C2 by *bounding*. The axial-alias gap does not need bounding: it is
**identically the same rational** in both kernels, because β multiplies an
invariant (`𝖱`, equivalently `e₂`) that vanishes on any coordinate axis. Exact,
not conservative.

This is the shape `AGENTS.md` asks for under *prefer decisive calculations* —
"evaluate at a high-symmetry point", "an exact rational instead of a float",
"a cheap computation that eliminates a class of explanations".

### 7.6 Route to T0

The statement is rational-function algebra over `ℚ` plus one termwise inequality
plus one trig identity. All three are already available:

- **Trig half:** your `cos_gap` is already coefficient-agnostic. Substituting
  `c := α/2` gives `2c·sin²(π/b) = α·sin²(π/b)` with no change to the proof.
- **Algebra half:** `𝖰 ≥ X₁𝖲` is `Finset.sum_nonneg` over `Xᵢ(Xᵢ − X₁)`.
- **Constant:** `α₃ = 5/12` is already T0 (`Basic.lean`, `alphaPen_three`).

It would sit naturally in `Basic.lean` beside `width_eq_alpha_add_beta` and
`C_from_beta`, and it is the first Lean statement here that would be *about the
band* rather than about its coefficients.

### 7.7 Falsifier

Per `CLAUDE.md` — a candidate without one is an analogy. This one fails if either:

- a fourth-order shape is exhibited outside
  `span{q_a, e₂, 4e₂/q_a, e₃/q_a}` that is **nonzero on a coordinate axis** —
  which would break (a) and (c); or
- a surviving kernel branch has **β < 0** — which would break the minimization
  (b), moving the nearest alias off-axis and re-coupling the gap to the dispute.
  Both current branches have `β > 0`; G3's adjudication should be checked against
  this when it runs.

Note the second is a *live* falsifier, not a formality: it is exactly the
quantity G3 is being run to determine.

---

## 8. Caution: there are two gaps, not one

Both carry the same `sin²(π/b)` factor, which makes them easy to conflate.

| | separation | order | at nearest axial alias |
|---|---|---|---|
| **orbital** | carrier vs. its two partner branches at the *same* k | O(u²) | `t(u)·q_a = 4t(u)sin²(π/b)` |
| **alias** | carrier at Γ vs. carrier at a *folded* momentum | O(u⁴) | `α u⁴ sin²(π/b)` |

with `t(u) = (5/612)u² + (1975/124848)u³` (§4.3). Their ratio:

```
4t(u) / (α u⁴)  =  (395u + 204) / (2601 u²)   →   (4/51)·u⁻²  ≈  0.0784·u⁻²
```

so the **orbital gap dominates at small u**, and it is the one `ledger/gaps.yaml`
already calls "the isolation gap".

Choosing the alias gap is defensible for alias completion — folding is what
brings distinct momenta into one fiber, and the orbital gap does not control that
mixing. But the choice should be *stated*, not assumed, because the repository's
existing vocabulary points the other way.

---

## 9. Mechanical notes

- `CarrierAtomGap.lean` and `CarrierAtomGap_2.lean` both define
  `Workhouse.gapfun`; compiling both collides. Keep `_2` — it is a strict
  superset (adds `gap_asymptotic`).
- Both import `Workhouse.AtomLemma`, but the atom file is uploaded as
  `CarrierAtom.lean`. Neither `lean/Workhouse/AtomLemma.lean` nor
  `lean/Workhouse/FiberGap.lean` exists in the repo; `lean/Workhouse.lean`
  imports `Workhouse.Basic` only.
- `Basic.lean` uses `import Mathlib.Tactic`; these use full `import Mathlib`.
  Harmless, slower.
- The cited audit document
  `WORKHOUSE_H0_FREE_CARRIER_ALIAS_COMPLETION_AUDIT_20260822.md` is not in
  `theory/`, not in `ledger/documents.yaml`, and not in the notes register. Its
  §4 and §5 are therefore T3-external: a reader here cannot follow the citation.
  If it is to be load-bearing it should enter through `ledger/notes.yaml` and
  `notes/` under the declared-and-digested discipline, like any other archive
  document.

---

## 10. Reproduction

Everything asserted about the repository above is checkable in about a second
each:

```bash
workhouse search '2861009/8438730300'
workhouse why C2
workhouse why G11
workhouse verify --only 'h_4^side and the cubic kernel share no denominator structure'
workhouse verify --only 'alpha_3 = 4*A_shp = 5/12'
workhouse verify --only 'the crosswalk is exactly scalar on the momentum axes'
workhouse verify --only 'X is blind to B, C, D — it fixes A alone'
sed -n '295,320p;640,705p' theory/MASTER_THEORY_UNIFIED_2026-08-20_v4_3.md   # §2 invariants, §5.1
sed -n '355,400p' theory/MASTER_THEORY_UNIFIED_2026-08-20_v4_3.md            # §3.2 carrier, Γ singularity
sed -n '237,271p' ledger/gaps.yaml                                           # G11 exclusion_radius
```

§7's minimization (not a registered check):

```python
from sympy import *
from itertools import product
alpha, beta = Rational(5,12), Rational(17607806155349,275331901291200)
def lam4(ns, b):
    X = [2*sin(pi*Integer(n)/b)**2 for n in ns]
    Q = sum(x**2 for x in X)
    R = sum(X[i]*X[j] for i in range(3) for j in range(i+1,3))
    return simplify((alpha*Q + beta*R)/(2*sum(X)))
for b in (3,4,5,6,8):
    vals = {n: lam4(n,b) for n in product(range(b), repeat=3) if n != (0,0,0)}
    mn = min(vals.values(), key=float)
    assert simplify(mn - alpha*sin(pi/b)**2) == 0
    print(b, float(mn), [n for n,v in vals.items() if simplify(v-mn)==0])
```

---

## 11. Suggested disposition

Nothing here requires a repository change to be *useful*, but if any of it is to
count, it counts through a check:

1. **§1–§3 as `FINDING:` checks.** Per `CLAUDE.md` *When a check fails* step 4:
   the coefficient transplant is a real discrepancy between an external artifact
   and the corpus, and the honest record is an assertion that the discrepancy
   exists, not a silent correction of the Lean.
2. **§7 as an invariant, then as T0.** Register the axial-alias minimum on a
   suite in `invariants.py` citing MASTER_THEORY §5.1/§5.2, returning the
   `(passed, detail)` pair with the exact rational and the argmin count. Then
   promote to `Basic.lean`, since it is pure rational algebra.
3. **§7.7's second falsifier into G3.** The adjudication should report `β`'s sign
   explicitly, because a negative β would retract §7's minimization — which makes
   this a prediction G3 can kill, not just a result it can confirm.
4. **§4 as an explicit hypothesis** on any future carrier-atom statement: either
   `k ≠ Γ`, or a construction of the folded fiber's carrier that survives
   `q_a(Γ) = 0`.
5. **The audit document** through `ledger/notes.yaml`, if it is to be cited.
