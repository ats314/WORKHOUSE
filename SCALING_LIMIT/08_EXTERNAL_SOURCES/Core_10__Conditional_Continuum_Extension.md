---
file: Core_10__Conditional_Continuum_Extension.md
status: DRAFT
depends_on:
  - Appendix_A__Notation_and_Constants.md
  - Appendix_L__OS_Reconstruction_and_Gap_Extraction.md
  - Appendix_M__Continuum_Permanence_Interfaces.md
  - Appendix_N__External_Inputs_Ledger.md
  - Core_9__Thermodynamic_Limit_and_OS_Gap_at_Fixed_Cutoff.md
feeds_into:
  - Core Manuscript (conditional continuum mass-gap statement)
---

# Core-10 — Conditional continuum extension along a scaling trajectory

## Core-10.0 Output and contract

**Definition Core-10.0.1 (purpose).**  
This file records a *conditional* continuation of the fixed-cutoff gap statement (Theorem **Core-9.5.5**) along a sequence of cutoffs `a_n\downarrow 0`. The file is organized as two explicit interfaces:

1. **Euclidean interface (reflection positivity permanence):** a projective-limit construction of a limiting Euclidean state, with reflection positivity verified on cylinder observables via Appendix **M.1**.
2. **Hamiltonian interface (gap permanence):** a monotone quadratic-form limit construction of a limiting self-adjoint operator, with a persistent spectral gap verified via Appendix **M.2** and **External Input M.2.7**.

No claim is made here about the existence of the scaling limit or about uniformity of the fixed-cutoff gap bound along that limit; these are isolated as explicit assumptions below.

**Definition Core-10.0.2 (exported statement).**  
The exported conclusion is the conditional continuum gap statement:

- **Theorem Core-10.4.1**: under the hypotheses of Sections **Core-10.1–Core-10.3**, the limiting operator `H_\infty` has a spectral gap bounded below by a strictly positive constant `m_0`, in the sense of Definition **L.4.5**.

---

## Core-10.1 Scaling trajectory and fixed-cutoff gap inputs

### Core-10.1.1 Trajectory data

**Definition Core-10.1.1 (scaling trajectory).**  
A **scaling trajectory** is a sequence
\[
(a_n,\beta_n)_{n\ge 1}
\quad\text{with}\quad
a_n\in(0,\infty),\ a_n\downarrow 0,
\qquad
\beta_n\in(0,\infty),
\tag{10.1}
\]
where `a` is the cutoff parameter of Definition **A.1.2** and `\beta` is the Wilson coupling parameter (Definition **A.6.4**).

**Definition Core-10.1.2 (fixed-cutoff OS Hamiltonians along a trajectory).**  
For each `n\ge 1`, let `\mu_{\infty,n}` be an infinite-volume thermodynamic limit point at cutoff `a_n` and coupling `\beta_n` in the sense of Definition **Core-9.2.1** (with the parameters `a,\beta` replaced by `a_n,\beta_n`). Let `H_n` denote the associated OS Hamiltonian as in Theorem **Core-9.5.5** (constructed by External Input **L.2.6** and Definition **L.2.8**).

Let
\[
\mathcal K_n := \ker(H_n)\subseteq \mathcal H_{\mathrm{OS},n}
\tag{10.2}
\]
denote the (possibly nontrivial) vacuum subspace at scale `n`.

### Core-10.1.2 Fixed-cutoff gap along the trajectory

**Assumption Core-10.1.3 (fixed-cutoff gap bound available at every scale).**  
For every `n\ge 1`, the hypotheses of Theorem **Core-9.5.5** hold for the pair `(\mu_{\infty,n},a_n)` with exponent
\[
\eta_{\star,n}
\quad\text{defined exactly as in Definition Core-9.0.2 (formula (9.1)), but with }\beta=\beta_n.
\tag{10.3}
\]
Equivalently, for each `n`, the resulting OS Hamiltonian `H_n` obeys the fixed-cutoff spectral-gap bound
\[
\sigma(H_n)\cap\bigl(0,\eta_{\star,n}/a_n\bigr)=\emptyset
\qquad\text{(in the sense of Theorem Core-9.5.5).}
\tag{10.4}
\]

