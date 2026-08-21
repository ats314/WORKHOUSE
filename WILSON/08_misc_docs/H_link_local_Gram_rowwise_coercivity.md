# Coercivity of $\langle \nabla S_\Lambda,\nabla V\rangle$: reduction to a link-local Gram row-sum condition

This note specializes the drift obstruction from the Lyapunov calculation to the case
\[
S_\Lambda = S_W + S_H,
\qquad
S_W(U)=\beta\sum_{p\in P(\Lambda)} \widetilde z_p(U),
\qquad
S_H(U)=\sum_{\ell\in E(\Lambda)} H(U_\ell),
\]
(with $H\equiv 0$ allowed), and chooses
\[
V(U)=\sum_{p\in P(\Lambda)} \widetilde z_p(U)^2
\qquad (\Phi(s)=s^2).
\]
It rewrites
\[
\mathcal J(U):=\langle \nabla S_\Lambda(U),\nabla V(U)\rangle
\]
as a sum over links of **weighted Gram row sums**, and reduces the missing coercivity bound
\[
\mathcal J(U)\ \gtrsim\ \sum_p \widetilde z_p(U)
\quad\text{outside a small set}
\]
to a finite-dimensional inequality on $G^m$ with $m\le \nu$.

The essential point: after locality and conjugation-invariance are used, the problem is no longer “infinite volume” but “local cancellation in a fixed finite-dimensional star.”

---

## 1. Standing notation

Let $G=\mathrm{SU}(N)$, $M_\Lambda=G^{E(\Lambda)}$, and
\[
\widetilde z(g)=1-\frac1N\Re\operatorname{Tr}(g)\in[0,2],
\qquad \widetilde z_p(U)=\widetilde z(U_p(U)).
\]
Let $(X_\ell^a)$ be the right-invariant link vector fields, and
\[
\langle \nabla f,\nabla g\rangle
=\sum_{\ell\in E(\Lambda)}\sum_a (X_\ell^a f)(X_\ell^a g).
\]
Define the incidence constant
\[
P(\ell):=\{p\in P(\Lambda):\ell\subset\partial p\},
\qquad \nu:=\max_{\ell}|P(\ell)|.
\]

---

## 2. Explicit linkwise expansion of $\mathcal J=\langle\nabla S_\Lambda,\nabla V\rangle$

Define the linkwise contributions
\[
\mathcal J_\ell(U):=\sum_a (X_\ell^a S_\Lambda)(X_\ell^a V),
\qquad \mathcal J(U)=\sum_{\ell\in E(\Lambda)} \mathcal J_\ell(U).
\]
Split $\mathcal J=\mathcal J^{(W)}+\mathcal J^{(H)}$.

### Lemma 2.1 (first derivatives)
For each $\ell,a$,
\[
X_\ell^a S_W=\beta\sum_{q\in P(\ell)} X_\ell^a\widetilde z_q,
\qquad
X_\ell^a S_H = X_\ell^a H(U_\ell),
\]
and
\[
X_\ell^a V
=\sum_{p\in P(\ell)} 2\widetilde z_p\,X_\ell^a\widetilde z_p.
\]

**Proof.** Locality: if $\ell\notin\partial p$ then $X_\ell^a\widetilde z_p\equiv 0$. Apply the chain rule to $\widetilde z_p^2$. ∎

---

## 3. Gram matrix on a link-star

Fix a link $\ell$ and enumerate its incident plaquettes:
\[
P(\ell)=\{p_1,\dots,p_m\},\qquad m:=|P(\ell)|\le \nu.
\]
Define the link-plaquette gradients
\[
g_{\ell,i}^a(U):=X_\ell^a\widetilde z_{p_i}(U),
\qquad g_{\ell,i}(U):=(g_{\ell,i}^a(U))_a\in\mathbb R^{\dim\mathfrak g}.
\]
Define the linkwise Gram matrix
\[
G_\ell(U)\in\mathbb R^{m\times m},
\qquad (G_\ell)_{ij}(U):=\sum_a g_{\ell,i}^a(U)\,g_{\ell,j}^a(U)
=\langle \nabla_\ell \widetilde z_{p_i},\nabla_\ell \widetilde z_{p_j}\rangle.
\]
Define row sums
\[
r_{\ell,i}(U):=\sum_{j=1}^m (G_\ell)_{ij}(U).
\]
If $S_H$ is present, define also
\[
h_\ell^a(U):=X_\ell^a H(U_\ell),\qquad h_\ell(U):=(h_\ell^a(U))_a,
\]
and the cross-couplings
\[
b_{\ell,i}(U):=\sum_a h_\ell^a(U)\,g_{\ell,i}^a(U)=\langle h_\ell,g_{\ell,i}\rangle.
\]

