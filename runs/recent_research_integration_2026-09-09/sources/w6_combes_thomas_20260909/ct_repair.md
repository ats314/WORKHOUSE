# Combes–Thomas repair in the full fast energy norm

9 September 2026 UTC. Conditional analytic theorem and an application audit.
This note proves the implications stated below. It does not establish their
hypotheses for the coupled Wilson operator, and it does not turn finite
algebra controls into an all-volume estimate.

## 1. The dual identity is exact, with a real positive reference form

Let A be strictly positive self-adjoint on a Hilbert space H, with closed
form a and form domain V. For a continuous conjugate-linear functional
rho on V, the notation below denotes the inverse **form** pairing, whether
or not rho is an H-vector:

\[
 \boxed{\sup_{q\ne0}\frac{|\rho(q)|^2}{a[q]}
       =\langle\rho,A^{-1}\rho\rangle.}                 \tag{CT1}
\]

The equality follows from the Riesz representative in the a-inner product;
the maximizing vector, when rho is nonzero, is its weak inverse image.
Thus replacing the weak target by (CT1) is a useful exact reformulation,
but supplies no new bound on its value.

For A=F-z this positive-inner-product statement requires real z below the
spectrum. If z=s+it is complex, use H_s=F-s>0 as the reference form. The
spectral theorem gives

\[
 |\langle\rho,(F-z)^{-1}\rho\rangle|
 \le\langle\rho,(F-s)^{-1}\rho\rangle.                  \tag{CT2}
\]

The unqualified complex pairing is not a nonnegative squared norm.

## 2. A full-energy preconditioned block theorem

Let X be a countable metric graph and E=direct-sum over B in X of E_B.
The block projections P_B are required to be mutually orthogonal. Let
D_B be positive self-adjoint and D=direct-sum D_B >= d_* I, with d_*>0.
D_B is allowed to retain horizontal energy; it need not be a vertical
conditional operator.

For a particularly transparent sufficient set of domain hypotheses, assume
that the closed fast form is

\[
 a[q,r]=\langle D^{1/2}q,\mathbb B D^{1/2}r\rangle,
 \qquad q,r\in V_D=D(D^{1/2}),                           \tag{CT3}
\]

where B (written as the blackboard-bold operator below) is bounded
self-adjoint on E and

\[
 \mathbb B\ge\kappa I,\qquad \kappa>0.
\]

This specifies the sense in which B=D^{-1/2} A D^{-1/2}; an informal product
of unbounded operators is not needed. Norm equivalence makes (CT3) closed,
and its associated A has

\[
 A^{-1}=D^{-1/2}\mathbb B^{-1}D^{-1/2}.                 \tag{CT4}
\]

Write B_BC=P_B B P_C. Suppose, for B != C,

\[
 \mathbb B_{BC}=0\quad\hbox{if }d(B,C)>R,
 \qquad
 \sup_B\sum_{C\ne B}\|\mathbb B_{BC}\|\le J,
 \qquad
 \sup_C\sum_{B\ne C}\|\mathbb B_{BC}\|\le J.            \tag{CT5}
\]

Take R>0 and choose mu>0 such that

\[
 J(e^{\mu R}-1)\le\kappa/2.
\]

Then

\[
 \boxed{\|P_B\mathbb B^{-1}P_C\|
       \le\frac2\kappa e^{-\mu d(B,C)}.}              \tag{CT6}
\]

One explicit choice, for J>0, is

\[
 \mu=R^{-1}\log\left(1+\frac\kappa{2J}\right).         \tag{CT7}
\]

For J=0 the inverse is block diagonal and no decay restriction is needed.
All constants are volume-independent if the hypotheses are uniform.

### Proof including infinite-volume weights

Fix C and L>0. Put w_B=exp(mu min(d(B,C),L)) and W_L=direct-sum w_B I_B.
Both W_L and its inverse are bounded, and on every nonzero off-diagonal
block one has

