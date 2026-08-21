# 2. Lattice Yang–Mills setup and Euclidean measure

This section fixes the lattice Yang–Mills model at a finite ultraviolet cutoff and pins down the basic objects that will be used in the analytic chain later: the configuration manifold, the gauge action, plaquette holonomies, the Wilson action, the Euclidean Gibbs measure, and the class of local observables whose correlations we aim to control.

Unless stated otherwise, we work in Euclidean spacetime dimension **4**. We reserve the index
\(\mu=0\) for the **Euclidean time** direction and \(\mu\in\{1,2,3\}\) for spatial directions.

We also fix once and for all:

* a compact Lie group \(G\) with identity \(\mathbf 1\),
* a faithful unitary representation \(\rho:G\to U(n)\) (so \(n\) is fixed),
* the associated trace \(\mathrm{Tr}\) on \(\mathbb C^{n\times n}\).

The **inverse coupling** is \(\beta>0\). A physical lattice spacing \(a>0\) can be inserted by rescaling distances and time-translation steps; the combinatorial definitions below do not depend on \(a\). The OS Hamiltonian conversion in Part 11 will use that one Euclidean time-step corresponds to a physical time increment \(a\).

---

## 2.1 Spacetime lattice, edges, plaquettes, orientation conventions

### 2.1.1 The periodic four–torus lattice

Fix integers \(L_0,L_1,L_2,L_3\ge 1\) and define the finite periodic lattice
\[
\Lambda\;:=\;\prod_{\mu=0}^3 (\mathbb Z/L_\mu\mathbb Z).
\]
We write \(x\in\Lambda\) as \(x=(x_0,x_1,x_2,x_3)\), and all arithmetic in each coordinate is understood modulo \(L_\mu\). Let \(\hat e_\mu\) denote the \(\mu\)-th standard basis vector.

For later reflection-positivity arguments (Part 4), one typically assumes \(L_0\) is even so that the reflection hyperplane can be placed *between* two time slices. We will impose that hypothesis explicitly when needed; nothing in this section requires it.

### 2.1.2 Oriented links (edges)

Define the set of **positively oriented** nearest-neighbor links
\[
E(\Lambda)\;:=\;\{(x,\mu):\ x\in\Lambda,\ \mu\in\{0,1,2,3\}\}.
\]
A link \(b=(x,\mu)\in E(\Lambda)\) is the directed edge from the **tail** \(\partial_- b:=x\) to the **head** \(\partial_+ b:=x+\hat e_\mu\).

It is often convenient to speak about *all* oriented links, including negative directions. We therefore introduce the extended notation
\[
(x,-\mu)\quad\text{for the directed edge from }x\text{ to }x-\hat e_\mu.
\]
Whenever a quantity is defined only on \(E(\Lambda)\), we extend it to negative directions by the standard identification
\[
(x,-\mu)\equiv (x-\hat e_\mu,\mu)^{-1}.
\]
This convention will be used implicitly whenever inverses appear in holonomy words.

### 2.1.3 Oriented plaquettes

Define the set of **positively oriented plaquettes**
\[
P(\Lambda)\;:=\;\big\{(x;\mu,\nu):\ x\in\Lambda,\ 0\le \mu<\nu\le 3\big\}.
\]
The plaquette \(p=(x;\mu,\nu)\) is the elementary square in the \((\mu,\nu)\)-plane with basepoint \(x\), oriented counterclockwise when viewed from the positive \((\mu,\nu)\)-normal.

Its ordered boundary links are
\[
\partial p=(b_1,b_2,b_3,b_4)
:=\big((x,\mu),\ (x+\hat e_\mu,\nu),\ (x+\hat e_\nu,\mu),\ (x,\nu)\big),
\]
and the oriented boundary traversal is
\[
(x,\mu)\ \cdot\ (x+\hat e_\mu,\nu)\ \cdot\ (x+\hat e_\nu,\mu)^{-1}\ \cdot\ (x,\nu)^{-1}.
\]
Equivalently, the boundary consists of the four *positively oriented* links \(b_1,\dots,b_4\), where \(b_1,b_2\) appear with exponent \(+1\) and \(b_3,b_4\) appear with exponent \(-1\) in the plaquette holonomy word.

