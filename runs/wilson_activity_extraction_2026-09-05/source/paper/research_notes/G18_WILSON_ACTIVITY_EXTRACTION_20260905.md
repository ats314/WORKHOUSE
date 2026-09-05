# Exact connected activities for the vacuum-dressed Wilson transfer

5 September 2026. Additive continuation from the byte-pinned creator-parent
and spectral-flow theorem. This note proves existence and exact algebraic
properties of the actual transfer activities. Their required weighted norm
remains the next quantitative target.

## 1. Statement and established inputs

The [creator-parent theorem](G18_WILSON_CREATOR_PARENT_AND_SPECTRAL_FLOW_20260905.md)
supplies an exact finite-volume unitary taking the product vacuum to the
actual symmetric Wilson Perron line. It uses a common spectral filter and
a dimension-independent parent gap. The
[excited-window bridge](G18_EXCITED_WINDOW_OPERATOR_BRIDGE_20260904.md),
Section 5, requires a disjoint-support expansion of that dressed transfer,
with self-adjoint activities annihilating their local vacua.

Such activities now have an exact construction. Apply partition
Möbius inversion to the dressed transfers of all induced finite link
subsystems, each with its own parent unitary and Perron normalization.
The resulting activities are bounded, self-adjoint, locally
vacuum-annihilating, and zero on disconnected induced plaquette supports.
They reconstruct the actual dressed transfer in every finite subsystem.
No restriction identity between different subsystem unitaries is assumed.

The construction uses only real-coupling finite-volume component
factorization. It requires no multivariate analytic continuation of the
spectral-flow unitary and gives no uniform bound on the activity norms.

## 2. A finite-family partition extraction lemma

Let `Lambda` be a finite set of links, with arbitrary link Hilbert spaces,
unit product vacua `Omega_X`, and `P_X=|Omega_X><Omega_X|`. For every
`X subset Lambda`, specify a bounded self-adjoint operator `G_X` on the
corresponding tensor factor, with

```text
G_empty=1,  G_{i}=D_i,  G_X Omega_X=Omega_X.
```

The free `D_i` are bounded and self-adjoint. No partial-trace consistency
between `G_X` and `G_Y` is required. Operators are embedded in larger
tensor factors by the identity outside their named support.

For every nonempty `X`, let `Pi(X)` be its set of unordered set partitions
and define

```text
C_X = sum_(pi in Pi(X)) (-1)^(|pi|-1)(|pi|-1)!
                         tensor_(B in pi) G_B,
F_{i}=0,  F_X=C_X for |X|>=2.                         (1)
```

Then all activities are bounded and self-adjoint, and

```text
F_X P_X=P_X F_X=0.                                  (2)
```

For every `Gamma subset Lambda` they obey the exact expansion

```text
G_Gamma = sum_(A a family of pairwise disjoint subsets X of Gamma, |X|>=2)
            (tensor_(X in A) F_X)
              tensor (tensor_(i in Gamma outside union A) D_i).   (3)
```

The empty family contributes the full free product. The activities are
unique among families with `F_{i}=0` satisfying (3) on all subsystems.

### Proof of inversion and the operator ordering

Introduce central commuting formal variables `z_i` with `z_i^2=0`, and
write `z_X=product_(i in X) z_i`. In the finite support algebra put

```text
Z=1+sum_(nonempty X subset Lambda) G_X z_X.
```

The nonconstant ideal is nilpotent. Products with overlapping supports
vanish because some variable is squared. Surviving products have
disjoint operator supports and therefore commute. Thus this
support-respecting subalgebra is commutative even though its overlapping
operator coefficients generally do not commute.

The coefficient of `z_X` in the finite polynomial `log Z` is `C_X`:
a partition into `k` blocks occurs `k!` times in `(Z-1)^k`, and the
logarithm contributes `(-1)^(k-1)/k`. The identity
`Z=exp(sum_X C_X z_X)` now yields the usual partition inversion.
Since `C_{i}=D_i`, separating its singleton blocks gives (3). Equally,
`F_Gamma` is the only term on the right of (3) not determined by proper
subsets, so induction proves uniqueness.