**Assumption Core-10.1.4 (uniform physical mass lower bound along the trajectory).**  
There exists a constant
\[
m_0>0
\tag{10.5}
\]
such that for all `n\ge 1`,
\[
\frac{\eta_{\star,n}}{a_n}\ \ge\ m_0.
\tag{10.6}
\]
(Equivalently: `\inf_n \eta_{\star,n}/a_n \ge m_0`.)

---

## Core-10.2 Euclidean scaling limits: reflection positivity on cylinder observables

This section isolates the Euclidean-state part of a continuum extension. It does not invoke any OS reconstruction in the limit; it only records which hypotheses guarantee that reflection positivity survives the passage to a scaling-limit measure on cylinder observables.

### Core-10.2.1 Projective system hypotheses

**Assumption Core-10.2.1 (projective system of OS data along the trajectory).**  
There exists a directed index set `I` and a cofinal sequence `(i_n)_{n\ge 1}\subset I` such that:

1. For each `i\in I`, there is an OS datum
   \[
   (\Omega_i,\mathcal F_i,\mu_i,\Theta_i,\{\tau_k^{\Omega_i}\}_{k\in\mathbb Z},\mathcal A_{i,+})
   \tag{10.7}
   \]
   in the sense of Definition **M.1.1**.

2. For each `i\preceq j` in `I`, there is a measurable map `P_{j\to i}:\Omega_j\to\Omega_i` such that the collection
   \[
   \bigl\{(\Omega_i,\mu_i,\Theta_i,\mathcal A_{i,+}),\ P_{j\to i}\bigr\}_{i\preceq j}
   \tag{10.8}
   \]
   satisfies the projective-system conditions of Definition **M.1.5** (projective compatibility, reflection equivariance, positive-time compatibility, and measure consistency).

3. For each `n`, the OS datum at level `i_n` encodes the infinite-volume fixed-cutoff Euclidean state `\mu_{\infty,n}` from Definition **Core-10.1.2** in the sense that:
   - the measure component `\mu_{i_n}` is identified with `\mu_{\infty,n}` (up to a relabeling of underlying configuration spaces);
   - the reflection `\Theta_{i_n}` and positive-time algebra `\mathcal A_{i_n,+}` agree with those used in Theorem **Core-9.5.5** for `\mu_{\infty,n}`.

No further compatibility is imposed in this file.

**Assumption Core-10.2.2 (existence of a projective-limit measure).**  
There exists a measurable space `(\Omega_\infty,\mathcal F_\infty)`, measurable maps `\pi_i:\Omega_\infty\to\Omega_i` forming a projective cone as in Definition **M.1.6**, and a probability measure `\mu_\infty` on `\Omega_\infty` satisfying the consistency condition of Assumption **M.1.7**:
\[
(\pi_i)_\#\mu_\infty = \mu_i
\qquad\forall i\in I.
\tag{10.9}
\]
Moreover, there exists a measurable involution `\Theta_\infty:\Omega_\infty\to\Omega_\infty` such that
\[
\pi_i\circ\Theta_\infty = \Theta_i\circ\pi_i
\qquad\forall i\in I.
\tag{10.10}
\]

### Core-10.2.2 Consequence: cylinder reflection positivity

**Proposition Core-10.2.3 (reflection positivity for the projective-limit state on cylinder observables).**  
Under Assumptions **Core-10.2.1–Core-10.2.2**, let `\mathcal A_{\infty,+}^{\mathrm{cyl}}` be the cylinder positive-time algebra defined in Proposition **M.1.8**:
\[
\mathcal A_{\infty,+}^{\mathrm{cyl}}
:=
\{\widetilde F\circ\pi_i:\ i\in I,\ \widetilde F\in\mathcal A_{i,+}\}.
\tag{10.11}
\]
Then `\mu_\infty` is reflection positive on `\mathcal A_{\infty,+}^{\mathrm{cyl}}`, i.e.
\[
\mu_\infty\big((\theta_\infty F)F\big)\ge 0
\qquad\forall\,F\in\mathcal A_{\infty,+}^{\mathrm{cyl}},
\tag{10.12}
\]
where `\theta_\infty` is induced by `\Theta_\infty` as in Definition **L.1.5**.

*Proof.* This is exactly Proposition **M.1.8**, applied to the projective system and limit data of Assumptions **Core-10.2.1–Core-10.2.2**. ∎

---

## Core-10.3 Hamiltonian scaling limits: gap permanence via monotone quadratic forms

This section isolates a **sufficient** operator-theoretic interface ensuring that a uniform fixed-cutoff gap bound (in physical units) survives the passage to a limiting operator.