It will be useful (especially in Part 3) to encode this by incidence signs
\[
\varepsilon_{b,p}\in\{-1,0,+1\},\qquad
\varepsilon_{b,p}=
\begin{cases}
+1,& b\in\{b_1,b_2\},\\
-1,& b\in\{b_3,b_4\},\\
0,& \text{otherwise.}
\end{cases}
\]

### 2.1.4 Basic cardinalities

Because \(\Lambda\) is a periodic \(4\)-torus,
\[
|\Lambda|=\prod_{\mu=0}^3 L_\mu,\qquad |E(\Lambda)|=4|\Lambda|,\qquad |P(\Lambda)|=\binom{4}{2}|\Lambda|=6|\Lambda|.
\]
These relations will be used frequently to keep track of which constants are volume-independent.

---

## 2.2 Configuration space and gauge group action

### 2.2.1 Configuration manifold

A **lattice gauge field configuration** is an assignment of a group element to each positively oriented link:
\[
M_\Lambda\;:=\;G^{E(\Lambda)}
\;=\;\{U=(U_b)_{b\in E(\Lambda)}:\ U_b\in G\}.
\]
We routinely write \(U_{x,\mu}\) for \(U_{(x,\mu)}\).

**Orientation convention.** We extend \(U\) to negatively oriented links by
\[
U_{x,-\mu}\;:=\;U_{x-\hat e_\mu,\mu}^{-1}.
\tag{2.1}
\]
This ensures that if a path traverses a link against its positive orientation, the holonomy uses the group inverse.

### 2.2.2 Gauge group and its action

The (finite-volume) **gauge group** is the vertex-wise product
\[
\mathcal G_\Lambda\;:=\;G^{\Lambda}
\;=\;\{g=(g_x)_{x\in\Lambda}:\ g_x\in G\}.
\]
It acts on configurations by the usual left–right transformation
\[
(g\cdot U)_{x,\mu}\;:=\;g_x\,U_{x,\mu}\,g_{x+\hat e_\mu}^{-1}.
\tag{2.2}
\]
This action is smooth and preserves the orientation convention (2.1).

Two configurations \(U,V\in M_\Lambda\) are **gauge equivalent** if \(V=g\cdot U\) for some \(g\in\mathcal G_\Lambda\).

A function \(F:M_\Lambda\to\mathbb C\) is **gauge invariant** if
\(F(g\cdot U)=F(U)\) for all \(g\in\mathcal G_\Lambda\).

---

## 2.3 Plaquette holonomy and Wilson action

### 2.3.1 Holonomy along lattice paths

Let \(\gamma\) be an oriented lattice path consisting of a sequence of nearest-neighbor oriented links
\(\gamma=(b_1,\dots,b_k)\), where each \(b_i\) may be a positively oriented link or a negatively oriented link.

The (ordered) **path holonomy** is
\[
U_\gamma(U)\;:=\;U_{b_1}(U)\,U_{b_2}(U)\cdots U_{b_k}(U),
\tag{2.3}
\]
where negatively oriented links are interpreted via (2.1).

### 2.3.2 Plaquette holonomy

For an oriented plaquette \(p=(x;\mu,\nu)\in P(\Lambda)\) with \(\mu<\nu\), the **plaquette holonomy** is the holonomy around its boundary:
\[
U_p(U)
:=
U_{x,\mu}\,U_{x+\hat e_\mu,\nu}\,U_{x+\hat e_\nu,\mu}^{-1}\,U_{x,\nu}^{-1}.
\tag{2.4}
\]
This is the fundamental gauge-covariant “curvature” variable.

