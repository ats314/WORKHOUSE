# Exact activities for the dressed Wilson transfer

This additive run records the analytic partition extraction in
`paper/research_notes/G18_WILSON_ACTIVITY_EXTRACTION_20260905.md` and
independently executed rational tensor controls. It continues the pinned
creator-parent theorem; the parent proof and run remain unchanged.

The induced dressed transfers use one coupling path and spectral filter,
with each subsystem's own Perron normalization and unitary. Partition
Möbius inversion constructs the unique activities with zero singleton
activity, exact disjoint-support reconstruction, self-adjointness, and both
local vacuum annihilation legs. Component factorization of the common-filter
flow makes disconnected activities vanish at the actual real coupling.

The basic uniform norm `sup_i sum_(X contains i)(5/4)^|X| ||F_X||<=1/400`
remains open. A stronger cardinality margin would also supply extra spatial
activity decay. The source-transformation bound and complete excited
spectral identification remain separate. These exact finite controls do
not establish any of those norms for Wilson rotors.

## Executed controls

- `certificate.json`: two positive four-site binary models made from
  ordered, overlapping, noncommuting two-site projectors. Exact partition
  inversion is compared with a root-block recurrence using a separate
  tensor embedding: 32 subsystem reconstructions, 30 local vacuum checks,
  and 14 disconnected cancellations. The connected-chain full activity
  is nonzero, while the disconnected-pair full activity vanishes.
- `independent/`: a separate additive-family and disconnected-product
  implementation gives 24 subsystem reconstructions, 22 anchoring checks,
  nine disconnected cancellations, and a nonzero overlap commutator.
  The earlier ordered-model draft and exact output are preserved as well.
- The missing-factorization control uses positive vacuum-fixing
  `G_X=(I+sum_i q_i)^(-1)` on two disconnected links. Its mixed activity
  is exactly `diag(0,0,0,1/12)`: vacuum fixing alone does not imply the
  component cancellation.
- `source/` pins the canonical executed sources and proof. `derivation/`
  retains the independently reviewed argument and the next bounded
  calculation. No new Lean theorem is claimed by this run.

## Reproduce

```text
python scripts/verify_wilson_activity_extraction.py --output outputs/activity-replay.json
python -m pytest tests/test_wilson_activity_extraction.py
python -B runs/wilson_activity_extraction_2026-09-05/independent/check_transfer_activity_mobius.py
```

The canonical verifier rejects an existing output and disabled assertions.
`SHA256SUMS` pins every run file. The finite examples test the generic
operator extraction lemma; their two-site toy interactions are not the
four-link Wilson plaquette model.
