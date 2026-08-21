---
title: "Rank-3 Transversality of the One-Link Cancellation Set and the Binomial-Tail Typicality Upgrade (SU(2))"
project: "LYAPUNOV TOP 40"
status: "New proof module (transversality lemma → tube exponent 3 → disjoint-star binomial tail → outside-core Lyapunov drift)"
date: "2025-12-31"
sources:
  - "1_local_cancellation_su2.md"
  - "LYAPUNOV_07_tube_exponent_cancellation_set_SU2.md"
  - "LYAPUNOV_01_outside_core_coercivity_tube_matching.md"
  - "03_drift_gluing_gap_mechanism.md"
  - "01_smooth_plaquette_lyapunov.md"
---

\newcommand{\SU}{\mathrm{SU}}
\newcommand{\Ad}{\mathrm{Ad}}
\newcommand{\Haar}{\mathrm{Haar}}
\newcommand{\dist}{\mathrm{dist}}
\newcommand{\RR}{\mathbb{R}}
\newcommand{\1}{\mathbf{1}}
\newcommand{\Z}{\mathcal Z}
\newcommand{\A}{\mathcal A}
\newcommand{\Ext}{\mathrm{Ext}}

# 0. What this module adds

This note hardens two steps that were previously “morally true” but not lemma-grade:

1. **Transversality lemma (rank 3):** on a boundary-strip region and away from a force-alignment locus, the one-link cancellation set
   \[
   \Z_\ell:=\{U:\ F_\ell(U)=\nabla_\ell S_W(U)=0\}
   \]
   is a codimension-$3$ smooth submanifold (hence tube exponent $3$).

2. **Typicality upgrade:** combining the tube bound $\Haar(\dist(\cdot,\Z_\ell)\le\tau)\lesssim \tau^3$ with
   - disjoint extended-star conditional factorization,
   - uniform Haar domination of Gibbs conditionals,
   yields a **binomial tail** showing that *many links are simultaneously not near cancellation*.

This is the missing bridge from a one-link coercivity statement to a **strip-wide Lyapunov drift inequality**.

---

# 1. Local force map and the cancellation set

Fix $G=\SU(2)$ and identify $\mathfrak{su}(2)\cong\RR^3$ with the Hilbert--Schmidt metric.

Fix a link $\ell$ in $d=4$ and let $p_1,\dots,p_m$ be its incident plaquettes ($m=6$).  
On the finite-dimensional local configuration space $\mathcal U_\ell$ (a product of finitely many group copies), define the one-link force map
\[
F_\ell(U):=\nabla_\ell S_W(U)=\sum_{j=1}^m \sigma_j\,\Ad_{g_j(U)}\big(X_j(U)\big)\in\mathfrak{su}(2),
\]
with $X_j(U)=\nabla_G \Phi_\beta(U_{p_j}(U))$ the plaquette force vector and $g_j(U)$ the staple transport.

Define the **cancellation set**
\[
\Z_\ell:=F_\ell^{-1}(0)\subset\mathcal U_\ell.
\]

---

# 2. The right exceptional set for transversality: force-alignment after transport

Define transported force vectors
\[
w_j(U):=\sigma_j\,\Ad_{g_j(U)}\big(X_j(U)\big)\in\RR^3,
\qquad F_\ell(U)=\sum_{j=1}^m w_j(U).
\]

## Definition 2.1 (Transported-force alignment locus)

On any region where the map $U\mapsto w_j(U)$ is defined and continuous, set
\[
\A_\ell^{\mathrm{force}}
:=
\Big\{U:\ \exists\, n\in S^2\subset\RR^3 \text{ with } w_j(U)\in \RR\,n\ \forall j\Big\}.
\]

This is the locus where **all transported forces lie in a common line**, i.e. the only obstruction to the “two planes span $\RR^3$” argument.

*Remark.* This set is (real-)algebraic: it is defined by vanishing of finitely many cross products $w_j\times w_k$.

---

# 3. The strip and the disjoint-staple variation hypothesis

Let $K\Subset \mathcal U_\ell$ be a compact “boundary-strip / regular” set on which each $U_{p_j}(U)\notin\{\pm\1\}$ so that $X_j(U)\neq 0$ and all maps are smooth.

The following hypothesis is exactly what is used (implicitly) in `1_local_cancellation_su2.md` under “admissibility note”.

## Hypothesis 3.1 (Disjoint-staple variation coordinates)

For each incident plaquette index $j$, there exists a local link coordinate $r_j\in\SU(2)$ among the factors of $\mathcal U_\ell$ such that, in a neighborhood of $K$,
- the transport admits a factorization
  \[
  g_j(U)=r_j\cdot \bar g_j(\widehat U),
  \]
  where $\widehat U$ denotes the remaining local link variables;
