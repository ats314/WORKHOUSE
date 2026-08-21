# A conditional projected-capacity firewall closure for SU(2) lattice gauge theory

## Lemma Q, positive source-radius stability, and local cap-intersection geometry

**Draft v3.3, journal-agnostic.**  
**Date:** 2026-05-26.  
**Status:** Conditional theorem architecture with targeted finite-volume evidence. This manuscript does **not** prove the four-dimensional SU(2) Yang–Mills mass gap.

**Pass 3.3 update.** This pass unifies the analytic core around the positive source-radius partition function and local cap-intersection geometry. The central innovation is the structural pivot

\[
\text{direct product moments}
\quad\leadsto\quad
\text{positive source-radius bound for }Z_A(s),
\]

which converts rare-source factorization into a coefficient-extraction consequence of a real-positive generating function estimate. This pass also makes explicit that the exact SU(2) vMF heat-bath geometry is the local engine for the \(q_\eta\) factor, while the Bałaban/Dimock expansion is needed only for far-source factorization.

**Pass 3.2 update.** This pass sharpens the manuscript in four places:  
1. it adds an explicit theorem-dependency ledger separating proved reductions from open hypotheses;  
2. it introduces a tempered-boundary formulation for Lemma Q, avoiding an over-strong adversarial-boundary statement;  
3. it states the finite-dimensional LCI theorem as the next standalone analytic target;  
4. it adds a referee-risk section identifying likely objections and the corresponding manuscript-safe responses.


---

## Abstract

We organize the projected Maxwell Birman–Schwinger firewall (PMBSF) program for SU(2) lattice gauge theory into an explicit conditional theorem. The deterministic operator spine is finite-dimensional and unconditional: the projected plaquette comparator

\[
A_p=P\mathbf 1_{\partial p}P,
\]

the polymer-type ordered trace-overlap summability framework, and the projected Birman–Schwinger firewall criterion reduce sparse-defect coercivity to projected-capacity control. The remaining probabilistic input is a local SU(2) rare-source factorization estimate, called **Lemma Q**, for smoothed high-plaquette sources \(X_{p,\eta}\) inside frozen-exterior Bałaban blocks.

The main structural refinement in this draft is to replace the direct product-moment attack on Lemma Q by a positive source-radius route. For a block Gibbs measure \(\mu_C^\xi\), define

\[
Z_A(s)=\mathbb E_{\mu_C^\xi}\prod_{p\in A}(1+sX_{p,\eta}).
\]

If \(Z_A(\rho/q_\eta)\le e^{K|A|}\), positivity of the coefficients gives Lemma Q:

\[
\mathbb E_{\mu_C^\xi}\prod_{p\in B}X_{p,\eta}
\le
(e^K\rho^{-1}q_\eta)^{|B|}.
\]

We prove that this positive source-radius bound follows from a sharper tilted one-source stability condition, TOS+J:

\[
\mathbb E_{\mu^{S,s}}X_{p,\eta}
\le
Cq_\eta\exp\left(\sum_{r\in S}J(p,r)\right),
\qquad
J(p,r)\le C_Je^{-m_Jd_C(p,r)}.
\]

We then reduce TOS+J to two concrete inputs: local cap-intersection stability (LCI) for the exact SU(2) one-link heat-bath law on \(S^3\), and a Bałaban/Dimock far-source stability theorem. The one-link conditional is

\[
U_\ell\mid U_{\ell^c}
\sim
\mathrm{vMF}_4\left(
\frac{\overline H_\ell}{\|H_\ell\|},
\beta\|H_\ell\|
\right),
\]

and each incident plaquette source is bounded by a spherical cap

\[
X_{p,\eta}\le \mathbf 1_{\{u\cdot n_p\le 1-(t-\eta)\}}.
\]

Thus the local part of the source-stability problem becomes a finite-dimensional \(S^3\) cap-intersection problem. The nonlocal part is the remaining source-weighted Bałaban stability problem.

We include targeted numerical evidence at \(\beta=3.5\), \(q_\eta=0.003\), \(\eta=0.005\). Exact heat-bath frozen-block diagnostics at side 8 and exact heat-bath side-10/core-margin-3 Stage B geometry support the block source-stability mechanism. The exact heat-bath Stage B run gives median cavity ratio \(1.0158\), maximum cavity ratio \(2.5930\), median rooted cavity ratio \(1.0221\), and maximum rooted ratio \(2.3431\) across 64 frozen-boundary blocks and 864 core plaquettes per block. Full-volume pair/rooted covariance diagnostics through \(L=64\) support the \(k=1\) consequence. These diagnostics do not prove Lemma Q.

The central conditional theorem is:

\[
\boxed{
\text{LCI-good typicality + Bałaban far-source stability}
\Rightarrow
\text{TOS+J}
\Rightarrow
\text{Lemma Q}
\Rightarrow
\text{projected-capacity firewall closure}.
}
\]


The analytic novelty is the partition-function pivot: Lemma Q is not attacked through direct product-moment mixing, but through the large positive source-radius estimate

\[
Z_A(\rho/q_\eta)\le e^{K|A|}.
\]

This converts multiplicative rare-source factorization into a coefficient-extraction consequence of positivity.


The open analytic tasks are the local LCI-good typicality theorem, the far-source stability theorem in the source-weighted Bałaban expansion, and the \(\eta\to0\) boundary-band gate.

**Keywords.** SU(2) lattice gauge theory; Yang–Mills mass gap; projected capacity; Birman–Schwinger criterion; cluster expansion; von Mises–Fisher distribution; spherical caps; rare events; source stability.

---

## 1. Introduction

### 1.1 Scope

This paper is about a conditional route toward SU(2) lattice Yang–Mills coercivity using projected-capacity control. It is not a continuum Yang–Mills mass-gap proof. It does not construct the continuum quantum field theory on \(\mathbb R^4\), does not prove the Osterwalder–Schrader axioms, and does not prove a positive physical mass gap in the reconstructed Hilbert space.

The purpose is narrower:

\[
\boxed{
\text{isolate the exact local SU(2) probability theorem needed by the PMBSF firewall mechanism.}
}
\]

That theorem is Lemma Q, or more sharply the LCI/TOS+J theorem developed below.

### 1.2 The conditional architecture

The PMBSF program has three logically separate components.

First, a deterministic projected-capacity spine. This includes the transverse Maxwell projector \(P\), the projected plaquette comparator

\[
A_p=P\mathbf1_{\partial p}P,
\]

the trace-overlap quantity

\[
\operatorname{tr}(A_pA_q),
\]

and the projected Birman–Schwinger criterion

\[
\|M^{-1/2}PV_DP M^{-1/2}\|<1.
\]

Second, a probabilistic sparse-source theorem for SU(2) Wilson fields. This is Lemma Q. It states that smoothed high-plaquette sources in a shaved block core retain one factor of their global intensity \(q_\eta\) per marked plaquette, even after freezing the exterior.

Third, a source-weighted constructive expansion. The Bałaban/Dimock machinery supplies the unmarked small/large-field and polymer-locality architecture. What is needed here is a marked upgrade carrying one \(q_\eta\) factor per inserted high-plaquette source.

The conditional theorem is:

