# Extract 08 — VSU Spherical Collapse: Exact Unscreened Free-Fall Time (and a Dimensional Catch)

\begin{center}
\textbf{Theme:} in the unscreened VSU regime the acceleration scales like $1/r$, which makes the collapse-time integral 
\emph{logarithmic} and exactly evaluable. The project’s current scaling has a small exponent typo.
\end{center}

## 0. The equation of motion in the unscreened regime

In the weak-field/unscreened VSU regime the acceleration magnitude scales as
\[
g(r)\simeq \frac{\sqrt{GMa_0}}{r},
\]
so the spherical-collapse radius obeys
\[
\ddot r = -\frac{\sqrt{GMa_0}}{r}.
\]

This is a genuinely different dynamical law than Newtonian collapse, where $\ddot r\propto -1/r^2$.

---

## 1. First integral (energy form)

Multiply the equation by $\dot r$:
\[
\dot r\,\ddot r = -\frac{\sqrt{GMa_0}}{r}\dot r
\quad\Longrightarrow\quad
\frac{d}{dt}\Big(\frac12 \dot r^2\Big) = -\sqrt{GMa_0}\,\frac{d}{dt}(\ln r).
\]

Integrate from the initial condition $(r,\dot r)=(r_i,0)$ to $(r,\dot r)$:
\[
\boxed{
\frac12 \dot r^2 = \sqrt{GMa_0}\,\ln\!\Big(\frac{r_i}{r}\Big).
}
\]

So
\[
\dot r = -\sqrt{2\sqrt{GMa_0}\,\ln(r_i/r)}.
\]

---

## 2. Exact collapse time

The collapse time (from $r_i$ to $0$) is
\[
t_{\rm coll}^{\rm VSU}
= \int_0^{r_i} \frac{dr}{\sqrt{2\sqrt{GMa_0}\,\ln(r_i/r)}}.
\]

### 2.1 Change of variables

Let
\[
u := \ln(r_i/r)
\quad\Longleftrightarrow\quad
r=r_i e^{-u},\qquad dr=-r_i e^{-u}\,du.
\]
As $r$ goes from $r_i$ down to $0$, $u$ goes from $0$ to $\infty$.

Then
\[
t_{\rm coll}^{\rm VSU}
=\frac{r_i}{\sqrt{2\sqrt{GMa_0}}}\int_0^\infty \frac{e^{-u}}{\sqrt{u}}\,du.
\]

The integral is a Gamma function:
\[
\int_0^\infty u^{-1/2}e^{-u}\,du = \Gamma(1/2)=\sqrt{\pi}.
\]

### 2.2 Result

\[
\boxed{
t_{\rm coll}^{\rm VSU}
=
\sqrt{\frac{\pi}{2}}\;
\frac{r_i}{(GMa_0)^{1/4}}.
}
\]

**Dimensional sanity check.**  
$(GMa_0)^{1/4}$ has units of velocity, so $r_i/(GMa_0)^{1/4}$ has units of time, as it should.

---

## 3. Relation to the project’s current scaling

The project file writes the unscreened collapse time as an integral of exactly the same form, but then states the scaling
\[
t_{\rm coll}^{\rm VSU}\propto \frac{r_i^{3/2}}{(GMa_0)^{1/4}}.
\]

That extra factor of $r_i^{1/2}$ cannot be correct (dimensionally it would leave a leftover $\sqrt{\rm length}$).  
The exact evaluation above shows the correct scaling is \textbf{linear in $r_i$}:
\[
t_{\rm coll}^{\rm VSU}\propto \frac{r_i}{(GMa_0)^{1/4}}.
\]

The *ratio* to the Newtonian free-fall time retains the project’s advertised scaling in $g_N/a_0$ (up to an $O(1)$ constant), so the downstream qualitative statements survive, but the raw $r_i$-power should be fixed.

---

## 4. Ratio to Newtonian collapse (with the constant)

Newtonian free-fall (starting from rest at $r_i$) is
\[
t_{\rm coll}^{\rm N} = \frac{\pi}{2\sqrt2}\,\frac{r_i^{3/2}}{\sqrt{GM}}.
\]

Therefore
\[
\frac{t_{\rm coll}^{\rm VSU}}{t_{\rm coll}^{\rm N}}
=
\frac{\sqrt{\pi/2}\; r_i (GM)^{1/2}}{(\pi/(2\sqrt2))\,r_i^{3/2}(GMa_0)^{1/4}}
=
\frac{2}{\sqrt{\pi}}\;\Big(\frac{GM/r_i^2}{a_0}\Big)^{1/4}.
\]

Define the Newtonian surface acceleration at $r_i$:
\[
g_N:=\frac{GM}{r_i^2}.
\]

Then
\[
\boxed{
\frac{t_{\rm coll}^{\rm VSU}}{t_{\rm coll}^{\rm N}}
=
\frac{2}{\sqrt{\pi}}\Big(\frac{g_N}{a_0}\Big)^{1/4}.
}
\]

So for $g_N\ll a_0$ the collapse is indeed faster than Newtonian collapse.

---

## 5. Tiny numerical check (code + result)

Below is minimal Python confirming the constant $\sqrt{\pi/2}$ by direct quadrature of the dimensionless integral
\[
I:=\int_0^1\frac{dx}{\sqrt{\ln(1/x)}} = \sqrt{\pi}.
\]

```python
import mpmath as mp

mp.mp.dps = 50  # crank precision so the equality is visible numerically

f = lambda x: 1/mp.sqrt(mp.log(1/x))
I = mp.quad(f, [0, 1])   # integrable endpoint singularity at x=0
print("I =", I)
print("sqrt(pi) =", mp.sqrt(mp.pi))
print("difference =", I - mp.sqrt(mp.pi))
```

Expected output (to numerical precision):
- `I ≈ 1.77245385090552`
- `sqrt(pi) ≈ 1.77245385090552`

---

## 6. Why this is interesting physically

Because the unscreened acceleration behaves as $g\propto 1/r$:

- the potential is logarithmic, $\Phi\propto -\ln r$,
- the kinetic energy grows only like $\ln(r_i/r)$,
- the collapse time involves an \emph{exact} Gamma-function integral.

That mathematical structure is unusual compared to standard $1/r^2$ gravity and could generate distinctive phenomenology:

1. **Nontrivial mass/size scaling of nonlinear structure formation.**
2. **A potentially scale-dependent critical overdensity $\delta_c(M,z)$** (not just a constant).
3. **Modified halo bias** if the excursion-set / Press–Schechter mapping is updated consistently.

---

## 7. What further work would make this “publishable”

1. **Derive $\delta_c(M,z)$ from first principles.**  
   The quick scaling arguments in the project are suggestive, but the proper $\delta_c$ comes from matching the nonlinear collapse solution to the *linear* growth equation evaluated at the collapse time.

2. **Include the screened-to-unscreened transition during collapse.**  
   Collapse begins in one regime and can cross the screening radius $r_s=\sqrt{GM/a_0}$.

3. **Connect to observables: halo mass function, bias, cluster abundance.**  
   If $\delta_c$ becomes mass dependent, that is a direct imprint on $dn/dM$ and bias $b(M)$.

4. **Sanity-check against existing constraints** (CMB lensing, cluster counts, Lyman-$\alpha$), once the model is globally well-defined on the cosmological branch.

