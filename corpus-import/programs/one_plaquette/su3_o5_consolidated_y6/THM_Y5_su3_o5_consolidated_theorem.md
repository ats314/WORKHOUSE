# Consolidated SU(3) result through fifth order

**Date:** 2026-06-14  
**Status:** PASS  
**Expansion variable:**

\[
\boxed{u=\frac{\beta_{\rm lat}}6=\frac1{g_H^4}}.
\]

This document merges the verified fifth-order glueball calculation with the
normalization-corrected string-tension certificate. It also records the first
completed sixth-order component: the exact folded/des-Cloizeaux path weights.

## 1. Exact one-flux C-odd rest mass through \(O(u^5)\)

\[
\boxed{
\begin{aligned}
m_{1^{+-}}(u)={}&\frac83+u+\frac{11}{306}u^2
-\frac{109151}{249696}u^3\\
&-\frac{20721577909065127111}{7250590288602460800}u^4\\
&-\frac{866236750503342026253096691057}
{1169668083793811403447133488000}u^5+O(u^6).
\end{aligned}}
\]

Thus

\[
\boxed{m_5=-\frac{866236750503342026253096691057}
{1169668083793811403447133488000}}
\approx-0.740583386437038.
\]

This is project-native and independently verified from the complete
five-insertion contraction.

## 2. Exact fifth-order band coefficient

For \(X_i=1-\cos k_i\), \(S=\sum_iX_i\),
\(Q=\sum_iX_i^2\), and \(R=\sum_{i<j}X_iX_j\),

\[
\boxed{c_5(k)=q_5+\frac{A_5Q+B_5R}{2S}},
\]

with

\[
q_5=m_5,\qquad A_5=\frac{313}{240},\qquad
B_5=\frac{1881863087742908605903793}
{1652932248975967181040000}.
\]

Both shape coefficients are positive. The fifth-order coefficient therefore
has its unique minimum at \(\Gamma\), its unique maximum at \(R\), and exact
bandwidth

\[
\boxed{\Delta c_5=A_5+B_5=
\frac{4037562229115732471176793}
{1652932248975967181040000}}.
\]

## 3. Normalization-corrected string tension

The project-native result is

\[
\boxed{
\sigma(u)=\frac23-\frac{22}{153}u^2-\frac{61}{408}u^3
-\frac{737327120374220449}{7250590288602460800}u^4+O(u^5)}.
\]

The exact historical KPS targets in the same variable are

\[
\sigma_5=-\frac{137767222189182735950309}
{2009803206414863779920000},
\]

\[
\sigma_6=-\frac{
13130661661034190772935959348816444649800714410750015999}
{168641444007491247688836385300053017225944999004544000000}.
\]

These two coefficients are not yet project-native reruns. The correct bridge is

\[
\boxed{\sigma(u)=\frac12W(2u)}.
\]

The older \((-1/4)^n\) conversion belongs to a superseded mixed-variable
normalization and must not be combined with the glueball coefficients above.

## 4. Mass-to-string-tension ratio through fifth order

Using the exact historical \(\sigma_5\) target,

\[
\boxed{
\frac{m_{1^{+-}}(u)}{\sqrt{\sigma(u)}}
=\sqrt6\sum_{n=0}^{5}c_nu^n+O(u^6)},
\]

where

\[
\begin{aligned}
c_0&=\frac43,&c_1&=\frac12,&c_2&=\frac{11}{68},\\
c_3&=-\frac{7559}{499392},&
c_4&=-\frac{15752822901180179}{12642703205932800},\\
c_5&=-\frac{10670728893034386567182468628311}
{46786723351752456137885339520000}.
\end{aligned}
\]

Numerically,

\[
c_5\approx-0.228071729084544,
\qquad \sqrt6\,c_5\approx-0.558659361011414.
\]

At sixth order the ratio coefficient is

\[
\boxed{
c_6=\frac{m_6}{2}+
\frac{1181646977233006828729169209802562361069278851250351799}
{168641444007491247688836385300053017225944999004544000000}}.
\]

Therefore the only unknown numerator needed for the ratio through \(O(u^6)\)
is \(m_6\).

## 5. Sixth-order progress completed here

The folded/des-Cloizeaux recurrence used by the fifth-order engine is
order-generic. It has now been checked at six insertions by:

- all 32 zero/nonzero intermediate-denominator patterns;
- exact path-reversal symmetry;
- the nonresonant resolvent-product limit;
- four independent rational-matrix comparisons between the full
  Rayleigh-Schrödinger coefficient and the sum of folded ordered paths.

All gates pass. Folded terms are no longer an unresolved part of the \(m_6\)
calculation.

## 6. Best execution path for \(m_6\)

The efficient target is the scalar zero-momentum coefficient
\(q_6=m_6\), not the full sixth-order dispersion.

1. Enumerate connected six-insertion supports with external-memory sharding;
   the fifth-order census already contains 6,676,658 support classes, so a
   monolithic in-memory sixth-order expansion is the wrong architecture.
2. Apply triality and charge-conjugation reduction before global tensor
   contraction.
3. Replace hand-enumerated determinant cases with the fusion-path basis as the
   primary local basis. Sixth order can introduce degree-eight links and
   double-epsilon sectors absent at fifth order.
4. Contract only the zero-momentum trace first. Construct the full
   189-record-or-larger real-space kernel only after \(m_6\) is fixed.

This path directly closes the physical ratio while avoiding unnecessary
sixth-order band-shape work.

## 7. Universal sixth-order local carrier census

The full eight-event token space contains \(3^8-1=6560\) nonzero local link
signatures. Exact SU(3) fusion from the singlet back to the singlet leaves
2,186 feasible signatures. Their canonical \((n_f,n_{\bar f})\) sectors are

\[
(0,3),(0,6),(1,1),(1,4),(1,7),(2,2),(2,5),(3,3),(4,4).
\]

The new sixth-order sectors are the balanced degree-eight sector \((4,4)\)
and the double-determinant sectors \((0,6)\) and \((1,7)\). The largest
singlet fusion-path multiplicity is 23; the largest intermediate irrep
encountered in the universal census has dimension 27.

This proves that the fusion-path representation can carry every possible
sixth-order local sector without hand-selecting epsilon-delta cases. What
remains is to construct normalized edge tensors and projectors only for the
subset of signatures realized by the connected geometry census.
