---
file: Appendix_A__Notation_and_Constants.md
status: DRAFT
depends_on: []
feeds_into:
  - Core-1 (Lattice gauge model at fixed cutoff)
  - Core-2 (OS/reflection positivity framework)
  - Core-3 (Vacuum linearization and Hessian identification)
  - Core-4 (Small-field geometry and Bakry–Émery curvature lower bounds)
  - Core-5 (Helffer–Sjöstrand covariance representation and matrix BL)
  - Core-6 (Finite-range inverse decay / Green-kernel bounds)
  - Core-7 (Fixed-cutoff exponential clustering)
  - Core-8 (Thermodynamic limit at fixed cutoff)
  - Core-9 (OS reconstruction: Euclidean time decay ⇒ Hamiltonian gap)
  - Core-10 (Conditional continuum extension along a scaling trajectory)
---

# Appendix A — Notation and constants (single source of truth)

## A.0 Scope and rule set

**Definition A.0.1 (status labels).** Every labeled item in the Core Manuscript and Appendices is tagged as exactly one of:
- **Definition**
- **Assumption**
- **Lemma**
- **Proposition**
- **Theorem**
- **External Input**

**Definition A.0.2 (separation of proved / assumed / conditional material).**
- Items tagged **Lemma/Proposition/Theorem** are planned to be proved within the manuscript set.
- Items tagged **Assumption** are hypotheses internal to the program and are not proved within the manuscript set.
- Items tagged **External Input** are invoked without proof and must be cited to an external reference in the Core Manuscript.

**Definition A.0.3 (no hidden imports).**
Every file in the manuscript set begins with a machine-checkable header listing:
- `depends_on`: an explicit list of other files whose **Definitions/Assumptions/Lemmas/Propositions/Theorems/External Inputs** are used in the file (no transitive omission).
- `feeds_into`: the downstream Core items that the file is designed to support.

**Definition A.0.4 (single source of truth for constants).**
Every named constant (e.g. `r_sf`, `C_BCH`, `m^2`, `η_CT`) is introduced exactly once in the manuscript set: in this Appendix A.
All other files may only *reference* constants by name, citing the defining item number in this appendix.

**Definition A.0.5 (constant naming convention).**
Constants are grouped and named by functional role:
- radii and smallness thresholds: `r_*` (e.g. `r_log`, `r_BCH`, `r_sf`);
- group/geometric constants: `κ_G`, `ι_G`;
- combinatorial constants (dimension-dependent): `m_∂`, `ν_P`, `D_E`;
- analytic inequality constants: `c_*`, `C_*`;
- exponential decay rates: `η_*`;
- mass parameters (strictly positive): `m^2_*`.

No symbol is reused for a different quantity.

---

## A.1 Global parameters and index sets

**Definition A.1.1 (dimension and coordinate directions).**
The lattice dimension is fixed as
\[
d := 4,
\qquad
\mathsf I_d := \{0,1,2,3\}.
\]
The distinguished Euclidean time direction is the index `0`.

**Definition A.1.2 (lattice spacing / cutoff).**
The lattice spacing (cutoff scale) is a fixed parameter
\[
a \in (0,\infty).
\]
All fixed-cutoff statements are formulated at fixed `a`. Conditional continuum statements treat a sequence `(a_n)_{n\ge 1}` with `a_n\downarrow 0`.

**Definition A.1.3 (finite periodic lattice).**
A finite periodic lattice is specified by side lengths
\[
L = (L_\mu)_{\mu\in\mathsf I_d}\in (\mathbb N_{\ge 2})^{\mathsf I_d},
\qquad
\Lambda_L := \prod_{\mu\in\mathsf I_d} (\mathbb Z/L_\mu\mathbb Z).
\]
Vertices are identified with elements of `Λ_L`.

**Definition A.1.4 (unit coordinate vectors and shifts).**
For `\mu\in\mathsf I_d`, `\hat e_\mu` denotes the unit vector in direction `\mu`.
For `x\in\Lambda_L`, the shifts `x\pm \hat e_\mu` are understood modulo the periodic identifications.

---

## A.2 Cell sets, orientations, and combinatorial constants

### A.2.1 Cells

**Definition A.2.1 (vertex set).**
\[
V(\Lambda_L) := \Lambda_L.
\]