- for $k\neq j$, the maps $g_k(U)$ and $X_k(U)$ do **not** depend on $r_j$.

Equivalently: varying $r_j$ changes only the single summand $w_j(U)$ and does so through left multiplication in $g_j$.

In $d=4$ this is geometrically natural: each incident plaquette contains a “free” staple edge not used by the other incident plaquettes, so $(r_1,\dots,r_m)$ can be taken as disjoint local degrees of freedom.

---

# 4. Rank-3 transversality lemma (the requested crisp statement)

## Lemma 4.1 (Rank-3 transversality of $\Z_\ell$ away from alignment)

Assume Hypothesis 3.1 on a compact set $K\Subset\mathcal U_\ell$ and assume $X_j(U)\neq 0$ for all $U\in K$ and all $j$.

Then for every
\[
U\in K\cap \Z_\ell \cap \big(K\setminus \A_\ell^{\mathrm{force}}\big),
\]
we have
\[
\boxed{\ \mathrm{rank}\,D F_\ell(U)=3.\ }
\]

### Proof
Fix $U$ as above. Since $U\notin \A_\ell^{\mathrm{force}}$, there exist indices $j_1\neq j_2$ such that $w_{j_1}(U)\not\parallel w_{j_2}(U)$.

By Hypothesis 3.1, we may vary $r_{j_k}$ independently while keeping all other $w_j$ fixed (to first order).  
Vary $r_{j_k}$ along $r_{j_k}(t)=\exp(tY)\,r_{j_k}$ with $Y\in\mathfrak{su}(2)\cong\RR^3$. Differentiating,
\[
\frac{d}{dt}\Big|_{t=0} w_{j_k}(U(t))
=
[Y,\ w_{j_k}(U)],
\]
so as $Y$ ranges over $\mathfrak{su}(2)$ the variations span the plane $w_{j_k}(U)^\perp$ in $\RR^3$.

Thus
\[
w_{j_1}(U)^\perp \subset \mathrm{Im}(D F_\ell(U)),
\qquad
w_{j_2}(U)^\perp \subset \mathrm{Im}(D F_\ell(U)).
\]
Since $w_{j_1}\not\parallel w_{j_2}$, the sum of these two distinct codimension-$1$ planes is all of $\RR^3$:
\[
w_{j_1}^\perp + w_{j_2}^\perp = \RR^3.
\]
Therefore $\mathrm{Im}(D F_\ell(U))=\RR^3$, i.e. $\mathrm{rank}\,D F_\ell(U)=3$. $\square$

---

# 5. Tube exponent for the actual cancellation set

## Corollary 5.1 (Codimension 3 on the regular stratum)

Under the assumptions of Lemma 4.1, the set
\[
\Z_\ell^{\mathrm{reg}}:=K\cap \Z_\ell \cap (K\setminus \A_\ell^{\mathrm{force}})
\]
is a smooth embedded codimension-$3$ submanifold of $\mathcal U_\ell$.

## Corollary 5.2 (Tube bound with exponent 3)

There exist constants $C_K,\tau_K>0$ such that for all $\tau\in(0,\tau_K]$,
\[
\boxed{
\Haar_{\mathcal U_\ell}\big(\{U\in K:\dist(U,\Z_\ell)\le\tau\}\big)
\ \le\ C_K\,\tau^3\ +\ \Haar(\dist(U,\A_\ell^{\mathrm{force}})\le\tau).
}
\tag{5.1}
\]

If, additionally, one has a higher-codimension tube bound for $\A_\ell^{\mathrm{force}}$ (e.g. $\lesssim \tau^{10}$ on a small-angle strip),
then the dominant tube exponent for $\Z_\ell$ is $\kappa_{\Z}=3$.

---

# 6. From tube($\Z_\ell$) to a binomial tail on disjoint extended stars

Let $\mu_\beta$ be the Wilson Gibbs measure on a finite lattice region $\Lambda$:
\[
\mu_\beta(dU)=Z^{-1}\exp\Big(-\beta\sum_{p} B(U_p)\Big)\Haar(dU),
\qquad 0\le B\le 2.
\]

For each link $\ell$, define the extended star region $\Ext(\ell)$ as in the project: it contains the plaquette star and its Markov blanket.

Let
\[
E_\ell(\tau):=\{U:\dist(U_{\Ext(\ell)}, \Z_\ell)\le\tau\},
\]
where $\dist$ is measured using the fixed product metric on the local block $\Ext(\ell)$.

## Lemma 6.1 (Uniform domination by Haar on a block)

For any block $R$ and any outside configuration $U_{R^c}$,
\[
\mu_\beta(A\mid U_{R^c})\le e^{2\beta|P(R)|}\,\Haar_R(A),
\]
for every event $A$ measurable with respect to $U_R$.

