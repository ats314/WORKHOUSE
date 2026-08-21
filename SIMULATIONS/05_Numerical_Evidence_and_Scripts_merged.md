# Numerical evidence and scripts (curated)

This note collects the simulations that are (i) aligned with the project’s analytic bottlenecks,
and (ii) produce **falsification-style** evidence rather than just “pretty plots.”

---

## 1. What counts as a useful numerical result here?

The project’s hard step is a coercivity-on-$K^c$ principle:
rough configurations should not have tiny force unless they are Cartan-aligned.

So the numerics should do one of:

- find a **counterexample**: rough + non-Cartan + tiny force,
- or provide evidence that counterexamples are rare/nonexistent at tested scales.

---

## 2. SU(2) A100/H100 stress-test hunt (4D, quaternion links)

### Goal
Massively parallel scan for configurations with:
- $B_{\mathrm{avg}}\ge \varepsilon$ (roughness),
- alignment score $\ge A_{\min}$ (not Cartan-ish),
- and small force norm.

### Key observed outcome (example run)
In a scan of 2000 fresh batches (batch size 32), the best hit still had very large force:
- best_force $\approx 1.06\times 10^4$
- $B_{\mathrm{avg}}\approx 0.534$
- alignment $\approx 0.667$

Interpreted cautiously: in the probed region of configuration space,
rough + non-Cartan configurations appear far from stationary.

### Script (as provided in chat; saved separately as `su2_a100_stress_test.py`)
See the downloadable script.

---

## 3. Local-cancellation lemma probing (documented experiment)

A smaller-scale experiment (exact force, random gauge transforms, random starts) reports:

- disorder stays $\mathcal O(1)$ while force norm stays bounded away from 0,
- increasing $L$ does not show force trending to 0,
- only near-abelian configurations approach low force.

This is exactly the qualitative signature expected from the Cartan-alignment coercivity program.

---

## 4. Spectral unit test (physics-correct normalization)

The project also includes a corrected momentum-space “unit test” for a massive real vector field Langevin dynamics
(in a sandbox model, not gauge theory).

Key fix: use FFT normalization `norm="ortho"` to avoid volume-scaling artifacts.
For $\lambda=0$, the measured spectral propagator should match:
\[
G(k) = \langle |A(k)|^2\rangle \approx \frac{1}{m^2 + \alpha \hat p(k)^2}.
\]

The script is saved as `spectral_unit_test.py`.

---

## 5. Downloadable scripts

- `su2_a100_stress_test.py`: SU(2) 4D hunt / SGLD manifold Langevin on $SU(2)$ links (unit quaternions).
- `spectral_unit_test.py`: momentum-space FFT-normalized sandbox verification.