**Definition A.2.2 (positively oriented link set and reversal).**
The positively oriented link set is
\[
E(\Lambda_L)
:= \{(x,\mu): x\in \Lambda_L,\ \mu\in\mathsf I_d\}.
\]
The link `b=(x,\mu)` is viewed as the oriented edge from `x` to `x+\hat e_\mu`.
The reversed link symbol is `b^{-1}:=(x+\hat e_\mu,\mu)^{-1}`, and reversal of a link variable is always interpreted by
\[
U_{b^{-1}} := U_b^{-1}.
\]

**Definition A.2.3 (oriented plaquette set).**
The oriented plaquette set is
\[
P(\Lambda_L)
:= \{(x;\mu,\nu): x\in\Lambda_L,\ \mu,\nu\in\mathsf I_d,\ 0\le \mu<\nu\le 3\}.
\]

**Definition A.2.4 (plaquette boundary and incidence coefficients).**
For `p=(x;\mu,\nu)\in P(\Lambda_L)` with `\mu<\nu`, define the oriented boundary (as a signed 1–chain)
\[
\partial p
:= (x,\mu) + (x+\hat e_\mu,\nu) - (x+\hat e_\nu,\mu) - (x,\nu).
\]
For `p\in P(\Lambda_L)` and `b\in E(\Lambda_L)`, the incidence coefficient `\sigma_{p,b}\in\{-1,0,+1\}` is defined by
\[
\partial p = \sum_{b\in E(\Lambda_L)} \sigma_{p,b}\, b.
\]

### A.2.2 Dimension-dependent constants

**Definition A.2.5 (plaquette boundary length).**
\[
m_\partial := 4.
\]
This is the number of links in the boundary of any plaquette in the hypercubic lattice.

**Definition A.2.6 (plaquette–link overlap constant).**
\[
\nu_P
:= \sup_{b\in E(\Lambda_L)} \#\{p\in P(\Lambda_L):\ b\ \text{appears in}\ \partial p\}.
\]
This constant is purely combinatorial and depends only on the lattice dimension `d`.

**Proposition A.2.7 (explicit bound on `ν_P` for `d=4`).**
For the periodic hypercubic lattice in dimension `d=4`,
\[
\nu_P \le 2(d-1) = 6.
\]
*(Proof deferred; depends only on local incidence counting.)*

**Definition A.2.8 (link adjacency relation).**
For distinct links `b,b'\in E(\Lambda_L)`, write `b\sim b'` if there exists a plaquette `p\in P(\Lambda_L)` such that both `b` and `b'` appear (with nonzero incidence) in `\partial p`.

**Definition A.2.9 (link graph distance).**
Let `\mathrm{dist}_E` denote the graph distance induced by the adjacency relation `\sim` on `E(\Lambda_L)`.

**Definition A.2.10 (link graph degree bound).**
\[
D_E
:= \sup_{b\in E(\Lambda_L)} \#\{b'\in E(\Lambda_L):\ b'\neq b,\ b'\sim b\}.
\]
This constant depends only on `d` and not on the volume.

**Proposition A.2.11 (bound on `D_E` in terms of `ν_P`).**
\[
D_E \le 3\,\nu_P.
\]
In particular, in `d=4` one may take `D_E\le 18`.
*(Proof deferred; each plaquette contributes at most three neighbors to a fixed link.)*

---

## A.3 Gauge group, representation, and Lie-algebra conventions

### A.3.1 Group and representation

**Assumption A.3.1 (compact gauge group).**
`G` is a compact Lie group with identity element `\mathbf 1`.

**Definition A.3.2 (Lie algebra and adjoint action).**
\[
\mathfrak g := T_{\mathbf 1}G,
\qquad
\mathrm{Ad}_g:\mathfrak g\to\mathfrak g
\ \text{denotes the adjoint action}.
\]

**Assumption A.3.3 (fixed faithful unitary representation).**
A faithful unitary representation is fixed once and for all:
\[
\rho:G\to U(n),
\qquad n\in\mathbb N.
\]
Whenever `\mathrm{Tr}` or `\Re\mathrm{Tr}` appears with an argument in `G`, it denotes the trace in the representation `\rho`, i.e. `\mathrm{Tr}(g):=\mathrm{Tr}(\rho(g))`.

