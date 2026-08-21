# Tensor networks as a testbench: theta terms, sign problems, and scaling

## Why include this in a “derivations and proofs” extraction?

Because any mass-gap program that leans on subtle analytic inequalities should have a computational reality-check pipeline. The project contains a cluster of notes/calculations about why tensor networks (TN) can beat standard Quantum Monte Carlo (QMC) when a \(\theta\)-term induces a sign problem.

Even if this doesn’t directly prove a mass gap, it’s a credible route to *stress-test* the conjectural stability mechanisms numerically.

---

## 1. The sign problem in one line

With a \(\theta\)-term, path integral weights look like
\[
w(C)=|w(C)|\,e^{i\theta Q(C)},
\]
so they are not probabilities.

A standard trick rewrites expectation values as
\[
\langle \mathcal O\rangle
=\frac{\langle \mathcal O\,\mathrm{sign}\rangle_{|w|}}{\langle \mathrm{sign}\rangle_{|w|}},
\]
but the average sign typically decays exponentially with inverse temperature and/or volume, producing exponential cost.

---

## 2. Tensor-network workaround: keep tensors nonnegative, apply the phase once

The project notes a strategy:
- build local tensors with real, nonnegative entries (no local cancellations),
- and insert the complex topological phase as a global factor at the end (or track total charge \(Q\) through coarse-graining).

This doesn’t magically solve all complexity issues, but it avoids the *specific* exponential blow-up from the QMC sign problem.

---

## 3. Scaling claims

The project records polynomial/algebraic scaling for TN in the 1D rotor with \(\theta\)-term, e.g.
\[
\mathcal C_{\mathrm{TN}}\sim O(\beta^{15/4}\,\varepsilon^{-5/4}),
\]
in contrast to sign-problem-limited QMC scaling that is effectively exponential in \(\beta\) and precision.

It also notes:
- MPO contraction (1D) is efficient and exact,
- PEPS contraction (2D) becomes NP-hard and requires approximations,
which is why 4D gauge theory TN is *possible but brutal*.

---

## 4. Where this plugs into the mass-gap story

A concrete “science loop” you can run:

1. Use HOTRG/TRG to coarse-grain a lattice gauge model with controlled truncations.
2. Track observables sensitive to a gap (correlation length, transfer matrix spectrum proxies, Wilson loop excitation energies).
3. Compare the effective convexity constants / Hessian eigenvalue behavior across scales with the Riccati/MFIP predictions.

If the convexity lower bound decays as predicted (e.g. like \(1/(2t)\) in some notes) or stabilizes to a positive value, that feeds back into what assumptions are realistic in the analytic RG stability conjecture.

---

## 5. Big open technical issue

TN methods scale with bond dimension \(D\), and in higher dimensions \(D\) can blow up exponentially with correlation length. So the TN pipeline is not a guaranteed win—just a *more honest* fight than sign-problem QMC.

But as a companion to the analytic work, it’s exactly the kind of computational microscope you want.