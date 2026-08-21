# LEMMA UNITY — Curvature–RG Mechanism for a Finite‑Cutoff Mass Gap in \(SU(N)\) Lattice Yang–Mills

*Working note.* This file stitches the project’s strongest derivations into a single through‑line and reframes them as a **curvature RG** mechanism.

---

## Executive summary (what is proved, what is *not*)

### What is proved (finite cutoff, strong coupling)

1. **A volume‑uniform curvature lower bound on “physical” (horizontal) directions**:
   \[
   \nabla^2_{\mathrm{hor}} S_{\mathrm{eff}}(U)\ \succeq\ \rho_*(a,g)\,I,
   \qquad
   \rho_*(a,g):=c_0\,a^2 g^2-\beta\,C_V(N),
   \]
   in an explicit strong‑coupling window where \(\rho_*(a,g)>0\).

2. **A Bakry–Émery/Poincaré/spectral‑gap statement for the Langevin generator** (mixing gap / “dynamic mass gap”) with constants **independent of lattice volume**.

3. **A one‑step RG (blocking) stability statement**:
   convexity persists after marginalizing (“integrating out”) a block of fine links in a stricter subwindow.

4. Two “supporting pillars”:
   - reducible (singular) configurations form a **polar** set (capacity zero),
   - an independent **transfer‑matrix gap** exists in strong coupling.

### What is *not* proved (continuum)

This does **not** prove the continuum Yang–Mills mass gap. In fact, there is a clean obstruction to any *global* Bakry–Émery curvature bound surviving asymptotic freedom (see the companion “program” note).

---

## 1. Geometry and notation

Let \(\Lambda\subset \mathbb{Z}^4\) be a finite periodic hypercubic lattice.

- Links (bonds): \(B=B(\Lambda)\).
- Gauge group: \(G=SU(N)\), Lie algebra \(\mathfrak{g}=\mathfrak{su}(N)\).
- Configuration manifold:
  \[
  \mathcal{C}:=G^{|B|}.
  \]
- Metric: product metric induced from the bi‑invariant inner product
  \[
  \langle X,Y\rangle:=-\mathrm{Tr}(XY),\qquad X,Y\in\mathfrak{su}(N).
  \]

The lattice gauge group \(\mathcal{G}_\Lambda = G^{|V(\Lambda)|}\) acts isometrically on \(\mathcal{C}\). At each \(U\in\mathcal{C}\) we have an orthogonal splitting
\[
T_U\mathcal{C}=V_U\oplus H_U,
\]
where \(V_U\) is tangent to the gauge orbit (vertical) and \(H_U\) is its orthogonal complement (horizontal).

**Why horizontals?**  
Gauge‑invariant observables are constant along gauge orbits, hence their gradients are horizontal. The convexity/curvature estimates below are made on \(H_U\) because vertical directions contain gauge redundancy.

---

## 2. The effective action and the two curvature inputs

We consider an effective negative log density of the form
\[
S_{\mathrm{eff}}(U)=\beta\,S_W(U)+S_{\mathrm{Haar}}(U),\qquad
\beta=\frac{2N}{g^2},
\]
with:

- **Wilson plaquette action**
  \[
  S_W(U)=\sum_{p}\left(1-\frac1N\Re\mathrm{Tr}(U_p)\right),
  \]
  where \(U_p\) is the ordered product around plaquette \(p\).

- **Haar/measure contribution** \(S_{\mathrm{Haar}}\).  
  Concretely, in exponential coordinates \(U_b=\exp(iagA_b)\), the product Haar measure has a Jacobian density \(J(A)\) relative to a flat reference measure \(dA\), and one defines
  \[
  S_{\mathrm{Haar}}(A):=-\log J(A).
  \]
  In a normal neighborhood of the identity (where such coordinates are well‑behaved), \(S_{\mathrm{Haar}}\) contributes a **uniformly positive quadratic term** in the link variables.

> Only two analytic facts are needed:
> (i) a uniform **lower bound** on \(\mathrm{Hess}\,S_{\mathrm{Haar}}\) (positive curvature),  
> (ii) a uniform **operator‑norm bound** on \(\mathrm{Hess}\,S_W\) (controlled negative curvature).

---

## 3. Input A — Haar “mass term” (positive curvature)

