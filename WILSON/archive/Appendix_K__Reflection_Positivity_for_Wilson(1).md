---
file: Appendix_K__Reflection_Positivity_for_Wilson.md
status: DRAFT
depends_on:
  - Appendix_A__Notation_and_Constants.md
feeds_into:
  - Core-3 (OS framework at fixed cutoff: reflection positivity input)
  - Core-9 (Thermodynamic limit at fixed cutoff: structural axiom permanence uses finite-volume RP)
  - Appendix_L__OS_Reconstruction_and_Gap_Extraction.md
---

# Appendix K — Reflection positivity for the Wilson lattice gauge measure

## K.0 Scope and outputs

**Definition K.0.1 (scope).**  
This appendix proves **finite-volume Osterwalder–Schrader reflection positivity** for the Wilson Gibbs measure `\mu_{\Lambda_L,\beta}` (Definition A.6.5) on the periodic lattice `\Lambda_L` (Definition A.1.3), with respect to a fixed reflection across a Euclidean time hyperplane.

**Definition K.0.2 (main output).**  
The main output is Theorem K.5.1: for every bounded cylinder observable `F` depending only on positive-time link variables, one has
\[
\mathbb E_{\Lambda_L,\beta}\big[(\theta F)\,F\big]\ge 0,
\]
with the OS involution `\theta` induced by the configuration reflection `\Theta` defined below.

**Definition K.0.3 (no additional axioms).**  
This appendix does **not** address OS reconstruction (transfer operator, Hilbert space completion) nor the Euclidean-time-to-Hamiltonian gap conversion. Those appear in Appendix L.

**Definition K.0.4 (no new named constants).**  
This appendix introduces no named constants. All parameters (`d=4`, `\beta>0`, `n`, etc.) and all underlying objects (`G`, `\rho`, `\Lambda_L`, `M_{\Lambda_L}`, `S_{\Lambda_L,\beta}`, `\mu_{\Lambda_L,\beta}`) are as fixed in Appendix A.

---

## K.1 Reflection datum on the periodic lattice

Throughout this appendix:
- the dimension is `d=4` (Definition A.1.1), with Euclidean time direction `0`;
- the periodic lattice is `\Lambda_L=\prod_{\mu\in\mathsf I_d}(\mathbb Z/L_\mu\mathbb Z)` (Definition A.1.3);
- configurations are `U\in M_{\Lambda_L}=G^{E(\Lambda_L)}` (Definition A.4.1).

### K.1.1 Time reflection on vertices

**Assumption K.1.1 (even temporal extent).**  
The temporal side length `L_0` is even.

**Definition K.1.2 (vertex reflection across a mid-plane).**  
Write a vertex as `x=(x_0,\vec x)` with `x_0\in \mathbb Z/L_0\mathbb Z` and `\vec x\in \prod_{\mu=1}^3(\mathbb Z/L_\mu\mathbb Z)`.  
Define the reflection `\vartheta:V(\Lambda_L)\to V(\Lambda_L)` by
\[
\vartheta(x_0,\vec x):=(1-x_0,\vec x),
\]
where subtraction is in `\mathbb Z/L_0\mathbb Z`.

**Lemma K.1.3 (involution).**  
`\vartheta` is an involution: `\vartheta^2=\mathrm{Id}`.

*Proof.* For any `x_0`, `\vartheta(\vartheta(x_0,\vec x))=(1-(1-x_0),\vec x)=(x_0,\vec x)`. ∎

**Definition K.1.4 (positive/negative time slices).**  
Let `T:=L_0/2\in\mathbb N`. Using the standard representatives `\{0,1,\dots,L_0-1\}` for time coordinates, define
\[
T_+ := \{1,2,\dots,T\},
\qquad
T_- := \{0,L_0-1,L_0-2,\dots,T+1\}.
\]
Define the corresponding vertex subsets
\[
\Lambda_+ := \{x\in\Lambda_L: x_0\in T_+\},
\qquad
\Lambda_- := \{x\in\Lambda_L: x_0\in T_-\}.
\]

**Lemma K.1.5 (partition and reflection exchange).**  
One has `\Lambda_L=\Lambda_+\sqcup\Lambda_-` and `\vartheta(\Lambda_+)=\Lambda_-`.

*Proof.* The time sets `T_+` and `T_-` are disjoint and cover `\{0,1,\dots,L_0-1\}`. By Definition K.1.2, `\vartheta` maps time `t` to `1-t`, which bijects `T_+` and `T_-`. ∎

### K.1.2 Directed links and configuration reflection

The Wilson action uses plaquette holonomies, which are naturally expressed in terms of **directed** edges. We work with a directed-edge extension of the configuration.

