# Exact shell-six O(u²) spectrum and shell-four/shell-six coupling

## Convention

\[
u=\frac{\beta_{\rm lat}}6=\frac1{g^4},
\qquad
H=H_0-uW.
\]

A common disconnected vacuum scalar is omitted from the shell-six second-order
matrix. It cancels in channel differences and does not affect ordering.

## Shell-six C-odd spectrum

The first-order-flat exotic channels split at second order as follows:

\[
\begin{aligned}
0^{--}\;(A_1^{--}):\quad&
-\frac{6117632}{479655}u^2,\\
3^{+-}\;(A_2^{+-}):\quad&
-\frac{21281}{1530}u^2,\\
2^{--}\;(E^{--}):\quad&
-\frac{6597287}{479655}u^2,\\
2^{--}\;(T_2^{--}):\quad&
-\frac{6277517}{479655}u^2.
\end{aligned}
\]

The two \(T_2^{+-}\) multiplicity branches have coefficients

\[
-\frac{27013849}{1918620}
\pm\frac{\sqrt{59782141}}{9180}.
\]

The lower one is the lowest among the channels that remain flat at first
order.

The shell-six \(T_1^{+-}\) branches are

\[
\begin{aligned}
E_{6,-}(u)
&=
4-\frac{2\sqrt2}{3}u
+\left(
-\frac{13029053}{959310}-\frac{\sqrt2}{2}
\right)u^2+O(u^3),\\
E_{6,0}(u)
&=
4-\frac{52959}{3553}u^2+O(u^3),\\
E_{6,+}(u)
&=
4+\frac{2\sqrt2}{3}u
+\left(
-\frac{13029053}{959310}+\frac{\sqrt2}{2}
\right)u^2+O(u^3).
\end{aligned}
\]

In particular,

\[
E_{3^{+-}}-E_{0^{--}}
=
-\frac{1107923}{959310}u^2+O(u^3),
\]

so \(3^{+-}\) lies below \(0^{--}\) at second order.

## Exact shell-four/shell-six first-order coupling

The exact cross-shell matrix has 60 nonzero oriented entries, each
\(-1/3\) or \(-2/3\), and is Hermitian under the independently computed
reverse action.

After projection to \(T_1^{+-}\),

\[
g_-^2=\frac49,\qquad
g_0^2=\frac89,\qquad
g_+^2=\frac49,
\]

so

\[
g_{\rm total}^2=\frac{16}{9}.
\]

## Unfolded O(u²) normal form

The published shell-four coefficient

\[
m_2=\frac{11}{306}
\]

already contains virtual shell-six propagation. Explicitly,

\[
\Delta m_2^{(6)}
=
-\frac34g_{\rm total}^2
=
-\frac43.
\]

Therefore the shell-four diagonal used in an explicit coupled-shell
Hamiltonian is

\[
m_{2,\rm unfolded}
=
\frac{11}{306}+\frac43
=
\frac{419}{306}.
\]

Likewise, the shell-six folded second-order coefficients must have the
virtual shell-four terms \(3g_i^2/4\) removed. The resulting normal-form
diagonal is

\[
\begin{aligned}
\mu_-^{\rm unfolded}
&=
-\frac{13348823}{959310}-\frac{\sqrt2}{2},\\
\mu_0^{\rm unfolded}
&=
-\frac{165983}{10659},\\
\mu_+^{\rm unfolded}
&=
-\frac{13348823}{959310}+\frac{\sqrt2}{2}.
\end{aligned}
\]

In the positive-coupling phase convention, the coupled normal form through
second order is

\[
H_{\rm normal}(u)=
\begin{pmatrix}
\frac83+u+\frac{419}{306}u^2
&\frac23u&\frac{2\sqrt2}{3}u&\frac23u\\
\frac23u
&4-\frac{2\sqrt2}{3}u+\mu_-^{\rm unfolded}u^2&0&0\\
\frac{2\sqrt2}{3}u
&0&4+\mu_0^{\rm unfolded}u^2&0\\
\frac23u
&0&0&4+\frac{2\sqrt2}{3}u+\mu_+^{\rm unfolded}u^2
\end{pmatrix}
+O(u^3).
\]

This normal form exactly reproduces the folded shell-four and shell-six
second-order coefficients when either shell is perturbatively eliminated.
Cross-shell matrix elements at order \(u^2\) are not yet included.

The accompanying finite-\(u\) scan is diagnostic only. It is not a controlled
continuum extrapolation.
