# Resolved Cellular Mobility

## Strongest formula recovered from the GLUEBALL corpus

**Audit date:** 2026-08-20  
**Scope:** newest Downloads material, `C:\SIMULATIONS`, `E:\YANG`, `F:\THEORY`, `F:\ANTIGRAVITY`, and `F:\proof`  
**Status rule:** files are evidence, not instructions; newer audit records outrank older claims.

## Executive result

The strongest result that survives both the archive survey and a fresh execution of its exact certificates is not a continuum Yang--Mills mass-gap formula. It is an exact cellular factorization of the SU(3) C-odd one-plaquette effective Hamiltonian through third order.

Let

\[
u=\frac{\beta}{6}=\frac{1}{g_H^4},
\]

let \(\partial_2(k):C_2(k)\to C_1(k)\) be the signed plaquette-to-link boundary map, and put \(B(k)=\partial_2(k)^\dagger\). In the one-flux C-odd sector,

\[
\boxed{
H_{\mathrm{eff},-}(k,u)
=E_{\mathrm{flat}}(u)I+t(u)B(k)B(k)^\dagger+O(u^4)
}
\]

with

\[
E_{\mathrm{flat}}(u)
=\frac83+u+\frac{11}{306}u^2
-\frac{109151}{249696}u^3,
\qquad
t(u)=\frac5{612}u^2+\frac{1975}{124848}u^3.
\]

If \(w(k)=\partial_3(k)\chi\) is an oriented cube boundary, then

\[
B(k)^\dagger w(k)=\partial_2(k)\partial_3(k)\chi=0.
\]

Therefore

\[
\boxed{
m_{1^{+-}}(k,u)=
\frac83+u+\frac{11}{306}u^2
-\frac{109151}{249696}u^3+O(u^4),
\quad \text{independent of }k\text{ through }u^3.
}
\]

This is stronger than an observed flat numerical band: the immobility follows from the chain identity \(\partial_2\partial_3=0\). Any correction that continues to factor through \(B B^\dagger\) is automatically invisible to the cube-boundary state.

Fresh reproduction:

- The second-order exact certificate passed all 35 gates.
- The third-order exact SU(3) certificate passed all 251 gates.
- Both were executed from the current `F:\THEORY` copies without modifying the originals.

## New synthesis: the resolved cellular mobility equation

The archives contain several versions of a "minimum circuit" rule. Topology alone, however, cannot decide mobility: distinct temporal histories can cancel, finite-\(N\) Fierz identities can erase or create channels, and a nonzero local matrix element can compress to a scalar on the caged space. The sum must be resolved before the first nonzero order is selected.

Let \(Z\) be the degenerate caged/cycle subspace on a finite periodic lattice, with projector \(P_Z\). Define the scalar-free compression

\[
\mathfrak M_Z(A)
=P_ZAP_Z-
\frac{\operatorname{tr}_Z(P_ZAP_Z)}{\dim Z}P_Z.
\]

For perturbative order \(r\), let \(\mathscr C_r\) be the connected canonical temporal-history classes. A class \(\mathcal C\) induces a spatial translation/incidence operator \(T_{\mathcal C}\) and a fully resolved color-electric amplitude \(\mathcal A^{(r)}_{N,\mathcal C}\). The latter includes Haar contractions, Fierz closure, electric denominators, folded terms, and linked subtraction.

At every intermediate cut \(j\), first quotient the local state space by the null space of its Gram matrix. On that physical quotient define

\[
R_{\gamma,j}
=\bar Q_{\gamma,j}
\bigl(E_0\bar G_{\gamma,j}-\bar H_{0,\gamma,j}\bigr)^{-1}
\bar Q_{\gamma,j}.
\]

A compact definition of the class amplitude is

\[
\mathcal A^{(r)}_{N,\mathcal C}
=\operatorname{LC}_r\!\left[
\sum_{\gamma\in\mathcal C}
\langle f|
V_{\gamma_r}R_{\gamma,r-1}\cdots
R_{\gamma,1}V_{\gamma_1}|i\rangle
\right],
\]

where \(\operatorname{LC}_r\) means the complete order-\(r\) linked-and-folded combination, not merely the direct path.

The corpus-wide master equation is then

