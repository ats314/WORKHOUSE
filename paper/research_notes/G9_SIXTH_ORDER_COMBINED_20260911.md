# G9: combined sixth-order support and an unavoidable carrier shape

11 September 2026. Canonical source base: `fa1bbadddd52955cb6517a0d7af5b59c086c40df`.
This continues the merged RUR census while keeping its mathematical and dynamical
claims separate. The original note is preserved unchanged; the original script
and tests are byte-preserved in the [run](../../runs/g9_sixth_combined_2026-09-11/README.md).

## 1. What the census establishes

The walk enumeration gives 90 closed rooted four-step unit-edge walks: 66 have
immediate retracing and 24 are planar squares. At six steps there are 192
non-retracing walks using all three axes. These are edge walks, not ordered
plaquette insertions with electric states, Haar weights, projectors and folds.
No map from those 192 walks to weighted RUR histories was provided. In particular,
the census supplies no net coefficient of RUR, RR, q e2 or e3 in H6.

The old amplitude formula was assigned directly, not derived from the enumerated
walks. Its numerical positivity is not a check of that missing identification.
The old carrier function also assigned sigma(R)=0 and sigma(U)=q, whereas the
actual unnormalized symbols are -2 e2 and q^2. It returned a nonzero expression
for the claimed zero defect and separately set a Boolean to true. The revised
script computes the symbols and tests the defect itself. Its old amplitude API
now raises an explicit missing-dynamics error. This does not falsify a possible
physical RUR coefficient; it withdraws the claimed derivation of one.

Our conventions, from the actual Laurent operators in `kernel_orbits.py`, are

    a_j = 2-z_j-z_j^-1,  q = sum a_j,
    e2 = a1*a2+a1*a3+a2*a3, e3 = a1*a2*a3,
    psi*psi = q, U = psi psi*, P_c = U/q, Q_c = I-P_c,
    S = L_down-4I, R = the cross-plane part of S.

These e2,e3 are Bloch invariants, not representation Casimirs. U is the
up-Laplacian, not its normalized projector. Its kernel is the complementary
plane, not the carrier line. Cleared identities hold at q=0; normalized carrier
formulas below require q>0.

## 2. Complete formal sixth-order folds

Let P_E be the isolated electric model-space projector, D=Q_E/(E0-H0), and
V0 the original self-adjoint perturbation. If P_E V0 P_E=a P_E, set V=V0-aI
on the entire Hilbert space. Then P_E V P_E=0. It is essential to shift the
complementary block as well. In the one-face odd SU(3) calculation a=1;
in the vacuum calculation a=0. This is an electric projection, distinct
from the momentum-dependent carrier projection P_c inside the model space.

Put chi_0=P_E. Intermediate normalization gives the exact recursions

    K_n = P_E V chi_(n-1),
    chi_n = D V chi_(n-1) - D sum_(j=1..n-1) chi_(n-j) K_j.

Indeed, inserting H0(P_E+chi)+gV(P_E+chi)=(P_E+chi)(E0+K)
into its P_E and Q_E components gives these equations. No odd order is dropped.
With M=P_E+chi*chi, the canonical Hermitian effective operator is
M^(1/2) K M^(-1/2). Expanding the binomial series gives the following compact
sixth-order formula. Define

    A_m = P_E V (D V)^(m-1) P_E,
    B_m = sum of A_m with exactly one of its (m-1) D slots replaced by D^2,
    C_2 = P_E V D^3 V P_E.

The code stores the raw words and combines equal terms exactly. Then

    H6 = A6 - {A4,B2}/2 - {A3,B3}/2 - {A2,B4}/2
            + {A2^2,C2}/2 + 3{A2,B2^2}/8 + B2 A2 B2/4.       (F6)

The anticommutator is XY+YX. Expanding (F6) gives exactly 18 words in
P_E,V,D. The term involving A3,B3 is present: dropping odd electric histories
would give an incomplete formula. The JSON report lists every word with its
rational coefficient. The same recursion reproduces the established
H4=A4-{A2,B2}/2. Independent rational matrix checks verify both the invariant
subspace equation and normalization through degree six with a rank-two P_E
and noncommuting effective coefficients.

(F6) is the full universal folded operator support in this scalar-first-order
convention. It does not evaluate its Wilson plaquette matrix elements, prove a
specific SUR support, or carry out connected multi-plaquette rooted subtraction.
Those require the actual electric/Haar implementation on each support. The
one-face evaluation below supplies a complete physical test case.

## 3. Exact Hodge word reduction

