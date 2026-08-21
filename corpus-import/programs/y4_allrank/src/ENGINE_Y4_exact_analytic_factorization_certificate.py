#!/usr/bin/env python3
"""
EXACT ANALYTIC GLOBAL BAND-EDGE CERTIFICATE
SU(3) T1^{+-} O(y^4) projected band

Uses the verified 189-record real-space H4 kernel in the SAME cell/origin gauge:

    psi(k) = (exp(i k_z)-1, -(exp(i k_y)-1), exp(i k_x)-1)^T

It derives, in exact rational arithmetic, the closed factorization

    D(k) = psi^†[H4(k)-qI]psi
         = A sum_i X_i^2 + B sum_{i<j} X_i X_j,

where X_i = 1-cos(k_i), A=5/12, and
B=17607806155349/275331901291200.

This gives a purely analytic proof of the unique global minimum at Gamma and
unique global maximum at R, with no interval arithmetic.
"""

import gzip
import hashlib
import json
import sys
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path

# Strict known-file policy: use the named kernel; if absent, stop.
DEFAULT_JSON = Path('/content/CERT_Y4_full_real_space_h4_kernel.json')
DEFAULT_GZ = Path('/content/DATA_Y4_full_real_space_h4_kernel.json.gz')
LOCAL_JSON = Path('/mnt/data/CERT_Y4_full_real_space_h4_kernel.json')

EXPECTED_Q = F(-20721577909065127111, 7250590288602460800)
EXPECTED_X = F(-17700498622147435111, 7250590288602460800)
EXPECTED_M = F(-4367164159624988707, 1812647572150615200)
EXPECTED_R = F(-3447362930970494909, 1450118057720492160)
EXPECTED_B = F(17607806155349, 275331901291200)


def gate(name, condition, detail=''):
    status = 'PASS' if condition else 'FAIL'
    print(f'{status:4s} {name:52s} {detail}')
    if not condition:
        raise AssertionError(f'{name}: {detail}')


def sha256(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def load_payload(path):
    if path.suffix == '.gz':
        with gzip.open(path, 'rt', encoding='utf-8') as f:
            return json.load(f)
    with path.open('r', encoding='utf-8') as f:
        return json.load(f)


def find_kernel():
    if len(sys.argv) > 1:
        p = Path(sys.argv[1])
        if not p.exists():
            raise FileNotFoundError(f'Required kernel is missing: {p}')
        return p.resolve()
    for p in (DEFAULT_JSON, DEFAULT_GZ, LOCAL_JSON):
        if p.exists():
            return p.resolve()
    raise FileNotFoundError(
        'Required kernel is missing. Upload '
        '/content/CERT_Y4_full_real_space_h4_kernel.json and rerun.'
    )


def levi(a, b, c):
    if len({a, b, c}) != 3:
        return 0
    p = [a, b, c]
    inv = sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3))
    return -1 if inv % 2 else 1


def unit(axis, sign):
    v = [0, 0, 0]
    v[axis] = sign
    return tuple(v)


def add3(a, b, c=(0, 0, 0)):
    return tuple(a[i] + b[i] + c[i] for i in range(3))


def canonical_positive(freq):
    for x in freq:
        if x != 0:
            return x > 0
    return False


def parity_cos(freq, point):
    return -1 if sum(freq[i] * point[i] for i in range(3)) % 2 else 1


KERNEL_PATH = find_kernel()
print('Using kernel:', KERNEL_PATH)
payload = load_payload(KERNEL_PATH)
records = payload['kernel']
planes = [tuple(map(int, p)) for p in payload['meta']['basis_planes']]
plane_index = {p: i for i, p in enumerate(planes)}

gate('kernel record count', len(records) == 189, str(len(records)))
gate('basis ordering', planes == [(0, 1), (0, 2), (1, 2)], str(planes))