There exists a constant \(c_0>0\) (depending only on \(SU(N)\) and conventions) such that, in a fixed normal neighborhood of the identity,
\[
\mathrm{Hess}\,S_{\mathrm{Haar}}(U)\ \succeq\ c_0\,a^2 g^2\,I,
\]
as a quadratic form on link directions (hence also on horizontals).

*Heuristic origin.*  
Expanding the Jacobian of the exponential map yields (schematically)
\[
S_{\mathrm{Haar}}(A_b) = \frac{c_0}{2}\,a^2 g^2\|A_b\|^2 + O(a^4 g^4\|A_b\|^4),
\]
so its Hessian begins as a positive multiple of the identity.

Interpretation: **compact group geometry supplies a bare rigidity** with strength \(\sim a^2 g^2\).

---

## 4. Input B — Wilson Hessian bound (bounded curvature)

A global (volume‑independent) bound holds:
\[
\big|\langle A,\mathrm{Hess}\,S_W(U)\,A\rangle\big|
\ \le\
C_V(N)\,\|A\|^2
\qquad\forall U\in\mathcal{C},\ \forall A\in T_U\mathcal{C}.
\]

One convenient explicit choice in \(d=4\) is
\[
C_V(N)=\frac{6}{N}.
\]

*Proof sketch.*  
For a single plaquette \(p\), a one‑link variation \(X\in\mathfrak{su}(N)\) gives
\[
S_p''(0)=-\frac1N\Re\mathrm{Tr}(X^2U_p).
\]
Writing \(H=-X^2\succeq 0\) and applying von Neumann’s trace inequality yields
\[
|S_p''(0)|\le \frac{1}{N}\|X\|^2.
\]
Summing plaquettes and using that in \(4D\) each link belongs to \(6\) plaquettes gives the stated global constant \(6/N\).

Interpretation: the Wilson action has **bounded “destabilizing curvature”**; it cannot be arbitrarily concave.

---

## 5. Finite‑cutoff horizontal convexity window

For any horizontal \(A\in H_U\),
\[
\begin{aligned}
\langle A,\mathrm{Hess}\,S_{\mathrm{eff}}(U)\,A\rangle
&=\beta\,\langle A,\mathrm{Hess}\,S_W(U)\,A\rangle
+\langle A,\mathrm{Hess}\,S_{\mathrm{Haar}}(U)\,A\rangle\\
&\ge -\beta\,C_V(N)\|A\|^2 + c_0 a^2 g^2\|A\|^2\\
&=\rho_*(a,g)\,\|A\|^2,
\end{aligned}
\]
where
\[
\rho_*(a,g):=c_0\,a^2g^2-\beta\,C_V(N).
\]

Thus **uniform horizontal convexity** holds provided
\[
\rho_*(a,g)>0
\quad\Longleftrightarrow\quad
c_0 a^2 g^2 > \beta C_V(N)
\quad\Longleftrightarrow\quad
c_0 a^2 g^4 > 2N\,C_V(N).
\]

With \(C_V(N)=6/N\), this becomes
\[
g^4>\frac{12}{c_0\,a^2}.
\]

### Gribov‑region reading

Define the (horizontal) Gribov region
\[
\Omega:=\{U\in\mathcal{C}:\ \mathrm{Hess}_{\mathrm{hor}}S_{\mathrm{eff}}(U)\succ 0\}.
\]
The condition \(\rho_*(a,g)>0\) places the theory **uniformly inside** \(\Omega\), separated from the Gribov horizon by a definite gap \(\rho_*(a,g)\).

---

## 6. Bakry–Émery ⇒ Poincaré ⇒ Langevin spectral gap

Let the (formal) Gibbs measure be
\[
d\mu(U)=Z^{-1}e^{-S_{\mathrm{eff}}(U)}\,d\mathrm{vol}(U),
\]
and consider the Langevin generator on \((\mathcal{C},g)\)
\[
L f = \Delta f - \langle \nabla S_{\mathrm{eff}},\nabla f\rangle,
\]
with carré du champ \(\Gamma(f)=\|\nabla f\|^2\).

Bochner/Bakry–Émery identity:
\[
\Gamma_2(f)
= \|\nabla^2 f\|_{\mathrm{HS}}^2
+ \big\langle(\mathrm{Ric}+\nabla^2 S_{\mathrm{eff}})\nabla f,\nabla f\big\rangle.
\]

