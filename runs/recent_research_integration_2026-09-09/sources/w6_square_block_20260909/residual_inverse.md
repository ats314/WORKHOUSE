# Complete selected-inverse defect insertion on the square block

9 September 2026. Exact first residual coefficient with the actual
source-compatible full unitary jet fixed in [source.md](source.md).

## Definitions and the complete polynomial

Use the independent Gaussian vectors \(q,u,s,v\) from
[graph.md](graph.md), with component variances
\(\sqrt2,1/2,2,\sqrt6/4\) and frequencies
\(\sqrt2,2,2,\sqrt6\). Put

\[
a=|q|^2,\quad T=q\cdot(u\times s),\quad
\delta=\frac{2-4\sqrt2}{7},\quad m=4+\sqrt2,
\]

and

\[
A=\frac{2\sqrt2-1}{7},\quad
B=\frac{\sqrt2-4}{14},\quad
C=\frac{4-\sqrt2}{7},\quad D=\frac{\sqrt2}{4}.
\]

For the first retained excitation \(\phi_1=a-3\sqrt2\),

\[
t_1\phi_1=\delta T,\qquad u_0=F_0^{-1}t_1\phi_1=\delta T/m.
\]

The complete first transported operator gives \(W_1T=P\), where

\[
\begin{split}
P={}&2A|s|^2+2Ba-2Cq\cdot u\\
&+A\left[-\frac{\sqrt2}{4}(a|s|^2-(q\cdot s)^2)
               +(u\cdot s)^2-|u|^2|s|^2\right]\\
&+B\left[-a|u|^2+(q\cdot u)^2
               +\frac14((q\cdot s)^2-a|s|^2)\right]\\
&+\frac C4\left[(q\cdot u)|s|^2-(q\cdot s)(u\cdot s)\right]\\
&+\frac{D\sqrt6}{3}\left[2(q\cdot u)(v\cdot s)
                 -(q\cdot s)(v\cdot u)-(u\cdot s)(v\cdot q)\right].
\end{split}
\tag{R1}
\]

This includes the \(v\)-mode even though the first source force itself
does not contain it. Its omission would change the inverse norm.
The exact conditional projection is

\[
\mathbb E[P\mid q]=A(6-\sqrt2a).
\]

Consequently the first coefficient in
\(\rho_g=(F_g-F_0)F_0^{-1}t_1\phi_1\) is

\[
\boxed{
\rho_1=Q_0W_1u_0
=\frac{\delta}{m}\left[P+A\sqrt2(a-3\sqrt2)\right].
}
\tag{R2}
\]

## Exact full inverse for the first source

The residual has **66 nonzero Hermite components**, all with positive
fast degree, in total degrees two and four. In the ordering
\((n_q,n_u,n_s,n_v)\), their squared norms group as follows:

| Gaussian degrees | Squared norm |
|---|---|
| \((2,2,0,0)\), \((2,0,2,0)\), each | \((28674-19800\sqrt2)/117649\) |
| \((0,2,0,0)\), \((0,0,2,0)\), each | \((19116-13200\sqrt2)/117649\) |
| \((1,1,2,0)\) | \((-19800+14337\sqrt2)/117649\) |
| \((1,1,0,0)\) | \((-13200+9558\sqrt2)/117649\) |
| \((1,1,1,1)\) | \((-216\sqrt6+339\sqrt3)/2401\) |
| \((0,2,2,0)\) | \((114696-79200\sqrt2)/117649\) |

Divide each row by its full energy
\(\sqrt2 n_q+2n_u+2n_s+\sqrt6n_v\) and sum. The exact result is

\[
\boxed{
\begin{split}
\langle\rho_1,F_0^{-1}\rho_1\rangle
={}&\frac{346641}{285719}-\frac{976221\sqrt2}{1142876}
       -\frac{489\sqrt6}{1372}+\frac{174\sqrt3}{343}\\
={}&0.0108488157709989640977674212662\ldots.
\end{split}}
\tag{R3}
\]

Relative to \(b[\phi_1]=24\sqrt2\), this is
\(0.000319636299979872099261149372271\ldots\).
The inverse is verified by reconstructing every Hermite component and
checking \(F_0F_0^{-1}\rho_1=\rho_1\) as a full polynomial identity.

## All-radial-energy bound

