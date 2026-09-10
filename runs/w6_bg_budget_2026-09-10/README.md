# W6 actual ground jets and conditional source-tail budget

Date: 10 September 2026. This run integrates three standalone analytic notes,
preserves their exact bytes and helpers, and replays **24 exact finite algebra
controls**. It does not certify a uniform small-coupling Hardy constant or an
interacting growing-grid floor.

The portable successor derivations are:

- [Actual ground jets and the complete transport budget](../../docs/derivations/w6-ground-jets-and-transport-budget.md).
- [Conditional-score tail control and the local phase repair](../../docs/derivations/w6-conditional-score-tail-control.md).

## Mathematical consequence

The new fixed-square argument proves inverse-power energy bounds for the raw
electric/magnetic form derivatives, the ground-energy derivatives and the
actual ground-vector jets through order three. It also controls the
vacuum-only generator through its second derivative. Explicit energy bounds
on the **complete actual source generator** then imply the requested complete
residual derivative constants. Those source-generator bounds remain a model
estimate to prove.

The actual noncommuting inequality `1-w<=V`, the true-ground form identity and
the physical gap also prove the uniform all-source potential moment
`g^-2 integral(1-w)|f|^2 <= (1+E/gamma)b_g[f]` for centered sources. The
additional pointwise conditional score-to-potential estimate M10 remains open;
its sufficient Hardy constant is derived with the vacuum-energy term retained.

The second new argument proves finiteness of the actual Hardy quantity on every
closed positive-coupling interval and computes its endpoint behavior. An exact
Gaussian example shows why averaged ground-score control and near-well jets
do not by themselves control rare-source tails. A specified local phase-adapted
vector field removes the dangerous centered leading phase term under stated
conditional-phase hypotheses. Chart-complement tails and a uniform whole-fiber
Hardy estimate remain open.

## Attribution and preserved inputs

[source_manifest.json](source_manifest.json) records the original absolute path,
SHA-256 and byte count of each of the eleven final preserved source files. The nine campaign
files are new standalone work. The subdivision Markdown and
[W6Subdivision.lean](sources/prior_subdivision/lean/Workhouse/W6Subdivision.lean)
are **prior project work**; the new budget uses their composite approximation
without claiming that theorem as a new result. No Lean source was built by
this run. Existing compact-source, actual-ground and Gaussian-grid results
are linked from the successor documents and retain their previous scopes.

Original notes retain their historical local references and exact bytes.
Portable links and the explicit normalization crosswalk occur only in the
successor documents. An uncited external-literature search paragraph was not
a proof input and was omitted from the tail-control successor; it remains
verbatim in the intake.

## Replay and analytic review

From the repository root, with Python and SymPy available:

```text
python runs/w6_bg_budget_2026-09-10/replay.py
```

[replay/replay_record.json](replay/replay_record.json) records the actual Python
runtime, all three exit codes, 15 residual controls plus 4 tail controls and 5 source-moment controls, and the
post-replay identity check of every preserved source. The three programs write
their deterministic output beside their preserved sources; the replay checks
that these outputs still match the received bytes. Stdout and stderr are
retained in the replay directory.

The first attempt used the bundled Python runtime, which lacked SymPy. It
passed the 15 standard-library controls but could not import the four-control
script; its outputs are preserved in [attempt_01_bundled](replay/attempt_01_bundled/replay_record.json).
The successful replay used the existing repository Python environment with
SymPy already installed. No package installation was performed.

The controls verify rational derivative identities, normalization and Leibniz
coefficients, the physical-clock product identity, and exact Gaussian and
compact-endpoint coefficient arithmetic. They do not formalize elliptic
regularity, the compact operator domains, conditional phase existence, or a
Wilson continuum theorem.

An independent analytic peer review checked the ground derivative and
normalization identities, energy-space recursion, vacuum generator estimates
and transport Leibniz constants. The tail-control review retained the necessary
chart-restricted variance scope, complementary-tail/conditional-mean obligation,
and explicit fourth-moment hypothesis in the cutoff argument. The finite
replay is narrower evidence than those analytic derivations.

[SHA256SUMS](SHA256SUMS) seals the files within this run, excluding itself.
Repository ledger registration, full regression verification and GitHub landing
are separate integration operations; this run does not claim them completed.

The pre-clarification intake of the source-moment note is also retained under
[intake_stages](intake_stages/actual_potential_moment_before_explicit_nonnegative_constants.md);
the manifest records its hash separately. The final original note and successor
state the nonnegative score constants explicitly.