### Core-10.3.1 Spectral gap implies a uniform form inequality

**Lemma Core-10.3.1 (gap ⇒ quadratic-form coercivity above the vacuum sector).**  
Let `\mathcal H` be a Hilbert space and let `H\ge 0` be a self-adjoint operator on `\mathcal H`. Let
\[
\mathcal K := \ker(H),
\qquad
P_{\mathcal K}:\mathcal H\to\mathcal K
\tag{10.13}
\]
denote the vacuum subspace and its orthogonal projection.

Assume that for some `\Delta>0`,
\[
\sigma(H)\cap(0,\Delta)=\emptyset.
\tag{10.14}
\]
Then the quadratic form `q_H(\psi):=\|H^{1/2}\psi\|^2` obeys, for all `\psi\in D(H^{1/2})`,
\[
q_H(\psi)\ \ge\ \Delta\,\|(I-P_{\mathcal K})\psi\|^2.
\tag{10.15}
\]

*Proof.*  
Let `E_H` be the spectral measure of `H`. For `\psi\in D(H^{1/2})`, define the finite measure
\[
\nu_\psi(B):=\langle \psi, E_H(B)\psi\rangle,
\]
on Borel sets `B\subset[0,\infty)`. Then
\[
q_H(\psi)=\langle \psi, H\psi\rangle = \int_{[0,\infty)} \lambda\, d\nu_\psi(\lambda),
\tag{10.16}
\]
and
\[
\|(I-P_{\mathcal K})\psi\|^2
=\langle \psi, E_H((0,\infty))\psi\rangle
= \nu_\psi((0,\infty)).
\tag{10.17}
\]
The spectral-gap assumption (10.14) implies that `\nu_\psi` is supported on `{0}\cup[\Delta,\infty)`. Therefore,
\[
\int_{[0,\infty)} \lambda\, d\nu_\psi(\lambda)
\ge
\int_{[\Delta,\infty)} \lambda\, d\nu_\psi(\lambda)
\ge
\Delta\,\nu_\psi([\Delta,\infty))
=
\Delta\,\nu_\psi((0,\infty)),
\]
which is exactly (10.15) by (10.16)–(10.17). ∎

### Core-10.3.2 Monotone form limit interface

**Assumption Core-10.3.2 (common Hilbert space and monotone approximating forms).**  
There exist:

- a Hilbert space `\mathcal H_\infty`;
- a closed subspace `\mathcal K_\infty\subseteq\mathcal H_\infty`;
- a dense linear subspace `\mathcal D_0\subseteq\mathcal H_\infty`;

and a sequence of nonnegative quadratic forms `(q_n)_{n\ge 1}` on `\mathcal H_\infty` such that the hypotheses of Assumption **M.2.4** hold with `(\mathcal H,\mathcal K,\mathcal D_0,q_n)=(\mathcal H_\infty,\mathcal K_\infty,\mathcal D_0,q_n)`.

In particular, on the common core `\mathcal D_0`:

1. `q_n` is monotone nondecreasing in `n`;
2. `q_n(\psi)=0` for all `\psi\in\mathcal D_0\cap\mathcal K_\infty`;
3. the pointwise supremum
   \[
   q_\infty(\psi):=\sup_{n\ge 1} q_n(\psi)
   \qquad(\psi\in\mathcal D_0)
   \tag{10.18}
   \]
   is well-defined in `[0,\infty]`.

**Assumption Core-10.3.3 (uniform form gap bound inherited from fixed-cutoff gaps).**  
With the same constant `m_0>0` as in Assumption **Core-10.1.4**, one has the uniform coercivity bound
\[
q_n(\psi)\ \ge\ m_0\,\|(I-P_{\mathcal K_\infty})\psi\|^2
\qquad\forall\,\psi\in\mathcal D_0,\ \forall\,n\ge 1.
\tag{10.19}
\]
(One sufficient way to verify (10.19) is to construct `q_n` as transported OS Hamiltonian forms from the fixed-cutoff Hamiltonians `H_n` and apply Lemma **Core-10.3.1** together with (10.4)–(10.6); this construction is not performed in this file.)

**Assumption Core-10.3.4 (closability and closed limit form).**  
The form `q_\infty|_{\mathcal D_0}` is closable, and its closure `\overline q_\infty` is a densely defined closed nonnegative quadratic form on `\mathcal H_\infty` with form core `\mathcal D_0` (Definition **M.2.2**).