\[
 |w_B/w_{B'}-1|\le e^{\mu R}-1.
\]

The Schur bound for operator-valued matrices therefore yields

\[
 W_L\mathbb B W_L^{-1}=\mathbb B+E_L,
 \qquad\|E_L\|\le J(e^{\mu R}-1)\le\kappa/2.
\]

Neumann inversion around B, whose inverse has norm <=1/kappa, proves
||(B+E_L)^{-1}||<=2/kappa. Taking the B,C block of the conjugated inverse
gives (CT6) with d(B,C) replaced by min(d(B,C),L). Letting L grow proves
(CT6), without conjugating by an unbounded exponential weight.

The kernel in original energy units is

\[
 \boxed{
 \overline{D_B^{1/2}P_B A^{-1}P_C D_C^{1/2}}
       =P_B\mathbb B^{-1}P_C.}                         \tag{CT8}
\]

The overline denotes the bounded extension from the natural dense block
domains. Formula (CT4) proves the equality there and hence its extension.
The energy weights in (CT8) are essential: replacing it by a scalar
unweighted resolvent estimate and then bounding ||rho_B|| can discard the
horizontal denominator a second time.

The CT proof also permits an unbounded self-adjoint block-diagonal part
plus a bounded off-diagonal operator satisfying (CT5). Bounded truncated
weights preserve the diagonal operator domain and the same commutator
argument applies. In that version the representation of A must separately
be made as a closed form, or equivalently through its positive inverse;
the bounded-B domain hypothesis in (CT3) is a convenient sufficient case.

## 3. In a true orthogonal direct sum, localization is unnecessary for this bound

For rho in V_D^*, define f=D^{-1/2}rho by
rho(q)=<D^{1/2}q,f>, using an inner product conjugate-linear in its first
argument. It is an E-vector precisely when rho is continuous in
the D-form norm. Write f_B=P_Bf, equivalently f_B=D_B^{-1/2}rho_B. Equations
(CT3)-(CT4) give the exact identity

\[
 \langle\rho,A^{-1}\rho\rangle
       =\langle f,\mathbb B^{-1}f\rangle
       \le\kappa^{-1}\sum_B\|f_B\|^2.                \tag{CT9}
\]

Consequently, if the complete source satisfies

\[
 \sum_B\|D_B^{-1/2}\rho_B(p)\|^2
       \le C_0^2 g^2 b[p],                             \tag{CT10}
\]

then its desired dual energy is <=C_0^2 g^2 b[p]/kappa. Neither CT nor a
lattice Green sum is needed. The weak-bound constant is C_0/sqrt(kappa).
This statement permits form-dual residuals that have no bounded L2 norm.

Using (CT6) instead proves the weaker bound

\[
 \langle\rho,A^{-1}\rho\rangle
 \le\frac{2M_X(\mu)}\kappa\sum_B\|f_B\|^2,
 \quad M_X(\mu)=\sup_B\sum_C e^{-\mu d(B,C)},           \tag{CT11}
\]

when the geometric sum is finite. That localization bound has uses beyond
the total quadratic norm, but it cannot improve (CT9). For Z^d with the
l1 metric,

\[
 M_{\mathbb Z^d}(\mu)
 =\left(\frac{1+e^{-\mu}}{1-e^{-\mu}}\right)^d.
\]

The dimension and metric must be those of the proved block decomposition.
Finite periodic boxes obey the same upper bound by selecting shortest
integer displacement representatives. An arbitrary metric graph needs its
own uniform growth/summability hypothesis.

## 4. Local sources in a many-body space require a synthesis theorem

A local source support in a tensor-product configuration Hilbert space does
not produce mutually orthogonal spatial projections. One state can have
excitations in several blocks; local functions for an interacting measure
can have nonzero long-range inner products. Thus a lattice differential
operator cannot simply be replaced by the direct sum in (CT3).

Here is an exact replacement. Let V be the A-form domain in the actual
Hilbert space H. For each B, let J_B:E_B -> V^* be a bounded local source
map in the form-dual norm, and set

\[
 K_B=A^{-1/2}J_B:E_B\longrightarrow H.
\]

This notation means the Riesz extension on the dual domain. For finite
families f=(f_B), let rho=sum_B J_B f_B. Then

\[
 \langle\rho,A^{-1}\rho\rangle
 =\left\|\sum_B K_B f_B\right\|^2
 =\sum_{B,C}\langle f_B,K_B^*K_C f_C\rangle.           \tag{CT12}
\]

If one proves the **source-kernel** estimate

\[
 \|K_B^*K_C\|
 =\|J_B^*A^{-1}J_C\|
 \le C_{\rm ker}e^{-\mu d(B,C)},                       \tag{CT13}
\]

then the operator-valued Schur test proves

\[
 \langle\rho,A^{-1}\rho\rangle
 \le C_{\rm ker}M_X(\mu)\sum_B\|f_B\|^2.             \tag{CT14}
\]

Finite sums extend to l2 families by continuity. This is the appropriate
many-body version of the proposed kernel summation. Establishing (CT13)
requires compatibility of J_B with a proved localization structure of the
actual A. An abstract spectral floor and the bare-coordinate support of
J_B do not establish it.

There is again a simpler sufficient alternative. Suppose A>=kappa D_full
as forms on the same H, and J_B=D_full^{1/2} V_B in the form-dual sense.
If the synthesis map

\[
 V:f\longmapsto\sum_B V_Bf_B,
 \qquad \|Vf\|^2\le S^2\sum_B\|f_B\|^2               \tag{CT15}
\]

is bounded, then inverse order gives

\[
 \langle\rho,A^{-1}\rho\rangle
 \le\frac{S^2}\kappa\sum_B\|f_B\|^2.                \tag{CT16}
\]

One way to prove (CT15) is a uniform Schur bound on the Gram blocks
V_B^* V_C. Orthogonality yields S=1; verified finite overlap or summable
correlations can yield other uniform S. Neither is automatic in a true
interacting conditional measure.

The need for synthesis control is elementary: take H=C, A=I and J_B=I
for N labels. Every individual source map has norm one, but f_B=1 gives
inverse energy N^2 while sum_B ||f_B||^2=N. Uniform individual block bounds
therefore do not establish a uniform sum bound when the maps overlap.

## 5. The previous exact model already rejects the proposed unweighted C_0

In the exact torus model from the continuation report,

\[
 \rho_n=\frac{g n^4}{2(n^2+1)}\cos(2k)e^{iny},
 \qquad b[p_n]=n^2.
\]

Normalized Haar measure gives

\[
 \frac{\|\rho_n\|^2}{g^2 b[p_n]}
 =\frac{n^6}{8(n^2+1)^2}\longrightarrow\infty.         \tag{CT17}
\]

Thus even replacing the failed derivative norm by an unweighted local L2
residual norm is too strong in this model. The full-energy block choice
D_n=n^2-partial_k^2 on fast mean-zero functions retains the missing factor:

\[
 \frac{\|D_n^{-1/2}\rho_n\|^2}{g^2 b[p_n]}
 =\frac{n^6}{8(n^2+1)^2(n^2+4)}\le\frac18.            \tag{CT18}
\]

The last inequality is exactly
(n^2+1)^2(n^2+4)-n^6=6n^4+9n^2+4>0. This is a genuine all-mode analytic
bound, not a maximum over finitely many sampled values. It is a control
example rather than a Wilson theorem.

## 6. What a coupled Wilson application must still establish

The repair separates three unproved application inputs:

1. A closed-form representation and uniform coercive comparison for the
   complete, ground-shifted, transported physical fast A_{g,Lambda}; a
   bouquet spectral lower bound does not identify its local curvature.
2. Either an actual orthogonal localization structure with full-energy
   preconditioner and uniform off-diagonal controls, or a source-synthesis
   theorem such as (CT13) or (CT15) in the actual many-body Hilbert space.
3. An all-retained-energy bound for the complete transported residual in
   the corresponding weighted local norms, such as (CT10), including its
   electric, Haar, vacuum, marginal, source and projection contributions.

Once these are proved, (CT9), (CT14), or (CT16) gives the needed residual
energy. With a diagonal defect bound |d[u_0,u_0]|<=a_0|g|b[p] and |g|<=g_0,
the residual identity then yields W6 with constant a_0+C_dual g_0, where
C_dual is the coefficient of g^2b[p] in the proved dual-energy estimate.
The weak residual-bound constant is sqrt(C_dual). The present theorem does
not assert any of the three Wilson inputs on the strength of finite tests.