**Definition A.3.4 (trace bilinear form induced by `ρ`).**
Let `d\rho:\mathfrak g\to\mathfrak u(n)` be the derived representation.
Define the symmetric bilinear form
\[
B_\rho(X,Y)
:=
-\Re\mathrm{Tr}\big(d\rho(X)\,d\rho(Y)\big),
\qquad X,Y\in\mathfrak g.
\]
Faithfulness of `ρ` implies that `B_\rho` is positive definite.

### A.3.2 Metric normalization

**Definition A.3.5 (Ad-invariant inner product on `\mathfrak g`).**
The Lie-algebra inner product is fixed as
\[
\langle X,Y\rangle_{\mathfrak g} := B_\rho(X,Y),
\qquad X,Y\in\mathfrak g.
\]
All norms `|X|_{\mathfrak g}` are induced from this inner product.

**Definition A.3.6 (bi-invariant Riemannian metric on `G`).**
Let `g_G` denote the bi-invariant Riemannian metric on `G` obtained by left-translation of `\langle\cdot,\cdot\rangle_{\mathfrak g}`.

**Definition A.3.7 (injectivity radius at the identity).**
Let
\[
\iota_G := \mathrm{inj}_G(\mathbf 1)\in (0,\infty)
\]
denote the Riemannian injectivity radius of `(G,g_G)` at the identity.

**Assumption A.3.8 (positive Ricci lower bound).**
There exists a constant `\kappa_G>0` such that
\[
\mathrm{Ric}_G \succeq \kappa_G\, g_G
\quad\text{as quadratic forms on }TG.
\]
(Used only in the “Haar mass”/Bakry–Émery curvature lower bound mechanism.)

---

## A.4 Configuration manifold and differential operators

### A.4.1 Configuration manifold

**Definition A.4.1 (configuration manifold).**
\[
M_{\Lambda_L} := G^{E(\Lambda_L)}.
\]

**Definition A.4.2 (product metric).**
Equip `M_{\Lambda_L}` with the product metric
\[
g_{\Lambda_L} := \bigoplus_{b\in E(\Lambda_L)} g_G.
\]

**Definition A.4.3 (right-trivialization of tangent spaces).**
For `U=(U_b)_{b\in E(\Lambda_L)}\in M_{\Lambda_L}`, define the right-trivialization map
\[
\omega_U^R: T_U M_{\Lambda_L}\to \mathfrak g^{E(\Lambda_L)}
\]
componentwise by
\[
(\omega_U^R V)_b := (dR_{U_b^{-1}})_{U_b}(V_b)\in\mathfrak g,
\qquad b\in E(\Lambda_L),
\]
where `V_b\in T_{U_b}G` is the `b`-component of `V` under the product decomposition.
Its inverse is denoted `\tau_U^R := (\omega_U^R)^{-1}`.

**Definition A.4.4 (cochain notation for right-trivialized vectors).**
Under right-trivialization we identify
\[
\mathfrak g^{E(\Lambda_L)} \equiv \mathcal C^1(\Lambda_L;\mathfrak g).
\]
Thus right-trivialized tangent vectors are written as `1`-cochains.

### A.4.2 Differential operators on `M_{\Lambda_L}`

**Definition A.4.5 (gradient and Hessian).**
For a smooth function `F:M_{\Lambda_L}\to\mathbb R`, the gradient and Hessian with respect to `g_{\Lambda_L}` are denoted by
\[
\nabla F,
\qquad
\nabla^2 F.
\]

**Definition A.4.6 (Laplace–Beltrami operator).**
The Laplace–Beltrami operator on `(M_{\Lambda_L},g_{\Lambda_L})` is denoted by `\Delta_{\Lambda_L}`.

**Definition A.4.7 (carré du champ).**
For smooth `F,G`, define
\[
\Gamma_{\Lambda_L}(F,G) := \langle \nabla F,\nabla G\rangle_{g_{\Lambda_L}},
\qquad
\Gamma_{\Lambda_L}(F):=\Gamma_{\Lambda_L}(F,F).
\]

**Definition A.4.8 (diffusion generator for the Gibbs measure).**
For a smooth potential `S:M_{\Lambda_L}\to\mathbb R`, define the symmetric diffusion generator
\[
\mathcal L_S := \Delta_{\Lambda_L} - \langle \nabla S,\nabla(\cdot)\rangle_{g_{\Lambda_L}}.
\]
When `S=S_{\Lambda_L,\beta}` is the Wilson action (Definition A.6.2), write `\mathcal L_{\Lambda_L,\beta}`.

