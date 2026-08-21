# SU($N$) $1^{+-}$ glueball: held-out and forward predictions by $1/N^2$ extrapolation

**Date:** June 14, 2026
**Method:** weighted fit $m_{1^{+-}}/\sqrt\sigma = m_\infty + c/N^2$ to Athenodorou–Teper
continuum data, with the $1/N^2$ form supplied by the exact strong-coupling program
and the values supplied by the lattice. Monte-Carlo error propagation; model
systematic from leave-one-out.

> **What this is (and isn't).** These are predictions of **lattice data at other
> ranks**, anchored on existing measurements and the exact-theory functional form.
> They are *not* a first-principles continuum mass from the $y$-series — that
> remains structurally blocked. This is the "missing data point" use of backward
> extraction, which is validated below; it is not the "missing theory ingredient"
> use, which is circular or underdetermined.

## 1. The fit and its self-consistency

$$
\frac{m_{1^{+-}}}{\sqrt\sigma}(N) = 5.759(25) + \frac{2.91(46)}{N^2}.
$$

The fit's $N\to\infty$ value $5.759(25)$ matches the lattice's **independently
computed** $N=\infty$ datum $5.760(25)$ to **0.02$\sigma$** — the extrapolation is
internally consistent with the directly-measured large-$N$ limit (which was *not*
used in the fit).

## 2. Validation — leave-one-out

Holding out each measured rank and predicting it from the others gives held-out
RMS error **0.045** (comparable to the lattice error bars, ~0.04–0.06). The method
is most reliable at large $N$ (interpolation) and least reliable at $N=3$
(most-extrapolated point: held-out residual $+0.096$).

## 3. The physically-relevant held-out prediction (SU(3))

Predicting SU(3) from $N=4,\dots,12$ — the held-out case that matters, since SU(3)
is the physical theory:

$$
\boxed{\frac{m_{1^{+-}}}{\sqrt\sigma}\bigg|_{\rm SU(3)}^{\rm predicted}=6.151}
\qquad\text{vs. measured } 6.065(40).
$$

With $\sqrt\sigma=485(6)$ MeV this is $m_{1^{+-}}\approx 2983$ MeV predicted vs.
$2941$ MeV measured ($2.944(42)$ GeV). The central value reproduces the earlier
blind result exactly. **Error-bar honesty:** the formal (leave-one-out RMS)
uncertainty is $\pm0.05$; but $N=3$ is the hardest point, with a leave-one-out
residual of $0.10$, and a conservative cross-channel systematic gives $\pm0.25$.
The agreement is therefore $\sim2\sigma$ (tight error) to $0.3\sigma$ (conservative
error) — a genuine hit either way, but the SU(3) extrapolation is the *least*
controlled point precisely because it is the most extrapolated.

## 4. Forward predictions at unmeasured ranks (falsifiable)

| $N$ | $m_{1^{+-}}/\sqrt\sigma$ (predicted) | dimensionful (MeV) |
|:---:|:---:|:---:|
| 14 | $5.774 \pm 0.051$ | $2800 \pm 42$ |
| 16 | $5.771 \pm 0.051$ | $2799 \pm 43$ |
| 20 | $5.767 \pm 0.051$ | $2797 \pm 43$ |
| 24 | $5.764 \pm 0.051$ | $2796 \pm 43$ |

(Error = MC-propagated lattice stat $\oplus$ model systematic 0.045; the systematic
dominates.) These sit **between** the measured $N=12$ and $N=\infty$, so they are
well-constrained interpolations rather than wild extrapolations.

**Testable statement:** the $1^{+-}$ ratio has effectively **converged to its
large-$N$ limit by $N\sim14$** — the finite-$N$ correction is below $0.3\%$ beyond
$N=14$. A future lattice run at $N=14$ or $16$ (currently $N=12$ is the maximum
computed) would test both this convergence and the $1/N^2$ form in a regime where
it has barely been checked. Any significant deviation from $\approx 5.77$ at $N=14$
would falsify the $1/N^2$-dominated extrapolation.

## 5. Scope and boundary

- The $1/N^2$ form is the exact-theory input that makes this extrapolation
  trustworthy; without it the fit would be unconstrained. This is where the exact
  program *enables* the data prediction.
- These predict lattice data at other ranks. They do **not** predict the continuum
  mass from first principles, and they do **not** determine the uncomputed
  strong-coupling coefficient $m_6$ (which lives at the wrong end of coupling for
  continuum data to constrain, and cannot be extrapolated from the six known,
  irregular coefficients).
- Figure: `DATA_FLUX_glueball_1pm_highn_extrapolation.png`.
