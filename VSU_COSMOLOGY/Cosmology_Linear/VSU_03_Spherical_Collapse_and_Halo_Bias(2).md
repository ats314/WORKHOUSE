# VSU 03 — Spherical Collapse, an Exact Collapse-Time Integral, and Halo Bias

**Scope.** This note sharpens the nonlinear structure-formation sector of VSU:

- spherical-collapse dynamics implied by the VSU force law,
- the **exact** collapse-time integral (including the numerical prefactor) in the unscreened regime,
- the collapse-time ratio relative to Newtonian free fall,
- implications for a mass-/environment-dependent collapse threshold \(\delta_c(M,z)\) and halo bias.

**Primary sources:** `05.2_Spherical_Collapse.md`, `05.3_Halo_Bias.md`, plus the force-law inputs in `02.1_Force_Law_and_Asymptotics.md`.

---

## 1. Setup: top-hat collapse with a modified force law

Consider a pressureless spherical overdensity of total mass \(M\) and physical radius \(r(t)\), neglecting shell crossing. The radial equation of motion is

\[
\ddot r = -g(r).
\]

VSU’s spherical force law is fixed implicitly by

\[
g(r)\,\mu\!\left(\frac{g(r)}{a_0}\right) = \frac{GM}{r^2},
\qquad
\mu(x)=1-e^{-x}.
\]

Asymptotically (`02.1_Force_Law_and_Asymptotics.md`):

- **Screened / strong-field:** \(g\gg a_0\Rightarrow g\simeq GM/r^2\).
- **Unscreened / weak-field:** \(g\ll a_0\Rightarrow g\simeq \sqrt{GMa_0}/r\).

The transition occurs near the screening radius

\[
\boxed{r_s=\sqrt{\frac{GM}{a_0}}.}
\]

---

## 2. Newtonian benchmark: free-fall time from rest

For Newtonian collapse from rest at \(r=r_i\),

\[
\ddot r = -\frac{GM}{r^2},
\]

the standard free-fall time is

\[
\boxed{
t_{\rm coll}^{\rm N}
=
\frac{\pi}{2\sqrt2}\,\frac{r_i^{3/2}}{\sqrt{GM}}.
}
\]

(This matches `05.2_Spherical_Collapse.md`.)

---

## 3. Unscreened VSU collapse: exact energy integral and exact time

In the unscreened regime (\(g\ll a_0\)) we have

\[
\ddot r = -\frac{\sqrt{GMa_0}}{r} =: -\frac{A}{r},
\qquad A:=\sqrt{GMa_0}.
\]

Multiply by \(\dot r\) and integrate:

\[
\dot r\,\ddot r = -A\,\frac{\dot r}{r}
\quad\Rightarrow\quad
\frac12\dot r^2 = A\ln\!\left(\frac{r_i}{r}\right),
\]
where \(\dot r(r_i)=0\) fixes the integration constant.

Therefore the collapse time is

\[
t_{\rm coll}^{\rm VSU}
=
\int_0^{r_i}\frac{dr}{\sqrt{2A\ln(r_i/r)}}.
\]

### 3.1 Exact evaluation (prefactor included)

Let \(u=\ln(r_i/r)\), so \(r=r_ie^{-u}\) and \(dr=-r_ie^{-u}du\). Then

\[
t_{\rm coll}^{\rm VSU}
=
\frac{r_i}{\sqrt{2A}}\int_0^\infty e^{-u}u^{-1/2}\,du
=
\frac{r_i}{\sqrt{2A}}\Gamma\!\left(\frac12\right)
=
\boxed{
\sqrt{\frac{\pi}{2}}\,
\frac{r_i}{(GMa_0)^{1/4}}.
}
\]

**Important correction vs the current project file.**  
`05.2_Spherical_Collapse.md` states only a proportionality and (as written) gives
\[
t_{\rm coll}^{\rm VSU}\propto \frac{r_i^{3/2}}{(GMa_0)^{1/4}},
\]
which is dimensionally inconsistent. The exact integral above fixes both the scaling (\(\propto r_i\)) and the numerical prefactor.

---

## 4. Collapse-time ratio and clean scaling

Define the initial Newtonian acceleration
\[
g_N:=\frac{GM}{r_i^2}.
\]

Then the ratio of unscreened VSU collapse time to Newtonian free fall is

\[
\boxed{
\frac{t_{\rm coll}^{\rm VSU}}{t_{\rm coll}^{\rm N}}
=
\frac{2}{\sqrt{\pi}}\left(\frac{g_N}{a_0}\right)^{1/4}.
}
\]

So in the genuinely unscreened regime \(g_N\ll a_0\), collapse is parametrically faster than Newtonian:
\[
t_{\rm coll}^{\rm VSU}\ll t_{\rm coll}^{\rm N}.
\]

---

## 5. Two-phase collapse (screening “turns on” during infall)

Even if collapse begins unscreened at large \(r\), it will typically enter a screened inner phase once \(r\lesssim r_s\). Thus collapse proceeds in two phases:

