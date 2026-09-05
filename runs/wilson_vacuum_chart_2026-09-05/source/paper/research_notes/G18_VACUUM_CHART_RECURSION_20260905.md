# A local vacuum chart at every fixed magnetic order

Date: 5 September 2026.

This note extends the second-order construction in
`G18_SECOND_ORDER_WILSON_VACUUM_CHART_20260905.md`. It proves a formal
multivariate induction for the actual symmetric Wilson transfer, with a
volume-, temporal-mesh-, and representation-uniform full-operator bound at
each fixed order. It also proves that every vacuum-rotation generator is
independent of the positive integer temporal block power.

The result does not assert convergence of the nonlinear chart. An explicit
recursive bound is given below; it proves finiteness at each order, but does
not supply a positive convergence radius. The last section states precisely
which additional scalar majorant would supply that radius.

## 1. Conventions and the local coefficient problem

Use the second-order note's link supports, actual transfer

\[
 T_A(z)=e^{\tau\sum_{p\in A}z_pv_p/2}
         e^{-\tau K_{X(A)}}e^{\tau\sum_{p\in A}z_pv_p/2},
 \qquad B_A(z)=T_A(z)^m,
 \qquad D_X=e^{-sK_X},\quad s=m\tau.
\]

Here `A` is a finite active face set, `X(A)` its link union,
`||v_p|| <= J`, `s <= s_1`, and

\[
 D_X\Omega_X=\Omega_X,\qquad
 \|D_XQ_X\|\le\delta\le\delta_0:=4/5,
 \quad P_X=|\Omega_X\rangle\langle\Omega_X|,\quad Q_X=1-P_X.
 \tag{1}
\]

The positive real vacuum branch of `B_A` has the analytic eigenvalue
`b_A(z)` continuing 1. Normalize the operator by this actual eigenvalue.
All Taylor coefficients are ordinary coefficients: `[z^alpha]`, without
extra multinomial or derivative factors.

A multiindex `alpha=(alpha_p)` has finite nonempty face support
`A(alpha)={p:alpha_p>0}` and degree `|alpha|=sum_p alpha_p`. Its support is
connected when `A(alpha)` is connected in the shared-link face graph.
Connectedness is a property of the distinct active faces; a repeated face
does not create an extra vertex. Write `X_alpha=X(A(alpha))`.

If `A` decomposes into shared-link components `A_i`, their link sets are
disjoint and, before any Taylor expansion,

\[
 B_A=\bigotimes_i B_{A_i},\qquad b_A=\prod_i b_{A_i}.
 \tag{2}
\]

Likewise, setting all couplings outside `A` to zero in a larger volume
gives `B_A tensor D_outside` and vacuum eigenvalue `b_A`. These identities
hold on the full link Hilbert space. Gauge restriction is performed after
the identities and estimates; it is not used to assert a tensor product of
gauge-constrained spaces.

## 2. Induction and the connected generators

For each degree `j`, define an anti-Hermitian polynomial of local operators

\[
 S_{j,A}(z)=
 \sum_{\substack{|\alpha|=j,\ A(\alpha)\subset A\\
                  A(\alpha)\ {\rm connected}}}
 z^\alpha S_\alpha,
 \qquad
 U_{<n,A}=e^{S_{1,A}}e^{S_{2,A}}\cdots e^{S_{n-1,A}}.
 \tag{3}
\]

Every local `S_alpha` is embedded by the identity on other links. For
complex couplings use `U^{-1}`. For real couplings it is `U^*`.

**Inductive hypothesis.** In every finite active subsystem, all nonconstant
coefficients of degree less than `n` of

\[
 E_A^{<n}(z)=U_{<n,A}^{-1}\,B_A(z)b_A(z)^{-1}\,U_{<n,A}
 \tag{4}
\]

annihilate the subsystem vacuum on both sides. The previously defined
generators have connected supports and agree under restriction of the
active variables. At `n=1` the hypothesis is empty.

For connected `alpha` of degree `n`, compute in its minimal active
subsystem and set

\[
 A_\alpha=[z^\alpha]E_{A(\alpha)}^{<n}(z),\qquad
 \chi_\alpha=(1-D_{X_\alpha})^{-1}Q_{X_\alpha}
                         A_\alpha\Omega_{X_\alpha},
 \tag{5}
\]

