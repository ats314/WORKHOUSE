# From harmonic boundary coercivity to the entire literal quantum complement

5 September 2026. Outputs-only analytic successor. The theorem below closes
the gap between the established full harmonic matrix inequality and an
entire Gaussian quantum form bound for a precisely specified coordinate
source. It does not prove a nonlinear Wilson complement bound or identify
equal-time sources with an OS-history reducing range.

## 1. Exact Gaussian setup and source identification

Let E be a finite-dimensional real Euclidean space, K=K*>0, and
Omega=K^(1/2). Use the actual unit-kinetic oscillator

```
H_osc=-(1/2)Delta_q+(1/2)<q,Kq>,
H=H_osc-(1/2)Tr Omega=dGamma(Omega).                    (1)
```

Its normalized ground is proportional to exp(-<q,Omega q>/2); write it
as Phi. Its probability density Phi^2 has covariance (2Omega)^(-1).
For a linear observation L:E->Y, put S=ran L* and let P_S be its Euclidean
orthogonal projection. Redundancy in L is allowed: its Gaussian pushforward
measure is then supported on ran L, and zero-norm relations are quotiented.

The literal equal-time source isometry is

```
J f(q)=f(Lq)Phi(q),
J:L2(law(Lq)) -> L2(E,dq).                             (2)
```

In normal Fock coordinates,

```
<b,q>Phi=(1/sqrt(2))a*(Omega^(-1/2)b)Phi.
R=Omega^(-1/2)S,
ran J=Gamma_s(R_C),          P=Gamma(P_R), Q=I-P.       (3)
```

To justify the entire range, Wick-order arbitrary polynomials in Lq using
their actual marginal covariance. Their degree-n images span Sym^n(R_C).
Different Wick degrees are orthogonal and polynomial functions are dense
in the finite Gaussian marginal L2 space, including its supported quotient
when L is redundant. Thus the closure is exactly (3), not only its first
or second particle sector. In particular P contains the true vacuum.

## 2. The full matrix hypothesis and the inverse-frequency bridge

Assume the full form inequality

```
K >= kappa(I-P_S),          kappa>0.                   (4)
```

This is stronger than a compression inequality on S-perp; it retains
the arbitrary off-diagonal coupling to S. It is exactly the form already
proved for the planar box split and the three-dimensional Coulomb split.
Put c=sqrt(kappa).

Operator monotonicity of the square root on nonnegative matrices gives

```
Omega >= c(I-P_S).                                    (5)
```

For x in R-perp, let y=Omega^(-1/2)x. Equation (3) implies y in S-perp.
Applying (5) to y gives

```
<x,Omega^(-1)x>=||y||^2
 <=c^(-1)<y,Omega y>=c^(-1)||x||^2.
Q_R Omega^(-1) Q_R <= c^(-1)Q_R.                      (6)
```

There is no commutation assumption on K and P_S or on Omega and P_R.
The inverse bound is equivalent to the full one-particle form inequality

```
Omega >= c Q_R.                                      (7)
```

Indeed, (6) bounds ||Omega^(-1/2)Q_R||^2 by 1/c. The adjoint has the
same norm, so for any z,
||Q_R z||=||Q_R Omega^(-1/2)Omega^(1/2)z||
<=c^(-1/2)||Omega^(1/2)z||, which is (7). This step is a full-form
conclusion from a compressed inverse; it is not obtained by discarding
an off-diagonal block of Omega.

## 3. Entire Fock-space coercivity

Second quantization preserves form order. On each n-particle sector, sum
(7) over the n tensor factors and then restrict to symmetric tensors:

```
dGamma(Omega) >= c dGamma(Q_R) = c N_Q.                (8)
```

Under Gamma(E_C)=Gamma(R_C) tensor Gamma(R_C-perp), N_Q counts the quanta
in the second factor. Its zero eigenspace is Gamma(R_C) tensor vacuum,
and every other eigenvalue is at least one. Thus

```
H >= c N_Q >= c(I-Gamma(P_R)) = c Q.                  (9)
```

For finite-dimensional E and positive Omega, H has form domain D(sqrt(N)),
where N is total number. Both sides of (8) are bounded in that form norm,
and finite-particle vectors are a form core, so (8)--(9) hold on the whole
closed form domain. The projection P commutes with N and therefore
preserves this domain, even though it generally does not commute with H.
Consequently the actual restricted quantum form on ran Q is closed,
densely defined and at least c. Equation (9) is stronger than this
compression bound: it holds for every full Fock-space vector.

No physical class-function factor two is inserted. A physical invariant
can contain one discarded adjoint quantum paired with a retained adjoint
quantum, so its energy need not be at least 2c.

## 4. The entire low-window literal source frame

