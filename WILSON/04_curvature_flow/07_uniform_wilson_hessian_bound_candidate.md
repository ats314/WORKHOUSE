# Candidate: Uniform Wilson Hessian Bound via HS-Norm Contraction of the Exponential

This document is an attempt to **replace the earlier “huge constants with $e^{c\|A\|}$ growth” approach**
with a cleaner observation:

> For anti-Hermitian $A$, $e^A$ is unitary, and **left/right multiplication by unitaries is an isometry for the Hilbert–Schmidt (HS) norm**.

That gives **uniform** (amplitude-independent) bounds on $D\exp$ and $D^2\exp$ in HS norm, which then propagate to the Wilson plaquette map and (with local geometry counting) to a uniform Hessian bound:
\[
\|\nabla^2 S_W(A)\|_{\mathrm{op}} \le C_W\,\beta.
\]

This is the kind of lemma that can feed both:
- a cleaner analytic convexity analysis, and
- validated numerics (via Lipschitz constants).

---

## 1. HS norm facts

For matrices, define
\[
\|X\|_{\mathrm{HS}} := \sqrt{\operatorname{Tr}(X^\dagger X)}.
\]
If $U,V$ are unitary, then
\[
\|UXV\|_{\mathrm{HS}} = \|X\|_{\mathrm{HS}}.
\]

---

## 2. Uniform bounds for $D\exp$ and $D^2\exp$ in HS norm

Let $A$ be anti-Hermitian ($A^\dagger=-A$), so $e^{tA}$ is unitary for all real $t$.

### Lemma 2.1 (First derivative contraction)
The Fréchet derivative satisfies
\[
D e^{A}[H] = \int_0^1 e^{(1-s)A} H e^{sA}\,ds,
\]
and therefore
\[
\boxed{\ \|D e^{A}[H]\|_{\mathrm{HS}} \le \|H\|_{\mathrm{HS}}.\ }
\]

**Proof.** Each integrand is $UHV$ with $U,V$ unitary, hence has HS norm $\|H\|_{\mathrm{HS}}$. Integrate over $s\in[0,1]$. ∎

### Lemma 2.2 (Second derivative uniform bound)
A standard symmetric integral formula gives
\[
D^2 e^A[H,K]
=
\int_0^1\!\!\int_0^s e^{(1-s)A} H e^{(s-u)A} K e^{uA}\,du\,ds
+
\int_0^1\!\!\int_0^s e^{(1-s)A} K e^{(s-u)A} H e^{uA}\,du\,ds.
\]
Then
\[
\boxed{\ \|D^2 e^{A}[H,K]\|_{\mathrm{HS}} \le \|H\|_{\mathrm{HS}}\,\|K\|_{\mathrm{HS}}.\ }
\]

**Proof.** Consider one integrand $U H V K W$ with $U,V,W$ unitary. Then
\[
\|U H V K W\|_{\mathrm{HS}} = \|H V K\|_{\mathrm{HS}}
\le \|H\|_{\mathrm{HS}}\,\|VK\|_{\mathrm{op}}
= \|H\|_{\mathrm{HS}}\|K\|_{\mathrm{op}}
\le \|H\|_{\mathrm{HS}}\|K\|_{\mathrm{HS}}.
\]
Each double integral has area $1/2$ and there are two symmetric terms, giving total constant $1$. ∎

---

## 3. Uniform block bounds for one plaquette term

Fix a plaquette with link algebra variables $(A_1,A_2,A_3,A_4)\in \mathfrak{su}(N)^4$ and define
\[
U_p(A) := e^{A_1} e^{A_2} e^{-A_3} e^{-A_4},
\qquad
S_p(A) := \beta\left(1-\frac{1}{N}\operatorname{ReTr}(U_p(A))\right).
\]
Since $\operatorname{ReTr}$ is linear in $U_p$, all second derivatives come from $D^2 U_p$.