---

## A.5 Lattice cochains and discrete operators

### A.5.1 Cochain spaces

**Definition A.5.1 (`\mathfrak g`-valued cochains).**
\[
\mathcal C^0(\Lambda_L;\mathfrak g) := \mathfrak g^{V(\Lambda_L)},
\qquad
\mathcal C^1(\Lambda_L;\mathfrak g) := \mathfrak g^{E(\Lambda_L)},
\qquad
\mathcal C^2(\Lambda_L;\mathfrak g) := \mathfrak g^{P(\Lambda_L)}.
\]

**Definition A.5.2 (`\ell^2` inner products).**
Equip each `\mathcal C^k(\Lambda_L;\mathfrak g)` with the `\ell^2` inner product induced by `\langle\cdot,\cdot\rangle_{\mathfrak g}`; denote it by `\langle\cdot,\cdot\rangle_{\mathcal C^k}` and the induced norm by `|\cdot|_{\mathcal C^k}`.

### A.5.2 Coboundaries and adjoints

**Definition A.5.3 (discrete coboundary `d_0:\mathcal C^0\to\mathcal C^1`).**
For `\varphi\in\mathcal C^0(\Lambda_L;\mathfrak g)` and `b=(x,\mu)\in E(\Lambda_L)`,
\[
(d_0\varphi)_b := \varphi_{x+\hat e_\mu}-\varphi_x.
\]

**Definition A.5.4 (discrete coboundary `d_1:\mathcal C^1\to\mathcal C^2`).**
For `X\in\mathcal C^1(\Lambda_L;\mathfrak g)` and `p\in P(\Lambda_L)`,
\[
(d_1X)_p := \sum_{b\in E(\Lambda_L)} \sigma_{p,b}\,X_b.
\]

**Definition A.5.5 (adjoints `d_0^*`, `d_1^*`).**
Define `d_0^*:\mathcal C^1\to\mathcal C^0` and `d_1^*:\mathcal C^2\to\mathcal C^1` as Hilbert adjoints with respect to the `\ell^2` inner products:
\[
\langle d_0\varphi, X\rangle_{\mathcal C^1} = \langle \varphi, d_0^* X\rangle_{\mathcal C^0},
\qquad
\langle d_1X, F\rangle_{\mathcal C^2} = \langle X, d_1^* F\rangle_{\mathcal C^1}.
\]

**Definition A.5.6 (Hodge Laplacians and Maxwell operator).**
\[
\Delta_0 := d_0^*d_0,
\qquad
\Delta_1 := d_0d_0^* + d_1^*d_1,
\qquad
\Delta_2 := d_1 d_1^*,
\qquad
\mathsf M_1 := d_1^*d_1.
\]

---

## A.6 Wilson action and vacuum configuration

### A.6.1 Plaquette holonomy

**Definition A.6.1 (plaquette holonomy).**
For `U\in M_{\Lambda_L}` and `p=(x;\mu,\nu)\in P(\Lambda_L)` with `\mu<\nu`, define
\[
U_p(U) := U_{x,\mu}\,U_{x+\hat e_\mu,\nu}\,U_{x+\hat e_\nu,\mu}^{-1}\,U_{x,\nu}^{-1}\ \in G.
\]

### A.6.2 Wilson potential and action

**Definition A.6.2 (single-plaquette potential).**
For `\beta>0`, define
\[
\Phi_\beta(V) := \beta\Bigl(1-\frac{1}{n}\Re\mathrm{Tr}(V)\Bigr),
\qquad V\in G.
\]

**Definition A.6.3 (finite-volume Wilson action).**
For a finite periodic lattice `\Lambda_L` and `\beta>0`, define
\[
S_{\Lambda_L,\beta}(U) := \sum_{p\in P(\Lambda_L)} \Phi_\beta\big(U_p(U)\big),
\qquad U\in M_{\Lambda_L}.
\]

### A.6.3 Vacuum configuration

**Definition A.6.4 (vacuum configuration).**
The vacuum configuration is
\[
U^{(0)}\in M_{\Lambda_L},
\qquad
U^{(0)}_b := \mathbf 1 \ \text{for every }b\in E(\Lambda_L).
\]

