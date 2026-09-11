# Review: universal-cellular-hodge-20260911

Reviewed 2026-09-11 by Codex in `C:/WORKHOUSE/REPO`, branch `workspace/main`,
base `7cf8a646521259a34a772d65c8740ef7597f0265`. Live `origin/main` matched
that base when inspected. The review covers the uncommitted Hodge package
identified by the user's pasted handoff.

**Verdict: changes required; no commit or push.** The verified algebra supplies
useful results, but the submitted physical-history resolution and whole-proof
coverage claims do not follow from the implemented checks. The source package
and scientific ledgers were left intact for correction; this review adds only
review records, reproductions, and logs.

## Established results retained

- Under the stated regular cellular sphere-boundary assumptions and unweighted
  incidence inner products, `L_up = psi psi^T`, `||psi||^2 = F`, `L_up Q = 0`,
  and `(L_tot)ff = p_f + 1` have valid direct analytic arguments. The native
  finite-cell controls reproduce their stated examples.
- The tetrahedral face-space identities `L_down = 4 Q`, `L_up = 4 P`, and
  `Comm(S4) = span(P,Q)` hold. An independent linear system using all sixteen
  matrix entries and all twenty-four permutations gives commutant dimension 2.
  Scalar compression follows for an operator commuting with this representation.
- The five new Lean lemmas compile in the strict full build. They establish
  their encoded rank-one projector, conditional duality, and scalar arithmetic
  statements; compilation does not identify physical tetrahedral histories.
- With the repository operator **`S = L_down - 4 I`**, the general master
  formula is recoverable: `L_down + U = q I` and `U^2 = q U` imply
  `S = (q-4)I-U` and `S^m = (q-4)^m I - Pi_m(q)U`. This follows by induction
  with `Pi_0=0` and `Pi_(m+1)=(q-4)^m-4 Pi_m`. The geometric-sum definition
  is polynomial, including at `q=0`; the quotient notation there needs its
  polynomial extension. The exact native checks reproduce `m=0,...,4`.

## Findings

### P1: counted flux returns are not projected physical histories

Location: `src/workhouse/invariants/universal_cellular_hodge.py:211-227`;
duplicated in `scripts/verify_universal_hodge_tetrahedral.py:282-299`.

The checker enumerates boundary-flux additions and flags a return when an
intermediate six-dimensional flux vector equals the start-face boundary,
the target-face boundary, or zero. It then tests only the separate identity
`Q*(1,1,1,1)^T=0`. It constructs no Haar/Fierz state, physical retained
projection, resolvent, or projected insertion chain for any counted history.
The script simply increments `annihilated_count` when a flagged prefix exists.

This is a concrete missing identification: in the checker's own four-dimensional
face space, `Q e0 = (3,-1,-1,-1)^T/4`, of squared norm `3/4`, whereas
`Q psi=0`. Also `B psi=0` but `B e0` is nonzero. Returning to a face flux is
therefore not the asserted return to the carrier line. A zero flux label is
also not a proof that a quantum state is the zero vector or is retained.

The independent enumeration reproduces exactly 96 paths and the submitted
60/36 partition. Merely including the other two positive face boundaries in
that same combinatorial predicate changes 60 to 62, illustrating that the
partition depends on an unproved retained-sector choice. This is not a claim
that 62 is the correct physical count.

**Repair:** construct the actual states and retained projector and calculate
each projected history, including its channel and resolvent data. Until then,
retain the count as a flux enumeration and the generic `QP=0` lemma as scoped
support; remove the asserted physical-history certification and the unsupported
U3/U7 promotions at `ledger/gaps.yaml:1649` and `:1738`. The existing cubic
actual-support result and finite-cell Hodge identities remain established.
This review does not assert that the desired physical vanishing is false.

### P1: the manuscript and check use different S operators

Location: `docs/derivations/universal-cellular-hodge-tetrahedral.md:179-187`;
the same text is in the research-note and research-document copies.

The source defines `S=L_down+L_up`, hence `S=qI` on the cubic fibre, and says
`S psi=q psi`. The check actually gets `S=L_down-4I` from `HF._ops()`.
The displayed power formula gives `S psi=-4 psi` already at `m=1`.

At the exact Bloch point `z=(-1,-1,-1)`, `q=12`, `e2=48`, `e3=64`,
`sigma(RR)=768`, and `sigma(RUR)=9216`. The source-defined operator yields
`sigma(R S R)=9216`, while the displayed formula and code yield `-3072`.

**Repair:** consistently use the shifted repository operator `S=L_down-4I`,
retain `L_tot=qI`, and replace the erroneous carrier/complement derivation
with the induction above. Preserve the received versions and update source
digests and all source/ledger mirrors together.

