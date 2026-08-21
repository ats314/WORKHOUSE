# PRO12 Notes 01 — Turning H1 (Uniform LSI) into an Output

## Purpose
The project currently treats **H1** (“a scale-uniform Log–Sobolev inequality / spectral gap”) as a foundational hypothesis.
This note condenses the strongest material in the repo into a single *derivation blueprint* for making **H1 a theorem**.

The hinge statement is:

\[
\boxed{\text{Uniform positive Bakry–Émery curvature on the horizontal (physical) bundle }\Rightarrow \text{uniform LSI}\Rightarrow \text{uniform spectral gap}.}
\]

The repo already contains three big ingredients:

1. a **horizontal projector skeleton** (gauge-invariant gradients live in the horizontal bundle),
2. a **local curvature floor** coming from the **Haar Jacobian** in exponential coordinates,
3. a **local-to-global drift patching** mechanism + a quantitative **RG curvature stability class** \((\kappa_*,\alpha)\).

What’s missing is *closing the loop* from an actual RG map / flow equation to the PBH/Riccati inequality and then pinning down positivity of the source term and mixing control. This note makes that loop explicit.

---

## 1. The geometric object you actually need

Let \(M_\Lambda = G^{E(\Lambda)}\) be the lattice link-manifold with product bi-invariant metric \(g_\Lambda\).
Let \(\mathcal G_\Lambda = G^{V(\Lambda)}\) act by lattice gauge transformations.
At a configuration \(U\), tangent vectors split into

\[
T_U M_\Lambda = V_U \oplus H_U, \qquad H_U := V_U^{\perp}.
\]

For a gauge-invariant observable \(f\), we have
\[
 df_U(X^\sharp(U)) = 0 \;\forall X \quad\Rightarrow\quad \nabla f(U)\in H_U.
\]
So every functional inequality you care about only “sees” the geometry in horizontals.

**Target curvature statement (horizontal Bakry–Émery):**

a lower bound of the schematic form
\[
\mathrm{Ric}_{\mathrm{BE}}\big|_{H_U}
\;:=\;
\Big(\mathrm{Ric}_{g_\Lambda} + \nabla^2 V\Big)\Big|_{H_U}
\;\ge\; \rho_0\, g_\Lambda\Big|_{H_U}
\qquad\text{uniformly in }\Lambda.
\]

Then Bakry–Émery gives (at each lattice spacing)
\[
C_{\mathrm{LSI}} \le \frac{2}{\rho_0},\qquad \lambda_1\ge\rho_0.
\]

**This is exactly what H1 asserts.** The point here: the repo already sketches how to obtain \(\rho_0>0\) uniformly.

---

## 2. Local curvature floor from the Haar Jacobian

Work in right-invariant exponential coordinates on each link:
\[
U_\ell = \exp(X_\ell),\qquad X_\ell\in\mathfrak g.
\]
The Haar volume element becomes
\[
d\mathrm{Haar}(U_\ell) = J(X_\ell)\, dX_\ell,
\]
so writing the YM measure relative to Lebesgue \(dX\) introduces the **Haar potential**
\[
V_{\mathrm{Haar}}(X) := -\log J(X).
\]
Two facts matter:

1. Near the identity, \(V_{\mathrm{Haar}}\) is strictly convex and isotropic;
2. Its Hessian supplies a **uniform curvature floor** in a controlled ball (the “SAFE region”).

Numerically (and consistent with the theoretical normalization in the repo):

- \(SU(2)\): smallest Hessian eigenvalue near the identity \(\approx 1/6\).
- \(SU(3)\): smallest Hessian eigenvalue near the identity \(\approx 1/4\).

This is the constant named
\[
\kappa_* \approx 0.25 \quad \text{(for }SU(3)\text{)}.
\]

---

## 3. Wilson Hessian positivity lives in the co-exact horizontal sector

