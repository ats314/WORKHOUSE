---
title: "q-6j vs classical 6j: small-$\theta$ error scaling and a safe truncation window for tensor networks"
date: "2025-12-02"
---

# Context and motivation

The project notebooks explore a concrete computational route to **4D Yang–Mills with a $\theta$-term** that is phrased in the language of **$q$-deformed $\mathrm{SU}(2)$ recoupling theory** (i.e. $q$-6$j$ symbols), then pushed through a **tensor-network / HOTRG-style** coarse graining.

The potentially novel part is not the definition of the $q$-6$j$ symbol itself (standard), but:

1. an **empirical small-$\theta$ scaling law** for the deformation error
2. using that law to define a **numerically “safe” $(J_{\max},\theta)$ window** that stabilizes truncation and contraction.

This is the sort of thing that, if upgraded from “numerically plausible” to “provable”, becomes a real tool.

---

# $q=e^{i\theta}$ and $q$-integers on the unit circle

Set
\[
q \;=\; e^{i\theta},\qquad \theta\in\mathbb{R}.
\]

For $q$ on the unit circle, the standard $q$-integer can be written as a sine ratio:
\[
[n]_q \;=\; \frac{q^n-q^{-n}}{q-q^{-1}}
      \;=\; \frac{\sin(n\theta)}{\sin\theta}.
\]

A small-$\theta$ expansion (Taylor series of sine) gives
\[
[n]_q
= n\left(1-\frac{(n^2-1)\theta^2}{6} + O(\theta^4)\right)
= n - \frac{n(n^2-1)}{6}\theta^2 + O(\theta^4).
\]

Define the $q$-factorial (for integer $n\ge 0$)
\[
[n]_q! \;=\;\prod_{k=1}^n [k]_q,\qquad [0]_q!:=1.
\]

Numerically, the notebooks use the stable “log factorial” form:
\[
\log([n]_q!) = \sum_{k=1}^n \log|[k]_q|.
\]

---

# Classical vs. $q$-deformed Racah formula for the 6$j$

Work with **doubled spins**:
\[
a,b,c,d,e,f\in\mathbb{Z}_{\ge 0},\qquad
j_a=\frac a2,\dots
\]
so that all triangle constraints become integer parity constraints.

## Triangle prefactors

Classically, the Racah prefactor uses
\[
\Delta(a,b,c)
=\sqrt{\frac{(A)!\,(B)!\,(C)!}{(D)!}}
\]
where
\[
A=a+b-c,\quad B=a-b+c,\quad C=-a+b+c,\quad D=a+b+c+2,
\]
and all arguments must be nonnegative even integers for admissibility.

The $q$-deformed analogue is
\[
\Delta_q(a,b,c)
=\sqrt{\frac{[A/2]_q!\,[B/2]_q!\,[C/2]_q!}{[D/2]_q!}}.
\]

## Racah sum core

The (classical) Racah sum is
\[
S = \sum_{z=z_{\min}}^{z_{\max}} (-1)^z\,
\frac{(z+1)!}{(z-x_1)!\,(z-x_2)!\,(z-x_3)!\,(z-x_4)!\,
(y_1-z)!\,(y_2-z)!\,(y_3-z)!},
\]
with integer combinations
\[
\begin{aligned}
x_1&=\tfrac12(a+b+c),\quad
x_2=\tfrac12(a+e+f),\quad
x_3=\tfrac12(d+b+f),\quad
x_4=\tfrac12(d+e+c),\\
y_1&=\tfrac12(a+b+d+e),\quad
y_2=\tfrac12(a+c+d+f),\quad
y_3=\tfrac12(b+c+e+f),
\end{aligned}
\]
and bounds $z_{\min}=\max(x_i)$, $z_{\max}=\min(y_i)$.

The $q$-deformed sum is the same but with factorials replaced by $q$-factorials:
\[
S_q = \sum_{z=z_{\min}}^{z_{\max}} (-1)^z\,
\frac{[z+1]_q!}{[z-x_1]_q!\cdots [y_3-z]_q!}.
\]

Finally,
\[
\begin{aligned}
\left\{\begin{matrix}
a&b&c\\ d&e&f
\end{matrix}\right\}
&=\Delta(a,b,c)\Delta(a,e,f)\Delta(d,b,f)\Delta(d,e,c)\; S,\\[4pt]
\left\{\begin{matrix}
a&b&c\\ d&e&f
\end{matrix}\right\}_q
&=\Delta_q(a,b,c)\Delta_q(a,e,f)\Delta_q(d,b,f)\Delta_q(d,e,c)\; S_q.
\end{aligned}
\]

