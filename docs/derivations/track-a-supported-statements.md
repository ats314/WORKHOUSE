# Supported Track A statements and their formal scope

9 September 2026. This successor records the supported mathematical content of
the supplied W6/SC17/G17 completion report. The
[received drafts and arithmetic outputs](../../runs/track_a_formalization_2026-09-09/source_manifest.json)
are preserved byte-for-byte. Their original completion language is historical
evidence, not the current conclusion. Use the generated
[proof map](../derivation_formalization.md) for precise Lean links and the
[run record](../../runs/track_a_formalization_2026-09-09/README.md) for verification.

The statements below distinguish complete abstract theorems from the additional
identifications needed for the interacting Wilson model. Bounded operators on
an arbitrary real Hilbert space are allowed; no finite-dimensional restriction
is implicit. An unbounded generator still requires a justified form-domain
realization. A conditional theorem proves its implication without establishing
every hypothesis for a particular physical model.

## W6-V: actual variational residual identity and dual energy

Source: [W6 continuation, R1–R4](../../runs/recent_research_integration_2026-09-09/sources/w6_continuation_20260909/W6_PATH_FORWARD.md).

Let A0, Ag, R0, Rg be bounded linear operators on a real Hilbert space, with
A0 R0=I and Ag Rg=Rg Ag=I, and Ag symmetric. For a source t set
u=R0 t and rho=Ag u-t. Then

\[
\langle t,(R_g-R_0)t\rangle
=-\langle u,(A_g-A_0)u\rangle+\langle\rho,R_g\rho\rangle.
\]

An energy coordinate U is a continuous linear equivalence. For a continuous
functional f define its actual energy dual norm as `||f o U^{-1}||`.
If `kappa ||Uv||^2 <= <v,Ag v>` and kappa>0, then

\[
0\le\langle\rho,R_g\rho\rangle
\le\|\langle\rho,\cdot\rangle\|_{\ell^*}^2/\kappa.
\]

If Ug exactly represents the interacting bilinear energy, its dual norm squared
equals this inverse energy. These identities do not require commuting operators.

## W6-F: bounded-operator factorization controls the residual functional

Source: W6 continuation, R5–R6, and the
[received W6 note, section 3](../../runs/track_a_formalization_2026-09-09/sources/paper/research_notes/G19_W6_CUBIC_RESIDUAL_BOUNDS_20260910.md).

For continuous linear maps X from the source space, Y from the fast Hilbert
space, and K on the factor space, define the actual continuous functional

\[
f_p(v)=g\langle K Yv,Xp\rangle.
\]

Under `||Xp||^2 <= C_B b[p]`, `||Yv||^2 <= C_L ||Uv||^2`,
and `||K||^2 <= K_F`, with nonnegative budgets, its lower-energy dual norm is
bounded by `|g| sqrt(C_B C_L K_F) sqrt(b[p])`.
This proves the factorization implication. Identifying this functional with
the complete interacting Wilson residual is an additional obligation.

## W6-E: sufficient selected-inverse error certificate

Under W6-V, suppose the absolute value of the actual diagonal difference is bounded by
`a |g| b[p]`, the actual residual dual norm is bounded by
`c |g| sqrt(b[p])`, and `|g|<=g0`, with c,b[p]>=0. Then

\[
|\langle t,(R_g-R_0)t\rangle|
\le(a+\kappa^{-1}c^2g_0)|g|b[p].
\]

W6-F supplies c when its factorization has been realized. The diagonal estimate,
coercivity fraction, and model-specific factorization constants must be proved
independently; they are not consequences of a Gaussian coefficient alone.

## W6-C: exact Gaussian coefficient substitutions

Source: [dynamic fiber covariance, equation 16](../../paper/research_notes/G19_DYNAMIC_FIBER_COVARIANCE_AND_CUBIC_ENERGY_20260906.md)
and the received W6 note, section 2. For L>0, put
`c_spec=1/(sqrt(33)L)`, `a_spec=c_spec/2`, `sigma_bar=1/(2c_spec)`. Then

\[
9/a_{\rm spec}=18\sqrt{33}L,\quad
18\bar\sigma/(a_{\rm spec}+c_{\rm spec})=198L^2,\quad
6\bar\sigma^2/(a_{\rm spec}+2c_{\rm spec})=99\sqrt{33}L^3/5.
\]

The floating-point values obtained by assigning Sbar=4pi/3 and C_B=C_L=1
remain evaluations at chosen inputs. These identities do not certify those
inputs as uniform bounds for the interacting model.

## SC17-R: Riccati roots and the continuous barrier

Source: [SC17 spatial closure, Part III.2, R4–R9](wilson-sc17-spatial-closure.md).
For beta>0, c>=0, `4 beta^2 c<1`, define

\[
r_-=(1-\sqrt{1-4\beta^2 c})/(2\beta).
\]

Then r_minus>=0, `beta r_minus^2+beta c=r_minus`, and
`2 beta r_minus<1`. For T>=0, a continuous real function M on [0,T], initially zero,
that satisfies `M(t)<=beta M(t)^2+beta c` cannot enter the forbidden interval
between the two roots, hence stays below r_minus. The proof uses continuity
and the intermediate value theorem; the desired upper bound is not an input.

For `c=delta/(2 epsilon)`, this is the algebraic and continuity mechanism
in the source. When `1/(2 beta)<=a`, it also gives `r_minus<a`.
Deriving R8 from the actual ground-transformed Duhamel equation, with its stated
regularity and conservative Markov evolution, remains a separate realization.

## SC17-B: constructed noncommutative Banach-algebra fixed point

