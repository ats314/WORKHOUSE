# Exact Gaussian endpoint memory for the local covariant path block

5 September 2026. Analytic research continuation. This derives the exact endpoint
operator with its actual Gaussian source normalization, proves a uniform
low-momentum approximation for the averaged-path source, and exhibits its
nonzero leading conditional score. The nonlinear comparison must retain
this quadratic baseline rather than require its entire score to be small.

## 1. Existing inputs and the operator being compared

The current graph entries RESULT:GAUSSIAN_QUANTUM_FAST_SOURCES and
RESULT:GAUSSIAN_OS_OBSERVABILITY were queried first. They already identify
the literal coordinate Wick range and the potentially larger whole-history
range. The recent complete endpoint theorem concerns J^*exp(-tau h)J and
its logarithm, including all retained directions. Those are inputs here.
The new local path source and its alias-tail estimate are in
[local covariant path proof](G19_LOCAL_COVARIANT_AVERAGED_PATH_SOURCES_20260905.md).

The averaged linear path operation itself has prior provenance. In
[Dimock, *Multiscale block averaging for QED in d=3*, arXiv:1712.10029v3](https://arxiv.org/html/1712.10029v3),
Section 3.1, equation (189), Q averages straight length-L bond paths with
factor L^(-4). Our counting-metric convention has R=LQ, after translating
the centered blocks to lower-corner blocks. His scaled derivative identity
(192) is the corresponding cochain relation. The repository already
treats nonlinear Balaban averaging and reflection-compatible geometry in
[G19_BALABAN_BLOCKING_REFLECTION_POSITIVITY_20260830.md](G19_BALABAN_BLOCKING_REFLECTION_POSITIVITY_20260830.md).
These precedents do not by themselves supply the quantum endpoint below.
Dimock's Section 3.7.3, equations (304)-(307), conditions a gauge-fixed
Laplacian Green operator at fixed averages. Here the true quantum ground
covariance is Omega^(-1)/2, with square-root spatial precision. Its
conditional covariance and endpoint normalization are different operators;
the cited Laplacian exponential-decay estimate cannot simply be inherited.

Let E be a finite real Euclidean space, Omega=Omega^*>0, and
h=dGamma(Omega) be the vacuum-subtracted harmonic oscillator. In coordinate
representation its ground is proportional to exp(-<q,Omega q>/2). Let
L:E->Y be a linear observation of full row rank; otherwise replace Y by
its supported quotient. Put W=L^* and

```text
G=W^* Omega^(-1) W>0,
j1=Omega^(-1/2) W G^(-1/2),             j1^*j1=I_Y.     (1)
```

The actual marginal covariance of Lq is G/2. Identifying its L2 space with
the standard Gaussian Fock space by Wick polynomials gives the literal
isometry J f(q)=f(Lq)Phi(q) as J=Gamma(j1). In particular this is the
actual marginal normalization; replacing G by the Euclidean row Gram
W^*W changes the source isometry.

For every tau>0 define

```text
C_tau=J^*exp(-tau h)J,
M_tau=G^(-1/2) W^* Omega^(-1)exp(-tau Omega)W G^(-1/2).
```

Then the following identities hold exactly on the full Fock space:

```text
C_tau=Gamma(M_tau),
K_tau=-tau^(-1)log C_tau=dGamma(B_tau),
B_tau=-tau^(-1)log M_tau.                              (2)
```

On each n-particle sector, exp(-tau dGamma(Omega)) is the symmetric
restriction of exp(-tau Omega) tensor n. Inserting j1 tensor n proves
the first identity sector by sector. The positive matrix M_tau has
eigenvalues in (0,1), since Omega>0. Diagonalizing M_tau shows that the
logarithm on that sector is the sum of its one-particle logarithms. The
vacuum eigenvalue is one. Finite-particle vectors form a core for the
nonnegative direct-sum operators, proving (2) with their closed domains.

These identities hold after restriction to the complete compact-group
invariant Fock subspace when Omega and L are equivariant. One-particle
color vectors need not themselves be physical singlets: restriction is
performed on the whole Fock space with all invariant tensors retained.

For fixed tau, (2) is a second-quantized Hamiltonian. The family C_tau is
generally not a semigroup in tau. Indeed M_(2tau)-M_tau^2 is the positive
one-particle omitted-range term
j1^*exp(-tau Omega)(I-j1j1^*)exp(-tau Omega)j1.
Thus B_tau may depend on the endpoint time. The full Fock STATIC Schur
operator is another object and is generally not second quantization of
its one-particle static Schur complement; Section 6 gives exact numbers.

## 2. The actual two-polarization alias matrix

Use the periodic n^3 original-link complex, n=Lm, and the local averaged-path
cochain map R from the predecessor. On fine transverse cochains C=ker d0^*,
its physical source is W=R^*|_(C_c), C_c=ker d0c^*. At each coarse momentum
K in [-pi,pi]^3 choose an isometric matrix N_K:C^(p_K)->ker D(K)^*, with
p_K=2 at K!=0 and p_0=3. No global continuous polarization frame is needed.
Changing N_K conjugates the following matrices by a unitary.

For fine aliases k=(K+2pi r)/L modulo 2pi, put

```text
d_i(k)=exp(i k_i)-1,       D_i(K)=exp(i K_i)-1,
a_i(k_i)=L^(-1)sum_(t=0)^(L-1) exp(i k_i t),
a(k)=product_i a_i(k_i),
W_k=L^(-1/2)diag_i(conjugate(a(k)a_i(k_i)))N_K.         (3)
```

The phase identity a_i d_i=D_i/L ensures W_k lies in the fine transverse
fiber. In the original-link kinetic metric the fundamental SU(N) regulated
frequencies are

```text
omega(k)=sqrt(u q(k)+rho^2),
q(k)=4sum_i sin^2(k_i/2),       rho>0.                  (4)
```

For a fixed character representation replace u by v^2=2b_rep u throughout.
The exact marginal and lagged covariance matrices in this polarization
frame are

```text
G_K=sum_(k alias K) omega(k)^(-1) W_k^*W_k,
H_(tau,K)=sum_(k alias K) omega(k)^(-1)exp(-tau omega(k)) W_k^*W_k,
M_(tau,K)=G_K^(-1/2) H_(tau,K) G_K^(-1/2),
B_(tau,K)=-tau^(-1)log M_(tau,K).                       (5)
```

Equations (3)-(5) are the requested actual two-polarization coarse matrix,
including its Haar-tangent counting norms and Gaussian marginal covariance.
The matrices G_K and H_(tau,K) need not commute. In particular one may not
replace (5) by separate scalar averages in arbitrarily chosen polarizations.

At K=0 all nonprincipal box symbols vanish. Here W_0=L^(-1/2)I_3 and

```text
G_0=(L rho)^(-1)I_3,
M_(tau,0)=exp(-tau rho)I_3,
B_(tau,0)=rho I_3.                                    (6)
```

The three harmonic cochain directions per color are retained exactly.
Their marginal variance diverges as rho tends to zero. Equation (6) does
not produce a normalized Gaussian vacuum at rho=0.

## 3. Inverse-frequency weighting improves the low-alias error

First set rho=0 in a NONZERO coarse momentum block; that block has no zero
fine frequency and is a positive finite oscillator in its own right.
Equivalently, remove the three global harmonic cochain directions before
forming the unregulated finite Gaussian model. Neither convention asserts
an unregulated vacuum on those missing flat coordinates.

Write k0=K/L for the principal alias and omega0=v sqrt(q(k0)), where
v=sqrt(u) for the fundamental case. The predecessor proves, for every
coarse transverse b, the exact Euclidean source estimate

```text
sum_(k!=k0)||W_k b||^2 <= eta(K)||W_k0 b||^2,
eta(K)=pi^8 |K|^2/1536.                               (7)
```

Every high alias has omega(k)>=2v/L, whereas omega0<=v|K|/L. Split the
actual marginal Gram as G_K=G_low+G_high, where
G_low=omega0^(-1)W_k0^*W_k0>0. Multiplying (7) by the inverse frequencies
therefore gives the MATRIX inequality

```text
0<=G_high<=epsilon(K)G_low,
epsilon(K)=pi^8 |K|^3/3072.                            (8)
```

This cubic rather than quadratic error is the effect of the actual
inverse-frequency source weight. It is not obtained by simply using the
Euclidean low/high source angle in the Gaussian formula.

The principal alias minimizes every coordinate absolute momentum and
therefore q(k), so omega(k)>=omega0 for all its aliases. The two lagged
Gram inequalities

```text
exp(-tau omega0)G_low <= H_(tau,K)
                          <= exp(-tau omega0)G_K
```

and (8), by congruence with G_K^(-1/2), imply

```text
exp(-tau omega0)/(1+epsilon(K)) I
 <=M_(tau,K)<=exp(-tau omega0) I.                      (9)
```

No commutation of G_low and G_high was used. Each of the two endpoint
polarization frequencies nu_j(tau,K) consequently obeys

```text
omega0<=nu_j(tau,K)
      <=omega0+tau^(-1)log(1+epsilon(K)).              (10)
```

At the natural coarse time tau=s L/v with fixed s>0, use
omega0>=2v|K|/(pi L) and log(1+x)<=x to obtain

```text
0<=nu_j/omega0-1<=pi^9 |K|^2/(6144s).                 (11)
```

Also sqrt(q(k0))=|K|/L [1+O(|K|^2/L^2)]. Thus

```text
nu_j(sL/v,K)=v|K|/L [1+O_s(|K|^2)]                   (12)
```

as K tends to zero through nonzero allowed momenta. The constants are
independent of the number of boxes and of L>=2. This controls both
polarizations, including any splitting between them, not a single chosen
source matrix element. For K sufficiently small the two endpoint levels
are below 2v/L and approximate the complete principal one-particle low
fiber, while all nonprincipal fine aliases lie above that threshold.

For a positive regulator the same proof gives the exact variant

```text
epsilon_rho(K)=eta(K) omega0/sqrt(4v^2/L^2+rho^2),
omega0=sqrt(v^2 q(k0)+rho^2),
omega0<=nu_j<=omega0+tau^(-1)log(1+epsilon_rho(K)).      (13)
```

One should not replace epsilon_rho by its massless cubic expression at
arbitrary fixed rho. That simplification is uniform when rho L/v is at
most a fixed multiple of |K|. At K=0 the exact separate formula (6)
applies. These distinctions keep the infrared and volume limits honest.

There is also a whole low-Fock-window consequence in the finite model with
harmonic zero modes removed. Identify the coarse one-particle space with
the principal transverse fibers and put H0=dGamma(omega0(K)I_(p_K)).
Since B_(tau,K)>=omega0(K)I, K_tau>=H0. Moreover H0 commutes with K_tau:
the first operator is scalar in each polarization fiber. On H0<=E,
every occupied momentum satisfies |K|<=pi L E/(2v), so (11), summed over
particles, gives

```text
H0<=K_tau<=(1+delta_E)H0 on ran 1_[0,E](H0),
delta_E=pi^11 (LE/v)^2/(24576s).                       (14)
```

There is no particle-number factor in this relative form estimate. If
E<2v/L, the complete fine oscillator window below E contains no high-alias
quantum, so it lies entirely in the principal Fock model. For discrete
eigenvalue counts one obtains

```text
N_fine(E/(1+delta_E))<=N_endpoint(E)<=N_fine(E),
                         0<E<2v/L.                   (15)
```

The same inequalities hold on the full residual compact-group invariant
space, using invariant Fock restriction and the equivariant identification
of the principal fibers. They are not claims about a physical one-particle
singlet. Each finite nonzero-mode model has a positive minimum frequency;
the estimates are uniform in its volume, but no infinite-volume Gaussian
Hilbert realization is silently inferred from them.

## 4. The unweighted row Gram is local; the marginal Gram is different

The full unconstrained coarse row Gram R R^* is diagonal in link component.
This is the auxiliary cochain R, not the anchored derivative T=R-d0c Phi.
The exact one-dimensional fourth-alias moment is

```text
sum_r |a_i((K_i+2pi r)/L)|^4
 =(2+cos K_i)/3+(1-cos K_i)/(3L^2).
```

Using the other two Parseval sums gives

```text
(RR^*)_i(K)=L^(-1)[A_L+B_L cos K_i],
A_L=(2L^2+1)/(3L^2),       B_L=(L^2-1)/(3L^2),
1/(3L)<=RR^*<=1/L.                                    (16)
```

In real coarse coordinates, this is L^(-1)[A_L I+B_L P_i], where
P_i=(T_i+T_i^*)/2 is the nearest-neighbor averaging operator in direction i.
Since r_L=B_L/A_L<1/2,

```text
(RR^*)_i^(-1)=(L/A_L)sum_(n>=0)(-r_L)^n P_i^n.         (17)
```

A kernel entry at coarse cyclic distance d in this direction vanishes for
every n<d. Summing the geometric majorant proves

```text
|[(RR^*)_i^(-1)]_(x,y)|<=3L .2^(-d),                  (18)
```

and it is zero between distinct lines in the other two directions. The
inverse square root has a similar bound from its binomial series, for
example 2sqrt(3L/2) .2^(-d). All of these bounds are uniform in coarse
period. L=1 has B_L=0 and the identity map as expected.

This observation does not make every relevant normalization local. The
physical compression P_(C_c)RR^*P_(C_c) may involve the coarse Coulomb
projector. More decisively, the actual marginal is
G=W^*Omega^(-1)W, not RR^*. The inverse-frequency factor carries the
massless/regulated long-distance covariance and must remain in (5).

## 5. The actual Gaussian baseline already has a leading score

Use Euclidean coordinates q,z with unit kinetic metric, and a fixed
positive precision matrix

```text
Omega_base=[[A,B],[B^*,C]]>0.
```

The oscillator frequencies are Omega_base/g^2 and its true ground density
is proportional to exp(-< (q,z),Omega_base(q,z)>/g^2). The normalized
conditional law of z at q is Gaussian with mean -C^(-1)B^*q and covariance
(g^2/2)C^(-1). Its exact intrinsic score, with zero product-metric
horizontal connection, is

```text
s(q,z)=-(2/g^2)B[z+C^(-1)B^*q],
I(q)=(2/g^2)B C^(-1)B^*.                              (19)
```

It is independent of q. It vanishes exactly when B=0, equivalently when
the coordinate source subspace reduces Omega_base. When B!=0, restricting
q to a shrinking rescaled compact set does not remove this score. A fast
inverse of order g^2 leaves a generally order-one relative Schur effect,
not the special strip's O(g^2) or O(g^4) relative loss.
An invertible coarse-coordinate rescaling transforms the Fisher matrix
and kinetic cometric oppositely, so the weighted conclusion is independent
of the choice of normalized Euclidean source coordinates.

This occurs for the ACTUAL averaged-path map, not only an invented Gaussian
observation. Set n=6,L=2 and coarse K=(2pi/3,0,0). Choose the transverse
coarse polarization e2. Only two fine aliases contribute, with Euclidean
source weights 3/4 and 1/4. Their fine frequencies in units of v are 1 and
sqrt(3); set v=g^(-2) in this example. Rephase the two fine coordinates and
rotate to the unit Euclidean
source vector (sqrt(3)/2,1/2) and its orthogonal complement. The precision
blocks in (19) are exactly

```text
A=(3+sqrt(3))/4,
C=(1+3sqrt(3))/4,
B=(3-sqrt(3))/4 !=0.                                 (20)
```

Thus the conditional Fisher in that normalized physical-coordinate block
is 2B^2/(C g^2), a strictly positive multiple of g^(-2). The complex Fourier
calculation realifies into the paired cosine/sine coordinates with the
same positive coefficient. Tensoring with the color representation keeps
the covariance and the full simultaneous gauge-invariant polynomial
algebra. This is a tangent Gaussian statement, not an assertion about the
nonlinear Wilson ground at that momentum.

## 6. A complete invariant example also separates static and endpoint memory

Take the two-mode precision Omega_base=[[2,1],[1,2]], with eigenfrequencies
1 and 3 in units g^(-2), and observe the first original coordinate.
Equation (19) gives I=1/g^2. In normalized one-particle source/fiber
coordinates the Hamiltonian matrix is

```text
h1=g^(-2)[[3/2,sqrt(3)/2],[sqrt(3)/2,5/2]].            (21)
```

The actual marginal normalization gives source weights 3/4 at frequency
1 and 1/4 at frequency 3. At tau=s g^2,

```text
M_tau=(3/4)exp(-s)+(1/4)exp(-3s),
B_tau=-(1/(s g^2))log M_tau.                          (22)
```

Equation (2) determines every endpoint particle sector exactly from this
one number. The static Schur complement behaves differently. In units
g^(-2), its one-particle retained energy is a1=3/2, its loss is 3/10,
and its unnormalized Schur value is k1=6/5. On the symmetric two-particle
basis (source-source, normalized source-fiber, fiber-fiber), the matrix is

```text
h2=[[3,sqrt(3/2),0],
    [sqrt(3/2),4,sqrt(3/2)],
    [0,sqrt(3/2),5]].                                  (23)
```

Eliminating the last two coordinates gives

```text
loss2=15/37,       k2=96/37 !=2k1,
loss2/a2=5/37.                                       (24)
```

The ratio is independent of g and is a genuine static loss, not merely
failure of a Fisher upper bound. The normalized graph-source values also
fail additivity: they are 15/14 and 444/191, respectively, rather than the
second being twice the first.

This example has a physical invariant realization. Tensor the two spatial
modes with an adjoint color space and use the normalized invariant pair
vectors sum_a a^*(source,a)^2 Omega, sum_a a^*(source,a)a^*(fiber,a)Omega,
and sum_a a^*(fiber,a)^2 Omega. Their normalizations give exactly (23).
The first retained pair is the centered radial class source of the
observed coordinate. Thus even an invariant radial source can have the
nonvanishing relative baseline (24) when the true quadratic ground is
coupled. The special nonlinear strip estimate cannot be transferred to a
different nonreducing harmonic geometry by assuming all leading scores
have already canceled.

## 7. What the nonlinear comparison must now preserve

The local path block has a completely specified Gaussian endpoint baseline:
the exact alias covariance (5), the fixed-time second quantization (2), and
the uniform low-momentum comparison (11)-(15). Its full static Schur memory
is distinct. The exact examples (19)-(24) prohibit replacing this baseline
by an assumed small total conditional score on every coupled block.

The next actual Wilson target is the nonlinear excess relative to this
quadratic endpoint or memory, with its true source normalization and
physical clock preserved. The necessary estimates must control that
excess on a complete relevant energy/source window, and include any
high retained states and fast tails. Neither the exact Gaussian identity
nor the local row-Gram inverse constructs interacting Wilson convergence,
an OS-history map, a compatible multiscale hierarchy or a continuum vacuum.

## Evidence boundary

The accompanying exact controls check functorial tensor compression in
several finite particle sectors, the coupled one-/two-particle static
numbers, the exact Gaussian score and the n=6,L=2 path weights, row-Gram
moment coefficients and the scalar alias-bound constants. They do not
replace Wick density, closed direct-sum domains, logarithm calculus or
the all-volume analytic estimates proved above. No numerical glueball
input is part of this argument.

The verifier is [check_gaussian_endpoint_baseline.py](../../runs/gaussian_path_nonlinear_input_2026-09-06/check_gaussian_endpoint_baseline.py);
its exact result is [gaussian_endpoint_baseline_controls_frozen.json](../../runs/gaussian_path_nonlinear_input_2026-09-06/gaussian_endpoint_baseline_controls_frozen.json).
From the reproduction run directory, replay it with
`python check_gaussian_endpoint_baseline.py --replay gaussian_endpoint_baseline_controls_frozen.json`.
The report pins the proof and verifier bytes. It rejects an altered report,
an existing output destination, and execution with assertions disabled.

## Canonical provenance and reproduction

The [original derivation](../../runs/gaussian_path_nonlinear_input_2026-09-06/EXACT_GAUSSIAN_PATH_ENDPOINT_BASELINE.md) is preserved
with SHA256 `fa237619dd29c63f04a02abea6a0061ba131a4ec9db347d989757762812bcea8`. This copy changes only stage metadata and links,
normalizes line endings and appends this separate provenance record.
The [sealed run](../../runs/gaussian_path_nonlinear_input_2026-09-06/README.md) contains the original controls
and independent reviews; their finite algebraic scope does not certify the
full analytic theorem by itself.

- [check_gaussian_endpoint_baseline.py](../../runs/gaussian_path_nonlinear_input_2026-09-06/check_gaussian_endpoint_baseline.py)
- [gaussian_endpoint_baseline_controls_frozen.json](../../runs/gaussian_path_nonlinear_input_2026-09-06/gaussian_endpoint_baseline_controls_frozen.json)
- [INDEPENDENT_GAUSSIAN_ENDPOINT_REVIEW.md](../../runs/gaussian_path_nonlinear_input_2026-09-06/INDEPENDENT_GAUSSIAN_ENDPOINT_REVIEW.md)
- [GAUSSIAN_ENDPOINT_VALIDATION.json](../../runs/gaussian_path_nonlinear_input_2026-09-06/GAUSSIAN_ENDPOINT_VALIDATION.json)
