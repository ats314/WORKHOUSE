# Haar convexity + Wilson stability: a localized **matrix hinge** inequality

\begin{abstract}
We isolate a quantitative, operator-level lower bound for the Bakry--\'{E}mery curvature matrix of the Wilson--Haar Gibbs measure on the configuration manifold \(M_\Lambda = G^{E(\Lambda)}\). The bound has the schematic form
\[
\mathrm{Ric}_{\mu_\Lambda}(U) \ \succeq\  m^2 I + t\, d_1^*d_1
\qquad (U\in K_\Lambda(r)),
\]
with explicit \(m^2>0\) coming from Haar geometry and explicit \(t>0\) coming from the Wilson Hessian at the vacuum. The remainder is an \(O(\beta r)\) perturbation controlled only by locality/overlap constants.
\end{abstract}

## 1. Setting

- Fix a finite oriented lattice \(\Lambda\subset \mathbb Z^d\) (typically \(d=4\)). Let \(E(\Lambda)\) be the set of oriented edges and \(P(\Lambda)\) the set of oriented plaquettes.
- Let \(G=\mathrm{SU}(N)\) with a fixed \(\mathrm{Ad}\)-invariant inner product \(\langle\cdot,\cdot\rangle_{\mathfrak g}\) on \(\mathfrak g=\mathrm{Lie}(G)\), inducing a bi-invariant Riemannian metric \(g_G\) on \(G\).
- Configuration manifold:
\[
M_\Lambda := G^{E(\Lambda)},
\]
with product metric \(g_\Lambda\) and product Haar probability measure \(d\mu_{\mathrm{Haar}}^{\otimes E(\Lambda)}\). For a bi-invariant metric, Haar equals Riemannian volume.

### Wilson action and Gibbs measure
Take the standard Wilson plaquette action
\[
S_W(U):= \frac{\beta}{N}\sum_{p\in P(\Lambda)} \Bigl(1-\frac{1}{N}\Re\Tr\,U_p(U)\Bigr),
\]
with \(U_p\) the ordered product around \(\partial p\). The (finite-volume) Wilson--Haar Gibbs measure is
\[
\mu_\Lambda(dU) := Z_\Lambda^{-1} e^{-S_W(U)}\, d\mathrm{vol}_{g_\Lambda}(U).
\]

### The Bakry--\'{E}mery curvature matrix
For the reversible diffusion generator
\[
Lf = \Delta_{g_\Lambda}f - \langle\nabla S_W,\nabla f\rangle,
\]
the Bochner--Bakry--\'{E}mery identity involves
\[
\mathrm{Ric}_{\mu_\Lambda}(U) := \mathrm{Ric}_{g_\Lambda}(U)+\nabla^2 S_W(U),
\]
viewed as a symmetric operator on \(T_U M_\Lambda\).

## 2. Haar (geometric) positivity: the on-site mass term
Assume the group Ricci curvature satisfies
\[
\mathrm{Ric}_G \ge \kappa_G\, g_G \quad (\kappa_G>0).
\]
Then on the product manifold
\[
\mathrm{Ric}_{g_\Lambda}(U) \succeq c_H I, \qquad c_H := \kappa_G, 
\]
uniformly in \(\Lambda\). (Product structure makes this block-diagonal across links.)

**Interpretation:** \(c_H\) is the volume-uniform “Haar mass” term; it exists even with \(\beta=0\).

## 3. The vacuum Maxwell matrix \(d_1^*d_1\)
Let \(\mathcal C^k(\Lambda;\mathfrak g)\) denote \(\mathfrak g\)-valued \(k\)-cochains. The coboundary \(d_1:\mathcal C^1\to \mathcal C^2\) is the plaquette curl.

