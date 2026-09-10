# The actual Gaussian fast Green operator and its cubic energy prior

6 September 2026. Analytic continuation of the nonlinear-excess route. This
note determines the actual fast-complement inverse on every finite Wick
degree, including a nonreducing literal observation. It identifies the
energy kernel needed for the cubic correction. It does not prove the full
interacting nonlinear estimate or remove the physical spatial cutoff.

## 1. Established inputs and conventions

Use the Gaussian literal-source identification in
`paper/research_notes/G19_GAUSSIAN_PATH_ENDPOINT_BASELINE_20260906.md`
and the physical averaged-path cotangent W in
`paper/research_notes/G19_CONDITIONAL_QUANTUM_PATH_COVARIANCE_20260906.md`.
The algebra below first applies to a finite real Euclidean space E, a
strictly positive self-adjoint oscillator frequency Omega, and an injective
cotangent map W:E_c -> E. Complex Fourier coordinates use adjoints instead
of transposes. The Gaussian probability covariance is (1/2) Omega^-1.

The full ground-transformed oscillator is h0=dGamma(Omega). Its literal
source projection is P=Gamma(p), where p projects onto

```
ran(Omega^(-1/2) W).
```

Here Omega^(-1/2) really is the inverse square root. The source isometry
uses the additional Gram normalization (W*Omega^-1 W)^(-1/2), which changes
neither this range nor its orthogonal projection. Set Q=I-P and let
F0=Q h0 Q be the self-adjoint form compression on Q. In the actual path
geometry the established full Gaussian fast inequality supplies its
uniform positive floor. No assumption that P commutes with h0 is made.

All finite formulas below also apply after restriction to the fixed
compact-simple residual invariant sector: every spatial map acts as the
identity on color and commutes with that symmetry. The actual periodic
Gaussian application keeps rho>0. No normalized joint massless Gaussian
is introduced on its retained harmonic directions.

## 2. Exact shorting identity on n-particle space

Work first on the full n-fold tensor space, n>=1, and define

```
D_n = Omega^(1) + ... + Omega^(n),
L_n = tensor_(j=1)^n Omega^(-1/2),
U_n = tensor_(j=1)^n W,
P_n = orthogonal projection onto ran(L_n U_n),
Q_n = I-P_n,
R_n = Q_n (Q_n D_n Q_n |_Qn)^(-1) Q_n,
A_n = L_n D_n^(-1) L_n
    = (tensor_(j=1)^n Omega^(-1)) D_n^(-1).
```

The coordinate-force Green operator is T_n=L_n R_n L_n. Then

```
T_n = A_n - A_n U_n (U_n* A_n U_n)^(-1) U_n* A_n.       (1)
```

All operators and inverses here are finite and positive on their stated
spaces. If a symmetry restriction leaves a zero-dimensional source range,
the subtraction is zero. Formula (1) is shorting of the *energy prior* A_n;
the equal-time prior tensor Omega^-1 would give a different answer.

Proof. For positive D and any full-column-rank source S, the constrained
equation for x=Q(Q D Q|_Q)^(-1)Q b is

```
D x + S lambda = b,       S* x=0,       Q=I-P_ran(S).
```

Solving the first equation and then the constraint gives

```
x = [D^-1 - D^-1 S(S*D^-1 S)^-1 S*D^-1] b.             (2)
```

This is the inverse of the compressed operator; it is generally not the
compression Q D^-1 Q. Apply (2) with D=D_n and S=L_n U_n, multiply on
both sides by L_n, and use [D_n,L_n]=0. The result is (1). Equivalently,
the same formula follows by maximizing 2 Re<b,x>-<x,Dx> under S*x=0.

Permutation equivariance allows restriction to symmetric Fock tensors,
and also to any invariant combined spatial/color symmetry type. The
physical Lie-cubic subspace has alternating spatial and alternating color
tensors, whose product has the required bosonic symmetry.

In an eigenbasis of Omega, the diagonal entries of the prior are

```
A_n(i_1,...,i_n)
 = 1/[omega_i1 ... omega_in (omega_i1+...+omega_in)].    (3)
```

Thus the actual sum-of-frequencies denominator appears before the source
is removed. The subtraction in (1) retains the baseline coarse/fast
coupling exactly, even when that coupling is nonzero.

## 3. Two consequences that simplify the scale calculation

For n=1, A_1=Omega^-2, so

```
T_1 = Omega^-2
    - Omega^-2 W(W*Omega^-2 W)^-1 W*Omega^-2.           (4)
```

For the actual harmonic path, Omega^2=v^2 K_E+rho^2 I. Therefore the
first-chaos *quantum energy response* is the conditioned inverse of the
second-order spatial operator v^2 K_E+rho^2 I. The equal-time quantum
conditional covariance instead uses Omega^-1 and a factor 1/2. This is
an exact connection between the two conditioning problems; identifying
their covariances would lose an energy denominator. Formula (4) alone
does not import any locality estimate from a different gauge choice.

For n>1, conditioning every leg separately and then tensoring is wrong:
Q_n retains every state with at least one fast component. The tensor of
one-leg fast projectors retains only states with every component fast.
The discrepancy persists when the source happens to reduce Omega.

