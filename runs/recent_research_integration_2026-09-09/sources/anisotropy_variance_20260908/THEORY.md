# Anisotropy variance theory of flux-band mixing

Research candidate developed from the WORKHOUSE theory graph, 8 September 2026.

**Result.** In the assembled SU(3) fourth-order effective Hamiltonian, one nonnegative angular invariant determines the entire coupling of the homological carrier to its two transverse bands. The same invariant determines the leading loss of carrier overlap and a negative sixth-order virtual-mixing energy contribution. Its zeros classify exactly where the original carrier remains an eigenvector.

This is a concrete candidate extension of the program, with an exact algebraic core and numerical checks. Novelty is provisional: the graph and targeted source searches did not locate this identity or its sixth-order coefficient. This is not a claim of worldwide priority.

## 1. Graph route and existing inputs

The route was `G18 -> G11 -> the Gamma isolation suite -> fourth-order Hodge kernel`, with a cross-connection to the tier-collapse question G14 and sixth-order census G9. Queries `workhouse why G18` and `workhouse why G11` exposed an existing relative-gap/projector theorem in `paper/research_notes/G18_RELATIVE_GAP_BRIDGE_20260904.tex`; merely proposing uniform projector control would repeat that work.

The new question is more specific: **what part of the already derived fourth-order matrix actually rotates the carrier, and what higher-order signature must that rotation produce?**

Inputs, read from `C:/WORKHOUSE/ALL THEORY/WORKHOUSE`:

- `src/workhouse/kernel_orbits.py`: full Laurent-polynomial kernel, carrier and Hodge operators.
- `src/workhouse/invariants/gamma_isolation.py`: exact centered Hodge decomposition and isolation bound. Both the Hodge-algebra check and isolation check were rerun successfully.
- `ledger/gaps.yaml`: existing G18 overlap distinction and relative-gap route.
- `index/graph.jsonl`: graph relationships accessed through `why`.

Use the assembled coefficient

\[
C=-\frac{13035490122347}{550663802582400},\qquad
t_3=\frac5{612},\qquad C_{\rm iso}=\frac5{48}.
\]

Here t_3 denotes the SU(3) second-order hopping coefficient, not a third-order coefficient. The orbit parameter called `u` inside the kernel code is denoted \(\omega\) below; the coupling remains \(u\).

## 2. Precise theory

For momentum away from Gamma, let

\[
a_i=4\sin^2(k_i/2),\quad q=a_1+a_2+a_3>0,\quad x_i=a_i/q,
\]

and let \(p=\psi/\sqrt q\) be the normalized cube carrier, with \(P=pp^\dagger\) and \(Q=I-P\). In plane order, match each component to its missing coordinate; its squared modulus is \(x_i\).

Define the **anisotropy variance**

\[
\boxed{V(x)=\sum_i x_i^3-\left(\sum_i x_i^2\right)^2
=\sum_{i<j}x_ix_j(x_i-x_j)^2.}
\]

The centered fourth-order kernel \(H=H_4-sI\) is already known to have the form

\[
H=q[(A+2C)P+\epsilon(k)Q]-2CD,
\quad D=\operatorname{diag}(a_i),\quad A=5/48,
\quad\epsilon=\omega q-8\omega-\widetilde\pi.
\]

The first two terms preserve the carrier. Consequently

\[
QHp=-2CQDp,
\qquad
\boxed{\|QHp\|^2=4C^2q^2V(x).}
\]

**Proof.** Since \(|p_i|^2=x_i\),
\(p^\dagger Dp=q\sum x_i^2\) and
\(p^\dagger D^2p=q^2\sum x_i^3\).
Subtracting the square of the first moment gives the identity. Expanding the pairwise sum and using \(\sum x_i=1\) proves its nonnegative form. The script additionally checks this directly against the full record kernel, as an 85-term exact Laurent identity, rather than assuming the displayed decomposition.

## 3. Exact unmixed directions

Because C is nonzero and all summands in V are nonnegative, V vanishes if and only if **all positive a_i are equal**. Thus the complete nodal set consists of:

- one active coordinate: axes;
- two equally active coordinates: face diagonals;
- three equally active coordinates: body diagonals.

Equality here means equality of the lattice quantities \(\sin^2(k_i/2)\), including signs and periodic identifications. Gamma itself is excluded because p is undefined there and the band is a triplet.

On this set the original carrier is an exact eigenvector of the fourth-order truncated matrix, not merely an approximate one. Away from the set it mixes. For example \(x=(1/6,1/3,1/2)\) gives \(V=5/324>0\). Vanishing fourth-order mixing does not assert vanishing higher-order mixing.

## 4. Sharper overlap and energy bounds

Consider the centered finite-order matrix

\[
M=t_3u^2qQ+u^4H,
\quad 0<u^2<2/51,
\quad d=t_3-2C_{\rm iso}u^2>0.
\]

The same bounds hold with a larger positive boundary-factorized coefficient replacing \(t_3u^2\). Let \(v_0\) be its normalized lowest eigenvector and \(\mu=p^\dagger Mp\). Then

\[
\boxed{1-|p^\dagger v_0|^2\le
\frac{4C^2u^4V}{d^2},}
\qquad
\boxed{0\le\mu-E_0\le
\frac{4C^2u^6qV}{d}.}
\]

