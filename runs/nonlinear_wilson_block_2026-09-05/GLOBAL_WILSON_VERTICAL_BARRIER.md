# Global nonlinear Wilson vertical bound through coarse energy barriers

5 September 2026. New research candidate following the sealed scale-comparison
package. This file is not part of that sealed package. The question is whether
the actual single-block physical vertical fast estimate can hold on the entire
coarse group, rather than just the small neighborhood used in the previous
vertical-rotor theorem.

## 1. Actual operators and established input

Fix SU(N), N>=2, with the existing metric -2 ReTr(XY), and u>0. Write
v(U)=N-ReTr U. For the two-square bouquet and adjacent-square strip, keep
the exact original-link metric of
paper/research_notes/G19_WILSON_PHYSICAL_FIBER_FAST_GAP_20260905.md.
With coarse holonomy U=U1 U2 and fiber K=U1, their intrinsic vertical
Hamiltonians on Haar L2(SU(N)) are

```
A_U = T_U + 2u[v(K)+v(K^-1 U)].                            (1)
T_U^bouquet = -Delta,
T_U^strip = -(1/2) sum_ab S(U)^ab L_a L_b,
S(U) = 15[8I-Ad(U)-Ad(U)*]^-1.
```

These have compact resolvent and unique positive ground states. Let
E_j(U), j=0,1,..., be their full fiber eigenvalues counting multiplicity,
and P_U their rank-one ground projections. No stabilizer-invariant
excited-space restriction is imposed in this notation.
At U=I, these are the established central rotors

```
A_I^bouquet = -Delta+4u v(K),
A_I^strip = -(5/4)Delta+4u v(K).
```

Write e0=E_0(I), e1=E_1(I), delta=e1-e0>0. The established compact-rotor
theorem proves, at fixed N and u tending to infinity,

```
delta_bouquet = 2 sqrt(u)+O_N(u^(1/4)),
delta_strip = sqrt(5) sqrt(u)+O_N(u^(1/4)),
e1 = O_N(sqrt(u)).                                       (2)
```

These full fiber gaps are the ones used below. The class-function factor
two at U=I cannot be assigned to a generic noncentral stabilizer.

## 2. Statement

For every u>0, every U in SU(N), and every eigenvalue index j,

```
E_j(U) >= min(E_j(I), u/N^2).                             (3a)
```

Thus below the explicit energy u/N^2, no coarse holonomy introduces
more fiber spectral levels than the central rotor. This is a statement
about the entire counted spectrum, not only two selected modes. It has
no large-u hypothesis. The fast-gap consequence below uses that the
central first excitation has entered this energy window.

For either block, suppose

```
u >= N^2 e1.                                             (3)
```

This is a sufficient spectral threshold, not an equation defining u.
Equation (2) implies (3) for all sufficiently large u at every fixed N.
Then every U in SU(N), including the central and cut-locus coarse values,
satisfies

```
E_0(U) >= e0,       E_1(U) >= e1,
A_U-e0 >= delta (I-P_U).                                 (4)
```

The ground offset E_0(U)-e0 is retained. Subtracting E_0(U) instead is
a different claim: the conditional gap can be only order one at U=-I
in SU(2). Thus (4) is the global vertical fast-energy inequality needed
for a subsequent physical form comparison, with the coarse energy cost
explicit. It is not yet a full vacuum-subtracted multiblock inequality.

## 3. Global barrier, with no choice of square root

For unitaries A,B,

```
||I-AB||_F <= ||I-A||_F+||I-B||_F,
v(AB) <= 2[v(A)+v(B)].                                   (5)
```

The second follows from v(A)=||I-A||_F^2/2 and (x+y)^2<=2(x^2+y^2).
Consequently the exact potential and nonnegative electric form give

```
A_U >= u v(U) I.                                        (6)
```

Whenever v(U)>N^-2, (3) implies A_U>e1. This entire region, not only
the singular central values, is therefore already above both desired
fiber levels. No pointwise conditional gap is required there.

## 4. An exact comparison on the remaining neighborhood

Suppose v(U)<=N^-2. Let theta_i in [-pi,pi] be its principal eigenangles.
For each i,

```
|theta_i| <= (pi/2)|1-exp(i theta_i)|
          <= pi/(sqrt(2) N).
```

Thus |sum theta_i|<=pi/sqrt(2)<2pi. Since det U=1, that sum is an
integer multiple of 2pi and must be zero. The principal square root
H=U^(1/2) consequently belongs to SU(N); its determinant has not been
silently replaced by that of a U(N) matrix. Put

```
A=Re H,       eta=Tr(I-A),       K=H F.
```

All eigenvalues c_i=cos(theta_i/2) are nonnegative, and

```
v(U)=2 sum_i(1-c_i^2),
2 eta <= v(U) <= 4 eta,
0<=eta<=1/(2N^2),       A >= (1-eta)I.                   (7)
```

