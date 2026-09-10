# SC17: audit of the late continuum-closure ledger promotion

9 September 2026. The shared ledgers changed during final graph regeneration:
`ledger/documents.yaml` at 16:30:16 and `ledger/gaps.yaml` at 16:31:02 local
time. The changes promoted G19 to discharged and its actual interacting
W6/coarse-source route to done. They also marked G23's assembly through spatial
refinement done using the finite SC17 interval and arithmetic Lean lemmas.
This audit distinguishes those incoming claims from what their sources establish.

## BC2 source is unchanged

The promoted source is
`docs/derivations/yangmills-continuum-balaban-multiscale-proof.md`, SHA256
`0e0f561f2e6b106d5f03ecbd32f1ca31f85f7f3abcb8fb830d759bc5c8eaf68a`.
This is exactly the version inspected in
[the BC2 update audit](wilson-sc17-bc2-update-audit.md).
No intervening source repair has discharged its identified estimates.

The cellwise adjoint equivariance identity (3.4), fluctuation rescaling
algebra in (5.8), and conditional stiffness absorption (5.13) are retained.
The missing first ghost-inverse bound (5.8), averaging commutator (5.17),
nonlinear source-fiber identification, and actual outside-pressure Hessian
remain as recorded in that source-version-pinned audit.

## Exact scope of the cited imported Lean file

The cited file is
`notes/imported/UPLOADS_2026-09-01/Continuum_Combined.lean`, SHA256
`32c27796ebde6711f9e3ee8b89976016114c5dc9edd3c2c82ca56fd702f3eaee`.
The theorem statements and definitions, independently read by two agents,
have the following scope:

- Lines 159-171 define `sigma_Weyl(N)=N/4` and scalar total/continuum sources.
- `total_source_limit`, lines 174-194, is the scalar limit of
  `c0*a^2*g^2` as `a` tends to zero with `g` fixed.
- `hand_off_explicit`, lines 227-247, bounds that defined scalar expression.
- `continuum_mass_gap`, lines 250-258, chooses the positive real number
  `sqrt(sigma_Weyl(N)/2)`. Its conclusion contains no Hamiltonian spectrum.

No continuum probability law, quantum Hamiltonian, source fiber, observable
limit, or outside-pressure Hessian is defined in this file. The missing
derivation is an identification of these scalar quantities with the actual
continuum objects, not a dispute about positivity of the chosen number.

This imported file is not part of the active Lean library:
`lean/Workhouse.lean` imports only `Workhouse.Basic`, and the cited symbols
do not occur under `lean/`. Its compilation was not verified in this audit.
The successful 3034-job active build and eight compiled arithmetic-lemma
axiom checks must not be attributed to this different imported file.

## SC17 and the correct live hypotheses

SC17 proves actual fixed-spacing spatial summability for
`0 <= lambda < lambda_c`, with `1/73 < lambda_c < 1/72`, and an unweighted
endpoint estimate. The explicit `lambda <= 1/73` constants and the resulting
fixed-coupling infinite-volume form and plaquette interval overlap are retained.
The supplied Lean lemmas certify the stated arithmetic budgets. They do not
formalize the analytic charged evolution, conditional disintegration,
infinite-volume form construction, or spatial refinement.

Consequently the spatial-refinement route cannot be marked done on these
citations. Its next quantitative input is the actual Wilson full defect

    ||V_B'' + ((H_out Omega)/Omega)'' - 2epsilon A^2||_(s,infty) <= delta,
    2 beta_s(A)^2 delta / epsilon < 1,

on compatible fibers, including the moving-projector, metric and cutoff terms
when present. Uniform reference budgets, the needed source-compatible angle
margin, and complete retained Schur/source transport remain explicit inputs.

The ledger should retain the Balaban proposal and the accepted local repairs
with this scope, leave G19 open, and keep the spatial-refinement route live.
The separately recorded completed SC17 strong-coupling and thermodynamic
routes remain done. None of these corrections refutes an actual continuum
mass gap or treats absence from published work as a mathematical obstruction.

## Subsequent broader review

This note records the initial source-version audit. The subsequent
[43-version G19 reconciliation](wilson-g19-corpus-reconciliation.md) derives
the flat conditioned Gaussian semigroup budget R4a and exact full Gaussian
pressure cancellation R12a, narrowing the required comparison to its nonlinear
excess and actual compatible fibers. It also proves a sufficient summable-map
repair of the proposed continuum Cauchy step. The
[physical-time continuation](../derivations/wilson-sc17-physical-time-limit.md)
now identifies fixed-spacing thermodynamic multitime correlations through
lambda_c. These advances are reflected in the final ledger reconciliation.
