# Scoped results and actual complement control from the M10 proof repair

11 September 2026. These proofs support the repaired
[derivation](../../docs/derivations/w6-synchronized-m10-domination.md).
Actual quantum full-fiber M10 is not proved. The final section establishes the actual centered complement estimate.

## Uniform action gap outside the full minimizing set

Let X=SU(2)^3 x SU(2) be the common compact (y,Q) space and let S be the
actual Agmon distance for the original electric metric from the unique well.
The calibrated center result S5 in the
[transport derivation](../../docs/derivations/w6-conditional-transport-obstruction.md)
proves min_y S(y,Q)=I(theta(Q)), with
I(theta)=32 sqrt(2)(1-cos(theta/8)). The distance S is continuous because
local weighted path lengths are bounded by a constant times the distance
of the smooth electric metric. Let Zmin be the complete zero set of
S-I(theta), including the entire sphere in the antipodal fiber.

For any open U containing Zmin with nonempty complement, X\U is compact
and the continuous function S-I(theta) is positive there. It attains a
strictly positive minimum kappa. Thus S>=I+kappa uniformly outside U.
This supplies the correct uniform complement geometry, with no asserted
numerical constant from the magnetic Hessian. It supplies neither weighted
parameter derivatives of the ground nor a normalized conditional score bound.

## Uniform reference angular and normal score budget

For lambda>=0, let t in [-1,1] have density proportional to
exp(-lambda(1-t)) dt. If lambda>0, x=lambda(1-t) has density proportional to
exp(-x) on [0,L], L=2lambda. Integration by parts yields

```
E x =1-L/(exp(L)-1) <=1,
E x^2=2-(L^2+2L)/(exp(L)-1) <=2.
```

The correction terms are nonnegative; at lambda=0, x is identically zero.
For independent z in R^7 with density proportional to exp(-|z|^2/g^2),
X=|z|^2/g^2 satisfies E X=7/2 and E X^2=63/4 by one-dimensional Gaussian
moments and independence. Hence E(X+x)^2<=63/4+7+2=99/4 for every lambda>=0.
This includes the whole weak-concentration/strong-concentration crossover.

If an actual tube submeasure is bounded above by M times this specified
reference probability, and sigma-beta=(X+x)/g+epsilon with actual
E[1_tube epsilon^2|Q]<=E0/g^2, the square inequality gives
E[1_tube |sigma-beta|^2|Q]<=(99 M/2+2 E0)/g^2.
The actual measure comparison and score-error estimate are additional
hypotheses, not consequences of the magnetic angular expansion.

## Verification scope

The companion invariant suite derives the moments exactly and checks the
endpoint limits. Compactness and conditional measure comparison are analytic
arguments. No whole-statement Lean formalization or actual-ground M10 closure
is claimed. The received overstatement is preserved in the repair run.

## Actual centered conditional complement theorem

The remaining R9 inputs can be obtained with arbitrarily small exponential
slack on the actual fixed compact square. This does not estimate the local
relative amplitude to polynomial accuracy, which remains a separate task.

Put h=g^2, P_h=h H_g=-(h^2/2)Delta_Gamma+V and lambda_h=h e_g. The prior
fixed-square results give a unique nondegenerate zero of V, ellipticity,
0<=e_g<=E, and the actual positive normalized ground with
`||partial_g Psi_g||_2<=C/g`. The local actual-ground comparison in S3 gives
a positive lower WKB bound on a sufficiently small fixed well neighborhood.
The latter is an undifferentiated comparison; no derivative of its remainder
is used below. The original-edge diffusion has smooth coefficients on the
compact manifold and principal cometric Gamma.

**Weighted numerator.** Fix a in (0,1) and Phi=(1-a)S. The Agmon eikonal
inequality gives `Gamma(Phi,Phi)/2<=(1-a)^2 V` almost everywhere. Lipschitz
weights are admissible in the quadratic-form identity. For
`(P_h-lambda_h)u=F` the identity is

