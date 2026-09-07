# Dynamic conditional path covariance and connected cubic fiber energy

Outputs-only analytic continuation, 6 September 2026. This note advances the
time-integrated Gaussian input to the nonlinear-excess route of G19. It does
not compute the complete nonlinear Wilson coefficient. Its principal input is
the established fixed-scale conditional covariance theorem in
`paper/research_notes/G19_CONDITIONAL_QUANTUM_PATH_COVARIANCE_20260906.md`.
The companion exact checks certify finite algebra and Wick denominators;
they do not machine-certify the Fourier estimates below.

## 1. Statement and exact hypotheses

Fix L >= 2, 0 <= epsilon = rho/v <= epsilon_* < infinity, and v > 0.
The fine period is n = Lm >= 3. Use the actual physical averaged-path map,
the Euclidean transverse edge space E, S = ran W and F = S-perp in E from
the input theorem. All spaces include every physical alias and color.
Let

```
c = 1/(sqrt(33) L),             M = sqrt(12 + epsilon_*^2),
Omega = (v^2 K_E + rho^2)^(1/2),
Omega_F = Q_F Omega Q_F |_F,
C_fast = Q_F Omega_F^(-1) Q_F,
Sigma_t = (1/2) Q_F Omega_F^(-1) exp(-t Omega_F) Q_F.
```

For rho = 0, these formulas define the normalized affine-fiber Gaussian
and its stationary OU process. They do not define a normalized massless
joint Gaussian. For rho > 0 they are the exact conditional covariances of
that joint Gaussian. The fiber generator on centered functions is

```
L_F = -(1/2) Delta_F + <Omega_F z, grad_F>,
E[Z_0 Z_t^*] = Sigma_t.
```

There is B = B(L, epsilon_*) < infinity, independent of m, rho/v and t,
such that in block coordinates, with a = c/2,

```
||Sigma_t,infinity(x)||op <= (B/v) exp(-a v t) (1+|x|)^(-4),       (1)
Sigma_t,m(x) = sum_(p in Z^3) Sigma_t,infinity(x+mp),              (2)
sup_m sum_x ||Sigma_t,m(x)||op <= (B_1/v) exp(-a v t),            (3)
sup_m integral_0^infinity sum_x ||Sigma_t,m(x)||op dt
    <= B_1/(a v^2).                                             (4)
```

This proves the requested integrable time envelope, with its polynomial
factor equal to one. No constants in (1)-(4) are claimed uniform in L.
An individual spatial-component absolute row sum costs at most
sqrt(3L^3) relative to the block-operator row sum. Color identity adds no
color-dimension factor to either covariance bound.

## 2. A fixed spectral band removes the moving-frame problem

Set H_epsilon(K) = v C_fast(K), an ambient 3L^3 by 3L^3 Hermitian matrix
in the fixed physical-edge block coordinates. The input gives

```
spec H_epsilon(K) subset {0} union [1/M, 1/c].                    (5)
```

Indeed c v <= Omega_F <= M v; the second bound follows from K_E <= 12.
The fast rank is 2L^3-2 both at K = 0 and away from it. The singular
unconditioned principal transverse projector does not cause a rank jump
of H. No choice of a transverse two-frame is made below.

Write s = vt, g_s(z) = z exp(-s/z) on the positive spectral island and
give g_s the value zero on a disjoint neighborhood of the zero island.
Spectral calculus gives the exact ambient identity

```
Sigma_t(K) = (1/(2v)) g_s(H_epsilon(K)).                          (6)
```

The definition at the zero island is essential: it does not mean inserting
an inverse for the unphysical or retained zero eigenvalues.

Choose one positively oriented contour Gamma around [1/M,1/c], excluding
zero, with uniformly positive spectral distance and

```
Re(1/z) >= c/2   for all z in Gamma.                             (7)
```

Such a contour exists because the compact positive interval lies strictly
inside {z : Re(1/z) > c/2}; a sufficiently thin rounded rectangle suffices.
Its distances and length depend only on L and epsilon_*. Consequently