### Lemma 3.1 (exact Gram row-sum identity)
Let $z_{\ell,i}(U):=\widetilde z_{p_i}(U)$. Then
\[
\boxed{
\mathcal J^{(W)}_\ell(U)=2\beta\sum_{i=1}^m z_{\ell,i}(U)\,r_{\ell,i}(U),
\qquad
\mathcal J^{(H)}_\ell(U)=2\sum_{i=1}^m z_{\ell,i}(U)\,b_{\ell,i}(U).
}
\]
Consequently
\[
\boxed{
\mathcal J(U)
=2\sum_{\ell\in E(\Lambda)}\sum_{i=1}^m z_{\ell,i}(U)\,\big(\beta r_{\ell,i}(U)+b_{\ell,i}(U)\big).
}
\]

**Proof.** Insert Lemma 2.1 into $\mathcal J_\ell=\sum_a (X_\ell^a S)(X_\ell^a V)$ and expand:
\[
\mathcal J_\ell^{(W)}
=\sum_a\Big(\beta\sum_{j}g_{\ell,j}^a\Big)\Big(\sum_i 2z_{\ell,i} g_{\ell,i}^a\Big)
=2\beta\sum_{i,j} z_{\ell,i}\sum_a g_{\ell,i}^a g_{\ell,j}^a
=2\beta\sum_i z_{\ell,i}\sum_j (G_\ell)_{ij}.
\]
The Haar term is analogous. ∎

---

## 4. From local coefficients to global coercivity

Define
\[
D(U):=\sum_{p\in P(\Lambda)} \widetilde z_p(U).
\]
Each plaquette has exactly 4 boundary links, hence
\[
\sum_{\ell\in E(\Lambda)}\sum_{p\in P(\ell)} \widetilde z_p =4D.
\]
Therefore, if one can show that for some $\kappa>0$ and a set $K\subset M_\Lambda$,
\[
\beta r_{\ell,i}(U)+b_{\ell,i}(U)\ \ge\ \kappa\quad\text{for all }\ell,i\text{ whenever }U\notin K,
\]
then outside $K$,
\[
\mathcal J(U)\ge 2\kappa\sum_{\ell}\sum_{p\in P(\ell)}\widetilde z_p(U)=8\kappa\,D(U).
\]
This is the desired coercivity input for the drift.

Thus the problem becomes a **uniform lower bound on the local coefficients**
\[
\beta r_{\ell,i}+b_{\ell,i}.
\]

---

## 5. Finite-dimensional reduction: $r_{\ell,i}$ becomes a row sum $R_i$ on $G^m$

Because $\widetilde z$ is a class function and the metric is bi-invariant, Ad-conjugations arising from how $U_\ell$ enters a plaquette holonomy can be removed by conjugating the plaquette holonomy.

