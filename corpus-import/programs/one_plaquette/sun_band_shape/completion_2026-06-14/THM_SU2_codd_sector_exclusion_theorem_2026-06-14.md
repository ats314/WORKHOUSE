# SU(2) exclusion of the C-odd one-flux branch

**Status:** proved by exact group identities.  
**Date:** June 14, 2026.

Let

\[
\varepsilon=i\sigma_2=
\begin{pmatrix}0&1\\-1&0\end{pmatrix}\in SU(2).
\]

Every fundamental matrix can be written

\[
U=
\begin{pmatrix}
a_0+i a_3 & a_2+i a_1\\
-a_2+i a_1 & a_0-i a_3
\end{pmatrix},
\qquad \sum_\mu a_\mu^2=1.
\]

Direct multiplication gives

\[
\boxed{U^*=\varepsilon U\varepsilon^{-1}}.
\]

For a lattice configuration, choose the constant gauge transformation
\(g_x=\varepsilon\) at every vertex. Then every oriented link transforms as

\[
U_{xy}\longmapsto g_xU_{xy}g_y^{-1}
=\varepsilon U_{xy}\varepsilon^{-1}=U_{xy}^*.
\]

Thus charge conjugation is a gauge transformation in pure \(SU(2)\) gauge
theory. Gauge transformations act trivially on the physical Hilbert space, so

\[
\boxed{C=I},\qquad
\boxed{P_{C=-}=\frac{I-C}{2}=0}.
\]

Equivalently, the fundamental character is real,

\[
\chi_{1/2}(U)=\operatorname{Tr}U=2a_0
=\chi_{1/2}(U^*),
\]

and the antisymmetrized fundamental/antifundamental plaquette excitation
vanishes identically. The local class-function statement is the same:
for traceless Hermitian \(2\times2\) matrices, \(\operatorname{Tr}X^3=0\).

## Theorem-status consequence

\[
\boxed{\text{There is no }SU(2)\;T_1^{+-}\text{ one-flux branch.}}
\]

Therefore \(A_2\), \(B_2\), and \(q_2\) are not missing coefficients of
this band; they are undefined because the \(C=-\) sector is zero. The
nontrivial theorem domain \(SU(N), N\ge3\) is maximal.

Machine-readable certificate SHA-256: `a08813386b498e274bc374b6e8da0ed7c3199f1166598d6b2b692734d60796a1`.
