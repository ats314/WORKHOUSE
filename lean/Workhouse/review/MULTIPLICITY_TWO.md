# WORKHOUSE multiplicity-two rigor — `spec S(k) = {−4, −4+q_a, −4+q_a}` with multiplicities

Date: 2026-08-23
Status: T0 (machine-checked Lean 4 / Mathlib, no `sorry`, standard axioms only).
Scope: completes the spectrum of the signed incidence operator `S(k)` (U1) by proving the
`(−4+q_a)`-eigenspace is 2-dimensional, turning the eigenvalue **multiplicities** from a
remark into a theorem.
Repository status: read-only; this note is external to the WORKHOUSE clone. Nothing committed
or pushed. The Lean source is staged (uncommitted) at `lean/Workhouse/Spectrum.lean`.

---

## 0. What this closes

`incidence_gram` (`B(k)B(k)† = q_a·I − ψψ†`) plus `Smat_carrier_eigen` (`S(k)ψ = −4ψ`) and
`Smat_perp_eigen` (`ψ†v = 0 ⟹ S(k)v = (−4+q_a)v`) already exhibited **which** eigenvalues occur
and on **which** vectors. What remained a prose remark was the *multiplicity* count: that the
`(−4+q_a)`-eigenspace is exactly 2-dimensional (so the multiset is `{−4, −4+q_a, −4+q_a}`, not,
say, `{−4, −4+q_a}` with the second occurring once). This note makes that a theorem, via
`finrank_ℂ (ℂ ∙ ψ)ᗮ = 2` for the nonzero carrier.

---

## 1. The carrier is nonzero exactly off `Γ`

```lean
theorem carrier_ne_zero (d1 d2 d3 : ℂ) (h : d1 ≠ 0 ∨ d2 ≠ 0 ∨ d3 ≠ 0) :
    psi d1 d2 d3 ≠ 0
```

With `ψ(k) = (d̄₃, −d̄₂, d̄₁)` and `dᵢ = e^{ikᵢ} − 1`, the hypothesis `d1 ≠ 0 ∨ d2 ≠ 0 ∨ d3 ≠ 0`
is precisely **`k ≠ Γ`** (at `Γ` all `e^{ikᵢ} = 1`, so all `dᵢ = 0` and `ψ = 0`). The proof
reads off a nonzero component: if `dᵢ ≠ 0` then `star dᵢ ≠ 0` (`star_eq_zero`), and that is a
component of `ψ`, so `ψ ≠ 0`.

This is the Lean form of the corpus's own caveat (v4.3 §3.2): *"The normalized vector has no
continuous extension to `Γ`, where all three incidence branches meet."* The flat band is
singular exactly at `Γ`; away from it, the carrier is a genuine nonzero vector.

---

## 2. Multiplicity two

```lean
theorem orthogonal_finrank_two (ψ : EuclideanSpace ℂ (Fin 3)) (hψ : ψ ≠ 0) :
    Module.finrank ℂ (ℂ ∙ ψ)ᗮ = 2
```

A general fact: in `ℂ³`, the orthogonal complement of any nonzero vector has dimension 2.
Proof: `Submodule.finrank_orthogonal_span_singleton` gives `finrank (ℂ∙ψ)ᗮ = finrank E − 1`
under `Fact (finrank E = n+1)`; with `finrank_euclideanSpace_fin` (`finrank ℂ³ = 3 = 2+1`),
`n = 2`.

Specialized to the carrier:

```lean
theorem carrier_perp_finrank (d1 d2 d3 : ℂ) (h : d1 ≠ 0 ∨ d2 ≠ 0 ∨ d3 ≠ 0) :
    Module.finrank ℂ (ℂ ∙ ((EuclideanSpace.equiv (Fin 3) ℂ).symm (psi d1 d2 d3)))ᗮ = 2
```

