# Two scoped results from the M10 proof repair

11 September 2026. These proofs support the repaired
[derivation](../../docs/derivations/w6-synchronized-m10-domination.md).
Actual quantum full-fiber M10 is not proved by either result.

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
