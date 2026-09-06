# Independent audit of the entire Gaussian literal complement

5 September 2026. Accepted source snapshot:
`ENTIRE_GAUSSIAN_LITERAL_COMPLEMENT.md`, SHA256
`e578fcab11c7cd9f291d316d824da96a3abf0bea1e62b2b71c1071fc19950575`.
This is an analytic review. No canonical input or sealed run was changed.

## 1. Full one-particle inequality

The proof of the main implication is correct without commutation assumptions.
K>=kappa Q_S and operator monotonicity give Omega>=c Q_S with c=sqrt(kappa).
The actual coordinate source creates the subspace R=Omega^(-1/2)S. If x is
orthogonal to R, then y=Omega^(-1/2)x is orthogonal to S. Consequently

    c <x,Omega^-1 x> = c ||y||^2
       <= <y,Omega y> = ||x||^2.

This compressed inverse bound controls the norm of Omega^(-1/2)Q_R; the
adjoint has the same norm. Applying the adjoint to Omega^(1/2)z proves

    ||Q_R z||^2 <= c^-1 <z,Omega z>.

Thus the conclusion Omega>=c Q_R is a full form inequality. It is stronger
than compression of Omega to R-perp and is obtained without discarding
off-diagonal blocks. The original full K inequality is essential: a lower
bound only on the compression of K to S-perp does not supply this proof.

## 2. Full Fock range, physical sectors and domains

Marginal-covariance Wick polynomials in the observation coordinates generate
Sym^n(R_C) in every degree. Gaussian polynomial density, with redundant
observation directions quotiented, identifies the complete literal source
range with Gamma_s(R_C). It contains the true ground exactly.

Summing the full one-particle inequality on tensor factors gives
dGamma(Omega)>=c dGamma(Q_R). The latter number operator is zero precisely
on Gamma_s(R_C) and at least one on its orthogonal complement. Therefore
the full quantum form is at least c(I-Gamma(P_R)), on all particle sectors
and their closed form sum. Since finite positive Omega gives form domain
D(sqrt(N)), the stated core and projection preservation are sufficient.

The entire low-window frame follows by compressing this full form inequality.
Its lower bound is on B B*=Pi P Pi; the displayed bounded right inverse
therefore proves surjectivity even when an independently defined low window
has infinite rank. It does not mistake source injectivity for totality.

If the compact physical group commutes with K and preserves S, all operators
preserve its invariant space. Haar averaging polynomial approximants gives
the whole invariant source range, including higher invariant tensors.
The absence of a universal class-sector factor two is correct.

## 3. Geometric applications and the regulator

The periodic original-link theorem supplies the full K_C>=kappa_L Q_S,
with S=ran(P_C B). The observation B* restricted to the transverse space
has exactly this adjoint range. This respects Hodge/Bianchi constraints;
it does not replace constrained links with independent plaquette variables.

Adding rho^2 I gives
K_rho >= (2 b_rho u kappa_L+rho^2)Q_S. Thus the stated quantum floor and
source frame hold uniformly in box count and rho>0 for the regulated
Gaussian's own ground representation. The retained torus zero directions
still have diverging covariance as rho tends to zero. The proof does not
assert a normalized unregulated Gaussian vacuum or full positive gap.

The planar distinction agrees with Section 7 of the pinned predecessor:
electric-dual box coordinates create K^-1/4 B, whereas literal arithmetic
face coordinates create K^1/4 B. The specially weighted face source has the
required range but is nonlocal and retains its infrared normalization issue.
This theorem is not silently transferred to unweighted loop averages.

## 4. Physical wrong-source counterexample

I independently recomputed the two-mode example. For
Omega=diag(1/100,100), S=span(100,1), the matrix
K-(I-P_S) is positive semidefinite with determinant zero. The substituted
source Omega^(1/2)S is span(1,1), while the correct source is span(10000,1).

For n slow quanta, write p=2^-n for the squared retained projection.
The projected vector has mean energy n(omega_s+omega_f)/2, and the original
vector is an exact eigenvector of energy n omega_s. Hence the complementary
Rayleigh quotient equals

    n omega_s + n(omega_f-omega_s)/(2(2^n-1)).

At n=10 it is 1/10+(9999/20)/1023=803/1364<1. This refutes the actual
complement floor for the wrong source, not merely a proposed matrix proof.

The invariant-color strengthening is valid. A nonzero degree-ten symmetric
adjoint invariant exists for every stated compact simple color action,
for example the fifth power of its invariant positive quadratic form.
Tensoring it with the spatial slow vector in all ten slots gives a bosonic
physical invariant. The source projection acts only spatially, so its norm,
binomial occupation weights and energy are exactly those just computed.
No SU(N) exception occurs at N=2. The example remains a generic Gaussian
model, not a claimed realization by a particular Wilson incidence complex.

## 5. Fixed-regulator Schur realization

The number-sector construction is correct. From mn<=h_n<=Mn, the inverse
of the complementary block is at most 1/(mn), so ||U_n||<=M/m. This bound
is independent of particle number. Minimization gives mn<=k0_n<=Mn on
the retained sector. Direct sums yield bounded U preserving D(sqrt(N)),
closed k0 on the retained number-form domain, and the exact triangular
domain for square completion. The bounded positive induced mass and its
inverse square root preserve that same number-form domain.

The vacuum is fixed. No global L2 bound on F^(1/2)U or uniform M/m as the
smallest frequency vanishes is needed or asserted. These qualifications
are compatible with the regulator-independent complement floor itself.

## Scope of acceptance

All ten sections are accepted at their stated finite-dimensional Gaussian,
specified regulator, physical-invariant and geometric-source scopes.
The all-size conclusion follows analytically from the existing full
incidence/Hodge bound and the inverse-frequency/Fock argument. Finite
controls test the matrices and source distinctions, not operator monotonicity
or Gaussian density by sampling. Nonlinear Wilson comparison, local source
identification, temporal histories and flat-sector quantization remain
separate obligations.

## Final source and control freeze

The author subsequently clarified two existing scope points: Section 7
explicitly divides the face oscillator by sqrt(u) before restoring that
energy factor, and Section 9 explicitly distinguishes full-Fock Schur
elimination from second quantization of a one-particle Schur operation.
I read and accepted both changes. The final accepted proof SHA256 is
`35172fb21b341d52975bb2c3abc3fcd49a15dbda8d444fb3e0191077523bef01`.
The preceding audit retains the earlier snapshot identifier to show which
version received its original full read.

The final original checker SHA256 is
`bc57649b314ce6b78c30a0588d70d7197bec959be2434bef32b3ba27fb2505f5`;
its saved JSON SHA256 is
`0f83b7bbfb6f5bd07156033768ff4af121958929d0f16c5952e0c05d67b58b15`.
I inspected its five payload families: two exact noncommuting matrix chains,
ordered tensor inequalities through degree four, the complete 26-dimensional
window at energy 1/4, the ten-boson wrong-source complement, and rational
regulated zero-mode examples. Zero-pivot PSD conditions are retained. The
ordered-tensor inequalities validly restrict to symmetric bosons; the
all-degree theorem is analytic. The color-polynomial check is explicit SO(3)
finite evidence, while the all-group invariant lift is the analytic argument.

The independent original-payload replay under `next_publication/run_plan/`
compares the complete final payload and every declared source pin with
NumPy/SciPy imports blocked. It does not assemble a canonical run or claim
that finite examples alone prove the entire Fock statement.
