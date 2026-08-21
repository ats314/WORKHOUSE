Document 7 — Strong-Coupling Transfer Matrix Mass Gap

# Document 7: Strong-Coupling Transfer Matrix Mass Gap

So far we’ve used a **geometric / probabilistic** path (Hessian + Bakry–Émery). Here we sketch the complementary **Hamiltonian / transfer matrix** argument for the mass gap in the strong-coupling regime.

## 1. Anisotropic Lattice and Transfer Matrix

Consider an anisotropic Wilson action with separate spatial and temporal couplings:
\[
  S(U) =
  \beta_s \sum_{p\,\text{spatial}}\Big(1 - \frac{1}{N}\Re\mathrm{Tr}U_p\Big)
  + \beta_t \sum_{p\,\text{temporal}}\Big(1 - \frac{1}{N}\Re\mathrm{Tr}U_p\Big).
\]

The partition function can be written as
\[
  Z = \mathrm{Tr}(T^{N_t}),
\]
where \(T\) is the transfer matrix between time slices (spacing \(a_t\)), and
\[
  T = e^{-a_t H},
\]
with \(H\) the Hamiltonian in the Kogut–Susskind Hamiltonian formulation.

The eigenvalues of \(T\) are \(\lambda_n = e^{-a_t E_n}\), where \(E_n\) are the energy levels.

## 2. Strong-Coupling Expansion of Correlators

Let \(O\) be a gauge-invariant operator (e.g. a Wilson loop or Polyakov loop). Its Euclidean time correlator
\[
  G(T) := \langle O(0) O(T)\rangle
\]
can be written spectrally:
\[
  G(T) = \sum_n |c_n|^2 e^{-E_n T},\quad c_n = \langle n|O|0\rangle.
\]

In the strong-coupling expansion (\(\beta_t\) small), \(G(T)\) is dominated by the minimal area surface of temporal plaquettes connecting the operator insertion at time 0 and time \(T\). Each temporal plaquette brings a factor of order \(\beta_t\), so for an operator of spatial extent \(L\),
\[
  |G(T)| \lesssim C(\beta_s,\Lambda_s)\,(c\beta_t)^{L T/a_t},
\]
where:

- \(L\) is the minimal length (or perimeter) associated with the operator;
- \(c>0\) is a group- and dimension-dependent constant;
- \(C(\beta_s,\Lambda_s)\) is a prefactor depending on spatial details but **not** on \(T\).

## 3. Lower Bound via the First Excited State

Choose \(O\) so that:

- It creates a nontrivial excitation: \(\langle 0|O|0\rangle=0\);
- The overlap with the first excited state is nonzero: \(c_1 = \langle 1|O|0\rangle \neq 0\).

Then for large \(T\),
\[
  G(T)
  = |c_1|^2 e^{-(E_1 - E_0)T} + \text{higher excited terms}.
\]

Thus
\[
  |G(T)|
  \ge |c_1|^2 e^{-\Delta T}
  - \sum_{n\ge2} |c_n|^2 e^{-(E_n - E_0)T},
\]
where \(\Delta = E_1 - E_0\). For sufficiently large \(T\), the first term dominates, and we obtain
\[
  |G(T)| \gtrsim C'\, e^{-\Delta T},
\]
for some \(C'>0\).

Combining with the strong-coupling upper bound:
\[
  C' e^{-\Delta T}
  \lesssim C(\beta_s,\Lambda_s)\,(c\beta_t)^{L T/a_t}.
\]

Take logs and divide by \(T\), then let \(T\to\infty\):
\[
  -\Delta
  \lesssim \frac{L}{a_t}\log(c\beta_t),
\]
which yields a **lower bound** on \(\Delta\):
\[
  \Delta \gtrsim \frac{L}{a_t}\,|\log(c\beta_t)|.
\]

More precisely, one can show:

**Theorem 3.1 (Strong-Coupling Transfer Matrix Gap).**  
For sufficiently small \(\beta_t\),
\[
  \frac{\lambda_1}{\lambda_0} \le (c\beta_t)^L < 1,
\]
where \(L\) is a minimal nontrivial loop length, and \(c>0\) independent of \(T\). Consequently,
\[
  \Delta := E_1 - E_0
  = -\frac{1}{a_t}\log\frac{\lambda_1}{\lambda_0}
  \ge \frac{L}{a_t}|\log(c\beta_t)| > 0.
\]

Thus, in the strong-coupling regime, the Hamiltonian has a strictly positive mass gap.

## 4. Complementarity with the Geometric Path

- The **geometric path** (Documents 3–5) produces a mass gap via **uniform convexity** and Bakry–Émery, valid for \(g^4 > 12/(c_0 a^2)\).
- The **Hamiltonian path** here gives a mass gap via strong-coupling expansion, valid for small \(\beta_t\) (large temporal coupling).

In the overlapping strong-coupling region, both arguments are available and mutually consistent. This is strong evidence that the gap is a robust feature of the theory at finite cutoff, not an artifact of a particular formalism.


⸻
