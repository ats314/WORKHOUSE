# SU(N) closed-surface band theorem — Stage 1

**Status:** PASS  
**Domain:** integer `N >= 3`

## Exact shared-link result

For the four fused channels

- `1` and `Adj` from `F x Fbar`,
- `A2` and `S2` from `F x F`,

the dimension-weighted second-order contributions are

```text
w_1   = -2/(N*(N - 1)*(N + 1))
w_Adj = -2*(N - 1)*(N + 1)/(N*(2*N**2 - 1))
w_A2  = -(N - 1)/((N + 1)*(2*N - 3))
w_S2  = -(N + 1)/((N - 1)*(2*N + 3))
```

The orientation-family sums are

```text
W_mixed = -2*N**3/((N - 1)*(N + 1)*(2*N**2 - 1))
W_like  = -4*N*(N**2 - 2)/((N - 1)*(N + 1)*(2*N - 3)*(2*N + 3))
```

and the signed C-odd hopping is

```text
t_N = W_like-W_mixed
    = 2*N*(N - 2)*(N + 2)/((N - 1)*(N + 1)*(2*N - 3)*(2*N + 3)*(2*N**2 - 1)).
```

Every factor in this expression is positive for integer `N>=3`, so

```text
t_N > 0.
```

At `N=3`,

```text
t_3 = 5/612 = 5/612,
Sigma_3 = -481/612 = -481/612,
```

recovering the certified SU(3) domino constants.

The large-N behavior is

```text
-1/(16*N**5) + 1/(4*N**3) + O(N**(-7), (N, oo))
```

so `t_N ~ 1/(4N^3)`.

## Universal geometric flatness

In half-angle variables `q_i=2 sin(k_i/2)` up to an irrelevant phase, the oriented plaquette-boundary symbol is

```text
B = Matrix([[-q_y, q_x, 0], [-q_z, 0, q_x], [0, -q_z, q_y]])
```

and the closed-surface vector is

```text
psi = Matrix([[q_z], [-q_y], [q_x]]).
```

Exactly,

```text
B^T psi = 0,
det B = 0,
N_e psi = -4 psi,   N_e=B B^T-4I.
```

Therefore every second-order effective operator

```text
H_2,N(k)=d_N I+t_N N_e(k)
```

has the momentum-independent eigenvalue `d_N-4t_N`. Thus the C-odd closed-surface branch is universally flat at second order for every `SU(N)`, `N>=3`.

## Conditional fourth-order reduction

If the generic-N projected fourth-order Laurent support contains only the cubic frequency orbits

```text
{e_i}, {2e_i}, {e_i+e_j, e_i-e_j},
```

then cubic symmetry, inversion symmetry, and continuity at Gamma imply

```text
D_N(k)=A_N sum_i X_i^2+B_N sum_(i<j) X_i X_j,
X_i=1-cos(k_i).
```

Only four exact parity-point values are needed:

```text
A_N = c_X-q_N,
B_N = 2(c_M-c_X) = c_R-c_X,
c_R = 2c_M-c_X.   [hard consistency gate]
```

The certified SU(3) values give

```text
A_3 = 5/12,
B_3 = 17607806155349/275331901291200,
```

and satisfy the parity identity exactly.

## Remaining Stage-2 obligations

1. Prove the generic-N fourth-order three-orbit support lemma.
2. Compute exact `q_N,c_X(N),c_M(N),c_R(N)` for enough `N` to reconstruct rational functions.
3. Derive closed forms for `A_N` and `B_N`.
4. Prove `A_N>0` and `B_N>0` for all integer `N>=3`, treating exceptional small `N` separately if required.

No Monte Carlo or GPU computation is involved in this theorem chain.
