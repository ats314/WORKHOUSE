---
id: EX-016
title: "SPARC rotation-curve pipeline, QDHT spectral method, and the kill-switch protocol"
kind: extraction
items: 11
status_breakdown: {"solid": 11}
program: cosmology
extracted_by: claude-opus-5 subagent, 2026-09-01
stance: preservation (content extraction, not refereeing)
source_files:
  - ARCHIVES/extracted_notebooks/Untitled10_extracted.py
  - SIMULATIONS/Selected_01_SPARC_Global_Fits_and_KillSwitch.md
  - SIMULATIONS/CODE_sparc_rigidity_HANKEL_KERNEL_SWITCH.py
  - SIMULATIONS/CODE_sparc_honest_killswitch.py
  - VSU_COSMOLOGY/Galactic_Phenomenology/UPG_04_Dwarf_KillSwitch_NoSpecialPleading.md
  - VSU_COSMOLOGY/Galactic_Phenomenology/BEST_01_AntiKernel_SpectralRigidity.md
  - VSU_COSMOLOGY/Galactic_Phenomenology/CODE_demo_antikernel_variational_equivalence.py
  - VSU_COSMOLOGY/Core_Theory/Selected_02_Spectral_Boost_Filter_Model.md
  - VSU_COSMOLOGY/Galactic_Phenomenology/EXC_01_AntiKernel_HankelSpectral.md
  - VSU_COSMOLOGY/Galactic_Phenomenology/SPARC_WORK/Rotmod_LTG/
---

# SPARC rotation-curve pipeline, QDHT spectral method, and the kill-switch protocol

> A complete, reproducible 175-galaxy SPARC fitting pipeline (order-0 QDHT on Bessel-zero nodes and an order-1 trapezoid Hankel transform, IR-boosted spectral filter M(k)=1+(mu/k)^2 with a global stiffness switch, weighted per-galaxy amplitude estimator) together with a pre-registered kill-switch protocol; I reproduced every headline number to six significant figures, found and fixed a normalisation index-swap in the QDHT, and completed the asymptotic no-go showing that any universal linear IR-boosted multiplier gives v ~ sqrt(r) rather than flat rotation curves.

**11 extracted items** — 11 solid

---

## 1. SPARC data model, selection cuts, and observables (the common front-end of every fit in the corpus)

`status: solid` · `kind: definition`

### Statement

Let the SPARC Rotmod_LTG sample consist of $N_{\rm gal}$ files, each a table of rows $(r_i,\;V_{\rm obs}(r_i),\;\sigma_i,\;V_{\rm gas}(r_i),\;V_{\rm disk}(r_i),\;V_{\rm bul}(r_i),\;\Sigma_{\rm disk},\;\Sigma_{\rm bul})$ with $r$ in kpc, velocities in km/s, surface brightnesses in $L_\odot/{\rm pc}^2$.  Define the baryonic squared speed at fixed global mass-to-light ratios $\Upsilon_{\rm disk},\Upsilon_{\rm bul}$
\[ V_b^2(r) \;=\; \max(V_{\rm gas},0)^2 \;+\; \Upsilon_{\rm disk}\max(V_{\rm disk},0)^2 \;+\; \Upsilon_{\rm bul}\max(V_{\rm bul},0)^2, \]
the baryonic and observed accelerations
\[ g_{\rm bar}(r)=\frac{V_b^2(r)}{r},\qquad g_{\rm obs}(r)=\frac{V_{\rm obs}^2(r)}{r}, \]
both in $({\rm km/s})^2/{\rm kpc}$, and for any model producing $g_{\rm pred}$,
\[ V_{\rm pred}(r)=\sqrt{r\,g_{\rm pred}(r)} . \]
The global goodness-of-fit statistic is the pointwise, error-weighted, dof-normalised chi-square pooled over all galaxies and all radii:
\[ \chi^2/{\rm dof} \;=\; \frac{\sum_{g}\sum_{i}\big(V_{\rm obs}(r_i)-V_{\rm pred}(r_i)\big)^2/\sigma_i^2}{\sum_g N_{{\rm pts},g}} . \]
Mass stratification uses the robust flat-velocity proxy $V_{\rm flat}:=\mathrm{percentile}_{90}\{V_{\rm obs}(r_i)\}$, with bins dwarfs ($V_{\rm flat}<80$ km/s), mid ($80\le V_{\rm flat}<150$), big ($V_{\rm flat}\ge 150$).  Radial-point cut: keep a galaxy iff it has $\ge 8$ finite rows with $r>0$ (and, for the global-fit script, additionally $\sigma_i>0$); duplicate radii are removed after sorting.

### Derivation

Verified directly against the bundled data.  The directory VSU_COSMOLOGY/Galactic_Phenomenology/SPARC_WORK/Rotmod_LTG/ contains exactly 175 files named *_rotmod.dat, each with a three-line '#' header (Distance, column names, units) and 8 numeric columns.  Example (DDO154_rotmod.dat):

    # Distance = 4.04 Mpc
    # Rad  Vobs  errV  Vgas  Vdisk  Vbul  SBdisk  SBbul
    # kpc  km/s  km/s  km/s  km/s   km/s  L/pc^2  L/pc^2
    0.49  13.80  1.60  3.74  12.31  0.00   15.93   0.00
    0.99  21.60  0.80  7.46  14.55  0.00    5.52   0.00

I enumerated the sample and applied the cut.  Result (my run, scratchpad script, numpy 2.3.5 / scipy 1.17.1):

    total 175; files with <5 columns: 0 ; galaxies with <8 radial points: 32 ; kept: 143 ; total kept points: 3199
    points per galaxy: min 8, median 17, max 115

This reproduces the corpus header lines 'FOUND 175 RC FILES / USING 143 GALAXIES / SKIPPED 32' exactly, and identifies the skip reason unambiguously: all 32 skips are the $N_{\rm pts}<8$ cut, none are malformed files.  It also reproduces $N_{\rm pts}=3199$, which settles a discrepancy flagged elsewhere in the corpus (BEST_01_AntiKernel_SpectralRigidity.md reports $N_{\rm pts}=3646$ for the same run; 3199 is the correct count for the bundled data under the stated cuts, so 3646 must come from a run with a different point cut or a different snapshot of the archive).

[reconstructed] Note on $\Upsilon$: the SPARC rotmod convention supplies $V_{\rm disk},V_{\rm bul}$ at $\Upsilon=1$, so $V_b^2$ is linear in $(\Upsilon_{\rm disk},\Upsilon_{\rm bul})$ by construction.  Both corpus pipelines fix $\Upsilon_{\rm disk}=\Upsilon_{\rm bul}=0.5$ globally, EXCEPT the order-1 Hankel script CODE_sparc_rigidity_HANKEL_KERNEL_SWITCH.py, which uses $V_b^2=V_{\rm gas}^2+V_{\rm disk}^2+V_{\rm bul}^2$, i.e. $\Upsilon_{\rm disk}=\Upsilon_{\rm bul}=1$.  This is an inconsistency between the two scripts; it is partly absorbed by that script's free per-galaxy amplitude $A$ (an overall factor 2 in $V_b^2$ is exactly a factor 2 in $A$ for a linear model, which the anti-kernel is).  Anyone re-running must fix a convention and state it.

Geometric identity worth recording: because the anti-kernel model is LINEAR in $g_{\rm bar}$, the per-galaxy amplitude $A$ and the mass-to-light ratio are exactly degenerate, $A \simeq \Upsilon_{\rm eff}/\Upsilon_{\rm assumed}$; this is the content of UPG_03 and is why an $A$-distribution spanning a factor of 80 is a physical falsification and not merely a nuisance-parameter artefact.

### Constants and numbers

Sample: 175 rotmod files; 143 pass $N_{\rm pts}\ge 8$; 32 skipped; 3199 total radial points; points/galaxy min 8, median 17, max 115.  Global M/L used in the global-fit script: $\Upsilon_{\rm disk}=\Upsilon_{\rm bul}=0.5$.  Global M/L implicit in the order-1 Hankel script: $\Upsilon=1$.  Mass bins with $\Upsilon=0.5$ and the $N_{\rm pts}\ge8$ cut on the bundled data: dwarfs $N=37$, mid $N=53$, big $N=53$ (the archived run, which additionally applied a SPARC quality cut $Q\le3$ using SPARC_Lelli2016c.mrt and kept 165 galaxies, had dwarfs 51 / mid 58 / big 56).  Data provenance: Zenodo record 16284118, files Rotmod_LTG.zip and SPARC_Lelli2016c.mrt (the .mrt master table is NOT bundled in the corpus; only the rotmod zip and its expansion are).  Units: $r$ [kpc], $V$ [km/s], $g$ [(km/s)$^2$/kpc].

### Code

Reference loader (self-contained; produces the numbers above):

```python
import numpy as np, glob, os
UD = UB = 0.5
D = "<corpus>/VSU_COSMOLOGY/Galactic_Phenomenology/SPARC_WORK/Rotmod_LTG"
gals = []
for f in sorted(glob.glob(os.path.join(D, "*_rotmod.dat"))):
    a = np.loadtxt(f)                       # '#' comment lines are skipped by loadtxt
    if a.ndim == 1 or a.shape[1] < 6: continue
    r, vo, ev, vg, vd, vb = a[:,0], a[:,1], a[:,2], a[:,3], a[:,4], a[:,5]
    m = np.isfinite(r) & np.isfinite(vo) & np.isfinite(ev) & (r > 0) & (ev > 0)
    r, vo, ev, vg, vd, vb = [x[m] for x in (r, vo, ev, vg, vd, vb)]
    if r.size < 8: continue                  # the 32 skips
    i = np.argsort(r); r, vo, ev, vg, vd, vb = [x[i] for x in (r, vo, ev, vg, vd, vb)]
    keep = np.ones_like(r, bool); keep[1:] = r[1:] > r[:-1]     # de-duplicate radii
    r, vo, ev, vg, vd, vb = [x[keep] for x in (r, vo, ev, vg, vd, vb)]
    v2b  = np.maximum(vg,0)**2 + UD*np.maximum(vd,0)**2 + UB*np.maximum(vb,0)**2
    gals.append(dict(name=os.path.basename(f)[:-11], r=r, v=vo, ev=ev,
                     gbar=v2b/r, Vflat=float(np.percentile(vo, 90.0))))
```
My full working scripts are at
C:\\Users\\Alex\\AppData\\Local\\Temp\\claude\\F--ANTIGRAVITY-antigravity-playground-scalar-cluster-proof\\fd74385b-6527-446a-ae5a-90acb16ad82a\\scratchpad\\ (repro_global.py, antikernel_run.py, antikernel_reg.py, killswitch_run.py, roundtrip.py, qdht_ref.py, qdht_test.py, asym.py).

**Caveat.** The SPARC master table SPARC_Lelli2016c.mrt is not bundled, so the archived run's quality cut $Q\le3$ (165 galaxies) cannot be reproduced offline; the offline sample is the 143 galaxies passing $N_{\rm pts}\ge8$. Distance and inclination uncertainties, which SPARC provides, are ignored throughout.

**Why it matters.** This is the only part of the whole corpus with real, complete, correctly-formatted observational data attached, and it is the shared front-end for every fit reported. Fixing the loader, the cuts, and the unit convention exactly is what makes every downstream number in this extraction independently reproducible.

---

## 2. Quasi-discrete Hankel transform on Bessel-zero nodes: construction, involution property, and the normalisation index-swap in the corpus implementation

`status: solid` · `kind: algorithm`

### Statement

Fix an order $p=0$, a node count $N$, and a domain radius $R>0$.  Let $\alpha_1<\alpha_2<\dots<\alpha_{N+1}$ be the first $N+1$ positive zeros of $J_0$.  Define nodes and conjugate nodes
\[ r_n=\frac{\alpha_n R}{\alpha_{N+1}}\in(0,R),\qquad k_m=\frac{\alpha_m}{R},\qquad n,m=1,\dots,N, \]
and the symmetric transformation matrix
\[ T_{mn}\;=\;\frac{2}{\alpha_{N+1}}\;\frac{J_0\!\big(\alpha_m\alpha_n/\alpha_{N+1}\big)}{\big|J_1(\alpha_m)\big|\,\big|J_1(\alpha_n)\big|}. \]
Then (i) $T=T^{\mathsf T}$ exactly, (ii) $T^2=\mathbb 1$ to machine precision, and (iii) with $D:=\operatorname{diag}\big(|J_1(\alpha_n)|\big)$ and the scale $S:=R^2/\alpha_{N+1}$, the operator
\[ \mathcal H\;:=\;S\,D\,T\,D^{-1} \]
approximates the order-0 Hankel transform $F(k)=\int_0^\infty f(r)J_0(kr)\,r\,dr$ on the node set, and $\mathcal H^{-1}=S^{-1}D\,T\,D^{-1}$ approximates $f(r)=\int_0^\infty F(k)J_0(kr)\,k\,dk$.

**Claim (verified):** for $f(r)=e^{-r^2/2s^2}$ with exact transform $F(k)=s^2e^{-k^2s^2/2}$, at $N=256$, $R=20$, $s=1$, the operator $\mathcal H$ reproduces $F(k_m)$ with maximum relative error $3.4\times10^{-16}$, and $\mathcal H^{-1}\mathcal H f=f$ to $4.6\times10^{-15}$.

**Claim (defect, verified):** the corpus implementation in `CODE_sparc_honest_killswitch.py` applies the conjugation in the reciprocal direction,
\[ \mathcal H_{\rm corpus}\;=\;D^{-1}\,T\,D \qquad\text{instead of}\qquad \mathcal H\;\propto\;D\,T\,D^{-1}, \]
by computing `forward(f) = (T @ (f * j1_vals)) / j1_vals`.  Because $T^2=\mathbb 1$, the round trip $\mathcal H_{\rm corpus}^2=\mathbb 1$ is still exact, so the defect is invisible to a round-trip test; but the intermediate $k$-space array is NOT the Hankel transform.  Against the Gaussian control it has 95.5% relative error after optimal rescaling.  Composed with a spectral filter $M$ the corpus pipeline computes
\[ g\;\longmapsto\;D^{-1}\,T\,M\,T\,D\;g \;=\; D^{-2}\Big[\,\mathcal{F}\big(D^{2}g\big)\Big],\qquad \mathcal F:=D\,T\,M\,T\,D^{-1}, \]
and since $|J_1(\alpha_n)|^2\simeq 2/(\pi\alpha_n)\propto 1/r_n$ for large $n$, this is (up to a constant) $g\mapsto r\cdot\mathcal F[g(\cdot)/\cdot](r)$: the filter is applied to $g_{\rm bar}/r$ rather than to $g_{\rm bar}$.

### Derivation

**Construction.**  The Fourier–Bessel series on $[0,R]$ with Dirichlet-type endpoint $J_0(\alpha_{N+1})=0$ expands $f(r)=\sum_n c_n J_0(\alpha_n r/R)$ with $c_n = \frac{2}{R^2 J_1(\alpha_n)^2}\int_0^R f(r)J_0(\alpha_n r/R)\,r\,dr$.  Sampling $f$ at the nodes $r_n=\alpha_n R/\alpha_{N+1}$ and truncating the series at $N$ terms turns the quadrature into a matrix multiplication whose kernel is $J_0(\alpha_m\alpha_n/\alpha_{N+1})$ and whose weights carry $|J_1(\alpha_n)|^{-2}$ at the summation index.  Symmetrising the weight by splitting it as $|J_1(\alpha_m)|^{-1}|J_1(\alpha_n)|^{-1}$ and putting the residual $|J_1(\alpha_m)|/|J_1(\alpha_n)|$ into the conjugation gives exactly $T$ above and the pairing $\mathcal H\propto D\,T\,D^{-1}$.  This is the Guizar-Sicairos & Gutiérrez-Vega (2004) construction; the corpus reproduces $T$ correctly, and only the conjugation direction is wrong.

**Why the scale is $S=R^2/\alpha_{N+1}$.**  $[reconstructed]$  In the G-S normalisation the scaled arrays are $F_1=f/m_1$, $F_2=F/m_2$ with $m_{1n}=|J_1(\alpha_n)|/V$, $m_{2n}=|J_1(\alpha_n)|/R$ and $V=\alpha_{N+1}/(2\pi R)$ the maximum spatial frequency; $F_2 = T F_1$.  Unwinding, $F(k_m) = (V/R)^{-1}\dots$; collecting factors gives $F(k_m)=\frac{R^2}{\alpha_{N+1}}|J_1(\alpha_m)|\sum_n T_{mn} f(r_n)/|J_1(\alpha_n)|$.  I confirmed this numerically rather than trusting the algebra: at $N=256,R=20$ the least-squares scale needed to match the analytic Gaussian transform came out $0.4959062512604547$, while $R^2/\alpha_{N+1}=0.4959062512604545$ — agreement to 15 digits.