Each term in (1) is a tensor product of self-adjoint operators, hence
`C_X` is self-adjoint. Every such tensor product fixes its product vacuum.
On the invariant ambient vacuum line,

```text
Z Omega_Lambda = product_i(1+z_i) Omega_Lambda,
(log Z) Omega_Lambda = (sum_i z_i) Omega_Lambda.
```

Therefore `C_X Omega_X=0` when `|X|>=2`. Self-adjointness proves
annihilation from the left as well, giving (2). The singleton activities
are zero by definition. No positivity of an individual `F_X` is asserted.

### Component cancellation

Suppose `X=A disjoint-union B`, with both parts nonempty, and for every
`S subset X` the induced family satisfies

```text
G_S = G_(S intersection A) tensor G_(S intersection B).           (4)
```

Then `Z_X=Z_A Z_B`, and these factors commute. Consequently
`log Z_X=log Z_A+log Z_B`, so the coefficient with support meeting both
parts is zero. In particular `F_X=0`. This is an identity at the chosen
real coupling, not a perturbative cancellation inferred from samples.

## 3. Application to the actual induced Wilson family

Fix the real-coupling domain `|u|<=u_star/8` and the stronger input weight
of the creator-parent theorem. Fix one temporal mesh `tau` and one
positive integer block power `m` for the entire family.

For every finite link set `X`, retain exactly those plaquettes whose full
four-link supports lie in `X`, and define

```text
T_X=exp(tau u V_X/2) exp(-tau K_X) exp(tau u V_X/2),
B_X=T_X^m,  b_X=the Perron eigenvalue of B_X,
G_X=b_X^(-1) U_X^* B_X U_X.                         (5)
```

Here `K_X` is the same additive free kinetic operator on the retained
links. The unitaries `U_X` are the actual creator-parent spectral flows
along the same coupling path, with one common filter, one cutoff below
`247/256`, and `U_X(0)=I` on every subsystem. These conventions fix the
operator family, including its phases and component factorization.

Deleting plaquettes preserves four distinct links per plaquette, the
maximum incidence of four plaquettes at a link, the magnetic norm bound,
and the additive kinetic gap. Thus every induced model meets the
finite-volume creator-parent hypotheses. The stated positive Wilson
kernel identifies its actual Perron branch. Hence `G_X` is bounded,
positive and self-adjoint and satisfies `G_X Omega_X=Omega_X`.

On a singleton there is no magnetic plaquette. Its creators vanish and
its parent path is constant, so `U_i=I`, `b_i=1`, and

```text
G_i=exp(-m tau K_i)=D_i.                             (6)
```

For a disconnected induced plaquette hypergraph, split its vertex set
into nonempty parts `A,B` with no retained plaquette crossing the split.
All smaller induced transfers and their Perron eigenvalues factor over
the same split. The normalized actual vacuum vectors tensorize, so
their unique creator logarithms are sums of the component families.
Their parents consequently have the form `H_A tensor I + I tensor H_B`.

The common-filter spectral-flow generator is a linear filtered integral
of the evolved derivative of this parent. Evolving a derivative term
from `A` under `H_A+H_B` is its evolution under `H_A`, with identity on
`B`; the same holds for the other component. The generator is therefore
the sum of the two component generators. Uniqueness of its bounded
unitary differential equation with initial value `I` proves

```text
U_X=U_A tensor U_B.
```

This is an exact operator identity. It is stronger than equality of the
transported vacuum lines and leaves no arbitrary relative phase. The
argument also applies to every `S subset X`, establishing (4).

The lemma now constructs the actual activities in (3). A nonzero
activity support of size at least two must be a connected union of
retained plaquettes. An isolated link is a separate component and would
force cancellation. In particular no support of size two or three
carries an activity when plaquettes have four distinct links.

