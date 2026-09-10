# Yang-Mills source and theory map

This collection starts from Arthur Jaffe and Edward Witten's **Quantum Yang-Mills Theory**, the 14-page official Clay problem statement supplied by Alex. The attachment and the [official PDF](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf) have the same SHA-256:

`3558403ca14c11e382f73a09e548222708540bfdf478cf96aa11c52d43e23e09`

The collection covers all 50 numbered bibliography entries, splitting bundled publications into distinct works, and adds directly relevant later research. Acquisition records distinguish a downloaded source, a verified catalogue record, and an unresolved retrieval. A reference in the Clay document is a citation relationship; independent computations retain their own provenance.

## Why this document matters here

Page 12, section 6.6, explicitly places **curvature of the space of connections**, **quantum confinement despite classical flat directions**, and **changes of variables or duality** among possible mechanisms for a Yang-Mills gap. Its references [11], [43], and [44] connect these ideas to Feynman, Simon, and Singer. This gives the geometric research a precise external lineage and concrete comparison targets. Whether WORKHOUSE's particular operator realizes a mechanism is decided by its definitions and checks.

The most direct bridge to WORKHOUSE is the separation of several mathematical tasks:

| Clay passage | Mathematical task | Repository connection |
|---|---|---|
| pp. 5-6, sections 3-4 | A physical Hilbert space, local observables, covariance, positive energy, and an appropriate axiom system | G18, G23 |
| p. 6, section 4 | A nontrivial theory on R4 for every compact simple gauge group, with a finite positive excitation threshold | G19 and the rank scope of the spectral program |
| p. 6, section 5; pp. 7, 12 | Control of the volume limit and a gap with uniform constants | G17, G18, G19 |
| pp. 7-8, section 6.1 | Convergent approximations with quantitative bounds | G17 and the exact linked-cluster program |
| p. 11, section 6.5 | Reflection-positive Wilson regularization and gauge-invariant continuum expectations | G19, G23 |
| p. 12, section 6.6 | Curvature and quantum localization along classically flat directions | G20, G22, G23; G18 operator identification |

These are page-specific connections to the supplied text. Statements about what was unknown in the 2006 document are historical statements, not an adjudication of later work.

## Files and use

- [DERIVATION_PROGRAM.md](DERIVATION_PROGRAM.md) connects the sources to reconstructed proofs, exact checks, Lean lemmas, and the next mathematical interfaces. [The extraction index](extraction/README.md) locates every acquired PDF page.
- `theory_graph.yaml` contains the authored statement and dependency map. Every study node is a T3 reading or proposed implication; adding literature does not alter an existing Lean or Python certificate.
- [THEORY_MAP.md](THEORY_MAP.md) gives three readable diagrams of the construction target, geometric route, and constructive route. `seed.json` records the attachment-to-official-source identity check.
- `sources_01_25.json` and `sources_26_50.json` preserve the numbered bibliography and acquisition evidence, including bundled works and corrected metadata.
- `sources_related.json` and `source_babelon.json` record the additional geometric sources.
- `COVERAGE.md` and `references.bib` are generated from those records. Coverage reports exact counts and access limitations.
- `literature/index.yaml` is the native literature register. `index/claims.jsonl` and `index/graph.jsonl` are regenerated through the normal WORKHOUSE commands.
- Local reading copies are in `literature/inbox/JW_2006/`. The existing repository licence policy keeps copies without redistribution permission in that ignored directory. Source metadata, hashes, locators, and the authored analysis are versionable; explicitly redistributable copies can live in `literature/fulltext/`.

Example queries, from the repository root:

```text
workhouse why STUDY:YM:target
workhouse why STUDY:YM:orbit-curvature
workhouse why STUDY:YM:flat-directions
workhouse lit --for G23
workhouse why LIT:JW_2006
workhouse atlas
```

## Concrete research use

The curvature route should identify the metric, physical operator, measure, and domain before importing a gap estimate. The regulator and volume dependence of each constant must then be explicit. A bound for a local Hessian, a diffusion generator, a projected band, or a finite lattice remains useful at its stated scope; the graph makes the additional operator and limit identifications visible.

The constructive route can reuse the exact all-rank cluster coefficients as established inputs while addressing convergence, gauge-invariant expectations, and uniform control. The graph keeps that route connected to the actual existing G17-G19 records, including their completed checks and recorded dead routes.

The source map is a research instrument: it identifies which external result supplies a definition or method, which local result can feed it, and what calculation would establish the next implication. It does not use a historical statement of difficulty as a restriction on new mathematics.