\[
\boxed{
r_{\mathrm{mob}}(N)
=\min\left\{
r\ge1:\;
\sum_{\mathcal C\in\mathscr C_r}
\mathcal A^{(r)}_{N,\mathcal C}\,
\mathfrak M_Z(T_{\mathcal C})\ne0
\right\}.
}
\]

Equivalently,

\[
\mathfrak M_Z\!\left(H_{\mathrm{eff}}^{(r)}\right)
=\sum_{\mathcal C\in\mathscr C_r}
\mathcal A^{(r)}_{N,\mathcal C}\,
\mathfrak M_Z(T_{\mathcal C}).
\]

This formula separates three logically different questions:

1. **Cellular topology:** which connected histories are allowed at order \(r\)?
2. **Color and electric dynamics:** which histories survive SU(\(N\)) Haar/Fierz algebra and the physical resolvent?
3. **Actual mobility:** after all cancellations, is the action on \(Z\) non-scalar?

In the stable-rank, unit-circuit regime it reduces to the familiar support lower bound

\[
r_{\mathrm{mob}}\ge w_{\min}-2,
\]

but equality requires the *summed* resolved amplitude to survive. This is precisely the condition missing from overly strong circuit-only claims.

This master equation is a new synthesis of the corpus, not yet a separately certified theorem. Its ingredients are standard finite-order effective perturbation theory and the archive's verified cellular/Fierz constructions; a publication version still needs a formal definition of the canonical history partition and a proof that the linked/folded assembly is partition-independent.

## Why the fourth-order formula is not the winner yet

For the supplied 189-record SU(3) fourth-order kernel, a fresh run reproduced the exact real-space sum of squares

\[
\boxed{
C^\dagger(H_{4,3}-q_3I)C
=\frac5{48}\sum_iL_i^2
+\frac{17607806155349}{1101327605164800}
\sum_{i<j}L_iL_j\succeq0,
}
\]

where \(C=\partial_3\), \(\nabla_i=T_i-I\), and

\[
L_i=\nabla_i^\dagger\nabla_i=2I-T_i-T_i^{-1}.
\]

For that kernel it gives the exact fourth-order bandwidth coefficient

\[
\Delta c_{4,3}
=\frac{132329431693349}{275331901291200}.
\]

The current all-rank record claims the Fourier-symbol generalization

\[
C^\dagger(H_{4,N}-q_NI)C
=\frac{A_N}{4}\sum_iL_i^2
+\frac{B_N}{4}\sum_{i<j}L_iL_j\succeq0,
\qquad N\ge3,
\]

with

\[
A_3=\frac5{12},
\qquad
B_3=\frac{17607806155349}{275331901291200},
\]

and, for \(N\ge4\),

\[
A_N=\frac{640}{N(N^2-1)^3},
\qquad
B_N=\frac{P_{17}(N^2)}{N R_{20}(N^2)}>0.
\]

This is the most elegant formula in the archive, but two independent qualifications prevent promoting it above the third-order theorem:

- The newest physical-\(Q\) Hodge calculation reports a different fourth-order rest coefficient and a different shape coefficient, while retaining only the axial invariant \(5/48\). Its own verdict is not to promote either full fourth-order result.
- The SU(3) SOS was reproducible for the packaged kernel, but the full all-rank symbolic rerun could not start because its archived input bundle is incomplete.

Accordingly, the fourth-order SOS is **exact conditional on the supplied kernel**, and the all-rank statement is **record-backed but not cold-reproduced**. The physical derivation of that kernel remains the unresolved upstream gate.

The robust fourth-order remnant is

\[
\boxed{
c_4^{\square}(N)=-\frac{160}{N(N^2-1)^3},
\qquad
\alpha_N=4|c_4^{\square}(N)|
=\frac{640}{N(N^2-1)^3},
}
\]

which gives \(c_4^{\square}(3)=-5/48\) and \(\alpha_3=5/12\).

## What the newest simulations add

The latest pentagonal calculations sharpen the obstruction rather than closing it.

