# Simulation Appendix: Maxwell Green Kernel, Gauge Fixing, and an A100-Ready SU(2) Workload

This note contains:

1. **A verified numerical check** of Proposition 9.X-style exponential decay bounds for the massive Maxwell Green kernel via FFT inversion on a 4D torus.
2. A **gauge-fixing experiment** showing how the row-sum constant $C_0$ collapses in Feynman gauge.
3. A **“worthy A100”** batched SU(2) simulation designed to directly test:
   - GAP-FC-02 (“rough ⇒ force bounded below”), and
   - GAP-FC-04 (typicality / tails of disorder functionals).

---

## 1) FFT inversion of the massive Maxwell operator on $\mathbb T^4$

We invert
\[
M = m^2 I + \alpha\,\Delta_1,\qquad \Delta_1=d_1^\ast d_1,
\]
acting on 1-forms (links), on a periodic $L^4$ lattice.
We compute $M^{-1}$ exactly in Fourier space using the longitudinal/transverse projector formula, then inverse FFT to obtain the real-space kernel and verify the bound
\[
\big|(M^{-1})_{bb_0}\big|
\ \le\ \frac{2}{m^2}\,e^{-\eta\,d_E(b,b_0)}.
\]

### Full corrected PyTorch code (runs on GPU if available)