### Lemma 3.1 (Block bilinear form bound)
Let $H=(H_1,\dots,H_4)$ and $K=(K_1,\dots,K_4)$ be variations in $\mathfrak{su}(N)^4$ with HS norms.
Then there is a constant $C_{p,N}$ such that
\[
|D^2 S_p(A)[H,K]|
\le
C_{p,N}\,\beta\,\|H\|_2\,\|K\|_2,
\qquad
\|H\|_2^2:=\sum_{i=1}^4 \|H_i\|_{\mathrm{HS}}^2,
\]
and one may take explicitly
\[
\boxed{\ C_{p,N} = \frac{4}{\sqrt{N}}.\ }
\]

**Proof sketch.**
By product rule, $D^2 U_p$ is a sum of terms with either:
- one $D^2 e^{A_i}[H_i,K_i]$ inserted, or
- two $D e^{A_i}[H_i]$ and $D e^{A_j}[K_j]$ inserted.

Using Lemma 2.1–2.2 and HS isometry under unitary left/right multiplication gives:
\[
\|D^2 U_p(A)[H,K]\|_{\mathrm{HS}}
\le \left(\sum_{i=1}^4 \|H_i\|_{\mathrm{HS}}\right)\left(\sum_{j=1}^4 \|K_j\|_{\mathrm{HS}}\right).
\]
Then by Cauchy–Schwarz,
\[
\sum_i \|H_i\| \le 2\|H\|_2,\qquad \sum_j \|K_j\| \le 2\|K\|_2,
\]
hence $\|D^2 U_p\|_{\mathrm{HS}}\le 4\|H\|_2\|K\|_2$.

Finally, $|\operatorname{Tr}(M)| \le \sqrt{N}\,\|M\|_{\mathrm{HS}}$ gives
\[
|D^2 S_p(A)[H,K]|
\le \frac{\beta}{N}\,|\operatorname{Tr}(D^2U_p)|
\le \frac{\beta}{N}\,\sqrt{N}\,\|D^2U_p\|_{\mathrm{HS}}
\le \frac{4}{\sqrt{N}}\beta\,\|H\|_2\|K\|_2.
\]
∎

---

## 4. Global Wilson Hessian bound (finite lattice)

Let $\mathcal{E}$ be the set of oriented links and $S_W = \sum_{p} S_p$.
Consider the Hessian $\nabla^2 S_W(A)$ as a block operator on $\mathfrak{su}(N)^{\mathcal{E}}$ with the $\ell^2$ link norm.

Each link belongs to at most $n_p=6$ plaquettes in 4D, and each plaquette couples a link to at most 4 links total.

Using a standard “block row sum” estimate:
\[
\|\nabla^2 S_W(A)\|_{\mathrm{op}}
\le
\sup_{\ell\in\mathcal{E}}
\sum_{\ell'} \|(\nabla^2 S_W(A))_{\ell\ell'}\|_{\mathrm{op}}.
\]

From Lemma 3.1, each plaquette contribution to any block operator norm is $\le \beta/\sqrt{N}$ up to a small constant factor, and the row has at most $4n_p$ nonzero blocks from those plaquettes.

A conservative bound is:
\[
\boxed{
\|\nabla^2 S_W(A)\|_{\mathrm{op}}
\le
\frac{24}{\sqrt{N}}\,\beta
\quad\text{for all }A.
}
\]
For $N=3$ this is $24/\sqrt{3}\approx 13.86$.

---

## 5. Status and what still needs checking

This derivation is **structurally** clean and avoids $e^{c\|A\|}$ blowup by using:
- anti-Hermiticity $\Rightarrow$ unitarity,
- HS isometries under left/right multiplication,
- trace bounded by HS norm.

Two details to check carefully in a full writeup:
1. the exact symmetric integral formula for $D^2 e^A$ (a standard identity, but should be cited),
2. bookkeeping constants in the “block row sum” step (depending on exactly how the Hessian is represented as a link-by-link block matrix).

If this lemma stands as written, it is a **major simplification** versus the earlier constant inflation and the volume-scaling problems.

---

## 6. Why this is exciting

Because it suggests the Wilson Hessian might be uniformly bounded in the *right norm*,
making strong statements *possible* at least in finite volume and in regimes where the coordinate chart is under control.

Even if you ultimately abandon exponential coordinates globally, the HS-contraction trick is still useful for:
- local convexity certification,
- Lipschitz bounds needed for validated numerics,
- and sharpening any analytic estimates that currently blow up with $\|A\|$.

