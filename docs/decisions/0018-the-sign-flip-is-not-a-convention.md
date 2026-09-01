# 18. The (rho, pi) sign flip between the rival kernels is not a convention

Date: 2026-09-01. Status: accepted — a negative result, recorded per ADR 0005.

## Context

C2 reduces, in the orbit basis of the kernel-orbits suite, to three signed
numbers: the two rival fourth-order kernels agree on the support, on all six
cubic orbits, on the normalized shape table and on both tier-collapse
identities, and disagree in one scale and in the signs of the two amplitudes
`rho` (cross-plane) and `pi` (in-plane), the normal orbit unmoved. Two orbits
flipping together while a third does not reads like a convention, and the
off-axis channel run had already found one such (an entry that is minus the
conjugate of the recorded rotation row). On 2026-09-01 the graph recorded this
as the one untried route on G3: derive from Hermiticity and cubic covariance
the sign pattern the Bloch basis permits, and ask which kernel is consistent.

## What was computed

Three checks in `src/workhouse/invariants/orbits.py`, machinery in
`src/workhouse/kernel_orbits.py`, all engine-free.

1. **Symmetry fixes no sign** (T1). Kernel records are corner-based; the cubic
   group acts on plaquette centres, `Delta = d + c(op) - c(ip)`, with the
   orientation character `chi_g(P) = s_i s_j sgn(order)` — which is `PSI_SIGN`
   read at the identity, the cube boundary `d_3`. With that, every one of the
   six orbits is separately Hermitian and invariant under all 48 elements of
   O_h. Two controls: without the character the cross-plane orbits keep 12
   elements; on the raw corner-based displacement they keep 6. Symmetry is
   linear, so the kernels with `rho` flipped, `pi` flipped, or both are equally
   Hermitian and covariant. All four sign patterns are admissible.

2. **No convention reaches the flip** (T1). The conventions available in the
   plane basis are the 48 signed permutations of the fibre with `k` untouched.
   Only `+-1` preserves the 144 skeleton and doubled records both kernels
   agree on. `pi` is a same-plane orbit, untouched by every regauging. Every
   diagonal regauging other than `+-1` flips two of the three cross-plane
   pairs and throws `rho` — and the cross-plane skeleton with it — out of the
   cubic shape span.

3. **The cold kernel is in the same basis** (T2, 1e-9 relative on record
   equality). The v10a.26 dump passes the identical test with the identical
   character, so the regauging result transfers.

## Decision

The route closes `done` with a negative result. The refutation it might have
delivered — one kernel's sign pattern forbidden by symmetry — is not available,
because symmetry constrains neither sign. What it delivered instead: the flip
is not a basis convention of either computation. The two kernels are two
different Hermitian, cubic-covariant operators written in one basis, and C2 is
a disagreement about which fourth-order operator the theory produces, not
about how to write one down.

Nothing here prefers either side of C2, and nothing is promoted. G3 keeps one
live route, the independent cross-amplitude computation, and this ADR is the
reason no future session should spend time on a convention explanation.

## Consequences

- `ledger/gaps.yaml`: the G3 step is `done`, `closed_by` the three checks;
  `ledger/contradictions.yaml`: C2 carries `sign_flip_is_not_a_convention`
  beside the earlier `sign_flip_is_not_the_whole_story`.
- `kernel_orbits` now carries the cubic group on plaquette records
  (`cubic_group`, `transform_record`, `covariant_elements`, `regauge`), the
  first place in the repository where the orientation character is computed
  rather than asserted. Any future kernel — the cross-amplitude computation
  included — should pass `covariant_elements(...) == 48` per orbit before its
  amplitudes are read.
