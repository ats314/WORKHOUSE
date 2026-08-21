# Glueball coupling-normalization audit

**Date:** 2026-06-14  
**Verdict:** the fourth-order contraction is correctly normalized in its actual computational variable, but the manuscript defines that variable incorrectly by a factor of four.

## Decisive identity

Let \(\beta\) denote the coefficient in

\[
H_\beta=
\frac12\sum_\ell C_2(\ell)+
\beta\sum_p\left(1-\frac13\operatorname{ReTr}U_p\right).
\]

After removing the additive constant,

\[
H_\beta=H_0-\frac{\beta}{6}
\sum_p(\chi_p+\bar\chi_p).
\]

The exact source chain contracts unit insertions of
\(-\chi_p-\bar\chi_p\). Therefore its natural series variable is

\[
\boxed{u=\frac{\beta}{6}}.
\]

The standard Hamiltonian convention has \(\beta=6/g_H^4\), hence

\[
\boxed{u=\frac1{g_H^4}}.
\]

The manuscript instead states

\[
Y=\frac{2\beta}{3}=4u.
\]

That statement is incompatible with the coefficients printed in the same manuscript.

## Independent one-plaquette bridge check

The local class coupling is one quarter of the lattice coupling:

\[
b=\frac{\beta}{4}.
\]

Using

\[
\Delta_-(b)=
\frac23+\frac b6+\frac1{18}b^2+\frac7{432}b^3+O(b^4),
\]

the four-link plaquette tower is

\[
4\Delta_-(\beta/4)=
\frac83+\frac{\beta}{6}+\frac{\beta^2}{72}
+\frac{7\beta^3}{6912}+O(\beta^4).
\]

In \(u=\beta/6\) this is exactly

\[
\boxed{
\frac83+u+\frac12u^2+\frac7{32}u^3+O(u^4)
},
\]

which is the tower used by the source chain.

In the manuscript's written variable \(Y=2\beta/3\), the same tower would be

\[
\frac83+\frac14Y+\frac1{32}Y^2+
\frac7{2048}Y^3+O(Y^4),
\]

not the displayed \(8/3+Y+(1/2)Y^2+(7/32)Y^3\).

## Source-chain trace

Stage 3I forms the rooted fourth-order weight as

```text
rooted_odd = odd_signed_multiplicity * accumulator["complete_odd"]
```

and Stage 3J inserts it directly into the real-space kernel:

```text
amplitude = Fraction(word["canonical_complete_sum_odd"])
```

There is no later \(1/256\) multiplier. This is correct for \(u=\beta/6\),
because the Hamiltonian perturbation is \(-u(\chi+\bar\chi)\).

It would be wrong only if the fourth-order numbers were labeled as coefficients
of \(Y^4\) with \(Y=2\beta/3\).

## Coefficient conversion

Let \(Y=4u\). The existing coefficients and their representation in the old
written variable are:

| order | coefficient of `u^n` | coefficient of `Y^n` |
|---:|---:|---:|
| 0 | `8/3` | `8/3` |
| 1 | `1` | `1/4` |
| 2 | `11/306` | `11/4896` |
| 3 | `-109151/249696` | `-109151/15980544` |
| 4 | `-20721577909065127111/7250590288602460800` | `-20721577909065127111/1856151113882229964800` |

The fourth-order shape coefficients transform as

\[
A_Y=\frac{A_u}{256}=5/3072,
\qquad
B_Y=\frac{B_u}{256}=17607806155349/70484966730547200.
\]

The location of the band edges, positivity, factorization, and the order at
which dispersion first appears are unchanged by this rescaling.

## KPS string tension in the same variable

KPS use

\[
x=\frac2{g_H^4}=2u.
\]

Because the project dimensionless Hamiltonian is one half of the KPS bracket,

\[
\boxed{\sigma(u)=\frac12W(2u)}.
\]

| order | coefficient of `u^n` | coefficient of old `Y^n` |
|---:|---:|---:|
| 0 | `2/3` | `2/3` |
| 1 | `0` | `0` |
| 2 | `-22/153` | `-11/1224` |
| 3 | `-61/408` | `-61/26112` |
| 4 | `-737327120374220449/7250590288602460800` | `-737327120374220449/1856151113882229964800` |
| 5 | `-137767222189182735950309/2009803206414863779920000` | `-137767222189182735950309/2058038483368820510638080000` |
| 6 | `-13130661661034190772935959348816444649800714410750015999/168641444007491247688836385300053017225944999004544000000` | `-13130661661034190772935959348816444649800714410750015999/690755354654684150533473834189017158557470715922612224000000` |

In particular,

\[
\sigma_3(u)=-\frac{61}{408},
\qquad
\sigma_5(u)=-137767222189182735950309/2009803206414863779920000.
\]

The positive odd coefficients obtained from \(W(-2u)\) are not physical; the
coupling conversion has no sign reversal.

## Correct coherent ratio template

Keeping the existing glueball coefficients means using \(u\), not the old
written \(Y\). Then

\[
\frac{m_{1^{+-}}(u)}{\sqrt{\sigma(u)}}
=
\sqrt6\sum_{n=0}^6 c_nu^n+O(u^7),
\]

with

\[
c_0=4/3,\quad
c_1=1/2,\quad
c_2=11/68,\quad
c_3=-7559/499392,\quad
c_4=-15752822901180179/12642703205932800,
\]

\[
\boxed{c_5=\frac{m_{5}}{2} + \frac{108889196164826769179507}{765639316729471916160000}},
\qquad
\boxed{c_6=\frac{m_{6}}{2} + \frac{1181646977233006828729169209802562361069278851250351799}{168641444007491247688836385300053017225944999004544000000}}.
\]

## Required correction

The least disruptive repair is

\[
\boxed{y:=\beta/6=1/g_H^4}
\]

throughout the glueball paper. All computed coefficients then remain unchanged.

The alternative is to retain \(Y=2\beta/3\), but then every order-\(n\)
coefficient, including all \(q_N,A_N,B_N\), must be divided by \(4^n\).

## Status

\[
\boxed{\text{Fourth-order geometry and contraction: unchanged}}
\]

\[
\boxed{\text{Fourth-order coefficients: valid in }u=\beta/6}
\]

\[
\boxed{\text{Manuscript equation }y=2\beta/3\text{: incorrect}}
\]
