# Glueball Band Structure at O(y²): Exact Dispersions, an Exactly Flat C-Odd Band, and Closure of the Signed Band Problem

**Companion result to:** *Two-Sided Spectral Control of Wilson One-Plaquette Class Gaps and an Exactly Verified Strong-Coupling Bridge to the SU(3) Glueball Channels* (draft June 11, 2026).

**Version 2 (June 11, late).** This edition applies the §8.2 hopping correction (t₊ = −481/612 + 3/4 = −11/306, the vacuum-route-inclusive hop) to every C-even quantity, per master-document §6.11. Changed: A₁⁺⁺ bottom, band top, curvature, effective mass, bandwidth, per-bond and manifold-width ratios. Unchanged: the entire C-odd sector (flat-band theorem, 11/306, incidence factorization), E⁺⁺ = 223/1020 (t-independent at λ = 0), quantum numbers, and the structural lemmas. The §7 caveat on O(y³) is superseded: flatness is now certified through third order (rigid shift d₃ = −109151/249696).

**Certificate:** `ENGINE_FLUX_glueball_band_certificate_v2.py` — 36 hard gates, all passing (the original 29 minus the as-written A₁⁺⁺ pin, plus eight corrected-value gates including an as-written provenance gate and a six-field cross-check against RUN_TROM_d3_results.json) (symbolic identities in sympy, exact rationals via `fractions.Fraction`, finite-lattice cross-checks at L=4, gauge-invariance and frustration checks, dense 40³ Brillouin-zone scan).

---

## 1. What this computes

The paper's Theorems 6.2–6.3 assemble the O(y²) glueball masses at the uniform (k=0) projection and leave one problem open: the C-odd assembly is a **signed hopping problem** on the plaquette shared-link adjacency graph, with hopping `t⁻(s) = 5s/612` depending on the relative shared-link orientation `s = ±1`. The paper bounds the C-odd y² coefficient to the interval **[−3/102, 17/102]** and stops.

This note solves the band problem in both charge sectors. Plaquettes of the cubic lattice come in three orientations (xy, xz, yz), so the one-excitation effective Hamiltonian at O(y²) is a 3×3 Bloch problem at each k. In units of y², with the paper's exact constants (per-neighbor self-energy −481/612, vacuum subtraction +3/4, within-plaquette pieces 13/20 and 1/2 from the Bridge Theorem; hopping t₊ = −11/306 per §8.2 — as-written −481/612):

```
E₊(k) = 13/20 − 22/51 − (11/306)·λ(k),   λ(k) ∈ spec A(k)   (C-even)
E₋(k) = 1/2  − 22/51 + (5/612)·μ(k),      μ(k) ∈ spec S(k)   (C-odd)
```

`A(k)` and `S(k)` are the unsigned and signed 3×3 Bloch matrices of the shared-link adjacency (12-regular; signs from the relative orientation table, derived from first principles out of the oriented boundary chains and gate-checked for translation invariance).

The signed graph is **genuinely frustrated**: triangles of plaquettes meeting at a corner carry sign product −1 (gate), while same-link triangles carry +1. So no gauge of plaquette orientations trivializes the signs — this is exactly why the paper's uniform projection was "not automatic" for C-odd, and why the problem had to be solved as a band structure.

## 2. The incidence factorization (the structural lemma)

Let `N(k)` and `Ñ(k)` be the 3×3 (orbital × link-direction) Bloch incidence matrices built from the unsigned / signed plaquette boundary chains. With `u_j = 1 − e^{ik_j}`, `v_j = 1 + e^{ik_j}`:

```
A(k) + 4·I = N(k) N(k)†          det N(k) = −2 v₁v₂v₃
S(k) + 4·I = Ñ(k) Ñ(k)†          det Ñ(k) ≡ 0
```

(both identities verified symbolically). Consequences:

- Both spectra are bounded below by −4 at every k (positive semidefiniteness), and the C-even spectrum is bounded above by 12 (12-regular graph). So `λ(k) ∈ [−4, 12]`, `μ(k) ∈ [−4, 8]` (upper C-odd value from the scan + exact diagonalization at the maximizer).
- `det Ñ ≡ 0` means `Ñ†` has a kernel **at every k**: the C-odd spectrum contains the eigenvalue −4 at every momentum.

## 3. Main result: an exactly flat C-odd band; the open interval closes