At the identity configuration \(U^{(0)}\) (all links equal to the group identity), linearizing turns tangent vectors into \(\mathfrak g\)-valued 1-cochains \(\mathcal C^1\).

You get the discrete Hodge decomposition:
\[
\mathcal C^1 = \underbrace{\mathrm{im}(d_0)}_{\text{vertical / pure gauge}}
\oplus
\underbrace{\ker(\Delta_1)}_{\text{harmonic / global}}
\oplus
\underbrace{\mathrm{im}(d_1^*)}_{\text{co-exact / physical}}.
\]

In this linear regime,
\[
V_{U^{(0)}} \simeq \mathrm{im}(d_0),
\qquad
H_{U^{(0)}} \simeq \ker(\Delta_1)\oplus\mathrm{im}(d_1^*).
\]

The repo’s key structural identity is that the Wilson action has Hessian
\[
\nabla^2 S_W\big(U^{(0)}\big) = 2c_W\, d_1^* d_1.
\]
Consequences:

- It vanishes on \(\mathrm{im}(d_0)\) (gauge) and \(\ker(\Delta_1)\) (harmonic).
- It is strictly positive on \(\mathrm{im}(d_1^*)\) (local physical modes).

So the Wilson piece gives you positivity **exactly where physics lives** (local horizontals), while the Haar curvature contributes positivity everywhere and stabilizes topology/harmonics.

---

## 4. Local-to-global drift patching

Local curvature bounds are not enough: you need to control excursions outside SAFE.

The repo’s drift mechanism is the standard “Lyapunov + local LSI implies global LSI” paradigm:

- choose a coercive Lyapunov function \(W\ge 1\) with a drift inequality
\[
LW \le -\alpha W + b\,\mathbf 1_K,
\]
- prove a local LSI on a compact set \(K\) (typically SAFE),
- conclude a **global** LSI with constant controlled by \(\alpha\), the local LSI constant on \(K\), and \(\int W\,d\mu\).

This provides the “escape valve”: even if curvature is certified only on SAFE, the drift forces the measure to spend most mass there.

---

## 5. The RG curvature class and why \(\alpha\) matters

The repo introduces an RG-stability class of curvature-controlled pairs \((g,V)\):

\[
(g,V)\in\mathcal C(\kappa)
\quad\Longleftrightarrow\quad
\mathrm{Ric}_g + \nabla^2 V \ge \kappa g.
\]

An RG trajectory \((g_n,V_n) = \mathcal R^n(g_0,V_0)\) is called \((\kappa_*,\alpha)\)-stable if
\[
\mathrm{Ric}_{V_n} \ge \alpha^n \kappa_*\, g_n \qquad \forall n\ge 0.
\]

In the SAFE constants ledger, the repo records
\[
\kappa_*\approx 0.25,
\qquad
\delta\approx 0.006,
\qquad
\alpha = 1-\delta/\kappa_* \approx 0.976.
\]

The interpretation is crisp:

- \(\kappa_*\) is the curvature floor you have “for free” from Haar,
- \(\delta\) is the maximal curvature loss per RG step from the interacting piece (Wilson / blocking / reparametrization),
- \(\alpha\) is the per-step degradation factor.

If you can also show that the RG map is eventually contractive (PBH/Riccati improvement after burn-in), you can turn \(\alpha<1\) into an *effective* \(\alpha\approx 1\) and get a genuinely uniform infimum.

---

## 6. What remains to be proved (the “PBH hinge”)

To truly demote H1 from axiom to output, the remaining tasks are:

1. **Derive PBH/Riccati from a real RG map** (e.g. a gradient-flow–defined coarse-graining like Wilson flow + blocking), not as a postulate.
2. **Prove positivity of the source term \(\mathcal R(t)\)** on the physical/horizontal sector.
3. **Control off-diagonal mixing** under coarse-graining so that negative curvature cannot leak into horizontals.

The code delivered alongside this note is designed to *test these mechanisms numerically* on small lattices for \(SU(2)\) and \(SU(3)\), using autodiff Hessian-vector products and explicit horizontal projection.