**Definition A.6.5 (finite-volume Gibbs measure).**
Let `\mathrm{vol}_{g_{\Lambda_L}}` denote the Riemannian volume measure on `(M_{\Lambda_L},g_{\Lambda_L})`.
Define the Wilson Gibbs probability measure
\[
\mu_{\Lambda_L,\beta}(dU)
:= Z_{\Lambda_L,\beta}^{-1}\,e^{-S_{\Lambda_L,\beta}(U)}\,\mathrm{vol}_{g_{\Lambda_L}}(dU),
\]
where the partition function `Z_{\Lambda_L,\beta}` is the normalizing constant
\[
Z_{\Lambda_L,\beta}
:= \int_{M_{\Lambda_L}} e^{-S_{\Lambda_L,\beta}(U)}\,\mathrm{vol}_{g_{\Lambda_L}}(dU).
\]

**Definition A.6.6 (expectation and covariance).**
For an integrable function `F` on `M_{\Lambda_L}`, write
\[
\mathbb E_{\Lambda_L,\beta}[F] := \int F\,d\mu_{\Lambda_L,\beta}.
\]
For integrable `F,G`, define
\[
\mathrm{Cov}_{\Lambda_L,\beta}(F,G)
:= \mathbb E_{\Lambda_L,\beta}[FG] - \mathbb E_{\Lambda_L,\beta}[F]\ \mathbb E_{\Lambda_L,\beta}[G].
\]

**Definition A.6.7 (conditional Gibbs measure on an event).**
For an event `K\subset M_{\Lambda_L}` with `0<\mu_{\Lambda_L,\beta}(K)<1`, define the conditional probability measure
\[
\mu_{\Lambda_L,\beta}(\cdot\mid K) := \frac{\mu_{\Lambda_L,\beta}(\cdot\cap K)}{\mu_{\Lambda_L,\beta}(K)}.
\]

---

## A.7 Small-field radii and local Lie-theoretic Taylor constants

### A.7.1 Logarithm domain and BCH constants

**Definition A.7.1 (logarithm radius).**
Fix
\[
r_{\log} := \frac{\iota_G}{2}\in (0,\iota_G),
\]
so that the Riemannian exponential at `\mathbf 1` is a diffeomorphism on the open ball `{X\in\mathfrak g:|X|_{\mathfrak g}< r_{\log}}` and admits a smooth inverse `\log` on the group ball `B_{r_{\log}}^G(\mathbf 1)`.

**Lemma A.7.2 (uniform two-term BCH constants).**
There exist constants
\[
r_{\mathrm{BCH}}\in (0,r_{\log}],
\qquad
C_{\mathrm{BCH}}\in (0,\infty),
\]
depending only on `(G,g_G)`, such that for all `A,B\in\mathfrak g` with `|A|_{\mathfrak g},|B|_{\mathfrak g}\le r_{\mathrm{BCH}}`,
\[
\log\big(\exp(A)\exp(B)\big)
=
A+B+R(A,B),
\qquad
|R(A,B)|_{\mathfrak g}\le C_{\mathrm{BCH}}(|A|_{\mathfrak g}+|B|_{\mathfrak g})^2.
\]
*(Proof deferred; compactness + Taylor remainder in local coordinates.)*

### A.7.2 Trace-potential Taylor constants

**Lemma A.7.3 (trace-potential cubic Taylor constants at the identity).**
There exist constants
\[
r_{\mathrm{Tr}}\in (0,r_{\log}],
\qquad
C_{\mathrm{Tr}}\in (0,\infty),
\]
depending only on `(G,\rho,g_G)`, such that for all `Y\in\mathfrak g` with `|Y|_{\mathfrak g}\le r_{\mathrm{Tr}}`,
\[
\Phi_\beta(\exp Y)
=
\frac{\beta}{2n}\,|Y|_{\mathfrak g}^2 + \mathcal E_\beta(Y),
\qquad
|\mathcal E_\beta(Y)| \le C_{\mathrm{Tr}}\,\beta\,|Y|_{\mathfrak g}^3.
\]
*(Proof deferred; Taylor expansion of `\Re\mathrm{Tr}(\rho(\exp Y))` in `Y`.)*

### A.7.3 Canonical small-field radius