Lemma 2.1 (gauge covariance of plaquette holonomy).
For \(p=(x;\mu,\nu)\in P(\Lambda)\) and \(g\in\mathcal G_\Lambda\),
\[
U_p(g\cdot U)\;=\;g_x\,U_p(U)\,g_x^{-1}.
\tag{2.5}
\]

Proof.
Insert (2.2) into the plaquette word (2.4). Every interior vertex factor cancels telescopically, leaving only conjugation by the gauge element at the basepoint \(x\).
\(\square\)

In particular, any **conjugation-invariant** class function of \(U_p\) is automatically gauge invariant.

### 2.3.3 Wilson plaquette potential and action

Define the (representation-based) **trace defect**
\[
\widetilde z:G\to\mathbb R,\qquad
\widetilde z(g):=1-\frac{1}{n}\Re\,\mathrm{Tr}(\rho(g)).
\tag{2.6}
\]
This is a smooth conjugation-invariant function with a strict minimum at \(\mathbf 1\) (faithfulness of \(\rho\) is used for strictness).

The **single-plaquette Wilson potential** at inverse coupling \(\beta>0\) is
\[
\Phi_\beta(g)\;:=\;\beta\,\widetilde z(g)
\;=\;\beta\Bigl(1-\frac{1}{n}\Re\,\mathrm{Tr}(\rho(g))\Bigr),
\qquad g\in G.
\tag{2.7}
\]

The **Wilson action** on \(M_\Lambda\) is
\[
S_{\Lambda,\beta}(U)
\;:=\;
\sum_{p\in P(\Lambda)}\Phi_\beta\big(U_p(U)\big).
\tag{2.8}
\]
We will often abbreviate \(S_W:=S_{\Lambda,\beta}\) when \(\Lambda\) and \(\beta\) are held fixed.

Lemma 2.2 (nonnegativity and the vacuum configuration).
For all \(g\in G\), \(\widetilde z(g)\ge 0\). Moreover \(\widetilde z(g)=0\) iff \(g=\mathbf 1\). Consequently,
\(S_{\Lambda,\beta}(U)\ge 0\) for all \(U\in M_\Lambda\), and the unique global minimizer is the **vacuum configuration**
\[
U^{(0)}\in M_\Lambda,\qquad U^{(0)}_b\equiv \mathbf 1\ \text{for all }b\in E(\Lambda),
\tag{2.9}
\]
with \(S_{\Lambda,\beta}(U^{(0)})=0\).

Proof.
Because \(\rho(g)\in U(n)\), all eigenvalues lie on the unit circle, so
\(\Re\,\mathrm{Tr}(\rho(g))\le n\), hence \(\widetilde z(g)\ge 0\). If \(\widetilde z(g)=0\), then \(\Re\,\mathrm{Tr}(\rho(g))=n\), which forces all eigenvalues of \(\rho(g)\) to equal \(1\), hence \(\rho(g)=I_n\). Faithfulness of \(\rho\) gives \(g=\mathbf 1\).
\(\square\)

Lemma 2.3 (gauge invariance of the Wilson action).
For all \(g\in\mathcal G_\Lambda\) and \(U\in M_\Lambda\),
\(S_{\Lambda,\beta}(g\cdot U)=S_{\Lambda,\beta}(U)\).

Proof.
By Lemma 2.1, \(U_p\) transforms by conjugation. Since \(\widetilde z\) (equivalently \(\Phi_\beta\)) is a class function, \(\Phi_\beta(g_x U_p g_x^{-1})=\Phi_\beta(U_p)\) for each plaquette \(p\). Summing over \(p\) gives the claim.
\(\square\)

Remark 2.4 (locality).
Each plaquette term in (2.8) depends only on the **four** link variables in \(\partial p\). This strict locality is the combinatorial reason that later stability and coercivity estimates depend on bounded-overlap constants rather than on the total number of plaquettes.

---

## 2.4 Euclidean Gibbs measure (Haar × Wilson)

### 2.4.1 Haar reference measure

