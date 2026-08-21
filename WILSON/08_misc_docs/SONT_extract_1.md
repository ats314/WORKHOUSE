# Local cancellation and coercive drift in SU(2) lattice Yang–Mills (project extract)

*Status:* **derived from project files; proof-level** (finite-cutoff, finite volume).  
*Theme:* turning a **geometric obstruction (gradient cancellations)** into a **coercive drift** mechanism for functional inequalities.

---

## 1. The microlocal obstruction: why naive curvature bounds fail

A recurring technical bottleneck in the project is that the “good” coercive term in the
Bochner/Bakry–Émery expansion involves a *pairing*
\[
P_\Lambda(U) \;:=\; \frac12\big\langle \nabla S_\Lambda(U),\,\nabla V_\Lambda(U)\big\rangle ,
\]
and the main desired estimate is a **lower bound**
\[
P_\Lambda(U)\;\ge\; \rho\, V_\Lambda(U) \qquad\text{(uniformly on a controlled set),}
\]
because this forces a spectral/functional-inequality contraction mechanism at the level of the
Dirichlet form.

The project explicitly flags that **this can fail** if $\nabla S$ and $\nabla V$ are systematically
anti-aligned (or cancel by symmetry), and therefore any global $CD(\rho,\infty)$ type estimate must
be replaced by a *geometry-of-cancellation* statement.

---

## 2. “Aligned Cartan” cancellation: the SU(2) local cancellation theorem

The key novel-looking lemma in the project is a **rigidity statement**: cancellation of several
rotated vectors in $\mathfrak{su}(2)\cong \mathbb R^3$ is only possible if they are almost collinear,
i.e. concentrated near a single Cartan axis.

### Theorem (Local cancellation / aligned Cartan rigidity)

Fix a small neighborhood $B_r^G(1)\subset SU(2)$. There exists an “aligned Cartan” subset
\[
\mathcal A_r^G \;\subset\; B_r^G(1)
\]
such that for any collection of Lie algebra elements $X_1,\dots,X_n\in\mathfrak{g}$ and signs
$\sigma_i\in\{\pm 1\}$, the implication holds:

> If all group elements $g_i\in B_r^G(1)$ satisfy
> \[
> \sum_{i=1}^n \sigma_i\,\mathrm{Ad}_{g_i}(X_i)=0,
> \]
> then either the configuration lies in the exceptional aligned set ($g_i\in\mathcal A_r^G$), or else
> the $X_i$ must be “large” in an explicitly coercive way (equivalently, cancellation is impossible
> unless the vectors are essentially collinear).

The proof sketch in the project is geometric: in $\mathbb R^3$, exact cancellation of several
rotated vectors forces the “pairwise opposite” structure, which in turn forces all vectors to lie
on (approximately) a common line, i.e. a Cartan axis.

*Why it matters:* in Wilson theory, the linkwise forces are sums of $\mathrm{Ad}$-rotated plaquette
forces. The lemma therefore supplies an **almost-everywhere lower bound**
\[
\big|\nabla S\big| \;\gtrsim\; \text{(local roughness indicator)}
\]
*except on a thin aligned-Cartan exceptional set*. This is precisely the sort of geometric input
needed to rescue $P_\Lambda\ge \rho V_\Lambda$.

---

## 3. From cancellation rigidity to drift: “badness” as an order parameter

The project introduces a roughness / badness observable, written schematically as
\[
\mathcal B_\Lambda(U)\;=\;\text{average of local block badness } B_{x,\varepsilon}(U),
\]
and studies the drift of $\mathcal B_\Lambda$ under the Langevin generator:
\[
L_\Lambda\,\mathcal B_\Lambda \;\le\; -c\,\mathcal B_\Lambda + c'\,\mathbf 1_{K},
\]
where $K$ is the “good core” (small badness).

The aligned-Cartan cancellation theorem is the missing link in that drift computation: it provides a
mechanism to prevent the “rough-but-zero-force” pathology (a rough configuration where all plaquette
forces cancel), by showing that such cancellations demand simultaneous alignment across multiple
transverse planes — an overdetermined condition.

---

## 4. New-theory potential: “cancellation geometry” as a structural principle

The most exportable idea here is not SU(2)-specific; it is the **programmatic pattern**:

1. Identify the *pairing term* $P=\langle \nabla S,\nabla V\rangle$ as the true coercive quantity.
2. Prove **rigidity of cancellations** for the relevant gauge group (SU(N): $\mathfrak{su}(N)$ with
   adjoint action).
3. Use rigidity to show: “roughness $\Rightarrow |\nabla S|$ is bounded below” off a controlled
   exceptional locus.
4. Conclude a **coercive drift** and hence a functional inequality on the controlled region.

For SU(N), step (2) becomes a genuinely new geometric-algebra question:
how do $\mathrm{Ad}$-rotations in $\mathfrak{su}(N)$ constrain cancellations of sums?

A plausible route is to treat $\mathrm{Ad}$ as acting on the root-space decomposition and to prove
that exact/near cancellation forces concentration near a maximal torus (a “Cartan concentration”
phenomenon). If true, that becomes a reusable lemma in nonabelian probability on compact groups.

---

## 5. Concrete “next math” tasks

1. **Quantify the exceptional set.** Give a sharp bound on the measure (under the conditional Gibbs
   measure) of the aligned-Cartan locus $\mathcal A_r^G$.
2. **Generalize to SU(N).** Replace “collinearity in $\mathbb R^3$” by “Cartan concentration in
   $\mathfrak{su}(N)$”, with quantitative constants.
3. **Plug into the microlocal coercivity lemma.** Convert cancellation rigidity into an explicit
   lower bound on $P_\Lambda(U)$ on the controlled set $K_c$.
4. **Bootstrap to a global inequality.** Combine with boundary-strip gluing (see Doc 2/3) to
   propagate drift into uniform Poincaré/LSI bounds.

---