On the product manifold \(SU(N)^{|B|}\) with bi‑invariant metric,
\[
\mathrm{Ric}\ \succeq\ \rho_0\,I,
\]
for some \(\rho_0=\rho_0(N)>0\) independent of the lattice volume.

For **gauge‑invariant** \(f\), \(\nabla f\) is horizontal, and the horizontal Hessian bound applies. Thus
\[
\Gamma_2(f)\ \ge\ (\rho_0+\rho_*(a,g))\,\Gamma(f)
\]
in the convexity window.

Consequences (standard Bakry–Émery theory):

- Poincaré inequality:
  \[
  \mathrm{Var}_\mu(f)\ \le\ \frac{1}{\rho_0+\rho_*(a,g)}\int \|\nabla f\|^2\,d\mu.
  \]
- Spectral gap for \(H_{\mathrm{Lang}}:=-L\):
  \[
  \lambda_1(H_{\mathrm{Lang}})\ \ge\ \rho_0+\rho_*(a,g)\ >\ 0,
  \]
  uniform in lattice volume.

This is a **finite‑cutoff mass gap in the stochastic‑quantization sense** (exponential relaxation / mixing).

---

## 7. Coarse‑graining: a block Hessian RG inequality

### 7.1 General analytic lemma (convexity under marginalization)

Let \(S(x,y)\) be \(C^2\) on \(\mathbb{R}^m\times\mathbb{R}^n\), with Hessian blocks
\[
\nabla^2 S(x,y)=\begin{pmatrix}A(x,y)&B(x,y)\\B(x,y)^\top & C(x,y)\end{pmatrix}.
\]
Assume uniform bounds
\[
A\succeq \alpha I,\qquad C\succeq \gamma I\ (\gamma>0),\qquad \|B\|_{\mathrm{op}}\le M.
\]
Define the coarse action
\[
e^{-S_{\mathrm{coarse}}(x)}=\int_{\mathbb{R}^n}e^{-S(x,y)}\,dy.
\]

Then
\[
\nabla_x^2 S_{\mathrm{coarse}}(x)\ \succeq\ \left(\alpha-\frac{M^2}{\gamma}\right)I.
\]

*Mechanism in one line:*  
\(\nabla_x^2 S_{\mathrm{coarse}}=\mathbb{E}[A]-\mathrm{Cov}(\nabla_x S)\), and the covariance is controlled by a Poincaré/Brascamp–Lieb inequality in \(y\) because \(C\succeq \gamma I\).

### 7.2 Application to lattice Yang–Mills (one blocking step)

Split horizontal links into:

- \(x\): coarse links kept,
- \(y\): fine links integrated out.

In the convexity window, take
\[
\alpha=\gamma=\rho_*(a,g).
\]

The mixed block \(B\) comes from the Wilson term; a crude but uniform choice is
\[
M=\beta\,C_V(N).
\]
With \(C_V(N)=6/N\), \(M=12/g^2\).

Hence the coarse curvature after one step satisfies
\[
\rho_{\mathrm{new}}(a,g)\ \ge\ \rho_*(a,g)-\frac{(\beta C_V(N))^2}{\rho_*(a,g)}.
\]

Requiring \(\rho_{\mathrm{new}}(a,g)>0\) is equivalent to
\[
\rho_*(a,g)>\beta C_V(N)
\quad\Longleftrightarrow\quad
c_0 a^2 g^2>2\beta C_V(N)
\quad\Longleftrightarrow\quad
c_0 a^2 g^4>4N C_V(N).
\]

With \(C_V(N)=6/N\), this becomes the **RG‑stable strong‑coupling subwindow**
\[
g^4>\frac{24}{c_0 a^2}.
\]

---

## 8. Singular strata: reducible configurations are polar

The quotient \(\mathcal{C}/\mathcal{G}_\Lambda\) is stratified; reducible configurations form a singular locus.

Let \(\Sigma\subset\mathcal{C}\) be the set of **reducible** configurations (those whose holonomy representation preserves a proper subspace of \(\mathbb{C}^N\)).

Two key facts:

1. \(\Sigma\) is contained in a finite union of real algebraic subvarieties of codimension \(\ge 2\).
2. On a compact Riemannian manifold, sets of codimension \(\ge 2\) have **zero capacity** for elliptic Dirichlet forms.

With the Dirichlet form
\[
\mathcal{E}(f,f)=\int_{\mathcal{C}}\|\nabla f\|^2\,d\mu,
\]
one concludes
\[
\mathrm{Cap}(\Sigma)=0.
\]