**Definition K.1.6 (directed link set and endpoints).**  
Let `E(\Lambda_L)` be the positively oriented link set (Definition A.2.2). Define the directed link set
\[
\widetilde E(\Lambda_L):=\{b, b^{-1}: b\in E(\Lambda_L)\}.
\]
For a directed link `b\in\widetilde E(\Lambda_L)`, define its initial and terminal vertices `\partial_-b,\partial_+b\in V(\Lambda_L)` by:
- if `b=(x,\mu)\in E(\Lambda_L)`, then `\partial_-b:=x` and `\partial_+b:=x+\hat e_\mu`;
- if `b=b_0^{-1}` with `b_0\in E(\Lambda_L)`, then `\partial_-b:=\partial_+b_0` and `\partial_+b:=\partial_-b_0`.

**Definition K.1.7 (directed extension of a configuration).**  
Given `U\in M_{\Lambda_L}=G^{E(\Lambda_L)}`, extend it to a map on directed links (still denoted `U`) by
\[
U_{b^{-1}}:=U_b^{-1},\qquad b\in E(\Lambda_L).
\]

**Definition K.1.8 (reflection on directed links).**  
Define `\vartheta:\widetilde E(\Lambda_L)\to \widetilde E(\Lambda_L)` by
\[
\vartheta(b):=(\vartheta(\partial_-b)\to \vartheta(\partial_+b)),
\qquad b\in\widetilde E(\Lambda_L),
\]
i.e. apply the vertex reflection to the endpoints.

**Lemma K.1.9 (compatibility with inversion and involution).**  
For all directed links `b\in\widetilde E(\Lambda_L)`,
\[
\vartheta(b^{-1})=(\vartheta b)^{-1},
\qquad
\vartheta^2(b)=b.
\]

*Proof.* The endpoint map swaps under inversion by definition, and `\vartheta` is an involution on vertices (Lemma K.1.3). ∎

**Definition K.1.10 (configuration reflection).**  
Define `\Theta:M_{\Lambda_L}\to M_{\Lambda_L}` by pullback along `\vartheta` on directed links:
\[
(\Theta U)_b := U_{\vartheta b},\qquad b\in E(\Lambda_L),
\]
where the right-hand side uses the directed extension (Definition K.1.7).

**Lemma K.1.11 (`\Theta` is an involution on configurations).**  
`\Theta^2=\mathrm{Id}` on `M_{\Lambda_L}`.

*Proof.* For `b\in E(\Lambda_L)`, using Lemma K.1.9,
\[
(\Theta^2 U)_b=(\Theta U)_{\vartheta b}=U_{\vartheta(\vartheta b)}=U_b.
\]
∎

### K.1.3 Link partition and the positive-time algebra

**Definition K.1.12 (positive/negative/boundary link sets).**  
Define subsets of the positively oriented links `E(\Lambda_L)` by endpoint time locations:
\[
E_+ := \{b\in E(\Lambda_L): \partial_-b,\partial_+b\in\Lambda_+\},
\qquad
E_- := \{b\in E(\Lambda_L): \partial_-b,\partial_+b\in\Lambda_-\},
\]
\[
E_0 := E(\Lambda_L)\setminus(E_+\cup E_-).
\]

**Lemma K.1.13 (reflection exchanges `E_+` and `E_-`).**  
The map `\Theta` induces a bijection between link-coordinate subspaces: it exchanges the sets `E_+\leftrightarrow E_-` and preserves `E_0` setwise.

*Proof.* If a link has both endpoints in `\Lambda_+`, then its reflected directed link has both endpoints in `\vartheta(\Lambda_+)=\Lambda_-` (Lemma K.1.5). The same reasoning applies in the opposite direction and for mixed-endpoint links. ∎

**Definition K.1.14 (factorization of configuration space).**  
Define
\[
M_+ := G^{E_+},\quad M_0:=G^{E_0},\quad M_-:=G^{E_-}.
\]
The product decomposition of the index set yields an identification
\[
M_{\Lambda_L}=G^{E(\Lambda_L)}\cong M_-\times M_0\times M_+.
\]
We write configurations as `U=(U_-,U_0,U_+)` under this identification.

**Definition K.1.15 (positive-time algebra).**  
Let `\mathcal A_+` be the unital `*`-algebra of bounded complex-valued cylinder observables on `M_{\Lambda_L}` that depend on only finitely many link variables in `E_+` (equivalently: functions measurable with respect to the sigma-algebra generated by `\{U_b:b\in E_+\}`).

**Definition K.1.16 (OS involution on observables).**  
For a bounded complex-valued observable `F` on `M_{\Lambda_L}`, define
\[
(\theta F)(U):=\overline{F(\Theta U)}.
\]

**Definition K.1.17 (reflection positivity property).**  
A probability measure `\mu` on `M_{\Lambda_L}` is **reflection positive** (with respect to `(\Theta,\mathcal A_+)`) if
\[
\int_{M_{\Lambda_L}} (\theta F)(U)\,F(U)\,\mu(dU)\ge 0
\qquad\text{for all }F\in\mathcal A_+.
\]

