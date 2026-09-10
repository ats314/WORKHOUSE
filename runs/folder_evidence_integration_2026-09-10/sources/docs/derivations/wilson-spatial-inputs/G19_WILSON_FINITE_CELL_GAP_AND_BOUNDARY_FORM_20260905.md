# The physical Wilson gap on a finite cell complex and its boundary form

5 September 2026. Analytic derivation continuing the physical scale-block package. The target is to replace a special two-square calculation by
a theorem for actual coupled Wilson cells, and identify the precise growing-
block constants needed for a scale comparison. 

## 1. Existing inputs, provenance and the new statement

G19 retains the actual history and physical scale comparison, alongside
the closed raw averaging/diffusion shortcut. The fixed-cell theorem below
uses the established physical quotient and localization mechanisms, with
their sources named explicitly.

The Hessian mechanism is established older work. The recovered
`EXTRACT_02_Wilson_Hessian_Discrete_Curl.md`, dated 29 December 2025, derives
the Wilson Hessian as `2 c_W d1* d1` and separates gradients and harmonic
one-cochains from coexact modes. Its graph inventory digest is
`ab2c9981fecceba6d4c4ed88ac6e9df8936908d3a7bbf2317acfbe0a24a8983b`, matching
the recovered bytes at
`C:/WORKHOUSE/09_ARCHIVE/sorted_second_pass/EXTRACT_02_Wilson_Hessian_Discrete_Curl.md`.
The exact Bloch identity `B B*=qI-d conjugate(d)^T` is also already a passing
G14 check. The Hessian itself is not claimed as a discovery here.

The new implication is a full finite-complex physical spectral theorem:
the original-link electric form determines the correct transverse metric,
the curl singular values determine oscillator frequencies, and diagonal
Gauss removes every one-quantum state. A generic first-order odd Taylor
term need not vanish as an operator, but has zero matrix on the ground and
first physical cluster; finite Hermite correctors improve their actual
eigenvalue errors to order one. An exact discrete IMS formula then exposes
the boundary cost and the need to retain slow curl modes as the block grows.

Canonical inputs from the completed package are:

- `paper/research_notes/G19_WILSON_TWO_SQUARE_PHYSICAL_SHELLS_20260905.md`,
  original-link quotient, invariant oscillator and compact localization;
- `paper/research_notes/G19_WILSON_STRIP_BO_AND_TWO_STRIP_SPLITTING_20260905.md`,
  finite Hermite correctors and physical cluster counting;
- `paper/research_notes/G19_WILSON_PHYSICAL_FIBER_FAST_GAP_20260905.md`,
  faithful character normalization and compact unique-well localization;
- `paper/research_notes/G19_OS_BLOCKING_AND_REVERSE_MASS_MATCHING_20260905.md`,
  the separate actual-history intertwiner/complement obligation.

## 2. Actual operator and explicit hypotheses

Let K be a finite connected oriented two-dimensional cell complex. Its
one-skeleton has vertices V, edges E, and closed oriented face words F.
Repeated edges in a face word are allowed if their signed occurrences are
retained. Write

```text
d0 : R^V -> R^E,             d1 : R^E -> R^F,
d1 d0=0,                    C=ker d0*,
r=dim C=|E|-|V|+1 > 0.
```

These spaces initially have the ordinary original-link Euclidean metric.
Let positive face weights form W=diag(w_f). Let G be compact connected with
simple Lie algebra g of dimension d, equipped with a fixed bi-invariant
metric. Let rho be a faithful finite-dimensional unitary representation and
define its positive trace constant by

```text
-Re Tr(d rho(X) d rho(Y)) = b_rho <X,Y>.
```

The actual gauge-invariant Hamiltonian is the Friedrichs realization of

```text
H_K(u) = -(1/2) sum_e Delta_e + 2u V_K(U),
V_K(U) = sum_f w_f [dim(rho)-Re chi_rho(U_boundary f)].       (1)
```

All vertex gauge transformations, including the root transformation, are
imposed. For the usual fundamental SU(N) representation and metric
`<X,Y>=-2 ReTr(XY)`, `b_rho=1/2`.

Two geometrical hypotheses are required:

1. Every connection with all face holonomies equal to I is vertex-gauge
   equivalent to the trivial connection. Equivalently its flat gauge-orbit
   space is a point. Simple connectedness of K is sufficient.
