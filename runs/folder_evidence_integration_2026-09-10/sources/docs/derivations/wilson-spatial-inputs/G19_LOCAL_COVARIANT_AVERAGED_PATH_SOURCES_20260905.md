# Local gauge-covariant path averages with a uniform transverse tangent bound

5 September 2026. Analytic research continuation. This constructs an
actual local gauge-covariant matrix-valued Wilson block and proves a full
harmonic form bound for its physical transverse tangent source space. It
removes the need to apply the fine-lattice global Coulomb projector to a
box source before giving that source a nonlinear local meaning.

The map is globally defined; the fast estimate is a theorem about its
linearization and the actual curl Hessian. No nonlinear quantum fast bound,
true-vacuum source comparison, reflection/history identification or
continuum conclusion is inferred from the tangent theorem.

## 1. Current inputs and conventions

The current graph entries RESULT:WILSON_THREE_DIMENSIONAL_HARMONIC_BOUNDARY
and RESULT:GAUSSIAN_QUANTUM_FAST_SOURCES were queried before this derivation.
The former already proves a strong full harmonic inequality for the
nonlocal fine-Coulomb-projected box space. The latter already supplies the
whole Gaussian quantum consequence of a full matrix inequality. Their
explicit unresolved source-locality qualification is the target here.

Let n>=3, let L>=2 divide n, and write m=n/L. Fine sites are x in (Z/nZ)^3;
coarse sites are v=L y with y in (Z/mZ)^3. A positive edge is labeled by
its basepoint and coordinate direction. Reversal means the negative of
that oriented cell, not identification with another positive edge label.
The coarse graph uses the same labeled-cell convention even for m=1 or
m=2: loop edges and parallel/oppositely directed labeled edges remain
distinct coarse cells. This avoids a hidden small-period convention.

Fine and coarse cochains have the ordinary counting-measure inner products.
Define forward coboundaries

```text
(d0 f)_i(x)=f(x+e_i)-f(x),
(d0c h)_i(v)=h(v+L e_i)-h(v),
(d1 A)_ij=delta_i A_j-delta_j A_i,       i<j.
```

Let C=ker d0^*, C_c=ker d0c^*. The established original-link Hodge identity
gives on C

```text
K_C=d1^*d1,     <A,K_C A>=sum_(i,j)||delta_i A_j||^2.    (1)
```

This retains every interface and respects d1 d0=0 and d2 d1=0. All results
tensor with the Lie algebra of a faithfully embedded compact matrix group
G subset U(D), with a fixed Ad-invariant metric. The spatial constants
below do not depend on the color dimension.

## 2. The actual local matrix block

For x in B_v=v+{0,...,L-1}^3 choose an anchor path alpha_v(x) from v to x
inside that cube. For example, travel in coordinate order 1,2,3. Choose
the anchors by translation, with the empty path at x=v. Let p_i(x) be the
length-L positive i-direction path from x to x+L e_i. Define

```text
M_i(v)=L^(-3) sum_(x in B_v)
 U(alpha_v(x)) U(p_i(x)) U(alpha_(v+L e_i)(x+L e_i))^(-1).
                                                               (2)
```

The inverse is the holonomy of the reversed anchor path. Each summand is
a matrix in G, but M_i(v) is retained as its complex matrix average. It
need not be unitary or invertible; the construction uses neither a global
polar decomposition nor a determinant root.

Under the exact fine gauge action U_e -> g(tail e) U_e g(head e)^(-1),
all internal endpoint factors cancel in each summand. Thus

```text
M_i(v) -> g(v) M_i(v) g(v+L e_i)^(-1).                 (3)
```

No gauge-fixing hypothesis is needed. Each path in (2) has length at most
L+6(L-1)=7L-6. Its edge basepoints lie in B_v union B_(v+L e_i). Thus each
matrix block is a function of fine links in two adjacent cubes, including
their actual crossing links. The definition is translation covariant by
coarse lattice translations. It may single out a coordinate ordering in
its anchors; no rotational or reflection covariance is asserted from that
choice without a separate symmetrization or proof.

## 3. Exact tangent cochain identities and physical cotangents

Linearize U_e(t)=exp(t A_e) at the identity. Let

```text
(R_i A)(v)=L^(-3) sum_(x in B_v) sum_(t=0)^(L-1) A_i(x+t e_i),
(Phi A)(v)=L^(-3) sum_(x in B_v) sum_(e in alpha_v(x)) A_e,
(B f)(v)=L^(-3) sum_(x in B_v) f(x),
(E f)(v)=f(v).
```

Anchor sums are oriented. Differentiating the finite products in (2) gives

```text
T:=D M|_I=R-d0c Phi.                                  (4)
```