Let Pi=1_[0,E_*](H) with 0<=E_*<c. On ran Pi, (9) gives

```
Pi Q Pi <= (E_*/c)Pi,
Pi P Pi >= (1-E_*/c)Pi.                              (10)
```

For the literal source isometry in (2), B=Pi J therefore satisfies
B B*=Pi P Pi >=(1-E_*/c)Pi. It is onto the entire low window, with
right inverse B*(B B*)^(-1) and inverse norm at most
(1-E_*/c)^(-1/2). This is the full low space, including every particle
sector and the true vacuum. The argument also applies to an infinite-rank
window whenever the same operator hypotheses have separately been defined.

The frame norm is the actual Gaussian marginal L2 norm in (2). It is
not a bound for unnormalized raw coefficients of a selected finite list
of loop observables. The source-frequency weight remains in that norm.

## 5. Restriction to the full physical invariant Fock space

Suppose a compact group G acts orthogonally on E, commutes with K, and
preserves S. Then it preserves R, and P=Gamma(P_R) commutes with the
Fock action. Both (9) and (10) restrict to the entire invariant physical
space Gamma(E_C)^G, without changing c.

The corresponding literal physical source range really is Gamma(R_C)^G.
Given any invariant vector in Gamma(R_C), approximate it by polynomial
source-vacuum vectors and Haar-average those approximants over G. The
average remains a polynomial in the retained coordinate components,
is invariant, and converges because group averaging is a contraction.
Equivalently each finite Wick degree gives all invariant tensors in
Sym^n(R_C). This includes higher invariant and orientation tensors;
it is not a claim that quadratic contractions alone generate every sector.

For Wilson tangent fields, the group action is the residual simultaneous
adjoint color action and the spatial matrices tensor with the identity
on the Lie algebra. This restriction does not restore the nonlinear local
gauge constraints or identify a prescribed nonlinear history map.

## 6. Actual three-dimensional harmonic application and the regulator

The established source
`paper/research_notes/G19_WILSON_THREE_DIMENSIONAL_HARMONIC_BOUNDARY_20260905.md`
uses the actual periodic link space

```
C=ker d0*,       K_C=d1*d1 on C,
S=ran(P_C B),    K_C>=kappa_L(I_C-P_S),
kappa_L=4sin^2(pi/(2L))>=4/L^2.                       (11)
```

B inserts componentwise normalized box indicators. The literal linear
observation on transverse link coordinates is L=B*|_C, so ran L*=S
exactly. Redundancy caused by Coulomb projection is handled as in (2).
The adjoint vectors P_C B use the global Green operator and may be
nonlocal. This is a specified coordinate source, not an unidentified
local Wilson-loop block.

The actual unit-kinetic tangent Hamiltonian has squared-frequency matrix
2 b_rho u K_C. Add a strictly positive squared-frequency regulator rho^2 I:

```
K_rho=2 b_rho u K_C+rho^2 I_C,          rho>0.
R_rho=K_rho^(-1/4) ran(P_C B).
```

Applying (9) gives, after subtracting this regulated Gaussian's own exact
vacuum energy,

```
H_rho >= sqrt(2 b_rho u kappa_L +rho^2)
            [I-Gamma(P_(R_rho))]
       >=sqrt(2 b_rho u kappa_L)[I-Gamma(P_(R_rho))].   (12)
```

The floor is uniform in the number of boxes and in rho>0. The same
constant gives the entire low-window literal physical source frame (10).
For fundamental SU(N), b_rho=1/2, so the regulator-independent floor is
at least 2sqrt(u)/L. In the stated physical conversion it is at least
2 c_H(a)/(La).

All harmonic cochain zero modes lie in S and remain retained. Their
regulated covariance diverges as rho tends to zero, and there is no
normalized unregulated Gaussian vacuum on those free Euclidean variables.
The uniform inequality does not construct one, nor a positive unregulated
full gap. An actual flat-sector quantization or an independently defined
representation is still required to take that limit.

This supplies the full quantum harmonic bridge explicitly left open in
Section 5 of the established three-dimensional note. Its other nonlinear,
locality and OS qualifications remain in force.

## 7. Planar application and the face-coordinate distinction

The planar source
`G19_WILSON_HARMONIC_BOUNDARY_COMPARISON_20260905.md` proves the full
K=CC* >= kappa_L(I-P_B), with every interface and exterior edge retained.
After division by sqrt(u), its actual face oscillator is

```
h_face=-(1/2)grad_phi* K grad_phi+(1/2)||phi||^2.
```