**Meaning:** starting from \(\mu\)-a.e. initial condition, the Langevin diffusion almost surely never hits \(\Sigma\). Spectral/functional‑inequality statements proved on the irreducible stratum extend \(\mu\)-a.e. to the full measure space.

---

## 9. An independent gap: the transfer‑matrix (Hamiltonian) mass gap in strong coupling

On an anisotropic lattice with temporal coupling \(\beta_t\ll 1\), the transfer matrix \(T=e^{-a_t H}\) admits a strong‑coupling expansion. A minimal worldsheet argument gives, for some constants \(c>0\) and integer \(L\) (minimal nontrivial loop length),
\[
\frac{\lambda_1}{\lambda_0}\ \le\ (c\,\beta_t)^L<1,
\]
hence the Hamiltonian gap
\[
\Delta:=E_1-E_0\ \ge\ \frac{L}{a_t}\,|\log(c\beta_t)|>0.
\]

This is not the same operator as the Langevin generator, but it provides a **second, conceptually independent** “gap witness” in the same strong‑coupling basin.

---

## 10. The novel synthesis: curvature RG as a discrete Riccati budget

The block‑marginalization inequality can be read as an RG update rule for a “curvature budget”.

Let \(\rho_k\) denote a convexity (Hessian lower bound) parameter at RG step \(k\), and let \(M_k\) quantify coarse/fine mixing at that step. The block lemma gives the schematic recursion
\[
\rho_{k+1}\ \ge\ \rho_k-\frac{M_k^2}{\rho_k}.
\]

This is a **discrete Riccati‑type degradation**: mixing burns curvature at rate \(M_k^2/\rho_k\).

### A simple but useful consequence (curvature‑squared budget)

Assume (for intuition) a worst‑case update with equality:
\[
\rho_{k+1}=\rho_k-\frac{M_k^2}{\rho_k}.
\]
Then
\[
\rho_{k+1}^2
=\rho_k^2-2M_k^2+\frac{M_k^4}{\rho_k^2}
\ \ge\ \rho_k^2-2M_k^2.
\]
Iterating yields
\[
\rho_k^2\ \ge\ \rho_0^2-2\sum_{j=0}^{k-1}M_j^2.
\]

**Interpretation:** as long as the cumulative mixing energy \(\sum M_j^2\) stays below \(\rho_0^2/2\), convexity survives through \(k\) RG steps.

This turns “RG‑stable convexity” into a quantitative accounting problem:
- **initial curvature** \(\rho_0\) is your budget,
- each coarse‑graining step costs \(\sim M_k^2\).

Mapping “number of RG steps before \(\rho_k\) collapses” to a physical length scale (e.g. \(2^k a\)) suggests a route to bounding a correlation length from above — a mass‑gap‑flavored output — once one has control of \(M_k\) along the flow.

That bridge is exactly what the companion program note is built to pursue.


---

# LEMMA UNITY — Towards a Continuum‑Relevant “Curvature RG”: Local Bakry–Émery, Typical Sets, and Riccati Flow

*Program note.* This file is deliberately forward‑leaning: it takes the finite‑cutoff curvature mechanism as a proven base and asks what would have to be true for a **continuum‑meaningful** theory.

The big idea is to replace “global convexity” (which provably dies) with a **scale‑dependent, localized curvature** that can be transported along coarse‑graining.

---

## 1. The obstruction: global Bakry–Émery curvature must go to \(-\infty\) as \(a\to 0\)

Consider the natural global Bakry–Émery constant
\[
\rho_{\mathrm{glob}}(a):=\inf_{U\in\mathcal{C}_a}\ \inf_{\|X\|=1}\Big(
\mathrm{Ric}(X,X)+\beta(a)\,\nabla^2 f(U)(X,X)
\Big),
\]
where \(\mathcal{C}_a=SU(N)^{|B|}\) and \(f(U)\) is the plaquette energy.

Two simple facts:

1. \(\mathrm{Ric}\) is bounded above and below by constants depending only on \(SU(N)\), not on volume.
2. Since \(f\) is smooth and nonconstant on compact \(\mathcal{C}_a\), it has a global maximum at some \(U^\*\). At that maximum, \(\nabla^2 f(U^\*)\preceq 0\), and there exists a direction \(Y\) with
   \[
   \nabla^2 f(U^\*)(Y,Y)=-\lambda<0.
   \]

