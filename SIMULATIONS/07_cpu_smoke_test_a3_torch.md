# CPU Smoke-Test for (A3) Using PyTorch Autograd (Results Included)

## Purpose
Even without a GPU in this environment, we can still sanity-check the *geometry* of (A3) by:

1. implementing \(\mathrm{SU}(2)\) as unit quaternions,
2. implementing a standard Karcher-mean fixed-point iteration,
3. differentiating \(F_v(\pi(U))\) w.r.t. fine exponential coordinates \(x_b\in\mathbb{R}^3\),
4. measuring the ratio
\[
R(U,v)=\frac{\lVert \nabla (F_v\circ\pi)(U)\rVert^2}{\lVert \nabla F_v(\pi(U))\rVert^2}
\]
for random probes \(v\) and random small-field samples.

This is **not** a proof. It is a de-risking check that the implementation matches the expected scaling \(R\approx 1/N\) in the small-field regime.

---

## Code (PyTorch, CPU)

```python
import torch, numpy as np

torch.set_default_dtype(torch.float64)
device = torch.device('cpu')

def q_normalize(q):
    return q / (q.norm(dim=-1, keepdim=True) + 1e-12)

def q_conj(q):
    return torch.cat([q[..., :1], -q[..., 1:]], dim=-1)

def q_mul(a,b):
    aw,av = a[..., :1], a[..., 1:]
    bw,bv = b[..., :1], b[..., 1:]
    w = aw*bw - (av*bv).sum(dim=-1, keepdim=True)
    v = aw*bv + bw*av + torch.cross(av, bv, dim=-1)
    return torch.cat([w,v], dim=-1)

def su2_exp(x, half=1.0):
    r = x.norm(dim=-1, keepdim=True)
    rr = half*r
    w = torch.cos(rr)
    s = torch.sin(rr)/(r+1e-12)
    v = s*x
    return q_normalize(torch.cat([w,v], dim=-1))

def su2_log(q):
    q = q_normalize(q)
    w = q[..., 0:1].clamp(-1.0,1.0)
    v = q[..., 1:]
    vnorm = v.norm(dim=-1, keepdim=True)
    rr = torch.atan2(vnorm, w)
    x = rr * v / (vnorm+1e-12)
    return x

def karcher_mean(qs, num_iters=25, step=1.0):
    qs = q_normalize(qs)
    q = q_normalize(qs.mean(dim=-2))
    for _ in range(num_iters):
        dq = q_mul(q_conj(q).unsqueeze(-2), qs)
        logs = su2_log(dq)
        delta = logs.mean(dim=-2)
        q = q_mul(q, su2_exp(step*delta))
        q = q_normalize(q)
    return q

def block_pi(x_block, num_iters=25):
    qs = su2_exp(x_block)
    return karcher_mean(qs, num_iters=num_iters, step=1.0)

def F_v(V, v):
    y = su2_log(V)
    return (y*v).sum(dim=-1)

def R_ratio(x_block, v, num_iters=25):
    V = block_pi(x_block, num_iters=num_iters)
    val = F_v(V, v)
    g, = torch.autograd.grad(val, x_block, create_graph=False, retain_graph=False)
    num = (g*g).sum()
    den = (v*v).sum() + 1e-12
    return (num/den).detach().cpu().item()

def experiment(B=30, N=16, sigma=0.05, num_iters=25, seed=0):
    torch.manual_seed(seed)
    Rs=[]
    for _ in range(B):
        x = sigma*torch.randn(N,3, device=device, requires_grad=True)
        v = torch.randn(3, device=device)
        v = v/(v.norm()+1e-12)
        Rs.append(R_ratio(x, v, num_iters=num_iters))
    Rs = np.array(Rs)
    return dict(mean=float(Rs.mean()), std=float(Rs.std()),
                min=float(Rs.min()), max=float(Rs.max()))
```

---

## Results (N=16)

Using \(B=30\) samples per setting (random \(v\), random \(x_b\sim \mathcal{N}(0,\sigma^2)\)), Karcher iterations \(=25\):

| \(\sigma\) | mean(R) | std(R) | min(R) | max(R) |
|---:|---:|---:|---:|---:|
| 0.05 | 0.06270 | 0.00005 | 0.06261 | 0.06282 |
| 0.15 | 0.06432 | 0.00051 | 0.06354 | 0.06552 |
| 0.30 | 0.07055 | 0.00254 | 0.06690 | 0.07696 |
| 0.60 | 0.12632 | 0.05111 | 0.08482 | 0.35205 |

Interpretation:
- For **small field** (\(\sigma\approx 0.05\)), the ratio is essentially \(1/16=0.0625\), matching the linearized intertwining prediction.
- As dispersion grows, the ratio increases and becomes unstable—exactly what you expect when leaving a normal neighborhood (log branch / nonconvexity / multiple local minima for the mean).

This strongly supports the claim that **geodesic averaging is contractive in the regime where it is geometrically well-defined**, and it also pinpoints why you should not claim global (A3) without either localization or switching to decimation.

