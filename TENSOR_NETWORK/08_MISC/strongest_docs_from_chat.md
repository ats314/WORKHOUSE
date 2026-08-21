# Strongest Documents Extracted From This Chat (Markdown + LaTeX)

This is a curated set of the **most reusable, highest-signal documents** that emerged during our conversation, rewritten as clean standalone references.

---

## Document 1 — Ground Truth Reference: SU(2) 6j Sanity Checks

### 1.1 Conventions
We assume the **standard Wigner 6j** normalization used by common references (and by `sympy.physics.wigner.wigner_6j`).

A Wigner 6j symbol is written:
\[
\begin{Bmatrix}
j_1 & j_2 & j_3\\
j_4 & j_5 & j_6
\end{Bmatrix}.
\]

### 1.2 “Do Not Proceed If These Fail” Test Values
These are small-spin, high-value regression tests. If your implementation disagrees, fix *that* before touching tensor networks.

\[
\begin{Bmatrix}
\frac12 & \frac12 & 1\\
\frac12 & \frac12 & 1
\end{Bmatrix}
= \frac{1}{6}
\approx 0.1666666667
\]

\[
\begin{Bmatrix}
\frac12 & \frac12 & 0\\
\frac12 & \frac12 & 0
\end{Bmatrix}
= -\frac{1}{2}
= -0.5
\]

\[
\begin{Bmatrix}
1 & 1 & 1\\
1 & 1 & 1
\end{Bmatrix}
= \frac{1}{6}
\approx 0.1666666667
\]

### 1.3 What These Catch
- Wrong Racah phase convention (e.g. missing or incorrect \((-1)^{\cdot}\)).
- Incorrect factorial/gamma handling for half-integers.
- Silent triangle-inequality bugs (terms that should be zero).
- Wrong “expected value” myths (e.g. confusing \(1/\sqrt{6}\) with \(1/6\)).

---

## Document 2 — χ\_top Extraction: Definitions, Positivity, and the Fit You Should Use

### 2.1 Definitions
Given a θ-dependent partition function \(Z(\theta)\), define free energy:
\[
F(\theta) = -\log Z(\theta).
\]
Topological susceptibility:
\[
\chi_{\mathrm{top}} := \left.\frac{\partial^2 F(\theta)}{\partial \theta^2}\right|_{\theta=0}.
\]

### 2.2 When χ\_top Must Be Nonnegative
If \(Z(\theta)\) is the **characteristic function** of a real random variable \(Q\) (topological charge),
\[
Z(\theta) = \mathbb{E}\left[e^{i\theta Q}\right],
\]
then
\[
F(\theta) = -\log Z(\theta)
\quad\Rightarrow\quad
\chi_{\mathrm{top}} = \mathrm{Var}(Q)\ge 0.
\]
So **negative \(\chi_{\mathrm{top}}\)** usually indicates one of:
- \(Z(\theta)\) is not a valid characteristic function (unphysical or incorrectly normalized),
- \(F(\theta)\) was not computed consistently from \(Z(\theta)\),
- the fit/extraction method is wrong for your sampling scheme,
- or your “θ insertion” is not a mathematically consistent θ-term.

### 2.3 Fourier-Series Formula (Most General)
If \(F(\theta)\) is even and \(2\pi\)-periodic,
\[
F(\theta)=a_0+\sum_{n\ge1} a_n \cos(n\theta),
\]
then
\[
\chi_{\mathrm{top}} = F''(0) = -\sum_{n\ge1} n^2 a_n.
\]

### 2.4 Minimal Practical Fit Used in the Chat
A common reduced ansatz used in the discussion was:
\[
F_{\mathrm{fit}}(\theta)=c_0 + c_1\cos(2\theta)+c_2\cos(4\theta).
\]
Then
\[
\chi_{\mathrm{top}} = F_{\mathrm{fit}}''(0)= -4c_1 -16c_2.
\]

**Actionable rule:** if your fitted \(\chi_{\mathrm{top}}\) is negative, check whether your fitted coefficients have the sign structure required by a valid \(Z(\theta)\), and whether your θ-dependence is derived from the model rather than imposed.

---

## Document 3 — q-Deformed SU(2) 6j: Definition + Stable Log-Space Evaluation

This is a clean spec (not a proof) of the q-6j evaluation algorithm we converged on.

### 3.1 q-Number and q-Factorial
Let \(q=e^{i\theta}\), and define for **integer** \(n\ge 0\):
\[
[n]_q=\frac{\sin(n\theta)}{\sin\theta}.
\]
Then
\[
[n]_q! = \prod_{k=1}^{n} [k]_q,\qquad [0]_q!=1.
\]

### 3.2 q-Triangle Coefficient
For admissible half-integer spins \(a,b,c\) (triangle inequalities + \(a+b+c\in\mathbb{Z}\)),
\[
\Delta_q(a,b,c)=
\sqrt{
\frac{
[a+b-c]_q!\,[a-b+c]_q!\,[-a+b+c]_q!
}{
[a+b+c+1]_q!
}
}.
\]

