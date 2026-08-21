# Extract 09 — Gauge horizontality, cochain algebra, and why the Maxwell inverse is actually well-defined

\begin{center}
\textbf{Extracted from: Appendix B (cell complex/cochains), Appendix C (configuration geometry), Appendix A (Haar mass constant).}
\end{center}

## 0. What this piece adds to the project’s “mass gap pipeline”

Earlier extracts gave the headline chain
\[
\text{Bakry–Émery curvature on a good set}
\;\Rightarrow\;
\text{HS covariance} 
\;\Rightarrow\;
M_{\Lambda_L}^{-1}\text{ decay}
\;\Rightarrow\;
\text{clustering}\;\Rightarrow\;\text{OS gap}.
\]

This extract fills a missing structural joint:

\begin{quote}
\textbf{Gauge invariance forces the gradients of physical observables to live in a horizontal subspace where the “Maxwell operator” acts cleanly.}
\end{quote}

That’s how you avoid the classic obstruction: the massless Maxwell stiffness $d_1^*d_1$ has gauge zero-modes ($\mathrm{im}(d_0)$). The project resolves this in a geometrically natural way: (i) isolate horizontals, (ii) observe invariance of horizontals under $d_1^*d_1$, and (iii) add a strictly positive Haar/Jacobian mass $m_H^2$ so inversion is unambiguous.

---

## 1. Discrete differential geometry on the hypercubic torus

Work on a periodic $d$-dimensional lattice $\Lambda_L$ with cells:

- vertices $V(\Lambda_L)$,
- oriented links $E(\Lambda_L)$,
- oriented plaquettes $P(\Lambda_L)$.

Define $\mathfrak g$-valued cochains
\[
\mathcal C^0(\Lambda_L;\mathfrak g),\qquad \mathcal C^1(\Lambda_L;\mathfrak g),\qquad \mathcal C^2(\Lambda_L;\mathfrak g)
\]
with $\ell^2$ inner products from the Lie-algebra inner product $\langle\cdot,\cdot\rangle_{\mathfrak g}$.

### 1.1 Coboundaries

The 0→1 coboundary (discrete gradient)
\[
(d_0\varphi)_{x,\mu}=\varphi_{x+\hat e_\mu}-\varphi_x,
\]

and the 1→2 coboundary (discrete curl)
\[
(d_1X)_{p=(x;\mu,\nu)}=X_{x,\mu}+X_{x+\hat e_\mu,\nu}-X_{x+\hat e_\nu,\mu}-X_{x,\nu}.
\]

### 1.2 The cochain-complex identity

A basic but crucial identity is
\[
\boxed{\quad d_1\,d_0\equiv 0.\quad}
\]
This says: discrete gradients are curl-free, exactly as in continuum electromagnetism.

---

## 2. Adjoint formulas and the horizontal splitting

The $\ell^2$ adjoint of $d_0$ is the discrete divergence:
\[
\boxed{\quad (d_0^*X)_x = \sum_{\mu}\bigl(X_{x-\hat e_\mu,\mu}-X_{x,\mu}\bigr).\quad}
\]

The adjoint of $d_1$ is incidence-weighted summation over plaquettes:
\[
\boxed{\quad (d_1^*F)_b = \sum_{p\in P(\Lambda_L)} \sigma_{p,b}\,F_p.\quad}
\]

Finite-dimensional Hilbert-space algebra gives the orthogonal decomposition
\[
\boxed{\quad
\mathcal C^1(\Lambda_L;\mathfrak g)
=
\mathrm{im}(d_0)\ \oplus\ \ker(d_0^*).
\quad}
\]
Define the horizontal subspace
\[
\boxed{\quad H^{(0)}:=\ker(d_0^*)\subset \mathcal C^1(\Lambda_L;\mathfrak g).\quad}
\]
Interpretation:

- $\mathrm{im}(d_0)$ are infinitesimal gauge directions (pure gauge),
- $H^{(0)}$ are the canonical orthogonal complement (physical directions at the vacuum).

---

## 3. Gauge geometry on configuration space and “horizontal gradients”

The configuration manifold is
\[
M_{\Lambda_L}=G^{E(\Lambda_L)}
\]
with product Riemannian metric from a bi-invariant metric on $G$.

The lattice gauge group is
\[
\mathcal G_{\Lambda_L}=G^{V(\Lambda_L)}
\]
acting on links by
\[
(g\cdot U)_{x,\mu}=g_x\,U_{x,\mu}\,g_{x+\hat e_\mu}^{-1}.
\]

### 3.1 Linearization at the vacuum

Let $U^{(0)}$ denote the vacuum configuration ($U_b=\mathbf 1$ for every link).
If $g(t)_x=\exp(t\varphi_x)$ for a 0-cochain $\varphi$, then
\[
\boxed{\quad
\omega_{U^{(0)}}^R\big(\dot U(0)\big) = -d_0\varphi\in\mathcal C^1(\Lambda_L;\mathfrak g).
\quad}
\]
Therefore the right-trivialized tangent space to the gauge orbit through $U^{(0)}$ is
\[
\boxed{\quad
\omega_{U^{(0)}}^R\Big(T_{U^{(0)}}(\mathcal G_{\Lambda_L}\cdot U^{(0)})\Big)=\mathrm{im}(d_0).
\quad}
\]

### 3.2 Gauge invariance forces horizontality