For any retained radial polynomial \(\phi(a)\), let

\[
f=\phi',\qquad
\psi=\mathscr D^{-1}f,\qquad
\mathscr D=-8a\partial_a^2+(2\sqrt2a-20)\partial_a+m.
\]

The exact complete residual formula is

\[
\rho_1=\delta\big\{[P-A(6-\sqrt2a)]\psi
       +2A[a|s|^2-(q\cdot s)^2-T^2-2a]\psi'\big\}.
\tag{R4}
\]

The companion exact fast moment calculation gives, after radial
integration by parts,

\[
\|\rho_1\|^2
=\delta^2\mathbb E\left[
 (c_Ba-c_Aa^2)|\psi|^2+80c_Aa^2|\psi'|^2\right],
\tag{R5}
\]

where

\[
c_A=\frac{9-4\sqrt2}{49}>0,\qquad
c_B=-\frac{211}{98}+\frac{\sqrt6}{4}+\frac{134\sqrt2}{49}>0.
\]

For complex sources (R5) uses the real part of the integrated cross
term; the same identity and bounds apply. Write
\(d\mu(a)\propto a^{1/2}e^{-a/(2\sqrt2)}da\) and
\(d\nu=a\,d\mu\). On \(L^2(d\nu)\),

\[
S=\mathscr D-m
=-\nu^{-1}\partial_a(8a\nu\partial_a)\ge0,
\quad
\langle\psi,S\psi\rangle_{\nu}
=8\mathbb E[a^2|\psi'|^2].
\]

The spectral theorem gives the two estimates

\[
\mathbb E[a|\psi|^2]\le m^{-2}\mathbb E[a|f|^2],
\qquad
\mathbb E[a^2|\psi'|^2]
\le\frac1{32m}\mathbb E[a|f|^2],
\tag{R6}
\]

because \(x/(x+m)^2\le1/(4m)\) for \(x\ge0\).
The retained form is \(b[\phi]=8\mathbb E[a|f|^2]\).
Dropping only the nonpositive term \(-c_Aa^2|\psi|^2\) in (R5),

\[
\|\rho_1\|^2\le K b[\phi],\qquad
K=\frac{\delta^2}{8}
 \left[\frac{c_B}{m^2}+\frac{5c_A}{2m}\right]
=0.00378246491509140632588063375578\ldots<\frac1{256}.
\tag{R7}
\]

The full Gaussian fast operator has floor at least 2: conditioning
removes precisely states with no excitation in the fast modes, whose
lowest frequency is 2. Therefore

\[
\boxed{
\langle\rho_1,F_0^{-1}\rho_1\rangle
\le\tfrac12\|\rho_1\|^2
\le\frac1{512}b[\phi].
}
\tag{R8}
\]

This is an all-retained-energy estimate for the **complete first
residual coefficient**, obtained after the source force has first
passed through its full horizontal-plus-fast inverse. It does not use
an unweighted estimate on the original unsmoothed source force.

Radial polynomials are a form core for the Gaussian retained generator.
The bound (R7) defines a unique continuous residual map on its finite
energy form domain. The positive radial Friedrichs realization of
\(S+m\) defines \(\psi\) for every \(f\in L^2(d\nu)\). Thus the
polynomial identities extend in their stated form/inverse norms;
no pointwise derivative assumption on a general source is needed.

## First diagonal defect

For every radial source, \(u_0=F_0^{-1}t_1\phi\) is odd under the
simultaneous sign change of all four Gaussian vectors. The physical
operator \(W_1\) changes parity, so \(W_1u_0\) is even. Hence

\[
\boxed{\langle u_0,W_1u_0\rangle=0.}
\tag{R9}
\]

This removes the first diagonal coefficient in the selected-inverse
defect identity. Equations (R8) and (R9) concern the complete local
first transported jet. Controlling higher coefficients or the finite
coupling residual requires their corresponding estimates.

## Independent verification

[verify_residual.py](verify_residual.py) records **10 exact controls**
for the complete polynomial, projection, all Hermite components and
inverse equation. [verify_residual_audit.py](verify_residual_audit.py)
adds **12 exact controls** for the independent moment cross-check,
positive radial operator, resolvent estimate and a rational certificate
for \(K<1/256\). The full source normal form used in (R1) was audited
against all original operator coefficients by the source calculation.
