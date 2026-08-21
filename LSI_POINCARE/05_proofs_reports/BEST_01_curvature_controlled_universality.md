# Curvature-Controlled Universality Classes (Working Framework)

This note distills a *big idea* that keeps resurfacing across the project files:

> Treat **Bakry–Émery convexity / functional-inequality constants** as the fundamental RG-propagated invariant, and define “universality classes of gauge measures” by that invariant rather than by microscopic lattice actions.

This is not Standard Model lore; it’s closer to:

> **QFT as a controlled limit of convex measures with operator-theoretic reconstruction.**

I’m writing this as a **working framework** (a precise “definition + conditional theorem” package), not as a claim that the Clay statement is already closed.

---

## 1. The invariant you actually propagate

The project’s technical engine repeatedly tries to propagate one of these equivalent controls (on the *physical/gauge-invariant sector*):

- a **uniform Bakry–Émery curvature lower bound** \(\kappa>0\),
- a **Poincaré (spectral gap) constant** \(\lambda_{\mathrm{PI}}>0\),
- a **log–Sobolev constant** \(\alpha_{\mathrm{LSI}}>0\).

The (ideal) implication chain is the standard one:

\[
\nabla^2 V \succeq \kappa I \quad\Longrightarrow\quad \mathrm{LSI}(\alpha\ge \kappa)
\quad\Longrightarrow\quad \mathrm{PI}(\lambda\ge \alpha).
\]

So from a systems perspective, the “RG invariant” you’re trying to carry is essentially:

\[
\boxed{\text{a positive functional-inequality constant, uniform in volume and scale.}}
\]

---

## 2. Definition: curvature-controlled gauge measures

Fix a compact Lie group \(G\) (e.g. \(SU(3)\)).  
For each lattice spacing \(a\), let \(\mathcal A_a\) be the configuration space of link fields, and \(\mu_a\) a gauge-invariant probability measure.

### Definition (Curvature-controlled family)
A family \(\{\mu_a\}\) is **\((\kappa_0,\alpha,b;R_0)\)-curvature-controlled** if there exists:

1. A SAFE region \(K_a\subset \mathcal A_a\) (e.g. \(\|A\|\le R_0\) in right-invariant coordinates) such that on \(K_a\),
   \[
   \mathrm{Ric}_{\mu_a}^{\mathrm{phys}} \ \succeq\ \kappa_0 I,
   \]
   uniformly in volume (and uniformly in \(a\) along the RG trajectory).

2. A Lyapunov function \(W_a\ge 1\) with drift condition (for the gauge-invariant diffusion generator \(L_a\))
   \[
   L_a W_a \ \le\ -\lambda W_a + b\,\mathbf 1_{K_a},
   \]
   with \(\lambda,b\) independent of the lattice volume.

3. An RG/coarse-graining map \(R_{a\to a'}\) that is contractive on physical directions and degrades convexity at most by a factor \(\alpha\in(0,1]\):
   \[
   \kappa(a') \ \ge\ \alpha\,\kappa(a),
   \]
   along the chosen RG step.

This is the “input data” needed to force global PI/LSI and keep it from collapsing as \(a\to 0\).

---

## 3. Conditional theorem: curvature control \(\Rightarrow\) universality-class style stability

### Theorem (Conditional “curvature class” stability)
Assume \(\{\mu_a\}\) is \((\kappa_0,\alpha,b;R_0)\)-curvature-controlled and that the standard local-to-global patching theorems apply on each \(\mathcal A_a\). Then:

1. Each \(\mu_a\) satisfies a **global** PI/LSI on the gauge-invariant sector with constants bounded below by a function of \((\kappa_0,\alpha,b)\) independent of volume.

2. Consequently, the associated gauge-invariant diffusion generator has a uniform spectral gap \(\lambda_*(a)\ge \lambda_*>0\).

3. If, in addition, a diffusion\(\to\)OS bridge inequality holds (see `BEST_03_diffusion_to_OS_bridge.md`), then the OS Hamiltonian satisfies a **uniform mass gap**:
   \[
   \Delta_{\mathrm{OS}}(a)\ \ge\ \Delta_0>0
   \]
   and the gap persists in the continuum limit.

*Proof skeleton.* Local curvature gives local FI on \(K_a\); Lyapunov drift patches it globally; RG contractivity prevents loss of \(\kappa\); the bridge theorem converts diffusion decay into Euclidean-time OS decay.

---

## 4. Why call this a “universality class”?

Because the definition does **not** mention the Wilson action, Haar measure, or any particular lattice discretization. It’s a geometric/analytic *envelope*.

Two microscopic gauge measures could be considered to lie in the same curvature-controlled “universality class” if they share:

- the same coarse-graining (or comparable) contraction structure,
- comparable \((\kappa_0,\alpha,b)\) data,
- and the same continuum OS reconstruction.

That would be a new way to slice the space of lattice gauge theories.

---

## 5. Where the physics bites back

To connect this to Clay’s YM problem, you’d ultimately need to prove:

- the curvature-controlled family corresponding to your lattice model lands in the **same continuum OS theory** as standard YM (same Schwinger functions / same Wilson-loop scaling), or else explicitly acknowledge it defines a different universality class.

Either outcome can still be mathematically valuable; they’re just different claims.

---

## 6. Concrete “next-theorems” this framework suggests

If you wanted to turn this framework into publishable standalone results, the clean targets are:

1. **A gauge-invariant local-to-global LSI theorem** for lattice gauge measures with an explicit Lyapunov drift.
2. **A comparison/intertwining theorem** that upgrades diffusion gap to OS Euclidean-time decay (the “readout layer”).
3. **A universality theorem**: show that adding/removing the Haar Jacobian term is RG-irrelevant for gauge-invariant observables (if you want Clay equivalence).
