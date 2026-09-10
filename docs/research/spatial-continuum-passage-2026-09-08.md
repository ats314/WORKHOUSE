# Spatial continuum passage: current result and next estimate

The [spatial Schur-excess derivation](../derivations/wilson-spatial-schur-excess.md)
continues the completed fixed-spacing temporal bridge using the newer
September 5-7 spatial proofs, preserved with commit and byte provenance.

The new analytic result is an exact Schur reduction around the full reference
graph, together with an explicit O(g^3) relative remainder theorem. It keeps
quadratic memory and its induced metric, and assembles the complete second-order
Wilson operator and chosen-source normalization. Direct quartic magnetic
energy, electric metric, Haar, vacuum subtraction, moving sources and the
baseline/fast-variation cross terms all enter the same expression.

The accumulated physical-gap bound is

    Delta_J >= A_J / [Delta_0^(-1)+sum_(j<J) A_(j+1)/f_j],
    A_J=product_(j<J)(1-epsilon_j).

The proof also gives complete source-frame and specified-observable amplitude
budgets. For a hypothetical logarithmic trajectory g_j^2 proportional to 1/j,
an O(g_j^3) relative remainder is summable. An available generic O(g_j^2)
bound cannot guarantee that budget. This does not derive a running coupling.

The [selected-inverse continuation](../derivations/wilson-selected-inverse-wall.md)
tests SP8 on an actual compact SU(2) plaquette. A whole-fast-space Gaussian
upper form bound after finite-rank retention is impossible: the compact
high-character energies grow quadratically, while the radial oscillator
spectrum grows linearly. The conditional SP8 theorem remains valid, but this
particular implementation is a dead graph route.

The exact Schur identity also admits the weaker selected-inverse theorem W5.
Its precise open Wilson estimate is W6: a volume-independent signed fast-form
pairing between the Gaussian and interacting inverse images of the full graph
force. The Gaussian synthesis estimate does not bound the interacting image.
The actual fast floor and connected direct and source remainders also remain
to be established. Alternatively, SP8 could use a compatible compact reference.
Use the smooth redundant compact observation supplied by the September 7
flat-holonomy theorem, retaining the exact Gauss action and harmonic slow
dynamics. The existing localized cubic synthesis bound controls only part of
the full force. A chosen submersive chart does not identify the entire original
matrix-observation algebra.

After those estimates, the full second-order generated form and actual coarse operator,
physical clock and literal sources must be matched. High retained energies and
the compatible scale hierarchy must be controlled before the complete-gap
iteration applies. A nontrivial continuum correlation limit and the
field-theory axioms remain separate necessary conclusions.

The [validation report](../validation/wilson-spatial-2026-09-08.json) records the
exact controls and input hashes. The two Lean lemmas formalize the positive
weighted step and its all-finite-scale telescoping; they do not formalize or
assume the missing interacting Wilson estimates. The full closed-form theorem
is an analytic proof under its explicit hypotheses.

This continuation is local workspace work; it has not been committed, pushed
or merged.
