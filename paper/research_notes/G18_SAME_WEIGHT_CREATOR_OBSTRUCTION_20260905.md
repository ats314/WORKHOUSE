# Actual SU(3) disjoint active plaquettes: obstruction and damped linearization

This strengthens the two-level calculation in
`runs/wilson_rooted_contraction_2026-09-05/derivations/DISJOINT_BLOCK_LINEARIZATION.md`. The exact statement uses arbitrary
trial creator families and independently active disjoint Wilson plaquettes.
It does not by itself treat the restriction in which every lattice
plaquette has the same nonzero coupling. Thus it disproves equation (17)
as a uniform assertion over active plaquette families; a claim only for
the full translation-invariant interaction needs a separate argument.

## Tensor-general derivative

On one block let `Omega` be a unit vacuum, `eta` a unit vector orthogonal
to it, `E=exp(tV)`, `a=<Omega,E Omega> != 0`, and `q=1-|Omega><Omega|`.
Set

```
w = q E Omega/a,
theta = <Omega,E eta>/a,
g = q E eta/a,
Leta = g-theta*w.
```

For `n` disjoint blocks and input creator `z eta^(tensor n)`, the
normalized output is

```
[product_i(Omega+w_i)]
 * [1+z*product_i(theta*Omega+Leta_i)]/[1+z*theta^n]
```

in the disjoint-support creation algebra. Indeed, each local quotient is
`(theta*Omega+g)/(Omega+w)=theta*Omega+g-theta*w` because two nonempty
creators on the same block multiply to zero. The derivative of its
creation logarithm on a nonempty subset `X` of blocks is therefore

```
theta^(n-|X|) * (Leta)^(tensor |X|).                      (1)
```

No two-level invariant subspace is assumed in (1).

## Exact SU(3) inputs and exact four-link support

For a Wilson plaquette, take `V=Tr(U_p)+Tr(U_p)^*` and
`eta=V Omega/sqrt(2)`. Haar invariance reduces the four-link integral to
one SU(3) holonomy integral. Write `chi=Tr` for the fundamental character.
The center kills terms of nonzero triality, Schur orthogonality gives
`integral chi*conjugate(chi)=1`, and the determinant tensor is the unique
singlet in `3 tensor 3 tensor 3`. Hence

```
<V> = 0,    <V^2> = 2,    <V^3> = 2.                    (2)
```

In particular `eta` is normalized. At real `t=0`,

```
theta(t) = sqrt(2)*t+O(t^2),
Leta(t) = eta+t*q V eta+O(t^2),
<eta,V eta> = <V^3>/<V^2> = 1,
A(t) := ||Leta(t)|| = 1+t+O(t^2).                        (3)
```

All expansions are norm-analytic locally because `||V||<=6` and `a(0)=1`.
The remainder in the norm expansion is well defined since `||eta||=1`.

Both `w` and `Leta` have exact four-link support, not merely nonzero block
support. Every vector involved is a function of the plaquette holonomy.
Integrating any one of its four links returns its Haar mean, independently
of the other links. Centering that function therefore annihilates every
single-link vacuum projection. This proves membership in the tensor product
of the four nonvacuum link spaces. It remains valid for complex `t` with
nonzero `a(t)`.

For real `t`, an additional exact expression is available. If
`a(t)=<exp(tV)>` and `m(t)=a'(t)/a(t)`, then

```
Leta = exp(tV)*(V-m(t))/(sqrt(2)*a(t)),
A(t)^2 = [a''(2t)-2*m(t)*a'(2t)+m(t)^2*a(2t)]/[2*a(t)^2].
```

The exact Weyl constant-term check in `scripts/verify_rooted_creator_obstruction.py` verifies
the moments in (2) independently and checks the first derivative in (3).

### An explicit positive interval, with no asymptotic remainder left open

For `0<t<=1/200`, let `r=18*t^2*exp(6*t)`. The operator Taylor remainder
is at most `r`. The exponential series gives
`exp(6t)<=1/(1-6t)<=100/97<2`, so `r<=36*t^2`.
With `a=<Omega,E Omega>`, `b=<Omega,E eta>`, and `c=<eta,E eta>`,
the moments above imply

```
1 <= a <= 1+r,
c >= 1+t-r,
abs(b) <= sqrt(2)*t+r <= 3*t.
```

The first lower bound follows pointwise from `exp(tV)>=1+tV` and
`<V>=0`. The last bound uses `sqrt(2)<=3/2` and
`36*t<=9/50`. The numerator `1+t-r` is positive on this interval.
Since all quantities are real,

```
<eta,Leta> = c/a-b^2/a^2
    >= (1+t-r)/(1+r)-9*t^2
    >= 1+t-2*r-t*r-9*t^2
    >= 1+t-81*t^2-36*t^3
    >= 1+t-82*t^2
    >= 1+t/2.
```