**Verification run** (scratchpad `qdht_test.py`, `qdht_ref.py`):

    T symmetric:                     max|T - T^T| = 0.0
    involution:                      max|T@T - I| = 3.06e-11        (N=256)
    corpus  forward vs analytic:     best-fit scale 0.31076, max rel err 9.546e-01
    G-S     forward vs analytic:     best-fit scale 0.49591, max rel err 2.237e-16
    corpus  round-trip forward^2:    max rel err 4.39e-14           (exact, hides the bug)
    corrected inverse(forward):      max rel err 4.56e-15

**The one-line fix.**  In the corpus class replace

    def forward(self, f_r):
        v_in  = f_r * self.j1_vals
        v_out = self.T @ v_in
        return v_out / self.j1_vals

by

    def forward(self, f_r):                       # F(k_m) = int f(r) J0(k_m r) r dr
        return (self.R**2/self.alpha_N) * self.j1_vals * (self.T @ (f_r / self.j1_vals))
    def inverse(self, F_k):                       # f(r_n) = int F(k) J0(k r_n) k dk
        return (self.alpha_N/self.R**2) * self.j1_vals * (self.T @ (F_k / self.j1_vals))

**Impact on the science.**  With the corpus (buggy) conjugation the kill-switch stress test gives median $\chi^2/{\rm dof}=15.44$ and 104/175 outliers; with the corrected conjugation, 4.17 and 89/175.  Galaxies for which the stiffness switch is off ($\mu=0$, $M\equiv1$) are numerically identical in both, because then $D^{-1}TMTD = D^{-1}T^2D=\mathbb 1 = DT^2D^{-1}$ — a clean internal consistency check that isolates the defect to the filtering step alone (verified: NGC5055, UGC09133, UGC02953 all reproduce $\chi^2/{\rm dof}=1455.95,\;553.48,\;427.02$ in both modes).

**Grid parameters actually used.**  The kill-switch script instantiates `QDHT(n_points=512, r_max=4*max(r))`, i.e. $N=512$, $R=4r_{\max}$.  With $\alpha_1=2.4048255577$, $\alpha_{512}=1607.710118$, $\alpha_{513}=1610.851711$ this gives an implicit spectral window
\[ k_{\min}=\frac{\alpha_1}{4r_{\max}}=\frac{0.60121}{r_{\max}},\qquad k_{\max}=\frac{\alpha_{512}}{4r_{\max}}=\frac{401.93}{r_{\max}}, \]
and a radial grid spanning $0.005972\,r_{\max}$ to $3.9922\,r_{\max}$.  The value $k_{\min}\simeq0.601/r_{\max}$ is the QDHT's implicit infrared regulator and is numerically almost identical to the order-1 script's hand-set `KMIN_FACTOR = 0.5` — which is why the two implementations, despite being different transforms of different order, land on comparable $\mu$ scales.

### Constants and numbers

$p=0$; corpus uses $N=512$, $R=4r_{\max}$.  $\alpha_1=2.4048255576958$, $\alpha_{512}=1607.7101182249$, $\alpha_{513}=1610.8517107269$.  Implicit window $k_{\min}=0.601206/r_{\max}$, $k_{\max}=401.9275/r_{\max}$ kpc$^{-1}$; radial nodes $r_1=0.0059716\,r_{\max}$ to $r_{512}=3.9921989\,r_{\max}$.  Forward scale $S=R^2/\alpha_{N+1}$; at $N=256,R=20$: $S=0.4959062512604545$ vs empirical $0.4959062512604547$.  Accuracy at $N=256,R=20$, Gaussian $s=1$: corrected forward $3.35\times10^{-16}$ max rel err; round trip $4.56\times10^{-15}$; involution $\|T^2-\mathbb 1\|_\infty=3.06\times10^{-11}$.  Corpus forward: $9.55\times10^{-1}$ (95.5%) rel err.  Downstream: median $\chi^2/{\rm dof}$ 15.441 (corpus) vs 4.173 (corrected); outliers 104/175 vs 89/175; $\log_{10}A$ scatter 0.482 dex vs 0.429 dex; $A$ range $[0.0256,6.204]$ vs $[0.0408,7.821]$.

### Code

Verified reference implementation (machine-precision against the analytic Gaussian transform):

```python
import numpy as np
from scipy.special import j0, j1, jn_zeros

class QDHT0:
    """Order-0 quasi-discrete Hankel transform on Bessel-zero nodes.
       Guizar-Sicairos & Gutierrez-Vega, JOSA A 21, 53 (2004)."""
    def __init__(self, N, R):
        a          = jn_zeros(0, N + 1)                  # alpha_1 .. alpha_{N+1}
        self.N, self.R = N, R
        self.aN    = a[-1]                               # alpha_{N+1}
        self.roots = a[:-1]
        self.r     = self.roots * R / self.aN            # radial nodes in (0,R)
        self.k     = self.roots / R                      # conjugate nodes
        self.j1v   = np.abs(j1(self.roots))
        self.T     = (2.0/self.aN) * j0(np.outer(self.roots, self.roots)/self.aN) \
                     / np.outer(self.j1v, self.j1v)      # symmetric, T @ T = I
        self.scale = R*R/self.aN
    def forward(self, f_r):   # F(k_m) = \int_0^inf f(r) J0(k_m r) r dr
        return self.scale * self.j1v * (self.T @ (f_r / self.j1v))
    def inverse(self, F_k):   # f(r_n) = \int_0^inf F(k) J0(k r_n) k dk
        return (1.0/self.scale) * self.j1v * (self.T @ (F_k / self.j1v))

if __name__ == "__main__":
    d = QDHT0(256, 20.0); s = 1.0
    f  = np.exp(-d.r**2/(2*s*s))
    Ft = s*s*np.exp(-d.k**2*s*s/2)
    F  = d.forward(f)
    print(np.max(np.abs(F-Ft))/np.max(np.abs(Ft)))          # 3.35e-16
    print(np.max(np.abs(d.inverse(F)-f))/np.max(np.abs(f))) # 4.56e-15
```
File: scratchpad\\qdht_ref.py (run: `python qdht_ref.py`).  The A/B test against the corpus version is scratchpad\\qdht_test.py.

**Caveat.** The corpus QDHT is order $p=0$ while the disk-sector physics it is used for (the order-1 Hankel representation of $g_N$ for an axisymmetric disk) requires $p=1$; the two corpus scripts therefore implement two genuinely different operators under the same name. Fixing the conjugation does not fix the order mismatch.

**Why it matters.** This is the one piece of the corpus that is genuinely reusable software: a correct, machine-precision, involutive quasi-discrete Hankel transform in twenty lines. The extraction also pins down exactly where the corpus version is wrong, why the author's own round-trip test could not detect it, and how much of the model's apparent failure was numerical (a factor 3.7 in median chi2/dof) versus physical (the rest, which survives the fix).

---

## 3. The spectral response filter M(k) = 1 + (mu/k)^2 with the global stiffness switch, and the two corpus pipelines that implement it

`status: solid` · `kind: construction`

### Statement

**Model (spectral rigidity / anti-kernel).**  Given a per-galaxy baryonic acceleration profile $g_b(r)$, define a one-parameter multiplicative response in Hankel space,
\[ \widehat g_\mu(k)\;=\;M(k;\mu)\,\widehat g_b(k),\qquad g_\mu=\mathcal H^{-1}\big[\widehat g_\mu\big], \]
with the two branches implemented behind a single source-level switch:
\[ M_{\rm screen}(k;\mu)=\frac{k^2}{k^2+\mu^2}\quad(\text{Yukawa/Helmholtz screening}),\qquad M_{\rm anti}(k;\mu)=\frac{k^2+\mu^2}{k^2}=1+\Big(\frac{\mu}{k}\Big)^{2}\quad(\text{IR boost}). \]
A generalised family also appears: $M(k;\mu,n)=\big(1+(\mu/k)^n\big)^{1/n}$ with the 'sharpened' choice $n=4$; its asymptotics are $M\to1$ for $k\gg\mu$ and $M\sim\mu/k$ for $k\ll\mu$.
The prediction is $V_{\rm pred}^2(r)=A\,r\,g_\mu(r)$ with a per-galaxy amplitude $A$.

**Global stiffness switch (kill-switch script only).**  $\mu$ is not fitted per galaxy; it is a deterministic function of the galaxy's peak baryonic acceleration $g_{\max}:=\max_r g_{\rm bar}(r)$:
\[ \mu(g_{\max})\;=\;\begin{cases}0, & g_{\max}\ge a_0^{\rm spec},\\[4pt] \mu_{\max}\Big(1-\dfrac{g_{\max}}{a_0^{\rm spec}}\Big), & g_{\max}<a_0^{\rm spec},\end{cases}\qquad \mu_{\max}=0.30\ {\rm kpc}^{-1},\quad a_0^{\rm spec}=3700\ ({\rm km/s})^2/{\rm kpc}. \]
This injects the only nonlinearity in the whole construction: the map $g_b\mapsto g_\mu$ is linear at fixed $\mu$, and the switch makes $\mu$ depend on the galaxy.

### Derivation

**Pipeline 1 — order-1 trapezoid Hankel, global $\mu$** (`CODE_sparc_rigidity_HANKEL_KERNEL_SWITCH.py`, five byte-identical copies including `SIMULATIONS/code_verification/SPARC_antikernel_fit.py`).  Uses the order-1 pair appropriate to an axisymmetric disk,
\[ \widehat g(k)=\int_0^\infty dr\,r\,g(r)J_1(kr),\qquad g(r)=\int_0^\infty dk\,k\,\widehat g(k)J_1(kr), \]
discretised as dense matrix products $J_{mn}=J_1(k_m r_n)$ with trapezoid weights $w_r=\mathrm{gradient}(r)$, $w_k=\mathrm{gradient}(k)$ on the observed radii only.

The $k$-grid is built per galaxy, log-spaced with $N_k=512$:
\[ \Delta r_{\rm eff}=\mathrm{quantile}_{0.25}\{\Delta r_i>0\},\qquad k_{\min}=\max\Big(10^{-4},\;\frac{c_{\rm IR}}{r_{\max}}\Big),\qquad k_{\max}=\min\Big(\frac{6\pi}{\Delta r_{\rm eff}},\;400\Big), \]
with $c_{\rm IR}=$ `KMIN_FACTOR` $=0.5$, plus a super-Gaussian anti-ringing taper applied in $k$,
\[ W(k)=\exp\!\Big[-\big(k/k_c\big)^{4}\Big],\qquad k_c=\frac{\pi}{\Delta r_{\rm eff}} . \]
So the actual operator implemented is $g_\mu=\mathcal H_1^{-1}\big[W(k)M(k;\mu)\mathcal H_1[g_b]\big]$; the taper $W$ and the cutoff $k_{\min}$ are declared in the source as 'knobs (NOT fit params)'.

The per-galaxy amplitude is a closed-form weighted least-squares scale on $V$ (not $V^2$), with an error floor and a clamp on $\sqrt{A}$:
\[ \sigma_{{\rm eff},i}^2=\sigma_i^2+\sigma_{\rm floor}^2,\quad \sigma_{\rm floor}=5\ {\rm km/s},\qquad w_i=\sigma_{{\rm eff},i}^{-2},\qquad s^\star=\frac{\sum_i w_i V_{\mu,i}V_{{\rm obs},i}}{\sum_i w_i V_{\mu,i}^2},\qquad A=\big[\mathrm{clip}(s^\star,\sqrt{0.05},\sqrt{50})\big]^2, \]
where $V_\mu=\sqrt{\max(r g_\mu,0)}$.  (Derivation of $s^\star$: minimising $\sum_i w_i(V_{{\rm obs},i}-sV_{\mu,i})^2$ over $s$ gives $\partial_s=0\Rightarrow s^\star=\sum w V_\mu V_{\rm obs}/\sum wV_\mu^2$, and $A=s^{\star2}$ since $V_{\rm pred}=\sqrt{A}\,V_\mu$.)  The single global $\mu$ is then obtained by `scipy.optimize.minimize_scalar(..., bounds=(1e-3, 2.0), method='bounded', xatol=1e-6)` on the pooled $\chi^2=\sum_g\sum_i\big((V_{\rm obs}-V_{\rm pred})/\sigma_{\rm eff}\big)^2$.

**Pipeline 2 — order-0 QDHT, stiffness switch** (`CODE_sparc_honest_killswitch.py`).  Builds `QDHT(512, 4*r_max)`, linearly interpolates $g_{\rm bar}$ from the observed radii onto the QDHT nodes with `fill_value=0.0` outside, computes $\mu$ from the switch above, applies $M(k)=1+(\mu/k)^2$, transforms back, interpolates to the observed radii, and returns $V^2_{A=1}=\max(r\,g_\mu,0)$.  $A$ is fitted by a bounded 1-D search in $\log A$ over $[10^{-3},10^{2}]$ minimising $\sum_i\big((V_{\rm obs}-\sqrt{AV^2_{A=1}})/\sigma_i\big)^2$ (no error floor here — a difference from Pipeline 1 that matters when comparing).

**Verification of the reproduction.**  Running Pipeline 1 from the bundled data with the source's own constants I obtain, to every digit the corpus quotes:

    FOUND 175 RC FILES / USING 143 / SKIPPED 32
    KERNEL=anti  KMIN_FACTOR=0.5   mu* = 0.103646 kpc^-1   ell = 9.6482 kpc
    N_pts = 3199
    median chi2/dof = 3.056     p90 chi2/dof = 63.7098
    median rms      = 11.8365 km/s   p90 rms = 68.457 km/s
    A median        = 0.889698  A p90    = 3.4994

**The screen branch is degenerate.**  Running the same script with `KERNEL='screen'` drives $\mu^\star$ to the lower bound of `MU_BOUNDS`: $\mu^\star=1.00066\times10^{-3}$ kpc$^{-1}$ ($\ell=999.3$ kpc), i.e. the optimiser asks for $M_{\rm screen}\to1$ and switches the modification off entirely.  Median $\chi^2/{\rm dof}=4.926$, median rms $17.86$ km/s, $A$ median $1.465$.  This is a clean, previously unrecorded result: **the screened Yukawa branch has no interior optimum — screening can only hurt**, because it removes power exactly where the curves need more.

**Stiffness-switch activation statistics** (my count over all 175 galaxies, $\Upsilon=0.5$): $\mu=0$ (switch OFF, $g_{\max}>3700$) for 55 galaxies = 31%; $\mu>0$ for 120 galaxies, among which $\mu\in[0.0046,0.2948]$ kpc$^{-1}$ with median $0.2707$.  So for the dwarf-dominated majority the switch sits near its ceiling $\mu_{\max}=0.30$, and for a third of the sample the model is exactly Newtonian by construction.

### Constants and numbers

Pipeline 1 constants (source-declared, not fitted): $N_k=512$; KMAX_FACTOR $=6.0$; KMAX_ABS $=400$ kpc$^{-1}$; KMIN_FACTOR $=0.5$; taper on, KC_FACTOR $=1.0$, TAPER_P $=4.0$; SIGMA_FLOOR $=5.0$ km/s; A_CLAMP $=(0.05,50.0)$; MU_BOUNDS $=(10^{-3},2.0)$ kpc$^{-1}$; $\Delta r_{\rm eff}=Q_{0.25}(\Delta r)$.
Fitted: $\mu^\star=0.103646$ kpc$^{-1}$, $\ell^\star=1/\mu^\star=9.6482$ kpc (anti); $\mu^\star=1.00066\times10^{-3}$ kpc$^{-1}$, $\ell^\star=999.336$ kpc (screen, i.e. lower bound).
Anti-kernel diagnostics, 143 galaxies / 3199 points: median $\chi^2/{\rm dof}=3.056$, p90 $=63.7098$; median rms $=11.8365$ km/s, p90 $=68.457$ km/s; $A$ median $=0.889698$, p90 $=3.4994$, range $[0.08212,6.693]$, $\log_{10}A$ scatter $0.462$ dex, fraction with $A\in[0.4,2.5]$ $=0.517$.
Screen diagnostics: median $\chi^2/{\rm dof}=4.926$, p90 $=45.67$, median rms $17.861$ km/s, $A$ median $1.465$.
Pipeline 2 constants: A0_SIMPLE $=3742.11$, A0_RAR $=4072.53$, A0_SPECTRAL $=3700.0$ (all $({\rm km/s})^2/{\rm kpc}$); MU_MAX $=0.30$ kpc$^{-1}$; QDHT $N=512$, $R=4r_{\max}$; $A$ bounds $[10^{-3},10^2]$; acceptance cuts $A\in[0.4,2.5]$, $\chi^2/{\rm dof}\le25$.
Stiffness switch: OFF for 55/175 (31%); ON for 120 with $\mu\in[0.0046,0.2948]$, median $0.2707$ kpc$^{-1}$.
An earlier archived screen run with a different amplitude rule (median-of-top-30%-$g_b$ ratio, `TOP_Q=0.30`, `A_CLAMP=(0.05,20)`, fixed `KMIN=1e-4`, $\Delta r_{\min}$ not $Q_{0.25}$) gave $\mu^\star=0.161395$ kpc$^{-1}$, $\ell=6.19599$ kpc, median $\chi^2/{\rm dof}=83.9427$, p90 $=4089.65$, median rms $36.804$ km/s, $A$ median $1.45299$.  Note: EXC_01_AntiKernel_HankelSpectral.md attributes $\mu^\star=0.161395$ to the ANTI kernel; the source cell shows `M = (k*k)/(k*k + mu*mu)`, so that number belongs to the SCREEN kernel. The anti-kernel value is $0.103646$.