If an observable $F\in C^\infty(M_{\Lambda_L})$ is gauge-invariant ($F\circ\Phi_g=F$ for all $g$), then differentiating along any gauge-orbit curve gives
\[
\langle \nabla F(U^{(0)}),\dot U(0)\rangle = 0.
\]
Using the orbit identification above, this implies
\[
\boxed{\quad
\omega_{U^{(0)}}^R\big(\nabla F(U^{(0)})\big)\in H^{(0)}=\ker(d_0^*).
\quad}
\]

This is the key structural fact: **the gradients that appear in the HS covariance formula are automatically horizontal for gauge-invariant observables (at the vacuum).**

---

## 4. Maxwell stiffness, gauge zero-modes, and invariance of horizontals

Define the discrete Maxwell operator
\[
\mathsf M_1 := d_1^*d_1\quad\text{on }\mathcal C^1(\Lambda_L;\mathfrak g).
\]
It is positive semidefinite:
\[
\langle X,\mathsf M_1 X\rangle = \|d_1X\|_{\mathcal C^2}^2\ge 0.
\]

### 4.1 Gauge directions lie in the kernel

Because $d_1d_0=0$,
\[
\boxed{\quad \mathsf M_1(d_0\varphi)=0\quad\text{for every }\varphi\in\mathcal C^0.\quad}
\]
So $\mathsf M_1$ has the expected gauge kernel.

### 4.2 Horizontals are invariant under $\mathsf M_1$

Using $(d_1d_0)^*=d_0^*d_1^*=0$, for $X\in\ker(d_0^*)$ we have
\[
 d_0^*(\mathsf M_1X)=d_0^*d_1^*d_1X=0.
\]
Hence
\[
\boxed{\quad \mathsf M_1(H^{(0)})\subset H^{(0)}.\quad}
\]

This is what makes it legitimate to talk about $\mathsf M_1$ acting “within the physical sector.”

---

## 5. The Haar/Jacobian mass term and the massive Maxwell operator

In exponential coordinates on $G$, the Riemannian volume form pulls back as
\[
(\exp_G)^*(\mathrm{vol}_{g_G}) = J_G(X)\,dX,
\]
so the measure contributes a “Haar potential”
\[
S_H(X)=-\log J_G(X).
\]
A standing geometric assumption yields a quadratic Hessian bound at the origin:
\[
\boxed{\quad \nabla^2 S_H(0) \succeq \frac{\kappa_G}{3}\,\mathrm{Id}.\quad}
\]
Define the Haar mass
\[
\boxed{\quad m_H^2:=\frac{\kappa_G}{3}.\quad}
\]

The project packages the stiffness + mass into
\[
\boxed{\quad
M_{\Lambda_L} := m_H^2\,\mathrm{Id} + \alpha_W\,\mathsf M_1,
\qquad \alpha_W:=\frac{\beta}{n}.
\quad}
\]

Properties:

- uniform positivity: $M_{\Lambda_L}\succeq m_H^2\,\mathrm{Id}$,
- range-one interaction in the link graph,
- invariance of horizontals: $M_{\Lambda_L}(H^{(0)})\subset H^{(0)}$.

This is the operator whose inverse kernel enters the covariance bounds.

---

## 6. Quantitative 4D constants (the “plug-in” numbers)

On the periodic hypercubic lattice in $d=4$:

- each link belongs to $\nu_P=2(d-1)=6$ plaquettes,
- the link-graph degree obeys $D_E\le 3\nu_P\le 18$,
- the off-diagonal row-sum constant satisfies
\[
\boxed{\quad C_0(\mathsf M_1)\le 3\nu_P\le 18.\quad}
\]

Therefore one can insert explicit constants into Combes–Thomas/Davies bounds, e.g.
\[
\eta_{\mathrm{CT}}(M_{\Lambda_L})\ge \log\Big(1+\frac{m_H^2}{2\alpha_W C_0(\mathsf M_1)}\Big)
\ \ge\ \log\Big(1+\frac{m_H^2}{36\alpha_W}\Big).
\]

So once $m_H^2$ is known (or bounded below) and $\beta$ is large enough, you can get an **explicit exponential correlation length**.

---

## 7. Where this slots into the broader theory

The structural picture is:

1. **Gauge invariance** $\Rightarrow$ gradients of physical observables are horizontal.
2. On horizontals, the Maxwell stiffness is well behaved (and invariant).
3. A **Haar/Jacobian mass** supplies strict positivity (no infrared catastrophe).
4. Deterministic operator theory gives **exponential decay of $M^{-1}$**, which becomes exponential clustering via HS/BL.

This isn’t just bookkeeping: it is the geometric reason the whole “mass gap pipeline” isn’t murdered by gauge redundancy.

---

## 8. Further work that looks genuinely promising

1. **Extend horizontality beyond the vacuum.**  Proposition C.3.7 is at $U^{(0)}$. A global statement for a small-field tube around the vacuum would tighten the full argument.

2. **Topological zero-modes.**  On a torus one expects harmonic 1-cochains. The mass term likely kills them, but it would be good to isolate the exact kernel structure of $d_1^*d_1$ and show how $m_H^2$ resolves it.

3. **Compute/optimize $\kappa_G$ for concrete groups.**  For $G=\mathrm{SU}(N)$ with the chosen normalization, one can probably make $m_H^2$ explicit, improving quantitative decay rates.

4. **Renormalization-friendly formulation.**  The splitting $\mathcal C^1=\mathrm{im}(d_0)\oplus\ker(d_0^*)$ is an ideal place to build block RG maps that respect gauge geometry.
