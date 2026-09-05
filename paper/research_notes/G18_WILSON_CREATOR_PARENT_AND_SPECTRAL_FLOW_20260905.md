# A uniformly gapped parent and quasi-local transport of the actual Wilson vacuum

5 September 2026. Analytic continuation from verified GitHub main
`ac39704568b09ae3613e3f5b099466ea3c0fa545`.

The rooted contraction and creator-limit theorems now give a bounded,
uniformly gapped auxiliary parent for the **actual symmetric Wilson Perron
vacuum**, and a quasi-local automorphism transporting its selected full
quantum state from the product vacuum. The parent gap is at least `247/256`.
This parent is constructed for vacuum transport; its excitation energies
are not the excitation energies of the Wilson transfer operator.

The new mechanism is a pair of orthogonal vacuum/excited block cancellations
and an exact sum-of-squares identity. They convert a rooted creator bound
into a volume-independent gap without estimating a global creator
exponential. Connected Taylor witnesses provide spatial decay, which then
allows an infinite-dimensional-site spectral-flow theorem to be applied.

## Theorem and direct inputs

Fix the calibrated Wilson model and the rooted-contraction hypotheses:
bounded four-link magnetic terms of norm at most `J_star>0`, at most four
plaquettes per link, additive
one-link excited kinetic gap `gamma>0`, `0<tau<=tau0`, and the stated
compact, self-adjoint, positivity-improving real Wilson kernel. Choose

```text
mu >= max(gamma tau0/2, log(2)+gamma tau0/4),
u_star = min(9 gamma/(309680 J_star exp(4mu)),
             9/(8450 tau0 J_star exp(4mu))).
```

Use the exact-support creator algebra and local coefficient compatibility
of the endpoint and coefficient-limit notes. Then:

1. On `|u|<u_star` the actual symmetric vacuum has analytic creators `w`
   with `||w||_(mu-gamma tau0/4)<=1/8`, uniformly in volume and mesh.
2. Its finite-volume parent `H_par=sum_i(q_i-A_i)^*(q_i-A_i)` has the
   corresponding vacuum line as its zero eigenspace and satisfies
   `H_par^2 >= (247/256) H_par`.
3. The actual creators stabilize locally in infinite volume. For real
   `|u|<=u_star/8`, their parent interactions and path derivatives have
   exponential connected-cover decay, uniformly in volume and mesh.
4. The selected finite-volume Wilson vacuum states converge on every
   bounded local quantum observable to the pure, locally normal state
   `omega_W=omega_0 composed with alpha_u`, for a quasi-local automorphism
   `alpha_u`. The corresponding local-vector parent form has a unique
   vacuum and gap at least `247/256` in its GNS representation.

Open cubic boxes and centered periodic cubic exhaustions are covered with
the metric comparison in Section 5. Identification with the previously
constructed Euclidean multiplication-source state also restricts to its
stated source domain `|u|<u_c`. No continuum limit, actual Wilson excited
gap, complete excited Riesz-range identification, or exponential operator
activity majorant is inferred from the auxiliary parent gap.

The full theorem is analytic. The Lean and exact finite controls described
in Section 6 certify their narrower statements.

## 1. Actual symmetric creators

Use the hypotheses and constants of
`paper/research_notes/G18_ROOTED_WILSON_CONTRACTION_20260905.md`, with `R=1/4`.
In finite volume let

```text
T = M C M,  M=exp(tau u V/2),  C=exp(-tau K),
phi=exp_star(v),  ||v||_mu <= R/4 = 1/16,
lambda phi = C exp(tau u V) phi.
```

The last identity is the actual fixed-point equation. Choose

```text
mu >= max(gamma tau0/2, log(2)+gamma tau0/4),
sigma_tau = mu-gamma tau/4,
sigma0 = mu-gamma tau0/4 >= log(2).
```

For each fixed complex coupling in the theorem's disk, run its magnetic
creator flow from the initial datum `v(u)` for the half time `tau/2`:

```text
w(u)=F_(tau/2)(u,v(u)).
```

The flow theorem applies to this initial datum because `1/16<R/2`. Its
rootwise estimate gives, with the same `A(R)` as in that theorem,

```text
||w||_(sigma_tau)
  <= ||v||_mu + |u| (tau/2) A(R)
  <= R/4 + R/4 = R/2 = 1/8 =: a.
```

The second inequality uses `|u| tau0 A(R)<=R/2`. Thus the stronger bound
`1/8`, rather than merely `R=1/4`, is available throughout the original
common coupling disk. In particular `||w||_(sigma0)<=a` uniformly in mesh.
The flow is holomorphic jointly in its initial data and coupling in the
interior domain; composition with the holomorphic fixed point proves
holomorphy of `w(u)` for `|u|<u_star`.

The scalar is exactly

```text
a_half(u)=<Omega0, M(u) exp_star(v(u))>
        =exp(integral_0^(tau/2) c(t,u) dt) != 0,
exp_star(w(u)) = M(u) exp_star(v(u)) / a_half(u).
```

The flow's scalar differential identity proves this nonvanishing throughout
the constructed complex disk, not just near zero. Since
`T M phi=M C exp(tau uV)phi=lambda M phi`, the normalized vector
`Psi=exp_star(w)/||exp_star(w)||` is the actual symmetric Wilson eigenvector.
For real coupling, the already stated compact, self-adjoint,
positivity-improving Wilson-kernel premise and the rooted theorem's branch
continuation identify it with the Perron vacuum throughout `|u|<u_star`.
Its phase has no effect on the vector state. The scalar `a_half` and the
Hilbert norm can be extensive; no uniform global similarity condition number
or infinite-product vector is asserted.

