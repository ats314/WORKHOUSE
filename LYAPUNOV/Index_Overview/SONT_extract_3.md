# Reflection positivity, strip actions, and transfer matrices (project extract)

*Status:* **project extract; structural**, not “new” by itself, but it is the stage on which any
mass-gap proof must ultimately live: a spectral statement about a positive transfer operator.

---

## 1. Strip decomposition and the transfer kernel

The project uses a standard but very useful trick: define a **strip action** on a time slab
between slices $t$ and $t+1$ so that

1. concatenating strips adds actions exactly, and  
2. integrating over the time-like links produces a **positive integral kernel**.

Schematic form:
\[
S_{\mathrm{strip}}(U_t,U_{t+1};U_{\text{timelike}}) \;=\;
\text{(plaquettes in the slab)} \;+\; \tfrac12\text{(plaquettes on shared boundaries)}.
\]

That “half-weighting” ensures exact additivity:
\[
S_{[t,t+2]} = S_{\mathrm{strip}}(t,t+1)+S_{\mathrm{strip}}(t+1,t+2).
\]

After integrating time-like links, one obtains a kernel
\[
K(U_t,U_{t+1}) \;\ge\; 0
\]
and thus a transfer operator $T$ on an $L^2(\nu)$ space of time-slice configurations:
\[
(Tf)(U_t) \;=\; \int K(U_t,U_{t+1})\,f(U_{t+1})\,d\nu(U_{t+1}).
\]
The kernel positivity is the “microscopic” reflection positivity mechanism.

---

## 2. Reflection positivity and projective limits

A technically important project point is that reflection positivity must persist under taking limits.
The files include a lemma of the form:

> if each finite-volume measure $\mu_n$ is reflection-positive and the system is compatible under
> restriction maps (a projective family), then the projective limit measure $\mu$ is reflection-positive.

This matters because it is what allows you to even **define** a physical Hilbert space and Hamiltonian
in the limit:
\[
T = e^{-aH}\quad\Rightarrow\quad H\ \text{self-adjoint,}\ \ \mathrm{spec}(H)\subset[0,\infty).
\]

---

## 3. The “mass gap lives here”

Once you have $H$ (or $T$), the mass gap is a clean spectral statement:
\[
\mathrm{spec}(H) = \{0\}\cup [m,\infty),\qquad m>0,
\]
equivalently
\[
\sup\mathrm{spec}\big(T|_{\Omega^\perp}\big)\;\le\;e^{-am},
\]
where $\Omega$ is the vacuum vector.

Everything else in the project is ultimately “engineering” to obtain a lower bound on $m$ that
survives limits.

---

## 4. Where the project’s novel analytic ingredients plug in

The project’s “new-ish” ingredients (see Docs 1–2) are designed to feed this operator stage:

- blockwise functional inequalities $\Rightarrow$ uniform contraction for coarse-grained semigroups;  
- drift/cancellation rigidity $\Rightarrow$ prevent rough-but-flat obstructions;  
- boundary-strip gluing $\Rightarrow$ propagate local contraction into global spectral control.

The transfer operator is the endgame object: if an inequality implies
\[
\|T^n\psi\|\le e^{-nm a}\|\psi\|\quad(\psi\perp \Omega),
\]
you have a mass gap.

---
