# Prime Relations: Full Reduction of the Late-Time Growth Index Shift

## Scope

This document isolates the “prime relations” stack that reduces the late-time growth-index shift
\[
\boxed{\gamma(k)=\frac{6}{11}-\frac{3}{55}\alpha_\infty(k)}
\]
down to its irreducible operator and contour ingredients.

It is intended as a compact “result note” that can point into the detailed Prime Relations appendix series.

---

## 1. Exact starting point

Define \(N=\ln a\) and \(f=d\ln D/dN\). The exact first-order growth equation is
\[
f' + f^2 + \left(2+\frac{H'}{H}\right)f = \frac{3}{2}\Omega_m(1+\alpha_\infty).
\]
For flat \(\Lambda\)CDM, \(H'/H=-(3/2)\Omega_m\), \(\Omega_m'=-3\Omega_m(1-\Omega_m)\).

---

## 2. GR reference exponent \(6/11\)

In the late-time regime \(\Omega_m\ll1\), the dominant GR scaling is
\[
f_0=\Omega_m^{6/11}.
\]

---

## 3. Operator reduction (first-order inhomogeneous problem)

Linearize \(f=f_0+\delta f\) and isolate a first-order operator
\[
\mathcal L_f\delta f = \frac{3}{2}\Omega_m\alpha_\infty,
\qquad
\mathcal L_f = \partial_N + A(N),\ \ A(N)=2f_0+2-\frac{3}{2}\Omega_m.
\]

Late-time split:
\[
\mathcal L_f = (\partial_N+2) + 2\Omega_m^{6/11} + O(\Omega_m).
\]

---

## 4. Laplace resolvent and pole mechanics

Define \(R_f(s)=(\mathcal L_f-s)^{-1}\). The unperturbed resolvent has a simple pole at \(s_0=-2\).
First-order resolvent expansion produces a double pole; double-pole resummation yields a shifted pole.

Contour inversion and residue evaluation identify the additive pole shift \(\Delta s\), which converts to the exponent shift \(\Delta\gamma\) via
\[
\Delta\gamma = \frac{\Delta s}{f_0\ln\Omega_m}.
\]

---

## 5. Prime factorization

The final coefficient decomposes as
\[
\frac{3}{55}=\frac{3}{11}\cdot\frac{1}{5},
\qquad 55=11\times 5,
\]
with the \(11\) arising from a spectral-weight integral tied to \(\Omega_m'=-3\Omega_m(1-\Omega_m)\) and the \(5\) arising from the explicit linearization coefficient in the first-order \(f\)-operator.

---

## 6. Pointer

The full multi-file Prime Relations appendix stack (definition → exact dynamics → GR scaling → operator split → resolvent → contour → residue → rigidity) is contained in `PRIME RELATIONS.txt` and the generated Prime Relations .md series in the canvas.

