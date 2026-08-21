# Exact analytic factorization of the SU(3) $T_1^{+-}$ band at $O(y^4)$

**Status:** PASS  
**Kernel:** `/mnt/data/CERT_Y4_full_real_space_h4_kernel.json`  
**SHA-256:** `d2a4121a9798b2c364a52f7845fd7014ce2463563642470102cb080336a9fd51`

## Exact projected band

Use the cell/origin-gauge flat vector

```text
psi(k) = (exp(i k_z)-1, -(exp(i k_y)-1), exp(i k_x)-1)^T.
```

Let

```text
X_i = 1-cos(k_i),    0 <= X_i <= 2,
S   = X_0+X_1+X_2,
Q   = X_0^2+X_1^2+X_2^2,
R2  = X_0 X_1+X_0 X_2+X_1 X_2.
```

The exact 189-record kernel reduces to

```text
D(k) = psi(k)^† [H4(k)-q I] psi(k)
     = (5/12) Q
       + (17607806155349/275331901291200) R2,
```

with

```text
q = -20721577909065127111/7250590288602460800,
||psi(k)||^2 = 2S.
```

Therefore, for `S>0`,

```text
c4(k)-q = [(5/12)Q + (17607806155349/275331901291200)R2] / (2S).
```

## Exact global minimum

Both coefficients are strictly positive and `X_i>=0`. For every nonzero momentum modulo `2 pi`, `S>0` and `Q>0`, hence

```text
D(k)>0,
c4(k)>q.
```

At Gamma, `H4(0)=q I3`, so the continuous band value is exactly `q`. Thus Gamma is the unique global minimum modulo reciprocal-lattice periodicity.

## Exact global maximum

On `0<=X_i<=2`,

```text
Q <= 2S,
R2 <= 2S.
```

The second inequality follows by setting `x_i=X_i/2`:

```text
(x0+x1+x2)-(x0 x1+x0 x2+x1 x2)
= x0(1-x1)+x1(1-x2)+x2(1-x0) >= 0.
```

Hence

```text
c4(k)-q <= 5/12 + 17607806155349/275331901291200
         = 132329431693349/275331901291200.
```

Equality requires `X_0=X_1=X_2=2`, i.e. `k=(pi,pi,pi)` modulo periodicity. Thus R is the unique global maximum.

## Exact band points

| Point | Exact `c4` | Exact lift above Gamma |
|---|---:|---:|
| Gamma | `-20721577909065127111/7250590288602460800` | `0` |
| X | `-17700498622147435111/7250590288602460800` | `5/12` |
| M | `-4367164159624988707/1812647572150615200` | `247051057231349/550663802582400` |
| R | `-3447362930970494909/1450118057720492160` | `132329431693349/275331901291200` |

## Curvature correction

The earlier statement that the Gamma curvature is isotropic is false. For `k=t n`, `|n|=1`,

```text
c4(t n)-q
= (t^2/4)[(5/12) sum_i n_i^4
  + (17607806155349/275331901291200) sum_i<j n_i^2 n_j^2] + O(t^4).
```

Its coefficient ranges from

```text
diagonal: 132329431693349/3303982815494400
axis:     5/48 = 5/48.
```

The direction dependence is allowed because the lower-order flat eigenspace is three-dimensional at Gamma. At R the quadratic coefficient is isotropic:

```text
c4(R+delta)=c4(R)-(132329431693349/3303982815494400)|delta|^2+O(|delta|^4).
```

## Final theorem

The full projected fourth-order band has the exact global edges

```text
min c4 = c4(Gamma) = -20721577909065127111/7250590288602460800,
max c4 = c4(R)     = -3447362930970494909/1450118057720492160,
bandwidth           = 132329431693349/275331901291200.
```

No interval arithmetic is required.
