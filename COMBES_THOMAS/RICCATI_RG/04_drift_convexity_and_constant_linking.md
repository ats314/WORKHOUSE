# Lyapunov Drift Fits, Convexity Scans, and Constant Linking

This document collects the “empirical but repeatable” diagnostics that point toward a coherent analytic story, even when they are not yet full identities.

---

## 1. Drift inequality checks: large slack is a feature

The canonical form tested is:
\[
\mathcal{L}V \le -\lambda V + b,
\]
with \(\mathcal{L}\) the generator (e.g. of a lattice gauge Markov chain) and \(V\) a Lyapunov function.

In the drift-strip / drift-check runs, multiple parameter settings pass with very large slack. A representative output shows:

- \(\mathbb{E}[V] \approx 2.00052\)
- \(\mathbb{E}[\mathcal{L}V] \approx -3.54493\)
- \(\mathbb{E}[\text{RHS}] \approx -0.00279\)
- minimum slack \(\approx 1.98638\)
- PASS = True

At higher \(\beta\), the same pattern persists with even more slack.

Interpretation:

- either the chosen \(V\) is extremely conservative,
- or the sampled regime is far from the “critical” region where the inequality becomes tight.

---

## 2. A constant-link hypothesis: \(b\) tracks \(C_0\)

A separate fit reports (β=0 case):

- \(\hat\lambda \approx 1.5166\)
- \(\hat b \approx 43.1239\)

This is numerically close to the Maxwell \(C_0(\Delta_1)\approx 43.9077\) computed in the decay-bound pipeline.

This suggests a testable big-picture idea:

> the same operator norm / row-sum constant that controls exponential decay might also control the drift offset term \(b\).

This is not proven, but it is exactly the kind of cross-diagnostic coherence that warrants a targeted A100 sweep.

---

## 3. Convexity and β: fixed stabilizers fail on growing dragons

Convexity / curvature scans show a robust trend: as β increases, curvature positivity becomes harder to maintain unless the stabilizer scales appropriately.

One small-\(L\) scan compares Wilson vs Wilson+Haar:

- β=0.5: \(\lambda_{\min}(W+\text{Haar})\approx +0.1907\), while \(\lambda_{\min}(W)\approx -0.0594\)
- β=1.0: \(\lambda_{\min}(W+\text{Haar})\approx +0.1159\), while \(\lambda_{\min}(W)\approx -0.1341\)
- β=2.0: \(\lambda_{\min}(W+\text{Haar})\approx -0.0394\) (positivity fails again)

A separate scan shows that a “scale” parameter shifts the β-threshold: larger scale can flip negativity earlier.

Interpretation:

- a constant Haar coefficient is a *fixed mass term*,
- while the Wilson curvature contribution grows with β,
- so stability requires either (i) β-scaled stabilization, or (ii) shrinking convex neighborhoods.

---

## 4. Concrete next tests

1. Define a stabilizer family \(c_H(\beta)\) and test whether \(\lambda_{\min}\) remains positive over a fixed local neighborhood.
2. Fit \(b\) and compare it against \((C_0, D_E)\) across \(L\) (constant unification).
3. Evaluate drift inequalities on the projected (physical) subspace to avoid gauge-mode pollution.

