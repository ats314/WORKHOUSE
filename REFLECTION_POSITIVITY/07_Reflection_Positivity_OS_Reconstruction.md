# 07 — Reflection Positivity and OS Reconstruction

## Abstract
We derive the **Osterwalder-Schrader (OS) Reconstruction** theorem, which rigorously constructs the physical Hilbert space and Hamiltonian from the Euclidean path integral. We prove the **Reflection Positivity** property for the Wilson action, construct the transfer matrix, and show how exponential clustering in Euclidean time directly implies the Hamiltonian mass gap.

**Connected Files:**
- **[05] Combes-Thomas:** Proves the Euclidean correlation decay.
- **[19] Bridge Inequality:** The technical link from diffusion gap to transfer gap.
- **[37] Gap Dictionary:** Translates between Euclidean and Hamiltonian languages.

---

## 1. The Problem: From Path Integral to Quantum Mechanics

### 1.1 The Euclidean Path Integral
We have a well-defined probability measure $\mu$ on field configurations:
$$
d\mu(U) = \frac{1}{Z} e^{-S(U)} \prod_\ell dU_\ell
$$
This defines **correlation functions**:
$$
\langle \mathcal{O}_1 \cdots \mathcal{O}_n \rangle = \int \mathcal{O}_1(U) \cdots \mathcal{O}_n(U) d\mu(U)
$$

### 1.2 The Goal
Construct:
1. A **Hilbert space** $\mathcal{H}$ of physical states.
2. A positive **Hamiltonian** $H \ge 0$ with $H|\Omega\rangle = 0$ (ground state).
3. **Operators** $\hat{\mathcal{O}}$ corresponding to observables.

Such that:
$$
\langle \mathcal{O}_1(0) \mathcal{O}_2(t) \rangle = \langle \Omega | \hat{\mathcal{O}}_1 e^{-tH} \hat{\mathcal{O}}_2 | \Omega \rangle
$$

### 1.3 Why This Is Non-Trivial
The path integral is over a space of **classical** field configurations.
Quantum mechanics requires a **Hilbert space** with complex amplitudes and unitary evolution.
The bridge between them is **Reflection Positivity**.

---

## 2. Reflection Positivity

### 2.1 The Time Reflection
Let spacetime be $\Lambda = \Sigma \times \mathbb{Z}$ where $\Sigma$ is spatial and $\mathbb{Z}$ is discrete time.

Define the time reflection:
$$
\theta: (x, t) \mapsto (x, -t)
$$

Extend to fields: $(\theta U)_{(x,t),\mu} = U_{(x,-t),\mu}^\dagger$ (for time-like links).

### 2.2 The Positive and Negative Half-Spaces
- **Future:** $\Lambda_+ = \Sigma \times \{0, 1, 2, \ldots\}$
- **Past:** $\Lambda_- = \Sigma \times \{\ldots, -2, -1, 0\}$
- **Time-zero slice:** $\Sigma_0 = \Sigma \times \{0\}$

Let $\mathcal{A}_+$ be the algebra of observables supported on $\Lambda_+$.

### 2.3 The OS Inner Product
For $A, B \in \mathcal{A}_+$, define:
$$
\langle A, B \rangle_{OS} := \langle \theta(A)^* B \rangle_\mu
$$

### 2.4 The Positivity Condition
**Definition:** A measure $\mu$ is **Reflection Positive** if:
$$
\langle A, A \rangle_{OS} = \langle \theta(A)^* A \rangle \ge 0 \quad \forall A \in \mathcal{A}_+
$$

This says: The bilinear form $\langle \cdot, \cdot \rangle_{OS}$ is positive semi-definite.

---

## 3. Proof of Reflection Positivity for Wilson Action

### 3.1 Decomposition of the Action
The Wilson action splits as:
$$
S(U) = S_-(U) + S_+(U) + S_0(U)
$$
where:
- $S_+(U)$: Plaquettes in $\Lambda_+$ (future).
- $S_-(U)$: Plaquettes in $\Lambda_-$ (past).
- $S_0(U)$: Plaquettes crossing time zero.

Key observation: $S_-(U) = S_+(\theta U)$ by the reflection symmetry of the action.

### 3.2 The Time-Zero Links
The plaquettes in $S_0$ involve "time-zero links" connecting the two halves.
For the temporal plaquette at $(x, 0)$:
$$
U_p = U_{(x,0),0} U_{(x,1),i} U_{(x,0),0}^\dagger U_{(x,0),i}
$$

The key is the **temporal link** $U_{(x,0),0}$.

### 3.3 Gaussian Representation
The crucial step: The Wilson action for a single plaquette can be written as:
$$
e^{\beta \text{Tr}(U_p + U_p^\dagger)/N} = \int K(U_p, V) dV
$$
where $K$ is a positive kernel (using character expansion or heat kernel).

This shows that $e^{-S_0}$ acts as a **positive definite kernel** connecting past and future.

