---
title: "Appendix: Disjoint Staple Coordinates Around a Link in 4D (SU(2))"
project: "LYAPUNOV TOP 40"
status: "Appendix module (explicit coordinate choice verifying Hypothesis 3.1)"
date: "2025-12-31"
depends_on:
  - "LYAPUNOV_08_transversality_rank3_and_binomial_tail_drift.md"
---

\newcommand{\SU}{\mathrm{SU}}
\newcommand{\Ad}{\mathrm{Ad}}
\newcommand{\1}{\mathbf{1}}

# Appendix A. Explicit construction of the coordinates $r_j$ in $d=4$

This appendix verifies **Hypothesis 3.1** in `LYAPUNOV_08_transversality_rank3_and_binomial_tail_drift.md` by an explicit combinatorial construction on the $4$D hypercubic lattice. The conclusion is:

> **Claim (disjoint staple coordinates).**  
> For a fixed oriented link $\ell=(x,\mu)$ in $d=4$, there are exactly $m=6$ incident plaquettes, and one can choose $m$ local link variables $r_1,\dots,r_m$ inside the extended star $\Ext(\ell)$ such that each staple transport $g_j(U)$ factorizes as
> \[
> g_j(U)=r_j\cdot \bar g_j(\widehat U),
> \]
> and for $k\neq j$ neither $g_k$ nor the incident plaquette holonomies $U_{p_k}$ depend on $r_j$.

The construction is completely explicit.

---

## A.1 Lattice and notation

Let the lattice be $\mathbb Z^4$ (or a finite periodic box), with coordinate unit vectors $e_0,e_1,e_2,e_3$.

For each site $y$ and direction $\alpha\in\{0,1,2,3\}$, let $U_\alpha(y)\in \SU(2)$ denote the group element on the oriented link
\[
(y,\alpha):\quad y\to y+e_\alpha.
\]
For traversing links in the negative direction, use the standard convention
\[
U_{-\alpha}(y):=U_\alpha(y-e_\alpha)^{-1},
\]
so that $U_{-\alpha}(y)$ is the link from $y$ to $y-e_\alpha$.

Fix an oriented link
\[
\ell=(x,\mu):\quad x\to x+e_\mu,
\qquad U_\ell:=U_\mu(x).
\]

---

## A.2 The six incident plaquettes and their holonomies

In $d=4$, the link $\ell$ lies in $m=2(d-1)=6$ plaquettes: for each transverse direction $\nu\in\{0,1,2,3\}\setminus\{\mu\}$ there are two plaquettes in the $(\mu,\nu)$-plane, one on the ``$+\nu$ side'' and one on the ``$-\nu$ side''.

### (i) The $+\nu$ plaquette

Let $p_{\nu}^{+}$ be the plaquette with corners
\[
x,\quad x+e_\mu,\quad x+e_\mu+e_\nu,\quad x+e_\nu,
\]
oriented so that it starts with $\ell$.
Its holonomy is
\[
U_{p_{\nu}^{+}}
=
U_\mu(x)\,U_\nu(x+e_\mu)\,U_\mu(x+e_\nu)^{-1}\,U_\nu(x)^{-1}.
\tag{A.1}
\]

### (ii) The $-\nu$ plaquette

Let $p_{\nu}^{-}$ be the plaquette with corners
\[
x,\quad x+e_\mu,\quad x+e_\mu-e_\nu,\quad x-e_\nu,
\]
again oriented to start with $\ell$.
Traversing from $x+e_\mu$ to $x+e_\mu-e_\nu$ uses the negative $\nu$ link, etc., so
\[
U_{p_{\nu}^{-}}
=
U_\mu(x)\,U_\nu(x+e_\mu-e_\nu)^{-1}\,U_\mu(x-e_\nu)^{-1}\,U_\nu(x-e_\nu).
\tag{A.2}
\]

---

## A.3 Staple transports $g_{\nu}^{\pm}$ and the coordinate choice $r_{\nu}^{\pm}$

For each incident plaquette, define the staple transport $g_{\nu}^{\pm}(U)$ by factoring out the central link $U_\ell$ on the left:
\[
U_{p_{\nu}^{\pm}} = U_\ell\,g_{\nu}^{\pm}(U).
\]

From (A.1) and (A.2) we obtain:

