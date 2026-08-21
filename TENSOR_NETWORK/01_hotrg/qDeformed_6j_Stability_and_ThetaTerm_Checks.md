# q-Deformed \(6j\) Symbols, Numerical Stability, and \(\theta\)-Term Sanity Checks

> **Purpose.** This is the “don’t lie to yourself with complex tensors” document:  
> robust \(q\)-\(6j\) computation needs log-space numerics, and any \(\theta\)-term pipeline must pass non-negotiable positivity checks (e.g. \(\chi_{\mathrm{top}}\ge 0\) at \(\theta=0\) in a sensible setup).

This file is *not* a proof of the Yang–Mills mass gap; it’s a rigorous-ish set of computational constraints for the q-deformed/topological sector side of the project.

---

## 1. \(q\)-deformation and the physical mapping problem

A recurring idea is to encode a \(\theta\)-term weight \(e^{i\theta Q}\) through a local replacement of classical recoupling coefficients by quantum-group recoupling coefficients:
\[
\left\{\begin{matrix} \cdot & \cdot & \cdot \\ \cdot & \cdot & \cdot\end{matrix}\right\}
\quad \rightsquigarrow \quad
\left\{\begin{matrix} \cdot & \cdot & \cdot \\ \cdot & \cdot & \cdot\end{matrix}\right\}_q,
\qquad q=e^{i\vartheta}.
\]

The *physics risk*: \(4\)D Yang–Mills is not a TQFT. A naive “q-deform everything” might project the system toward topological behavior rather than YM dynamics plus a \(\theta\)-term.

So the mapping question is:

- What observable/topological quantity is the \(q\)-phase actually weighting?
- Is \(q=e^{i\theta}\), \(q=e^{i\theta/2}\), or something coupling-dependent?

Any serious program needs this mapping written down with gauge-invariant definitions.

---

## 2. A non-negotiable sanity check: \(\chi_{\mathrm{top}}\ge 0\)

If \(Z(\theta)\) is the partition function of a unitary theory with a \(\theta\)-term coupled to an integer topological charge \(Q\), a standard formal identity is
\[
Z(\theta)=\left\langle e^{i\theta Q}\right\rangle_{\theta=0}.
\]

Define the free energy density \(F(\theta)\) (convention-dependent constants ignored):
\[
F(\theta)= -\frac{1}{V}\log Z(\theta).
\]

Then at \(\theta=0\), the **topological susceptibility**
\[
\chi_{\mathrm{top}} := \left.\frac{\partial^2 F}{\partial \theta^2}\right|_{\theta=0}
\]
is expected to satisfy
\[
\chi_{\mathrm{top}}=\frac{1}{V}\langle Q^2\rangle_{\theta=0}\;\ge\;0.
\]

So:

- If your numerics produce \(\chi_{\mathrm{top}}<0\) near \(\theta=0\), you either:
  1. computed the derivative incorrectly (sign/norm error),
  2. are not actually computing a genuine \(Z(\theta)\) of the intended theory,
  3. have a severe truncation/sign instability (HOTRG + complex weights).

This is a **hard gate**. Nothing downstream is trustworthy until this is fixed.

---

## 3. Stability of \(q\)-Racah / \(q\)-\(6j\): log-space is mandatory

The quantum \(6j\) symbols for \(U_q(\mathfrak{su}(2))\) can be expressed in terms of \(q\)-Racah polynomials (or equivalent \(q\)-hypergeometric sums). Direct evaluation using factorial-like products will overflow/underflow and also suffer catastrophic cancellation when \(q\) is complex.

### 3.1 Basic strategy
Compute all multiplicative weights in **logarithmic form**:
- precompute \(\log [n]_q\) and \(\log [n]_q!\),
- evaluate prefactors as sums of logs,
- evaluate the Racah sum via log-sum-exp with complex phases.

Even then:
- for \(q\) near the unit circle, \([n]_q\) can be tiny (near zeros), causing numerical spikes,
- for large spins, the internal sum has many terms and heavy cancellation.

### 3.2 A practical bound shape (classical limit)
In the project exploration, the classical limit error was empirically consistent with a bound of the form
\[
\left|\left\{\cdots\right\}_q - \left\{\cdots\right\}\right|
\;\lesssim\; C\,\theta^2\, J_{\max}^{5/2},
\qquad q=e^{i\theta},
\]
in small \(\theta\) regimes and moderate \(J_{\max}\).

This is not a theorem here; it is the kind of scaling you can test and then use to pick a safe region \((\theta,J_{\max})\) for simulations.

---

## 4. Complex HOTRG: where the ghosts live

In HOTRG (or any tensor RG), the core move is an SVD-based truncation. With complex tensors:

- singular values are real nonnegative, but the truncation can destroy phase structure,
- normalization steps (dividing by max norm) accumulate a complex “free energy budget” that must be tracked carefully,
- truncation error can masquerade as physics (especially for \(\theta\)-dependent oscillations).

### 4.1 Minimum diagnostics
At each coarse-graining step, track:
1. the norm/scale factor and its phase,
2. the spectrum of singular values (is it decaying cleanly or flat/chaotic?),
3. stability under changing bond dimension \(\chi\),
4. conjugation/charge symmetry constraints (if present) before and after truncation.

---

## 5. What “success” looks like

You have a believable \(\theta\)-term pipeline if:

1. \(\chi_{\mathrm{top}}\ge 0\) at \(\theta=0\), robust under \(\chi\)-extrapolation.
2. \(F(\theta)\) is smooth near \(0\) and even in \(\theta\) (expected from CP at \(\theta=0\) in many cases).
3. The \(q\)-\(6j\) implementation passes:
   - symmetry identities (tetrahedral symmetries),
   - \(q\to 1\) limit checks,
   - stability sweeps in \(J_{\max}\), \(\theta\).
4. Results are stable under multiple truncation schemes (e.g. isotropic vs anisotropic RG steps).

Until these pass, any “phase transition at \(\theta=\pi\)” diagnosis is just numerical astrology.

---

## 6. Why this matters for the mass gap story

Even if the mass gap mechanism is pursued via curvature/Haar/polarity, the \(\theta\)-term side is valuable for:

- probing topological sector effects (slow modes, tunneling suppression),
- testing whether a deformation changes *dynamics* or only *topological weighting*,
- separating “local mass gap” from “global/topological finite-size effects”.

But the whole game collapses if the numerical pipeline violates basic positivity/consistency constraints.
