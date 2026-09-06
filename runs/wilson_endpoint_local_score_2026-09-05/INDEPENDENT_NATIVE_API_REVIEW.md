# Independent endpoint and local-source native API review

5 September 2026. Read-only review of the staged v1 and additive v2 APIs
and invariant suite. The mathematical scope is accepted. This does not
substitute for the code owner's final canonical tests and source handoff.

The two-lag moment API checks exact rational symmetric moment data,
contraction inequalities, positive leakage and strict positive indices.
Its entire discarded-space bound is prominently marked as an external
hypothesis. It does not infer that bound from moments. The finite-transfer
API separately checks the complete positive contraction, normalized source
Gram, whole vacuum inclusion and every omitted direction before computing
the exact Schur index. Extending the complementary resolvent by zI on P
is harmless because R has range in Q; d<z guarantees invertibility.

The local-gradient API requires the constant-annihilating five-state form,
positive isotropic radial/adjoint energies, a nonnegative bounded bad form
and exactly centered profiles. It evaluates the full source Gram and all
form entries, including arbitrary profile superpositions and local bad-form
mixing. For one copy the maximum of radial and pair trace ratios may be a
nonoptimal upper cap; it remains valid and the API does not claim attainment.
The score contraction API is explicitly only the exact leading SU(2)
Lie/Gaussian coefficient. No finite API certifies the Wilson-ground
derivative remainder, countable closure or interacting covariance.

V2 adds one complex-rational full-floor API. It requires a Hermitian
idempotent Coulomb projection, K=P_C K P_C, independent transverse source
columns and their actual Hermitian Gram. It checks all physical zero modes
are retained, then uses exact Hermitian elimination on K and the FULL
K-kappa(P_C-P_S). The compression-only negative is appropriate because
positivity of Q_S K Q_S does not imply this full inequality. The path and
Fourier suite descriptions keep the n=4,L=2 complex-rational controls,
two noncommuting SU(2) examples and twelve finite alias moments separate
from the analytic all-size/compact-group/Fock conclusions.

The native model bodies are independently recomputed constructions and
exact identities, rather than loading their expected JSON as acceptance
data. Reusable replay functions compare complete recomputed reports and
reject changed fields. Explicit ValueError validation handles invalid
generic certificates; the runner and aggregate controls reject optimized
acceptance. The earlier accepted v1 public/suite hashes were
`d8863194d6762aa2bdd838bd819c9de8ec8354ad703432f767b1f6e90a05ca74`
and `95043c40a323744b2431ef88e646de5c3905746c2f0fb3d6bc4a51b07451a41d`.
The code owner's v2 inventory records the deliberate additions and final
hashes; no previously accepted API semantics were changed.
