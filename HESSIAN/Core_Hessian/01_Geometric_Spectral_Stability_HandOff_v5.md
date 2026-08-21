# Geometric–Spectral Stability for the Yang–Mills Mass Gap  
*Expanded hand‑off note: “seed → sustain → lock‑in” across scales (v2)*

> **Purpose.** This is a cleaned‑up and *more explicit* version of the original hand‑off sketch.  
> It tries to (i) separate what is finite‑cutoff/rigorous from what is conjectural,  
> (ii) make the geometry/probability/physics dictionary precise enough to work with, and  
> (iii) state the “hand‑off” step as a comparison principle problem (continuous Riccati + discrete MFIP).

---

## 0. Executive picture

The organizing hypothesis of the project is a **three‑phase mechanism** for a Yang–Mills mass gap:

1. **Seed (finite cutoff, \(a>0\)).**  
   Compact group geometry + the Haar Jacobian generate **explicit local convexity** in link‑algebra coordinates, i.e. a positive quadratic term (“Haar mass”).  

2. **Sustain / hand‑off (multiscale).**  
   Under a *smoothing/coarse‑graining* map (an RG step, or a heat‑kernel surrogate), the **horizontal Hessian** of the effective action evolves by a **matrix reaction–diffusion equation** whose smallest eigenvalue should satisfy a **Riccati‑type inequality with a positive source**:
   \[
   \dot\lambda \;\gtrsim\; -\alpha\,\lambda^2 + \sigma_*.
   \]
   If \(\sigma_*>0\) is *cutoff‑independent*, then even an \(a^2\)-scaled seed can “ignite” a scale that stabilizes at \(\lambda\sim\sqrt{\sigma_*}\) and does **not** vanish as \(a\to 0\).

3. **Lock‑in (phase/topology).**  
   In the confining phase, Wilson loops generate a string tension. The hypothesis is that along a renormalization trajectory with no phase transition, this sector obstructs a continuous collapse of the transfer‑matrix gap to \(0\).

The genuinely hard part is (2): proving a **nonvanishing source \(\sigma_*\)** and a rigorous eigenvalue comparison principle **uniformly in \(a\)**.

---

## 1. Setup and dictionary

### 1.1 Lattice configuration manifold

Fix a finite 4D lattice \(\Lambda\) with bond set \(\mathcal{B}\). The configuration space is
\[
\mathcal{C}_\Lambda = SU(N)^{|\mathcal{B}|},
\]
a compact Riemannian manifold (product of bi‑invariant metrics).

The Euclidean lattice measure is written in geometric form as
\[
d\mu_{\Lambda}(U) \;\propto\; e^{-S_{\mathrm{eff}}(U)}\,d\mathrm{vol}(U),
\qquad 
S_{\mathrm{eff}}(U)=\beta S_W(U)+S_{\mathrm{Haar}}(U).
\]

Here \(S_{\mathrm{Haar}}\) is the **measure action** coming from the Haar volume element in exponential coordinates; it is not an optional addition.

### 1.2 Operators and “gaps”: what is being gapped?

There are (at least) two natural operators in the background:

- **(A) Langevin / diffusion generator on \(\mathcal{C}_\Lambda\):**
  \[
  L f = \Delta f - \langle \nabla S_{\mathrm{eff}}, \nabla f\rangle,
  \]
  symmetric in \(L^2(\mu_\Lambda)\). A lower bound on the Bakry–Émery tensor
  \(\mathrm{Ric}+\nabla^2 S_{\mathrm{eff}}\) yields a **spectral gap for \(-L\)** (Poincaré inequality).

- **(B) Transfer matrix \(T\) in the Hamiltonian reconstruction:**
  \[
  H = -a_t^{-1}\log T,\qquad 
  \Delta_{\text{TM}}(a_t)= -a_t^{-1}\log(\lambda_1/\lambda_0),
  \]
  where \(\lambda_0>\lambda_1\) are the top eigenvalues of \(T\). This is the **finite‑cutoff mass gap** in the usual lattice Hamiltonian sense.

These two gaps are *not the same object*. The project’s strategy is:

- use geometric convexity and functional inequalities as a **robust analytic control tool** (especially suited to multiscale stability), and  
- use transfer‑matrix technology (strong coupling) as an **honest physical gap anchor**.

A key open interface is to quantify how curvature‑based control feeds into transfer‑matrix spectral information away from strong coupling.