In a polynomial carrier gauge let a=(a1,a2,a3), psi=1, with left carrier a^T.
Then U=1 a^T, S=(q-4)I-U and R=diag(a)-U. The scalar a^T W 1 is polynomial
and symmetric in the a_j. Exact symmetrization gives sigma(W) in Q[q,e2,e3].
This gauge is used to compute, not infer, the following table. All 40 words
of lengths zero through three also agree coefficient by coefficient with the
independently implemented spatial Laurent operators.

| Word | Cleared symbol sigma(W) |
| --- | --- |
| I | q |
| U | q^2 |
| S, S^2 | -4q, 16q |
| R | -2e2 |
| UR, RU | -2q e2 |
| RR | q e2+3e3 |
| RUR | 4e2^2 |
| RSR | (q-4)(q e2+3e3)-4e2^2 |
| RRR | -2e2^2-2q e3 |
| URR, RRU | q^2 e2+3q e3 |

For example sigma(RUR+2 RRR)=-4q e3: both individual words contain e2^2,
but this sum does not. A word census must therefore retain coefficients and
combine them before testing shape membership. Even support is not unique
modulo operator identities; the complete carrier polynomial is the invariant
object being tested. The script's `reduce_support` accepts exact weighted words
and returns their sum. Missing direct H6 input is represented as unknown, not zero.

## 4. All dynamics terms in the sixth-order band coefficient

Use the same local, orthonormal electric-shell convention as the assembled H4.
At fixed nonzero momentum, remove scalar anchors and write

    H_eff(u) = u^2 t3 q Q_c + u^3 H3 + u^4 H4 + u^5 H5 + u^6 H6 + O(u^7).

The recorded SU(3) third-order factorization is H3=b3 L_down modulo a scalar
(`MASTER_THEORY_UNIFIED_2026-08-20_v4_3.md`, section 4.3), so Q_c H3 P_c=0.
For the scalar carrier branch, expand the Schur complement of H_eff/u^2.
The off-diagonal block first appears at order u^2, from H4. Consequently its
order-u^4 contribution is H4-Q_c-H4 with leading inverse (t3 q)^-1.
H5 first couples to H4 at order u^5 in the scaled operator (order u^7 in H_eff).
The u H3 correction to the complementary inverse also starts at order u^7.
Unknown off-diagonal H6 contributes still later. Thus the complete order-six
coefficient, with all direct electric folds already included in H6, is

    lambda6 = sigma(H6)/q - [q sigma(H4^2)-sigma(H4)^2]/(t3 q^3).      (S6)

Any scalar vacuum subtraction is part of H6 and causes no change to this
argument. This is not an assumption that H5 vanishes. If H3 had carrier-complement
coupling, (S6) would not be the complete formula; its recorded decoupling is
an explicit input.

The actual H4 support is {I,U,S,S^2,R}, with R coefficient -2C. Evaluating every
one of the 25 ordered pairs, including their projected subtraction, gives zero
for 24 pairs. Only the RR pair remains. This agrees independently with direct
composition of the full assembled spatial kernel. Define

    kappa = 4 C^2/t3
          = 169924002729806205028788409 / 619343593697933825385600000 > 0,
    t3 = 5/612.

Then the known dynamical mixing support is

    -(kappa/q) RR + (kappa/q^2) RUR,

where these are effective carrier operators, with rational q coefficients from
the in-shell resolvent. Their normalized expectation is

    lambda6_mix = -kappa*(e2/q + 3e3/q^2 - 4e2^2/q^3).

The RUR here comes from inserting P_c=U/q in the projected subtraction. It is
not evidence that a direct six-insertion electric history has local word RUR.
The ratio 1:3:-4 belongs to this complete mixing term, not necessarily to the
full coefficient including sigma(H6)/q.

## 5. Noncancellation after every local direct term is included

Assume the order-six electric-shell effective operator is a finite-range,
translation-covariant stencil (or has Laurent-polynomial entries) in this same
basis. Write F=sigma(H6). Finite-order linked-cluster assembly has this form
when its electric denominators and support subtractions are evaluated before
selecting the dispersive carrier. No in-shell 1/q resolvent is included again
in F. The remaining calculation is precisely this local F.

Equation (S6) gives

    q^3 lambda6 = q^2 F - kappa*(q^2 e2 + 3q e3 - 4e2^2).          (N6)

For every symmetric polynomial F, its remainder modulo q^2 is exactly

    4 kappa e2^2 - 3 kappa q e3.                                 (R6)

Thus the canonical rational remainder contains BOTH e3/q^2 and e2^2/q^3.
The e2/q term can be canceled by a direct F=kappa e2, for example the
local H6=-(kappa/2)R. The 1:3:-4 ratio is therefore not a constraint on all
sixth-order shapes. A direct h RUR contributes 4h e2^2/q and cannot cancel
the e2^2/q^3 component.

