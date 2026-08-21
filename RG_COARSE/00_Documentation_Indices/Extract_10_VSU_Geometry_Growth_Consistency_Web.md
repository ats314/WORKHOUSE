# Extract 10 — VSU “geometry vs growth” consistency web (BAO/AP invariants, ISW sign, and the S\_8 mapping)

\begin{center}
\textbf{Extracted from: 03.1, 03.2, 03.3, 03.5, 04.2, 04.3, 04.4, 04.5, 06.2, 06.3.}
\end{center}

## 0. Why this is the most “testable” part of the VSU notes

The VSU files build a particularly sharp *separation principle*:

\[
\boxed{\text{Background geometry is kept exactly }\Lambda\text{CDM, while perturbation/growth is modified.}}
\]

That split is powerful because it spawns a web of correlated predictions:

- **BAO peak positions** should remain unchanged (early-time physics untouched).
- **Alcock–Paczy\'nski (AP)** distortions should remain unchanged (pure geometry).
- **Weak lensing amplitude** and **RSD** can shift (they depend on growth / potentials).
- **ISW** is a sign-and-amplitude diagnostic of how potentials decay at late times.

This extract packages the “web” into a single coherent block, and flags a subtle sign/bookkeeping issue that matters if you’re trying to address the empirical $S_8$ tension.

---

## 1. Background geometry: locked to \(\Lambda\)CDM

From `03.1_Background_Cosmology.md`, the background is flat FLRW with matter + \(\Lambda\):
\[
H^2(a)=H_0^2\bigl(\Omega_{m0}a^{-3}+\Omega_{\Lambda0}\bigr),\qquad \Omega_{m0}+\Omega_{\Lambda0}=1.
\]
Therefore geometric distances are standard:
\[
D_A(z)=\frac{1}{1+z}\int_0^z\frac{dz'}{H(z')},\qquad
F_{\rm AP}(z)=(1+z)D_A(z)H(z).
\]

**Immediate consequence:**
\[
\boxed{\;F_{\rm AP}^{\rm VSU}(z)=F_{\rm AP}^{\rm GR}(z).\;}
\]
(That is the core content of `04.5_Alcock_Paczynski_Consistency.md`.)

---

## 2. Linear growth: where modifications actually live

On sub-horizon scales (`03.3_Matter_Growth_Equation.md`), the matter contrast obeys
\[
\ddot\delta+2H\dot\delta-4\pi G\bar\rho_m\,\bigl[1+\alpha_{\rm eff}(k,a)\bigr]\,\delta=0.
\]
Equivalently, for the growth factor \(D(a,k)\):
\[
D''+\left(\frac{3}{a}+\frac{1}{H}\frac{dH}{da}\right)D'-\frac{3}{2}\frac{\Omega_m(a)}{a^2}\bigl[1+\alpha_{\rm eff}(k,a)\bigr]D=0.
\]
Late-time saturation (`03.5_Late_Time_Asymptotics.md`) assumes
\[
\alpha_{\rm eff}(k,a)\to \alpha_\infty(k)\quad (z\lesssim 2),
\]
and leads to the growth-index shift
\[
\boxed{\;\gamma(k)=\frac{6}{11}-\frac{3}{55}\alpha_\infty(k).\;}
\]
Since \(\Omega_m(a)<1\) at late times, a *positive* \(\alpha_\infty\) makes \(\gamma\) smaller and thus makes
\(f=\Omega_m^{\gamma}\) larger → faster growth.

That part of the analytic logic is tight.

---

## 3. BAO phase / peak positions: invariant

