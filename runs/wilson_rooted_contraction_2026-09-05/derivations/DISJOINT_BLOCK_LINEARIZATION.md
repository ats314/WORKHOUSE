# Exact disjoint-block test of the rooted Lipschitz criterion

This calculation tests equation (17) of
`paper/research_notes/G18_WILSON_ENDPOINT_GAUGE_AND_MAJORANT_20260905.md`
on a bounded, commuting two-level tensor model. It does not identify an
invariant two-level subspace of the actual SU(3) Wilson multiplier. Therefore
it rules out a deduction of (17) from the generic tensor/commutativity/
vacuum-centering assumptions alone; extending the obstruction to that
particular multiplier requires an additional argument.

## 1. Exact normalized creation logarithm

Let `H=[[0,a],[a,b]]`, `E=exp(tH)=[[p,q],[q,r]]`, with `p != 0`.
The entries, and `t`, may be complex. Put

```
theta = q/p,       delta = (p*r-q*q)/(p*p).
```

There are `n` disjoint two-level blocks, with vacuum `e0` and excited vector
`e1`. For the single trial creator `v_J=z e1^(tensor n)`, `|J|=n`, its
creation exponential is exactly `e0^(tensor n)+z e1^(tensor n)`.

Use commuting nilpotent variables `x_i`, `x_i^2=0`, for exact-support
creators. The unnormalized transformed vector is

```
product_i (p+q*x_i) + z*product_i (q+r*x_i).
```

Its vacuum coefficient is `p^n+z*q^n`. Local division in the nilpotent
algebra gives

```
(q+r*x_i)/(p+q*x_i) = theta + delta*x_i.
```

Consequently the normalized output and its creation logarithm are exactly

```
Phi(z) = product_i(1+theta*x_i)
         * [1+z*product_i(theta+delta*x_i)]/[1+z*theta^n],

log_star Phi(z) = theta*sum_i x_i
                 + log_star[1+z*product_i(theta+delta*x_i)]
                 - log[1+z*theta^n].
```

These are analytic germs at `z=0`. Differentiation gives

```
partial_z log_star Phi(0)
    = product_i(theta+delta*x_i) - theta^n.
```

For every nonempty subset `S` of size `k`, the exact derivative is
`theta^(n-k)*delta^k`. In particular the full-support derivative is

```
partial_z F_J(t,0) = delta(t)^n.
```

This result includes both scalar normalization and every disconnected
subtraction. It is not a computation of the unnormalized vacuum vector.

## 2. Exact rooted norm ratios, including the support-size denominator

Take `tau>0`, `t=tau*u`, and `N=(F-v)/tau` as in the endpoint note. The
input direction has rooted norm `exp(mu*n)`. Write

```
s = exp(-mu)*abs(theta),       d = abs(delta).
```

The full-support contribution alone to the derivative's norm ratio from
`||.||_mu` to `||.||_(mu,-1)` is

```
abs(delta^n-1)/(tau*n).
```

For the full output family, a fixed root belongs to `binomial(n-1,k-1)`
subsets of size `k`. Symmetry makes every root attain the same norm.
Using `binomial(n-1,k-1)/k=binomial(n,k)/n`, the exact ratio is

```
L_n = [(s+d)^n - s^n - d^n + abs(delta^n-1)]/(tau*n).       (A)
```

Thus the `1/|S|` factor is included exactly. It cannot suppress an
exponential in support size. If (17) held on a common ball, its derivative
at zero would give `L_n <= A*B*abs(u)` independently of `n`. Arbitrarily
small directional amplitudes `z` stay in that ball, so a large-support
direction cannot be excluded by its exponentially small allowed amplitude.

## 3. Explicit real and complex failures of the undamped criterion

For real `a,b`, put `rho=sqrt(a*a+b*b/4)`. When `rho != 0`,

```
p = exp(b*t/2) * [cosh(rho*t) - b/(2*rho)*sinh(rho*t)],
theta = (a/rho)*sinh(rho*t)
        / [cosh(rho*t)-b/(2*rho)*sinh(rho*t)],
delta = [cosh(rho*t)-b/(2*rho)*sinh(rho*t)]^(-2).
```

The last identity follows from `det(exp(tH))=exp(bt)`.

* **Real time, nonzero excited diagonal.** If `b>0`, then
  `delta(t)=1+b*t+O(t^2)>1` for sufficiently small positive real `t`.
  The full-support ratio already grows exponentially with `n`.
* **Real time, purely off-diagonal block.** Set `b=0`, `a>0`, and let
  `eta=tanh(a*t)>0`. Then `theta=eta`, `delta=1-eta^2`. For
  `0<eta<exp(-mu)`, `s+d=1+eta*(exp(-mu)-eta)>1`. Formula (A) becomes
  `[(s+d)^n-s^n+1-2*d^n]/(tau*n)` and grows exponentially, even though
  the full-support contribution tends to zero. The proper output supports
  are essential in this example. Every fixed finite `mu` admits such
  arbitrarily small positive `t`.
