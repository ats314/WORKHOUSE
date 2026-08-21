\`\`\`latex id="c7l5gc" %
============================================================

\% ============================================================

This section formulates the deterministic projected-capacity layer and
combines it with the conditional hard-defect Peierls estimate from
Section\~. The output is a rooted source-stability criterion. The
theorem is conditional on the Wilson free-energy stability input and on
a deterministic projected-capacity envelope.

Let (\_L=(Z/LZ)\^4). Let (E\_L) be the set of oriented links and let \[
H\_L = \^2(E\_L;(N)) \] be the finite-dimensional real Hilbert space of
Lie-algebra-valued link fields.

Let \[ P\_{,L}:H\_LH\_L \] be a fixed finite-volume orthogonal projector
onto the physical projected Maxwell window. Examples include a
transverse Hodge window, an infrared Fourier window, or a massive
projected comparator window. The exact choice is not fixed in this
abstract theorem; the only properties used below are orthogonality and
volume-uniform deterministic capacity estimates.

For a plaquette set (P\_L), let \[ E\_L \] denote the set of links
incident to at least one plaquette in (). Let \[ \_{} \] be the
multiplication operator on (H\_L) by the indicator of those links.

Define the projected capacity of () by This quantity measures how
strongly the physical projected window can concentrate on the link
boundary of the plaquette animal ().

The global top norm \[ \| P\_{,L}*{D*(U)}P\_{,L} \| \] is not the right
object at fixed positive defect density. The rooted object is instead
the capacity of the connected defect island containing a prescribed root
plaquette.

Let (p\_0P\_L). Let (C\_{p\_0}(U)) be the connected component of
(D\_(U)) containing (p\_0), with the convention \[ C\_{p\_0}(U)=
p\_0D\_(U). \] The rooted capacity random variable is

The deterministic input needed for the theorem is a capacity envelope
for connected plaquette animals.

This linear envelope is deliberately weak. Stronger estimates, for
example sublinear or diameter-sensitive capacity bounds, may improve
constants, but are not needed for the basic rooted summability theorem.

The key rooted source-stability object is the exponential moment where
(a,s). This quantity weights the rooted defect island by both its volume
and its projected capacity.

The empty cluster contributes (1). For the nonempty part, decompose
according to the possible rooted animals: The right-hand side is not
sharp, because it sums over all animals contained in the defect set
rather than only the exact connected component. Sharpness is not needed;
the upper bound is sufficient for source stability.

The exponential moment above controls local source insertions whose
defect cost is bounded by rooted capacity.

Let (J) be a source supported near (p\_0). Suppose its
defect-amplification factor obeys the deterministic bound for some
constants (C\_J,a\_J,s\_J). Then Theorem gives whenever This is the
rooted source-stability conclusion.

The rooted theorem does not assert \[ \| P\_{,L}*{D*(U)}P\_{,L} \| c\<1
L. \] Such a global statement is not expected at fixed positive defect
density.

Instead, the theorem controls the connected defect island attached to a
fixed source location. This is the correct object for local source
stability: correlation functions with localized insertions are sensitive
to the defect geometry connected to those insertions, not to the worst
rare island somewhere else in the volume.

The linear envelope (\_L()b\_0+b\_1\|\|) is sufficient but crude. A
sharper projected-capacity theorem could improve . Useful refinements
would be estimates of the form \[ \_L() b\_0+b\_1\|\|\^, \<\<1, \] or
block-capacity estimates depending on the coarse-grained geometry of (),
rather than only on its size.

Such improvements matter because projected Maxwell windows respond to
geometry, not merely cardinality. Thin, dispersed, or weakly connected
animals may have substantially smaller projected capacity than compact
blocks of the same size. The numerical projected-capacity audits are
best interpreted as calibration data for finding the correct
deterministic envelope.

The result of this section is conditional but precise:

\[ \]

The missing theorem is not a local class-gap computation. It is the
volume-uniform Wilson free-energy and projected-capacity estimate needed
to verify the hypotheses. \`\`\`
