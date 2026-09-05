# A uniform parent gap from exact-support creator coordinates

Independent analytic derivation, 5 September 2026. Draft for review.

## Statement and assumptions

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

## 1. Commuting nonorthogonal projections and the exact vacuum

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

## 2. Two exact orthogonal-block norm savings

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

## 3. Uniform row sum of off-diagonal commutators

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

## 4. The positive square identity

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
kappa<1. Section 1 identifies the zero space exactly.

## 5. Explicit rooted-weight corollaries

Suppose mu>=log(2) and the creator family obeys

    ||w||_mu := max_i sum_{X contains i} exp(mu |X|) b_X <= a.

For integers n>=1,

    n exp(-mu n) <= n/2^n <= 1/2,
    (n-1) exp(-mu n) <= (n-1)/2^n <= 1/4.

The respective sharp maxima at mu=log(2) occur at n=1,2 and n=2,3.
Consequently

    M1 <= a/2,     K1 <= a/4,
    gap(H) >= 1-a/4-a^2/4,                            (7)

whenever the displayed lower bound is positive. Two useful cases are

    a<=1/4  ==> gap(H)>=59/64,
    a<=1/8  ==> gap(H)>=247/256.

These corollaries apply to any exact-support creator family satisfying
the stated weighted bound. Obtaining the relevant a and mu for the
actual symmetric Wilson vacuum is an input to this theorem, not assumed
to follow merely by changing coordinates without a norm estimate.

## Scope and evidence

The proof is finite-volume Hilbert-space analysis and exact bounded-operator
algebra. It permits infinite-dimensional link factors and complex creator
vectors. H always uses the actual Hilbert-space adjoint, so H remains
positive even for a complex-coupling creator family, although that does not
assert holomorphic dependence of H on complex coupling. Holomorphy of the
coordinates and uniform control of the gap are distinct properties.

The finite-volume similarity is used only to compute the common kernel.
No global infinite-volume exponential, condition-number estimate,
thermodynamic GNS realization, or identification with the physical Wilson
excited operator is inferred here. Those consequences require their own
arguments from these local coordinates and bounds.
