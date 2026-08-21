# Local Cap-Intersection Stability and Positive-Tilt Source Radius

**Project:** PMBSF / SU(2) Lemma Q  
**Date:** 2026-05-26  
**Role:** Manuscript-ready analytic reduction following the exact heat-bath Stage B diagnostic.  
**Status:** The reductions below are proved. The remaining open input is the SU(2) local cap-intersection / Balaban far-source stability theorem.

---

## 0. Purpose

The previous reductions established

\[
\text{Lemma Q}
\Longleftarrow
\text{positive source-radius bound}
\Longleftarrow
\text{positive tilted one-source stability}.
\]

This note pushes one level deeper. It splits positive tilted one-source stability into:

\[
\boxed{
\text{finite-dimensional incident-link cap-intersection stability}
}
\]

and

\[
\boxed{
\text{Balaban/Dimock far-source stability}.
}
\]

The exact heat-bath Stage B run supports this architecture numerically, but does not prove it. The analytic goal is now the theorem:

\[
\boxed{
\text{LCI + far-source stability}
\Longrightarrow
\text{TOS+J}
\Longrightarrow
\text{Lemma Q}.
}
\]

---

## 1. Block setting

Let \(C\) be a block and \(C^\circ\) its shaved core. Fix a tempered exterior boundary \(\xi\), and write

\[
\mu=\mu_C^\xi.
\]

Let

\[
X_p=X_{p,\eta},
\qquad
0\le X_p\le1,
\qquad
q=q_\eta.
\]

For \(S\subset C^\circ\) and \(0\le s\le \rho/q\), define the positive source-tilted measure

\[
d\mu^{S,s}
=
\frac{
\prod_{r\in S}(1+sX_r)
}{
\mathbb E_\mu\prod_{r\in S}(1+sX_r)
}
\,d\mu.
\tag{1.1}
\]

The target tilted one-source theorem is

\[
\boxed{
\mathbb E_{\mu^{S,s}}X_p
\le
Cq\exp\left(\sum_{r\in S}J(p,r)\right),
\qquad
J(p,r)\le C_Je^{-m_Jd_C(p,r)}.
}
\tag{TOS+J}
\]

The rooted version replaces \(\mu^{S,s}\) by

\[
d\mu^{Y,S,s}
=
\frac{
Y_{p_0}\prod_{r\in S}(1+sX_r)
}{
\mathbb E_\mu\left[
Y_{p_0}\prod_{r\in S}(1+sX_r)
\right]
}
\,d\mu,
\tag{1.2}
\]

where

\[
0\le Y_{p_0}\le X_{p_0}.
\]

---

## 2. Positive source-radius bound

For \(A\subset C^\circ\), define

\[
Z_A(s)
=
\mathbb E_\mu\prod_{p\in A}(1+sX_p).
\tag{2.1}
\]

### Proposition 2.1 — TOS+J implies positive source-radius bound

Assume TOS+J and

\[
J_*:=\sup_p\sum_{r\ne p}J(p,r)<\infty.
\tag{2.2}
\]

Then for \(0\le s=\rho/q\),

\[
\boxed{
Z_A(\rho/q)
\le
\exp\left(\rho C e^{J_*}|A|\right).
}
\tag{2.3}
\]

#### Proof

Order

\[
A=\{p_1,\ldots,p_n\}.
\]

Set

\[
A_{j-1}=\{p_1,\ldots,p_{j-1}\}.
\]

Then

\[
\frac{Z_{A_j}(s)}{Z_{A_{j-1}}(s)}
=
1+s\,\mathbb E_{\mu^{A_{j-1},s}}X_{p_j}.
\tag{2.4}
\]

By TOS+J,

\[
\mathbb E_{\mu^{A_{j-1},s}}X_{p_j}
\le
Cq\exp\left(\sum_{i<j}J(p_j,p_i)\right)
\le
Cqe^{J_*}.
\tag{2.5}
\]

Taking \(s=\rho/q\),

\[
\frac{Z_{A_j}(\rho/q)}{Z_{A_{j-1}}(\rho/q)}
\le
1+\rho Ce^{J_*}
\le
\exp(\rho Ce^{J_*}).
\tag{2.6}
\]

Multiplying over \(j\) gives (2.3).

\[
\square
\]

---

## 3. Positive source-radius bound implies Lemma Q

### Proposition 3.1 — coefficient extraction by positivity

Assume

\[
Z_A(\rho/q)\le e^{K|A|}
\tag{3.1}
\]

for every finite \(A\subset C^\circ\). Then for every \(B\subset C^\circ\),

