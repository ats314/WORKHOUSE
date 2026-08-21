# Exponential Decay of the Massive Maxwell Green Kernel
## Combes–Thomas vs Davies Rates (and what the simulations say)

This note collects the “finite-range inverse decay” results used to turn the Helffer–Sjöstrand covariance formula into exponential clustering.

The operator is the **massive Maxwell operator** on $1$-cochains:

\[
M \;=\; m^2 I + \alpha\,\Delta_1,
\qquad
\Delta_1 := d_1^\*d_1,
\qquad
m^2>0,\ \alpha>0.
\]

It acts on
\[
\mathcal C^1(\Lambda;\mathfrak g)\cong \ell^2(E(\Lambda);\mathfrak g),
\]
and we measure distance in the **link adjacency graph**: $b\sim b'$ if $b,b'$ co-bound a plaquette, with graph distance $\mathrm{dist}_E$.

---

## 1. Constants: row-sum controls

Let $A$ be a block matrix indexed by links $b,b'$ with blocks in $\mathrm{End}(\mathfrak g)$.
The key purely local constant is the **off-diagonal row-sum**:

\[
C_0(A) \;:=\; \sup_{b}\ \sum_{b'\neq b}\ \|A_{b,b'}\|_{\mathrm{op}}.
\]

Two refinements used in the repo:

- $C_\partial(\Delta_1)$: a boundary-sensitive row-sum restricting to neighbors that increase the distance level by $\pm1$,
- $C_{\mathrm{part}}(\Delta_1)$: row-sum restricted to block-crossing edges when one partitions the lattice.

These matter because Davies-type bounds are sensitive to which terms survive in the conjugated commutator.

---

## 2. The robust route: Combes–Thomas for finite-range positive operators

**Template.**  
Let $A$ be self-adjoint on $\ell^2(V;\mathsf H_0)$ with:

1. $A\succeq a_0 I$ (uniform positivity gap),
2. finite range $R$ in a graph distance $\mathrm{dist}$,
3. off-diagonal row-sum bound $B:=\sup_x\sum_{y\neq x}\|A_{xy}\|_{\mathrm{op}}$.

Then the inverse kernel decays exponentially:

\[
\|(A^{-1})_{xy}\|_{\mathrm{op}}
\;\le\;
\frac{2}{a_0}\,e^{-\eta\,\mathrm{dist}(x,y)},
\qquad
\eta=\frac{1}{R}\log\!\Bigl(1+\frac{a_0}{2B}\Bigr).
\]

**Specialization to $M$.**  
For the massive Maxwell operator:

- $a_0=m^2$,
- $R=1$ in $\mathrm{dist}_E$,
- $B\le \alpha\,C_0(\Delta_1)$ (or the cruder $\alpha D_E$ via bounded link degree).

Thus one gets a universal Combes–Thomas exponent

\[
\eta_{\mathrm{CT}}
\;=\;
\log\!\Bigl(1+\frac{m^2}{2\alpha C_0(\Delta_1)}\Bigr)
\quad
\text{(or with $C_0$ replaced by a crude degree bound).}
\]

**Scaling note.**  
For small $m$, $\eta_{\mathrm{CT}}\sim m^2$.

That is **safe** but not tight.

---

## 3. The sharper route: Davies method for the massive Maxwell inverse

The project also records a Davies-type bound specialized to $M$.
The resulting admissible exponent is

\[
\eta_{\mathrm{DG}}
\;=\;
\operatorname{arcosh}\!\Bigl(1+\frac{m^2}{2\alpha\,C_0(\Delta_1)}\Bigr)
\;=\;
2\,\operatorname{arsinh}\!\Bigl(\frac{m}{2\sqrt{\alpha\,C_0(\Delta_1)}}\Bigr).
\]

**Scaling note.**  
For small $m$, $\eta_{\mathrm{DG}}\sim m$.

That is a big qualitative improvement: the bound now has the “right” small-mass scaling.

**Boundary refinement.**  
Replacing $C_0(\Delta_1)$ by $C_\partial(\Delta_1)$ (or by $C_{\mathrm{part}}$ in a block setting) increases $\eta_{\mathrm{DG}}$ without changing the argument, because the conjugated commutator only sees terms that jump distance levels.

---

## 4. Simulation evidence: the bound holds but is not tight

The simulation logs include a “coherence sweep” comparing:

- the *provable* exponents $\eta_{\mathrm{CT}}$ and $\eta_{\mathrm{DG}}$ computed from a measured $C_0$,
- the *observed* decay slope of the Green kernel along an axis (low-$k$ / large-$r$ behavior),
  which tracks approximately $\sqrt{m^2}$.

Representative output (from the project logs) shows, for example:

- for $m^2=0.1$, an observed/expected slope $\kappa_{\rm expected}\approx 0.315$,
- while $\eta_{\mathrm{DG}}$ computed from the conservative constant is $\approx 0.034$,
  and $\eta_{\mathrm{CT}}$ is even smaller.

Interpretation: the Combes–Thomas and Davies methods are doing what they promise (uniformity and robustness),
but they intentionally throw away Fourier/symbol information, so they are **not** close to sharp.

This is actually good news for the proof pipeline: **a conservative exponent is enough** to get exponential clustering at fixed cutoff,
and the observed decay being much faster suggests large slack for future quantitative sharpening.

---

## 5. What would make this “new theory” rather than “good estimates”?

A physics-forward view is that $M$ is the **linear-response operator of the Gibbs state**.
The reason it appears in the HS identity is not accidental; it is a manifestation of:

- **stochastic quantization** (Parisi–Wu): the Euclidean measure is an invariant distribution of a heat flow,
- **Witten deformation**: the generator on forms is a Hessian-shifted Laplacian,
- **geometric mass**: compact group curvature contributes a uniform positive floor.

From that view, off-diagonal decay of $M^{-1}$ is the lattice analog of “massive propagator decay,”
and the Davies improvement is a way of capturing the *correct small-mass scaling* without Fourier analysis.

---

## Appendix: minimal code skeleton (FFT scalar case)

The repo also contains FFT-based code to compute an exact scalar massive Green function on $L^4$ and fit a decay slope.
The $1$-form Maxwell case is more elaborate (gauge/horizontal sectors), but the same structure applies.

```python
import numpy as np
from numpy.fft import fftn, ifftn

def scalar_green(L, m2):
    k = [np.fft.fftfreq(L) * 2*np.pi for _ in range(4)]
    K0, K1, K2, K3 = np.meshgrid(*k, indexing='ij')
    p2 = 4*(np.sin(K0/2)**2 + np.sin(K1/2)**2 + np.sin(K2/2)**2 + np.sin(K3/2)**2)
    D_hat = 1.0/(p2 + m2)
    G = ifftn(D_hat).real
    return G / G[(0,0,0,0)]

def fit_eta_axis(G):
    L = G.shape[0]
    r = np.arange(L//2)
    g = np.abs(G[r,0,0,0])
    sl = slice(2, 6)                # avoid r=0 and strong lattice artifacts
    coeffs = np.polyfit(r[sl], np.log(g[sl]), 1)
    return -coeffs[0]
```

---

## Cross references

- Abstract Combes–Thomas lemma: Part 9.1.
- Davies refinement and $C_0,C_\partial$ constants: Part 9.X and corollaries.
- Covariance-to-kernel mechanism: HS section in Part 6 and “good set” localization in Part 8–10.
- Simulation tables: `MAXWELL SIMS.txt` and the run PDFs.
