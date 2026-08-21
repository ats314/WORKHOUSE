# SU(3) Outside-Core Coercivity: Phase Plan + Working Lemmas (One-Link → Strip → Probability)

This note is a **workable formalization** of the 4-step plan:

1. Define the SU(3) **aligned Cartan locus** at one link.
2. Quantify a **local cancellation / coercivity lemma** away from that locus.
3. Lift one-link coercivity to **strip coercivity** via incidence combinatorics.
4. Control the **probability / capacity** of near-alignment in the strip (large \(\beta\)).

Throughout:
- Gauge group \(G=\mathrm{SU}(3)\) with the bi-invariant Hilbert–Schmidt metric
  \(\langle X,Y\rangle := -\tfrac12\operatorname{Tr}(XY)\) on \(\mathfrak{su}(3)\).
- Plaquette defect (fundamental character proxy):
  \[
  \widetilde z(g):=1-\frac13\Re\operatorname{Tr}(g)\in[0,2].
  \]
- Wilson action at fixed cutoff:
  \[
  S_\beta(U)=\beta\sum_{p\in P(\Lambda)}\widetilde z(U_p).
  \]

---

## Phase 1 — Define the one-link forces and the aligned Cartan locus

### 1.1 One-link geometry and "plaquette forces"

Fix an oriented link \(\ell\) (a directed edge). Let \(p_1,\dots,p_m\) be the plaquettes incident to \(\ell\).  
In \(d=4\), \(m=2(d-1)=6\).

For each incident plaquette \(p_j\), write its holonomy as
\[
U_{p_j}(U)= A_j(U)\,U_\ell^{\sigma_j}\,B_j(U),
\qquad \sigma_j\in\{+1,-1\},
\]
where \(A_j,B_j\) are words in the neighboring links (length \(\le 3\)).

Define the (right-trivialized) **single-plaquette force in group variables**
\[
X(g):=\nabla_G \widetilde z(g)\in\mathfrak{su}(3).
\]
A direct variation computation (right multiplication \(g\mapsto g e^{tX}\)) gives the explicit formula
\[
X(g)=\frac13\,\Big(g-g^\dagger\Big)_0,
\tag{F1}
\]
where \((\cdot)_0\) denotes traceless anti-Hermitian projection (trace part is irrelevant for pairing with \(\mathfrak{su}(3)\)).

Then the link gradient of the **unscaled** plaquette sum
\[
F(U):=\sum_{p}\widetilde z(U_p)
\]
has the canonical “transported force sum” form
\[
\nabla_\ell F(U)=\sum_{j=1}^m \operatorname{Ad}_{g_j(U)}\,X\!\big(U_{p_j}(U)\big),
\tag{F2}
\]
where \(g_j(U)\in \mathrm{SU}(3)\) is a local transport built from \(A_j,B_j\) and the sign \(\sigma_j\).
(Equivalently, one can write \(\nabla_\ell S_\beta=\beta\,\nabla_\ell F\).)

> **Key structural point.** Each \(X(U_{p_j})\) lies in the Lie algebra of the centralizer of \(U_{p_j}\).
For regular \(U_{p_j}\), that centralizer is a conjugate Cartan.

---

### 1.2 The aligned Cartan locus \(\mathcal A_\ell\)

Fix the standard Cartan subalgebra
\[
\mathfrak t
=
\left\{
\operatorname{diag}(i a, i b, -i(a+b)):\ a,b\in\mathbb R
\right\},
\quad
T=\exp(\mathfrak t)\subset \mathrm{SU}(3),
\quad
N(T)=\{g:\ gTg^{-1}=T\}.
\]

Let \(\mathfrak t_h:=\operatorname{Ad}_h\mathfrak t\) and \(T_h:=hTh^{-1}\).

**Definition (aligned Cartan locus at \(\ell\)).**
\(\mathcal A_\ell\) is the set of local configurations \(U\) around \(\ell\) for which there exists \(h\in \mathrm{SU}(3)\) such that:

1. **All incident plaquette holonomies lie in the same maximal torus:**
   \[
   U_{p_j}(U)\in T_h\qquad\text{for all }j,
   \]
   so automatically \(X(U_{p_j}(U))\in\mathfrak t_h\).

2. **All transports preserve that torus:**
   \[
   g_j(U)\in N(T_h)\qquad\text{for all }j,
   \]
   so \(\operatorname{Ad}_{g_j}\mathfrak t_h=\mathfrak t_h\).