**Definition A.7.4 (canonical small-field radius).**
Define the small-field radius
\[
r_{\mathrm{sf}}
:= \min\Bigl\{\frac{r_{\log}}{4},\ \frac{r_{\mathrm{BCH}}}{4},\ \frac{r_{\mathrm{Tr}}}{4}\Bigr\}.
\]

---

## A.8 Haar/Jacobian “mass” constants

**Definition A.8.1 (Haar/Jacobian potential in exponential coordinates).**
Let `J_G:\mathfrak g\to (0,\infty)` denote the Jacobian density of the exponential map at the identity in normal coordinates, i.e. on `{X:|X|_{\mathfrak g}<r_{\log}}`,
\[
(\exp_G)^*(\mathrm{vol}_{g_G}) = J_G(X)\,dX.
\]
Define the Haar/Jacobian potential
\[
S_H(X) := -\log J_G(X).
\]

**Lemma A.8.2 (quadratic Hessian bound for the Haar potential at the origin).**
Under Assumption A.3.8, the Hessian of `S_H` at `0\in\mathfrak g` satisfies
\[
\nabla^2 S_H(0) \succeq \frac{\kappa_G}{3}\, \mathrm{Id}_{\mathfrak g}.
\]
*(Proof deferred; normal-coordinate expansion of `\sqrt{\det g_{ij}}`.)*

**Definition A.8.3 (Haar mass parameter).**
Define
\[
m_H^2 := \frac{\kappa_G}{3}.
\]
This is the canonical mass parameter extracted from Lemma A.8.2.

---

## A.9 Massive Maxwell operator constants and row-sum constants

### A.9.1 Maxwell coefficient and massive operator

**Definition A.9.1 (vacuum Wilson–Maxwell coefficient).**
Define
\[
\alpha_W := \frac{\beta}{n}.
\]
(With the metric normalization of Definition A.3.5, this is the coefficient appearing in the vacuum Hessian identity.)

**Definition A.9.2 (massive Maxwell operator on 1-cochains).**
Define the massive Maxwell operator on `\mathcal C^1(\Lambda_L;\mathfrak g)` by
\[
M_{\Lambda_L} := m_H^2\,\mathrm{Id} + \alpha_W\,\mathsf M_1
= m_H^2\,\mathrm{Id} + \alpha_W\, d_1^*d_1.
\]

### A.9.2 Row-sum constants for `d_1^*d_1`

**Definition A.9.3 (row-sum constant for `\mathsf M_1=d_1^*d_1`).**
Define
\[
C_0(\mathsf M_1)
:= \sup_{b\in E(\Lambda_L)}\ \sum_{\substack{\tilde b\in E(\Lambda_L)\\ \tilde b\neq b}}
\big|\big(\mathsf M_1\big)_{b\tilde b}\big|_{\mathrm{op}},
\]
where the block matrix is taken in the link index with fiber `\mathfrak g` and `|\cdot|_{\mathrm{op}}` is the operator norm on `\mathrm{End}(\mathfrak g)`.

**Definition A.9.4 (boundary row-sum constant for `\mathsf M_1`).**
For each `b'\in E(\Lambda_L)` define the 1-Lipschitz weight `\phi_{b'}(b):=\mathrm{dist}_E(b,b')`.
Define
\[
C_\partial(\mathsf M_1)
:= \sup_{b'\in E(\Lambda_L)}\ \sup_{b\in E(\Lambda_L)}\
\sum_{\substack{\tilde b\in E(\Lambda_L)\setminus\{b\}\\
|\phi_{b'}(b)-\phi_{b'}(\tilde b)|=1}}
\big|\big(\mathsf M_1\big)_{b\tilde b}\big|_{\mathrm{op}}.
\]
By definition, `C_\partial(\mathsf M_1)\le C_0(\mathsf M_1)`.

**Proposition A.9.5 (dimension-only bound on `C_0(\mathsf M_1)` via `D_E`).**
\[
C_0(\mathsf M_1) \le D_E.
\]
*(Proof deferred; `\mathsf M_1` has range one in the link graph and unit-size incidence coefficients.)*

---

## A.10 Combes–Thomas decay constants (abstract form)