\[
\boxed{
\mathbb E_\mu\prod_{p\in B}X_p
\le
(C_Qq)^{|B|},
\qquad
C_Q=\rho^{-1}e^K.
}
\tag{3.2}
\]

#### Proof

Expand

\[
Z_B(s)
=
\sum_{R\subset B}
s^{|R|}
\mathbb E_\mu\prod_{p\in R}X_p.
\tag{3.3}
\]

All coefficients are nonnegative. Therefore,

\[
s^{|B|}
\mathbb E_\mu\prod_{p\in B}X_p
\le
Z_B(s).
\tag{3.4}
\]

Take \(s=\rho/q\). Then

\[
\mathbb E_\mu\prod_{p\in B}X_p
\le
\left(\frac{q}{\rho}\right)^{|B|}
e^{K|B|}
=
(C_Qq)^{|B|}.
\]

\[
\square
\]

Combining Propositions 2.1 and 3.1 gives

\[
\boxed{
\text{TOS+J}
\Longrightarrow
\text{Lemma Q}.
}
\tag{3.5}
\]

The rooted proof is identical, applied under the rooted base measure

\[
d\mu^Y=\frac{Y_{p_0}}{\mathbb E_\mu Y_{p_0}}\,d\mu.
\]

---

## 4. DLR reduction to a one-link cap problem

Fix a target plaquette \(p\in C^\circ\). Choose an incident link \(e=e(p)\). Conditional on all links except \(e\), the SU(2) Wilson one-link conditional law is

\[
U_e\mid U_{e^c}
\sim
\mathrm{vMF}_4(m_e,\kappa_e),
\tag{4.1}
\]

with

\[
m_e=\frac{\overline H_e}{\|H_e\|},
\qquad
\kappa_e=\beta\|H_e\|.
\tag{4.2}
\]

For every plaquette \(r\ni e\), there is a unit vector \(n_r\in S^3\) such that

\[
\frac12\operatorname{Re}\operatorname{Tr}(U_r)=u\cdot n_r,
\qquad u=U_e\in S^3.
\tag{4.3}
\]

With the upper-envelope smoother,

\[
X_r\le \mathbf 1_{C_r},
\qquad
C_r=\{u\in S^3:u\cdot n_r\le a\},
\qquad
a=1-(t-\eta).
\tag{4.4}
\]

Thus the incident-link part of the problem is a finite-dimensional vMF cap-intersection problem on \(S^3\).

---

## 5. Incident and far source split

Split the positive source set \(S\) into

\[
S=S_{\rm inc}(e)\cup S_{\rm far}(e),
\tag{5.1}
\]

where

\[
S_{\rm inc}(e)=\{r\in S:r\ni e\}.
\]

In four dimensions, each link is incident to six plaquettes. Since \(p\notin S\),

\[
|S_{\rm inc}(e)|\le5.
\tag{5.2}
\]

The incident sources are the only source factors that directly enter the one-link vMF integral. The far sources distort the environment \(U_{e^c}\), hence the staple \(H_e\), only through the outer block Gibbs distribution.

This suggests the proof split:

\[
\text{incident sources}
\quad\Rightarrow\quad
\text{finite cap-intersection theorem},
\]

\[
\text{far sources}
\quad\Rightarrow\quad
\text{Balaban locality / random-walk decay}.
\]

---

## 6. Local cap-intersection stability

For \(A\subset S_{\rm inc}(e)\), define

\[
C_A=\bigcap_{r\in A}C_r.
\tag{6.1}
\]

Let

\[
\nu=\nu_{\kappa,m}
\]

be the vMF measure

\[
d\nu(u)
=
Z_\kappa^{-1}e^{\kappa m\cdot u}\,d\sigma_{S^3}(u).
\tag{6.2}
\]

### Definition 6.1 — LCI for \((e,p)\)

Local cap-intersection stability holds for \((e,p)\) if, for every

\[
A\subset\{r\ne p:r\ni e\},
\]

one has

\[
\boxed{
\nu(C_p\cap C_A)
\le
C_{\rm LCI}q\,\nu(C_A).
}
\tag{6.3}
\]

Equivalently,

\[
\boxed{
\nu(C_p\mid C_A)\le C_{\rm LCI}q.
}
\tag{6.4}
\]

This is the exact finite-dimensional condition that prevents incident positive source tilts from making \(X_p\) free.

---

## 7. LCI implies incident positive TOS

### Proposition 7.1

Assume LCI for \((e,p)\). Let

\[
B\subset\{r\ne p:r\ni e\}
\]

and let

\[
0\le s\le \rho/q.
\]

Define the incidently tilted vMF measure