Equivalently, after conjugation by \(h^{-1}\), all transported forces in (F2) lie in \(\mathfrak t\):
\[
\operatorname{Ad}_{h^{-1}}\operatorname{Ad}_{g_j(U)}X(U_{p_j}(U))\in \mathfrak t.
\]

This is the SU(3) analogue of the SU(2) “axis alignment” locus:
it is the local condition for the star neighborhood to be **gauge-abelianized**.

---

### 1.3 A quantitative near-alignment score

For \(\eta>0\), define the **near-alignment event** at \(\ell\) by the existence of a torus \(T_h\) such that:

- each incident plaquette holonomy is \(\eta\)-close to \(T_h\), and
- each transport \(g_j\) is \(\eta\)-close to \(N(T_h)\),

measured in the bi-invariant Riemannian distance \(d_G\):
\[
\mathsf{NearAlign}_\ell(\eta)
:=
\Big\{
\exists h:\ 
\max_j d_G\big(U_{p_j},T_h\big)\le \eta,
\ \max_j d_G\big(g_j,N(T_h)\big)\le \eta
\Big\}.
\tag{NA}
\]

Then
\[
\mathcal A_\ell = \bigcap_{\eta>0}\mathsf{NearAlign}_\ell(\eta).
\]

---

## Phase 2 — Quantify the SU(3) local cancellation / coercivity lemma

### 2.1 Single-plaquette force size away from the center critical set

For SU(3),
\[
X(g)=\tfrac13(g-g^\dagger)_0,
\quad
|X(g)| = |\nabla_G \widetilde z(g)|.
\]

On the **small/medium defect regime** \(\widetilde z(g)\in[0,1]\) one expects a uniform bound
\[
|X(g)|\ \ge\ \kappa_3\,\sqrt{\widetilde z(g)}
\quad\text{for some absolute }\kappa_3>0,
\tag{SP}
\]
because the only nontrivial critical points of \(\widetilde z\) (besides identity) occur at center elements (\(\widetilde z=3/2\)).

A conservative constant that is empirically safe is \(\kappa_3\approx 0.5\).
(One can compute the exact infimum numerically on the Weyl alcove if desired.)

---

### 2.2 Local coercivity away from near-alignment (target lemma)

Fix \(\varepsilon\in(0,1]\) and \(\eta>0\). Define the one-link “rough star” event:
\[
\mathsf{Rough}_\ell(\varepsilon)
:=
\Big\{
\max_{1\le j\le m}\widetilde z(U_{p_j})\ge \varepsilon
\Big\}.
\tag{R}
\]

**Lemma (local coercivity away from Cartan alignment; quantitative target).**  
There exists an explicit function \(c_{\mathrm{geom}}(\eta)\in(0,1]\) such that on
\[
\mathsf{Rough}_\ell(\varepsilon)\ \cap\ \mathsf{NearAlign}_\ell(\eta)^c
\]
one has the lower bound
\[
\boxed{
|\nabla_\ell F(U)|
\ \ge\
c_{\mathrm{geom}}(\eta)\,\kappa_3\,\sqrt{\varepsilon}.
}
\tag{LC}
\]

Equivalently for the action:
\[
|\nabla_\ell S_\beta(U)|
\ \ge\
\beta\,c_{\mathrm{geom}}(\eta)\,\kappa_3\,\sqrt{\varepsilon}.
\]

**Interpretation.**  
Away from near-abelianization of the star at \(\ell\), a single rough plaquette forces a definite amount of link-level force.

> This is the SU(3) replacement for the SU(2) compactness-based constant \(c_{\mathrm{loc}}(\varepsilon,\beta,\tau)\).

**How to make \(c_{\mathrm{geom}}(\eta)\) explicit.**  
One concrete route is to show: on \(\mathsf{NearAlign}_\ell(\eta)^c\), there exists at least one incident plaquette whose transported force has a root-space component of size \(\gtrsim \eta\) of its norm, and **root-space components in distinct root planes are orthogonal**. That yields a Pythagorean lower bound on the sum.

---

## Phase 3 — Lift one-link coercivity to strip coercivity (combinatorics)

Let
\[
B(U):=\frac{1}{|P|}\sum_{p}\widetilde z(U_p)=\frac{F(U)}{|P|}.
\]

