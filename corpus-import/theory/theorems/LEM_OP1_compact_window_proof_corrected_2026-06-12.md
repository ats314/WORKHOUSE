# Lemma A — Compact-Window Proof

**Date:** June 12, 2026  
**Certificate:** `m5_10_lemma_a_compact_certificate.py`  
**Certificate output:** `m5_10_lemma_a_compact_certificate.json`

## 1. Statement

For an integer \(L\ge 4\), define

\[
q(t):=e^{-2t}I_0(2t)
\]

and

\[
q_L(t)
:=
\frac1L\sum_{k=0}^{L-1}
\exp\!\left[-4t\sin^2\!\left(\frac{\pi k}{L}\right)\right].
\]

Let

\[
\tau:=\frac{t}{L^2}.
\]

Then, for every integer \(L\ge4\) and every

\[
0<\tau\le \frac25,
\]

one has

\[
\boxed{
q_L(t)^4-\frac1{L^4}\le q(t)^4.
}
\tag{1.1}
\]

Equivalently, with

\[
a_L(\tau):=Lq(\tau L^2),
\qquad
b_L(\tau):=Lq_L(\tau L^2),
\]

it is enough to prove

\[
F_L(\tau)
:=
1+a_L(\tau)^4-b_L(\tau)^4
\ge0.
\tag{1.2}
\]

The proof is divided at

\[
\tau_0=\frac1{25}=0.04.
\]

---

## 2. Exact image representation

For \(n\in\mathbb Z\), set

\[
p_t(n):=e^{-2t}I_n(2t).
\]

The Fourier representation is

\[
p_t(n)
=
\frac1{2\pi}
\int_{-\pi}^{\pi}
\exp\!\bigl[-2t(1-\cos\theta)\bigr]
 e^{-in\theta}\,d\theta.
\tag{2.1}
\]

The roots-of-unity filter gives

\[
\frac1L\sum_{k=0}^{L-1}
 e^{-4t\sin^2(\pi k/L)}
=
\sum_{j\in\mathbb Z}p_t(jL).
\]

Therefore

\[
q_L(t)
=
q(t)+2\sum_{j\ge1}p_t(jL).
\tag{2.2}
\]

This identity is exact.

---

## 3. Contour-shift image bound

Shift the contour in (2.1) from \(\theta\) to \(\theta-i\eta\), where \(\eta>0\). Taking absolute values gives

\[
p_t(n)
\le
q(t)
\exp\!\left[-n\eta+2t(\cosh\eta-1)\right].
\tag{3.1}
\]

The exponent is minimized at

\[
\sinh\eta=\frac{n}{2t}.
\]

Hence

\[
p_t(n)
\le
q(t)e^{-J(t,n)},
\tag{3.2}
\]

where

\[
J(t,n)
:=
 n\operatorname{arsinh}\!\left(\frac{n}{2t}\right)
-
2t\left(
\sqrt{1+\frac{n^2}{4t^2}}-1
\right).
\tag{3.3}
\]

For \(t=\tau L^2\), define

\[
J_{j,L}(\tau):=J(\tau L^2,jL),
\qquad
S_L(\tau):=\sum_{j\ge1}e^{-J_{j,L}(\tau)}.
\tag{3.4}
\]

For fixed \(t>0\), \(n\mapsto J(t,n)\) is the Legendre transform of
\(\eta\mapsto2t(\cosh\eta-1)\). Explicitly,

\[
\frac{\partial J}{\partial n}
=\operatorname{arsinh}\!\left(\frac{n}{2t}\right)>0,
\qquad
\frac{\partial^2J}{\partial n^2}
=\frac1{\sqrt{n^2+4t^2}}>0.
\]

Hence it is increasing and convex on \(n\ge0\), and the increments
\(J(t,(j+1)L)-J(t,jL)\) increase with \(j\). This justifies the
geometric tail enclosure used by the interval certificate after any finite
partial sum of \(S_L\).

Equations (2.2) and (3.2) imply

