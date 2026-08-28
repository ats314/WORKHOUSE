# WORKHOUSE H0 free-carrier alias-completion audit

Date: 2026-08-22
Status: H0 discharged at Gaussian order; isolation rate proven; folded-fiber atom lemma verified and Lean-ready. The residual bound on block-induced alias mixing (= G17) is not supplied.
Scope: the common alias-complete `p=0` representation and its cross-Gram/frame lower bound (hypothesis **H0** of `WORKHOUSE_FIXED_TO_CONTINUUM_MASTER_CHAIN`, Step D), tested on the free/Gaussian leading-order carrier; the exact carrier dispersion power; and the folded-fiber matrix-atom stability lemma feeding `WORKHOUSE_MATRIX_KL_CARRIER_ATOM_THEOREM` Thm 3.4.
Repository status: read-only; this report is external to the WORKHOUSE clone. No exact rational was promoted; no tolerance was widened.

---

## 0. One-paragraph result

H0 — the "first open model object" of the fixed-to-continuum chain (construct the common alias-complete `p=0` representation and prove a uniform cross-Gram/frame lower bound) — **holds exactly and uniformly at Gaussian order**: the `b^d` block-origin construction reproduces the true fine `p=0` carrier with frame bound equal to the fixed-spacing bound `z_*`, independent of the block factor `b` and of dimension `d`. H0 is therefore **not** where the continuum difficulty lives. The computation instead relocates the difficulty precisely: the `p=0`-fiber isolation gap collapses as `g(b) ~ u^4/b^2` (power proven by the exact `O(u^3)` homological flatness `B(k)†ψ(k)=0`; exact coefficient `2861009/4219365150 · u^4 sin^2(π/b)`), so a fixed isolating contour is unavailable and the shrinking-island route (Matrix-KL Thm 3.4) is mandatory. On the folded fiber the carrier atom survives block-induced alias mixing `V` (`‖V‖=ε`) with whitened weight `λ_min(Z) ≥ 1 − (2ε/g)²` — a finite-dimensional Davis–Kahan lemma, verified numerically. Combining: a uniform carrier atom requires `ε_mix(b) = o(u^4/b^2)`, which is a **G17** statement and the sole remaining hard input.

---

## 1. What H0 is

From `WORKHOUSE_FIXED_TO_CONTINUUM_MASTER_CHAIN` §3 (Step D) and `WORKHOUSE_UNIFORM_CARRIER_RESIDUE_H3_AUDIT` §6, hypothesis **H0** (the model object logically prior to the entry inequalities TE, SE) is:

> Construct a common gauge-, `C`-, cubic-, and translation-covariant identification of the induced coarse OS representation with the fixed-spacing reference, **including all `b_n^3` block-origin embeddings**, prove their closed span reduces the fine transfer and one-step translations, construct the alias-fiber disintegration, and prove a **uniform cross-Gram/frame lower bound for the true fine `p=0` component**.