```python
import math
from collections import deque

import torch
import torch.fft as fft

# ============================================================
# VERIFY PROPOSITION 9.X / 9.X' NUMERICALLY (PROJECT-ALIGNED)
# ============================================================

# --------------------------
# User parameters
# --------------------------
L = 16               # 16^4 grid (increase to 32/48/64 on an A100)
d = 4                # dimension
m2 = 0.3             # mass squared
alpha = 1.0          # kinetic coefficient
nu0 = 0              # target link orientation
x0 = (0, 0, 0, 0)    # target link tail coordinate

# --------------------------
# Device / precision
# --------------------------
device = "cuda" if torch.cuda.is_available() else "cpu"
real = torch.float64
cplx = torch.complex128
print(f"Running on {device} with L={L}...")

# --------------------------
# Helpers: indexing on torus
# --------------------------
def mod(a): return a % L

def add_vec(x, e):
    return tuple(mod(x[i] + e[i]) for i in range(d))

def sub_vec(x, e):
    return tuple(mod(x[i] - e[i]) for i in range(d))

# Unit vectors
E = []
for mu in range(d):
    e = [0]*d
    e[mu] = 1
    E.append(tuple(e))

def site_index(x):
    idx = 0
    for i in range(d):
        idx = idx * L + x[i]
    return idx

def link_index(x, mu):
    return site_index(x) * d + mu

def index_to_site_mu(idx_link):
    mu = idx_link % d
    idx_site = idx_link // d
    x = [0]*d
    for i in reversed(range(d)):
        x[i] = idx_site % L
        idx_site //= L
    return tuple(x), mu

# --------------------------
# Link adjacency (b ~ b' iff share a plaquette)
# --------------------------
def neighbors(x, mu):
    nbrs = set()
    e_mu = E[mu]
    for nu in range(d):
        if nu == mu:
            continue
        e_nu = E[nu]

        # Plaquette based at x in (mu,nu) plane:
        # links: (x,mu), (x,nu), (x+e_mu,nu), (x+e_nu,mu)
        nbrs.add((x, nu))
        nbrs.add((add_vec(x, e_mu), nu))
        nbrs.add((add_vec(x, e_nu), mu))

        # Plaquette based at x-e_nu:
        x_m = sub_vec(x, e_nu)
        nbrs.add((x_m, nu))
        nbrs.add((add_vec(x_m, e_mu), nu))
        nbrs.add((x_m, mu))

    nbrs.discard((x, mu))
    return list(nbrs)

# --------------------------
# BFS: compute graph distance dist_E(., b0) and measure D_E
# --------------------------
Nsites = L**d
Nlinks = d * Nsites

b0 = link_index(x0, nu0)
dist = [-1] * Nlinks
dist[b0] = 0
q = deque([b0])

max_deg = 0
print("Starting BFS to compute graph distances...")

while q:
    b = q.popleft()
    x, mu = index_to_site_mu(b)
    nbrs = neighbors(x, mu)

    max_deg = max(max_deg, len(nbrs))

    for (y, nu) in nbrs:
        bb = link_index(y, nu)
        if dist[bb] == -1:
            dist[bb] = dist[b] + 1
            q.append(bb)

if any(v < 0 for v in dist):
    raise RuntimeError("Link graph not connected.")

D_E = max_deg
print(f"BFS complete. Max degree D_E = {D_E}")

# --------------------------
# Fourier grid p and hat{p} = 2 sin(p/2)
# --------------------------
freq = fft.fftfreq(L, d=1.0).to(device=device, dtype=real)
p1d = 2.0 * math.pi * freq

p = []
for mu in range(d):
    shape = [1]*d
    shape[mu] = L
    p_mu = p1d.view(*shape).expand(*([L]*d))
    p.append(p_mu)
p = torch.stack(p, dim=0)              # (d, L, L, L, L)

hatp = 2.0 * torch.sin(p / 2.0)        # (d, ...)
p2 = torch.sum(hatp**2, dim=0)         # (...)

# --------------------------
# Symbol of Delta1 = d1* d1 on 1-forms:
# Q_mu_nu(p) = p2 * δ_mu_nu - hatp_mu * hatp_nu
#
# Then M^{-1}(p) for M = m^2 I + alpha Q via projectors:
# inv_trans = 1/(m^2 + alpha p2), inv_long = 1/m^2
# M^{-1} = inv_trans * I + (inv_long - inv_trans) * P_L
# --------------------------
m = math.sqrt(m2)
inv_long = 1.0 / m2
inv_trans = 1.0 / (m2 + alpha * p2)

# Longitudinal projector P_L = (hatp hatp^T)/p2 (0 at p=0)
P_L = torch.zeros((d, d) + tuple([L]*d), device=device, dtype=real)
mask = p2 > 0
p2_safe = torch.where(mask, p2, torch.ones_like(p2))

for mu in range(d):
    for nu in range(d):
        val = (hatp[mu] * hatp[nu]) / p2_safe
        P_L[mu, nu] = torch.where(mask, val, torch.zeros_like(p2))

# M^{-1} symbol
M_inv = torch.zeros_like(P_L, dtype=real)
inv_trans_expand = inv_trans.unsqueeze(0).unsqueeze(0)

for mu in range(d):
    M_inv[mu, mu] = inv_trans

M_inv = M_inv + (inv_long - inv_trans_expand) * P_L

# --------------------------
# Inverse FFT -> Green kernel in position space
# NOTE: M_inv[mu,nu] is already 4D, so ifftn() with default dims is correct.
# --------------------------
print("Computing inverse FFT for Green's function...")
G = torch.zeros_like(M_inv, dtype=cplx)
for mu in range(d):
    for nu in range(d):
        G[mu, nu] = fft.ifftn(M_inv[mu, nu].to(dtype=cplx))

G = G.real.to(dtype=real)

# --------------------------
# Compute C0(Delta1) from the real-space kernel of Delta1
# --------------------------
print("Computing C0(Delta1) constant...")

Q = torch.zeros_like(P_L, dtype=real)
for mu in range(d):
    Q[mu, mu] = p2
for mu in range(d):
    for nu in range(d):
        Q[mu, nu] = Q[mu, nu] - hatp[mu] * hatp[nu]

KDelta = torch.zeros_like(Q, dtype=cplx)
for mu in range(d):
    for nu in range(d):
        KDelta[mu, nu] = fft.ifftn(Q[mu, nu].to(dtype=cplx))
KDelta = KDelta.real.to(dtype=real)

origin_site = site_index((0,0,0,0))
KDelta_flat = KDelta.reshape(d, d, Nsites)

C0 = 0.0
for mu in range(d):
    abs_row = torch.abs(KDelta_flat[mu])
    s = torch.sum(abs_row)
    s = s - torch.abs(KDelta_flat[mu, mu, origin_site])  # remove diagonal
    C0 = max(C0, float(s))

# --------------------------
# Exponents from project formulas
# --------------------------
eta_DG_DE = 2.0 * math.asinh(m / (2.0 * math.sqrt(alpha * D_E)))
eta_DG_C0 = 2.0 * math.asinh(m / (2.0 * math.sqrt(alpha * C0)))
eta_CT_C0 = math.log(1.0 + m2 / (2.0 * alpha * C0))

# --------------------------
# Verify bound for a fixed target link b0
# --------------------------
G_slice = G[:, nu0].reshape(d, Nsites)  # G_{mu,nu0}(x)

mu_idx = torch.arange(d, device=device, dtype=torch.int64).repeat(Nsites)
site_idx = torch.arange(Nsites, device=device, dtype=torch.int64).repeat_interleave(d)
vals = torch.abs(G_slice[mu_idx, site_idx]).to(dtype=real)

dist_t = torch.tensor(dist, device=device, dtype=real)

def check_eta(eta, name):
    ratio = (m2/2.0) * vals * torch.exp(eta * dist_t)
    mx = torch.max(ratio)
    arg = torch.argmax(ratio).item()
    x_arg, mu_arg = index_to_site_mu(arg)
    print(f"[{name}] eta={eta:.6f} | max_ratio={float(mx):.6e} at (x={x_arg}, mu={mu_arg}), dist={dist[arg]}")
    return float(mx)

print("\n==== Geometry / constants ====")
print(f"L={L} d={d} Nsites={Nsites} Nlinks={Nlinks}")
print(f"m2={m2} alpha={alpha}")
print(f"D_E (measured) = {D_E}")
print(f"C0(Delta1) (measured) = {C0:.6f}")

print("\n==== Exponents ====")
print(f"eta_DG(D_E) = {eta_DG_DE:.6f}")
print(f"eta_DG(C0)  = {eta_DG_C0:.6f}")
print(f"eta_CT(C0)  = {eta_CT_C0:.6f}")

print("\n==== Verifying bounds ====")
mx1 = check_eta(eta_DG_DE, "DG_DE")
mx2 = check_eta(eta_DG_C0, "DG_C0")
mx3 = check_eta(eta_CT_C0, "CT_C0")

print("\n==== Verdict ====")
print("Bound passes for eta if max_ratio <= 1 (up to numerical tolerance).")
print(f"DG_DE: {mx1:.6e} | DG_C0: {mx2:.6e} | CT_C0: {mx3:.6e}")
```