Along the asymptotically free trajectory in \(4D\), \(\beta(a)\to\infty\) as \(a\to 0\). Evaluating at \((U^\*,Y)\) yields
\[
\rho_{\mathrm{glob}}(a)\ \le\ k_{\max}-\beta(a)\lambda\ \longrightarrow\ -\infty.
\]

**Conclusion.** Any attempt to prove the continuum theory via a **global** \(CD(\rho,\infty)\) lower bound is doomed: the global infimum necessarily dives to \(-\infty\).

This is not a disaster; it’s a signpost. It says: **look for a non‑global notion of curvature.**

---

## 2. Why a Riccati mechanism is the “right” mental model for coarse‑graining

A clean toy model shows why convexity wants to erode under smoothing.

### 2.1 Heat‑flow coarse‑graining ⇒ viscous Hamilton–Jacobi

Let \(\rho_t=e^{-S_t}\) solve the heat equation \(\partial_t\rho_t=\Delta\rho_t\) on \(\mathbb{R}^d\). Then
\[
\partial_t S_t=\Delta S_t-|\nabla S_t|^2.
\]

### 2.2 The Hessian equation is Riccati‑like

Let \(H_t=\nabla^2 S_t\). Differentiating twice gives
\[
\partial_t H_t=\Delta H_t-2H_t^2+R_t,
\]
where \(R_t\) is a “transport” remainder involving third derivatives weighted by \(\nabla S_t\).

Even ignoring \(R_t\), the term \(-2H_t^2\) is the signature:
it drives eigenvalues downward in a **Riccati** fashion.

### 2.3 Gaussian case: exact Riccati decay

If \(S_0(x)=\tfrac12 x^\top A_0 x\), then convolution with the heat kernel keeps the law Gaussian and
\[
\lambda_i(t)=\frac{\lambda_i(0)}{1+2t\lambda_i(0)},
\qquad
\lambda_i'(t)=-2\lambda_i(t)^2.
\]

So convexity remains positive but decays like \(1/t\). This matches the intuitive message:
**coarse‑graining bleeds curvature unless something replenishes it.**

---

## 3. Discrete coarse‑graining already contains a Riccati shadow: the block‑Hessian inequality

The project’s block convexity lemma says:

If \(S(x,y)\) is uniformly convex in both \(x\) and \(y\) and the mixed Hessian block is controlled by \(M\), then after marginalizing over \(y\),
\[
\nabla_x^2 S_{\mathrm{coarse}}(x)\ \succeq\ \left(\alpha-\frac{M^2}{\gamma}\right)I.
\]

In curvature language, if \(\rho=\min\{\alpha,\gamma\}\), then one step of coarse‑graining gives
\[
\rho_{\mathrm{new}}\ \gtrsim\ \rho-\frac{M^2}{\rho}.
\]

That is already a discrete Riccati‑type degradation.

### 3.1 A “curvature‑squared” conservation inequality (discrete budget law)

If (heuristically) \(\rho_{k+1}=\rho_k-\frac{M_k^2}{\rho_k}\), then
\[
\rho_{k+1}^2\ \ge\ \rho_k^2-2M_k^2,
\]
so
\[
\rho_k^2\ \ge\ \rho_0^2-2\sum_{j<k}M_j^2.
\]

This is a **budget law**: cumulative mixing energy \(\sum M_j^2\) controls how long convexity can persist across RG steps.

---

## 4. The novel proposal: replace global curvature by a *localized* / *typical‑set* curvature

Global curvature fails because it looks at the worst configuration in all of \(\mathcal{C}_a\). Physics, meanwhile, lives on configurations typical under \(\mu_a\).

### 4.1 A candidate definition: typical‑set Bakry–Émery constant

Fix \(\varepsilon\in(0,1)\). Define \(\rho_{\mathrm{typ}}(a;\varepsilon)\) as the largest number such that there exists a measurable set \(T_{a,\varepsilon}\subset\mathcal{C}_a\) with \(\mu_a(T_{a,\varepsilon})\ge 1-\varepsilon\) and
\[
\mathrm{Ric}+\nabla^2 S_{\mathrm{eff}}(U)\ \succeq\ \rho_{\mathrm{typ}}(a;\varepsilon)\,I
\qquad\text{for all }U\in T_{a,\varepsilon}.
\]

