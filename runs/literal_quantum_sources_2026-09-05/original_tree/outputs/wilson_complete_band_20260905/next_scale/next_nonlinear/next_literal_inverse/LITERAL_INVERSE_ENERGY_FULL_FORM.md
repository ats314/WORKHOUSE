# From exact-vacuum spectral leakage to a full Hamiltonian bound

5 September 2026. Analytic addendum to the unchanged literal and common-Gauss
source derivations. This strengthens their actual additive conclusions from
restricted fast coercivity to a full form inequality. It adds no interacting
Hamiltonian or OS-history identification.

## 1. Pseudoinverse lemma with the true vacuum retained

Let h be a nonnegative self-adjoint operator with closed form, unique unit
vacuum Omega, and a strictly positive full gap on Omega-perp. Let Pi0 be its
vacuum projection. Let P be an orthogonal projection with P Omega=Omega,
and Q=I-P. Define G=h_+^-1 as the inverse on Omega-perp and zero on Omega.
It is bounded and nonnegative. If

    Q G Q <= gamma Q,             gamma>0,                (1)

then the entire form satisfies

    h >= gamma^-1 Q.                                     (2)

Proof: (1) gives ||G^(1/2)Q||<=sqrt(gamma), and the adjoint has the same
norm. For every psi in D(h^(1/2)), exact vacuum retention gives

    Q psi = Q(I-Pi0)psi = Q G^(1/2) h^(1/2)psi.

Taking norms proves (2). No commutation of P with h is assumed. This is a
full form statement, not the result of deleting a cross block. The equality
Q Pi0=0 is essential. Nor is preservation of D(h^(1/2)) by P needed merely
for this implication; the earlier source constructions separately supply
the restricted-form domains when their compressions are discussed.

More generally, the same proof works for any vacuum kernel if Q annihilates
that entire kernel and the inverse on its orthogonal complement is bounded.

## 2. The one-block and independent-copy literal source

Use the true-vacuum projection and the complete physical low spectrum from
`../next_literal/LITERAL_VACUUM_COARSE_PROJECTION.md`. Denote the first
physical energy by a>0, the next threshold by t>a, and the complete first
excited projection by Pi1. For one block Pi1 is rank one; for the independent
copies it is the full one-excitation span. The exact vacuum has energy zero.

The known spectral decomposition gives

    h >= a Pi1+t(I-Pi0-Pi1),
    G <= a^-1 Pi1+t^-1(I-Pi0-Pi1).                       (3)

If ||Q Pi1||=delta, with 0<=delta<1, then (3) and Q Pi0=0 imply

    QGQ <= [1/t+(1/a-1/t)delta^2]Q.

Consequently the full Hamiltonian bound is

    h >= c Q,
    c=[1/t+(1/a-1/t)delta^2]^-1.                         (4)

This is the inverse-energy analogue of the refined restricted-compression
floor f=t-(t-a)delta^2. Generally c<=f; the stronger applicability of the
full inequality costs a different constant. In fact

    f-c=(t-a)^2 delta^2(1-delta^2)/[a+(t-a)delta^2]>=0.   (5)

One cannot assign f itself to the full form without further information.

In the actual fixed-rank strip, a/sqrt(u) tends to 2sqrt(3),
t/sqrt(u) tends to sqrt(3)+sqrt(5), and delta tends to zero. The preceding
literal proof establishes exact vacuum inclusion and the complete low-space
leakage. Thus

    c(u)/sqrt(u) -> sqrt(3)+sqrt(5).                      (6)

For independent Gauss copies, exact excitation supports make the full
one-excitation leakage delta independent of copy count. Their known full
gap is a and the threshold is t once 2a>=t. Equations (3)--(6) therefore
hold uniformly for all finite copies and for their countable exact-vacuum
incomplete tensor product. The required positive full gap is an established
input of this additive spectral decomposition, not inferred circularly from
the new inequality.

## 3. One common Gauss constraint