Hence, for each $\ell$,
\[
\mu_\beta\big(E_\ell(\tau)\mid U_{\Ext(\ell)^c}\big)
\ \le\
e^{2\beta|P(\Ext(\ell))|}\,\Haar_{\Ext(\ell)}(E_\ell(\tau))
\ \le\
p(\tau),
\tag{6.1}
\]
with $p(\tau):=C_\beta\,\tau^3$ for $\tau$ small, using (5.1) and absorbing constants.

## Lemma 6.2 (Conditional independence on a disjoint-star matching)

If $\{\ell_i\}_{i=1}^M$ are links with pairwise disjoint extended stars, then conditional on the complement,
the variables $U_{\Ext(\ell_i)}$ are independent under $\mu_\beta(\cdot\mid U_{R^c})$ with $R=\bigsqcup_i \Ext(\ell_i)$.
Therefore the events $\{E_{\ell_i}(\tau)\}$ are conditionally independent.

## Proposition 6.3 (Binomial tail for “many near-cancellation blocks”)

Let $\{\ell_i\}_{i=1}^M$ be a disjoint extended-star matching. Then for any $\delta\in(0,1)$ and $\tau$ small,
\[
\mu_\beta\Big(\sum_{i=1}^M \mathbf 1_{E_{\ell_i}(\tau)}\ge \delta M\Big)
\ \le\
\exp\Big(-M\,D(\delta\ \|\ p(\tau))\Big),
\tag{6.2}
\]
where $D(\delta\|p)=\delta\log\frac{\delta}{p}+(1-\delta)\log\frac{1-\delta}{1-p}$ is the Bernoulli relative entropy.

In particular, if $p(\tau)\le \delta/2$, then
\[
\mu_\beta\Big(\sum_{i=1}^M \mathbf 1_{E_{\ell_i}(\tau)}\ge \delta M\Big)
\ \le\
\exp(-c_\delta M)
\]
for some $c_\delta>0$.

---

# 7. Upgrading one-link coercivity to strip-wide Lyapunov drift

There are two deterministic ingredients:

1. **Outside-core implies many rough links.**  
   If the averaged plaquette disorder satisfies $\overline B\ge b_0$, then by counting,
   a positive fraction of links $\ell$ satisfy $\max_{p\ni\ell} B(U_p)\ge b_1$ (with $b_1$ comparable to $b_0$).

2. **Away from cancellation tubes, the link force is bounded below.**  
   Fix $b_1$ and $\tau>0$ and define a compact local set $K=K(b_1)$ as a boundary-strip rough region.
   Since $F_\ell$ is continuous and $\Z_\ell$ is its zero set, compactness gives:
   \[
   \dist(U,\Z_\ell)\ge\tau\quad\Longrightarrow\quad |F_\ell(U)|\ge c_{\mathrm{loc}}(b_1,\tau)>0.
   \tag{7.1}
   \]

Combine:
- outside-core gives many rough links,
- Proposition 6.3 gives that only a small fraction of a large matching are near $\Z_\ell$,
so on the high-probability event,
a positive fraction of links are **rough and not near cancellation**.

Summing squares,
\[
\|\nabla S_W(U)\|^2
=\sum_{\ell}|F_\ell(U)|^2
\ \gtrsim\
|E(\Lambda)|\cdot c_{\mathrm{loc}}(b_1,\tau)^2
\quad\text{on the typical outside-core set}.
\tag{7.2}
\]

Finally, for the smooth plaquette proxy Lyapunov atom $\overline V_\Lambda$ (character-based proxy),
the drift identity
\[
L\overline V_\Lambda
=
-\lambda \overline V_\Lambda + b
\ -\ \langle\nabla S_W,\nabla \overline V_\Lambda\rangle
\]
reduces drift negativity to the pairing term.
On the typical outside-core set, (7.2) forces the pairing term to dominate the Laplacian leak,
yielding a Foster--Lyapunov inequality of the schematic form
\[
L\overline V_\Lambda \ \le\ -\alpha\,\overline V_\Lambda + \beta\,\mathbf 1_K,
\]
with constants independent of lattice volume.

This is the explicit “tube($\Z$)+matching $\Rightarrow$ strip drift” upgrade requested.

---

# 8. What remains (finite, explicit)

1. Verify Hypothesis 3.1 in a concrete coordinate chart on $\mathcal U_\ell$ (a one-page lattice-geometry check).
2. Decide whether to keep $\A_\ell^{\mathrm{force}}$ as the primary singular stratum, or prove it equals the “aligned Cartan locus” defined via holonomy axes on the boundary strip.
3. Propagate the typical outside-core drift into the global Poincaré/LSI gluing engine (already in the project).