### Example output (from one run at $L=16$, $m^2=0.3$, $\alpha=1$)

```
BFS complete. Max degree D_E = 18
...
Geometry: D_E=18, C0=43.9077
Exponents: eta_DG(D_E)=0.1290, eta_DG(C0)=0.0826, eta_CT(C0)=0.00341
[DG_DE] max_ratio=1.412e-01 at dist=0
[DG_C0] max_ratio=1.412e-01 at dist=0
[CT_C0] max_ratio=1.412e-01 at dist=0
```

So the theoretical bounds are satisfied numerically (all max ratios $\ll 1$).

**Notable phenomenon:** for curl–curl in this discretization, the row-sum constant $C_0$ can be *larger* than the degree constant $D_E$ because taking absolute values destroys sign cancellations.

---

## 2) Gauge-fixing experiment: $C_0$ collapses in Feynman gauge

Modify the operator to include a gauge-fixing term:
\[
M_\xi = m^2 I + \alpha\,d_1^\ast d_1 + \xi\,d_0 d_0^\ast.
\]
At $\xi=\alpha$ (Feynman gauge), the symbol becomes diagonal and each component propagates like a scalar Laplacian.

### Minimal code block to measure the new $C_0$

Assuming you already computed `hatp`, `p2`, and the projection machinery above:

```python
xi = alpha
print(f"\nRunning gauge-fixed experiment (xi = {xi})...")

# inverse symbol in gauge-fixed operator:
inv_trans = 1.0 / (m2 + alpha * p2)
inv_long  = 1.0 / (m2 + xi    * p2)

M_inv_GF = torch.zeros_like(P_L, dtype=real)
inv_trans_expand = inv_trans.unsqueeze(0).unsqueeze(0)
inv_long_expand  = inv_long.unsqueeze(0).unsqueeze(0)

for mu in range(d):
    M_inv_GF[mu, mu] = inv_trans

# only adds something if xi != alpha; in Feynman gauge inv_long==inv_trans
if xi != alpha:
    M_inv_GF = M_inv_GF + (inv_long_expand - inv_trans_expand) * P_L

# kinetic symbol for K = alpha*(curlcurl) + xi*(graddiv):
Q_GF = torch.zeros_like(P_L, dtype=real)
for mu in range(d):
    Q_GF[mu, mu] += alpha * p2
    for nu in range(d):
        Q_GF[mu, nu] -= alpha * hatp[mu] * hatp[nu]
for mu in range(d):
    for nu in range(d):
        Q_GF[mu, nu] += xi * hatp[mu] * hatp[nu]

# kernel and C0 row-sum
KDelta_GF = torch.zeros_like(Q_GF, dtype=cplx)
for mu in range(d):
    for nu in range(d):
        KDelta_GF[mu, nu] = fft.ifftn(Q_GF[mu, nu].to(dtype=cplx))
KDelta_GF = KDelta_GF.real.to(dtype=real)

KDelta_flat_GF = KDelta_GF.reshape(d, d, Nsites)
C0_GF = 0.0
for mu in range(d):
    abs_row = torch.abs(KDelta_flat_GF[mu])
    s = torch.sum(abs_row)
    s = s - torch.abs(KDelta_flat_GF[mu, mu, origin_site])
    C0_GF = max(C0_GF, float(s))

print(f"Old C0 (curlcurl): {C0:.4f}")
print(f"New C0 (Feynman gauge): {C0_GF:.4f}  (expect ~2d = {2*d})")
```

### Example measured output (same run)
```
Old C0 (curlcurl): 43.9077
New C0 (Feynman gauge): 8.0000
```

That is the scalar coordination number $2d=8$.

---

## 3) A small “exact force” SU(2) counterexample-search toy model (2D)

This is a quick experiment intended to *hunt* for configurations with **high disorder** but **tiny Wilson force** (a would-be counterexample to A′).

The project includes a small code file `exact_force_su2_2d.py`; here is representative output:

```
Initial disorder: 0.959... , Initial grad norm: 79.7...
Iter  0 | disorder=0.9587 | grad_norm=79.772740
Iter  5 | disorder=0.9464 | grad_norm=79.630530
...
Iter 45 | disorder=0.8621 | grad_norm=79.141091

Initial disorder: 0.050..., Initial grad norm: 1.466...
Iter  0 | disorder=0.0508 | grad_norm=1.371163
Iter  5 | disorder=0.0293 | grad_norm=0.469132
...
Iter 45 | disorder=0.0021 | grad_norm=0.064141
```

**Interpretation:** in this testbed,
- rough random data did not “accidentally” have tiny force;
- structured near-Cartan data flowed quickly toward vacuum.

This supports A′ qualitatively, but does not prove it.

---

## 4) A “worthy A100” simulation: batched SU(2) GPU search for flat rough directions

### What this targets

It is designed to directly test:

- **GAP-FC-02:** Does $\mathcal B_\Lambda\ge \varepsilon_0$ force $\|\nabla S\|\ge c_0$ uniformly?
- **GAP-FC-04:** How fast does $\mu(\mathcal B_\Lambda\ge \varepsilon_0)$ decay with volume (empirically), and what separation-tuned bound is plausible?

### Core idea

Run *many configurations in parallel* (batch dimension $B$) and do an **adversarial constrained optimization**:

