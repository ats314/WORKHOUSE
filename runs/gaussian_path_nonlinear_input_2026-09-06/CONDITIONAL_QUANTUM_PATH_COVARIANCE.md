# Conditional quantum covariance of the actual path source

Outputs-only research continuation, 6 September 2026. The current local-path
and full Gaussian source results are established inputs. The statements here
concern the actual harmonic path map on a fixed block scale L, its complete
conditional Gaussian fiber, and the spatial kernel of that covariance. They
do not supply a nonlinear interacting conditional measure or continuum limit.

## 1. Inputs, normalization and provenance

Use the original periodic positive-edge convention in
`paper/research_notes/G19_LOCAL_COVARIANT_AVERAGED_PATH_SOURCES_20260905.md`.
The fine period is n=Lm, n>=3, L>=2. On fine and coarse transverse spaces
E=ker d0* and E_c=ker d0c*, let

```text
K_E=d1*d1,       W=R*|E_c,       S=ran W,
R d0=d0c B,     T*|E_c=R*|E_c,
K_E >= kappa_L (I_E-P_S),     kappa_L=1/(33L^2).
```

T is the tangent of the actual gauge-covariant matrix-valued path average.
R and T have the same physical cotangents, although their actions on vertex
gradients use different restriction maps. The three harmonic edge directions
belong to S. These assertions are already proved in the input note; they are
not new consequences of covariance manipulation.

Set v>0, rho>0 and

```text
Omega_rho=(v^2 K_E+rho^2 I_E)^(1/2),       C_rho=Omega_rho^(-1).
```

For the actual unit-kinetic Gaussian oscillator, the vacuum density is
proportional to exp(-<A,Omega_rho A>). Its coordinate covariance is C_rho/2.
All matrices called C below are therefore **twice** their probability
covariances. The color matrix is the identity on a fixed compact simple
adjoint space; v^2=2 b_rep u in the established representation convention.

