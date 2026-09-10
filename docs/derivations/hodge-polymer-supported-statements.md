# Hodge and polymer ingredients with exact formal scope

10 September 2026. This successor states the mathematics retained from the
pending HodgeFeshbach and PolymerCluster formalizations. The original working
files and theorem registrations were preserved before correction. The
[integration record](../research/formalization-scope-2026-09-10.md) gives that
provenance and the validation boundary.

The analytic [Hodge result](../../paper/research_notes/G14_HODGE_FESHBACH_CHANNEL_20260908.md)
and its [scope correction](../research/september_feshbach_integration.md)
remain the physical incidence-algebra sources. Abstract consequences below
do not independently construct the Bloch incidence operators. The
[G17 transcription](../../paper/research_notes/G17_HAMILTONIAN_OSTERWALDER_SEILER_TRANSCRIPTION_20260910.md)
is a preserved attempted argument; its geometric series is not a proof of its
claimed Hamiltonian cluster expansion or free-energy estimate.

## H1: complementary kernels from Hodge relations

Let V be a module over a field K and let D,U be K-linear endomorphisms.
Assume D+U=qI and DU=0. Then D²=qD, UD=0 and U²=qU, by composing
D+U=qI on each side and subtracting. If q is nonzero, the kernels are
complementary and every vector has the decomposition

\[
v=q^{-1}Uv+q^{-1}Dv,\qquad q^{-1}Uv\in\ker D,\quad q^{-1}Dv\in\ker U.
\]

The intersection is zero because a vector killed by both operators is killed
by qI. The decomposition proves that the sum is all of V. This abstract
direct sum does not by itself establish orthogonality or verify a particular
lattice's incidence relations.

## H2: carrier action and absence of Hodge coupling

Under D+U=qI and Dψ=0, Uψ=qψ. Put S=D-4I. Then Sψ=-4ψ.
For any linear map Q with Qψ=0, all three vectors QDψ, QUψ and QSψ vanish.
No idempotence assumption on Q is required for this implication.

More generally, if Dψ=0 and Uψ=λψ, every finite word in D and U maps ψ
to a scalar multiple of ψ. Induction on the word proves this: a leading D
kills the scalar multiple and a leading U multiplies its coefficient by λ.
No assertion that ψ spans an entire kernel is needed. Separately, if
UQv=0 for every v, then UQRψ=0 for any linear R.

## H3: rank-one normalization, excitation and factorization

Let E be a real inner-product space, let q=⟨ψ,ψ⟩ be nonzero, and define

\[
Uv=\langle\psi,v\rangle\psi,\qquad
Pv=q^{-1}Uv,\qquad Qv=v-Pv.
\]

Thus U is the up-Laplacian normalization, while P is the normalized carrier
projector: Uψ=qψ and Pψ=ψ. For a continuous linear R and
φ=Rψ-⟨ψ,Rψ⟩ψ/q, inner-product linearity gives ⟨ψ,φ⟩=0. Consequently
both Uφ and Pφ vanish. Dividing U by q does not change its kernel but does
change its eigenvalue and the operator used in word products.

The rank-one factorization is an actual operator statement. For a linear R,

\[
RUR\psi=\langle\psi,R\psi\rangle R\psi,\qquad
\langle\psi,RUR\psi\rangle=\langle\psi,R\psi\rangle^2.
\]

Since ⟨ψ,Uψ⟩=q², its denominator-cleared scalar defect vanishes.
This does not assert that a perturbative Hamiltonian contains an RUR term;
the dynamical amplitude and cancellation require a separate calculation.

## H4: finite word patterns and supplied polynomial identities

There are 3+9+27=39 nonempty words of length at most three in S,U,R.
The Boolean pattern “two R letters with no U between them” selects exactly
RR, SRR, URR, RSR, RRS, RRU and RRR; it does not select RUR.
Enumeration verifies this syntactic statement. An equivalence between this
predicate and a nonzero evaluated Feshbach defect is additional mathematics.

For rational q,e₂,e₃, the supplied polynomials
r₂=q e₂+3e₃ and r₃=4e₂² satisfy

\[
r_2-qe_2=3e_3,\qquad q^2r_3-(-2e_2)q^2(-2e_2)=0.
\]

The supplied one-R expression
(-4)^nS (-2)^nR q^(nU+1-nR) e₂^nR evaluates at (nS,nU,nR)=(0,1,1)
to -2qe₂. The exponent is natural subtraction in this definition.
These substitutions do not derive the polynomials from lattice operators.
The native exact Laurent computation remains the source of those operator
identifications and of the actual fourth-order support theorem.

## P1: geometric-series majorant

For real 0≤x<1,

\[
\sum_{n=0}^{\infty}x^{n+1}=\frac{x}{1-x}.
\]

Multiply the convergent geometric series by x. The displayed quotient is
nonnegative, positive when x>0, and increasing on [0,1). The last assertion
follows by multiplying by the positive denominators. This is a scalar sum;
no partition function, pressure, polymer activity or free energy is defined
or bounded by this argument.

## P2: parameter bounds and the separate tree budget

For real D,β,c put x=(Dβ/4)exp(c). If D,β≥0, then x≥0.
If also c≥0, then (Dβ/4)^n≤x^n for every natural n, including zero.
The series with this x converges under x<1. At β=0 the parameter is zero;
if D>0, β₀=((D/4)exp(c))⁻¹ is positive and 0≤β<β₀ implies x<1.

The stronger scalar tree budget has a distinct threshold. For 0≤x<1 and
c≥0, multiplying by 1-x>0 and dividing by 1+c>0 gives

\[
\frac{x}{1-x}\le c\quad\Longleftrightarrow\quad x\le\frac{c}{1+c}.
\]

For c=1 this demands x≤1/2. The geometric radius x<1 alone supplies no
such budget. An actual polymer theorem further needs its activities,
incompatibility relation, counting bound and identification with the target
Hamiltonian or transfer model. An alpha-dependent moment bound and uniform
source-radius estimate remain the G17 transcription's separate obligations.
