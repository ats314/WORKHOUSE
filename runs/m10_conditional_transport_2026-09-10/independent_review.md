# Independent mathematical review of the final transport derivation

10 September 2026. Reviewer: independent positive-route agent.

Reviewed source:
`C:\WORKHOUSE\worktrees\m10-conditional-transport-20260910\docs\derivations\w6-conditional-transport-obstruction.md`

SHA-256 at review:
`33f5cefc2105ec3ec354edacce46371cfede62a2e46ec1557cacc5ae80f473e5`

**Verdict:** No further actionable mathematical error found after checking the
revised S3 and S6 passages. The earlier eigenvalue-identification, local
ambient-domain and remainder-order issues have been addressed.

Verified analytically:

- S1-S2 retain the Haar divergence, conditional normalizer and coarse motion.
  The variance factor is 1/4; the normalized-vector speed in S9 is sqrt(K),
  with no additional factor two. Conjugation invariance justifies replacing
  conditioning on full Q by conditioning on its trace for these moments.
- The original-edge principal symbol is Gamma/2. The Agmon calibration has
  I'(theta)^2=v_*(theta), and the twelve-dimensional vacuum prefactor h^-3
  gives the nine-dimensional fiber normalization h^-3/2 exp(-2I/h).
- Revised S3 applies the local comparison theorem on an open well chart,
  avoiding an unsupported assertion about returning global characteristics.
  The cutoff ground-transform Rayleigh estimate identifies the Dirichlet
  eigenvalue with the compact ground branch before the physical h gamma gap
  is used. Positivity and invariant domains/cutoffs keep both grounds in the
  physical sector. Exponential comparison and conditional normalization are
  retained before taking the fixed rare-fiber limit.
- S4 uses the correct half-density pullback sign: concentration moves to
  Phi_{-t}(m). Distinct limiting point masses give vanishing overlap. The
  logarithmic interval speed bound in S11 contradicts that limit for a fixed
  sufficiently small positive t. No coupling derivative of a WKB remainder
  or asserted g^-4 score law is needed.
- S12-S15 give the stated synchronized tangency and conditional tube
  implication. The Lie-vector conversion |q|=2 theta and the coefficient
  2 pi^2 in its potential comparison are consistent. The revised smooth-phase
  annulus and positive cutoff-margin qualifications are appropriate.

The explicit external analytic dependency is the scalar, one-well
specialization of Klein and Rosenberger, [The Tunneling Effect for Schroedinger
operators on a vector bundle](https://arxiv.org/html/2005.13852#S6), Hypotheses
1.1, 3.2 and 6.1, Theorems 6.2 and 6.5, particularly the weighted comparison
(6.9) and ensuing spatial elliptic bootstrap. Its half-integer expansion
supports the corrected O(sqrt(h)) remainder. This primary source was read
during the review. The theorem is an external analytic input, not a result
verified by the campaign's finite symbolic checks.

The established conclusion is existential and actual: at least one smooth
common-cutoff product transport admitted by Q8 fails M10 for the true compact
square ground law. The proof does not establish failure for every Q8 member.
The synchronized field is a different explicit admissible selection. Its
full all-fiber uniform M10 estimate remains open; the differentiated relative
amplitude, conditional complement and antipodal degeneration estimates have
not been supplied by the concentration theorem.

No tests, symbolic scripts or Lean builds were run by this reviewer. This is
an independent analytic review of the displayed argument and cited theorem;
it does not independently re-prove the project's prior physical gap or Q5.
