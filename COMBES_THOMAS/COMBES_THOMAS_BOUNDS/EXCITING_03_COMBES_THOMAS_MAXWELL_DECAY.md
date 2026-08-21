# Exciting Extract 03: Combes–Thomas inverse decay for the massive Maxwell operator on the link graph

This note extracts the quantitative inverse-decay mechanism (Combes–Thomas conjugation) that turns the *operator* bound

\[
\mathrm{Cov}\ \lesssim\ \langle \nabla F,\ M^{-1}\nabla G\rangle
\]

into an explicit **exponential-in-distance** estimate. The lemma is standard in functional analysis, but its specialization here is unusually clean because the lattice Maxwell operator is strictly finite-range in the link adjacency metric.

---

## 1. Abstract block-operator setup on a finite graph

Let \(V\) be a finite set equipped with a graph distance \(\mathrm{dist}:V\times V\to\mathbb N\cup\{0\}\).  
Let \(\mathsf H_0\) be a finite-dimensional real Hilbert space (in the gauge application, \(\mathsf H_0\simeq\mathfrak g\)).  
Let
\[
\mathsf H := \ell^2(V;\mathsf H_0).
\]

Any linear operator \(A:\mathsf H\to\mathsf H\) has block form
\[
(Af)(x)=\sum_{y\in V} A_{xy}f(y),
\qquad A_{xy}\in \mathrm{End}(\mathsf H_0).
\tag{1.1}
\]
Write \(\|\cdot\|_{\mathrm{op}}\) for the operator norm on \(\mathrm{End}(\mathsf H_0)\), and also for the induced operator norm on \(\mathsf H\).

---

## 2. The finite-range inverse-decay lemma (Combes–Thomas)

Assume:

1. **Uniform positivity (mass gap):** There exists \(a_0>0\) such that
\[
A\succeq a_0 I \qquad\text{on }\mathsf H.
\tag{2.1}
\]
2. **Finite range:** There exists \(R\ge 1\) such that
\[
A_{xy}=0\quad\text{whenever }\mathrm{dist}(x,y)>R.
\tag{2.2}
\]
3. **Off-diagonal row-sum bound:** Define
\[
B := \sup_{x\in V}\sum_{\substack{y\in V\\y\neq x}} \|A_{xy}\|_{\mathrm{op}} <\infty.
\tag{2.3}
\]

**Lemma 2.1 (Combes–Thomas exponential inverse decay).**  
Under (2.1)–(2.3),
\[
\| (A^{-1})_{xy}\|_{\mathrm{op}}
\ \le\
\frac{2}{a_0}\,\exp\!\big(-\eta\,\mathrm{dist}(x,y)\big),
\tag{2.4}
\]
where one may take
\[
\eta=\frac{1}{R}\log\!\Bigl(1+\frac{a_0}{2B}\Bigr).
\tag{2.5}
\]
(If \(B=0\), then \(A\) is diagonal in the \(V\)-index and (2.4) holds trivially with \(\eta=+\infty\).)

### Proof (conjugation by an exponential weight)

Fix \(y\in V\). Let \(\phi_y(x):=\mathrm{dist}(x,y)\), which is 1-Lipschitz:
\[
|\phi_y(x)-\phi_y(x')|\le \mathrm{dist}(x,x').
\]
For \(t\ge0\), define the diagonal multiplication operator \(W_t\) on \(\mathsf H\) by
\[
(W_tf)(x):=e^{t\phi_y(x)}f(x).
\]
Set \(A_t:=W_tAW_t^{-1}\). Then
\[
(A_t)_{xy}=e^{t(\phi_y(x)-\phi_y(y))}\,A_{xy}.
\tag{2.6}
\]
Let \(K_t:=A_t-A\). For \(\mathrm{dist}(x,y)\le R\) (the only case where \(A_{xy}\neq0\)),
\[
\| (K_t)_{xy}\|_{\mathrm{op}}
=
|e^{t(\phi_y(x)-\phi_y(y))}-1|\,\|A_{xy}\|_{\mathrm{op}}
\le (e^{tR}-1)\|A_{xy}\|_{\mathrm{op}}.
\]
Summing \(y\neq x\) yields
\[
\sum_{y\neq x}\|(K_t)_{xy}\|_{\mathrm{op}}\le (e^{tR}-1)\,B,
\]
and a block Schur bound gives
\[
\|K_t\|\le (e^{tR}-1)B.
\tag{2.7}
\]
Choose \(t\) so that \(\|K_t\|\le a_0/2\), i.e.
\[
(e^{tR}-1)B\le \frac{a_0}{2}
\quad\Longleftrightarrow\quad
t\le \frac{1}{R}\log\!\Bigl(1+\frac{a_0}{2B}\Bigr).
\tag{2.8}
\]
Then \(A_t=A+K_t\) is invertible and
\[
\|A_t^{-1}\|\le \frac{2}{a_0}.
\tag{2.9}
\]
Finally, \(A^{-1}=W_t^{-1}A_t^{-1}W_t\), so
\[
\|(A^{-1})_{xy}\|_{\mathrm{op}}
\le e^{-t\phi_y(x)}\|A_t^{-1}\|e^{t\phi_y(y)}
= e^{-t\,\mathrm{dist}(x,y)}\|A_t^{-1}\|
\le \frac{2}{a_0}e^{-t\,\mathrm{dist}(x,y)}.
\]
Take \(t=\eta\) at the upper limit in (2.8). \(\square\)

