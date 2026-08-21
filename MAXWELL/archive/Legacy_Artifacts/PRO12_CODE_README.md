# PRO12 Colab Code — What to run first

This README accompanies `PRO12_CODE_Colab_Hessian_Flow.py`.

The script is intentionally “skeleton-first”: it gives you the horizontal projector, the Wilson + Haar coordinate action, Hessian–vector products, Lanczos extremal eigenvalues, and two diagnostics you asked for:

- PBH/Riccati source-term test (finite differences): `pbh_source_quadratic_form`
- off-diagonal mixing proxy: commutator norm estimate `commutator_norm_estimate`

---

## 0. Colab setup (A100)
In a Colab notebook cell:

```bash
!nvidia-smi
```

Then copy/upload the script file and run:

```bash
!python PRO12_CODE_Colab_Hessian_Flow.py --demo haar
```

---

## 1. Stage 1 — “cheap”: linearized Wilson + quadratic Haar mass

```bash
!python PRO12_CODE_Colab_Hessian_Flow.py --demo linear --L 4 --D 4 --beta 2.0 --kappa 0.25 --m_steps 80
```

What you should see:
- smallest horizontal eigenvalue ≈ κ (because constant co-closed modes have curl=0)
- largest eigenvalue grows with β and UV momentum

---

## 2. Stage 2 — nonlinear SU(2) / SU(3) with autodiff HVPs

SU(2):

```bash
!python PRO12_CODE_Colab_Hessian_Flow.py --demo su2 --L 2 --D 4 --beta 2.0 --project covariant
```

SU(3):

```bash
!python PRO12_CODE_Colab_Hessian_Flow.py --demo su3 --L 2 --D 4 --beta 6.0 --project covariant
```

Notes:
- `--project covariant` solves the Faddeev–Popov Poisson equation by CG.
- `--project linear` uses FFT and is only correct very near identity.

---

## 3. PBH/Riccati positivity probe (run inside Python)

In Colab:

```python
import torch
from PRO12_CODE_Colab_Hessian_Flow import make_lattice, su3_basis, expm_from_coords, wilson_action, haar_potential
from PRO12_CODE_Colab_Hessian_Flow import adjoint_rep, project_horizontal_covariant, hvp, pbh_source_quadratic_form

device = 'cuda' if torch.cuda.is_available() else 'cpu'
lat = make_lattice(L=2, D=4, device=device)
basis = su3_basis(device)
m = basis.shape[0]
N = basis.shape[-1]

x0 = (0.03*torch.randn((lat.n_sites, lat.D, m), device=device)).requires_grad_(True)
x = x0.reshape(-1)

def action_flat(z):
    X = z.reshape(lat.n_sites, lat.D, m)
    U = expm_from_coords(X, basis).reshape(lat.n_sites, lat.D, N, N)
    S = wilson_action(U, lat, beta=6.0) + torch.sum(haar_potential(X.reshape(-1,m), basis))
    return S

with torch.no_grad():
    U = expm_from_coords(x0, basis).reshape(lat.n_sites, lat.D, N, N)
AdU = adjoint_rep(U.reshape(-1,N,N), basis).reshape(lat.n_sites, lat.D, m, m)
proj = lambda v: project_horizontal_covariant(v.reshape(lat.n_sites, lat.D, m), AdU, lat).reshape(-1)

print(pbh_source_quadratic_form(action_flat, x, proj, dt=1e-3, n_samples=64))
```

Interpretation:
- You get (min, mean, max) of vᵀ R v over random horizontal vectors.
- If these are mostly ≥ 0 in the SAFE regime, that’s evidence the missing “source positivity” step is true in that regime.

---

## 4. Off-diagonal mixing proxy

```python
from PRO12_CODE_Colab_Hessian_Flow import make_spatial_projector_links, commutator_norm_estimate

# define H_op(v) = HVP at your x, with your projection choices
# then estimate ||[H,P_loc]||
mask = make_spatial_projector_links(lat, radius=0.8).to(device)

# Example placeholder: use the projected Hessian operator built from hvp

def H_op(v):
    return proj(hvp(action_flat, x, proj(v)))

print(commutator_norm_estimate(H_op, mask, n=x.numel(), n_iter=30))
```

If the commutator norm is small and decreases under flow/blocking, that’s strong evidence for the repo’s “mixing control” claims.

---

## 5. Where to push next
- Replace the coordinate gradient step in the PBH test with an actual Wilson/Lüscher flow update.
- Add explicit coarse-graining (blocking) to build an RG map; compare Hessians before/after.
- Increase lattice size once the L=2 sanity checks look stable.

