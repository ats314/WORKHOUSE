# 39. Retain generated memory and compare the physical Schur forms

Date: 2026-09-05. Status: accepted.

## Context and decision

The established infrared Wilson transfer and complete physical source band
need an actual scale comparison. ADR 0038 retained the exact OS history
intertwiner and asked which physical modes remain outside its range. The
[Gaussian history theorem](../../paper/research_notes/G19_GAUSSIAN_OS_HISTORY_OBSERVABILITY_20260905.md)
now answers that diagnostic exactly: the range is determined by visible
frequencies over all positive times. It can be the entire fine space even
when fewer equal-time coordinates are retained. The symmetric strip also
has a mixed coarse/fine physical singlet below its separately invariant
fiber excitation. Configuration fibers therefore cannot identify the
actual OS complement by dimension or by an independent class gap.

Keep the generic history theorem and the older failed-route evidence.
Refine the live target to the actual generated history dynamics, including
memory, and a controlled physical low-energy approximation. A bound on a
nontrivial actual OS complement is still useful when that complement is
proved to exist. It is one case of the comparison, not a general definition
of removed configuration modes.

## Established mechanism

The [finite-cell theorem](../../paper/research_notes/G19_WILSON_FINITE_CELL_GAP_AND_BOUNDARY_FORM_20260905.md)
proves the full physical first cluster on fixed complexes satisfying the
explicit flat-orbit and curl hypotheses. It preserves the old Hessian
provenance and improves the ground/first-cluster remainder by finite
Hermite correctors. The error constant is not uniform merely because the
Hessian is local.

The [planar boundary comparison](../../paper/research_notes/G19_WILSON_HARMONIC_BOUNDARY_COMPARISON_20260905.md)
keeps every interface and exterior-link square. The
[three-dimensional companion](../../paper/research_notes/G19_WILSON_THREE_DIMENSIONAL_HARMONIC_BOUNDARY_20260905.md)
uses original periodic link cochains, Coulomb transversality and retained
torus harmonic directions. Both obtain a fast squared-frequency bound
depending on box size rather than box count. The global retained projection
need not be a local Wilson history map, and the unregulated torus tangent
zero modes do not have a normalized Gaussian vacuum.

The [closed-form Schur theorem](../../paper/research_notes/G19_FORM_SCHUR_SCALE_COMPARISON_20260905.md)
gives an exact physical comparison under explicit form assumptions. It
keeps the induced norm `M=I+U*U`, requires no small off-diagonal coupling,
and gives the complete gap bound
`Delta_fine >= (Delta_coarse^-1+f^-1)^-1`. A finite sum of inverse fast
energies is sufficient to iterate after actual normalized coarse matching
in common physical units. Its graph-source frame is onto the whole
window `[0,E]`, with lower bound `1-(E/f)^2`; identifying those vectors
with literal or renormalized Wilson sources remains a separate estimate.

Keep the Gaussian memory result as a corollary in that same proof. In the
Gaussian specialization the matrix eigenvalues are squared frequencies;
in the general form theorem they are actual Hamiltonian energies. The
positive-frequency Loewner bound and the literal-source coordinate factors
remain explicit. Publishing a second standalone Schur note would duplicate
the same proof mechanism and obscure this normalization distinction.

## Consequences and evidence

G19 and G23 remain open. The decisive Wilson hypotheses are now precise:
the full vacuum-subtracted restricted quantum form must have the uniform
fast bound; its dressing must be bounded; the normalized Schur form must
match a controlled coarse physical theory; and generated memory, locality,
the physical clock and renormalized sources must survive the actual
history construction. A harmonic coordinate compression is not that
quantum projection. Nontrivial continuum correlations and the field-theory
axioms remain required beyond a conditional gap recursion.

The [combined oscillator method review](../../paper/research_notes/G19_COUPLED_OSCILLATOR_METHOD_REVIEW_20260905.md)
preserves the user's useful exact invariant and its primary PDF, together
with the checked transformation repairs and relative-energy criterion.
It is method/comparison evidence, not a Wilson theorem dependency.
External numerical glueball values likewise remain outside the proof graph.

Register the new analytic statements with explicit hypotheses and narrow
finite-control support. Preserve original drafts and source bytes in the
new run. Keep the completed PR 103 proof/run package unchanged; only the
current navigation and live routes are updated. Regenerate derived views
after the canonical sources and new run are sealed.
