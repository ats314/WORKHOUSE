# Repairing the conditional-gradient RG recursion

5 September 2026. Derivation prompted by the reversed conditional-gradient
step in the preserved [EX-014 extraction](../../notes/imported/EXTRACT_2026-09-01/EX-014-rg-schur-riccati.md),
Section 1, STEP 6. The extraction has SHA256
`fc55bb4934560183d5529822693ce7ad90ca9bc6f521546cb505d8e30f6cc703`. This is a theorem for
conditional configuration-space Dirichlet forms. It is not yet an actual
Wilson all-scale estimate or an identification with OS transfer energy.

## 1. Averaging and the correct coarse metric

Let `B:R^m ->R^k` have full row rank, and set `y=Bx`. For a pullback
`f(x)=F(Bx)`, the exact chain rule is

```text
|grad_x f|^2 = <grad_y F, B B* grad_y F>.
```

Thus the quotient coarse metric is `B B*`. For arithmetic averaging of
`m` scalar coordinates, `B=(1/m,...,1/m)` and `B B*=1/m`.

Under the standard isotropic Gaussian fine measure, conditional
expectation has the explicit formula

```text
grad_y P f = (B B*)^(-1) B E[grad_x f | y].
```

The coarse metric therefore gives

```text
<grad_y P f, B B* grad_y P f>
 <= E[|grad_x f|^2 | y].                                (1)
```

The constant one is attained by nonconstant linear pullbacks. In the
unweighted Euclidean `y` metric for arithmetic averaging, the optimal
constant is `m`, also attained by `f=y`. The factor `1/m` belongs to the
pullback energy, not to the reverse conditional-expectation gradient
bound asserted in the imported EX-014 argument.

This already provides a normalization-consistent exact Gaussian test for
any proposed nonlinear/gauge block metric.

## 2. The conditional score term for an interacting measure

Use orthonormal fine coordinates `x=(q,z)`, where `q` is the normalized
coarse coordinate and `z` is its orthogonal fiber coordinate. In the
arithmetic example, `q=sqrt(m)y`.

Let the measure have density proportional to `exp(-V(q,z))`, with a
product coordinate domain and regularity/decay sufficient to differentiate
the conditional integral. Write `mu_q(dz)` for its conditional measure
and `nu(dq)` for its coarse marginal. Assume uniformly in `q`:

```text
Var_(mu_q)(f) <= kappa^(-1) E_(mu_q)|grad_z f|^2,
||grad_z grad_q V|| <= M,
kappa>0.
```

Then the exact derivative formula is

```text
grad_q P f = E_q grad_q f - Cov_q(f,grad_q V).            (2)
```

The covariance term includes the derivative of the conditional
normalizer. Omitting it would falsely make interacting decimation behave
like an independent product measure.

Put `c=M/kappa`. For every unit vector `v` in the coarse coordinates,
two uses of conditional Poincare and Cauchy-Schwarz give

```text
|Cov_q(f,v.grad_q V)|
 <=sqrt(Var_q f Var_q(v.grad_q V))
 <=(M/kappa) sqrt(E_q|grad_z f|^2).
```

Taking the supremum over `v` and using Jensen for the first term of (2)
proves

```text
|grad_q P f|
 <=sqrt(E_q|grad_q f|^2)+c sqrt(E_q|grad_z f|^2).         (3)
```

The hypothesis may equivalently be supplied by the conditional variance
bound on every component of the score, rather than by a pointwise mixed
Hessian bound. This may be useful when a pointwise large-field bound is
too strong. Such a variance estimate must still be established for the
actual conditional measure.

## 3. The sharp surviving two-scale Poincare theorem

Suppose the coarse marginal satisfies

```text
Var_nu F <= C integral |grad_q F|^2 dnu.
```

The law of total variance, the fiber bound and (3) give

```text
Var_mu f
 <= integral [ C(sqrt(A_q)+c sqrt(B_q))^2
                  +kappa^(-1)B_q ] dnu(q),
A_q=E_q|grad_q f|^2, B_q=E_q|grad_z f|^2.
```

Consequently the fine Poincare constant is bounded by the largest
eigenvalue of the explicit two-by-two matrix

```text
L(C,kappa^(-1),c)
 = [[C, cC], [cC, kappa^(-1)+c^2 C]].                    (4)
```

This is sharper than adding two unrelated worst-case gradient bounds.
At `c=0`, (4) is `max(C,kappa^(-1))`, not `C+kappa^(-1)`.

The matrix estimate is exactly sharp even within Gaussian measures.
For one coarse and one fiber coordinate take

```text
V(q,z)=q^2/(2C)+(kappa/2)(z-cq)^2.
```

Its coarse marginal has variance `C`, its conditional fiber has gap
`kappa`, and `|partial_z partial_q V|=kappa|c|`. Its covariance matrix
is exactly (4), so the fine Gaussian Poincare constant is its largest
eigenvalue. No stronger general constant follows from only these inputs.

## 4. Scale conversion does not create a contraction

