# Infinite-lattice continuation of the Wilson creator coordinates

Date: 5 September 2026. Analytic consequence of the uniform contraction theorem.

This note assumes the uniform finite-volume theorem proved in
`G18_ROOTED_WILSON_CONTRACTION_20260905.md`. It constructs a canonical analytic
infinite-lattice creator family from the actual finite-volume Wilson
vacuum coordinates. Its proof uses exact active-plaquette factorization
and the already proved holomorphic radius. It does not construct an
infinite-volume Hilbert-space vacuum vector, a physical state, or an
excited operator chart.

## 1. Precise input and conclusion

Use a fixed infinite cubic lattice, identical link Hilbert spaces, the
same link kinetic operators, and the same local Wilson plaquette
multipliers. Consider finite open boxes, or periodic boxes compared in
interior coordinate charts, whose neighborhoods exhaust this lattice.
Each plaquette has four distinct links, and each link belongs to at most
four plaquettes. The parameters `gamma`, `tau_0`, `mu`, and `J_*` are
those of the moving-weight theorem.

For a fixed `0<tau<=tau_0`, let `v^Lambda(u)` denote that theorem's
finite-volume fixed point. Put `a=R/4`; its input is

\[
 v^\Lambda(0)=0,\qquad
 v^\Lambda:\{|u|<u_*\}\longrightarrow X_\mu(\Lambda)
 \text{ holomorphic},\qquad
 \|v^\Lambda(u)\|_\mu\le a.                 \tag{1}
\]

The constants `a` and `u_*` are independent of volume and `tau`. At the
explicit radius `R=1/4`, `a=1/16`. The coordinate is the exact endpoint
creator logarithm of the actual finite-volume Perron branch near zero;
the moving-weight theorem identifies the same branch throughout its
stated real interval under the positive Wilson-kernel premise.

Let `X_mu(infinity)` be the space of families indexed by all finite
nonempty link sets, with each component in the corresponding exact
excited tensor factor, and norm

\[
 \|v\|_\mu=\sup_\ell\sum_{J\ni\ell}e^{\mu|J|}\|v_J\|.
                                                               \tag{2}
\]

This is a Banach space. For example, a norm-Cauchy sequence is Cauchy in
each component Hilbert space; the component limits and the norm
convergence follow from the defining nonnegative sums and their uniform
Cauchy bound.

There is a unique family obtained by stabilization of the finite-volume
Taylor coefficients,

\[
 v^\infty(u)=\sum_{n\ge1}u^n v_n^\infty,
 \qquad |u|<u_* .                              \tag{3}
\]

The series converges in (2), defines a holomorphic map, and satisfies
`||v^infinity(u)||_mu<=a`. All these assertions are uniform in the mesh
range. Uniqueness here means uniqueness of this stabilized analytic
continuation. It does not assert uniqueness of an arbitrary physical
infinite-volume vacuum or state.

## 2. Exact locality of a fixed Taylor coefficient

Introduce independent formal couplings `z_p` on the finitely many
plaquettes of a finite volume. The finite-volume isolated free-vacuum
eigenpair has its ordinary multivariate analytic germ at zero. No
volume-uniform multivariate radius is needed for the following argument.

For a multi-index `alpha`, let `S={p:alpha_p>0}` be its active plaquette
set. To extract this coefficient, all variables outside `S` may first
be set to zero. The actual symmetric transfer then factors into the
transfer on the link footprint of `S` and the free transfer on all
remaining links. Both the magnetic endpoint and the Haar normalization
factor in the same way. The normalized endpoint vector therefore has
vacuum spectators, so its creator logarithm is supported inside the
footprint of `S`.

More strongly, join two active plaquettes when they share a link. If
`S` has several components in this graph, their link footprints are
disjoint. The actual transfer and its normalized analytic vacuum branch
are tensor products over these components. In exact-support algebra,
the endpoint vector is consequently the star product of the component
vectors. Its finite creator logarithm is the sum of their logarithms.
A monomial using variables from more than one component has coefficient
zero in that logarithm. Thus every nonzero creator monomial has a
connected active-plaquette witness.

This reasoning identifies the coefficients of `v^Lambda` because the
moving-weight fixed point agrees with this analytic vacuum germ near
zero. It does not assume convergence of the earlier all-order unitary
rotation construction.

A monomial of total degree `n` has `r<=n` distinct active plaquettes.
If they are connected, order them along a spanning tree: the first has
four links and each subsequent plaquette shares a link with its
predecessors. Therefore its full link footprint has size at most

\[
 4+3(r-1)=3r+1\le3n+1.                         \tag{4}
\]

