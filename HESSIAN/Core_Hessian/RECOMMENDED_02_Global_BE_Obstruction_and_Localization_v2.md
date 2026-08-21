# Global Bakry–Émery Obstruction and the Case for Localization

This note does two things:

1. It gives a **sharp, explicit obstruction** to any attempt to get a *global* Bakry–Émery lower bound in the continuum (\(\beta\to\infty\)) purely from “nice geometry + Wilson action”.
2. It lays out a **localization bridge**: what kind of “good region + negligible bad region” theorem would be needed to turn *local* convexity into a global spectral gap.

---

## 1. Setup minimal

Let \(\mathcal C_a = \mathrm{SU}(N)^{|B|}\) be lattice configuration space (one group element per bond/link), equipped with the product Riemannian structure induced by
\[
\langle X,Y\rangle = -\mathrm{Tr}(XY),\qquad X,Y\in\mathfrak{su}(N).
\]

Let the Wilson action be
\[
S_W(U) = \sum_{p} \left(1-\frac{1}{N}\mathrm{ReTr}(U_p)\right),
\]
and \(\beta=\frac{2N}{g^2}\).

A canonical diffusion to study is the Langevin generator (with respect to the Gibbs measure)
\[
d\mu_{\beta}(U)\propto e^{-\beta S_W(U)}\,d\mathrm{vol}(U),
\qquad 
L=\Delta - \langle \nabla(\beta S_W),\nabla\,\cdot\,\rangle .
\]

On a Riemannian manifold, the Bakry–Émery curvature lower bound is (schematically)
\[
\mathrm{Ric} + \nabla^2(\beta S_W)\succeq \rho\,I
\quad\Longrightarrow\quad
\text{Poincaré/log-Sobolev}\Longrightarrow \text{spectral gap}\gtrsim\rho.
\]

The critical point: \(\rho\) is the **global infimum** over \(\mathcal C_a\).

---

## 2. A concrete negative Wilson Hessian direction exists for every \(N\ge 2\)

The obstruction is brutally simple: \(S_W\) is not globally convex on the compact manifold \(\mathcal C_a\).
In fact we can write down an explicit plaquette configuration with a strictly negative second derivative.

### Lemma 2.1 explicit negative second derivative for one plaquette
Let
\[
S_p(U)=1-\frac{1}{N}\mathrm{ReTr}(U),\qquad U\in \mathrm{SU}(N).
\]
There exist \(U_0\in\mathrm{SU}(N)\) and \(X\in\mathfrak{su}(N)\) with \(\|X\|=1\) such that
\[
\frac{d^2}{dt^2}S_p(e^{tX}U_0)\Big|_{t=0} = -\frac{1}{N}.
\]

**Proof.**  
Take
\[
U_0=\mathrm{diag}(-1,-1,1,\dots,1)\in\mathrm{SU}(N).
\]
Embed an \(\mathfrak{su}(2)\) generator into the upper-left \(2\times 2\) block.
Choose \(X\) so that on that block \(X^2=-(1/2)I_2\) and \(\|X\|^2=-\mathrm{Tr}(X^2)=1\) (e.g. \(X=\sqrt2\,(i\sigma_3/2)\) inside the block).

Then, using \(S_p(t)=1-\frac{1}{N}\mathrm{ReTr}(e^{tX}U_0)\),
\[
S_p''(0)= -\frac{1}{N}\mathrm{ReTr}(X^2U_0).
\]
On the \(2\times 2\) block, \(U_0=-I_2\), so \(X^2U_0 = (-\tfrac12 I_2)(-I_2)=+\tfrac12 I_2\), which has trace \(1\).
All other blocks contribute \(0\).
Hence \(\mathrm{ReTr}(X^2U_0)=1\) and \(S_p''(0)=-(1/N)\).
\(\square\)

