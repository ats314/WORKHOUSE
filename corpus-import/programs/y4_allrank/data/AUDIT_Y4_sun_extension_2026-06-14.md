# SU(N) extension audit for the fourth-order \(T_1^{+-}\) band

**Date:** June 14, 2026  
**Status:** Stable-rank geometry and denominator layer proved for integer \(N\ge 7\); symbolic contraction layer open.

## 1. Source recovery verdict

The uploaded `y4_complete_from_scratch` notebook contains the complete self-contained
SU(3) pipeline:

\[
\text{Stage 0}\to\text{Stage 1}\to\text{Stage 2}
\to\text{Stage 3B}\to\text{3C}\to\text{3E}
\to\text{3G}\to\text{3I}\to\text{3J}.
\]

It includes the previously missing Stage-3I generator
`y4_stage3i_complete_folded_descloizeaux.py`, which creates

```text
y4_complete_folded_word_weights.json.gz
```

and Stage 3J then creates the 189-record real-space kernel.

The notebook run terminates with the exact verdict

\[
\text{flat through }O(y^3),\qquad
\text{first nonzero bandwidth at }O(y^4).
\]

Thus the SU(3) provenance chain is no longer missing.

## 2. Which stages are group-independent

| Stage | Role | \(SU(N)\) status |
|---|---|---|
| 0 | connected plaquette geometry and cubic quotient | reusable after replacing triality by \(N\)-ality |
| 1 | representation channels and electric denominators | group-specific; replaced here for stable rank |
| 2 | local Haar projectors | group-specific; symbolic balanced formulas known |
| 3B | time-ordered channel graph | group-specific; stable bipartition version now available |
| 3C | explicit carrier/projector matrices | SU(3)-specific and must be replaced |
| 3E | trace-index wiring | essentially group-independent |
| 3G | local fusion-tree tensor contraction | SU(3)-specific and must be replaced |
| 3I | folded/des-Cloizeaux assembly | reusable once symbolic tensors and denominators are supplied |
| 3J | real-space kernel and flat-vector projection | reusable, with rational functions of \(N\) replacing rationals |

The principal remaining bottleneck is therefore not the geometry or folded
effective-Hamiltonian algebra. It is the symbolic replacement for Stages 3C and 3G.

## 3. Stable-rank theorem

The complete fourth-order geometry has maximum local tensor degree six. For a local
tensor containing \(n_f\) fundamental and \(n_{\bar f}\) antifundamental factors,
an \(SU(N)\) singlet requires

\[
n_f-n_{\bar f}\equiv 0\pmod N.
\]

For integer \(N\ge7\),

\[
|n_f-n_{\bar f}|\le6<N,
\]

so singlet feasibility is equivalent to

\[
n_f=n_{\bar f}.
\]

Therefore:

> **Stable-rank local-invariant theorem.** At fourth order and for every
> \(SU(N)\) with \(N\ge7\), all determinant/epsilon sectors vanish. The complete
> local Haar problem consists only of the balanced families
> \((1,1),(2,2),(3,3)\).

The exceptional ranks are:

- \(N=3\): epsilon sectors at degree 3 and double-epsilon sectors at degree 6;
- \(N=4\): possible determinant sectors at degree 4;
- \(N=5\): possible determinant sectors at degree 5;
- \(N=6\): possible determinant sectors at degree 6;
- \(N=2\): pseudoreality and charge conjugation require separate treatment.

Consequently, a universal theorem should be organized as a stable-rank theorem
for \(N\ge7\), followed by finite exceptional-rank appendices.

## 4. Exact stable-rank local Haar coefficients

For \(N\ge7\), the only required Weingarten coefficients are

\[
\operatorname{Wg}_1(e)=\frac1N,
\]

\[
\operatorname{Wg}_2(e)=\frac1{N^2-1},
\qquad
\operatorname{Wg}_2((12))
=-\frac1{N(N^2-1)},
\]

and

\[
\operatorname{Wg}_3(e)
=
\frac{N^2-2}{N(N^2-1)(N^2-4)},
\]

\[
\operatorname{Wg}_3((12))
=
-\frac1{(N^2-1)(N^2-4)},
\qquad
\operatorname{Wg}_3((123))
=
\frac2{N(N^2-1)(N^2-4)}.
\]

These reproduce the SU(3) balanced coefficients
\(1/3\), \(1/8\), \(-1/24\), \(7/120\), \(-1/40\), and \(1/60\).

## 5. Stable-rank representation channels

Use bipartitions \((\lambda,\mu)\) for the stable mixed-tensor irreducibles.
Tensoring by the fundamental obeys

\[
(\lambda,\mu)\otimes V
=
\bigoplus_{\lambda+\square}(\lambda+\square,\mu)
\oplus
\bigoplus_{\mu-\square}(\lambda,\mu-\square),
\]

while tensoring by the antifundamental exchanges \(\lambda\) and \(\mu\).

The exact quadratic Casimir is