2. `B=W^(1/2) d1|C` is injective. Equivalently `H^1(K;R)=0`.

The second hypothesis is the directly computable local nondegeneracy
condition. The first rules out additional global minima. In particular a
positive Hessian on C alone is not a global uniqueness theorem: the one-
generator presentation with face word a² has `d1=[2]`, but SU(2) has the
distinct flat assignments a=I and a=-I. A faithful character vanishes only
when the face holonomy is I, not only in a neighborhood of I.

There are no unmentioned surrounding face interactions or fixed external
holonomies in (1). Those change the potential and its minima and must enter
an application explicitly. The group, representation, weights and entire
finite complex are fixed as u tends to infinity.

Let `0<sigma_1<=...<=sigma_r` be B's singular values, counting multiplicity,
and let m be the multiplicity of sigma_1. Define

```text
omega_j = sqrt(2 b_rho) sigma_j,
e0 = (d/2) sum_j omega_j,                 M=m(m+1)/2.        (2)
```

For physical eigenvalues, counting multiplicity, the theorem is

```text
E0(u) = e0 sqrt(u)+O_K,G,rho,W(1),
E_j(u) = [e0+2 omega_1]sqrt(u)+O_K,G,rho,W(1), 1<=j<=M,
gap_phys(u) = 2 sqrt(2 b_rho) sigma_1 sqrt(u)+O(1).         (3)
```

The first excited cluster has exactly M eigenvalues for sufficiently large
u. It can split at order one; multiplicity M refers to the cluster, not to
an asserted exact degeneracy. If m=1 it is an isolated simple eigenvalue.
There is a positive fixed-complex margin to the next physical cluster. A
lower margin available without classifying higher invariants is

```text
delta >= min(omega_1, omega_(m+1)-omega_1),                 (4)
```

where the absent second quantity is omitted if m=r. Formula (3) includes
all compact connected simple groups admitting the stated faithful rho, not
just SU(N). It is a finite-volume weak-field theorem, not a continuum gap.

## 3. Gauge-tree quotient without replacing the electric metric

Choose a root and a maximal tree. Integrating tree gauge variables gives
exact product Haar measure on the r non-tree based holonomies, with residual
simultaneous conjugation by G. This measure identity does not replace the
original-link kinetic form by r independent face Laplacians.

The reduced electric form is the sum of squares of the derivatives induced
by every original edge. Non-tree edges alone give all individual based
holonomy derivatives, and tree edges add nonnegative squares. Thus it is a
smooth uniformly elliptic form on compact G^r, preserving the residual
invariant subspace. It has compact resolvent. Its positive ground state is
unique and invariant, since the elliptic heat semigroup is positivity
improving and commutes with the group.

Here is the exact tangent calculation that removes dependence on the tree.
Let R be the r-by-|E| matrix whose rows are the oriented fundamental cycles
of the tree. If A is the original infinitesimal edge connection, tangent
based holonomies are y=RA. The infinitesimal electric cometric in y is

```text
C_tree=R R*.
```

Let Q have orthonormal columns spanning C. Then `T=RQ` is invertible and
`R R*=T T*`, because R vanishes on im d0. In the coordinates y=Tz, the
principal electric term is exactly `-(1/2)Delta_z`, with
`z in C tensor g`. The face linearization is `d1 Qz`. Indeed a tree-gauge
representative and Qz differ by a gradient and give the same d1. Thus the
tree cometric and face word Hessian combine to the invariant operator

```text
K_C = (d1 Q)* W (d1 Q),
H_quad(u) = -(1/2)Delta_z + b_rho u <z,K_C z>.             (5)
```

No graph-coordinate rescaling is chosen to make a desired bound true.
Formula (5) is the quotient of the original link metric. In particular the
two-square face matrix is `[[4,-1],[-1,4]]`, with singular frequencies
sqrt(3) and sqrt(5), recovering the actual strip result in its exact units.

The Hessian follows because
`v_rho(exp X)=(b_rho/2)|X|²+O(|X|⁴)` and
`log U_boundary f=(d1 A)_f+O(|A|²)`.
The composite Wilson potential can contain cubic terms; the fourth-order
remainder for a single exponential character does not remove BCH cubic
terms on an arbitrary cell complex.

## 4. The physical oscillator and the first-shell selection rule

