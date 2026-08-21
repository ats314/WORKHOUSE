# Finite-range Combes--Thomas decay for the inverse of the massive Maxwell operator

\begin{abstract}
We record a self-contained Combes--Thomas type lemma: if $A\succeq a_0 I$ and has finite interaction range on a graph with an off-diagonal row-sum bound $B$, then $A^{-1}$ has exponentially decaying blocks with an explicit exponent $\eta=(1/R)\log(1+a_0/(2B))$. We then specialize to the operator $M=m^2 I + t\,d_1^*d_1$ acting on link cochains.
\end{abstract}

## 1. Abstract setup: operators on a finite graph with fiber

Let $V$ be a finite set with a graph distance $\mathrm{dist}(\cdot,\cdot)$. Let $\mathsf H_0$ be a finite-dimensional real Hilbert space and set
\[
\mathsf H := \ell^2(V;\mathsf H_0).
\]
Any linear operator $A:\mathsf H\to\mathsf H$ can be written as a block kernel
\[
(Af)(x) = \sum_{y\in V} A_{xy} f(y),\qquad A_{xy}\in \mathrm{End}(\mathsf H_0).
\]
Write $\|\cdot\|_{\mathrm{op}}$ for the operator norm on $\mathrm{End}(\mathsf H_0)$.

## 2. Assumptions

Assume:

1. **Uniform positivity:** $A$ is self-adjoint and there exists $a_0>0$ such that
\[
A\succeq a_0 I.
\]
2. **Finite range:** there exists an integer $R\ge 1$ such that
\[
A_{xy}=0\quad \text{whenever }\mathrm{dist}(x,y)>R.
\]
3. **Row-sum bound:** define
\[
B := \sup_{x\in V}\sum_{y\neq x} \|A_{xy}\|_{\mathrm{op}} <\infty.
\]

## 3. Lemma (Combes--Thomas on finite range kernels)

\begin{lemma}[Finite-range Combes--Thomas]
Under Assumptions 1--3, for all $x,y\in V$,
\[
\|(A^{-1})_{xy}\|_{\mathrm{op}} \le \frac{2}{a_0}\,\exp\big(-\eta\,\mathrm{dist}(x,y)\big),
\]
where
\[
\eta := \frac{1}{R}\log\Bigl(1+\frac{a_0}{2B}\Bigr).
\]
(If $B=0$, $A$ is diagonal in the $V$ index and the bound holds with $\eta=+\infty$.)
\end{lemma}

\begin{proof}[Proof sketch (complete, but kept compact)]
Fix $y\in V$. Let $\phi_y(x):=\mathrm{dist}(x,y)$ and define the weight $(W_t f)(x)=e^{t\phi_y(x)}f(x)$. Consider $A_t:=W_t A W_t^{-1}=A+K_t$.

If $A_{xy}\neq 0$, then $\mathrm{dist}(x,y)\le R$ and $|\phi_y(x)-\phi_y(y)|\le R$, hence
\[
\| (K_t)_{xy}\|_{\mathrm{op}} \le (e^{tR}-1)\,\|A_{xy}\|_{\mathrm{op}}.
\]
A Schur test gives $\|K_t\|\le (e^{tR}-1)B$. Choose $t$ so that $\|K_t\|\le a_0/2$, equivalently $t\le \eta$.

Then $\|A_t^{-1}\|\le 2/a_0$ by Neumann series. Finally,
\[
A^{-1}=W_t^{-1}A_t^{-1}W_t\quad\Rightarrow\quad \|(A^{-1})_{xy}\|\le e^{-t\mathrm{dist}(x,y)}\|A_t^{-1}\|\le \frac{2}{a_0}e^{-t\mathrm{dist}(x,y)}.
\]
Take $t=\eta$.
\end{proof}

## 4. Specialization: the massive Maxwell operator on link cochains

In the lattice gauge application, the fiber is $\mathsf H_0\simeq \mathfrak g$ and the index set $V$ is the link set $E(\Lambda)$ with link-adjacency distance.

Define
\[
M := m^2 I + t\, d_1^*d_1
\]
acting on $\mathcal C^1(\Lambda;\mathfrak g)$ (often restricted to horizontals $\ker d_0^*$). Here:

- $m^2>0$ comes from Haar/Bakry--\'{E}mery on-site coercivity,
- $t>0$ is the Wilson prefactor,
- $d_1^*d_1$ is the discrete Maxwell operator.

### Checking the assumptions

- Positivity: $M\succeq m^2 I$ so $a_0=m^2$.
- Finite range: $(d_1^*d_1)_{\ell\ell'}$ vanishes unless $\ell,\ell'$ lie in a common plaquette; hence $R$ is an $O(1)$ constant in link-graph distance.
- Row-sum bound: if each link touches at most $\nu$ plaquettes and each plaquette has 4 edges, then the number of nonzero off-diagonal neighbors per row is $O(\nu)$ and $B\lesssim t\,\nu$.

Thus the abstract lemma yields an explicit decay rate depending only on $m^2,t$ and local incidence constants.

## 5. Sharper decay on $\mathbb Z^d$ (optional)

On the infinite lattice $\mathbb Z^d$ one can Fourier transform the symbol of $d_1^*d_1$ and shift contours to obtain a sharper exponent of the form
\[
\nu(m^2,t)=2\,\mathrm{arsinh}\!\Big(\sqrt{\frac{m^2}{8td}}\Big)
\]
for the kernel of $(m^2I+t d_1^*d_1)^{-1}$ on 1-forms. This is useful for continuum-scaling bookkeeping.

## 6. Why this matters for the larger program

This is the “green kernel” step that converts a matrix covariance bound into **exponential** clustering: once covariances are controlled by $M^{-1}$ and $M^{-1}$ has an exponentially decaying kernel, the only remaining task is to control the localization error that replaced $\nu_\Lambda$ by the conditional measure on the hinge set.
