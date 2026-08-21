# Stress-testing the curvature–mass fit (small-$n$ reality check)

*Generated 2025-12-29.*

## What exists right now

The repository proposes an **effective geometric mass proxy** $\mu_\mathrm{eff}$ (built from curvature bookkeeping) and compares it to a measured lattice mass gap $m_\mathrm{lat}$ over a short $\beta$ window.

The simplest falsifiable hypothesis is proportionality **through the origin**:
\[
m_\mathrm{lat} \approx k\,\mu_\mathrm{eff}.
\]

Using the five-point dataset in `curvature_mass_fit.py` / `06_evidence_curvature_mass_fit.md`, the constrained least-squares fit gives:

\[
k = 0.962363,\qquad R^2 = 0.998237.
\]

This is visually and numerically tight — but with $n=5$ points, it is **not** yet evidence of a law of nature. It is evidence of a *promising correlation* that needs stress-testing.

---

## 1. Immediate small-$n$ sanity checks

### 1.1 Leave-one-out (LOO) sensitivity

Refit $k$ using 4 points at a time (drop one $\beta$ value, refit).

Observed range:
\[
k_\mathrm{LOO} \in [0.960809,\,0.964760].
\]

Interpretation: no single point dominates the fit. That’s good — but it’s still small-$n$.

### 1.2 Bootstrap slope uncertainty (treating the 5 pairs as exact)

Resampling the five $(\mu_\mathrm{eff},m_\mathrm{lat})$ pairs with replacement and refitting gives an approximate 95% bootstrap interval:

\[
k \in [0.958320,\,0.967701],
\]
with median near 0.962363.

---

## 2. What would actually convince a skeptical physicist

You need to break the “five points can lie” curse.

### 2.1 Expand the $\beta$ window

- Add points deeper into strong coupling and further toward weak coupling.
- Check whether a single slope works across windows, or whether you need a running $k(\beta)$.

### 2.2 Add error bars (both axes if possible)

Right now the regression is essentially deterministic. In reality:

- $m_\mathrm{lat}$ has statistical and systematic uncertainties (fit range, excited-state contamination, finite volume).
- $\mu_\mathrm{eff}$ has model uncertainty (SAFE constants, projector choice, RG degradation assumptions).

A believable claim requires uncertainty propagation.

### 2.3 Try competing models

Use the scaffold `fit_stress_test.py` to compare:

- linear-through-origin: $m=a\mu$
- affine: $m=a\mu+b$
- power: $m=c\mu^p$
- square-root: $m=c\sqrt\mu$

If linear-through-origin keeps winning *after* you add noise/points, that’s when it gets spicy.

### 2.4 Cross-theory tests

If the mechanism is “geometry drives gap”, then similar proportionality should (in some form) appear for:

- different gauge groups (SU(2), SU(4), …),
- different mass channels (glueball $0^{++}$ vs string tension vs torelon),
- different lattice actions (Wilson vs improved).

---

## 3. Reproducible code

- `curvature_mass_fit.py` reproduces the slope and the $R^2$ from the five hard-coded points.
- `fit_stress_test.py` is a *general* regression + bootstrap harness once you supply a CSV with more points and (optional) uncertainties.

