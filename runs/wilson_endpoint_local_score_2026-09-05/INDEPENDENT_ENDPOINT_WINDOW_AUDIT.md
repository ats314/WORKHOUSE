# Independent endpoint-window audit

5 September 2026. Read-only audit of `LITERAL_ENDPOINT_COMPLETE_WINDOW.md`.
No current canonical proof, code or sealed run is changed.

The operator argument is accepted. The following checks were made independently.

1. The positive contraction C_tau=J*exp(-tau h)J is injective even when its
   inverse is unbounded. Spectral calculus therefore defines a densely
   defined nonnegative self-adjoint logarithm. Exact retention of the whole
   vacuum kernel gives precisely the stated kernel correspondence.
2. For B=exp(-tau h/2)J, polar decomposition identifies the nonzero parts of
   B*B and BB* including multiplicity. The inequality BB*<=exp(-tau h)
   controls the complete source space. On the entire fine low space, the
   frame yields the lower Rayleigh inequality. Min-max then gives both
   energy bounds; separate column overlaps would not suffice.
3. A finite-rank complete fine cluster supplies a rank-r positive low part
   of the compressed endpoint operator, while its entire high part has
   norm at most exp(-tau t). This proves exactly r coarse levels below t
   under the strict separation condition. The source-space low/high cross
   terms of the high part are retained, not set to zero.
4. Gap counting must be read on vacuum orthogonal complements. This makes
   the claimed lower inverse comparison meaningful even for an infinite
   vacuum multiplicity; the near-bottom spectral-interval argument then
   proves the full gap implication. Infinite rank alone is not used as a
   dimension-counting substitute.
5. For additive strips the source, true vacuum and semigroup factor exactly.
   At tau=s/sqrt(u), the finite common-Gauss separation remains strict and
   the endpoint energy error is o(sqrt(u)). The countable version follows
   from local endpoint thresholds and the exact support classification,
   rather than from an infinite counting-function inequality alone.

The explicit local thresholds requested from the author are: the unrestricted
endpoint slow adjoint alpha_K is in [alpha,alpha-log(p_A)/tau], the remainder
outside its vacuum and complete adjoint is at least beta; the first local
physical radial a_K is in [a,a-log(p_r)/tau] and its physical remainder is at
least b. Equivariant polar/min-max comparison supplies these statements when
the corresponding local frame intervals are strictly separated. Three
nonvacuum factors then cost at least 3alpha; a two-factor state outside the
slow pair costs at least alpha+beta; a local invariant outside the radial
costs at least b. These give the countable complete classification, including
the actual pair energy 2alpha_K. No new assumption is needed beyond the stated
local spectral/frame inputs.

The temporal claims also check:

- The exact defect C_(tau+sigma)-C_tau C_sigma has the stated Q insertion.
  At equal times it is a positive square, and its vanishing makes P reduce
  exp(-tau h), hence h by spectral calculus.
- Operator monotonicity of log, with the positive resolvent definition of
  -log at spectral zero, gives the closed-form inequality K_2tau<=K_tau.
  A bounded inverse was not used. The fixed low-window error goes to zero
  along dyadic coarsening as tau grows.
- The four-vertex path has A_13=0, B_13=0 and (A^2)_13=1/2, so its coarse
  logarithmic rate is -tau^2/4+O(tau^3). This is a genuine stationary Markov
  compression whose positive operator logarithm need not generate a
  continuous-time Markov semigroup. The discrete-time RP chain has the right
  two-endpoint law, while its longer histories need not be the fine histories.
- The source-energy obstruction uses a legitimate abstract isometry and
  exact vacuum. Its frame remains good while its static retained energy
  diverges; the exact endpoint still has the stated finite error. This is
  an abstract finite quantum control, not an actual Wilson counterexample.
- The scale-budget inequality follows from
  -log(1-lambda/c)<=lambda/(c-E_star). The given physical-time choice makes
  rho_j summable under the explicit c_j>=C/a_j hypothesis and preserves the
  common energy clock. It does not construct a compatible interacting
  endpoint hierarchy, spatial locality or continuum correlations.

No mathematical blocker was found. The author was asked to spell out the
vacuum-complement counting and local endpoint irrep thresholds before final
freeze; these are precision requirements for the accepted argument, not
additional Wilson estimates. The finite exact controls remain distinct from
the closed-domain, countable and actual Wilson limiting conclusions.

## Two-lag complete-count certificate and final freeze

The final proof SHA256 is
`4dcb8da8880414960035de61780dedd5ac7f31f3e1159846b37235000e01b930`.
The author supplied the requested vacuum-complement and countable local-irrep
clarifications. The finite-source approximation in Section 3.1 also now
explicitly requires exact retention of J*ker h; a small approximation norm
alone cannot remove the vacuum coefficient from the complementary tail.

Section 3.1 is independently accepted. The full fine low frame and exact
vacuum imply D=Q0 exp(-tau h)Q0 <= d I with
d=gamma0 exp(-tau t)+(1-gamma0)exp(-tau a). The second-lag identity is exactly
V=J0*exp(-2tau h)J0-A^2=R*R. For z>d, bounded triangular congruence makes
the entire complementary block D-z negative, so the complete positive
index is that of A-z+R*(z-D)^(-1)R. Resolvent order bounds this between
the positive indices of A-z and A-z+V/(z-d). Equality of the two finite
indices therefore certifies the complete fine spectral count; no truncated
complement or separate-column frame premise is used. The earlier G18
source-moment identity is correctly credited, while the complete spectral
tail remains an explicit additional input.

The final frozen finite report is `literal_endpoint_window_controls_frozen.json`,
SHA256 `34e85020ea4c8fa27a25885fb58dcbe21cb5a290ad256f3f7202d86e3578aa0f`.
It preserves the four exact control families and six source pins, including
the noncommuting five-state three-threshold count, the genuine Markov-log
negative and the static-source-energy negative. The final control source
SHA256 is `c003fbe9429de59150dc7f4f5d41fb608ebe6e88e787228a673915996a8b3ee8`.
These finite controls remain distinct from the analytic domain and actual
additive Wilson conclusions accepted in this review.