The strongest noncancellation conclusion does not even require F to be
symmetric. For any Laurent-polynomial F, (N6) modulo q equals 4 kappa e2^2.
To prove q does not divide this expression in the actual Laurent ring, take

    z1=z2=-1, z3=5+2 sqrt(6).

Every z is nonzero, a=(4,4,-8), q=0 and e2=-48. The numerator is 9216 kappa,
not zero. A divisible Laurent polynomial would vanish at this point.
Therefore q^3 lambda6 is not divisible by q, whatever the local direct H6 is.
In particular lambda6 cannot lie in the old shape span
{1,q,e2,4e2/q,e3/q}, nor can local direct RUR terms remove the extra rational
shape. Equality on the whole real punctured Bloch zone would be a Laurent
identity after clearing denominators and is excluded by this witness.

This is an algebraic divisor argument on the complexified momentum torus,
not a physical singularity: for real k approaching Gamma, a_j=O(|k|^2) and
lambda6_mix=O(q). The normalized carrier remains undefined at Gamma itself.
On a single finite momentum mesh one can interpolate functions differently;
the claim concerns the shared local stencil over the whole Bloch zone, not
an arbitrary volume-dependent interpolant. No convergence or continuum claim follows.

## 6. Complete one-face SU(3) dynamical check

On one square, Haar-orthonormal irreducible characters chi_(p,q) give

    H0 chi_(p,q) = 2 C2(p,q) chi_(p,q),
    C2(p,q)=(p^2+pq+q^2+3p+3q)/3,
    V0=-(chi_(1,0)+chi_(0,1)).

Multiplication uses the exact fundamental and conjugate fusion rules with
negative Dynkin labels omitted. In the odd sector use
(chi_(p,q)-chi_(q,p))/sqrt(2), p>q. Self-conjugate representations vanish;
reversed pairs contribute the exact minus sign. The lowest odd state is (1,0),
E0=8/3; the vacuum is (0,0), E0=0. The recursion generates every reached
representation, applies (E0-H0)^-1 only away from the target, and retains the
normalization/energy subtraction at every order. Orthogonality of characters
is the exact Haar/Gram quotient, not a numerical nullspace approximation.

| coefficient | odd level | vacuum | vacuum-subtracted gap |
| --- | --- | --- | --- |
| u^0 | 8/3 | 0 | 8/3 |
| u^1 | 1 | 0 | 1 |
| u^2 | -1/4 | -3/4 | 1/2 |
| u^3 | -1/16 | -9/32 | 7/32 |
| u^4 | -13/896 | -39/1280 | 143/8960 |
| u^5 | -23/12544 | 693/10240 | -34877/501760 |
| u^6 | 407/702464 | 6051/102400 | -2055143/35123200 |

The JSON retains the representation support at every order. An independent
matrix construction from fusion adjacency evaluates all 18 words of (F6)
and reproduces both sixth-order energies exactly, using V=V0-aI with the
appropriate first-order scalar. Three interaction steps from each target
contain every intermediate representation of a closed six-step history;
the test therefore does not omit a returning sixth-order path.

This is the complete one-face rooted contribution. Its translational on-site
extension is scalar in orientation and has no q e2/e3 or additional RUR shape.
It supplies one physical cluster and a normalization test. It is not the
nonplanar connected cluster requested by the open G9 route, and it is not the
global m6 coefficient. Multi-face Haar contractions remain to be evaluated.

## 7. Reproduction and graph consequence

Run from the canonical checkout with its own environment:

```text
python scripts/g9_sixth_order_rur_census.py
python scripts/g9_sixth_order_rur_census.py --json --out NEW_REPORT.json
pytest -q tests/test_sixth_order.py tests/test_g9_rur_dynamics.py
workhouse verify --only G9
```

The output path must be new. The registered checks are exact T1 calculations
at their stated scopes; no new Lean statement is claimed.

The folded-support and one-face obligations are discharged. The full band
coefficient has a provably surviving additional rational shape under the
recorded H3 factorization and local-shell assumptions. This rules out total
cancellation back into the old five-shape ansatz. It does not determine the
coefficients of q e2/e3 in the direct cleared F, or decide whether a direct
local RUR word survives its own connected assembly. The next G9 step is to
evaluate (F6) on the smallest connected multi-plane plaquette supports, retain
all exact Haar/projector/denominator weights and rooted subtractions, and
reduce the resulting F. That calculation will supply its polynomial shapes;
it cannot remove the remainder (R6). G9 remains open, and this finite-order
spectral result supplies no additional continuum mass-gap conclusion.