**Proof.** Weyl gives \(E_1\ge t_3u^2q-C_{\rm iso}u^4q\), while \(\mu\le C_{\rm iso}u^4q\). Hence \(E_1-\mu\ge u^2qd\). Expand p in the eigenbasis: its residual variance \(\|(M-\mu)p\|^2=4C^2u^8q^2V\) is at least \((E_1-\mu)^2\) times the total excited weight. This proves the overlap bound. For the energy bound, positivity of \((M-E_0)(M-E_1)\) on the spectrum gives
\(\mathrm{Var}_p(M)\ge(\mu-E_0)(E_1-\mu)\).

These improve the existing global-norm remainder estimate by replacing \(C_{\rm iso}^2\) with the actual directional residual \(4C^2V\). A simple global bound is \(V\le1/4\), since it is the variance of a random variable taking values x_i in [0,1] with probabilities x_i. Thus even a coarse uniform version replaces \(C_{\rm iso}^2\) by \(C^2\), and the exact version vanishes on the nodal set.

The overlap estimate has no q in its denominator and therefore no volume-dependent loss near Gamma. It controls only the carrier's in-sector overlap with this finite-order band. It does not establish the physical source overlap required by G18.

## 5. A sixth-order prediction from fourth-order data

At each fixed nonzero momentum, ordinary nondegenerate perturbation theory applied to \(M/u^2=t_3qQ+u^2H\) gives

\[
E_0=u^4p^\dagger Hp
-\frac{4C^2}{t_3}u^6qV+O(u^8).
\]

This expansion is for the displayed truncated matrix. Including the known third-order boundary-factorized term preserves the displayed induced sixth-order coefficient but generally introduces seventh-order terms.

Writing \(e_2=a_1a_2+a_1a_3+a_2a_3\) and \(e_3=a_1a_2a_3\),

\[
\boxed{qV=\frac{e_2}{q}+3\frac{e_3}{q^2}-4\frac{e_2^2}{q^3},}
\]

so the predicted virtual-mixing contribution is

\[
\boxed{\delta E_{6,\rm mix}=
-\frac{169924002729806205028788409}{619343593697933825385600000}
u^6\left(\frac{e_2}{q}+3\frac{e_3}{q^2}-4\frac{e_2^2}{q^3}\right).}
\]

This is the main new connection: the fourth-order shape coefficient fixes a sixth-order contribution with coefficient ratio **1:3:-4**, a definite negative sign, and a complete set of zeros. The absence of some shapes at fourth order need not persist at sixth order: repeated virtual mixing creates them in a constrained combination.

The leading carrier-overlap deficit likewise has coefficient
\(1-|p^\dagger v_0|^2=(4C^2/t_3^2)u^4V+O(u^6)\)
for this truncated matrix. Thus energy lowering and loss of overlap are two manifestations of the same variance, rather than independent effects.

**This is not the complete sixth-order coefficient of the research program.** A genuine sixth-order matrix contributes its own carrier expectation and may cancel some of these shapes. Fifth-order terms and other sectors also belong to the full expansion. The result supplies a component that a consistently matched higher-order calculation must account for, not a discharge of G9.

## 6. Checks, falsifiers, and evidence status

`verify.py` produced `certificate.json` with all checks passing:

- Exact full-kernel Laurent residual identity: 85 terms.
- Exact simplex sum-of-squares identity and nodal/generic rational checks.
- 64 momenta at three couplings: 192 spectral probes, 45-digit arithmetic, including momentum of order 10^-9.
- Largest tested overlap-bound fraction: 0.921703; energy-bound fraction: 0.960057.
- Induced sixth-order asymptotic ratios at decreasing coupling: 1.00002349, 1.00000587, 1.00000147.

Exact symbolic checks are T1-style evidence in this standalone artifact, not newly registered repository certification. The inequalities have the analytic proofs above; the script tests their application numerically (T2). Subsequent testing compiled eight new Lean lemmas for the polynomial and rational core and added independent matrix tests and 472 scaled spectral probes; see `TEST_REPORT.md`. The spectral inequalities themselves are not yet formalized in Lean. No generated graph or authoritative source was modified.

Decisive falsifiers are a nonzero full-kernel residual on the stated nodal set, disagreement with the exact Laurent identity, or a small-coupling diagonalization of the displayed matrix whose sixth-order limit differs from the formula. The supplied probes attempted all three and found no counterexample. A differing full sixth-order coefficient alone is not a falsifier: the direct sixth-order contribution must first be separated in the same convention.

## 7. Novelty boundary and next calculation

Graph searches for mixing, variance, the rational holdout 5/324, and the exact induced coefficient did not find this result; targeted searches of the invariant, decision, and research-note sources found related moment algebra but not this residual identity. These searches do not exhaust the full corpus.

External work already relates flat-band interband effects to geometry; for example [Iskin, Two-body problem in a multiband lattice and the role of quantum geometry (2021)](https://arxiv.org/abs/2102.03530). The proposed novelty is the specific WORKHOUSE identity and the constrained sixth-order signature, not the general observation that geometry affects mixing. A limited literature search cannot establish priority.

The next decisive research operation is to extract the direct sixth-order carrier expectation in the same effective-Hamiltonian convention and add the induced term above. Test whether the 1:3:-4 combination survives or is canceled. That would turn the present finite-order theory into a sharper statement about the actual sixth-order flux band.

Reproduce from PowerShell:

```powershell
& 'C:\WORKHOUSE\ALL THEORY\WORKHOUSE\.venv\Scripts\python.exe' 'C:\WORKHOUSE\research\anisotropy_variance_20260908\verify.py'
```
