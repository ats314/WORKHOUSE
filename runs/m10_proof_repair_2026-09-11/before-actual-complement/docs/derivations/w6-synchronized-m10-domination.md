# W6 synchronized M10: repaired criteria and remaining actual-ground estimate

Repaired 11 September 2026 after independent review of commit `85675ed`.
The received completion claim and scripts are preserved byte for byte in
[runs/m10_proof_repair_2026-09-11](../../runs/m10_proof_repair_2026-09-11/README.md).
The earlier all-fiber proof did not justify parameter differentiation,
conditional normalization, or the antipodal angular transition. The corrected
actual-model M10 status is **open**. This note proves the implications below
and identifies their unsupplied actual-ground inputs; it does not assert that
changing a status resolves the mathematical target.

## 1. Statement and scope

On the fixed four-face compact SU(2) block, let
`N_g=partial_g Psi_g+D Psi_g/g`, `sigma_g=N_g/Psi_g`,
`D=Z+(div_Haar Z)/2`, and `K_g(w)=Var(sigma_g|w)`.
The target is

```
K_g(w) <= C0+C1*g^-2 E(V|w),  0<g<g_*,  w in [-1,1].       (M10)
```

Constants must be independent of both g and the fiber. We use normalized
Haar measure in the common full-Q fiber y=(U0,U1,U2), with U3=U2^-1 Q, and
`h_g(Q)=integral Psi_g(y,Q)^2 dy`. Simultaneous conjugation makes both
conditional mean and variance class functions of Q. Thus conditioning on w
introduces no extra variance of the full-Q conditional means. At the central
fibers use the continuous positive-ground disintegration in full Q.

S13 tangency, the quadratic phase jet at the well, the magnetic spectrum and
endpoint gauge invariance are established project inputs. The true quantum
conditional law is not the magnetic Gibbs measure or the reference law below.

## 2. Synchronized tangency

For one smooth cutoff chi, supported below pi and equal to one near zero,

```
z0(r)=z1(r)=r chi(4r), z2(r)=r chi(2r), zQ(r)=r chi(r).
m(theta)=(theta/4,theta/4,theta/2).
Zy(m(theta))-Dm(theta) ZQ(theta)=0.                         (R1)
```

Substitution proves this identity. Where the actual phase is smooth, with
conditional minimum graph m, differentiate S_y(m(q),q)=0 to obtain
`partial_y(2S-ZS)=-B(q)(Zy-Dm ZQ)=0` at the center. This proves cancellation
of the linear phase drift in that regime. It does not construct a smooth
phase at an angular degeneration. Identical unsynchronized profiles need
not obey R1; the exact check supplies an explicit nonzero profile witness.
See [the original transport argument](w6-conditional-transport-obstruction.md).

## 3. Small-angle tube implication

Only the quadratic jet S2 is homogeneous: `Z S2=2S2`. The actual phase may
have higher terms. Smoothness, R1, the zero fast Hessian of 2S2-ZS2 at q=0,
and bounded third derivatives give

```
|F(q,eta)-F(q,0)| <= cF (|q| |eta|^2+|eta|^3), F=2S-ZS.
```

Assume the actual conditional tube moments are bounded by
`E_tube |eta|^(2j)<=c_(2j) g^(2j)`, j=1,2,3, and
`|grad_eta a_g|<=ca/g`. With `beta=F(q,0)/g^3+a_g(q,0)`, two applications
of (x+y)^2<=2x^2+2y^2 prove

```
E_tube |sigma-beta|^2 <=4 cF^2(c4 |q|^2/g^2+c6)+2 ca^2 c2. (R2)
```

Here the tube expectation is normalized on the tube; its probability in the
full-fiber decomposition is at most one. A line segment used for the amplitude
estimate must stay in the coordinate tube; choose a convex small normal chart.

For the actual magnetic minimum,
`v_*(theta)=16(1-cos(theta/4))=32 sin^2(theta/8)`.
Concavity of sin on [0,pi/2] gives sin x>=2x/pi, so
`v_*>=2 theta^2/pi^2`. Since |q|=2theta,
`|q|^2<=2 pi^2 v_*<=2 pi^2 E(V|Q)`.
Thus R2 is bounded by C0+C1*g^-2 E(V|Q), with
`C0=4 cF^2 c6+2 ca^2 c2`, `C1=8 pi^2 cF^2 c4`.
This is a proved sufficient implication; its actual uniform amplitude and
moment premises are not discharged by the finite algebra.