flat = []
for mu, nu in planes:
    rho = list({0, 1, 2} - {mu, nu})
    gate(f'plane {(mu, nu)} complement', len(rho) == 1, str(rho))
    rho = rho[0]
    s = levi(mu, nu, rho)
    gate(f'plane {(mu, nu)} Levi-Civita sign', s in (-1, 1), f'rho={rho}, sign={s}')
    flat.append((rho, s))

# Parse exact kernel. Record input=a, output=b contributes H[b,a].
kernel = defaultdict(F)
for rec in records:
    a = plane_index[tuple(rec['input_plane'])]
    b = plane_index[tuple(rec['output_plane'])]
    r = tuple(map(int, rec['displacement']))
    kernel[(a, b, r)] += F(rec['weight'])

gate('189 sparse exact keys', len(kernel) == 189, str(len(kernel)))
herm = all(
    kernel.get((b, a, tuple(-x for x in r)), F(0)) == w
    for (a, b, r), w in kernel.items()
)
gate('exact real-space Hermiticity', herm, 'exact')

H0 = [[F(0) for _ in range(3)] for _ in range(3)]
for (a, b, _r), w in kernel.items():
    H0[b][a] += w
q = H0[0][0]
gate('H4(0)=q I3', all(H0[i][j] == (q if i == j else 0) for i in range(3) for j in range(3)), str(q))
gate('q exact anchor', q == EXPECTED_Q, str(q))

# Build exact Laurent polynomial D(k)=psi^†(H4-qI)psi.
L = defaultdict(F)
zero = (0, 0, 0)
for (a, b, r), w in kernel.items():
    rho_a, s_a = flat[a]
    rho_b, s_b = flat[b]
    left = [(unit(rho_b, -1), F(s_b)), (zero, F(-s_b))]
    right = [(unit(rho_a, +1), F(s_a)), (zero, F(-s_a))]
    for lf, lc in left:
        for rf, rc in right:
            L[add3(r, lf, rf)] += w * lc * rc

# -q|psi|^2, with |e^{ik}-1|^2=2-e^{ik}-e^{-ik}.
for rho, _s in flat:
    L[zero] += -2 * q
    L[unit(rho, +1)] += q
    L[unit(rho, -1)] += q
L = {f: c for f, c in L.items() if c != 0}

gate('Laurent term count', len(L) == 25, str(len(L)))
gate('Laurent inversion symmetry', all(L.get(tuple(-x for x in f), F(0)) == c for f, c in L.items()), 'exact')

constant = L[zero]
cos_terms = {f: 2*c for f, c in L.items() if f != zero and canonical_positive(f)}
gate('cosine term count', len(cos_terms) == 12, str(len(cos_terms)))
gate('D(0)=0', constant + sum(cos_terms.values()) == 0, 'exact')

# Exact cubic orbit structure.
e1 = (1, 0, 0)
e2 = (2, 0, 0)
p11 = (1, 1, 0)
pm11 = (1, -1, 0)
a = cos_terms[e1]
d = cos_terms[e2]
b = cos_terms[p11]

def perm_orbit(freq):
    import itertools
    return {tuple(freq[p[i]] for i in range(3)) for p in itertools.permutations(range(3))}

axis1 = {(1,0,0),(0,1,0),(0,0,1)}
axis2 = {(2,0,0),(0,2,0),(0,0,2)}
pair = {(1,1,0),(1,-1,0),(1,0,1),(1,0,-1),(0,1,1),(0,1,-1)}
gate('frequency support is exactly 3+3+6', set(cos_terms) == axis1 | axis2 | pair, str(sorted(cos_terms)))
gate('unit-axis orbit coefficient', all(cos_terms[f] == a for f in axis1), str(a))
gate('double-axis orbit coefficient', all(cos_terms[f] == d for f in axis2), str(d))
gate('pair orbit coefficient', all(cos_terms[f] == b for f in pair), str(b))