```
g_s(H) = (1/(2 pi i)) integral_Gamma
                  z exp(-s/z) (zI-H)^(-1) dz,                   (8)
|z exp(-s/z)| <= C exp(-cs/2).
```

All resolvent norms on Gamma are bounded by a fixed constant, uniformly
in the momentum, regulator and time. Repeated eigenvalues inside the
positive island are harmless; (8) never differentiates their eigenvectors.

## 3. Transfer of the conormal derivative bound

Here are the exact static analytic inputs being used. On a fixed small
ball around K = 0 there is a smooth ambient matrix B_epsilon(K) such that

```
H_epsilon = B_epsilon + R_epsilon,
||partial^alpha R_epsilon(K)|| <= C_alpha |K|^(1-|alpha|),
                                                  |alpha| <= 5. (9)
```

The derivatives of B are uniformly bounded. In alias coordinates it is
diag(0, v C_h), conjugated by the smooth alias-to-block unitary. Both B
and H have spectrum in {0} union [1/M,1/c] after reducing the ball if
necessary. To verify the upper endpoint for B, take |K|_infinity small
enough that every high alias has |k_j| modulo 2pi >= pi/L in at least
one coordinate. Then q(k) >= 4 sin^2(pi/(2L)) >= 4/L^2 > c^2.
The lower endpoint follows again from q <= 12 and epsilon <= epsilon_*.

For clarity, (9) is precisely the existing pole-cancellation result:
V = O(|K|), A = V^* C_h V = O(|K|^2), and

```
C_fast,00 = A (I+omega_0 A)^(-1),
C_fast,0h = -(I+omega_0 A)^(-1) V^* C_h,
C_fast,hh = C_h - omega_0 C_h V(I+omega_0 A)^(-1)V^*C_h.
```

The singular principal projector has derivatives O(|K|^(-|alpha|)),
but is multiplied in V by a ratio vanishing to first order. Thus the
mixed block has the order-one remainder in (9), uniformly through the
regulator limit. The fast covariance at zero is exactly diag(0,C_h(0)).

Set R_z(H) = (zI-H)^(-1). The resolvent identity is

```
R_z(H)-R_z(B) = R_z(H) R_epsilon R_z(B).                         (10)
```

Its differentiated products are uniformly bounded by

```
||partial^alpha [R_z(H)-R_z(B)]||
       <= C_alpha |K|^(1-|alpha|),    |alpha| <= 5.              (11)
```

Here is explicit derivative bookkeeping. Every derivative of a resolvent
is a finite sum of products of resolvents and nonzero derivatives of its
matrix argument. Expand each derivative of H as a derivative of B plus
a derivative of R. Every term in the differentiated (10) has at least
one R or derivative of R. If k >= 1 such factors receive a total of r
derivatives, they contribute at most C |K|^(k-r). The remaining smooth
derivatives are bounded. Since r <= |alpha|, k-r >= 1-|alpha|, which
implies (11) on |K| <= 1. This argument also includes undifferentiated R.

Insert (11) in (8). Uniformly for s >= 0,

```
||partial^alpha [g_s(H)-g_s(B)]||
 <= C_alpha exp(-cs/2) |K|^(1-|alpha|),  |alpha| <= 5,            (12)
||partial^alpha g_s(B)|| <= C_alpha exp(-cs/2), |alpha| <= 5.
```

Away from zero, the original fixed-coordinate H is smooth and periodic
with uniformly bounded derivatives; (8) gives the second bound there too.
Cutoff derivatives preserve these bounds. This proves the necessary
regularity without ever pretending that F or a transverse frame is fixed.

## 4. Fourier decay, periodization and time integration

Use a dyadic partition on the momentum ball. On a shell of radius lambda,
(12) gives an L1 bound C exp(-cs/2) lambda^4 and a fifth-derivative L1
bound C exp(-cs/2) lambda^(-1), including derivatives of the cutoff.
Five integrations by parts in a coordinate with |x_i| >= |x|/sqrt(3)
therefore bound the shell Fourier coefficient by

