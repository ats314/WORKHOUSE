# Continuum Wilson block evidence, 5 September 2026

This run records the native exact finite controls, original independent algebra, and four saved untruncated SU(2) rotor enclosures. The complete analytic block, oscillator-remainder, OS-intertwining and conditional scale statements are the separately pinned proof sources. This is not a continuum Yang-Mills certificate.

Run from the repository environment:

```text
python -B runs/continuum_wilson_block_2026-09-05/replay_frozen.py
```

The replay rejects optimization, verifies the entire manifest before and after, loads the copied native modules through an empty fake package rather than the installed workhouse package, compares their exact payloads to certificate.json, reruns all six pinned invariant checks and matches the embedded rotor certificates, recomputes three original independent control payloads without rewriting them, and replays the four saved rotor enclosures by integer signs. The original Sturm recurrence is AST-loaded with only Fraction and math globals; the original replay main retains its source hashes and corrupted-interval check. NumPy and SciPy imports are deliberately blocked, and the eigensolver proposal path is disabled. The original numerical-generation scripts remain unchanged. No bytecode caches are written.

Every runner SOURCES path is mirrored under source/. Original scripts and JSON records remain byte-for-byte copies at the top level; original research drafts are under original_drafts/. proof_provenance.json distinguishes those drafts from the canonical proof bytes. Source changes require a new run rather than editing this record. The original generation scripts may refuse existing JSON or write reports; use replay_frozen.py for a read-only replay.
