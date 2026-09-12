# Appendix I. The remaining coercive input for Lyapunov drift

This appendix isolates (and slightly reframes) the *one* action-dependent estimate that remains to close the Lyapunov drift mechanism in Part 7.

Sections 7.2–7.3 repaired the classic “constant leakage” problem in Lyapunov computations on compact groups by:

* using a **globally smooth conjugation-invariant plaquette proxy** \(g\mapsto \widetilde z(g)\), so that first/second derivatives are uniformly bounded; and
* choosing an outer profile \(\Phi\) with **\(\Phi'(0)=0\)** (in the main text \(\Phi(s)=s^2\)), which forces all diffusion-generated terms to be weighted by \(\widetilde z_p\) and hence controlled by an extensive “badness” functional.

After those repairs, every term in \( (L_\Lambda W_\Lambda)/W_\Lambda \) is already controlled by the extensive functional \(\mathcal D_\Lambda\) *except* a single mixed term of the form
\[
\mathcal P_\Lambda(U)
\;:=\;
\sum_{p\in P(\Lambda)} \widetilde z_p(U)\,\big\langle \nabla S_\Lambda(U),\,\nabla \widetilde z_p(U)\big\rangle_{g_\Lambda}.
\tag{I.1}
\]
The point of this appendix is to (i) state the coercivity targets precisely, (ii) record algebraic rewrites that reduce \(\mathcal P_\Lambda\) to local combinatorics, and (iii) spell out plausible proof routes and what still seems genuinely hard.

Throughout, \(\Lambda\) is a finite periodic lattice in fixed dimension (\(d=4\) in the main applications), \(M_\Lambda=G^{E(\Lambda)}\) is the configuration manifold with the product bi-invariant metric, and
\[
L_\Lambda f=\Delta_\Lambda f-\langle \nabla S_\Lambda,\nabla f\rangle_{g_\Lambda}
\]
is the reversible generator for the Gibbs measure \(\mu_\Lambda\propto e^{-S_\Lambda}\,d\mathrm{vol}_{g_\Lambda}\).

---

## I.1 Reminder: where the pairing term enters the Lyapunov drift

We keep the smooth trace-defect proxy from §7.2:
\[
\widetilde z(g):=1-\frac1n\Re\,\mathrm{Tr}(\rho(g)),
\qquad
\widetilde z_p(U):=\widetilde z\big(U_p(U)\big),
\qquad 0\le \widetilde z\le 2.
\tag{I.2}
\]
Define the extensive “badness totals”
\[
\mathcal D_\Lambda(U):=\sum_{p\in P(\Lambda)}\widetilde z_p(U),
\qquad
V_\Lambda(U):=\sum_{p\in P(\Lambda)}\widetilde z_p(U)^2,
\qquad
W_\Lambda(U):=e^{\kappa V_\Lambda(U)}.
\tag{I.3}
\]

Corollary 7.36 in the main text yields the uniform upper bound
\[
\frac{L_\Lambda W_\Lambda}{W_\Lambda}(U)
\;\le\;
\big(\kappa C_V+\kappa^2 C_\Gamma\big)\,\mathcal D_\Lambda(U)
\;-
\;2\kappa\,\mathcal P_\Lambda(U),
\tag{I.4}
\]
where \(C_V, C_\Gamma\) are *volume-uniform* constants depending only on \((G,g_G)\), \(\rho\), and the bounded-overlap constant \(\nu\).

Thus, the Lyapunov drift mechanism reduces to proving a **lower bound** on \(\mathcal P_\Lambda\) in terms of \(\mathcal D_\Lambda\) (or in terms of a closely related averaged functional).

---

## I.2 Coercivity targets

The strongest—and cleanest—target is the uniform linear coercivity inequality recorded as Assumption 7.38. We restate it here for convenience.

### I.2.1 Strong (linear) coercivity target

**Assumption I.1 (uniform linear coercivity of the pairing term).** There exist constants
\(c_{\mathrm{pair}}>0\) and \(C_{\mathrm{pair}}\ge 0\), depending only on \((G,g_G)\), \(\rho\), and the action family \(\{S_\Lambda\}\) (but *not* on \(|\Lambda|\)), such that for all \(\Lambda\) and all \(U\in M_\Lambda\),
\[
\mathcal P_\Lambda(U)
\;\ge\;
 c_{\mathrm{pair}}\,\mathcal D_\Lambda(U)
\;-
C_{\mathrm{pair}}.
\tag{I.5}
\]

Under (I.5), the main text shows that one can choose \(\kappa>0\) so that \(W_\Lambda=e^{\kappa V_\Lambda}\) satisfies a Foster–Lyapunov drift inequality of the form
\[
L_\Lambda W_\Lambda\;\le\;-\lambda W_\Lambda + b\,\mathbf 1_{K_\Lambda},
\tag{I.6}
\]
with \(\lambda,b\) uniform in \(|\Lambda|\), which can then be patched with a local Poincaré inequality on \(K_\Lambda\) to obtain a global (volume-uniform) Poincaré inequality.

### I.2.2 Weaker coercivity forms that may still suffice

The linear bound (I.5) may be stronger than what the geometry naturally gives. Two weaker—but still potentially sufficient—variants are worth recording explicitly because they dovetail with the canonical localization set \(K_\Lambda(\varepsilon)\) from Part 8.

Write the **average badness**
\[
\mathcal B_\Lambda(U):=\frac{1}{|P(\Lambda)|}\,\mathcal D_\Lambda(U)
=\frac1{|P(\Lambda)|}\sum_p \widetilde z_p(U),
\qquad 0\le \mathcal B_\Lambda\le 2.
\tag{I.7}
\]

1. **Quadratic-in-average coercivity.** If one can prove
\[
\mathcal P_\Lambda(U)\;\ge\;c_2\,|P(\Lambda)|\,\mathcal B_\Lambda(U)^2\;-
C_2\,|P(\Lambda)|,
\tag{I.8}
\]
then inserting \(\mathcal D_\Lambda=|P|\,\mathcal B_\Lambda\) into (I.4) produces a drift bound that is negative whenever \(\mathcal B_\Lambda\) is larger than an \(O(1)\) threshold. This aligns naturally with using \(K_\Lambda(\varepsilon)=\{\mathcal B_\Lambda\le\varepsilon\}\) as the “core” set.

2. **One-sided coercivity off the core set.** It is often enough to show a bound only on the complement of a canonical set:
\[
\mathcal P_\Lambda(U)\;\ge\;c_\varepsilon\,\mathcal D_\Lambda(U)
\qquad\text{for all }U\notin K_\Lambda(\varepsilon),
\tag{I.9}
\]
with \(c_\varepsilon>0\) independent of \(|\Lambda|\). This is weaker than (I.5), but still yields negative drift outside \(K_\Lambda(\varepsilon)\) and is often the “right” form for compact-state-space models.

In what follows we focus on the Wilson action (where the algebraic structure is explicit) and explain what kinds of intermediate lemmas would imply one of these coercivity forms.

---

## I.3 Algebraic rewrites and locality of the pairing functional

### I.3.1 A universal identity: \(\mathcal P_\Lambda\) is the \(\langle\nabla S,\nabla V\rangle\) pairing

With \(V_\Lambda=\sum_p \widetilde z_p^2\), we have
\[
\nabla V_\Lambda
=\sum_p \nabla(\widetilde z_p^2)
=\sum_p 2\widetilde z_p\,\nabla\widetilde z_p.
\tag{I.10}
\]
Hence the mixed term is exactly
\[
\mathcal P_\Lambda(U)=\frac12\,\big\langle \nabla S_\Lambda(U),\,\nabla V_\Lambda(U)\big\rangle_{g_\Lambda}.
\tag{I.11}
\]
This formulation makes clear that the missing input is a genuine **coercivity/monotonicity** statement: we need the action gradient to have a uniformly positive alignment with the “radial” direction determined by the badness functional \(V_\Lambda\).

### I.3.2 Specialization to Wilson: \(\mathcal P_\Lambda\) as a local double sum of carré-du-champ terms

For the Wilson action
\[
S_W(U)=\beta\sum_{q\in P(\Lambda)}\widetilde z_q(U),
\tag{I.12}
\]
we have
\[
\nabla S_W=\beta\sum_q \nabla \widetilde z_q.
\tag{I.13}
\]
Plugging this into (I.1) gives
\[
\mathcal P_\Lambda(U)
=\beta\sum_{p,q\in P(\Lambda)} \widetilde z_p(U)
\,\Gamma_\Lambda\big(\widetilde z_p,\widetilde z_q\big)(U),
\qquad
\Gamma_\Lambda(f,g):=\langle\nabla f,\nabla g\rangle_{g_\Lambda}.
\tag{I.14}
\]

The key structural simplification is **locality**:

* each \(\widetilde z_p\) depends on exactly four link variables (the boundary of \(p\));
* therefore \(\Gamma_\Lambda(\widetilde z_p,\widetilde z_q)\equiv 0\) whenever \(p\) and \(q\) do not share a link.

Equivalently, (I.14) can be rewritten as a sum over links. Let \(\partial p\subset E(\Lambda)\) be the four boundary links of \(p\). Decomposing gradients into link gradients (as in §3.5/§7.2) gives
\[
\Gamma_\Lambda(\widetilde z_p,\widetilde z_q)
=\sum_{\ell\in E(\Lambda)}\langle \nabla_\ell \widetilde z_p,\,\nabla_\ell \widetilde z_q\rangle_{\mathfrak g},
\tag{I.15}
\]
and \(\nabla_\ell \widetilde z_p\equiv 0\) unless \(\ell\in\partial p\). Thus
\[
\mathcal P_\Lambda(U)
=\beta\sum_{\ell\in E(\Lambda)}\;
\sum_{p:\,\ell\in\partial p}\;\sum_{q:\,\ell\in\partial q}
\widetilde z_p(U)\,\langle \nabla_\ell \widetilde z_p(U),\,\nabla_\ell \widetilde z_q(U)\rangle.
\tag{I.16}
\]
All three sums in (I.16) are uniformly finite-range: in fixed dimension the number of plaquettes meeting a given link is bounded by the overlap constant \(\nu\).

This “linkwise local” form is the right starting point for any attempt to control \(\mathcal P_\Lambda\) from below.

---

## I.4 What is easy, and what is hard

### I.4.1 Easy: global upper bounds (not what we need)

From §7.2 we have global *upper* controls such as
\(\Gamma_\Lambda(\widetilde z_p)\lesssim \widetilde z_p\) and \(|\nabla \widetilde z_p|\lesssim 1\). These yield bounds like
\(\mathcal P_\Lambda\lesssim \beta\,\mathcal D_\Lambda^2\) or \(\mathcal P_\Lambda\lesssim \beta\,|P|\mathcal D_\Lambda\),
which are fine for moment estimates but useless for the drift negativity (we need a **lower** bound).

### I.4.2 Easy: local two-sided comparability \(|\nabla \widetilde z|^2 \asymp \widetilde z\) near the vacuum

The ratio
\(
Q(g)=|\nabla_G\widetilde z(g)|^2/\widetilde z(g)
\)
extends continuously to \(g=\mathbf 1\) with a strictly positive limit (computed in §7.2). Therefore:

**Lemma I.2 (local lower gradient bound near \(\mathbf 1\)).** There exist \(r_{\nabla}>0\) and \(c_{\nabla}>0\), depending only on \((G,g_G)\) and \(\rho\), such that
\[
|\nabla_G\widetilde z(g)|^2\ \ge\ c_{\nabla}\,\widetilde z(g)
\qquad\forall g\in B_{r_{\nabla}}^G(\mathbf 1).
\tag{I.17}
\]
Consequently, on any event where all plaquette holonomies lie in \(B_{r_{\nabla}}^G(\mathbf 1)\), one has
\[
\Gamma_\Lambda(\widetilde z_p)(U)=|\nabla\widetilde z_p(U)|^2\ \ge\ c_{\nabla}\,\widetilde z_p(U)
\qquad\text{for each }p.
\tag{I.18}
\]

This is the kind of “microlocal coercivity” one would like to feed into the pairing term; the obstruction is that \(\mathcal P_\Lambda\) involves **cross terms** \(\Gamma(\widetilde z_p,\widetilde z_q)\) for \(p\neq q\), whose sign is not controlled a priori.

### I.4.3 Hard: controlling the sign of cross terms

From (I.14), the self-terms \(p=q\) contribute
\[
\beta\sum_p \widetilde z_p\,\Gamma_\Lambda(\widetilde z_p)\ \ge\ 0.
\tag{I.19}
\]
The difficulty is the contribution of pairs \(p\neq q\) that share a link:
\[
\beta\sum_{p\neq q} \widetilde z_p\,\Gamma_\Lambda(\widetilde z_p,\widetilde z_q).
\tag{I.20}
\]
These terms can be negative (they are inner products of different gradients), and a uniform lower bound on the *total* sum requires a nontrivial geometric statement: one must rule out configurations in which many neighboring plaquette gradients are systematically anti-aligned in a way that scales with volume.

This is exactly the “term II dominates term I” obstruction flagged in the outline.

---

## I.5 A plausible proof route on a small-field regime

Although the ultimate Lyapunov input should control drift *globally*, it is instructive to see what one can hope to prove on a uniform small-field set where the action is known to be strongly convex in the horizontal directions (Part 5).

### I.5.1 Linearization viewpoint

In exponential coordinates \(U=\mathrm{Exp}_\Lambda(A)\) with \(A\in \mathcal C^1(\Lambda;\mathfrak g)\) small, one has the schematic expansions
\[
U_p(U)=\exp\big((d_1A)_p+O(|A|^2)\big),
\qquad
\widetilde z_p(U)=\frac{1}{2n\lambda_\rho}\,|(d_1A)_p|^2+O(|A|^3).
\tag{I.21}
\]
Moreover, for the Wilson action,
\[
\nabla^2 S_W(U^{(0)})=\frac{\beta}{n\lambda_\rho}\,d_1^*d_1,
\tag{I.22}
\]
and the matrix hinge of Part 5 yields \(\nabla^2S_W(U)\) as a controlled perturbation of \(d_1^*d_1\) on \(K_\Lambda(r)\).

In this linearized regime, a morally correct heuristic is:

* \(S_W(A)\) behaves like a quadratic form \(\langle A,\,d_1^*d_1A\rangle\),
* \(V_\Lambda(A)=\sum_p \widetilde z_p(A)^2\) behaves like \(\sum_p |(d_1A)_p|^4\), and
* \(\mathcal P_\Lambda=(1/2)\langle\nabla S_W,\nabla V_\Lambda\rangle\) behaves like a **quartic coercivity** term.

Turning that heuristic into an inequality like (I.8) would require two ingredients:

1. a *uniform* estimate relating \(\nabla_A\widetilde z_p\) to \(d_1^*\) acting on plaquette variables (a discrete “chain rule” in cochain language), and
2. a discrete inequality converting the resulting expression into a coercive functional of \(\{\widetilde z_p\}\), with constants independent of \(|\Lambda|\).

This is exactly where the Hodge decomposition and bounded-overlap constants are expected to enter.

### I.5.2 What this would buy

If one could prove, on a canonical set where plaquette holonomies stay in a fixed neighborhood of \(\mathbf 1\), a bound of the schematic form
\[
\mathcal P_\Lambda(U)\ \gtrsim\ \beta\sum_p \widetilde z_p(U)^2,
\tag{I.23}
\]
then Jensen gives
\(
\sum_p \widetilde z_p^2\ge |P|\,\mathcal B_\Lambda^2
\), so (I.23) implies the quadratic-in-average coercivity (I.8) (up to harmless constants). This would drive drift negativity whenever the averaged badness \(\mathcal B_\Lambda\) exceeds a fixed threshold—precisely the kind of drift compatible with the canonical localization set in Part 8.

---

## I.6 Alternative escape hatches if strong coercivity fails

If a uniform pointwise coercivity inequality (I.5) cannot be proved for the Wilson action as stated, there are at least two conceptually clean ways to keep the overall mass-gap program alive.

1. **Redesign the drift set to match averaged coercivity.** If one can only show (I.8) or (I.9), then one should take the Lyapunov “core” set to be \(K_\Lambda(\varepsilon)=\{\mathcal B_\Lambda\le\varepsilon\}\), not a fixed sublevel set of \(\mathcal D_\Lambda\). This matches the localization architecture already used in Part 8 and avoids union-bound volume leakage.

2. **Replace measure-small localization by capacity/Lyapunov localization.** If typicality estimates for \(K_\Lambda(\varepsilon)\) are obtained via a drift/capacity argument rather than via global LSI, the required coercivity can sometimes be weakened: one needs control of exit probabilities from \(K_\Lambda(\varepsilon)\) rather than a pointwise drift inequality everywhere.

These alternatives change the “plumbing” in Parts 7–8 but do not affect the core HS + massive-Maxwell mechanism (Parts 6 and 9).

---

## I.7 Open input (referee-facing statement)

To keep the dependency ledger honest, we end with a single explicit open lemma.

**Open Lemma I.3 (coercive pairing inequality).** Prove one of the following, with constants independent of \(|\Lambda|\), for the chosen action family \(\{S_\Lambda\}\) (in particular for the Wilson action):

* the linear coercivity bound (I.5); or
* a weaker averaged/coercive alternative such as (I.8) or (I.9) that still implies a Foster–Lyapunov drift inequality with volume-uniform consequences.

Once such an inequality is available, the rest of the chain from Part 7 onward is “bookkeeping”: Theorem 7.46 upgrades local functional inequalities to global Poincaré (and, conditionally, LSI/SPI), Part 8 upgrades good-set covariance bounds to full covariances, and Parts 9–11 convert Euclidean time decay into an OS Hamiltonian mass gap.