\[
 S_\alpha=|\chi_\alpha\rangle\langle\Omega_{X_\alpha}|
          -|\Omega_{X_\alpha}\rangle\langle\chi_\alpha|,
 \qquad
 F_\alpha=A_\alpha+[D_{X_\alpha},S_\alpha].
 \tag{6}
\]

The inverse in (5) is restricted to `Q_X`. Its norm is at most 5.

### Theorem 1. Formal local vacuum anchoring at every degree

Equations (3)--(6) are well-defined inductively at every fixed degree. They
give

\[
 F_\alpha P_{X_\alpha}=P_{X_\alpha}F_\alpha=0,
 \qquad \|S_\alpha\|\le5\|A_\alpha\|,
 \qquad \|F_\alpha\|\le11\|A_\alpha\|.
 \tag{7}
\]

After adjoining `exp(S_n)` on the right of `U_{<n}`, every coefficient of
degree at most `n` of the rotated normalized transfer is vacuum-anchored.
No generator with disconnected face support is needed.

**Proof.** First check factorization. Since every earlier generator has
connected face support, setting the inactive variables to zero removes
every generator involving an inactive face. If the remaining active faces
split into components, each surviving generator lies in just one
component. Operators on distinct components commute, so every exponential
in (3), and their ordered product, factorizes across those components.
Together with (2), this proves exact factorization of (4).

Normalize its analytic eigenvector at eigenvalue 1 by
`<Omega_X,psi_A(z)>=1`. Its coefficients of degrees `1,...,n-1` vanish.
Indeed the eigenvector equation at each of these degrees is
`(1-D_X)psi_beta=0`: all lower operator coefficients kill the vacuum and
all lower eigenvector coefficients already vanish. Invertibility on `Q_X`
and the normalization give `psi_beta=0`.

The equation at a degree-`n` monomial therefore has no lower cross terms:

\[
 (1-D_X)[z^\alpha]\psi_A
      =([z^\alpha]E_A^{<n})\Omega_X.
 \tag{8}
\]

Taking its vacuum component shows ` <Omega_X,A_alpha Omega_X>=0`.
In particular (5) is its uniquely normalized eigenvector coefficient.
For real independent variables (4) is self-adjoint; hence each coefficient
`A_alpha` is self-adjoint. Equations (5)--(6) now give
`[D_X,S_alpha]Omega_X=-A_alpha Omega_X`. The left vacuum leg vanishes by
self-adjointness. The rank-two anti-Hermitian generator has norm exactly
`||chi_alpha||`, proving (7).

For a disconnected degree-`n` monomial, factorization of (4) gives a
tensor product of coefficients on its nonempty components. Each component
has strictly smaller degree, so its coefficient is already anchored.
Their tensor product is anchored without a new rotation.