\[
\boxed{
\text{Lemma Q + source-weighted Bałaban expansion + boundary-band gate}
\Rightarrow
\text{SU(2) projected-capacity firewall closure}.
}
\]

This draft refines Lemma Q into a sharper proof interface:

\[
\boxed{
\text{LCI-good typicality + Bałaban far-source stability}
\Rightarrow
\text{TOS+J}
\Rightarrow
\text{positive source-radius}
\Rightarrow
\text{Lemma Q}.
}
\]

### 1.3 Why the positive source-radius route is preferable

An earlier route tried to obtain \(q_\eta^{|B|}\) factors by complex Cauchy extraction from source variables of radius \(O(q_\eta^{-1})\). That is technically dangerous because logarithms and ratios of source partition functions may have zeros in large complex polydiscs. The present draft instead uses only nonnegative real source parameters.

Because

\[
0\le X_{p,\eta}\le1,
\]

the generating function

\[
Z_A(s)=\mathbb E\prod_{p\in A}(1+sX_{p,\eta})
\]

has nonnegative coefficients for \(s\ge0\). A positive real bound at \(s=\rho/q_\eta\) is enough to extract Lemma Q directly. No complex zero-free theorem is required.

This is the main technical simplification of this draft.

---

## 1.4 Theorem-dependency ledger

The manuscript uses the following dependency graph.

\[
\boxed{
\mathrm{LCI}_{\rm good}
+
\mathrm{BFS}_{\rm far}
\Longrightarrow
\mathrm{TOS{+}J}
}
\tag{1.1}
\]

\[
\boxed{
\mathrm{TOS{+}J}
\Longrightarrow
Z_A(\rho/q_\eta)\le e^{K|A|}
}
\tag{1.2}
\]

\[
\boxed{
Z_A(\rho/q_\eta)\le e^{K|A|}
\Longrightarrow
\mathrm{Lemma\ Q}
}
\tag{1.3}
\]

\[
\boxed{
\mathrm{Lemma\ Q}
+
\mathrm{SWB}
+
\mathrm{BBG}
\Longrightarrow
\mathrm{PMBSF\ firewall\ closure}.
}
\tag{1.4}
\]

Here:

- \(\mathrm{LCI}_{\rm good}\) is local cap-intersection stability for incident heat-bath caps on \(S^3\), with rooted absorption of its complement.
- \(\mathrm{BFS}_{\rm far}\) is Bałaban far-source stability: far positive source tilts distort local source rates only through an exponentially summable kernel.
- \(\mathrm{TOS{+}J}\) is positive tilted one-source stability with kernel \(J(p,r)\).
- \(\mathrm{SWB}\) is the source-weighted Bałaban expansion.
- \(\mathrm{BBG}\) is the boundary-band gate passing from smooth source \(X_{p,\eta}\) to the hard threshold.

The reductions (1.2) and (1.3) are proved in this manuscript. The implication (1.1) is reduced to a finite-dimensional local cap theorem plus a source-weighted Bałaban locality theorem. The implication (1.4) is conditional on the source-weighted Bałaban and boundary-band inputs.

Thus the paper proves a conditional architecture, not the SU(2) Yang--Mills mass gap.

### 1.5 Proved reductions versus open hypotheses

The proved reductions are:

\[
\mathrm{TOS{+}J}\Rightarrow\mathrm{positive\ source\ radius},
\]

\[
\mathrm{positive\ source\ radius}\Rightarrow\mathrm{Lemma\ Q},
\]

\[
\mathrm{LCI}\Rightarrow\mathrm{incident\ positive\ tilt\ stability},
\]

and the deterministic Birman--Schwinger implication

\[
\Theta_D<1\Rightarrow M-PV_DP\succeq(1-\Theta_D)M.
\]

The open hypotheses are:

\[
\mathrm{LCI}_{\rm good}\ \text{typicality},
\qquad
\mathrm{BFS}_{\rm far},
\qquad
\mathrm{SWB},
\qquad
\mathrm{BBG}.
\]

This distinction should be maintained everywhere in the final manuscript.


---

## 1.6 Unified analytic core: from LCI to Lemma Q

The analytic core of the manuscript is the following three-stage reduction.

\[
\boxed{
\text{positive source-radius partition function}
}
\]

\[
\boxed{
\text{exact SU(2) local cap-intersection geometry}
}
\]

\[
\boxed{
\text{Bałaban far-source factorization}
}
\]

The point of this restructuring is to avoid a fragile direct attack on product moments

\[
\mathbb E_{\mu_C^\xi}\prod_{p\in B}X_{p,\eta}.
\]

A direct product-moment attack is vulnerable to two defects. First, it tends to produce additive cluster-mixing errors, whereas Lemma Q requires multiplicative \(q_\eta\)-per-source factors. Second, a pointwise statement uniform over arbitrary exterior boundaries is too strong; rare adversarial exterior configurations can distort the local defect geometry. The present approach isolates this problem into a tempered-boundary / rooted-bad-geometry budget.

### 1.6.1 Stage I: the positive source-radius pivot

Let \(A\subset C^\circ\). Define

\[
Z_A(s)
=
\mathbb E_{\mu_C^\xi}
\prod_{p\in A}(1+sX_{p,\eta}),
\qquad s\ge0.
\]

The key positive-radius estimate is

\[
\boxed{
Z_A(\rho/q_\eta)
\le
\exp(K|A|).
}
\tag{1.6.1}
\]

This is a real-positive statement. No complex zero-free theorem is needed.

Since

\[
Z_A(s)
=
\sum_{B\subset A}
s^{|B|}
\mathbb E_{\mu_C^\xi}\prod_{p\in B}X_{p,\eta}
\]

has nonnegative coefficients, taking \(A=B\) and \(s=\rho/q_\eta\) gives

\[
(\rho/q_\eta)^{|B|}
\mathbb E_{\mu_C^\xi}\prod_{p\in B}X_{p,\eta}
\le
Z_B(\rho/q_\eta)
\le
e^{K|B|}.
\]

Therefore,

\[
\boxed{
\mathbb E_{\mu_C^\xi}\prod_{p\in B}X_{p,\eta}
\le
(e^K\rho^{-1}q_\eta)^{|B|}.
}
\tag{1.6.2}
\]

This is Lemma Q with \(C_Q=e^K/\rho\).

If the positive-radius estimate is proved using TOS+J, then

\[
K=\rho C e^{J_*},
\qquad
J_*=\sup_p\sum_rJ(p,r),
\]

and

\[
C_Q(\rho)=\rho^{-1}\exp(\rho Ce^{J_*}).
\]

One may optimize over \(\rho\) within the interval where TOS+J is valid. The proof itself does not require optimization; it requires only one admissible \(\rho>0\).

**Novelty.** This converts rare-source factorization into a partition-function radius statement. The multiplicative \(q_\eta^{|B|}\) factor is recovered algebraically from the scale \(s\sim q_\eta^{-1}\), not by cancellation in cumulants.

### 1.6.2 Stage II: exact SU(2) local cap-intersection mechanism

Choose an incident heat-bath link \(e=e(p)\). Conditional on all other links,