Let \(dg\) denote the normalized Haar probability measure on \(G\). The canonical reference measure on the configuration space is the product Haar measure
\[
d\mu_{\mathrm{Haar}}(U)
\;:=\;
\prod_{b\in E(\Lambda)} dg(U_b).
\tag{2.10}
\]
Because \(G\) is compact, \(\mu_{\mathrm{Haar}}\) is a probability measure on \(M_\Lambda\).

(Part 3 will also view \(M_\Lambda\) as a compact Riemannian manifold with a product bi-invariant metric; for that metric, the Riemannian volume form coincides with Haar, up to the normalization convention.)

### 2.4.2 The Wilson Gibbs measure

Define the finite-volume **Euclidean Gibbs measure**
\[
d\mu_{\Lambda,\beta}(U)
\;:=\;
Z_{\Lambda,\beta}^{-1}\,e^{-S_{\Lambda,\beta}(U)}\,d\mu_{\mathrm{Haar}}(U),
\tag{2.11}
\]
where the partition function is
\[
Z_{\Lambda,\beta}:=\int_{M_\Lambda} e^{-S_{\Lambda,\beta}(U)}\,d\mu_{\mathrm{Haar}}(U)\in(0,\infty).
\tag{2.12}
\]
We write \(\mu(F):=\int F\,d\mu\) for expectations when \(\Lambda,\beta\) are clear.

Lemma 2.5 (gauge invariance of \(\mu_{\Lambda,\beta}\)).
The measure \(\mu_{\Lambda,\beta}\) is gauge invariant: for every measurable \(A\subseteq M_\Lambda\) and every \(g\in\mathcal G_\Lambda\),
\[
\mu_{\Lambda,\beta}(g\cdot A)=\mu_{\Lambda,\beta}(A).
\tag{2.13}
\]
Equivalently, for every integrable \(F\), \(\mu_{\Lambda,\beta}(F\circ(g\cdot))=\mu_{\Lambda,\beta}(F)\).

Proof.
The product Haar measure is invariant under left and right multiplication in each coordinate, hence invariant under the gauge action (2.2). Lemma 2.3 gives \(S_W(g\cdot U)=S_W(U)\). Thus the density \(e^{-S_W}\) is invariant as well.
\(\square\)

### 2.4.3 Lattice translations

For any lattice vector \(y\in\Lambda\), define the configuration translation \(\tau_y:M_\Lambda\to M_\Lambda\) by
\[
(\tau_y U)_{x,\mu}:=U_{x-y,\mu},
\tag{2.14}
\]
where subtraction is modulo \(L_\mu\) in each coordinate.

Lemma 2.6 (translation invariance of \(\mu_{\Lambda,\beta}\)).
For every \(y\in\Lambda\) and every integrable \(F\),
\(\mu_{\Lambda,\beta}(F\circ\tau_y)=\mu_{\Lambda,\beta}(F)\).

Proof.
The product Haar measure is translation invariant by relabeling link coordinates, and the action \(S_W\) is a sum of identical plaquette terms, hence invariant under the induced relabeling of plaquettes.
\(\square\)

We will use translations mainly in the Euclidean time direction \(\mu=0\), where \(\tau_{n\hat e_0}\) implements time shifts by \(n\) lattice steps (physical time \(na\)).

---

## 2.5 Local observables, supports, covariances, and time translations

The quantitative statements later (clustering, OS mass-gap conversion) are about correlations of **local** observables: functions depending on finitely many link variables.

### 2.5.1 Local observables and link support

A (bounded) observable \(F:M_\Lambda\to\mathbb C\) is called **local** (or a **cylinder function**) if there exists a finite subset \(A\subseteq E(\Lambda)\) such that \(F(U)\) depends only on \(\{U_b: b\in A\}\).

Definition 2.7 (link support).
For a local observable \(F\), define its **link support** \(\mathrm{supp}_E(F)\subseteq E(\Lambda)\) to be the *minimal* such set \(A\) (with respect to inclusion).

