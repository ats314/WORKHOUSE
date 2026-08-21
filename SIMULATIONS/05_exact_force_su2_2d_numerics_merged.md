# Numerical note: exact-force gradient descent for 2D $SU(2)$ Wilson action

## 1. Purpose

A small toy computation searches for configurations with **high plaquette disorder** but **small Wilson force** (small $\|\nabla S\|$), as a landscape sanity check against “rough but flat” stationary points.

Model: 2D $SU(2)$ lattice gauge theory on an $L\times L$ periodic torus.  
Method: exact analytic force + naive gradient descent.

## 2. Code

Script: `exact_force_su2_2d.py` (included verbatim).

```python
import numpy as np

# SU(2) via unit quaternions
def normalize(q):
    return q / np.linalg.norm(q)

def qmul(q1, q2):
    a1,b1,c1,d1 = q1
    a2,b2,c2,d2 = q2
    return np.array([
        a1*a2 - b1*b2 - c1*c2 - d1*d2,
        a1*b2 + b1*a2 + c1*d2 - d1*c2,
        a1*c2 - b1*d2 + c1*a2 + d1*b2,
        a1*d2 + b1*c2 - c1*b2 + d1*a2
    ])

def qinv(q):
    return np.array([q[0],-q[1],-q[2],-q[3]])

def imag(q):
    return q[1:]

def cartan(theta):
    return np.array([np.cos(theta), 0.0, 0.0, np.sin(theta)])

def run(L=6, init='random', theta=1.2, eps0=0.6, lam=10.0, lr=0.03, iters=50, report_every=5):
    Nd = 2
    def mod(x): return x % L

    # initialize links
    links = {}
    for x in range(L):
        for y in range(L):
            for mu in range(Nd):
                if init == 'random':
                    q = np.random.normal(size=4)
                    links[(x,y,mu)] = normalize(q)
                elif init == 'checkerboard_cartan':
                    sign = 1 if (x+y+mu) % 2 == 0 else -1
                    links[(x,y,mu)] = cartan(sign*theta)
                else:
                    raise ValueError("init must be 'random' or 'checkerboard_cartan'")

    def plaquette(x,y):
        Ux  = links[(mod(x),   mod(y),   0)]
        Uy  = links[(mod(x+1), mod(y),   1)]
        Ux2 = qinv(links[(mod(x), mod(y+1), 0)])
        Uy2 = qinv(links[(mod(x), mod(y),   1)])
        return qmul(qmul(Ux, Uy), qmul(Ux2, Uy2))

    def disorder():
        s = 0.0
        for x in range(L):
            for y in range(L):
                s += (1.0 - plaquette(x,y)[0])
        return s / (L*L)

    def link_force(x,y,mu):
        F = np.zeros(3)
        if mu == 0:
            F += imag(plaquette(x,y))
            F -= imag(plaquette(x,y-1))
        if mu == 1:
            F += imag(plaquette(x-1,y))
            F -= imag(plaquette(x,y))
        return F

    def grad_norm():
        g = 0.0
        for x in range(L):
            for y in range(L):
                for mu in range(Nd):
                    F = link_force(x,y,mu)
                    g += np.dot(F,F)
        return g

    print(f"init={init} L={L}")
    print("Initial disorder:", disorder())
    print("Initial grad norm:", grad_norm())

    for it in range(iters):
        for x in range(L):
            for y in range(L):
                for mu in range(Nd):
                    q0 = links[(x,y,mu)]
                    F = link_force(x,y,mu)
                    dq = np.array([0.0, F[0], F[1], F[2]])
                    B = disorder()
                    if B < eps0:
                        dq *= (1.0 + lam*(eps0 - B))
                    links[(x,y,mu)] = normalize(q0 - lr*dq)

        if it % report_every == 0:
            print(f"Iter {it:2d} | disorder={disorder():.4f} | grad_norm={grad_norm():.6f}")

if __name__ == '__main__':
    run(L=6, init='random')
    run(L=6, init='checkerboard_cartan')
```

