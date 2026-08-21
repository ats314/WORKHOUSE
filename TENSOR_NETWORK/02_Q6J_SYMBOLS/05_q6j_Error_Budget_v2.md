# q–6j Classical-Limit Error Budget (Small \(\theta\), Finite Spin Cutoff)

## 0. Scope

This document extracts the q-deformation error-control result (Appendix E) for \(SU(2)\) q–6j symbols in the regime
\[
q=e^{i\theta},\qquad |\theta|\ll 1,\qquad j\le J_{\max}.
\]

The deliverable is a **quantitative bound** comparing the q–6j symbol to the classical 6j symbol, with explicit dependence on \(\theta\) and \(J_{\max}\).

---

## 1. q-integers: pointwise expansion and a uniform cutoff bound

Recall
\[
[n]_q = \frac{\sin(n\theta)}{\sin\theta}.
\]

Taylor expanding \(\sin\) at small \(\theta\) gives (for fixed \(n\theta\) small)
\[
[n]_q = n\left(1 - \frac{(n^2-1)\theta^2}{6} + O(n^4\theta^4)\right),
\]
hence the cutoff-uniform estimate
\[
|[n]_q - n|\;\lesssim\;\theta^2\,n^3
\qquad \text{for } 1\le n\le J_{\max}
\]
in the controlled regime.

---

## 2. q-factorials: multiplicative expansion

With \([N]_q! := \prod_{k=1}^N [k]_q\), take logs and expand:
\[
\log [N]_q! = \log N! + O(\theta^2 N^3),
\]
which exponentiates to a bound of the form
\[
|[N]_q! - N!|\;\lesssim\;\theta^2\,N^3\,N!
\]
for \(N\le J_{\max}\) and \(\theta J_{\max}\) sufficiently small.

---

## 3. Racah summands: ratios of q-factorials

The q–6j symbol is built from products and ratios of q-factorials (triangle coefficients + Racah sum).

Appendix E’s bookkeeping yields a **relative error** control for each summand of schematic size
\[
\text{relative error} \;=\; O(\theta^2 J_{\max}^3).
\]

---

## 4. Absolute error bound: combining with classical magnitude decay

To convert relative error into an absolute bound, one needs an upper bound on the magnitude of the classical 6j symbol.

Appendix E uses only that \(|\{6j\}|\) decays as a negative power of \(J_{\max}\), and records that the precise exponent depends on conventions / the semiclassical regime (common scalings quoted in the literature include \(J^{-3/2}\) in generic oscillatory regimes and weaker \(J^{-1/2}\) envelope bounds).

For the purpose of an *absolute* q–classical difference estimate, Appendix E assumes a conservative decay exponent \(\alpha\ge 1/2\) and derives:

\[
\big|\{6j\}_q - \{6j\}\big| \;\le\; C\,\theta^2\,J_{\max}^{5/2}
\]
in the controlled window (small \(\theta J_{\max}\)).

---

## 5. Practical inversion: how small must \(\theta\) be?

If you want \(|\{6j\}_q-\{6j\}|\le \varepsilon\), the bound implies the sufficient condition
\[
|\theta| \;\le\; \sqrt{\varepsilon/C}\; J_{\max}^{-5/4}.
\]

The constant \(C\) is not fixed in the corpus; the value of this inequality is the **scaling law** in \(\theta\) and \(J_{\max}\).

---

## 6. What is structurally reusable

- A clean, cutoff-explicit error budget for q-deformation at small \(\theta\).
- A “dial” for how close \(q\) must be to \(1\) for a given spin cutoff.
- A component that can be transplanted into any construction that uses q–6j data (tensor categories, transfer operators, q-deformed lattice models).

