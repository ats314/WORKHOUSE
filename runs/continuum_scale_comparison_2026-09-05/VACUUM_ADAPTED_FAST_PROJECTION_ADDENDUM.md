# The fast projection must follow the actual vacuum

5 September 2026. Outputs-only target addendum to
[the closed-form Schur comparison](CLOSED_FORM_SCHUR_GAP_AND_SCALE_BUDGET.md).
This supplies a concrete obstruction and repair for choosing its projection;
it is not a new Wilson theorem or a claim that boundary interactions vanish.

Let the slow Hamiltonian H_s>=0 have a normalized vacuum and gap Delta_s>0.
Take r fast qubits and real 0<c,s<1 with c²+s²=1. Set

```text
omega=c|0>+s|1>,
h_i=I-|omega><omega|,
H_r=H_s tensor I + I tensor sum_(i=1)^r h_i,
Omega_r=omega^tensor r.
```

Each h_i has gap one and the fast terms commute. The true full gap is
`min(Delta_s,1)` for every r. There are no boundary interactions to blame.

Choose instead the raw reference projection

```text
P_raw=I_s tensor |0^r><0^r|,     Q_raw=I-P_raw,
F_raw=Q_raw H_r Q_raw on ran Q_raw.
```

Use the slow vacuum and the fast test vector
`psi=Omega_r-c^r|0^r>`. Its exact norm and energy are

```text
||psi||²=1-c^(2r),
<psi,H_fast psi>=r s² c^(2r).
```

The second identity follows because H_fast Omega_r=0 and the expectation
of each h_i in |0^r> is s². Hence, writing f_r=inf spec F_raw,

```text
f_r <= r s² c^(2r)/(1-c^(2r)) -> 0.                     (1)
```

There is a matching exponential lower control. The full fast gap implies
`H_fast>=I-|Omega_r><Omega_r|`. Compression to the raw Q space gives
`Q_raw-|Q_raw Omega_r><Q_raw Omega_r|`, whose least eigenvalue is c^(2r).
The slow Hamiltonian is nonnegative, so

```text
c^(2r) <= f_r <= r s² c^(2r)/(1-c^(2r)).                (2)
```

The raw fast bound therefore deteriorates exponentially although the actual
physical gap remains fixed. A proposed volume-uniform hypothesis on F must
be tested against vacuum mismatch before adding interactions or a scale map.

The same issue appears in the exact raw Schur dressing. On the slow vacuum
direction its graph must contain the actual total vacuum. Thus

```text
U_raw |0^r> = -Q_raw Omega_r/c^r,
||U_raw |0^r>||²=c^(-2r)-1,
M_raw=I+U_raw*U_raw has value c^(-2r) on that direction. (3)
```

The closed-form theorem remains correct for every finite r; its raw fast
premise and graph norm are simply the wrong uniformly controlled objects.
In particular dropping M cannot repair the failure.

Now let the onsite unitary

```text
W=[[c,-s],[s,c]]
```

map |0> to omega, and transport the retained projection by W^tensor r:

```text
P_dressed=I_s tensor |Omega_r><Omega_r|,
Q_dressed=I-P_dressed.
```

This projection reduces the actual product Hamiltonian, and

```text
Q_dressed H_r Q_dressed >= Q_dressed,
U_dressed=0,           K0_dressed=H_s,         M_dressed=I. (4)
```

The full Schur fast hypothesis is restored exactly and uniformly. The
dressing has bounded support per site. Its finite-volume products define
a compatible quasi-local automorphism on local observables; an infinite
product unitary or product vector in the original reference-vacuum Hilbert
space is not required. GNS transport is the appropriate infinite-volume
language if the two product vacua are orthogonal in that representation.

This makes the next Wilson obligation more specific. Its retained/fast
projection must follow the actual vacuum in a norm suitable for the
restricted physical Hamiltonian form. The already established WORKHOUSE
creator coordinates and quasi-local vacuum transport provide the mechanism
to investigate, instead of reusing a raw tensor reference projection. A
proof must still control the dressed interactions, the actual fast form F,
the induced coarse operator and physical sources. The product example does
not itself supply those Wilson estimates.

[check_vacuum_projection_mismatch.py](check_vacuum_projection_mismatch.py)
and its saved JSON verify (1)-(4) exactly for c=3/5,s=4/5 and r=1,2,3,4.
The tensor unitary diagonalizes the independently assembled Hamiltonian to
the exact number operator; the Rayleigh quotient, vacuum graph norm and
dressed gap are checked with rational matrices. Formula (2) and its
all-r asymptotic conclusion are the elementary analytic argument above.
