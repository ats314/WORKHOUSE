# PRO12 Notes 02 — The Horizontal Projector Skeleton (and how to compute it)

## 1. Gauge action and vertical directions
On a lattice Λ, link variables are

- sites: V(Λ)
- oriented edges/links: E(Λ)
- group: G = SU(2) or SU(3)
- configuration manifold: M_Λ = G^{E(Λ)}

A gauge transformation g = (g_x)_{x∈V(Λ)} acts on a link (x,μ) by

U_{x,μ} ↦ g_x · U_{x,μ} · g_{x+μ}^{-1}.

An infinitesimal gauge parameter X = (X_x) with X_x ∈ 𝔤 gives a **vertical vector** (tangent to the gauge orbit):

(X^♯(U))_{x,μ} = X_x U_{x,μ} - U_{x,μ} X_{x+μ}.

This formula is one of the most important “structural primitives” in the whole project.

---

## 2. Right-invariant coordinates and the covariant difference operator
Using right-invariant identification on each link:

T_{U_{x,μ}}G ≅ 𝔤 via  W_{x,μ} := δU_{x,μ} U_{x,μ}^{-1}.

In these coordinates, the vertical direction becomes a **covariant difference**:

δU_{x,μ} U_{x,μ}^{-1}
= X_x - Ad_{U_{x,μ}}(X_{x+μ}).

Define D_U (a lattice covariant derivative along links) by

(D_U φ)_{x,μ} := φ_x - Ad_{U_{x,μ}}(φ_{x+μ}),

for site-fields φ : V(Λ) → 𝔤.

Then: vertical directions = im(D_U).

---

## 3. Inner products and the adjoint D_U^*
Equip 𝔤 with the bi-invariant inner product ⟨A,B⟩ := -Tr(A B) (anti-Hermitian convention).
Then link-fields W have inner product

⟨W,W'⟩_1 := Σ_{(x,μ)∈E(Λ)} ⟨W_{x,μ}, W'_{x,μ}⟩.

The adjoint D_U^* is defined by

⟨W, D_U φ⟩_1 = ⟨D_U^* W, φ⟩_0.

A direct (index-shift + Ad-invariance) calculation gives the standard lattice formula

(D_U^* W)_x = Σ_μ ( W_{x,μ} - Ad_{U_{x-μ,μ}}^{-1}(W_{x-μ,μ}) ).

So horizontality is literally “covariant divergence-free”.

---

## 4. The horizontal projector
Define

- vertical subspace V_U := im(D_U)
- horizontal subspace H_U := V_U^⊥

Then the orthogonal projector onto horizontals is

P_U = I - D_U · (D_U^* D_U)^{-1} · D_U^*.

Here M_U := D_U^* D_U is the **Faddeev–Popov (FP) operator**.
On a periodic lattice, M_U has a small nullspace from global gauge symmetry; numerically you fix this by imposing mean-zero on site fields (Σ_x φ_x = 0).

### Linearized limit (cheap check)
At U = identity, Ad_{U} = I, so

(D φ)_{x,μ} = φ_x - φ_{x+μ},
(D^* W)_x = Σ_μ (W_{x,μ} - W_{x-μ,μ}).

Thus P reduces to the familiar Hodge projector

P = I - grad · Δ^{-1} · div

(“Coulomb gauge” / divergence-free projector), solvable exactly by FFT.

---

## 5. Where the Wilson Hessian lives (Hodge decomposition)
Near the identity configuration U^(0), tangent vectors identify with 𝔤-valued 1-cochains C^1.
The lattice Hodge decomposition is

C^1 = im(d_0) ⊕ ker(Δ_1) ⊕ im(d_1^*),

with

Δ_1 = d_1^* d_1 + d_0 d_0^*.

Interpretation:

- im(d_0): exact 1-forms = pure gauge (vertical)
- ker(Δ_1): harmonic 1-forms = global/topological modes (torons)
- im(d_1^*): co-exact 1-forms = local physical modes

At U^(0), horizontals are

H_{U^(0)} ≅ ker(Δ_1) ⊕ im(d_1^*).

And the repo’s key identity is

∇² S_W(U^(0)) = 2 c_W · d_1^* d_1.

So:

- it annihilates im(d_0) and ker(Δ_1)
- it is strictly positive on im(d_1^*)

This is the analytic reflection of the physical statement “the plaquette action penalizes curvature (curl), not pure gauge”.

---

## 6. Why this projector is the right computational primitive
If you want to test any of the hard steps (PBH/Riccati from RG, source positivity, mixing control), you keep needing the same operator pipeline:

1. pick a configuration U (or X with U=exp X)
2. compute P_U (via an FP solve)
3. compute Hessian–vector products H(U)·v (autodiff)
4. study the symmetric operator  P_U H(U) P_U  on random vectors / via Lanczos

That pipeline is exactly what the Colab code implements.