\[
b_L(\tau)
\le
 a_L(\tau)\bigl(1+2S_L(\tau)\bigr).
\tag{3.5}
\]

Let

\[
h(S):=(1+2S)^4-1.
\]

Then

\[
b_L(\tau)^4-a_L(\tau)^4
\le
 a_L(\tau)^4h(S_L(\tau)).
\tag{3.6}
\]

Thus the pre-mixing problem reduces to proving that the right side of (3.6) is less than one.

---

## 4. Monotonicity of the image rate

### 4.1 Dependence on \(\tau\)

Differentiating the optimized exponent gives

\[
-\tau\frac{\partial J_{j,L}}{\partial\tau}
=
2\tau L^2
\left(
\sqrt{1+\frac{j^2}{4\tau^2L^2}}-1
\right)
=:
E_{j,L}(\tau).
\tag{4.1}
\]

The quantity \(E_{j,L}(\tau)\):

- increases with \(j\);
- increases with \(L\);
- decreases with \(\tau\).

Indeed,

\[
E_{j,L}(\tau)
=
\frac{j^2}
{2\bigl(\sqrt{\tau^2+j^2/(4L^2)}+\tau\bigr)},
\tag{4.2}
\]

from which the three monotonicities follow directly.

Consequently, for \(j\ge1\), \(L\ge8\), and \(0<\tau\le1/25\),

\[
E_{j,L}(\tau)
\ge
E_{1,8}(1/25)
=
4.378126130979\ldots>2.
\tag{4.3}
\]

Since each summand in \(S_L\) has logarithmic derivative \(E_{j,L}\),

\[
\frac{d\log S_L}{d\log\tau}>2.
\tag{4.4}
\]

Because \(h\) is convex and \(h(0)=0\),

\[
S h'(S)\ge h(S),
\]

and therefore

\[
\frac{d\log h(S_L(\tau))}{d\log\tau}>2.
\tag{4.5}
\]

### 4.2 Dependence on \(L\)

Write

\[
x=\frac{j}{2\tau L}
\]

and

\[
\phi(x)=x\operatorname{arsinh}x-\sqrt{1+x^2}+1.
\]

Then

\[
J_{j,L}(\tau)=2\tau L^2\phi(x).
\]

A direct derivative gives

\[
\frac{\partial J_{j,L}}{\partial L}
=
2\tau L
\left[
 x\operatorname{arsinh}x
-2\bigl(\sqrt{1+x^2}-1\bigr)
\right].
\tag{4.6}
\]

Set

\[
G(x)
:=
 x\operatorname{arsinh}x
-2\bigl(\sqrt{1+x^2}-1\bigr).
\]

Then \(G(0)=0\) and

\[
G'(x)
=
\operatorname{arsinh}x-\frac{x}{\sqrt{1+x^2}}>0
\qquad(x>0).
\tag{4.7}
\]

Thus

\[
\frac{\partial J_{j,L}}{\partial L}>0,
\]

so \(S_L(\tau)\) decreases with \(L\).

---

## 5. Pre-mixing interval: \(0<\tau\le1/25\)

### 5.1 Uniform branch \(L\ge8\)

Using

\[
q(t)
=
\frac2\pi
\int_0^{\pi/2}e^{-4t\sin^2u}\,du
\]

and

\[
\sin u\ge\frac{2u}{\pi}
\qquad
(0\le u\le\pi/2),
\]

we obtain

\[
q(t)
\le
\frac2\pi
\int_0^\infty
e^{-16tu^2/\pi^2}\,du
=
\frac{\sqrt\pi}{4\sqrt t}.
\tag{5.1}
\]

Therefore

\[
a_L(\tau)
=Lq(\tau L^2)
\le
\frac{\sqrt\pi}{4\sqrt\tau}.
\tag{5.2}
\]

Combining (3.6) and (5.2),

\[
b_L^4-a_L^4
\le
\mathcal C_L(\tau)
:=
\frac{\pi^2}{256\tau^2}
 h(S_L(\tau)).
\tag{5.3}
\]