# Algebra after X_i=1-cos(k_i):
# D = C+a sum c_i+d sum cos(2k_i)+b sum_{i<j}[cos(ki+kj)+cos(ki-kj)]
#   = (-a-4d-4b) sum X_i + 2d sum X_i^2 + 2b sum_{i<j}X_iX_j.
linear_X = -a - 4*d - 4*b
A = 2*d
B = 2*b

gate('linear X term cancels', linear_X == 0, str(linear_X))
gate('factor A=5/12', A == F(5, 12), str(A))
gate('factor B exact witness', B == EXPECTED_B, str(B))
gate('factor coefficients positive', A > 0 and B > 0, f'A={A}, B={B}')

# Independent exact anchor evaluation from the Laurent polynomial.
def D_parity(point):
    return constant + sum(amp * parity_cos(freq, point) for freq, amp in cos_terms.items())

def c4_parity(point):
    norm = F(4 * sum(point), 1)
    return q if norm == 0 else q + D_parity(point) / norm

cX = c4_parity((1,0,0))
cM = c4_parity((1,1,0))
cR = c4_parity((1,1,1))
gate('X exact anchor', cX == EXPECTED_X and cX-q == A, str(cX))
gate('M exact anchor', cM == EXPECTED_M and cM-q == A+B/2, str(cM))
gate('R exact anchor', cR == EXPECTED_R and cR-q == A+B, str(cR))

bandwidth = A + B
gate('exact bandwidth', bandwidth == F(132329431693349, 275331901291200), str(bandwidth))

# Exact theorem logic:
# X_i in [0,2]. For nonzero momentum mod 2pi, S=sum X_i>0.
# D=A Q+B R>0 because A,B>0 and Q=sum X_i^2>0.
# Therefore Gamma is the unique global minimum.
# Also Q<=2S and R<=2S, where
#   R<=2S follows after y_i=X_i/2:
#   sum y_i - sum_{i<j}y_i y_j
#   = y0(1-y1)+y1(1-y2)+y2(1-y0)>=0.
# Hence (c4-q)=D/(2S)<=A+B, with equality only at X0=X1=X2=2.

gate('analytic global-minimum hypotheses', A > 0 and B > 0, 'Xi>=0 makes D strictly positive off Gamma')
gate('analytic global-maximum hypotheses', A > 0 and B > 0, 'Xi^2<=2Xi and pair-sum<=2S')

# Directional Gamma curvature range, correcting the earlier isotropy claim.
kappa_axis = A / 4
kappa_diag = (A + B) / 12
gate('Gamma directional curvature extrema', kappa_axis == F(5,48) and kappa_diag == F(132329431693349,3303982815494400), f'diagonal={kappa_diag}, axis={kappa_axis}')
# R expansion: c4(R+delta)=c4(R)-(A+B)|delta|^2/12+O(|delta|^4).
kappa_R = -(A + B) / 12
gate('R isotropic quadratic coefficient', kappa_R == -kappa_diag, str(kappa_R))

if Path('/content').exists():
    outdir = Path('/content/Y4_EXACT_ANALYTIC_FACTOR_CERT')
else:
    outdir = Path('/mnt/data/Y4_EXACT_ANALYTIC_FACTOR_CERT')
outdir.mkdir(parents=True, exist_ok=True)