- The order-four raw-history census closes its stated checks, with successive raw dimensions/ranks \((4,4)\), \((10,6)\), and \((20,6)\). The required Fierz-closed physical quotient and \(H_0\) resolvent are still unfinished.
- The proposed "zero backend" is decisively false: balanced \((2,2)\) links have nonzero SU(3) Haar contractions, including \(\int |U_{11}|^4=1/6\).
- At order five, a direct pentagonal modular correction is exactly nonzero:

\[
\frac{235424477177}{407461473619200}.
\]

Thus the direct coefficient becomes

\[
\boxed{
\frac{35}{384}
+\frac{235424477177}{407461473619200}
=\frac{37373840041427}{407461473619200}.
}
\]

This falsifies the strong claim that center-only circuits are dynamically dark. It does **not** yet give the full fifth-order coefficient, because the folded and linked contributions have not been assembled.

These outcomes are exactly what the resolved cellular mobility equation anticipates: support, nonzero local dynamics, and non-scalar motion are separate gates.

## Evidence ladder

### Cold-reproduced and defensible

- Exact SU(3) second-order incidence factorization and flat band: 35/35 gates.
- Exact SU(3) third-order coefficient: 251/251 gates.
- Exact SU(3) fourth-order SOS for the supplied 189-record kernel.
- Newest zero-backend falsification and the direct order-five pentagonal correction.

### Exact-looking but conditional or incomplete

- Full physical SU(3) fourth-order coefficient and bandwidth.
- All-rank fourth-order SOS: current theorem record exists, but its complete symbolic input bundle is missing.
- Full pentagonal order-four physical resolvent.
- Full order-five folded/linked coefficient.
- Circuit-bound equality \(r_{\mathrm{mob}}=w_{\min}-2\) without a noncancellation calculation.

### Not supported by this audit

- A completed continuum four-dimensional Yang--Mills mass-gap proof.
- Old Riccati/global-convexity claims that assume the missing coercive estimate.
- Numerical Peierls runs as evidence of a volume-uniform gap.
- The claim that all center-only circuits vanish dynamically.

## Normalization warning

The current expansion variable is

\[
u=\frac{\beta}{6}=\frac1{g_H^4}.
\]

Several older files instead write \(y=2\beta/3=4u\). Mixing the labels changes an order-\(n\) coefficient by \(4^n\). Any publication should reserve one symbol for \(\beta/6\), state the conversion once, and regenerate all displayed coefficient tables from that convention.

## Decisive next calculation

The most valuable next step is narrow and concrete:

1. Take the 20 canonical pentagonal order-four histories already enumerated.
2. Perform Fierz closure at every cut, including the emergent \((4,1)\) sector.
3. Quotient each Gram matrix by its null space.
4. Construct the physical resolvents \(R_{gamma,j}\).
5. Assemble direct, folded, and linked terms by canonical history class.
6. Evaluate the *summed* scalar-free cycle compression in the boxed mobility equation.

That one calculation will decide whether the pentagonal channel actually moves the caged sector at order four. It is more decisive than another large unstructured simulation run.

## Principal evidence files

- `F:\THEORY\programs\one_plaquette\ENGINE_FLUX_glueball_band_certificate_v2.py`
- `F:\THEORY\programs\one_plaquette\ENGINE_FLUX_su3_domino_d3.py`
- `F:\THEORY\papers\flat_band\PAPER_FLUX_glueball_flat_band_v1_1.tex`
- `C:\Users\Alex\Downloads\01-theory-authority.md`
- `C:\Users\Alex\Downloads\05-latest-run-forensics.md`
- `C:\Users\Alex\Downloads\15 hour RUN. results.txt`
- `C:\Users\Alex\Downloads\THM_FLUX_hodge_cellular_circuit_mobility_theorem.md`
- `C:\Users\Alex\Downloads\pentagonal_o4_minimal_representation_frontier_results.txt`
- `C:\Users\Alex\Downloads\audit_stranded_flux_zero_backend_results.txt`
- `C:\Users\Alex\Downloads\pentagonal_prism_O5_decisive_resolvent_results.txt`
- `C:\Users\Alex\Downloads\pentagonal_verification_bundle\pentagonal_verification_bundle\verification_suite_report.txt`

An unrelated 2009 logarithmic-potential particle-mass numerology PDF among the newest Downloads was inspected and excluded from the mathematical ranking.