### 3.3 q-Racah Formula
Define:
\[
\begin{Bmatrix}
j_1 & j_2 & j_3\\
j_4 & j_5 & j_6
\end{Bmatrix}_q
=
\Delta_q(j_1,j_2,j_3)\Delta_q(j_1,j_5,j_6)\Delta_q(j_4,j_2,j_6)\Delta_q(j_4,j_5,j_3)
\;\sum_{t=t_{\min}}^{t_{\max}} (-1)^t\,\frac{[t+1]_q!}{\prod_{k=1}^{7}[n_k(t)]_q!},
\]
with the standard Racah denominator arguments:
\[
\begin{aligned}
n_1(t)&=t-(j_1+j_2+j_3),&
n_2(t)&=t-(j_1+j_5+j_6),&
n_3(t)&=t-(j_4+j_2+j_6),\\
n_4(t)&=t-(j_4+j_5+j_3),&
n_5(t)&=(j_1+j_2+j_4+j_5)-t,\\
n_6(t)&=(j_1+j_3+j_4+j_6)-t,&
n_7(t)&=(j_2+j_3+j_5+j_6)-t.
\end{aligned}
\]
The sum includes only integer \(t\) such that all \(n_k(t)\ge 0\).

### 3.4 **Correct Numeric Strategy**
Key principle: the Racah expression is a sum of oscillatory complex amplitudes.  
You **must not** sum logs.

Compute each term as:
- \( \log|[n]_q!|\) and \(\arg([n]_q!)\) in log-space,
- build
\[
\log |T_t| = \log|[t+1]_q!|-\sum_{k=1}^7\log|[n_k(t)]_q!|
\]
and
\[
\phi_t = \arg([t+1]_q!) - \sum_{k=1}^7 \arg([n_k(t)]_q!) + \pi t,
\]
then construct the complex term
\[
T_t = \exp(\log|T_t|)\,e^{i\phi_t},
\]
and finally sum:
\[
\sum_t T_t.
\]

### 3.5 Special Points
- As \(\theta\to 0\), \([n]_q\to n\) and \(\{6j\}_q\to \{6j\}\).
- At \(\theta\to \pi\), \([n]_q\) has removable singular behavior for integer n, but implementation must handle the limit carefully.

---

## Document 4 — The “Manus Quadratic Fit” Audit Checklist

A key lesson from the chat: a notebook can “work” and still be **synthetic**.

### 4.1 The Red Flag Pattern
If a code defines:
\[
F(\theta) := F_0 + \tfrac12 \chi \theta^2
\]
for some heuristic \(\chi\), then samples \(F(\theta)\) and fits a quadratic to recover \(\chi\), it is not *computing* \(\chi\). It is **self-fulfilling**.

### 4.2 How to Detect It Quickly
Ask:
1. Does θ enter the tensor network weights/tensors **before** contraction?
2. Is \(Z(\theta)\) actually recomputed (or reweighted) for each θ?
3. Is \(\chi_{\mathrm{top}}\) derived from \(F(\theta)\) that came from those θ-dependent contractions?

If θ never enters the TN and \(F(\theta)\) is constructed by fiat, then you are testing only:
- the fitting pipeline,
- not the physics.

### 4.3 How to Upgrade It
To make the pipeline physically meaningful, replace the synthetic step with:
- a model where \(Z(\theta)\) is explicitly computable as a sector sum  
  \[
  Z(\theta)=\sum_Q Z_Q e^{i\theta Q}
  \]
  with \(Z_Q\ge 0\) from a sign-problem-free TN representation; then
  \[
  \chi_{\mathrm{top}} = \frac{\langle Q^2\rangle - \langle Q\rangle^2}{V}.
  \]
This is straightforward in some models (e.g. 1D rotor, 2D U(1)), and is the correct place to validate the χ extraction machinery.

---

## Document 5 — The Linear Roadmap That Prevents Thrash

### Stage A — Kernel Infrastructure (No Physics Claims)
**Goal:** a correct, tested \(6j\) kernel and a tensor generator that runs.

Definition of done:
- small-spin 6j tests pass (Document 1),
- tensor generation runs for small \(J_{\max}\) without OOM,
- contraction/compression is numerically stable (finite outputs).

### Stage B — First Physics Anchor (2D model with external checks)
**Goal:** a minimal model with an observable you can verify.

Definition of done:
- build a 2D TN for a known theory (or one with checkable small-lattice integrals),
- compute \(Z\) on \(1\times 1\) and \(2\times 2\),
- match an independent calculation (analytic or brute-force integration).

### Stage C — Add θ / q-Deformation
**Goal:** θ-dependence that is derived, not imposed.

Definition of done:
- validate \(F(\theta)\) periodicity and smoothness,
- extract \(\chi_{\mathrm{top}}\) and verify \(\chi_{\mathrm{top}}\ge 0\) when it should be,
- only then attempt scale-up to 4D constructions.

---

## Document 6 — Compact Fusion-Model Prompt That Actually Moves the Work

> **Task:** Given a θ-dependent free energy \(F(\theta)=-\log Z(\theta)\) produced by a TN contraction, design and implement an extraction of \(\chi_{\mathrm{top}} = F''(0)\) that is robust to sampling noise.  
> Requirements:
> 1. Provide the minimal Fourier/quadratic fit that respects \(2\pi\)-periodicity and evenness.  
> 2. Provide a positivity diagnostic (when χ must be ≥ 0).  
> 3. Provide a “synthetic θ” detector (Document 4).  
> Output must be: explicit formulas + code snippets + pass/fail checks for a given set of sampled \(F(\theta)\) points.

---

*End of curated documents.*
