# G17 SU(3) plaquette-covariance attack

**Date:** 2026-08-30  
**Status:** exact small-complex theorem; general sign unresolved  
**Question:** Does every finite inhomogeneous Wilson measure with nonnegative
couplings satisfy
\[
 \operatorname{Cov}_b\!\left(\tfrac13\operatorname{ReTr}U_p,
 \tfrac13\operatorname{ReTr}U_q\right)\ge 0
\]
for all elementary plaquettes of a standard periodic SU(3) hypercubic lattice?

## Verdict

No proof of this exact SU(3) statement was located, and no counterexample was
found on the smallest genuinely coupled plaquette surface.  It must remain an
open condition in the paper.  It is not safe to cite a U(N), Abelian, or generic
"positive character expansion" result as if it proved the statement.

There is, however, an exact positive result that narrows the obstruction:
on a genus-zero two-dimensional plaquette complex, any two distinct faces with
the same coupling have nonnegative covariance.  In particular, on the six-face
boundary of one cube all within-soft-class and within-hard-class covariances in
the two-coupling G17 geometry are nonnegative.  The first unresolved surface
case is the cross-class covariance.  Beyond two dimensions, non-Abelian link
recoupling introduces signed Haar channels, so the planar proof does not lift
coefficient by coefficient.

## 1. Exact genus-zero face theorem

**Theorem (same-coupling faces on a closed genus-zero complex).**  Let `K` be
a finite connected oriented two-dimensional cell complex homeomorphic to
`S^2`, with normalized SU(3) Haar variables on its edges and one central
Wilson factor `exp(b_f ReTr(U_f)/3)` on each face.  For any two distinct faces
`p != q`, if `b_p=b_q>=0` and all other face couplings are arbitrary and
nonnegative, then
\[
 \operatorname{Cov}\!\left(\tfrac13\operatorname{ReTr}U_p,
 \tfrac13\operatorname{ReTr}U_q\right)\ge0.
\]