## 4. Antipodal geometry and a uniform angular reference calculation

The [magnetic geometry](w6-antipodal-magnetic-geometry.md) establishes seven
normal magnetic eigenvalues >=4(sqrt(2)-1), and two soft eigenvalues

```
8 cos(theta/4)-4 sqrt(2)=sqrt(2) delta+O(delta^2), delta=pi-theta.
```

At Q=-I the minimizing sphere is one conjugation orbit, and the actual score
is constant on it. For delta>0 only the stabilizer of Q acts within its fiber;
the full angular variable remains. These statements do not identify the
magnetic Hessian with the action Hessian or quantum conditional precision.

The following calculation resolves the elementary crossover for a specified
reference law, including delta/g^2 tending to zero, a finite value, or infinity.
For lambda>=0 let t=n3 in [-1,1], with density proportional to
`exp(-lambda(1-t)) dt`, the rotational surface measure reduced to t. For
lambda>0 put x=lambda(1-t) and L=2lambda. Direct integration gives

```
E x   =1-L/(exp(L)-1) <=1,
E x^2 =2-(L^2+2L)/(exp(L)-1) <=2.                          (R3)
```

The subtracted quantities are nonnegative. At lambda=0, x=0 identically;
the limits of the moments are zero. As lambda tends to infinity the moments
tend to 1 and 2. No positive angular Hessian lower bound is needed.

Adjoin seven independent normal coordinates with density proportional to
`exp(-|z|^2/g^2)`. With X=|z|^2/g^2, Gaussian integration gives
`E X=7/2`, `E X^2=63/4`. Independence and R3 imply

```
E_ref (X+x)^2 <=63/4+7+2=99/4.                             (R4)
```

This is the score budget for a reference wave proportional to
`exp(-|z|^2/(2g^2)-delta(1-t)/g^2)`, where lambda=2delta/g^2.
Its nonconstant g-score equals (X+x)/g; normalization changes only a fiber
constant absorbed into beta.

**Comparison implication.** Suppose the actual conditional tube submeasure,
in specified normal/angular coordinates, is <=M times this reference
probability measure, with M independent of g and delta. Suppose also that
its actual score is `sigma-beta=(X+x)/g+epsilon`, with
`E[1_tube epsilon^2|Q]<=E0/g^2`. Then

```
E[1_tube |sigma-beta|^2|Q] <= (99 M/2+2 E0)/g^2.            (R5)
```

This follows by the same square inequality. An amplitude bounded above and
below relative to a reference law supplies a density comparison after
normalization, but **neither that comparison nor the score error estimate
has been proved for the actual Wilson ground here**. The magnetic angular
expansion alone does not supply them: its O(delta^2) error divided by g^2
is not uniformly small over a fixed antipodal neighborhood.

## 5. Correct parameter-derivative criterion

Write the true local ground as `Psi_g=g^-6 A(q,eta;h) exp(-S/h)`, h=g^2,
where this phase representation is valid. Put ell=log A. The exact identity is

```
g grad_eta a_g = 2 grad_eta(h partial_h ell)
                 +grad_eta(Z ell)+(1/2)grad_eta div Z.    (R6)
```

Consequently uniform bounds L, B, J on the three gradients on the right
give `|grad_eta a_g| <= (2L+B+J/2)/g`. This **weaker logarithmic-parameter
criterion** suffices; the old claim `partial_g log A=O(g)` is unnecessary.
It is a proved implication with explicit independent premises.

A spatial asymptotic series does not supply the first premise. For example,
`A=1+eta*g^4*sin(g^-6)` is positive on a bounded eta interval for sufficiently
small g and equals 1+O(g^4) in every spatial C^k norm. For Z=eta partial_eta,
the spatial gradient of its relative score at eta=0 is
`5g^3 sin(g^-6)-6g^-3 cos(g^-6)`, which is not O(1/g).
This refutes the inference, not the actual-ground bound.

