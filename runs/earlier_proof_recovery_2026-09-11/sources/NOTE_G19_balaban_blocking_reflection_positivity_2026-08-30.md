# G19: reflection positivity of a Balaban-form gauge blocking step

**Date:** 2026-08-30  
**Status:** one general lemma and two counterexamples proved; application to a
reflection-adapted Balaban-form deterministic step proved; the literal
lower-corner/coordinate-order convention of CMP 98 fails the required
reflection-equivariance identity in general.  Nothing here proves a continuum
limit, a mass gap, or preservation under the later large/small-field and
gauge-fixing operations.

## 1. Primary-source extraction

The primary source inspected is T. Balaban, *Averaging Operations for Lattice
Gauge Theories*, Commun. Math. Phys. **98** (1985), 17--51,
DOI `10.1007/BF01211042`.

Local Project Euclid scan:

`C:\Users\Alex\Downloads\Balaban_1985_Averaging_Operations_Lattice_Gauge_Theories.pdf`

SHA-256:

`03409ad81885593d65535550eafac08639e66123d4acf92462847ae2ee4dd7d6`

The exact facts used below are:

1. Equation (10), printed p. 19 / PDF p. 3, defines
   \[
   \rho'(V)=\int dU\,\delta\!\left(V\overline U^{-1}\right)\rho(U).
   \]
   Thus the raw RG step is the deterministic pushforward by
   $P(U)=\overline U$, not a general Markov kernel.
2. Equation (11), on the same page, states gauge covariance of the average.
3. Equation (15), on the same page, is
   \[
   P(U)_c=
   \exp\!\left[
     i\sum_{x\in B(c_-)}L^{-d}\frac1i
       \Log\!\left(U(\Gamma_{c,x})U(c)^{-1}\right)
   \right]U(c).
   \tag{B}
   \]
4. Immediately after equation (43), printed p. 24 / PDF p. 8, Balaban states
   the locality property
   \[
   P(U)_c\text{ depends only on }U_b,
   \qquad b\subset B(c_-)\cup B(c_+).
   \tag{L}
   \]
5. The paper contains no reflection-positivity theorem and makes no choice of
   blocks or path trees adapted to a time-reflection plane.

Balaban's referenced path definition was also checked in T. Balaban,
*Propagators and Renormalization Transformations for Lattice Gauge Theories. I*,
Commun. Math. Phys. **95** (1984), 17--40,
DOI `10.1007/BF01215753`.  Equation (1.6), printed p. 18 / PDF p. 2, uses
lower-corner blocks, while equation (1.7) on the same page defines the fixed
coordinate-order axial tree.  Equation (1.8), printed p. 19 / PDF p. 3, is the
linear averaging operation that CMP 98 equation (15) is required to reproduce.

Local Project Euclid scan:

`C:\Users\Alex\Downloads\Balaban_1984_Propagators_Renormalization_I.pdf`

SHA-256:

`6f637e4c85941a4dfd91be0f8845f05104edec962ca7e3307f8ae3dc3b5bf875`

The fine Wilson measure is reflection positive on the physical/gauge-invariant
positive-time algebra by Osterwalder--Seiler, *Ann. Phys.* **110** (1978),
440--471, DOI `10.1016/0003-4916(78)90039-8`.  P. Menotti and A. Pelissetto,
*General Proof of Osterwalder-Schrader Positivity for the Wilson Action*,
Commun. Math. Phys. **113** (1987), 369--373,
DOI `10.1007/BF01221251`, proves the site-plane version for all
gauge-invariant observables.  Official Project Euclid scan:

`C:\Users\Alex\Downloads\Menotti_Pelissetto_1987_General_Proof_OS_Positivity_Wilson_Action.pdf`

SHA-256:

`4645f7192f1e1386bce12231d116f14219f837ba19520a67caa0e6121347c776`

Those results are inputs here, not re-proved.