The path-sum linear average is not unprecedented. After translating centered
versus corner cubes, Dimock's Q in [arXiv:1712.10029v3, section 3.1,
equation (189)](https://arxiv.org/html/1712.10029v3#S3.SS1) is R/L. His
conditional covariance in section 3.7.3, equations (304)-(307), is built from
a gauge-fixed second-order Laplacian and an explicit local gauge correction.
The exponential bounds there, equations (308)-(309), do not apply merely by
replacing that precision with the quantum ground precision Omega_rho.
The conditioning identity itself is standard Gaussian square completion.
The new calculation below is its phase-correct application to this quantum
path source, including low-pole cancellation and its transverse regularity.

## 2. Entire conditional fiber and its exact precision

W is injective on E_c. The Gram G=W*C W is positive there. Conditioning on
the whole linear observation W*A gives mean C W G^(-1)y and covariance

```text
Cov(A | W*A=y)=C_fast/2,
C_fast=C-CW(W*CW)^(-1)W*C.                             (1)
```

Let F=ker W*=S-perp inside E, let Q_F be its Euclidean orthogonal projection,
and write Omega_F=Q_F Omega Q_F|F. Completing the exponent on the affine
fiber gives the equivalent exact identity

```text
C_fast=Q_F Omega_F^(-1) Q_F.                          (2)
```

For an algebraic verification, (1) is self-adjoint, W*C_fast=0, and
Q_F Omega C_fast=Q_F. These determine the inverse in (2). In particular
C_fast>=0, its range is exactly F, and its kernel inside E is S. This is
not the compression Q_F C Q_F, which generally differs.

The established full K bound and monotonicity of square root imply

```text
Omega >= c_rho Q_F,
Omega_F >= c_rho I_F,
0<=C_fast<=c_rho^(-1)Q_F,
c_rho=sqrt(v^2 kappa_L+rho^2)>=v/(sqrt(33)L).           (3)
```

The conditional fiber is complete: no excited coordinate or occupation is
truncated. Its probability measure has precision Omega_F in the density
exp(-<x,Omega_F x>). With Dirichlet form (1/2) integral |grad_F f|^2, its
Ornstein-Uhlenbeck gap is inf spec Omega_F, hence at least c_rho. Equivalently
its vacuum-subtracted fiber oscillator has those one-particle frequencies.
The factor 1/2 in both covariance and Dirichlet form is essential.

Integrating this conditional Poincare inequality over the exact marginal,
and using |grad_F f|<=|grad f|, recovers the entire literal quantum bound
H>=c_rho(I-P_literal). This is consistent with the established
inverse-frequency Fock source R_Fock=Omega^(-1/2)S. Formula (2) is a useful
coordinate form of that same mechanism, not a replacement of R_Fock by S.
The conditional family is equivariant in the coarse value; the full bound
restricts to the residual invariant Fock space as in the existing proof.

## 3. Exact cancellation of the principal alias pole

Use the unitary coarse Bloch decomposition. Near coarse momentum K=0 choose
principal k0=K/L and the other L^3-1 fine aliases. At K!=0 the principal
transverse space is two-dimensional; at K=0 it is three-dimensional.

Write q(k)=4 sum_j sin^2(k_j/2), d_j(k)=exp(ik_j)-1 and
P(k)=I-d(k)d(k)*/q(k) away from a zero. At the principal zero use P(0)=I.
The established symbols are

```text
a_j(k_j)=L^(-1) sum_(s=0)^(L-1) exp(ik_j s),
a(k)=product_j a_j(k_j),
r_i(k)=L^(-1/2) a(k)a_i(k_i).
```

All r_i(k0) are nonzero. Principal matching reparametrizes the physical
source, without changing its range, as W=(I;V) from the principal transverse
space to principal plus high aliases. Embedded in fixed three-component
principal coordinates it is

```text
P0=P(k0),
V_r=diag_i(conjugate(r_i(k_r)/r_i(k0))) P0,    r!=0.   (4)
```

The phase-sensitive cochain identity makes V_r transverse at its high
alias. No continuous choice of a two-vector transverse frame is required.

On the physical alias spaces the covariance is diag(omega0^(-1)I,C_h), where
omega0=sqrt(v^2q(k0)+rho^2), and C_h is the direct sum of
P(k_r)/sqrt(v^2q(k_r)+rho^2). Put

```text
A=V*C_hV,       Z=(I+omega0 A)^(-1).
```

A=P0 A P0, and Z may be taken on the fixed three-dimensional principal
ambient space, acting as identity on its unused longitudinal direction.
Direct substitution in (1), or a Schur inversion, gives

```text
C_fast,00 = A Z,
C_fast,0h = -Z V*C_h,
C_fast,h0 = -C_h V Z,
C_fast,hh = C_h-omega0 C_h V Z V*C_h.                 (5)
```

For example omega0^(-1)I-omega0^(-2)(omega0^(-1)I+A)^(-1)
equals A(I+omega0 A)^(-1). Thus the singular principal covariance cancels
as a matrix, including its transverse polarization dependence. There is
no approximation and no inverse of an unregulated flat covariance in (5).

For fixed L, uniformly for small K and 0<=rho/v<=epsilon_* with fixed finite
epsilon_*, the high covariance is bounded and smooth, and V=O_L(|K|).
Consequently

```text
C_fast,00=O_L(|K|^2/v),
C_fast,0h=O_L(|K|/v),
C_fast,hh=C_h+O_L((rho/v+|K|)|K|^2/v).                (6)
```

In the massless case the relative weighted correction omega0 A is
O_L(|K|^3). This is the weighted high/principal tail also encountered in
the independently derived endpoint baseline; it is stronger than the
unweighted O(|K|^2) source-tail norm estimate. It does **not** by itself
make the transverse mixed covariance analytic.

At K=0 every high source symbol vanishes and the observation retains all
three principal harmonic coordinates. Hence the exact conditional block
is diag(0,C_h(0)), for every rho>0. Formula (5) extends continuously to this
value. Its rho down to zero limit is finite. On each finite torus, the
massless joint Gaussian still has no normalized flat vacuum. One may define a
normalized Gaussian on each affine fiber: Omega_F remains strictly
positive and all flat directions are fixed by the observation. This is a
conditional fiber kernel, not a construction of an unregulated joint vacuum.
The fast dimension is 2L^3-2 both off and at K=0: at zero, the fine and
coarse transverse spaces each acquire exactly one additional direction.

## 4. Fixed-scale summability theorem

Fix L>=2 and epsilon_*<infinity. In fixed physical-edge coordinates within
a block, let F_epsilon(K) be the matrix symbol C_fast with v scaled to one
and epsilon=rho/v. It is a 3L^3 by 3L^3 ambient matrix with zero action on
unphysical directions. The following constants may depend on L and
epsilon_*, but not on m, the color dimension or 0<=epsilon<=epsilon_*.

**Claim.** There is a constant B_(L,epsilon_*) such that the infinite-block
kernel and every finite torus periodization obey

```text
||C_fast,infinity(x)||op <= B_(L,epsilon_*)/v (1+|x|)^(-4),
sup_(m,rho) sum_(x in (Z/mZ)^3) ||C_fast,m(x)||op
    <= B'_(L,epsilon_*)/v.                            (7)
```

The finite kernels also obey the sum of the right-hand infinite-kernel
bound over x+mZ^3. In particular they have a uniformly summable spatial
kernel in block distance. This theorem asserts no uniform-in-L bound on
B_(L,epsilon_*). The separate norm estimate (3) has its explicit all-L
constant sqrt(33)L/v.

These are operator norms on the full 3L^3-dimensional intra-block spatial
matrix. An absolute row sum over individual spatial components is at most
sqrt(3L^3) times this block-operator row sum. The probability covariance
has an additional factor 1/2. Tensoring by the color identity changes
neither operator-norm bound nor a fixed-color component row sum; separate
vertex color contractions must retain their actual tensor factors.

Here is a derivative proof, rather than an inference from (3).

Choose a small fixed coarse momentum ball around zero. Every high alias
has q(k_r)>=c_L>0 there, so all derivatives of C_h are uniformly bounded
for epsilon in the compact interval. Every high ratio in (4) is analytic,
vanishes at zero, and has bounded derivatives. Meanwhile

```text
||partial^alpha P0|| <= C_(L,alpha)|K|^(-|alpha|).
```

This follows directly from P0=I-d0d0*/q0 and q0 comparable to |K|^2.
The principal d0 has a simple zero; quotient differentiation gives the
displayed bound. Product differentiation therefore gives

```text
||partial^alpha V|| <= C_(L,alpha)|K|^(1-|alpha|),
||partial^alpha A|| <= C_(L,alpha)|K|^(2-|alpha|).       (8)
```

For omega0/v=sqrt(q0+epsilon^2), its value is uniformly bounded, and for
|alpha|>=1 its derivatives are bounded by
C_alpha |K|^(1-|alpha|), uniformly including epsilon=0. This follows by
ordinary differentiation, using q0+epsilon^2>=c|K|^2. Since A>=0,
||Z||<=1. Repeatedly differentiating (I+omega0 A)Z=I then gives, for
|alpha|>=1,

```text
||partial^alpha Z|| <= C_(L,alpha)|K|^(2-|alpha|).
```

The bound is deliberately uniform for a nonzero epsilon; at epsilon=0
the leading correction is one order smaller. Applying these bounds to
(5) and subtracting the smooth block B=diag(0,C_h) yields

```text
||partial^alpha(F_epsilon-B)||
       <= C_(L,alpha)|K|^(1-|alpha|),    |alpha|<=5.   (9)
```

So far these are alias coordinates. The unitary matrix from aliases to
the fixed intra-block coordinates has entries proportional to
exp(i(K+2pi r).x/L). It is smooth with bounded derivatives on this ball;
conjugation preserves (9), with a conjugated smooth B. Away from zero the
fixed-coordinate symbol is smooth and periodic. To see that no chart
singularity has been hidden, express the coarse Gram inverse on E_c as
(P_c G P_c+I-P_c)^(-1) on three coordinates. Both it and the positive
fine covariance are smooth and uniformly invertible on the relevant
subspaces on compact sets avoiding K=0. The finite path matrix is a
periodic Bloch matrix. Alias changes at the boundary merely permute the
smooth presentation of this same matrix.

For completeness, (9) implies the Fourier estimate in (7). A dyadic
partition near zero has annuli of radius lambda=2^(-j). The remainder's
L1 norm on one annulus is at most C lambda^4, and its fifth derivative's
L1 norm is at most C lambda^(-1). Integration by parts five times in a
coordinate with |x_i|>=|x|/sqrt(3) gives

```text
||Fourier(annulus remainder)(x)||
    <=C lambda^4 min(1,(lambda|x|)^(-5)).              (10)
```

Summing annuli above and below lambda=1/(1+|x|) gives C(1+|x|)^(-4).
The smooth part decays at least as fast after five integrations by parts.
Matrix operator norms obey the same integral estimate; the matrix size
is fixed with L. Since exponent 4 exceeds the spatial dimension 3, the
coefficients are absolutely summable and their Fourier series converges
uniformly, including the specified K=0 value. Sampling that series on a
coarse torus proves exact periodization

```text
C_fast,m(x)=sum_(p in Z^3) C_fast,infinity(x+mp).        (11)
```

Absolute summability and the triangle inequality yield the uniform row
sum in (7). This also explains why a rank change in the *unconditioned*
principal transverse space does not create a torus-volume divergence:
the whole conditioned symbol has the continuous extension already proved.

## 5. An explicit non-exponential boundary

There is in general no exponential spatial bound for this matrix kernel,
even with rho>0. The obstruction is visible at L=2, without numerics.
Take high alias (pi+K1/2,K2/2,K3/2). The exact ratio in its first direction is

```text
a_high/a_principal=-i tan(K1/4).
```

Consequently its matched source block has leading
V_h=(iK1/4) P_(e1-perp) P_(K-perp)+O(|K|^2). The high covariance tends to
P_(e1-perp)/sqrt(4v^2+rho^2). Formula (5) therefore gives

```text
C_fast,0h(K)= iK1/[4sqrt(4v^2+rho^2)]
                 P_(K-perp)P_(e1-perp)+O(|K|^2).       (12)
```

Its yy entry has homogeneous leading term proportional to
K1(1-K2^2/|K|^2). Along K=t(1,0,0), t(0,1,0), and t(1,1,0), the
directional coefficients, after removing the common prefactor, are
1, 0 and 1/2. They cannot be values of one linear derivative. Thus the
symbol is continuous but not differentiable at zero. The smooth invertible
alias-to-block transformation cannot turn it into a differentiable symbol.

Exponentially summable block coefficients would give a real-analytic
Fourier symbol by absolutely differentiating their series, contradicting
(12). This is not a claim that every gauge-invariant field-strength kernel
has the same tail: curls or a different local gauge repair can change the
observable and remove particular directional factors. It is the precise
boundary of exponential locality for the specified ambient transverse
conditional coordinate covariance. The summability theorem above remains
valid, and is sufficient for estimates based on an absolute spatial row sum.

## 6. Exact controls and remaining mathematical obligation

The companion `check_conditional_quantum_covariance.py` retains three
independent finite controls:

1. Rational noncommuting Gaussian matrices, direct conditioning versus the
   compressed-precision inverse, all blocks of (5), and the arbitrary-symbol
   orders t^2, t and t^3 when V=tB and omega0=t.
2. An actual L=2, n=4 alias block at coarse (pi,0,0). Choose v^2=84,
   rho^2=121: its exact frequencies are 17,25,31, so the complete physical
   covariance and source calculation lies in Q(i). All physical omitted
   directions remain in the matrix inverse.
3. Exact Taylor and directional algebra for (12), including the failed
   linear-derivative test. This controls the concrete non-exponential witness.

Finite controls certify these algebraic statements, not the derivative
inequalities, dyadic Fourier proof, all-volume passage or Gaussian density
theorems. Those are the explicit analytic arguments above.

The result closes a harmonic conditional-covariance locality question at
each fixed scale: the low pole cancels, the complete fiber has a uniform
gap, and its coordinate covariance has a summable spatial kernel. It does
not bound its conditional score by a small constant, construct an
interacting product law, identify the nonlinear true-ground source range,
or control an entire scale hierarchy. Uniform-in-L derivative constants,
if needed, require a separate quantified alias estimate; they are not
silently supplied by the all-L operator norm bound.
