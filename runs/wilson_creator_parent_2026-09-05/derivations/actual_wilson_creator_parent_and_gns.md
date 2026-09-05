# Actual Wilson creators, spatial locality, and a parent GNS realization

Research draft, 5 September 2026. This draft uses the rooted contraction and
coefficient-limit notes already on main at `ac397045`. The finite parent-gap
lemma mentioned below is the independently developed companion calculation;
the present draft supplies endpoint restoration, locality, interaction bounds,
and the physical-state implication.

## 1. Restoring the actual symmetric vacuum

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

## 2. Connected witnesses survive endpoint restoration

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

### Spatial weight and moments

For a nonempty finite link support `X`, let `c(X)` be the minimum number of
plaquettes in a connected plaquette family whose footprint contains `X`.
Connectivity means adjacency by a shared link. On the infinite cubic lattice
this is finite; a coefficient with degree `n` vanishes unless `c(X)<=n`.
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

## 3. A bounded-interaction parent for the actual vacuum

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
to obtain a self-adjoint interaction `Phi`. Its rooted interaction norm
obeys

```text
||H_parent-N||_(nu,kappa)
 := sup_ell sum_(Z contains ell) exp(nu |Z|+kappa c(Z)) ||Phi_Z||
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

### Finite-volume gap input from the companion argument

The independently derived orthogonal-block parent estimate is

```text
gap(H_parent) >= 1-K_1-M_1^2,
K_1=sup_i sum_(X contains i) (|X|-1)||w_X||,
M_1=sup_i sum_(X contains i) |X|||w_X||.
```

The root bound at `log(2)` implies
`K_1<=a/4`, `M_1<=a/2`, because
`(m-1)/2^m<=1/4` and `m/2^m<=1/2`. Thus that companion lemma gives

```text
gap(H_parent) >= 1-a/4-a^2/4 = 247/256.
```

The proof of the finite gap estimate belongs with the companion derivation;
the GNS conclusion below is conditional on that lemma, and otherwise still
gives a positive parent form and its exact annihilator state.

## 4. What this establishes in the physical infinite-volume state

Take real `u` in the intersection of the creator domain and the source
expansion domain `|u|<u_c` of
`G19_DISCRETE_TIME_VACUUM_AND_WINDOW_20260904.md`, equation (15). If an
explicit positive spatial interaction weight is wanted, also impose the
smaller disk from Section 2. Use an exhaustion covered by that source-limit
theorem and the creator coefficient-locality statement.

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

The existing discrete-time vacuum theorem, Section 5, identifies the
finite-volume zero-temperature state with precisely the same Perron vector
state and proves the common thermodynamic limit of all bounded local
multiplication-source correlations. Therefore all the subnet states above
restrict to that established Wilson equal-time multiplication-source state.
Their equal-time multiplication GNS cyclic subspaces are canonically
isometric: inner products of `A Omega` and `B Omega` agree because
`omega(A^dagger B)` agrees. The extension to every bounded local quantum
operator, and identification of the full Euclidean transfer representation,
are not uniqueness statements proved by this observation.

### A gapped parent operator in each such GNS representation

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
extension, including its gauge-invariant subspace. It does not prove that
different extensions coincide, or identify this auxiliary operator with
the Wilson transfer generator.

## 5. Consequence and remaining bridge

The endpoint coordinate has now been converted to the actual symmetric
Wilson creator family with a uniform `1/8` bound, connected-witness spatial
decay, exact quasi-local annihilators, and a bounded-interaction parent.
The established scalar Wilson limit anchors its physical multiplication
sector. With the companion finite gap lemma, every full quantum subnet
realization has a uniformly gapped parent operator.

What still requires an argument is a controlled local unitary or equivalent
metric that transports the actual Wilson transfer and its local sources
into a chart with the operator-activity bound required by
`G18_EXCITED_WINDOW_OPERATOR_BRIDGE_20260904.md`, Section 5. Sharing a vacuum
and having an auxiliary parent gap does not make the two excitation spectra
equal. Complete excited Riesz-range totality, spatially weighted source
transport, and Wilson/Hamiltonian sharp-shell matching remain separate.

No spectral-flow theorem is invoked here, and no external theorem's
hypotheses are presumed to follow just from the rooted creator norm.
