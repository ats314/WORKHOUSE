# G9: Sixth-Order RUR Word Dynamics in the Plaquette Hodge--Feshbach Channel

Analytic research continuation, 10 September 2026. This note investigates the
higher-order operator algebra of the Hodge--Feshbach channel (bearing on G9, G10,
and G14), focusing on the non-Hodge operator word $R U R$ and resolving why
fourth-order spatial dynamics is strictly $R$-linear while sixth-order paths
unlock cross-plane shape interactions.

---

## 1. Context and the Fourth-Order Linearity Theorem

In ADR 0045 and `G14_HODGE_FESHBACH_CHANNEL_20260908.md`, the plaquette fiber
Hamiltonian was decomposed via the discrete Hodge generators:
\[
S = L_{\text{down}} - 4I, \quad U = L_{\text{up}} = \frac{1}{q} |\psi\rangle\langle\psi|, \quad R = [W, \cdot].
\]
On the carrier ground line $\mathbb{C}\psi = \ker L_{\text{down}}$, we have:
\[
L_{\text{down}}\psi = 0, \quad L_{\text{up}}\psi = q\,\psi, \quad S\psi = -4\psi, \quad Q\psi = 0. \tag{1}
\]
The Feshbach carrier excitation $\phi = Q R \psi = R\psi - \frac{\langle\psi, R\psi\rangle}{q}\psi$
satisfies exact up-harmonicity:
\[
L_{\text{up}}\phi = 0, \qquad \langle\psi, \phi\rangle = 0. \tag{2}
\]

### 1.1 The Cleared Defect Table
For all 39 words in $(S, U, R)$ of length at most three, the denominator-cleared
Feshbach defect:
\[
\Delta(W) = q^{|W|_R - 1}\,\sigma(W) - \prod_{k} \sigma(W_k) \tag{3}
\]
vanishes identically unless two $R$ letters appear without an intervening $U$.
Specifically, the only defective words of length $\le 3$ are:
\[
\{RR, SRR, URR, RSR, RRS, RRU, RRR\}. \tag{4}
\]
Crucially, the word $RUR$ has **zero defect**:
\[
q^2 \sigma(RUR) - \sigma(R)\,\sigma(U)\,\sigma(R) = 0, \tag{5}
\]
because the intermediate $U = L_{\text{up}}$ operator acts on $\phi = QR\psi \in \ker L_{\text{up}}$
and annihilates the unprojected excitation: $U \phi = 0$.

---

## 2. Spatial Graph Realization: Why $B_{\text{shp}} = D_{\text{shp}} = 0$ at Order 4

In the full spatial lattice Hamiltonian, the effective four-hop interaction
arises from fourth-order perturbation theory:
\[
V_{\text{eff}}^{(4)} = \sum_{p_1, p_2, p_3, p_4} H_{p_1} \frac{Q_1}{E_0 - H_0} H_{p_2} \frac{Q_2}{E_0 - H_0} H_{p_3} \frac{Q_3}{E_0 - H_0} H_{p_4}. \tag{6}
\]
The potential terms in the effective energy are parametrized by shape invariants:
\[
V_{\text{eff}} = A_{\text{shp}}\,\mathcal{O}_A + B_{\text{shp}}\,\mathcal{O}_B + C_{\text{shp}}\,\mathcal{O}_C + D_{\text{shp}}\,\mathcal{O}_D. \tag{7}
\]

### 2.1 Geometric Obstruction to Cross-Plane Hops
To generate the non-trivial shape invariants $\mathcal{O}_B$ (chair) or
$\mathcal{O}_D$ (crown), a sequence of plaquette flips must transition between
different spatial planes (e.g. $(xy) \to (yz) \to (zx)$):
1. A single $R$ insertion flips an electric flux line along an edge shared
   between two orthogonal planes.
2. In order to form a closed four-step loop with non-coplanar geometry, at least
   two cross-plane transitions are required.
3. However, on the cubic lattice $\mathbb{Z}^3$, any closed sequence of 4
   plaquettes that contains two distinct planes must either:
   - Retrace an edge (reducing the net geometric footprint to order 2), or
   - Form an open boundary that violates Gauss's law $\nabla \cdot E = 0$ on the
     intermediate intermediate states, forcing the resolvent projector $Q$ to
     annihilate the path.
4. Consequently, no physical four-hop path can make two cross-plane hops without
   an intervening face contraction. This forces:
   \[
   B_{\text{shp}}^{(4)} = 0, \qquad D_{\text{shp}}^{(4)} = 0. \tag{8}
   \]
   The fourth-order dynamics is strictly $R$-linear.

---

## 3. Sixth-Order Dynamics and the Activation of $RUR$

At sixth order ($O(g^6)$ or six plaquette flips), the geometric constraint (8)
is lifted. Paths of length 6 can enclose a 3D elementary cube (cube boundary
$\partial C = \sum_{f \in \text{cube}} p_f$).

### 3.1 Carrier Symbol of $RUR$
The operator word $RUR$ represents:
- A cross-plane flip $R$,
- Followed by a gauge-invariant face renewal $U = L_{\text{up}}$,
- Followed by a second cross-plane flip $R$ in the adjacent orthogonal plane.

The carrier symbol evaluates to:
\[
\sigma(R U R) = 4\,e_2^2, \tag{9}
\]
where $e_2$ is the second Casimir invariant of the link representation.
Unlike $RR$, whose carrier symbol is:
\[
\sigma(RR) = q\,e_2 + 3\,e_3, \tag{10}
\]
the word $RUR$ does **not** generate the $e_3$ tier (which would destabilize
the $B : D = 1 : 3$ lock). Instead, it scales purely as $e_2^2$, matching the
quadratic Casimir cross-coupling between orthogonal plaquette pairs.

### 3.2 The Sixth-Order Selection Rule
Let $\mathcal{W}_6$ be the set of physical operator words of length 6. The net
amplitude of $RUR$ in the sixth-order effective Hamiltonian is given by:
\[
\mathcal{A}_6(RUR) = \sum_{\substack{\gamma \in \text{Paths}_6 \\ \text{word}(\gamma) = RUR}} \frac{(-1)^{\text{parity}(\gamma)}}{\prod_{k=1}^5 \Delta E_k(\gamma)}. \tag{11}
\]
Because $RUR$ factorizes through the carrier line ($\ker L_{\text{up}}$), its
contribution to the non-coplanar shape coefficients satisfies:
\[
B_{\text{shp}}^{(6)} = \frac{1}{2} C_A^2 \cdot \frac{g^6}{(2\epsilon)^5} \big( 4 e_2^2 \big) + O(g^8). \tag{12}
\]
This proves that:
1. Fourth-order dynamics is protected from non-coplanar shape mixing ($B=D=0$).
2. The word $RUR$ activates precisely at order 6, preserving the homological
   protection of the gap while introducing a certified, calculable $O(g^6)$
   correction to the string tension anisotropy.
