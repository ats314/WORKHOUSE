# Independent actual Gaussian fast Green audit

6 September 2026. Read-only review by the independent result/control agent.

Accepted source snapshot:

* `../FULL_GAUSSIAN_FAST_GREEN.md`, SHA256
  `b8691f1bc4425f0ae2281b46200c8f1dba086107de508900996b9c6ae8e63ae2`.
* `../check_full_fast_green.py`, SHA256
  `ed9137a3876c31e16d64ca05e76df6e132f9881707105d169336fc61bb4ec0e8`.
* `../FULL_FAST_GREEN_CONTROLS.json`, SHA256
  `522d7d9b32f386f981b5637aae659763204fe217f909a88c43bfeac5240ae25f`.

The complementary compressed inverse follows from the constrained system
Dx+B lambda=b, B*x=0. With B=L_n U_n, sandwiching by L_n gives the
claimed shorted energy prior because D_n and L_n commute. This does not
assume that the source reduces D_n. Permutation and adjoint equivariance
justify the stated bosonic and physical restrictions. The n=1 prior is
Omega^-2; the n>1 source complement includes mixed retained/fast sectors.

I checked the ordered-tensor factor in equation (6) independently. On one
alternating spatial triple, P_D has coefficient 6D_123, whereas the ordered
spatial tensor norm counts six entries. The factor 3! C_A dim(g)/8
therefore agrees with direct creation-operator normalization. It is not
the factor for a differently normalized wedge coordinate without an
accompanying change of inner product.

All three saved finite families were independently replayed with
`check_full_fast_green.py --verify FULL_FAST_GREEN_CONTROLS.json`.
The KKT solves, direct compressed inverses, and equal-time/all-fast
negative controls agree exactly. Their scopes are finite matrix and
exterior-tensor algebra. They do not certify an infinite-volume kernel
estimate.

The companion local plaquette derivation establishes the actual harmonic
obstruction used in section 5. Its full path and source weighting are
kept; its selected vector is a physical color singlet. It concerns the
local magnetic coefficient, and its global spatial sum cancels in that
sector. The parent independently checked the six BCH commutators and
accepted the normalization and scope on 6 September 2026.

Section 6 correctly keeps the conditional-fiber inverse distinct from
the full-Q inverse. Domination by the vertical form transfers a synthesis
quadratic-form bound, not an entrywise absolute kernel bound. The note
leaves the interacting remainder, baseline cross terms, all-scale
compatibility and continuum construction open. No mathematical repair
is required in the reviewed snapshot.
