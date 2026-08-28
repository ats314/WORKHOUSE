# WORKHOUSE fixed-spacing proof chain and exact stopping point

**Date:** 2026-08-22  
**Mode:** WORKHOUSE repository read-only  
**Purpose:** state the strongest result reached, its exact dependencies, and
the first point at which the proof campaign cannot presently continue.

## Outcome

The complete protected one-plaquette (C=-) shell has been transported, at
sufficiently small strong-coupling coordinate and fixed lattice spacing, to
an isolated infinite-volume three-component lattice quasiparticle band. The
literal three-orientation Wilson source
(operatorname{Im}operatorname{Tr}U_p) has a bounded, invertible source map
onto that band at every lattice momentum.

Equivalently, in the physical charge-odd GNS sector there is an isolated
Riesz subspace

\[
\mathcal K_{1,-}(u)
\simeq \ell^2(\mathbb Z^3)\otimes\mathbb C^3,
\]

on which the Hamiltonian is an exponentially local (3\times3) convolution
operator with a Bloch matrix analytic in a complex momentum strip. The band
has a true external spectral gap, and the complete three-source Wilson Gram
matrix is positive definite at every real momentum.

This proves an actual **fixed-spacing lattice quasiparticle band**. It does
not yet prove a relativistic continuum particle.

The CMP(2)–CMP(4) arguments were subjected to independent adversarial passes.
The final CMP(4) review found two local decay-quantifier defects—globalizing a
Cauchy–Schwarz bound and requiring (e^\mu\vartheta<1)—which are repaired in
the final proof. These were exposition gaps, not new assumptions.

## Proof chain

### 1. Exact electric shell

In the gauge-invariant, center-neutral, charge-odd block, the free spectrum
strictly below (4) consists exactly of the rank-(3L^3) odd plaquette shell
at energy (8/3); the complementary electric gap is sharply (4/3). For
(L\ge6), the strict sub-(4) classification does not need the center
restriction.

Artifact: [electric-shell theorem](./WORKHOUSE_ELECTRIC_SHELL_THEOREM_PROOF.md)

### 2. All-orders isolated Riesz patch

The exact cell regrouping has onsite gap one after rescaling by (3/2), and
the bundled interaction norm is exactly (27|u|). Yarotsky spectral
localization isolates the full additive shell in an existential small-(u)
domain. Gauge, neutral-center, and charge-odd projections commute with the
Riesz projection, and analytic rank constancy transports rank (3L^3).

Artifact: [spectral-localization import](./WORKHOUSE_YAROTSKY_SPECTRAL_LOCALIZATION_IMPORT_NOTE.md)

The periodic finite-quotient step is a derived bounded-hypergraph proof
transport, not a verbatim numbered theorem in the source. It must be typeset
explicitly in any submission. The constants are existential, so no numerical
coupling threshold is claimed.

### 3. Totality and nonzero projected seeds — CMP(1)

Yarotsky's unweighted coefficient estimate gives a close-projection bound
for the complete physical shell. The interacting Riesz range is exactly the
closed span of all projected plaquette seeds. A local vacuum-continuity bound
makes each projected seed nonzero.

Artifacts:

- [CMP(1) theorem](./WORKHOUSE_CMP1_TOTALITY_NO_DARK_STATES_THEOREM.md)
- [CMP(1) close-projection proof](./WORKHOUSE_CMP1_CLOSE_PROJECTION_PROOF.md)

### 4. Spatial frame and analytic band — CMP(2)–CMP(3)

The rooted form of the coefficient estimate localizes each projected
three-cell seed. The one-sided projection identity reduces the Gram estimate
to one marked Riesz expansion. Local vacuum continuity controls contact
terms; Yarotsky clustering controls the tail. The resulting block Gram
kernel satisfies (|G-I|_mu<1), so the translated seeds form an exact
(ell^2) frame onto the Riesz range. The same one-mark method controls the
Hamiltonian kernel.

Artifact: [CMP(2)–CMP(3) band theorem](./WORKHOUSE_CMP2_CMP3_FIXED_SPACING_BAND_THEOREM.md)

### 5. Literal Wilson source — CMP(4)

After the phase normalization (c_W=i\sqrt2), the difference

\[
D_p=c_W M_{\operatorname{ImTr}U_p}-\widehat w_p
\]

annihilates the local product-vacuum sector exactly. This makes its contact
Gram terms small, while clustering gives an exponentially summable tail. If
(T_c) is the canonical projected source, (T_D) the projected difference,
(G=T_c^*T_c), and (C=T_c^*T_D), then

\[
T_W=T_c\bigl(I+G^{-1}C\bigr).
\]

The second factor is invertible in the weighted convolution algebra at
sufficiently small (u). Thus the Wilson source reaches the entire band at
every momentum. No new BCH/tree expansion is needed.

Artifacts:

- [CMP(4) detailed proof](./WORKHOUSE_CMP4_WILSON_SOURCE_TRANSFER_PROOF.md)

## Exact stopping point

The proof cannot presently be continued from small (u), fixed spacing, to
the four-dimensional continuum trajectory. Strong coupling and the
asymptotically free continuum lie at opposite ends of the coupling axis.
Finite-order coefficients and fixed-spacing analyticity do not bridge them.

The missing result is a **uniform source-carrying invariant-mass-island
theorem**. Along a reflection-positive scaling sequence (a\to0), it must
prove cutoff-independent constants (M_-,M_+,\Delta_*,z_*>0) such that:

1. the band has finite physical mass, (M_-\le M_a\le M_+);
2. the complete joint spectrum outside its mass tube stays at invariant-mass
   distance at least (Delta_*), including dark states;
3. a fixed-physical-radius normalized Wilson source has shell weight at least
   (z_*);
4. the joint energy-momentum spectral data and full Schwinger family converge
   with the Osterwalder–Schrader axioms;
5. the complete limiting shell multiplicity is controlled across all cubic
   partner sectors.

Those hypotheses would pass a nonzero isolated atom to the OS limit; standard
OS reconstruction and Haag–Ruelle theory would then produce a stable massive
particle. No available theorem supplies these uniform hypotheses for
four-dimensional (SU(3)) Yang–Mills. Proving them is essentially the
particle-resolved constructive continuum problem.

## What computation can and cannot do next

An A100 or 7900 XTX can test the expected continuum behavior—mass scaling,
Wilson-source overlap, (A_2/T_1/T_2) partner patterns, finite-volume effects,
and possible gap closure. Such runs would be valuable falsifiers and design
inputs. They cannot prove the cutoff-uniform spectral gap, residue, or OS
convergence required above.

Therefore no GPU run was launched in this proof campaign. The present blocker
is a missing constructive theorem, not insufficient compute.

## Claim boundary

The strongest current claim is:

> At sufficiently small strong-coupling coordinate and fixed lattice spacing,
> the protected (T_1^{+-}) plaquette shell becomes an isolated
> three-component infinite-volume lattice quasiparticle band with a
> positive-definite literal-Wilson-source map at every lattice momentum.

The claim that remains unproved is:

> This band survives the continuum scaling limit as an isolated relativistic
> particle mass shell with nonzero residue and specified spin.

All files named here were created outside the read-only WORKHOUSE clone.
