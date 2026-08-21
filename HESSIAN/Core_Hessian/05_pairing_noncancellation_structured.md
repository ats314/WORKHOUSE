# The pairing/noncancellation bottleneck — and a structured route beyond the “false SU(2) claim”

This note extracts the project’s sharp identification of the remaining hard local input:
a **uniform coercivity lower bound** for a pairing functional that contains
potentially negative cross terms.

It also explains why the naive “adjoint-rotated vectors can’t cancel unless aligned” claim is false,
and what *additional lattice architecture* could plausibly make a true noncancellation statement.

---

## 1. The Lyapunov drift architecture (what is already closed)

The project builds a Lyapunov function of the form
\[
V_\Lambda(U) := \sum_{p\in P(\Lambda)} \Phi(\widetilde z_p(U)),
\quad\text{with the concrete choice }\Phi(s)=s^2,
\]
and uses \(W_\Lambda=e^{\kappa V_\Lambda}\) in drift arguments.

A key achievement is that all *positive* chain-rule terms are controlled uniformly by
\[
\mathcal D_\Lambda(U):=\sum_{p\in P(\Lambda)} \widetilde z_p(U),
\]
with constants independent of \(|\Lambda|\).
For example (schematically):
- the Laplacian/Hessian term in \(L_\Lambda V_\Lambda\),
- the sum of \(\Gamma(\widetilde z_p)\),
- and the “exponential carré du champ” \(\Gamma(V_\Lambda)\),
are each bounded by \(A_i\,\mathcal D_\Lambda\) with explicit \(A_i\) depending only on overlap and group constants.

This closure relies on locality + isometries for plaquette lifts and bounded overlap.

---

## 2. The remaining hard term: the pairing functional \(\mathcal P_\Lambda\)

The obstruction is the drift contribution involving the action gradient:
\[
\mathcal P_\Lambda(U) := \sum_{p\in P(\Lambda)} \widetilde z_p(U)\,
\big\langle \nabla S_W(U),\ \nabla \widetilde z_p(U)\big\rangle.
\]

Using \(\nabla S_W = \beta\sum_q \nabla \widetilde z_q\), one expands
\[
\mathcal P_\Lambda
= \beta\sum_{p,q}\widetilde z_p\,\Gamma(\widetilde z_p,\widetilde z_q).
\]

- The **self-terms** \(p=q\) are nonnegative:
  \[
  \beta\sum_p \widetilde z_p\,\Gamma(\widetilde z_p)\ge 0.
  \]
- The **cross terms** \(p\neq q\) can have either sign:
  \[
  \beta\sum_{p\neq q}\widetilde z_p\,\Gamma(\widetilde z_p,\widetilde z_q),
  \]
  and negative contributions must be ruled out *uniformly in volume*.

The project states this crisply: one must exclude configurations in which neighboring plaquette gradients
are systematically anti-aligned in a way that scales with \(|\Lambda|\).

---

## 3. Why the naive “SU(2) noncancellation” statement is false

Identifying \(\mathfrak{su}(2)\cong\mathbb R^3\),
it is easy to find non-collinear vectors \(Y_1,Y_2,Y_3\) (all with \(\|Y_i\|=1\)) such that
\[
Y_1+Y_2+Y_3 = 0
\]
(equilateral triangle).
So any claim of the form “a sum of rotated vectors vanishes only if they are all collinear”
is simply incorrect without additional constraints.

The *only* way to salvage a true “noncancellation” lemma is to use extra structure:
the vectors in \(\mathcal P_\Lambda\) are not arbitrary—they are gradients of specific plaquette-lifted class functions,
transported through a constrained lattice architecture.

---

## 4. What additional structure is actually available

### 4.1 Locality + isometric transport
For a plaquette lift \(\widetilde z_p(U)=\widetilde z(U_p(U))\),
the dependence on a single link \(\ell\in\partial p\) has the form
\[
U_\ell \mapsto \widetilde z(A\,U_\ell^\sigma\,B),
\qquad \sigma\in\{\pm1\},
\]
where \(A,B\) depend on the other three links.
Since left/right multiplication and inversion are isometries, the gradient norm is preserved.

So each link-gradient contribution is an **adjoint transport** of a single-group gradient:
\[
\nabla_\ell \widetilde z_p(U)
=
\mathrm{Ad}_{g_{p,\ell}(U)}\big(\nabla_G \widetilde z(U_p)\big)
\quad\text{(schematically)}.
\]

But importantly: the transports \(g_{p,\ell}(U)\) are not independent random rotations;
they are built from *shared link variables* (“staples”).