Concretely: for each link-star $(\ell,p_i)$ there exist local group elements $C_{\ell,i}(U)\in G$ (built from the other three links in $\partial p_i$) such that the **link-framed holonomy**
\[
\widehat U_{\ell,i}(U):=C_{\ell,i}(U)^{-1}U_{p_i}(U)C_{\ell,i}(U)\in G
\]
satisfies
\[
X_\ell^a \widetilde z_{p_i}(U)=\big\langle u\big(\widehat U_{\ell,i}(U)\big),\,T^a\big\rangle_{\mathfrak g},
\qquad u(g):=\nabla\widetilde z(g)\in\mathfrak g.
\]
Therefore, for fixed $\ell$, the vectors $g_{\ell,i}$ can be identified with the Lie-algebra vectors $u(g_i)$ where
\[
(g_1,\dots,g_m):=\big(\widehat U_{\ell,1}(U),\dots,\widehat U_{\ell,m}(U)\big)\in G^m.
\]
In particular,
\[
(G_\ell)_{ij}(U)=\langle u(g_i),u(g_j)\rangle_{\mathfrak g},
\qquad
r_{\ell,i}(U)=\sum_{j=1}^m \langle u(g_i),u(g_j)\rangle.
\]
Define the finite-dimensional row sums for $\mathbf g=(g_1,\dots,g_m)\in G^m$:
\[
R_i(\mathbf g):=\sum_{j=1}^m\langle u(g_i),u(g_j)\rangle,
\qquad i=1,\dots,m.
\]
Then
\[
\boxed{\ r_{\ell,i}(U)=R_i\big(\widehat U_{\ell,1}(U),\dots,\widehat U_{\ell,m}(U)\big).\ }
\]
Hence the Wilson-part coercivity is governed entirely by the sign/magnitude structure of these finite-dimensional row sums.

---

## 6. A strictly weaker exceptional set: row-wise negative mass

Let $u_i:=u(g_i)\in\mathfrak g$. Then
\[
R_i=\sum_{j=1}^m\langle u_i,u_j\rangle = |u_i|^2 + \sum_{j\ne i}\langle u_i,u_j\rangle.
\]
Write $x_-:=\max\{-x,0\}$.

### Definition 6.1 (row-wise negative mass)
\[
N_i(\mathbf g):=\sum_{j\ne i}\big(\langle u_i,u_j\rangle\big)_-.
\]

### Lemma 6.2 (row-sum bound)
\[
R_i(\mathbf g)\ \ge\ |u_i|^2 - N_i(\mathbf g).
\]

**Proof.** Drop the nonnegative parts of the off-diagonal sum. ∎

### Corollary 6.3 (row-wise criterion)
If
\[
N_i(\mathbf g)\le \tfrac12|u_i|^2,
\]
then
\[
R_i(\mathbf g)\ge \tfrac12|u_i|^2.
\]

### Definition 6.2 (row-wise exceptional set)
Fix $\sigma>0$. Define
\[
\boxed{
\mathcal K^{\mathrm{row}}_\sigma
:=
\Big\{\min_i |u(g_i)|<\sigma\Big\}
\ \cup\
\Big\{\exists i:\ N_i(\mathbf g)>\tfrac12|u_i|^2\Big\}\ \subset\ G^m.
}
\]

### Proposition 6.4 (uniform lower bound outside $\mathcal K^{\mathrm{row}}_\sigma$)
For every $\mathbf g\in G^m\setminus\mathcal K^{\mathrm{row}}_\sigma$ and every $i$,
\[
\boxed{\ R_i(\mathbf g)\ge \tfrac12|u_i|^2\ge \tfrac12\sigma^2.\ }
\]

**Proof.** Outside $\mathcal K^{\mathrm{row}}_\sigma$, $|u_i|\ge \sigma$ and $N_i\le \tfrac12|u_i|^2$ for all $i$. Apply Corollary 6.3. ∎

**Why this is strictly weaker than pairwise thresholds.** Pairwise exclusions require $\langle u_i,u_j\rangle$ not too negative for every pair. Row-wise exclusion permits a few strongly negative pairs as long as the total negative mass $N_i$ stays below $\tfrac12|u_i|^2$.

---

## 7. What remains (and what does not)

At this point, the coercivity problem has been reduced to the following two tasks:

1. **Finite-dimensional geometry:** understand the critical set $\{u=0\}$ and the behavior of $u(g)=\nabla\widetilde z(g)$ well enough to choose $\sigma$ and characterize $\mathcal K^{\mathrm{row}}_\sigma$ effectively.

2. **Model-specific control (probability/energy):** prove that the actual link-star tuples
\(
\widehat{\mathbf U}_\ell(U)\in G^{m(\ell)}
\)
land in $G^m\setminus \mathcal K^{\mathrm{row}}_\sigma$ outside a global “small set” $K\subset M_\Lambda$ with quantitative tail bounds under $\mu_\Lambda$.

Nothing in this reduction depends on the lattice volume: the obstruction is local cancellation on a fixed star of size $m\le\nu$.
