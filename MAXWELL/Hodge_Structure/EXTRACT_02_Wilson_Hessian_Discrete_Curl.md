---
title: "Wilson Hessian as a Discrete Cochain Laplacian (Linearized Lattice Yang–Mills)"
date: "2025-12-29"
---

# Wilson Hessian as a discrete cochain Laplacian

## Abstract

Linearizing lattice Yang–Mills near the trivial configuration turns the Wilson action into a quadratic form
on Lie-algebra-valued $1$-cochains. The quadratic form is exactly the discrete Hodge energy
\[
S_W^{(2)}(X) \;=\; c_W\,\langle d_1 X, d_1 X\rangle_2,
\]
so the Hessian is
\[
\nabla^2 S_W(U^{(0)}) \;=\; 2c_W\,d_1^\ast d_1.
\]
This note reconstructs the derivation (using BCH to identify the linearized plaquette curvature),
characterizes the kernel (closed $1$-forms), and isolates a “physical positivity” statement:
on co-exact modes (the image of $d_1^\ast$) the operator is strictly positive.

---

## 1. Setup: lattice cochains and exponential coordinates

Let $\Lambda$ be a finite lattice with oriented edges $E(\Lambda)$ and oriented plaquettes $P(\Lambda)$.
Write $\mathfrak g$ for the Lie algebra of a compact gauge group $G$.

A Lie-algebra-valued $1$-cochain is an assignment
\[
X \in \mathcal C^1(\Lambda;\mathfrak g),\qquad X_{x,\mu}\in\mathfrak g\quad\text{for each edge }(x,\mu).
\]

Near the identity configuration $U^{(0)}$, we parametrize link variables by right-invariant exponentials
\[
U_{x,\mu} \;=\; \exp_G(X_{x,\mu}), \qquad X_{x,\mu}\ \text{small}.
\tag{1.1}
\]

---

## 2. Linearized plaquette holonomy is discrete curl

Fix a plaquette $p=(x;\mu,\nu)$ in directions $(\mu,\nu)$.
The plaquette holonomy is
\[
U_p \;=\; U_{x,\mu}\,U_{x+\hat\mu,\nu}\,U_{x+\hat\nu,\mu}^{-1}\,U_{x,\nu}^{-1}.
\tag{2.1}
\]
Using (1.1), this becomes a product of exponentials:
\[
U_p \;=\; \exp(X_1)\exp(X_2)\exp(-X_3)\exp(-X_4),
\tag{2.2}
\]
where
\[
X_1=X_{x,\mu},\quad X_2=X_{x+\hat\mu,\nu},\quad X_3=X_{x+\hat\nu,\mu},\quad X_4=X_{x,\nu}.
\]

By the BCH formula, there exists a smooth map $\Phi:\mathfrak g^4\to\mathfrak g$ such that
\[
U_p \;=\; \exp\!\big(\Phi(X_1,X_2,-X_3,-X_4)\big).
\tag{2.3}
\]
Write the decomposition
\[
\Phi(X_1,X_2,-X_3,-X_4) = A_p(X) + R_p(X),
\tag{2.4}
\]
with the **linear part**
\[
A_p(X) := X_1 + X_2 - X_3 - X_4
\tag{2.5}
\]
and the remainder $R_p(X)=O(\|X\|^2)$.

The map $X\mapsto A_p(X)$ is exactly the discrete exterior derivative $d_1$ on $1$-cochains:
\[
(d_1 X)_p \;=\; X_{x,\mu}+X_{x+\hat\mu,\nu}-X_{x+\hat\nu,\mu}-X_{x,\nu}.
\tag{2.6}
\]

---

## 3. Quadratic expansion of the Wilson action

The Wilson action has the general form
\[
S_W(U) \;=\; \sum_{p\in P(\Lambda)} \mathcal L\big(U_p(U)\big),
\tag{3.1}
\]
where $\mathcal L$ is a class function with a strict minimum at the identity (for standard $SU(N)$ Wilson, $\mathcal L(U)=\frac{\beta}{N}\mathrm{Re\,Tr}(1-U)$).

Because $\mathcal L$ is smooth and minimized at $U=\mathbf 1$, its second-order expansion around $U_p=\mathbf 1$ depends only on the quadratic term in $\Phi$:
\[
\mathcal L\big(\exp(\Phi)\big)
= c\,\|\Phi\|^2 + O(\|\Phi\|^3).
\tag{3.2}
\]
Inserting (2.4), the quadratic part depends only on the linear piece $A_p(X)$:
\[
\mathcal L\big(\exp(\Phi)\big)
= c\,\|A_p(X)\|^2 + O(\|X\|^3).
\tag{3.3}
\]

Summing over plaquettes yields the quadratic approximation
\[
S_W(U) \;=\; S_W(U^{(0)}) \;+\; c_W \sum_{p\in P(\Lambda)} \|(d_1 X)_p\|^2 \;+\; O(\|X\|^3).
\tag{3.4}
\]
In the canonical cochain inner products $\langle\cdot,\cdot\rangle_k$ this is
\[
S_W^{(2)}(X) = c_W\,\langle d_1 X, d_1 X\rangle_2 = c_W\,\langle X, d_1^\ast d_1 X\rangle_1.
\tag{3.5}
\]

---

## 4. Hessian formula and kernel

**Proposition 4.1 (Wilson Hessian at the identity).**  
At $U^{(0)}$,
\[
\nabla^2 S_W(U^{(0)}) \;=\; 2c_W\,d_1^\ast d_1.
\tag{4.1}
\]

Immediate consequences:

- **Nonnegativity.**
\[
\langle X, d_1^\ast d_1 X\rangle_1 = \|d_1 X\|_2^2 \ge 0.
\tag{4.2}
\]
- **Kernel equals closed $1$-forms.**
\[
d_1^\ast d_1 X = 0 \iff d_1 X=0.
\tag{4.3}
\]

Thus the kernel is precisely the space of discrete closed $1$-cochains.

---

## 5. “Physical” positivity on co-exact modes

Assume a discrete Hodge decomposition
\[
\mathcal C^1 = \mathrm{im}(d_0)\ \oplus\ \mathcal H^1\ \oplus\ \mathrm{im}(d_1^\ast),
\tag{5.1}
\]
where $d_0$ is the discrete gradient and $\mathcal H^1$ is the harmonic subspace.

Define the co-exact subspace
\[
\mathcal C^1_{\mathrm{coex}} := \mathrm{im}(d_1^\ast).
\]

**Proposition 5.1 (Strict positivity on co-exact modes).**  
The operator $d_1^\ast d_1$ is strictly positive on $\mathcal C^1_{\mathrm{coex}}$:
\[
X\in \mathrm{im}(d_1^\ast),\ d_1 X=0 \quad\Longrightarrow\quad X=0.
\tag{5.2}
\]
Equivalently, $\nabla^2 S_W(U^{(0)})$ has a strictly positive spectrum when restricted to $\mathrm{im}(d_1^\ast)$.

---

## 6. Interpretation

- $d_1 X$ is the linearized lattice curvature (“curl”).
- $d_1^\ast d_1$ is the discrete Maxwell/Yang–Mills quadratic operator.
- The kernel corresponds to gauge/pure-gradient directions plus possible global harmonic modes.
- The “physical” modes are the co-exact ones; on these, the Wilson Hessian is positive and provides a stabilizing quadratic energy.

In the curvature–dimension program, this operator supplies additional convexity beyond the baseline curvature coming from Haar geometry.