Let A be a complete real normed algebra, S a bounded continuous linear map,
and D an element. Suppose `||S||<=beta`, `||D||<=d`, with beta>0, d>=0
and `4 beta^2 d<1`. Choose r=smallRoot(beta,d) from SC17-R; then
`beta(r^2+d)=r` and `2 beta r<1`. The map

\[
T(X)=S(X^2-D)
\]

preserves the closed radius-r ball and is a contraction there. Consequently
there exists a unique fixed point in that ball. The norm estimate and the
Lipschitz estimate are proved without commutativity, using
`X^2-Y^2 = X(X-Y)+(X-Y)Y`.

This constructs the abstract quadratic solution. It does not assert that an
arbitrary fixed point equals the physical Hessian, or supply a weighted Schur
Banach completion or a model-specific inverse S.

## SC17-P: exact interval arithmetic under the proposed inputs

Source: [preserved SC17 comparison script](../../runs/track_a_formalization_2026-09-09/sources/scripts/sc17_quantum_defect_check.py).
With L=3, C_s=6/5, a_min=1/(3 sqrt(33)), beta=108 sqrt(33)/25, and
`delta/epsilon=lambda sqrt(lambda)/24`, the comparison parameter is increasing
for lambda>=0. On `0<=lambda<=3/100`,

\[
p(\lambda)=2\beta^2\lambda\sqrt\lambda/24
\le96228\sqrt3/625000<1,\qquad
2\beta a_{\min}=72/25>1.
\]

This gives a positive conditional root margin on the full interval, not only
the seven sample points. The complete defect and semigroup estimates are
still hypotheses. A quartic Taylor coefficient does not supply the outside
pressure, metric, projector, and cutoff terms of R12–R14. The source's
polynomial spatial norm does not imply exponential spatial decay.

## G17-P: corrected raw partition estimate for actual probability measures

Source: [received G17 note, equations 9–14](../../runs/track_a_formalization_2026-09-09/sources/paper/research_notes/G17_HAMILTONIAN_OSTERWALDER_SEILER_TRANSCRIPTION_20260910.md),
with its source-independent constant corrected here.

For a probability measure mu, an almost-everywhere measurable real source f,
and an almost-everywhere bound `|f|<=b`, the exponential is in every Lp and

\[
\int e^{\alpha f}\,d\mu\le e^{|\alpha|b}.
\]

For a finite family of sources with `|V_p|<=1/2`, the sum has b=m/2, so
the raw tilted ratio is bounded by `K_alpha^m` with
`K_alpha=exp(|alpha|/2)`. No cluster expansion or physical-gap assumption is
needed for this weak inequality.

## G17-V: centered L2 source, variance, and bounded footprints

For the same probability space, write `Y=exp(alpha f)` and
`QY=Y-integral Y`. The centered vector is an actual member of L2, orthogonal
to constant functions, with

\[
\|QY\|_2^2=\int Y^2\,d\mu-(\int Y\,d\mu)^2.
\]

The range bound and Popoviciu's variance estimate give
`||QY||_2 <= sinh(|alpha|b)`. For a nonempty footprint of cardinality
`m<=Gamma0` with b=m/2, the radius `||QY||_2/sqrt(m)` is bounded by
`(|alpha|/2) sqrt(Gamma0) exp(|alpha|Gamma0/2)`.
The restriction on m is part of the theorem. Identifying Q with the physical
vacuum projection requires the normalized probability representation.

## G17-O: strict obstruction to a constant equal to one

If f is bounded, centered, and has positive second moment, then for real
alpha!=0,

\[
\int e^{\alpha f}\,d\mu>1.
\]

The proof uses the strict tangent inequality for the real exponential on a
set of positive measure. The hypotheses `integral f=0` and
`integral f^2=1/16` specialize this theorem to the moment data in the SU(2)
example. The construction of SU(2) Haar measure and derivation of those moments
are not included in this formalization and remain explicit inputs to that
specialization. The preserved beta-only proposed constant equals one at beta=0,
so it is incompatible with any such source.

A concrete symmetric two-atom probability measure on the real numbers, with
atoms at +/-1/4, instantiates this generic obstruction. It is not identified
with SU(2) Haar measure.

## G17-I: independent product sources have unbounded radius

For an actual finite product measure of n copies of mu, Fubini proves

\[
\int\exp(\alpha\sum_{i=1}^n V(x_i))\,d\mu^{\otimes n}
=M(\alpha)^n,\qquad M(\alpha)=\int e^{\alpha V}\,d\mu.
\]

Thus the centered second moment is `A^n-B^n`, where
`A=M(2alpha)` and `B=M(alpha)^2`. If `A>B>1`, then
`(A^n-B^n)/n` tends to infinity. The proof gives the quantitative lower bound
`(A^(n+1)-B^(n+1))/(n+1) >= (A-B)B^n`.
For bounded V the centered moment is the actual squared L2 source norm.
Independence therefore does not establish a radius uniform over all footprints.

More strongly, for a measurable, pointwise bounded V on a probability space,
alpha!=0, zero mean, and positive second moment, the strict inequalities A>B>1
follow from G17-O. The actual product-measure variance divided by n then tends
to infinity. A globally clipped representative of the two-atom source gives a
fully constructed example satisfying the pointwise bound.

## Remaining model obligations

The report's unconditional W6 closure, full Wilson Hessian-defect bound,
exponential spatial decay, Hamiltonian transcription and uniform physical gap
are not conclusions of the statements above. Their missing realization steps
remain in the original derivation groups. The repaired finite-footprint and
conditional results must be applied only within their explicit hypotheses.
The graph retains both the original sources and these precise successor
statements, with distinct whole-statement and supporting-proof links.