**Theorem (flat band).** The lowest C-odd branch is exactly flat at O(y²):

```
μ_flat(k) ≡ −4  for all k,   eigenvector  w(k) = ( ū₃, −ū₂, ū₁ )
```

so the C-odd one-plaquette excitation energy is **momentum-independent at this order**:

```
m₋(k, y) = 8/3 + y + (11/306) y² + O(y³)     for every k.
```

The exact coefficient is **11/306 = 7/102 − 20/612 ≈ +0.035948**, inside (and now replacing) the paper's open interval [−3/102, 17/102] from Theorem 6.3. The diagonal-only value 7/102 receives a band shift of exactly −5·4/612.

**Mechanism (∂∂ = 0).** `Ñ` is the signed face→edge boundary operator in Bloch form. Its left kernel is spanned by closed 2-chains, and the elementary closed 2-chains are the boundaries of unit cubes: a ±1 signing of the six faces of an elementary cube whose oriented boundary is link-free (found by exhaustive search over 2⁶ signings; gate). Each such cube 2-chain is an **exact, compactly localized eigenstate** of the finite-lattice signed adjacency at eigenvalue −4 (gate, machine precision). On an L³ torus the −4 eigenspace has dimension **L³ + 2** (L³ cube states + the two dispersive branches touching at k=0; gate at L=4: 66 = 64 + 2). The flatness of the lowest C-odd glueball band is the band-theory shadow of ∂₂∂₃ = 0.

**Physics statement.** The paper's Remark 6.4 framed near-immobility through the per-bond ratio |t⁻|/|t⁺| = 5/481 ≈ 1/96; with the §8.2-corrected hop the ratio is |t⁻|/|t⁺| = (5/612)/(11/306) = **5/22 ≈ 0.23**, so the ratio no longer carries the immobility claim. The claim survives in a stronger form: *the lowest C-odd branch is exactly dispersionless at O(y²)* — bandwidth 0, infinite effective mass at this order — while the full C-odd three-branch manifold has total width (5/612)·12 = **5/51 ≈ 0.098** in y² units, versus the corrected C-even bandwidth (11/306)·16 = **88/153 ≈ 0.575** (manifold-width ratio (5/51)/(88/153) = 15/88 ≈ 0.17).

## 4. Complete O(y²) band data (all exact)

**C-even** (`λ ∈ [−4, 12]`, no flat band since det N ≠ 0):

| object | value |
|---|---|
| A₁⁺⁺ band bottom (k=0, λ=12) | m₊ = 8/3 − y − (217/1020) y²  *(§8.2-corrected; the as-written −9397/1020 is retained as a provenance gate)* |
| E⁺⁺ doublet (k=0, λ=0) | 8/3 − y + (223/1020) y²  **(new)** |
| band top (λ=−4, on the planes k_j=π) | 8/3 − y + (1109/3060) y² |
| dispersion at the bottom | λ_{A₁}(k) = 12 − (4/3)|k|² + O(k⁴), isotropic ⇒ E₊(k) ≈ m₊ + (22/459)|k|² y² |
| effective mass | m* = 459/(44 y²) |
| bandwidth | (11/306)·16 = 88/153 ≈ 0.575 (y² units) |

**C-odd** (`μ ∈ [−4, 8]`):

