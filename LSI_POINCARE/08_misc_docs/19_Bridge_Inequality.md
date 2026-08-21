# 19 — The Bridge Inequality

## Abstract
The **Bridge Inequality** is the critical step linking the Diffusive Spectral Gap ($\lambda_{diff}$) to the Hamiltonian Mass Gap ($\gamma_T$). We present the precise statement, the one-step comparison theorem, and discuss proof strategies.

**Connected Files:**
- **[09] Local-to-Global:** Gives us $\lambda_{diff}$.
- **[07] OS Reconstruction:** Uses $\gamma_T$ to get physical mass.
- **[20] Protocols:** Numerical verification.
- **[16] Pipeline:** The primary bottleneck.

---

## 1. The Statement

### 1.1 The Two Objects
- **Diffusion gap $\lambda_{diff}$:** Spectral gap of Langevin generator $L$ on time-zero slice.
- **Transfer gap $\gamma_T$:** $1 - \lambda_1(T)$ where $T = e^{-H}$ is the Euclidean transfer matrix.

### 1.2 The Desired Inequality
$$
\boxed{\gamma_T \ge C \cdot a \cdot \lambda_{diff}}
$$
for some $C > 0$ uniform in lattice size.

---

## 2. The One-Step Comparison Theorem

*(From source: BEST_03_diffusion_to_OS_bridge.md)*

### 2.1 Hypotheses
**(H1) Time-zero representation:** Isometric embedding $J: L^2(\mu_\Sigma) \to \mathcal{H}_{OS}$ with $J\mathbf{1}$ = vacuum.

**(H2) Intertwining:** $T J = J K$ for some Markov contraction $K$ on $L^2(\mu_\Sigma)$.

**(H3) The Key Comparison (★):** For mean-zero $f$:
$$
\boxed{\langle f, (I-K)f \rangle \ge c \cdot \mathcal{E}_L(f,f)}
\tag{★}
$$

### 2.2 Conclusions
From (H1)-(H3):

1. **Spectral gap for $K$:**
$$\text{spec}(K) \setminus \{1\} \subseteq (-\infty, 1 - c\lambda_{diff}]$$

2. **OS mass gap:**
$$\Delta_{OS} = \inf(\text{spec}(H) \setminus \{0\}) \ge -\log(1 - c\lambda_{diff}) \ge c\lambda_{diff}$$

3. **Correlation decay:**
$$|\langle Jf, T^n Jf \rangle| \le e^{-n\Delta_{OS}} \|f\|_2^2$$

---

## 3. Proof of the Main Theorem

### 3.1 Spectral Argument
On $L^2_0(\mu_\Sigma)$ (mean-zero):
$$
\langle f, (I-K)f \rangle \ge c \mathcal{E}_L(f,f) \ge c\lambda_{diff} \|f\|_2^2
$$

This forces $I - K \succeq c\lambda_{diff} I$, hence:
$$
K \preceq (1 - c\lambda_{diff}) I
$$

### 3.2 Transfer to OS
Since $T = e^{-H}$ and $TJ = JK$:
$$
\Delta_{OS} = -\log(\text{max eigenvalue of } K|_{perp}) \ge -\log(1 - c\lambda_{diff})
$$

---

## 4. Why (★) Is the Bottleneck

### 4.1 Gaussian Case
For harmonic oscillator with $V = \frac{1}{2}\omega^2 x^2$:
- $K = e^{-\omega}$ (exact)
- $\mathcal{E}_L(f,f) = \omega \|f\|_2^2$ (for eigenfunctions)
- (★) holds with $c = 1/\omega$

### 4.2 Non-Gaussian Perturbations
The challenge is controlling:
- Non-commutativity: $[S_{kin}, S_{pot}] \ne 0$
- Baker-Campbell-Hausdorff corrections
- Gauge-theoretic commutators

### 4.3 Current State
- **Rigorous:** Gaussian case, strong coupling limit.
- **Numerical:** Verified on small lattices.
- **Open:** General proof for non-Abelian at weak coupling.

---

## 5. Alternative Strategies

### 5.1 Direct Hamiltonian Construction
Skip diffusion; construct $H$ via canonical quantization.
**Challenge:** Gauge fixing and renormalization.

### 5.2 Reflection Positivity Bootstrap
Use RP to bound $H$ directly from Euclidean correlations.
**Challenge:** Still need the input $\lambda_{diff}$.

### 5.3 Computer-Assisted Proof
Verify (★) on $2^4, 4^4$ lattices with interval arithmetic.
Extrapolate via finite-size scaling.
**Challenge:** Exponential cost in dimension.

---

## 6. The Physical Meaning

The Bridge says:
> **Diffusion in configuration space controls time evolution in Hilbert space.**

This is the rigorous version of:
- "Equilibrium statistical mechanics ↔ Ground state quantum mechanics"
- "Euclidean decay ↔ Minkowski gap"

---

## Summary

The Bridge Inequality is **the** critical gap:
$$
\text{Everything Before} \xrightarrow{?} \text{Everything After}
$$

Proving (★) would complete the Clay Millennium Problem.

---

## References
- B. Simon, *Functional Integration and Quantum Physics* (1979).
- M. Lüscher, *Construction of a self-adjoint Hamiltonian for LGT* (1977).
- **Source:** `BEST_03_diffusion_to_OS_bridge.md` (168 lines).