For example, let Omega=diag(1,4,9,16), W=(e1,e2,e3), and restrict the
spatial tensors to exterior degree three. The exterior cube of T_1 is
zero, whereas the actual T_3 in the ordered wedge basis
(123,124,134,234) is

```
diag(0, 1/1344, 1/3744, 1/16704).                     (5)
```

These are the three sectors with one fast mode and two retained modes.
They contribute to the physical Lie-cubic invariant. Their omission
cannot be repaired by changing a scalar normalization.

## 4. Exact connected Lie-cubic exchange

Let f_abc be the orthonormal invariant Lie tensor, normalized by
sum_bc f_abc f_dbc=C_A delta_ad; set d_G=dim Lie(G). For a real
alternating spatial tensor D, sum over all ordered triples and put

```
P_D(x)=sum_ijk,abc D_ijk f_abc x_i^a x_j^b x_k^c.
```

Every internal Gaussian contraction repeats two colors of f and vanishes.
Consequently P_D is pure Wick degree three for the color-diagonal full
Gaussian. Conditional expectation onto y=W*x is P_D(m(y)), with
m=Omega^-1 W(W*Omega^-1 W)^-1 y. This is also pure third chaos: its
possible lower contractions again repeat colors. Hence

```
F_D=P_D(x)-P_D(m(y))=Q P_D(x).
```

The actual full-complement inverse energy is

```
<F_D, F0^-1 F_E> = (3! C_A d_G / 2^3) <D,T_3 E>.      (6)
```

The right inner product is on ordered spatial tensors. Three cross
pairings contribute the covariance factors (1/2)^3; the six permutations
have the same sign after spatial and color alternation; contracting the
color tensors gives C_A d_G. Equation (1) supplies precisely the
compressed inverse between the two coordinate-to-Fock factors L_3.
This proves (6), including nonreducing sources. Using orthonormal wedge
coordinates instead changes tensor normalization and must be done on
both sides consistently.

The first Wilson ground-forcing theorem identifies such a Lie-cubic
structure under its stated fixed-complex hypotheses. Applying (6) to a
local magnetic vertex needs only its actual finite algebra. Neither fact
by itself gives locality of the complete electric ground-forcing tensor
or of its resolvent-corrected coefficients.

## 5. Retained harmonics are a real constraint on the rooted target

The denominators in (3) locate a failure of unrestricted regulator-uniform
local exchange bounds. With two retained harmonic legs of frequency rho
and one source-null fast leg of frequency omega_h, a nonzero Lie-cubic
component has an energy factor

```
1/[rho^2 omega_h (2rho+omega_h)].                      (7)
```

At fixed positive limiting omega_h this diverges as rho^-2. A fast gap
alone does not bound the variance of the retained coordinates. The
companion actual Wilson plaquette witness derives a nonzero component
of precisely this type. Its spatially summed component cancels, so an
absolute bound taken before that cancellation is stronger than the
globally summed calculation warrants. This does not refute a physical
gap or the fixed-spacing construction.

The viable estimate must specify control of those retained variables,
retain the relevant cancellations, or treat the harmonic sector with
its actual non-Gaussian dynamics. Deleting its physical degrees of
freedom is not a conclusion of this calculation.

## 6. Complementary bound and remaining nonlinear obligation

The companion dynamic conditional-covariance theorem proves spatially
summable, exponentially time-decaying fiber covariances at fixed L,
uniformly in volume and bounded rho/v. With bounded retained means and
uniform local coefficient incidence, it gives a rooted fiber-energy
bound for the three Wick degrees. The vertical form D_vert satisfies

```
F0 >= D_vert > 0,       F0^-1 <= D_vert^-1.             (8)
```

Thus that bound controls the actual selected exchange as a synthesis
quadratic form. It does not identify the fiber kernel with (6), and
positive-operator domination does not imply entrywise absolute row
domination. Formula (1) identifies the actual kernel needed when the
stronger locality statement is required.

Together these results advance the time-integrated second-order input
to the nonlinear scale comparison. The remaining calculation must
combine cubic exchange with the quartic magnetic term, electric metric,
Haar, moving-source, fast-form variation and nonzero baseline cross
terms, and control the complete interacting remainder. No uniform
nonlinear closure, compatible all-scale trajectory or continuum mass
gap follows from this partial coefficient alone.

## 7. Reproduction scope

`check_full_fast_green.py` compares (1) with direct compressed inversion
and an independent constrained Euler-Lagrange solve in three exact
nonreducing families. The third family is the physical spatial
exterior-three type. It also checks (5), rejects replacing the energy
prior by an equal-time prior, and checks the denominator in (7).
The companion actual-plaquette controls establish the specific finite
Wilson witness separately. The all-n proof and infinite-volume or
Fourier estimates remain analytic, not machine-certified by those samples.

## Repository provenance

The [sealed reproduction run](../../runs/dynamic_fast_green_2026-09-06/README.md)
preserves the original proof, exact programs and reports, independent review,
and the reconstruction record for this canonical copy. Program paths named
in the derivation refer to those preserved original inputs. The complete
analytic statement is recorded separately from its finite controls.
