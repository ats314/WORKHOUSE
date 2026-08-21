---
file: Core_3__OS_Framework_at_Fixed_Cutoff.md
status: DRAFT
depends_on:
  - Appendix_A__Notation_and_Constants.md
  - Core_2__Configuration_Geometry_and_Differential_Calculus.md
  - Appendix_K__Reflection_Positivity_for_Wilson.md
  - Appendix_L__OS_Reconstruction_and_Gap_Extraction.md
  - Appendix_N__External_Inputs_Ledger.md
feeds_into:
  - Core-9 (Thermodynamic limit and OS Hamiltonian gap at fixed cutoff)
  - Core-10 (Conditional continuum extension: OS gap permanence interfaces)
---

# Core-3 — OS framework at fixed cutoff

## Core-3.0 Interface

**Definition (Core-3.0.1: scope).**  
Fix `d=4` (Definition **A.1.1**) and a finite periodic lattice `\Lambda_L` (Definition **A.1.3**) at fixed cutoff `a>0` (Definition **A.1.2**).  
This file records the Osterwalder–Schrader (OS) structures and identities that later enable a conversion of *Euclidean time decay* into an *OS Hamiltonian spectral-gap* statement.

**Definition (Core-3.0.2: imported primitives).**  
The following items are used without redefinition:

- Cylinder algebras `\mathcal A(A)` and link support `\mathrm{supp}_E(\cdot)`: Definitions **Core-2.1.2–Core-2.1.4**.
- Wilson Gibbs measure `\mu_{\Lambda_L,\beta}`: Definition **A.6.5**.
- Reflection datum `(\Theta,\theta,\mathcal A_+)` for the lattice Wilson system: Definitions **K.1.10**, **K.1.16**, **K.1.15**.
- Abstract OS framework, OS Hilbert space `\mathcal H_{\mathrm{OS}}`, and transfer operator `T`: Appendix **L**, in particular Assumption **L.1.7** and External Input **L.2.6**.
- External-input registry discipline: Appendix **N**, Definitions **N.0.1–N.0.3**.

**Definition (Core-3.0.3: outputs of this file).**  
This file introduces (and later files may cite only) the following items:

1. lattice translations `\tau_y^\Omega` on `M_{\Lambda_L}` and induced pullbacks on observables (Definitions **Core-3.1.1–Core-3.1.2**);
2. translation invariance of the finite-volume Wilson measure (Proposition **Core-3.1.6**);
3. reflection covariance of lattice translations (Lemma **Core-3.1.7**);
4. reflection positivity for the finite-volume Wilson measure stated as a Core-level proposition with proof in Appendix **K** (Proposition **Core-3.2.1**);
5. the sole OS reconstruction dependency explicitly identified as an external input (External Input **Core-3.3.1**);
6. a centered covariance-to-matrix-element identity (Proposition **Core-3.4.1**) used downstream to connect Euclidean time decay bounds to transfer-operator matrix elements.

**Definition (Core-3.0.4: constants).**  
This file introduces no new named constants. Any constants (including `a`, `\beta`, and group/lattice parameters) are referenced from Appendix **A**.

---

## Core-3.1 Translations and symmetry identities at finite volume

### Core-3.1.1 Translations on the configuration space

**Definition (Core-3.1.1: vertex and link translations on `\Lambda_L`).**  
For `y\in\Lambda_L`, define the vertex translation map
\[
\mathsf t_y:V(\Lambda_L)\to V(\Lambda_L),\qquad \mathsf t_y(x):=x+y,
\]
with addition in the torus `\Lambda_L`.  
For positively oriented links `b=(x,\mu)\in E(\Lambda_L)` (Definition **A.2.2**), define the induced link translation
\[
\mathsf t_y(b):=(x+y,\mu)\in E(\Lambda_L).
\]
For plaquettes `p=(x;\mu,\nu)\in P(\Lambda_L)` (Definition **A.2.3**), define
\[
\mathsf t_y(p):=(x+y;\mu,\nu)\in P(\Lambda_L).
\]

**Definition (Core-3.1.2: induced translation action on configurations and observables).**  
Let `M_{\Lambda_L}:=G^{E(\Lambda_L)}` (Definition **A.4.1**). Define the translation action on configurations
\[
\tau_y^\Omega:M_{\Lambda_L}\to M_{\Lambda_L},\qquad (\tau_y^\Omega U)_b := U_{\mathsf t_{-y}(b)}\quad (b\in E(\Lambda_L)).
\]
Define the induced pullback on observables `F:M_{\Lambda_L}\to\mathbb C` by
\[
(\tau_y F)(U):=F\big((\tau_{-y}^\Omega U)\big).
\]