\[
U_e\mid U_{e^c}
\sim
\mathrm{vMF}_4
\left(
\frac{\overline H_e}{\|H_e\|},
\beta\|H_e\|
\right).
\]

For any incident plaquette \(r\ni e\), there exists \(n_r\in S^3\) such that

\[
\frac12\operatorname{Re}\operatorname{Tr}(U_r)=u\cdot n_r.
\]

The upper-envelope source satisfies

\[
X_{r,\eta}
\le
\mathbf1_{C_r},
\qquad
C_r=\{u\in S^3:u\cdot n_r\le a\},
\qquad
a=1-(t-\eta).
\]

Thus the near-field part of source stability is a finite-dimensional spherical cap problem under a vMF measure on \(S^3\).

The local cap-intersection condition is

\[
\boxed{
\nu_e(C_p\cap C_A)
\le
C_{\rm LCI}q_\eta\,\nu_e(C_A)
}
\tag{1.6.3}
\]

for every

\[
A\subset \{r\ne p:r\ni e\}.
\]

Because a link in four dimensions is incident to only six plaquettes, \(A\) has at most five elements. This is independent of lattice volume. The non-Abelian local dynamics have been compressed into the intersection geometry of finitely many caps on \(S^3\).

**Novelty.** The exact vMF\(_4\) heat-bath law is not a numerical sanity check; it is the local mathematical engine producing the \(q_\eta\) source cost.

### 1.6.3 Stage III: Balaban far-source factorization

Split the source set into

\[
S=S_{\rm inc}(e)\cup S_{\rm far}(e),
\]

where \(S_{\rm inc}(e)\) consists of plaquettes sharing the selected heat-bath link \(e\). LCI controls \(S_{\rm inc}\). Far sources do not enter the one-link integral directly. They affect \(X_p\) only by distorting the environment \(U_{e^c}\), hence the staple \(H_e\), the vMF parameters, and the cap normals.

The required far-source theorem is

\[
\boxed{
\mathbb E_{\mu^{S_{\rm far},s}}
\left[
X_{p,\eta}\mathbf1_{\mathcal G_{e,p}^{\rm LCI}}
\right]
\le
Cq_\eta
\exp\left(\sum_{r\in S_{\rm far}}J(p,r)\right),
}
\tag{1.6.4}
\]

with

\[
J(p,r)\le C_Je^{-m_Jd_C(p,r)}.
\]

This is the source-weighted Bałaban locality input. The massive block Green's function / random-walk expansion should supply the exponential kernel; the source-weighted upgrade must show that positive tilts of size \(O(q_\eta^{-1})\) do not destroy that locality.

Combining the incident LCI estimate and far-source estimate gives TOS+J:

\[
\boxed{
\mathbb E_{\mu^{S,s}}X_{p,\eta}
\le
Cq_\eta
\exp\left(\sum_{r\in S}J(p,r)\right).
}
\tag{1.6.5}
\]

Then TOS+J implies the positive source-radius bound, and the positive source-radius bound implies Lemma Q.

### 1.6.4 Closure chain

The unified analytic core is therefore

\[
\boxed{
\mathrm{LCI}_{\rm good}
+
\mathrm{BFS}_{\rm far}
\Rightarrow
\mathrm{TOS{+}J}
\Rightarrow
Z_A(\rho/q_\eta)\le e^{K|A|}
\Rightarrow
\mathrm{Lemma\ Q}.
}
\tag{1.6.6}
\]

Then the deterministic PMBSF spine gives

\[
\boxed{
\mathrm{Lemma\ Q}
+
\mathrm{SWB}
+
\mathrm{BBG}
\Rightarrow
\mathrm{projected\ firewall\ closure}.
}
\tag{1.6.7}
\]

This is the central derivation chain of the manuscript.


---

## 2. Lattice setup and source definitions

Let \(T_L^4=(\mathbb Z/L\mathbb Z)^4\). The SU(2) Wilson measure on link variables is

\[
\mu_{L,\beta}(dU)
=
Z_{L,\beta}^{-1}
\exp\left\{
\frac{\beta}{2}\sum_p\operatorname{Re}\operatorname{Tr}(U_p)
\right\}
\prod_\ell dH(U_\ell),
\]

where \(dH\) is Haar measure on SU(2).

Define the plaquette excess

\[
\phi_p(U)=1-\frac12\operatorname{Re}\operatorname{Tr}(U_p).
\]

Fix a threshold \(t\) and smoothing scale \(\eta>0\). The proof-friendly smooth source is the upper-envelope ramp

\[
X_{p,\eta}
=
\operatorname{clip}
\left(
\frac{\phi_p-t}{\eta}+1,
0,
1
\right).
\]

Then

\[
\mathbf1_{\{\phi_p\ge t\}}
\le
X_{p,\eta}
\le
\mathbf1_{\{\phi_p\ge t-\eta\}}.
\]

Let

\[
q_\eta=\mathbb E_{\mu_{L,\beta}}X_{p,\eta}.
\]

By translation invariance, \(q_\eta\) is independent of \(p\).

For rooted estimates, use a local observable \(Y_{p_0}\) satisfying

\[
0\le Y_{p_0}\le X_{p_0,\eta}.
\]

Typical rooted sources include

\[
Y_{p_0}=X_{p_0,\eta}\mathbf1_{\rm bad}
\]

or, in the refined LCI formulation,

\[
Y_{p_0}^{\rm LCI}
=
X_{p_0,\eta}\mathbf1_{(\mathcal G_{e,p_0}^{\rm LCI})^c}.
\]

---

## 3. Block geometry and Lemma Q

Let \(C\) be a Bałaban block and \(C^\circ\) its shaved core. Let \(\mathcal F_{C^c}\) denote the exterior link sigma-field. For a frozen exterior boundary \(\xi\), write

\[
\mu_C^\xi
\]

for the corresponding block Gibbs measure.

### 3.1 Lemma Q

Lemma Q states that, on suitable tempered exterior boundaries, there is a constant \(C_Q\) such that for all finite

\[
B\subset \mathcal P(C^\circ),
\]

one has

\[
\boxed{
\mathbb E_{\mu_C^\xi}
\prod_{p\in B}X_{p,\eta}
\le
(C_Qq_\eta)^{|B|}.
}
\tag{Q}
\]

The rooted version is

\[
\boxed{
\mathbb E_{\mu_C^\xi}
\left[
Y_{p_0}\prod_{p\in B}X_{p,\eta}
\right]
\le
(C_Qq_\eta)^{|B|}
\mathbb E_{\mu_C^\xi}Y_{p_0}.
}
\tag{Q-root}
\]

This point is important: the correct theorem should be stated for tempered or high-probability exterior boundaries, with the bad-boundary complement absorbed by a separate spike/rooted budget. A uniform adversarial-boundary theorem is likely too strong.

### 3.2 Tempered-boundary formulation

The pointwise statement of Lemma Q should not be read as a uniform assertion over arbitrary adversarial exterior link configurations. The Wilson measure has full support, and rare exterior boundaries can plausibly force high-defect geometry inside the block.

The correct formulation is:

\[
\boxed{
\xi\in\mathcal T_C
\Longrightarrow
\mathbb E_{\mu_C^\xi}\prod_{p\in B}X_{p,\eta}
\le
(C_Qq_\eta)^{|B|},
}
\tag{3.1}
\]