---

## 7. Minimal “theorem stack” once the hinge is closed

Once a uniform horizontal curvature bound is established (globally or via drift patching), the rest of the project’s machinery becomes straightforward:

1. **Uniform LSI and Poincaré** on each lattice spacing.
2. **Mosco stability / tightness** to pass LSI to the continuum Dirichlet form.
3. **OS reconstruction** and transfer of Euclidean decay to a Hamiltonian spectral gap.

In other words: the cathedral really does swing on the PBH hinge.

---

## 4. Local-to-global: drift patching is the globalizer

A local curvature/LSI statement in a bounded SAFE region is not enough: the YM configuration space is noncompact in the coordinate charts you use for estimates.
The repo includes a standard but lethal tool for that: **Lyapunov drift patching**.

The template is:

- Find a coercive Lyapunov function W ≥ 1 such that the generator L satisfies a drift condition

  **(Drift)**  LW ≤ -α·W + b·1_K    for some α>0 and a compact set K.

- Prove a **uniform local LSI** on K (this is where SAFE-region curvature lives).

Then a global LSI follows, with a constant controlled by α, the local constant on K, and a tame moment term involving ∫W dμ.

In other words: SAFE gives you a “good patch”; drift tells you trajectories return to the patch fast enough.

---

## 5. RG curvature stability class (κ*, α) and why the constants matter

The repo packages RG stability in a clean quantitative notion:

- Fix κ* > 0 and α ∈ (0,1].
- A trajectory under the coarse-graining map ℛ is (κ*, α)-curvature-stable if

  Ric_BE(V_n) ≥ α^n κ* · g_n   for all n ≥ 0.

Then (stepwise Bakry–Émery) implies

- C_LSI^(n) ≤ 2/(α^n κ*)
- spectral gap λ₁^(n) ≥ α^n κ*

The repo’s SAFE-region ledger (for SU(3) in right-invariant exponential coordinates) spells out:

- κ* ≈ 0.25  (Haar-induced curvature floor)
- δ ≈ 0.006 (maximal Hessian variation from the Wilson piece across the SAFE ball)
- α = 1 - δ/κ* ≈ 0.976

So curvature degrades *slowly* per RG step, and for ≲ 100 steps you still have α^n κ* comfortably positive.
This is exactly the “cathedral hinge”: once α is close enough to 1 and you have a mechanism that eventually improves convexity, you get a uniform infimum κ_∞ > 0.

---

## 6. What’s still nontrivial (and exactly where code helps)

The repo is very explicit about the three remaining hard steps:

1. **Derive PBH/Riccati from an actual RG map (or exact gradient flow)** rather than postulating it.
2. **Show positivity of the source term R(t)** on the physical/local/horizontal sector.
3. **Control off-diagonal mixing under coarse-graining** so negative curvature cannot leak in from decoupled sectors.

These are geometry-meets-QFT statements, and they’re *hard to prove abstractly*.
But they are also exactly the kind of statements you can probe numerically on small lattices using:

- autodiff Hessian–vector products (HVPs),
- a gauge-covariant horizontal projector (Faddeev–Popov solve),
- a flow-time blocking map (gradient flow + decimation),
- operator-norm tests for commutators / Schur complements.

A full Colab-ready PyTorch implementation is provided in the code file shipped with these notes.

---

## 7. The endgame chain (once H1 is output)

Once H1 is proven (uniform LSI / spectral gap on every lattice scale), the remainder of the project is comparatively “mechanical functional analysis”:

- Tightness + existence of a continuum limit measure,
- Mosco convergence to lift the Dirichlet form / LSI,
- Osterwalder–Schrader reconstruction to convert Euclidean decay into a Hamiltonian mass gap.

That pipeline is already laid out cleanly in the repo; the one piece that must not remain axiomatic is the uniform curvature/LSI input.

