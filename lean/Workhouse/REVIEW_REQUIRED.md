# ⚠ REVIEW REQUIRED — Fable, next real session (DO NOT MERGE)

This branch (`claude/arxiv-corpus-review-7lx1lj`) contains an **unreviewed** Lean 4 / Mathlib
formalization of the SU(N) flux-band carrier→continuum chain, authored in an
arXiv-corpus-review session. It is committed for persistence only.

**Action required:** on the next real launch, **Fable** must review this before it is merged,
cited, or used downstream. Until then treat every theorem here as *machine-checked but
un-audited by a second party*.

## What is here (all build clean, no `sorry`)

`lean/Workhouse/{AtomLemma, FiberGap, Flatness, CarrierAtomGap, Incidence, Spectrum}.lean`,
imported from `lean/Workhouse.lean` (alongside the pre-existing `Basic.lean`).

Certifies (T0): the U1 incidence factorization `B B† = q_a·I − ψψ†` and `S+4I = B B†`; the
carrier kernel `B†ψ=0`; `spec S = {−4, −4+q_a, −4+q_a}` with multiplicities (−4 simple,
−4+q_a mult 2, for k≠Γ); `q_a = Σ 4sin²(kᵢ/2)`; homological flatness (`B†ψ=0 ⇒` k-independent
eigenvalue); the exact fiber gap `g(b)=(2861009/4219365150)u⁴sin²(π/b)` and `g(b) ∼ c·u⁴/b²`;
the carrier-atom window bound `≥ 1−(2ε/g)²`; the `o(u⁴/b²)` clean-atom rule.

## What is NOT proved (still T3 — physics inputs)

1. The `O(u³)` factorized *form* `H_eff⁻ = E_flat·I + t·B B† + O(u⁴)` (taken as hypothesis).
2. The interacting `ε_mix = o(u⁴/b²)` bound = **G17** (the real spectral bridge).

Also: the `u⁴` *power* is proven, but the `O(u⁴)` *coefficient* `2861009/8438730300` is the
historical branch and inherits the **C2** dispute.

## Verify

```
cd lean && lake exe cache get && lake build      # clean, no sorry
# axioms: #print axioms on each theorem → [propext, Classical.choice, Quot.sound]
```
Built against `leanprover/lean4:v4.34.0-rc1` + repo-pinned Mathlib.

## Review context (in `lean/Workhouse/review/`)

- `KEY_DERIVATIONS.md` — every derivation with steps and verification tags.
- `T0_T3_BOUNDARY.md` — what the Lean layer certifies vs the two physics inputs.
- `H0_FREE_CARRIER_AUDIT.md` — the H0 / isolation-collapse analysis.
- `MULTIPLICITY_TWO.md` — the spectrum multiplicity rigor.

## Reviewer checklist (Fable)

- [ ] Re-run `lake build` + `#print axioms`; confirm no `sorry`, standard axioms only.
- [ ] Confirm the Lean statements faithfully match the corpus objects (v4.3 §3.2 `B(k)`, `ψ`,
      `S`, `q_a`); flag any transcription drift as a `FINDING:`.
- [ ] Confirm the C2-disputed coefficient is only ever an input, never promoted.
- [ ] Decide placement/naming in the ledger; decide whether to keep the `review/` docs in-tree.
- [ ] Do NOT merge to the default branch without maintainer (Alex) sign-off.