Diagonalize K_C and rescale `z=u^(-1/4)x`. Its limiting oscillator is

```text
H0=sum_j[-(1/2)Delta_xj+b_rho sigma_j² |x_j|²],
Omega0 proportional to exp[-(1/2)sum_j omega_j |x_j|²].    (6)
```

Each mode x_j is an adjoint vector. A Hermite multi-degree has excitation
`sum_j n_j omega_j`. There is no invariant one-quantum vector because a
simple Lie algebra has no nonzero vector fixed by every adjoint action.

The invariant bilinear form on the compact simple adjoint is unique and
symmetric. For symmetric bilinear forms, a self-adjoint intertwiner has
invariant eigenspaces, hence ideals, so is scalar. An alternating invariant
form would give a skew-adjoint intertwiner J. Its square is a nonpositive
scalar by the same argument. If nonzero, `ad(JX)=J ad(X)` would imply the
Killing form satisfies `Kill(JX,JX)=-c² Kill(X,X)`, contradicting its strict
negative definiteness. Thus no additional alternating invariant is present.

Consequently the degree-two invariants among the m minimal modes are exactly

```text
(x_i.x_j - delta_ij d/(2 omega_1)) Omega0, 1<=i<=j<=m.     (7)
```

They are linearly independent and number M. Every other degree-two state
has excitation at least omega_1+omega_(m+1). Every state of degree at least
three has excitation at least 3 omega_1. This proves the first physical
cluster and (4), without claiming that cubic invariant tensors are absent.

## 5. Compact localization and the order-one remainder

Tree coordinates leave a smooth compact manifold G^r and a globally unique
potential minimum. Flatten its product Haar density in a fixed exponential
chart, using a group-invariant cutoff. A fixed invertible tangent map T
keeps conjugation linear. The electric cometric is positive and smooth;
the potential is positive off the minimum and has positive Hessian there.

First obtain only harmonic convergence and the exact cluster count. For
`h=u^(-1/2)`, apply IMS to `P_h=h² H_E+2V_K` with an inner ball of radius
`r_h=h^(1/3)`. Locally the metric and quadratic-potential errors have relative
size O(r_h), and the IMS term is O(h²/r_h²). Thus each fixed low physical
eigenvalue of P_h differs from its harmonic value h lambda by O(h^(4/3));
outside the inner ball the potential scale r_h² is much larger than h.
Upper bounds use compactly cut-off Gaussian Hermite vectors; lower bounds
use the local quadratic comparison and the outside potential bound. The
cutoffs and group averaging commute, so the same min-max comparison applies
on the physical subspace. It fixes the ranks one and M in disjoint harmonic
islands. This step alone would give only an O(u^(1/3)) unscaled error.

Now improve those two specific islands. Put `g=u^(-1/4)`, flatten Haar, and
rescale the chart. On every fixed polynomial times Omega0, with a cutoff
equal to one near the minimum, the actual differential operator has

```text
g² H_K(g^-4) = H0+g H1+O(g²).                            (8)
```

The last term has O(g²) L2 norm on these vectors. This follows by Taylor
expanding smooth coefficients: the unretained terms are bounded by a fixed
polynomial in x times the Gaussian. Cutoff commutators are exponentially
small in 1/g². No unbounded-energy operator-norm expansion is asserted.

H1 is an odd operator under simultaneous tangent inversion x->-x: its
second-derivative coefficients are linear, its corresponding first-
derivative coefficients constant, and its potential part cubic. A scalar
zero-order coefficient at this order, if written in a different smooth
half-density convention, is also odd. The ground and all vectors in (7)
are even. Thus, for each of their harmonic projectors P,

```text
P H1 P=0.                                                (9)
```

This is a projected parity identity. It does not say H1 vanishes on every
physical function, or that the full Wilson operator is inversion symmetric.

For a basis vector phi of either island, define the first corrector

```text
psi1=-(H0-lambda)^(-1) on (1-P)H_phys, applied to H1 phi.  (10)
```

H1 phi is an invariant odd polynomial times Omega0 with finite Hermite
degree. The inverse is only on the physical subspace; a nonphysical
one-quantum state could have a coincident numerical energy and is irrelevant.
There is no physical odd degree-one state, so every nonzero input component
has degree at least three. Its denominator is at least 3omega_1 for the
ground and at least omega_1 for the first excited cluster. Thus the inverse
in (10) acts on a finite collection of explicitly separated denominators.
The cut-off vector phi+g psi1 has residual O(g²) at energy lambda in (8).
Its Gram matrix is I+O(g²), since its cross-parity first-order term vanishes.