Define a boundary strip \(\Sigma=\{\varepsilon<B<\varepsilon+\delta\}\) for some fixed \(\delta>0\).

### 3.1 Counting rough plaquettes from an average defect

If \(B\ge \varepsilon\) and \(\widetilde z\le 2\), then for the threshold \(\varepsilon/2\),
\[
| \{p:\widetilde z(U_p)\ge \varepsilon/2\}|
\ \ge\
\frac{(\varepsilon-\varepsilon/2)|P|}{2}
=
\frac{\varepsilon}{4}|P|.
\tag{C1}
\]

### 3.2 From rough plaquettes to rough links

Each plaquette touches 4 links; each link is touched by at most \(\nu=6\) plaquettes in \(d=4\).
Hence the number of links incident to at least one \(\varepsilon/2\)-rough plaquette is at least
\[
|E_{\mathrm{rough}}|
\ \ge\
\frac{4}{\nu}\cdot \frac{\varepsilon}{4}|P|
=
\frac{\varepsilon}{6}|P|.
\tag{C2}
\]
Since \(|P|=\tfrac32|E|\) on a 4D hypercubic lattice, this becomes
\[
|E_{\mathrm{rough}}|\ \ge\ \frac{\varepsilon}{4}|E|.
\]

### 3.3 Global gradient lower bound except for near-alignment exceptions

Using \(\|\nabla F\|^2=\sum_{\ell\in E}\|\nabla_\ell F\|^2\), combine (LC) and (C2) to get:
\[
\|\nabla F\|^2
\ \ge\
|E_{\mathrm{rough}}\setminus E_{\mathrm{NA}}|\;
c_{\mathrm{geom}}(\eta)^2\,\kappa_3^2\,\frac{\varepsilon}{2},
\tag{C3}
\]
where \(E_{\mathrm{NA}}\) denotes the set of near-aligned links.

Thus, unless a large fraction of rough links are near-aligned, one gets a uniform lower bound on \(\|\nabla F\|^2\) on the strip.

This is the deterministic combinatorial lifting step.

---

## Phase 4 — Control probability/capacity of near-alignment in the strip (large \(\beta\))

### 4.1 Local codimension heuristic (why near-alignment should be small)

For generic \(g\in \mathrm{SU}(3)\), its centralizer is a 2D torus (dimension 2).  
Requiring another element to commute with it forces that element into the same torus: codimension \(8-2=6\).

At a link \(\ell\), near-alignment requires several incident plaquette holonomies and transports to be simultaneously close to a common torus/normalizer, producing a **high-codimension tubular neighborhood**.

Heuristic: for fixed \(\eta\ll 1\),
\[
\mu_{\mathrm{Haar}}(\mathsf{NearAlign}_\ell(\eta))
\ \lesssim\
C\,\eta^{c_*},
\quad c_*\approx 6(m-1)-8\ \ (\text{still } >0 \text{ for }m=6).
\tag{P1}
\]
This becomes exponentially small in volume if it must occur on a positive density of links.

### 4.2 Energy suppression at large \(\beta\) on the strip

On the strip \(B\in[\varepsilon,\varepsilon+\delta]\),
\[
S_\beta(U)=\beta|P|B(U)\ \ge\ \beta\varepsilon |P|.
\]
So the Gibbs density contributes an exponential suppression factor \(e^{-\beta\varepsilon|P|}\) for **every** configuration in the strip, independent of alignment considerations.

Thus, for large \(\beta\), the strip itself can be exponentially rare, and near-alignment inside it can be negligible even with a crude bound.

### 4.3 Capacity alternative

Even if probability is not tiny, one can attempt a **capacity** bound:
show \(\mathsf{NearAlign}(\eta)\) has sufficiently small capacity for the diffusion generated by \(L\),
so that barrier/gluing arguments can tolerate failures of pointwise strip drift on this set.

This is structurally similar to “polar set” handling in stratified maximum principles.

---

## Summary: What remains genuinely hard

- Making \(c_{\mathrm{geom}}(\eta)\) explicit (Phase 2) requires a precise **root-space transversality** statement:
  away from near-normalizer transports, root components cannot cancel across different plaquettes.
- Proving a clean probability or capacity estimate (Phase 4) depends on whether the strip is chosen in a regime where
  energy suppression dominates, or whether one needs a purely geometric measure/capacity argument.