* **Complex time, purely off-diagonal block.** For `t=i*y`, `b=0`, and
  `0<abs(a*y)<pi/2`, `delta=sec(a*y)^2>1` and
  `theta=i*tan(a*y)`. The full-support ratio alone grows exponentially.

Hence even a centered, bounded, mutually commuting magnetic model does
not satisfy the proposed undamped same-weight estimate for arbitrary
trial families. This is a limitation of that particular sufficient
criterion; it does not imply divergence of the actual fixed point.

## 4. Retaining the full free damping

Assign free excitation energy `gamma>0` to each block. On a support of
size `k`, compose `N` with the full endpoint resolvent

```
r_tau(k*gamma) = tau/[exp(tau*k*gamma)-1].
```

Set `h=tau*gamma`. The resulting derivative is measured from `||.||_mu`
to `||.||_mu`; its exact ratio is

```
M_n = sum_(k=1)^(n-1) binomial(n-1,k-1)
                      * s^(n-k)*d^k/[exp(h*k)-1]
      + abs(delta^n-1)/[exp(h*n)-1].                       (B)
```

The full-support part is bounded in `n` when `d<=exp(h)`, and grows
exponentially when `d>exp(h)`. But this alone does not control the full
family. Expanding `1/(exp(h*k)-1)=sum_(m>=1)exp(-m*h*k)` shows that

```
M_n = sum_(m>=1) d*exp(-m*h)
                 * [s+d*exp(-m*h)]^(n-1)
      + [abs(delta^n-1)-d^n]/[exp(h*n)-1].                 (C)
```

The final correction has absolute value at most `1/[exp(h*n)-1]`, by the
reverse triangle inequality. Therefore the precise support-growth
threshold in this model is

```
c_damp = s+d*exp(-h).
```

If `c_damp>1`, the `m=1` term in (C) gives exponential growth. If
`c_damp<=1`, the sum in (C) is at most `d/[exp(h)-1]`, and the correction
is bounded; hence there is no growth with volume. This last bound alone
is not uniform as `tau` tends to zero.

## 5. A sufficient bound uniform in the mesh and support size

A useful stronger estimate keeps half of the damping. Put

```
q0 = exp(-h/2),       c_half = s+q0*max(1,d).
```

Since `1/(exp(x)-1) <= exp(-x/2)/x` for `x>0`, formula (B) implies

```
M_n <= [(s+q0*d)^n-s^n-(q0*d)^n
         +q0^n*abs(delta^n-1)]/(h*n).
```

Use `(x+s)^n-x^n <= n*s*(x+s)^(n-1)` for nonnegative `x,s`, and
`abs(delta^n-1) <= n*abs(delta-1)*max(1,d)^(n-1)`. This gives

```
M_n <= [s+q0*abs(delta-1)]/(gamma*tau) * c_half^(n-1).    (D)
```

When `c_half<=1`, (D) is uniform in volume. Since `theta(t)=a*t+O(t^2)`
and `delta(t)=1+b*t+O(t^2)`, its prefactor is `O(abs(u)/gamma)` for
`t=tau*u`; local analyticity makes that bound uniform for bounded
`0<tau<=tau_max` after choosing a sufficiently small coupling radius.
For small `tau`, the explicit sufficient condition is

```
abs(u)*(abs(b)+exp(-mu)*abs(a)) < gamma/2
```

with a strict margin controlling higher-order terms. More precisely the
first-order expansion uses `max(0,Re(b*u))` in place of `abs(b)*abs(u)`.
The statement for a whole bounded mesh interval follows by reducing the
coupling radius further, not just by this asymptotic inequality.

For example, fix a small complex disk on which
`abs(theta(t))<=C_theta*abs(t)` and
`max(1,abs(delta(t)))<=exp(C_delta*abs(t))`. It suffices that

```
C_delta*abs(u) <= gamma/4,
exp(-mu)*C_theta*abs(u)
    <= [1-exp(-gamma*tau_max/4)]/tau_max.
```

Then `c_half<=1` throughout that mesh interval. A corresponding bound
`abs(delta(t)-1)<=C_diff*abs(t)` turns (D) into
`M_n <= [exp(-mu)*C_theta+C_diff]*abs(u)/gamma`.

The damping therefore repairs the linearized model in a uniform small
coupling domain. It is not an unconditional repair: (B)--(C) still diverge
if the damped threshold exceeds one. The calculation supports estimating
the *composite* resolvent/nonlinear map directly, rather than first
discarding its exponential damping through inequality (16).

## Verification and limits

`scripts/verify_rooted_creator_obstruction.py` independently computes the normalized vector
and the finite nilpotent logarithm derivative using exact rational
arithmetic for `n=1,...,7`. It checks every nonempty coefficient against
`theta^(n-k)*delta^k`, checks the exact support-count norm formula, and
compares the closed two-level exponential with an independent matrix
exponential. Numerical tables illustrate (A), (B), and (D); they are not
used to prove the support-growth thresholds above.

This is a directional derivative at `v=0`. It does not yet prove the
nonlinear composite map is Lipschitz on a common rooted ball, establish
the actual Wilson-space analogue of these constants, or settle the
conversion from endpoint coordinates to a unitary vacuum chart.