## 2. A generic uniform creator-parent gap

Let I be a finite set of links. Each link Hilbert space H_i has a unit
vacuum Omega_i, vacuum projection p_i, and excited projection q_i=1-p_i.
The spaces may be infinite dimensional. For every nonempty X subset I,
let w_X belong to the exact excited tensor factor tensor_{i in X} q_i H_i.
Embed the bounded rank-one creator

    a_X = |w_X><Omega_X| tensor 1_{I\X}

in the full finite-link tensor product. Write b_X=||w_X||=||a_X|| and

    A   = sum_{X nonempty} a_X,
    A_i = sum_{X contains i} a_X,
    P_i = q_i-A_i,
    H   = sum_i P_i^* P_i.

Define

    M1 = max_i sum_{X contains i} |X| b_X,
    K1 = max_i sum_{X contains i} (|X|-1) b_X,
    kappa = K1 + M1^2.

Then H is a bounded positive self-adjoint operator with

    ker H = span{exp(A) Omega},
    H^2 >= (1-kappa) H.

Consequently, if kappa<1, H has a simple zero eigenvalue and spectral gap
at least 1-kappa, uniformly in the number of links and the dimensions of
their Hilbert spaces. No bound on ||exp(A)|| ||exp(-A)|| is used.

This is the gap of the explicitly constructed parent operator H. The
statement does not identify H with the physical Wilson kinetic generator
or prove an interacting Wilson excited-band or source-frame theorem.

### 2.1. Commuting nonorthogonal projections and the exact vacuum

Disjoint creators commute as tensor factors. If X and Y intersect, both
products a_X a_Y and a_Y a_X vanish: a shared link is excited after the
first creator and the second creator's vacuum bra annihilates it. Thus
all creators commute. Their sum A is nilpotent of degree at most |I|+1,
so exp(A) and exp(-A) are finite operator polynomials and are inverse.

For i in X, q_i a_X=a_X and a_X q_i=0; if i is outside X, q_i commutes
with a_X. Hence

    [A,q_i]=-A_i,       [A,A_i]=0,
    P_i=exp(A) q_i exp(-A).

The P_i commute and satisfy P_i^2=P_i. Their common kernel is the
invertible image under exp(A) of the common kernel of the q_i. The latter
is precisely the one-dimensional product-vacuum space. Positivity gives

    <psi,H psi> = sum_i ||P_i psi||^2,

which proves the stated kernel and existence of its zero eigenvector.

### 2.2. Two exact orthogonal-block norm savings

For distinct i,j, put A_ij=sum_{X contains i,j}a_X. Direct commutation gives

    C_ij := [P_i,P_j^*]
          = A_ij + A_ij^* + [A_i,A_j^*].                 (1)

The signs follow from [q_i,a_X^*]=-a_X^* when i belongs to X and
[a_X,q_j]=-a_X when j belongs to X.

First, A_ij=q_i A_ij p_i. In the orthogonal splitting into link i's
vacuum and excited sectors, A_ij+A_ij^* is a self-adjoint off-diagonal
block matrix. Squaring this matrix proves

    ||A_ij+A_ij^*|| = ||A_ij||
                     <= sum_{X contains i,j} b_X.       (2)

Thus a generic triangle bound with factor two is unnecessary.

Second, disjoint a_X and a_Y^* commute. When S=X intersection Y is
nonempty, define the orthogonal projections

    p_S = tensor_{s in S} p_s,
    e_S = tensor_{s in S} q_s,

embedded by the identity elsewhere. Exact excited support implies

    a_X a_Y^* = e_S (a_X a_Y^*) e_S,
    a_Y^* a_X = p_S (a_Y^* a_X) p_S.

Since p_S e_S=0, these two products occupy orthogonal diagonal blocks,
even when w_X and w_Y are entangled vectors on their supports. Therefore

    ||[a_X,a_Y^*]||
      = max{||a_X a_Y^*||, ||a_Y^* a_X||}
      <= b_X b_Y.                                     (3)

This is another factor-two improvement over the generic commutator bound.

### 2.3. Uniform row sum of off-diagonal commutators

Sum (2) over j different from i. Each creator with support X containing i
is counted |X|-1 times, so its row sum is at most K1. From (3),

    sum_{j != i} ||[A_i,A_j^*]||
      <= sum_{X contains i} b_X
           sum_{Y intersects X} (|Y|-1_{i in Y}) b_Y
      <= sum_{X contains i} b_X
           sum_{k in X} sum_{Y contains k} |Y| b_Y
      <= M1 sum_{X contains i} |X| b_X
      <= M1^2.

The second inequality is a nonnegative union bound; overcounting a set Y
that intersects X several times only enlarges the upper bound. Equation
(1) consequently yields

    max_i sum_{j != i} ||C_ij|| <= K1+M1^2=kappa.       (4)

The estimate includes arbitrary overlapping creator supports. In particular
it is not a disjoint-block approximation or a finite-support truncation.

### 2.4. The positive square identity

For any bounded idempotent P, set B=P^*P. Exact multiplication gives

    B^2-B = ((P^*-1)P)^* ((P^*-1)P) >= 0.             (5)

Thus this inequality does not require P to be orthogonal. For i different
from j, commute P_i past P_j^*, then use P_i P_j=P_j P_i:

    (P_i^*P_i)(P_j^*P_j)
      = (P_i P_j)^*(P_i P_j) + P_i^* C_ij P_j.         (6)

