# The remaining coercive input: pairing term \(P_\Lambda\) in the Lyapunov drift

> **This is the bottleneck.**  
> After the “smooth proxy” fix, the project reduces the uniform drift condition
> to a single coercivity statement about a pairing term.
> Proving (or correctly weakening) this lemma looks like the highest-leverage next move.

---

## 1. What the drift computation reduces to

Let \(\Lambda\) be a finite lattice region.
Let \(S_W\) be the Wilson action and \(V_\Lambda\) the Lyapunov functional built from the smooth plaquette proxy.

For the generator
\[
\mathcal L = \Delta - \langle \nabla S_W,\nabla(\cdot)\rangle,
\]
one has
\[
\mathcal L V_\Lambda \;=\; \Delta V_\Lambda \;-\; P_\Lambda(U),
\]
where the **pairing term** is
\[
P_\Lambda(U)
:= \sum_{\ell\in\Lambda_1} \big\langle \nabla_\ell S_W(U),\;\nabla_\ell V_\Lambda(U)\big\rangle.
\]

The project isolates the “needed inequality” as:

> **Target coercivity (schematic).** Find constants \(A,B>0\) s.t.
> \[
> P_\Lambda(U)\;\ge\; A\,V_\Lambda(U)\;-\;B|\Lambda|
> \]
> (globally or at least on a good set).

If this holds, then together with an upper bound on \(\Delta V_\Lambda\), you get
\[
\mathcal L V_\Lambda \;\le\; -a\,V_\Lambda + b|\Lambda|,
\]
and hence the uniform functional inequalities.

---

## 2. Why this inequality is hard

On \(\mathbb R^n\) with a convex potential, \(\langle \nabla S,\nabla V\rangle\) is controlled by convexity
and alignment arguments.

Here, the configuration space is compact and curved:
- gradients live in different tangent spaces (one per link),
- “plaquette defects” are not globally convex due to cut-locus / topology,
- cancellations are gauge- and geometry-sensitive.

So you need either:
- a **local** coercivity argument (small-field regime) plus a probabilistic tail control, or
- a structural identity that shows alignment holds on average.

---

## 3. Three plausible proof routes

### Route A: small-field coercivity + tail truncation

1. Restrict to a small tubular neighborhood of the vacuum:
   \(U_\ell = \exp(X_\ell)\) with \(\|X_\ell\|\ll 1\).
2. Expand \(S_W\) and \(V_\Lambda\) to leading order:
   \(S_W\) becomes a quadratic form \(\sim \sum_p \|d_1 X\|^2\),
   and \(V_\Lambda\) becomes a quadratic-in-\(\tau\) proxy \(\sim \sum_p \tau(U_p)^2\).
3. Prove coercivity in this regime by matrix inequalities on the discrete differential complex
   (this is where the Hodge stiffness lemma becomes relevant).
4. Use the Lyapunov itself to control the complement (“bad set”) by Markov / exponential tails, paying \(B|\Lambda|\).

**Risk.** Topological sectors / large holonomies can defeat global convexity; you must make sure the truncation
set is the one that appears naturally in the drift argument (not an artificial one).

---

### Route B: per-link local inequality (“force aligns with defect gradient”)

Try to show that each link \(\ell\) satisfies a local bound
\[
\big\langle \nabla_\ell S_W,\;\nabla_\ell V_\Lambda\big\rangle
\;\ge\; a \sum_{p\ni \ell}\Phi(\tau(U_p))\;-\;b,
\]
by analyzing the \(\ell\)-dependence of the plaquettes incident to \(\ell\).

Then summing over \(\ell\) gives the global inequality with \(A=a\) and \(B=b\,|\Lambda_1|\).

**Idea.** On compact groups, gradients of class functions have strong monotonicity properties along geodesics;
if you can make that quantitative for the chosen proxy \(\Phi\), you get coercivity “for free.”

---

### Route C: prove a weaker *ratio* certificate

The simulation pipeline suggests a ratio-based approach:
control
\[
\frac{P_\Lambda(U)}{V_\Lambda(U)} \quad\text{and}\quad \frac{\mathcal L V_\Lambda(U)}{V_\Lambda(U)}
\]
on the subset where \(V_\Lambda\) is not tiny.
This removes intercept “fudge factors” and focuses on genuine coercivity.

A theorem of the form
\[
P_\Lambda(U) \ge c(\tau_0)\,V_\Lambda(U)\quad \text{whenever } V_\Lambda(U)\ge \tau_0|\Lambda|
\]
may be enough for the drift method, depending on how the good-set decomposition is organized.

---

## 4. What to do next (highest value work)

1. **Write the quadratic small-field model explicitly** (Lie algebra approximation) and prove the inequality there.
   If it fails, you learn *exactly* what structure is missing.

2. **Check whether gauge-fixing helps.**
   Since \(S_W\) is gauge-invariant but the generator can be formulated with a gauge-fixed metric,
   you might get better alignment estimates for \(\nabla_\ell S_W\) and \(\nabla_\ell V_\Lambda\).

3. **Turn the numerics into a lemma blueprint.**
   The drift decomposition identity can often be promoted to a deterministic algebraic identity.
   If the sign alignment is exact (not statistical), that should have a clean proof.

---