For `k ≠ Γ`, the carrier's orthogonal complement is 2-dimensional. (`ψ` is transported from
`Fin 3 → ℂ` into `EuclideanSpace ℂ (Fin 3)` by the canonical identification; nonvanishing
transfers through it by injectivity.)

---

## 3. The spectrum, now with multiplicities

Assemble the three eigen-facts over `ℂ³` (all T0):

| Eigenvalue | Eigenspace | Dimension | Source |
|---|---|---|---|
| `−4` | `ℂ ∙ ψ` (carrier line) | 1 | `Smat_carrier_eigen` (`Sψ = −4ψ`), `carrier_ne_zero` (`ψ ≠ 0`) |
| `−4 + q_a` | `(ℂ ∙ ψ)ᗮ` | 2 | `Smat_perp_eigen` (`ψ†v=0 ⟹ Sv=(−4+q_a)v`), `carrier_perp_finrank` |

`1 + 2 = 3 = dim ℂ³`, and the two eigenspaces are orthogonal, so they exhaust the space:

$$\operatorname{spec} S(k) \;=\; \{\,-4,\; -4+q_a,\; -4+q_a\,\}\qquad (k \neq \Gamma),$$

with `−4` **simple** and `−4+q_a` of **multiplicity 2** — exactly the corpus's boxed spectrum
(v4.3 §3.2), now a machine-checked eigenspace decomposition rather than an assertion.

Equivalently for `B(k)B(k)† = q_a·I − ψψ†`: `spec = {0, q_a, q_a}` (`0` on the carrier,
`q_a` with multiplicity 2 on `ψ^⟂`); subtract `4I` for `S`.

---

## 4. Honest scope

- **`k ≠ Γ` is required and is exactly the right hypothesis.** At `Γ` the carrier degenerates
  (`ψ = 0`), the three branches meet, and the clean `1 + 2` split does not hold — the flat band
  is singular there. The theorem correctly excludes only that point.
- The result is proved over the **fixed-`k` fiber** (a `3×3` matrix identity). It is the
  homological/spectral structure at a momentum, not a statement about the interacting
  Hamiltonian or the continuum — those remain the two standing physics inputs (the `O(u³)`
  factorized *form* of `H_eff`, and the `ε_mix = o(u⁴/b²)` bound / G17), unchanged by this note.
- "Multiplicity 2" here means `finrank` of the eigenspace = 2. Combined with orthogonality and
  `dim = 3`, this is the full eigenvalue multiset; no separate diagonalizability argument is
  needed because self-adjoint `S(k)` is diagonalizable and the two orthogonal eigenspaces
  already sum to the whole space.

---

## 5. Verification

- Builds against `leanprover/lean4:v4.34.0-rc1` + repo-pinned Mathlib (identical
  `lean-toolchain` / `lakefile.toml` / `lake-manifest.json`).
- `#print axioms` on `carrier_ne_zero`, `orthogonal_finrank_two`, `carrier_perp_finrank`:
  each depends only on `[propext, Classical.choice, Quot.sound]` — no `sorryAx`.
- Source: `lean/Workhouse/Spectrum.lean` (staged, uncommitted), which imports
  `Workhouse.Incidence` for `Bmat`, `psi`, `qa`, `Smat`, `incidence_gram`, `Smat_carrier_eigen`.

## 6. Provenance (corpus anchors)

- `B(k)`, `ψ(k) = (d̄₃,−d̄₂,d̄₁)`, `S(k)+4I = B(k)B(k)†`, `spec S = {−4,−4+q_a,−4+q_a}`,
  singularity of the normalized carrier at `Γ`: `theory/MASTER_THEORY_UNIFIED_2026-08-20_v4_3.md`
  §3.2 (lines ~358–402).
- `dᵢ = e^{ikᵢ} − 1`, `q_a = Σ|dᵢ|²`: same document §2.5.
- "Incidence factorization, spectrum, Betti count — Proven; analytic; 14/14 cold topology
  gates": same document, results table.