---

# Empirical error scaling in the symmetric family

The notebook tests the **symmetric tetrahedron** family
\[
\left\{\begin{matrix}
j&j&j\\ j&j&j
\end{matrix}\right\},
\qquad j\in\left\{\tfrac12,1,\tfrac32,\dots, J_{\max}\right\}.
\]

Define the maximal deformation error
\[
\delta_{\max}(J_{\max},\theta)
:= \max_{j\le J_{\max}}
\left|
\left\{\begin{matrix}
j&j&j\\ j&j&j
\end{matrix}\right\}_q
-
\left\{\begin{matrix}
j&j&j\\ j&j&j
\end{matrix}\right\}
\right|.
\]

## Empirical scaling law (conjectural)

A global scan suggests that
\[
\boxed{
\delta_{\max}(J_{\max},\theta)\;\lesssim\; C\;\theta^2\; J_{\max}^{5/2}
}
\qquad\text{for small }\theta,
\]
with an observed constant roughly
\[
C \approx 0.18
\quad\text{(empirical, from a coarse grid scan)}.
\]

This is *not yet a theorem*; it is a numerically observed pattern in one family.
But it is a sharp enough pattern to become a working conjecture.

---

# A practical “safe window” for truncation

Suppose we want a target deformation error tolerance $\varepsilon$, e.g.
\[
\varepsilon = 10^{-3}.
\]

If the empirical inequality holds, then a sufficient condition is
\[
C\;\theta^2\; J_{\max}^{5/2}\;\le\;\varepsilon,
\qquad\text{i.e.}\qquad
\theta \;\le\; \sqrt{\frac{\varepsilon}{C}}\; J_{\max}^{-5/4}.
\]

Plugging $C\approx 0.18$ and $\varepsilon=10^{-3}$ yields a rough bound
\[
\theta \;\lesssim\; 0.0746\; J_{\max}^{-5/4}.
\]

The notebook then hard-clamps to a conservative region
\[
\boxed{
J_{\max}\le 4,\qquad \theta\le 0.02,
}
\]
and labels it “proven safe” in the computational workflow (safe numerically, not yet mathematically proven).

---

# Why this might matter for 4D YM numerics

If one builds a tensor network from $q$-recoupling data (e.g. $q$-6$j$ symbols or related face amplitudes), the standard stability disasters are:

- truncation error at large spin $j$
- oscillatory phases when $q=e^{i\theta}$
- numerical under/overflow in factorial expressions.

A controlled window like $(J_{\max},\theta)\in [0,4]\times[0,0.02]$ gives you a sandbox where:

- the deformation away from $q=1$ remains perturbative
- the recoupling weights remain stable enough for SVD-based compression.

That is potentially a stepping stone toward “turning on $\theta$” in a controlled way.

---

# How to turn the conjecture into a proof (a research plan)

A plausible proof strategy would use *perturbation theory of $q$-recoupling at $q=1$*.

1. **Differentiate** the $q$-6$j$ symbol w.r.t. $\theta$ at $\theta=0$ by differentiating through $\log([n]_q!)$ and the Racah sum.

2. Show the first derivative vanishes by symmetry (consistent with the observed $\theta^2$ leading behavior).

3. Bound the second derivative by estimating:
   - growth of the number of Racah terms with $j$
   - size of combinatorial factors from factorial ratios
   - cancellations from alternating signs.

4. Relate the power $J_{\max}^{5/2}$ to known semiclassical asymptotics (Ponzano–Regge-type behavior) for the classical 6$j$ and its smooth deformations.

If successful, you would get a genuine *a priori* error bound of the form
\[
\delta_{\max}(J_{\max},\theta)\le C_{\mathrm{rig}}\,\theta^2\,J_{\max}^{p},
\]
with explicit $C_{\mathrm{rig}}$ and $p$.

---

# Immediate next computational upgrades

- Replace the “placeholder face tensor” used in the HOTRG demo with an actual face amplitude built from $q$-6$j$ data.
- Scan the error on **generic** admissible $(a,b,c,d,e,f)$, not just the symmetric tetrahedron.
- Track how the safe window changes if you:
  - increase $J_{\max}$
  - vary the deformation $q$ off the unit circle (if allowed)
  - switch from absolute error to relative error.