```
C exp(-cs/2) lambda^4 min(1,(lambda |x|)^(-5)).                   (13)
```

Sum shells at lambda below and above (1+|x|)^(-1). Each sum is bounded by
C exp(-cs/2) (1+|x|)^(-4). The smooth part obeys the same bound. Restoring
1/(2v) proves (1). The proof is in a finite-dimensional operator norm;
it is independent of the number of coarse blocks.

Since 4 > 3, the Fourier coefficients are absolutely summable uniformly
in K. Sampling their uniformly convergent Fourier series on the coarse
torus gives (2), including the exact continuous K=0 value. Triangle
inequality proves (3); Tonelli and the elementary exponential integral
prove (4). This argument controls absolute spatial rows before time
integration, not just the operator norm of an integrated covariance.

## 5. Exact two-time connected Lie-cubic formula

Let the real spatial tensors D_ijk and E_lrs be alternating, with sums
over all ordered triples. Let the invariant color tensor f_abc satisfy
sum_bc f_abc f_dbc = C_A delta_ad; write d = dim Lie(G). For a fixed
conditional mean m and the stationary fiber OU process Z_t, put

```
P_D(x) = sum_ijk,abc D_ijk f_abc x_i^a x_j^b x_k^c,
F_D(t) = P_D(m+Z_t) - P_D(m).
```

Every same-time internal contraction repeats two colors of f and is zero.
The force is conditionally centered. Its mutually orthogonal Wick degrees
1, 2 and 3 remain orthogonal at two times. With sigma_t = Sigma_t,

```
E[F_D(0) F_E(t)]
 = 9 sum D_ijk E_lrs sigma_t,ks
                    <[m_i,m_j],[m_l,m_r]>
 +18 C_A sum D_ijk E_lrs sigma_t,jr sigma_t,ks <m_i,m_l>
 + 6 C_A d sum D_ijk E_lrs sigma_t,il sigma_t,jr sigma_t,ks.      (14)
```

The factors are 3^2, 3^2 2!, and 3!. Alternation of the spatial tensor
and of f cancels the signs from exchanged cross pairings. No independence
of spatial sites is assumed.

For an exact finite-torus spectral formula, choose a real orthonormal
eigenbasis e_alpha of Omega_F, with frequency lambda_alpha > 0. Then

```
sigma_t,ij = sum_alpha e_i,alpha e_j,alpha
                          exp(-lambda_alpha t)/(2lambda_alpha).
```

Integrating each term in (14) gives the fiber energy
E_F(D,E;m) = <F_D,L_F^(-1)F_E>, with propagator replacements

```
integral sigma_t,ks dt
 = sum_alpha e_k,alpha e_s,alpha /(2lambda_alpha^2),

integral sigma_t,jr sigma_t,ks dt
 = sum_alpha,beta e_j,alpha e_r,alpha e_k,beta e_s,beta
     /[4lambda_alpha lambda_beta (lambda_alpha+lambda_beta)],

integral sigma_t,il sigma_t,jr sigma_t,ks dt
 = sum_alpha,beta,gamma
     e_i,alpha e_l,alpha e_j,beta e_r,beta e_k,gamma e_s,gamma
     /[8lambda_alpha lambda_beta lambda_gamma
                    (lambda_alpha+lambda_beta+lambda_gamma)].  (15)
```

Thus each Wick degree has its actual sum-of-frequencies energy denominator,
in addition to its probability-covariance factors. Replacing equal-time
variance by a single chosen denominator would discard this information.

## 6. Uniform rooted fiber-energy bound

For local alternating vertices D_v, assume

```
a_v = sum_ijk |D_v,ijk|,       A = sup_v a_v < infinity,
a_* = sup_k sum_v,ij |D_v,ijk| < infinity,
beta_G = sup_(|x|=|y|=1) |[x,y]|.
```

