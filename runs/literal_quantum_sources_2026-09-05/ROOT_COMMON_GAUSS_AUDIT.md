# Independent common-Gauss proof audit

5 September 2026. Root reviewed COMMON_GAUSS_LITERAL_FAST_FLOOR.md through
Section 6 independently of its author. The proof is accepted at the stated
analytic scope: additive actual Wilson blocks with one common residual Gauss
constraint, fixed rank, uniform number of blocks. No ambient coupling theorem
is inferred.

Checks of the nontrivial steps:

1. Exact P Omega=Omega makes P commute with the local vacuum projection.
   Consequently exact nonvacuum support sets reduce the tensor P and Q.
   The tensor Gram lower bound survives arbitrary entangled superpositions,
   because distinct exact supports remain orthogonal after applying Q.
2. At threshold min(b,alpha+beta,3alpha), three excited blocks are excluded
   by energy, two excited blocks must both be in the full slow adjoint, and
   one excited block must be locally invariant. This accounts for every
   physical state below threshold; it does not discard a fast adjoint by
   declaring each block separately physical.
3. The slow adjoint's actual irreducibility follows by equivariant cluster
   identification with the isolated first oscillator cluster. Schur's lemma
   then gives scalar energy and scalar compressed Gram on that entire
   multiplet. Fixed rank is essential when basiswise cutoff convergence is
   promoted to the finite-dimensional operator norm.
4. The weaker unrestricted IMS estimate is sufficient: writing h=u^-1/2,
   a radius h^(1/3) gives an O(h^(4/3)) low-energy error for h^2 H, hence
   O(u^(1/3)) for H. This is o(sqrt(u)); the stronger physical parity
   remainder is not imported into the unrestricted cluster argument.
5. The bounded coarse cutoff is taken before the large-u limit. Its
   multiplication commutes with Haar flattening. No uniform pointwise
   lower bound on the true marginal is used for source approximation.
6. The one-block radial and two-block singlet errors occupy disjoint exact
   supports. Thus the weighted spectral deficit norm is the maximum of
   their two deficits, giving equation (10), rather than a count of states.
7. Infinite-rank source onto follows from BB* bounded below on the complete
   low target. It is not inferred from B*B. For countable additive copies,
   the exact-support decomposition gives the same bound on its Hilbert
   direct sum. Density of the restricted form can be justified by finite
   support truncations, which commute with h and Q, followed by smooth
   approximation on each finite product; fixed-product H1 bounds suffice.

The all-size conclusions remain analytic. Exact finite support and
representation controls illustrate these mechanisms without certifying the
elliptic localization limit or an interacting lattice.
