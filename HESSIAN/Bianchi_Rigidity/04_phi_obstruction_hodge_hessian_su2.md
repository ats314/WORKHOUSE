# Hodge Projection & “Phi Obstruction” Diagnostic for SU(2) Wilson Hessians

## What this is

This note extracts a *diagnostic computation*:

\[
\Phi_{\rm proxy} \;=\; \mathbb{E}\big[(\kappa_\star - \lambda_{\min}(\Pi_{\rm phys}\,\mathrm{Hess}\,S\,\Pi_{\rm phys}))_+\big],
\]
where:

- \(S\) is the SU(2) Wilson action on a periodic \(L^4\) lattice,
- \(\mathrm{Hess}\,S\) is taken as a **Riemannian Hessian** on \((S^3)^{E}\) (unit quaternions per link),
- \(\Pi_{\rm phys}\) is intended to project away gauge (exact) directions (Hodge/Coulomb-type projection),
- \((\cdot)_+ = \max(0,\cdot)\),
- \(\kappa_\star>0\) is a chosen “target curvature floor.”

The observable is designed to flag **near-zero curvature** events in the “physical” subspace.

---

## 1. Representation: SU(2) as unit quaternions

Each link is a unit quaternion \(q=(a,b,c,d)\in S^3\).  
Quaternion operations used:

- multiplication \(q\cdot r\),
- conjugate \(q^\ast\),
- normalization \(q/\|q\|\),
- trace proxy \(\Re\operatorname{Tr}(U(q)) = 2a\).

So for a plaquette quaternion \(q_p\),
\[
1-\tfrac12\Re\operatorname{Tr}(U_p) \equiv 1-a_p.
\]

---

## 2. Wilson action

On a periodic lattice:

\[
S_W[U] = \beta \sum_{p}(1-\tfrac12\Re \operatorname{Tr}(U_p)).
\]

The implementation computes plaquette products from four links and accumulates.

---

## 3. Riemannian Hessian-vector product (HVP)

The notebook constructs an HVP for the Riemannian Hessian using autodiff:

1. Euclidean gradient \(g_E=\nabla_E S\) (PyTorch autograd).
2. Project to tangent:
   \[
   \Pi_T(v) = v - \langle v,U\rangle\,U.
   \]
3. Use a directional derivative trick to obtain \(H_E v\) from second derivatives.
4. Apply tangent projections and a correction term (from the manifold constraint).

The core routine has the form:

```python
def hvp_riemannian(U, lat, beta, v):
    U = U.detach().requires_grad_(True)
    S = wilson_action(U, lat, beta)
    gE = grad(S, U, create_graph=True)[0]
    vT = proj_tangent(v, U)
    gv = (gE * vT).sum()
    HvE = grad(gv, U, create_graph=False)[0]
    inner = (gE.detach() * U.detach()).sum(dim=-1, keepdim=True)
    HvR = proj_tangent(HvE, U.detach()) - inner * vT
    HvR = proj_tangent(HvR, U.detach())
    return HvR.detach()
```

---

## 4. Lanczos estimate of \(\lambda_{\min}\)

A Lanczos iteration is run on the linear operator
\[
A(x)=\Pi_T\,\mathrm{Hess}\,S\,\Pi_T x
\]
(with optional shift) to estimate the smallest eigenvalue.

---

## 5. Reported diagnostic run and results

Parameters:

- \(L=4\), \(d=4\)
- \(\beta=6.0\)
- burn-in 300 steps
- step size \(5\times 10^{-4}\), noise scale \(5\times 10^{-3}\)
- \(n_{\rm samples}=12\), separated by 50 Langevin steps
- Lanczos iterations: 40
- \(\kappa_\star = 0.5\)

Sanity checks printed:

- symmetry check \( \langle x,Ay\rangle-\langle Ax,y\rangle \approx -10^{-12}\) (good),
- **finite difference check mismatch**:
  \[
  v^\top Hv \approx 59.30,\quad \text{finite-diff}\approx 29.27,\quad \text{diff}\approx 30.
  \]
  This indicates a likely implementation inconsistency (either manifold correction, normalization, or FD geometry).

Eigenvalue samples:

- early samples: \(\lambda_{\min}\approx 8.66, 11.04, 12.79, 15.54, 17.53, 20.28, 4.47\) (all \(>\kappa_\star\)).
- later samples: \(\lambda_{\min}\approx 0.1738, 0.00558, 0.000508, 7.83\!\times\!10^{-5}, 3.55\!\times\!10^{-5}\)

Defects \((\kappa_\star-\lambda_{\min})_+\) then jump close to \(0.5\).

Summary printed:

- \(\mathbb E[\lambda_{\min}] \approx 7.53948\)
- \(\Phi_{\rm proxy} \approx 0.193333\) for \(\kappa_\star=0.5\)

---

## 6. Interpretation (as a working theory)

Even with the caveat that the finite-difference check shows an inconsistency, the qualitative phenomenon is interesting:

- Most samples have a very healthy curvature floor.
- A subset show **near-zero curvature** in the estimated minimum eigenvalue.

This resembles a “rare-event” structure one might associate with:
- near-gauge directions not fully projected out,
- proximity to a Gribov-horizon-like boundary in gauge-fixed space,
- or numerical artifacts from the HVP / projection.

Because the finite-diff mismatch is large, *the first priority is correctness*.  
But if the effect survives debugging, \(\Phi_{\rm proxy}\) could become a meaningful “convexity defect observable” that can be tracked across \(\beta\), \(L\), and RG steps.

---

## 7. Immediate upgrades

1. Fix the finite difference check:
   - ensure the FD path is a *geodesic* on \(S^3\) (e.g., \(U(t)=U\exp(t\xi)\)) rather than linear renormalization,
   - or modify the HVP to match the chosen retraction.
2. Implement the full \(\Pi_{\rm phys}\) Hodge projection (the file begins a follow-up script that uses an FFT Poisson solve).
3. Compare:
   - tangent-only projection vs Hodge/Coulomb projection,
   - and explicitly remove harmonic (toron) modes.
4. Repeat at larger \(L\) and/or different \(\beta\); examine the tail probability of near-zero events.

---

## Sources used

- `RUN 124.pdf` (full script, output logs, follow-on Pi_phys version scaffold).
- `RUN 122.pdf` (related discrete Hodge decomposition / torus cochains sanity checks).
- `Simulations_and_Results_Summary.txt` (context: curvature floor and RG intent).