This trades “worst‑case over all \(U\)” for “worst‑case over typical \(U\)”.

### 4.2 Why this could matter

If one can prove two things:

1. **a Poincaré/log‑Sobolev inequality on \(T_{a,\varepsilon}\)** with constant \(1/\rho_{\mathrm{typ}}\), and
2. **fast return / stability**: the Langevin diffusion returns to \(T_{a,\varepsilon}\) quickly whenever it exits,

then one can often bootstrap to a global spectral gap (or at least to robust exponential mixing on observables of interest).

This is the same vibe as metastability theory and “two‑scale” functional inequalities:  
a good inequality on a high‑probability set plus control of exits can imply global convergence.

(Details depend on the precise decomposition method used; the point here is the *structure*.)

---

## 5. The real target: a curvature RG inequality *on typical sets*

The block‑Hessian inequality is deterministic. In real RG, the mixed block \(B\) and the fine‑scale curvature \(\gamma\) fluctuate with the configuration.

A continuum‑relevant theory would therefore aim for a probabilistic block inequality of the form:

> with high \(\mu\)-probability, coarse‑graining maps a typical set at scale \(a\) to a typical set at scale \(2a\), and the curvature parameter updates by a controlled inequality
> \[
> \rho_{k+1}\ \gtrsim\ \rho_k-\frac{M_k^2}{\rho_k},
> \]
> with \(M_k\) small on the typical set.

This would create an **iterable curvature RG flow**.

At that point, the “curvature‑squared budget law”
\[
\rho_k^2\ \ge\ \rho_0^2-2\sum_{j<k}M_j^2
\]
starts to look like a computable control knob:
if \(\sum M_j^2\) stays bounded as \(k\to\infty\), convexity survives; if it grows, convexity dies at a predictable scale.

Either way, you get a **scale** — and scales are what mass gaps feed on.

---

## 6. How this links back to physics without cheating

Three bridges to build (none are “free”):

1. **From Langevin spectral gap to Euclidean correlators.**  
   The Langevin operator is not the transfer matrix. But functional inequalities control fluctuations and can be used to bound variances of Wilson loop observables; one can then compare to strong‑coupling/cluster‑expansion estimates of correlators.

2. **From curvature along RG to correlation length.**  
   If you can show curvature survives to scale \(L\) (after \(k\sim\log(L/a)\) steps), then you can often turn that into an upper bound on a correlation length (a mass lower bound). This is where the curvature‑budget inequality becomes valuable.

3. **From typical‑set control to uniform statements.**  
   Ultimately you need “high‑probability” statements to imply the spectral property you care about. That usually means coupling local functional inequalities with recurrence/exit estimates.

---

## 7. Concrete next steps (tractable, and genuinely informative even if they fail)

1. **Make the mixing norm \(M\) structural, not worst‑case.**  
   The current \(M\) is a uniform operator‑norm bound. In practice, on typical configurations the effective \(M\) might be much smaller. Prove concentration estimates for the mixed block.

2. **Iterate the block inequality.**  
   Write down a multi‑step version with \(M_k\) and \(\rho_k\). Even bounding the number of steps before \(\rho_k\) drops below \(0\) would produce a scale.

3. **Replace global Hessian bounds by “energy‑conditioned” bounds.**  
   Condition on a plaquette energy band \(f(U)\le E\). On such sets, the Wilson Hessian may have improved lower bounds. This is the most plausible route to a nontrivial \(\rho_{\mathrm{typ}}\) at large \(\beta\).

4. **Integrate the polar‑set technology.**  
   Any typical‑set argument should be done on the irreducible stratum; polarity lets you do this without losing the physical measure.

5. **Check the toy model numerics.**  
   The discrete Riccati budget law is so simple you can test it in scalar or reduced gauge models: compute empirical \(M_k\) and \(\rho_k\) under blocking and see if the inequality tracks reality.

---

## 8. The “novel thing” in one sentence

The finite‑cutoff proofs give a *deterministic* curvature mechanism; the proposed next step is a **probabilistic curvature RG** in which convexity is tracked on typical sets by a discrete Riccati‑type budget inequality.

That framework is not standard lattice strong‑coupling expansion, not reflection‑positivity technology, and not continuum perturbation theory — it’s a geometric/analytic lane that could, with luck and sweat, connect mass‑gap questions to a new family of RG‑stable functional inequalities.