The spectral theorem then gives the required number of actual eigenvalues
within O(g²) of each harmonic island. The preceding harmonic rank count
excludes additional or missing eigenvalues in those islands. Multiplying
back by g^-2 proves (3). The constants involve the fixed chart derivatives,
Gaussian moments and the finite oscillator denominators. They are not
uniform merely because the leading Hessian formula is local.

## 6. A decisive growing-block example

For the filled open L-by-L square cell complex, embedded as a spatial patch,
`d1 d1*` on its L² faces is the Dirichlet square-grid matrix

```text
4I - adjacency_of_the_face_grid.
```

It is positive definite, and its eigenvectors are products of sines. Direct
substitution of `sin(pi j x/(L+1)) sin(pi k y/(L+1))` gives

```text
sigma_jk²=4-2cos(pi j/(L+1))-2cos(pi k/(L+1)),
sigma_min²=4-4cos(pi/(L+1)) ~ 2pi²/(L+1)².               (11)
```

The positive spectrum is the same as that of d1*d1 on C. Flat connections
are trivial on this contractible complex. Thus its actual physical gap has
leading coefficient

```text
2 sqrt(2 b_rho) sqrt(4-4cos(pi/(L+1))) sqrt(u).            (12)
```

For every fixed L this is a theorem with the error in (3). The coefficient
falls like 1/L; hence the general first physical block gap cannot have a
strictly positive coefficient independent of L. This does not take an
unjustified joint L,u limit: if a common positive coefficient and a common
u threshold existed, one could first choose L with its leading coefficient
smaller and then let u grow at that fixed L, contradicting (12).

This is the expected slow curl sector, rather than an obstruction to a
fast-mode scale comparison. It says which modes must be retained.

## 7. Exact boundary localization and the slow/fast quadratic split

Let `K=d1* W d1` on original edge cochains, before taking C. For scalar
cutoffs eta_a(e) with `sum_a eta_a(e)²=1`, the exact discrete IMS identity is

```text
sum_a <eta_a q,K eta_a q>-<q,Kq>
 = -(1/2)sum_(e,e') K_ee' <q_e,q_e'>
                    sum_a(eta_a(e)-eta_a(e'))².           (13)
```

Expand the left side and use
`sum_a eta_a(e)eta_a(e')-1=-(1/2)sum_a(eta_a(e)-eta_a(e'))²`.
There is no sign assumption on off-diagonal curl entries. In particular

```text
absolute error <= (1/2) max_e sum_e' |K_ee'|
                   sum_a(eta_a(e)-eta_a(e'))²  ||q||².    (14)
```

On complexes with uniformly bounded face perimeters, face/edge incidence,
weights and cutoff overlap, a cutoff varying on diameter L gives C/L² in
(14). This is a quantitative boundary-coupling identity for the actual
plaquette Hessian, not a decoupled-block assumption.

However eta_a q is generally not transverse even if q is. Let P_C be the
orthogonal projection off gradients. Then `d1 P_C=d1`, so transverse
projection leaves the curl energy unchanged, but can change the norm and
is nonlocal. A localized pure gradient can acquire nonzero curl. Consequently
one cannot combine (13) with a local transverse Poincare bound and silently
identify the projected local norms with the full norm. A uniform argument
requires a stable local Hodge decomposition with explicit retained coarse
pieces. The finite controls include a negative example of exactly this
localization issue.

For any orthogonal transverse split `C=C_s direct_sum C_f`, write K_C in
blocks. If `K_ff>=k_f² I`, its potential has the exact completion

```text
<z,K_C z> = <z_f+R z_s,K_ff(z_f+R z_s)>
                +<z_s,K_eff z_s>,
R=K_ff^-1 K_fs,   K_eff=K_ss-K_sf K_ff^-1 K_fs.           (15)
```

In coordinates x=z_s and y=z_f+Rz_s, the original quadratic kinetic form is

```text
(1/2)[||grad_x+R* grad_y||²+||grad_y||²].                 (16)
```

Equations (15)-(16) retain the full cross term. Dropping it is not justified
by the potential square or by an arbitrary change of metric. A spectral
split of K_C has R=0 and yields an exact harmonic tensor factorization;
this is the simplest reference for a genuine slow/fast comparison.