By (4.5), \(\mathcal C_L(\tau)\) increases with \(\tau\). By Section 4.2, it decreases with \(L\). Hence its maximum on

\[
L\ge8,
\qquad
0<\tau\le1/25
\]

occurs at \((L,\tau)=(8,1/25)\).

The interval certificate gives

\[
\mathcal C_8(1/25)
\le
0.836044301556099\ldots<1.
\tag{5.4}
\]

Thus

\[
F_L(\tau)>0
\qquad
(L\ge8,
0<\tau\le1/25).
\tag{5.5}
\]

The certified margin in (5.4) is

\[
1-\mathcal C_8(1/25)
\ge
0.163955698443901.
\]

### 5.2 Finite branch \(L=4,5,6,7\)

For each fixed \(L\), the certificate divides

\[
[10^{-12},1/25]
\]

into logarithmic cells. On a cell \([\alpha,\beta]\), monotonicity gives

\[
a_L(\tau)
\le a_L(\alpha),
\qquad
S_L(\tau)
\le S_L(\beta).
\]

Hence

\[
b_L(\tau)^4-a_L(\tau)^4
\le
 a_L(\alpha)^4h(S_L(\beta)).
\tag{5.6}
\]

All quantities in (5.6) are enclosed using directed interval arithmetic. The remaining interval \(0<\tau\le10^{-12}\) is covered by

\[
a_L(\tau)\le L,
\qquad
S_L(\tau)\le S_L(10^{-12}).
\tag{5.7}
\]

The certificate returns:

| \(L\) | largest certified cost upper bound |
|---:|---:|
| 4 | 0.893193750273 |
| 5 | 0.761189165295 |
| 6 | 0.501994942731 |
| 7 | 0.756916845979 |

Every bound is strictly below one. Therefore

\[
F_L(\tau)>0
\qquad
(L=4,5,6,7,
0<\tau\le1/25).
\tag{5.8}
\]

Combining (5.5) and (5.8) proves (1.1) on the complete pre-mixing interval.

---

## 6. Compact interval: \(1/25\le\tau\le2/5\)

### 6.1 Lower envelope for \(a_L\)

Using

\[
q(t)
=
\frac2\pi
\int_0^1
\frac{e^{-4tu^2}}{\sqrt{1-u^2}}\,du
\ge
\frac2\pi
\int_0^1e^{-4tu^2}\,du,
\]

we find

\[
q(t)
\ge
\frac{\operatorname{erf}(2\sqrt t)}{\sqrt{4\pi t}}.
\]

The standard bound

\[
\operatorname{erfc}z
\le
\frac{e^{-z^2}}{\sqrt\pi z}
\qquad(z>0)
\]

gives

\[
q(t)
\ge
\frac1{\sqrt{4\pi t}}
-
\frac{e^{-4t}}{4\pi t}.
\tag{6.1}
\]

For \(L\ge8\) and \(\tau\ge1/25\), the subtractive term is maximized at \((L,\tau)=(8,1/25)\). Thus

\[
a_L(\tau)
\ge
A(\tau)
:=
\frac1{\sqrt{4\pi\tau}}-\varepsilon_0,
\tag{6.2}
\]

where

\[
\varepsilon_0
=
\frac{25}{32\pi}e^{-256/25}.
\tag{6.3}
\]

### 6.2 Upper envelope for \(b_L\)

By symmetry,

\[
b_L(\tau)
=
\sum_{k=0}^{L-1}
\exp\!\left[-4\tau L^2
\sin^2\!\left(\frac{\pi k}{L}\right)\right].
\tag{6.4}
\]

For \(k=1,2,3,4\), use

\[
\sin x\ge x-\frac{x^3}{6}
=x\left(1-\frac{x^2}{6}\right).
\]

Since \(L\ge8\),

\[
L^2\sin^2\!\left(\frac{\pi k}{L}\right)
\ge
\pi^2k^2
\left(
1-\frac{\pi^2k^2}{6\cdot8^2}
\right)^2.
\tag{6.5}
\]

For \(5\le k\le L/2\), use