---

## 3. Application: massive Maxwell operator on the link graph

Now specialize to the lattice-gauge operator
\[
M:=m^2 I + \alpha\,d_1^\*d_1
\qquad\text{on}\qquad \mathcal C^1(\Lambda;\mathfrak g)\cong \ell^2(E(\Lambda);\mathfrak g).
\tag{3.1}
\]

### 3.1 The underlying graph and distance

Let \(V=E(\Lambda)\) be the set of oriented links, and define adjacency \(b\sim b'\) iff there exists a plaquette whose boundary contains both \(b\) and \(b'\). Let \(\mathrm{dist}_E\) be the induced graph distance.

This adjacency is exactly adapted to \(d_1^\*d_1\), because a plaquette term couples only links on the same plaquette boundary.

### 3.2 Verify the Combes–Thomas hypotheses

1. **Positivity.** Because \(d_1^\*d_1\succeq0\),
\[
\langle X,MX\rangle
= m^2\|X\|^2 + \alpha\|d_1X\|^2 \ge m^2\|X\|^2.
\]
Thus \(M\succeq m^2 I\). We may take \(a_0=m^2\).

2. **Finite range.** The operator \(d_1\) is a local incidence operator: \((d_1X)_p\) depends only on the four links in \(\partial p\). Likewise, \(d_1^\*\) distributes a plaquette value back to its boundary links. Consequently, \((d_1^\*d_1)_{bb'}\neq0\) only if \(b=b'\) or \(b\sim b'\). Hence \(M\) has range \(R=1\) in \(\mathrm{dist}_E\).

3. **Off-diagonal row-sum bound.** Each link belongs to at most \(\nu\) plaquettes, and each such plaquette boundary contains exactly three *other* links. Hence the number of neighbors of a link in the \(\sim\)-graph is at most \(3\nu\) (in \(d=4\), this is \(\le 18\)). The coefficients \((d_1^\*d_1)_{bb'}\) are uniformly bounded in operator norm by a dimension-dependent constant \(c_{\mathrm{inc}}\) (for the standard incidence matrices, \(c_{\mathrm{inc}}=1\)). Therefore
\[
B \;\le\; \sup_b \sum_{b'\neq b}\|(\alpha d_1^\*d_1)_{bb'}\|_{\mathrm{op}}
\ \le\ \alpha\,(3\nu)\,c_{\mathrm{inc}}.
\tag{3.2}
\]

### 3.3 Exponential decay of the Green kernel

Apply Lemma 2.1 with \(a_0=m^2\), \(R=1\), and \(B\) as in (3.2):

**Corollary 3.1 (massive Maxwell Green kernel decays exponentially).**  
There exist constants \(C,\eta>0\) depending only on \((m^2,\alpha)\) and on the lattice dimension (through \(\nu\) and \(c_{\mathrm{inc}}\)), such that for all links \(b,b'\),
\[
\|(M^{-1})_{bb'}\|_{\mathrm{op}}
\ \le\
\frac{2}{m^2}\,\exp\!\big(-\eta\,\mathrm{dist}_E(b,b')\big),
\tag{3.3}
\]
with an explicit admissible choice
\[
\eta = \log\!\Bigl(1+\frac{m^2}{2B}\Bigr)
\ \ge\
\log\!\Bigl(1+\frac{m^2}{2\alpha(3\nu)c_{\mathrm{inc}}}\Bigr).
\tag{3.4}
\]

### Comment on horizontal restriction

In the HS covariance bound, the relevant inputs are horizontal gradients (divergence-free at the vacuum). Since \(M\) preserves the horizontal sector, the decay (3.3) is compatible with restricting to that sector. One can either:
- apply Combes–Thomas to \(M\) on the full \(\ell^2(E;\mathfrak g)\), then restrict bilinear forms to horizontals, or
- apply it directly to the invariant sector using an orthonormal basis adapted to the link graph.

---

## 4. What could be developed further

Combes–Thomas is robust, but the *numerology* can likely be improved:

- A Fourier analysis on a periodic lattice can give sharper constants and a dispersion-relation expression for the decay rate (especially in the abelianized linear theory).
- One can attempt to optimize the metric \(\mathrm{dist}_E\) (e.g. use vertex distance instead of link adjacency) to produce a more physically interpretable exponent.

In any case, the qualitative conclusion is strikingly stable: **mass + finite range \(\Rightarrow\) exponential kernel decay**, uniformly in the volume.
