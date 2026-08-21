# SU(3) fifth-order one-flux mass coefficient

**Status:** PASS  
**Date:** 2026-06-14  
**Expansion variable:** \(u=\beta/6=1/g_H^4\)

## Result

For the one-plaquette \(T_1^{+-}\) branch,

\[
m_{1^{+-}}(u)
=
\frac83+u+\frac{11}{306}u^2
-\frac{109151}{249696}u^3
-\frac{20721577909065127111}{7250590288602460800}u^4
+m_5u^5+O(u^6),
\]

the exact fifth-order rest-energy coefficient is

\[
\boxed{
m_5=
-\frac{866236750503342026253096691057}
{1169668083793811403447133488000}
}
\]

or

\[
m_5\approx -0.740583386437038.
\]

This is the zero-momentum trace coefficient

\[
m_5=\frac13\operatorname{tr}H_5(0).
\]

It does not yet determine the full fifth-order dispersion \(H_5(k)-m_5I\).

## Corrected ordered local algebra

The earlier unordered local census contained 258 final token signatures.  
The actual ordered-transition contraction contains

\[
\boxed{574}
\]

distinct ordered local signatures. The distinction matters because prefix Casimirs depend on the order of the five perturbing insertions.

The corrected determinant-complete local compiler produced:

| object | exact count |
|---|---:|
| ordered local signatures | 574 |
| rank-one local fusion-path tensors | 1,624 |
| maximum invariant-space dimension | 11 |
| final local degree | 7 |
| allowed determinant-dressed families | \((5,2),(2,5),(4,1),(1,4),(3,0),(0,3)\) |
| balanced families | \((2,2),(1,1)\) |

Every local vector is built directly from delta and epsilon invariants. Exact Gram reduction, nested prefix-Casimir diagonalization, orthogonality, completeness, and normalization gates passed.

## Global contraction census

| object | exact count |
|---|---:|
| ordered transitions | 13,276 |
| charge-conjugation orbits | 53,351 |
| trace topologies | 16,071 |
| global fusion-tree paths | 526,805 |
| ordered words with zero complete contribution | 5,075 |

The contraction includes all balanced and determinant-dressed final Haar sectors.

## Fifth-order folded/des-Cloizeaux rule

Let a four-bit word record the four intermediate cuts:

- `0`: a nonresonant \(Q\)-space cut;
- `1`: a return to the one-flux model space \(P\).

After factoring the ordinary Rayleigh--Schrodinger denominator expression, a reversal-symmetric des-Cloizeaux representative uses

| number/pattern of \(P\)-returns | multiplier |
|---|---:|
| `0000` | \(1\) |
| exactly one return | \(1/2\) |
| exactly two returns, nonalternating | \(1/3\) |
| `0101` or `1010` | \(1/12\) |
| exactly three returns | \(1/4\) |
| `1111` | \(0\) |

This rule was generated from Bloch wave-operator recursion followed by exact metric orthonormalization. It reproduces the fifth-order Hermitian effective Hamiltonian on 14 independent rational matrix anchors with model-space dimensions two and three.

Path-level folded redistribution has an affine ambiguity when \(PVP=aP\). The lattice answer is nevertheless unique: the exact pattern sums obey identities that cancel every free redistribution parameter.

## Exact pattern reduction

After the full Haar and geometry contraction, the only independent surviving pattern sums are

\[
C_{0000}
=
-5871724573605720944161941470537/62078801439742312434168960000,
\]

\[
C_{0001}=C_{1000}
=
-68773336105372320795886362345421433/140360170055257368413656018560000,
\]

\[
C_{0101}=C_{0110}=C_{1010}
=
1014252151151/865945728,
\]

and

\[
C_{0111}=C_{1011}=C_{1101}=C_{1110}
=
-18814775285/10391348736.
\]

All other one- and two-return classes vanish exactly. Consequently every valid fifth-order des-Cloizeaux redistribution gives

\[
m_5
=
C_{0000}+C_{0001}
+\frac12C_{0101}+C_{0111},
\]

which reduces to the boxed rational value above.

The individual terms are large, but cancel exactly:

| contribution | decimal |
|---|---:|
| \(C_{0000}\) | -94.585018354538 |
| \(C_{0001}\) | -489.977577529989 |
| \(\tfrac12C_{0101}\) | 585.632631674003 |
| \(C_{0111}\) | -1.810619175913 |
| total \(m_5\) | -0.740583386437 |

## Scale-matched ratio through fifth order

Using the exact Kogut--Pearson--Shigemitsu axial string-tension series in the same variable \(u\),

\[
\frac{m_{1^{+-}}(u)}{\sqrt{\sigma(u)}}
=
\sqrt6\left[
\cdots+c_5u^5+O(u^6)
\right],
\]

with

\[
\boxed{
c_5=
-\frac{10670728893034386567182468628311}
{46786723351752456137885339520000}
}
\]

and therefore the full coefficient of \(u^5\) is

\[
\sqrt6\,c_5\approx -0.558659361011414.
\]

This remains a strong-coupling coefficient, not a continuum extrapolation.

## Validation chain

1. The identical contraction machinery reproduces the certified fourth-order coefficient exactly.
2. The fifth-order local algebra is determinant complete through degree seven.
3. The 526,805 global fusion paths are summed exactly as rational numbers.
4. The folded rule is independently regressed against exact canonical effective Hamiltonians.
5. The final answer is invariant under the full affine family of legal path redistributions.
6. The machine verifier passes every count, pattern identity, folded anchor, and exact rational gate.

## Remaining targets

\[
\boxed{H_5(k)-m_5I}
\]

is still required to determine whether fifth-order mobility vanishes.

The next rest-energy target is

\[
\boxed{m_6=\frac13\operatorname{tr}H_6(0)}.
\]
