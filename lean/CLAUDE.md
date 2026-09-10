# Lean working agreement

Apply the repository [working agreement](../CLAUDE.md) and the
[formalization workflow](../docs/formalization_workflow.md). The rules here
concern proof scope and its integration; the generated
[proof map](../docs/derivation_formalization.md) records current coverage.

## Mathematical scope

Formalize the research statement at its natural level: algebra, geometry,
probability measures, Hilbert/Banach operators, domains, closed forms,
limits, spectral projections, and reconstruction when required. The
maintainer's formalization request includes full analytic statements.

Construct the actual objects required by the source. Explicit hypotheses may
be the source's stated inputs, but must not hide the conclusion or substitute
a finite/scalar surrogate for an infinite operator theorem. A useful supporting
lemma can be integrated with its narrow scope while the larger theorem remains
open to formalization. Accept valid proofs under their precise assumptions;
novelty is not a reason to weaken or reject them.

## Proof and source boundaries

- No `sorry`, `admit`, or new axioms that replace a proof. Strict builds use
  `lake build --wfail`; dependency export also audits transitive axioms.
- State domain, integrability, positivity, completeness, normalization, and
  parameter-uniformity hypotheses wherever the argument uses them. Preserve
  the source's physical time and operator identifications.
- Register every theorem, including helpers, in `ledger/theorems.yaml`.
  Give derivation proofs exact `proof_sources` and matching whole or scoped
  links in `ledger/derivation_statements.yaml`.
- `lean`/`formalizes` describe whole statements; `lean_support`/`supported_by`
  describe named ingredients. `promotes` requires the entire named check,
  alone or jointly with its other registered proofs.
- Keep analytic status, evidence level, and machine-verification tier distinct.
  T3 does not imply that a valid analytic proof is false or unproved.
- Preserve received proofs, failed attempts, and sealed runs. Record corrections
  and successor statements with provenance; do not change a source digest to
  conceal a disagreement or label old evidence as a new run.

## Integration

Import new modules in `Workhouse.lean`, compile strictly, then run the kernel
export from the repository Python environment. Regenerate the proof map before
catalogue/frontier/certified views, and inspect `workhouse why` for both the
source statement and each affected proof. The workflow gives exact commands
and checks. Serialize full builds/exports when agents share a checkout.

Equivalent reformulations are welcome when the equivalence is justified.
For example, denominator-cleared polynomial identities must retain the
conditions needed when interpreting them as rational formulas. Tactic
convenience does not authorize dropping a mathematical obligation.