\[
\boxed{
C_2(\lambda,\mu)
=
\frac{
N^2(|\lambda|+|\mu|)
+N[\kappa(\lambda)+\kappa(\mu)]
-(|\lambda|-|\mu|)^2
}{2N}
}
\]

with

\[
\kappa(\lambda)
=
\sum_{i\ge1}\lambda_i(\lambda_i+1-2i).
\]

The electric energy of a link is \(C_2/2\). Therefore every intermediate
denominator is an explicit rational function of \(N\).

## 6. Exact stable-rank Stage-1 certificate

A fresh exact scan of the 182,440 connected supports gives:

| Quantity | Exact count |
|---|---:|
| Candidate support/output pairs | 895,524 |
| Stable support/output classes | 439 |
| Canonical ordered words | 4,171 |
| Exact-balance sign assignments | 33,500 |
| Charge-conjugation orbits | 16,750 |
| Unique balanced token signatures | 140 |
| \((1,1)\) tensor occurrences | 173,520 |
| \((2,2)\) tensor occurrences | 13,140 |
| \((3,3)\) tensor occurrences | 400 |
| Symbolic energy signatures | 37,500 |
| Resonant energy signatures | 17,073 |
| Nonresonant energy signatures | 20,427 |
| All-resonant orbits | 7,452 |
| Mixed orbits | 2,673 |
| Nonresonant-only orbits | 6,625 |
| Distinct denominator polynomials | 94 |
| Accidental integer denominator roots for \(N\ge7\) | 0 |

The stable bipartition engine was evaluated at \(N=3\) and compared against the
existing SU(3) \((p,q)\) channel engine on all 140 balanced token signatures.
There were zero mismatches.

### Canonical-frame correction

The sign mask must be recomputed after an ordered transition is rotated into its
canonical frame. Carrying the pre-rotation mask through the cubic rotation can
mislabel the signs because the orientation of a canonical plane can change.
The final SU(3) pipeline remains correct because Stage 1 independently rejects
such assignments. The stable-rank certificate removes the issue at the source.

## 7. Kinematic factorization is group-independent

Let

\[
D_N(k)
=
\psi(k)^\dagger[H_{4,N}(k)-q_NI]\psi(k),
\]

where \(\psi\) is the cube-boundary flat vector. Suppose the rank-\(N\) kernel
has the same geometry-derived properties as the SU(3) kernel:

1. exact Hermiticity;
2. cubic covariance and independent reflections;
3. displacement support restricted to unit axes, double axes, and two-axis
   diagonals;
4. \(H_{4,N}(0)=q_NI\).

Then the most general invariant Fourier polynomial is

\[
D_N(k)
=
c_0+c_1\sum_i\cos k_i
+c_2\sum_i\cos2k_i
+c_3\sum_{i<j}
[\cos(k_i+k_j)+\cos(k_i-k_j)].
\]

Because \(\psi(k)=O(k)\) and \(H_{4,N}(k)-q_NI=O(k)\),

\[
D_N(k)=O(|k|^3).
\]

Reflection symmetry makes \(D_N\) even, so in fact

\[
D_N(k)=O(|k|^4).
\]

Consequently its constant and quadratic Taylor terms vanish. Writing

\[
X_i=1-\cos k_i,
\]

the Fourier polynomial must reduce exactly to

\[
\boxed{
D_N(k)
=
A_N\sum_iX_i^2+
B_N\sum_{i<j}X_iX_j.
}
\]

Thus the two-invariant factorization is not an SU(3) numerical accident. It is
forced by the group-independent geometry and symmetry, provided the four listed
kernel gates hold.

The coefficients can be extracted without fitting:

\[
A_N=c_{4,N}(X)-c_{4,N}(\Gamma),
\]

\[
B_N
=
2[c_{4,N}(M)-c_{4,N}(X)]
=
c_{4,N}(R)-c_{4,N}(X).
\]

The equality of the two expressions for \(B_N\) is an exact consistency gate.

## 8. Remaining computation

The next load-bearing task is a symbolic balanced contraction engine for
Stages 3C/3G. The efficient representation is the walled-Brauer diagram basis,
not explicit \(SU(N)\) carrier matrices.

The required output is only

\[
q_N,\qquad A_N,\qquad B_N,
\]

as rational functions of \(N\), together with gates

\[
A_N>0,\qquad B_N>0
\]

for every integer \(N\ge7\). These signs would immediately prove the unique
minimum at \(\Gamma\), unique maximum at \(R\), and bandwidth

\[
\Delta c_{4,N}=A_N+B_N.
\]

## 9. Current status

\[
\boxed{
\text{SU(3) fourth-order theorem: proved}
}
\]

\[
\boxed{
\text{Stable-rank }SU(N\ge7)\text{ geometry and denominators: proved}
}
\]

\[
\boxed{
\text{Stable-rank symbolic contraction and }A_N,B_N:
\text{ open}
}
\]