---

## K.2 Haar product measure and Wilson weight normalization

The Gibbs measure `\mu_{\Lambda_L,\beta}` is defined using the Riemannian volume `\mathrm{vol}_{g_{\Lambda_L}}` (Definition A.6.5). For reflection positivity it is convenient to work with product Haar measure; we record the equivalence.

**Definition K.2.1 (Haar probability measure on `G` and product Haar on configurations).**  
Let `dg` denote the Haar **probability** measure on `G`. Define the product Haar probability measure on `M_{\Lambda_L}=G^{E(\Lambda_L)}` by
\[
dU:=\prod_{b\in E(\Lambda_L)} dg(U_b).
\]

**Lemma K.2.2 (Riemannian volume agrees with Haar up to scale).**  
The Riemannian volume measure `\mathrm{vol}_{g_G}` on `(G,g_G)` is bi-invariant and therefore equals Haar measure multiplied by a strictly positive scalar. Consequently, the product volume measure `\mathrm{vol}_{g_{\Lambda_L}}` on `M_{\Lambda_L}=G^{E(\Lambda_L)}` differs from the product Haar probability measure `dU` only by multiplication by a strictly positive scalar.

In particular, the Gibbs probability measure `\mu_{\Lambda_L,\beta}` (Definition A.6.5) coincides with the probability measure defined by
\[
\mu_{\Lambda_L,\beta}(dU)
:=
\Big(\int_{M_{\Lambda_L}} e^{-S_{\Lambda_L,\beta}(U)}\,dU\Big)^{-1}
e^{-S_{\Lambda_L,\beta}(U)}\,dU.
\]

*Proof.* Since `g_G` is bi-invariant (Definition A.3.6), left and right translations on `G` are isometries. Isometries preserve Riemannian volume, hence `\mathrm{vol}_{g_G}` is left- and right-invariant. As `G` is compact, `\mathrm{vol}_{g_G}` is a finite nonzero bi-invariant Borel measure; by uniqueness of Haar measure up to a multiplicative scalar, `\mathrm{vol}_{g_G}` is Haar multiplied by a strictly positive scalar.

The product metric `g_{\Lambda_L}=\bigoplus_{b\in E(\Lambda_L)} g_G` (Definition A.4.2) yields a product volume measure, hence `\mathrm{vol}_{g_{\Lambda_L}}` is the product of the factor measures and therefore differs from `dU` by multiplication by a strictly positive scalar. This scalar cancels in the normalization defining the Gibbs probability measure, giving the stated expression. ∎

**Lemma K.2.3 (`\Theta`-invariance of product Haar).**  
For any bounded measurable `F` on `M_{\Lambda_L}`,
\[
\int F(\Theta U)\,dU = \int F(U)\,dU.
\]

*Proof.* By construction, `\Theta` acts on link coordinates as a permutation of link indices composed with inversion on some coordinates (those for which `\vartheta b` lands in the inverse orientation when restricted back to `E(\Lambda_L)`). Product measures are invariant under coordinate permutations, and Haar measure satisfies `dg(g^{-1})=dg(g)` (since inversion is a continuous group automorphism and Haar is unique). Combining these gives invariance. ∎

**Definition K.2.4 (plaquette weight without the additive constant).**  
Define the continuous class function
\[
w_\beta: G\to(0,\infty),
\qquad
w_\beta(g):=\exp\!\Big(\frac{\beta}{n}\Re\mathrm{Tr}(g)\Big),
\]
where `n` is the representation dimension (Assumption A.3.3).

**Lemma K.2.5 (Wilson weight factorization).**  
Let `S_{\Lambda_L,\beta}` be the Wilson action (Definition A.6.3). Then
\[
\exp\big(-S_{\Lambda_L,\beta}(U)\big)
= \exp\big(-\beta\,|P(\Lambda_L)|\big)\prod_{p\in P(\Lambda_L)} w_\beta\big(U_p(U)\big).
\]
Consequently, in all expectations under `\mu_{\Lambda_L,\beta}`, the global constant `\exp(-\beta|P(\Lambda_L)|)` cancels against the partition function and may be omitted.

*Proof.* By Definition A.6.2,
\[
\exp\big(-\Phi_\beta(g)\big)=\exp\Big(-\beta\Big(1-\frac{1}{n}\Re\mathrm{Tr}(g)\Big)\Big)=e^{-\beta}\,\exp\!\Big(\frac{\beta}{n}\Re\mathrm{Tr}(g)\Big)=e^{-\beta}\,w_\beta(g).
\]
Multiply over plaquettes and collect the factor `e^{-\beta}`. ∎