**Definition A.10.1 (abstract Combes–Thomas parameters).**
Let `V` be a finite set with a graph distance `\mathrm{dist}` and let `A` be a self-adjoint operator on `\ell^2(V;\mathfrak g)` with block matrix entries `(A_{xy})_{x,y\in V}`.
Define:
- positivity constant `a_0(A)` as the largest `a_0>0` such that `A\succeq a_0 I`;
- range `R(A)` as the smallest integer `R\ge 0` such that `A_{xy}=0` whenever `\mathrm{dist}(x,y)>R`;
- row-sum constant
  \[
  B_0(A) := \sup_{x\in V}\sum_{\substack{y\in V\\y\neq x}} |A_{xy}|_{\mathrm{op}}.
  \]

**Definition A.10.2 (Combes–Thomas decay rate).**
For an operator `A` satisfying `a_0(A)>0` and `B_0(A)<\infty`, define the Combes–Thomas decay rate
\[
\eta_{\mathrm{CT}}(A)
:=
\frac{1}{R(A)}\log\Bigl(1+\frac{a_0(A)}{2B_0(A)}\Bigr)
\quad\text{when }R(A)\ge 1,
\]
and `\eta_{\mathrm{CT}}(A):=+\infty` when `R(A)=0`.

---

## A.11 Typicality / good-set constants (placeholders)

**Assumption A.11.1 (good-set event family).**
For each finite periodic lattice `\Lambda_L`, a measurable event `K_{\Lambda_L}\subset M_{\Lambda_L}` is specified.
(Used as a localization device for conditional inequalities; the construction and verification are not contained in Appendix A.)

**Assumption A.11.2 (typicality exponent).**
There exists a constant `c_{\mathrm{typ}}>0` such that for all sufficiently large volumes,
\[
\mu_{\Lambda_L,\beta}\big(K_{\Lambda_L}^c\big) \le \exp\big(-c_{\mathrm{typ}}\,|P(\Lambda_L)|\big).
\]
This is the sole “volume-scale typicality” input used to convert conditional clustering bounds into unconditional clustering bounds.

---

## A.12 Symbol index

**Definition A.12.1 (symbol index; convenience only).** The list below is a navigation aid; the authoritative introductions are the numbered items in this Appendix A.

- `d` — dimension (Definition A.1.1)
- `a` — lattice spacing / cutoff (Definition A.1.2)
- `\Lambda_L` — finite periodic lattice (Definition A.1.3)
- `E(\Lambda_L),P(\Lambda_L)` — links, plaquettes (Definitions A.2.2–A.2.3)
- `\sigma_{p,b}` — incidence coefficients (Definition A.2.4)
- `m_\partial,\nu_P,D_E` — combinatorial constants (Definitions A.2.5–A.2.11)
- `G,\mathfrak g,\rho,n` — group/representation data (Assumptions A.3.1, A.3.3)
- `\langle\cdot,\cdot\rangle_{\mathfrak g},g_G` — metric data (Definitions A.3.5–A.3.6)
- `\iota_G,\kappa_G,m_H^2` — geometric/mass constants (Definition A.3.7, Assumption A.3.8, Definition A.8.3)
- `M_{\Lambda_L}` — configuration manifold and metric (Definitions A.4.1–A.4.2)
- `d_0,d_1,d_0^*,d_1^*` — cochain operators (Definitions A.5.3–A.5.5)
- `\Phi_\beta,S_{\Lambda_L,\beta}` — Wilson potential/action (Definitions A.6.2–A.6.3)
- `\mu_{\Lambda_L,\beta},Z_{\Lambda_L,\beta}` — Gibbs measure and partition function (Definition A.6.5)
- `\mathbb E_{\Lambda_L,\beta},\mathrm{Cov}_{\Lambda_L,\beta}` — expectation and covariance (Definition A.6.6)
- `\mu_{\Lambda_L,\beta}(\cdot\mid K)` — conditional measure (Definition A.6.7)
- `r_{\log},r_{\mathrm{BCH}},r_{\mathrm{Tr}},r_{\mathrm{sf}}` — small-field radii (Definitions/Lemmas A.7.1–A.7.4)
- `\alpha_W` — Maxwell coefficient (Definition A.9.1)
- `C_0(\mathsf M_1),C_\partial(\mathsf M_1)` — row-sum constants (Definitions A.9.3–A.9.4)
- `\eta_{\mathrm{CT}}(A)` — Combes–Thomas decay rate (Definition A.10.2)
- `c_{\mathrm{typ}}` — typicality exponent (Assumption A.11.2)