---

## 2. The seed: Haar Jacobian \(\Rightarrow\) local “Haar mass” convexity

### 2.1 Exponential coordinates and the Jacobian

Near the identity, write each link variable as
\[
U=\exp(iagA),\qquad A\in\mathfrak{su}(N),
\]
with lattice spacing \(a\) and bare coupling \(g\).

The Jacobian of the exponential map is the standard Lie‑theoretic determinant
\[
J(A)=\det_{\mathfrak{g}}\!\left(
\frac{\sinh\!\left(\tfrac{1}{2}\operatorname{ad}_{iagA}\right)}
     {\tfrac{1}{2}\operatorname{ad}_{iagA}}
\right),
\qquad S_{\mathrm{Haar}}(A):=-\log J(A).
\]

### 2.2 Small‑field expansion (invariant content)

Using \(\log(\sinh x/x)=x^2/6+O(x^4)\) and \(X=\tfrac12\operatorname{ad}_{iagA}\),
\[
S_{\mathrm{Haar}}(A)
= \frac{a^2 g^2}{24}\;\mathrm{Tr}_{\mathrm{ad}}(\operatorname{ad}_A^2)
+O(a^4\|A\|^4).
\]

On a compact semisimple Lie algebra, \(\mathrm{Tr}_{\mathrm{ad}}(\operatorname{ad}_A^2)\) is **negative** and proportional to \(-\|A\|^2\) in the \((-)\)Killing norm, hence
\[
S_{\mathrm{Haar}}(A)=c_{\mathrm{H}}\,a^2 g^2\,\|A\|^2 + O(a^4\|A\|^4),
\qquad c_{\mathrm{H}}>0.
\]

**Interpretation.** Summed over bonds \(b\in\mathcal{B}\), this is an explicit positive quadratic term:
\[
S_{\mathrm{Haar,tot}}(A)\approx c_{\mathrm{H}}\,a^2 g^2\sum_{b\in\mathcal{B}}\|A_b\|^2.
\]

This is the **finite‑cutoff convexity seed**. It is small when \(a\) is small (and even smaller once \(g(a)\to 0\) along an asymptotically free trajectory), so by itself it does *not* solve the continuum problem. Its role is to provide a **sign** and a **starting inequality**.

---

## 3. Curvature \(\Rightarrow\) functional inequalities: Bakry–Émery bridge

On a Riemannian manifold \((M,g)\) with density \(e^{-S}\,d\mathrm{vol}\), define
\[
L = \Delta - \langle \nabla S, \nabla \cdot\rangle.
\]
Bakry–Émery theory gives (schematically)
\[
\Gamma_2(f)
=
\|\nabla^2 f\|_{\mathrm{HS}}^2 + \big\langle (\mathrm{Ric}+\nabla^2 S)\nabla f,\nabla f\big\rangle.
\]

Thus a uniform lower bound
\[
\mathrm{Ric}+\nabla^2 S \;\ge\; \rho\,g,\qquad \rho>0,
\]
implies a Poincaré inequality and a **spectral gap for \(-L\)** at least \(\rho\).

### 3.1 Gauge symmetry and “horizontal” directions

For lattice gauge theory, \(\mathcal{C}_\Lambda\) has gauge redundancy: the action is constant along gauge orbits. Accordingly:

- **Vertical directions:** tangent to gauge orbits (pure gauge).  
- **Horizontal directions:** orthogonal complement (physical directions), defined using the product metric.

The relevant convexity is the **horizontal Hessian**:
\[
\nabla^2 S_{\mathrm{eff}}\big|_{\mathrm{hor}}.
\]

### 3.2 Reducible configurations and the role of capacity (important subtlety)

The orbit space has singular strata (reducibles: stabilizer larger than the center). The clean way to keep analysis honest is:

- prove reducibles form a **polar set** (capacity zero) for the Dirichlet form, and  
- prove horizontal convexity bounds on the **irreducible sector**.

**Caveat (codimension matters).** For \((1,2)\)-capacity, codimension \(1\) sets are generally *not* polar. A safe sufficient condition is that reducibles lie in a finite union of strata of **codimension \(\ge 2\)** (or Hausdorff dimension \(\le m-2\) in \(m=\dim \mathcal{C}_\Lambda\)).

This is where the “polarity firewall” enters: it allows one to ignore orbit‑space singularities in spectral statements without resolving them geometrically.