```
(h^2/2) integral Gamma(exp(Phi/h)u)
 + integral (V-lambda_h-Gamma(Phi,Phi)/2) exp(2Phi/h)|u|^2
 = Re integral exp(2Phi/h) F conjugate(u).                 (R12)
```

Set c_a=1-(1-a)^2>0 and A_h={V<=2(E+1)h/c_a}. Since the well is unique
and nondegenerate, A_h is in the local well chart for small h and S<=C_a h
there. Thus exp(Phi/h) is uniformly bounded on A_h. Outside A_h the
coefficient in R12 is >=h, and everywhere it is >=-Eh. With
v=exp(Phi/h)u and f=exp(Phi/h)F, Young's inequality yields

```
||v||_2^2 <= 2(E+1)||1_(A_h) v||_2^2 + h^-2 ||f||_2^2.   (R13)
```

For the homogeneous ground equation, the undivided identity instead gives
`||exp(Phi/h)Psi_g||_2^2<=(E+1)||1_(A_h)exp(Phi/h)Psi_g||_2^2`, hence a
uniform bound. The established first-jet equation SF6 is

```
(P_h-lambda_h) partial_g Psi_g
 = (4/g)(V-<V>_(mu_g)) Psi_g.                             (R14)
```

V is bounded; therefore its weighted right side is O(1/g). Apply R13 and
the unweighted first-jet bound to obtain
`||exp(Phi/h)partial_g Psi_g||_2<=C_a g^-3`.
Rescaled interior elliptic estimates on balls of radius h upgrade these
bounds to pointwise bounds for Psi_g, its spatial first derivatives, and
partial_g Psi_g, losing only fixed powers of g. To see the uniformity,
rescale each ball to unit radius: h^2 Delta becomes uniformly elliptic,
V and lambda_h are bounded, and the right side R14 is a bounded smooth
coefficient times Psi_g/g. Bootstrap the ground equation and then R14.
The oscillation of Phi/h on a radius-h ball is bounded by the uniform
Lipschitz constant of S. A finite smooth atlas controls all constants.
For a fixed smooth dilation D this proves, for some finite N,

```
|Psi_g|+|N_g| <= C_a g^-N exp(-(1-a)S/g^2).                (R15)
```

The possible cut locus of S causes no loss: only a Lipschitz energy weight
and its oscillation on small balls were used, not a smooth global WKB phase.

**Lower ground bound.** For every b>0 there is g_b>0 such that, for all
configurations x and 0<g<g_b,

```
Psi_g(x) >= exp(-(S(x)+b)/g^2).                           (R16)
```

Here is a direct positive-ground argument. The diffusion X^h with generator
(h/2)Delta_Gamma satisfies the exact Feynman--Kac identity

```
Psi_g(x)=exp(T lambda_h/h)
 E_x[ exp(-h^-1 integral_0^T V(X^h_s) ds) Psi_g(X^h_T) ].   (R17)
```

It follows directly by Ito's formula and the ground equation; bounded
coefficients and compactness justify expectation and finite-time stopping.
Choose a small fixed well ball B on which the existing local comparison
gives `Psi_g>=exp(-epsilon/h)` for sufficiently small h. This follows by
choosing max_B S small and absorbing the positive local amplitude/polynomial
prefactor into an arbitrarily small further exponent.

For any starting point x, choose a finite-time smooth controlled path gamma
ending in the interior of B with

```
J(gamma)=integral_0^T (|dot gamma|_G^2/2+V(gamma)) ds
 <= S(x)+epsilon.                                       (R18)
```

Indeed take a smooth finite-length path whose Agmon length approximates S,
then reparametrize by speed sqrt(2(V+rho)), rho>0. Its time is finite and
its kinetic-plus-potential action tends to that Agmon length as rho tends
to zero. Smooth approximations preserve the arbitrarily small error. The
original spanning electric fields realize its velocity by deterministic
controls u(s) with sum |u|^2=|dot gamma|_G^2; use the smooth cometric inverse.

