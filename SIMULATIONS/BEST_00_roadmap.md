# Curvature-First Yang–Mills Program: Roadmap (Extracted)

This file is a **cleaned foundation map** of what the project is *trying to prove* (and where the technical novelty lives), assembled from the project notes in this workspace.

The core idea is to treat **convexity / functional-inequality control** as the primary invariant that is propagated by coarse-graining, and then to read out a **mass gap** via Osterwalder–Schrader (OS) reconstruction.

---

## 1. The pipeline in one line

\[
\boxed{
\text{Local convexity (SAFE)}\ +\ \text{Lyapunov drift}\ \Rightarrow\ \text{Global LSI/PI}\ \Rightarrow\ \text{Diffusion gap}\ \xRightarrow[\text{bridge}]{\text{intertwining}}\ \text{OS gap}\ \Rightarrow\ \text{Continuum mass gap}.
}
\]

There are *two* key “bridges”:

1. **Local-to-global FI patching** (SAFE-region inequalities + Lyapunov drift).
2. **Diffusion-to-OS bridge** (turn diffusion contraction into Euclidean-time correlation decay).

---

## 2. Modules in the project files

### Module A — SAFE-region convexity and explicit constants
- Goal: show the action (Haar + Wilson, projected to physical sector) is uniformly convex on a small ball \(\|A\|\le R_0\).
- Deliverable: explicit numerical lower bounds \(\kappa_*>0\), and explicit “error budget” \(\delta\) for Wilson/BCH terms.
- Why it matters: it’s the seed curvature that later becomes a global FI constant.

(See `From Local to Global LSI ...` and the SU(3) constants scan.)

### Module B — Lyapunov drift and tail control
- Goal: build a gauge-invariant Lyapunov \(W\ge 1\) with
  \[
  LW \le -\alpha W + \beta\,\mathbf 1_{\text{SAFE}}.
  \]
- Why it matters: lets you **patch** local FI into global FI without dimension-dependent blowup.

(See the Lyapunov and global FI sections in the “Full Proof Attempt” file.)

### Module C — Global PI/LSI for the gauge-invariant diffusion
- Goal: conclude global PI/LSI constants **independent of lattice volume** on the gauge-invariant sector.
- Output: diffusion spectral gap \(\lambda_{\mathrm{diff}}>0\).

This is the “geometric invariant” layer.

### Module D — Riccati convexity restoration under PBH/RG-type flow
- Goal: show convexity is stable (and can increase) under coarse-graining, via a matrix Riccati inequality
  \[
  \dot H \succeq -H^2 + K(t)I.
  \]
- Output: explicit lower bound \(u(t)\ge \sqrt{\kappa}\tanh(\sqrt{\kappa}t)\) for the minimum Hessian eigenvalue envelope.

This is your “convexification engine”.

### Module E — Projective-limit reflection positivity + continuum OS reconstruction
- Goal: if each lattice measure is reflection positive and the projections commute with reflection, then the projective limit measure is reflection positive, and OS reconstruction exists in the limit.

This is infrastructure needed to talk about a continuum Hamiltonian at all.

### Module F — The diffusion↔OS bridge (the main new math bottleneck)
- Goal: one theorem that converts diffusion contraction in configuration space into Euclidean-time decay in the OS Hilbert space.
- In operator terms, you want a one-step comparison like
  \[
  \langle f,(I-K)f\rangle \ge c\,\langle f,(-L)f\rangle
  \]
  where \(K\) is the Euclidean-time transfer operator restricted to time-zero observables, and \(L\) is the configuration-space diffusion generator.

This is *exactly* the point where your project stops being “standard probability tech” and becomes “new constructive QFT tech”.

---

## 3. What looks genuinely novel (as a research program)

- Reframing “mass gap” as a **spectral corollary of a convexity/LSI invariant** carried by RG.
- Treating **RG as a convexification flow**, with quantitative Riccati-style restoration bounds.
- A push toward **computable positivity tests** (reflection positivity stress tests).
- The conceptual move: **define universality classes by curvature/LSI data**, not by actions.

All of these are publishable directions even if they don’t immediately settle the Clay statement.

---

## 4. What is explicitly *not* done in this roadmap

This roadmap does **not** certify that the Clay YM axioms are satisfied or that the continuum theory is the standard YM universality class. It isolates the promising mathematics and the explicit bottlenecks.

The “new theorem to earn” is the Diffusion→OS bridge.
