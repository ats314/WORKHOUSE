# Test report: anisotropy variance theory

The candidate's mathematical tests pass. Repository-wide verification is recorded separately below; passing the standalone tests does not imply graph integration or physical sixth-order closure.

## New mathematical tests

`test_independent.py`: **7 passed**.

The tests evaluate the full record matrix directly at exact rational complex phases, check Hermiticity and the Hodge decomposition, and verify the residual using ordinary matrix multiplication. This route does not call the Laurent carrier-projection or composition functions used by the original verifier.

An independent characteristic-polynomial calculation verifies that the candidate's sixth-order coefficient solves the eigenvalue expansion with a nonzero coefficient multiplying the unknown. It tests the determinant rather than assuming the perturbation formula.

The numerical adversarial test uses **472 spectral probes**, 75-digit arithmetic, and a fixed random seed. Momenta reach 10^-30; coupling approaches the stated isolation threshold to relative distance 10^-8. The matrix is divided by u^2 q before diagonalization, so the 10^-60 tolerance does not become vacuous near Gamma. Both the overlap and energy bounds pass, as does the band-gap bound. Worst bound fractions are recorded in `adversarial_certificate.json`.

Other tests check the overlap asymptotic coefficient, explicitly reject Gamma as a rank-one-carrier point, check nodal classification and the variance bound on rational simplexes of denominator up to 24, and distinguish the induced sixth-order contribution from a direct sixth-order scalar addition.

## Lean

`Variance.lean`: **8 lemmas compiled**, with warnings treated as errors. They cover the variance identity, nonnegativity, the 1:3:-4 shape identity, three nodal families, the exact rational holdout, and the induced rational coefficient. Printed axiom dependencies for the core identities contain only `propext`, `Classical.choice`, and `Quot.sound`; no `sorryAx`.

The existing repository Lean core also passed `lake build --wfail` (3034 build jobs). This does not formalize the full spectral argument: the overlap and energy inequalities retain their written analytic proofs and numerical checks, and the full-kernel residual has exact symbolic verification.

## Failures found and corrected

The first independent matrix test used z^-1-1 for a carrier component, whereas this repository explicitly defines its `dbar` as z-1. This convention error in the new test harness caused a large exact discrepancy. After correcting it, a nodal fixture revealed Python negative integer powers producing floats. Sympifying all phase inputs restored exact arithmetic; no tolerance was added to the exact tests.

The first Lean attempt used the wrong sign in a `linear_combination` proof. Substitution of z=1-x-y followed by `ring` proves the same statement. Initial failure logs are retained alongside the final successful logs. None of these corrections changed the proposed mathematical formulas.

## Repository checks

- Repository lint: passed.
- Repository format check: passed, 201 files already formatted.
- Existing Lean core: passed.
- Full invariant and pytest results: see the completion entry below.

### Completion result

**Full invariant verification passed: 361/361.** `repository_verify.log` ends with that result and the process exited 0.

**Full repository pytest did not pass.** The first run was interrupted during expensive collection and restarted with a writable cache location. The restart exited 2 with six collection errors: `claims.py` imports `workhouse.study_graph`, but that module is absent. A fresh git diff shows concurrent modifications to `claims.py`, `graph.py`, and `literature.py`; `claims.py` was modified at 23:45:38 local time during this testing session. This task did not edit those files. The failed tests are atlas, CLI, finder, graph, provenance, and search. See `pytest.log` for the complete traces.

The baseline lint/format pass therefore applies to the checkout before those concurrent edits. No clean claim is made for the changed checkout. The candidate's tested kernel inputs were checked separately for source-hash stability.

The earlier separate graph-only run was canceled as redundant with the full suite; it is not reported as passing. The interrupted full-run log and the final collection-failure log are both retained. Resolving the concurrent missing-module change and rerunning the full repository suite remains necessary before a merge can be called green.

The candidate remains a standalone research artifact. It has not been registered in the theory graph, pushed, or merged. No claims about worldwide novelty, the complete sixth-order Hamiltonian, transfer-matrix identification, or the continuum limit follow from these tests.