If the retained spectral modes have smallest frequency omega_s and the
discarded ones have smallest frequency omega_f, the full oscillator's
nonvacuum-fast complement has unrestricted gap omega_f. On the global
physical subspace its first excitation is
`min(2omega_f,omega_s+omega_f)` when both sectors are nonempty: one retained
and one discarded adjoint quantum make a singlet, as do two discarded
quanta. For the usual low/high spectral split `omega_s<=omega_f`, it is
omega_s+omega_f. It is 2omega_f if there is no retained mode. Thus a separate class-function
fiber factor two must not be imposed on a globally gauge-invariant coupled
block. This recovers the mixed-shell mechanism from the actual two-strip
calculation and agrees with the Gaussian history observability analysis.

Retaining all spectral modes below a fixed curl threshold sigma_* leaves
a harmonic fast lower energy at least
`sqrt(2b_rho) sigma_* sqrt(u)`. With `u=g_H^-4` and the physical conversion
`H_phys=c_H(a)g_H² H/a`, that is order `c_H(a)/a`. The assertion here is
exact for the harmonic factorization. Passing it to an actual block/history
complement requires the additional controls in the next section.

## 8. The uniform constants still needed, and the decisive successor

The finite-complex theorem turns the next scale question into explicit
quantities. For a growing or interacting family one must control:

1. A fast curl threshold after retaining slow modes, and a stable local
   Hodge/coarse decomposition that pays the boundary error (14) without
   losing the physical norm. The full smallest curl singular value is
   demonstrably not such a uniform threshold.
2. The nonlinear electric/potential remainder in a norm adapted to the
   retained fields and growing dimension. The constants in (8)-(10) involve
   chart derivatives, oscillator moments, soft frequencies, island margins
   and the number of modes. Fixed-complex O(1) is not a uniform bound.
3. Global localization against competing flat or almost-flat configurations
   in the actual boundary background. Simple connectedness gives the single
   zero orbit for the isolated block; it does not by itself bound a uniform
   energy barrier outside an increasing-dimensional weak-field region.
4. The induced coarse stiffness and full kinetic cross term in (15)-(16),
   varying ground energy, and surrounding plaquette interactions. A graph
   with blocks joined by interactions is not the additive two-strip graph.
5. The actual reflection/time-covariant history observation and its reducing
   range. Harmonic fast factors, conditional configuration fibers and the
   OS-history complement are different constructions. In particular full
   time-history observability can make an apparent eliminated factor
   observable; the observation map must be specified and checked.

The [periodic three-dimensional companion](G19_WILSON_THREE_DIMENSIONAL_HARMONIC_BOUNDARY_20260905.md)
now supplies a stable harmonic retained/fast split by Coulomb-projected
box means, including the flat cochain sector. Its projection is nonlocal.
The remaining local comparison therefore needs a gauge/Hodge
decomposition for overlapping cubic blocks whose retained coarse sector
contains every curl mode below a chosen threshold, with an explicit boundary
row bound (14). Combine its exact quadratic Schur form with the actual
history observation's harmonic observable subspace. This would identify
whether a nontrivial physical complement survives and which local energy
must control it before attempting nonlinear or all-scale iteration.

This result advances the ultraviolet side of the Clay route by supplying
actual coupled finite-cell physical spectra for all the stated groups and
an exact boundary mechanism. A controlled trajectory, nontrivial continuum
correlation distributions and a positive finite physical mass still require
the uniform comparisons just listed.

## 9. Reproducible exact controls and their scope

`check_cell_complex_hessian.py` builds original oriented-edge incidence
matrices for one face, two adjacent faces and 2-by-2 and 3-by-3 filled squares.
It verifies `d1 d0=0`, transverse dimension, the exact face-grid matrix,
the complete characteristic polynomial against the sine spectrum, a
rational transverse projector, (13)-(14), and the localized-pure-gradient
negative control. Its saved JSON is a fresh output artifact.

Those finite exact checks establish their matrix identities and examples.
The general sine formula is proved by direct substitution in Section 6;
the physical eigenvalue theorem and its remainder are the analytic argument
in Sections 2-5. No finite check or Gaussian approximation is labeled as a
machine proof of the general analytic or continuum conclusion.