Summing (5)-(6) gives an exact decomposition of H^2 into H, nonnegative
diagonal corrections, nonnegative terms (P_i P_j)^*(P_i P_j), and

    E = sum_{i != j} P_i^* C_ij P_j.

The error E is self-adjoint because C_ji=C_ij^*. For every vector psi,
put x_i=||P_i psi|| and c_ij=||C_ij||=c_ji. Then

    <psi,E psi>
      >= -sum_{i != j} c_ij x_i x_j
      >= -(1/2) sum_{i != j} c_ij (x_i^2+x_j^2)
      = -sum_i x_i^2 sum_{j != i} c_ij
      >= -kappa sum_i ||P_i psi||^2
      = -kappa <psi,H psi>.

This proves H^2 >= (1-kappa)H. Functional calculus for the bounded positive
self-adjoint H places its spectrum in {0} union [1-kappa,infinity) when
kappa<1. The similarity argument above identifies the zero space exactly.

### 2.5. Explicit rooted-weight corollaries

For this generic corollary let nu>=log(2) and suppose the creator family obeys

    ||w||_nu := max_i sum_{X contains i} exp(nu |X|) b_X <= a.

For integers n>=1,

    n exp(-nu n) <= n/2^n <= 1/2,
    (n-1) exp(-nu n) <= (n-1)/2^n <= 1/4.

The respective sharp maxima at nu=log(2) occur at n=1,2 and n=2,3.
Consequently

    M1 <= a/2,     K1 <= a/4,
    gap(H) >= 1-a/4-a^2/4,                            (7)

whenever the displayed lower bound is positive. Two useful cases are

    a<=1/4  ==> gap(H)>=59/64,
    a<=1/8  ==> gap(H)>=247/256.

For the actual symmetric Wilson creators, Section 1 supplies nu=sigma0
and a=1/8. This proves the stated 247/256 parent gap; the norm bound is
obtained from the half-time flow rather than assumed after a change of
coordinates.

## 3. Spatial locality and derivatives

Introduce the independent active plaquette variables in the finite-volume
analytic germ. If the active plaquettes split into link-disjoint components,
the symmetric transfer, its actual vacuum branch, its Haar vacuum
normalization, and the magnetic endpoint all factor over those components.
The creator logarithm of the resulting star product is their sum. Therefore
the creator family `w`, just as `v`, has no Taylor monomial spanning separate
active components.

Every nonzero degree-`n` monomial has a connected witness of at most `n`
plaquettes, whose footprint has at most `3n+1` links. The output exact support
need not be connected. Consequently the complete rooted Taylor family
stabilizes at each degree in sufficiently large volumes. Cauchy on any
circle `0<r<u_star` gives

```text
||w_n^Lambda||_(sigma0) <= a r^(-n),
||w_n^infinity||_(sigma0) <= a r^(-n).
```

The coefficient-limit proof therefore applies without alteration to the
actual symmetric creators. They define an infinite analytic family
`w^infinity(u)` of norm at most `a`; if every active cluster through degree
`N` fits at a root, its local approximation error is at most

```text
2a q^(N+1)/(1-q),  q=|u|/r<1.
```

This is local convergence, not global convergence of zero-extended finite
boxes in the supremum over every lattice root.

### 3.1. Spatial weight and moments

For a nonempty finite link support `X`, let `c(X)` be the minimum number of
plaquettes in a connected plaquette family whose footprint contains `X`.
Connectivity means adjacency by a shared link. On the infinite cubic lattice
this is finite; a coefficient with degree `n` vanishes unless `c(X)<=n`.
For a finite periodic lattice use its intrinsic periodic cover number and
link-graph metric. A wrapping support need not have small diameter after
embedding a fundamental domain into the infinite lattice; Section 5.6
handles that comparison.
Define

```text
M_j(nu,kappa;w)
 = sup_i sum_(X contains i) |X|^j exp(nu |X|+kappa c(X)) ||w_X||.
```

At `nu=sigma0`, coefficient Cauchy estimates give, for
`z=exp(kappa)|u|/r<1`,

```text
M_0 <= a z/(1-z),
M_1 <= a sum_(n>=1) (3n+1) z^n
    = a z(4-z)/(1-z)^2.
```

No new multivariate convergence theorem or count of connected clusters is
needed: the entire rooted coefficient is already bounded by one-variable
Cauchy, and its support and witness sizes are bounded by its degree.
The spatially weighted series is holomorphic on
`|u|<exp(-kappa)u_star`.

For the concrete choice `r=u_star/2`, `kappa=log(2)`, and
`|u|<=u_star/8`, one has `z<=1/2` and `M_0(sigma0,kappa)<=a=1/8`.
Cardinal moments at weaker support weight follow more efficiently from this:
for `delta=sigma0-nu>0`,

```text
M_1(nu,kappa) <= [sup_(m>=1) m exp(-delta m)] M_0(sigma0,kappa)
              <= M_0(sigma0,kappa)/(e delta).
```

In particular, since `sigma0>=log(2)`,
`M_0(0,kappa)<=a/2` and `M_1(0,kappa)<=a/2`, because
`2^(-m)<=1/2` and `m/2^m<=1/2` for every positive integer `m`.

If `X` and `Y` intersect, then
`c(X union Y)<=c(X)+c(Y)`: their chosen connected covers are joined by the
shared link. Thus the weight used above is submultiplicative on intersecting
supports. In the link graph where two links are adjacent when one plaquette
contains both, `diameter(X)<=c(X)` for every covered set. These estimates
therefore imply exponential spatial tails, rather than just decay with
support cardinality.

### 3.2. Explicit derivative bounds with a decay margin