result = {
    'title': 'Exact analytic factorization and global band-edge theorem for SU(3) T1^{+-} at O(y^4)',
    'status': 'PASS',
    'kernel_path': str(KERNEL_PATH),
    'kernel_sha256': sha256(KERNEL_PATH),
    'kernel_records': len(records),
    'projection_gauge': 'cell/origin: (exp(ik_z)-1, -(exp(ik_y)-1), exp(ik_x)-1)',
    'q_exact': str(q),
    'factorization': {
        'variables': 'X_i=1-cos(k_i), 0<=X_i<=2',
        'D_exact': f'({A})*sum_i X_i^2 + ({B})*sum_i<j X_i X_j',
        'norm_exact': '||psi||^2=2*sum_i X_i',
        'c4_exact': 'c4(k)=q+D(k)/||psi(k)||^2 for k != Gamma, with continuous value c4(Gamma)=q',
        'A_exact': str(A),
        'B_exact': str(B),
    },
    'band_edges': {
        'Gamma_exact': str(q),
        'X_exact': str(cX),
        'M_exact': str(cM),
        'R_exact': str(cR),
        'bandwidth_exact': str(bandwidth),
    },
    'curvature': {
        'Gamma_axis_coefficient_exact': str(kappa_axis),
        'Gamma_diagonal_coefficient_exact': str(kappa_diag),
        'Gamma_note': 'The quadratic lift is direction-dependent because the lower-order flat eigenspace is three-dimensional at Gamma; it is not isotropic.',
        'R_isotropic_coefficient_exact': str(kappa_R),
    },
    'theorem': 'Gamma is the unique global minimum and R is the unique global maximum modulo reciprocal-lattice periodicity and cubic symmetry.',
}
json_path = outdir / 'CERT_Y4_exact_analytic_factorization_certificate.json'
json_path.write_text(json.dumps(result, indent=2, sort_keys=True), encoding='utf-8')

md = f'''# Exact analytic factorization of the SU(3) $T_1^{{+-}}$ band at $O(y^4)$

**Status:** PASS  
**Kernel:** `{KERNEL_PATH}`  
**SHA-256:** `{sha256(KERNEL_PATH)}`

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
       + ({B}) R2,
```

with

```text
q = {q},
||psi(k)||^2 = 2S.
```

Therefore, for `S>0`,

```text
c4(k)-q = [(5/12)Q + ({B})R2] / (2S).
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
c4(k)-q <= 5/12 + {B}
         = {bandwidth}.
```

Equality requires `X_0=X_1=X_2=2`, i.e. `k=(pi,pi,pi)` modulo periodicity. Thus R is the unique global maximum.

## Exact band points

| Point | Exact `c4` | Exact lift above Gamma |
|---|---:|---:|
| Gamma | `{q}` | `0` |
| X | `{cX}` | `{A}` |
| M | `{cM}` | `{A+B/2}` |
| R | `{cR}` | `{bandwidth}` |

## Curvature correction

The earlier statement that the Gamma curvature is isotropic is false. For `k=t n`, `|n|=1`,

```text
c4(t n)-q
= (t^2/4)[(5/12) sum_i n_i^4
  + ({B}) sum_i<j n_i^2 n_j^2] + O(t^4).
```

Its coefficient ranges from

```text
diagonal: {kappa_diag}
axis:     {kappa_axis} = 5/48.
```

The direction dependence is allowed because the lower-order flat eigenspace is three-dimensional at Gamma. At R the quadratic coefficient is isotropic:

```text
c4(R+delta)=c4(R)-({-kappa_R})|delta|^2+O(|delta|^4).
```

## Final theorem

The full projected fourth-order band has the exact global edges

```text
min c4 = c4(Gamma) = {q},
max c4 = c4(R)     = {cR},
bandwidth           = {bandwidth}.
```

No interval arithmetic is required.
'''
md_path = outdir / 'CERT_Y4_exact_analytic_factorization_certificate.md'
md_path.write_text(md, encoding='utf-8')

print('\n' + '='*100)
print('EXACT ANALYTIC GLOBAL BAND THEOREM: PASS')
print('='*100)
print('D(k) = (5/12) sum X_i^2 +', B, 'sum_{i<j} X_i X_j')
print('Gamma is the unique global minimum; R is the unique global maximum.')
print('Exact bandwidth =', bandwidth, '=', float(bandwidth))
print('Gamma curvature is directional, not isotropic:')
print('  diagonal coefficient =', kappa_diag, '=', float(kappa_diag))
print('  axis coefficient     =', kappa_axis, '=', float(kappa_axis))
print('R isotropic coefficient =', kappa_R, '=', float(kappa_R))
print('\nJSON:', json_path)
print('MD:  ', md_path)