---

## K.3 A sum-of-squares kernel expansion for the plaquette weight

The OS proof requires an explicit **Gram (sum-of-squares)** decomposition of the kernel `(g,h)\mapsto w_\beta(g^{-1}h)`.

### K.3.1 Characters and matrix coefficients

**Definition K.3.1 (character and matrix coefficients).**  
Let `\pi:G\to U(d_\pi)` be a finite-dimensional unitary representation. Fix an orthonormal basis of `\mathbb C^{d_\pi}` and write
\[
\pi(g)=(\pi_{ij}(g))_{1\le i,j\le d_\pi}.
\]
Define its character `\chi_\pi(g):=\mathrm{Tr}(\pi(g))`.

**Lemma K.3.2 (Gram decomposition for a character kernel).**  
For a finite-dimensional unitary representation `\pi` and all `g,h\in G`,
\[
\chi_\pi(g^{-1}h)
=\sum_{i,j=1}^{d_\pi} \overline{\pi_{ij}(g)}\,\pi_{ij}(h).
\]
In particular, the kernel `(g,h)\mapsto \chi_\pi(g^{-1}h)` is positive semidefinite.

*Proof.* Since `\pi` is unitary, `\pi(g^{-1})=\pi(g)^*`. Hence
\[
\chi_\pi(g^{-1}h)=\mathrm{Tr}\big(\pi(g)^*\pi(h)\big)=\sum_{i=1}^{d_\pi}\sum_{j=1}^{d_\pi} \overline{\pi_{ji}(g)}\,\pi_{ji}(h),
\]
which is the stated formula after relabeling indices. For positive semidefiniteness, for any `g_1,\dots,g_m\in G` and `c\in\mathbb C^m`,
\[
\sum_{a,b=1}^m \overline{c_a}c_b\,\chi_\pi(g_a^{-1}g_b)
=\sum_{i,j}\Big|\sum_{a=1}^m c_a\,\pi_{ij}(g_a)\Big|^2\ge 0.
\]
∎

### K.3.2 Positivity of the Wilson plaquette weight

We now exhibit `w_\beta` as a nonnegative combination of characters of explicitly constructed unitary representations.

**Lemma K.3.3 (unitarity identities for the fixed representation `\rho`).**  
Let `\rho:G\to U(n)` be the fixed unitary representation (Assumption A.3.3) and let `\chi(g):=\mathrm{Tr}(\rho(g))`. Then:
1. `\chi(g^{-1})=\overline{\chi(g)}` for all `g\in G`.
2. `|\chi(g)|\le n` for all `g\in G`.

*Proof.* Since `\rho(g)` is unitary, `\rho(g^{-1})=\rho(g)^*`. Hence `\chi(g^{-1})=\mathrm{Tr}(\rho(g)^*)=\overline{\mathrm{Tr}(\rho(g))}`. Also, the eigenvalues of `\rho(g)` lie on the unit circle, so the trace is the sum of `n` complex numbers of modulus `1`, giving `|\chi(g)|\le n`. ∎

**Lemma K.3.4 (series expansion into characters of tensor-product representations).**  
For every `\beta\ge 0` and all `g\in G`,
\[
w_\beta(g)
=\sum_{m=0}^\infty\sum_{\ell=0}^\infty \frac{1}{m!\,\ell!}\Big(\frac{\beta}{2n}\Big)^{m+\ell}\,\chi(g)^m\,\chi(g^{-1})^\ell.
\]
Moreover, for each pair `(m,\ell)`, the function `g\mapsto \chi(g)^m\chi(g^{-1})^\ell` is the character of the finite-dimensional unitary representation
\[
\pi_{m,\ell}:=\rho^{\otimes m}\otimes (\rho^*)^{\otimes \ell}.
\]

*Proof.* By Lemma K.3.3(1),
\[
\Re\chi(g)=\tfrac12\big(\chi(g)+\chi(g^{-1})\big).
\]
Therefore
\[
w_\beta(g)=\exp\!\Big(\frac{\beta}{n}\Re\chi(g)\Big)=\exp\!\Big(\frac{\beta}{2n}\chi(g)\Big)\,\exp\!\Big(\frac{\beta}{2n}\chi(g^{-1})\Big).
\]
Expanding each exponential into its absolutely convergent power series gives the stated double series.

For the representation claim: `\chi(g)^m` is the character of `\rho^{\otimes m}` because `\mathrm{Tr}(A\otimes B)=\mathrm{Tr}(A)\mathrm{Tr}(B)` and `(\rho^{\otimes m})(g)=\rho(g)^{\otimes m}`. Similarly, `\chi(g^{-1})` is the character of the dual representation `\rho^*` (since `\rho^*(g)=\rho(g^{-1})^\top` is unitary and has trace `\chi(g^{-1})`). Hence the product `\chi(g)^m\chi(g^{-1})^\ell` is the character of the tensor product `\pi_{m,\ell}`. ∎