---

## 4. The hand‑off: Hessian evolution and a Riccati comparison principle

This section makes the “handoff” step explicit: the goal is a **scalar inequality** for the smallest *horizontal* Hessian eigenvalue.

### 4.1 A controllable smoothing surrogate

A mathematically clean surrogate for coarse‑graining is heat‑kernel smoothing:
\[
\rho_t = e^{t\Delta}\rho_0,\qquad \partial_t\rho_t=\Delta \rho_t,
\qquad \rho_t\propto e^{-S_t}.
\]
This does not *equal* Wilsonian RG, but it is a legitimate semigroup that (i) integrates short‑scale structure and (ii) yields explicit PDE identities for \(S_t\).

Under this assumption one gets the **viscous Hamilton–Jacobi equation** (up to a \(t\)-only constant):
\[
\partial_t S_t = \Delta S_t - \|\nabla S_t\|^2.
\]

### 4.2 Hessian reaction–diffusion equation (structure)

Let \(H_t=\nabla^2 S_t\). Differentiating covariantly yields schematically
\[
\partial_t H_t
=
\Delta_L H_t
\;-\;2H_t^2
\;+\;\mathcal{R}_t,
\]
where:

- \(\Delta_L\) is a Lichnerowicz‑type Laplacian on symmetric tensors,  
- the quadratic reaction term \(-2H_t^2\) is the “Riccati part”, and  
- \(\mathcal{R}_t\) collects curvature commutators and higher‑derivative terms.

The key point is not the exact tensor formula, but that the evolution has the form:
\[
\text{(diffusion)} + \text{(quadratic reaction)} + \text{(source/error)}.
\]

### 4.3 From a matrix PDE to a scalar ODE: what must be proved

Let \(\lambda(t)\) be the **infimum over space** of the smallest horizontal eigenvalue of \(H_t\). A standard route (Hamilton’s matrix maximum principle / viscosity methods) aims to prove an inequality of the type
\[
\dot\lambda(t)\;\ge\; -\alpha\,\lambda(t)^2 + \sigma(t) - \varepsilon(t),
\]
where:

- \(\alpha>0\) is a geometric constant,  
- \(\sigma(t)\) is a **positive source** (intrinsic geometry and/or anomaly data), and  
- \(\varepsilon(t)\) is a **coarse‑graining error** term (nonlocality, truncation, gauge‑projection artifacts).

The “hand‑off” goal is to show that for large scales,
\[
\sigma(t)\ge \sigma_* >0\quad\text{and}\quad \varepsilon(t)\to 0
\]
in a way that is **uniform as \(a\to 0\)**.



#### 4.3.1 Hinge lemma: tensor maximum principle for the minimal eigenvalue (target)

Everything in the “hand‑off” reduces to one technical hinge: turning a **matrix/tensor parabolic inequality** for the (horizontal) Hessian into a **closed scalar inequality** for its smallest eigenvalue.

> **Lemma (Hamilton‑type tensor maximum principle for \(\lambda_{\min}\) — target).**  
> Let \((M,g)\) be a closed Riemannian manifold (or a compact domain with smooth boundary and *reflecting/Neumann* boundary conditions, so boundary terms do not spoil the maximum principle).  
> Let \(E\to M\) be a smooth metric vector bundle with compatible connection \(\nabla^E\), and write \(\Delta_E:=\nabla^{E,*}\nabla^E\) for the connection Laplacian acting on sections of \(E\) and on symmetric endomorphisms by components.  
> Let \(H_t\in C^\infty([0,T]\times M;\mathrm{Sym}(E))\) be a smooth family of symmetric bundle endomorphisms.  
> Assume that, in the sense of quadratic forms on \(E\), there is an inequality
> \[
> (\partial_t-\Delta_E)H_t \;\succeq\; -\alpha\,H_t^2 \;+\; \Sigma_t,
> \tag{MP}
> \]
> for some constant \(\alpha>0\), where \(\Sigma_t(x)\) satisfies the lower bound
> \[
> \Sigma_t(x)\;\succeq\; \sigma_*(t)\,\mathrm{Id}_E \;-\; E_t(x),
> \qquad \|E_t(x)\|_{\mathrm{op}}\le \varepsilon(t).
> \tag{S}
> \]
> Define the global minimal eigenvalue
> \[
> \lambda(t):=\inf_{x\in M}\lambda_{\min}\big(H_t(x)\big).
> \]
> Then \(\lambda(t)\) is locally absolutely continuous and satisfies, for a.e. \(t\in(0,T)\),
> \[
> \dot\lambda(t)\;\ge\; -\alpha\,\lambda(t)^2 \;+\; \sigma_*(t)\;-\;\varepsilon(t).
> \tag{Riccati-\(\lambda\)}
> \]
> Consequently, if \(\ell(t)\) solves the comparison ODE
> \[
> \dot\ell(t)= -\alpha\,\ell(t)^2 + \sigma_*(t)-\varepsilon(t),
> \qquad \ell(0)\le \lambda(0),
> \]
> then the tensor lower bound propagates:
> \[
> H_t(x)\succeq \ell(t)\,\mathrm{Id}_E
> \quad\text{for all }(t,x)\in[0,T]\times M.
> \]

