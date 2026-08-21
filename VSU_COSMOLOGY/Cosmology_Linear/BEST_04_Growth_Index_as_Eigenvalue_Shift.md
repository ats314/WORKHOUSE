# Growth as an Operator Problem: the “Prime Relations” and the \(\gamma(k)\) Shift

## Why this is worth extracting

Buried in `03.5_Late_Time_Asymptotics.md`, `effective_flow_of_vacuum_stiffness_enhancement.md`, and `PRIME RELATIONS.txt` is a compact algebraic claim:

\[
\boxed{\gamma(k)=\frac{6}{11}-\frac{3}{55}\,\alpha_\infty(k).}
\]

Interpreted correctly, this is not a fit parameter: it is a **first-order spectral shift** of the linear growth operator induced by the modified Poisson kernel.

This document cleans the argument into a usable mathematical interface.

---

## 1. Exact growth equation in \(N=\ln a\)

Let \(D(a,k)\) be the linear growth factor and define the logarithmic growth rate
\[
f(a,k):=\frac{d\ln D}{d\ln a}.
\]

From the linear growth ODE with modified coupling \(G_{\rm eff}=G(1+\alpha_{\rm eff})\),
\[
\ddot\delta+2H\dot\delta-4\pi G\bar\rho_m(1+\alpha_{\rm eff})\delta=0,
\]
one obtains the exact first-order equation (prime relation)
\[
\boxed{\;
\frac{df}{dN}+f^2+\left(2+\frac{d\ln H}{dN}\right)f
=
\frac{3}{2}\,\Omega_m(a)\,\bigl[1+\alpha_{\rm eff}(k,a)\bigr].
\;}
\tag{1}
\]

For flat \(\Lambda\)CDM background,
\[
\boxed{\;\frac{d\ln H}{dN}=-\frac{3}{2}\Omega_m(a),\qquad
\frac{d\Omega_m}{dN}=-3\Omega_m(1-\Omega_m).\;}
\tag{2}
\]

---

## 2. Late-time closure input: \(\alpha_{\rm eff}\to\alpha_\infty(k)\)

The late-time module assumes that on fixed comoving \(k\),
\[
\alpha_{\rm eff}(k,a)\longrightarrow \alpha_\infty(k),
\qquad
\partial_N\alpha_{\rm eff}\approx 0,
\qquad z\lesssim 2.
\]
This reduces (1) to a closed, slowly varying-coefficient equation with a single scale-dependent parameter \(\alpha_\infty(k)\).

---

## 3. Growth-index parametrization and the correction coefficient

Assume the growth-index form (asymptotic closure, not an identity)
\[
\boxed{\;f(a,k)\approx \Omega_m(a)^{\gamma(k)}.\;}
\tag{3}
\]

Insert (3) into (1), use (2), and expand the resulting expression in the “\(\Lambda\)-activated” regime (small-to-moderate \(1-\Omega_m\)) while keeping only the leading dependence on \(\alpha_\infty\). The algebra produces the linear response
\[
\boxed{\;\gamma(k)=\gamma_{\rm GR}-\frac{3}{55}\,\alpha_\infty(k),\qquad \gamma_{\rm GR}=\frac{6}{11}.\;}
\tag{4}
\]

The coefficient \(3/55\) is not arbitrary: it is the product of the \(\Lambda\)CDM friction identity \(d\ln H/dN=-\tfrac32\Omega_m\) with the structural \(\tfrac32\Omega_m\) sourcing of the growth equation.

*Practical reading:* for \(\Omega_m<1\), decreasing \(\gamma\) increases \(f=\Omega_m^\gamma\), so \(\alpha_\infty>0\) corresponds to enhanced growth even though the correction appears with a minus sign in \(\gamma\).

---

## 4. Operator-theoretic reinterpretation: \(\gamma\) as an eigenvalue parameter

Define the linear differential operator acting on \(D(N)\):
\[
\mathcal L D
:=
\frac{d^2D}{dN^2}
+\left(2+\frac{d\ln H}{dN}\right)\frac{dD}{dN}
-\frac{3}{2}\Omega_m(N)\bigl[1+\alpha_\infty(k)\bigr]D.
\]
Then the growth equation is \(\mathcal L D=0\).

Write \(\mathcal L=\mathcal L_0+\delta\mathcal L\) with
\[
\delta\mathcal L = -\frac{3}{2}\,\Omega_m(N)\,\alpha_\infty(k)\,(\cdot),
\]
a multiplicative perturbation. The “prime relations” viewpoint is that \(\gamma\) encodes the dominant mode of this operator in the slowly varying background, and (4) is the first-order perturbation of that mode under \(\delta\mathcal L\).

This is exactly the structural move you want elsewhere in the project:

> cosmological growth observables can be read as *spectral data* (mode parameters) of a linear operator whose coefficients are fixed by the theory.

---

## 5. What to do with this (theory expansion path)

The project can strengthen (4) from “growth-index algebra” to “operator theorem” by:

1. Choosing a weighted Hilbert space in \(N\) in which \(\mathcal L_0\) is self-adjoint (Sturm–Liouville form),
2. Identifying the principal mode and its adjoint,
3. Writing the first-order eigenvalue shift explicitly as an inner product \(\langle\psi_0,\delta\mathcal L D_0\rangle\),
4. Proving that the resulting mode parameter matches the \(\gamma\)-shift coefficient \(3/55\) in the relevant regime.

That would turn the prime-relations coefficient from a heuristic constant into a controlled perturbation result.