Haar measure is preserved by the left translation. The exact two-face
potential, including its scalar minimum, becomes

```
2u[v(HF)+v(F^-1 H)]
 =4u eta+4u Tr[A(I-Re F)]
 >=4u eta+(1-eta)4u v(F).                               (8)
```

Here I-Re F is positive semidefinite. Tr[(A-(1-eta)I)(I-Re F)]>=0
does not require the two matrices to commute.

For the bouquet translation preserves T_U=T_I. Positivity then gives

```
A_U >= (1-eta) A_I+4u eta I.                             (9)
```

For the strip write R=Ad(U), D=(I-R)(I-R*)>=0. The exact vertical metric
relative to its central value is

```
S(U)/(5/2) = 6(6I+D)^-1.
```

The adjoint action uses the fixed Lie-algebra metric. For every X,
||UXU^-1-X||_F<=2||U-I||_op||X||_F, and hence

```
||D|| = ||I-Ad(U)||^2
 <=4||I-U||_op^2 <=8 v(U) <=32 eta.
```

Spectral calculus gives 6/(6+d)>=1-d/6 for d>=0, so

```
S(U)/(5/2) >= [1-(16/3)eta] I.                           (10)
```

The translation K=HF rotates the left-invariant derivatives by Ad(H).
Since Ad(H) commutes with every polynomial and resolvent of Ad(U),
it leaves S(U) unchanged. Thus (10) is an inequality of the actual
translated electric forms. Set alpha=16/3. By (7),
1-alpha eta>=1-8/(3N^2)>=1/3 for N>=2. Combining (8) and (10) yields

```
A_U >= (1-alpha eta) A_I+4u eta I.                       (11)
```

For the bouquet the same formula holds with alpha=1.

## 5. Min-max, the whole fast complement and a retained barrier

First prove (3a) for every j. Within the neighborhood, (9) or (11)
gives a convex combination of E_j(I) and 4u/alpha, with weights
1-alpha eta and alpha eta. Since 4/alpha>=3/4>=1/N^2,
this is at least min(E_j(I),u/N^2). Outside the neighborhood (6)
is at least u/N^2 on the entire fiber. The min-max principle proves
(3a) without a truncation or a spectral gap hypothesis.

For j=0,1, (9) or (11) implies

```
E_j(U) >= E_j(I)+eta[4u-alpha E_j(I)].                    (12)
```

Condition (3), N>=2 and alpha<=16/3 imply 4u>=alpha e1,
so both levels in (12) are bounded below by their central values.
Together with (6) outside the neighborhood this proves the first two
claims of (4). The full fiber spectral theorem then proves its form claim.

A useful explicit scalar barrier is

```
b(U) = eta[4u-alpha e1],        if v(U)<=N^-2,
       u v(U)-e1,              if v(U)>N^-2.
```

It is nonnegative under (3) and gives the stronger statement

```
A_U-e0 >= delta(I-P_U)+b(U)I.                            (13)
```

Indeed the low-neighborhood lower bound for the ground is at least
e0+b(U), and every remaining eigenvalue is at least e1+b(U).
Outside, (6) dominates e0+delta(I-P_U)+b(U), since delta(I-P_U)<=delta I.

The analytic dependence of the uniformly elliptic operator family on U
gives measurable ground projections, regardless of the chosen proof chart.
For any positive finite coarse measure nu, integration yields on the
direct-integral form domain

```
integral <psi(U),(A_U-e0)psi(U)> dnu(U)
 >= delta integral ||(I-P_U)psi(U)||^2 dnu(U)
    + integral b(U)||psi(U)||^2 dnu(U).                  (14)
```

Gauge covariance makes the direct-integral projection compatible with
the residual gauge-invariant subspace. Restricting (14) to that subspace
preserves the inequality; it does not multiply delta by two.

## 6. Where this enters the full problem

Completing the exact link cometric into a horizontal square plus its
vertical Schur square writes the full two-face form as the nonnegative
horizontal form plus the direct integral in (1). Thus (14) also supplies
a full-block lower comparison before subtracting the full-block vacuum.
However e0 is the central FIBER ground, not the full-block ground E_vac.
In the harmonic strip, the missing slow oscillator zero-point energy is
already order sqrt(u). One cannot subtract E_vac from (14) and discard
E_vac-e0. Nor can one sum a fixed error over infinitely many blocks.

The result removes the small-coarse-field restriction from the actual
nonlinear single-block vertical form at every fixed rank. The next task
is to combine the retained barrier, horizontal motion and varying fiber
ground with a vacuum-adapted coarse operator, while bounding the full
vacuum-subtracted fast compression uniformly in volume. That is the
specific premise still needed by the closed-form Schur scale theorem.

Independent review and exact finite controls are companion output files.
The general theorem is the form and min-max argument above, not a rank
sweep, a numerical extrapolation, or a Lean certification.