Use the complete common-Gauss classification in
`../next_literal_common/COMMON_GAUSS_LITERAL_FAST_FLOOR.md`. Below
t=min(b,alpha+beta,3alpha), its physical low space consists of the true
vacuum, the radial states of energy a, and adjoint pair singlets of energy
2alpha. For sufficiently large u, max(a,2alpha)<t. Write their full
projections as R_rad and R_pair. The known full gap is min(a,2alpha).

The inverse spectral bound is

    G <= t^-1(I-Pi0)
       +(1/a-1/t)R_rad+(1/(2alpha)-1/t)R_pair.           (7)

The earlier exact-support proof gives radial leakage d_r^2 and pair leakage
d_pair^2=2d_A^2-d_A^4. The Q images of different radial/pair support vectors
are mutually orthogonal. Within every such support the displayed physical
low vector is unique. Thus the norm of the compressed inverse deficit is
the maximum, not the sum, of its two coefficients:

    gamma=1/t+max{(1/a-1/t)d_r^2,
                  (1/(2alpha)-1/t)(2d_A^2-d_A^4)},
    h >= gamma^-1 Q.                                    (8)

For one copy the pair term may be omitted; retaining it gives a valid weaker
bound. The exact support argument works for arbitrary superpositions and
for the countable l2 sums, without rank or copy-count factors. Since both
leakages tend to zero and t/sqrt(u) tends to sqrt(3)+sqrt(5), the full-form
coefficient in (8) has that same limit uniformly in copy count.

This statement is for additive blocks with their specified common residual
action. Interblock plaquettes or shared electric derivatives would change
the vacuum and exact spectral/support decomposition and are not included.

## 4. Entire low-window literal source frame

For either (4) or (8), let Pi_E=1_[0,E](h), with 0<=E<c, where c denotes
the corresponding full-form coefficient. Its entire spectral window obeys

    Pi_E Q Pi_E <= (E/c)Pi_E,
    Pi_E P Pi_E >= (1-E/c)Pi_E.                          (9)

If J is the actual literal source isometry onto ran P, then B=Pi_E J has
B B*>= (1-E/c)Pi_E. It is onto the whole window, and
B*(B B*)^-1 is a right inverse of norm at most (1-E/c)^-1/2. This includes
the true vacuum and remains valid at infinite rank. It uses the actual
quantum marginal source norm and a lower bound on B B*, not on B* B.

The prior exact low-window Gram formulas remain available and can be sharper
than (9). The new advantage is a single full-form mechanism with a directly
usable energy-window consequence.

## 5. Relation to the Gaussian theorem and exact negative control

The Gaussian proof first obtains a compressed inverse-frequency bound for
its exactly weighted coordinate source, and turns it into a full frequency
form before second quantization. Here the same inverse-norm factorization
acts directly on the actual additive quantum Hamiltonian, using its exact
true-vacuum source and established full low spectrum. Neither route discards
a noncommuting cross term.

The independent four-state control has

    h=diag(0,4,7,11),
    P=|e0><e0|+|v><v|,  v=(0,3/5,4/5,0),
    delta^2=16/25, a=4, t=7.

Its exact full coefficient is c=175/37, while the restricted-compression
floor is f=127/25. Direct rational PSD elimination verifies QGQ<=(37/175)Q
and h-(175/37)Q>=0. The latter is sharp on the vector (0,7,-3,0).
Replacing c by f makes the nonvacuum 2-by-2 principal determinant
-1296/625, so the full-form promotion of the compressed floor fails.

Rotating the retained vacuum line away from e0 also gives a negative
expectation on the actual vacuum for every claimed positive full coefficient.
This checks that exact vacuum inclusion is a mathematical premise of (1)--(2),
not a convenient choice of normalization.

## 6. Evidence and scope

`check_literal_inverse_energy.py` and its saved output verify the exact
four-state inverse cap, full PSD bound, saturation, compression distinction,
vacuum-inclusion negative control, and scalar constant identity (5).
These are finite controls. The full domain, spectral and countable-product
arguments are the analytic proof above plus the unchanged accepted inputs.

This addendum strengthens the existing literal/common results; it does not
create a new physical projection or require a new result node. It does not
identify the literal equal-time source range with all OS histories, supply
interacting Wilson score bounds, or prove a continuum limit.
