# Scale-matched SU(3) 1⁺⁻ ratio versus the continuum lattice spectrum

**Date:** 2026-06-14  
**Status:** diagnostic only; the fourth-order string-tension coefficient remains provisional pending the independent length/orbit audit.

## Lattice benchmark

The uploaded Athenodorou–Teper continuum table gives

\[
\boxed{M_{1^{+-}}/\sqrt\sigma=6.065(40)}.
\]

The Hamiltonian-limit mass datum gives

\[
2940(165)\,\mathrm{MeV}/485(6)\,\mathrm{MeV}
=6.061856\pm 0.348373.
\]

It differs from the continuum result by only `-0.009` combined standard deviations, so the continuum and Hamiltonian-limit targets are mutually consistent.

## Provisional ratio series

Using the exact glueball numerator and the provisional fourth-order string tension,

\[
\frac{m_{1^{+-}}(y)}{\sqrt{\sigma(y)}}
=
\sum_{n=0}^4 r_n y^n+O(y^5),
\]

with:

| order | exact coefficient | decimal |
|---:|---|---:|
| 0 | `4*sqrt(6)/3` | +3.265986323711 |
| 1 | `sqrt(6)/2` | +1.224744871392 |
| 2 | `11*sqrt(6)/68` | +0.396240987803 |
| 3 | `-82223*sqrt(6)/499392` | -0.403299202071 |
| 4 | `-95376133706950421293*sqrt(6)/72505902886024608000` | -3.222121950384 |

The strong-coupling anchor is

\[
R(0)=3.265986323711,
\]

whereas the continuum target is larger by a factor

\[
\frac{6.065}{R(0)}=1.857019.
\]

## Direct truncation test

The fourth-order polynomial has a unique positive stationary point at

\[
y_*=0.469077999523,
\qquad
R_4(y_*)=3.730048808620.
\]

This maximum is still `38.50%` below the continuum value. The polynomial equation

\[
R_4(y)=6.065
\]

has no positive real solution.

Therefore direct evaluation of the fourth-order polynomial cannot produce the continuum ratio.

## Padé diagnostics

| approximant | positive real poles | limit at \(y\to\infty\) | verdict |
|---|---|---:|---|
| [0/4] | none | 0.0 | pole-free but wrong asymptotic limit |
| [1/3] | 0.184573, 2.458196 | 0.0 | defective: positive-axis pole |
| [2/2] | 0.184911, 2.445704 | 0.2233488720120249 | defective: positive-axis pole |
| [3/1] | 0.125166 | ∞ | defective: positive-axis pole |

All near-diagonal Padé approximants are defective on the positive axis. The only pole-free fourth-order Padé tends to zero and therefore has the wrong continuum behavior.

## Dlog-Padé diagnostics

| approximant | positive real poles | verdict |
|---|---|---|
| [2/1] | 0.121381 | defective: positive-axis pole |
| [1/2] | 0.141926, 2.165467 | defective: positive-axis pole |
| [0/3] | none | pole-free but no stable continuum constant |

The Dlog sequence does not produce a stable pole-free continuation.

## Borel-Padé diagnostics

| Borel approximant | positive Borel-axis poles | verdict |
|---|---|---|
| [0/4] | none | pole-free but tends to zero |
| [1/3] | 0.568642 | ambiguous Borel integral |
| [2/2] | 1.017893, 3.838375 | ambiguous Borel integral |
| [3/1] | 0.500663 | ambiguous Borel integral |

The nontrivial near-diagonal Borel approximants have positive-axis singularities, making the Laplace integral prescription-dependent at this order.

## Conclusion

The new string-tension coefficient is sufficient to construct the first consistently scale-matched strong-coupling ratio, but **not** to extrapolate it to the continuum.

The data support three precise statements:

1. The correct physical target is \(M_{1^{+-}}/\sqrt\sigma=6.065\pm 0.040\).
2. The fourth-order series is internally stable only at small coupling; its direct polynomial peaks at \(R\approx 3.730\).
3. Standard Padé, Dlog-Padé, and Borel-Padé continuations fail the positive-axis pole and asymptotic-limit gates.

The minimum next requirement for a numerical continuum prediction is at least the fifth- and sixth-order ratio coefficients, preferably supplemented by one or more finite-coupling Hamiltonian anchor points. Shell-six mixing is also required before interpreting the isolated one-plaquette branch as the physical lowest \(1^{+-}\) state.