where \(\mathcal T_C\) is a tempered-boundary event, and the complement \(\mathcal T_C^c\) is handled by a separate spike/rooted budget. A usable definition of \(\mathcal T_C\) should require:

1. local heat-bath geometry sufficient for LCI-good on a shaved core;
2. no exterior-driven defect sheet entering \(C^\circ\);
3. localized small-field Green-function decay inside the block;
4. compatibility with the source-weighted Bałaban expansion.

Thus Lemma Q should be stated as a **tempered-block theorem**, not as a global adversarial-boundary theorem.


### 3.3 Cavity-intensity sufficient form

Define

\[
\lambda_p(S;\xi)
=
\frac{
\mathbb E_{\mu_C^\xi}
\left[
X_{p,\eta}\prod_{r\in S}X_{r,\eta}
\right]
}{
\mathbb E_{\mu_C^\xi}
\left[
\prod_{r\in S}X_{r,\eta}
\right]
}.
\]

A sufficient condition for Lemma Q is

\[
\boxed{
\lambda_p(S;\xi)
\le
q_\eta
\exp\left(
\sum_{r\in S}J(p,r)
\right),
\qquad
J(p,r)\le C_Je^{-m_Jd_C(p,r)}.
}
\tag{3.1}
\]

Indeed, ordering \(B=\{p_1,\ldots,p_n\}\),

\[
\mathbb E_{\mu_C^\xi}\prod_{i=1}^nX_{p_i,\eta}
=
\prod_{i=1}^n
\lambda_{p_i}(\{p_1,\ldots,p_{i-1}\};\xi),
\]

so (3.1) gives

\[
\mathbb E_{\mu_C^\xi}\prod_{p\in B}X_{p,\eta}
\le
q_\eta^{|B|}
\exp\left(
\sum_{i=1}^n\sum_{j<i}J(p_i,p_j)
\right).
\]

If

\[
\sup_p\sum_rJ(p,r)\le \log C_Q,
\]

then Lemma Q follows.

The positive source-radius route below is a sharper way to prove the same type of estimate.

---

## 4. Positive source-radius route

For \(A\subset \mathcal P(C^\circ)\), define

\[
Z_A(s)
=
\mathbb E_{\mu_C^\xi}
\prod_{p\in A}(1+sX_{p,\eta}),
\qquad s\ge0.
\]

### Proposition 4.1 — positive source-radius bound implies Lemma Q

Assume that for some \(\rho>0\) and \(K<\infty\),

\[
\boxed{
Z_A(\rho/q_\eta)\le e^{K|A|}
}
\tag{4.1}
\]

for every finite \(A\subset C^\circ\). Then Lemma Q holds with

\[
C_Q=e^K/\rho.
\]

#### Proof

Expand

\[
Z_A(s)=
\sum_{B\subset A}
s^{|B|}
\mathbb E_{\mu_C^\xi}\prod_{p\in B}X_{p,\eta}.
\]

All coefficients are nonnegative. Taking \(A=B\) and \(s=\rho/q_\eta\),

\[
(\rho/q_\eta)^{|B|}
\mathbb E_{\mu_C^\xi}\prod_{p\in B}X_{p,\eta}
\le
Z_B(\rho/q_\eta)
\le
e^{K|B|}.
\]

Therefore,

\[
\mathbb E_{\mu_C^\xi}\prod_{p\in B}X_{p,\eta}
\le
(e^K\rho^{-1}q_\eta)^{|B|}.
\]

This proves Lemma Q. \(\square\)

The rooted version follows by applying the same argument under the rooted base measure

\[
d\mu^Y=\frac{Y_{p_0}}{\mathbb E_{\mu_C^\xi}Y_{p_0}}\,d\mu_C^\xi.
\]

---

## 5. Positive tilted one-source stability

For \(S\subset C^\circ\) and \(0\le s\le\rho/q_\eta\), define

\[
d\mu^{S,s}
=
\frac{
\prod_{r\in S}(1+sX_{r,\eta})
}{
\mathbb E_{\mu_C^\xi}
\prod_{r\in S}(1+sX_{r,\eta})
}
\,d\mu_C^\xi.
\]

The target estimate is:

\[
\boxed{
\mathbb E_{\mu^{S,s}}X_{p,\eta}
\le
Cq_\eta
\exp\left(\sum_{r\in S}J(p,r)\right),
\qquad
J(p,r)\le C_Je^{-m_Jd_C(p,r)}.
}
\tag{TOS+J}
\]

### Proposition 5.1 — TOS+J implies positive source-radius

Assume TOS+J and

\[
J_*=\sup_p\sum_{r\ne p}J(p,r)<\infty.
\]

Then

\[
Z_A(\rho/q_\eta)
\le
\exp(\rho C e^{J_*}|A|).
\]

#### Proof

Order \(A=\{p_1,\ldots,p_n\}\) and define

\[
A_j=\{p_1,\ldots,p_j\}.
\]

Then

\[
\frac{Z_{A_j}(s)}{Z_{A_{j-1}}(s)}
=
1+s\,\mathbb E_{\mu^{A_{j-1},s}}X_{p_j,\eta}.
\]

Using TOS+J,

\[
\mathbb E_{\mu^{A_{j-1},s}}X_{p_j,\eta}
\le
Cq_\eta
\exp\left(\sum_{i<j}J(p_j,p_i)\right)
\le
Cq_\eta e^{J_*}.
\]

At \(s=\rho/q_\eta\),

\[
\frac{Z_{A_j}(\rho/q_\eta)}{Z_{A_{j-1}}(\rho/q_\eta)}
\le
1+\rho C e^{J_*}
\le
\exp(\rho C e^{J_*}).
\]

Multiplying over \(j\) proves the claim. \(\square\)

Combining Proposition 5.1 with Proposition 4.1 gives

\[
\boxed{
\text{TOS+J}\Rightarrow\text{Lemma Q}.
}
\]

---

## 6. Exact SU(2) heat-bath and spherical caps

Represent SU(2) as unit quaternions \(S^3\). Fix a link \(e\). Conditional on all links except \(e\), the Wilson action involving \(U_e=u\in S^3\) has the form

\[
\beta\,u\cdot\overline H_e+\text{constant}.
\]

Thus the one-link conditional is

\[
\boxed{
U_e\mid U_{e^c}
\sim
\mathrm{vMF}_4
\left(
\frac{\overline H_e}{\|H_e\|},
\beta\|H_e\|
\right).
}
\tag{6.1}
\]

For each incident plaquette \(r\ni e\), there is a unit vector \(n_r\in S^3\) such that

\[
\frac12\operatorname{Re}\operatorname{Tr}(U_r)=u\cdot n_r.
\]

Since

\[
X_{r,\eta}\le \mathbf1_{\{\phi_r\ge t-\eta\}},
\]

we have

\[
X_{r,\eta}
\le
\mathbf1_{C_r},
\qquad
C_r=\{u:u\cdot n_r\le a\},
\qquad
a=1-(t-\eta).
\]

Thus the incident-source part of TOS+J is a spherical cap-intersection problem for a \(\mathrm{vMF}_4\) measure.