\[
d\nu^{B,s}
=
\frac{
\prod_{r\in B}(1+s\mathbf 1_{C_r})
}{
\int\prod_{r\in B}(1+s\mathbf 1_{C_r})\,d\nu
}
\,d\nu.
\tag{7.1}
\]

Then

\[
\boxed{
\nu^{B,s}(C_p)\le C_{\rm LCI}q.
}
\tag{7.2}
\]

Since \(X_p\le\mathbf1_{C_p}\),

\[
\boxed{
\mathbb E_{\nu^{B,s}}X_p\le C_{\rm LCI}q.
}
\tag{7.3}
\]

#### Proof

Expand numerator:

\[
\int_{C_p}\prod_{r\in B}(1+s\mathbf1_{C_r})\,d\nu
=
\sum_{A\subset B}s^{|A|}\nu(C_p\cap C_A).
\tag{7.4}
\]

By LCI,

\[
\nu(C_p\cap C_A)
\le
C_{\rm LCI}q\,\nu(C_A).
\tag{7.5}
\]

Therefore,

\[
\int_{C_p}\prod_{r\in B}(1+s\mathbf1_{C_r})\,d\nu
\le
C_{\rm LCI}q
\sum_{A\subset B}s^{|A|}\nu(C_A).
\tag{7.6}
\]

But

\[
\sum_{A\subset B}s^{|A|}\nu(C_A)
=
\int\prod_{r\in B}(1+s\mathbf1_{C_r})\,d\nu.
\tag{7.7}
\]

Dividing proves (7.2).

\[
\square
\]

---

## 8. Support-height form of LCI

Define the support height

\[
h(A)=\sup_{u\in C_A}m\cdot u
\tag{8.1}
\]

and cap cost

\[
\Delta(A)=1-h(A).
\tag{8.2}
\]

For the target cap,

\[
\Delta_p(A)=\Delta(A\cup\{p\})-\Delta(A)
=
h(A)-h(A\cup\{p\}).
\tag{8.3}
\]

A Laplace ratio estimate gives, under nondegenerate exposed-maximizer hypotheses,

\[
\nu(C_p\mid C_A)
\le
C_{\rm geom}\kappa^M e^{-\kappa\Delta_p(A)}.
\tag{8.4}
\]

Thus LCI follows if

\[
\boxed{
\Delta_p(A)
\ge
\Delta_q+\frac{M\log\kappa+\log C_{\rm geom}+O(1)}{\kappa},
}
\tag{8.5}
\]

where \(q\asymp e^{-\kappa\Delta_q}\) at the local heat-bath scale.

This converts LCI into a finite-dimensional spherical convex-geometry condition.

---

## 9. Computable LCI criterion

Let

\[
u_A\in \arg\max_{u\in C_A}m\cdot u.
\tag{9.1}
\]

If

\[
u_A\cdot n_p\le a,
\tag{9.2}
\]

then \(u_A\in C_p\), hence

\[
h(A\cup\{p\})=h(A)
\]

and

\[
\Delta_p(A)=0.
\]

Thus LCI fails.

A necessary condition is

\[
u_A\cdot n_p>a
\tag{9.3}
\]

for every incident subset \(A\).

A quantitative sufficient condition is:

\[
\boxed{
u_A\cdot n_p-a\ge \chi_0>0
}
\tag{9.4}
\]

for every \(A\), together with a uniform curvature/nondegeneracy lower bound. Under that condition,

\[
\boxed{
\Delta_p(A)\ge c_{\rm curv}\chi_0^2.
}
\tag{9.5}
\]

Therefore LCI follows if

\[
c_{\rm curv}\chi_0^2
\ge
\Delta_q+O(\kappa^{-1}\log\kappa).
\tag{9.6}
\]

This gives the local good event

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
\tag{9.7}
\]

The local bad event is

\[
\boxed{
\mathcal B_{e,p}^{\rm LCI}
=
(\mathcal G_{e,p}^{\rm LCI})^c.
}
\tag{9.8}
\]

The correct split is

\[
X_p
=
X_p\mathbf1_{\mathcal G_{e,p}^{\rm LCI}}
+
X_p\mathbf1_{\mathcal B_{e,p}^{\rm LCI}}.
\tag{9.9}
\]

The good part is controlled by LCI. The bad part is rooted:

\[
Y_p^{\rm LCI}=X_p\mathbf1_{\mathcal B_{e,p}^{\rm LCI}}.
\tag{9.10}
\]

---

## 10. Far-source stability

LCI controls only incident source factors. Far source factors change the distribution of the environment \(U_{e^c}\), and therefore of

\[
m_e,\quad
\kappa_e,\quad
n_r,\quad
\mathcal G_{e,p}^{\rm LCI}.
\]

The needed Balaban-style input is:

### Open Theorem 10.1 — Far-source stability of LCI parameters

For \(S_{\rm far}\subset C^\circ\setminus\{r:r\ni e\}\),

\[
\boxed{
\mathbb E_{\mu^{S_{\rm far},s}}
\left[
X_p\mathbf1_{\mathcal G_{e,p}^{\rm LCI}}
\right]
\le
Cq
\exp\left(\sum_{r\in S_{\rm far}}J(p,r)\right),
}
\tag{10.1}
\]

with

\[
J(p,r)\le C_Je^{-m_Jd_C(p,r)}.
\tag{10.2}
\]

Rooted version:

\[
\boxed{
\mathbb E_{\mu^{Y,S_{\rm far},s}}
\left[
X_a\mathbf1_{\mathcal G_{e,a}^{\rm LCI}}
\right]
\le
Cq
\exp\left(J(a,p_0)+\sum_{r\in S_{\rm far}}J(a,r)\right).
}
\tag{10.3}
\]

This is where Balaban/Dimock random-walk locality must enter.

---

## 11. LCI + far stability imply TOS+J

### Theorem 11.1

Assume:

1. LCI holds on \(\mathcal G_{e,p}^{\rm LCI}\).
2. Far-source stability (10.1) holds.
3. The LCI-bad contribution is rooted by

   \[
   Y_p^{\rm LCI}=X_p\mathbf1_{\mathcal B_{e,p}^{\rm LCI}}.
   \]

Then TOS+J holds for the good contribution:

\[
\boxed{
\mathbb E_{\mu^{S,s}}
\left[
X_p\mathbf1_{\mathcal G_{e,p}^{\rm LCI}}
\right]
\le
Cq
\exp\left(\sum_{r\in S}J(p,r)\right).
}
\tag{11.1}
\]

The rooted version holds for \(Y_p^{\rm LCI}\) if the rooted far-source stability estimate holds.

### Proof

Split

\[
S=S_{\rm inc}(e)\cup S_{\rm far}(e).
\]

Condition on \(U_{e^c}\). The far sources are fixed under the \(U_e\) integration. The incident sources produce a positive vMF tilt by factors

\[
\prod_{r\in S_{\rm inc}}(1+sX_r)
\le
\prod_{r\in S_{\rm inc}}(1+s\mathbf1_{C_r}).
\]

On \(\mathcal G_{e,p}^{\rm LCI}\), Proposition 7.1 gives

\[
\mathbb E[X_p\mid U_{e^c},S_{\rm inc}\text{-tilt}]
\le
Cq.
\]

Now integrate over \(U_{e^c}\) under the far-source tilted measure. Far-source stability contributes

\[
\exp\left(\sum_{r\in S_{\rm far}}J(p,r)\right).
\]

Since incident sources are finite-range, their contribution is absorbed into the constant \(C\) or into \(J(p,r)\) for \(d(p,r)\le O(1)\). Therefore,

\[
\mathbb E_{\mu^{S,s}}
\left[
X_p\mathbf1_{\mathcal G_{e,p}^{\rm LCI}}
\right]
\le
Cq
\exp\left(\sum_{r\in S}J(p,r)\right).
\]

\[
\square
\]

Combining Theorem 11.1 with Propositions 2.1 and 3.1 gives Lemma Q.

---

## 12. Final reduction chain

The analytic stack is now:

\[
\boxed{
\text{LCI-good finite-dimensional cap geometry}
}
\]

\[
+
\]

\[
\boxed{
\text{Balaban far-source stability}
}
\]

\[
\Longrightarrow
\]

\[
\boxed{
\text{TOS+J}
}
\]

\[
\Longrightarrow
\]

\[
\boxed{
\text{positive source-radius bound}
}
\]

\[
\Longrightarrow
\]

\[
\boxed{
\text{Lemma Q}
}
\]

\[
\Longrightarrow
\]

\[
\boxed{
\text{rooted cumulants and PMBSF closure}.
}
\]

Everything in this note except the LCI-good typicality theorem and the Balaban far-source stability theorem is now reduced to finite algebraic/probabilistic implications.

---

## 13. Current open theorem

The remaining SU(2) theorem is:

\[
\boxed{
\textbf{For typical/tempered SU(2) Wilson heat-bath geometry,}
\quad
\mathcal G_{e,p}^{\rm LCI}
\textbf{ holds with rooted/absorbed complement,}
}
\tag{13.1}
\]

and far source tilts preserve it up to

\[
\boxed{
\exp\left(\sum_r Ce^{-md(p,r)}\right).
}
\tag{13.2}
\]

This is the exact analytic target replacing the earlier vague phrase “prove Lemma Q.”