**Proof (bundle version; written out).** Fix \(t_0\in(0,T)\). Choose \(x_0\in M\) with
\[
\lambda(t_0)=\lambda_{\min}(H_{t_0}(x_0)).
\]
Pick a unit eigenvector \(v_0\in E_{x_0}\) such that \(H_{t_0}(x_0)v_0=\lambda(t_0)v_0\).  
Extend \(v_0\) to a local section \(v\) near \(x_0\) by \(\nabla^E\)-parallel transport; then \(|v|\equiv 1\) and \((\nabla^E v)(x_0)=0\).

Define the scalar function \(\phi(x,t)=\langle H_t(x)v(x),v(x)\rangle\). At time \(t_0\), \(x\mapsto \phi(x,t_0)\) has a local minimum at \(x_0\) because
\[
\phi(x,t_0)\ge \lambda_{\min}(H_{t_0}(x))\ge \lambda(t_0)=\phi(x_0,t_0).
\]
Hence \(\Delta\phi(x_0,t_0)\ge 0\). Moreover \(\partial_t\phi=\langle (\partial_t H_t)v,v\rangle\), and expanding \(\Delta\phi\) using the product rule shows that at \((x_0,t_0)\) all terms involving \(\nabla^E v\) vanish; the remaining “\(\Delta v\)” term cancels because \(v\) has constant length and \(v_0\) is an eigenvector:
\[
0=\Delta |v|^2
=2\langle \Delta_E v,v\rangle + 2\sum_i\|\nabla^E_{e_i}v\|^2
\quad\Rightarrow\quad
\langle \Delta_E v,v\rangle(x_0)=0,
\]
so
\[
\langle H_{t_0}(x_0)\Delta_E v,v_0\rangle
=
\langle \Delta_E v, H_{t_0}(x_0)v_0\rangle
=
\lambda(t_0)\langle \Delta_E v,v_0\rangle
=0.
\]
Therefore
\[
(\partial_t-\Delta)\phi(x_0,t_0)
=
\left\langle \big((\partial_t-\Delta_E)H_{t_0}\big)(x_0)v_0,\,v_0\right\rangle.
\]
Insert (MP) and test on \(v_0\):
\[
(\partial_t-\Delta)\phi(x_0,t_0)
\ \ge\
-\alpha\,\langle H_{t_0}(x_0)^2 v_0,v_0\rangle
+\langle \Sigma_{t_0}(x_0)v_0,v_0\rangle
=
-\alpha\,\lambda(t_0)^2+\langle \Sigma_{t_0}(x_0)v_0,v_0\rangle.
\]
Using \(\Sigma_{t_0}(x_0)\succeq \sigma_*(t_0)I -E_{t_0}(x_0)\) and \(\|E_{t_0}(x_0)\|_{\mathrm{op}}\le \varepsilon(t_0)\),
\[
\langle \Sigma_{t_0}(x_0)v_0,v_0\rangle \ge \sigma_*(t_0)-\varepsilon(t_0).
\]
Finally, since \(\phi(\cdot,t_0)\) has a minimum at \(x_0\), \(\Delta\phi(x_0,t_0)\ge 0\) implies \(\partial_t\phi(x_0,t_0)\ge (\partial_t-\Delta)\phi(x_0,t_0)\). Putting the inequalities together yields
\[
\partial_t\phi(x_0,t_0)\ \ge\ -\alpha\,\lambda(t_0)^2+\sigma_*(t_0)-\varepsilon(t_0).
\]
This is exactly the viscosity (hence a.e.) inequality (Riccati-\(\lambda\)). ODE comparison then gives the propagated tensor bound \(H_t\succeq \ell(t)I\).  

