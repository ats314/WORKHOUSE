# Independent review of the conditional quantum path covariance

6 September 2026. Outputs-only review; existing canonical proofs and sealed
runs were not modified.

## Analytic acceptance

The arguments in `CONDITIONAL_QUANTUM_PATH_COVARIANCE.md`, sections 1–6,
are accepted with the fixed-block-scale scope stated there.

1. **Complete conditional precision.** Completing the Gaussian square on
   `F=ker W*` gives covariance `(1/2)(Q_F Omega Q_F|F)^(-1)`, embedded
   into the full space. It is not `Q_F Omega^-1 Q_F/2`. The proposed
   conditioning formula has range exactly F, annihilates W and is the
   inverse of the compressed precision there. These properties establish
   the identity without an invariance assumption on F.

2. **Full form bound.** From `K>=kappa Q_F`, functional calculus yields
   `sqrt(v²K+rho²I)>=sqrt(v²kappa+rho²)Q_F+rho(I-Q_F)`.
   The weaker bound used in the note follows immediately. The conditional
   Gaussian Poincare constant is correct because its covariance and the
   Dirichlet form both contain the factor one half. Integrating over the
   marginal bounds the entire literal orthogonal complement. This agrees
   with the existing inverse-frequency Wick source, and does not replace
   that Fock source by the Euclidean coordinate subspace.

3. **Principal pole cancellation.** Replacing W by its principal-matched
   graph `(I;V)` preserves its range. On the transverse principal space,
   `G=omega0^-1 I+V*C_hV`; direct substitution gives every block in (5).
   Extending Z as identity on the unused longitudinal direction is
   harmless because A and V* have transverse range. In particular the
   principal block is `A(I+omega0 A)^(-1)`, not a residual pole.
   At zero momentum the extra fine harmonic dimension and extra coarse
   harmonic dimension cancel: the fast fiber has dimension `2L³-2` both
   at zero and nonzero momentum. The continuous conditioned symbol is
   consistent with that count. A positive conditional fiber precision at
   zero regulator does not construct a massless joint flat-mode vacuum.

4. **Summability.** For fixed L, the high ratios are analytic and vanish
   to at least first order. The frame-free principal projection has
   derivative bounds of order `|K|^-|alpha|`, so V has conormal order
   one and A order two. For bounded `rho/v`, derivatives of the principal
   frequency of positive order have order `|K|^(1-|alpha|)`, uniformly
   down to zero regulator. Differentiating the inverse defining Z is
   legitimate and gives the claimed order-two remainder. Applying these
   estimates to all four blocks, and conjugating by the smooth unitary
   alias-to-block matrix, gives the order-one estimate (9).

   A radius-lambda annulus has remainder L1 norm O(lambda^4) and fifth
   derivative L1 norm O(lambda^-1). Five integrations by parts and the
   dyadic sum give O((1+|x|)^-4), not a logarithmically weakened exponent.
   The exponent exceeds dimension three. Absolute Fourier convergence
   justifies exact finite-torus sampling/periodization and the uniform
   row sum. No hidden volume factor enters. The constants in this
   derivative argument can depend on L; the separately proved operator
   norm constant cannot be substituted for those derivative constants.

5. **Failure of exponential locality.** At L=2 the high/principal ratio
   is `-i tan(K1/4)`. Including the conjugation in the source symbol and
   the minus sign in the mixed conditioning block gives exactly the
   phase in (12). Its yy homogeneous term has directional values
   `1,0,1/2` along `(1,0,0),(0,1,0),(1,1,0)`. These violate linearity
   of any derivative at zero. A smooth invertible change from aliases
   to fixed block coordinates cannot repair non-differentiability.
   Exponentially summable coefficients would give an analytic symbol,
   so the claimed obstruction follows, including positive regulator.
   It concerns this full transverse coordinate covariance, not every
   possible curl observable or locally gauge-repaired covariance.

## Primary provenance

I read the actual arXiv v3 source. Dimock's straight-path average in
equation (189) has normalization Q=R/L after block origins are matched.
Equations (304)–(307) condition a gauge-fixed second-order precision;
their exponential estimates (308)–(309) do not transfer by substituting
the square-root equal-time quantum precision. The draft accurately
identifies the common algebra and the different operator. Its new
summability theorem is supported by its own derivative proof.
[Dimock, sections 3.1 and 3.7.3](https://arxiv.org/html/1712.10029v3).

## Final exact-control snapshot

Final proof/checker/report SHA256:

- Proof: `53977ffd2dc929262269493895fc168ad1ff3b139cb15f8585c64c6d887d438d`.
- Checker: `05915339f8f2fca21f328c6cfe7e73b992c89a124dfb7463628f59feb0e9ea93`.
- Frozen report: `7e31229014934e4286c8f3a8927264c9376e5ac9bafebf2fecfae803690eea91`.

The complete three-family report was independently replayed in a fresh
Python process with NumPy/SciPy imports blocked and bytecode writes
disabled. Source and report hashes matched before and after. The evidence
is `INDEPENDENT_COVARIANCE_REPLAY_VALIDATION.json`.

The checker was fully read. Its noncommuting rational t-family verifies
both independent inverse formulas, every block and the claimed powers,
and rejects replacing conditioning by covariance compression. Its actual
Q(i) alias calculation keeps all 14 fast physical dimensions and compares
all 23 relevant ambient rows, including retained longitudinal zero rows.
The directional test checks the actual phase and the failed derivative.
The final scalar Gaussian control also checks the covariance/Dirichlet
factor one half. Its finite scope matches the proof's evidence boundary.

The final additions concerning fixed-color component row sums and fast
fiber rank are accepted. The analytic acceptance is independent of the
finite examples; no all-size derivative bound is claimed as machine-proved.