Finally conjugation by `exp(S_n)` changes a degree-`n` coefficient only by
`[D,S_n]`: every other commutator has degree greater than `n`. It leaves
lower coefficients unchanged. Thus (6) repairs exactly the connected
degree-`n` coefficients and completes the induction. Embedding its
generator by the identity gives `[D_X tensor D_out,S_alpha tensor I]
`=` `[D_X,S_alpha] tensor D_out`, as required for restriction consistency.
This proves the theorem. ∎

At first order (5) is the already derived
`S_p=d_tau(E_s)(v_pP_p-P_pv_p)`. At second order it is exactly the
repeated-face and overlapping-pair construction in the preceding note.

## 3. Full coefficient identity, support, and symmetries

For any multiindex `alpha`, let `alpha_1,...,alpha_c` be its restrictions
to the connected components of its active-face graph. Later rotations
cannot change a coefficient of degree `|alpha|`. The formal chart therefore
satisfies the exact coefficient identity

\[
 [z^\alpha]\widetilde D_L(z)
   =\left(\bigotimes_{i=1}^c F_{\alpha_i}\right)
       \otimes D_{X(\alpha)^c}.
 \tag{9}
\]

Here the notation on the left means the coefficient in any finite chart
`U_{<=N}` with `N>=|alpha|`; a convergent infinite product is not being
assumed. Equation (9) includes every repeated-variable and disconnected
term. Setting all face variables to `u` means summing (9) over all
multiindices of that degree, each once.

A connected set of `r` distinct faces has at most `3r+1` links: start
with four, and add each face along a spanning tree, sharing at least one
existing link. Consequently

\[
 |X_\alpha|\le3|\alpha|+1\quad\hbox{for connected }\alpha;
 \qquad |X(\alpha)|\le4|\alpha|\quad\hbox{in general}.
 \tag{10}
\]

All generators commute with gauge transformations, charge conjugation and
the electric one-form symmetries. The free vacuum, actual transfer and
normalized vacuum line are invariant, and the local inverse in (5)
commutes with these symmetries. Thus `chi_alpha` is invariant and so is its
rank-two generator. Restrictions to the physical neutral odd sector are
therefore legitimate at each stage.

### Corollary 2. The generators do not depend on the block power

Fix the fine transfer and `tau`. Every `S_alpha` is identical whether its
construction uses `T_A`, `T_A^m`, or any other positive integer power.

**Proof.** Induct on the degree. The previous rotations are power-independent
by the inductive hypothesis. Positive integer powers have the same vacuum
eigenvector for real couplings; after the common previous rotations and
normalization, its analytic germ is the same. Equation (8) identifies
`chi_alpha` with one coefficient of that germ. This proves power-independence
at the next degree. The operator coefficients `F_alpha` themselves remain
block-dependent. ∎

## 4. Explicit uniform bounds at every fixed order

Put `beta=J s_1`. Suppose `a_j` bounds `||S_alpha||` for connected
degree-`j` multiindices, uniformly in their placement, volume and mesh.
For example use the sharper first-order value

\[
 a_1=J(1/E_s+\tau_0/2),\qquad l_1=f_*.
\]

For `n>=2` define recursively

\[
 r_n=\frac{\log(41/40)}{\beta n},\qquad
 P_n=\sum_{j=1}^{n-1}\binom{n+j-1}{j}a_jr_n^j,
 \tag{11}
\]

\[
 k_n=\frac{41}{39}\,e^{2P_n}r_n^{-n},\qquad
 a_n=5k_n,\qquad l_n=11k_n.
 \tag{12}
\]

These are explicit finite positive constants at every finite `n`.
They bound `||A_alpha||`, `||S_alpha||`, and `||F_alpha||`, respectively.

**Proof.** A degree-`n` active subsystem has at most `n` distinct faces.
On the polydisc `|z_p|<=r_n`, expansion of the actual magnetic
exponentials with the free contractions left in place gives

\[
 \|B_A(z)-D_X\|\le e^{\beta n r_n}-1=1/40,
 \qquad \|B_A(z)\|\le41/40.
\]

The free operator is normal, with its simple eigenvalue 1 separated from
the rest by at least `1/5`. The standard resolvent Neumann argument on a
circle of radius `1/10` around 1 preserves the rank-one eigenbranch.
Normal spectral inclusion also places that branch within `1/40` of 1,
so `|b_A(z)|>=39/40`. These are estimates on the entire untruncated link
Hilbert space.

There are at most `binom(n+j-1,j)` degree-`j` monomials in at most `n`
variables. Thus both `U_{<n,A}` and its inverse have norm at most
`exp(P_n)` throughout this polydisc. It follows that

\[
 \|E_A^{<n}(z)\|\le(41/39)e^{2P_n}.
\]

Multivariate Cauchy extraction divides this bound by `r_n^n`. Apply
(7) to obtain (12). ∎

The recurrence deliberately retains all lower-order rotations and their
noncommuting products. It establishes uniformity at each fixed order; its
growth does not establish convergence of a magnetic series.

## 5. Uniform full-operator coefficients at arbitrary fixed degree

Define

\[
 w_j=4\,145^{j-1}l_j,\qquad
 W_n(t)=\sum_{j=1}^n w_jt^j.
 \tag{13}
\]

The factor counts all connected monomials meeting a chosen excited link.
A link belongs to four faces. Connected sets of `r` faces containing a
fixed root face are bounded by `144^{r-1}`. To see this, fix a deterministic
neighbor ordering and a rooted spanning tree for each such set; its
depth-first traversal is a face-graph walk of length `2(r-1)`, with at most
twelve choices per step. The visited set recovers the original face set,
so these walks give an injection into at most `12^{2(r-1)}` possibilities.
The positive multiplicities
of degree `j` on those `r` faces have `binom(j-1,r-1)` choices. Summing
over `r` gives `145^{j-1}`. All these counts are upper bounds on the
actual finite torus; wrapping does not invalidate them.

### Theorem 3. Full-operator bound at each fixed order

For every `n>=1`, the formal homogeneous coefficient satisfies

\[
 \boxed{
 \sup_{L,\epsilon}\|[u^n]\widetilde D_L(u)\|
 \le B_n:=
 \sum_{c=1}^n\frac{(5n)^c}{c!}
                  [t^n]W_n(t)^c<\infty .}
 \tag{14}
\]

**Proof.** Each connected `F_alpha` is self-adjoint and anchored, so
`-l_j Q_X <= F_alpha <= l_j Q_X`. Products on disjoint components admit
the product of these positive norm majorants. Tensoring the free outside
factor preserves the inequalities. All majorants commute with the exact
link-vacuum projections.

On a sector with `h` excited links, each component must meet that excited
set. A degree-`j` component has at most `h w_j/l_j` rooted choices. For
`c` disjoint components, allowing every independently rooted choice only
increases the sum. Divide by `c!`, since every actual unordered family
has exactly that many orderings. Its total footprint has at most `4n`
links, leaving the free damping `delta_0^max(h-4n,0)`. Equation (9)
therefore has norm at most

\[
 \sup_{h\ge1}\delta_0^{\max(h-4n,0)}
       \sum_{c=1}^n\frac{h^c}{c!}[t^n]W_n(t)^c.
 \tag{15}
\]

For `c<=n`, the maximum of
`h^c delta_0^max(h-4n,0)` is at most `(5n)^c`.
For `h<=5n` this is immediate. Above `5n` its logarithmic derivative is
`c/h-log(5/4)<1/5-log(5/4)<0`. This proves (14).
The free vacuum sector contributes zero at positive degree. ∎

The preceding second-order note's `40432 f_*^2/5` is much sharper than
(14) at `n=2`; (14) is intended to cover arbitrary fixed degree. Neither
estimate uses a finite-dimensional representation approximation.

## 6. What would close the nonlinear majorant

There is now one concrete growth question. Suppose improved connected
bounds, unlike the crude recurrence (12), prove that

\[
 W(t)=\sum_{j\ge1}4\,145^{j-1}l_jt^j
\]

has a positive radius. Choose a positive `r` in that radius such that
`W(r)<log(5/4)`. Then (15), using
`delta_0^max(h-4n,0)<=delta_0^{h-4n}`, gives the geometric coefficient
bound

\[
 \|[u^n]\widetilde D_L\|
 \le(r\delta_0^4)^{-n}
       \sup_{h\ge1}e^{-h\log(5/4)+hW(r)}
 \le(r\delta_0^4)^{-n}.
 \tag{16}
\]

This would supply a common norm-convergent series for the formal
transformed-operator coefficients. Convergence of the vacuum chart itself,
and equality of this sum with an exact chart of the normalized transfer,
still require generator control or an independently constructed equivalent
chart; a bound on `F_alpha` alone does not bound `S_alpha`. It is not
an assumption in Theorems 1--3, and (12) does not prove it. The available
scalar vacuum expansion likewise does not by itself provide this connected
operator-coefficient estimate: the local noncommuting chart coefficients
must be bounded as such.

The remaining nonlinear task is therefore narrower than a new spectral
calculation: prove a convergent rooted norm for the connected vacuum chart,
or construct an equivalent chart with such a norm. The exact induction,
disconnected factorization, spectator damping, arbitrary-fixed-order
bounds, and block-power compatibility above do not need to be assumed
again. Even after convergence, identification with the actual physical
excited Riesz range must use the operator-contour and GNS/source-totality
steps of the preceding bridge, rather than source moments alone.

## 7. Provenance and verification boundary

This is an additive analytic derivation from the actual-transfer definitions
and the calibrated kinetic gap in the supplied September 4 notes. The
second-order formula and its `40432/5` estimate were independently checked
against the preceding September 5 note before this extension was written.
The companion `src/workhouse/wilson_chart_recursion.py` implements the exact
finite tensor recursion. Its tests check overlapping supports through degree
four, a three-support chain through degree three, disjoint factorization,
excited spectators, and power-independent generators. Separate closed
spectrum/rotation formulas and the specialized quadratic engine provide
independent checks. `lean/Workhouse/VacuumChart.lean` proves the algebraic
rank-two cancellation kernel; it does not formalize this analytic induction
or its bounds. The native ledger records the fixed-order progress while
retaining nonlinear convergence and physical source projection as open.