### 3.4 The Positivity Proof
For $A \in \mathcal{A}_+$:
$$
\langle \theta(A)^* A \rangle = \int \overline{A(\theta U)} A(U) e^{-S(U)} dU
$$
$$
= \int \overline{A(\theta U)} e^{-S_-(U)} K(U_0, U_0') A(U) e^{-S_+(U)} dU
$$

Since $K \ge 0$ and the integral has the form $\int \overline{f} K g$, this is positive. $\square$

---

## 4. Construction of the Hilbert Space

### 4.1 The Null Space
Define:
$$
\mathcal{N} = \{ A \in \mathcal{A}_+ : \langle A, A \rangle_{OS} = 0 \}
$$

Elements of $\mathcal{N}$ are "null states".

### 4.2 The Pre-Hilbert Space
$$
\mathcal{D} = \mathcal{A}_+ / \mathcal{N}
$$
equipped with the inner product $\langle \cdot, \cdot \rangle_{OS}$.

### 4.3 The Physical Hilbert Space
$$
\mathcal{H} = \overline{\mathcal{D}}
$$
(Completion with respect to the OS norm.)

### 4.4 The Vacuum
The function $\Omega \equiv 1$ (constant function) is in $\mathcal{A}_+$.
Its image in $\mathcal{H}$ is the **ground state** $|\Omega\rangle$.

---

## 5. The Transfer Matrix and Hamiltonian

### 5.1 Time Translation
The shift operator $\tau: t \mapsto t+1$ acts on observables:
$$
(\tau A)(U) = A(\tau^{-1} U)
$$

This induces an operator $T$ on $\mathcal{H}$.

### 5.2 Properties of $T$
1. **Self-adjoint:** $\langle A, T B \rangle_{OS} = \langle T A, B \rangle_{OS}$ (by symmetry).
2. **Positive:** $\langle A, T A \rangle_{OS} \ge 0$ (by reflection positivity).
3. **Contraction:** $0 \le T \le I$ (by transfer matrix bounds).

### 5.3 The Hamiltonian
Since $T$ is positive and bounded, we can define:
$$
H = -\frac{1}{a} \log T
$$
where $a$ is the lattice spacing in the time direction.

Properties:
- $H \ge 0$ (since $T \le I$).
- $H |\Omega\rangle = 0$ (since $T |\Omega\rangle = |\Omega\rangle$ by translation invariance).

---

## 6. From Correlation Decay to Mass Gap

### 6.1 The Two-Point Function
Consider $\mathcal{O}$ localized at time 0 with $\langle \mathcal{O} \rangle = 0$.
The two-point correlation at time separation $t$ is:
$$
C(t) = \langle \theta(\mathcal{O}) \mathcal{O}(t) \rangle = \langle \Omega | \hat{\mathcal{O}} e^{-tH} \hat{\mathcal{O}} | \Omega \rangle
$$

### 6.2 Spectral Decomposition
Insert a complete set of energy eigenstates $|n\rangle$ with $H|n\rangle = E_n |n\rangle$:
$$
C(t) = \sum_n |\langle \Omega | \hat{\mathcal{O}} | n \rangle|^2 e^{-t E_n}
$$

### 6.3 Long-Time Behavior
As $t \to \infty$, the sum is dominated by the lowest non-vacuum state ($n=1$):
$$
C(t) \sim |\langle \Omega | \hat{\mathcal{O}} | 1 \rangle|^2 e^{-t E_1}
$$

### 6.4 The Mass Gap
If correlations decay exponentially:
$$
C(t) \sim e^{-mt}
$$
then the **mass gap** is:
$$
m = E_1 - E_0 = E_1
$$

**Theorem:** Euclidean clustering $\Longleftrightarrow$ Hamiltonian mass gap.

---

## 7. Connection to Previous Results

### 7.1 The Chain of Implications
1. **Matrix Hinge (File [03]):** $\text{Ric}_\mu \succeq m^2 I + \ldots$
2. **HS Covariance (File [04]):** $\text{Cov}(F,G) \le C e^{-\mu|x-y|}$
3. **Combes-Thomas (File [05]):** Spatial decay rate $\mu$.
4. **OS Reconstruction (This File):** Spatial decay $\Rightarrow$ Temporal decay $\Rightarrow$ Mass gap.

### 7.2 The Bridge Inequality (File [19])
The remaining step is connecting the **diffusion gap** (spectral gap of $L$) to the **transfer gap** (spectral gap of $I-T$).
This requires kernel comparison: $T \approx e^{-aL}$ for small $a$.

---

## 8. Example: Free Field

### 8.1 Setup
Let $\phi$ be a scalar field with action $S = \frac{1}{2}(\nabla \phi)^2 + \frac{1}{2}m^2 \phi^2$.

### 8.2 Transfer Matrix
The kernel is Gaussian:
$$
T(\phi_0, \phi_1) \propto e^{-\frac{1}{2a}|\phi_1 - \phi_0|^2 - \frac{a m^2}{2}|\phi_0|^2}
$$

### 8.3 Spectrum of $H$
The eigenvalues are $E_n = \omega(n + 1/2)$ where $\omega = \sqrt{m^2 + k^2}$ (harmonic oscillator).

Mass gap: $E_1 - E_0 = \omega \ge m$.

---

## Summary

Reflection Positivity is the "magic" that turns statistical mechanics into quantum mechanics:
1. It provides a **positive inner product** on the space of observables.
2. It constructs a **Hilbert space** of physical states.
3. It defines a **Hamiltonian** with $H \ge 0$.
4. It shows that **Euclidean decay = Hamiltonian gap**.

This is the rigorous foundation for extracting physics from lattice simulations.

---

## References
- K. Osterwalder, R. Schrader, *Axioms for Euclidean Green's functions I, II* (1973, 1975).
- J. Glimm, A. Jaffe, *Quantum Physics: A Functional Integral Point of View* (1987).
- **File [19]** (Bridge Inequality) for the remaining step.
- **File [37]** (Dictionary) for translation between languages.
