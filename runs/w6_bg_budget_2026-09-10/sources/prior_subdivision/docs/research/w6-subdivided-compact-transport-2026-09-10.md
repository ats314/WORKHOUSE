# W6: subdividing compact transport removes the extra source-growth gate

Date: 2026-09-10. Status: conditional analytic consequence of the actual
positive-reference compact transport estimates. This is a new composite
approximation result; it does not assert a uniform interacting Wilson estimate.

## S1. Inputs and the obligation advanced

The source is the positive-reference construction in
[compact_residual.md](../../runs/recent_research_integration_2026-09-09/sources/w6_compact_continuation_20260909/compact_residual.md),
C2 and C12–C20, and its
[positive-reference budget](../../runs/recent_research_integration_2026-09-09/sources/w6_compact_continuation_20260909/positive_reference_budget.md),
B1–B3. These use the actual fixed-square Hamiltonian, its ground state and
source projection. They are stronger inputs than a scalar Taylor analogy.

Assume, uniformly over the intervals in question, the derivative estimates
`M_k(s) ≤ c_k s^(-k)` for k = 1, 2, 3, with nonnegative finite c_k and a finite
graph-energy constant β. For a relative decreasing step h = (s−t)/s, the source
estimates imply

```
|E(s,t;p)| ≤ β h³ [c3/6 +
  (c1 c2 + h c2²/4 + c1³)/(1−c1 h)] b_s[p],
b_t[R(t,s)p] ≤ (1+c1 h) b_s[p].
```

Here E is the error in the **complete local second-order Schur increment**,
including the moving source, graph lift and fast inverse. The construction of
these local increments is retained from C18–C19.

With the prescribed couplings g_n = √(κ/n), one step per n gives a sufficient
summability condition c1 < 4 in B3. The result below removes that extra
restriction by subdividing each same physical coupling interval. The derivative
scaling assumptions themselves are not discharged by subdivision.

## S2. Compatible transport is a cocycle

Write P(t) for the actual source projection and Ω(t) for the normalized real
ground state. C2 uses U' = [P',P]U, χ = U*Ω and
S' = (|χ'><χ|−|χ><χ'|)S. Its product R = US satisfies

```
R' = A(t)R,
A(t) = [P'(t),P(t)] + |ν(t)><Ω(t)| − |Ω(t)><ν(t)|,
ν(t) = Ω'(t) − [P'(t),P(t)]Ω(t).
```

Indeed Uχ' = Ω'−[P',P]Ω. Thus A(t) is independent of the chosen starting point.
Uniqueness of this operator ODE gives R(t,u)R(u,s) = R(t,s), and the same R
transports the source and its fast complement. The H1-preservation and
regularity assumptions are exactly those established at positive compact
references in C2. No Gaussian-to-compact form-domain equivalence is invoked.

Schur minimization is covariant under these pullbacks. Consequently exact local
Schur differences telescope after pullback to the initial source chart. The sum
of the correspondingly pulled-back local jets is a well-defined composite
approximation, with error equal to the sum of the pulled-back local errors.

## S3. Source growth across arbitrary subdivisions

For any finite decreasing partition s_0 > … > s_m > 0, set
h_l = 1−s_(l+1)/s_l. For c1 ≥ 0,

```
log(1+c1 h_l) ≤ c1 h_l ≤ −c1 log(1−h_l).
```

Therefore

```
∏_l (1+c1 h_l) ≤ (s_0/s_m)^c1.
```

This bound is independent of the number or placement of substeps. In
particular, every transported source between g_n and g_(n+1), starting at
g_n0, has energy at most

```
G_n b_initial,       G_n = ((n+1)/n0)^(c1/2).
```

Only the upper source-energy comparison is used; no commutation of different
fast resolvents is assumed.

## S4. Cubic error gains two powers of the subdivision count

Choose integer n0 ≥ 1 with n0 ≥ 2c1. Let
r_n = 1−√(n/(n+1)) ≤ 1/(2n). Divide [g_(n+1),g_n] into m_n ≥ 1 equal coupling
steps. Their relative lengths are

```
h_l = (r_n/m_n)/(1−l r_n/m_n)
    ≤ r_n/(m_n(1−r_n)) ≤ 1/(n m_n).
```

Thus c1 h_l ≤ 1/2 and h_l ≤ 1. Set the finite constant

```
A = β [c3/6 + 2(c1 c2 + c2²/4 + c1³)].
```

Every local error is bounded by A h_l³ times the local source energy. S2
and S3 give, for the composite approximation over physical step n,

```
|E_n[p]| ≤ A G_n / (n³ m_n²) b_initial[p].                 (S4)
```

The two powers of m_n are obtained by summing m_n individual cubic errors;
they do not come from replacing a source norm by a smaller one.

## S5. Summability for every finite source-growth coefficient

Choose any positive integer m_n with m_n² ≥ G_n, for example

```
m_n = ceil(((n+1)/n0)^(c1/4)).
```

Then (S4) gives |E_n[p]| ≤ A n^(-3) b_initial[p]. The series of absolute
errors converges for **every finite c1 ≥ 0**, with a tail starting at N ≥ n0
bounded by

```
A [N^(-3) + 1/(2N²)] b_initial[p].
```

The tail bound follows by the decreasing-function integral comparison for
x^(-3). Alternatively m_n of order n^q suffices whenever q > c1/4−1.
The physical endpoints g_n and their spatial scales are unchanged.

The scalar finite-sum and summability implications are formalized in
[W6Subdivision.lean](../../lean/Workhouse/W6Subdivision.lean). Its inputs
explicitly retain the analytic local-error and source-growth bounds. It does
not encode the transport ODE or the Hamiltonian construction.

## S6. Consequence and the next obligation

Hypothesis discharged: the additional c1 < 4 restriction imposed by using one
local Taylor step per prescribed coupling interval.

Downstream consequence: the complete **composite** compact-reference Schur
approximation has a summable error budget for any finite c1, assuming the
uniform derivative and graph-energy estimates in S1.

The next mathematical inputs are actual `M_k(s) ≤ c_k s^(-k)` bounds toward
zero coupling, a volume-uniform version if the square is enlarged, and the
identification with the intended physical coarse theory. A sum of jets at
different compact references is not automatically the original endpoint
Taylor polynomial or the Gaussian K1/K2 coefficients. That identification
must be proved if that particular polynomial is the target. This note neither
assumes it nor infers a continuum mass gap from convergence of the composite
error series.

## Provenance and review

The earlier C2/C12–C20 and B1–B3 estimates are prior project work. The
subdivision construction S2–S5 was derived in this pass. An independent agent
checked the generator, cocycle, pullback telescoping and exponent arithmetic;
that review identified the necessary distinction between composite and
endpoint Taylor approximations. Source files are preserved unchanged.
