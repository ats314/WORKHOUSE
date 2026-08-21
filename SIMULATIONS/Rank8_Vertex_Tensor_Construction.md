# Rank-8 Vertex Tensor Construction for 4D SU(2) via \(U_q(\mathfrak{su}(2))\) Recoupling

This document extracts and formalizes the project’s most characteristic construction:
a **rank-8 vertex tensor** for a 4D hypercubic lattice built out of

- representation weights \(w_j(\beta)\),
- sums over intermediate fusion channels,
- and \(q\)-deformed 6j-symbols \(\{6j\}_q\) with \(q=e^{i\theta}\).

It is *not* presented in the notebooks as a fully proven equivalence to the Wilson-\(\theta\) lattice action.
Rather, it is the project’s concrete **state-sum ansatz** for encoding \(\theta\) locally.

---

## 1. Kinematics: spins and truncation

Choose a spin cutoff \(j_{\max}\) and allowed spins
\[
j \in \left\{0,\tfrac12,1,\tfrac32,\ldots,j_{\max}\right\}.
\]
Let \(D\) be the number of allowed spins. Each tensor index \(i\in\{0,\ldots,D-1\}\) maps to a spin \(j(i)\).

---

## 2. Representation weights

The notebooks use a simple Casimir-based weight
\[
w_j(\beta) \equiv e^{-\beta\, j(j+1)}.
\]

Interpretation:
- This resembles the **heat-kernel action** weight in representation space, where the quadratic Casimir \(C_2(j)=j(j+1)\) governs the suppression of higher spins.
- It is also a numerically convenient proxy when building a truncated tensor network.

---

## 3. The rank-8 tensor: an explicit recoupling ansatz

A 4D hypercubic vertex is 8-valent (four directions, two orientations), motivating a tensor
\[
T_{i_1 i_2 i_3 i_4 i_5 i_6 i_7 i_8}(\beta,\theta).
\]

The project constructs it schematically as:

1. Multiply weights for each incident spin,
2. Sum over an intermediate channel \(k\),
3. Insert \(q\)-deformed 6j-symbols as the recoupling “interaction”.

A representative formula consistent with the implementation is:

\[
T_{j_1\ldots j_8}(\beta,\theta)
=
\Big(\prod_{a=1}^8 w_{j_a}(\beta)\Big)
\sum_{k\in \mathcal{J}} w_{k}(\beta)\;
\left\{\begin{matrix}
j_1 & j_2 & k\\
j_3 & j_4 & k
\end{matrix}\right\}_q
\left\{\begin{matrix}
j_5 & j_6 & k\\
j_7 & j_8 & k
\end{matrix}\right\}_q,
\qquad q=e^{i\theta},
\]
where \(\mathcal{J}=\{0,\tfrac12,\ldots,j_{\max}\}\).

### Selection rules

Each 6j-symbol enforces triangle constraints implicitly. In code, triangle checks are applied to avoid computing invalid recouplings.

---

## 4. Normalization and “log partition bookkeeping”

Raw tensors can grow/shrink exponentially under contraction and truncation.
The project therefore normalizes at construction time:

- compute a norm scale
  \[
  \lambda = \max |T_{j_1\ldots j_8}|,
  \]
- rescale \(T \leftarrow T/\lambda\),
- and store \(\log\lambda\) for later reconstruction of \(\log Z\).

This is tracked across HOTRG steps in a running accumulator (called a “coherence budget” in the code).

---

## 5. HOTRG-like contraction step (simplified)

Given a rank-8 tensor \(T\) with bond dimension \(D\), reshape into a matrix
\[
M \in \mathbb{C}^{D^4 \times D^4}
\quad\text{via}\quad
M_{(i_1,i_2,i_3,i_4),(i_5,i_6,i_7,i_8)} := T_{i_1\ldots i_8}.
\]

Then perform an SVD
\[
M = U S V^\dagger,
\]
truncate to \(\chi\) singular values, reconstruct
\[
M^{(\chi)} = U_{[:,1:\chi]} \, S_{1:\chi} \, V^\dagger_{[1:\chi,:]},
\]
and reshape back to rank-8.

Finally renormalize again and add the log normalization to the accumulator.

This is a computational, not axiomatic, HOTRG step—but it captures the project’s core contraction strategy.

---

## 6. Extracting \(Z(\theta)\) and \(F(\theta)\)

After several coarse-graining steps, the contraction is approximated by a trace-like scalar
\[
Z(\theta)\approx e^{\sum_s \log\lambda_s}\;\mathrm{Tr}(T_{\text{final}}).
\]

The project typically reports the “free energy” as
\[
F(\theta) \equiv -\mathrm{Re}\,\log Z(\theta),
\]
and then studies \(F(\theta)\) across \(\theta\in[0,2\pi)\).

---

## 7. Why this construction is interesting (and what it is *not*)

### Interesting
- It is a **local, tensor-network realizable** way to introduce \(\theta\)-dependence through well-structured algebraic data (\(U_q(\mathfrak{su}(2))\) recoupling).
- It naturally interfaces with HOTRG and GPU acceleration ideas in later notebooks.
- It suggests a bridge between 4D lattice gauge theory and quantum-group categorical state sums.

### Not yet proven
- It is not (yet) derived from the Wilson-\(\theta\) action as an exact reformulation.
- Gauge constraints (Gauss law) and plaquette structure are represented only schematically in this simplified vertex form.
- The mapping \(q=e^{i\theta}\) should be treated as a **hypothesis** pending validations.

---

## 8. Immediate “next derivation” targets

To upgrade this from an ansatz to a controlled theory:

1. Derive the vertex tensor from an explicit **character expansion** of a chosen lattice action (heat kernel / Wilson) and show precisely where the recoupling coefficients enter.

2. Identify the object in the state sum that corresponds to the **integer topological charge** \(Q\).  
   If a categorical or combinatorial “charge” emerges, one can attempt to prove:
   \[
   Z(\theta)=\sum_Q Z_Q e^{i\theta Q}.
   \]

3. Clarify how \(q\)-deformation modifies that decomposition.  
   This is where the big-theory connection would either crystallize… or politely collapse.
