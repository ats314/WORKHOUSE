# Independent actual local true-ground score audit

5 September 2026. Read-only analytic audit of
`TRUE_GROUND_LOCALIZED_WILSON_SCORE.md`. All earlier canonical proofs and
sealed evidence remain unchanged.

The proof is accepted on its fixed-SU(2), fixed rescaled coarse chart and
additive-copy scope. Its derivative argument uses the actual joint ground,
not the constrained vertical ground or the raw Wilson conditional density.

The high-derivative step was checked in detail. The polynomial-Gaussian
coefficient equations can be solved to any fixed order because the oscillator
ground is simple and its complementary eigenvalues are separated. The
order-g forcing kills the product ground exactly, so the first eigenvector
correction is zero. A fixed original-chart cutoff leaves a superpolynomially
small Gaussian residual. The actual isolated scaled ground and the spectral
theorem give arbitrary prescribed L2 precision by choosing the expansion
order sufficiently high.

To pass from L2 to derivatives, the global original-coordinate elliptic
estimate applies to the fixed smooth electric operator. The error equation
has a bounded smooth potential with coefficients of order g^-4 after the
electric term is isolated. Each fixed bootstrap step therefore loses only
a fixed power of g. Residual derivatives, coordinate pullback and polynomial
fiber weights likewise lose only finitely many powers. Choosing a higher
finite expansion order compensates for every loss required here. Coarse
Sobolev embedding with fiber-L2 values supplies the uniform fixed-Q bounds.
The same global argument controls the exact ground outside the original
fiber cutoff. Neither an unjustified unbounded multiplier on an L2 error
nor a pointwise lower bound for the ground is used.

The conditional normalization is in Hilbert space. The rescaled marginal
norm stays positive on a fixed Q ball because the leading Phi_Q is positive
there. Projecting its coarse derivative perpendicular to the normalized
fiber vector cancels the scalar Phi_Q derivative. This yields
partial_Q phi_g=O(g²), including the scaled fiber derivative and polynomial
fiber weights needed by the horizontal calculation.

The leading constants also check independently. With X=sqrt(2)g Q and
F=exp(g Z/sqrt(2)), the exact residual r_E=(7/24)[X,E]+O(X²) becomes the
flat fiber velocity (7/12)[Q,E]+O(g). Since
Phi_Z is proportional to exp(-|Z|²/(2sqrt(5))),

```text
D_E phi_g = -7/(12sqrt(5)) <[Q,E],Z> Phi_Z + O_R(g).
I_g(E,F) = 4 <D_E phi_g,D_F phi_g>
         = 49/(72sqrt(5)) <[Q,E],[Q,F]> + O_R(g).
```

Here E(ZZ*)=sqrt(5)I/2. The flat derivative includes the half-density
divergence term; its leading constant vector has zero divergence, and the
weighted derivative estimate bounds the remainder. C_uu=6I+O(g²), giving
the stated weighted coefficient 49/(12sqrt(5)). This is a bounded Fisher
matrix on fixed Q compacts and makes no assertion at the remote center.

The class-source strengthening is exact in its geometric premise. If E
commutes with U (equivalently X in the chart), both b(U)E and the square-root
velocity equal E/2, so r_U(E)=0 exactly and C_uu E=6E. A class-function
gradient has this property. Its conditional score contraction is therefore
O(g), yielding a relative cross-vector norm O(g²); the actual fast inverse
contributes another g². Thus the selected class-source Schur loss is O(g⁴).
Common-Gauss pair sources have only the total Gauss constraint and retain
the correctly stated O(g²) relative bound.

The complete source-frame step is sound: fixed finite rescaled cutoffs
retain nonzero local radial and adjoint overlaps, while the established
complete fine spectral classification and exact excitation supports give
the entire onto frame, uniformly in finite/countable additive-copy number.
Centering a radial cutoff changes no gradient support. Local conditional
score covariance is diagonal across independent factors, so arbitrary
source superpositions incur no volume factor. The countable extension uses
form-norm convergence and the uniform actual fast inverse.

The theorem does not identify this chosen chart with the complete marginal
spectral window, solve the high-retained complement of a static Schur gap,
or introduce ambient interactions. Those limits remain explicit and are
consistent with the separate endpoint-window comparison now under review.
The companion finite algebra controls check normalizations and cancellations;
they do not replace the analytic elliptic and countable arguments audited here.

## Final fixed-rank extension and byte-freeze amendment

The final proof SHA256 is
`92c90d38b44975a75fe5f69f483ef1fea2190385e345dc33d575d6ac05848f55`.
The final explicit class-source consequence and fixed-SU(N) extension were
read independently after the initial SU(2) review above and are accepted.
The same fundamental trace metric gives the isotropic quadratic potential
and frequencies in dimension d=N^2-1. The order-g forcing still annihilates
the invariant product Gaussian by [Q,Q]=0. Finite-order equivariant Hermite
recursion, the isolated physical ground and compact elliptic bootstrap use
only fixed N, with constants allowed to depend on N and the chart radius.
The Fisher leading term is correctly written as the adjoint Gram form
49/(72sqrt(5)) <[Q,E],[Q,F]> rather than the SU(2)-specific three-dimensional
cross-product matrix. Centralizer directions give the same exact geometric
class cancellation. The real irreducible adjoint and its unique invariant
bilinear form supply the stated radial/pair chart. No rank-uniform constant
or new interacting-volume statement is inferred.