For the path `s -> su`, `0<=s<=1`, take `r=u_star/2` and
`beta_plus=log(5/2)`. On `|u|<=u_star/8` put
`t=exp(beta_plus)|u|/r<=5/8`. The degree-n bound and `c(X)<=n` give

```text
sup_s ||w(su)||_(sigma0,beta_plus) <= a t/(1-t) <= 5/24,
sup_s ||partial_s w(su)||_(sigma0,beta_plus)
    <= a sum_(n>=1) n t^n = a t/(1-t)^2 <= 5/9.
```

Thus the sum of these two norms is at most `55/72`. These are norm
derivatives of creator vectors; the parent uses adjoints and is a smooth
real path, not a holomorphic self-adjoint operator in complex coupling.
They hold for the actual finite families, their limit, and restrictions.
Differentiating `(su)^n` contributes `n u^n s^(n-1)`; the factor
`s^(n-1)<=1` includes the degree-one term at `s=0`. The displayed summable
majorant justifies termwise differentiation uniformly along the path.

When all witnesses through degree N fit at a specified root, the finite
minus infinite local rooted norms are bounded respectively by

```text
2a t^(N+1)/(1-t),
2a t^(N+1) ((N+1)-N t)/(1-t)^2.
```

For the derivative, the second expression is `2a sum_(n>N) n t^n`.
The same estimates hold uniformly in s. They prove local interaction and
derivative convergence with uniform tails. Retain the smaller support
weight `sigma0/2>0` and cover weight `log(2)<beta_plus` below: the two
strict margins absorb all fixed support-size polynomials and leave
exponential spatial tails. No global norm convergence of zero-extended
boxes is used.

For periodic families, weighted differences are compared on each fixed
embedded neighborhood, where cover numbers agree for sufficiently large
volumes. Exterior tails are bounded separately in their intrinsic metrics.
There is no whole-family ambient cover-weight difference bound for a
cut-open torus. Unweighted rooted differences still follow from coefficient
stabilization and the support-norm Taylor tail.


## 4. Parent interaction and the GNS form

Let `a_X=|w_X><Omega_X|`, embedded with identity spectators, and put

```text
W=sum_X a_X,  A_i=sum_(X contains i) a_X,
b_i=q_i-A_i,
H_parent=sum_i b_i^dagger b_i,  N=sum_i q_i.
```

These are bounded finite-volume operators; the individual link Hilbert spaces
need not have finite dimension. Creators commute and intersecting creator
products vanish. Hence `[q_i,W]=A_i`, `[W,A_i]=0`, and the exact relation is

```text
b_i = exp(W) q_i exp(-W),
b_i exp(W)Omega0=0.
```

The joint kernel in finite volume is one-dimensional: conjugation by the
invertible finite-volume `exp(W)` sends it to the joint kernel of all `q_i`,
namely the free product-vacuum line. Thus `H_parent` has exactly the actual
Wilson Perron vacuum as its zero-energy state. This does not identify the
parent excitation energies with the Wilson transfer energies.

Since `q_i A_i=A_i` and `A_i^dagger q_i=A_i^dagger`,

```text
H_parent-N = -sum_X |X|(a_X+a_X^dagger)
             +sum_(X,Y) |X intersection Y| a_X^dagger a_Y.
```

Group the displayed terms by support `Z=X` and `Z=X union Y`, respectively,
to obtain the self-adjoint perturbation interaction `Phi_pert` for
`H_parent-N`. Its rooted interaction norm
obeys

```text
||H_parent-N||_(nu,kappa)
 := sup_ell sum_(Z contains ell) exp(nu |Z|+kappa c(Z)) ||Phi_pert,Z||
 <= 2 M_1(nu,kappa) [1+M_0(nu,kappa)].
```

For the linear term this is immediate. For a quadratic term charge the root
to `X` or `Y`, at a factor at most two; summing the shared index `i` over
`X` costs `|X|`, and summing `Y contains i` costs `M_0`. Intersecting-support
submultiplicativity gives exactly the displayed bound. This proof does not
replace operator norms by selected vacuum matrix elements.

The interaction is arbitrarily small in a fixed positive spatial weight as
`u` tends to zero. At the concrete smaller disk above,

```text
||H_parent-N||_(0,log(2)) <= a(1+a/2)=17/128.
```

The uniform bound on the original disk at zero spatial weight is the same,
using `||w||_(log(2))<=a`. Gauge, charge, and lattice symmetries respected by
the actual transfer and vacuum pass through the exact-support projections
and creator logarithm; the parent interaction preserves those symmetries.

### 4.1. State and closed parent form

Take real `|u|<u_star` and an open-box or centered periodic exhaustion
compatible with coefficient locality. The parent-form construction below
requires this creator domain. For identification with the previously
constructed multiplication-source state, additionally impose the source
domain `|u|<u_c` of `G19_DISCRETE_TIME_VACUUM_AND_WINDOW_20260904.md`,
equation (15), and use an exhaustion covered by that source-limit theorem.
The stronger spectral-flow conclusion in Section 5 uses `|u|<=u_star/8`.

Let `mathcal A` be the quasi-local C*-algebra obtained by completing the
union of the full bounded operator algebras on finite link sets. Extend each
actual finite Wilson vector state by the reference product state outside its
volume. These define states on `mathcal A`. State-space weak-* compactness
gives a convergent subnet. A sequence is not asserted, since infinite link
dimensions make the full local algebras nonseparable in norm. Denote any
such limit by `omega`.

For every fixed link, the creators give norm-convergent quasi-local operators

```text
A_i^infinity=sum_(X contains i) a_X^infinity,
b_i^infinity=q_i-A_i^infinity.
```

