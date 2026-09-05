# 35. A gapped creator parent realizes the Wilson vacuum

Date: 2026-09-05. Status: accepted.

## Context

The rooted contraction and stabilized creator coefficients are established
analytic inputs. Their convergence does not bound a global creator
similarity in volume, and it does not by itself construct the actual
symmetric Wilson state on the full local quantum algebra. The live G18
route therefore asked for a controlled physical operator realization.

## Derivation and decision

Restore the magnetic half-endpoint to obtain the actual symmetric creators
with rooted norm at most `1/8`. For their exact-support rank-one operators,
set `P_i=q_i-sum_(X contains i)a_X` and `H_par=sum_i P_i^*P_i`.
The `P_i` are commuting idempotents. Two orthogonal block cancellations and
an exact sum-of-squares identity give

```text
H_par^2 >= (1-K1-M1^2) H_par,
gap(H_par) >= 247/256.
```

The finite-volume similarity identifies only the unique kernel. Its norm
is unnecessary for the gap proof. Connected Taylor witnesses and Cauchy
estimates give exponential spatial bounds for the parent interactions and
their coupling derivatives. These verify the infinite-dimensional-site
spectral-flow assumptions of Nachtergaele, Sims and Young. The periodic
comparison uses intrinsic torus metrics, since wrapping interactions do
not have a uniform ambient-lattice decay norm.

Record the resulting actual symmetric creator family, generic parent gap,
parent GNS realization, and selected Wilson vacuum spectral flow as
separate analytic results. Close the vacuum realization route using those
results. A subsequent finite-family partition logarithm now constructs
the dressed Wilson activities exactly. A common spectral filter makes
induced disconnected subsystems factor, so their connected activities
cancel. Self-adjointness and the normalized vacuum give both local
annihilation legs. The next route is their full-operator activity estimate
and the source bound. The bridge already requires exponential support
cardinality weight `(5/4)^|X|`; diameter decay from spectral flow does not
imply it. Connected supports do convert a proved cardinality bound into
bare spatial decay, and a stronger cardinality margin supplies the
additional spatial weight.

## Scope and alternatives

The parent supplies a vacuum transport, not the Wilson excitation energies.
The GNS equivalence is with the product representation composed with the
quasi-local automorphism. No global implementing unitary in the original
free representation is claimed. The selected full local state is pure and
locally normal; matching the existing Euclidean multiplication-source
state uses its separate domain and observable identification.

Directly bounding the global similarity would fail even for disjoint
single-link creators inside the rooted ball: the condition number grows
exponentially with volume. Dropping the positive quadratic term from the
parent destroys positivity and vacuum annihilation. Both failed shortcuts
have explicit reproducible controls and are retained as evidence.

## Verification and provenance

The complete proof is
[the parent and spectral-flow note](../../paper/research_notes/G18_WILSON_CREATOR_PARENT_AND_SPECTRAL_FLOW_20260905.md).
The new run is `runs/wilson_creator_parent_2026-09-05`. Six exact tensor
models carry 81 rational PSD congruence certificates with independent
reconstruction. Three Lean lemmas prove the two star-ring identities and
the scalar `247/256` bound under their explicit hypotheses. The uniform
Hilbert-space, thermodynamic and spectral-flow statements retain analytic
evidence and are not promoted by those narrower machine controls.

The new note and run receive additive pins. Existing sealed sources retain
their original stage-specific conclusions; current documentation and the
result/route graph carry this continuation.

The additive
[activity extraction note](../../paper/research_notes/G18_WILSON_ACTIVITY_EXTRACTION_20260905.md)
and `runs/wilson_activity_extraction_2026-09-05` record the partition
construction and independent finite controls. The generic extraction proof
commutes only coefficients on disjoint supports; overlapping coefficients
need not commute. Neither its exact inversion nor finite controls prove
the weighted activity norm.