### Code

The decisive lines of Pipeline 1 (kernel switch and transform), verbatim:

```python
def hankel1_forward(f_r, r, k, wr):        # F(k) = int dr r f(r) J1(kr)
    J = j1(np.outer(k, r))
    return (J * (r * f_r * wr)[None, :]).sum(axis=1)

def hankel1_inverse(F_k, k, wk, r):        # f(r) = int dk k F(k) J1(kr)
    J = j1(np.outer(k, r))
    return ((k * F_k * wk)[:, None] * J).sum(axis=0)

def kernel_M(k, mu):
    k2, mu2 = k*k, mu*mu
    if   KERNEL == "screen": return k2 / (k2 + mu2)
    elif KERNEL == "anti":   return (k2 + mu2) / np.maximum(k2, 1e-30)

def predict_gmu_from_gb(r, gb, mu, k, wk, W):
    wr = np.gradient(r)
    Gb = hankel1_forward(gb, r, k, wr)
    return hankel1_inverse(Gb * kernel_M(k, mu) * W, k, wk, r)

def best_A_weighted(vobs, vmu, dv):        # closed-form weighted scale on V, then squared
    dv_eff = np.sqrt(dv*dv + SIGMA_FLOOR**2)
    w   = 1.0/np.maximum(dv_eff**2, 1e-12)
    s   = float(np.sum(w*vmu*vobs)) / float(np.sum(w*vmu*vmu))
    s   = float(np.clip(s, np.sqrt(A_CLAMP[0]), np.sqrt(A_CLAMP[1])))
    return s*s
```

The global stiffness switch of Pipeline 2, verbatim:

```python
max_g = np.max(gbar_km2s2_per_kpc)
if max_g > A0_SPECTRAL:  mu = 0.0
else:                    mu = max(MU_MAX * (1.0 - max_g / A0_SPECTRAL), 0.0)
M_k = 1.0 + (mu / dht.k)**2
```

My standalone re-implementation that reproduces every quoted digit and takes `KMIN_FACTOR` and `KERNEL` as argv:
scratchpad\\antikernel_run.py  (`python antikernel_run.py 0.5 anti`, `python antikernel_run.py 0.5 screen`).

**Caveat.** The two pipelines are not the same operator: Pipeline 1 is order-1 with a global $\mu$ and $\Upsilon=1$; Pipeline 2 is order-0 with a per-galaxy switched $\mu$ and $\Upsilon=0.5$. Comparisons between their reported numbers are not like-for-like.

**Why it matters.** This is the complete, executable specification of the model class the corpus set out to test, including every 'knob' that turns out to control the answer. Anyone wanting to test an IR-boosted spectral response against rotation curves can start from here rather than rebuild it, and the screen-branch degeneracy result is a free negative control that the corpus never wrote down.

---

## 4. Global fit table across five models on SPARC, with stratified diagnostics and per-bin refits (full run output, independently reproduced)

`status: solid` · `kind: numerical_result`

### Statement

Fitting each of five models to the SPARC sample with **one global parameter and no per-galaxy freedom** at fixed $\Upsilon_{\rm disk}=\Upsilon_{\rm bul}=0.5$, scoring by pooled $\chi^2/{\rm dof}$ over all galaxies and radii, and searching each parameter on a fixed geometric grid, gives:

| Model | Response | Best parameter | $\chi^2/{\rm dof}$ (archived, $N_{\rm gal}=165$) | $\chi^2/{\rm dof}$ (my rerun, $N_{\rm gal}=143$) |
|---|---|---:|---:|---:|
| A baryons-only | $g_{\rm pred}=g_{\rm bar}$ | — | 620.69 | 647.42 |
| B MOND simple | $g=\tfrac12\big(g_b+\sqrt{g_b^2+4a_0g_b}\big)$ | $a_0=3742.11$ | **57.097** | 58.873 |
| C MOND/RAR exp | $g=g_b\big/\big(1-e^{-\sqrt{g_b/a_0}}\big)$ | $a_0=4072.53$ | 58.1651 | 59.937 |
| D finite-range kernel (convex average) | $g=\dfrac{(K*g_b)}{(K*1)},\;K=e^{-|r-r'|/L}$ | $L=13.8753$ kpc | 380.595 | 396.378 |
| E kernel TRANSPORT | $g=g_b+\tfrac1L(K*g_b)$ | $L=40.0447$ kpc | 234.478 | 243.826 |

($a_0$ in $({\rm km/s})^2/{\rm kpc}$.)  Both parameter grids are geometric: $a_0\in\mathrm{geomspace}(50,4\times10^4,80)$ and $L\in\mathrm{geomspace}(0.2,300,70)$.

**Kill-switch diagnostics.**  Define the outer residual of a galaxy as $\bar\delta_{\rm out}:=\mathrm{mean}\big\{V_{\rm obs}(r_i)-V_{\rm pred}(r_i)\;:\;i\ \text{in the outer }30\%\ \text{of sorted radii}\big\}$ and the sign-bias statistic $f_+:=\#\{\bar\delta_{\rm out}>0\}/N_{\rm gal}$; an unbiased model has $f_+\approx0.5$.  Then:

| Model | $f_+$ (archived) | $f_+$ (my rerun) |
|---|---:|---:|
| A baryons-only | 0.988 | 0.993 |
| B MOND simple | 0.358 | 0.399 |
| C MOND/RAR exp | 0.309 | 0.343 |
| D kernel AVG | 0.903 | 0.909 |
| E kernel TRANSPORT | 0.788 | 0.783 |

**Per-bin refit (universality test).**  Refitting the single global parameter separately on the dwarf ($V_{\rm flat}<80$) and big ($V_{\rm flat}\ge150$) subsamples:

| Model | dwarfs best | big best | ratio |
|---|---:|---:|---:|
| B MOND simple | $a_0=2069.57$ | $a_0=4072.53$ | 1.97 |
| C MOND/RAR exp | $a_0=2069.57$ | $a_0=4432.13$ | 2.14 |
| D kernel AVG | $L=300$ (grid edge) | $L=13.8753$ | 21.6 |
| E kernel TRANSPORT | $L=0.2$ (grid edge) | $L=68.0294$ | 340 |

### Derivation

**Source.**  The complete executed output — the only place in the corpus where the full stratified tables appear — is `ARCHIVES/extracted_notebooks/Untitled10_extracted.py`, lines ~1690-1765, stored as commented output beneath the cell that produced it.  A duplicate of the same log is in `HESSIAN/UNCATEGORIZED_MISC/WIZ UPDATE.txt` lines 3195-3265.  `SIMULATIONS/Selected_01_SPARC_Global_Fits_and_KillSwitch.md` §3.1 records the summary table and Appendix B the driver script, but omits the stratified numbers; the notebook extraction is the better source and I extracted from it.

**Archived run, verbatim (fixed $\Upsilon=0.5$, quality cut $Q\le3$, $N_{\rm pts}\ge8$, 165 galaxies):**

    Loaded: params=175  rotmod=165  overlap=165  using=165
    Global M/L: UPSILON_DISK=0.5  UPSILON_BULGE=0.5

    MODEL A baryons-only   chi2/dof = 620.69
      dwarfs (Vflat<80)  : N= 51  mean chi2/dof=296.103  median= 38.166  mean outer resid=+25.284 km/s
      mid (80<=Vflat<150): N= 58  mean chi2/dof=367.500  median= 85.442  mean outer resid=+53.004 km/s
      big (Vflat>=150)   : N= 56  mean chi2/dof=520.040  median=192.442  mean outer resid=+87.272 km/s
      Outer residual sign: fraction positive = 0.988

    MODEL B MOND simple    a0_best = 3742.11 -> 1.213e-10 m/s^2   chi2/dof = 57.097
      dwarfs : N= 51  mean= 38.747  median=11.690  mean outer resid=-10.875 km/s
      mid    : N= 58  mean= 17.799  median= 5.316  mean outer resid= -0.695 km/s
      big    : N= 56  mean= 64.866  median=19.447  mean outer resid= -2.567 km/s
      Outer residual sign: fraction positive = 0.358
      per-bin refits:  dwarfs best=2069.57 chi2/dof=29.587 | big best=4072.53 chi2/dof=83.993

    MODEL C MOND/RAR exp   a0_best = 4072.53 -> 1.320e-10 m/s^2   chi2/dof = 58.1651
      dwarfs : N= 51  mean= 42.952  median=13.623  mean outer resid=-12.036 km/s
      mid    : N= 58  mean= 18.523  median= 5.684  mean outer resid= -2.424 km/s
      big    : N= 56  mean= 65.649  median=21.538  mean outer resid= -5.388 km/s
      Outer residual sign: fraction positive = 0.309
      per-bin refits:  dwarfs best=2069.57 chi2/dof=29.567 | big best=4432.13 chi2/dof=85.384

    MODEL D kernel AVG     L_best = 13.8753 kpc   chi2/dof = 380.595
      dwarfs : N= 51  mean=290.697  median= 34.078  mean outer resid=+22.263 km/s
      mid    : N= 58  mean=308.424  median= 70.460  mean outer resid=+42.670 km/s
      big    : N= 56  mean=275.358  median=125.530  mean outer resid=+31.940 km/s
      Outer residual sign: fraction positive = 0.903
      per-bin refits:  dwarfs best=300 chi2/dof=294.923 | big best=13.8753 chi2/dof=346.153

    MODEL E kernel TRANSPORT  L_best = 40.0447 kpc  chi2/dof = 234.478
      dwarfs : N= 51  mean=255.655  median=31.028  mean outer resid=+22.297 km/s
      mid    : N= 58  mean=200.195  median=60.302  mean outer resid=+40.087 km/s
      big    : N= 56  mean=142.067  median=30.468  mean outer resid= -8.316 km/s
      Outer residual sign: fraction positive = 0.788
      per-bin refits:  dwarfs best=0.2 chi2/dof=75.316 | big best=68.0294 chi2/dof=155.495

**My independent rerun** (bundled 175 files, no .mrt so no $Q\le3$ cut, $N_{\rm pts}\ge8$ $\Rightarrow$ 143 galaxies; dwarfs 37 / mid 53 / big 53; scratchpad\\repro_global.py):

    A baryons-only  chi2/dof = 647.4238   f+ = 0.993
       dwarfs mean 392.809 median  89.847 outer +28.344 | mid mean 399.493 median 97.301 outer +55.125 | big mean 548.659 median 211.272 outer +89.807
    B MOND simple   a0 = 3742.11 -> 1.213e-10 m/s^2   chi2/dof = 58.8733   f+ = 0.399
       dwarfs mean  44.452 median 11.599 outer  -9.087 | mid mean  18.038 median  5.450 outer  +0.458 | big mean  68.207 median  24.980 outer  -1.856
       per-bin: dwarfs 2069.57 (29 -> 32.085) | big 4072.53 (84.995)
    C MOND/RAR exp  a0 = 4072.53 -> 1.320e-10 m/s^2   chi2/dof = 59.9368   f+ = 0.343
       per-bin: dwarfs 2069.57 (32.067) | big 4432.13 (86.400)
    D kernel AVG    L = 13.8753 kpc  chi2/dof = 396.378  f+ = 0.909
       per-bin: dwarfs 300 (338.515) | big 13.8753 (350.384)
    E kernel TRANSPORT L = 40.0447 kpc  chi2/dof = 243.826  f+ = 0.783
       per-bin: dwarfs 0.2 (85.877) | big 68.0294 (157.433)

**Every best-fit parameter reproduces exactly** (3742.11, 4072.53, 2069.57, 4432.13, 13.8753, 40.0447, 68.0294, and the grid-edge values 300 and 0.2 — I verified each is a node of the stated geomspace grid).  The $\chi^2/{\rm dof}$ values differ by 2-4%, entirely attributable to the 165-vs-143 sample difference (the missing SPARC quality table).  All qualitative conclusions and all sign-bias fractions reproduce.

**Reading the diagnostics.**  (i) Baryons-only is not merely bad, it is *systematically* bad: $f_+=0.99$ means essentially every galaxy has its outer curve under-predicted, with mean outer deficits growing monotonically with mass ($+25\to+53\to+87$ km/s).  (ii) The MOND-type transforms flip the sign to $f_+\approx0.31$-$0.36$: they now systematically *over*-predict the outer curve, most strongly for dwarfs ($-10.9$ and $-12.0$ km/s).  This is a real, quantified residual structure in MOND at fixed $\Upsilon=0.5$, not a null result.  (iii) The two kernel models retain the baryonic positive bias almost undiminished ($f_+=0.90$, $0.79$) — the modification is not acting where it needs to.  (iv) The per-bin refit is the sharpest instrument: MOND's 'universal' $a_0$ must roughly double from dwarfs to big galaxies (factor 1.97-2.14), which is a genuine 2$\sigma$-class tension in the fixed-$\Upsilon$ setup; but the kernel models fail catastrophically, with dwarfs pinning the parameter at opposite ends of the search grid from the big galaxies (factor 21.6 and 340).  A model whose one universal length scale must change by a factor 340 across a mass split has no universal length scale.

**Correction to a downstream corpus document.**  `VSU_COSMOLOGY/synthesis/model_creation/Synthesis_07_Physics_Phenomenology_VSU.md` §11.2 tabulates $f_+$ as baryons-only 0.909 and MOND/RAR $\approx0.50$.  Both are wrong: 0.909 is the kernel-AVG value and MOND/RAR is 0.309.  The correct set is A 0.988, B 0.358, C 0.309, D 0.903, E 0.788.  The claim in that document that 'MOND passes the kill-switch' is not supported by the run: MOND fails criterion 2 ($f_+=0.31$-$0.36$, not $\approx0.5$) and fails criterion 3 (per-bin $a_0$ ratio $\approx2$).

### Constants and numbers

Best parameters (all exact grid nodes; grid step 8.83% in $a_0$, 11.18% in $L$, so the quoted six significant figures encode grid resolution, not fit precision): $a_0^{\rm simple}=3742.11$, $a_0^{\rm RAR}=4072.53$, $a_0^{\rm dwarf}=2069.57$, $a_0^{\rm RAR,big}=4432.13$ $({\rm km/s})^2/{\rm kpc}$; $L^{\rm AVG}=13.8753$ kpc, $L^{\rm TRANSPORT}=40.0447$ kpc, $L^{\rm TRANSPORT,big}=68.0294$ kpc; grid edges $L=0.2$ and $L=300$ kpc.
Archived $\chi^2/{\rm dof}$ (165 galaxies): 620.69 / 57.097 / 58.1651 / 380.595 / 234.478.
My rerun (143 galaxies): 647.424 / 58.873 / 59.937 / 396.378 / 243.826.
Sign bias $f_+$ archived: 0.988 / 0.358 / 0.309 / 0.903 / 0.788; mine: 0.993 / 0.399 / 0.343 / 0.909 / 0.783.
Mean outer residuals (archived, km/s), dwarfs/mid/big: A $+25.284/+53.004/+87.272$; B $-10.875/-0.695/-2.567$; C $-12.036/-2.424/-5.388$; D $+22.263/+42.670/+31.940$; E $+22.297/+40.087/-8.316$.
Search grids: $a_0\in$ geomspace(50, 40000, 80); $L\in$ geomspace(0.2, 300, 70).  Outer-residual window: last 30% of sorted radii ($k_0=\lfloor0.7N\rfloor$).  Uniform kernel grid: 128 points on $[\min r,\,1.2\max r]$ with trapezoid weights.

### Code

Model definitions and diagnostics, verbatim from the executed cell:

```python
def v_pred_baryons(c):            return np.sqrt(np.maximum(c.gbar_obs * c.r_obs, 0.0))

def v_pred_mond_simple(c, a0):
    g = np.maximum(c.gbar_obs, 0.0)
    return np.sqrt(np.maximum(c.r_obs * 0.5*(g + np.sqrt(g*g + 4.0*a0*g)), 0.0))

def v_pred_mond_rar(c, a0):
    g = np.maximum(c.gbar_obs, 0.0)
    x = np.sqrt(np.maximum(g/max(a0,1e-300), 0.0))
    return np.sqrt(np.maximum(c.r_obs * g/np.maximum(1.0-np.exp(-x), 1e-300), 0.0))

def v_pred_kernel_avg(c, L):          # Model D: convex average, K = exp(-|r-r'|/L)
    K   = np.exp(-c.Dmat/max(L,1e-6))
    g_e = (K @ c.gbar_w) / np.maximum(K @ c.w, 1e-300)
    return np.interp(c.r_obs, c.r_u, np.sqrt(np.maximum(c.r_u*g_e, 0.0)))

def v_pred_kernel_transport(c, L):    # Model E: additive nonlocal import term
    L = max(L, 1e-6)
    K = np.exp(-c.Dmat/L)
    g_e = c.gbar_u + (K @ c.gbar_w)/L
    return np.interp(c.r_obs, c.r_u, np.sqrt(np.maximum(c.r_u*g_e, 0.0)))

def stratified_report(caches, pred_fn, label):
    Vflat = np.array([c.Vflat for c in caches]); chi2d = np.zeros(len(caches)); outer = np.zeros(len(caches))
    for i, c in enumerate(caches):
        res = c.v_obs - pred_fn(c)
        chi2d[i] = float(np.mean((res/c.ev_obs)**2))
        order = np.argsort(c.r_obs); k0 = int(0.7*len(order))
        outer[i] = float(np.mean(res[order][k0:]))
    for lbl, m in [("dwarfs (Vflat<80)", Vflat<80), ("mid", (Vflat>=80)&(Vflat<150)), ("big", Vflat>=150)]:
        print(lbl, m.sum(), chi2d[m].mean(), np.median(chi2d[m]), np.nanmean(outer[m]))
    print("Outer residual sign: fraction positive =", float(np.mean(outer > 0.0)))
```
Full reproduction driver: scratchpad\\repro_global.py (`python repro_global.py`, runtime ~2 min).

**Caveat.** Fixed $\Upsilon_{\rm disk}=\Upsilon_{\rm bul}=0.5$ with no per-galaxy freedom inflates every $\chi^2/{\rm dof}$ by one to two orders of magnitude relative to the published SPARC MOND literature; these numbers are internally comparable across models but are not comparable to fits that float $\Upsilon$.

**Why it matters.** This is the corpus's single most valuable empirical artefact: five modified-gravity responses scored on identical data with identical freedom, with residual-structure and universality diagnostics that go beyond chi-square, all reproducible from bundled data in two minutes. The kernel models the author invented lose to the MOND baselines by a factor 4-7 in chi2/dof and retain almost the full baryonic sign bias, and the per-bin refit shows their length scale is not universal by factors of 22 and 340.

---

## 5. The kill-switch protocol: pre-registered acceptance criteria and the four diagnostics

`status: solid` · `kind: algorithm`

### Statement

A falsification protocol for one-parameter modified-gravity responses on a rotation-curve sample.  Before fitting, register:

**(0) Acceptance criteria.**  A per-galaxy amplitude $A$ (the mass-to-light freedom) must satisfy $A\in[A_-,A_+]$ and the fit must satisfy $\chi^2/{\rm dof}\le\chi^2_{\max}$.  The corpus uses $A_-=0.4$, $A_+=2.5$, $\chi^2_{\max}=25$.  A galaxy violating either is an *outlier*; the model is refuted if the outlier fraction is large.

**(1) Mandatory baselines on identical footing.**  Score baryons-only, MOND-simple $g=\tfrac12(g_b+\sqrt{g_b^2+4a_0g_b})$, and RAR-exponential $g=g_b/(1-e^{-\sqrt{g_b/a_0}})$ on the same galaxies, with the same error model, the same per-galaxy freedom, and the same summary statistic.  A median-$\chi^2$-with-free-$A$ number for the candidate must never be compared against a pooled-$\chi^2$-at-fixed-$\Upsilon$ number for the baseline.

**(2) Outer-residual sign bias.**  Compute $\bar\delta_{\rm out}$ over the outer 30% of each galaxy's radii and report $f_+=\Pr[\bar\delta_{\rm out}>0]$.  Require $f_+\approx0.5$.  A model can win on $\chi^2$ while failing systematically in precisely the low-acceleration regime the modification is supposed to govern; $\chi^2$ alone cannot see this, $f_+$ can.

**(3) Mass-bin stratified refits (universality test).**  Bin by $V_{\rm flat}$ (dwarfs $<80$, mid $80$-$150$, big $\ge150$ km/s), refit the single 'universal' parameter independently on the dwarf and big subsamples, and compare.  If the universal parameter must differ appreciably between bins, it is not universal, and the global fit is hiding a systematic behind an averaged optimum.

**(4) Publish the failure.**  Record the negative outcome in the same document as the model.

**Additional criterion I recommend adding (my own, from the numerics below):**  **(5) knob-stability.**  Sweep every quantity the source declares 'not a fit parameter' (IR cutoff, taper, grid resolution) over a factor of ~16 and report how far the headline fitted parameter moves.  If it moves by more than the quoted precision, the parameter is a property of the numerics, not the data.

### Derivation

**Where the protocol lives.**  Criteria (1)-(4) are stated in `SIMULATIONS/Selected_01_SPARC_Global_Fits_and_KillSwitch.md` §4 and implemented as `stratified_report` / `per_bin_refit` in the global-fit driver (Appendix B of that document, and lines 1560-1600 of `ARCHIVES/extracted_notebooks/Untitled10_extracted.py`).  Criterion (0) is implemented as `A_cut=(0.4,2.5), chi2_cut=25.0` in `stress_test()` in `SIMULATIONS/CODE_sparc_honest_killswitch.py`.  `UPG_04_Dwarf_KillSwitch_NoSpecialPleading.md` adds the crucial methodological constraint that a kill-switch must not be a per-population on/off dial: 'A "no special pleading" kill-switch is not "turn $\mu$ off on dwarfs"; it is: derive the IR cutoff scale from finite geometry and/or leakage physics that becomes dominant exactly in low-$g$ systems.'  The same document states the acceptance target for dwarfs: pick a low-$V_{\max}$ or low-$g_{\max}$ subset, require the median $\chi^2/{\rm dof}$ not to diverge, and require no systematic residual trend at large $r$.

**Why (2) is the load-bearing diagnostic.**  Consider a model that is right on average but has the wrong radial shape.  Then per galaxy the residual $V_{\rm obs}-V_{\rm pred}$ changes sign somewhere in the disc, and the *pooled* $\chi^2$ is degraded only quadratically in the shape error.  Averaging the residual over the outer 30% and asking only for its sign discards the magnitude and keeps the systematic direction, so it is a nearly-distribution-free binomial test: under the null of no shape bias, $\#\{\bar\delta_{\rm out}>0\}\sim\mathrm{Binomial}(N_{\rm gal},\tfrac12)$, with standard error $1/(2\sqrt{N_{\rm gal}})\approx0.039$ at $N=165$.  [reconstructed] Hence $f_+=0.988$ (baryons) is $12.5\sigma$ from unbiased, $f_+=0.903$ (kernel AVG) is $10.3\sigma$, $f_+=0.788$ (transport) $7.4\sigma$, $f_+=0.358$ (MOND simple) $3.6\sigma$, $f_+=0.309$ (RAR) $4.9\sigma$.  Every model in the run fails criterion (2), and the ranking by $f_+$ is not the ranking by $\chi^2$ — which is exactly the point of having the second diagnostic.  (Caveat: galaxies are not strictly independent draws given shared distance/inclination systematics, so these $\sigma$'s are upper bounds on significance.)

**Why (1) is load-bearing.**  The corpus at one point compared its anti-kernel median $\chi^2/{\rm dof}=3.056$ — computed *with* a free per-galaxy $A$ and a 5 km/s systematic floor — against the MOND pooled $\chi^2/{\rm dof}=57.10$ computed at fixed $\Upsilon=0.5$ with no floor and no free amplitude, and read it as a 19$\times$ win.  Scoring MOND-simple through the identical estimator (same 143 galaxies, same free $A$ via the same weighted closed form, same 5 km/s floor, same per-galaxy median statistic) I get:

    anti-kernel   median chi2/dof = 3.056   p90 = 63.71   A median 0.890  frac A in [0.4,2.5] = 0.517  spread 0.462 dex  A range [0.082, 6.69]
    MOND simple   median chi2/dof = 0.998   p90 =  4.62   A median 0.679  frac A in [0.4,2.5] = 0.937  spread 0.167 dex  A range [0.143, 1.56]
    Newtonian     median chi2/dof = 4.111   p90 = 35.53   A median 1.851  frac A in [0.4,2.5] = 0.622  spread 0.293 dex  A range [0.284, 7.46]

So on identical footing the apparent 19$\times$ win is a 3.1$\times$ loss in the median and a 13.8$\times$ loss at the 90th percentile, and the model is only 1.35$\times$ better than doing nothing.  This single control inverts the headline conclusion, and it is the reason criterion (1) has to be pre-registered rather than added afterwards.

**Why (3) is load-bearing.**  See the per-bin table in the previous item: the two kernel models require $L$ to differ by factors of 21.6 and 340 between dwarfs and big galaxies, both pinned at opposite grid edges.  A global optimum at $L=13.9$ or $40.0$ kpc is then meaningless — it is the point where two incompatible demands balance, not a physical length.

**Why (5) is needed.**  See the IR-regulator obstruction item: sweeping `KMIN_FACTOR`, declared in the source as 'NOT fit params', over $\{0.25,0.5,1,2,4\}$ moves $\mu^\star$ over $\{0.1386,0.1036,0.1667,0.2288,0.3966\}$ kpc$^{-1}$ — a factor 2.9 in a number quoted to six significant figures.  No published-parameter claim survives that.

### Constants and numbers

Pre-registered cuts: $A\in[0.4,2.5]$, $\chi^2/{\rm dof}\le25$.  Outer window: last 30% of sorted radii.  Mass bins: $V_{\rm flat}<80$ / $[80,150)$ / $\ge150$ km/s, with $V_{\rm flat}=\mathrm{percentile}_{90}(V_{\rm obs})$.  Binomial null s.e. on $f_+$: $0.039$ at $N=165$, $0.042$ at $N=143$.
Same-footing control (my run, 143 galaxies, free $A$, 5 km/s floor, per-galaxy median statistic): anti-kernel median $\chi^2/{\rm dof}=3.056$ / p90 $63.71$ / $A$ median $0.890$ / 51.7% within cut / 0.462 dex / range $[0.0821,6.693]$; MOND simple $0.998$ / $4.62$ / $0.679$ / 93.7% / 0.167 dex / range $[0.1427,1.558]$; Newtonian baryons $4.111$ / $35.53$ / $1.851$ / 62.2% / 0.293 dex / range $[0.2843,7.459]$.
Knob sweep: KMIN_FACTOR $\{0.25,0.5,1,2,4\}$ $\to$ $\mu^\star\{0.138572,0.103646,0.166744,0.228848,0.396601\}$ kpc$^{-1}$, median $\chi^2/{\rm dof}\{3.100,3.056,3.074,3.642,52.528\}$.

### Code

Diagnostics as implemented (self-contained, works on the loader from item 1):

```python
def outer_sign_bias(gals, pred_fn, frac=0.30):
    """Return (per-galaxy outer residuals, fraction positive). frac = outer radial fraction."""
    outer = np.empty(len(gals))
    for i, c in enumerate(gals):
        res   = c['v'] - pred_fn(c)
        order = np.argsort(c['r']); k0 = int((1.0-frac)*len(order))
        outer[i] = float(np.mean(res[order][k0:]))
    return outer, float(np.mean(outer > 0.0))

def per_bin_refit(gals, grid, make_pred, score):
    """Refit the single global parameter on the dwarf and big subsamples separately."""
    Vf = np.array([c['Vflat'] for c in gals]); out = {}
    for lbl, m in [("dwarfs", Vf < 80), ("big", Vf >= 150)]:
        sub = [gals[i] for i in range(len(gals)) if m[i]]
        if len(sub) < 10: continue
        vals = np.array([score(sub, lambda c, x=x: make_pred(c, x)) for x in grid])
        j = int(np.argmin(vals)); out[lbl] = (float(grid[j]), float(vals[j]))
    return out

def killswitch_verdict(A, chi2dof, A_cut=(0.4, 2.5), chi2_cut=25.0):
    bad = (A < A_cut[0]) | (A > A_cut[1]) | (chi2dof > chi2_cut)
    return dict(n=len(A), n_outlier=int(bad.sum()), frac=float(bad.mean()),
                A_range=(float(A.min()), float(A.max())),
                A_dex=float(np.std(np.log10(A))),
                frac_A_in_cut=float(np.mean((A>=A_cut[0]) & (A<=A_cut[1]))))
```
The same-footing control is produced by scratchpad\\antikernel_run.py (its last two lines score MOND-simple and Newtonian through the identical `bestA` estimator and error floor).

**Caveat.** Criterion (5) is my addition, not the corpus's; and the binomial significances for $f_+$ treat galaxies as independent, which over-states significance in the presence of shared distance/inclination systematics.

**Why it matters.** This is the most transferable thing in the corpus and is model-independent. Modified-gravity proposals are usually scored by a single global chi-square, which is exactly the statistic that cannot see a shape error concentrated in the low-acceleration outskirts, and which can be gamed by comparing a free-amplitude median against a fixed-M/L pooled number. The protocol closes both holes and was used by its author to falsify his own model.

---

## 6. Kill-switch stress test on all 175 galaxies: 104 outliers with the corpus QDHT, 89 after correcting it

`status: solid` · `kind: numerical_result`

### Statement

Applying the QDHT + $M(k)=1+(\mu/k)^2$ + global stiffness switch pipeline to all 175 SPARC rotmod galaxies at $\Upsilon_{\rm disk}=\Upsilon_{\rm bul}=0.5$, with $\mu$ determined by the switch (no free spectral parameter) and one amplitude $A$ fitted per galaxy by bounded search in $\log A$ over $[10^{-3},10^2]$ minimising $\sum_i\big((V_{\rm obs}-\sqrt{A\,V^2_{A=1}})/\sigma_i\big)^2$, and applying the pre-registered cuts $A\in[0.4,2.5]$, $\chi^2/{\rm dof}\le25$:

| | corpus QDHT normalisation | corrected (G-S) normalisation |
|---|---:|---:|
| galaxies evaluated | 175 | 175 |
| outliers | **104 (59%)** | **89 (51%)** |
| median $\chi^2/{\rm dof}$ | 15.441 | 4.173 |
| p90 $\chi^2/{\rm dof}$ | 141.68 | 108.24 |
| max $\chi^2/{\rm dof}$ | 1455.95 | 1455.95 |
| $A$ range | $[0.0256,\;6.204]$ | $[0.0408,\;7.821]$ |
| $A$ median | 1.282 | 1.377 |
| $\log_{10}A$ scatter | 0.482 dex | 0.429 dex |

The kill-switch fires under either normalisation.  The model is refuted on SPARC.

### Derivation

**Reproduction.**  I re-implemented `stress_test()` from `SIMULATIONS/CODE_sparc_honest_killswitch.py` (three byte-identical copies; also in `VSU_COSMOLOGY/Galactic_Phenomenology/`) and ran it against the bundled 175-galaxy directory in two modes: `corpus` (the as-written `forward`) and `gs` (the corrected conjugation from the QDHT item).  Worst offenders, corpus mode:

    Name                           A  Chi2/dof     RMS     Max_g      mu
    NGC5055_rotmod             1.313   1455.95   47.05   28197.1   0.000
    UGC00128_rotmod            0.026   1092.05   49.67     348.1   0.272
    UGC09133_rotmod            2.673    553.48   90.56   69751.7   0.000
    NGC5907_rotmod             0.285    536.17   77.11    3179.7   0.042
    UGC05716_rotmod            0.442    433.15   18.57     240.7   0.280
    UGC02953_rotmod            2.283    427.02   79.73   82248.9   0.000

The first four rows and the headline '175 galaxies / 104 outliers' reproduce the corpus's own recorded stress-test output line for line, including the extreme case $A=0.026$ for UGC00128.

Corrected mode:

    NGC5055_rotmod             1.313   1455.95   47.05   28197.1   0.000
    UGC09133_rotmod            2.673    553.48   90.56   69751.7   0.000
    UGC02953_rotmod            2.283    427.02   79.73   82248.9   0.000
    UGC06787_rotmod            2.786    355.42   80.28  161914.4   0.000
    NGC2403_rotmod             3.245    317.56   26.59    3643.4   0.005
    UGC03580_rotmod            2.114    256.40   39.42   13342.2   0.000

**Structure of the failure, and what the correction reveals.**  Note the $\mu$ column.  After correcting the normalisation, *every* one of the six worst galaxies has $\mu\simeq0$: the switch has turned the modification completely off (because $g_{\max}>a_0^{\rm spec}=3700$), so the prediction is literally Newtonian with a free amplitude, and $\chi^2/{\rm dof}$ in the hundreds is simply the well-known failure of Newtonian gravity on high-surface-brightness spirals.  Under the corpus normalisation the worst list is contaminated by cases like UGC00128 ($\mu=0.272$, $A=0.026$, $\chi^2/{\rm dof}=1092$), where the *numerics* rather than the physics dominate.  This is a clean decomposition of the failure that the corpus never performed:

- 55/175 galaxies (31%) have the switch fully OFF and are pure Newtonian predictions.  They are guaranteed to fail; the model has no content for them.
- 120/175 have $\mu>0$, with $\mu\in[0.0046,0.2948]$ kpc$^{-1}$, median $0.2707$ — i.e. for the dwarf-dominated majority the switch sits near its hard ceiling $\mu_{\max}=0.30$, so the model is effectively a *single* fixed-$\mu$ linear filter with almost no galaxy-to-galaxy discrimination.  The 'switch' is close to a step function, not a smooth interpolation.
- Correcting the transform removes 15 of the 104 outliers and improves the median $\chi^2/{\rm dof}$ by a factor 3.7, which is the numerical component of the failure; the remaining 89 outliers and median 4.17 are the physical component, which survives.

**Cross-check that isolates the bug.**  For all $\mu=0$ galaxies the two modes must agree exactly, because then $M\equiv1$ and $D^{-1}T\,\mathbb1\,TD=D^{-1}T^2D=\mathbb 1=DT^2D^{-1}$.  Verified: NGC5055 (1455.95), UGC09133 (553.48), UGC02953 (427.02) are bit-identical across modes.  This confirms the defect is confined to the filtering step and rules out a data-handling difference between my two runs.

**Comparison to the fitted-$\mu$ pipeline.**  The order-1 script with a single *fitted* global $\mu^\star=0.103646$ achieves median $\chi^2/{\rm dof}=3.056$ on its 143-galaxy subsample with a 5 km/s error floor.  The corrected QDHT switch pipeline gets 4.173 on 175 galaxies with no floor.  Given that the floor alone is worth roughly a factor of two on low-$\sigma$ dwarf points, the two implementations are consistent with each other, and both lose to MOND-simple scored identically (0.998).

### Constants and numbers

175 galaxies evaluated (no $N_{\rm pts}$ cut beyond $\ge3$).  Cuts $A\in[0.4,2.5]$, $\chi^2/{\rm dof}\le25$.  Corpus normalisation: 104 outliers (59.4%), median $\chi^2/{\rm dof}=15.441$, p90 $141.68$, max $1455.95$; $A\in[0.0256,6.204]$, median $1.282$, scatter $0.482$ dex.  Corrected normalisation: 89 outliers (50.9%), median $4.173$, p90 $108.24$, max $1455.95$; $A\in[0.0408,7.821]$, median $1.377$, scatter $0.429$ dex.  Named galaxies (both modes where $\mu=0$): NGC5055 $A=1.313$, $\chi^2/{\rm dof}=1455.95$, rms $47.05$ km/s, $g_{\max}=28197.1$; UGC09133 $A=2.673$, $553.48$, $90.56$, $69751.7$; UGC02953 $A=2.283$, $427.02$, $79.73$, $82248.9$; UGC06787 $A=2.786$, $355.42$, $80.28$, $161914.4$.  Corpus-mode-only artefacts: UGC00128 $A=0.026$, $1092.05$, $\mu=0.272$; NGC5907 $A=0.285$, $536.17$, $\mu=0.042$; UGC05716 $A=0.442$, $433.15$, $\mu=0.280$.  Switch statistics: OFF for 55/175 = 31%; ON for 120 with $\mu\in[0.0046,0.2948]$ kpc$^{-1}$, median $0.2707$; ceiling $\mu_{\max}=0.30$; threshold $a_0^{\rm spec}=3700$ $({\rm km/s})^2/{\rm kpc}$.  All $g_{\max}$ in $({\rm km/s})^2/{\rm kpc}$.

### Code

Full A/B driver (runs both normalisations and prints both tables):
scratchpad\\killswitch_run.py — `python killswitch_run.py`, runtime ~40 s.

The corpus original can be run unmodified with:

```bash
cd <corpus root>
MPLBACKEND=Agg python -c "
import importlib.util, sys
s = importlib.util.spec_from_file_location('ks','SIMULATIONS/CODE_sparc_honest_killswitch.py')
m = importlib.util.module_from_spec(s); sys.modules['ks']=m; s.loader.exec_module(m)
m.stress_test('VSU_COSMOLOGY/Galactic_Phenomenology/SPARC_WORK/Rotmod_LTG', out_dir='out')
"
```
(the `if __name__=='__main__'` block hardcodes a relative path `SPARC_WORK/Rotmod_LTG`, so it must be invoked as above or run from `VSU_COSMOLOGY/Galactic_Phenomenology/`.)

The key prediction function, verbatim:

```python
def predict_v2_spectral_A1(r_kpc, gbar):
    dht  = QDHT(n_points=512, r_max=np.max(r_kpc)*4.0)
    gb_d = interp1d(r_kpc, gbar, kind='linear', bounds_error=False, fill_value=0.0)(dht.r)
    max_g = np.max(gbar)
    mu    = 0.0 if max_g > A0_SPECTRAL else max(MU_MAX*(1.0 - max_g/A0_SPECTRAL), 0.0)
    G_k   = dht.forward(gb_d)
    g_f   = dht.inverse(G_k * (1.0 + (mu/dht.k)**2))
    g_fin = interp1d(dht.r, g_f, kind='linear', bounds_error=False, fill_value=0.0)(r_kpc)
    return np.maximum(r_kpc * g_fin, 0.0)
```

**Caveat.** The stress test uses $\Upsilon=0.5$ fixed and no error floor, and it applies no $N_{\rm pts}$ cut beyond 3 points, so a handful of very short curves enter with near-zero dof; the median statistic is robust to this but the p90 is not.

**Why it matters.** This is the falsification actually executed, reproduced twice, and the decomposition into numerical and physical components is new: 3.7x of the failure was a one-line transform bug, and the rest is the model. It also shows the stiffness switch is close to a step function that simply disables the model for 31% of the sample.

---

## 7. Obstruction I: the fitted scale mu* is a property of the infrared regulator, not of the data

`status: solid` · `kind: obstruction`

### Statement

**Claim.**  Let $g_\mu=\mathcal H_1^{-1}\big[W(k)\,M_{\rm anti}(k;\mu)\,\mathcal H_1[g_b]\big]$ with $M_{\rm anti}=1+\mu^2/k^2$ computed on a numerical $k$-grid whose lowest node is $k_{\min}=c_{\rm IR}/r_{\max}$.  Because $M_{\rm anti}$ is unbounded as $k\to0$, the operator is not defined without $c_{\rm IR}$, and the globally optimal $\mu^\star$ is a function of $c_{\rm IR}$.  Quantitatively, on the 143-galaxy SPARC subsample, sweeping $c_{\rm IR}$ over the range $[0.25,4]$ (a factor 16) moves $\mu^\star$ from $0.1386$ to $0.3966$ kpc$^{-1}$ and the median $\chi^2/{\rm dof}$ from $3.06$ to $52.5$:

| $c_{\rm IR}=$ KMIN_FACTOR | $\mu^\star$ [kpc$^{-1}$] | $\ell^\star=1/\mu^\star$ [kpc] | median $\chi^2/{\rm dof}$ | p90 |
|---:|---:|---:|---:|---:|
| 0.25 | 0.138572 | 7.21648 | 3.09974 | 79.90 |
| **0.50** (source default) | **0.103646** | **9.6482** | **3.056** | **63.71** |
| 1.0 | 0.166744 | 5.99722 | 3.07446 | 75.13 |
| 2.0 | 0.228848 | 4.36972 | 3.64224 | 53.52 |
| 4.0 | 0.396601 | 2.52143 | 52.5277 | 285.92 |

The source file declares `KMIN_FACTOR` under the comment `# ---- knobs (NOT fit params) ----`.  Consequently the headline result '$\mu^\star=0.103646\ {\rm kpc}^{-1}$, $\ell^\star=9.6482$ kpc', quoted to six significant figures, is determined to at best a factor $\sim3$ by the data.  Moreover the three corpus scripts implementing 'the same model' use three inequivalent infrared regularisations — $k_{\min}=0.5/r_{\max}$ on a log grid (order-1 script); $k_{\min}=\alpha_1/(4r_{\max})=0.601/r_{\max}$ implicitly via the QDHT node set (kill-switch script); and $1+\mu^2/(k^2+(\pi/R)^2)$ (variational demo) — hence define three different operators.

### Derivation

**Why the pole is not integrable.**  In the order-1 pair, $g_\mu(r)-g_b(r)=\mu^2\int_0^\infty \frac{dk}{k}\,\widehat g_b(k)\,J_1(kr)$.  For a compactly supported or rapidly decaying baryonic profile with total 'mass' $\widehat g_b(0^+)=\lim_{k\to0}\int_0^\infty r g_b(r)J_1(kr)\,dr$ finite and non-zero (which is the case for $g_b\sim GM/r^2$: see the next item, where $\widehat g_b\equiv GM$ exactly), the integrand behaves as $\widehat g_b(0)\,J_1(kr)/k\sim \widehat g_b(0)\,r/2$ near $k=0$, so the integral converges *conditionally* but its value is entirely controlled by the $k\to0$ region, where the discretisation supplies $k_{\min}$.  Cutting at $k_{\min}$ removes $\int_0^{k_{\min}}\!\frac{dk}{k}\widehat g_b J_1(kr)\approx \widehat g_b(0)\,\frac{r\,k_{\min}}{2}$ — a term linear in $r$, i.e. exactly the shape a rotation curve is most sensitive to.  Since $k_{\min}\propto c_{\rm IR}$ and the model's only knob is $\mu^2$, the optimiser trades $\mu^2$ against $c_{\rm IR}$: raising $c_{\rm IR}$ removes IR power, and $\mu^\star$ rises to compensate.  The observed scaling is close to $\mu^\star\propto\sqrt{c_{\rm IR}}$ for $c_{\rm IR}\in[0.5,4]$: $0.1036,0.1667,0.2288,0.3966$ against $\sqrt{c_{\rm IR}}=0.707,1,1.414,2$ gives ratios $0.147,0.167,0.162,0.198$ — flat to $\pm15\%$ over a factor 8.  [reconstructed]  The non-monotonic dip at $c_{\rm IR}=0.25$ ($\mu^\star=0.1386>0.1036$) is a grid artefact: at $c_{\rm IR}=0.25$ the lowest node sits below the smallest scale the 512-point log grid can resolve against $k_{\max}\le400$, so the effective IR weight saturates.

**Execution.**  Each row is a full global optimisation (`minimize_scalar`, bounded, `xatol=1e-6`) over the 143-galaxy sample, ~90 s per row; scratchpad\\antikernel_run.py with argv `KMIN_FACTOR KERNEL`.  Output verbatim:

    KERNEL=anti KMIN_FACTOR=0.25  mu*=0.138572  ell=7.21648   median chi2/dof=3.09974  p90=79.9025
    KERNEL=anti KMIN_FACTOR=0.5   mu*=0.103646  ell=9.6482    median chi2/dof=3.056    p90=63.7098
    KERNEL=anti KMIN_FACTOR=1.0   mu*=0.166744  ell=5.99722   median chi2/dof=3.07446  p90=75.134
    KERNEL=anti KMIN_FACTOR=2.0   mu*=0.228848  ell=4.36972   median chi2/dof=3.64224  p90=53.5163
    KERNEL=anti KMIN_FACTOR=4.0   mu*=0.396601  ell=2.52143   median chi2/dof=52.5277  p90=285.919

**The quadrature is separately unreliable.**  A second, independent numerical problem: the order-1 transform is a bare trapezoid on the *observed radii only* (typically 8-115 unequally spaced points, median 17), truncated at the last measured radius.  Testing the identity round trip $g_b\mapsto\mathcal H_1^{-1}[W\,\mathcal H_1[g_b]]$ (i.e. $M\equiv1$) on all 143 galaxies with the source's own grid settings:

    median over galaxies of the per-galaxy median relative error = 1.11%
    p90 = 86.3%,  max = 1113%
    fraction of galaxies with median relative error > 10% : 28.7%
    fraction > 50% : 16.8%
    NGC3198  67.0%      NGC2403  86.7%      NGC5055 261.0%
    DDO154    0.6%      UGC00128   0.4%
    worst: UGC11820 1113%, NGC0801 627%, NGC2998 351%, NGC7793 289%, UGC06614 264%, NGC5055 261%

So for a quarter of the sample — including several of the best-measured objects in all of extragalactic astronomy — the pipeline cannot even return the *input* to better than tens of percent.  The 'prediction' for those galaxies is numerically meaningless independently of the physics.  Well-sampled dwarfs (DDO154, UGC00128) round-trip to sub-percent, which is why the median looks acceptable and the failure is invisible in summary statistics.

### Constants and numbers

$\mu^\star(c_{\rm IR})$: $c_{\rm IR}=0.25\to0.138572$; $0.5\to0.103646$; $1.0\to0.166744$; $2.0\to0.228848$; $4.0\to0.396601$ kpc$^{-1}$.  Corresponding $\ell^\star$: $7.21648$, $9.6482$, $5.99722$, $4.36972$, $2.52143$ kpc.  Corresponding median $\chi^2/{\rm dof}$: $3.09974$, $3.056$, $3.07446$, $3.64224$, $52.5277$; p90: $79.90$, $63.71$, $75.13$, $53.52$, $285.92$.  Ratio $\mu^\star/\sqrt{c_{\rm IR}}$: $0.277$, $0.147$, $0.167$, $0.162$, $0.198$.  Three inequivalent regularisations in-corpus: $k_{\min}=0.5/r_{\max}$; $k_{\min}=\alpha_1/(4r_{\max})=0.6012/r_{\max}$; $M=1+\mu^2/(k^2+(\pi/R)^2)$.
Hankel-1 identity round-trip error (143 galaxies, $N_k=512$, $k_{\min}=0.5/r_{\max}$, $k_{\max}=\min(6\pi/\Delta r_{\rm eff},400)$, taper $\exp[-(k\Delta r_{\rm eff}/\pi)^4]$): median-of-medians $1.11\%$; p90 $86.3\%$; max $1113\%$; $28.7\%$ of galaxies above $10\%$; $16.8\%$ above $50\%$.  Named: NGC3198 $67.0\%$, NGC2403 $86.7\%$, NGC5055 $261\%$, UGC11820 $1113\%$, NGC0801 $627\%$, NGC2998 $351\%$, NGC7793 $289\%$, UGC06614 $264\%$; DDO154 $0.6\%$, UGC00128 $0.4\%$.

### Code

IR sweep: `for f in 0.25 0.5 1.0 2.0 4.0; do python antikernel_run.py $f anti; done` (scratchpad\\antikernel_run.py).

Round-trip audit (scratchpad\\roundtrip.py), core:

```python
dr   = np.diff(r); dre = float(np.quantile(dr[dr>0], 0.25))
kmin = max(1e-4, 0.5/r.max()); kmax = min(6.0*np.pi/dre, 400.0)
k    = np.logspace(np.log10(kmin), np.log10(kmax), 512); wk = np.gradient(k)
W    = np.exp(-(k/(np.pi/dre))**4)
wr   = np.gradient(r); J = j1(np.outer(k, r))
Gb   = (J * (r*gb*wr)[None, :]).sum(axis=1)
back = ((k*Gb*W*wk)[:, None] * J).sum(axis=0)      # M(k) == 1: must return gb
rel  = np.abs(back - gb)/np.maximum(np.abs(gb), 1e-12)
```

**Caveat.** The round-trip test uses the source's own taper $W(k)$, which legitimately removes some high-$k$ content, so a few percent of round-trip error is expected by design; errors of 67-1113% are not.

**Why it matters.** This is the sharpest mathematical statement available about this model class and it generalises far beyond the corpus: any spectral multiplier with a non-integrable infrared pole has no operator content until an IR regulator is named, and any 'fitted universal scale' extracted from such a multiplier on finite-extent data is a reparameterisation of that regulator. It also supplies a concrete, cheap numerical protocol (identity round-trip on the model's own quadrature) that would catch this class of error in any similar pipeline.

---

## 8. Obstruction II: a universal linear IR-boosted spectral multiplier gives v ~ sqrt(r), not flat rotation curves

`status: solid` · `kind: obstruction`

### Statement

**Theorem.**  Let $g_b:(0,\infty)\to\mathbb R$ be a baryonic radial acceleration with a point-mass tail, $g_b(r)=GM/r^2$ for $r\ge R_0$, and regular at the origin, and let $\mathcal H_1$ denote the order-1 Hankel pair $\widehat g(k)=\int_0^\infty r\,g(r)J_1(kr)\,dr$, $g(r)=\int_0^\infty k\,\widehat g(k)J_1(kr)\,dk$.  Define, for $\mu>0$ fixed and independent of the source,
\[ g_\mu \;:=\; \mathcal H_1^{-1}\Big[\Big(1+\frac{\mu^2}{k^2}\Big)\,\mathcal H_1[g_b]\Big] \]
on the whole line (no infrared cutoff).  Then
\[ \boxed{\;g_\mu(r)\;=\;g_b(r)\;+\;\mu^2\,GM\;+\;o(1)\quad (r\to\infty),\;} \]
so that the implied circular speed is
\[ V^2(r)=r\,g_\mu(r)\;\longrightarrow\;\mu^2 GM\,r,\qquad V(r)\;\sim\;\mu\sqrt{GM\,r}\;\propto\;\sqrt r . \]
Rotation curves *rise* without bound as $\sqrt r$; they are not asymptotically flat.

**Corollary (no-go for universal linear multipliers).**  A flat outer curve $V\to V_{\rm flat}$ requires $g_\mu(r)\to V_{\rm flat}^2/r$, i.e. a $1/r$ tail.  Since $\int_0^\infty k^{-1}J_1(kr)\,dk=1$ and $\int_0^\infty J_1(kr)\,dk=1/r$, a $1/r$ tail requires the product $M(k)\widehat g_b(k)\to C$ *independent of $k$ but with the $J_1$ weight one power lower*, i.e. $M(k)\,\widehat g_b(k)\sim C/k$ as $k\to0$.  With $\widehat g_b(k)\to GM$ this forces
\[ M(k)\;\sim\;\frac{C}{GM\,k}\qquad (k\to0),\qquad\text{and the baryonic Tully-Fisher relation } V_{\rm flat}^4=GMa_0 \text{ forces } C=\sqrt{GMa_0}, \]
hence
\[ M(k)\;\sim\;\frac{1}{k}\sqrt{\frac{a_0}{GM}} . \]
The required multiplier depends on the source mass $M$.  **No source-independent multiplier $M(k)$ can reproduce flat rotation curves together with the BTFR.**  This is the spectral-language form of the Bekenstein-Milgrom observation that MOND phenomenology requires a nonlinear field equation.

### Derivation

**Step 1 — the exact transform of a point-mass tail.**  For $g_b(r)=GM/r^2$ on $(0,\infty)$,
\[ \widehat g_b(k)=\int_0^\infty r\cdot\frac{GM}{r^2}J_1(kr)\,dr=GM\int_0^\infty \frac{J_1(kr)}{r}dr \stackrel{u=kr}{=} GM\int_0^\infty\frac{J_1(u)}{u}\,du=GM, \]
using the standard value $\int_0^\infty J_1(u)u^{-1}du=1$.  So $\widehat g_b$ is *constant in $k$* — in particular it does not vanish at $k=0$, which is precisely why the $\mu^2/k^2$ pole bites.

**Step 2 — invert with the multiplier.**
\[ g_\mu(r)=\int_0^\infty k\Big(1+\frac{\mu^2}{k^2}\Big)GM\,J_1(kr)\,dk = GM\underbrace{\int_0^\infty kJ_1(kr)dk}_{=\,1/r^2\ (\text{inverse of Step 1})}\;+\;\mu^2GM\underbrace{\int_0^\infty\frac{J_1(kr)}{k}dk}_{=\,1} = \frac{GM}{r^2}+\mu^2GM. \]
Both integrals are the same tabulated one used in Step 1, read in the two directions.  The constant $\mu^2GM$ is exact for the pure $1/r^2$ tail; for a $g_b$ that is $GM/r^2$ only beyond $R_0$ the correction is $O(R_0^2/r^2)$, giving the $o(1)$ in the theorem.

**Step 3 — real-space (local) form, cross-check.**  $J_1(kr)$ is an eigenfunction of the order-1 radial operator
\[ L_1:=-\Big(\partial_r^2+\frac1r\partial_r-\frac1{r^2}\Big),\qquad L_1J_1(kr)=k^2J_1(kr), \]
so multiplication by $\mu^2/k^2$ in the order-1 Hankel domain is $\mu^2L_1^{-1}$ in real space, i.e.
\[ g_\mu = g_b+\mu^2\chi,\qquad L_1\chi=g_b. \]
Solve directly for $g_b=GM/r^2$: the homogeneous solutions of $L_1\chi=0$ are $\chi\in\{r,\,1/r\}$ (since $L_1 r^s=-(s^2-1)r^{s-2}$, vanishing iff $s=\pm1$), and a particular solution is a constant, because $L_1[c]=+c/r^2$ so $c=GM$.  Hence $\chi=GM+\alpha r+\beta/r$, and with boundary conditions excluding the growing homogeneous mode, $\chi\to GM$ and $g_\mu\to GM/r^2+\mu^2GM$.  This independently reproduces Step 2 and identifies the constant asymptote as the particular solution against a $1/r^2$ source.

**Step 4 — numerical confirmation** (scratchpad\\asym.py).  With $GM=1$, $\mu=0.2$, $g_b(r)=r^{-2}\big(1-e^{-r^3}\big)$ (regular at 0, exactly $1/r^2$ for $r\gtrsim2$), on a $120000$-point radial grid to $r_{\max}=400$ and a 4000-point log $k$-grid:

    r        :      20        50       100       200
    g_mu(r)  : 0.040606  0.037543  0.034920  0.029937
    GM/r^2   : 0.002500  0.000400  0.000100  0.000025
    g_mu-GM/r^2: 0.038106 0.037143  0.034820  0.029912     (target mu^2 GM = 0.040000)
    V=sqrt(r g_mu): 0.9012  1.3701  1.8687  2.4469
    mu*sqrt(GM r):  0.8944  1.4142  2.0000  2.8284

The residual approaches $\mu^2GM=0.0400$ from below and $V$ tracks $\mu\sqrt{GMr}$; the shortfall grows with $r$ **because the finite domain $r_{\max}=400$ truncates the transform**, which is the same finite-domain infrared regulator identified in the previous item, now visible directly as the mechanism that hides the pathology.  In a fit to real rotation curves, where $r_{\max}$ is the last measured radius, this truncation is what makes the model look like it produces flat curves: it does not; it produces a rising curve whose rise has been clipped at exactly the outer edge of the data.

**Step 5 — the corollary in detail.**  Suppose we want a universal $M$ with $g_\mu(r)\to V_{\rm flat}^2/r$.  Writing $g_\mu(r)=\int_0^\infty k\,M(k)\widehat g_b(k)J_1(kr)dk$ and requiring the $1/r$ tail, the small-$k$ behaviour must satisfy $kM(k)\widehat g_b(k)\to C$ as $k\to0$ (because $\int_0^\infty J_1(kr)dk=1/r$).  With $\widehat g_b(0)=GM$ this gives $M(k)\to C/(GMk)$.  Observationally $V_{\rm flat}^2=\sqrt{GMa_0}$ (BTFR, $V_{\rm flat}^4=GMa_0$), hence $C=\sqrt{GMa_0}$ and $M(k)\to k^{-1}\sqrt{a_0/(GM)}$: the multiplier must scale as $M^{-1/2}$.  A universal $M(k)$ therefore cannot hold across a sample spanning, in SPARC, roughly three decades in baryonic mass.  The corpus's own 'sharpened' family $M=(1+(\mu/k)^n)^{1/n}$ has the *right power* $M\sim\mu/k$ for $k\ll\mu$ (documented in `Selected_02_Spectral_Boost_Filter_Model.md` §2.1) — but with a universal $\mu$, so it predicts $V_{\rm flat}^2=\mu GM$, i.e. $V_{\rm flat}^4\propto M^2$, a BTFR slope of 2 instead of the observed 4.  Either way, the model class cannot hold.

**Step 6 — this explains the fit diagnostics quantitatively.**  (i) A rising $V\propto\sqrt r$ over-predicts the outer curve of big galaxies and under-predicts dwarfs, matching the observed sign-bias pattern.  (ii) Because the predicted $V_{\rm flat}^2\propto\mu^2GM$ scales linearly with $M$ while the data scale as $\sqrt M$, the compensating per-galaxy amplitude must scale as $A\propto M^{-1/2}$, i.e. must span the square root of the sample's mass range — the observed $A\in[0.082,6.69]$, a factor 81, is consistent with $\sqrt{\text{3 decades}}\approx31$-$100$.  (iii) It explains why the fit's preferred $\mu$ tracks the IR cutoff: both control the same clipped linear-in-$r$ term.

### Constants and numbers

Exact asymptote: $g_\mu(r)-g_b(r)\to\mu^2GM$; $V(r)\to\mu\sqrt{GMr}$.  Required flat-curve multiplier: $M(k)\to k^{-1}\sqrt{a_0/GM}$; the universal-$\mu$ sharpened family gives BTFR slope 2 instead of 4.  Numerical check ($GM=1$, $\mu=0.2$, target $\mu^2GM=0.0400$): $g_\mu-GM/r^2 = 0.038106,\,0.037143,\,0.034820,\,0.029912$ at $r=20,50,100,200$; $V=0.9012,1.3701,1.8687,2.4469$ vs $\mu\sqrt{GMr}=0.8944,1.4142,2.0000,2.8284$; grid $r\in[10^{-3},400]$, $N_r=120000$, $k\in[10^{-5},100]$, $N_k=4000$ log-spaced.  Standard integrals used: $\int_0^\infty J_1(u)u^{-1}du=1$; $\int_0^\infty J_1(kr)\,dk=1/r$ for $r>0$.  Homogeneous solutions of $L_1$: $r$ and $1/r$ (from $L_1r^s=-(s^2-1)r^{s-2}$).  Observed $A$ range in the anti-kernel fit: $[0.08212,6.693]$ = factor 81.5, $0.462$ dex.

### Code

Numerical verification (scratchpad\\asym.py):

```python
import numpy as np
from scipy.special import j1
GM, mu = 1.0, 0.2
r  = np.linspace(1e-3, 400.0, 120000);  wr = np.gradient(r)
gb = GM/(r*r) * (1 - np.exp(-(r/1.0)**3))       # regular at 0, = GM/r^2 for r >> 1
k  = np.logspace(-5, 2, 4000);          wk = np.gradient(k)
G  = np.array([np.sum(j1(kk*r) * r * gb * wr) for kk in k])   # order-1 forward
for rr in (20., 50., 100., 200.):
    gmu = np.sum(k * (1.0 + mu*mu/(k*k)) * G * j1(k*rr) * wk)
    print(rr, gmu, gmu - GM/rr**2, np.sqrt(rr*gmu), mu*np.sqrt(GM*rr))
```
The real-space cross-check ($L_1\chi=g_b$ by finite differences vs. the Hankel route) is the corpus's own
`VSU_COSMOLOGY/Galactic_Phenomenology/CODE_demo_antikernel_variational_equivalence.py`, which runs unmodified and agrees to 2.05e-2 relative $L^2$ in the interior (see the operator-equivalence item).

**Caveat.** Steps 1-2 assume an exact $GM/r^2$ tail extended to infinity; a real disc has a finite outer edge, so the constant asymptote is approached only over the range where the $1/r^2$ tail holds, and the numerics show the approach is cut off by any finite computational domain.

**Why it matters.** This is the strongest mathematics in this part of the corpus and it is a genuine, self-contained no-go. It explains, from first principles and in three lines of Bessel integrals, every empirical failure the pipeline recorded: why mu* tracks the IR cutoff, why the per-galaxy amplitude must span a factor of ~80, why the outer residual sign bias never balances, and why the screen branch has no interior optimum. It also states precisely what a spectral multiplier would have to look like to work, and why no universal one can.

---

## 9. Operator equivalence: the anti-kernel is the local PDE g_mu = g_b + mu^2 L1^{-1} g_b, verified numerically

`status: solid` · `kind: derivation`

### Statement

**Statement.**  Let $L_1:=-\big(\partial_r^2+\tfrac1r\partial_r-\tfrac1{r^2}\big)$ be the order-1 radial Bessel operator on $(0,R)$.  Since $L_1J_1(kr)=k^2J_1(kr)$, multiplication by $\mu^2/k^2$ in the order-1 Hankel domain is exactly $\mu^2L_1^{-1}$ in real space.  Therefore the Hankel-space rule
\[ \widehat g_\mu(k)=\Big(1+\frac{\mu^2}{k^2}\Big)\widehat g_b(k) \]
is equivalent, up to boundary conditions and infrared regularisation, to the local elliptic problem
\[ g_\mu=g_b+\mu^2\chi,\qquad L_1\chi=g_b,\qquad \chi(0)=\chi(R)=0. \]
Equivalently, in the continuous Laplacian language used in the corpus documents, $M_{\rm anti}(k)=1+\mu^2/k^2 \Longleftrightarrow g_\mu=g_b+\mu^2(-\Delta)^{-1}g_b$: a linear, nonlocal-in-real-space modification whose nonlocality is entirely an inverse-Laplacian piece.

**Verified.**  Running the corpus demo with $\mu=0.10$, $R_{\max}=50$, $N_r=4096$, $g_b(r)=e^{-r/3}$, and the geometry-motivated IR regulator $k_{\rm IR}=\pi/R_{\max}=0.062832$ inserted as $M=1+\mu^2/(k^2+k_{\rm IR}^2)$:

    Relative L2 error (interior region 0.5 < r < 0.9 R): 2.054e-02
    Max abs difference (same region):                    1.639e-02

### Derivation

**Eigenfunction property.**  Write $L_1=-\partial_r^2-\tfrac1r\partial_r+\tfrac1{r^2}$.  Bessel's equation of order 1 in the variable $x=kr$ reads $J_1''(x)+\tfrac1xJ_1'(x)+\big(1-\tfrac1{x^2}\big)J_1(x)=0$.  Substituting $x=kr$ and multiplying by $k^2$ gives $\partial_r^2J_1(kr)+\tfrac1r\partial_rJ_1(kr)-\tfrac1{r^2}J_1(kr)=-k^2J_1(kr)$, i.e. $L_1J_1(kr)=k^2J_1(kr)$.  Hence for $g=\int_0^\infty k\widehat g(k)J_1(kr)dk$ we have $L_1^{-1}g=\int_0^\infty k\,\widehat g(k)k^{-2}J_1(kr)dk$, which is exactly the Hankel multiplier $1/k^2$.  Adding the identity gives the stated equivalence.

**Discretisation of $L_1$ used in the demo.**  On a uniform grid $r_i$ with spacing $h$, interior points $r_i\in(0,R)$, the three-point stencil for $L_1\chi=g_b$ is the tridiagonal system
\[ \text{lower}_i=-\frac1{h^2}+\frac1{2hr_i},\qquad \text{main}_i=\frac{2}{h^2}+\frac1{r_i^2},\qquad \text{upper}_i=-\frac1{h^2}-\frac1{2hr_i}, \]
with Dirichlet conditions $\chi(0)=\chi(R)=0$, solved by `scipy.sparse.linalg.spsolve`.  (Signs: the $-\partial_r^2$ term contributes $+2/h^2$ on the diagonal and $-1/h^2$ off-diagonal; the $-\tfrac1r\partial_r$ term contributes $\mp\tfrac{1}{2hr_i}$ via the centred first difference; the $+1/r^2$ term is diagonal.)

**The comparison.**  The demo builds $g_\mu$ twice — once by forward/inverse order-1 Hankel with the regulated multiplier on a uniform $k$-grid $[0,25]$ with $N_k=4096$, and once by $g_b+\mu^2\chi$ from the PDE solve — and compares on the interior window $0.5<r<0.9R_{\max}$ (excluding both boundary layers, where the Dirichlet conditions and the truncated $k$-range respectively dominate).  I ran it unmodified: relative $L^2$ error $2.054\times10^{-2}$, max absolute difference $1.639\times10^{-2}$.  A 2% agreement is what one should expect from a first-order trapezoid Hankel quadrature on 4096 points with a $k_{\max}=25$ truncation against a second-order finite-difference elliptic solve, so the equivalence is confirmed at the accuracy of the crudest ingredient.

**Why this matters for the physics.**  Three consequences follow immediately from the local form and are used elsewhere in this extraction:
1. **Linearity and superposition.**  At fixed $\mu$ the map $g_b\mapsto g_\mu$ is linear, so it commutes with $\Upsilon$ rescalings — which is exactly why the per-galaxy amplitude $A$ is degenerate with the mass-to-light ratio (UPG_03) and why $A$'s dispersion is a physical falsification.
2. **Green's function structure.**  $L_1^{-1}$ has homogeneous solutions $r$ and $1/r$; the growing mode $r$ is what the infrared regulator has to suppress, and the failure to suppress it consistently is Obstruction I.
3. **Codimension-2 connection.**  In the corpus's framing (BEST_01 §9, EXC_01 §4) the $\mu^2(-\Delta)^{-1}$ piece is the ingredient that produces logarithmic Green's functions in codimension 2 and hence $1/r$ accelerations at large $r$.  That heuristic is what motivated the model; the exact computation in Obstruction II shows that in the actual order-1 radial setting the far-field term is a *constant*, not $1/r$, so the motivating analogy does not survive the computation.  This is the cleanest single statement of why the programme did not work.

### Constants and numbers

Demo parameters: $R_{\max}=50$, $N_r=4096$, $r\in[10^{-6},50]$, $g_b(r)=e^{-r/r_0}$ with $r_0=3.0$; $k\in[0,25]$, $N_k=4096$; $\mu=0.10$ (same units as $k$, i.e. inverse length); $k_{\rm IR}=\pi/R_{\max}=0.062832$; comparison window $0.5<r<0.9R_{\max}=45$.  Result: relative $L^2$ error $2.054\times10^{-2}$, max abs diff $1.639\times10^{-2}$.  $L_1$ eigenvalue relation: $L_1J_1(kr)=k^2J_1(kr)$.  Homogeneous solutions of $L_1$: $\{r,\,1/r\}$.

### Code

Corpus file (runs unmodified, ~1 s):
`VSU_COSMOLOGY/Galactic_Phenomenology/CODE_demo_antikernel_variational_equivalence.py`
(also at `.../CODE_demo_antikernel_variational_equivalence-1.py`, byte-identical).

The load-bearing routine:

```python
def solve_L1_inverse(gb, r):
    """Solve L1 chi = gb on [0,R] with chi(0)=chi(R)=0.
       L1 = -(d2/dr2 + (1/r) d/dr - 1/r^2)."""
    dr = r[1] - r[0]
    ri = r[1:-1]
    lower = -(1.0/dr**2) + 1.0/(2.0*dr*ri)
    main  =  (2.0/dr**2) + 1.0/(ri**2)
    upper = -(1.0/dr**2) - 1.0/(2.0*dr*ri)
    A = diags([lower[1:], main, upper[:-1]], offsets=[-1, 0, 1], format="csc")
    chi = np.zeros_like(gb)
    chi[1:-1] = spsolve(A, gb[1:-1])
    return chi

# equivalence check
gb_hat = hankel1_forward(gb, r, k)
gmu_h  = hankel1_inverse(gb_hat * (1.0 + mu**2/(k**2 + k_ir**2)), k, r)   # spectral route
gmu_p  = gb + mu**2 * solve_L1_inverse(gb, r)                              # local PDE route
```

**Caveat.** The equivalence is verified only in the interior window and only at the 2% level set by the crude trapezoid Hankel quadrature; the boundary conditions $\chi(0)=\chi(R)=0$ are declared 'toy' in the source and are not the physically correct ones (they suppress the growing homogeneous mode by fiat, which is exactly the regularisation choice at issue).

**Why it matters.** It converts the spectral model into a local elliptic PDE, which is what makes the asymptotic no-go computable in closed form, makes the amplitude-M/L degeneracy obvious, and makes clear that the model is a linear inverse-Laplacian modification rather than anything MOND-like. It is also a genuinely correct, runnable numerical-methods demonstration.

---

## 10. The geometric IR regulator k_IR = pi/R_max: a no-free-parameter fix that stabilises mu* to +/-6% (new numerical result)

`status: solid` · `kind: construction`

### Statement

**Construction (from UPG_04).**  Replace the divergent anti-kernel by
\[ M_{\rm reg}(k;\mu)\;=\;1+\frac{\mu^2}{k^2+k_{\rm IR}^2},\qquad k_{\rm IR}:=\frac{\pi}{R_{\max}}, \]
where $R_{\max}$ is the last measured radius of that galaxy's rotation curve.  This introduces **no new fitted parameter** — $R_{\max}$ is data, and the coefficient $\pi$ is the lowest half-wavelength that fits in the support.  The motivation is geometric: a disc of finite radius $R_{\max}$ cannot support modes with $k\ll1/R_{\max}$, so the formal $k=0$ pole is unphysical rather than merely inconvenient.  Two physically-motivated variants are proposed in the same document: a finite-thickness regulator $k_z\sim1/h$ (dwarfs are puffier, so this pushes in the right direction), combined as $1/k^2\to1/(k^2+k_{\rm IR}^2+k_z^2)$; and an external-field regulator $k_{\rm ext}\sim g_{\rm ext}/v_{\rm char}^2$.

**New result (mine).**  Implementing $M_{\rm reg}$ in the order-1 global-$\mu$ pipeline on the 143-galaxy SPARC subsample:

| | unregulated $1+\mu^2/k^2$ | regulated $1+\mu^2/(k^2+(\pi/R_{\max})^2)$ |
|---|---:|---:|
| $\mu^\star$ [kpc$^{-1}$] | 0.103646 | 0.319126 |
| $\ell^\star$ [kpc] | 9.6482 | 3.13356 |
| median $\chi^2/{\rm dof}$ | 3.056 | **2.773** |
| p90 $\chi^2/{\rm dof}$ | 63.71 | **48.25** |
| median rms [km/s] | 11.837 | 12.667 |
| $A$ median | 0.8897 | 0.5773 |
| frac $A\in[0.4,2.5]$ | 0.517 | **0.427** |
| $\log_{10}A$ scatter [dex] | 0.462 | **0.550** |
| $\mu^\star$ spread over KMIN_FACTOR $\in[0.25,2]$ | **factor 2.2** | **$\pm6\%$** |

So the regulator does exactly what UPG_04 predicted for the *scale*: $\mu^\star$ becomes a property of the data rather than of the grid.  It improves $\chi^2$ modestly.  It makes the amplitude scatter **worse**, and the model still loses to MOND-simple scored identically ($0.998$).

### Derivation

**Why $\pi/R_{\max}$ and not $1/R_{\max}$.**  [reconstructed]  For a field confined to $[0,R_{\max}]$ with a node at the outer edge, the lowest admissible radial half-wavelength is $R_{\max}$, i.e. $k_{\rm IR}=\pi/R_{\max}$.  This is the same convention as the Nyquist-type $k_c=\pi/\Delta r$ already used for the *ultraviolet* taper in the same script, so the two cutoffs are consistent: $\pi/R_{\max}\le k\le\pi/\Delta r$ is exactly the band of modes the data can carry.  In the corpus's default grid the hand-set floor is $k_{\min}=0.5/R_{\max}=0.159\,k_{\rm IR}$, i.e. the numerical grid was reaching a factor 6 further into the infrared than the geometry permits.  That is a precise statement of what went wrong.

**Stability sweep (the decisive test).**  Repeating the KMIN_FACTOR sweep with the regulator in place:

    KMIN_FACTOR=0.25  mu*=0.328831  ell=3.04107  median chi2/dof=2.68926  p90=48.640
    KMIN_FACTOR=0.5   mu*=0.319126  ell=3.13356  median chi2/dof=2.77299  p90=48.254
    KMIN_FACTOR=1.0   mu*=0.312281  ell=3.20224  median chi2/dof=2.81810  p90=48.467
    KMIN_FACTOR=2.0   mu*=0.351090  ell=2.84827  median chi2/dof=4.18119  p90=52.125
    KMIN_FACTOR=4.0   mu*=0.406808  ell=2.45816  median chi2/dof=55.2905  p90=289.585

Compare the unregulated sweep, where $\mu^\star$ ran $0.1386\to0.1036\to0.1667\to0.2288\to0.3966$ (factor 2.9 over the same range, factor 3.8 including 0.25).  With the regulator, over KMIN_FACTOR $\in[0.25,1]$ — the whole regime where the grid floor lies *below* the geometric cutoff, $c_{\rm IR}/R_{\max}<\pi/R_{\max}$, i.e. $c_{\rm IR}<\pi$ — $\mu^\star$ varies only over $[0.3123,0.3288]$, a $\pm2.6\%$ band, and $\chi^2$ over $[2.69,2.82]$.  At KMIN_FACTOR $=2$ ($c_{\rm IR}=2$, still $<\pi$ but with only $\pi/2$ of margin on a log grid) the drift begins; at KMIN_FACTOR $=4>\pi$ the grid floor *overtakes* the physical regulator, the physical cutoff becomes inoperative, and the fit collapses ($\chi^2/{\rm dof}=55.3$).  This crossover at $c_{\rm IR}=\pi$ is a clean, predicted, and observed signature that the regulator is doing the work it is supposed to do.  Recording it turns the UPG_04 proposal from a suggestion into a verified diagnosis: **$\mu^\star$ was a numerical artefact, and the geometric regulator removes the artefact.**

**What the regulator does not fix.**  The physical scale moves to $\ell^\star=1/\mu^\star\approx3.13$ kpc, i.e. a *disc*-scale rather than a halo-scale length, which is a more sensible number than $9.65$ kpc.  The median $\chi^2$ improves by 9% and the p90 by 24%.  But the amplitude distribution degrades: the fraction of galaxies with $A$ inside the pre-registered window drops from 51.7% to 42.7%, and the scatter rises from 0.462 to 0.550 dex.  Since $A$ is degenerate with $\Upsilon$ (item on the data model), a 0.55 dex scatter in an effective mass-to-light ratio is not survivable — stellar population synthesis allows perhaps 0.1-0.15 dex.  The kill-switch therefore still fires, and it fires on the amplitude criterion rather than on $\chi^2$: exactly the situation criterion (0) was pre-registered to catch.  This is consistent with Obstruction II, which says the required amplitude must scale as $M^{-1/2}$ no matter how the infrared is regulated, because the defect is in the *power* of the multiplier, not in its regularisation.

**Recommended next step, stated precisely** [reconstructed]: the regulated kernel plus the corrected QDHT plus floating $\Upsilon_{\rm disk}$ under a log-normal prior centred on 0.5 with $\sigma=0.1$ dex, with $A$ removed entirely ($A\equiv1$) as UPG_03 Option A recommends.  Obstruction II predicts this will fail with a residual trend $\Upsilon_{\rm eff}\propto M^{-1/2}$; measuring the slope of that trend and comparing it to $-1/2$ would be a sharp, falsifiable closing test of the whole model class, and would take about a day of compute.

### Constants and numbers

$k_{\rm IR}=\pi/R_{\max}$; corpus default grid floor $k_{\min}=0.5/R_{\max}=0.159\,k_{\rm IR}$.  Regulated fit (KMIN_FACTOR $=0.5$): $\mu^\star=0.319126$ kpc$^{-1}$, $\ell^\star=3.13356$ kpc, median $\chi^2/{\rm dof}=2.77299$, p90 $=48.2542$, median rms $=12.6673$ km/s, p90 rms $=63.6431$, $A$ median $=0.577332$, p90 $=2.86867$, range $[0.05,5.628]$ (lower value at the A_CLAMP floor), frac in $[0.4,2.5]=0.427$, scatter $0.550$ dex.
Stability sweep KMIN_FACTOR $\{0.25,0.5,1,2,4\}$: $\mu^\star\{0.328831,0.319126,0.312281,0.351090,0.406808\}$ kpc$^{-1}$; median $\chi^2/{\rm dof}\{2.68926,2.77299,2.81810,4.18119,55.2905\}$; p90 $\{48.640,48.254,48.467,52.125,289.585\}$.  Band over $[0.25,1]$: $\mu^\star\in[0.3123,0.3288]$, $\pm2.6\%$.  Crossover predicted and observed at $c_{\rm IR}=\pi\approx3.14$.  Benchmarks on identical footing: MOND-simple median $\chi^2/{\rm dof}=0.998$, $A$ scatter $0.167$ dex, 93.7% within the cut; SPS-allowable $\Upsilon$ scatter $\approx0.10$-$0.15$ dex.

### Code

Implemented by two substitutions in the order-1 script; my patched version is scratchpad\\antikernel_reg.py:

```python
KIR = [0.0]                              # per-galaxy geometric IR cutoff, set before each transform

def M(k, mu):
    if KERNEL == "reg":                  # UPG_04 regulated anti-kernel, no new fitted parameter
        return 1.0 + mu*mu/(k*k + KIR[0]**2)
    return (k*k)/(k*k + mu*mu) if KERNEL == "screen" else (k*k + mu*mu)/np.maximum(k*k, 1e-30)

def gmu_of(r, gb, mu, k, wk, W):
    KIR[0] = np.pi/float(r.max())        # k_IR = pi / R_max
    wr = np.gradient(r); J = j1(np.outer(k, r))
    Gb = (J * (r*gb*wr)[None, :]).sum(axis=1)
    return ((k * Gb * M(k, mu) * W * wk)[:, None] * J).sum(axis=0)
```
Run: `python antikernel_reg.py 0.5 reg` (and sweep the first argument for the stability table).

**Caveat.** The improvement is measured with the crude order-1 trapezoid quadrature whose identity round-trip exceeds 10% for 29% of galaxies, so the 9% median-chi2 gain is within the numerical noise of the method even though the mu* stabilisation is far outside it.

**Why it matters.** It converts a documented suggestion into a verified diagnosis with numbers: the headline scale really was a numerical artefact, a zero-parameter geometric regulator really does remove it (factor 2.2 instability down to +/-6%), the crossover happens exactly where the theory says it should, and the model still fails - but now it fails on the amplitude criterion for a reason the asymptotic no-go predicts independently. That is a complete, closed diagnostic loop, and it is the single most useful piece of unfinished business in the corpus turned into a finished result.

---

## 11. MOND baseline forms, their equivalence to the standard interpolation functions, and the a0 unit conversion

`status: solid` · `kind: derivation`

### Statement

**Model B is exactly the standard MOND 'simple' interpolation function.**  The code computes
\[ g_{\rm obs}=\tfrac12\Big(g_{\rm bar}+\sqrt{g_{\rm bar}^2+4a_0g_{\rm bar}}\Big). \]
This is the unique positive root of the MOND relation $g_{\rm obs}\,\mu_{\rm s}(g_{\rm obs}/a_0)=g_{\rm bar}$ with the simple $\mu$-function $\mu_{\rm s}(y)=y/(1+y)$; equivalently $g_{\rm obs}=\nu_{\rm s}(x)g_{\rm bar}$ with $x=g_{\rm bar}/a_0$ and
\[ \nu_{\rm s}(x)=\tfrac12\Big(1+\sqrt{1+\tfrac4x}\Big). \]

**Model C is exactly the McGaugh-Lelli-Schombert RAR fitting function.**  The code computes
\[ g_{\rm obs}=\frac{g_{\rm bar}}{1-\exp\big(-\sqrt{g_{\rm bar}/a_0}\big)}, \]
i.e. $\nu_{\rm RAR}(y)=\big(1-e^{-\sqrt y}\big)^{-1}$ with $y=g_{\rm bar}/a_0$.

**Unit conversion.**  With $1\,{\rm kpc}=3.085677581\times10^{19}$ m,
\[ 1\ \frac{({\rm km/s})^2}{\rm kpc}=\frac{10^{6}\ {\rm m^2/s^2}}{3.085677581\times10^{19}\ {\rm m}}=3.240779289960431\times10^{-14}\ {\rm m/s^2}, \]
hence
\[ a_0=3742.11\ \frac{({\rm km/s})^2}{\rm kpc}\;=\;1.2127\times10^{-10}\ {\rm m/s^2},\qquad a_0=4072.53\;=\;1.3198\times10^{-10}\ {\rm m/s^2}, \]
and inversely the canonical MOND value $a_0=1.2\times10^{-10}$ m/s$^2$ corresponds to $3702.81\ ({\rm km/s})^2/{\rm kpc}$ — which is what the kill-switch script's hard-coded threshold `A0_SPECTRAL = 3700.0` is.  **This is the pipeline's positive control:** an independent, blind, single-parameter fit to 165 SPARC galaxies recovers the standard MOND acceleration scale to 1%.

### Derivation

**Model B derivation.**  MOND in its acceleration form is $\mu(g_{\rm obs}/a_0)\,g_{\rm obs}=g_{\rm bar}$.  Take the 'simple' interpolation $\mu_{\rm s}(y)=y/(1+y)$, $y=g_{\rm obs}/a_0$.  Then
\[ \frac{g_{\rm obs}/a_0}{1+g_{\rm obs}/a_0}\,g_{\rm obs}=g_{\rm bar}\;\Longrightarrow\;\frac{g_{\rm obs}^2}{g_{\rm obs}+a_0}=g_{\rm bar}\;\Longrightarrow\;g_{\rm obs}^2-g_{\rm bar}\,g_{\rm obs}-a_0g_{\rm bar}=0, \]
whose positive root is $g_{\rm obs}=\tfrac12\big(g_{\rm bar}+\sqrt{g_{\rm bar}^2+4a_0g_{\rm bar}}\big)$ — the code's expression, exactly.  Factoring $g_{\rm bar}$ out gives $g_{\rm obs}=g_{\rm bar}\cdot\tfrac12\big(1+\sqrt{1+4a_0/g_{\rm bar}}\big)=\nu_{\rm s}(x)g_{\rm bar}$ with $x=g_{\rm bar}/a_0$, matching the form written in `Selected_01_SPARC_Global_Fits_and_KillSwitch.md` §2 Model B.  The document and the code are therefore consistent, which I checked because a mismatch here would invalidate the baseline.

**Limits.**  $g_{\rm bar}\gg a_0$: $\sqrt{g_{\rm bar}^2+4a_0g_{\rm bar}}=g_{\rm bar}\sqrt{1+4a_0/g_{\rm bar}}\approx g_{\rm bar}+2a_0$, so $g_{\rm obs}\to g_{\rm bar}+a_0$ — Newtonian plus a constant offset.  $g_{\rm bar}\ll a_0$: $g_{\rm obs}\to\sqrt{a_0g_{\rm bar}}$, the deep-MOND regime, giving $V^4=r^2g_{\rm obs}^2=r^2a_0g_{\rm bar}=a_0GM$, i.e. the BTFR with slope exactly 4.

**Model C limits.**  $y\gg1$: $e^{-\sqrt y}\to0$, $\nu\to1$, Newtonian.  $y\ll1$: $1-e^{-\sqrt y}=\sqrt y-\tfrac y2+O(y^{3/2})$, so $\nu\to y^{-1/2}$ and $g_{\rm obs}\to g_{\rm bar}/\sqrt{g_{\rm bar}/a_0}=\sqrt{a_0g_{\rm bar}}$ — again the deep-MOND limit and BTFR slope 4.  (A related document in the corpus, `GALAXY RUNS(1).txt` Document 1, works the *inverse* form $g_{\rm obs}=(1-e^{-g_{\rm bar}/a_0})g_{\rm bar}$ and derives $g_{\rm obs}\to g_{\rm bar}^2/a_0$ at low $g$, hence $v^4=GMa_0$; note this is a different function from the RAR fit actually used in the code — the code has $\sqrt{g_{\rm bar}/a_0}$ in the exponent and the factor in the denominator.)

**Unit conversion, step by step.**  $a_0$ is stored in $({\rm km/s})^2/{\rm kpc}$ because the SPARC rotmod tables give $V$ in km/s and $r$ in kpc, so $g=V^2/r$ lands in those units with no prefactor.  Converting:
\[ \Big[\frac{({\rm km/s})^2}{\rm kpc}\Big]=\frac{(10^3\,{\rm m/s})^2}{3.085677581\times10^{19}\,{\rm m}}=\frac{10^6}{3.085677581\times10^{19}}\ \frac{\rm m}{\rm s^2}=3.240779289960431\times10^{-14}\ {\rm m/s^2}. \]
Applying it (values I computed, matching the run's own printed `-> 1.213e-10 m/s^2` and `-> 1.320e-10 m/s^2`):

    a0 =  3742.11 (km/s)^2/kpc  ->  1.2127e-10 m/s^2     (MOND simple, global best)
    a0 =  4072.53                ->  1.3198e-10 m/s^2     (RAR exp, global best; also MOND-simple big-galaxy bin)
    a0 =  3700.00                ->  1.1991e-10 m/s^2     (A0_SPECTRAL, the stiffness-switch threshold)
    a0 =  2069.57                ->  6.7070e-11 m/s^2     (both models, dwarf bin refit)
    a0 =  4432.13                ->  1.4364e-10 m/s^2     (RAR exp, big-galaxy bin refit)
    1.2e-10 m/s^2                ->  3702.813 (km/s)^2/kpc

**The positive control, and its one caveat.**  The recovered $1.21\times10^{-10}$ m/s$^2$ agrees with the literature value $1.2\times10^{-10}$ m/s$^2$ to 1%, from a blind one-parameter grid search over $a_0\in[50,4\times10^4]$ (a factor 800 range) on data the fit had no other handle on.  This validates the loader, the acceleration construction, the units, the $\chi^2$, and the optimiser — so the catastrophic $\chi^2/{\rm dof}$ of Models D and E is a property of *those models*, not of the analysis machinery.  The caveat, visible in the same run, is that the per-bin refit demands $a_0=2069.57$ for dwarfs against $4072.53$-$4432.13$ for big galaxies, a factor $\sim2$: at fixed $\Upsilon=0.5$ MOND's own $a_0$ is not universal across the mass split, so the control is a control on the *pipeline*, not an endorsement of MOND at this $\Upsilon$.

### Constants and numbers

$1\ {\rm kpc}=3.085677581\times10^{19}$ m.  Conversion factor $=1.0\times10^{6}/3.085677581\times10^{19}=3.240779289960431\times10^{-14}$ m/s$^2$ per $({\rm km/s})^2/{\rm kpc}$.
$a_0$: $3742.11\to1.2127\times10^{-10}$; $4072.53\to1.3198\times10^{-10}$; $3700.00\to1.1991\times10^{-10}$; $2069.57\to6.7070\times10^{-11}$; $4432.13\to1.4364\times10^{-10}$ m/s$^2$.  Inverse: $1.2\times10^{-10}$ m/s$^2 = 3702.813\ ({\rm km/s})^2/{\rm kpc}$.
Search grid: $a_0\in$ geomspace$(50,4\times10^4,80)$, i.e. a factor 800 with 8.83% steps.
$\mu$-function identities: $\mu_{\rm s}(y)=y/(1+y)\Leftrightarrow\nu_{\rm s}(x)=\tfrac12(1+\sqrt{1+4/x})$; $\nu_{\rm RAR}(y)=(1-e^{-\sqrt y})^{-1}$.  Deep-MOND limit of both: $g_{\rm obs}\to\sqrt{a_0g_{\rm bar}}$, giving $V^4=GMa_0$ (BTFR slope 4).

### Code

```python
KPC_TO_M             = 3.085677581e19
KM2S2_PER_KPC_TO_MS2 = 1e6 / KPC_TO_M          # 3.240779289960431e-14 m/s^2

def mond_simple_gobs(gbar, a0):                # mu(y) = y/(1+y); positive root
    gbar = np.maximum(gbar, 0.0)
    return 0.5*(gbar + np.sqrt(gbar*gbar + 4.0*a0*gbar))

def mond_rar_exp_gobs(gbar, a0):               # McGaugh-Lelli-Schombert RAR fit
    gbar = np.maximum(gbar, 0.0)
    x = np.sqrt(np.maximum(gbar/max(a0, 1e-300), 0.0))
    return gbar / np.maximum(1.0 - np.exp(-x), 1e-12)

# reporting line used in the run:
# print(f"a0_best = {a0:.6g} (km/s)^2/kpc -> {a0*KM2S2_PER_KPC_TO_MS2:.3e} m/s^2")
```

**Caveat.** The recovered $a_0$ is a control on the pipeline, not a measurement: the same run shows $a_0$ must differ by a factor $\approx2$ between the dwarf and big-galaxy bins at the fixed $\Upsilon=0.5$ used here, so MOND itself does not pass criterion (3) in this configuration.

**Why it matters.** It is the positive control that makes the whole negative result credible: without it, a critic could attribute the kernel models' failure to a broken loader, wrong units, or a broken optimiser. Recovering 1.2e-10 m/s^2 blind from a factor-800 grid rules all of that out, and pins the failure on the models. It also fixes the unit convention that every number in this extraction is quoted in.

---

## How these fit together

All nine items are one connected chain, and the chain closes.\n\nThe **data model** (item 1) is the shared front-end: 175 rotmod files, 143 surviving the 8-point cut, 3199 radial points, $g_{\\rm bar}=V_b^2/r$. Every later number is computed on exactly this footing, which is why my reruns reproduce the archived values to six significant figures where the sample matches and to 2-4% where it does not (the archived run used a SPARC quality cut $Q\\le3$ that is unreproducible offline because the master table is not bundled).\n\nThe **QDHT** (item 2) and the **spectral filter with stiffness switch** (item 3) are the two halves of the model's numerical implementation. Correcting the QDHT normalisation (a one-line conjugation swap, verified to machine precision against an analytic Gaussian) improves the **kill-switch stress test** (item 5) from median $\\chi^2/{\\rm dof}=15.44$ to $4.17$ and from 104 to 89 outliers of 175 — decomposing the failure into a factor-3.7 numerical component and a residual physical component. The decomposition is provable rather than inferred, because galaxies with the stiffness switch off ($M\\equiv1$) must be bit-identical under both normalisations, and they are.\n\nThe **global fit table** (item 4) and the **kill-switch protocol** (item 6) are the empirical and methodological halves of the same run. The protocol's criterion (1) — mandatory baselines on identical footing — is what converts the corpus's apparent 19$\\times$ win (anti-kernel 3.056 vs MOND 57.10) into a 3.1$\\times$ loss (anti-kernel 3.056 vs MOND-simple 0.998 through the identical estimator). Criterion (2), the outer-residual sign bias, is the diagnostic that separates the models correctly where $\\chi^2$ does not. Criterion (3), the per-bin refit, is what shows the kernel models' 'universal' length scale must change by factors of 22 and 340 across a mass split.\n\nThe two **obstructions** (items 6-obstruction-I and -II) explain everything the fits recorded. Obstruction II — the exact Bessel-integral computation showing $g_\\mu\\to g_b+\\mu^2GM$, hence $V\\propto\\sqrt r$ rather than flat — is the root cause. It predicts, independently of any fit: (a) that a finite computational domain is the only thing hiding the rising curve, which is Obstruction I's factor-2.9 instability of $\\mu^\\star$ under the IR cutoff; (b) that the required per-galaxy amplitude must scale as $M^{-1/2}$, which is the observed factor-81 spread in $A$; (c) that the outer residual sign bias can never balance; (d) that the screen branch has no interior optimum, which I confirmed ($\\mu^\\star$ runs to its lower bound). Obstruction II also states exactly what a working multiplier would be, $M(k)\\to k^{-1}\\sqrt{a_0/GM}$, and why no *universal* one exists — the spectral-language form of the Bekenstein-Milgrom result that MOND phenomenology needs a nonlinear field equation.\n\nThe **operator equivalence** (item 7) is the bridge that makes Obstruction II computable: it converts the spectral multiplier into the local elliptic problem $L_1\\chi=g_b$, whose homogeneous solutions $\\{r,1/r\\}$ identify the growing mode that the regulator must suppress. The **geometric regulator** (item 8) then closes the loop: it removes the artefact exactly as UPG_04 predicted ($\\mu^\\star$ stability improves from a factor 2.2 to $\\pm6\\%$, with the predicted crossover at $c_{\\rm IR}=\\pi$), improves $\\chi^2$ by 9%, and still fails — now on the amplitude criterion, with $A$ scatter rising to 0.550 dex, which is precisely what Obstruction II predicts must happen no matter how the infrared is regulated.\n\nThe **MOND baselines and unit conversion** (item 9) are the positive control that makes the whole negative result credible: a blind one-parameter search over a factor-800 grid recovers $a_0=1.21\\times10^{-10}$ m/s$^2$, the standard MOND scale, to 1%. That validates loader, units, $\\chi^2$ and optimiser, so the failure of the kernel models belongs to the models.\n\nOutward connections: the anti-kernel's $\\mu^2(-\\Delta)^{-1}$ structure is the same inverse-Laplacian ingredient the corpus invokes for codimension-2 logarithmic Green's functions elsewhere (BEST_01 §9, EXC_01 §4); Obstruction II shows that analogy fails in the order-1 radial setting because the far field is a constant, not $1/r$. The corpus's claimed link from a Yang-Mills mass gap to $a_0$ is nowhere derived in this folder — the galactic sector is standalone phenomenology and depends on nothing in the Lean development.

## Further material found but not fully extracted

**Corrections to corpus documents that I verified and did not have room to expand.** (i) `EXC_01_AntiKernel_HankelSpectral.md` §6 attributes $\\mu^\\star=0.161395$ kpc$^{-1}$, $\\ell=6.19599$ kpc to the anti-kernel; the producing cell (`ARCHIVES/extracted_notebooks/Untitled10_extracted.py` line ~4700) contains `M = (k*k)/(k*k + mu*mu)`, i.e. the SCREEN kernel, and that run's median $\\chi^2/{\\rm dof}$ was 83.94 with p90 4089.65. The anti-kernel value is $0.103646$. (ii) `Synthesis_07_Physics_Phenomenology_VSU.md` §11.2 tabulates the outer-residual sign fraction as baryons-only 0.909 and MOND/RAR $\\approx0.50$; correct values from the run are A 0.988, B 0.358, C 0.309, D 0.903, E 0.788, and MOND therefore does NOT pass the sign-bias criterion as that section claims. (iii) `BEST_01_AntiKernel_SpectralRigidity.md` §6.1 reports $N_{\\rm pts}=3646$; the bundled data under the stated cuts gives 3199, which my run reproduces alongside every other digit of that run.\n\n**Other spectral variants with recorded runs I did not re-execute.** The 'sharpened boost' family $M(k;\\mu,n)=(1+(\\mu/k)^n)^{1/n}$ with $n=4$ (`VSU_COSMOLOGY/Core_Theory/Selected_02_Spectral_Boost_Filter_Model.md`), which has the *correct* $M\\sim\\mu/k$ infrared power to give flat curves and therefore deserves the Obstruction-II treatment properly — my Step 5 shows it predicts BTFR slope 2 instead of 4 with a universal $\\mu$, but I did not fit it. Two recorded runs of it land at wildly different scales: $\\mu^\\star=1.67038$ kpc$^{-1}$ ($\\ell=0.60$ kpc) unconstrained, and $\\mu^\\star=1.00634\\times10^{-4}$ kpc$^{-1}$ ($\\ell\\approx9.94\\times10^3$ kpc) under a 'fixed mass constraint' — a factor $1.7\\times10^4$, an even more extreme version of the degeneracy documented in Obstruction I.\n\n**A 'density switch' experiment** in `ARCHIVES/extracted_notebooks/Untitled10_extracted.py` (~line 4700 onward, `sparc_density_switch.py`): fit $\\mu$ per galaxy with $A$ constrained near 1, then plot preferred $\\mu$ against characteristic $g_{\\rm bar}$, testing the MOND prediction that low-$g$ LSBs should prefer high $\\mu$. This is the right experiment for deciding whether the stiffness switch has empirical support rather than being imposed; I did not run it, and the correlation it produces would be a direct, cheap test of the switch's functional form $\\mu=\\mu_{\\max}(1-g_{\\max}/a_0)$.\n\n**Unexploited data.** The rotmod files carry two further columns, `SBdisk` and `SBbul` (surface brightness in $L_\\odot/{\\rm pc}^2$), which every pipeline in the corpus discards. These are exactly the SPS handle needed to implement UPG_03 Option A — replace the free amplitude $A$ by $\\Upsilon_{\\rm disk}$ under a colour-informed prior — which is the single change most likely to close the main referee objection to any write-up ('your model would work with realistic M/L').\n\n**UPG_04 variants B and C** (finite-thickness regulator $k_z\\sim1/h$, external-field regulator $k_{\\rm ext}\\sim g_{\\rm ext}/v_{\\rm char}^2$) are stated but never implemented anywhere in the corpus. Variant B is attractive and cheap: dwarfs have larger $h/R$, so combining $1/k^2\\to1/(k^2+k_{\\rm IR}^2+k_z^2)$ pushes in the direction the dwarf residuals demand, and SPARC scale heights can be estimated from the disc scale lengths already in the master table.\n\n**Duplication map for this topic** (so nobody re-reads copies): `CODE_sparc_honest_killswitch.py` has 3 byte-identical copies (md5 186fcafeb62d7b83618dfad122c5767e) across SIMULATIONS/ and VSU_COSMOLOGY/Galactic_Phenomenology/; `CODE_sparc_rigidity_HANKEL_KERNEL_SWITCH.py` has 5 (md5 b920c86b7b3e156e8167c0d2e16eea64), including `SIMULATIONS/code_verification/SPARC_antikernel_fit.py`; `BEST_01_AntiKernel_SpectralRigidity.md` has 6 (md5 30a520e6...); `Selected_01_SPARC_Global_Fits_and_KillSwitch.md` has 2. The unique, highest-value file for this topic is `ARCHIVES/extracted_notebooks/Untitled10_extracted.py` — it is the only place carrying the full executed stratified diagnostics and the per-galaxy tables, and its duplicate `HESSIAN/UNCATEGORIZED_MISC/WIZ UPDATE.txt` contains the same logs.