Root-local coefficient convergence implies
`||A_i^Lambda-A_i^infinity||->0`. Since the finite vector state has
`omega_Lambda((b_i^Lambda)^dagger b_i^Lambda)=0`, norm continuity and weak-*
convergence imply

```text
omega((b_i^infinity)^dagger b_i^infinity)=0,
pi_omega(b_i^infinity)Omega_omega=0.
```

This is a physical state realization of the actual symmetric creator
annihilation equations. It avoids an infinite sum `W` or a purported
normalizable `exp(W)Omega0`.

On the stated source-domain intersection, the existing discrete-time
vacuum theorem, Section 5, identifies the
finite-volume zero-temperature state with precisely the same Perron vector
state and proves the common thermodynamic limit of all bounded local
multiplication-source correlations. Therefore all the subnet states above
restrict to that established Wilson equal-time multiplication-source state.
Their equal-time multiplication GNS cyclic subspaces are canonically
isometric: inner products of `A Omega` and `B Omega` agree because
`omega(A^dagger B)` agrees. The extension to every bounded local quantum
operator, and identification of the full Euclidean transfer representation,
are not uniqueness statements proved by this observation.

### 4.2. A gapped parent operator in each such GNS representation

Let `B_i=pi_omega(b_i^infinity)`. On the dense local-vector domain define

```text
q_0(A Omega_omega)=sum_i ||B_i A Omega_omega||^2.
```

This is finite. If `S` supports `A`, then `B_i Omega=0` and

```text
sum_i ||[b_i,A]||
 <= |S| ||A|| + 2||A|| sum_(X intersects S) |X|||w_X||
 <= |S| ||A|| [1+2 M_1(0,0)].
```

The first term accounts for `[q_i,A]` and uses `||[q_i,A]||<=||A||` for an
orthogonal projection; the weaker `2||A||` also suffices. Thus the relevant
commutator sequence is square summable. The maximal form
`sum_i||B_i psi||^2` is closed: its graph map from `psi` to `(B_i psi)_i`
is closed because each coordinate operator is bounded. Its restriction to
local vectors is therefore closable. Write `overline(q_0)` for this closure.
No claim that local vectors are a core for the maximal summed form is needed.

For each local `A`, the finite parent gap gives

```text
omega_Lambda(A^dagger H_parent^Lambda A)
 >= g [omega_Lambda(A^dagger A)-|omega_Lambda(A)|^2],
g=247/256.
```

The left side equals
`omega_Lambda(A^dagger[H_parent^Lambda,A])`. The interaction expansion and
its rooted cardinal moments make these commutators norm-convergent for fixed
`A`: each degree has identical local coefficients in large volumes, while
the Cauchy and `(3n+1)` moment estimates make their tails uniformly
summable. Its limit is `q_0(A Omega)`. Consequently

```text
q_0(A Omega) >= g [||A Omega||^2-|<Omega,A Omega>|^2].
```

Passing to the form closure preserves this inequality. The nonnegative
self-adjoint operator associated with `overline(q_0)` therefore has the
unique ground-state line `C Omega` and spectrum in `{0} union [g,infinity)`.
Equivalently it is the Friedrichs parent realization from local vectors.
This provides a gapped auxiliary parent in every obtained full quantum GNS
extension, and the same lower bound on its invariant physical subspace when
the retained symmetries commute with the parent. It does not prove that
different extensions coincide, or identify this auxiliary operator with
the Wilson transfer generator.

This form argument by itself applies to any obtained subnet and does not
establish uniqueness of the full extension. Section 5 strengthens it by
proving a common limit of the selected finite-volume states.


## 5. Quasi-local spectral transport of the selected Wilson vacuum

### 5.1. Primary-source hypotheses