### P1: whole-statement Lean coverage is overstated

Location: `ledger/derivation_statements.yaml:6051-6071` and corresponding
`formalizes` entries in `ledger/theorems.yaml`.

`tetrahedral_hodge_duality` assumes `L_down=4Q` and `L_up=4P`; its conclusion
is their sum and zero product. It contains no tetrahedral incidence matrix
or S4 representation, yet the ledger links it as a full formalization of
the combined tetrahedral/S4 commutant statement.

`feshbach_intermediate_return_annihilation` proves that `Q` kills `c psi`.
It contains no histories, path count, or physical projection identification,
yet it is linked as formalizing the entire 60-history claim with
`remaining: None; formalized in Lean 4`.

**Repair:** move these to `lean_support`, clear the corresponding whole
`formalizes` entries, describe the missing constructions explicitly, and
regenerate the export/coverage/graph in the documented order. The lemmas
themselves are valid and need not be discarded.

### P2: the explicit Pi4 polynomial is incorrect

Location: `docs/derivations/universal-cellular-hodge-tetrahedral.md:222-223`
and its two copies.

The geometric sum expands to `Pi4(q)=q^3-16q^2+96q-256`, whereas the source
prints `q^3-16q^2+112q-384`. At `q=12` the values are 320 and 384.
The resulting printed `sigma(R S^4 R)` is `-393216`, while the direct exact
operator calculation gives `196608`. The existing test calculates the correct
geometric sum; it never checks this printed instance.

**Repair:** correct the explicit polynomial and its substituted formula in
all mirrors, retaining source provenance. Check explicit manuscript instances
against their symbolic definitions.

### P2: the submitted Python files fail the publication lint gate

Ruff reports **30 errors** across the new invariant module, verification script,
and tests (imports, unused names, comparison style, and long lines). All three
also fail `ruff format --check`. `git diff --check` additionally reports a new
blank line at EOF in four changed ledgers.

**Repair:** fix and format the exact owned files, then run the full required
verification after correcting the mathematical assertions. Lint alone would
be routine to fix, but fixing it does not resolve the proof blockers above.

### Additional source correction

Theorem 3 correctly characterizes a scalar diagonal by equal face perimeters,
then incorrectly says it fails for all other polyhedra. Nonregular triangulated
polyhedral spheres also have perimeter 3 on every face, hence diagonal 4.
Keep the equal-perimeter criterion; remove the asserted classification by
geometric regularity. No change to the diagonal identity is needed.

## Executed verification

| Check | Observed result |
| --- | --- |
| Targeted pytest: universal Hodge, documents, graph, derivation statements, Lean dependencies | 89 passed, exit 0 |
| `lake build --wfail` from `lean/` | Passed, 3630 jobs; retained `lean-build.log` |
| Native filters: universal cellular Hodge / tetrahedral / Carrier Symbol Master Theorem / total Laplacian diagonal | 1/1, 6/6, 1/1, 1/1 passed; retained logs |
| Independent `diagnose.py` | Exit 0; exact witnesses retained in `diagnostics.json` |
| Ruff check on the three new Python files | Failed, 30 diagnostics |
| Ruff format check on the three new Python files | Failed, 3 files |
| `git diff --check` | Failed, four ledger EOF issues |

The 89-test total is 5 universal-Hodge, 4 documents, 31 graph, 8 derivation,
and 41 Lean-dependency tests. The successful test run was observed in the
tool session; unlike the Lean/native logs it was not redirected to a log file.
The full `make check`, full `make verify`, a new dependency export, graph
regeneration, and remote CI were not executed: the source review and lint
already fail the prerequisite for publication. No old run is counted as a
fresh execution.

Reproduce the exact review diagnostics from the repository root:

```powershell
uv run --no-sync python runs/universal_cellular_hodge_review_2026-09-11/diagnose.py
```

## Provenance and stopping point

The retained `start.json` and `end.json` are saved graph briefings, not fresh
calculations. Start fingerprint:
`b82515a3330dd4cd176c3fc07eb590f4d1d2f92e890706ffeeae8b908fc8bae1`.
End fingerprint:
`39a037f6187cf179bf83574081971769d6964b7badb6bfc20adbd4f09d4a41ca`.
The start was `matched`; the end was `stale` because this newly added review
package expanded the input manifest. Comparing manifests showed only review
artifacts added, no existing input bytes changed. All three saved graph-file
hashes remained identical. The graph was deliberately not regenerated to
publish the disputed claims as current verification.

The Hodge and corrected master-operator identities can advance finite-cell
and operator-word reasoning. They do not yet discharge the physical
tetrahedral-history identification or the U3/U7 common-mechanism obligation.
That is the next mathematical repair needed before this package can be
committed and pushed as verified.