Every nonempty output exact support `J` lies inside that footprint.
It need not itself be geometrically connected: links may return to the
Haar vacuum during the coefficient calculation. The connected object
used here is the active-plaquette witness.

If `ell` lies in `J`, some active plaquette contains `ell`, and all
active plaquettes lie within `n-1` steps of it in the plaquette
overlap graph. Each plaquette has at most twelve neighbors in that
graph. Hence only finitely many active clusters and multi-indices can
contribute at degree `n` to the entire coefficient family rooted at
`ell`. Their transfer computations take place on identical finite
link subsystems in every sufficiently large volume. The whole rooted
degree-`n` family consequently stabilizes exactly, including its
Hilbert-space vectors, once those neighborhoods fit without a boundary
or a periodic identification.

This proves coefficient locality using the actual Wilson transfer.
There is no representation cutoff, compactness extraction of Hilbert
vectors, or merely numerical coefficient comparison in this step.

## 3. Cauchy bounds and convergence in the infinite rooted norm

Fix `0<r<u_*` and write
`v^Lambda(u)=sum_{n>=1}u^n v_n^Lambda`. Applying the Banach-valued
Cauchy coefficient estimate to (1) gives

\[
 \|v_n^\Lambda\|_\mu\le a r^{-n}.              \tag{5}
\]

For each root, the degree-`n` family stabilizes as proved above. Define
`v_n^infinity` by these compatible stabilized components. Passing (5)
to each rooted finite sum, and then to their supremum, gives

\[
 \|v_n^\infty\|_\mu\le a r^{-n}.              \tag{6}
\]

The estimate is independent of the root, volume, and mesh. For
`|u|<r`, it makes (3) an absolutely convergent Banach-space power
series. As `r` can be any number below `u_*`, its analytic domain is
the whole disk `|u|<u_*`.

The bound `a` for the sum follows from (1), rather than from replacing
the power series by a geometric majorant. For every fixed support,
the finite-volume series converge in that component to (3): its
coefficients eventually agree at each fixed degree, and (5)--(6)
bound both tails. For any finite collection of supports containing
a chosen root, component convergence preserves the bound `a` on
their weighted norm sum. Taking the supremum over such finite
collections and then over roots proves

\[
 \boxed{\|v^\infty(u)\|_\mu\le a.}             \tag{7}
\]

## 4. Quantitative local rooted convergence

Write
`r_ell(w;mu)=sum_{J contains ell}e^{mu|J|}||w_J||`.
Embed the links of a finite box into the infinite link labels and
extend its family by zero. For periodic boxes one may use the usual
link labels of a fundamental box; comparison is at roots whose
relevant neighborhoods do not meet the identified boundary.

Suppose every active cluster of at most `N` plaquettes contributing at
`ell` fits faithfully in the chosen volume. The two entire rooted
Taylor families agree through degree `N`. Applying (5)--(6) to the
remaining terms gives, with `q=|u|/r<1`,

\[
 \boxed{
 r_\ell(v^\Lambda(u)-v^\infty(u);\mu)
 \le 2a\frac{q^{N+1}}{1-q}.}                  \tag{8}
\]

At `R=1/4`, the prefactor is `2a=1/8`. The same bound holds at every
root whose order-`N` neighborhood fits, so it is uniform on a growing
interior region. It is not a claim that finite-volume zero extensions
converge in the supremum over every root of the infinite lattice:
their boundary and exterior roots preclude that conclusion.

## 5. Exact scope of the extension

The resulting object is a canonical analytic family of local creator
coefficients, with a volume- and mesh-independent support weight,
coupling radius, and local convergence bound. Translation or gauge
symmetries respected by the finite-volume germs pass to the stabilized
coefficients. Its Taylor coefficients retain the exact connected
active-plaquette witness and the footprint bound (4).

Neither `exp_star(v^infinity)` nor the infinite sum of embedded
creators is asserted to be a bounded global operator or a normalizable
vector in the free infinite tensor product. The finite-volume scalar
normalizers can be extensive. Constructing a physical infinite-volume
state from local observables, proving its compatibility with the
existing GNS carrier, and transporting the excited spectral/source
projection require their own arguments. Those claims do not follow
just from the creator-family norm (7).

## 6. Provenance and evidence

This is an independently reviewed analytic consequence of the companion
contraction theorem and exact active-variable factorization. The Cauchy
bound, coefficient stabilization and local tail estimate are proved above;
no finite lattice experiment is being substituted for the infinite-lattice
argument. The associated finite algebra and source snapshots are preserved
in `runs/wilson_rooted_contraction_2026-09-05`.
