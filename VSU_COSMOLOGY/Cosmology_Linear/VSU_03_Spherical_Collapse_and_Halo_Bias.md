# VSU Nonlinear Structure: Screening, Spherical Collapse, and Halo Bias (with an Exact Integral)

## Abstract

This note extracts the nonlinear-structure sector of VSU and sharpens one key result:

- spherical-collapse dynamics in the **unscreened** \(g\ll a_0\) regime,
- the *exact* collapse-time integral (including its numerical prefactor),
- the collapse-time ratio relative to Newtonian free fall,
- implications for a mass-/environment-dependent \(\delta_c\) and halo bias.

The main novelty here is that a MOND-like \(g\propto 1/r\) collapse law yields a **logarithmic energy integral**, so the collapse time is analytic and unusually sensitive to the initial Newtonian acceleration \(g_N\).

---

## 1. Two-phase nonlinear dynamics from the force law

For a spherical top-hat (pressureless) overdensity of mass \(M\) and physical radius \(r(t)\),
\[
\ddot r=-g(r).
\]

In VSU, the spherical force law is determined implicitly by
\[
g\,\mu\!\left(\frac{g}{a_0}\right)=\frac{GM}{r^2},
\qquad
\mu(x)=1-e^{-x}.
\]

Asymptotically:

- **Screened (Newtonian):** if \(g\gg a_0\), then \(g\simeq GM/r^2\).
- **Unscreened (stiffness/MOND-like):** if \(g\ll a_0\), then \(g\simeq \sqrt{GMa_0}/r\).

The transition radius is
\[
r_s=\sqrt{\frac{GM}{a_0}}.
\]
For \(r\gg r_s\) the motion is unscreened; for \(r\ll r_s\) it becomes Newtonian.

---

## 2. Newtonian free-fall time (benchmark)

For collapse from rest at \(r=r_i\) under \(\ddot r=-GM/r^2\),
\[
\boxed{
t_{\rm coll}^{\rm N}
=
\frac{\pi}{2\sqrt2}\,\frac{r_i^{3/2}}{\sqrt{GM}}.
}
\]

---

## 3. Unscreened collapse: exact energy integral and exact time

In the unscreened regime,
\[
\ddot r=-\frac{\sqrt{GMa_0}}{r}=: -\frac{A}{r},
\qquad A:=\sqrt{GMa_0}.
\]

Multiply by \(\dot r\) and integrate:
\[
\dot r\,\ddot r = -A\,\frac{\dot r}{r}
\quad\Rightarrow\quad
\frac12\dot r^2 = A\ln\!\left(\frac{r_i}{r}\right),
\]
where the integration constant is set by \(\dot r(r_i)=0\).

Therefore
\[
t_{\rm coll}^{\rm VSU}
=
\int_0^{r_i}\frac{dr}{\sqrt{2A\ln(r_i/r)}}.
\]

### 3.1 Exact evaluation

Use the substitution \(u=\ln(r_i/r)\) so \(r=r_ie^{-u}\) and \(dr=-r_ie^{-u}du\). Then
\[
t_{\rm coll}^{\rm VSU}
=
\frac{r_i}{\sqrt{2A}}
\int_0^\infty e^{-u}u^{-1/2}\,du
=
\frac{r_i}{\sqrt{2A}}\Gamma\!\left(\frac12\right)
=
\frac{r_i}{\sqrt{2A}}\sqrt{\pi}.
\]

Since \(A=\sqrt{GMa_0}\),
\[
\boxed{
t_{\rm coll}^{\rm VSU}
=
\sqrt{\frac{\pi}{2}}\,
\frac{r_i}{(GMa_0)^{1/4}}.
}
\]

**Dimensional sanity check:** \((GMa_0)^{1/4}\) has units of velocity, so \(r_i/(GMa_0)^{1/4}\) has units of time.

---

## 4. Collapse-time ratio: a clean, testable scaling

Define the initial Newtonian acceleration
\[
g_N:=\frac{GM}{r_i^2}.
\]

Then the ratio is
\[
\frac{t_{\rm coll}^{\rm VSU}}{t_{\rm coll}^{\rm N}}
=
\frac{\sqrt{\pi/2}\,r_i/(GMa_0)^{1/4}}{(\pi/2\sqrt2)\,r_i^{3/2}/\sqrt{GM}}
=
\boxed{
\frac{2}{\sqrt{\pi}}\left(\frac{g_N}{a_0}\right)^{1/4}.
}
\]

So in the genuinely unscreened regime \(g_N\ll a_0\), collapse is faster than Newtonian:
\[
t_{\rm coll}^{\rm VSU}\ll t_{\rm coll}^{\rm N}.
\]

### 4.1 Numerical feel (using the exact prefactor)

