# F008 — Lean layer audit (#14)

**Date:** June 12, 2026. **Read:** inventory + census of all 73 modules in `05_LEAN/synthesis10_source/` + full/statement-level reads of the load-bearing ones (RiccatiFixedPoint, HaarMassCoeff, CombesThomas, LogSobolev, LatticeGap; AnomalySource/CarreDuChamp axiom status per inventory). Active build env at `proof/lean/` not rebuilt this pass.

## Census

73 files, 6,315 lines (avg ~86/module). **Zero `sorry` anywhere.** 4 axiom lines (the inventory's CarreDuChamp/AnomalySource caveat). 3 modules use `native_decide` (HOTRGMethods, HypercubicLattice, SixJSymmetry). No build errors on record (20 modules compiled in the cached env per archive docs).

## The honest characterization

The modules are **real, correct, zero-sorry Lean proofs — of scalar shadows of the chain's claims.** Examples, precisely:

| Module | Header claims | Actually proves |
|---|---|---|
| RiccatiFixedPoint | "stable fixed point of dλ/dt = σ−2λ²" | σ − 2(√(σ/2))² = 0 and uniqueness of the positive root — *algebra about ℝ, no ODE, no stability* |
| HaarMassCoeff / LatticeGap | Haar mass mechanism | c₀(N) = (N²−1)/2N evaluations (3/4, 4/3), positivity, and `mass_gap_positive`: c₀>0 ∧ a>0 ⇒ c₀a²>0 — *arithmetic* |
| CombesThomas | CT decay | positivity/monotonicity of the *formula* C·e^{−ηd} as a real function — *no operators, no kernel, no theorem about M⁻¹* |
| LogSobolev | LSI | facts about the scalar 2/ρ and e^{−ρt} decay — *no measure, no entropy functional* |

This matches the project's own honest "**~8.8% claim closure**" figure — the inventory never overclaimed. Verdict in the good-stuff/slop frame: **not slop — disciplined, compiling micro-mathematics — but interface-level**: the Lean layer currently certifies the *constants and inequality shapes* the chain uses, not the chain's operator/measure content. No formalized statement today would constrain a wrong proof of the actual theorems.

## Consequence: M5 is a qualitative upgrade, not polish

The M2 exact-kernel certificate is **finite rational linear algebra on concrete data** (kernel tables + defect sets → cert(D)² = ΣG² < 1). Formalizing *that* would be the first Lean artifact in the corpus that carries real load — a machine-checked statement about the actual comparator on an actual lattice, in `native_decide`/`norm_num` reach. Same character as OP-14 (domino/flat-band). Recommended M5 design: (i) kernel table as rational data with a provenance hash; (ii) theorem: for the recorded D, cert < 1; (iii) meta-theorem: cert ≥ θ via the HS inequality stated abstractly. Steps (i)–(ii) are mechanical; (iii) is the first genuinely mathematical Lean target.

## Actionables
- M5 scope rewritten as above (STATE row updated).
- Unit #14's claim-closure audit per-module table: deferred to the M5 session (it will produce one as a by-product).
- The 3 `native_decide` modules should be re-verified in the active build when M5 runs (known axiom-of-trust caveat).