The second inequality follows after clearing the positive denominator:
its excess is `(2+t)*r^2`. The penultimate inequality uses `36*t<=1`,
and the final one uses `82*t<=41/100<1/2`. Cauchy--Schwarz therefore gives
the explicit bound `A(t)>=1+t/2` throughout `0<t<=1/200`.
The direct rational lower bound

```
(1+t-36*t^2)/(1+36*t^2)-9*t^2 >= 1+t/2
```

is separately checked in the Lean source `lean/Workhouse/RootedScalarBounds.lean`.
That scalar theorem checks the rational estimate only; the operator
Taylor bound and the SU(3) moment calculation are established above.

## Failure of the undamped same-weight estimate

Let `J` be the union of `n` disjoint active plaquettes, so `|J|=4n`.
Put `B=exp(-4mu)*abs(theta)`. A root link belongs to one distinguished
plaquette and to `binomial(n-1,k-1)` unions of `k` selected plaquettes.
Equation (1) gives the exact derivative ratio for `F`:

```
||D_v F(t,0)[eta^tensor n]||_(mu,-1) / exp(4mu*n)
    = [(A+B)^n-B^n]/(4n).                               (4)
```

For `N=(F-v)/tau`, the triangle inequality yields the rigorous lower bound

```
||D_v N(t,0)[eta^tensor n]||_(mu,-1) / exp(4mu*n)
    >= [(A+B)^n-B^n-1]/(4*tau*n).                        (5)
```

For sufficiently small real `t>0`, (3) gives `A>1` and
`A+B=1+(1+sqrt(2)*exp(-4mu))*t+O(t^2)>1`. Thus (5) diverges
exponentially with `n` for every fixed `tau>0` and `t=tau*u>0`, however
small `u` is chosen. Even the full-support lower bound
`(A^n-1)/(4*tau*n)` suffices here.

The amplitudes `z` can be taken arbitrarily small within the proposed
rooted ball, so the restriction to a common ball does not remove this
derivative obstruction. The selected plaquettes are disjoint and their
magnetic multipliers commute exactly. Their union need not be connected:
equation (17), as stated for arbitrary trial creator families, permits this
input. A future domain restricting trial families requires its own closure
argument and is a different criterion.

## A positive bound for the composite linearization

Let the free energy per excited link be at least `gamma>0`. An exact
four-link block then has energy at least `Gamma=4gamma`. Put

```
h = tau*Gamma,   q0 = exp(-h/2),
c_half = B+q0*max(1,A),    D = ||Leta-eta||.
```

On a union of `k` blocks, spectral calculus gives

```
||(exp(tau*K)-1)^(-1)|| <= exp(-h*k/2)/(h*k).
```

Apply this *after* taking the difference `D_v F-I`. Proper-subset
derivatives have norm `abs(theta)^(n-k)*A^k`, while the full derivative
difference is bounded by `n*D*max(1,A)^(n-1)`. The same binomial identity
as in (4) yields

```
||R_tau D_v N(t,0)[eta^tensor n]||_mu / exp(4mu*n)
    <= [B+q0*D]/(Gamma*tau) * c_half^(n-1).              (6)
```

Thus `c_half<=1` supplies a uniform volume bound. It also supplies a
uniform mesh bound of order `abs(u)` on a sufficiently small coupling
disk. To make this last assertion explicit, choose a disk `|t|<=t0`
with `h0(t)=exp(6|t|)-1<=1/2`. Direct operator estimates give

```
abs(theta) <= h0/(1-h0),
D <= 2*h0/(1-h0)+h0^2/(1-h0)^2.
```

Hence constants `C_theta,C_D` exist explicitly with
`abs(theta)<=C_theta*|t|`, `D<=C_D*|t|`, and
`max(1,A)<=exp(C_D*|t|)` throughout this disk. For any bounded mesh interval
`0<tau<=tau_max`, it suffices to choose

```
tau_max*abs(u) <= t0,
C_D*abs(u) <= Gamma/4,
exp(-4mu)*C_theta*abs(u)
    <= [1-exp(-Gamma*tau_max/4)]/tau_max.
```

Then `c_half<=1` for the entire interval and (6) is at most
`[exp(-4mu)*C_theta+C_D]*abs(u)/Gamma`, independently of `n` and `tau`.

This establishes a positive composite-map bound only for the specified
derivative directions at `v=0` and disjoint active plaquettes. The full estimate for arbitrary trial families, overlapping plaquettes
and the complete interaction is proved in `G18_ROOTED_WILSON_CONTRACTION_20260905.md` by a moving
support weight and full kinetic smoothing. Equation (6) here is an
independent directional check of that mechanism.