### 4.2 Small-field regime linearization (the key “architecture”)
On the canonical small-field region \(K_\Lambda(r)\), one can write links in exponential coordinates
\[
U_\ell = \exp(A_\ell),
\quad A\in \mathcal C^1(\Lambda;\mathfrak g),\quad \|A\|\ll 1,
\]
and then the plaquette holonomy satisfies
\[
U_p \approx \exp\big((d_1 A)_p\big).
\]

In this regime, gradients of \(\widetilde z_p\) are approximately linear in the “field strength”
\(F:=d_1 A\), and linkwise forces are approximately a discrete divergence of \(F\):
\[
\nabla_\ell S_W(U)\ \approx\ \alpha\,(d_1^\* F)_\ell
\quad\text{with }\alpha=\frac{\beta}{n\lambda_\rho}.
\]

This is the first serious piece of extra structure:
cross terms in the star sum are *not arbitrary* inner products; they organize into
discrete differential operators with algebraic identities (e.g. \(d_1 d_0=0\)) and Hodge decompositions.

---

## 5. A structured “noncancellation” statement that is actually true in the linear regime

Here is a star-level coercivity statement that **is true** (and useful),
because it uses the lattice differential complex.

### Lemma (linear Maxwell coercivity on horizontals, finite volume)
Let \(A\in\mathcal C^1(\Lambda;\mathfrak g)\) be horizontal: \(d_0^\*A=0\).
Set \(F=d_1 A\in\mathcal C^2(\Lambda;\mathfrak g)\).
Then
\[
\|d_1^\* F\|_{\mathcal C^1}^2
=
\langle F,\ d_1 d_1^\* F\rangle_{\mathcal C^2}
\ \ge\ 
\lambda_{\min}\,\|F_\perp\|_{\mathcal C^2}^2,
\]
where \(F_\perp\) denotes the component orthogonal to the kernel of \(d_1 d_1^\*\)
(coexact/harmonic splitting), and \(\lambda_{\min}\) is the spectral gap of \(d_1 d_1^\*\) on that sector.

**Interpretation.**
In the linearized theory, the linkwise force \(\approx d_1^\*F\) cannot vanish unless the curvature \(F\) lies in the null sector.
So “cancellation” is controlled by discrete Hodge theory, not by a fake R\(^3\) argument.

### Consequence (one-link lower bound from a global average)
If \(\|F\|_{\mathcal C^2}^2\) is bounded below, then
\[
\max_{\ell\in E(\Lambda)} \|\nabla_\ell S_W\|
\ \gtrsim\
\alpha\,\frac{\|F\|_{\mathcal C^2}}{\sqrt{|E(\Lambda)|}},
\]
and since \(|E|\asymp |P|\) in fixed dimension, this yields a **volume-uniform link force** lower bound from a uniform plaquette-energy density.

This is a genuine (and structurally correct) “noncancellation” mechanism.

---

## 6. What remains to lift this to the nonlinear Wilson setting

To turn the linear lemma into the project’s needed uniform lower bound for \(\mathcal P_\Lambda\),
one needs three upgrades:

1. **Nonlinear-to-linear control** on \(K_\Lambda(r)\): show
   \(\nabla_\ell S_W(U)\) is a small perturbation of \(\alpha(d_1^\* d_1 A)_\ell\) in right-trivialized coordinates.

2. **Weighted cross terms**: \(\mathcal P_\Lambda\) is *weighted* by \(\widetilde z_p\),
   so one needs a weighted Hodge-type inequality or a monotonicity lemma ensuring that weights cannot concentrate in a cancellation-friendly pattern.

3. **Uniformity in volume/topology**: treat harmonic modes (torus effects) carefully, likely by pinning boundary conditions, adding a tiny mass, or projecting them away as is done in the hinge pipeline.

---

## 7. A practical research plan (concrete next steps)

1. Write an exact right-trivialized formula for \(\nabla_\ell \widetilde z_p(U)\) in terms of \(U_p\) and staple transports.

2. Prove a **Jacobian stability estimate**: on \(K_\Lambda(r)\),
   the linear map from small \(A\) to forces \(\nabla S_W\) has condition number bounded independently of \(|\Lambda|\).

3. Use the already-proved **matrix hinge** (strong convexity on horizontals) to control the nonlinear remainder terms.

4. Derive a uniform lower bound of the type
   \[
   \mathcal P_\Lambda(U)\ \ge\ c\,\beta\,\mathcal D_\Lambda(U) - C,
   \]
   which is the missing coercivity input for the global Lyapunov drift step.

This is the right level of “star-level noncancellation” for the problem:
it uses the lattice differential complex and the Wilson architecture, rather than impossible claims about arbitrary rotations in \(\mathbb R^3\).

