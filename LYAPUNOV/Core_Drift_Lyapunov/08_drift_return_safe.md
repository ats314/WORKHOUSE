
# Drift / Return-to-SAFE: What you *can* prove, what fails, and a path to a real theorem

## Why this matters

The local curvature certificate in a SAFE region \( \mathcal{S}=B_{R_0}\) is only half the game.
To upgrade **local** convexity/LSI to **global** LSI with usable constants, you need a mechanism that prevents the dynamics (or the equilibrium measure) from living mostly outside \(\mathcal{S}\).

In the existing writeup, this role is played by a **Lyapunov drift inequality**
\[
\mathcal{L}W \le -a\,W + b\,\mathbf{1}_{\mathcal{S}},
\]
for the generator \(\mathcal{L}\) of the reversible diffusion (Langevin on the configuration manifold).

This note does two things:

1. **Refutes** the naive global drift claim for the most natural Lyapunov candidates (plaquette action, squared distance, etc.) without extra hypotheses.
2. Gives a realistic route to a correct “return-to-SAFE” theorem: either
   - (A) a *dynamics* argument with a carefully constructed Lyapunov function and a small set that includes all non-SAFE critical regions, or
   - (B) a *static* argument proving that the Gibbs measure assigns overwhelming weight to a slightly enlarged certified region (usually via cluster expansion / high-temperature uniqueness / polymer estimates, not by drift).

---

## 1. Why the naive drift fails (mechanism)

Take the standard reversible diffusion with stationary measure
\[
\mu(dU)\propto e^{-V(U)}\,d\mathrm{vol}(U),
\qquad
\mathcal{L} = \Delta - \langle\nabla V,\nabla\cdot\rangle.
\]

A common attempt is to choose \(W(U)=1+S_W(U)\) or \(W(U)=e^{\eta S_W(U)}\), where \(S_W\) is the Wilson action (sum over plaquettes).

### Obstruction: large-action critical points exist
For compact gauge groups, the single-plaquette class function
\[
\phi(U)=1-\frac{1}{N}\Re\mathrm{Tr}(U)
\]
has not only a global minimum at \(U=I\), but also **other critical points** (e.g. center elements), where \(\nabla\phi=0\) but \(\phi\) is large.

At such points, the dominant negative drift term
\(-\langle\nabla V,\nabla W\rangle\) collapses because \(\nabla S_W=0\),
yet \(W\) itself is large. This breaks any inequality of the form
\[
\mathcal{L}W \le -a W + b\mathbf{1}_{\mathcal{S}}
\]
with \(\mathcal{S}\) a *small-field* neighborhood of the identity, unless you enlarge the “small set” to include neighborhoods of these other critical regions.

This is not a technical quibble; it is a structural fact about smooth functions on compact manifolds: **no global Lyapunov drift toward a single small neighborhood can hold if the potential has other stationary points outside that neighborhood.**

---

## 2. What you *can* prove without lying to yourself

### Option A: Drift to a *multi-well* small set
Let \(\mathcal{K}\) be a union of neighborhoods around **all** critical sets of \(V\) that are relevant at the chosen parameters (including center-like sectors, harmonic sectors, etc.).
Then one can often prove a Harris-type drift/minorization:
\[
\mathcal{L}W \le -a W + b\mathbf{1}_{\mathcal{K}},
\]
because outside \(\mathcal{K}\) the gradient cannot be small everywhere.

But this does *not* directly give “the measure spends its life in the SAFE certificate region” unless:
- the SAFE region contains \(\mathcal{K}\), or
- you prove that \(\mu(\mathcal{K}\setminus\mathcal{S})\) is tiny and can be absorbed.

### Option B: Static concentration (no drift required)
Instead of chasing a drift inequality, prove directly that under the target scaling regime (e.g. small effective coupling),
\[
\mu(\mathcal{S}^c)\ll 1
\]
uniformly in volume. This is typically done by:

- high-temperature uniqueness / Dobrushin conditions (small β),
- cluster/polymer expansions for Gibbs measures,
- reflection-positivity + chessboard estimates (for certain events),
- or a gauge-fixed large-deviation argument where the only obstructions are finite-dimensional holonomies.

**This is usually the right tool** if your SAFE region is genuinely local (all links small) and you need a volume-uniform result.

---

## 3. A realistic “return-to-SAFE” theorem you can aim for

### Theorem template (conditional return-to-SAFE)
Assume:

1. (Local convexity) In \(\mathcal{S}\), the Bakry–Émery curvature satisfies
   \(\mathrm{Ric}_V \ge \kappa_* >0\).
2. (Tail control) There exists a gauge-invariant observable \(E(U)\ge 0\)
   (e.g. average plaquette energy) and constants \(c_1,c_2\) independent of volume such that
   \[
   \mu\{E\ge t\}\le e^{-c_1 t + c_2}
   \]
   and moreover \(E\le t_0\Rightarrow U\in\mathcal{S}\) **after a canonical gauge choice** up to a finite-dimensional harmonic sector.
3. (Harmonic sector control) The residual holonomy sector has a spectral gap / LSI constant bounded below independently of volume.

Then you can combine (1) + (2) + (3) to build a global LSI via a two-level decomposition (conditional LSI + Herbst tail bounds).

### What’s missing today
To instantiate this template you need one genuinely new estimate:

- a theorem converting **small plaquette energy** into **small link fields in a fixed gauge**, up to harmonic modes,
  with constants independent of volume.

This is a discrete Uhlenbeck-type gauge lemma (“small curvature ⇒ good gauge”), and it is the correct bottleneck to attack.

---

## 4. Bottom line

- A one-well Lyapunov drift straight back into a tiny “all links small” region is not generally true on compact gauge manifolds because of other stationary sectors.
- The most promising fix is to either:
  - prove a *gauge-fixed* small-curvature ⇒ small-field theorem (then concentration in small curvature implies concentration in SAFE), or
  - switch to a high-temperature Dobrushin/Zegarlinski approach that never requires “return to SAFE.”

