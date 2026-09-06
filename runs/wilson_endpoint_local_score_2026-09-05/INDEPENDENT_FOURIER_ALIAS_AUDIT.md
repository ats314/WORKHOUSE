# Independent averaged-path Fourier and transverse-tail audit

5 September 2026. Outputs-only bounded audit of the proposed local
gauge-covariant averaged-path cochain map. This audits its linearized
cochain/Fourier mechanism; construction of the nonlinear matrix-valued map
and its covariance is supplied separately by the author.

Let the fine periodic side be n=Lm. Use unitary Fourier transforms on the
fine and coarse vertex sets and one forward-oriented link in each of the
three directions. For a coarse momentum K in [-pi,pi)^3, its aliases are
k=(K+2pi r)/L modulo 2pi. Define

```text
d_i(k)=exp(i k_i)-1,       D_i(K)=exp(i K_i)-1,
a_i(k)=L^-1 sum_(s=0)^(L-1) exp(i k_i s),
a(k)=product_i a_i(k),
R_i(k)=L^-1/2 a(k) a_i(k).
```

The normalization L^-1/2 is the path length L times the unitary Fourier
alias factor L^-3/2. The fundamental identity is exact, including phases:

```text
a_i(k) d_i(k)=D_i(K)/L.
```

Consequently d(k)* R(k)*b=L^-3/2 conjugate(a(k)) D(K)*b.
Thus R* takes coarse transverse cochains into fine transverse cochains,
without a subsequent nonlocal Coulomb projection. At the principal alias
k0=K/L, every a_i(k0) is nonzero and has modulus at least 2/pi. Its
diagonal R* map is therefore a bijection between the two transverse
momentum fibers. At K=0 both fibers have dimension three and the same
statement holds; the three constant link modes are retained exactly.

## Exact alias norm and the tail bound

Write b_j=|a_j(k0)|^2. Given a fine principal transverse vector A0, choose
the unique coarse transverse vector whose lift has principal component A0.
For each component i, the squared norm of the remaining aliases divided
by |A0_i|^2 is

```text
T_i = [sum_(r_i) |a_i(k_ri)|^4] /
      [b_i^2 product_(j!=i) b_j] - 1.                 (1)
```

Indeed the alias sums separate by coordinate and
sum_(r_j)|a_j(k_rj)|^2=1. This explains both the fourth power in the i
coordinate and every principal normalization factor; they cannot be
removed from (1). The exact optional fourth-moment identity is

```text
sum_r |a((K+2pi r)/L)|^4
  = (2+cos K)/3 + (1-cos K)/(3L^2).                   (2)
```

For the advertised bound only this sum being at most one is needed.
An elementary characteristic-function estimate gives

```text
1-b_j = L^-2 sum_(s,t) [1-cos(K_j(s-t)/L)]
      <= (L^2-1)K_j^2/(12L^2) <= K_j^2/12.
```

Using 1-product x_j <= sum(1-x_j), all x_j in [0,1], gives

```text
1-b_i^2 product_(j!=i)b_j
 <= 2(1-b_i)+sum_(j!=i)(1-b_j) <= |K|^2/6.
```

Since b_i^2 product_(j!=i)b_j >= (2/pi)^8, equation (1) yields

```text
||tail(A0)||^2 <= C |K|^2 ||A0||^2,
C=(pi/2)^8/6.                                       (3)
```

This proof covers Nyquist ties by selecting either one of the tied
principal aliases. At K=0 all nonprincipal lifted aliases vanish. For
L=1 the retained map is the identity and there is no complementary space.

## Conversion to the full transverse fast form

Let C_f=ker d0* and S=ran(R*|C_coarse). On C_f the exact cubic Hodge
identity identifies curl energy with multiplication by
lambda(k)=sum_i 4sin^2(k_i/2). In every alias fiber,

```text
lambda(k0) >= 4|K|^2/(pi^2 L^2),
lambda(k_nonprincipal) >= 4/L^2.                    (4)
```

The latter follows because one representative coordinate has magnitude
at least pi/L, and sin(pi/(2L)) >= 1/L for L>=1. Split any transverse
A into its principal and remaining aliases. The lift selected above
belongs to S and agrees with its principal part. Therefore

```text
dist(A,S)^2 <= 2||A_high||^2+2C |K|^2||A0||^2
            <= (pi^10 L^2/3072) <A,K_C A>.             (5)
```

The last step compares the two separate energy coefficients in (4);
C pi^2>1 makes the principal one the larger. Summing (5) over momenta
proves the full form statement

```text
K_C >= 3072/(pi^10 L^2) (I-P_S) on C_f.               (6)
```

All constants are independent of the number of coarse blocks. S is now
the electric-dual range of the actual local commuting cochain map, rather
than the Coulomb projection of arbitrary componentwise box averages.
Equation (6) is a squared-frequency/Hessian statement. The torus harmonic
modes remain retained; it neither creates a positive vacuum frequency in
them nor identifies an unregulated nonlinear Wilson or OS projection.

## Independent finite control boundary

`check_fourier_alias_independent.py` checks the cochain polynomial identity
and exact second/fourth alias moment coefficients for L=1,...,12 by direct
integer counting, independently of a floating Fourier grid. A separate
n=4,L=2 complex-rational transverse fiber checks the adjoint phases,
principal matching and the nonprincipal/principal squared-norm ratio 3.
Removing the directional a_i factor fails transversality on a selected
alias. The analytic inequalities and all-size conclusion (6) are proved
above; these finite controls check their normalization and do not replace
the proof or the nonlinear path-map construction.

## Local physical tangent-algebra review

The author's Section 6 local interpretation was also checked. A matrix
average need not be unitary; its global definition is not replaced by a
polar map. Near the identity the local unitary polar factor with determinant
root chosen near one is smoothly endpoint-equivariant and has the same
traceless anti-Hermitian derivative. Coarse tree gauge fixing leaves one
based holonomy per non-tree edge and one common residual conjugation.
The linear map from the Coulomb complement to these cycle coordinates is
invertible: its kernel is precisely an infinitesimal tree gauge gradient.
Invariant tangent polynomials therefore pull back from smooth invariant
functions of the local logarithmic cycle coordinates. A cutoff on the
quotient neighborhood, extended to its compact gauge-orbit saturation,
can be chosen invariant. The common Ad-invariant tangent algebra is thus
the stated full Gaussian physical algebra, rather than only separate
quadratic characters. This proves a local/tangent interpretation and does
not prove nonlinear true-ground source density or an OS-history identity.

The initially emitted `fourier_alias_independent_controls.json` records the
earlier audit bytes. The final report is
`fourier_alias_independent_controls_frozen.json`, generated after the
matrix-valued terminology correction and this bounded tangent review;
the original control source and mathematical calculation are unchanged.