**Lemma (Core-3.1.3: group property).**  
The maps `\{\tau_y^\Omega\}_{y\in\Lambda_L}` form an action of the additive group `\Lambda_L`:
\[
\tau_0^\Omega=\mathrm{Id},\qquad \tau_{y_1}^\Omega\circ\tau_{y_2}^\Omega=\tau_{y_1+y_2}^\Omega.
\]
Consequently, `\{\tau_y\}` is a `*`-algebra automorphism group on bounded observables under pointwise multiplication and complex conjugation.

*Proof.* Fix `U\in M_{\Lambda_L}` and `b\in E(\Lambda_L)`. Then
\[
\big((\tau_{y_1}^\Omega\circ\tau_{y_2}^\Omega)U\big)_b
=(\tau_{y_2}^\Omega U)_{\mathsf t_{-y_1}(b)}
=U_{\mathsf t_{-y_2}(\mathsf t_{-y_1}(b))}
=U_{\mathsf t_{-(y_1+y_2)}(b)}
=\big(\tau_{y_1+y_2}^\Omega U\big)_b.
\]
The statement for observables follows because `\tau_y` is defined by pullback along `\tau_y^\Omega`, hence preserves products and conjugation. ∎

### Core-3.1.2 Translation invariance of the Wilson measure

**Lemma (Core-3.1.4: translation invariance of product Haar).**  
Let `dU` be the product Haar probability measure on `M_{\Lambda_L}` (Definition **K.2.1**). Then for any bounded measurable `F`,
\[
\int F(\tau_y^\Omega U)\,dU=\int F(U)\,dU\qquad(y\in\Lambda_L).
\]

*Proof.* The map `\tau_y^\Omega` permutes the link coordinates: it is the coordinate relabeling `U_b\mapsto U_{\mathsf t_{-y}(b)}`. Since `dU` is the product of identical Haar factors over `b\in E(\Lambda_L)`, it is invariant under such coordinate permutations. ∎

**Lemma (Core-3.1.5: translation covariance of plaquette holonomy).**  
Let `U_p(U)` be the plaquette holonomy (Definition **A.6.1**). Then for all `y\in\Lambda_L`, all plaquettes `p\in P(\Lambda_L)`, and all configurations `U\in M_{\Lambda_L}`,
\[
U_p(\tau_y^\Omega U)=U_{\mathsf t_{-y}(p)}(U).
\]

*Proof.* Write `p=(x;\mu,\nu)` with `\mu<\nu`. By Definition **A.6.1**,
\[
U_p(U)=U_{x,\mu}\,U_{x+\hat e_\mu,\nu}\,U_{x+\hat e_\nu,\mu}^{-1}\,U_{x,\nu}^{-1}.
\]
By Definition **Core-3.1.2**,
\[
(\tau_y^\Omega U)_{x,\mu}=U_{x-y,\mu},\quad (\tau_y^\Omega U)_{x+\hat e_\mu,\nu}=U_{x+\hat e_\mu-y,\nu},\quad (\tau_y^\Omega U)_{x+\hat e_\nu,\mu}=U_{x+\hat e_\nu-y,\mu},\quad (\tau_y^\Omega U)_{x,\nu}=U_{x-y,\nu}.
\]
Substituting into the product defining `U_p(\tau_y^\Omega U)` yields the holonomy of the translated plaquette `\mathsf t_{-y}(p)=(x-y;\mu,\nu)` evaluated at `U`. ∎

**Proposition (Core-3.1.6: translation invariance of the Wilson action and Gibbs measure).**  
Let `S_{\Lambda_L,\beta}` and `\mu_{\Lambda_L,\beta}` be the Wilson action and Gibbs measure (Definitions **A.6.3** and **A.6.5**). Then:

1. (**Action invariance**) For all `y\in\Lambda_L` and `U\in M_{\Lambda_L}`,
   \[
   S_{\Lambda_L,\beta}(\tau_y^\Omega U)=S_{\Lambda_L,\beta}(U).
   \]
2. (**Measure invariance**) For all bounded measurable `F` and all `y\in\Lambda_L`,
   \[
   \mathbb E_{\Lambda_L,\beta}[\tau_y F]=\mathbb E_{\Lambda_L,\beta}[F].
   \]

*Proof.*