Use |m_i| <= M_0 on both vertex supports. The bound may be enforced by
retained cutoffs 0 <= chi_v(y) <= 1 with precisely this support property.
Let Sbar be the constant in the component version of (3), so that

```
S_t = sup_i sum_j |sigma_t,ij| <= (Sbar/v) exp(-a v t),
sigma_*,t = sup_ij |sigma_t,ij|
          <= (sigmabar/v) exp(-c v t),    sigmabar = 1/(2c).
```

The second estimate is the exact operator spectral bound and is valid
also on every finite torus. One cross propagator in each term of (14)
is summed using a_*; all the other propagators use sigma_*,t. Therefore

```
sum_w |E_F(D_v,D_w;m)|
 <= a_v a_* Sbar [
      9 beta_G^2 M_0^4 /(a v^2)
    +18 C_A M_0^2 sigmabar /((a+c) v^3)
    + 6 C_A d sigmabar^2 /((a+2c) v^4)].                         (16)
```

The same bound holds after multiplying entries by chi_v chi_w. Symmetry
gives the column bound as well. With a_v replaced by A, call the right
side K_F. The Schur test yields, pointwise in retained y and then after
integrating its exact marginal,

```
<sum_v c_v(y) chi_v(y) F_Dv,
 D_vert^(-1) sum_w c_w(y) chi_w(y) F_Dw>
 <= K_F sum_v ||c_v||_(L2(mu_Y))^2,                              (17)
```

where D_vert is the direct integral of the fiber OU generators restricted
to conditionally centered functions. There is no total-volume factor.

## 7. Relation to the actual full Gaussian fast complement

For rho > 0, let h0 be the full ground-transformed oscillator generator in
L2(mu), P the conditional expectation onto the literal observed algebra,
and Q = I-P. Write F0 = Q h0 Q as its self-adjoint form compression on Q.
Its form and the vertical form satisfy on their common domain

```
<f,F0 f> = (1/2) integral |grad f|^2 dmu
         >= (1/2) integral |Q_F grad f|^2 dmu
          = <f,D_vert f>.
```

The vertical form extends to a closed direct-integral form on Q, has gap
c v, and the full form domain is contained in its domain. The variational
formula for inverse positive forms therefore gives

```
0 <= F0^(-1) <= D_vert^(-1)   as quadratic forms on Q.           (18)
```

Combining (17) and (18) gives the same synthesis upper bound for the
actual F0 inverse. This useful domination does not identify its entries
with (15) or transfer the entrywise absolute rooted row estimate (16).
An order inequality between positive operators alone does not preserve
entrywise absolute row sums.

The distinction is already strict in two real dimensions. Take

```
Omega = [[2,1],[1,3]],      observed coordinate y=x1,
r = x2+x1/3,               E[r^2]=1/6.
```

The fiber generator sends r to 3r, whereas the full compressed generator
sends r to (10/3)r. Consequently

```
<r,D_vert^(-1)r> = 1/18,   <r,F0^(-1)r> = 1/20.               (19)
```

The full h0 sends r to (10/3)r+(5/9)x1, so the observation does not reduce
h0. Formula (19) is an exact negative control against replacing F0 by
the fiber generator, including in a claimed two-time Wick identity.

## 8. Consequence and remaining obligation

The fixed-L, volume/regulator-uniform dynamic conditional covariance and
rooted Lie-cubic fiber energy are analytic consequences of the actual
path covariance theorem. Their integrable time envelope is proved using
the spatial symbol, not inferred from a spectral norm bound. The vertical
form comparison also bounds the positive selected full fast exchange in
the synthesis norm under the stated coefficient and mean-cutoff norms.

This does not prove absolute rooted locality of the actual F0 inverse,
identify its exact cubic coefficient, or control the remaining quartic
Wilson, electric metric, Haar, moving-source, baseline cross and fast-form
variation terms. Uniform bounds for the actual ground-corrector spatial
coefficients, interacting remainders and a full scale trajectory remain
separate obligations. No ledger, main manuscript or established-result
registration is changed by this outputs-only subtask.