(For the Yang–Mills application, take \(E=T^{\mathrm{hor}}M\); the only extra work is to check that the chosen connection/Laplacian respects the horizontal restriction up to an error absorbed in \(\varepsilon(t)\).)



**Yang–Mills “to be verified” hypotheses.** In the intended application:
- \(M\) is the **irreducible sector** of configuration space (or a gauge slice) and \(E\) is the **horizontal bundle**; check that \(E\) is a smooth subbundle there and that the chosen Laplacian (rough/Lichnerowicz) respects the horizontal restriction.  
- The commutator/curvature terms \(\mathcal{R}_t\) in §4.2 must be reorganised into a *scalar floor* \(\sigma_*(t)\) plus an error \(E_t\) with \(\varepsilon(t)\) controlled uniformly along the refinement trajectory.  
- Reducibles can be excised without changing Dirichlet‑form spectral statements because they are polar/capacity‑zero (the “polarity firewall” of §3.2).

*Remark.* If one drops diffusion (\(\Delta_E=0\)) and takes \(\Sigma_t\simeq K_{\mathrm{eff}}\mathrm{Id}\), then (Riccati-\(\lambda\)) collapses to the scalar Riccati comparison \(\dot\lambda\ge -\alpha\lambda^2+K_{\mathrm{eff}}\), with stable fixed point \(\sqrt{K_{\mathrm{eff}}/\alpha}\). Diffusion is a friend: it cannot decrease the spatial minimum under the maximum principle.


### 4.4 The Riccati comparison lemma (explicit)

If one can reduce to a pure ODE comparison
\[
\dot\ell = -\alpha\,\ell^2 + \sigma_*,\qquad \sigma_*>0,
\]
then the fixed point \(\ell_*=\sqrt{\sigma_*/\alpha}\) is stable, and any \(\ell(0)\ge 0\) yields \(\ell(t)\uparrow \ell_*\) (after a transient).

For \(\alpha=2\) the solution is explicit:
\[
\ell(t)=\sqrt{\frac{\sigma_*}{2}}\,
\tanh\!\left(\sqrt{2\sigma_*}\,t + \operatorname{arctanh}\!\Big(\sqrt{\tfrac{2}{\sigma_*}}\ell(0)\Big)\right),
\]
so in particular \(\inf_{t\ge 0}\ell(t)\ge \min\{\ell(0),\sqrt{\sigma_*/2}\}\).

**Hand‑off interpretation.** The Haar seed only needs to guarantee \(\ell(0)\ge 0\) (or tiny positive). The long‑time lower bound is controlled by \(\sigma_*\), not by the vanishing seed scale.

---

## 5. Discrete multiscale version: MFIP (fixed‑point inequality)

A discrete analogue of the Riccati picture is the **Multiscale Fixed‑Point Inequality (MFIP)**:

\[
\rho_{j+1} \;\ge\; K\,\rho_j \;-\;\varepsilon_j \;+\;\sigma_*,
\qquad 0<K<1.
\]

Here \(\rho_j\) plays the role of a “curvature/gap” parameter at scale \(j\).  
If \(\varepsilon_j\) is summable (or \(\limsup \varepsilon_j\) is small) and \(\sigma_*>0\), then \(\rho_j\) has a positive fixed‑point lower bound:
\[
\liminf_{j\to\infty}\rho_j \;\ge\; \frac{\sigma_*-\varepsilon_\infty}{1-K}.
\]

This is the same story as Riccati, but in a form closer to Wilsonian RG bookkeeping:  
**errors must not eat the source.**

---

## 6. The lock‑in: transfer matrix, Wilson loops, and phase structure

At strong coupling (small temporal plaquette coupling), standard character‑expansion arguments imply:

- the transfer matrix has a unique positive maximal eigenvalue,  
- Wilson loops generate low‑lying excitations, and  
- there is an explicit bound of the form
  \[
  \frac{\lambda_1}{\lambda_0}\;\lesssim\; (c\,\beta_t)^{L_{\min}},
  \]
  hence a strictly positive finite‑\(a\) mass gap.

The **lock‑in hypothesis** is then:

- if the confining phase persists along a renormalization trajectory to the continuum limit (no intervening phase transition),  
- then a nonzero string tension / center symmetry structure obstructs the transfer‑matrix gap from continuously collapsing to zero.

A mathematically useful way to sharpen “lock‑in” is to replace it by **phase‑diagram control**:

- identify an order parameter / inequality that certifies confinement (e.g. an area‑law lower bound or center symmetry constraints), and  
- show it persists along the trajectory.

---

## 7. Clean conjecture statement (with explicit failure modes)

> **Conjecture (Geometric–Spectral Stability / Hand‑off).**  
> Consider a sequence of lattices with spacing \(a\to 0\) and corresponding measures \(d\mu_a\propto e^{-S_{\mathrm{eff},a}}d\mathrm{vol}\) on \(\mathcal{C}_a\).  
> Suppose there exists a multiscale map (RG step or smoothing surrogate) producing a scale‑indexed family \(S_{j,a}\) such that:
>
> 1. (**Seed at finite cutoff**) On the irreducible sector and horizontal directions,
>    \(\nabla^2 S_{0,a}\big|_{\mathrm{hor}}\ge 0\) (or \(\ge \rho_*(a)>0\)).
>
> 2. (**Hand‑off inequality**) The smallest horizontal Hessian eigenvalue \(\rho_{j,a}\) satisfies an MFIP recursion
>    \[
>    \rho_{j+1,a}\ge K\rho_{j,a}-\varepsilon_{j,a}+\sigma_*,
>    \]
>    with \(K\in(0,1)\) independent of \(a\), \(\varepsilon_{j,a}\to 0\) as \(j\to\infty\) uniformly in \(a\), and \(\sigma_*>0\) independent of \(a\).
>
> 3. (**Polarity firewall**) Reducibles are polar (capacity zero), so failures of convexity confined to reducible strata do not affect the spectral theory.
>
> 4. (**Phase control / lock‑in**) The confining Wilson‑loop sector persists along the trajectory with a nonzero string tension or equivalent obstruction to gap collapse.
>
> Then the continuum limit has a nonzero mass gap.

**How it can fail (useful as a debugging checklist):**

- \(\sigma_*=0\) (no anomaly/topology source survives).  
- \(\varepsilon_{j,a}\) is not summable/uniform (errors accumulate and eat the source).  
- reducibles are not polar in the relevant form (singular strata dominate).  
- a phase transition intervenes (lock‑in breaks).  
- the chosen “flow” is not genuinely connected to the physical RG/continuum reconstruction.

---

## 8. Concrete next steps (what to prove / compute)

1. **Matrix maximum principle in the horizontal bundle.**  
   Write the Hessian evolution on \(\mathcal{C}_\Lambda\) and prove an eigenvalue comparison inequality for the *horizontal* minimal eigenvalue, with error terms explicitly controlled.

2. **Identify a real candidate for \(\sigma_*\).**  
   Two plausible routes:
   - **Trace anomaly route:** connect \(\langle F^2\rangle\) / \(\beta(g)\) data to a lower bound on effective curvature.
   - **Topology route:** use \(\theta\)-dependence and topological susceptibility \(\chi_t\) to produce a convexity datum.

3. **Polarity with correct codimension thresholds.**  
   Give a clean stratification/codimension bound for reducible loci on finite lattices and verify capacity \(0\) using codimension \(\ge 2\) (or Hausdorff dimension \(\le m-2\)).

4. **Bridge curvature control to transfer‑matrix statements.**  
   Even a partial result—e.g. a regime where curvature bounds imply exponential decay of suitable Euclidean correlators—would make the program much more rigid.

---

### Where to look in the package

- Haar mass seed and horizontal Hessian: `03_Haar_Mass_and_Horizontal_Hessian_Gap.md` + `YM_Lattice_Haar_Hessian_MassGap.tex`.  
- Riccati/vHJ derivations: `Dynamic_Hessian_Riccati_Flow.tex`.  
- MFIP / conjectural bookkeeping: `02_Conjectures_A_B_Multiscale_Stability.md`.  
- Polarity/capacity cautions: `04_Polarity_of_Reducibles_Capacity.md`.  
- Transfer matrix gap at strong coupling: `YM_Lattice_Transfer_Matrix_Gap.tex`.  
- \(\theta\)/topology computational angle: `05_Theta_Term_QuantumGroup_TensorNetwork.md`.