### Core-10.3.3 Consequence: limiting operator has a spectral gap

**Proposition Core-10.3.5 (gap permanence under monotone form limits).**  
Assume **Core-10.3.2–Core-10.3.4**. Let `H_\infty\ge 0` be the unique self-adjoint operator associated with the closed form `\overline q_\infty` by **External Input M.2.7** (Appendix M). Then
\[
\sigma(H_\infty)\ \subseteq\ \{0\}\ \cup\ [m_0,\infty),
\tag{10.20}
\]
and in particular `\mathrm{gap}(H_\infty)\ge m_0` in the sense of Definition **L.4.5**.

*Proof.*  
Assumption **Core-10.3.3** is exactly Assumption **M.2.5** with `\Delta=m_0`, and Assumption **Core-10.3.2** supplies Assumption **M.2.4**. Therefore Proposition **M.2.6** yields the form inequality
\[
\overline q_\infty(\psi)\ \ge\ m_0\,\|(I-P_{\mathcal K_\infty})\psi\|^2
\qquad\forall\,\psi\in D(\overline q_\infty).
\tag{10.21}
\]
Apply **External Input M.2.7** to represent `\overline q_\infty` by `H_\infty` and to transfer (10.21) into the operator/spectral conclusion. Concretely, Corollary **M.2.9** gives (10.20) and the gap bound. ∎

---

## Core-10.4 Conditional continuum mass-gap statement

**Theorem Core-10.4.1 (conditional continuum mass gap along a scaling trajectory).**  
Assume:

1. *(Fixed-cutoff mass-gap along the trajectory.)* Assumptions **Core-10.1.3–Core-10.1.4** hold, producing the uniform physical lower bound `m_0>0`.

2. *(Existence of a continuum Euclidean state with reflection positivity on cylinder observables.)* Assumptions **Core-10.2.1–Core-10.2.2** hold, and hence Proposition **Core-10.2.3** applies.

3. *(Existence of a limiting Hamiltonian as a monotone closed-form limit.)* Assumptions **Core-10.3.2–Core-10.3.4** hold, so that `H_\infty` is defined and Proposition **Core-10.3.5** applies.

Then `H_\infty` has a spectral gap of size at least `m_0` above its vacuum sector `\mathcal K_\infty`:
\[
\sigma(H_\infty)\cap(0,m_0)=\emptyset,
\qquad\text{i.e.}\qquad
\mathrm{gap}(H_\infty)\ge m_0
\ \ \text{(Definition L.4.5).}
\tag{10.22}
\]

*Proof.* Immediate from Proposition **Core-10.3.5**. ∎

---

## Core-10.5 Dependency and conditionality ledger

**Definition Core-10.5.1 (proved vs. assumed vs. external).**

- **Proved in this file:** Lemma **Core-10.3.1**, Proposition **Core-10.2.3**, Proposition **Core-10.3.5**, Theorem **Core-10.4.1**.

- **Assumptions (conditional hypotheses) in this file:** Assumptions **Core-10.1.3–Core-10.1.4** (uniform availability of fixed-cutoff gaps and a uniform physical lower bound), Assumptions **Core-10.2.1–Core-10.2.2** (existence of a projective-limit Euclidean state), and Assumptions **Core-10.3.2–Core-10.3.4** (common Hilbert space and monotone closed-form limit).

- **External inputs used in this file:** **External Input M.2.7** (representation of closed forms), as registered in Appendix **N** (Definition **N.0.3**). No other external inputs are invoked.

**Definition Core-10.5.2 (what remains open after Core-10).**  
After Core-10 is in place, any unconditional continuum mass-gap theorem along a cutoff-removal trajectory requires, at minimum, discharging the `Assumption`-tagged hypotheses in this file, most notably:
- constructing a projective-limit Euclidean state satisfying the reflection-positivity compatibility conditions of Appendix **M.1** along the chosen trajectory, and
- constructing a limiting Hamiltonian `H_\infty` as a closed-form limit satisfying the monotonicity/coercivity conditions of Appendix **M.2** with a strictly positive uniform constant `m_0`.

No additional analytic ingredients beyond the fixed-cutoff chain (Core-1 through Core-9) and the permanence interfaces (Appendix M) enter the statement of Theorem **Core-10.4.1**.