At the vacuum configuration \(U^{(0)}\equiv \mathbf 1\), use right-trivialization to identify
\[
T_{U^{(0)}}M_\Lambda \cong \mathcal C^1(\Lambda;\mathfrak g).
\]
Then the quadratic expansion of \(S_W\) at \(U^{(0)}\) yields the vacuum Hessian identity
\[
\nabla^2 S_W(U^{(0)}) = t\, d_1^*d_1,
\qquad t = t(N,\beta,\langle\cdot,\cdot\rangle_{\mathfrak g})>0.
\]
In the common \(G=\mathrm{SU}(3)\) normalization used in the notes this simplifies to \(t=\beta/3\).

## 4. The canonical small-field region \(K_\Lambda(r)\)
Let \(B_r(e)\subset G\) be the geodesic ball around the identity. Define
\[
K_\Lambda(r) := \{U\in M_\Lambda: U_\ell\in B_r(e)\ \forall\,\ell\in E(\Lambda)\}.
\]
This is a *linkwise* small-field set, chosen so Taylor constants of the plaquette map are uniform.

Let \(\nu\) be the local incidence constant
\[
\nu := \max_{\ell\in E(\Lambda)} \#\{p\in P(\Lambda): \ell\in \partial p\},
\]
which depends only on dimension and lattice type (not on \(|\Lambda|\)).

## 5. Wilson Hessian stability on \(K_\Lambda(r)\)
The second derivative of the single-plaquette class function in the four link variables is Lipschitz on a fixed compact neighborhood. Concretely, there exists a constant \(M_3(r_\star)\) (a uniform third-derivative bound on a compact chart) such that for all \(U\in K_\Lambda(r)\) and all tangent vectors \(X\in T_U M_\Lambda\),
\[
\nabla^2 S_W(U)(X,X)
\ \ge\ \nabla^2 S_W(U^{(0)})(X,X)\ -\ R_W(r)\,\|X\|^2,
\]
with explicit remainder
\[
R_W(r) = C_W\,\beta\, r,\qquad C_W := \frac{2\nu\,M_3(r_\star)}{N} \ \text{(up to normalization conventions)}.
\]
The only “large” object is \(\nu\), which is a bounded-degree constant.

## 6. The hinge inequality
Combine Haar positivity and Wilson stability.

\begin{proposition}[Localized hinge inequality]
Fix \(r\le r_\star\). For all \(U\in K_\Lambda(r)\),
\[
\mathrm{Ric}_{\mu_\Lambda}(U)
= \mathrm{Ric}_{g_\Lambda}(U)+\nabla^2 S_W(U)
\ \succeq\ (c_H-R_W(r))I + t\,d_1^*d_1.
\]
\end{proposition}

In particular, if \(r\) is chosen so that \(R_W(r)\le c_H/2\) (i.e. \(r\lesssim c_H/(\beta C_W)\)), then
\[
\mathrm{Ric}_{\mu_\Lambda}(U)\ \succeq\ M := \frac{c_H}{2}I + t\, d_1^*d_1,
\qquad (U\in K_\Lambda(r)).
\]

## 7. Gauge projection remark (why horizontals matter)
Gauge invariance implies that for gauge-invariant observables \(F\), the gradient \(\nabla F\) is horizontal (orthogonal to gauge orbits). In the notes this is encoded as restriction to \(\ker d_0^*\) at the vacuum (and its transported horizontal bundle off-vacuum). The hinge is then used only on that horizontal sector.

## 8. Status and “why this is exciting”

- The inequality is *complete* as a local (small-field) operator statement: it is an explicit, volume-uniform coercivity matrix that keeps the Maxwell geometry \(d_1^*d_1\) intact.
- This matrix form is precisely what allows Helffer--Sj\"ostrand covariance bounds and Green-kernel decay arguments to stay sharp.

**What remains external to this lemma:** turning a *local* hinge into a *global* statement requires a localization/typicality mechanism (Lyapunov drift or concentration) to ensure \(\mu_\Lambda(K_\Lambda(r))\) is sufficiently close to 1 in the regime of interest.
