# The intrinsic SU(2) physical class rotor: exact normalization and gap controls

5 September 2026. Outputs-only continuation toward a physical fast-mode
estimate for the actual bouquet block. The operator studied is

    H(u)=-Delta_SU(2)+4u(2-Tr K),   u>=0,

on conjugation-invariant L2(SU(2)). It is the intrinsic vertical rotor
in the stated bouquet metric normalization. This note does not identify
it with a reducing fast complement of the full OS Hamiltonian.

## 1. Exact group, radial and Jacobi normalizations

Write the eigenvalues of K as exp(±i theta), 0<=theta<=pi. The normalized
class Haar measure is `(2/pi)sin^2(theta)dtheta`, the fundamental trace is
`2cos(theta)`, and

    chi_j(theta)=sin((2j+1)theta)/sin(theta),
    j=0,1/2,1,... .

These conventions and orthonormality are also recorded in
[SISSA's group-theory notes, §3.7](https://www.sissa.it/tpp/phdsection/OnlineResources/4037/SISSA_Groups_course_MS_2025.pdf).
The calculations here directly verify the normalization rather than
depend on a name for the group metric.

With the Casimir convention `-Delta chi_j=j(j+1)chi_j`, the radial
operator is

    -Delta=-1/4 [d²/dtheta²+2cot(theta)d/dtheta].

In particular the fundamental Casimir is 3/4. The unit S3 Laplacian
without the factor 1/4 would instead give 3 and is a different clock.
The exact character multiplication rule is

    (Tr K)chi_j=chi_(j+1/2)+chi_(j-1/2),

where the second term is absent for j=0. Therefore the exact infinite
Jacobi operator in the orthonormal character basis has

    H_jj=j(j+1)+8u,
    H_(j,j+1/2)=H_(j+1/2,j)=-4u.                         (1)

The script verifies the character recurrence and radial Casimir
identities for polynomial degrees zero through eight, 25 Haar inner
products, and the symbolic radial conjugation. The displayed general
formulas follow directly from the sine formula and trigonometric
addition identity; the finite checks are narrower controls of them.

The unitary map `g=sqrt(2/pi)sin(theta)f` maps the class Hilbert space to
ordinary L2(0,pi), and gives the Dirichlet operator

    H=-1/4 d²/dtheta²-1/4+8u(1-cos(theta)).              (2)

Its endpoint domain is the Friedrichs Dirichlet domain. It is not the
full-line oscillator or the unweighted radial Laplacian.

## 2. What the large-u calculation predicts

Set `x=2u^(1/4)theta`. The interval becomes `(0,2pi u^(1/4))`, and

    H=sqrt(u)(-d²/dx²+x²)-1/4-x^4/48
                         +x^6/(5760 sqrt(u))+... .     (3)

The half-line Dirichlet oscillator uses the odd full-line Hermite
levels m=1,3,5,... . Its first energies are 3sqrt(u),7sqrt(u),..., so
the leading class gap is 4sqrt(u). The exact oscillator fourth moments
are

    <x^4>_(m=1)=15/4,   <x^4>_(m=3)=75/4.

Consequently the first Rayleigh correction coefficients from (3) are

    E0: -1/4-(15/4)/48=-21/64,
    E1: -1/4-(75/4)/48=-41/64,
    E1-E0: -5/16.                                      (4)

These are exact algebraic coefficients, checked by symbolic Hermite
integration in `check_su2_oscillator_correction.py`. Obtaining the full
asymptotic formulas with controlled remainders requires localization
and spectral comparison; the numerical fit below is not that proof.
The independent IMS/min-max argument supplies the analytic leading
asymptotic. This control is consistent with its class-sector constant 4.

## 3. Rigorous bounds for the untruncated rotor at fixed u

Let P_N retain j=0,...,(N-1)/2 and A_N=P_N H P_N. The first discarded
kinetic eigenvalue is

    kappa_N=N(N+2)/4.

The potential in H is nonnegative, so the discarded compression
`C_N=Q_N H Q_N` obeys `C_N>=kappa_N`. By (1), the only cross-boundary
matrix element is -4u. For any barrier B<kappa_N, the elementary
quadratic-form inequality `2 Re<b,z> >= -||b||²/t-t||z||²`, with
`t=kappa_N-B`, gives

    H >= L_N(B) direct-sum B I_(Q_N),
    L_N(B)=A_N-[16u²/(kappa_N-B)]|last><last|.           (5)

This is an operator-form bound on the full infinite Jacobi operator.
Its compact resolvent follows from the increasing diagonal Casimir
and bounded multiplication potential. If the first two eigenvalues
of L_N(B) are below B, min-max and Rayleigh–Ritz give

    lambda_k(L_N(B)) <= E_k(H) <= lambda_k(A_N),
    k=0,1.                                             (6)

No closeness assumption on the truncated eigenvectors is used. Keeping
N large enough prevents the negative last-row correction from creating
an irrelevant artificial low boundary mode. Here N=max(32,8sqrt(u))
and B=12sqrt(u)+1 at the certified square-integer u values. Exact Sturm
counts independently verify that both comparison eigenvalues lie below B.

For each comparison matrix, floating arithmetic only proposes rational
endpoints. All coefficients and endpoints are then scaled to integers,
and the exact determinant recurrence

    p_0=1,
    p_(n+1)=d_n p_n-b²p_(n-1)

counts eigenvalues by sign changes. The accepted intervals have counts
k and k+1 at their endpoints. Internal zero principal determinants are
handled by omitting zeros from the Sturm sequence; an exact two-mode
control checks that boundary case. The first two full-rotor intervals
then follow from (6), and their differences enclose the untruncated gap.

The resulting exact intervals, displayed as terminating decimals, are:

| u | Character cutoff N | Certified (E1-E0)/sqrt(u) interval |
|---:|---:|---:|
| 1 | 32 | [3.663546, 3.663554] |
| 100 | 80 | [3.9685463, 3.9685471] |
| 10000 | 800 | [3.99687295, 3.99687303] |
| 1000000 | 8000 | [3.999687476, 3.999687484] |

The u=1000000 certificate took about 3.6 seconds in this execution.
These are rigorous fixed-u infinite-rotor enclosures from the form
comparison and exact arithmetic. They are not merely stable finite
cutoff eigenvalues, and they do not prove a uniform asymptotic remainder.
In particular they disprove the literal lower bound `gap>=4sqrt(u)` at
these finite couplings while supporting the leading asymptotic constant.

## 4. Separate numerical cutoff experiment

The numerical scan uses N=max(32,ceil(16u^(1/4))) and 2N, retaining the
first three finite Jacobi eigenvalues. Representative values are:

| u | Numerical gap/sqrt(u) | Maximum scaled two-cutoff discrepancy |
|---:|---:|---:|
| 10 | 3.8990723226023607 | 1.38e-12 |
| 100 | 3.9685466501021844 | 5.93e-13 |
| 10000 | 3.9968729949506354 | 3.69e-14 |
| 1000000 | 3.9996874799770294 | 3.64e-15 |
| 100000000 | 3.999968749797344 | 1.46e-15 |

The last two differences from 4 are consistent with
`-5/(16sqrt(u))`. The exact coefficients in (4) explain that pattern;
the decimal agreement does not establish the remainder. Cutoff
agreement is reported as numerical evidence only.

## 5. Reproduction and program consequence

Run from the checkout with its Python environment:

    python outputs/wilson_complete_band_20260905/check_su2_physical_rotor.py
    python outputs/wilson_complete_band_20260905/extend_su2_rotor_certificate.py
    python outputs/wilson_complete_band_20260905/replay_su2_rotor_certificates.py
    python outputs/wilson_complete_band_20260905/check_su2_oscillator_correction.py

The first two commands generate evidence only in a fresh copy of the
artifact directory without preexisting JSON outputs; they refuse to
overwrite the retained evidence. The replay and oscillator commands run
directly against the existing artifacts. The replay uses the saved exact
endpoints, disables the numerical eigensolver, checks source hashes and
all integer Sturm counts, and verifies that a deliberately corrupted
interval is rejected. It replayed all four fixed-u enclosures successfully.

Artifacts are `su2_physical_rotor_control.json` and
`su2_rotor_1000000_certificate.json`, with the scripts' source hashes and
the numerical software versions retained. Canonical repository records
and the complete-band sealed run were not modified.

This supplies a physical-energy check for an intrinsic fast rotor with
gap growing on the sqrt(u) scale. It supports replacing a misleading
slow configuration-diffusion quantity by the correctly normalized
vertical quantum energy in the next block argument. The remaining
step is to prove that this rotor controls the full chosen fast
complement, including coarse/fast coupling and induced geometry, and
to connect that complement to the physical OS transfer form. No such
identification or continuum Yang–Mills conclusion follows just from
the present class-rotor calculation.
