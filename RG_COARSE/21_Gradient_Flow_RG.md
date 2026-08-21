# 21 — Gradient Flow as Geometric RG

## Abstract
We reinterpret the **Yang-Mills Gradient Flow (Wilson Flow)** as an exact, deterministic Renormalization Group transformation on the configuration manifold. This provides the continuous link between the UV (lattice scale) and the IR (confinement scale), serving as the vehicle for the "Glue-and-Rescale" proof strategy.

**Connected Files:**
- **[06] Riccati:** The scalar flow equation.
- **[30] PBH Flow:** The tensor flow equation.
- **[10] Gap Transfer:** How the gap evolves.

---

## 1. The Gradient Flow Equation

*(From source: HAAR/Selection_G_Gradient_Flow_as_Geometric_RG_for_Lattice_YM.md)*

### 1.1 Lattice Definition
Let $V \in G^{|E|}$ be the link variables. The flow is an ODE:
$$
\partial_t V_t = - g_0^2 \nabla_{V_t} S_W(V_t), \quad V_0 = V
$$
This smooths the configuration, damping high-frequency noise.

### 1.2 The Induced Measure
Define the effective action $S_t$ by the pushforward of the Gibbs measure:
$$
e^{-S_t(V')} = \int \delta(V' - V_t(V)) e^{-S_0(V)} dV
$$
This is an **exact geometric coarse-graining**.

---

## 2. The Evolution Equation (Geometric FRG)

### 2.1 The PDE for $S_t$
Differentiating the pushforward identity yields a Hamilton-Jacobi-Bellman type equation:
$$
\partial_t S_t = \|\nabla S_t\|^2 - \Delta S_t + \dots
$$
- **Drift Term:** $\|\nabla S\|^2$ (Contractive).
- **Diffusion Term:** $-\Delta S$ (Expansive/Entropic).

### 2.2 Connection to Ricci Flow
This flow on the *potential* $S$ induces a flow on the *effective metric* of the moduli space, closely related to **Perelman's Ricci Flow**.
The mass gap corresponds to the stability of the manifold against collapse.

---

## 3. The "Glue-and-Rescale" Strategy

### 3.1 Step 1: Smooth
Run flow for time $t \sim 1$.
The configurations become $C^\infty$ smooth.
Dislocations and defects annihilate.

### 3.2 Step 2: Rescale
Rescale the lattice $a \to 2a$.
The surviving degrees of freedom form the effective coarse-grid action.

### 3.3 Step 3: Check Curvature
Verify that if $\text{Hess}(S_0) \ge c_0 I$, then $\text{Hess}(S_t) \ge c_t I$ with $c_t > 0$.
(See File [06] Riccati).

---

## 4. Why Use Gradient Flow?

1. **Gauge Covariance:** The flow preserves gauge symmetry exactly at finite $t$.
2. **Renormalizability:** Lüscher proved that gradient flow observables are automatically renormalized.
3. **Topology:** It preserves the topological charge sector (for small $t$), allowing us to study $\theta$-vacua.

---

## 5. Next Steps

1. **Write the Exact PDE:** Explicitly on $SU(N)$.
2. **Prove Stability:** Show $\text{Hess}(S_t)$ stays positive for short times.
3. **Define Lyapunov:** Use the flow time $t_{\text{hit}}$ as a Lyapunov function for the drift argument.

---

## Summary

Gradient Flow is the **Time** in the "Space-Time" of the Renormalization Group.
$$
RG = \text{Flow}_t \circ \text{Decimation}
$$

---

## References
- **Source:** `Selection_G_Gradient_Flow_as_Geometric_RG_for_Lattice_YM.md`.
- M. Lüscher, *Properties and uses of the Wilson flow in lattice QCD* (2010).