The path sum telescopes on a gradient. The long paths give
R d0=d0c B, while the anchors give Phi d0=B-E. Consequently

```text
R d0=d0c B,       T d0=d0c E.                          (5)
```

The actual gauge-covariant derivative T therefore commutes with restriction
of the gauge parameter to coarse vertices. The auxiliary R commutes with
the box average of that parameter. These are different zero-cochain maps;
replacing one by the other would misstate the nonlinear gauge covariance.

For b in the coarse transverse cotangent space C_c, (4)-(5) imply

```text
T^* b=R^* b,
d0^* R^* b=B^* d0c^* b=0.
S:=ran(R^*|_(C_c))=ran(T^*|_(C_c)) subset C.            (6)
```

Thus anchor choices disappear exactly from the physical transverse tangent
source space. No fine Coulomb projection is required in (6). The orthogonal
projector P_S itself need not be local, and implementing a coarse gauge
quotient can still involve nonlocal coordinates. The local assertion is
about the actual map (2), not about locality of every orthogonal projection.

The principal Fourier calculation below also proves that R^* is injective
on C_c. Hence dim S=2m^3+1 per color, including all three torus harmonic
cochain directions. At m=1 this formula gives precisely the three coarse
winding-loop directions.

## 4. Fourier aliases and an exact low-mode matching map

Use unitary discrete Fourier transforms in the fine and coarse counting
norms. For a coarse momentum K with components in [-pi,pi], its fine aliases
are k=(K+2pi r)/L modulo 2pi. Choose one representative in [-pi,pi] for each
fine component. The principal alias is k0=K/L; on a boundary choose either
consistent representative. Define

```text
d_i(k)=exp(i k_i)-1,        D_i(K)=exp(i K_i)-1,
a_i(k_i)=L^(-1) sum_(s=0)^(L-1) exp(i k_i s),
a(k)=product_j a_j(k_j).
```

Direct summation of R gives its alias row in component i,

```text
r_i(k)=L^(-1/2) a(k) a_i(k_i),
(R A)_i_hat(K)=sum_(k alias K) r_i(k) A_i_hat(k).       (7)
```

The common factor is L times the scalar box symbol, multiplied by the
unitary-Fourier normalization L^(-3/2). The exact identity

```text
a_i(k_i) d_i(k)=D_i(K)/L                               (8)
```

proves phase-sensitive transversality: if sum_i conjugate(D_i)b_i=0,
then at every alias
sum_i conjugate(d_i) conjugate(r_i)b_i=0. This is the Fourier version of
(6); discarding the phases of a_i would not prove it.

At the principal alias,

```text
|a_i(k0_i)|>=2/pi.                                    (9)
```

Indeed |a_i|=|sin(K_i/2)|/[L|sin(K_i/(2L))|], interpreted as one at K_i=0.
Use sin t>=2t/pi on [0,pi/2] in the numerator and sin t<=t in the
denominator. Each component is nonzero. Given any principal transverse
vector A0, choose

```text
b_i=A0_i / conjugate(r_i(k0)).                         (10)
```

Then (8) and the fine transverse condition show b is coarse transverse.
The source R^*b matches A0 exactly at the principal alias. This proves the
claimed bijection between coarse transverse vectors and principal fine
transverse vectors, including the three-dimensional zero-momentum space.

## 5. High-alias leakage and the full form inequality

Write b_j(r_j)=|a_j((K_j+2pi r_j)/L)|^2 and b_j0=b_j(0), labeling the
principal alias as zero. Finite Fourier orthogonality gives

```text
sum_(r_j) b_j(r_j)=1.                                 (11)
```

For independent uniform s,t in {0,...,L-1},

```text
1-b_j0=E[1-cos(K_j(s-t)/L)]
       <=K_j^2(L^2-1)/(12L^2)<=K_j^2/12.               (12)
```

This is the exact variance estimate E(s-t)^2=(L^2-1)/6 combined with
1-cos z<=z^2/2; it is not an asymptotic small-K expansion.

For the matched source in (10), the sum of squared high-alias amplitudes
in component i divided by |A0_i|^2 is exactly

```text
T_i=[sum_(r_i) b_i(r_i)^2] /
             [b_i0^2 product_(j!=i) b_j0] -1.           (13)
```

All other alias sums factor to one by (11). The numerator before division,
after subtracting the principal contribution, is nonnegative and at most

```text
1-b_i0^2 product_(j!=i)b_j0
 <=2(1-b_i0)+sum_(j!=i)(1-b_j0)<=|K|^2/6.             (14)
```

Here sum b_i^2<=1 follows from (11). By (9) the denominator in (13) is at
least (2/pi)^8. Consequently the matched source has high-alias tail

```text
||source_high||^2 <= (pi/2)^8 |K|^2/6 ||A0||^2.        (15)
```