Remarks.
1. If \(F\) is smooth, an equivalent characterization is: \(b\notin\mathrm{supp}_E(F)\) iff the derivative of \(F\) in the \(b\)-coordinate vanishes identically (i.e. all linkwise directional derivatives in that coordinate are zero).
2. Gauge-invariant local observables include Wilson loops \(U\mapsto \Re\,\mathrm{Tr}(\rho(U_\gamma(U)))\) for closed loops \(\gamma\), as well as local functions of finitely many plaquette holonomies.

### 2.5.2 Translations on observables

Translations act on observables by pullback:
\[
(\tau_y F)(U):=F(\tau_{-y}U).
\tag{2.15}
\]
Translation invariance of \(\mu_{\Lambda,\beta}\) (Lemma 2.6) then reads \(\mu(\tau_y F)=\mu(F)\).

### 2.5.3 Covariances

For integrable observables \(F,G\), define the covariance
\[
\mathrm{Cov}_{\mu}(F,G)
:=\mu(FG)-\mu(F)\mu(G).
\tag{2.16}
\]
(When working with complex-valued observables in the OS framework, one often uses sesquilinear forms \(\mu(\overline{F}G)\); the relevant antilinear involution is introduced in Part 4.)

The covariance is invariant under translations:
\[
\mathrm{Cov}_\mu(\tau_y F,\tau_y G)=\mathrm{Cov}_\mu(F,G),
\tag{2.17}
\]
and if \(F\) is replaced by its centered version \(F^\circ:=F-\mu(F)\), then
\(\mathrm{Cov}_\mu(F,G)=\mu(F^\circ G^\circ)\).

### 2.5.4 Distances between supports

To state exponential clustering, we need a notion of separation between local supports. There are multiple equivalent choices on a periodic lattice; we record the two that will appear later.

1. **Vertex distance.** Let \(\mathrm{dist}_V(x,y)\) be the graph distance on \(\Lambda\) induced by nearest-neighbor steps (with periodic wrap-around). For link sets \(A,B\subseteq E(\Lambda)\), define
\[
\mathrm{dist}_V(A,B):=\min\{\mathrm{dist}_V(\partial_- b,\partial_- b'):\ b\in A,\ b'\in B\},
\tag{2.18}
\]
or any equivalent endpoint-based variant.

2. **Link adjacency distance.** Later (Part 6.5 and Part 9) we use the distance adapted to the finite-range structure of the Maxwell operator: declare links \(b\sim b'\) adjacent if they co-appear in the boundary of some plaquette, and let \(\mathrm{dist}_E(b,b')\) be the induced graph distance on \(E(\Lambda)\). For link supports \(A,B\), set
\[
\mathrm{dist}_E(A,B):=\min\{\mathrm{dist}_E(b,b'):\ b\in A,\ b'\in B\}.
\tag{2.19}
\]
This is the metric in which we will prove exponential decay of the Green kernel of the massive Maxwell operator.

3. **Time separation.** For OS mass-gap conversion, the relevant separation is along the time direction. If \(\pi_0(x)=x_0\) is the time coordinate, we set
\[
\mathrm{dist}_0(A,B):=\min\{|x_0-y_0|_{\mathrm{per}}:\ x\in\mathcal V(A),\ y\in\mathcal V(B)\},
\tag{2.20}
\]
where \(\mathcal V(A)\) denotes the set of vertices incident to links in \(A\), and \(|\cdot|_{\mathrm{per}}\) is the periodic distance on \(\mathbb Z/L_0\mathbb Z\). In infinite volume this becomes the usual absolute difference in \(\mathbb Z\).

Remark 2.8.
The precise choice of distance is mostly bookkeeping: on bounded-degree graphs, all the natural notions of separation are comparable up to constants. What matters for the later Combes–Thomas argument is that the operator under study has finite range with respect to the chosen adjacency.

---

This completes the model-level setup. Part 3 equips \(M_\Lambda\) with its product Riemannian geometry and develops the cochain calculus \((d_0,d_1)\) that will identify the vacuum Wilson Hessian with a discrete Maxwell operator.