The cited [Klein--Rosenberger Theorem 6.5](https://arxiv.org/html/2005.13852#S6)
(2020 preprint) gives spatial weighted comparison under its Hypothesis 6.1.
An actual parameter-differentiated comparison and its valid domain must be
proved separately. Existing global ground-jet energy bounds do not by
themselves supply a relative estimate on exponentially rare fibers.

## 6. Correct complement argument and compact action gap

For any reference beta(Q), exact cancellation gives

```
E[1_out |sigma-beta|^2|Q]
 = h_g(Q)^-1 integral_out |N_g-beta Psi_g|^2 dy.             (R7)
```

The conditional denominator and the common reference are both retained.

**Actual geometric gap.** Use the common compact total space
`X=SU(2)^3 x SU(2)` of (y,Q). The actual Agmon distance S from the unique
well is continuous: its weighted path length is locally bounded above by
a constant times the smooth electric-metric distance. The calibrated result
S5 in the original transport argument proves
`min_y S(y,Q)=I(theta(Q))`, where `I(theta)=32 sqrt(2)(1-cos(theta/8))`.
Its equality set Zmin contains all regular minimizers and the entire
antipodal minimizing sphere. Choose an open set U containing **all** of
Zmin, including that sphere. On the compact complement X\U, the continuous
nonnegative function `S-I(theta)` has no zeros. If the complement is nonempty,
it therefore attains a minimum kappa>0:

```
S(y,Q)>=I(theta(Q))+kappa on X\U.                          (R8)
```

This proves a uniform positive action gap for this appropriately enlarged
family of tubes. It supplies no numerical value from a magnetic Hessian.
A fixed-radius tube around only the single regular minimizer cannot be used
uniformly: other limiting sphere points have action excess tending to zero.

**Weighted comparison implication.** Suppose, in addition to R8, the actual
centered numerator and normalization satisfy, uniformly in Q,

```
|N_g-beta Psi_g| <= B g^-p exp(-(S-epsilon)/g^2),
h_g(Q) >= b g^r exp(-2(I(theta)+epsilon)/g^2),              (R9)
```

where B,b>0, p,r are fixed and `0<=epsilon<kappa/2`. Normalized fiber Haar
volume is one. Integration in R7 gives

```
E[1_out |sigma-beta|^2|Q]
 <= (B^2/b) g^(-2p-r) exp(-2(kappa-2epsilon)/g^2).          (R10)
```

Polynomial losses are absorbed into a smaller positive exponent. Indeed,
for a=kappa-2epsilon>0 and m=max(2p+r,0), the function
`t^(m/2) exp(-a t)` is bounded for t=g^-2, g<=1; for m>0 its global maximum
is `(m/(2 a e))^(m/2)`, and for m=0 it is at most one. Therefore R10 is
bounded by a constant times exp(-a/g^2). This proves the normalized
complement implication without assuming exact polynomial prefactors.
The actual uniform differentiated numerator and normalization in R9 remain
unsupplied. Denominator cancellation and R8 alone do not imply R9.

## 7. Assembly criterion and actual status

Assume the actual small-angle hypotheses of section 3, bounded uniform
phase/amplitude/moment controls on the intermediate annulus, the actual
comparison/error hypotheses of R5 near the antipode, and R9 for the same
reference beta on the respective fibers. Then

```
Var(sigma|Q) <= E[1_tube |sigma-beta|^2|Q]
              +E[1_out |sigma-beta|^2|Q].                 (R11)
```

Section 3 bounds the small-angle term by C0+C1*g^-2 E(V|Q). On the
intermediate annulus tangency, bounded second phase derivatives, fourth
moments O(g^4), and the amplitude bound give an O(g^-2) tube term. R5 gives
the antipodal tube term. On both latter regimes theta>=theta0>0, so
`E(V|Q)>=v_*(theta0)>0` absorbs their O(g^-2) constants. R10 bounds the
complement. Taking the maximum of the finitely many constants proves M10.
Class invariance from section 1 transfers the result to w.

This is a proven assembly implication. Its actual-model hypotheses remain
open. M11--M15 cannot yet be invoked using this submission as their M10 input.
The repair establishes a correctly chosen uniform action-gap domain and the
reference angular crossover bound, but has not completed actual M10.

## 8. Verification and provenance

The registered suite checks exact tangency, a general quadratic jet,
sine-square algebra, the logarithmic-parameter identity, the remainder
counterexample, centered denominator cancellation, a magnetic/action Hessian
counterexample, and exact reference angular/Gaussian moments. The original
antipodal suite independently derives the magnetic Hessian from face words.
No Boolean fixture or finite potential sample is labeled a score proof.

Analytic compactness, sine concavity, measure comparison, and the conditional
assembly arguments retain their stated mathematical scope. Their full
statements have no dedicated Lean formalization. T1 applies to the exact
computations, not to the actual all-fiber target.