**Proposition K.3.5 (sum-of-squares kernel for `w_\beta`).**  
There exists a (countable) family of functions `{f_\alpha:G\to\mathbb C}` such that for all `g,h\in G`,
\[
w_\beta(g^{-1}h)=\sum_{\alpha} \overline{f_\alpha(g)}\,f_\alpha(h),
\tag{K.1}
\]
where the series converges absolutely and uniformly in `(g,h)`.

*Proof.* Combine Lemma K.3.4 and Lemma K.3.2. For each `(m,\ell)`, let `d_{m,\ell}:=\dim(\pi_{m,\ell})=n^{m+\ell}`, and fix an orthonormal basis of the representation space. Then by Lemma K.3.2,
\[
\chi_{\pi_{m,\ell}}(g^{-1}h)=\sum_{i,j=1}^{d_{m,\ell}} \overline{(\pi_{m,\ell})_{ij}(g)}\,(\pi_{m,\ell})_{ij}(h).
\]
Insert this into Lemma K.3.4 evaluated at `g^{-1}h`. Define the index set
\[
\alpha\equiv(m,\ell,i,j),
\qquad m,\ell\in\mathbb N_0,\ 1\le i,j\le d_{m,\ell},
\]
and set
\[
f_{m,\ell,i,j}(g)
:= \Big(\frac{1}{m!\,\ell!}\Big)^{1/2}\Big(\frac{\beta}{2n}\Big)^{(m+\ell)/2}\,(\pi_{m,\ell})_{ij}(g).
\]
Then (K.1) holds by construction.

It remains to prove absolute/uniform convergence. Since `\pi_{m,\ell}(g)` is unitary, the matrix coefficient bound `|(\pi_{m,\ell})_{ij}(g)|\le 1` holds. Therefore
\[
\sum_{i,j=1}^{d_{m,\ell}} |f_{m,\ell,i,j}(g)|^2
\le \frac{1}{m!\,\ell!}\Big(\frac{\beta}{2n}\Big)^{m+\ell}\,d_{m,\ell}
= \frac{1}{m!\,\ell!}\Big(\frac{\beta}{2}\Big)^{m+\ell}.
\]
Summing over `(m,\ell)` yields
\[
\sum_{\alpha}|f_\alpha(g)|^2\le \sum_{m,\ell\ge 0}\frac{(\beta/2)^{m+\ell}}{m!\,\ell!}=e^{\beta}.
\]
Hence by Cauchy–Schwarz, for all `g,h`,
\[
\sum_{\alpha}|\overline{f_\alpha(g)}f_\alpha(h)|
\le \Big(\sum_{\alpha}|f_\alpha(g)|^2\Big)^{1/2}\Big(\sum_{\alpha}|f_\alpha(h)|^2\Big)^{1/2}
\le e^{\beta}.
\]
This gives absolute convergence, uniformly in `(g,h)`. ∎

---

## K.4 Plaquette decomposition across the reflection plane

We now split the plaquettes into positive-side, negative-side, and straddling sets, and show that each straddling plaquette weight admits the Osterwalder–Seiler half-plaquette factorization required to apply Proposition K.3.5.

### K.4.1 Plaquette partition

**Definition K.4.1 (plaquette sets `P_+`, `P_-`, `P_0`).**  
Let `P(\Lambda_L)` be the oriented plaquette set (Definition A.2.3). Define:
- `P_+` as those plaquettes whose four boundary vertices all lie in `\Lambda_+`;
- `P_-` as those plaquettes whose four boundary vertices all lie in `\Lambda_-`;
- `P_0:=P(\Lambda_L)\setminus(P_+\cup P_-)`.

Equivalently, `p\in P_0` iff at least one boundary link of `p` lies in `E_0`.

**Lemma K.4.2 (reflection symmetry of the partition).**  
The reflection `\vartheta` induces a bijection of plaquettes that exchanges `P_+\leftrightarrow P_-` and preserves `P_0`.

*Proof.* The property “all boundary vertices lie in `\Lambda_+`” is mapped by `\vartheta` to “all boundary vertices lie in `\Lambda_-`” because `\vartheta(\Lambda_+)=\Lambda_-` (Lemma K.1.5). The complement is preserved. ∎

### K.4.2 Half-plaquette holonomies for straddling plaquettes

For a straddling plaquette `p\in P_0`, the holonomy `U_p(U)` depends on links from both sides plus boundary links. The OS argument uses `w_\beta(U_p(U))`, and since `w_\beta` is a class function (conjugation invariant) and inversion invariant, we can freely replace `U_p(U)` by any conjugate or inverse without changing the value of `w_\beta`.