1. By Definition **A.6.3**,
   \[
   S_{\Lambda_L,\beta}(U)=\sum_{p\in P(\Lambda_L)} \Phi_\beta\big(U_p(U)\big).
   \]
   Using Lemma **Core-3.1.5** and the fact that `p\mapsto \mathsf t_{-y}(p)` is a bijection of `P(\Lambda_L)`,
   \[
   S_{\Lambda_L,\beta}(\tau_y^\Omega U)
   =\sum_{p\in P(\Lambda_L)} \Phi_\beta\big(U_p(\tau_y^\Omega U)\big)
   =\sum_{p\in P(\Lambda_L)} \Phi_\beta\big(U_{\mathsf t_{-y}(p)}(U)\big)
   =\sum_{q\in P(\Lambda_L)} \Phi_\beta\big(U_q(U)\big)
   =S_{\Lambda_L,\beta}(U).
   \]

2. Use the Haar form of the Gibbs measure from Lemma **K.2.2**:
   \[
   \mu_{\Lambda_L,\beta}(dU)=Z^{-1} e^{-S_{\Lambda_L,\beta}(U)}\,dU.
   \]
   By (1), `e^{-S_{\Lambda_L,\beta}(\tau_y^\Omega U)}=e^{-S_{\Lambda_L,\beta}(U)}` and by Lemma **Core-3.1.4**, `dU` is invariant under `\tau_y^\Omega`. Therefore `\mu_{\Lambda_L,\beta}` is invariant under `\tau_y^\Omega` and the expectation identity follows from the definition of `\tau_y` as pullback. ∎

### Core-3.1.3 Reflection covariance of translations

**Lemma (Core-3.1.7: reflection conjugates time translations).**  
Assume the OS reflection datum from Appendix **K**, §K.1, in particular the vertex reflection `\vartheta` (Definition **K.1.2**) and the induced configuration reflection `\Theta` (Definition **K.1.10**).

Let `y=(y_0,\vec y)\in\Lambda_L`. Define the reflected translation vector
\[
\vartheta_*(y):=(-y_0,\vec y)\in\Lambda_L.
\]
Then the configuration maps satisfy
\[
\Theta\circ\tau_y^\Omega = \tau_{\vartheta_*(y)}^\Omega\circ\Theta.
\]
In particular, for pure time translations `y=n\hat e_0`, one has
\[
\Theta\circ\tau_{n\hat e_0}^\Omega = \tau_{-n\hat e_0}^\Omega\circ\Theta.
\]

*Proof.* It suffices to check the identity on each link coordinate. Fix `b=(x,\mu)\in E(\Lambda_L)`.

By Definition **K.1.10**, `(\Theta U)_b=U_{\vartheta b}` using the directed-link extension convention (Definition **K.1.7**). By Definition **Core-3.1.2**,
\[
\big((\Theta\circ\tau_y^\Omega)U\big)_b
=(\tau_y^\Omega U)_{\vartheta b}
=U_{\mathsf t_{-y}(\vartheta b)}.
\]
On the other hand,
\[
\big((\tau_{\vartheta_*(y)}^\Omega\circ\Theta)U\big)_b
=(\Theta U)_{\mathsf t_{-\vartheta_*(y)}(b)}
=U_{\vartheta(\mathsf t_{-\vartheta_*(y)}(b))}.
\]
Thus it remains to show equality of directed links:
\[
\mathsf t_{-y}(\vartheta b)=\vartheta(\mathsf t_{-\vartheta_*(y)}(b)).
\]
This follows from the corresponding vertex identity `\mathsf t_{-y}(\vartheta x)=\vartheta(\mathsf t_{-\vartheta_*(y)}x)` for all vertices `x`, which is a direct computation from Definition **K.1.2**:
\[
\vartheta(x_0,\vec x)=(1-x_0,\vec x),\qquad \mathsf t_{-y}(x_0,\vec x)=(x_0-y_0,\vec x-\vec y).
\]
Applying these formulas gives
\[
\mathsf t_{-y}(\vartheta(x_0,\vec x))=(1-x_0-y_0,\vec x-\vec y)
=\vartheta(x_0+y_0,\vec x-\vec y)
=\vartheta(\mathsf t_{-\vartheta_*(y)}(x_0,\vec x)),
\]
since `-\vartheta_*(y)=(y_0,-\vec y)`. This proves the desired conjugacy relation on links and hence on configurations. ∎

---

## Core-3.2 Reflection positivity input