Everything in this application is finite tensor algebra on the actual
open or periodic induced geometry. `U_Y` need not be the operator
restriction of `U_X`, and `G_Y` need not be a partial trace or compression
of `G_X`. The family (5), rather than such a false consistency property,
is what defines (1).

## 4. The remaining cardinality norm and its spatial consequence

At the spectral block of the excited-window bridge the free kernels
have `D_i=P_i+d_i`, with `0<=d_i<=delta(1-P_i)` and `delta=4/5`.
The exact expansion and local vacuum-annihilation hypotheses of its
Theorem 5 are now supplied by (1)-(6). Its remaining basic assumption is

```text
eta(u)=sup_(Lambda,tau,i) sum_(X subset Lambda, i in X)
                              (5/4)^|X| ||F_X(u)|| <= 1/400.     (7)
```

This is a support-cardinality norm. Quasi-local diameter bounds on the
spectral-flow automorphism do not alone imply (7): a ball of radius `R`
in three dimensions has cardinality of order `R^3`. Even decay such as
`exp(-R/log(R+2)^2)` does not absorb `exp(c R^3)`. This observation
separates the two norms; it does not disprove (7) for the actual Wilson
activities.

Connected support gives a useful implication in the other direction.
Use the link graph in which links are adjacent when one retained
plaquette contains both. Every surviving `X` is connected in that graph,
so its diameter is at most `|X|-1`. Consequently (7), if proved, controls
the bare spatial activity sum

```text
sup_i sum_(X contains i) exp(kappa diameter(X)) ||F_X|| <= eta,
0<=kappa<=log(5/4).                                 (8)
```

For periodic systems these are intrinsic graph diameters. Formula (8)
does not provide an additional spatial weight while retaining the entire
factor `(5/4)^|X|`. A stronger target with a cardinality margin is

```text
eta_epsilon(u)=sup_(Lambda,tau,i) sum_(X subset Lambda, i in X)
             exp((log(5/4)+epsilon)|X|) ||F_X(u)|| <= 1/400,
epsilon>0.                                         (9)
```

It implies both (7) and the combined bound with weight
`(5/4)^|X| exp(epsilon diameter(X))`. The required source-transformation
norm remains separate, even if (9) is obtained.

## 5. Next calculation and evidence boundary

The next target is a common estimate such as `eta_epsilon(u)<=C|u|` on
an explicit nonzero interval, with `C|u|<=1/400`. The finite-family
definition (1) makes the object to be estimated concrete. One-plaquette
and overlapping-pair full-operator coefficients are bounded starting
calculations; scalar vacuum matrix elements cannot replace their
operator norms. Every subsystem must retain its own Perron normalization
and common-filter parent unitary during the subtraction.

At `u=0`, all `G_X` are free products, so every activity in (1) is zero.
For any fixed finite `X` its construction is bounded and exact. Neither
fact controls the sum over all supports: the partition formula itself
contains rapidly growing combinatorial coefficients whose cancellations
still require a uniform estimate.

The lemma and its Wilson application were derived and checked
independently using the support algebra and exact component factorization.
They use the already pinned parent theorem as an input and do not alter
that theorem or its run. The independent finite controls in
`runs/wilson_activity_extraction_2026-09-05` retain overlapping noncommuting
two-link operators. One implementation compares partition inversion with
disjoint-family reconstruction; another uses ordered positive transfer
products and a root-block recurrence which does not enumerate partitions.
A positive vacuum-fixing family without component factorization has
disconnected cumulant `diag(0,0,0,1/12)`, testing the necessity of the
separate factorization hypothesis. These are exact finite tensor controls,
not calculations of Wilson rotor activities or their uniform norms.
No new Lean theorem or machine certification of
the full activity norm is asserted. Until (7), or a proved sufficient
replacement, and the needed source bounds are established, the complete
Wilson excited Riesz-range and sharp-shell matching tasks remain open.
