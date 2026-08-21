# 18 — Mosco Convergence: The Continuum Limit

## Abstract
We develop the **Mosco Convergence** framework to define the continuum limit of the Yang-Mills Dirichlet forms. We define a common "Core Hilbert Space," show how lattice approximations converge in the Mosco sense, and prove that Mosco convergence preserves spectral gaps. This is the rigorous definition of "the limit $a \to 0$ exists."

**Connected Files:**
- **[21] Gradient Flow:** Provides the smoothing map for the recovery sequence.
- **[10] RG One-Step:** The discrete version of scale change.
- **[37] Gap Dictionary:** Connects Dirichlet form convergence to mass stability.

---

## 1. The Problem: What is the Continuum Limit?

### 1.1 The Naive Picture
"Take lattice spacing $a \to 0$ and hope the theory converges."

**Why it's hard:**
1. The Hilbert space $L^2(G^{|E|})$ changes dimension as $a \to 0$.
2. The action $S_a$ and measure $\mu_a$ both depend on $a$.
3. There is no fixed "target" to converge to.

### 1.2 The Mosco Answer
Mosco convergence is a mode of convergence for **quadratic forms** on **varying Hilbert spaces**.
It captures the idea: "The energy landscapes converge."

---

## 2. Formal Definition

### 2.1 Setup
Let $(\mathcal{H}_n, \mathcal{E}_n)$ be a sequence of:
- Hilbert spaces $\mathcal{H}_n$.
- Closed quadratic forms (Dirichlet forms) $\mathcal{E}_n: \mathcal{D}(\mathcal{E}_n) \to [0, \infty]$.

### 2.2 Embedding
Assume there is a common "ambient" Hilbert space $\mathcal{H}$ with embeddings $J_n: \mathcal{H}_n \hookrightarrow \mathcal{H}$.
(For example, $\mathcal{H} = L^2(\text{continuum})$ and $J_n$ extends lattice functions by interpolation.)

### 2.3 Mosco Convergence
$\mathcal{E}_n \xrightarrow{M} \mathcal{E}$ if:

**(M1) Lower Bound:** For any sequence $u_n \rightharpoonup u$ (weakly in $\mathcal{H}$):
$$
\mathcal{E}(u) \le \liminf_{n \to \infty} \mathcal{E}_n(u_n)
$$

**(M2) Recovery Sequence:** For any $u \in \mathcal{D}(\mathcal{E})$, there exists $u_n \to u$ (strongly in $\mathcal{H}$) with:
$$
\mathcal{E}_n(u_n) \to \mathcal{E}(u)
$$

---

## 3. Why Mosco Implies Gap Stability

### 3.1 Spectral Theorem for Forms
Each $\mathcal{E}_n$ has an associated self-adjoint operator $L_n$ with:
$$
\mathcal{E}_n(u, v) = \langle L_n^{1/2} u, L_n^{1/2} v \rangle
$$

### 3.2 Spectral Gap
The gap is:
$$
\lambda_1(\mathcal{E}_n) = \inf\left\{ \mathcal{E}_n(u) : \|u\|=1, \langle u, \Omega \rangle = 0 \right\}
$$

### 3.3 Gap Continuity
**Theorem (Kuwae-Shioya):** If $\mathcal{E}_n \xrightarrow{M} \mathcal{E}$, then:
$$
\lambda_1(\mathcal{E}_n) \to \lambda_1(\mathcal{E})
$$

**Corollary:** If $\lambda_1(\mathcal{E}_n) \ge m^2 > 0$ uniformly, then $\lambda_1(\mathcal{E}) \ge m^2$.

---

## 4. The Yang-Mills Application

### 4.1 The Lattice Dirichlet Form
On lattice $\Lambda_a$ with spacing $a$:
$$
\mathcal{E}_a(f) = \int |\nabla f|^2 + V(U) |f|^2 \, d\mu_a
$$
where $|\nabla f|^2$ is the gradient with respect to group variables.

### 4.2 The Continuum Dirichlet Form
Formally:
$$
\mathcal{E}(f) = \int_{\mathcal{A}/\mathcal{G}} |Df|^2_{H^1} + V(\Omega) |f|^2 \, d\mu
$$
where $\mathcal{A}/\mathcal{G}$ is the (still-to-be-defined) continuum orbit space.

### 4.3 The Challenge
We must construct $\mathcal{E}$ as the Mosco limit of $\mathcal{E}_a$.
This requires:
1. **Uniform coercivity:** $\mathcal{E}_a(f) \ge c \|f\|^2$ uniformly in $a$.
2. **Compactness:** From any sequence $\{f_a\}$ with $\mathcal{E}_a(f_a) \le C$, extract a convergent subsequence.

---

## 5. Constructing the Recovery Sequence

### 5.1 The Strategy
Given a smooth continuum field $A$:
1. Run **Gradient Flow (File [21])** for time $\epsilon$ to smooth.
2. Discretize the smoothed field to lattice $\Lambda_a$.
3. The lattice energy $\mathcal{E}_a(A_a)$ converges to the continuum energy.

### 5.2 Why Flow is Needed
Without smoothing, discretization introduces aliasing errors.
The flow kills UV modes that would corrupt the energy.

### 5.3 The Double Limit
Take $a \to 0$ first, then $\epsilon \to 0$.
(Or choose $\epsilon(a) \to 0$ slowly enough.)

---

## 6. Verification on Gaussian

### 6.1 The Free Field
$$
\mathcal{E}_a(\phi) = \sum_x \frac{1}{2}(\nabla_a \phi(x))^2 + \frac{1}{2} m^2 \phi(x)^2
$$
where $\nabla_a$ is the lattice gradient.

### 6.2 Fourier Analysis
Eigenvalues of $-\Delta_a + m^2$:
$$
\lambda_k = m^2 + \frac{4}{a^2} \sum_\mu \sin^2\left(\frac{k_\mu a}{2}\right)
$$

As $a \to 0$: $\lambda_k \to m^2 + k^2$.

Gap: $\lambda_{\min} = m^2$ (independent of $a$). $\checkmark$

### 6.3 Mosco Convergence
The lattice Laplacians $\Delta_a$ Mosco-converge to $\Delta$.
The spectrum converges pointwise.

---

## 7. Non-Perturbative Challenges

### 7.1 UV Renormalization
In 4D Yang-Mills, the bare coupling $g(a)$ runs with $a$.
The form $\mathcal{E}_a$ must be defined with the **renormalized** action.

### 7.2 Gauge Fixing
The continuum orbit space $\mathcal{A}/\mathcal{G}$ is singular.
We work on the Gribov region (convex, polar boundary).

### 7.3 Fermionic Determinant
For full QCD, the fermion determinant adds a measure factor.
This is non-local and complicates the form analysis.

---

## Summary

Mosco convergence is the mathematically rigorous framework for "the continuum limit exists":
1. It doesn't require a fixed Hilbert space.
2. It preserves spectral gaps.
3. It is verified for free fields and expected for Yang-Mills.

Proving Mosco convergence for Yang-Mills would establish:
$$
\boxed{m_{phys} = \lim_{a \to 0} \frac{\lambda_1(a)}{a} > 0}
$$

---

## References
- U. Mosco, *Composite media and asymptotic Dirichlet forms* (1994).
- K. Kuwae, T. Shioya, *Convergence of spectral structures* (2003).
- **File [21]** (Gradient Flow) for the recovery construction.
- **File [10]** (RG) for the discrete analogue.
