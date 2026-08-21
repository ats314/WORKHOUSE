# SU(4) fourth-order exceptional-rank completion

**Status:** PASS  
**Version:** `2026-06-14-su4-hybrid-complete-v2`

## Complete exceptional corpus

The exact SU(4) N-ality scan introduces no new ordered words. The exceptional
sector is contained in 76 of the existing 4,171 ordered words and consists of

- 312 exceptional sign assignments;
- 156 charge-conjugation orbits;
- 96 distinct exceptional trace topologies;
- 1,806 exact local-channel choices, of which 214 contract nontrivially.

The finite-rank local algebra contains 42 oriented exceptional signatures and
78 exact rank-one joint Casimir channels. The allowed final Haar families are

\[
(4,0),\quad(0,4),\quad(5,1),\quad(1,5).
\]

Determinant singlet channels occur in the resolvent only at the third
des-Cloizeaux cut.

## Exact correction on the flat branch

The exceptional correction has 13 root-kernel entries and 39 cubic-completed
real-space entries. It is **not** a scalar multiple of the identity on the
complete three-component one-flux space.

Let

\[
\psi(k)=
\begin{pmatrix}
e^{ik_2}-1\\
-(e^{ik_1}-1)\\
e^{ik_0}-1
\end{pmatrix}.
\]

The exact Laurent-polynomial identity is

\[
\boxed{
H^{\rm exc}_{4,4}(k)\,\psi(k)
=
-\frac{304746539168}{160249753125}\,\psi(k)
}
\]

throughout the Brillouin zone. Hence the exceptional sector shifts the exact
flat branch by the momentum-independent amount

\[
\boxed{
\Delta q_4=-\frac{304746539168}{160249753125}
}
\]

while

\[
\boxed{\Delta A_4=\Delta B_4=0}.
\]

## Complete SU(4) coefficients

\[
\boxed{
q_4=
-\frac{162485785670299274695454289332603}
{121294607143027203361265133093750}
}
\]

\[
\boxed{A_4=\frac{32}{675}}
\]

\[
\boxed{
B_4=
\frac{3601925923737103752887}
{70481696720359496343750}
}
\]

and therefore

\[
\boxed{
\Delta c_{4,4}=A_4+B_4
=
\frac{2314426811641505637629}
{23493898906786498781250}
>0.
}
\]

The parity-point values obey

\[
c_X=q_4+A_4,\qquad
c_M=q_4+A_4+\frac12B_4,\qquad
c_R=q_4+A_4+B_4,
\]

and exactly

\[
\boxed{c_R-2c_M+c_X=0}.
\]

## Full dispersion theorem

For \(k\ne\Gamma\), with \(X_i=1-\cos k_i\),

\[
\boxed{
c_{4,4}(k)=q_4+
\frac{
A_4\sum_iX_i^2+
B_4\sum_{i<j}X_iX_j
}{2\sum_iX_i}
}
\]

with continuous extension \(c_{4,4}(\Gamma)=q_4\).

Because \(A_4>0\) and \(B_4>0\),

\[
\boxed{\Gamma\text{ is the unique global minimum}},
\qquad
\boxed{R\text{ is the unique global maximum}}.
\]

Thus the SU(4) fourth-order one-flux \(T_1^{+-}\) band is strictly
dispersive.

## Verification chain

- canonical symbolic source SHA-256:
  `8feec874aa16c823bb837efa8df626d5cf735db5ecaa6c90b8806ddf456b51a5`;
- exact balanced rerun: 3,850 trace topologies and 35,130 fusion paths;
- stable 4,171-word corpus reproduced;
- complete exceptional scan: 76 words and 156 C-orbits;
- all explicit epsilon/delta-epsilon Gram matrices verified;
- all 78 joint channel projectors factorized and normalized exactly;
- exact all-zone Laurent-polynomial residual:
  `(0,0,0)`;
- corrected kernel support: 63 root entries and 189 real-space entries.

## Correction to the preliminary interpretation

The preliminary statement
`Delta H_4,4(k)=Delta q_4 I_3` was too strong. The certified statement is the
flat-branch eigenvalue identity

\[
H^{\rm exc}_{4,4}(k)\psi(k)=\Delta q_4\psi(k).
\]

This distinction does not change \(q_4\), \(A_4\), \(B_4\), the bandwidth,
or the global extrema.
