# M5 C-Form Envelope and Full-Channel Conversion

**Date:** June 12, 2026  
**Certificate:** `m5_cform_full_channel_certificate.py`  
**Certificate output:** `m5_cform_full_channel_certificate.json`

## 1. Exact M4 definitions

Let

\[
s=\frac{L}{4},
\qquad
m_0^2=\frac{1}{2s^2},
\qquad
a_W=\frac{\beta}{6},
\]

so that

\[
\mu^2:=\frac{m_0^2}{a_W}=\frac{3}{\beta s^2}.
\tag{1.1}
\]

For the four-dimensional lattice symbol

\[
\widehat\omega(n)
=
\sum_{\nu=1}^4 4\sin^2\!\left(\frac{\pi n_\nu}{L}\right),
\]

the coexact channel constant is

\[
T_C
=
\frac{3}{4L^4}
\sum_{n\ne0}
\bigl(m_0^2+a_W\widehat\omega(n)\bigr)^{-2}.
\tag{1.2}
\]

Factoring out \(a_W^{-2}\) gives

\[
T_C
=
\frac{1}{a_W^2}
\frac{3}{4L^4}
\sum_{n\ne0}
\bigl(\mu^2+\widehat\omega(n)\bigr)^{-2}.
\]

Define

\[
Y_L(\mu^2)
:=
\frac{3}{4L^4}
\sum_{n\ne0}
\bigl(\mu^2+\widehat\omega(n)\bigr)^{-2}.
\tag{1.3}
\]

Since \(a_W=\beta/6\),

\[
\boxed{T_C=\frac{36}{\beta^2}Y_L(\mu^2).}
\tag{1.4}
\]

Using

\[
(\mu^2+\lambda)^{-2}
=
\int_0^\infty t e^{-t(\mu^2+\lambda)}\,dt
\]

and the product heat kernel gives the exact representation

\[
Y_L(\mu^2)
=
\frac34\int_0^\infty
te^{-\mu^2t}
\left(q_L(t)^4-L^{-4}\right)dt.
\tag{1.5}
\]

Thus the heat-kernel comparison in Lemma A is exactly the comparison needed for the M4 coexact constant.

## 2. AF-diagonal renormalized quantity

Set

\[
x=\log s,
\qquad
\beta(x)=\beta_0+\gamma x,
\]

with

\[
\beta_0=\frac{28}{5},
\qquad
\gamma=\frac{11}{8\pi^2},
\qquad
A=\frac{3}{32\pi^2}.
\tag{2.1}
\]

Equation (1.1) becomes

\[
\mu^2(x)=\frac{3e^{-2x}}{\beta(x)},
\]

and therefore

\[
\log\frac1{\mu^2}
=
\log\beta+2x-\log3.
\tag{2.2}
\]

Define

\[
C_L(x)
:=
Y_L(\mu^2(x))
-Ax-\frac{A}{2}\log\beta(x),
\tag{2.3}
\]

and define \(C_\infty(x)\) by replacing \(Y_L\) with \(Y_\infty\).

Lemma A gives

\[
Y_L(\mu^2)\le Y_\infty(\mu^2),
\]

hence

\[
C_L(x)\le C_\infty(x).
\tag{2.4}
\]

Lemma B gives

\[
C_\infty(x)<\frac1{28}
\qquad(x\ge0).
\tag{2.5}
\]

Combining (2.3)--(2.5),

\[
Y_L(\mu^2(x))
<
Ax+\frac{A}{2}\log\beta(x)+\frac1{28}.
\tag{2.6}
\]

## 3. C-form envelope

For a general constant \(C\), define

\[
F_C(x)
:=
\frac{36}{\beta(x)^2}
\left(
Ax+\frac{A}{2}\log\beta(x)+C
\right).
\tag{3.1}
\]

Equations (1.4) and (2.6) imply

\[
T_C<F_{1/28}(x).
\tag{3.2}
\]

Let

\[
N_C(x)=Ax+\frac{A}{2}\log\beta(x)+C.
\]

A direct differentiation gives

\[
F_C'(x)
=-\frac{36A}{\beta(x)^3}D_C(\beta(x)),
\tag{3.3}
\]

where

\[
D_C(\beta)
=
\beta+\gamma\log\beta
-2\beta_0-\frac{\gamma}{2}
+\frac{2\gamma C}{A}.
\tag{3.4}
\]

Since

\[
D_C'(\beta)=1+\frac{\gamma}{\beta}>0,
\]

there is at most one stationary point. For \(C=1/28\), the directed certificate proves

\[
D_{1/28}(9.9)<0<D_{1/28}(10),
\]

so the unique maximizer satisfies

\[
9.9<\beta_*<10.
\tag{3.5}
\]

At the stationary point, equation \(D_C(\beta_*)=0\) is equivalent to

\[
2\gamma N_C(x_*)
=A\left(\beta_*+\frac{\gamma}{2}\right).
\]

Since

\[
\frac{A}{\gamma}=\frac{3}{44},
\]

the maximum is

\[
\overline T(C)
=
\frac{27}{22}
\frac{\beta_*+\gamma/2}{\beta_*^2}.
\tag{3.6}
\]

The function on the right of (3.6) is strictly decreasing for \(\beta>0\). By (3.5),

\[
\overline T(1/28)
<
\frac{27}{22}
\frac{9.9+\gamma/2}{9.9^2}.
\]

Directed interval evaluation gives

\[
\frac{27}{22}
\frac{9.9+\gamma/2}{9.9^2}
<
0.124839197517583
<
\frac18.
\tag{3.7}
\]

The numerical stationary values, included only for calibration, are

\[
\beta_*=9.902614271147116\ldots,
\]

\[
x_*=30.883709633966154\ldots,
\]

and

\[
\overline T(1/28)
=0.124806009996272\ldots.
\tag{3.8}
\]

Therefore

\[
\boxed{T_C<\frac18.}
\tag{3.9}
\]

## 4. Harmonic and full-channel conversion

The harmonic contribution is

\[
T_H
=
\frac{1}{(m_0^2)^2L^4}.
\tag{4.1}
\]

Using \(m_0^2=1/(2s^2)\) and \(L=4s\),

\[
(m_0^2)^2L^4
=
\frac{1}{4s^4}(4s)^4
=64.
\]

Hence

\[
\boxed{T_H=\frac1{64}.}
\tag{4.2}
\]

The full constant is

\[
T_{\mathrm{full}}=T_H+T_C.
\]

Equation (3.9) therefore yields

\[
\boxed{
T_{\mathrm{full}}
<
\frac1{64}+\frac18
=
\frac9{64}.
}
\tag{4.3}
\]

## 5. Integer thresholds

With the M4 definitions

\[
N_C^*=\left\lfloor\frac1{T_C}\right\rfloor,
\qquad
N^*=\left\lfloor\frac1{T_{\mathrm{full}}}\right\rfloor,
\]

the strict bounds imply

\[
\frac1{T_C}>8,
\qquad
\frac1{T_{\mathrm{full}}}>\frac{64}{9}>7.
\]

Thus

\[
\boxed{N_C^*\ge8,}
\qquad
\boxed{N^*\ge7.}