**Proposition (Core-3.2.1: finite-volume reflection positivity for the Wilson measure).**  
Assume the temporal side length `L_0` is even (Assumption **K.1.1**). Let `\mu_{\Lambda_L,\beta}` be the Wilson Gibbs measure (Definition **A.6.5**), and let `(\Theta,\theta,\mathcal A_+)` be the OS reflection datum and positive-time algebra from Appendix **K**, §K.1 (Definitions **K.1.10**, **K.1.16**, **K.1.15**). Then
\[
\mathbb E_{\Lambda_L,\beta}\big[(\theta F)\,F\big]\ge 0
\qquad\text{for all }F\in\mathcal A_+.
\]

*Proof.* This is exactly Theorem **K.5.1**. ∎

---

## Core-3.3 OS reconstruction: explicit external dependency

**External Input (Core-3.3.1: OS reconstruction theorem in the invoked form).**  
This manuscript set invokes **External Input L.2.6** (Appendix **L**) in the exact form recorded there (and listed in the external-input registry, Definition **N.0.3**).

Downstream files may cite OS reconstruction **only** via the label “External Input **L.2.6**” (Appendix **N**, Definition **N.2.2**).

---

## Core-3.4 Euclidean-to-operator dictionary: centered covariance as a transfer matrix element

**Proposition (Core-3.4.1: centered cross-covariance as an OS matrix element).**  
Let `\mu` be a probability measure on a measurable space `\Omega`, equipped with:
- a reflection `\Theta` and OS involution `\theta` (Definitions **L.1.4–L.1.5**),
- time translations `\{\tau_n\}_{n\in\mathbb Z}` (Definition **L.1.3**),
- a positive-time algebra `\mathcal A_+` (Definition **L.1.6**),

such that Assumption **L.1.7** holds.

Let `T` and `\mathcal H_{\mathrm{OS}}` be given by External Input **L.2.6**. For `F,G\in\mathcal A_+`, let `F^\circ` and `G^\circ` denote the centered observables (Definition **L.4.1**). Then for every integer `n\ge 0`,
\[
\big\langle [F^\circ],\,T^n[G^\circ]\big\rangle_{\mathrm{OS}}
=\mathrm{Cov}_\mu\big(\theta F,\,\tau_n G\big).
\]

*Proof.* By External Input **L.2.6** (transfer identity) applied to `F^\circ,G^\circ\in\mathcal A_+`,
\[
\big\langle [F^\circ],\,T^n[G^\circ]\big\rangle_{\mathrm{OS}}=\mu\big((\theta F^\circ)\,(\tau_n G^\circ)\big).
\]
Using centering (Definition **L.4.1**),
\[
F^\circ=F-\mu(F),\qquad G^\circ=G-\mu(G).
\]
By reflection invariance and time-translation invariance in Assumption **L.1.7(1)–(2)**,
\[
\mu(\theta F)=\overline{\mu(F)},\qquad \mu(\tau_n G)=\mu(G).
\]
Since `\theta` is antilinear and satisfies `\theta(1)=1`, one has `\theta(\mu(F))=\overline{\mu(F)}` and hence
\[
\theta F^\circ=\theta F-\mu(\theta F).
\]
Similarly, `\tau_n G^\circ=\tau_n G-\mu(\tau_n G)`. Therefore,
\[
\mu\big((\theta F^\circ)(\tau_n G^\circ)\big)
=\mu\big((\theta F)(\tau_n G)\big)-\mu(\theta F)\,\mu(\tau_n G)
=\mathrm{Cov}_\mu(\theta F,\tau_n G),
\]
which is the claim. ∎

---

## Core-3.5 Dependency notes (non-normative)

**Definition (Core-3.5.1: permitted downstream citations).**  
Downstream files may cite this file only for:

- Definitions **Core-3.1.1–Core-3.1.2** and Lemma **Core-3.1.3** (translation action on configurations and observables);
- Proposition **Core-3.1.6** (translation invariance of `\mu_{\Lambda_L,\beta}`);
- Lemma **Core-3.1.7** (reflection covariance of translations);
- Proposition **Core-3.2.1** (reflection positivity statement; proof in Appendix **K**);
- External Input **Core-3.3.1** (alias for External Input **L.2.6**);
- Proposition **Core-3.4.1** (centered covariance as a transfer-operator matrix element).

Any later use of OS reconstruction must cite **External Input L.2.6** (Appendix **N**, Definition **N.2.2**) rather than restating it.