## 2. The exact permanence lemma

Let $(X,\mu,\theta;\mathcal A_+)$ be a reflected probability space.  Write
\[
 (\Theta F)(U)=\overline{F(\theta U)}.
\]
Reflection positivity means
\[
 \int (\Theta F)F\,d\mu\geq0
 \qquad(F\in\mathcal A_+).
\]
Let $(X',\theta';\mathcal A'_+)$ be a coarse reflected configuration space.

### Lemma 2.1 (deterministic pushforward permanence)

Let $P:X\to X'$ be measurable and suppose
\[
 P\theta=\theta'P\quad\mu\text{-a.e.},
 \qquad
 P^*\mathcal A'_+\subset\mathcal A_+.
 \tag{RP-P}
\]
If $\mu$ is reflection positive, then $P_\#\mu$ is reflection positive on
$\mathcal A'_+$.

The same conclusion holds on the gauge-invariant algebra if the first equality
is only true modulo a coarse gauge transformation:
\[
 P(\theta U)=g_\theta(U)\cdot\theta'P(U),
 \tag{RP-G}
\]
because every tested coarse observable is insensitive to $g_\theta(U)$.

#### Proof

For $F'\in\mathcal A'_+$, set $F=F'\circ P\in\mathcal A_+$.  Then
\[
 \begin{aligned}
 \int_{X'}(\Theta'F')F'\,d(P_\#\mu)
 &=\int_X
   \overline{F'(\theta'P(U))}F'(P(U))\,d\mu(U)\\
 &=\int_X(\Theta F)(U)F(U)\,d\mu(U)\geq0.
 \end{aligned}
\]
For (RP-G), insert gauge invariance in the second equality.  QED.

Both clauses of (RP-P) are load-bearing.  Reflection equivariance without
positive-time preservation is not enough: the pulled-back test observable may
depend on both sides of the plane.

## 3. Application to a reflection-adapted Balaban-form step

The following gives a concrete positive answer to the question for a
Balaban-form step, while exposing the extra geometry hidden by the phrase
"blocks aligned to the reflection plane."

### Lemma 3.1 (reflection-adapted Balaban blocking is RP)

Consider a periodic Wilson lattice with even temporal extent.  Let an odd block
factor $L$ divide the extent (hence the coarse temporal extent is also even).
Use centered $L^d$ blocks.  Put the time-reflection plane halfway between two
adjacent layers of block centers; in integer fine coordinates one convenient
choice is
\[
 \theta(t,\mathbf x)=(L-t,\mathbf x),
 \]
with coarse centers at $t=Lj$.  Then centered blocks obey
\[
 \theta B(Lj,\mathbf y)=B(L(1-j),\mathbf y).
 \tag{C1}
\]

Choose the reference contours and the family $\Gamma_{c,x}$ in (B) so that
they are closed under reflection and orientation reversal:
\[
 \theta\Gamma_{c,x}=\Gamma_{\theta'c,\theta x},
 \qquad
 \Gamma_{c^{-1},x'}=\Gamma_{c,x}^{-1}
 \tag{C2}
\]
after the evident relabelling of the transverse point.  Such a family exists:
choose the trees and paths in one open half, define those in the other half by
reflection, and pair the paths on the two bonds crossing the plane.  Define the
average on one orientation of each coarse bond by (B) and on the reverse bond
by group inverse.  The possible principal-log branch-cut set is Haar-null; or,
equivalently, the statement can be made on the regular domain on which the
Balaban logarithm is analytic.

Let $\mathcal A'_+$ be generated by gauge-invariant functions of coarse bonds
whose two endpoint blocks lie in the open positive half.  Then the deterministic
coarse measure $P_\#\mu_W$ is reflection positive on $\mathcal A'_+$.

#### Proof

Holonomy is functorial under a lattice reflection:
$U(\theta\Gamma)=(\theta U)(\Gamma)$, with inversion when the path
orientation reverses.  Matrix logarithm and exponential commute with unitary
conjugation.  Reindexing the equal-weight sum in (B) by
$x\mapsto\theta x$, using (C2), gives
\[
 P(\theta U)=\theta'P(U)
 \]
on the regular domain (and almost everywhere for the Wilson measure).  Gauge
covariance is exactly Balaban's equation (11).

For a positive coarse bond, (C1) and the placement of the plane put both endpoint
blocks wholly in the fine positive half.  Balaban's locality statement (L)
therefore gives
\[
 P^*\mathcal A'_+\subset\mathcal A_+.
 \]
Lemma 2.1 applies.  QED.

### What this does and does not close

This proves preservation for the **raw deterministic average** when its block
and path data are chosen reflection-adaptively.  Rescaling is only a lattice
relabeling and can be made equivariant as well.

It does not automatically cover:

- a field-dependent gauge fixing not paired under reflection;
- an asymmetric large/small-field partition;
- a localized or softened stochastic constraint;
- a full multistep effective action after any of those additions.

For any proposed non-centered convention, block alignment alone does not prove
either clause of (RP-P).  The exact check is
\[
 \boxed{
 P_{\rm CMP98}(\theta U)=
 g_\theta(U)\cdot\theta'P_{\rm CMP98}(U)
 \quad\text{and}\quad
 \operatorname{supp}P_c\subset\Lambda_+
 \text{ for every }c\in E'_+ .}
 \tag{G19-RP}
\]
The first equality might have held only modulo the coarse gauge transformation
induced by moving a block basepoint from the reflected upper corner back to the
chosen lower corner.  The next proposition shows that this anchor-change repair
does **not** work for the literal CMP 98 lower-corner/coordinate-order paths.

### Proposition 3.2 (literal CMP 98 corner paths are not reflection equivariant)

Take an SU(2) gauge field on the periodic $12\times12$ lattice, block factor
$L=3$, and time coordinate $1$.  Use the lower-corner blocks from CMP 98
equation (2) and the coordinate-order $0,1$ axial trees from CMP 95 equation
(1.7).  The site reflection
\[
 r(x,t)=(x,2-t)\pmod {12}
\]
permutes those blocks exactly; its action on block labels is
$r_B(X,T)=(X,-T)$.  Let all fine links be the identity except
\[
 U((0,0),e_0)=e^{i\varepsilon\sigma_x},\qquad
 U((0,0),e_1)=e^{i\varepsilon\sigma_y}.
\]
For the coarse plaquette rooted at $(9,9)$, exact expansion of Balaban's
equation (15) gives
\[
 \operatorname{tr}P(rU)(\partial p)
 -\operatorname{tr}(r_BP(U))(\partial p)
 =\frac{4}{81}\varepsilon^4+O(\varepsilon^5).
 \tag{CE}
\]
Hence $P(rU)$ and $r_BP(U)$ cannot be related by any coarse gauge
transformation.  Because the two sides are analytic near the identity and the
Taylor coefficient is nonzero, failure occurs on an open set, not merely on a
measure-zero branch-cut set.

#### Proof certificate

`C:\ALL THEORY\theory\notes\verify_balaban_corner_reflection_exact.py`

The certificate implements equation (15) through degree four using exact
rational arithmetic in $\mathbb Q(i)$.  It reports zero coefficients in degrees
$0,1,2,3$ and the exact real coefficient $4/81$ in degree $4$.  The SU(2)
witness embeds in SU($N$), $N\geq2$, by a block-diagonal subgroup.  It also
embeds in four lattice dimensions by taking the field constant in the two extra
coordinates and all extra-direction links equal to the identity.  Thus it
applies in particular to the four-dimensional SU(3) setting.

Consequently the literal convention cannot be used for the RP bridge as-is.
The finite-volume repair is to adopt the reflection-adapted block/path data of
Lemma 3.1 (or prove (G19-RP) for some other modified average).

## 4. Counterexample: general equivariant Markov kernels do not preserve RP

Several archive notes replace the deterministic map by a Markov kernel (K)
and use the false identity
\[
 K\bigl((\Theta'F)F\bigr)=(\Theta KF)(KF).
 \tag{false}
\]
Markov kernels are linear, not multiplicative.

### Proposition 4.1 (exact two-spin counterexample)

Let the fine space be one point, with its point mass and identity reflection;
it is reflection positive.  Let
\[
 X'=\{(s_-,s_+):s_\pm\in\{-1,+1\}\},
 \qquad
 \theta'(s_-,s_+)=(s_+,s_-),
\]
and let $\mathcal A'_+$ consist of functions of $s_+$.  Define a Markov
kernel from the one point by the reflection-invariant law
\[
 \nu=\tfrac12\delta_{(+1,-1)}+\tfrac12\delta_{(-1,+1)}.
\]
The kernel is reflection equivariant.  It maps every positive-time observable
to a constant, hence to the fine positive algebra.  Nevertheless, for
$F(s_-,s_+)=s_+$,
\[
 \int(\Theta'F)F\,d\nu
 =\mathbb E_\nu[s_-s_+]=-1<0.
\]
Thus equivariance plus one-sided mapping is insufficient for a stochastic
kernel.

A correct sufficient stochastic hypothesis is a reflection factorization: there
must exist a one-sided operator $T:\mathcal A'_+\to\mathcal A_+$ such that
\[
 K\bigl((\Theta'F)G\bigr)=(\Theta TF)(TG)
 \qquad(F,G\in\mathcal A'_+).
 \tag{RF}
\]
Then fine RP gives coarse RP immediately.  Deterministic pushforward is the
special case $TF=F\circ P$.  Conditional independence of the two coarse halves,
with a separately positive boundary kernel, is another possible route to (RF).

Consequently the Markov-kernel Lemma 2.1 in
`C:\Users\Alex\Desktop\RESEARCH\RG_COARSE\03_RP_OS_Permanence\06_reflection_positivity_permanence.md`
is refuted as written.  The deterministic lemma in the neighboring archive notes
is correct after positive-time preservation is included explicitly.

## 5. Adjacent Rev5 source-residue wording audit

The current Rev5 G19 insert already contains the essential correction from
`carrier4.txt`: equations (local source matching)--(overlap power) count the
**absolute atom weight** of the unrenormalized volume-normalized source, while
the paragraph immediately following the proof says explicitly that the common
$a^9|Z_6(a)|^2$ normalization cancels in a fixed-physical-time normalized
spectral ratio.  Therefore the paper currently does **not** infer collapse of a
Hilbert-normalized spectral fraction.

Three phrases should nevertheless be narrowed to prevent the earlier reading:

1. `Bare carrier-residue power counting` ->
   `Bare carrier absolute-weight power counting`.
2. `unit-normalized zero-momentum source` ->
   `volume-normalized zero-momentum source`.
3. `Thus the bare residue has the power ... that residue vanishes` ->
   `Thus this state's absolute spectral atom weight for the unrenormalized,
   volume-normalized source has the power ... that absolute weight vanishes`.

No change is needed to the subsequent firewall paragraph; it already states the
correct fixed-physical-time cancellation.

## 6. Bottom line

The RP-under-blocking question is not an untouched continuum theorem anymore.
For the raw deterministic Balaban-form step, it is a short pushforward theorem
plus two checkable geometry clauses.  A reflection-adapted centered version
satisfies them and preserves Wilson reflection positivity.  The literal CMP 98
corner-path convention fails the required identity by Proposition 3.2, so it
must be modified rather than cited as automatic.  Arbitrary
reflection-equivariant Markov blocking is not a substitute: it fails by
Proposition 4.1 unless the stronger reflection-factorization condition (RF) is
proved.
