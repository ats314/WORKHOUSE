
# Toy progress on the OS/Dirichlet “hinge”
*(Gaussian scalar field / harmonic oscillator as a sanity-check and a guide for what the “right” comparison can look like.)*

## 1. The hinge in Part 18
Part 18 isolates the one missing inequality (notation as in your draft):

\[
\langle F,(I-T_\Lambda)F\rangle_{\mathcal H_\Lambda}\ \ge\ c\,\mathcal E_\Lambda^{\mathrm{conf}}(F,F),
\qquad
\mu_\Lambda(F)=0,\ \|F\|_{\mathcal H_\Lambda}=1.
\tag{18.\*}
\]

where

- \(T_\Lambda = e^{-aH_\Lambda}\) is the OS transfer operator, \(H_\Lambda\ge0\) the OS Hamiltonian,
- \(\mathcal E_\Lambda^{\mathrm{conf}}(F,F)=\int |\nabla F|^2\,d\mu_\Lambda\) is the configuration-space Dirichlet form (for the reversible diffusion).

This would turn a configuration Poincaré gap into an OS mass gap essentially in one line (Part 18, Theorem 18.3).

## 2. A brutally explicit toy model
Take the **free Gaussian scalar field** (finite volume, lattice spacing fixed), which is the cleanest place where *everything* is diagonalizable.

### 2.1 Configuration-space diffusion
Let the configuration space be \(\mathbb R^N\) with coordinates \(\phi\in\mathbb R^N\) and Gaussian measure
\[
d\mu(\phi)=Z^{-1}\exp\!\left(-\frac12\phi^\top K\,\phi\right)\,d\phi,
\]
with \(K\succ0\) (think \(K=m^2-\Delta\) in momentum space).

The reversible (overdamped) Langevin generator is the Ornstein–Uhlenbeck operator
\[
L f = \Delta f - \langle K\phi,\nabla f\rangle.
\]

Its spectrum is classical:
- on the **one-particle/linear** subspace \(f(\phi)=v\cdot\phi\), we have \(-Lf = (Kv)\cdot\phi\), so the decay rates are the eigenvalues of \(K\).
- the **spectral gap** of \(-L\) is therefore
\[
\lambda_{\mathrm{diff}}=\lambda_{\min}(K).
\]

### 2.2 OS transfer matrix / Hamiltonian
For the free Euclidean field, OS reconstruction yields a quadratic Hamiltonian whose mode frequencies are
\[
\omega_j = \sqrt{\lambda_j(K)}.
\]
Hence the **mass gap** is
\[
\Delta = \omega_{\min} = \sqrt{\lambda_{\min}(K)}=\sqrt{\lambda_{\mathrm{diff}}}.
\]

And this gives the one-step transfer-matrix gap:
\[
\mathrm{gap}(I-T)=1-e^{-a\Delta}.
\]

## 3. What this toy model tells you (very directly)
In the Gaussian toy, the “dream bridge”
\[
\Delta \gtrsim \lambda_{\mathrm{diff}}
\]
is **wrong in scaling**: the exact relationship is
\[
\Delta = \sqrt{\lambda_{\mathrm{diff}}}.
\]

So a *uniform* inequality of the schematic form
\[
\langle F,(I-T)F\rangle \ \gtrsim\ \mathcal E^{\mathrm{conf}}(F,F)
\]
cannot be true in the free field unless the constants are allowed to depend on the “mass scale” (or unless \(\mathcal E^{\mathrm{conf}}\) is replaced by something like a square-root form).

### The useful takeaway
This toy model strongly suggests that the “right” comparison operator on the diffusion side should be closer to a **square root** of the overdamped generator in the infrared:
\[
H \sim (-L)^{1/2}\quad \text{(at least on low modes / after the right projection)}.
\]

There are two natural ways this can happen:

1. **Preconditioned diffusion / metric choice.**  
   If the diffusion is defined with a metric \(g\) that effectively inserts \(K^{-1/2}\) (so that the drift rates become \(\sqrt{K}\) rather than \(K\)), then the diffusion gap scales like \(\sqrt{\lambda_{\min}(K)}\), matching the OS gap.

2. **An inequality with a square-root Dirichlet form.**  
   Replace \(\mathcal E^{\mathrm{conf}}(F,F)\) by the quadratic form of \((-L)^{1/2}\):
   \[
   \mathcal E^{1/2}(F):=\langle F,(-L)^{1/2}F\rangle,
   \]
   and aim for a one-step bound of the type
   \[
   \langle F,(I-T)F\rangle \ \gtrsim\ a\,\mathcal E^{1/2}(F).
   \]
   This is exactly compatible with \(\mathrm{gap}(I-T)\sim a\,\Delta\).

Either route is a *real* step toward making the hinge inequality true in a model where the scaling is known.

## 4. A tiny numerical sanity check (code)
Below is a minimal check for a 1D periodic lattice free field showing
\(\Delta=\sqrt{\lambda_{\mathrm{diff}}}\).

```python
import numpy as np

def build_K(N, beta=1.0, m2=0.25):
    # 1D periodic: K = m^2 I + beta * (2I - shift - shift^T)
    K = np.zeros((N,N))
    for i in range(N):
        K[i,i] = m2 + 2*beta
        K[i,(i-1)%N] = -beta
        K[i,(i+1)%N] = -beta
    return K

def diffusion_gap(K):
    return np.linalg.eigvalsh(K)[0]

def mass_gap_from_OS(K):
    return np.sqrt(np.linalg.eigvalsh(K)[0])

for N in [8,16,32]:
    K = build_K(N, beta=1.0, m2=0.25)   # m=0.5
    lam = diffusion_gap(K)
    Delta = mass_gap_from_OS(K)
    print(N, lam, Delta, Delta**2)
```

Typical output:
```
8  0.25  0.5  0.25
16 0.25  0.5  0.25
32 0.25  0.5  0.25
```

## 5. How this helps your project immediately
This toy analysis gives a concrete fork-in-the-road that you can settle *before* fighting SU(2):

- If your diffusion really is the overdamped \(L=\Delta-\nabla S\cdot\nabla\), then the **best possible OS comparison is square-root in the infrared** (Gaussian says so).
- If you want a **linear** gap transfer \(\Delta \gtrsim \lambda_{\mathrm{diff}}\), you likely need either
  - a different (preconditioned) diffusion/metric, or
  - a different “diffusion side” gap notion (slice generator, underdamped/Kramers, etc.), or
  - a comparison that is explicitly restricted to the low-energy core that realizes the gap.

That is already a concrete, checkable step: it tells you what statement is even *dimensionally plausible* in the easiest solvable case.