Let q(k)=4 sum_j sin^2(k_j/2). Since |K|=L|k0| and q(k0)>=4|k0|^2/pi^2,

```text
||source_high||^2
 <=pi^10 L^2/6144 . q(k0)||A0||^2.                    (16)
```

Every nonprincipal alias has at least one |k_j|>=pi/L. Thus
q(k)>=4 sin^2(pi/(2L))>=4/L^2 on those aliases, including boundary ties.
For a general fine transverse A, split it into principal and high aliases
and use (10) independently in every coarse Fourier block to construct s in S
which matches its principal part. Equations (1),(16) and the high frequency
bound give

```text
||A_high||^2 <=L^2/4 . energy_high,
||s_high||^2 <=pi^10 L^2/6144 . energy_low,
dist(A,S)^2 <=||A_high-s_high||^2
 <=2||A_high||^2+2||s_high||^2
 <=pi^10 L^2/3072 . <A,K_C A>.                         (17)
```

The last step uses pi^10/3072>=1/2. The proof works on the complexified
cochain space. Restriction to real fields gives the same inequality since
R and the real orthogonal projection are real operators; no real principal
alias selection at a Nyquist boundary is required.

We have proved the full quadratic-form theorem

```text
K_C >= [3072/(pi^10 L^2)] (I_C-P_S)
    >= [1/(33L^2)] (I_C-P_S).                          (18)
```

For the second inequality use pi<22/7 and the exact integer inequality
22^10<33*3072*7^10. This is uniform in m and L. It is a full form bound,
not merely a compression bound: all couplings between S and its complement
remain in K_C. Its constant is weaker than that of the old fine-Coulomb box
space, in exchange for the local gauge-covariant realization of the source.

At K=0 the nonprincipal box symbols vanish, so R^* maps constant coarse
links to constant fine links and generates all three harmonic directions.
Their zero energy is consistent with (18). No inverse of K_C on those
directions has been used.

## 6. Physical tangent algebra and the Gaussian consequence

The local map (2) produces a coarse endpoint-covariant matrix connection.
Gauge-invariant functions, such as traces of closed products of M and M^*,
are genuine fine-lattice gauge-invariant observables. The linearization at
the identity belongs to the represented Lie algebra, and the infinitesimal
gauge quotient removes d0c directions. On transverse cotangents it is exactly (6).
The remaining stabilizer of the identity connection is the single global
G action, which acts on S by simultaneous adjoint color rotations.

This identifies the physical tangent source algebra as invariant functions
of the coarse transverse quotient, pulled back through T or R as in (6).
For a precise finite-dimensional local interpretation of its polynomials,
use only a sufficiently small Frobenius tubular neighborhood of the
embedded compact matrix group. There is a unique nearest-point retraction
r onto that group in such a neighborhood, and r is smooth. To see the
local fact needed here, the normal-coordinate map (g,n) -> g+n has
invertible derivative along its zero section; its local inverses patch,
and compactness gives a uniform smaller normal neighborhood with unique
nearest point. Left and right G multiplications are ambient Frobenius
isometries preserving G. Uniqueness therefore gives

```text
r(g1 M g2^(-1))=g1 r(M) g2^(-1),
D r|_I X=X for X in the represented Lie algebra.       (18a)
```

Thus r(M) is a local smooth equivariant G connection with the same tangent
as M. Fixing a coarse spanning tree expresses its remaining based
holonomies as local quotient coordinates with a common residual
conjugation. Their logarithms have an invertible linear chart on C_c:
the graph cycle space and the transverse complement both represent the
same quotient by vertex gradients. Any invariant polynomial of that
tangent chart can therefore be realized as the leading term of a smooth
gauge-invariant function in this neighborhood. A cutoff on the quotient,
or its gauge-saturated neighborhood, extends it if needed. This identifies
all tangent invariant polynomials, not only quadratic contractions.

This local retraction is used only to identify the tangent algebra. It
does not alter the global matrix block (2), require any global retraction
or polar construction, or claim locality of a spanning-tree gauge choice.

The Gaussian result can now be applied with this source space. Let G be
a fixed compact connected simple group with the chosen faithful unitary
representation. Define b_rep>0 by

```text
-ReTr(rho_*(X)rho_*(Y))=b_rep <X,Y>.
```

Simplicity makes this positive invariant form a scalar multiple of the
chosen invariant metric. For the character Wilson tangent Hamiltonian
in the original-link metric and a positive regulator epsilon, set

```text
K_reg=2b_rep u K_C+epsilon^2 I_C,       epsilon>0,
c_reg=sqrt(2b_rep u .3072/(pi^10 L^2)+epsilon^2).
```