### Corollary 2.2 global negativity scales like \(-\beta\)
Because a single plaquette term already has a negative Hessian direction of size \(1/N\), the global Wilson Hessian satisfies
\[
\inf_{U\in\mathcal C_a}\lambda_{\min}\big(\nabla^2 S_W(U)\big)\le -\frac{1}{N}.
\]
Therefore the global Bakry–Émery constant obeys the upper bound
\[
\rho_{\mathrm{BE}}(\beta)
\le \underbrace{\inf\lambda_{\min}(\mathrm{Ric})}_{\text{finite (positive) on compact } \mathcal C_a}
\;+\;\beta\left(-\frac{1}{N}\right).
\]
In particular, as \(\beta\to\infty\), \(\rho_{\mathrm{BE}}(\beta)\to -\infty\).

**Moral:** global Bakry–Émery curvature is the wrong global object for the continuum regime.

---

## 3. What this forces you to do

If you want any continuum-relevant “convexity \(\Rightarrow\) gap” story, you need one (or more) of the following:

1. **Localization:** prove convexity only on a large-probability “core region” \(\mathcal K_a\), and show the complement is negligible in the *Dirichlet-capacity* sense.
2. **A new Spark:** find a physically meaningful mechanism that generates IR convexity at some non-vanishing scale (independent of \(a\)).
3. **Abandon global BE as the main tool:** use alternative spectral-gap methods (e.g., multiscale/mixing/correlation inequalities) that don’t require a global Hessian lower bound.

The rest of the recommended bundle pursues (1) and (2).

---

## 4. The localization bridge what would make this work

The working template is:

- Define a core set \(\mathcal K_a\subset\mathcal C_a\) where the effective action is “well-behaved”.
  Typical choices:
  \[
  \mathcal K_a(\varepsilon)=\{U:\; \|U_p-I\|\le \varepsilon \text{ for all plaquettes }p\},
  \]
  or a gauge-fixed analogue where the gauge potential is small in an \(H^1\)-type norm.

- Prove a **local** functional inequality on \(\mathcal K_a\), e.g. a Poincaré inequality with Neumann boundary:
  \[
  \mathrm{Var}_{\mu|\mathcal K_a}(f)\le \frac{1}{\rho_{\mathrm{loc}}}\int_{\mathcal K_a}\|\nabla f\|^2\,d\mu.
  \]

- Show the complement is spectrally irrelevant, in one of two standard-looking ways:

  **(A) Capacity control.**  
  Prove \(\mathrm{Cap}(\mathcal C_a\setminus\mathcal K_a)\) is tiny (or \(\to 0\) as \(a\to 0\)).  
  Intuition: the diffusion almost surely stays in \(\mathcal K_a\) on spectral time-scales.

  **(B) Exit-time / metastability control.**  
  Show the expected exit time from \(\mathcal K_a\) is super-large:
  \[
  \mathbb E_{\mu|\mathcal K_a}[\tau_{\mathcal C_a\setminus\mathcal K_a}] \gg 1/\rho_{\mathrm{loc}}.
  \]

If either (A) or (B) holds in a quantitative way, one can hope to “glue” the local inequality into a global one.

### Why this is not optional
Lemma 2.1 shows that the diffusion *can* see negative curvature somewhere.
So the only way a convexity-based mechanism can survive is if those bad regions are dynamically/measure-theoretically irrelevant.

---

## 5. Where the “Spark” ideas plug in

A localization program becomes far more plausible if you can produce an **IR spark**:
a mechanism that generates a strictly convex effective potential on coarse modes *after* integrating out UV modes, even if the bare action is not globally convex.

That is the motivation for the **Entropic Gribov Spark** conjecture (see **RECOMMENDED_04_Entropic_Gribov_Spark_Conjecture.md**): convex geometry of the gauge-fixed fundamental domain could create an effective quadratic confinement of IR modes, giving you a physically-scaled \(\rho_{\mathrm{loc}}\) without relying on the cutoff Haar mass.
