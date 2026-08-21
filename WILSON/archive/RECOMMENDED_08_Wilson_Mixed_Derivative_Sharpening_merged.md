# Sharpening the Wilson Mixed Derivative Bound

This note is about one very specific bottleneck in the “Flow” step:

> In the block convexity inequality, the mixed Hessian block \(B\) enters as \(\|B\|_{\mathrm{op}}^2/\gamma\).  
> A conservative uniform bound \(\|B\|_{\mathrm{op}}\lesssim \beta\,\frac{24}{N}\) is safe, but it makes the RG-stable window painfully small.

So: any *rigorous* reduction of that constant — even only **on a high-probability set** — materially improves the whole program.

---

## 1. Why there are two different Wilson constants

For the Wilson action
\[
S_W(U)=\sum_p\Big(1-\frac1N\Re\mathrm{Tr}(U_p)\Big),
\]
there are (at least) two natural norm bounds:

### Quadratic form bound
A standard counting argument gives a bound of the type
\[
\big|\langle A,\mathrm{Hess}\,S_W(U)\,A\rangle\big|\ \le\ \frac{6}{N}\,\|A\|^2
\quad(d=4),
\]
for tangent vectors \(A\) (including horizontals).

This is a **bound on a quadratic form** along the same vector \(A\).

### Operator norm bound
In the block RG inequality you need control of *mixed derivatives* in the form
\[
\|B\|_{\mathrm{op}}\ \le\ M,
\]
where \(B\) is the off-diagonal block in the Hessian after a coarse/fine split.

Bounding \(\|B\|_{\mathrm{op}}\) by “absolute value + counting” typically introduces an extra factor \(\approx 4\) coming from the 4-link plaquette structure, yielding a safe estimate
\[
\|\mathrm{Hess}\,S_W(U)\|_{\mathrm{op}}\ \le\ C_V(N),\qquad C_V(N)\le \frac{24}{N}.
\]

**Moral:** \(6/N\) controls same-direction curvature; \(24/N\) controls worst mixed couplings.

The “Flow” step pays for the latter.

---

## 2. Where exactly the bound enters the block convexity engine

In the block convexity inequality (Schur complement + Brascamp–Lieb),
\[
\nabla_x^2 S_{\mathrm{eff}}(x)
\succeq
\alpha I - \frac{M^2}{\gamma}\,I,
\]
the dangerous term is \(M^2/\gamma\).

In gauge theory, \(\gamma\) is the convexity available in the eliminated (“fine”) directions, and \(M\) is the size of coarse–fine cross couplings.  
So improving \(M\) is mathematically equivalent to “making the RG step less lossy”.

---

## 3. Three realistic sharpening routes in increasing ambition

### Route 1: bound the **actual mixed block** \(B\), not the full Hessian
A common blunt move is:
\[
\|B\|_{\mathrm{op}} \le \|\mathrm{Hess}\,S_W\|_{\mathrm{op}} \le \frac{24}{N}.
\]
But \(B\) is typically much sparser than the full Hessian, because only plaquettes that **touch both the coarse and fine sectors** contribute.

So the first “pressure test” is purely combinatorial + local:

- pick the coarse/fine decomposition you actually use (checkerboard, block interior vs boundary, etc.),
- count only the plaquettes straddling the split,
- compute (or tightly bound) the operator norm of the resulting bipartite coupling graph.

For a good coarse choice, \(B\) should scale like a **surface term**, not a bulk term.

Deliverable:
\[
\|B\|_{\mathrm{op}}\ \le\ \frac{c_B}{N},
\qquad c_B < 24,
\]
with an explicit \(c_B\) depending only on the blocking geometry.

---

### Route 2: choose coarse variables so that the **quadratic part diagonalizes**
Near the identity, the Wilson action has a quadratic expansion:
\[
S_W(U)\approx \frac{\beta}{2}\,\langle A,\,(\mathrm{curl}^\ast\mathrm{curl})\,A\rangle + \text{(higher order)}.
\]
If you define “coarse” and “fine” directions by **Fourier mode split** (low vs high momenta) or by an orthogonal block-spin transform, then:

- the quadratic part becomes block-diagonal (or close),
- and the mixed block \(B\) is generated mostly by **nonlinear remainders**.

That suggests a template:

