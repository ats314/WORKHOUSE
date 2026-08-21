# Dichotomy Reduction: Mass Gap vs Uniform Lattice Spectral Gap

## Abstract

The project articulates a reduction principle: the continuum Yang–Mills mass gap problem is reframed as a **uniformity problem** for lattice spectral gaps as the lattice spacing \(a\to 0\).
This is packaged as a “dichotomy theorem”: either a uniform lattice gap persists (after appropriate scaling), or the continuum limit is gapless.

This document records that reduction as a **pipeline architecture** with explicit interfaces to be proved.

---

## 1. Lattice spectral gap input

On a finite lattice at spacing \(a\), consider a Markov generator \(L_a\) (e.g. gauge-fixed Langevin generator) with invariant measure \(\mu_a\).
Define the spectral gap (in \(L^2(\mu_a)\))
\[
\lambda_{\mathrm{lat}}(a) \ :=\ \inf_{f:\ \mathrm{Var}_{\mu_a}(f)\neq 0}\frac{\mathcal{E}_a(f,f)}{\mathrm{Var}_{\mu_a}(f)},
\]
where \(\mathcal{E}_a\) is the Dirichlet form associated to \(L_a\).

The mass-gap program in the corpus aims to produce a lower bound on \(\lambda_{\mathrm{lat}}(a)\) from convexity/curvature (Bakry–Émery, anomaly source).

---

## 2. The reduction statement (as recorded in the corpus)

### Dichotomy Statement (as formulated)

Assume:

1. a unique continuum limit exists as \(a\to 0\) (for the gauge theory under consideration),
2. the lattice-to-continuum reconstruction (OS/transfer machinery) holds in the relevant sector.

Then exactly one of the following is asserted:

1. **Mass Gap:** the continuum theory has a positive mass gap \(\Delta>0\), and the **Uniform Spectral Gap** condition holds:
   \[
   \liminf_{a\to 0}\frac{\lambda_{\mathrm{lat}}(a)}{a}\ >\ 0.
   \tag{2.1}
   \]
2. **Gapless:** the continuum theory is gapless, and (2.1) fails.

This dichotomy is not presented as closed within the corpus; rather it is a way to isolate “what remains” to be shown.

---

## 3. Why this is potentially useful

### Structural Principle: Uniformity is the only remaining obstruction

The reduction separates:

- **finite-\(a\) control** (where convexity/functional inequalities can be proved),
from
- **uniform-in-\(a\)** control (where UV renormalization and continuum limit issues reside).

In this view, the continuum mass gap is not blocked by mysterious new mechanisms; it is blocked by failure (or success) of a single uniformity statement.

---

## 4. Interfaces that must be supplied (explicitly open in the corpus)

To promote the dichotomy into a theorem, one must supply explicit bridges:

### Interface I: Uniform-in-\(a\) spectral gap from curvature sources

This is the “UV control” problem (Conjecture A and/or uniform anomaly positivity).
It is the step that prevents the lattice curvature floor from degrading as \(a\to 0\).

### Interface II: Spectral gap \(\Rightarrow\) correlator decay \(\Rightarrow\) Hamiltonian mass gap

This is the OS/transfer interface (Conjecture D in the corpus), and requires:
- a precise identification of which spectral gap is being controlled (full vs local sector),
- control of infrared/topological sectors (Conjecture IR).

---

## 5. What appears new (within the corpus)

### Pipeline Architecture
The “dichotomy theorem” functions as a **meta-interface**: it packages the mass gap question as a single measurable asymptotic statement \(\lambda_{\mathrm{lat}}(a)\gtrsim a\).

### Known vs new
- The idea that mass gap corresponds to exponential decay and transfer-matrix gap is standard.
- The specific refactoring “millennium gap \(\leftrightarrow\) uniform lattice Dirichlet spectral gap scaling” may be a nonstandard formulation (no clear prior equivalent known to me from this corpus alone), but it is conditional on substantial external inputs.

---

## 6. Minimal upgrades needed

1. State precisely which generator \(L_a\) is used (gauge-fixed Langevin? projected physical generator?).
2. Prove (or assume explicitly) a quantitative scaling relation between \(\lambda_{\mathrm{lat}}(a)\) and the transfer-matrix/Hamiltonian gap.
3. Provide a uniform renormalization estimate preventing degradation of the convexity source as \(a\to 0\).