# A gapped creator parent and the actual Wilson vacuum transport

This run supports the analytic proof in
`paper/research_notes/G18_WILSON_CREATOR_PARENT_AND_SPECTRAL_FLOW_20260905.md`.
It began from verified GitHub main `ac39704568b09ae3613e3f5b099466ea3c0fa545`.
The rooted contraction and analytic coefficient-limit theorems were already
established inputs.

Magnetic half-flow restores the actual symmetric creators with rooted norm
at most `1/8`. Their exact parent has unique Wilson vacuum and gap at least
`247/256`. Connected Taylor witnesses yield spatial and derivative bounds
on `|u|<=u_star/8`; the proof checks the infinite-dimensional-site NSY
spectral-flow hypotheses and supplies the intrinsic-metric periodic-volume
comparison. The selected full bounded-local-observable state is pure and
locally normal, with a quasi-local vacuum automorphism and a gapped GNS parent.

This is an auxiliary parent and a vacuum transport. The actual Wilson
transfer/source activity estimate and complete excited spectral identification
remain separate mathematical tasks. The parent excitation energies are not
identified with Wilson excitation energies.

## Evidence and scope

- `certificate.json` records the native finite controls, six exact tensor
  models, 81 rational PSD congruence certificates, independent reconstruction,
  exact scalar constants, negative controls, and executed-source hashes.
  These finite controls do not prove the arbitrary-dimensional analytic theorem.
- `independent/` preserves the independently developed rational verifier,
  matrix reconstruction/replayer, certificate and execution logs. Replay
  rejects an altered factorization. Cases include overlapping creators,
  entangled ternary vectors, mixed link dimensions, and a multibody family
  inside the theorem's rooted ball. Omitting the quadratic term destroys
  positivity and vacuum annihilation. A disjoint tensor family proves that
  small rooted norm alone cannot bound the global similarity uniformly.
- `derivations/` preserves independent analytic gap, actual-creator/GNS,
  and primary-source spectral-flow audits. Their draft wording reflects
  their individual scopes; the complete current theorem is the pinned note.
- `lean/` records strict compilation of six modules, 100 theorems, no
  `sorry`, and standard-axiom guards. The three new lemmas certify the
  two star-ring identities and the real scalar gap specialization. They
  do not formalize operator norms, spectral calculus, or infinite volume.
- `source/` preserves executed canonical sources and the final proof.
  `SHA256SUMS` pins every run file. All earlier sealed runs and notes retain
  their original bytes and conclusions at their historical stage.

## Reproduce

Use the ordinary project environment and fresh outputs:

```text
python -m pip install -e ".[dev]"
python scripts/verify_wilson_creator_parent.py --output outputs/parent-replay.json
python -m pytest tests/test_wilson_creator_parent.py
make lean
```

An independently implemented certificate replay is also preserved:

```text
python runs/wilson_creator_parent_2026-09-05/independent/replay_parent_certificate.py --certificate runs/wilson_creator_parent_2026-09-05/independent/finite_certificate_final.json --source runs/wilson_creator_parent_2026-09-05/independent/verify_creator_parent.py --output outputs/parent-independent-replay.json
```

The local Lean driver records this machine's read-only mathlib cache and
compiler; `make lean` is the portable build entry point. The source proof
cites arXiv:1810.02428v2 with exact theorem locators. No external paper is
redistributed and no finite-spin thermodynamic theorem is silently applied
to infinite-dimensional rotors.