\[
g_{\nu}^{+}(U)
=
U_\nu(x+e_\mu)\,U_\mu(x+e_\nu)^{-1}\,U_\nu(x)^{-1},
\tag{A.3}
\]
\[
g_{\nu}^{-}(U)
=
U_\nu(x+e_\mu-e_\nu)^{-1}\,U_\mu(x-e_\nu)^{-1}\,U_\nu(x-e_\nu).
\tag{A.4}
\]

### Coordinate choice

Define the six local link variables
\[
r_{\nu}^{+}\ :=\ U_\nu(x+e_\mu),
\qquad
r_{\nu}^{-}\ :=\ U_\nu(x+e_\mu-e_\nu)^{-1},
\qquad
\nu\neq \mu.
\tag{A.5}
\]

Then (A.3)–(A.4) become the desired factorization:
\[
g_{\nu}^{+}(U)=r_{\nu}^{+}\cdot\bar g_{\nu}^{+}(\widehat U),
\qquad
\bar g_{\nu}^{+}(\widehat U):=U_\mu(x+e_\nu)^{-1}\,U_\nu(x)^{-1},
\tag{A.6}
\]
\[
g_{\nu}^{-}(U)=r_{\nu}^{-}\cdot\bar g_{\nu}^{-}(\widehat U),
\qquad
\bar g_{\nu}^{-}(\widehat U):=U_\mu(x-e_\nu)^{-1}\,U_\nu(x-e_\nu).
\tag{A.7}
\]

Here $\widehat U$ denotes the collection of all local link variables in $\Ext(\ell)$ **except** the chosen coordinate $r_{\nu}^{\pm}$.

---

## A.4 Disjointness: each $r_{\nu}^{\pm}$ appears in exactly one staple

We now justify the key independence statement in Hypothesis 3.1.

### Lemma A.1 (Uniqueness of the coordinate link among incident plaquettes)

Fix $\nu\neq\mu$.

1. The oriented link $r_{\nu}^{+}=U_\nu(x+e_\mu)$ appears **only** in the holonomy of $p_{\nu}^{+}$ among the six incident plaquettes $\{p_{\rho}^{\pm}\}_{\rho\neq\mu}$.

2. The oriented link $r_{\nu}^{-}=U_\nu(x+e_\mu-e_\nu)^{-1}$ appears **only** in the holonomy of $p_{\nu}^{-}$ among the six incident plaquettes.

*Proof.*  
Inspect (A.1)–(A.2). The $\nu$-directed links at spatial locations involving $x+e_\mu$ occur only in the two plaquettes in the $(\mu,\nu)$-plane; moreover, the $+\nu$ plaquette uses the $\nu$-link at $x+e_\mu$, while the $-\nu$ plaquette uses the $\nu$-link at $x+e_\mu-e_\nu$ (in reverse). For any $\rho\neq\nu$, the plaquettes $p_{\rho}^{\pm}$ involve $\rho$-links, not $\nu$-links, so they cannot contain $r_{\nu}^{\pm}$. $\square$

### Corollary A.2 (Disjoint-staple variation)

Let $g_j$ range over the six staples $\{g_{\nu}^{\pm}\}_{\nu\neq\mu}$.  
Then varying a single coordinate $r_{\nu}^{\pm}$ changes **exactly one** staple $g_{\nu}^{\pm}$ (by left multiplication), and leaves all other staples $g_{\rho}^{\pm}$ unchanged. Likewise, it leaves all other incident plaquette holonomies $U_{p_{\rho}^{\pm}}$ unchanged.

This is precisely Hypothesis 3.1.

---

## A.5 Why the coordinates lie in the extended star $\Ext(\ell)$

By definition, the plaquette star $\St(\ell)$ contains all links in the boundaries of the incident plaquettes $p_{\nu}^{\pm}$, hence contains all links appearing in (A.1)–(A.2), in particular the six links $r_{\nu}^{\pm}$.

The extended star $\Ext(\ell)=\St(\ell)\cup\partial\St(\ell)$ therefore also contains $r_{\nu}^{\pm}$.

---

## A.6 Minimal takeaway

For a link $\ell=(x,\mu)$ in $d=4$, choosing the six links
\[
r_{\nu}^{+}=U_\nu(x+e_\mu),
\qquad
r_{\nu}^{-}=U_\nu(x+e_\mu-e_\nu)^{-1},
\qquad \nu\neq\mu,
\]
provides a concrete coordinate system in $\Ext(\ell)$ with the property that each $r_{\nu}^{\pm}$ appears in exactly one staple transport $g_{\nu}^{\pm}$.

This is the combinatorial input needed for the rank-$3$ transversality lemma for the cancellation set $\Z_\ell$.