\[
\min_U \ \|\nabla S(U)\|^2
\quad\text{subject to}\quad
\mathcal B_\Lambda(U)\ge \varepsilon_0.
\]

Implement with an augmented Lagrangian / penalty:
\[
\min_U \ \|\nabla S(U)\|^2 + \lambda\,\mathrm{ReLU}(\varepsilon_0-\mathcal B_\Lambda(U))^2.
\]

If the optimizer consistently fails to find $\|\nabla S\|\approx 0$ while keeping $\mathcal B_\Lambda\ge \varepsilon_0$ across many seeds and increasing $L$, that is powerful evidence for A′.

If it finds a family with small gradient at fixed disorder, you’ve discovered a genuine obstruction.

---

## 5) Minimal runnable skeleton (PyTorch, quaternion SU(2), 4D)

This is intentionally modular: you can start at small $L=4$ to debug, then scale to $L=12,16,20$ on an A100.

**Important practicality:** if you run this inside a notebook, `argparse` will see Jupyter’s `-f` argument. Use `parse_known_args()` or pass `args=[]`.

```python
import argparse
import math
import torch

# -------------------------
# CLI that works in notebooks
# -------------------------
def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--L", type=int, default=8)
    p.add_argument("--beta", type=float, default=2.4)
    p.add_argument("--eps0", type=float, default=0.15)
    p.add_argument("--batch", type=int, default=1024)
    p.add_argument("--steps", type=int, default=2000)
    p.add_argument("--lr", type=float, default=5e-3)
    p.add_argument("--lam", type=float, default=50.0)
    p.add_argument("--dtype", type=str, default="float32", choices=["float32","float64"])
    p.add_argument("--device", type=str, default="cuda")
    # NOTE: parse_known_args avoids the "-f kernel.json" crash in notebooks
    args, _ = p.parse_known_args()
    return args

# -------------------------
# SU(2) as unit quaternions
# q = (a,b,c,d) with a scalar part
# -------------------------
def qmul(q1, q2):
    a1,b1,c1,d1 = q1.unbind(-1)
    a2,b2,c2,d2 = q2.unbind(-1)
    return torch.stack([
        a1*a2 - b1*b2 - c1*c2 - d1*d2,
        a1*b2 + b1*a2 + c1*d2 - d1*c2,
        a1*c2 - b1*d2 + c1*a2 + d1*b2,
        a1*d2 + b1*c2 - c1*b2 + d1*a2
    ], dim=-1)

def qconj(q):
    a,b,c,d = q.unbind(-1)
    return torch.stack([a, -b, -c, -d], dim=-1)

def qnorm(q):
    return torch.sqrt(torch.sum(q*q, dim=-1, keepdim=True) + 1e-12)

def qnormalize(q):
    return q / qnorm(q)

def haar_quat(shape, device, dtype):
    # sample 4D gaussian then normalize => uniform on S^3 (Haar on SU(2))
    q = torch.randn(*shape, 4, device=device, dtype=dtype)
    return qnormalize(q)

# -------------------------
# Lattice helpers
# links: U[x,mu] with x in Z_L^4, mu in {0,1,2,3}
# We'll store as tensor U[B, L,L,L,L, 4, 4] where last dims are (mu, quat)
# -------------------------
def roll(x, shift, dim):
    return torch.roll(x, shifts=shift, dims=dim)

def plaquette(U, mu, nu):
    # U: [B, L,L,L,L, 4, 4]
    U_mu = U[..., mu, :]                   # at x
    U_nu = U[..., nu, :]                   # at x
    U_mu_shift_nu = roll(U_mu, -1, dim=1+nu)  # U_mu(x+e_nu)
    U_nu_shift_mu = roll(U_nu, -1, dim=1+mu)  # U_nu(x+e_mu)

    # U_p = U_mu(x) U_nu(x+e_mu) U_mu(x+e_nu)^(-1) U_nu(x)^(-1)
    return qmul(qmul(qmul(U_mu, U_nu_shift_mu), qconj(U_mu_shift_nu)), qconj(U_nu))

def wilson_defect(U_p):
    # defect = 1 - (1/2) Re Tr(U_p) ; for SU(2), ReTr = 2*a where a is scalar part
    a = U_p[..., 0]
    return 1.0 - a.clamp(-1.0, 1.0)

def disorder(U):
    # average over all oriented plaquettes mu<nu
    B = 0.0
    count = 0
    for mu in range(4):
        for nu in range(mu+1, 4):
            Up = plaquette(U, mu, nu)
            B = B + wilson_defect(Up).mean(dim=(1,2,3,4))  # per batch
            count += 1
    return B / count

# -------------------------
# Force proxy (cheap)
# -------------------------
def force_proxy(U, beta):
    # For A' hunting, you want something correlated with ||grad S||.
    # Computing the exact Wilson force is doable but longer; start with a proxy:
    # sum over plaquettes of (imag part magnitude)^2 as a stiffness indicator.
    F = 0.0
    count = 0
    for mu in range(4):
        for nu in range(mu+1, 4):
            Up = plaquette(U, mu, nu)
            v = Up[..., 1:]  # imaginary part
            F = F + (v*v).sum(dim=-1).mean(dim=(1,2,3,4))
            count += 1
    return beta * F / count

def main():
    args = parse_args()
    device = args.device if torch.cuda.is_available() else "cpu"
    dtype = torch.float32 if args.dtype == "float32" else torch.float64

    B = args.batch
    L = args.L

    # init
    U = haar_quat((B, L,L,L,L, 4), device=device, dtype=dtype)  # [B, L^4, 4 mu, 4 quat]
    U = U.view(B, L,L,L,L, 4, 4)

    # penalty parameter for enforcing disorder >= eps0
    lam = args.lam
    lr  = args.lr

    for t in range(args.steps):
        U.requires_grad_(True)
        Bv = disorder(U)                  # [B]
        Fv = force_proxy(U, args.beta)    # [B]

        # objective: minimize force proxy while keeping disorder high
        penalty = torch.relu(args.eps0 - Bv)
        loss = (Fv + lam * penalty*penalty).mean()

        loss.backward()
        with torch.no_grad():
            # gradient step in ambient R^4, then renormalize to SU(2)
            U = qnormalize(U - lr * U.grad)

        if (t % 50) == 0:
            with torch.no_grad():
                print(f"t={t:05d}  loss={loss.item():.4e}  "
                      f"disorder_mean={Bv.mean().item():.4f}  "
                      f"disorder_min={Bv.min().item():.4f}  "
                      f"forceproxy_mean={Fv.mean().item():.4f}  "
                      f"forceproxy_min={Fv.min().item():.4f}")

if __name__ == "__main__":
    main()
```

### How to scale it on an A100

- Use `--batch 4096` or `8192`.
- Increase `--L` to 12–20 (watch memory; tensor is $B\cdot L^4\cdot 4\cdot 4$ floats).
- Turn on mixed precision (`float32`) for speed; validate with smaller `float64` runs.

### What to record for the project

For each $(L,\beta,\varepsilon_0)$:

1. the minimum observed “force proxy” among batch (adversarial search),
2. the corresponding disorder level,
3. whether the minimum seems to drift toward 0 as $L$ increases.

If the minimum does **not** drift toward 0 and remains bounded below, you have strong evidence for A′.
If it does drift, inspect the minimizing configs: they likely concentrate in the aligned-Cartan exceptional set.

---

## 6) Optional: adding an explicit alignment diagnostic

To connect numerics to the **alignment lemma**, compute at each link the staple vectors in $\mathfrak{su}(2)\cong\mathbb R^3$ and measure how collinear they are (e.g. ratio of largest singular value to Frobenius norm of the $6\times 3$ stack).
Then you can empirically verify:

> near-cancellation of link force happens only when the 6 incident staple vectors are nearly collinear.

That would be extremely informative evidence for the “local cancellation ⇒ alignment” conjecture.

