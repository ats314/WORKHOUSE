# Horizon Link $a_0 \leftrightarrow H_0$ and Nonlocal Action Roadmap (Conjecture + Next Tests)

This document extracts the “cosmic unification” idea and the project’s own internal critique:  
galaxy-scale stiffness $a_0$ might be tied to the Hubble scale, but **the correct scientific stance is “working hypothesis,” not “Q.E.D.”**

---

## 1. The empirical coincidence (as stated in the archive)

The project states a numerical relation of the form

\[
a_0 \;\approx\; \frac{cH_0}{6}.
\]

Using $H_0 \approx 74\ {\rm km\,s^{-1}\,Mpc^{-1}}$, this yields $a_0\sim 1.2\times 10^{-10}\rm\,m/s^2$ (the galaxy phenomenology value).

A related comparison is to the de Sitter horizon / Gibbons–Hawking scale, which often produces factors like $2\pi$; the exact rational coefficient is not fixed by the current argument.

---

## 2. The project’s own “credibility fix”: stop claiming proof

The GRAV PDF explicitly recommends:

- replace “Q.E.D.” language with “closed phenomenological consistency loop,”
- add an effective action (even toy),
- consider a **nonlocal kernel** at the curvature level.

This is the right instinct. It moves the work from rhetoric toward a calculational program.

---

## 3. Minimal effective actions suggested in the archive

### 3.1 Scalar / AQUAL-like toy action

A Newtonian-limit scalar field action with stiffness function $F$:

\[
S = \int d^4x\,\sqrt{-g}\left[\frac{R}{16\pi G} + \frac{a_0^2}{8\pi G}\,F\!\left(\frac{|\nabla\Phi|^2}{a_0^2}\right) + \rho\,\Phi \right].
\]

This yields a modified Poisson structure of the form

\[
\nabla\cdot\big(\mu(|\nabla\Phi|/a_0)\,\nabla\Phi\big)=4\pi G\rho,
\qquad \mu=F'.
\]

### 3.2 Nonlocal curvature kernel (IR modification)

A schematic curvature-level deformation:

\[
R \;\to\; R + R\,\mathcal{K}(\Box/H_0^2)\,R,
\]

where $\mathcal{K}$ is a nonlocal form factor that turns on in the IR.

This is the natural place to encode:

- a cosmological IR scale ($H_0$),
- scale dependence ($k$-space modification),
- and (if done carefully) causal propagation.

---

## 4. The “physics to-do list” that turns this into a test

If the horizon link is real, you must show:

1. **Linear perturbations**: derive eigenmodes (sub-/super-horizon) and the modified growth equation.
2. **CMB**: recover acoustic peaks (especially the third peak) without CDM particles.
3. **Growth observables**: predict $f\sigma_8(z)$ and $S_8$ consistently with weak lensing + RSD.
4. **ISW sign**: show whether late-time potential decay flips the ISW cross-correlation sign.

The project already contains analytic scaffolding for these items (separate documents exist in the archive); the gap is running the pipeline against real likelihoods.

---

## 5. What counts as “success”

A credible success condition would look like:

- SPARC: fits competitive with best MOND/RAR fits **without** per-galaxy parameter hacks,
- clusters: lensing mass profile matched by the scalar sector self-energy (not just galaxy RCs),
- cosmology: CLASS/CAMB-level fit to Planck + BAO + SN + RSD within tolerances.

Until then, treat $a_0\sim cH_0$ as a **high-value clue**, not a theorem.