The reason `b_n^3` origins are required (audit's own statement): a fixed-origin block map is covariant only under block-step (coarse) translations. Reconstructing the fine `p=0` fiber — which needs the fine one-step translation structure — requires combining the `b_n^3` residue-class block origins.

This note tests H0 in the only regime where it is fully computable: the **free/Gaussian leading-order carrier** (`u→0` limit of the strong-coupling coordinate `u`).

---

## 2. The free/Gaussian carrier model

Grounded on the corpus one-plaquette theory (`theory/MASTER_THEORY_UNIFIED_2026-08-20_v4_3.md`; `theory/superseded/MASTER_THEORY.md` §4.4–4.6):

- **Carrier band** (rank `r=3`, the cubic `T_1^{+-}` triplet), lattice units:
  `E(k) = m_0 + Δ(u; k)`, `m_0 = 8/3` (the C-odd one-flux branch bottom, `m_-(u)=8/3+u+(11/306)u^2-(109151/249696)u^3+O(u^4)` at `k=0`).
- **Flatness**: `Δ(u;k)` is `k`-independent through `O(u^3)` (see §4).
- **Fixed-spacing source frame**: `J_0 : C^3 → K_*` with `J_0† J_0 ⪰ z_* I_3`, `z_* > 0` — the CMP(4) literal-Wilson frame bound at fixed spacing (external theorem `WORKHOUSE_CMP4_...`).

### 2.1 Blocking and the alias-folded `p=0` fiber

Block by `b` per dimension: fine spacing `a=1`, coarse `A=b`, `N_f = b·N_c` sites/dim. A coarse momentum receives `b^d` fine momenta ("aliases"). The `p=0` coarse fiber is spanned by the fine modes

`k_f^{(s)} = (2π/A) s`, `s ∈ {0,…,b−1}^d`,

with `s=0` the **true fine `p=0` carrier** and `s≠0` the aliases (fine momenta at the coarse Brillouin-zone scale). The carrier band aliased onto itself supplies the binding near-degeneracy.

### 2.2 The `b^d` block-origin sources

For block origin `τ ∈ {0,…,b−1}^d`, the fixed-origin coarse `p=0` source, resolved in the alias basis, is

`J^{(τ)}_s = e^{i k_f^{(s)}·τ} · G(k_f^{(s)}) · J_fine(k_f^{(s)})`,

where `G(k) = ∏_i (1/b) Σ_{m=0}^{b−1} e^{i k_i m}` is the block-average form factor. Two structural facts:

1. **DFT relation.** The phase table `e^{i k_f^{(s)}·τ} = e^{i 2π s·τ/b}` is (up to normalization) the `b^d`-point DFT matrix. Hence `{J^{(τ)}}_τ` is a unitary image of the alias-diagonal sources `{ e_s · G(k_f^{(s)}) J_fine(k_f^{(s)}) }`. The cross-Gram is unitarily equivalent to the block-diagonal `diag_s( |G(k_f^{(s)})|^2 · J_fine(k_f^{(s)})† P_carrier(k_f^{(s)}) J_fine(k_f^{(s)}) )`.
2. **Box form factor kills nonzero aliases exactly.** For the ideal box average, `G(k_f^{(s)}) = ∏_i δ_{s_i,0} = δ_{s,0}`. So every origin's coarse `p=0` source equals the `s=0` carrier; the aliases are never excited (they are, correctly, to be projected out).

---

## 3. Result 1 — H0 holds, uniformly (verified)

Computed with `h0_free.py` (Appendix A.1). `λ_min(carrier cross-Gram)` is per-origin-normalized and reported as a ratio to the fixed-spacing bound `z_*`.

| Setting | `λ_min(carrier)/z_*` | full-fiber `λ_min` | note |
|---|---|---|---|
| 1D, `b=2…64`, box kernel | **1.000000** (all `b`) | ~`10^{-33}` | aliases exactly suppressed |
| 1D, `b=2…32`, non-ideal (smooth) kernel | **1.000000** (all `b`) | `0.37 → ~0` | carrier frame still `z_*` |
| 3D, `b=2,3,4` (up to `b^3=64` aliases), box | **1.000000** | — | `b^d` introduces no degeneracy |

**Reading.**
- The per-origin carrier frame equals `z_*` **exactly and independently of `b` and `d`**. H0's uniform cross-Gram lower bound onto the true fine `p=0` component holds.
- The full-fiber `λ_min ≈ 0` (box) is expected and desirable: the block map excites only the carrier, not the aliases. With a non-ideal kernel the aliases are excited but their frame vanishes as `b→∞`; the carrier component is untouched because `G(0)=1` for any normalized kernel.

**Conclusion.** H0 is discharged at Gaussian order. It is not the obstruction, and should stop being listed as "the first open model object."

---

## 4. Result 2 (task a) — the dispersion power is `p=4`, proven

The `u`-power of the leading carrier dispersion sets the isolation rate. The corpus settles it:

- **Exact `O(u^3)` flatness, homological reason** (`v4_3` line 78): *"Because `B(k)†ψ(k)=0`, the carrier energy is independent of `k` through `O(u^3)`."* The carrier `ψ(k)=(d̄_3,−d̄_2,d̄_1)` lies in `ker B(k)†`, so every correction factoring through `B(k)B(k)†` is `k`-flat. This is `[PROVEN]` (not certified-within-truncation).
- **First dispersion at `O(u^4)`, exact coefficient** (`GLUEBALL_SOURCE_CONSOLIDATION_GUIDE_v4_3` line 317; ordinary `2τ_4 cos k` cap-band hopping, line 119):

  `ΔE(k) = −(2861009/8438730300) u^4 cos k`.

Therefore the **fiber isolation gap** — carrier at Γ vs the nearest self-alias at `k = 2π/b` — is, exactly (Appendix A.4):

`g(b) = (2861009/4219365150) · u^4 · sin^2(π/b)  ≈  6.6922×10^{-3} · u^4 / b^2`,

with `g(b)·b^2/u^4 → 2861009 π^2 / 4219365150 = 0.006692245400461788`.

**So `g(b) ~ u^4/b^2`, not `u^2/b^2`** (the earlier working estimate was two powers of `u` loose).

Two caveats, both material:

- The **power `p=4` is proven** (it is forced by the exact `O(u^3)` flatness). The **exact coefficient is the historical `O(u^4)` branch and is C2-disputed** (the physical planar `O(u^4)` coefficient `C_shp` is the one open contradiction; `GLUEBALL_..._GUIDE` line 594). The rate `u^4/b^2` is independent of the C2 resolution; only the constant `6.69×10^{-3}` is.
- The `O(u^2|k|^2)` near-Γ term (G11; `v4_3` line 887, `MASTER_THEORY` line 386) is a **different, larger** gap — the separation of the carrier from *other branches* (`~u^2/b^2`). The **binding** isolation is the carrier's self-alias gap `~u^4/b^2`, so that is the rate that governs the atom.

---

## 5. Result 3 (task b) — folded-fiber carrier-atom lemma (verified, Lean-ready)

In the free theory the isolation collapse is harmless: the box source lives on `s=0`, an exact eigenvector of the alias-diagonal free transfer, so the atom is clean with weight `z_*` for every `b` (source is blind to the aliases). The danger appears only when interactions couple `s=0` to the near-degenerate aliases. The following lemma bounds that.

### Lemma (carrier atom on the folded `p=0` fiber)

Let `𝓗` be finite-dimensional. Let `H_0` be self-adjoint with the rank-`3` carrier block at energy `m_0` and every alias block at energy `≥ m_0 + g` (`g>0` the fiber isolation gap). Let `V` be self-adjoint with `‖V‖ = ε < g/2`, `H = H_0 + V`. Let `P` be the spectral projection of `H_0` onto `{m_0}` and `Q` the spectral projection of `H` onto the window `W = [m_0 − g/2, m_0 + g/2]`. Let `J` be a source with `range(J) ⊆ range(P)` (box map: supported on the carrier) and Gram `G = J†J ≻ 0`. Then

`‖Q − P‖ ≤ 2ε/g`  (Davis–Kahan sin-θ), and consequently the whitened island fraction

`Z_W := G^{-1/2} J† Q J G^{-1/2}` satisfies `λ_min(Z_W) ≥ 1 − (2ε/g)^2`,

with island diameter `≤ g`.

**Proof.** `‖Q−P‖ ≤ 2ε/g` is sin-θ for the window `W` whose edges are distance `g/2` from `spec(H_0)\{m_0}` and from `m_0`. Since `J = P J`, `J†QJ = J† P Q P J`, and `P Q P ⪰ (1 − ‖P−Q‖^2) P` (projection algebra: `P(1−Q)P ⪯ ‖P−Q‖^2 P`). Whitening by `G^{-1/2}` gives `Z_W ⪰ (1 − ‖P−Q‖^2) I_3 ⪰ (1 − (2ε/g)^2) I_3`. ∎

### Numerical verification (`h0_fulllemma.py`, Appendix A.2)

Full `b^3` fiber (`3 b^3` dimensions), random Hermitian `V` normalized to `‖V‖=ε`, `d=3`:

| `b` | `g(b)` | `ε/g` | `λ_min(Z_W)` | bound `1−(2ε/g)^2` |
|---|---|---|---|---|
| 3 | 3.0e-2 | 0.20 | 0.996 | 0.84 ✓ |
| 3 | 3.0e-2 | 0.35 | 0.985 | 0.51 ✓ |
| 4 | 2.0e-2 | 0.35 | 0.992 | 0.51 ✓ |
| 6 | 1.0e-2 | 0.35 | 0.997 | 0.51 ✓ |

The bound holds in every case, conservatively (the sin-θ constant is not tight for generic `V`).

### Mechanism (2-level dominant channel, `h0_mechanism.py`, Appendix A.3)

Coupling the carrier to only the nearest alias, the atom weight is a **universal function of `ε/g`** (identical across `b=8,32,128`):

| `ε/g` | 0.1 | 1.0 | 3.0 | 10 |
|---|---|---|---|---|
| carrier atom weight | 0.990 | 0.724 | 0.582 | → 0.5 |

Since `g(b)→0`, any fixed alias coupling eventually satisfies `ε/g → ∞` and the atom smears to a 50/50 island.

### Uniformity corollary

Island diameter `≤ g(b) → 0` (a genuine shrinking island — this is exactly the `diam(I_n)→0` hypothesis of Matrix-KL Thm 3.4). The carrier atom has:

- **bounded-below weight uniformly in `b`** ⟺ `limsup_b 2ε_mix(b)/g(b) < 1`;
- **clean weight (→1)** ⟺ `ε_mix(b) = o(g(b))`.

---

## 6. Combined statement — the corrected TE target

With `g(b) ~ u^4/b^2` (§4) inserted into the lemma (§5), the carrier atom survives the folding **iff the block-induced alias mixing beats the proven gap**:

`ε_mix(b) < ½ g(b) ≈ 3.3×10^{-3} · u^4/b^2`   (nonvanishing weight),
`ε_mix(b) = o(u^4/b^2)`   (clean atom).

This is the sharp, **momentum-resolved** form of transfer-entry (TE) on the collapsing fiber. Consequences for the chain:

- The **fixed-contour TE** (`‖T̂_c − T_*‖ < d_*/4` with `d_*` fixed) is not the right target: the binding `d_* = g(b) → 0`. Replace it with the `ε_mix(b) = o(u^4/b^2)` condition and route through the shrinking-island Thm 3.4, not a fixed Riesz contour.
- The required inequality is a bound on the **off-diagonal** block-induced coupling, uniform along the trajectory — i.e. a **G17** (RG / Wilson free-energy / background-field stability) statement evaluated at scale `A`. This is the sole remaining hard input; H0 and the atom algebra are discharged.

---

## 7. What this changes in the ledger (proposed; not written — read-only)

- **H0**: downgrade from "first open model object" to "discharged at Gaussian order (this note); interacting version reduces to the `ε_mix` bound." H0 is not the barrier.
- **TE**: restate as `ε_mix(b) = o(u^4/b^2)` on the folded `p=0` fiber, feeding Matrix-KL Thm 3.4; retire the fixed-contour form.
- **Cross-links**: this ties G18's spectral bridge to G11 (the near-Γ / `L^{-2}` isolation, here `b^{-2}`) and to G17 (the only source of an `ε_mix` bound). It supplies the `diam(I_n)→0` input for Thm 3.4.

---

## 8. Honest scope and limitations

- **Gaussian order only.** §3 proves H0 and §5's atom algebra at leading order and identifies the required rate. Neither shows the *actual* interacting SU(3) `ε_mix(b)` satisfies `o(u^4/b^2)` — that is the G17-hard content, untouched here.
- **Coefficient vs power.** The `u^4` **power** is proven; the coefficient `6.69×10^{-3}` inherits the C2 dispute (it uses the historical `O(u^4)` branch). Do not promote the coefficient.
- **1D vs 3D dispersion.** `g(b)` used the `cos k` branch; the 3D isotropic cap band `Σ_i 2τ_4 cos k_i` has the same `u^4/b^2` leading rate. Anisotropic/cubic corrections change the constant, not the power.
- **Necessary vs sufficient.** The 2-level channel shows `o(u^4/b^2)` is *necessary*; the full-fiber lemma (all `b^d` channels) shows a matching *sufficient* condition `ε < g/2` with explicit weight `1−(2ε/g)^2`.
- **Sin-θ constant.** `‖Q−P‖ ≤ 2ε/g` is the standard bound; numerically it is conservative. The Lean formalization (§9) must either import a sin-θ theorem or supply the resolvent-contour proof; the `PQP ⪰ (1−‖P−Q‖^2)P` step is elementary.

---

## 9. Lean formalization target (next step)

The §5 lemma is pure finite-dimensional spectral linear algebra, suitable for Lean 4 / Mathlib:

- **Objects**: `H_0 H : Matrix (Fin n) (Fin n) ℂ` self-adjoint (or `𝓗` a finite-dim `InnerProductSpace ℂ`); spectral projections via `ContinuousFunctionalCalculus` / `cfc` indicator functions on the window `W`.
- **Hypotheses**: `spec H_0 ⊆ {m_0} ∪ [m_0+g, ∞)`, `‖H − H_0‖ ≤ ε`, `ε < g/2`, `range J ⊆ range P`, `J.adjoint * J ≻ 0`.
- **Conclusions**: (i) `‖Q − P‖ ≤ 2ε/g`; (ii) `(1 − (2ε/g)^2) • 1 ⪯ Z_W` in the Loewner order.
- **Lemma stack**: (a) window projection distance / sin-θ — the one piece that may need a self-contained resolvent-contour proof if Mathlib lacks Davis–Kahan; (b) `P(1−Q)P ⪯ ‖P−Q‖^2 • P` (projection algebra, elementary); (c) Loewner monotonicity under `G^{-1/2}(·)G^{-1/2}` congruence.
- **Payoff**: the failed/awkward step in (a) is exactly where the informal argument's constant matters; formalizing it pins the sin-θ constant used in the TE budget.

This upgrades the atom lemma to **T0**; it does not touch the `ε_mix` bound (which stays T3/open, = G17).

---

## 10. Status

- **Proved (this note, at Gaussian order)**: H0's uniform cross-Gram/frame lower bound onto the true fine `p=0` carrier (`λ_min/z_* = 1` for all `b,d` tested); the box map's exact suppression of non-carrier aliases; the folded-fiber atom lemma `λ_min(Z_W) ≥ 1−(2ε/g)^2`.
- **Proved (corpus, imported)**: exact `O(u^3)` carrier flatness from `B†ψ=0`; hence dispersion power `p=4`. Fiber gap `g(b) = (2861009/4219365150)u^4 sin^2(π/b)` (coefficient historical/C2-disputed; power proven).
- **Verified numerically**: the atom lemma on the full `b^3` fiber; the universal `ε/g` mechanism; the `g(b)·b^2/u^4 → 6.69×10^{-3}` rate.
- **Not supplied**: any bound on the interacting block-induced alias mixing `ε_mix(b)` — the `o(u^4/b^2)` requirement is a G17 statement and remains open.
- **Best honest claim**: H0 is not the barrier. The continuum carrier atom reduces, cleanly and quantitatively, to a single `o(u^4/b^2)` bound on block-induced alias mixing, routed through the shrinking-island Thm 3.4. Everything else on the carrier-visible branch is discharged.

---

## Appendix A. Reproduction

All scripts were run under `sympy`/`numpy`; the exact rational and the `1.000000` frame ratios are exact-arithmetic / machine-precision as marked. (Scripts held in the external scratchpad, not the clone.)

### A.1 H0 cross-Gram (`h0_free.py`) — core
```python
# alias labels s in {0..b-1}^d ; k_f^(s) = 2*pi*s/A, A=b ; box form factor kills s!=0
# per-origin carrier cross-Gram Gc = (1/b^d) sum_tau J^(tau)_{s=0} J^(tau)_{s=0}^H  ->  J0 J0^H
# report lambda_min(Gc)/z_*  ==> 1.000000 for all b (1D b<=64; 3D b<=4), box & smooth kernels
```

### A.2 Folded-fiber lemma (`h0_fulllemma.py`) — core
```python
D = kron(diag([m0 + c*u**2*q(k_f^(s)) for s in aliases]), eye(3))   # carrier at s=0
J = source supported on s=0 block, frame J^H J = z_* I3
V = random Hermitian, ||V||=eps ; H = D+V ; Q = spectral proj of H on [m0-g/2, m0+g/2]
Z = G^{-1/2} J^H Q J G^{-1/2} ; assert lambda_min(Z) >= 1-(2*eps/g)**2   # holds, conservatively
```

### A.3 Mechanism (`h0_mechanism.py`) — 2-level dominant channel
```python
H = [[m0, eps],[eps, m0+g]] ; source on s=0 ; weight = |<eigvec, e0>|^2 (max)
# weight = universal f(eps/g): 0.990 (0.1), 0.724 (1.0), 0.582 (3.0), ->0.5 (large); same for all b
```

### A.4 Exact gap rate (`sympy`)
```python
coeff = Rational(2861009, 8438730300)          # corpus O(u^4) cos-k dispersion coefficient
g = coeff*u**4*(1 - cos(2*pi/b))               # = (2861009/4219365150) u^4 sin^2(pi/b)
limit(g*b**2/u**4, b, oo) = 2861009*pi**2/4219365150 = 0.006692245400461788
```

## Appendix B. Provenance (corpus anchors)

- `m_0 = 8/3`, `m_-(u)=8/3+u+(11/306)u^2-(109151/249696)u^3+O(u^4)`: `theory/superseded/MASTER_THEORY.md` line 167; `theory/MASTER_THEORY_UNIFIED_2026-08-20_v4_3.md`.
- `q_a = C_2(fund) = 4/3`; spectrum `{-4,-4+q_a,-4+q_a}`; carrier `ψ=(d̄_3,-d̄_2,d̄_1)`: `v4_3` lines ~360, 1784; `FRONTIER.md` U1; `src/workhouse/constants.py`.
- Exact `O(u^3)` flatness from `B(k)†ψ(k)=0`: `v4_3` line 78.
- Exact `O(u^4)` dispersion `−(2861009/8438730300)u^4 cos k`; `2τ_4 cos k` cap band: `theory/GLUEBALL_SOURCE_CONSOLIDATION_GUIDE_2026-08-20_v4_3.md` lines 317, 119.
- `O(u^2|k|^2)` inter-branch separation = G11: `v4_3` line 887; `MASTER_THEORY.md` line 386.
- H0 / TE / SE / shrinking island / Thm 3.4 / z_* / M_* / d_*: uploaded audits `WORKHOUSE_FIXED_TO_CONTINUUM_MASTER_CHAIN`, `WORKHOUSE_UNIFORM_CARRIER_RESIDUE_H3_AUDIT`, `WORKHOUSE_MATRIX_KL_CARRIER_ATOM_THEOREM`, `WORKHOUSE_CARRIER4_PART_VI_AUDIT` (2026-08-22).
- G17 / G18 / G19 (load-bearing spectral-bridge / free-energy / continuum debts): `ledger/gaps.yaml`; `FRONTIER.md` §5, §7.