For a single cap, let

\[
\rho_r=m_e\cdot n_r.
\]

The support height is

\[
\sup_{u\cdot n_r\le a}m_e\cdot u
=
F(\rho_r,a)
=
\rho_ra+\sqrt{1-\rho_r^2}\sqrt{1-a^2}.
\]

The one-cap cost is

\[
\Delta_r=1-F(\rho_r,a).
\]

A Laplace estimate gives

\[
\nu(C_r)\lesssim \mathrm{poly}(\kappa_e)e^{-\kappa_e\Delta_r}.
\]

This is the one-link cap suppression seed. It is not, by itself, Lemma Q.

---

## 7. Local cap-intersection stability

Fix a target plaquette \(p\ni e\). For an incident set \(A\subset\{r\ne p:r\ni e\}\), define

\[
C_A=\bigcap_{r\in A}C_r.
\]

Let

\[
\nu_{\kappa,m}(du)=Z_\kappa^{-1}e^{\kappa m\cdot u}\,d\sigma_{S^3}(u).
\]

### Definition 7.1 — LCI

Local cap-intersection stability for \((e,p)\) is the estimate

\[
\boxed{
\nu_{\kappa,m}(C_p\cap C_A)
\le
C_{\rm LCI}q_\eta\,\nu_{\kappa,m}(C_A)
}
\tag{LCI}
\]

for every incident subset \(A\subset\{r\ne p:r\ni e\}\).

Since a four-dimensional link is incident to six plaquettes, \(A\) has at most five elements.

### Proposition 7.2 — LCI controls all incident positive tilts

Let

\[
d\nu^{B,s}
=
\frac{
\prod_{r\in B}(1+s\mathbf1_{C_r})
}{
\int\prod_{r\in B}(1+s\mathbf1_{C_r})\,d\nu
}
d\nu,
\qquad
0\le s\le\rho/q_\eta.
\]

If LCI holds, then

\[
\nu^{B,s}(C_p)\le C_{\rm LCI}q_\eta.
\]

#### Proof

Expand:

\[
\int_{C_p}\prod_{r\in B}(1+s\mathbf1_{C_r})\,d\nu
=
\sum_{A\subset B}s^{|A|}\nu(C_p\cap C_A).
\]

Using LCI,

\[
\nu(C_p\cap C_A)\le C_{\rm LCI}q_\eta\,\nu(C_A).
\]

Therefore,

\[
\int_{C_p}\prod_{r\in B}(1+s\mathbf1_{C_r})\,d\nu
\le
C_{\rm LCI}q_\eta
\sum_{A\subset B}s^{|A|}\nu(C_A).
\]

The sum on the right is the normalizing denominator. Dividing proves the claim. \(\square\)

---

## 8. Support-height criterion for LCI

For any incident set \(A\), define

\[
h(A)=\sup_{u\in C_A}m\cdot u,
\qquad
\Delta(A)=1-h(A).
\]

The incremental cost of adding \(C_p\) is

\[
\Delta_p(A)=\Delta(A\cup\{p\})-\Delta(A)
=
h(A)-h(A\cup\{p\}).
\]

Under nondegenerate exposed-maximizer hypotheses, Laplace comparison gives

\[
\nu(C_p\mid C_A)
\le
C_{\rm geom}\kappa^M e^{-\kappa\Delta_p(A)}.
\]

Thus LCI follows if

\[
\Delta_p(A)
\ge
\Delta_q+\frac{M\log\kappa+\log C_{\rm geom}+O(1)}{\kappa},
\]

where \(q_\eta\asymp e^{-\kappa\Delta_q}\) at the local heat-bath scale.

Let

\[
u_A\in\arg\max_{u\in C_A}m\cdot u.
\]

If

\[
u_A\cdot n_p\le a,
\]

then \(u_A\in C_p\), so

\[
\Delta_p(A)=0.
\]

Thus LCI fails. A computable sufficient good event is

\[
\boxed{
\mathcal G_{e,p}^{\rm LCI}
=
\left\{
\forall A\subset\{r\ne p:r\ni e\},
\quad
u_A\cdot n_p-a\ge\chi_0
\right\}.
}
\]

With a uniform curvature/nondegeneracy bound, this implies

\[
\Delta_p(A)\ge c_{\rm curv}\chi_0^2.
\]

The complement is treated as rooted:

\[
Y_p^{\rm LCI}
=
X_{p,\eta}\mathbf1_{(\mathcal G_{e,p}^{\rm LCI})^c}.
\]

---

## 9. The finite-dimensional LCI theorem target

The most concrete standalone analytic target is the following finite-dimensional statement.

### Theorem target 9.1 — Spherical cap increment theorem on \(S^3\)

Let

\[
\nu_{\kappa,m}(du)=Z_\kappa^{-1}e^{\kappa m\cdot u}\,d\sigma_{S^3}(u),
\qquad
m\in S^3.
\]

Let

\[
C_i=\{u\in S^3:u\cdot n_i\le a\}
\]

be a finite family of caps with common threshold \(a=1-(t-\eta)\). For a target cap \(C_p\), assume that for every incident subset \(A\subset\{r\ne p:r\ni e\}\):

1. \(C_A\) has a nondegenerate exposed maximizer

   \[
   u_A\in\arg\max_{u\in C_A}m\cdot u;
   \]

2. the target cap is violated at that maximizer with uniform margin

   \[
   u_A\cdot n_p-a\ge \chi_0;
   \]

3. the constrained support problem has uniform curvature lower bound \(c_{\rm curv}>0\).

Then

\[
h(A)-h(A\cup\{p\})\ge c\chi_0^2,
\]

where

\[
h(A)=\sup_{u\in C_A}m\cdot u.
\]

Consequently,

\[
\nu_{\kappa,m}(C_p\mid C_A)
\le
C_{\rm geom}\kappa^M e^{-\kappa c\chi_0^2}.
\]

If

\[
c\chi_0^2
\ge
\Delta_q+\frac{M\log\kappa+\log C_{\rm geom}+O(1)}{\kappa},
\]

then

\[
\nu_{\kappa,m}(C_p\mid C_A)\le Cq_\eta.
\]

This theorem would prove LCI on the local good event \(\mathcal G_{e,p}^{\rm LCI}\). The remaining SU(2) probability problem is then to prove that \(\mathcal G_{e,p}^{\rm LCI}\) is typical or has rooted/absorbed complement under the Wilson block measure.


## 9. Far-source stability

The LCI theorem controls only sources that share the selected heat-bath link \(e(p)\). Split

\[
S=S_{\rm inc}(e)\cup S_{\rm far}(e),
\]

where

\[
S_{\rm inc}(e)=\{r\in S:r\ni e\}.
\]

The far sources do not enter the one-link vMF integral directly. They change the environment \(U_{e^c}\), and therefore change

\[
H_e,\quad m_e,\quad \kappa_e,\quad n_r,\quad \mathcal G_{e,p}^{\rm LCI}.
\]

The needed Bałaban/Dimock input is

