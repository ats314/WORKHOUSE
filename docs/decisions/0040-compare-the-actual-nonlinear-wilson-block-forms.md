# 40. Compare the actual nonlinear Wilson block forms

Date: 2026-09-05. Status: accepted.

## Context and decision

ADR 0039 retained the exact history-memory question and gave sufficient
closed-form Schur hypotheses. The next step must realize those hypotheses
for actual Wilson quantum energies, with the vacuum subtraction and
physical observable space explicit. A harmonic coordinate inequality or
a configuration diffusion gap does not supply that realization.

Register three connected analytic results from the actual two-face blocks.
The [global vertical comparison](../../paper/research_notes/G19_WILSON_GLOBAL_VERTICAL_BARRIER_20260905.md)
uses the exact link metric, a genuine SU(N) root chart and the exterior
potential barrier to control the entire counted fiber spectrum on every
coarse holonomy. Its joint bound keeps both the full fast penalty and a
scalar Wilson coarse potential. A central class gap is not assigned to
a noncentral fiber, and the actual SU(2) conditional gap at minus identity
remains order one.

The [ground-bundle theorem](../../paper/research_notes/G19_WILSON_GROUND_BUNDLE_RELATIVE_FORM_20260905.md)
proves actual quantum-ground derivatives, the exact horizontal lift and a
zero Berry term on a fixed near-identity chart. The classical scalar
minimum is removed before differentiating and restored in the final
form. The projected coarse energy retains its real metric and Haar
measure, with a relative O(g^2) magnetic correction. The same constant
tensors for additive disjoint-edge copies; that observation adds no
surrounding plaquettes or shared-edge interactions.

The [actual adjacent-strip complement](../../paper/research_notes/G19_WILSON_ACTUAL_BLOCK_FAST_COMPLEMENT_20260905.md)
goes beyond a fiber inequality. The entire physical complement of the
conditional ground bundle has bottom
`(sqrt(3)+sqrt(5))sqrt(u)+o(sqrt(u))` above the true full-block vacuum.
The lower bound uses the complete physical low spectral space, while an
exactly constrained mixed trial controls the upper bound in energy as
well as norm. The first complement channel is a mixed singlet.

One horizontal integration by parts then bounds the actual cross form
and supplies a bounded fixed-u Riesz lift. Its Schur form is closed and
nonnegative on the exact triangular domain. Thus the earlier Schur
spectral comparison and whole-window graph-source frame apply to one
actual nonlinear block with an infinite-dimensional retained space.
This is not an identification with a prescribed bare coarse Wilson
Hamiltonian or a literal/OS source family.

## Dependencies, evidence and scope

The global barrier and local ground-bundle estimates use the established
actual rotor geometry and full fiber gap. The abstract Schur theorem is
their downstream application, not their premise. The third proof uses
the complete two-square physical shells and the ground-bundle estimates;
only its Schur corollary invokes the abstract form theorem. The global
barrier is complementary to that proof, not an artificial dependency.

Keep analytic proof, five native finite checks and seven Lean scalar
lemmas distinct. The Python controls establish their matrix, group,
scalar, geometric and finite projection statements. Lean formalizes the
scalar factor, cap, affine and two-sector transfers under explicit
analytic inputs. Neither certifies all SU(N) operator domains, spectral
convergence or a nonlinear volume limit. Preserve the original proofs,
controls and independent audits in the new run; keep the PR 104 proof
and run package unchanged.

G19 and G23 remain open for the interacting-volume scale comparison.
The actual finite-block fast form and normalized Schur operator now
exist. Uniform lift bounds, true many-block vacuum adaptation,
interactions across boundaries, prescribed coarse spectral matching,
temporal memory and renormalized source/clock control still require
proof. Tensoring a retained line with a small vacuum error is not a
volume-uniform argument, as the existing mismatch example demonstrates.
The exact history range must still be determined from its actual
observable algebra. Nontrivial continuum correlations, a finite physical
mass and the field-theory axioms remain the governing goal.

Regenerate the result graph and maintained views after all canonical
sources and evidence are frozen. Publication status must distinguish
local, pushed and merged work.
