---
title: "Extract 05 — OS Reconstruction, Mass Gap Extraction, and Continuum-Permanence Interfaces"
project: "APPENDIX PROOF OUTLINE"
---

## 1. Reflection positivity is the gatekeeper

To turn Euclidean correlation decay into a physical mass gap, the Osterwalder–Schrader (OS) framework requires **reflection positivity** (RP).

For lattice gauge theory with Wilson action, RP is established in the project (Appendix K) by verifying that the plaquette weight is a positive-type class function and that the action factorizes appropriately under time reflection.

This supplies the fundamental inequality:
\[
\langle F,\Theta F\rangle_{L^2(\mu)}\ \ge\ 0
\quad\text{for all }F\in\mathcal A_+,
\]
where \(\Theta\) is time reflection and \(\mathcal A_+\) are observables supported in the positive-time half-lattice.

---

## 2. OS framework at fixed cutoff: transfer matrix and Hamiltonian

Core 3 sets up the OS pre-Hilbert space by completing \(\mathcal A_+/\mathcal N\) under the RP inner product, where \(\mathcal N\) is the RP-null space.

Time translations induce a contraction semigroup on the OS Hilbert space, giving rise to a self-adjoint generator \(H\) (the OS Hamiltonian).

The physical mass gap is a spectral gap:
\[
\mathrm{spec}(H)\cap(0,m)\ =\ \varnothing.
\]

---

## 3. Gap extraction from Euclidean decay (Appendix L)

Appendix L provides a clean interface:

> **Euclidean exponential clustering \(\Rightarrow\) OS spectral gap.**  
> If time-separated correlations decay like \(e^{-m t}\) in the RP setup, then the OS Hamiltonian has a gap at least \(m\).

This is the step that converts the “correlation length” extracted from the hinge/Green-kernel analysis into a mass parameter in the reconstructed theory.

---

## 4. Thermodynamic limit at fixed cutoff (Core 9)

Core 9 transfers the fixed-volume OS gap to the infinite-volume limit via:

- existence of thermodynamic limits for the required correlation functions,
- preservation of reflection positivity and time-translation covariance in the limit,
- uniformity of the exponential clustering constants.

The outcome is an OS mass gap at **fixed lattice spacing** (fixed cutoff).

---

## 5. Conditional continuum extension (Core 10) and permanence interfaces (Appendix M)

The project then sketches a pathway to a continuum limit while retaining:

- reflection positivity,
- a spectral gap.

The tool is an abstract **permanence theory** for positive self-adjoint operators under limits of quadratic forms.

Appendix M packages standard functional-analytic facts as interfaces:

- closed, nonnegative quadratic forms \(\mathfrak a\) correspond to self-adjoint operators \(A\),
- monotone limits of forms (or Mosco convergence) imply strong resolvent convergence of operators,
- under suitable uniform coercivity/gap hypotheses, a spectral gap can persist in the limit.

Core 10 uses these interfaces to propose a *conditional continuum extension*:
if a projective system of OS measures/forms satisfies the needed uniform bounds, then the limiting continuum OS theory inherits a mass gap.

---

## 6. Why this is exciting

This part of the project is less about a single estimate and more about **architecture**:

- RP \(\to\) OS reconstruction \(\to\) mass gap extraction is classical,
- but *modularizing* the continuum limit as a set of “permanence interfaces” makes it easier to see exactly what must be proved (and what can be imported as known functional analysis).

If successful, the same interface approach should apply far beyond Wilson gauge theory: any RP Euclidean field theory built as a limit of finite-dimensional approximants could benefit from this permanence framework.