\[
\boxed{
\mathbb E_{\mu^{S_{\rm far},s}}
\left[
X_{p,\eta}\mathbf1_{\mathcal G_{e,p}^{\rm LCI}}
\right]
\le
Cq_\eta
\exp\left(\sum_{r\in S_{\rm far}}J(p,r)\right),
}
\tag{9.1}
\]

with

\[
J(p,r)\le C_Je^{-m_Jd_C(p,r)}.
\]

The rooted version is

\[
\boxed{
\mathbb E_{\mu^{Y,S_{\rm far},s}}
\left[
X_{a,\eta}\mathbf1_{\mathcal G_{e,a}^{\rm LCI}}
\right]
\le
Cq_\eta
\exp\left(J(a,p_0)+\sum_{r\in S_{\rm far}}J(a,r)\right).
}
\tag{9.2}
\]

This is the exact source-weighted Bałaban stability target.

---

## 10. LCI + far-source stability imply TOS+J

Condition on \(U_{e^c}\). Incident source factors produce a finite positive tilt of the one-link vMF law. By LCI,

\[
\mathbb E
\left[
X_{p,\eta}
\mid U_{e^c},S_{\rm inc}\text{-tilt},\mathcal G_{e,p}^{\rm LCI}
\right]
\le
Cq_\eta.
\]

Now integrate over \(U_{e^c}\) under the far-source tilted measure. By (9.1), far sources contribute only

\[
\exp\left(\sum_{r\in S_{\rm far}}J(p,r)\right).
\]

Since incident sources are finite-range, their contribution is absorbed into \(C\) or into \(J(p,r)\) for \(d(p,r)\le O(1)\). Therefore,

\[
\boxed{
\mathbb E_{\mu^{S,s}}
\left[
X_{p,\eta}\mathbf1_{\mathcal G_{e,p}^{\rm LCI}}
\right]
\le
Cq_\eta
\exp\left(\sum_{r\in S}J(p,r)\right).
}
\]

The LCI-bad contribution is handled by the rooted observable \(Y_p^{\rm LCI}\). Thus:

\[
\boxed{
\text{LCI-good typicality + far-source stability}
\Rightarrow
\text{TOS+J}.
}
\]

Combining with Sections 4 and 5 proves:

\[
\boxed{
\text{LCI-good typicality + far-source stability}
\Rightarrow
\text{Lemma Q}.
}
\]

---


## 11. Source-weighted Bałaban criterion

The previous sections reduce Lemma Q to two inputs:

\[
\text{LCI-good typicality}
\quad\text{and}\quad
\text{far-source stability}.
\]

This section states the source-weighted Bałaban criterion that should deliver the far-source stability estimate.

Let \(E_\Gamma^\xi\) denote a local polymer activity produced by a Bałaban/Dimock block expansion under frozen exterior boundary \(\xi\), where \(\Gamma\subset C^\circ\) is a connected plaquette polymer. Introduce source variables \(u=(u_p)_{p\in C^\circ}\) by deforming the block partition function to

\[
Z_C^\xi(u)
=
\mathbb E_{\mu_C^\xi}
\prod_{p\in C^\circ}(1+u_pX_{p,\eta}).
\]

A source-marked activity coefficient has the form

\[
E_{\Gamma,R}^\xi
=
[u_R]E_\Gamma^\xi(u),
\qquad
R\subset \Gamma.
\]

The desired marked activity estimate is

\[
\boxed{
|E_{\Gamma,R}^\xi|
\le
q_\eta^{|R|}
\epsilon(\beta,\eta)^{|\Gamma|}
e^{-m_0d_M(\Gamma)}.
}
\tag{11.1}
\]

Here \(d_M(\Gamma)\) is the tree length of \(\Gamma\) in the coarse \(M\)-block metric, and \(\epsilon(\beta,\eta)\) must be below the Kotecký–Preiss convergence threshold.

### 11.1 Why the ordinary expansion is insufficient

The unmarked Bałaban/Dimock expansion supplies estimates of the type

\[
|E_{\Gamma,\varnothing}^\xi|
\le
\epsilon(\beta)^{|\Gamma|}
e^{-m_0d_M(\Gamma)}.
\]

For PMBSF, this is not enough. The rare-source problem requires one explicit \(q_\eta\) factor for each marked plaquette source. Therefore the needed upgrade is not merely convergence of the polymer expansion, but convergence in the source-weighted norm

\[
\|E_\Gamma^\xi\|_{q}
:=
\sum_{R\subset \Gamma}
q_\eta^{-|R|}
|E_{\Gamma,R}^\xi|.
\]

A suitable sufficient estimate is

\[
\boxed{
\|E_\Gamma^\xi\|_{q}
\le
\epsilon_q^{|\Gamma|}
e^{-m_0d_M(\Gamma)}
}
\tag{11.2}
\]

with \(\epsilon_q<\epsilon_{\rm KP}\).

### 11.2 Large fields under source insertions

A useful monotonicity observation is:

\[
0\le X_{p,\eta}\le1.
\]

Therefore, for a positive real source tilt with \(s\ge0\),

\[
\prod_{p\in R}(1+sX_{p,\eta})
\le
(1+s)^{|R|}.
\]

For hard large-field suppression estimates, source insertions do not worsen the underlying large-field stability if the source factors are treated through the positive source-radius route. Large-field regions are still suppressed by the ordinary large-field mechanism. The new burden lies in the small-field/source-marked estimates and in controlling how far positive source tilts distort the heat-bath local geometry.

### 11.3 Far-source stability as a marked expansion estimate

The far-source stability estimate required in Section 9 is

\[
\mathbb E_{\mu^{S_{\rm far},s}}
\left[
X_{p,\eta}\mathbf1_{\mathcal G_{e,p}^{\rm LCI}}
\right]
\le
Cq_\eta
\exp\left(\sum_{r\in S_{\rm far}}J(p,r)\right),
\tag{11.3}
\]

with

\[
J(p,r)\le C_Je^{-m_Jd_C(p,r)}.
\]

A source-weighted polymer expansion should yield (11.3) by expressing the logarithm of the tilted block partition function as a sum of connected source-marked activities. Far sources can influence the selected heat-bath link only through connected polymers joining their support to a neighborhood of \(p\). Localized Green-function/random-walk decay supplies the exponential kernel.

Thus the far-source theorem is not an independent mystery. It is the marked version of the usual locality statement:

\[
\boxed{
\text{source-marked connected polymers joining }p\text{ to }r
\text{ are exponentially suppressed in }d_C(p,r).
}
\]

---

## 12. Boundary-band gate

The smooth source satisfies

\[
\mathbf1_{\{\phi_p\ge t\}}
\le
X_{p,\eta}
\le
\mathbf1_{\{\phi_p\ge t-\eta\}}.
\]

To pass from smooth sources to hard sources, one must control the boundary band

\[
B_{p,\eta}
=
\mathbf1_{\{t-\eta\le \phi_p<t\}}.
\]

Since

\[
0\le X_{p,\eta}-\mathbf1_{\{\phi_p\ge t\}}
\le
B_{p,\eta},
\]

a sufficient boundary-band gate is

