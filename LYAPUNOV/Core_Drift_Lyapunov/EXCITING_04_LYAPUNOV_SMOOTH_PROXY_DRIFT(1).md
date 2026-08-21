# Exciting Extract 04: A smooth plaquette proxy + Lyapunov drift bookkeeping that stays uniform in volume

This note extracts a key *technical* innovation in the globalization strategy:

> Use a **globally smooth conjugation-invariant plaquette proxy** \(\widetilde z(U_p)\), and choose an outer profile \(\Phi\) with \(\Phi'(0)=0\), so that all potentially dangerous second-order diffusion terms are automatically weighted by “badness” and do **not** leak a factor \(|P(\Lambda)|\).

The result is a clean, referee-auditable separation:

- all diffusion-generated terms \(\Delta\) and \(\Gamma\) are controlled by \(\sum_p \widetilde z_p\) with constants independent of \(|\Lambda|\);
- the only remaining obstruction is a *single* coercive inequality involving \(\langle \nabla S,\nabla \widetilde z_p\rangle\).

---

## 1. Setup: generator and Lyapunov candidate

On the configuration manifold \(M_\Lambda=G^{E(\Lambda)}\) with product metric \(g_\Lambda\), let
\[
L_\Lambda f := \Delta_\Lambda f - \langle \nabla S_\Lambda,\nabla f\rangle_{g_\Lambda}
\]
be the reversible generator for the Gibbs measure
\[
d\mu_\Lambda = Z_\Lambda^{-1}e^{-S_\Lambda}\,d\mathrm{vol}_{g_\Lambda}.
\]
Write
\[
\Gamma_\Lambda(f,g):=\langle \nabla f,\nabla g\rangle,\qquad \Gamma_\Lambda(f):=\Gamma_\Lambda(f,f).
\]

We work with the **trace-defect plaquette proxy**
\[
\widetilde z(g):=1-\frac1n\Re\mathrm{Tr}(\rho(g)),\qquad g\in G,
\]
and lift it to plaquettes:
\[
\widetilde z_p(U):=\widetilde z\big(U_p(U)\big),\qquad p\in P(\Lambda).
\]
This proxy is smooth, conjugation-invariant, and satisfies
\[
0\le \widetilde z \le 2,\qquad \widetilde z(g)=0\ \Longleftrightarrow\ g=\mathbf 1.
\]

Define the extensive “badness”
\[
\mathcal D_\Lambda(U):=\sum_{p\in P(\Lambda)}\widetilde z_p(U).
\tag{1.1}
\]

### 1.1 The Lyapunov functional

Choose an outer profile \(\Phi\) and set
\[
V_\Lambda(U):=\sum_{p\in P(\Lambda)}\Phi(\widetilde z_p(U)),\qquad
W_\Lambda(U):=\exp(\kappa V_\Lambda(U)).
\]
The canonical choice used in the manuscript is
\[
\Phi(s)=s^2,\qquad \Phi'(s)=2s,\qquad \Phi''(s)=2,
\]
not because it is sacred, but because \(\Phi'(0)=0\) kills the main volume-leak.

---

## 2. Global \(C^2\) bounds and the gradient domination trick

Because \(G\) is compact and \(\widetilde z\in C^\infty(G)\), there exist finite constants
\[
\sup_{g\in G}|\nabla_G\widetilde z(g)| \le C^{(1)}_{\widetilde z},\qquad
\sup_{g\in G}\|\nabla_G^2\widetilde z(g)\|_{\mathrm{op}} \le C^{(2)}_{\widetilde z}.
\tag{2.1}
\]

The genuinely useful inequality is the **weighted gradient domination**
\[
|\nabla_G\widetilde z(g)|^2 \le C_\nabla\,\widetilde z(g)\qquad\forall g\in G,
\tag{2.2}
\]
where one can take
\[
C_\nabla := \sup_{g\neq \mathbf 1}\frac{|\nabla_G\widetilde z(g)|^2}{\widetilde z(g)} <\infty.
\tag{2.3}
\]
Finiteness follows because near \(\mathbf 1\) the ratio has a finite Taylor limit:
\(\widetilde z(\exp Y)\sim c|Y|^2\) and \(\nabla\widetilde z(\exp Y)\sim c'Y\).

---

## 3. Lifting bounds to plaquettes: locality + isometries

Fix a plaquette \(p\) with four boundary links. Varying a single boundary link while holding the others fixed changes \(U_p\) by left/right multiplication and possibly inversion:
\[
g\mapsto A g^\sigma B,\qquad \sigma\in\{\pm 1\}.
\]
Because the metric on \(G\) is bi-invariant, these maps are **isometries**. Therefore the group bounds transfer to each \(\widetilde z_p\) with the same constants.

Crucially: \(\widetilde z_p\) depends on **only four links**, so every bound is local.

As a typical example, for a fixed link \(\ell\),
\[
|\nabla_\ell \widetilde z_p(U)|^2 \le C_\nabla\,\widetilde z_p(U)\,\mathbf 1_{\{\ell\in\partial p\}}.
\tag{3.1}
\]
Summing over \(\ell\) yields
\[
\Gamma_\Lambda(\widetilde z_p)(U)\le 4C_\nabla\,\widetilde z_p(U),
\tag{3.2}
\]
since \(|\partial p|=4\).

---

## 4. Drift computation: exact identity and uniform closure

Two diffusion identities (chain rules) drive the calculation:

**Lemma 4.1 (diffusion chain rule).**  
For \(\Psi\in C^2(\mathbb R)\) and smooth \(f\),
\[
L_\Lambda(\Psi\circ f) = \Psi'(f)\,L_\Lambda f + \Psi''(f)\,\Gamma_\Lambda(f).
\tag{4.1}
\]

**Lemma 4.2 (exponential chain rule).**
\[
\frac{L_\Lambda(e^{\kappa V})}{e^{\kappa V}}
=
\kappa\,L_\Lambda V + \kappa^2\,\Gamma_\Lambda(V).
\tag{4.2}
\]

### 4.1 Exact drift identity for \(\Phi(s)=s^2\)

With \(V_\Lambda=\sum_p \widetilde z_p^2\),
\[
L_\Lambda V_\Lambda
=
2\sum_p \widetilde z_p\,\Delta_\Lambda \widetilde z_p
\;-\;
2\sum_p \widetilde z_p\,\langle \nabla S_\Lambda,\nabla \widetilde z_p\rangle
\;+\;
2\sum_p \Gamma_\Lambda(\widetilde z_p).
\tag{4.3}
\]
Then
\[
\frac{L_\Lambda W_\Lambda}{W_\Lambda}
=
\kappa\,L_\Lambda V_\Lambda + \kappa^2\,\Gamma_\Lambda(V_\Lambda).
\tag{4.4}
\]

### 4.2 Uniform-constant closure of diffusion terms

Using (3.2) and the bounded overlap constant \(\nu\) (each link is in at most \(\nu\) plaquettes), one proves:

**Proposition 4.3 (diffusion-generated terms are controlled by \(\mathcal D_\Lambda\)).**  
There exist constants \(A_1,A_2,A_3<\infty\), depending only on \((G,\rho)\) and \(\nu\) (not on \(|\Lambda|\)), such that
\[
\Big|\sum_p \Phi'(\widetilde z_p)\,\Delta_\Lambda \widetilde z_p\Big|\le A_1\,\mathcal D_\Lambda,
\qquad
\sum_p \Phi''(\widetilde z_p)\,\Gamma_\Lambda(\widetilde z_p)\le A_2\,\mathcal D_\Lambda,
\qquad
\Gamma_\Lambda(V_\Lambda)\le A_3\,\mathcal D_\Lambda.
\tag{4.5}
\]
For \(\Phi(s)=s^2\), one may take (as in the main text)
\[
A_1=8C_\Delta,\qquad
A_2=8C_\nabla,\qquad
A_3=64\,\nu\,C_\nabla,
\tag{4.6}
\]
where \(C_\Delta:=\sup_{g\in G}|\Delta_G\widetilde z(g)|\).

### 4.3 The clean drift inequality with one open input

Combining (4.3)–(4.6) gives the volume-uniform bound
\[
\frac{L_\Lambda W_\Lambda}{W_\Lambda}(U)
\;\le\;
(\kappa C_V+\kappa^2 C_\Gamma)\,\mathcal D_\Lambda(U)
\;-\;
2\kappa\sum_{p}\widetilde z_p(U)\,\langle \nabla S_\Lambda(U),\nabla \widetilde z_p(U)\rangle,
\tag{4.7}
\]
with \(C_V=A_1+A_2\), \(C_\Gamma=A_3\).

Everything on the right is now uniform in \(|\Lambda|\) **except** the pairing term
\[
\mathcal P_\Lambda(U):=
\sum_{p}\widetilde z_p(U)\,\langle \nabla S_\Lambda(U),\nabla \widetilde z_p(U)\rangle.
\tag{4.8}
\]

---

## 5. The isolated coercive pairing input (open)

A natural target inequality is:

> There exist constants \(c_{\mathrm{pair}}>0\), \(C_{\mathrm{pair}}\ge0\), independent of \(\Lambda\), such that  
> \[
> \mathcal P_\Lambda(U)\ \ge\ c_{\mathrm{pair}}\mathcal D_\Lambda(U)-C_{\mathrm{pair}}
> \qquad\forall U.
> \tag{5.1}
> \]

If (5.1) holds, then (4.7) becomes a Foster–Lyapunov drift bound for a suitable \(\kappa>0\), yielding a set \(K_\Lambda\) into which the dynamics drifts.

This is precisely where the *specific structure* of the lattice action enters, and it is the major open analytic input flagged in the project’s dependency ledger.

---

## 6. Local-to-global Poincaré patching (functional-analytic plumbing)

Assume:

1. A **local Poincaré inequality** on a measurable core set \(K_\Lambda\):
\[
\int_{K_\Lambda}\bigl(f-\mu_{\Lambda,K}(f)\bigr)^2\,d\mu_\Lambda
\le \kappa_K\int \Gamma_\Lambda(f)\,d\mu_\Lambda.
\tag{6.1}
\]
2. A **Lyapunov drift inequality**:
\[
L_\Lambda W_\Lambda \le -\lambda W_\Lambda + b\,\mathbf 1_{K_\Lambda},
\qquad W_\Lambda\ge 1.
\tag{6.2}
\]

Then one can prove (by a standard Lyapunov–\(\Gamma\) inequality and variance decomposition):

**Theorem 6.1 (local-to-global Poincaré).**  
\[
\mathrm{Var}_{\mu_\Lambda}(f)
\le \frac{1+b\kappa_K}{\lambda}\int \Gamma_\Lambda(f)\,d\mu_\Lambda.
\tag{6.3}
\]
In particular, the spectral gap of \(-L_\Lambda\) is at least \(\lambda/(1+b\kappa_K)\).

The conceptual payoff: once (6.1) and (6.2) are volume-uniform, the global Poincaré constant is volume-uniform.

---

## 7. What could be developed further

There are two promising directions:

1. **Proving the pairing coercivity (5.1).**  
This is the real “physics geometry” bottleneck: it should encode how plaquette-level convexity controls link gradients through discrete geometric inequalities. Variants may involve:
- strict convexity of \(\Phi_\beta\) on a neighborhood,
- coercivity of a discrete gauge-covariant Laplacian,
- or a replacement localization strategy (capacity/drift) that avoids needing (5.1) pointwise.

2. **Sharper proxy/functional choices.**  
One can consider other \(\Phi\) (e.g. truncated quadratic or smooth convex growth) to optimize constants and typicality, while keeping \(\Phi'(0)=0\) to prevent volume leakage.

The “smooth proxy + \(\Phi'(0)=0\)” trick is general and may be reusable well beyond Wilson gauge theory.