Equation (18) gives K_reg>=c_reg^2(I-P_S). The established full Gaussian
source theorem then yields

```text
dGamma(sqrt(K_reg)) >= c_reg (I-Gamma(P_(K_reg^(-1/4)S))),
c_reg >= sqrt(2b_rep u)/(sqrt(33)L).                   (19)
```

For fundamental SU(N) with <X,Y>=-2ReTr(XY), b_rep=1/2,
so the latter floor is sqrt(u)/(sqrt(33)L). The spatial map and (18)
need no simplicity assumption; the scalar frequency formula just stated
uses it. For a general compact group one must retain its actual invariant
color Hessian or a separately supplied lower bound for that matrix.

It holds on the entire Fock form domain and its full residual invariant
subspace. For every E<c_reg the literal Gaussian coordinate source frame
onto the whole low window has lower Gram bound 1-E/c_reg, in its exact
Gaussian marginal norm. The coordinate observation is the transverse
tangent quotient of (2), not the old nonlocal fine-Coulomb box observation.
As always its Wick source space is K_reg^(-1/4)S, not S with its frequency
weight discarded.

The positive regulator keeps the retained flat modes meaningful as Gaussian
oscillators. Its removal does not produce a normalized free-flat vacuum.
The spatial fast scale in (19) is order sqrt(u)/L and becomes order 1/(La)
under the established physical Hamiltonian normalization with u=g_H^(-4).
This scale conversion is not a continuum mass statement.

## 7. What this resolves and what remains

The source-locality gap in the prior harmonic construction is narrowed in
a concrete way: an actual two-cube gauge-covariant map now has a commuting
cochain tangent, and that exact physical tangent enjoys a box-count-uniform
full fast bound. The original interfaces and gauge/Bianchi constraints
remain in the theorem. The construction is independent of anchor choices
after taking physical transverse cotangents.

An actual nonlinear vacuum-subtracted fast form for functions of the matrix
blocks is still not inferred. It requires control of the nonlinear ground
marginal, mixing and interactions. Likewise whole-history observability
can exceed an equal-time source range; the map's endpoint covariance alone
does not supply reflection positivity or an exact OS intertwiner. These
are the next comparison obligations, together with flat-sector treatment.

## Evidence and provenance

This proof independently checks the root's averaged-path/Fourier proposal.
The Hodge identity and Gaussian inverse-frequency step are existing inputs,
with the current source locations recorded in Section 1. The new ingredients
are (2)-(6), the phase-preserving principal matching, the exact alias-tail
bound and their combined local source interpretation.

The companion finite checker constructs the actual rational incidence,
anchor and path-average matrices. It verifies both distinct commuting
zero-cochain squares, the anchor cancellation on coarse transverse fields,
rank and retained constants. Its 1,536 direct real-space/plane-wave
equalities verify the phase-sensitive Fourier symbol independently of the
separate alias implementation. For n=4,L=2 the exact Fourier aliases lie in
Q(i), and exact Hermitian elimination checks the full rational weaker bound
in every coarse Fourier block, rather than only on selected test vectors.
These are finite controls of conventions and algebra. The all-size bound,
nonlinear gauge covariance, local quotient interpretation and full Fock
consequence are the analytic statements above.

## Canonical source provenance and reproduction

This is the canonical copy of the independently reviewed 5 September
derivation [LOCAL_COVARIANT_AVERAGED_PATH_SOURCES.md](../../runs/wilson_endpoint_local_score_2026-09-05/LOCAL_COVARIANT_AVERAGED_PATH_SOURCES.md),
whose original SHA256 is `7f2703641051ff90f9ab9e5b9d2155fc4ef69b7f9ac717f3f683a01bcf0a5653`. The original proof bytes are
preserved; this copy adjusts only stage metadata and relative links,
then appends this explicitly separate provenance and follow-up record.

The [reproduction run](../../runs/wilson_endpoint_local_score_2026-09-05/README.md) preserves the analytic
sources and the precisely scoped finite controls:

- [check_covariant_path_sources.py](../../runs/wilson_endpoint_local_score_2026-09-05/check_covariant_path_sources.py)
- [covariant_path_source_controls.json](../../runs/wilson_endpoint_local_score_2026-09-05/covariant_path_source_controls.json)
- [check_fourier_alias_independent.py](../../runs/wilson_endpoint_local_score_2026-09-05/check_fourier_alias_independent.py)
- [fourier_alias_independent_controls_frozen.json](../../runs/wilson_endpoint_local_score_2026-09-05/fourier_alias_independent_controls_frozen.json)
- [INDEPENDENT_FOURIER_ALIAS_AUDIT.md](../../runs/wilson_endpoint_local_score_2026-09-05/INDEPENDENT_FOURIER_ALIAS_AUDIT.md)