Let `a_next=L a`, `m=L^d`, and retain the ordinary unweighted coarse
average coordinate `y=q/sqrt(m)`. If configuration Dirichlet forms are
scaled by `a^(-2)`, then

```text
E_next(F)=(La)^(-2)|grad_y F|^2
          =[m/(L^2 a^2)]|grad_q F|^2.
```

Therefore the recursion for these dimensionally rescaled constants is
again (4), with

```text
A=(m/L^2) C_next,
B=a^2/kappa,
C_fine <= lambda_max L(A,B,c).                          (5)
```

For `d=4,L=2`, the coefficient is `m/L^2=4`, not `L^2/m=1/4`.
The imported recursion mixed raw/physical constants and reversed the
pullback derivative estimate. Both normalizations must be corrected.

Alternatively give the coarse `y` gradient the scale-compatible quotient
metric `L^2/m`. Its dimensionally rescaled energy equals
`a^(-2)|grad_q F|^2`; then (5) has `A=C_next`. At zero score coupling
this preserves the larger of the coarse and fiber constants. Changing
the metric removes an artificial loss or gain; it does not improve a
fixed physical operator's spectrum by a coordinate choice.

The word "scaled" here refers only to units in a configuration-space
Dirichlet form. Neither (4) nor (5) identifies this form with the actual
OS transfer-energy form. That is precisely the separate G23 time/form
comparison obligation.

## 5. A constructive square-summable score budget

There is a useful stable iteration when the fiber modes have a strict
gap relative to the transported coarse modes. Suppose in the matched
metric that

```text
A=C_next>0,
0<=B<=theta A,  0<=theta<1.
```

Then

```text
lambda_max L(A,B,c)
 <= A [1+c^2/(1-theta)].                                (6)
```

For proof, divide by `A`, increase `B/A` to `theta`, and put
`t=c^2/(1-theta)`. The matrix

```text
(1+t)I - [[1,c],[c,theta+c^2]]
```

has nonnegative diagonal entries and determinant
`t(t-c^2)>=0`; hence it is positive semidefinite. This proves (6).

Iterating from a controlled terminal coarse scale gives

```text
C_finest <= C_terminal
             product_k [1+c_k^2/(1-theta)]
           <= C_terminal exp(sum_k c_k^2/(1-theta)).      (7)
```

Thus a uniform terminal constant, a uniform strict fiber separation,
the correctly transported metric, and

```text
sum_k (M_k/kappa_k)^2 < infinity
```

are a sufficient configuration-form scale theorem. The square is
structural: a separated fiber enters the coarse estimate through its
off-diagonal score coupling twice.

The strict fiber separation cannot be silently removed. If `A=B`, the
largest eigenvalue of `L(A,A,c)/A` equals
`[(sqrt(4+c^2)+|c|)/2]^2=1+|c|+O(c^2)`. A square-summable but
non-summable sequence `c_k=1/k` then has divergent product. The separated
case in (6) removes precisely this first-order loss.

Without separation, the weaker general bound is

```text
lambda_max L(A,B,c) <= max(A,B) exp(|c|),
```

so a summable `sum |c_k|` budget still suffices when the other constants
are uniformly controlled. This follows by comparison with `L(1,1,|c|)`
and `2 asinh(|c|/2)<=|c|`.

## 6. What an asymptotically free trajectory would need to supply

Suppose, as an additional **actual-RG estimate**, that at ultraviolet
scale number `k` one proves

```text
g_k^2 <= C_g/(k+k0),
M_k/kappa_k <= C_s g_k^2,
B_k<=theta A_k,  theta<1,
```

with the measure, effective interactions and metric all belonging to the
same reflection-positive RG trajectory. Then the budget in (7) converges:

```text
sum_(k>=0) c_k^2
 <= (C_s C_g)^2 sum_(k>=0) (k+k0)^(-2)
 <= (C_s C_g)^2 (k0^(-2)+k0^(-1)).                      (8)
```

Equations (7)-(8) really are sufficient for a scale-uniform bound of the
specified configuration Dirichlet form. A score ratio merely of order
`g_k`, rather than `g_k^2`, would not give this convergent square budget
under the same running law. The actual Wilson estimate is not supplied
by this conditional calculation.

The actionable next computation is the leading **conditional score** of
the actual reflection-adapted gauge block, in a normalization compatible
with its coarse kinetic form. Determine whether its relative score
bound is of order `g^2` after gauge/connected subtraction, whether the
fast fiber has a uniform strict separation, and whether the large-field
part preserves those integrated bounds. Linearizing only the block-map
Jacobian does not answer any of these three questions.

For gauge fibers, the local product-coordinate differentiation in (2)
must be replaced by its justified horizontal/conditional analogue,
including Jacobians and moving-domain or connection terms. Reflection
positivity of the raw map remains available but does not provide these
analytic estimates. Finally a scale-uniform comparison to actual OS
transfer energy and continuum convergence are required before a
configuration Poincare statement becomes a continuum mass statement.

This repair preserves the valid conditional-variance mechanism, supplies
its sharp constants, and replaces the false geometric contraction with
a precise summable score target.