Below is the ratio \(\,t_{\rm coll}^{\rm VSU}/t_{\rm coll}^{\rm N}\,\) for a few values of \(g_N/a_0\) (note: the unscreened approximation is valid only for \(g_N/a_0\ll 1\)):

| \(g_N/a_0\) | \(t_{\rm VSU}/t_{\rm N}\) |
|---:|---:|
| \(10^{-8}\) | \(1.13\times 10^{-2}\) |
| \(10^{-6}\) | \(3.57\times 10^{-2}\) |
| \(10^{-4}\) | \(1.13\times 10^{-1}\) |
| \(10^{-2}\) | \(3.57\times 10^{-1}\) |
| \(1\) | \(1.13\) *(already outside unscreened validity)* |

---

### 4.2 Minimal numerical check code (reproducible)

```python
import math

def t_ratio(gN_over_a0: float) -> float:
    # Exact prefactor from the analytic integral (valid only in the unscreened regime gN/a0 << 1)
    return (2/math.sqrt(math.pi)) * (gN_over_a0**0.25)

for x in [1e-8, 1e-6, 1e-4, 1e-2, 1.0]:
    print(x, t_ratio(x))
```

Expected output (approximately):

```
1e-08 0.01128
1e-06 0.03568
0.0001 0.11284
0.01 0.35682
1.0 1.12838
```

(Again: the last line is *outside* the unscreened regime; screening should return the ratio toward \(\sim 1\).)

---

## 5. Toward a modified collapse threshold \(\delta_c(M,z)\)

In excursion-set and halo-model applications one often compresses nonlinear collapse physics into a “critical overdensity” \(\delta_c\), defined as the linearly extrapolated overdensity at the time of collapse.

A common *heuristic* mapping is:

- “shorter collapse time” \(\Rightarrow\) “smaller linear threshold.”

One can therefore posit (up to order-unity prefactors and with saturation to GR in the screened regime)
\[
\boxed{
\delta_c^{\rm VSU}(M,z)\sim
\delta_c^{\rm GR}\,
\min\!\left[1,\left(\frac{g_N(M,z)}{a_0}\right)^{1/4}\right].
}
\]
A more careful treatment would solve the full top-hat dynamics in an expanding background and then compute the linearly extrapolated density contrast explicitly.

### 5.1 Mass/redshift scaling (unscreened window only)

If one estimates \(r_i\propto (M/\bar\rho_m)^{1/3}\), then
\[
g_N=\frac{GM}{r_i^2}\propto G\,M^{1/3}\,\bar\rho_m^{2/3}.
\]
Since \(\bar\rho_m\propto (1+z)^3\),
\[
\left(\frac{g_N}{a_0}\right)^{1/4}\propto
M^{1/12}(1+z)^{1/2},
\]
**but this scaling only applies while \(g_N\ll a_0\)**. At sufficiently high \(z\) (or large \(M\)), the system becomes screened and \(\delta_c\to\delta_c^{\rm GR}\).

---

## 6. Halo bias: a mass- and environment-dependent prediction

In the simplest excursion-set expression, define peak height
\[
\nu(M,z):=\frac{\delta_c(M,z)}{\sigma(M,z)}.
\]
Then the Lagrangian bias is
\[
b_L(M,z)=\frac{\nu^2-1}{\delta_c},
\]
and the Eulerian bias is \(b_E=1+b_L\).

So any mass/environment dependence in \(\delta_c\) feeds directly into a **scale-dependent galaxy bias** once mapped through \(\sigma(M)\leftrightarrow P(k)\).

### 6.1 Key qualitative signature

- High-mass halos (large \(g_N\)): screened \(\Rightarrow\) GR-like bias.
- Low-mass halos in weak environments (small \(g_N\)): unscreened \(\Rightarrow\) altered \(\delta_c\) \(\Rightarrow\) systematically shifted bias.

Because the EFE is built in, the same halo mass can be biased differently depending on environment: a sharp and falsifiable target for data.

---

## 7. What to simulate next (minimal, high-payoff)

The analytic work suggests a very direct simulation program:

1. Implement the modified Poisson solve
   \[
   \nabla\!\cdot\!\bigl(\mu(|\nabla\Phi|/a_0)\nabla\Phi\bigr)=4\pi G\rho,
   \qquad \mu(x)=1-e^{-x},
   \]
   via multigrid or nonlinear conjugate gradients.

2. Measure:
   - collapse times for top-hat perturbations as a function of \(g_N/a_0\),
   - the effective \(\delta_c(M,z)\) from full dynamics,
   - halo mass function shifts and environment-dependent bias.

The clean scaling \(t_{\rm VSU}/t_{\rm N}\propto (g_N/a_0)^{1/4}\) is the “smoking gun” to check first.