\[
\boxed{
\sum_Y
\mathbb E
\left[
\sum_{r\in Y}B_{r,\eta}
\right]
\mathcal W_\theta(Y)
\le
\varepsilon_{\rm bdry}(\eta)
\sum_Yq^{|Y|}\mathcal W_\theta(Y),
\qquad
\varepsilon_{\rm bdry}(\eta)\to0.
}
\tag{12.1}
\]

Here \(Y\) runs over source polymers and \(\mathcal W_\theta(Y)\) is the same projected-capacity/polymer weight used in the PMBSF expansion.

This is not yet proved. It is listed separately because it is logically distinct from Lemma Q. Lemma Q is a fixed-\(\eta\) rare-source theorem. The boundary-band gate is the hard-threshold passage.

---

## 13. Deterministic PMBSF spine

This section records the deterministic operator part of the paper. It does not depend on SU(2) probability.

Let \(P=P_{\le\Lambda,L}\) be the physical/transverse Maxwell projector. For each plaquette \(p\), define

\[
A_p=P\mathbf1_{\partial p}P.
\]

Then

\[
\operatorname{tr}(A_pA_q)
=
\sum_{e\in\partial p}
\sum_{f\in\partial q}
|P(e,f)|^2.
\tag{13.1}
\]

The polymer-type ordered trace-overlap condition is

\[
\boxed{
\sup_p
\sum_q e^{-md(p,q)}
\frac{\operatorname{tr}(A_pA_q)}{\kappa_\Lambda^2}
\le
C_{\rm PTO}.
}
\tag{13.2}
\]

If the source theorem gives

\[
|\operatorname{Cov}(X_p,X_q)|
\le
Cq_\eta^2e^{-md(p,q)},
\tag{13.3}
\]

then

\[
\sum_q
|\operatorname{Cov}(X_p,X_q)|
\operatorname{tr}(A_pA_q)
\le
CC_{\rm PTO}q_\eta^2\kappa_\Lambda^2.
\tag{13.4}
\]

This is the PTO level-(iii) estimate.

For a defect potential \(V_D\), define the projected Birman–Schwinger statistic

\[
\Theta_D
=
\|M^{-1/2}PV_DP M^{-1/2}\|.
\tag{13.5}
\]

If

\[
\Theta_D<1,
\tag{13.6}
\]

then

\[
M^{-1/2}(M-PV_DP)M^{-1/2}
=
I-M^{-1/2}PV_DP M^{-1/2}
\succeq
(1-\Theta_D)I.
\]

Therefore,

\[
\boxed{
M-PV_DP\succeq (1-\Theta_D)M.
}
\tag{13.7}
\]

This is the deterministic projected firewall criterion.

---

## 14. Numerical evidence

The numerical evidence is not a proof. It supports the plausibility of the open local source-stability theorem.

### 14.1 Exact heat-bath side-8 anchor

The side-8 frozen-block run used exact SU(2) heat-bath sampling for both global generation and frozen-block resampling. At

\[
L=16,\qquad
\beta=3.5,\qquad
q_\eta=0.003,\qquad
\eta=0.005,
\]

the main reported values were:

\[
\operatorname{median}\Lambda=0.9249,
\qquad
\max\Lambda=1.4626,
\]

\[
\operatorname{median}\Lambda_{\rm root}=0.9563,
\qquad
\max\Lambda_{\rm root}=1.3998.
\]

This remains the compact primary conditional-sampling anchor.

### 14.2 Exact heat-bath side-10/core-margin-3 Stage B

The geometry-robustness run is

\[
\texttt{PMBSF\_SU2\_LemmaQ\_block\_conditional\_stageB\_heatbath\_20260525\_215913}.
\]

Configuration:

\[
L=16,\qquad
\beta=3.5,\qquad
q_\eta=0.003,\qquad
\eta=0.005.
\]

The exact update law was

\[
U_\ell\sim
\mathrm{vMF}_4
\left(
\frac{\overline H_\ell}{\|H_\ell\|},
\beta\|H_\ell\|
\right).
\]

The block geometry was side \(10\), core margin \(3\), \(64\) frozen-boundary blocks, \(864\) core plaquettes per block, and distance bins through \(d=12\).

Thresholding gave

\[
t=1.0104245908659366,
\qquad
q_\eta=0.003000000000000041,
\qquad
q_{\rm hard}=0.0029478073120117188.
\]

Main diagnostics:

\[
\max_{\rm depth}\operatorname{median}(q_{\rm cond}/q_\eta)=1.3020833,
\]

\[
q95(q_{\rm cond}/q_\eta)=2.6041667,
\qquad
\max(q_{\rm cond}/q_\eta)=9.1145833.
\]

Ordinary cavity:

\[
\max\Lambda=2.5930038,
\qquad
\operatorname{median}\Lambda=1.0158112.
\]

Rooted cavity:

\[
\max\Lambda_{\rm root}=2.3431348,
\qquad
\operatorname{median}\Lambda_{\rm root}=1.0221089.
\]

Cap predictors had correct signs but weak explanatory power:

\[
\text{slope}_g=-0.17918134,
\qquad
R_g^2=0.0075893205,
\]

\[
\text{slope}_\rho=-8.33064,
\qquad
R_\rho^2=0.022467109.
\]

This supersedes the earlier Metropolis side-10 Stage B run as the primary geometry-robustness anchor.

### 14.3 Full-volume pair/rooted covariance

The full-volume diagnostics test the \(k=1\) consequence:

\[
|\operatorname{Cov}(X_p,X_q)|
\le
Cq_\eta^2e^{-md(p,q)}.
\]

The retained \(L=64\) ledger reports:

\[
q_\eta=0.0030061514,
\qquad
q_{\rm hard}=0.0030000228,
\]

\[
\max|\operatorname{Cov}(X,X)|/q_\eta^2=0.86578135,
\]

\[
\operatorname{median}=0.0067171416.
\]

Rooted:

\[
\max=0.89244247,
\qquad
\operatorname{median}=0.0074250476.
\]

This supports the pair/rooted consequence of Lemma Q through \(L=64\), pending artifact-packaged citation of the \(L=64\) run.

### 14.4 Numerical hierarchy

The numerical hierarchy is now:

1. **Primary compact conditional anchor:** exact heat-bath side-8.
2. **Primary geometry-robustness anchor:** exact heat-bath side-10/core-margin-3 Stage B.
3. **Global consequence evidence:** full-volume pair/rooted covariance through \(L=64\).
4. **Deterministic spine evidence:** projected Birman–Schwinger/PTO/random plaquette-incidence diagnostics.

The older Metropolis side-10 Stage B run is historical only.

---

## 15. Central conditional theorem

### Theorem 15.1 — Conditional projected-capacity firewall closure

Assume:

1. **LCI-good typicality.** Typical/tempered SU(2) heat-bath geometry satisfies LCI for incident cap families, with rooted absorption of the LCI-bad complement.
2. **Bałaban far-source stability.** Far positive source tilts distort LCI-good source rates only by an exponentially summable kernel \(J\).
3. **Source-weighted Bałaban expansion.** Lemma Q propagates to rooted cumulants and pair/rooted covariance closure.
4. **Boundary-band gate.** The smooth-source estimates pass to hard sources as \(\eta\to0\).

Then the projected-capacity firewall closure holds in the finite spectral-window setting.

The proof chain is

