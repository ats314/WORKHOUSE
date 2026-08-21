# Working conjecture: encoding a 4D SU(2) θ-term via quantum-group deformation

> **Status note:** This document is a *working theory* extracted from the project notebooks.  
> It is **not** a proven equivalence to continuum 4D Yang–Mills with a θ-term.  
> The value is that it proposes a concrete, testable mapping that can be falsified or refined.

## 1. The “real” θ-term in Euclidean Yang–Mills

In Euclidean signature, the SU(2) Yang–Mills partition function with a θ-angle is

\[
Z(\theta)\;=\;\int \mathcal{D}A\;\exp\!\left(-S_{\text{YM}}[A]\;+\;i\,\theta\,Q[A]\right),
\]

where \(Q[A]\in\mathbb{Z}\) is the topological charge (instanton number in the continuum).

The free energy density is

\[
f(\theta)\;=\;-\frac{1}{V}\log Z(\theta),
\]

and the **topological susceptibility** is defined by the curvature at the origin:

\[
\chi_{\text{top}}
\;=\;
\left.\frac{\partial^2 f(\theta)}{\partial\theta^2}\right|_{\theta=0}
\;=\;
\frac{1}{V}\,\langle Q^2\rangle_{\theta=0},
\]
(using CP symmetry, \(\langle Q\rangle_{\theta=0}=0\)).

So the *physically standard* target observable is a second derivative of \(\log Z(\theta)\) at \(\theta=0\).

## 2. The project’s key hypothesis (as implemented)

The project implements a bold hypothesis:

> **Hypothesis H (θ ↔ q):** the θ-dependence can be represented by deforming the SU(2) recoupling data to that of the quantum group \(U_q(\mathfrak{su}(2))\) with  
> \[
q \;=\; e^{i\theta}.
\]

Under this hypothesis, the θ-angle enters the tensor-network weights through **q-deformed representation theory**:
- replace the ordinary dimension \(2j+1\) by the **quantum dimension**
  \[
  \dim_q(j)\;=\;[2j+1]_q,
  \]
- replace classical Wigner \(6j\)-symbols by **quantum \(6j\)-symbols** \(\{6j\}_q\) in the vertex amplitude.

This is conceptually similar to how quantum groups arise in **Chern–Simons / TQFT** and **spin-foam** constructions—except here it is being used as a proxy for 4D θ-physics.

## 3. Definitions used in the code: q-numbers and q-factorials

The central building block is the **q-number**
\[
[n]_q
\;=\;
\frac{q^n - q^{-n}}{q - q^{-1}}.
\]

When \(q=e^{i\theta}\) and \(q\neq \pm 1\), this simplifies to the trigonometric form
\[
[n]_q
\;=\;
\frac{\sin(n\theta)}{\sin(\theta)}.
\]

Then the **q-factorial** is
\[
[n]_q! \;=\;\prod_{k=1}^n [k]_q,
\quad
[0]_q!:=1.
\]

### Classical limit check

As \(\theta\to 0\), we have the standard small-angle limit
\[
\sin(n\theta)\sim n\theta,\qquad \sin(\theta)\sim \theta
\quad\Rightarrow\quad
[n]_q \to n,
\]
so \( [n]_q! \to n!\).  

Any reasonable implementation should reproduce the undeformed theory at \(\theta=0\).

## 4. Quantum 6j symbols as a θ-dependent recoupling kernel

The project computes (or approximates) a q-deformed \(6j\)-symbol via the **q-Racah formula** schematically:

\[
\begin{Bmatrix}
j_1 & j_2 & j_3\\
j_4 & j_5 & j_6
\end{Bmatrix}_q
\;=\;
\Delta_q(j_1,j_2,j_3)\Delta_q(j_1,j_5,j_6)\Delta_q(j_4,j_2,j_6)\Delta_q(j_4,j_5,j_3)
\;\sum_t
(-1)^t\; \mathcal{R}_q(t),
\]

where each \(\Delta_q\) and the Racah summand \(\mathcal{R}_q(t)\) are ratios of q-factorials.  
The exact expressions are standard in quantum angular momentum theory; the important fact here is:

- **θ enters only through q-factorials**, hence through trigonometric dependence in \([n]_q\).

In code terms, once you have a numerically stable method for q-factorials and the Racah sum, you can build θ-dependent local tensor elements.

## 5. What the code actually establishes (within its model)

Within the implemented tensor-network model:

1. A rank-8 vertex tensor \(T(\theta)\) is assembled whose entries depend on quantum dimensions and quantum \(6j\)-symbols.
2. A (simplified) 4D HOTRG-style contraction produces an estimate of \(\log Z(\theta)\).
3. From that, the project extracts \(F(\theta) := -\Re\log Z(\theta)\) and then estimates \(\chi_{\text{top}}\) by curvature methods.

That is **real progress** if the goal is:

- to build a numerically stable pipeline for \(Z(\theta)\) in a **representation / recoupling** formulation, and
- to validate that the contraction produces a **nontrivial periodic** \(F(\theta)\).

It is **not** (yet) a proof that this model equals continuum Yang–Mills, nor a mass-gap proof.

## 6. Why this hypothesis could be exciting

If Hypothesis H were correct (or correct after modification), it would mean:

- θ-physics could be studied by *category-level deformation* (changing the “fusion rules / recoupling coefficients”),
- which might yield a **sign-problem-mitigated** or structurally controlled tensor-network representation,
- and could connect 4D gauge theory to known quantum-group/topological structures (where rigorous mathematics already exists).

This is not guaranteed—but it is a *clean, falsifiable conjecture*.

## 7. Concrete “next falsification tests” (to avoid repeating work)

1. **Symmetry and orthogonality tests for \(\{6j\}_q\)**: confirm the standard tetrahedral symmetries and Biedenharn–Elliott identity numerically on low spins.
2. **Known solvable limits**:
   - one-plaquette SU(2) integral checks (exact Bessel-function formulas),
   - 2D SU(2) character-expansion models (where tensor methods are well benchmarked).
3. **θ→0 derivative consistency**: compute \(\partial_\theta^2 \log Z(\theta)\vert_{\theta=0}\) in two independent ways (finite difference vs Fourier curvature), verify agreement.
4. **Continuum scaling clues**: if you can extract a correlation length \(\xi(\beta)\) and show \(\xi\to\infty\) at some critical surface, that’s the start of a continuum discussion.

The ethos: *test small, test exact, then scale up*.
