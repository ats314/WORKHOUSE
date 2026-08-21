# Admissibility as Structural Inequality Calculus
*(Definitions and Rulebook Entry #1 — External-Field Linearization as Certificate Transport)*

## 0. Scope
This note defines three interfaces:

- **Mod**: a minimal category of *backgrounded models* that expose a linearization/Hessian/principal-symbol map.
- **Cert**: a poset-category of *structural certificates* (inequalities / positivity / gap).
- **A**: the *admissibility functor* sending a model to its best available certificate package.

Then we state **Rulebook Entry #1**: external-field linearization (VSU/EFE) and the OS “good set hinge” are the same certificate-transport mechanism: *Hessian domination by a reference background*.

---

## 1. Minimal category of models: \mathbf{Mod}

### Definition 1.1 (Object of Mod)
An object is a triple
\[
M = (\mathcal X,\, b,\, \mathscr L_b)
\]
where

1. \(\mathcal X\) is a configuration/state space (manifold, function space, lattice configuration space, …),
2. \(b\in\mathcal X\) is a chosen **background** (vacuum, strong external-field background, “good set” configuration, …),
3. \(\mathscr L_b\) is the **linearized structure operator** at \(b\), acting on perturbations \(v\in T_b\mathcal X\).
   - In variational settings, \(\mathscr L_b\) is a second variation/Hessian.
   - In PDE settings, \(\mathscr L_b\) may be represented by its principal symbol/principal part.

### Definition 1.2 (Morphism in Mod)
A morphism \(f:M\to M'\) is a map \(f:\mathcal X\to\mathcal X'\) with \(f(b)=b'\) such that the induced tangent map \(Df_b:T_b\mathcal X\to T_{b'}\mathcal X'\) satisfies a **comparison inequality**
\[
\langle v,\mathscr L_b v\rangle
\ \ge\
\langle Df_b v, \mathscr L_{b'}\, Df_b v\rangle\ -\ \varepsilon\,\|v\|^2,
\]
for some control parameter \(\varepsilon\ge0\).  
Interpretation: \(f\) transports the linearized structure, possibly losing at most \(\varepsilon\) of coercivity/gap.

---

## 2. Certificates: \mathbf{Cert}

### Definition 2.1 (Certificate package)
A certificate is a finite record
\[
C=(C_{\mathrm{cvx}},\,C_{\mathrm{coer}},\,C_{\mathrm{hyp}},\,C_{\mathrm{RP}},\,C_{\mathrm{gap}},\,C_{\mathrm{perm}},\dots),
\]
where each component is a structural statement, typically an inequality.

Examples of components:
- \(C_{\mathrm{cvx}}\): strict convexity / positive-definite Hessian.
- \(C_{\mathrm{coer}}\): coercivity: \(\mathscr L_b\succeq \lambda I\).
- \(C_{\mathrm{hyp}}\): hyperbolicity: principal symbol defines a Lorentzian cone.
- \(C_{\mathrm{RP}}\): reflection positivity.
- \(C_{\mathrm{gap}}\): spectral gap as a form/operator inequality.
- \(C_{\mathrm{perm}}\): permanence of the above under limits / coarse-graining.

### Definition 2.2 (Category structure)
\(\mathbf{Cert}\) is taken as a **poset-category**:  
\(C\to C'\) iff \(C\) **implies** \(C'\) (i.e. \(C\) is at least as strong as \(C'\), often meaning larger constants \(\lambda,\Delta\), fewer hypotheses, etc.).

---

## 3. The admissibility functor \mathbf{A}

### Definition 3.1 (Admissibility functor)
Define a functor
\[
\mathbf A:\mathbf{Mod}\to\mathbf{Cert}
\]
by sending each model-object \(M=(\mathcal X,b,\mathscr L_b)\) to the **best available** certificate package \(\mathbf A(M)\) that can be proved from the model’s structure at \(b\).

On morphisms \(f:M\to M'\), \(\mathbf A\) sends \(f\) to the induced implication
\[
\mathbf A(M')\ \Longrightarrow\ \mathbf A(M)\ \ \text{(with constants degraded by }\varepsilon\text{ if needed).}
\]

---

## 4. Rulebook Entry #1: External-field linearization as certificate transport

### Theorem 4.1 (Hessian domination \(\Rightarrow\) certificate transport)
Suppose \(M=(\mathcal X,b,\mathscr L_b)\) admits a deterministic reference operator \(\mathscr L_\star\) and a bound
\[
\mathscr L_b \ \succeq\ \mathscr L_\star\ -\ \varepsilon I.
\]
If \(\mathscr L_\star\succeq \lambda_\star I\), then
\[
\mathscr L_b\succeq (\lambda_\star-\varepsilon)I.
\]
Thus any coercivity/gap certificate at \(\mathscr L_\star\) transports to \(b\) with controlled loss.

### Instantiation A (VSU / External Field Effect)
Let the total field gradient split as \(p=p_{\rm ext}+p_{\rm int}\) with \(|p_{\rm ext}|\gg a_0\).  
Taylor expansion of the convex Hamiltonian density gives
\[
\mathcal H(p_{\rm ext}+p_{\rm int})
=
\mathcal H(p_{\rm ext})
+\langle \nabla\mathcal H(p_{\rm ext}),p_{\rm int}\rangle
+\tfrac12\langle p_{\rm int},D^2\mathcal H(p_{\rm ext})\,p_{\rm int}\rangle+\cdots.
\]
In the strong-field limit, \(D^2\mathcal H(p_{\rm ext})\to (4\pi G)^{-1}I\), so internal perturbations see the Newtonian quadratic tangent theory.

### Instantiation B (OS / “good set” hinge in lattice gauge)
At the vacuum, the Wilson-action Hessian equals the deterministic Maxwell operator (up to coupling):  
\(\nabla^2S(U^{(0)})=\alpha_W d_1^*d_1\).  
On the “good set” \(\mathcal K_{\Lambda_L,\beta}\), the Hessian is controlled relative to its vacuum value, giving a uniform lower bound (“matrix hinge”) by a deterministic massive Maxwell operator \(M^{\rm hinge}\).  
This is the same transport theorem: background restriction + Hessian closeness \(\Rightarrow\) coercivity certificate.

---

## 5. Why this unifies the two tracks
Both tracks implement the same pattern:

1. Choose a background \(b\) (strong external field, or good set).
2. Linearize at \(b\) to obtain \(\mathscr L_b\).
3. Prove \(\mathscr L_b\) is close to a deterministic reference \(\mathscr L_\star\).
4. Transport coercivity/gap/positivity certificates from \(\mathscr L_\star\) to \(\mathscr L_b\).

This is “admissibility as a firewall”: the inequality calculus decides which backgrounds/flows are safe, regardless of the detailed equation.