Let an oriented cellulation of the sphere have `F` faces.  Give face `f` the
central Wilson weight
\[
 w_{b_f}(U)=\exp\!\left[b_f X(U)\right],\qquad
 X(U)=\frac13\operatorname{ReTr}U,
\]
and expand it in SU(3) characters,
\[
 w_b(U)=\sum_R c_R(b)\chi_R(U).
\]
Every `c_R(b)` is nonnegative for `b >= 0`: expand the exponential of
`(chi_3+chi_bar3)/6` and use the nonnegative tensor-product multiplicities.
Successive Haar integrations on the two-dimensional complex give the exact
sphere formula
\[
 Z(b_1,\ldots,b_F)=
 \sum_R d_R^{\,2-F}\prod_{f=1}^{F}c_R(b_f).
\]
For positive couplings define
\[
 \pi(R)=Z^{-1}d_R^{\,2-F}\prod_f c_R(b_f),
 \qquad y_R(b)=\frac{c_R'(b)}{c_R(b)}.
\]
For distinct faces `p` and `q`, direct differentiation gives
\[
 \operatorname{Cov}(X_p,X_q)
 =\operatorname{Cov}_{\pi}
   \bigl(y_R(b_p),y_R(b_q)\bigr).
\]
Therefore, if `b_p=b_q=b`,
\[
 \boxed{\operatorname{Cov}(X_p,X_q)
 =\operatorname{Var}_{\pi}(y_R(b))\ge0.}
\]
Zero couplings follow by continuity.  This proves the stated theorem.

This is an exact theorem, not a numerical observation.  It removes only the
**within-class** part of the G17 sign question on a closed genus-zero surface:
two soft faces (both coupling `s`) or two hard faces (both coupling `beta`) on
the cube boundary.  It does not close even the cube comparison needed by G17,
because differentiating the soft-face defect while hard couplings are restored
requires the **cross-class** covariance `b_p=s`, `b_q=beta`.  It says still less
about the signed link recouplings present in a three- or four-dimensional
hypercubic lattice.

## 2. Controlled cube-boundary test of the unresolved sign

The separate instrument

`C:\ALL THEORY\programs\g17_covariance\scan_su3_cube_covariance.py`

implements the preceding character sum.  Its SHA-256 is

`de6de01978ddec38c300b7335da876f61c6d98eb9a980e3fbd9653a491893cd7`.

The sealed diagnostic record is

`C:\ALL THEORY\programs\g17_covariance\CERT_G17_SU3_CUBE_COVARIANCE_SCAN_20260830.json`

with SHA-256

`1d7461f32f63da4e15c2afa78dac693d006d32a5bc298ab0b750215786dbf803`.

The character coefficients are generated as a manifestly nonnegative Taylor
series under multiplication by `chi_3+chi_bar3`; no Monte Carlo sampling is
used in evaluating a chosen row.

Two-class scan:

- SU(3) irrep cutoff `p+q <= 30`;
- Taylor order 200;
- 120 logarithmically spaced couplings from 0.01 to 40;
- all 7,260 grid pairs `s <= beta`;
- every soft-face count 1 through 5, hence 36,300 cross-class covariance
  evaluations.

No negative value was found.  The minimum was
`2.3570555229834866e-16` at `s=0.01`, `beta=40`, five soft faces, which is a
roundoff-scale zero rather than evidence of strict positivity.  A separate
300,000-row arbitrary-inhomogeneous scan likewise found no negative value.

For the representative row `(0.3,1.2,4.0,9.0,2.5,6.5)`, the covariance of
faces 0 and 1 was respectively

- `0.0008468296050675313` at irrep cutoff 20 / Taylor order 140;
- `0.0008468296050675307` at cutoff 28 / order 180;
- `0.0008468296050675313` at cutoff 36 / order 220.

The final Taylor-term ratios were below `3e-114` in all three runs.  These are
controlled convergence diagnostics, but the finite scans are not a proof of
the unequal-coupling sign.

## 3. Exact obstruction to a generic Ginibre import

The broad claim that real SU(3) Wilson loops are all positively correlated is
false already at Haar measure.  Put
\[
 A(U)=\operatorname{ReTr}U,
 \qquad B(U)=\operatorname{ReTr}U^2.
\]
The SU(3) character identities
\[
 \operatorname{Tr}U=\chi_{3},\qquad
 \operatorname{Tr}U^2=\chi_{6}-\chi_{\bar3}
\]
and character orthogonality yield
\[
 \int A\,dU=\int B\,dU=0,
 \qquad
 \boxed{\int A(U)B(U)\,dU=-\frac12.}
\]
With both traces divided by three, the covariance is `-1/18`.  Here `B` is a
twice-wound loop, not a second elementary plaquette, so this does **not**
disprove the G17 elementary-plaquette conjecture.  It does prove that a generic
"all SU(3) Wilson loops are in a Ginibre cone" argument cannot be used.

There is a second local warning at the first `2 U + 2 U-bar` Haar moment.  The
unitary Weingarten coefficients at rank three are
\[
 \mathrm{Wg}_{3}(e)=\frac18,
 \qquad
 \boxed{\mathrm{Wg}_{3}((12))=-\frac1{24}}.
\]
For this balanced degree the SU(3) integral agrees with the U(3) integral.
Thus a link at which two sheets in each orientation meet already has a negative
crossed contraction.  This does not fix the sign after the complete spin-foam
sum, but it is the smallest exact blocker to any coefficientwise-positive lift
of the two-dimensional character proof.

## 4. Primary-source boundary

1. J. Ginibre, *General formulation of Griffiths' inequalities*, Commun. Math.
   Phys. **16** (1970) 310-328, DOI
   [10.1007/BF01646537](https://doi.org/10.1007/BF01646537).  Its conclusion
   requires the cone positivity hypotheses; those hypotheses must be checked,
   not inferred from the word "ferromagnetic."
2. E. T. Tomboulis, A. Ukawa and P. Windey, *Correlation inequalities and
   quark confinement in lattice gauge theories*, Nucl. Phys. B **180** (1981)
   294-300, DOI
   [10.1016/0550-3213(81)90421-1](https://doi.org/10.1016/0550-3213(81)90421-1).
   The paper's stated group scope is `Z_2` and `U(N)`; it does not state the
   inhomogeneous SU(3) elementary-plaquette covariance used by G17.
3. I. Chevyrev and C. Garban, *Villain Action in Lattice Gauge Theory*, J.
   Stat. Phys. **192** (2025) 38, DOI
   [10.1007/s10955-025-03420-1](https://doi.org/10.1007/s10955-025-03420-1),
   [arXiv:2404.09928](https://arxiv.org/abs/2404.09928).  Their carpet-graph
   convergence covers non-Abelian groups, including SU(3), but their Ginibre
   monotonicity corollary is expressly Abelian.

   Archived primary preprint: 18-page arXiv v2 (10 March 2025),
   `literature_primary/chevyrev_garban_2025_villain_action_lgt_arxiv.pdf`,
   SHA-256
   `89720d61bd0c0ebc2ac7e27d0d808de7ed8c13fc73f863c79302d38293cb2ae4`.
4. B. Collins and P. Sniady, *Integration with respect to the Haar measure on
   unitary, orthogonal and symplectic group*, Commun. Math. Phys. **264**
   (2006) 773-795, DOI
   [10.1007/s00220-006-1554-3](https://doi.org/10.1007/s00220-006-1554-3),
   [arXiv:math-ph/0402073](https://arxiv.org/abs/math-ph/0402073).  This supplies
   the exact Weingarten formula used above.

## 5. What the paper may safely say

The G17 covariance condition remains conditional.  It may now add:

- an exact genus-zero theorem proving the sign for equal-coupling face pairs;
- a precise statement that the unresolved minimal surface case is a
  soft/hard cross-class pair;
- the exact `-1/18` twice-wound SU(3) counterexample and `-1/24` recoupling
  coefficient as firewalls against an invalid generic Ginibre citation;
- the controlled cube scan as diagnostic evidence only.

The next theorem-grade target is not another undirected numerical scan.  It is
either (a) a total-positivity/score-covariance theorem for the SU(3) Wilson
character coefficients sufficient for the unequal-coupling sphere formula, or
(b) a signed-recouping estimate showing that the complete higher-dimensional
sum still has the one-sided defect comparison needed by G17.  Neither is
proved here.
