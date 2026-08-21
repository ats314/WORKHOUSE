
# Making the “physical projection” precise and RG-compatible
*(A concrete choice for \(\Pi_{\mathrm{phys}}\), and the exact compatibility condition you need with blocking.)*

## 1. What \(\Pi_{\mathrm{phys}}\) must do in your story
Your curvature-defect mechanism and the Bianchi-rigidity story both want a **clean split**
\[
T_U M_\Lambda \;\cong\; \mathcal G_U \oplus \mathcal G_U^\perp,
\]
where \(\mathcal G_U\) are gauge directions, and where “physical Hessians” (or reduced stiffness matrices) act coercively on \(\mathcal G_U^\perp\).

Operationally, that requires a projection on observables (or on tangent vectors) that:

1. really removes gauge directions (not approximately),
2. is compatible with the Gibbs measure (so IBP / Dirichlet technology survives),
3. is compatible with RG blocking (so the defect doesn’t get destroyed by coarse-graining).

## 2. The cleanest exact \(\Pi_{\mathrm{phys}}\): Haar averaging
Let the gauge group \(G^{V(\Lambda)}\) act on link configurations \(U\in G^{E(\Lambda)}\) by
\[
(g\cdot U)_{xy}=g_x\,U_{xy}\,g_y^{-1}.
\]

If the lattice action \(S_\Lambda(U)\) is gauge invariant, the Gibbs measure \(\mu_\Lambda\) is gauge invariant too.

Then the orthogonal projection (in \(L^2(\mu_\Lambda)\)) onto gauge-invariant functions is simply **group averaging**:
\[
(\Pi_{\mathrm{phys}}F)(U)
:=\int_{G^{V(\Lambda)}} F(g\cdot U)\,dg,
\]
where \(dg\) is Haar measure on \(G^{V(\Lambda)}\).

Properties (exact, no handwaving):
- \(\Pi_{\mathrm{phys}}^2=\Pi_{\mathrm{phys}}\) and \(\Pi_{\mathrm{phys}}^\ast=\Pi_{\mathrm{phys}}\).
- \(\Pi_{\mathrm{phys}}F = F\) iff \(F\) is gauge invariant.
- \(\Pi_{\mathrm{phys}}\) commutes with any gauge-invariant operator built from \(S_\Lambda\) and the bi-invariant metric.

This is the minimal “physics projection” with the fewest moving parts.

## 3. RG compatibility: the one condition you need
Let \(\pi: M_{\Lambda}\to M_{\Lambda'}\) be your blocking map (coarse graining), and let \(\pi_\ast\mu_\Lambda=\mu_{\Lambda'}\).

To make \(\Pi_{\mathrm{phys}}\) RG-compatible, it is enough that \(\pi\) is **gauge covariant**, i.e.
\[
\pi(g\cdot U)=\bar g\cdot \pi(U)
\quad\text{for some induced coarse gauge transform } \bar g.
\]
Equivalently, \(\pi\) intertwines the two gauge actions.

Then the projections commute with coarse graining in the strongest useful sense:

### Lemma (intertwining of projections)
If \(\pi\) is gauge covariant and \(\mu_\Lambda\) is gauge invariant, then
\[
\Pi_{\mathrm{phys}}^{(\Lambda')}\,\pi_\ast \;=\; \pi_\ast\,\Pi_{\mathrm{phys}}^{(\Lambda)}
\]
on observables (in the appropriate \(L^2\) spaces).

*Proof sketch.* Gauge covariance lets you change variables \(U\mapsto g\cdot U\) under \(\mu_\Lambda\) and slide the Haar averaging through the pushforward integral. ∎

This is the “RG-compatible” notion you want: the physical sector is preserved under blocking.

## 4. Gauge-fixing realizations (useful for Hessians)
If you need an explicit “\(\mathcal G^\perp\)” on tangent spaces (not just on observables), you can implement \(\Pi_{\mathrm{phys}}\) by a concrete gauge fixing:

- **Tree gauge:** choose a spanning tree \(T\subset E(\Lambda)\) and set \(U_e=\mathbf 1\) for \(e\in T\).
- **Background/linear gauge:** use a discrete Hodge decomposition \(1\text{-forms} = d0\text{-forms} \oplus \delta 2\text{-forms} \oplus \text{harmonic}\).

This is where “RG compatibility” becomes delicate: you must track how the gauge condition transforms under blocking.
A safe pattern is:

1. define blocking \(\pi\) on gauge-invariant Wilson loops/plaquettes first,
2. represent coarse links by a fixed path-ordered product on the fine lattice,
3. pick a gauge fixing that is defined *intrinsically* (e.g. Coulomb/Hodge) rather than by a geometric tree that changes under blocking.

## 5. Practical approximation: penalty projection in Hamiltonian language
If you’re working on the Hamiltonian side, a standard way to enforce “physicality” is to add a Gauss-law penalty term
\[
H \mapsto H + \kappa\sum_x G_x^2,
\]
and take \(\kappa\) large enough to push unphysical states up in energy.

This is not an exact projection, but it is often RG-friendly because it’s local and gauge-covariant. (This is precisely the kind of tuning issue discussed in digitized SU(2) Hamiltonian simulations.)

## 6. How this plugs into curvature-defect
Once \(\Pi_{\mathrm{phys}}\) is fixed, the curvature-defect functional you defined (in spirit)
\[
\delta(U) := \lambda_{\min}\!\left(\mathrm{Hess}\,S_\Lambda(U)\big|_{\mathcal G^\perp}\right)
\]
becomes an honest, gauge-invariant object **provided** the complement \(\mathcal G^\perp\) is defined in a gauge-covariant way (Hodge) or in a gauge-fixed chart (tree gauge).

Then the only remaining RG question is: does the blocked effective action preserve a positive lower bound on this reduced Hessian?  
That’s where your “conditional spectral floor monotonicity” lemma becomes relevant: it is exactly the kind of statement that can show “defect cannot systematically decrease under coarse-graining” if the blocking is an averaging/conditional expectation.
