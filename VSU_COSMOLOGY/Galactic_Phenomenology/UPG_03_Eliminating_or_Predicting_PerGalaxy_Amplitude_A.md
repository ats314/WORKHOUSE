# Eliminating (or predicting) the per-galaxy amplitude \(A\)

## 0. What \(A\) is doing right now

In the SPARC Hankel pipeline you currently compute a galaxy-by-galaxy amplitude \(A\) (often written as \(A_{\rm best}\)) so that the predicted squared speed is *linear* in \(A\):
\[
v^2_{\rm model}(r)=A\,v^2_{\rm model,\;A=1}(r;\mu,\ldots).
\]

Operationally, \(A\) is obtained as a weighted least-squares scale factor for each galaxy.

This makes the *shape* of the response (set by \(\mu\), tapering, cutoffs, etc.) globally testable, but it also makes the model less predictive, because \(A\) behaves like a per-galaxy “dial”.

## 1. Why \(A\) is almost certainly re-parameterizing baryonic systematics

Within SPARC/rotmod conventions, the baryonic templates are already linear in the stellar mass-to-light ratios,
\[
v^2_{\rm bar}(r;\Upsilon_{\rm disk},\Upsilon_{\rm bul})
= v^2_{\rm gas}(r) + \Upsilon_{\rm disk}\,v^2_{\rm disk,\,\Upsilon=1}(r)
+ \Upsilon_{\rm bul}\,v^2_{\rm bul,\,\Upsilon=1}(r).
\]

So any global multiplicative rescaling of the baryonic field is *degenerate* with some combination of:
- \(\Upsilon\) priors (stellar population synthesis),
- distance/inclination systematics, and
- beam-smearing / resolution effects (especially at small radii).

That means \(A\) should not be treated as an “extra physics amplitude” unless you can show it cannot be absorbed into those nuisance directions.

## 2. Two clean ways forward

### Option A: kill \(A\) by absorbing it into \(\Upsilon\) (preferred)

Replace the single amplitude \(A\) by explicit \(\Upsilon\) parameters with priors:
- galaxy-by-galaxy \(\Upsilon_{\rm disk},\Upsilon_{\rm bul}\) constrained by SPS (colors) and SPARC priors; or
- a *hierarchical* model: \(\Upsilon\) drawn from a population distribution with hyperparameters.

Then set \(A \equiv 1\) by definition.

This is the most honest version of “predicting \(A\)”: you’re not predicting a mysterious dial; you’re predicting \(\Upsilon\).

**Practical implementation in the existing pipeline**  
If your current code fixes \(\Upsilon_{\rm disk}=\Upsilon_{\rm bul}=0.5\), then the fitted amplitude effectively behaves like
\[
A \sim \frac{\Upsilon_{\rm eff}}{0.5}
\]
where \(\Upsilon_{\rm eff}\) is the baryon-weighted effective M/L of that galaxy.

A simple first upgrade is:
- treat \(\Upsilon_{\rm disk}\) as a free parameter with a prior (e.g. normal around 0.5 with \(\sigma\sim0.1{-}0.2\)),
- keep \(\Upsilon_{\rm bul}\) tied to \(\Upsilon_{\rm disk}\) or with its own prior,
- remove \(A\).

### Option B: predict \(A\) from morphology/environment regressors

If you want to keep \(A\) as a single scalar per galaxy (for computational convenience), then force it to be a *function*,
\[
A = A(\mathbf{x}),
\]
where \(\mathbf{x}\) is a feature vector available per galaxy (and ideally physically motivated).

Candidates:
- stellar color (SPS proxy for M/L),
- central surface brightness / scale length,
- bulge-to-disk ratio,
- environment density / external field proxy,
- gas fraction.

Then fit a *small* parametric model (e.g. linear in features or a shallow GP) across the SPARC sample.

The key is: the mapping must be predictive out-of-sample, otherwise you just rebuilt the dial in disguise.

## 3. A concrete “no-excuses” target metric

After eliminating or predicting \(A\), you can score the model by:
1. the global best-fit \(\mu\),
2. the distribution of residuals in \(v(r)\) (not just \(v^2\)),
3. stability on dwarfs (low-\(g\) systems), and
4. the posterior consistency of \(\Upsilon\) with SPS/SPARC priors.

If the anti-kernel is real physics, it should survive the removal of \(A\) without forcing \(\Upsilon\) to absurd values.

## 4. Immediate next step

Implement “Option A” first:
- remove \(A\),
- let \(\Upsilon_{\rm disk}\) vary with an SPS prior,
- keep \(\mu\) global.

This tests whether \(A\) was mostly nuisance re-scaling.

If that passes, then Option B becomes meaningful (it can reduce variance and improve predictive power).