\[
\sin\!\left(\frac{\pi k}{L}\right)
\ge
\frac{2k}{L}.
\tag{6.6}
\]

After extending the positive tail to infinity, we obtain

\[
b_L(\tau)
\le
B(\tau),
\tag{6.7}
\]

where

\[
B(\tau)
:=
1
+
2\sum_{k=1}^{4}
\exp\!\left[
-4\pi^2\tau k^2
\left(
1-\frac{\pi^2k^2}{6\cdot8^2}
\right)^2
\right]
+
2\sum_{k=5}^{\infty}e^{-16\tau k^2}.
\tag{6.8}
\]

### 6.3 Uniform branch \(L\ge8\)

The functions \(A(\tau)\) and \(B(\tau)\) are decreasing. Therefore, on a cell

\[
\alpha\le\tau\le\beta,
\]

we have

\[
F_L(\tau)
\ge
1+A(\beta)^4-B(\alpha)^4.
\tag{6.9}
\]

Directed interval evaluation of (6.9) over an adaptive partition of

\[
[1/25,2/5]
\]

gives

\[
F_L(\tau)
\ge
0.006854458247992\ldots
\tag{6.10}
\]

for every \(L\ge8\) and every \(1/25\le\tau\le2/5\).

### 6.4 Finite branch \(L=4,5,6,7\)

For fixed \(L\), both \(a_L\) and \(b_L\) decrease with \(\tau\). Hence, on a cell \([\alpha,\beta]\),

\[
F_L(\tau)
\ge
1+a_L(\beta)^4-b_L(\alpha)^4.
\tag{6.11}
\]

The certificate evaluates (6.11) using interval enclosures of the positive \(I_0\) series and the finite Fourier sum. It returns:

| \(L\) | smallest certified cell lower bound |
|---:|---:|
| 4 | 0.004846293203062 |
| 5 | 0.01505592679824 |
| 6 | 0.04027666790649 |
| 7 | 0.04008793725959 |

Therefore

\[
F_L(\tau)>0
\qquad
(L=4,5,6,7,
1/25\le\tau\le2/5).
\tag{6.12}
\]

Combining (6.10) and (6.12) proves (1.1) throughout the compact interval.

---

## 7. Conclusion

Sections 5 and 6 cover

\[
0<\tau\le2/5.
\]

Thus, for every integer \(L\ge4\) and every \(t>0\) with \(t/L^2\le2/5\),

\[
\boxed{
q_L(t)^4-\frac1{L^4}\le q(t)^4.
}
\]

This closes the previously open compact-window part of Lemma A.

---

## 8. Integral corollary and interface with Region A

Define

\[
Y_L(\mu^2)
:=
\frac34
\int_0^\infty
 t e^{-\mu^2t}
\left(q_L(t)^4-\frac1{L^4}\right)
\,dt
\]

and

\[
Y_\infty(\mu^2)
:=
\frac34
\int_0^\infty
 t e^{-\mu^2t}q(t)^4\,dt.
\]

The present theorem proves the pointwise integrand comparison for

\[
0<t/L^2\le2/5.
\]

Combining it with the previously established Region-A estimate for

\[
t/L^2\ge2/5
\]

gives the global pointwise comparison

\[
q_L(t)^4-\frac1{L^4}\le q(t)^4
\qquad(t>0).
\]

Since the Laplace weight is nonnegative,

\[
\boxed{
Y_L(\mu^2)\le Y_\infty(\mu^2)
}
\qquad
(L\ge4,\ \mu^2>0).
\tag{8.1}
\]

Equation (8.1) is the finite-to-continuum comparison required in Lemma A.

---

## 9. Certificate architecture

The certificate uses:

1. 100-digit scalar arithmetic for cell endpoints;
2. 80-digit interval arithmetic for all transcendental evaluations;
3. an explicit outward pad on every scalar endpoint;
4. positive-series enclosures for \(I_0\);
5. geometric bounds for both the image tail and Gaussian Fourier tail;
6. adaptive subdivision until every cell has a strict directed-rounding margin.

The script records its SHA-256 hash in the JSON output.