**Lemma K.4.3 (class and inversion invariance of `w_\beta`).**  
For all `g,k\in G`,
\[
w_\beta(kgk^{-1})=w_\beta(g),
\qquad
w_\beta(g^{-1})=w_\beta(g).
\]

*Proof.* Conjugation invariance follows from trace invariance: `\mathrm{Tr}(kgk^{-1})=\mathrm{Tr}(g)`. Inversion invariance uses unitarity: `\Re\mathrm{Tr}(g^{-1})=\Re\overline{\mathrm{Tr}(g)}=\Re\mathrm{Tr}(g)`. ∎

We now treat the straddling plaquettes explicitly. Because the reflection datum only involves the time coordinate, every straddling plaquette must involve the time direction `0` and one spatial direction `\nu\in\{1,2,3\}`. Moreover, by the choice of `\Lambda_\pm` (Definition K.1.4), straddling occurs exactly at the two time interfaces `x_0\in\{0,T\}`.

**Lemma K.4.4 (classification of straddling plaquettes).**  
Let `p=(x;\mu,\nu)\in P_0`. Then one of the following holds:
1. `\mu=0`, `\nu\in\{1,2,3\}`, and `x_0\equiv 0\ (\mathrm{mod}\ L_0)`;
2. `\mu=0`, `\nu\in\{1,2,3\}`, and `x_0\equiv T\ (\mathrm{mod}\ L_0)`.

*Proof.* A plaquette lies in `P_0` iff it uses at least one boundary link in `E_0`, i.e. a link whose endpoints lie in different time halves. Since spatial links preserve time coordinate, any boundary link must be time-directed (`\mu=0`). Therefore any straddling plaquette must include direction `0` and some spatial direction `\nu\in\{1,2,3\}`.

A time-directed link `(x,0)` belongs to `E_0` precisely when `x_0\in\{0,T\}` (it connects time slice `0\to 1` or `T\to T+1`). Hence a plaquette using a boundary time link must have base time coordinate `x_0\in\{0,T\}` in the oriented convention of Definition A.2.3 (where `\mu<\nu`). ∎

**Definition K.4.5 (half-plaquette holonomies `V_p^\pm`).**  
Let `p=(x;0,\nu)\in P_0` with `\nu\in\{1,2,3\}` and `x_0\in\{0,T\}`.

- If `x_0=0`, define
\[
V_p^+(U):=U_{x,0}\,U_{x+\hat e_0,\nu},
\qquad
V_p^-(U):=U_{x,\nu}\,U_{x+\hat e_\nu,0}.
\]
- If `x_0=T`, define
\[
V_p^+(U):=U_{x,\nu}\,U_{x+\hat e_\nu,0},
\qquad
V_p^-(U):=U_{x,0}\,U_{x+\hat e_0,\nu}.
\]

In both cases, the products are taken in the group `G` and depend only on a pair of edges on the plaquette boundary.

**Lemma K.4.6 (dependence on `(U_\pm,U_0)`).**  
For every straddling plaquette `p\in P_0`,
\[
V_p^+(U)\ \text{depends only on}\ (U_+,U_0),
\qquad
V_p^-(U)\ \text{depends only on}\ (U_-,U_0).
\]

*Proof.* Consider `x_0=0`. Then the spatial link `(x+\hat e_0,\nu)` lies at time `1\in T_+`, hence is in `E_+`. The spatial link `(x,\nu)` lies at time `0\in T_-`, hence is in `E_-`. The time links `(x,0)` and `(x+\hat e_\nu,0)` cross the interface `0\to 1`, hence lie in `E_0`. Thus `V_p^+` uses one `E_0` link and one `E_+` link, while `V_p^-` uses one `E_-` link and one `E_0` link.

The case `x_0=T` is analogous: the time links `(x,0)` and `(x+\hat e_\nu,0)` cross `T\to T+1` and are in `E_0`; the spatial link `(x,\nu)` is at time `T\in T_+` so is in `E_+`; the spatial link `(x+\hat e_0,\nu)` is at time `T+1\in T_-` so is in `E_-`. ∎

**Lemma K.4.7 (Osterwalder–Seiler factorization for a straddling plaquette weight).**  
For every straddling plaquette `p\in P_0` and every configuration `U`,
\[
w_\beta\big(U_p(U)\big)=w_\beta\big( (V_p^-(U))^{-1}\,V_p^+(U)\big).
\tag{K.2}
\]

*Proof.* Fix `p=(x;0,\nu)`.