Here K is in the kinetic energy. Fourier exchange gives a unit-kinetic
coordinate xi whose one-particle source is K^(-1/4)B. Thus the theorem
applies to the electric-dual box-coordinate polynomial source. Restoring
sqrt(u) gives the full harmonic energy floor sqrt(u kappa_L)>=2sqrt(u)/L.

Literal arithmetic face averages instead create K^(1/4)B, as already
proved in Section 7 of that note. They cannot be substituted into (3).
A specifically weighted face source phi(K^(-1/2)B a) has the required
one-particle range K^(-1/4)S, but this modification is nonlocal and its
raw coefficient norm need not be uniform in the infrared. No theorem
about unweighted face averages is inferred from (11).

## 8. An exact physical counterexample to the wrong source weight

The distinction is substantive even when the full matrix hypothesis holds.
Take two spatial modes with

```
Omega=diag(1/100,100),       K=Omega^2,
S=span(100,1),              kappa=1.
```

Direct rational arithmetic shows K-(I-P_S)>=0, with determinant zero.
The correct coordinate source is Omega^(-1/2)S. Substituting the other
weight gives instead

```
R_wrong=Omega^(1/2)S=span(1,1).
```

Let psi be ten slow-mode quanta and let Q_wrong be the complement of
Gamma(R_wrong). The squared removed norm is 2^-10. Computing the exact
binomial occupation weights of Q_wrong psi gives

```
<Q_wrong psi,H Q_wrong psi>/||Q_wrong psi||^2
 =1/10 + (9999/20)/(2^10-1)
 =803/1364 <1.                                        (13)
```

Thus the claimed unit floor actually fails for the substituted source.
This is a full Fock-complement counterexample, not just a failure of a
matrix proof step.

It is physical as well: tensor the two spatial modes with a compact
simple adjoint color space and use any normalized degree-ten invariant
symmetric color tensor, for example the fifth power of the quadratic
contraction. Put all ten spatial factors in the slow mode. Projection
onto R_wrong acts only spatially, preserves that color tensor, and has
the same binomial weights and energy (13). Therefore the counterexample
lies in the entire invariant Fock space, including SU(N) for every N>=2.

The example is a generic exact Gaussian model illustrating the necessary
source distinction. It does not identify this particular two-mode matrix
with a specified finite Wilson incidence geometry.

## 9. Optional exact fixed-regulator Schur realization

For finite E and positive Omega, choose 0<m<=Omega<=M. On particle sector
n>=1, mn<=h_n<=Mn. Since P=Gamma(P_R) commutes with total number, let
F_n=Q_n h_n Q_n and U_n=F_n^(-1)Q_n h_n P_n. Then

```
||U_n||<=M/m,
k0_n=P_n h_n P_n-P_n h_n Q_n F_n^(-1)Q_n h_n P_n,
mn<=k0_n<=Mn on ran P_n.                              (14)
```

The lower bound is obtained by minimizing h_n[p+q]>=mn(||p||^2+||q||^2)
over q. On the vacuum sector take U_0=0 and k0_0=0. Direct sums define a
bounded U, and U preserves D(sqrt(N)). The form k0 is closed on the
retained D(sqrt(N)) because its sector bounds are (14). Sectorwise square
completion gives

```
h[p+q]=k0[p]+||F^(1/2)(q+Up)||^2,                     (15)
```

with the exact triangular domain p in D(k0), q+Up in D(F^(1/2)). This
equals the original D(sqrt(N)) split because U preserves that space.
The hypotheses of the infinite-retained-space form-Schur theorem are
therefore realized for this actual regulated Gaussian Hamiltonian.

The bounded induced mass I+U*U preserves number sectors and its bounded
inverse square root preserves D(sqrt(N)); the normalized static Schur
operator and graph source are well-defined. The true vacuum is fixed
because U_0=0. No global L2 bound on F^(1/2)U is asserted: that operator
can grow as sqrt(n). This full-Fock Schur operation is not identified with
second quantization of the one-particle Schur operation. Nor is M/m uniform as the regulator is removed or
the smallest frequency tends to zero. These facts do not affect (9)--(12).

## 10. Evidence and remaining scope

`check_entire_gaussian_literal_complement.py` verifies rational positive
square-root chains with noncommuting retained projections; the compressed
inverse and full frequency inequalities; tensor-sector number bounds;
the physical wrong-weight counterexample (13); and regulated zero-mode
examples. It preserves all matrices and exact margins for replay.

The all-size implication is the analytic chain (4)--(9), applied to the
already established incidence/Hodge theorem. The finite examples do not
prove square-root operator monotonicity or Fock density by sampling.
The Gaussian history range generally contains more frequencies than its
equal-time range (3). Generated memory, nonlinear Wilson comparison,
flat-sector quantization, local loop-source identification and a continuum
mass remain distinct questions.