The BAO phase is set by \(k r_s\) with
\[
 r_s(\eta)=\int_0^{\eta}c_s(\eta')\,d\eta'.
\]
The BAO file (`04.4_BAO_Phase_and_Peaks.md`) argues that because:

1. the background expansion is unchanged, and
2. early-time modifications vanish / \(\Phi\) is effectively constant during oscillations,

one gets
\[
\boxed{\;\Delta\phi_{\rm BAO}=0\;\Rightarrow\;k_n r_s(\eta_*)=n\pi\text{ unchanged.}\;}
\]
So BAO peak *positions* remain a standard ruler; only late-time amplitudes change through \(D(k,z)\).

---

## 4. ISW sign: a clean sign check (with one subtlety)

The ISW anisotropy is
\[
\left(\frac{\Delta T}{T}\right)_{\rm ISW}=2\int_{\eta_*}^{\eta_0}d\eta\,\dot\Phi.
\]
For sub-horizon scales, combine the Poisson form of \(\Phi\) with \(D\):
\[
\Phi(k,a)\propto -\mathcal G(k,a)\frac{D(k,a)}{a},\qquad \mathcal G=1+\alpha_{\rm eff}.
\]
Then
\[
\boxed{\;\dot\Phi=H\Phi\left[f(k,a)-1+\frac{d\ln\mathcal G}{d\ln a}\right].\;}
\]
At late times the framework assumes \(d\ln\mathcal G/d\ln a\to 0\), so
\[
\dot\Phi\simeq H\Phi\,(f-1).
\]
Now do the sign logic carefully:

- In overdense regions \(\Phi<0\).
- At late times \(f<1\) (growth slows under \(\Lambda\)-domination), so \(f-1<0\).
- Therefore \(H>0\) and \(\Phi<0\) and \((f-1)<0\) gives
\[
\boxed{\;\dot\Phi>0\;\text{(potential becomes less negative / “decays”).}\;}
\]
That corresponds to the standard result: overdensities correlate with *positive* ISW temperature shifts.

**Amplitude diagnostic.** The ISW amplitude scales with \(|\dot\Phi|\). If VSU increases \(f\) while keeping \(f<1\), then \(|f-1|\) decreases, so \(|\dot\Phi|\) decreases:
\[
\boxed{\;\alpha_\infty>0\ \Rightarrow\ f_{\rm VSU}>f_{\rm GR}\ \Rightarrow\ |\dot\Phi|_{\rm VSU}<|\dot\Phi|_{\rm GR}.\;}
\]
This is essentially what `04.3_ISW_Sign_and_Amplitude.md` is aiming at, though one intermediate inequality in that file flips the sign of \(\dot\Phi\) (a bookkeeping glitch, not a conceptual deal-breaker).

---

## 5. The weak-lensing / \(S_8\) mapping and a sign-sensitive integral

The lensing-oriented files express a fractional shift of \(\sigma_8\) or \(S_8\) in terms of an integral that appears when integrating the growth index. A representative structure is
\[
\frac{D_{\rm VSU}}{D_{\rm GR}}\sim \exp\Big[-\frac{3}{55}\alpha_\infty\,\mathcal I(z)\Big],
\qquad
\mathcal I(z)=\int_z^{\infty}\frac{dz'}{1+z'}\,\Omega_m(z')^{6/11}\ln\Omega_m(z').
\]
Here’s the key sign fact in \(\Lambda\)CDM:

- For \(0<\Omega_m(z)<1\), \(\ln\Omega_m(z)<0\).
- The integrand is therefore negative, so
\[
\boxed{\;\mathcal I(0)<0\;\text{for }\Omega_{m0}<1.\;}
\]
A quick numerical check for \(\Omega_{m0}=0.3\) gives \(\mathcal I(0)\approx -0.383\):

```python
import mpmath as mp

mp.mp.dps = 50

def Omega_m(z, Om0=0.3, Ol0=0.7):
    a = 1/(1+z)
    return Om0*a**-3/(Om0*a**-3 + Ol0)

def I_of_z(z0, Om0=0.3, Ol0=0.7):
    f = lambda z: (Omega_m(z, Om0, Ol0)**(6/11))*mp.log(Omega_m(z, Om0, Ol0))/(1+z)
    return mp.quad(f, [z0, mp.inf])

print(I_of_z(0))
```

Output:
\[
\boxed{\;\mathcal I(0)\simeq -0.3829758404\;\text{for }(\Omega_{m0},\Omega_{\Lambda0})=(0.3,0.7).\;}
\]

**Why this matters:** if \(\alpha_\infty>0\), then \(-\tfrac{3}{55}\alpha_\infty\mathcal I(0)\) is *positive* and the exponential enhances \(D\), hence enhances \(\sigma_8\). So (with this sign convention) a positive enhancement tends to push \(S_8\) upward, not downward.

Some VSU observational notes state the opposite qualitative direction (“positive enhancement implies \(S_8\) suppression”). That can be fixed in one of two ways:

1. **Pure bookkeeping fix:** redefine \(\mathcal I\) with an explicit minus sign so the reported integral is positive.
2. **Physics fix:** if the goal is to suppress \(S_8\), the effective modification entering growth must be negative on the relevant window, or must enter the growth equation with opposite sign than \(1+\alpha\).

Either way, this is a *high-leverage consistency point* because it propagates into ISW amplitude predictions and multi-probe degeneracy breaking.

---

## 6. Degeneracy structure: why the web is falsifiable

`06.2_Observable_Degeneracy_Structure.md` and `06.3_Parameter_Minimality.md` emphasize that, at linear order:

- BAO/AP constrain geometry (here unchanged),
- RSD and lensing constrain growth (modified),
- ISW constrains potential decay (modified but sign-protected as long as \(f<1\)).

With only one new fundamental scale \(a_0\) and a fixed \(\mu(x)=1-e^{-x}\), you don’t get to tune these probes independently.

That’s a feature: the theory lives or dies by internal consistency across the web.

---

## 7. What to do next (the minimum needed to “close” the observational story)

1. **Fix the sign convention globally** for \(\Phi\), \(\mathcal I\), and the mapping between \(\alpha_{\rm eff}\) and growth. Then re-derive \(S_8\) and ISW shifts with one consistent set of definitions.

2. **Derive (or define) \(m_{\rm eff}(a)\)** in \(\alpha_{\rm eff}(k,a)=\dfrac{k^2}{k^2+a^2m_{\rm eff}^2}\,\dfrac{1}{\mu(g/a_0)}\). Without that, \(\alpha_\infty(k)\) is a placeholder.

3. **Quantify the prediction:** choose a fiducial \(a_0\) and compute window-averaged shifts for
\(f\sigma_8\), \(S_8\), and ISW cross-correlation. The “web” only becomes sharp when those windows are evaluated.

4. **Nonlinear bridge:** fold in the corrected spherical-collapse integral (see Extract 08) before quoting halo-bias scalings.

The punchline: BAO/AP invariance + ISW sign protection + correlated growth shifts are a strong, testable *signature class* — but it’s worth sanding down the remaining sign/definition splinters so the predictions can be compared cleanly to data.
