# Set aside the Synthesis10 Lean modules cited as formal support

Surface: `ledger/notes.yaml`, `reviews:`. Archive: `WORKHOUSE_FULL_2026-09-07`.
Verdict: `set-aside` — "reviewed, judged not load-bearing now", the register's
own vocabulary for exactly this case. Nothing is deleted; the files stay in the
archive and the reason stays on record.

Task record: [2026-09-11-synthesis10-lean-review.md](../../2026-09-11-synthesis10-lean-review.md).
Evidence: `graph-tasks/evidence/2026-09-11-synthesis10-lean-review/`.

## What this registers

Five synthesis documents dated 2026-09-11 cite 31 modules of the archived
`synthesis10` Lean 4 library as `Lean Support` for analytic Yang-Mills
statements. The modules exist, the theorem names exist, and the library
genuinely contains **0** `sorry`. The statements nevertheless do not formalize
what they are cited for, and three of them are tautologies:

```lean
-- DriftCertificates.lean:91  — cited for pairing-term coercivity
theorem pairing_coercivity (pairing c : ℝ) (h : pairing ≥ -c) : pairing ≥ -c := h

-- ReflectionPositivity.lean:40  — cited for OS reflection-positivity permanence
theorem rp_pushforward_preservation
    (μ_rp : Prop) (P_compatible : Prop) (h_rp : μ_rp) (h_compat : P_compatible)
    : μ_rp := h_rp

-- RicciCurvature.lean:54  — cited for the product Ricci floor
theorem product_ricci_bound (κ_G : ℝ) (n : ℕ) (v_sq : ℝ)
    (hκ : 0 < κ_G) (hv : 0 ≤ v_sq) : κ_G * v_sq ≤ κ_G * v_sq := by linarith
```

`rp_pushforward_preservation` takes reflection positivity as an uninterpreted
`Prop` and returns it; it would typecheck with any proposition substituted.

The whole-library basis for the other 28 entries, verified by grep across all
71 modules: **0** import `MeasureTheory`, `LieGroup`, `Topology`,
`ContinuousLinearMap` or `Integral`, so no module carries a measure, a Haar
metric, a curvature tensor or an operator. `SU(` and `Haar` occur in docstrings
and identifiers only. Proof bodies are 51 `by linarith`, 31 `by norm_num`,
16 `rfl`, and 17 that return a hypothesis unchanged.

One entry additionally records a numerical conflict: `RicciCurvature.lean:25`
defines `ricci_constant_su (N) : ℚ := N / 2`, contradicting the `κ_G = N/4` it
is cited to support (and `ricci_constant_su2 = 1` where `N/4` gives `1/2`).

## Scope, and what would refute this

- The verdict is about **formal coverage only**. It says nothing about whether
  the underlying analytic arguments are right. `M10` stays open, `G19` stays
  open, `SP20-SP24` stay conditional; this proposal does not touch them.
- No Lean was compiled. The claim is not "it fails to build" — it is that the
  statements do not quantify over the relevant objects. No `lakefile` sits
  beside the source, so this checkout holds no evidence of a build either way.
- Three modules were read in full; the other 28 rest on the structural facts
  above plus their own declaration forms. Each entry carries its reason so a
  reviewer can disagree file by file.
- Four modules that *do* use real `Matrix (Fin n) (Fin n)` types
  (`HOTRGMethods`, `IntegrableGauge`, `NonPlaceholder`, `MaxwellOperator`) are
  **not** among the 31 and are **not** set aside here.
- **Falsifier:** exhibit any one of the 31 whose statement quantifies over a
  Lie group, a measure, a Riemannian metric or an operator, rather than over
  scalars and uninterpreted `Prop`s — or show that a cited name proves the
  analytic statement attributed to it. That entry should then be withdrawn.

## Applied

Unlike a discovery-tool proposal, this one has been applied by hand in this
branch, which is the protocol's path to a ledger: 31 entries appended to
`ledger/notes.yaml` (append only; no existing entry altered).

Every digest was recomputed from the archive bytes and matched its
`notes/WORKHOUSE_FULL_2026-09-07.jsonl` inventory row: **31/31**.

Read-only validators after the edit:

- `workhouse.notes.validate()` — **0 problems**
- `workhouse status` — "Ledgers structurally sound."
- `results.load()` — ok; `derivation_statements._checked()` — ok

Isolation: briefings of `R2 C5 R14 G7` taken before and after the edit at the
same revision `0b667161` differ in exactly one input file, `ledger/notes.yaml`,
with byte-identical `targets`. No generated view was regenerated, because no
claim, symbol, gap or result changed.

## Checklist

| Item | Requirement | Done |
| --- | --- | --- |
| `hypotheses_compared` | The cited statement was compared with the Lean statement, not with its name. | yes — quoted in full above |
| `regime_stated` | Regime stated. | yes — finite Lean files; no lattice or continuum claim |
| `normalization_compared` | Normalizations compared explicitly. | yes — `N/2` in Lean vs `N/4` cited |
| `independence_of_origin_checked` | Copied prose distinguished from independent origin. | n/a — no relationship between sources is asserted |
| `falsifier_stated` | What would refute this is written down. | yes — above |
| `source_hashes_matched` | Every recorded hash matches the file bytes. | yes — 31/31 |
| `lean_compiled` | The library was built. | **no** — not attempted, and not claimed |
