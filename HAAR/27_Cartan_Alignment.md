# 27 — Cartan Alignment and Force Non-Cancellation

## Abstract
We address the "Force Non-Cancellation" problem (**GAP-FC-02**), which is required to prove Lyapunov drift. We identify the **Cartan-aligned configurations** as the only places where the force can vanish despite high energy, and propose a stratification strategy to handle them.

**Connected Files:**
- **[28] Typicality:** Requires the drift proved here.
- **[32] Defect Gas:** Uses the rarity of these alignments.
- **[08] Lyapunov Drift:** The direct consumer of this bound.

---

## 1. The Problem Statement (GAP-FC-02)

*(From source: HAAR/CURATED_05_CartanAlignment_NonCancellation.md)*

We need a lower bound on the force when the action is large:
$$
\mathcal{B}_\Lambda(U) \ge \varepsilon \implies \|\nabla S_\Lambda(U)\| \ge c_0(\varepsilon)
$$
**Obstruction:** The force $\nabla S$ is a sum of vectors. Can they cancel to zero even if individual terms are large?

---

## 2. Local Force Decomposition

At a link $\ell$, the force is a sum over 6 plaquettes:
$$
\nabla_\ell S = \beta \sum_{p \in \mathcal{P}(\ell)} \text{Ad}_{G_p} X_p
$$
where $X_p \in \mathfrak{su}(2) \cong \mathbb{R}^3$ depends on the plaquette angle.

If plaquettes are "rough" ($\vartheta \ge \varepsilon$), then $\|X_p\| \ge c(\varepsilon)$.
Cancellation means $\sum \text{Ad}_{G_p} X_p = 0$.

---

## 3. The Exceptional Set: Cartan Alignment

### 3.1 Definition
A configuration is **Cartan-aligned** at $\ell$ if all incident plaquette holonomies commute:
$$
[U_p, U_{p'}] = 0 \quad \forall p, p' \in \mathcal{P}(\ell)
$$

### 3.2 Implication
In SU(2), commuting matrices share a rotation axis $\hat{n}$.
The vectors $X_p$ become collinear. Cancellation is then an algebraic sum of scalars: $\sum (\pm 1) \sin \theta_p = 0$.
This is much easier to achieve than 3D vector cancellation!

---

## 4. Proposed Solution Strategy

### 4.1 Stratification
The zero set $Z_\ell = \{ U : \nabla_\ell S = 0 \}$ is real-analytic.
We stratify $Z_\ell = \mathcal{A}_\ell \cup \text{Transverse}$.
- **$\mathcal{A}_\ell$ (Aligned):** Handle via detailed "Abelian" analysis (cancellation is rare).
- **Transverse:** Generic cancelation is impossible for 6 independent 3D vectors.

### 4.2 Lojasiewicz Inequality
For analytic maps:
$$
\|\nabla S\| \ge \text{dist}(U, Z_\ell)^k
$$
This gives a quantitative polynomial lower bound on the force away from the exceptional set.

---

## 5. Why It Should Work in 4D

### 5.1 Transversality
In 4D, the 6 plaquettes lie in 3 orthogonal planes.
The transport data is "overdetermined."
Simultaneous alignment requires global geometric conspiracy.

### 5.2 Rarity
Cartan alignment is a high-codimension condition.
The set of aligned configurations has measure zero in the rough region.

---

## Summary

**Cartan Alignment** is the mechanism of "accidental" force stability.
By proving that such alignments are:
1. Rare (high codimension), or
2. Unstable (drift pushes away),
we verify the force lower bound needed for Lyapunov drift.

---

## References
- **Source:** `CURATED_05_CartanAlignment_NonCancellation.md`
- S. Lojasiewicz, *Ensembles semi-analytiques* (1993).
- **GAP-FC-02** in the project roadmap.
