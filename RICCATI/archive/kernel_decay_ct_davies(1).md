# Deterministic Kernel Decay: Combes–Thomas vs Davies for the Massive Maxwell Operator

## Scope

This document consolidates two deterministic decay engines present in the corpus:

- Combes–Thomas (Appendix G) for finite-range uniformly positive operators.
- Davies semigroup conjugation (Appendix H) specialized to the massive Maxwell operator.

It also records the alternative Riccati-flux derivation (12-23-25 PULSE).

---

## 1. Massive Maxwell operator on links

Appendices B/G/H work with
\[
M_{\Lambda_L}=m_H^2\,I+\alpha_W\,\mathsf M_1,\qquad \mathsf M_1=d_1^*d_1,
\]
acting on \(\mathcal C^1(\Lambda_L;\mathfrak g)\cong \ell^2(E(\Lambda_L);\mathfrak g)\), with link graph distance \(\mathrm{dist}_E\).

Appendix B provides finite-range structure and row-sum bounds for \(\mathsf M_1\), and invariance of horizontals.

---

## 2. Combes–Thomas decay (Appendix G)

Appendix G proves a block Combes–Thomas estimate: if \(A\succeq a_0(A)I\) and has range \(R(A)\) with off-diagonal row-sum \(B_0(A)\), then
\[
\|(A^{-1})_{xy}\|_{\mathrm{op}}
\le
\frac{2}{a_0(A)}\,e^{-\eta_{\mathrm{CT}}(A)\,\mathrm{dist}(x,y)}.
\]

Applied to \(M_{\Lambda_L}\), the constants are expressible in terms of \(m_H^2,\alpha_W\) and uniform lattice overlap constants.

---

## 3. Davies decay (Appendix H)

Appendix H uses:
- Laplace transform formula \(M^{-1}=\int_0^\infty e^{-m^2 t}e^{-tL}dt\),
- Davies conjugation \(W_{\lambda}LW_{\lambda}^{-1}\),
- semigroup norm bound \(\|e^{-tL_{\lambda}}\|\le e^{c(\lambda)t}\),

to obtain an explicit kernel decay estimate
\[
\|(M^{-1})_{bb'}\|_{\mathrm{op}}
\le C(\lambda)\,e^{-\lambda\,\mathrm{dist}_E(b,b')}
\]
under a condition \(c(\lambda)<m_H^2\).

---

## 4. Riccati-flux derivation (12-23-25 PULSE)

The PULSE note derives CT-type exponential decay from an exponential conjugation plus a Riccati differential inequality for surface energies/currents, yielding a rate \(\gamma=O(\delta)\) in terms of spectral distance \(\delta=\mathrm{dist}(E,\sigma(H))\).

This provides a third, conceptually distinct “engine” that matches the same output interface.

---

## 5. What’s novel/high-leverage here

- Two independent deterministic decay engines (CT and Davies) are developed for the same operator class, with constants tracked in a form compatible with uniform-in-volume objectives.
- The Riccati-flux approach offers an alternate proof architecture that can be transplanted into settings where CT hypotheses are hard to verify directly.

Next expansion targets:
- unify the constants between G and H into a single “decay constant ledger” for \(M_{\Lambda_L}^{-1}\);
- connect these deterministic bounds directly into HS covariance bounds (Appendix F) without extra soft inequalities.