**BMNS:** Bachmann, Michalakis, Nachtergaele, Sims,
[arXiv:1102.0842v2](https://arxiv.org/pdf/1102.0842v2).
Assumption 2.1 and Proposition 2.4, printed pages 3-5, give finite-volume
spectral transport for a self-adjoint path with bounded derivative and an
isolated spectral interval with uniform separation; Hilbert-space dimension
is unrestricted. However, Section 5, printed pages 21-22, explicitly
restricts its thermodynamic Theorems 5.2 and 5.5 to finite-dimensional
on-site spaces. The abstract alone therefore does not justify applying
those thermodynamic theorems directly to Wilson rotors.

**NSY:** Nachtergaele, Sims, Young,
[arXiv:1810.02428](https://arxiv.org/pdf/1810.02428).
Section 3.1.1 allows general on-site Hilbert spaces. Assumption 6.12,
printed page 78, requires self-adjoint strongly C1 interactions satisfying

    sum_{Z contains x,y}(||Phi_Z(s)||+|Z| ||Phi'_Z(s)||)
        <= C(s) F(d(x,y)),                              (SF)

with bounded measurable C and F(r)=exp(-g(r))/(1+r)^xi.
Theorem 6.14, printed page 81, assumes g(r)>=b r^theta, b>0,
0<theta<=1, and establishes the thermodynamic spectral flow; equation
(6.122) gives its norm limit on local observables. Theorem 6.3 gives exact
spectral transport. Theorem 7.4, printed page 85, transports selected limit
states. Definition 3.7 and Theorem 3.8 give interaction/dynamics continuity;
Section 7.1, printed page 84, explicitly discusses volume-dependent
interactions converging locally uniformly in this norm. Consistent normal
product-state expectations are used in Section 4 and equations (6.117)-(6.118).

These are the relevant references, rather than a finite-spin theorem
informally extrapolated to an infinite-dimensional link space.

### 5.2. Verified creator inputs

Fix real `|u|<=u_star/8` and use the path `u(s)=su`, `0<=s<=1`.
The relevant support weight is `sigma0=mu-gamma tau0/4`, as in Section 1;
it must not be replaced by the larger initial endpoint weight `mu`.

Sections 1-3 provide all creator inputs: the analytic actual symmetric
vacuum family vanishing at zero, its support norm at most `a=1/8`, the
connected-coefficient witnesses, the common parent gap `247/256`, and
the derivative/tail bounds in Section 3.2. In particular the sum of the
creator and derivative norms at weights `(sigma0,beta_plus)` is at most
`55/72`, with `beta_plus=log(5/2)`. Retaining weights `sigma0/2` and
`log(2)` leaves the positive margins `sigma0/2` and `log(5/4)`.

The connected-cover weight supplies spatial decay even when an exact
output support is disconnected. Open boxes use the infinite-lattice
metric. Periodic boxes use their intrinsic metrics until the local
comparison in Section 5.6. These distinctions are part of the verified
input, not further spectral hypotheses.

### 5.3. One consistent infinite-volume interaction

Let a_X(s)=|w_X^infinity(su)><Omega_X|, embedded by the identity. Define a
self-adjoint interaction on finite link sets by

    Phi_Z(s) = 1_{Z={i}} q_i - |Z|(a_Z(s)+a_Z(s)^*)
             + sum_{X union Y=Z} |X intersection Y| a_X(s)^* a_Y(s).
                                                               (1)

The singleton term means q_i if Z is the singleton {i}, and zero
otherwise. Terms with empty intersection have zero coefficient. The
quadratic sum is self-adjoint because exchanging X,Y takes adjoints.
At each finite Z, (1) is a finite sum of bounded operators.

For every finite link set Lambda, summing (1) over Z subset Lambda gives

    Hhat_Lambda(s)
      = sum_{i in Lambda}(q_i-Ahat_i,Lambda(s))^*
                            (q_i-Ahat_i,Lambda(s)),
    Ahat_i,Lambda(s)=sum_{X subset Lambda, X contains i} a_X(s).
                                                               (2)

This is exactly the parent of the truncated infinite creator family.
Indeed q_i a_X=a_X and a_X^*q_i=a_X^* when i belongs to X, and counting
the admissible i gives |X| and |X intersection Y| in (1). Thus the
finite-volume Hamiltonians in (2) are restrictions of ONE interaction;
they are not merely a collection of unrelated parents.

Restriction cannot increase the rooted norm. The generic parent-gap
proof therefore applies to every Hhat_Lambda along the whole real path:
its zero space is one-dimensional and its gap is at least 247/256.
Its ground vector need not equal the actual finite-Lambda Wilson vacuum.
That comparison is handled in the local comparison below.

One may set the fixed on-site Hamiltonians in the spectral-flow framework
equal to zero and include q_i in Phi. In particular, no unbounded Wilson
electric generator is being differentiated or conjugated in this use of
spectral flow. All local parent terms and their path derivatives are bounded.

### 5.4. The spectral-flow interaction norm

Use the cover number `c(X)` and link-graph metric of Section 3.1, so
`diam(X)<=c(X)` and `c(X union Y)<=c(X)+c(Y)` for intersecting supports.
Section 3.2 supplies eta=sigma0>=log(2), beta=beta_plus, and B<=55/72 with

    sup_s sup_i sum_{X contains i}
        exp(eta|X|+beta c(X))
        (||w_X(su)||+||partial_s w_X(su)||) <= B.         (3)

Use retained weights eta=sigma0/2 and beta=log(2) when estimating the
interaction. The discarded positive margins absorb any fixed polynomial
in support or cover sizes. For the quadratic terms in
(1), use ||a_X^*a_Y||<=||w_X|| ||w_Y|| and write the overlap count as
sum_i 1_{i in X intersection Y}. To sum terms whose union contains a root
x, distinguish x in X and x in Y. For example,

    sum_{X contains x} b_X sum_{Y intersects X}|X intersection Y| b_Y
      = sum_{X contains x} b_X sum_{i in X} sum_{Y contains i} b_Y
      <= (sup_i sum_{Y contains i}b_Y)
                            sum_{X contains x}|X|b_X.   (4)

Exactly the same counting works with the exponential cover weight, by
the two subadditivity inequalities for a union. Derivatives replace one
factor b by its derivative bound. The additional |Z| in (SF), as well as
the linear prefactor |Z| and overlap counts, are absorbed by the positive
support-weight margin in (3). Thus, for some k>0 and C0<infinity,

    sup_s sup_x sum_{Z contains x} exp(k diam(Z))
           (||Phi_Z(s)||+|Z| ||partial_s Phi_Z(s)||) <= C0.
                                                               (5)

This yields a pair bound C0 exp(-k d(x,y)). Choose, for example,

    F(r)=exp(-k r/2)/(1+r)^5.

The remaining factor (1+r)^5 exp(-k r/2) is bounded. The cubic-link
geometry has growth exponent 3, so this F has the required summability
and convolution properties. Equation (SF) follows with a finite constant.
Norm differentiability of each Phi_Z is stronger than strong C1.

For open boxes the same fixed-metric estimates hold uniformly for the
interaction Phi^Lambda built from actual w^Lambda. For periodic boxes
they hold in the intrinsic periodic metric, with the same constants;
they do NOT imply a uniform ambient F-norm after a wrapping interaction
has been embedded into a fundamental domain. On every fixed interior
set of link labels, both
Phi^Lambda and its derivative converge uniformly in s to Phi. There are
only finitely many subsets in such a fixed set, and the positive decay
margin controls the remaining tails. This verifies the local interaction
convergence needed for the open-box comparison. The periodic comparison
requires the extra intrinsic-metric argument in Section 5.6.

### 5.5. Comparing actual finite-volume parents with restrictions

The finite-volume Wilson parents have Phi^Lambda in place of Phi. Their
spectral-flow parameter can use a single gap cutoff smaller than 247/256,
for example gamma_flow=1/2. Choose the same filter and the same normal
product-state conditional expectations for all volumes.

For open boxes, here is the local-limit argument behind using the volume-dependent
version, rather than claiming Phi^Lambda is literally a restriction:

* Uniform interaction bounds give uniform Lieb-Robinson estimates for
  the physical-time dynamics of all these bounded parent Hamiltonians.
  On any local observable, the dynamics for Phi^Lambda and restrictions
  of Phi have the same limit, uniformly for s and bounded time intervals:
  first restrict to a large fixed neighborhood, then use local interaction
  convergence there; the exterior error is uniformly small by locality.
* The spectral-flow generator is a filtered time integral of evolved
  derivative terms. For a fixed local derivative term, truncate its time
  integral to [-T,T]. The omitted norm is bounded by its norm times the
  L1 tail of the common filter. The remaining integral converges by the
  preceding dynamics comparison and local derivative convergence.
* Decompose these filtered terms with the common product-state conditional
  expectations into successively enlarged supports. Their uniform
  locality estimates have summable moments after spectral filtering;
  the original exponential decay is sufficient for this. Truncating this
  support decomposition and the original derivative-support tail leaves
  finitely many local comparisons. Sending Lambda to infinity, then the
  support and time truncations to infinity, shows that both constructions
  have the same local limit for the spectral-flow interaction.
* Applying the local dynamics comparison to the two spectral-flow
  interactions gives the same quasi-local automorphism alpha_s. The
  comparison is uniform on the unit ball of every fixed local observable
  algebra and uniform in s. Reverse flows converge as well, so the limit
  is an automorphism, not just an endomorphism.

This uses local convergence with uniform tails, never the false assertion
that zero-extended finite boxes converge globally in a supremum over all
roots. Boundary-dependent terms need not be globally small.

### 5.6. Periodic boxes and their intrinsic metric

Take centered cubic tori of side L tending to infinity, with L>=3.
Use their link graph in which two links are adjacent if one plaquette
contains both. A wrapping plaquette has intrinsic diameter one even if
its chosen fundamental-domain representatives are O(L) apart. Accordingly
the periodic interaction is not declared to have uniform F-norm in the
ambient metric. The following comparison avoids that false inference.

The torus graph balls obey |B_L(x,R)|<=C(1+R)^3 with C independent of L.
For R below a fixed fraction of L, they are quotients of balls of the
infinite cubic-link graph; for larger R, the bound follows from the total
number 3L^3 of links. Uniform polynomial growth implies uniformly bounded
sums of F0(r)=(1+r)^(-5). The convolution constant is uniform as well:
for each intermediate z, either d_L(x,z)>=d_L(x,y)/2 or
d_L(z,y)>=d_L(x,y)/2. Combine that dichotomy with the triangle inequality
for the exponential factors in F(r)=exp(-b r)F0(r), then sum the other
factor. This bounds the convolution by a fixed multiple of F(d_L(x,y)).
All finite-volume Lieb-Robinson constants therefore use the same data.

For any fixed finite observable support S and radius R, the intrinsic
R-neighborhood of S embeds isometrically into the infinite lattice once
L is sufficiently large. In that neighborhood the local creator
coefficients and derivatives have the same stabilized Taylor terms.
The remainder bounds in Section 3 are uniform and decay with L.

First compare the physical-time parent evolutions. Restrict the torus
parent Hamiltonian to terms wholly supported in this embedded neighborhood.
For times |t|<=T, the uniform Lieb-Robinson restriction estimate bounds
the change on an observable B in A_S by

    C_T ||B|| sum_{x in S} sum_{y outside B_L(S,R)} F(d_L(x,y)),

with C_T independent of L. Uniform growth and summability make this
small as R increases, uniformly in L. On the fixed neighborhood, the
interaction and derivative coefficients converge in norm, so its
dynamics converge to the corresponding infinite-lattice restricted
dynamics. The analogous restriction error on the infinite lattice is
also small. Thus the full torus dynamics converge on A_S, uniformly
on its unit ball, in s, and for bounded time intervals. The order of
limits is: fix R,T; let L tend to infinity; then increase R,T as needed.

Next use the same spectral filter on all tori and the infinite lattice.
Its time tail is uniformly integrable. For a derivative term with fixed
local support, truncate the filter integral at T and use the preceding
dynamics convergence. The finite-volume conditional expectations are
formed with the same normal product vacuum state; on an embedded
neighborhood they agree with the infinite-system conditional expectations.
The filtered-term localization estimates depend only on the uniform
metric growth, F constants and filter. They therefore have the same
summable tails on every torus. Split their support expansions into a
fixed-radius interior part and the remaining tail. The interior part
converges termwise; the tail is uniformly small. This proves local
convergence of the torus spectral-flow interactions to the same
infinite-lattice interaction as in the open-box construction.

Finally repeat the first restriction/dynamics argument for these
spectral-flow interactions, using their summable, generally slower
decay function instead of the original exponential F. It follows that
the torus spectral flows converge to alpha_s uniformly on the unit ball
of every fixed A_S and uniformly in s. Reverse flows obey the same
argument. Wrapping terms have been controlled through intrinsic
distance to the fixed root, never through a nonexistent uniform
ambient interaction norm.

Consequently both open-box exhaustions and centered periodic exhaustions
select the same local automorphism and state. This extra argument is
what makes the periodic application precise; a bare citation of a
fixed-metric local-convergence theorem would omit it.

### 5.7. The selected actual Wilson state and its GNS representation

Use the convention alpha_Lambda,s(B)=U_Lambda(s)^* B U_Lambda(s), with
U_Lambda transporting the free parent ground projection to the ground
projection at s. The actual finite-volume parent ground projection is
the actual Wilson vacuum projection. For every local bounded observable B,

    omega_W,Lambda(su)(B) = omega_0(alpha_Lambda,s(B)).

The local comparison above therefore gives the full, rather than subsequential, selected
local limit

    omega_W(su)(B) = omega_0(alpha_s(B)).                 (6)

The limit is independent of the compared admissible exhaustions. The
product vacuum omega_0 is pure, and an automorphism preserves purity;
thus this selected state is pure on the full quasi-local link algebra.
This does not claim uniqueness among every abstract state satisfying
some different infinite-volume boundary condition or representation.

There is no residual local-normality problem. Restricted to a fixed
finite local algebra B(H_X), the right side of (6) is the functional-norm
limit of restrictions of finite-volume normal states, because the flow
comparison is uniform on that local unit ball. Normal functionals form
a norm-closed predual. Hence omega_W is locally normal, even though H_X
is infinite dimensional. Mere pointwise weak-star convergence would not
have been enough for this inference.

Let (H_W,pi_W,Omega_W) be its GNS representation and
(H_0,pi_0,Omega_0) the product state's representation. The map

    pi_W(B)Omega_W  |->  pi_0(alpha_s(B))Omega_0          (7)

preserves inner products by (6), has dense range because alpha_s is onto,
and extends to a unitary. Thus pi_W is unitarily equivalent to
pi_0 composed with alpha_s. Equation (7) is the precise automorphic GNS
equivalence. It does NOT assert that alpha_s is implemented by a unitary
inside the original free infinite tensor-product representation, nor
that the untransformed representations pi_W and pi_0 are equivalent.

If the already constructed physical Wilson state is defined by these
same finite-volume Perron expectations on the same bounded local
observable algebra, (6) identifies it directly with this state; uniqueness
of the local limit supplies the identification. If a prior Euclidean
construction has so far only specified a smaller commuting time-zero
algebra, its extension to the present noncommutative observable algebra
must be explicitly matched. Equality on a smaller commuting algebra alone
does not identify every electric or time-dependent observable.

When the parent family is covariant under the retained gauge and global
symmetries, the common spectral filter and invariant product reference
state make alpha_s symmetry-covariant. It then restricts to the invariant
observable algebra. This uses the actual covariance of the creator
family; it is not obtained by assuming a tensor decomposition of the
gauge-constrained Hilbert space.

## 6. Evidence, provenance, and the next mathematical target

The direct research inputs are the pinned endpoint equation,
`G18_ROOTED_WILSON_CONTRACTION_20260905.md`, and
`G18_WILSON_CREATOR_THERMODYNAMIC_LIMIT_20260905.md`. The September C2
resolution, all-rank assembly, and fixed-spacing Hamiltonian G18 theorem
remain established wider-program inputs; this proof does not rederive them.

Independent work in `runs/wilson_creator_parent_2026-09-05` records:

* The generic analytic parent-gap derivation, independently checked from
  exact-support algebra, including entangled vectors and infinite-dimensional
  link factors; the actual half-flow and GNS derivation; and the separate
  primary-source spectral-flow hypothesis audit.
* Six rational finite tensor models (81 PSD certificates), including intersecting supports and
  entangled multi-level excited vectors. The exact checks reconstruct all
  matrices, verify the vacuum, ranks, commuting idempotents, block norm
  bounds, and rational positive-semidefinite congruence certificates for
  both `H^2-gH` and `H-g(I-Psi Psi^*/||Psi||^2)`. A separate replay checks
  the certificates independently. These are finite controls, not a proof
  of the uniform Hilbert-space or infinite-volume assertions.
* Lean theorems `idempotent_square_defect` and `commuting_pair_square`
  prove the two star-ring identities under the displayed algebraic
  hypotheses. `wilson_gap_constant` proves the real scalar estimate from
  `a<=1/8`, `K<=a/4`, and `0<=M<=a/2`. Strict compilation and axiom guards
  use no new axioms or `sorry`. Operator inequalities, functional calculus,
  creator convergence, and spectral flow are not formalized by these lemmas.

This completes a quasi-local realization of the selected actual Wilson
vacuum. It does not show that spectral flow equals the earlier ordered
unitary-generator product, or that its spatial tails are strictly
exponential. The GNS unitary is the map in Section 5.7; no implementing
unitary in the original free infinite tensor-product representation is
asserted.

The next concrete target is the full-operator activity estimate for the
**actual Wilson transfer and its local sources after vacuum transport**:
construct vacuum-annihilating transported interactions and prove the
summability/decay bound required by
`G18_EXCITED_WINDOW_OPERATOR_BRIDGE_20260904.md`, Section 5, or prove an
adequate variant of that bridge for the decay supplied by spectral flow.
The existing bridge uses its explicit small activity condition, including
`eta<=1/400`; the parent gap alone does not establish it. Complete excited
Riesz-range totality, source transport, and sharp-shell Wilson/Hamiltonian
matching follow only after their respective operator estimates are proved.
