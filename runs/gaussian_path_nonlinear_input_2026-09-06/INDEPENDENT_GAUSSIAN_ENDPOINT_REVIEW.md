# Independent review of the Gaussian path endpoint baseline

6 September 2026. Outputs-only review by the independent merge-consistency
agent. Canonical sources and all previously sealed runs were read-only.

## Mathematical outcome

The complete derivation in `EXACT_GAUSSIAN_PATH_ENDPOINT_BASELINE.md` is
accepted. This review checked the actual marginal normalization, full
Fock-space domains, both transverse polarizations, the complete low-window
count, row-Gram locality and the coupled physical counterexample. The final
source/control snapshot and replay evidence are recorded below when frozen.

### Exact endpoint and complete window

The coordinate ground covariance is `(1/2) Omega^-1`, while the one-particle source map is
`j=Omega^(-1/2) W (W*Omega^-1 W)^(-1/2)`. This distinction is used
consistently. Wick normalization gives `J=Gamma(j)`. Symmetric tensor
compression proves the endpoint identity on every sector; diagonalizing its
positive one-particle matrix and taking the closed direct sum proves the
logarithm identity. The spectral limit zero of the Fock contraction does
not invalidate its unbounded logarithm. The vacuum remains in its domain.
Compact-group invariance is imposed on the entire Fock space, so no
one-particle color vector is mistakenly treated as a physical singlet.

The inverse-frequency high-alias weight gives
`G_high <= (pi^8 |K|^3/3072) G_low`. This is an order stronger than the
unweighted squared source tail. Both matrix bounds follow as Loewner
inequalities before whitening, without assuming commuting Gram matrices.
On the clock `tau=sL/v`, the stated relative constant
`pi^9 |K|^2/(6144s)` follows from
`omega0 >= 2v|K|/(pi L)`. This checks both polarizations simultaneously.

For the full Fock window, `H0` is scalar on each polarization block and
commutes with the endpoint operator. Every occupied momentum in `H0<=E`
satisfies `|K|<=pi LE/(2v)`. Applying the relative bound to each occupied
quantum and summing gives the stated `delta_E`; no particle-number or
volume factor is introduced. When `E<2v/L`, all nonprincipal fine aliases
are absent from the complete fine window. The two min-max counts therefore
compare the complete endpoint and fine spectra with the threshold
conventions stated in the proof. This is not just a frame lower bound on
selected trial sources. Removing the three flat coordinates, or keeping a
positive regulator, is necessary for the Gaussian vacuum statements.

### Locality and genuine Gaussian obstruction

The fourth alias moment gives
`(RR*)_i=L^-1(A_L+B_L cos K_i)` with the stated exact coefficients.
`B_L/A_L<1/2` makes the Neumann and binomial series give the stated inverse
and inverse-square-root kernel bounds, including short cyclic periods.
These are bounds for the auxiliary unconstrained row Gram. They are not
bounds for the anchored map's full row Gram, the physical Coulomb-compressed
Gram, or the inverse-frequency true marginal Gram. The draft distinguishes
these operators explicitly.

For the actual `n=6,L=2,K=(2pi/3,0,0)` path, direct alias evaluation gives
weights `3/4,1/4` and frequency squares `1,3`. Rotating into its normalized
Euclidean source and orthogonal fiber gives the displayed nonzero precision
cross term. The conditional Fisher is thus a positive multiple of `g^-2`
even on a bounded source region. This is a Gaussian statement with its
specified physical clock, not an inferred nonlinear Wilson score bound.

The separate two-mode example verifies an actual static loss, rather than
inferring a lower bound from a Fisher upper bound. Direct Schur elimination
gives `6/5` and `96/37`, and graph normalization gives `15/14` and `444/191`.
Their failure of additivity shows why full-Fock static elimination cannot
be replaced by second quantization of the one-particle static Schur
operator. The normalized adjoint-color invariant pair vectors form the
same three-dimensional sector, so the two-boson counterexample is physical.

## Primary-source comparison

I read Dimock's actual arXiv v3 paper. Its equation (189) has the same
straight-path average with one additional factor `L^-1`; matching the block
origins gives `R=L Q`. Equations (304)-(307) use a constrained, gauge-fixed
second-order Laplacian precision, and (308)-(309) prove locality for those
covariances. They do not establish locality for the square-root quantum
ground precision used here. The draft's attribution and operator distinction
are accurate. This is a mathematical comparison, not a novelty criterion.
[Dimock, sections 3.1 and 3.7.3](https://arxiv.org/html/1712.10029v3).

## Exact-control review

The checker was independently read, including the later explicit
21-dimensional colored two-boson intertwining. It recomputes its five
families from exact symbolic matrices, tensor products, Gaussian
normalization and integer alias counts. The expected JSON is not used as
an input to those mathematical calculations. Its positive-matrix routine
checks exact Hermitian Schur pivots and the zero-pivot residual row. The
source pins and all payload fields are compared during replay. Existing
output and optimized execution are rejected.

The finite controls support precisely the identities described above:
tensor compression through three bosons, a noncommuting matrix sandwich,
one actual transverse path block, invariant pair normalization, and finite
row-Gram moments/inverse kernels. They do not machine-certify Wick density,
the closed logarithm domain, or all-size analytic estimates. Those have
been reviewed as arguments.

## Final snapshot and replay

Final reviewed SHA256 values:

- Proof: `fa237619dd29c63f04a02abea6a0061ba131a4ec9db347d989757762812bcea8`.
- Checker: `ea8f6787ca3e05ff2f832eb8d8a73929a28943d79a550810a7e276bb8c4b04ef`.
- `gaussian_endpoint_baseline_controls_frozen.json`:
  `20b16e37ad24b448150afdef257043acb9d7edb3d317cc23f40b595aadcfea4c`.

An independent fresh Python process replayed all five complete payload
families successfully with NumPy and SciPy imports blocked and bytecode
writing disabled. The three hashes were recomputed before and after the
replay and remained identical. The author's additional negative-control
report is `GAUSSIAN_ENDPOINT_VALIDATION.json`; this review does not relabel
those separately executed negatives as independent reruns.

The final source/proof chain is accepted. No canonical publication or
all-scale nonlinear conclusion is implied by this outputs-only review.