1. Write \(S_W = Q + R\) (quadratic \(Q\) + remainder \(R\)).
2. Choose coordinates \((x,y)\) so that \(\nabla^2 Q\) has \(B_Q=0\).
3. Bound \(\|B\|_{\mathrm{op}} = \|B_R\|_{\mathrm{op}}\) by controlling \(R\) on a typical set.

This is the cleanest path to a *scale-improving* bound: it makes \(M\) proportional to the size of nonlinearity, not the raw Wilson scale.

---

### Route 3: sharpen **on a high-probability core** “typical set” estimate
The global obstruction argument already says you should localize. This is the same philosophy applied to \(M\).

Define a “good” set \(K(\delta)\) where plaquettes are close to the identity, e.g.
\[
K(\delta):=\left\{U:\ \max_{p}\Big(1-\frac1N\Re\mathrm{Tr}(U_p)\Big)\le \delta\right\}.
\]

On such a set you can try to prove a perturbative bound
\[
\|B(U)\|_{\mathrm{op}} \ \le\ \frac{c_0}{N} + \frac{c_1}{N}\,\delta,
\quad U\in K(\delta),
\]
or (better) a purely small bound \(\|B(U)\|_{\mathrm{op}}\le (c/N)\delta\) if your coarse/fine split kills the quadratic part.

Then the program only needs:
- a local Poincaré/LSI on \(K(\delta)\), and
- a capacity/exit-time estimate for \(K(\delta)^c\).

This is exactly the “localization makes obstruction actionable” theme, now used to improve \(M\).

---

## 4. A theorem shaped target bound

A very usable sharpening target is:

> **Target bound.** There exists a decomposition \((x,y)\) (a legitimate coarse-graining) and constants \(c,c'>0\) such that on a core \(K(\delta)\) one has  
> \[
> \|B(U)\|_{\mathrm{op}} \le \frac{c}{N}\,\delta,
> \qquad
> C(U):=\nabla_y^2 S(U)\succeq c' I
> \quad\text{for }U\in K(\delta),
> \]
> and \(\mu(K(\delta))\) is high.

Then the Schur complement loss term is
\[
\frac{M^2}{\gamma}\ \lesssim\ \frac{(c\delta/N)^2}{c'}
\]
which becomes small fast once \(\delta\) is small.

This is the rigorous way to say “the RG step is almost lossless on typical configurations”.

---

## 5. How to prove a typical set bound

A workable path (not guaranteed, but plausible):

1. **Local Taylor control.** Show that if \(U_p\) is \(\delta\)-close to \(I\), then the plaquette contribution \(S_p\) has Hessian close (in operator norm) to its Hessian at identity:
   \[
   \|\nabla^2 S_p(U_p)-\nabla^2 S_p(I)\|_{\mathrm{op}} \le C\,\delta.
   \]
   This is a finite-dimensional Lie-group estimate.

2. **Block-diagonalize the quadratic form.** Choose coarse variables \(x\) so that the quadratic Wilson Hessian has no coarse–fine mixing.

3. **Sum with locality.** Use the fact that the Wilson action is a sum over plaquettes (local interactions) so that global \(\|B\|\) inherits the same perturbative smallness.

4. **Make it probabilistic.** Prove that the Gibbs measure \(\mu\) puts high probability on \(K(\delta)\) at the scale where you apply the bound. This is a large-deviation / concentration estimate for plaquettes.

Even partial success is valuable: a bound that holds with probability \(1-e^{-cL^d}\) is “as good as deterministic” once you have the localization theorem template.

---

## 6. What to do right now

- **D1. Compute the exact operator norm of the quadratic Wilson Hessian** under your chosen RG linear transform.  
  If that norm is already \(<24/N\), you immediately sharpen \(M\).

- **D2. Extract a Lie-group inequality of the form**
  \[
  \|\nabla^2 S_p(U)-\nabla^2 S_p(I)\|_{\mathrm{op}}\le C\,\|I-U\|
  \]
  for a one-plaquette term.

- **D3. Combine D1 + D2 into a “typical-set” mixed-block bound**, valid on \(K(\delta)\).

These are theorem-sized bites, not philosophy.

---

## 7. Why this matters beyond constants

This isn’t just about making a window less ugly.

A typical-set sharpening of \(\|B\|_{\mathrm{op}}\) is the mathematical bridge between:

- “the global curvature infimum is wrecked by rare garbage,” and
- “the RG step is controlled on the region that actually matters.”

If you can make that bridge, the block convexity engine becomes something you can plausibly iterate.