| object | value |
|---|---|
| flat band (all k) | m₋ = 8/3 + y + (11/306) y²  **(new; closes Thm 6.3's open problem)** |
| dispersive branches near k=0 | μ = −4 + |k|² + O(k³), doubly degenerate (char poly −μ̂(μ̂−|k|²)² exactly) ⇒ curvature (5/612)|k|² y² |
| band top | μ = 8 at k = (π,π,π), multiplicity 2 (exact spec there: {−4, 8, 8}) ⇒ coefficient 41/306 |
| lowest-branch bandwidth | **0 (exact)** |
| full-manifold width | 5/51 ≈ 0.098 (y² units) |

All three C-odd branches touch −4 at k=0 (S(0) = −4·I, a gate), so the triple degeneracy at rest is exact at this order.

## 5. Quantum numbers at rest (cubic group, computed via Λ² of the vector rep)

- **C-even** k=0 triplet: characters (3, 0, 3, 1, 1) = **A₁ ⊕ E**, parity +. The A₁⁺⁺ (0⁺⁺) state sits at λ=12 (band bottom, the paper's object); the **E⁺⁺ doublet** (2⁺⁺-like) sits at λ=0 with exact coefficient 223/1020.
- **C-odd** k=0 triplet: characters (3, 0, −1, 1, −1) = **T₁**; plaquettes transform as 2-forms, so inversion acts as +1 ⇒ **T₁⁺⁻** (1⁺⁻-like, axial-vector). The inner product with A₁ is zero: **the C-odd one-plaquette sector contains no scalar at rest.** This refines the paper's "C-odd scalar channel" wording — the assembled mass 8/3 + y + (11/306)y² is the mass of the whole T₁⁺⁻ triplet (degenerate at this order), consistent with the standard strong-coupling expectation that the lightest C-odd glueball is the 1⁺⁻.

## 6. Verification design

36 gates, including: complex sanity (every link in exactly 4 plaquettes with signs +,+,−,−; 12 distinct neighbors per plaquette; unique shared link); translation invariance of the orbital-resolved sign table; Hermiticity; A(0)=4J and S(0)=−4I symbolically; union of Bloch spectra equals the full finite-lattice spectrum at L=4 (max deviation ~10⁻¹⁴, both sectors); C-odd spectrum invariant under random plaquette-orientation gauge flips; corner-triangle frustration −1, same-link triangle +1; both incidence factorizations as symbolic identities; det Ñ ≡ 0 and the explicit flat-band kernel vector; cube 2-chain existence, exact eigenvector property, and multiplicity L³+2; band extrema attained in a dense BZ scan with exact symbolic confirmation at (π,π,π); **the §8.2-corrected A₁⁺⁺ value −217/1020, with the as-written −9397/1020 retained as a provenance gate**; band top 1109/3060; E⁺⁺ t-independence; bandwidth 88/153; curvature 22/459; per-bond ratio 5/22; a six-field cross-check against RUN_TROM_d3_results.json's order-2 block; containment of 11/306 in the paper's interval; symbolic small-k expansions (12 − (4/3)|k|² and −μ̂(μ̂−|k|²)²); O_h character computations.

## 7. Caveats and scope

- **Order.** Flatness is exact at O(y²) — and, as of the June 11 O(y³) program, certified through O(y³): every tromino weight vanishes at third order (bare-link lemma), the signed-adjacency structure is retained, and the band shifts rigidly by d₃ y³ = −(109151/249696) y³ (ENGINE_FLUX_su3_domino_d3.py, ENGINE_TROM_tromino_contract_independent_check.py). The open frontier is O(y⁴), where trominoes first activate.
- **Basis.** These are the bands of single-plaquette flux states — the complete degenerate manifold at this order; multi-plaquette states enter the masses only at higher order under the paper's (provable-at-this-order) linked-cluster assumption.
- **Finite clusters.** The domino numbers of the paper's §7 use honest finite-system vacuum-path bookkeeping and are not directly the z=1 specialization of the infinite-volume band formulas; the consistency anchors between this note and the corrected program are the k=0 gates −217/1020 (A₁⁺⁺, §8.2) and the §7 domino levels {1769/3060, 13/20}, with −9397/1020 retained only as as-written provenance.

## 8. Suggested edits to the paper

1. Replace Theorem 6.3's interval [−3/102, 17/102] with the exact value **11/306** and add the flat-band theorem (incidence factorization + det Ñ ≡ 0 + cube 2-chains) as Theorem 6.3′.
2. Promote Remark 6.4 to the headline: *the lowest C-odd glueball branch is exactly flat at O(y²) (and through O(y³)); the C-even/C-odd manifold-width ratio is 88/153 : 5/51.* Replace the per-bond ratio 5/481 by the corrected 5/22 wherever quoted.
3. Relabel "C-odd scalar channel" → **T₁⁺⁻ (1⁺⁻-like) channel** throughout §6 and the abstract; note the C-even k=0 content A₁⁺⁺ ⊕ E⁺⁺ and quote the new E⁺⁺ coefficient 223/1020.
4. Add `ENGINE_FLUX_glueball_band_certificate_v2.py` to the Appendix A certificate list (v2 carries the §8.2-corrected constants; the original is superseded).
5. Optional figure: the three C-odd branches along Γ–X–M–R–Γ (flat line at 11/306 under two dispersive sheets) next to the C-even bands — the visual is the argument.