- If `x_0=0`, the plaquette holonomy (Definition A.6.1) is
\[
U_p(U)=U_{x,0}\,U_{x+\hat e_0,\nu}\,U_{x+\hat e_\nu,0}^{-1}\,U_{x,\nu}^{-1}.
\]
The right-hand side of (K.2) is
\[
(V_p^-(U))^{-1}V_p^+(U)
=(U_{x,\nu}\,U_{x+\hat e_\nu,0})^{-1}(U_{x,0}\,U_{x+\hat e_0,\nu})
=U_{x+\hat e_\nu,0}^{-1}\,U_{x,\nu}^{-1}\,U_{x,0}\,U_{x+\hat e_0,\nu}.
\]
This is a cyclic shift of the product defining `U_p(U)`. Cyclic shifts are conjugate in `G`, hence by Lemma K.4.3 (class invariance) they have the same `w_\beta` value.

- If `x_0=T`, then `U_p(U)` has the same formal product expression
\[
U_p(U)=U_{x,0}\,U_{x+\hat e_0,\nu}\,U_{x+\hat e_\nu,0}^{-1}\,U_{x,\nu}^{-1},
\]
but now the link-type membership differs (Lemma K.4.6). Consider instead the inverse
\[
U_p(U)^{-1}=U_{x,\nu}\,U_{x+\hat e_\nu,0}\,U_{x+\hat e_0,\nu}^{-1}\,U_{x,0}^{-1}.
\]
By Lemma K.4.3, `w_\beta(U_p)=w_\beta(U_p^{-1})`. The product `(V_p^-(U))^{-1}V_p^+(U)` for this case is
\[
(V_p^-(U))^{-1}V_p^+(U)
=(U_{x,0}\,U_{x+\hat e_0,\nu})^{-1}(U_{x,\nu}\,U_{x+\hat e_\nu,0})
=U_{x+\hat e_0,\nu}^{-1}\,U_{x,0}^{-1}\,U_{x,\nu}\,U_{x+\hat e_\nu,0},
\]
which is a cyclic shift of `U_p(U)^{-1}`. Again by Lemma K.4.3, the `w_\beta` values agree, establishing (K.2). ∎

---

## K.5 Reflection positivity for the Wilson Gibbs measure

We now assemble the ingredients.

**Theorem K.5.1 (finite-volume reflection positivity for the Wilson measure).**  
Assume `L_0` is even (Assumption K.1.1). Let `\mu_{\Lambda_L,\beta}` be the Wilson Gibbs measure on `M_{\Lambda_L}` (Definition A.6.5), and let `(\Theta,\mathcal A_+)` be the reflection datum from §K.1. Then `\mu_{\Lambda_L,\beta}` is reflection positive:
\[
\mathbb E_{\Lambda_L,\beta}\big[(\theta F)\,F\big]\ge 0
\qquad\text{for all }F\in\mathcal A_+.
\]

*Proof.* Fix `F\in\mathcal A_+`. By Lemma K.2.2 and Lemma K.2.5, we may compute expectations using the equivalent form
\[
\mu_{\Lambda_L,\beta}(dU)
\propto
\Big(\prod_{p\in P(\Lambda_L)} w_\beta(U_p(U))\Big)\,dU,
\]
where `\propto` denotes equality up to a positive normalizing constant.

**Step 1: split variables and plaquettes.**  
Write `U=(U_-,U_0,U_+)\in M_-\times M_0\times M_+` (Definition K.1.14), and note that `dU=dU_-\,dU_0\,dU_+`.

By Definition K.4.1, the plaquette set is partitioned as `P=P_+\sqcup P_0\sqcup P_-`. Plaquettes in `P_+` depend only on `U_+`, plaquettes in `P_-` depend only on `U_-`, and plaquettes in `P_0` may depend on all three blocks.

**Step 2: sum-of-squares expansion for the straddling plaquettes.**  
For each straddling plaquette `p\in P_0`, Lemma K.4.7 writes the weight as
\[
w_\beta(U_p(U))=w_\beta\big((V_p^-(U))^{-1}V_p^+(U)\big),
\]
where `V_p^+` depends only on `(U_+,U_0)` and `V_p^-` only on `(U_-,U_0)` (Lemma K.4.6).

Apply Proposition K.3.5 with `g=V_p^-(U)` and `h=V_p^+(U)`:
\[
w_\beta\big((V_p^-(U))^{-1}V_p^+(U)\big)
=\sum_{\alpha} \overline{f_\alpha\big(V_p^-(U)\big)}\,f_\alpha\big(V_p^+(U)\big),
\]
with absolute convergence uniform in `U`. Since `P_0` is finite, multiplying these expansions over `p\in P_0` yields
\[
\prod_{p\in P_0} w_\beta\big(U_p(U)\big)
=\sum_{\boldsymbol\alpha\in\mathcal I^{P_0}} \overline{F_{\boldsymbol\alpha}^-(U)}\,F_{\boldsymbol\alpha}^+(U),
\tag{K.3}
\]
where `\mathcal I` is the index set from Proposition K.3.5 and
\[
F_{\boldsymbol\alpha}^+(U):=\prod_{p\in P_0} f_{\alpha_p}\big(V_p^+(U)\big),
\qquad
F_{\boldsymbol\alpha}^-(U):=\prod_{p\in P_0} f_{\alpha_p}\big(V_p^-(U)\big).
\]
By Lemma K.4.6, `F_{\boldsymbol\alpha}^+` depends only on `(U_+,U_0)` and `F_{\boldsymbol\alpha}^-` only on `(U_-,U_0)`.

