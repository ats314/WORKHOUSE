# Vacuum connectivity as a percolation transition in 4D massive Gaussian fields

## Goal

This note extracts a GPU-based, finite-size scaling scan of the **excursion set** $\{x:\phi(x)>h\}$ for a 4D massive Gaussian field, producing an estimate of a critical threshold $h_c$ (and a fitted exponent $\nu$) for when a “giant” connected component appears.

This is a clean bridge between:
- lattice free-field theory (Gaussian measures),
- excursion-set topology / percolation,
- and “vacuum connectivity” as an order parameter.

---

## Model and construction

### Field definition
Generate a real scalar field $\phi$ on a periodic 4D lattice of size $L^4$ with Fourier-space covariance
\[
\mathbb{E}\,|\tilde\phi(p)|^2 \propto \frac{1}{\hat p^2 + m^2},
\qquad
\hat p_\mu = 2\sin\left(\frac{p_\mu}{2}\right).
\]

Implementation sketch:

1. Draw complex Gaussian noise in momentum space.
2. Multiply by $D^{1/2}(p) = (\hat p^2+m^2)^{-1/2}$.
3. Inverse FFT to real space.
4. Standardize to mean $0$ and variance $1$.

### Excursion set and connectivity criterion
For a threshold $h$, define the binary field
\[
\chi_h(x) = \mathbf{1}\{\phi(x)>h\}.
\]
Label connected components (nearest-neighbor connectivity in 4D).

Define a percolation-like “vacuum connected” event as:
\[
\text{largest cluster size} \;>\; f\,L^4,
\]
with $f=0.2$ used in the run (a “giant component” criterion).

---

## Simulation protocol

- Mass: $m^2=0.1$ in the reported scan.
- Lattice sizes: $L\in\{96,128,160,192\}$.
- Threshold scan: around $h\in[0.69,0.73]$ with fine spacing.
- Monte Carlo samples per $(L,h)$: 15.
- Hardware: GPU (CuPy).

---

## Reported results (finite-size scaling fit)

The simulation log reports a finite-size scaling estimate:

\[
\boxed{\nu \approx 0.7109,\qquad h_c \approx 0.728.}
\]

A coarse “headline” statement also appears in the log as a connectivity onset near $h\sim 0.71$ (consistent with being near the transition for finite $L$).

These numbers should be treated as *first-pass estimates* (sample size is modest; the “giant component >20%” proxy is not the only possible percolation definition).

---

## Why this has “new theory” potential

1. **Excursion-set percolation in correlated fields** is well-studied mathematically, but the exact location of $h_c(m^2)$ and scaling behavior for lattice free fields in 4D is an interesting object.
2. The “vacuum connectivity” language suggests a **topological order parameter** that can, in principle, be tracked under:
   - changes in $m^2$,
   - changes in lattice action (interacting fields),
   - RG blocking / coarse-graining.

A more ambitious direction is to treat $h$ as a *Morse filtration parameter* and study persistent homology (Betti numbers) rather than only the largest-cluster criterion.

---

## Code (GPU/CuPy skeleton extracted from project)

This is the key loop structure (simplified for readability but faithful in intent):

```python
import cupy as cp
import numpy as np
from scipy import ndimage

def gaussian_field_4d(L, m2=0.1, seed=0):
    rs = np.random.RandomState(seed)
    # complex Gaussian noise in k-space
    noise = rs.normal(size=(L,L,L,L)) + 1j*rs.normal(size=(L,L,L,L))
    noise = cp.asarray(noise)

    # lattice momenta and propagator sqrt
    k = cp.fft.fftfreq(L) * 2.0 * cp.pi
    kx,ky,kz,kt = cp.meshgrid(k,k,k,k, indexing="ij")
    phat2 = (2*cp.sin(kx/2))**2 + (2*cp.sin(ky/2))**2 + (2*cp.sin(kz/2))**2 + (2*cp.sin(kt/2))**2
    Dsqrt = 1.0 / cp.sqrt(phat2 + m2)

    phi_k = noise * Dsqrt
    phi_x = cp.fft.ifftn(phi_k).real

    # normalize
    phi_x = (phi_x - phi_x.mean()) / phi_x.std()
    return phi_x

def percolates(phi_x, h, frac=0.2):
    mask = (phi_x > h).get()  # to CPU for ndimage
    labeled, nlab = ndimage.label(mask)
    if nlab == 0:
        return False
    counts = np.bincount(labeled.ravel())
    largest = counts[1:].max() if counts.size > 1 else 0
    return largest > frac * mask.size

def sweep(L_list=(96,128,160,192), h_vals=np.linspace(0.69, 0.73, 20), samples=15):
    results = {}
    for L in L_list:
        probs = []
        for h in h_vals:
            hits = 0
            for s in range(samples):
                phi = gaussian_field_4d(L, m2=0.1, seed=1000*L + 37*s)
                hits += int(percolates(phi, h, frac=0.2))
            probs.append(hits/samples)
        results[L] = dict(h=h_vals, prob=np.array(probs))
    return results
```

---

## Next steps that would materially improve the science

1. **Replace the 20% giant-component proxy** with a spanning-cluster criterion (wrap-around in periodic directions).
2. Increase samples per $(L,h)$ and repeat the scaling fit with uncertainty quantification.
3. Sweep in $m^2$ to map a phase diagram $h_c(m^2)$.
4. Compute cluster size distributions and critical exponents (if any) beyond $\nu$.
5. Move from percolation to **persistent homology** for richer topological characterization.
