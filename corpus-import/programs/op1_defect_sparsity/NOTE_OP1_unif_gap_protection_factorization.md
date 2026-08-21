# UNIF: Gap Protection by Factorization — a Cross-Program Theme

**Date:** June 11, 2026
**Status:** Idea/theme note (no new results claimed; descriptive synthesis only)
**Sources:** One-plaquette program robustness theorem (`ORGANIZED/12_ONE_PLAQUETTE/`, master doc §8.6 and theory paper Theorem 5.1/"Link-mediated robustness"); P14 (RG flow stability); P09/MaxwellOperator.lean (vacuum Hessian = d₁*d₁); OP-11 (RG blocking diagnostics); P08 (charge sectors)
**Related:** `ORGANIZED/00_META/ONE_PLAQUETTE_PROGRAM_CONNECTIONS.md` §4.3, `CLAUDE_REVIEW/10_DOC_GOV_open_problems.md` OP-14

---

## 1. The observation

The workspace now contains two distinct mechanisms by which a spectral quantity survives corrections, and they are structurally different in an instructive way.

**Quantitative protection (core project, P14).** The Projected Bochner-Hessian flow argument makes the gap persist under RG flow *if* the anomaly source stays uniformly positive and geometric corrections decay like the running coupling squared. Protection is an inequality race: positive drift versus bounded corrections, with CONJ_B as the unproven positivity input.

**Structural protection (one-plaquette program, §8.6).** The flat T₁⁺⁻ band survives corrections *identically* — not because corrections are small, but because of an algebraic factorization. The effective hopping satisfies Ñ(k) + 4I = B(k)B(k)† with B the plaquette→link boundary symbol, so the band is exactly ker B†. The program's robustness theorem then states: any correction whose symbol factors through the link channel, H_corr = B M B† with M arbitrary Hermitian, annihilates the flat subspace — exact flatness at every link-mediated order, with no smallness assumption on M whatsoever. The mechanism is the chain-complex identity ∂∘∂ = 0 (closed surfaces have zero net signed amplitude into every link — an emergent lattice Gauss law at the effective-Hamiltonian level). Its sharpness theorem marks the boundary: site-mediated (corner-sharing) symbols escape the factorization and can break the protection, which is why the program's O(y⁴) question is open and pre-registered.

The contrast: P14-style protection needs the corrections controlled; factorization-style protection needs the corrections *structured*. Where the second applies, the first's hardest hypothesis (uniform positivity against arbitrary corrections) is unnecessary for the protected subspace.

## 2. Why this is not foreign to the core project

The factorizing operator is already a core-project object. P09/MaxwellOperator.lean establish ∇²S_W(vac) = (β/nλ_ρ)·d₁*d₁ — the same boundary/incidence structure (one dimension up the chain complex: d₁ is plaquette-coboundary on links; B is cube-boundary onto plaquettes in Bloch form). The Hodge decomposition, coexact projectors, and ker/im structure of d₀, d₁ are load-bearing throughout the defect program (OP-1's M = m²I + α·d₁*d₁, Hodge-projected θ_phys) and the blocking diagnostics (OP-11's "pushforward the fine-scale coexact projector vs recompute on the blocked lattice"). The one-plaquette result can be read as: at strong coupling, on the smallest nontrivial system, the *effective* Hamiltonian inherits an exact chain-complex factorization from the gauge theory's own incidence geometry, and that inheritance is what pins part of the spectrum.

## 3. Questions this suggests (open, unworked)

1. **Factorized remainders in the PBH flow.** In P14's correction terms, is there a part that provably factors through d₁ (or a blocked descendant of it)? Any such part cannot move spectral data supported on the corresponding kernel, and would shrink the burden carried by the positivity hypothesis to the non-factorizing remainder only. The one-plaquette sharpness theorem suggests the right split to look for: link-mediated (factorizing, harmless) versus site-mediated (potentially gap-moving).
2. **Protection as a commutator criterion along RG flow.** The program reduced its O(y⁴) frontier to one falsifiable condition: u†H₄P_⊥ ≡ 0, equivalently [H₄, P_flat] = 0 — a finite system of exact rational linear conditions on computable weights. The analogous diagnostic for RG blocking is computable: test whether [H_eff(t), P] ≈ 0 for the relevant projector P along the blocking trajectory. This is essentially OP-11's projector-consistency diagnostic, restated as a protection criterion with a binary outcome — the "pre-registered criterion" pattern is exportable even where the algebra is not.
3. **Emergent Gauss laws under coarse-graining.** The flat band is a Gauss law that *emerges* in degenerate perturbation theory, distinct from the microscopic gauge constraint. If blocked effective Hamiltonians retain a B M B† form (even approximately), kernel-pinned spectral features would be RG-robust for structural reasons. Whether any such form survives blocking is checkable on small lattices with existing tooling (OP-11/OP-12 infrastructure).
4. **Sector bookkeeping.** The protected band lives entirely in the C-odd sector (P08's ℋ⁻; protection uses ⟨odd|W|0⟩ = 0). Any attempt to transplant the mechanism should track which sector the candidate protected subspace occupies — P08 already supplies the decomposition.

## 4. Caveats

The one-plaquette results are strong-coupling lattice statements about an effective one-flux Hamiltonian; nothing here asserts they transfer to the PBH flow, the continuum, or the mass gap. The flat band is also not the gap: it is an excited band whose *dispersion* is protected, while the core project's object is the gap above the vacuum. The transferable content is the proof pattern (factor → kernel → corrections that respect the factorization are inert → sharp boundary where they don't), not any constant. This note exists to keep that pattern visible next to P14 and OP-11, where it may be useful.

---

*Compiled June 11, 2026 alongside the 12_ONE_PLAQUETTE deposit. See `00_META/ONE_PLAQUETTE_PROGRAM_CONNECTIONS.md` for the full connection map.*