Under the controlled diffusion law the drift is the control field (plus a
bounded O(h) diffusion drift), and the path converges in probability uniformly
on [0,T] to gamma. This follows from the Ito isometry, the maximal inequality
and Gronwall in a finite atlas. Thus with probability tending to one its
endpoint lies in B and its integrated V differs by at most epsilon.
Girsanov's deterministic-control density of the original law relative to
the controlled law is

```
exp(-h^-1/2 integral_0^T u.dW -(2h)^-1 integral_0^T |u|^2 ds).
```

The deterministic finite-energy controls satisfy Novikov for each h>0.
The stochastic integral has fixed finite variance. Restrict further to
`|sqrt(h) integral u.dW|<=epsilon`; this event also has probability tending
to one. On the intersection the density is bounded below by
`exp(-(integral |u|^2/2+epsilon)/h)`. In R17, lambda_h>=0, so its prefactor
is >=1. For sufficiently small h the intersection has probability >=1/2,
which yields `Psi_g(x)>=(1/2)exp(-(S(x)+4epsilon)/h)`.
The controls and terminal ball continue to work for starting points in a
neighborhood of x; continuity of S and of controlled trajectories only adds
arbitrarily small action slack. A finite cover of the compact manifold makes
the h threshold uniform. Choose all slack allowances below b and absorb
1/2 for smaller h. This proves R16 with no claim of a polynomial relative
WKB expansion or uniqueness of a minimizing trajectory.

The probability inputs are the ordinary finite-time Feynman--Kac and
Girsanov identities; see Lawler, *Stochastic Calculus*, sections 4.3 and 5.3:
https://www.math.uchicago.edu/~lawler/finbook.pdf . The application above states
the controls, action normalization, endpoint lower bound and uniformity.

**Normalization and centering.** Uniform continuity of S on the common
compact fiber space implies that, for any b>0, a fixed-radius fiber ball
about any minimizer has `S<=I(theta)+b/2`. All such Haar balls have a uniform
positive volume c_b. Apply R16 with slack b/2 and integrate the square:

```
h_g(Q)>=c_b exp(-2(I(theta)+b)/g^2), uniformly in Q.        (R19)
```

Also, S is bounded on the compact manifold. Combining R15 and R16 shows
that for every d>0 there are C_d,N_d such that
`|sigma_g(x)|<=C_d g^-N_d exp(d/g^2)` uniformly in x.
Choose the common reference beta_g(Q)=sigma_g(y_*(Q),Q), where y_* is any
conditional minimizer. Such a measurable selection exists; at the antipodal
sphere the value is independent of the selected axis by exact gauge symmetry.
This beta obeys the same subexponential bound. R15 for Psi then implies,
by selecting the two arbitrarily small slack parameters sufficiently small,

```
|N_g-beta_g(Q)Psi_g|<=B_b g^-p_b exp(-(S-b)/g^2)            (R20)
```

for every prescribed b>0. This is uniform even if the reference center is
not continuous in Q. On smooth regular phase tubes it is exactly the beta
used in R2. R19 and R20 are R9 with r=0 and epsilon=b. Choose b<kappa/2
and apply R10: the actual centered conditional complement is exponentially
small outside U, uniformly in all fibers. This discharges the complement
hypothesis for the enlarged tubes and this common reference. It does not
bound the actual score on the tube or establish its polynomial amplitude
and normal/angular comparison estimates.

The resulting explicit bound is C*g^(-2p_b)*exp(-2*(kappa-2b)/g^2), with b<kappa/2. Absorbing the fixed polynomial into half the exponent gives Cprime*exp(-(kappa-2b)/g^2). All constants are uniform in Q and small positive g on this fixed block.