**Step 3: factorization of the OS form.**  
Using Definition K.1.16 and (K.3),
\[
\begin{aligned}
\mathbb E_{\Lambda_L,\beta}\big[(\theta F)F\big]
&\propto
\int \overline{F(\Theta U)}\,F(U)
\Big(\prod_{p\in P_+} w_\beta(U_p(U))\Big)
\Big(\prod_{p\in P_-} w_\beta(U_p(U))\Big)
\Big(\prod_{p\in P_0} w_\beta(U_p(U))\Big)
\,dU\\
&=
\sum_{\boldsymbol\alpha}
\int \overline{F(\Theta U)}\,\overline{F_{\boldsymbol\alpha}^-(U)}\,F(U)\,F_{\boldsymbol\alpha}^+(U)
\Big(\prod_{p\in P_+} w_\beta(U_p(U))\Big)
\Big(\prod_{p\in P_-} w_\beta(U_p(U))\Big)
\,dU.
\end{aligned}
\]
For each fixed `\boldsymbol\alpha`, the integrand is a product of a function of `(U_+,U_0)` and a function of `(U_-,U_0)`. Hence, defining
\[
G_{\boldsymbol\alpha}(U_0)
:=
\int_{M_+} F(U_+)
\,F_{\boldsymbol\alpha}^+(U_+,U_0)
\,\Big(\prod_{p\in P_+} w_\beta(U_p(U_+,U_0))\Big)
\,dU_+,
\tag{K.4}
\]
\[
H_{\boldsymbol\alpha}(U_0)
:=
\int_{M_-} \overline{F(\Theta(U_-,U_0,U_+))}
\,\overline{F_{\boldsymbol\alpha}^-(U_-,U_0)}
\,\Big(\prod_{p\in P_-} w_\beta(U_p(U_-,U_0))\Big)
\,dU_-,
\tag{K.5}
\]
(where in (K.5) the expression `F(\Theta U)` depends on `U_-` and `U_0` only because `F\in\mathcal A_+`), we obtain
\[
\mathbb E_{\Lambda_L,\beta}\big[(\theta F)F\big]
\propto
\sum_{\boldsymbol\alpha}\int_{M_0} H_{\boldsymbol\alpha}(U_0)\,G_{\boldsymbol\alpha}(U_0)\,dU_0.
\tag{K.6}
\]

**Step 4: identify `H_{\boldsymbol\alpha}=\overline{G_{\boldsymbol\alpha}}`.**  
By Lemma K.1.13, the reflection `\Theta` induces a bijection between `M_+` and `M_-` (for fixed boundary coordinates `U_0`), and by Lemma K.2.3 the Jacobian of this change of variables is `1` with respect to `dU`. Moreover, Lemma K.4.2 identifies `P_-` as the reflected image of `P_+`, and the definitions of `F_{\boldsymbol\alpha}^\pm` together with Definition K.1.10 imply that the reflected negative-side integrand is the complex conjugate of the positive-side integrand. Concretely, applying the change of variables `U_-\mapsto \Theta U_+` (with `U_0` fixed) in (K.5) gives
\[
H_{\boldsymbol\alpha}(U_0)=\overline{G_{\boldsymbol\alpha}(U_0)}.
\]

**Step 5: conclude nonnegativity.**  
Insert `H_{\boldsymbol\alpha}=\overline{G_{\boldsymbol\alpha}}` into (K.6):
\[
\mathbb E_{\Lambda_L,\beta}\big[(\theta F)F\big]
\propto
\sum_{\boldsymbol\alpha}\int_{M_0} |G_{\boldsymbol\alpha}(U_0)|^2\,dU_0\ \ge 0.
\]
Dividing by the positive normalizing constant yields the stated inequality. ∎

**Lemma K.5.2 (gauge invariance is not used).**  
The proof of Theorem K.5.1 uses only: (i) product Haar invariance under reflection, (ii) locality of plaquette interactions, and (iii) the sum-of-squares kernel expansion of `w_\beta`. No gauge-invariance property of `F` is invoked.

*Proof.* The only structural property of `F` used in the proof of Theorem K.5.1 is the support restriction `F\in\mathcal A_+`, i.e. dependence on the `E_+` coordinates only (Definition K.1.9). No step invokes the gauge action on `M_{\Lambda_L}` or gauge invariance of the integrand. ∎