1. **Outer phase:** unscreened, \(g\simeq \sqrt{GMa_0}/r\).
2. **Inner phase:** screened, \(g\simeq GM/r^2\).

This is the nonlinear structure-formation analogue of “GR in the interior, modified gravity in the outskirts.”

---

## 6. Implications for \(\delta_c(M,z)\) and halo bias

The project proposes encoding “faster nonlinear collapse ⇒ smaller linear threshold” via

\[
\delta_c^{\rm VSU}(M,z)
=
\delta_c^{\rm GR}\left(\frac{g_N(M,z)}{a_0}\right)^{1/4},
\qquad
\delta_c^{\rm GR}\simeq 1.686.
\]

Two refinements are worth making explicit:

1. **Screened saturation:** in the screened regime \(g_N\gg a_0\), collapse should revert to GR, so it is natural to impose
   \[
   \delta_c^{\rm VSU}(M,z)\simeq \delta_c^{\rm GR}\,\min\!\left[1,\left(\frac{g_N}{a_0}\right)^{1/4}\right].
   \]
2. **Environment dependence:** \(g_N\) is not purely “mass-only” in a nonlinear theory—external fields (EFE) can effectively raise the background acceleration scale, pushing halos toward the screened limit.

Given \(\delta_c(M,z)\), excursion-set bias follows (`05.3_Halo_Bias.md`):

\[
\nu(M,z)=\frac{\delta_c(M,z)}{\sigma(M,z)},\qquad
b_L=\frac{\nu^2-1}{\delta_c},\qquad
b_E=1+b_L.
\]

A mass-/environment-dependent \(\delta_c\) thus predicts a distinctive bias signature.

---

## 7. Minimal numerical check (not in the project files): full-\(\mu\) collapse time

The exact result above assumes the **pure unscreened** force law \(g=A/r\).  
But in full VSU collapse, the implicit relation
\[
g(1-e^{-g/a_0})=\frac{GM}{r^2}
\]
causes a transition to Newtonian behavior at small \(r\).

A simple energy-integral computation (solve the implicit \(g(r)\) by Newton iteration, then integrate \(t=\int dr/\sqrt{2\int g\,dr}\)) gives:

| \(g_N/a_0\) (initial) | \(r_i\) (for \(GM=a_0=1\)) | \(t_{\rm coll}^{\rm full}\) | \(t_{\rm coll}^{\rm N}\) | ratio \(t_{\rm full}/t_N\) | unscreened asymptotic \( \frac{2}{\sqrt{\pi}}(g_N/a_0)^{1/4}\) |
|---:|---:|---:|---:|---:|---:|
| \(10^{-4}\) | 100 | 122.2 | 1111 | 0.1100 | 0.1128 |
| \(10^{-3}\) | 31.62 | 38.49 | 197.5 | 0.1949 | 0.2007 |
| \(10^{-2}\) | 10 | 12.00 | 35.12 | 0.3418 | 0.3568 |
| \(10^{-1}\) | 3.162 | 3.625 | 6.246 | 0.5803 | 0.6345 |
| \(1\) | 1 | 0.9777 | 1.111 | 0.8802 | 1.128 |

As expected, the asymptotic scaling is accurate for \(g_N/a_0\ll 1\) and breaks down near the transition.

### 7.1 Reproducible Python (minimal)

```python
import numpy as np, math

a0 = 1.0
GM = 1.0

def g_from_gN(gN, tol=1e-12, maxit=50):
    gN = np.asarray(gN, dtype=float)
    g  = np.where(gN < 1.0, np.sqrt(gN), gN)      # initial guess
    for _ in range(maxit):
        expm = np.exp(-g/a0)
        f    = g*(1-expm) - gN
        fp   = 1 - expm + (g/a0)*expm
        step = f/fp
        gnew = g - step
        gnew = np.where(gnew > 0, gnew, 0.5*g)    # keep positive
        if np.max(np.abs(step)/(gnew+1e-30)) < tol:
            return gnew
        g = gnew
    return g

def collapse_time_full(r_i, ngrid=30000, r_min=1e-8):
    r  = np.geomspace(r_min, r_i, ngrid)
    gN = GM / r**2
    g  = g_from_gN(gN)
    # cumulative integral of g dr from small r upward
    Icum = np.cumsum((g[1:]+g[:-1])*(r[1:]-r[:-1])/2)
    Icum = np.concatenate([[0.0], Icum])
    Itot = Icum[-1]
    I    = Itot - Icum                           # ∫_r^{r_i} g dr
    integrand      = 1/np.sqrt(2*I)
    integrand[-1]  = 0.0                          # endpoint
    return np.trapz(integrand, r)

def t_newton(r_i):
    return math.pi/(2*math.sqrt(2)) * r_i**1.5 / math.sqrt(GM)

# example: gN/a0 = 1e-4 ⇒ r_i = 100
r_i   = 100.0
tfull = collapse_time_full(r_i)
tN    = t_newton(r_i)
print("ratio =", tfull/tN)
```

---

## References (project files)

- `02.1_Force_Law_and_Asymptotics.md`
- `05.2_Spherical_Collapse.md`
- `05.3_Halo_Bias.md`