\[
\text{LCI-good typicality + far-source stability}
\Rightarrow
\text{TOS+J}
\Rightarrow
\text{positive source-radius}
\Rightarrow
\text{Lemma Q}.
\]

Then

\[
\text{Lemma Q}
\Rightarrow
\text{rooted source cumulants}
\Rightarrow
\text{pair/rooted covariance closure}
\Rightarrow
\text{PTO level-(iii)}
\Rightarrow
\text{projected Birman--Schwinger firewall}.
\]

This theorem is conditional. Its hypotheses include the current open analytic work.

---

## 16. Open analytic tasks

The remaining proof tasks are:

1. **LCI-good typicality.** Prove that typical/tempered SU(2) heat-bath geometry satisfies

   \[
   \nu(C_p\cap C_A)\le Cq_\eta\nu(C_A)
   \]

   for incident cap families, with rooted absorption of the complement.

2. **Balaban far-source stability.** Prove that far positive source tilts distort the LCI-good part only by

   \[
   \exp\left(\sum_{r\in S}Ce^{-md(p,r)}\right).
   \]

3. **Source-weighted Bałaban expansion.** Upgrade the standard unmarked polymer activities to marked source activities carrying \(q_\eta^{|R|}\).

4. **Boundary-band gate.** Prove the \(\eta\to0\) passage from the smooth upper-envelope source to the hard high-plaquette indicator.

5. **Continuum layer.** This paper does not address the \(a\to0\) continuum construction, OS reconstruction, nontriviality, or the Clay-level mass-gap theorem.

---

## 17. Referee-facing status table

| Component | Status | Role |
|---|---|---|
| Projected comparator \(A_p=P\mathbf1_{\partial p}P\) | deterministic | operator spine |
| PTO trace-overlap summability framework | deterministic / finite-dimensional | converts pair covariance to projected-capacity control |
| Birman–Schwinger firewall criterion | deterministic | coercivity if \(\Theta_D<1\) |
| Exact SU(2) heat-bath law | exact local identity | vMF cap formulation |
| Single-cap suppression | local analytic seed | one-source rarity on good geometry |
| LCI-good typicality | open | controls incident source tilts |
| Bałaban far-source stability | open | controls nonlocal source distortion |
| TOS+J \(\Rightarrow\) Lemma Q | proved reduction | positive source-radius route |
| Lemma Q | open | local rare-source factorization |
| Source-weighted Bałaban expansion | open | propagates Lemma Q to cumulants |
| Boundary-band gate | open | smooth-to-hard source passage |
| Exact-HB side-8 diagnostics | numerical support | primary compact conditional anchor |
| Exact-HB side-10 Stage B | numerical support | primary geometry-robustness anchor |
| \(L=64\) pair/rooted covariance | numerical support | global \(k=1\) consequence evidence |
| Clay mass gap | not proved | outside current manuscript scope |

---

## 18. Referee-risk register

### Risk 1: “This does not prove the Yang--Mills mass gap.”

Correct. The manuscript should explicitly agree. The claim is a conditional finite-lattice projected-capacity firewall framework plus targeted evidence for its local SU(2) probability input.

### Risk 2: “Lemma Q is still open.”

Correct. The manuscript contribution is the reduction of Lemma Q to the sharper LCI/TOS+J interface, plus proof of the positive source-radius reductions. Lemma Q is not claimed.

### Risk 3: “The exact-HB diagnostics are numerical, not proofs.”

Correct. They support the plausibility of TOS+J and LCI/rooted stability; they do not establish them.

### Risk 4: “The Bałaban machinery is not yet source-weighted.”

Correct. The paper identifies source-weighted Bałaban expansion as an open input. It does not claim the unmarked expansion automatically implies the marked one.

### Risk 5: “The \(L=64\) covariance result needs an artifact citation.”

Correct. The manuscript should either include the \(L=64\) run artifact in the supplementary package or downgrade the \(L=64\) claim to an internal ledger statement.

### Risk 6: “The cap predictor has low \(R^2\).”

Correct. The manuscript should not claim that one-link cap regression explains Lemma Q. The data support block source-stability; the cap geometry supplies a local seed, not the full theorem.

### Risk 7: “Tempered boundaries must be defined precisely.”

Correct. The next analytic pass should give a formal definition of \(\mathcal T_C\) and state the corresponding bad-boundary absorption theorem.


### Risk 8: “The positive source-radius bound is just Lemma Q in disguise.”

Partly, but this is the point of the reduction. The manuscript proves that the radius estimate implies Lemma Q by positivity, then identifies TOS+J as a smaller one-source stability theorem sufficient to prove the radius estimate. TOS+J is local and incremental; Lemma Q is a full product moment theorem.

### Risk 9: “LCI handles only incident plaquettes.”

Correct. That is the intended split. LCI is finite-dimensional and local; far plaquettes are assigned to the Bałaban far-source stability theorem. The manuscript should not imply that LCI alone proves Lemma Q.


## 19. Manuscript-safe statement

The correct claim is:

> We reduce SU(2) projected-capacity firewall closure to local cap-intersection stability plus Bałaban far-source stability, and we provide exact heat-bath finite-volume diagnostics supporting the resulting positive-tilt source-stability mechanism.

The incorrect claim is:

> We prove the SU(2) Yang–Mills mass gap.

The status is:

\[
\boxed{
\text{serious conditional theorem architecture + targeted exact heat-bath evidence; not a closed proof.}
}
\]

---

## 20. References placeholder

The final manuscript should include precise bibliography entries for:

- Wilson lattice gauge theory.
- Bałaban’s constructive gauge-theory papers.
- Dimock’s expository reconstruction of the Bałaban expansion.
- Kotecký–Preiss cluster expansion.
- Fernández–Procacci refined polymer convergence.
- Kennedy–Pendleton SU(2) heat-bath algorithm.
- von Mises–Fisher distribution references.
- Spherical cap asymptotics / convex-geometric Laplace estimates.
- Random-current/source-set analogues for comparison, clearly marked as abelian/Ising analogues, not direct SU(2) inputs.


---

## Appendix A. Pass 3.2 editorial note

This pass is not a new proof of Lemma Q. Its purpose is to harden the manuscript against overclaiming by making the dependency graph explicit.

The most important retained distinction is:

\[
\boxed{
\text{proved reductions}
\ne
\text{open SU(2) probability theorem}.
}
\]

The next actual analytic work should focus on the finite-dimensional LCI theorem target and the formal definition of tempered boundaries \(\mathcal T_C\).


## Appendix B. Pass 3.3 analytic-core note

Pass 3.3 consolidates the manuscript around two analytic innovations:

1. **Positive source-radius partition function.** The product-moment statement of Lemma Q is converted into a real-positive generating-function radius estimate. This avoids complex zero-free issues and additive cluster-mixing losses.

2. **Local cap-intersection geometry.** The exact SU(2) heat-bath law converts incident source stability into a finite-dimensional cap-intersection theorem on \(S^3\). This sequesters the non-Abelian one-link geometry into a local object independent of lattice volume.

The remaining global work is then exactly the Bałaban far-source factorization theorem. This is the correct division of labor between SU(2) geometry and constructive RG locality.