## 3. Representative output (random init, $L=6$)

Run parameters: `init='random'`, `iters=50`, `report_every=5`, with `seed=0`.

```
init=random L=6
Initial disorder: 0.9461164561717662
Initial grad norm: 93.00157947515486
Iter  0 | disorder=0.9398 | grad_norm=94.345499
Iter  5 | disorder=0.9171 | grad_norm=101.751492
Iter 10 | disorder=0.9174 | grad_norm=107.512340
Iter 15 | disorder=0.9317 | grad_norm=107.303433
Iter 20 | disorder=0.9443 | grad_norm=103.177357
Iter 25 | disorder=0.9520 | grad_norm=98.735340
Iter 30 | disorder=0.9580 | grad_norm=94.335631
Iter 35 | disorder=0.9654 | grad_norm=89.577836
Iter 40 | disorder=0.9759 | grad_norm=84.600223
Iter 45 | disorder=0.9874 | grad_norm=81.043630
```

## 4. Small ensemble summary (random init, $L=6$)

Ten runs with seeds $0,1,\dots,9$, each for 50 iterations (reporting every 5), produced the following last-reported values (iteration 45):

|   seed |   init_disorder |   init_grad_norm |   last_disorder |   last_grad_norm |   last_grad_per_link |
|-------:|----------------:|-----------------:|----------------:|-----------------:|---------------------:|
| 0.0000 |          0.9461 |          93.0016 |          0.9874 |          81.0436 |               1.1256 |
| 1.0000 |          1.0505 |         106.4673 |          1.0924 |          97.9474 |               1.3604 |
| 2.0000 |          0.9921 |         111.6774 |          1.1685 |          91.7518 |               1.2743 |
| 3.0000 |          0.9811 |         105.6040 |          1.1152 |          93.0791 |               1.2928 |
| 4.0000 |          1.0458 |         106.7521 |          0.9236 |          98.2918 |               1.3652 |
| 5.0000 |          1.0176 |         107.7406 |          1.1222 |          89.1052 |               1.2376 |
| 6.0000 |          0.9219 |          94.0816 |          0.7947 |          79.4290 |               1.1032 |
| 7.0000 |          0.9530 |         124.5935 |          0.9603 |          85.5396 |               1.1880 |
| 8.0000 |          1.1047 |         105.9683 |          1.1027 |          69.4610 |               0.9647 |
| 9.0000 |          0.9775 |         113.8469 |          0.9175 |          82.5181 |               1.1461 |

The quantity `last_grad_per_link := last_grad_norm/(2L^2)` normalizes by the number of links.

## 5. Checkerboard Cartan initialization ($L=6$)

A structured initialization `init='checkerboard_cartan'` shows that decreasing the force drives the configuration toward the vacuum:

- initial disorder $\approx 0.9125$, initial grad norm $\approx 285.7951$;
- last reported (iter 45): disorder $\approx 0.0019$, grad norm $\approx 1.1133$.

Representative output:

```
init=checkerboard_cartan L=6
Initial disorder: 0.9125010165605543
Initial grad norm: 285.79505123435405
Iter  0 | disorder=0.8314 | grad_norm=279.814772
Iter  5 | disorder=0.4840 | grad_norm=211.282464
Iter 10 | disorder=0.1130 | grad_norm=61.410277
Iter 15 | disorder=0.0332 | grad_norm=18.800831
Iter 20 | disorder=0.0147 | grad_norm=8.395530
Iter 25 | disorder=0.0081 | grad_norm=4.656804
Iter 30 | disorder=0.0051 | grad_norm=2.938210
Iter 35 | disorder=0.0035 | grad_norm=2.015856
Iter 40 | disorder=0.0025 | grad_norm=1.466269
Iter 45 | disorder=0.0019 | grad_norm=1.113321
```

## 6. Caveats

- This is **2D**, not 4D; it is only a toy landscape check.
- Plain gradient descent is not an ergodic sampler and can miss saddle phenomena.
- The observation “no rough stationary points were found in these runs” is evidence, not a proof.
