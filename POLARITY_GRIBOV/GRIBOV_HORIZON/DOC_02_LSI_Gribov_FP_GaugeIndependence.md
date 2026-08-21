# DOC 02 — LSI, Gribov Avoidance, and Gauge Independence via Faddeev–Popov

## 0. Purpose

Gauge fixing is usually where otherwise elegant Euclidean proofs go to die.

This note extracts the project’s central “safety valve” idea:

> **If the lattice/continuum measure satisfies a *uniform* log-Sobolev inequality (LSI), then the measure is effectively supported inside a region where the action is strongly convex; in such a region the gauge slice intersects each orbit uniquely, so the Faddeev–Popov (FP) identity is valid “where it matters”, and gauge-invariant expectations are gauge independent.**

This mechanism is used to protect:
- gauge independence (fixed vs unfixed expectations for gauge-invariant observables),
- reflection positivity on the physical algebra,
- and the OS reconstruction chain.

Primary project sources:
- `00_CORE_HYPOTHESES.md`
- `PROOF_REVIEW_OS1.md`
- `04_MASS_GAP_THEOREM.md`
- `From Local to Global LSI with Drift and TIghten the LSI Spectral Gap Chain.txt`

## 1. The geometric obstruction: Gribov copies

Let \(\mathscr{A}\) be the (lattice) configuration manifold \(G^{E(\Lambda)}\), with gauge group \(\mathscr{G}=G^{V(\Lambda)}\) acting by
\[
(U^g)_{x,\mu} = g_x\, U_{x,\mu}\, g_{x+\hat\mu}^{-1}.
\]

A gauge condition is a section \(G(U)=0\) (e.g. Landau gauge). The standard FP identity
\[
1 = \int_{\mathscr{G}} \delta(G(U^g))\det \Delta_{\rm FP}(U^g)\, dg
\tag{FP}
\]
implicitly assumes the orbit intersects the gauge slice uniquely (no Gribov copies), so that the delta function integrates to 1 and \(\det\Delta_{\rm FP}\) is nonzero.

Nonperturbatively, Gribov copies exist on the full configuration space; so (FP) cannot hold globally as a pointwise identity.

## 2. The project’s move: “measure-theoretic” FP validity

Rather than insisting on a global geometric statement (“no Gribov copies anywhere”), the project tries to prove a probabilistic statement:

> the measure is concentrated in a **SAFE region** \(K\subset \mathscr{A}\) where the gauge-fixed action is strongly convex and the gauge slice is unique.

Then one only needs (FP) on \(K\), plus a tail estimate controlling \(\mu(K^c)\).

This is where local-to-global LSI technology comes in.

## 3. Local-to-global upgrade via Lyapunov drift (skeleton)

Assume:
1. A **local LSI** holds on \(K\) with constant \(\rho_K>0\):
   \[
   \operatorname{Ent}_{\mu_K}(f^2) \le \frac{2}{\rho_K}\int |\nabla f|^2\, d\mu_K,
   \]
   uniformly in volume (blocks/tiles).

2. There exists a **Lyapunov function** \(W\ge 1\) for the diffusion generator \(L\) such that
   \[
   LW \le -\alpha W + b\,\mathbf{1}_K
   \qquad (\alpha>0).
   \tag{Lyap}
   \]
   This controls escape into \(K^c\) and yields tail bounds.

Then, by entropy/variance decomposition and patching arguments (Rothaus-type lemmas; weighted LSIs), one can upgrade to a **global LSI** with constant
\[
\rho \gtrsim \min\!\left(\rho_K,\ \frac{\alpha}{1+\log\int W\,d\mu + \text{cutoff errors}}\right).
\tag{Global}
\]

This is precisely the kind of “local convexity + drift back” mechanism used in hypocoercivity and metastability.

## 4. From strong convexity to uniqueness of gauge slice (working lemma)

On a lattice manifold, the gauge-fixing functional (e.g. Landau gauge functional) typically looks like a sum of local convex terms near identity. In a region where the Hessian is bounded below,
\[
\nabla^2 S_{\rm gf}(U)\big|_{\rm horiz} \ge \rho_0\, I,
\tag{Convex}
\]
one expects:
- the gauge-fixed action is strictly convex along gauge orbits in the relevant directions,
- thus each orbit has a unique minimizer satisfying the gauge condition.

A typical statement one would want is:

> **Lemma (Gribov-free region).**  
> On the SAFE set \(K=\{U:\nabla^2 S_{\rm gf}(U)\ge \rho_0 I\}\), the gauge-fixing map \(U\mapsto G(U)\) has a unique zero on each orbit, and \(\det\Delta_{\rm FP}(U)>0\).

The project treats (Convex) as morally implied by uniform LSI / Bakry–Émery curvature bounds, though turning that into a strict geometric statement is nontrivial.

## 5. Gauge independence for gauge-invariant observables

Let \(F\) be gauge invariant (\(F(U^g)=F(U)\)). Consider two measures:

- the unfixed Wilson measure \(d\mu^W(U)\propto e^{-S_W(U)}\, dU\) (Haar),
- the gauge-fixed measure \(d\mu^{\rm gf}(U)\propto e^{-S_W(U)}\delta(G(U))\det\Delta_{\rm FP}(U)\, dU\).

Assuming (FP) holds \(\mu^W\)-a.e. on the measure’s effective support, then:
\[
\int F\, d\mu^W
=
\int F(U)\!\left(\int \delta(G(U^g))\det\Delta_{\rm FP}(U^g)\, dg\right)\! d\mu^W(U)
=
\int F\, d\mu^{\rm gf}.
\]

Thus for gauge-invariant observables,
\[
\langle F\rangle_{\rm fixed} = \langle F\rangle_{\rm unfixed}.
\tag{GI}
\]

This is the key identity used to inherit reflection positivity from the unfixed lattice measure onto the gauge-fixed physical sector.

## 6. Why this is potentially generative

This is a “physics-proof” attempt at a deep structural statement:

- **Functional inequality (LSI) as a Gribov filter.**  
  Rather than handling Gribov copies by intricate gauge-group topology, the measure is claimed to avoid them because strict convexity forces it.

If it can be made rigorous, it suggests a broader principle:

> **Nonperturbative gauge fixing may be controlled by *concentration of measure* rather than by global gauge geometry.**

That is a theme that could generalize beyond Yang–Mills to other gauge systems (and even to constrained statistical models).

## 7. Key technical gaps (and concrete next steps)

1. **Convexity-from-LSI is not automatic.** LSI does not generally imply pointwise Hessian bounds; it implies concentration/spectral information. One must specify a route:
   - prove a Bakry–Émery curvature bound \(\Gamma_2\ge\rho\Gamma\), which *does* encode Hessian information, or
   - use local-to-global drift patching: show the measure spends nearly all time in a convex region.

2. **Specify the gauge condition.** “Gauge slice uniqueness” depends strongly on the gauge-fixing functional used (Landau, Coulomb, maximal Abelian, etc).

3. **Quantify the tail \(\mu(K^c)\).** The drift condition (Lyap) is the natural place to do it. Prove \(\mu(K^c)\) is exponentially small in block size or flow time.

4. **Track the sign of \(\det\Delta_{\rm FP}\).** Positivity is essential for reflection positivity inheritance in the argument used.

