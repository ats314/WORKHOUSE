# $T_1^{+-}$ flat-band theorem — rank-complete fourth order and SU(3) fifth order

**Date:** June 14, 2026
**Manuscript target:** `glueball_flat_band_paper_v0_8.tex`
**Status of all components:** see §13

**Scope.** Sections 1–8 give the **rank-complete fourth-order** theorem for all
integer $N\ge3$. Section 9 gives the **SU(3) fifth-order** band, continuing the
$N=3$ story from $O(u^4)$ to $O(u^5)$, together with the scale-matched mass /
string-tension ratio and the state of the sixth-order ($m_6$) calculation. The
fourth-order results hold for all ranks; the fifth-order results are SU(3) only.

---

## 1. Setup and notation

Let $H_\beta$ be the Kogut–Susskind Hamiltonian for pure $SU(N)$ gauge theory,

$$
H_\beta = \frac{1}{2}\sum_\ell C_2(\ell)
+ \beta\sum_p\!\left(1-\tfrac{1}{N}\operatorname{Re}\operatorname{Tr}U_p\right).
$$

The natural strong-coupling expansion variable is

$$
\boxed{u = \frac{\beta}{6} = \frac{1}{g_H^4}.}
$$

The perturbation is $-u(\chi_p+\bar\chi_p)$ per plaquette, and the
expansion variable is the coefficient of each plaquette character insertion.
All rest-energy and band coefficients in this document are in powers of $u$.

> **Coupling note (v0.7 correction).** The manuscript draft v0.7 defines
> $Y=2\beta/3$, which equals $4u$. The source chain contracts unit insertions of
> $-(\chi+\bar\chi)$, so its natural variable is $u$, not $Y$. Every printed
> coefficient is valid as written provided the variable is relabeled $y:=u=\beta/6$.
> No coefficient values change; only the definition line is corrected.

The one-flux $T_1^{+-}$ sector is the unique sector with charge conjugation
$C=-$, time reversal $T=+$, parity $P=+$, and one unit of fundamental flux
on an axis-aligned cube boundary.

Let $\psi(k)$ be the cell/origin-gauge flat vector

$$
\psi(k) = \bigl(e^{ik_z}-1,\;-(e^{ik_y}-1),\;e^{ik_x}-1\bigr)^T,
\qquad \|\psi(k)\|^2 = 2S,
\quad S = \sum_i X_i,\quad X_i = 1-\cos k_i.
$$

The dispersion relation at order $n$ is

$$
c_{n,N}(k) = \frac{\psi(k)^\dagger H_{n,N}(k)\,\psi(k)}{\|\psi(k)\|^2}.
$$

> **Notation convention (read before §9).** Band coefficients are written
> $q,A,B$ with a single integer subscript whose meaning depends on the part
> of the document:
> - In **§§1–8** (fourth order, all ranks) the subscript is the **gauge rank
>   $N$**, with coupling order fixed at $4$: $q_N,A_N,B_N$.
> - In **§9** (fifth order, SU(3) only) the gauge rank is fixed at $N=3$ and
>   the subscript is the **coupling order $n$**: $q_5,A_5,B_5$ are the
>   *fifth-order* coefficients of the SU(3) band, matching the source-bundle
>   notation.
>
> Consequently the symbol $q_5$ denotes **two different quantities**: the
> SU(5) fourth-order rest energy in §5.5
> ($-781009569168365268247626732239/6484474594581730088957376233472$) and the
> SU(3) fifth-order rest mass in §9
> ($-866236750503342026253096691057/1169668083793811403447133488000$). Each
> occurrence is tagged in place. No fourth-order rank-$5$ value of $A$ or $B$
> is instantiated symbolically, so $A_5,B_5$ appear only as fifth-order
> SU(3) quantities.

---

## 2. SU(2): C-odd sector vanishes identically

**Theorem (SU(2) exclusion).** *There is no $SU(2)$ one-flux $T_1^{+-}$ branch.*

**Proof.** In $SU(2)$ every fundamental matrix satisfies $U^*=\varepsilon U\varepsilon^{-1}$
with $\varepsilon=i\sigma_2$. The constant gauge transformation $g_x=\varepsilon$
at every vertex maps $U_{xy}\mapsto U_{xy}^*$, so charge conjugation is a
gauge transformation. Gauge transformations act trivially on the physical
Hilbert space, hence $C=I$ and $P_{C=-}=0$. $\square$

**Consequence.** The coefficients $q_2$, $A_2$, $B_2$ are undefined; the
theorem domain is $N\ge3$.

---

## 3. Degree-six rank classification

At fourth order each link carries at most six fundamental/antifundamental
factors ($r_\ell+s_\ell\le6$). A local $SU(N)$ invariant requires

$$
r_\ell - s_\ell \equiv 0\pmod{N}.
$$

The balanced component ($r_\ell=s_\ell$) is represented by walled-Brauer
pairings; nonzero-$N$-ality components are determinant-dressed, with
finite-rank linear dependencies removed by the exact Gram quotient.

The rank selector

$$
\mathbf{1}_{N\mid\nu} = \frac{1}{N}\sum_{a=0}^{N-1}e^{2\pi i a\nu/N}
$$

is the exact admissibility gate; it is not the Haar projector.

**Classification by rank:**

| Rank | Exceptional sectors | Effect on band |
|:---:|---|---|
| $N=2$ | $C=+$ only (gauge identity) | $T_1^{+-}$ sector is empty |
| $N=3$ | $\nu=\pm3,\pm6$ | modifies both $q_3$ and $B_3$ |
| $N=4$ | $\nu=\pm4$ | modifies $q_4$ only |
| $N=5$ | none (scan of 895,524 pairs) | balanced formulas exact |
| $N=6$ | $\nu=\pm6$ (one orbit) | modifies $q_6$ only |
| $N\ge7$ | none | balanced formulas exact |

---

## 4. Exact fourth-order band formula

**Theorem (rank-complete projected band).** *For every integer $N\ge3$ and
every nonzero momentum $k$,*

$$
\boxed{
c_{4,N}(k) = q_N + \frac{A_N\displaystyle\sum_i X_i^2 + B_N\displaystyle\sum_{i<j}X_iX_j}{2\displaystyle\sum_i X_i},
\qquad X_i = 1-\cos k_i,
}
$$

*with continuous value $q_N$ at $\Gamma$. The axial coefficient is universal,*

$$
\boxed{A_N = \frac{640}{N(N^2-1)^3}}\qquad(N\ge3).
$$

*The diagonal coefficient is*

$$
\boxed{
B_N = \begin{cases}
\dfrac{17607806155349}{275331901291200}, & N=3,\\[1.4ex]
\dfrac{P_{17}(N^2)}{N\,R_{20}(N^2)}, & N\ge4,
\end{cases}
}
$$

*where the integer-coefficient ledgers for $P_{17}$ and $R_{20}$ are
in* `B_BAL_REDUCED_P17_R20_CERTIFICATE.json`. *For the stable symbolic
formula at $N\ge7$, see §6.*

**Provenance notes:**
- $A_N$ is universal: $\Delta A_N = 0$ at every rank, so the axial coefficient
  equals the balanced value $640/[N(N^2-1)^3]$ for all $N\ge3$. This is a
  certified fact, not a consequence of the exceptional kernels being scalar —
  they are scalar at $N=4,6$ (shifting only $q_N$) but **not** at $N=3$, where
  the epsilon sectors also shift $B_3$ (§5.1). In every case the exceptional
  contribution has vanishing projection onto the axial $\sum_iX_i^2$ channel,
  leaving $A_N$ untouched. The closed form follows from direct walled-Brauer
  contraction of 140 balanced electric-history groups.
- $B_N$ at $N=3$ is the **full** SU(3) value including epsilon-sector
  corrections (see §5.1); the exceptional sectors are non-scalar here.
- $B_N$ at $N\ge4$ is the balanced walled-Brauer formula. The exceptional
  corrections at $N=4,6$ are scalar and affect $q_N$ only (§5).
- At $N=5$ the balanced formula equals the full result.

---

## 5. Exceptional finite-rank corrections

### 5.1 SU(3): epsilon sectors modify $q_3$ and $B_3$

The balanced walled-Brauer formula at $N=3$ gives

$$
B_3^{\rm bal} = \frac{15644916262153}{34416487661400},
$$

but the full SU(3) result including $\nu=\pm3,\pm6$ epsilon sectors is

$$
B_3^{\rm full} = \frac{17607806155349}{275331901291200}.
$$

The epsilon-sector correction to the band shape is

$$
\boxed{\Delta B_3 = B_3^{\rm full} - B_3^{\rm bal} = -\frac{25}{64}.}
$$

The correction to the rest energy is

$$
\boxed{\Delta q_3 = -\frac{16863189551}{76406976000}.}
$$

Hence the claim that all determinant sectors modify only $q_N$ is false.
It is true for $N\ge4$ but not for $SU(3)$.

### 5.2 SU(4): scalar exceptional kernel

$$
H_{4,4}^{\rm exc}(k)\,\psi(k) = -\frac{304746539168}{160249753125}\,\psi(k),
\qquad \Delta q_4 = -\frac{304746539168}{160249753125},\quad \Delta A_4 = \Delta B_4 = 0.
$$

Note: the exceptional kernel is scalar on the closed-surface branch, not on
the full three-component plaquette space.

### 5.3 SU(5): no exceptional sectors

The complete 895,524-pair scan finds no modulo-5-only assignments:
$H_{4,5} = H_{4,5}^{\rm bal}$.

### 5.4 SU(6): scalar exceptional kernel

$$
\Delta H_{4,6}(k) = \frac{6}{343}I_3,\qquad
\Delta q_6 = \frac{6}{343},\qquad \Delta A_6 = \Delta B_6 = 0.
$$

### 5.5 Exact rest energies at exceptional ranks

These are the fourth-order ($O(u^4)$) rest energies $q_N=c_{4,N}(\Gamma)$ at
gauge ranks $N=3,4,5,6$. (The $N=5$ entry $q_5$ here is **not** the SU(3)
fifth-order rest mass of §9; see the notation convention in §1.)

$$
q_3 = -\frac{20721577909065127111}{7250590288602460800},
$$

$$
q_4 = -\frac{162485785670299274695454289332603}{121294607143027203361265133093750},
$$

$$
q_5 = -\frac{781009569168365268247626732239}{6484474594581730088957376233472},
\qquad(\text{SU(5), fourth order})
$$

$$
q_6 = -\frac{55954617740619111266546735567327219227}{2665788121217129017242143775195086906250}.
$$

**Important:** $q_N^{\rm bal}$ at exceptional rank denotes the direct
finite-rank balanced contraction, not the analytic continuation of the
stable rational formula. This distinction is essential at $N=4$, where
the stable rational formula has a pole although the direct contraction is
finite.

---

## 6. Stable-rank symbolic formulas ($N\ge7$)

For all integer $N\ge7$, the balanced walled-Brauer contraction produces
exact closed-form rational functions of $N$.

### 6.1 Rest energy $q_N$

Set $z=N^2$:

$$
\boxed{q_N = -\frac{2}{3N}\frac{Q_{32}(z)}{D_{34}(z)}.}
$$

The denominator factorizes as

$$
D_{34}(z) = (z-16)(z-9)^3(z-4)(z-1)^3(2z-3)(2z-1)^3(3z-2)(3z-1)
(4z-25)(4z-9)^3(4z-7)(4z-5)(4z-3)(4z-1)(9z-25)
$$
$$
\times(9z-16)(16z-49)(16z-25)(16z-9)(16z-1)(4z^2-16z+9)
(16z^2-44z+25)(16z^2-33z+16).
$$

Every factor is positive for $z=N^2\ge49$. The numerator has the
Newton expansion

$$
Q_{32}(z) = \sum_{j=0}^{32}b_j\binom{z-49}{j},\qquad b_j>0,
$$

so $Q_{32}>0$ and $q_N<0$ for every integer $N\ge7$.
The 33 exact integers $b_j$ are in the machine-readable ledgers.

### 6.2 Axial coefficient $A_N$

The closed-form expression from §4 applies directly:

$$
A_N = \frac{640}{N(N^2-1)^3} > 0\qquad(N\ge7).
$$

### 6.3 Diagonal coefficient $B_N$

The stable contraction reduces to 743 electric-history groups. Writing the
result as a rational function of $N$ (polynomial degree 402 over degree 409):

$$
B_N = \frac{P_{402}(N)}{D_{409}(N)}.
$$

Every irreducible factor of $D_{409}$ is positive for $N\ge7$. The numerator
satisfies

$$
P_{402}(N) = \sum_{j=0}^{402}a_j\binom{N-7}{j},\qquad a_j>0,
$$

so $B_N>0$ for every integer $N\ge7$.
The complete 403-coefficient ledger is bundled with hashes.

### 6.4 Contraction census

| Object | Count |
|---|---:|
| Stable ordered words | 4,171 |
| Charge-conjugation orbits | 16,750 |
| Balanced local signatures | 140 |
| Local joint-Casimir path tensors | 330 |
| Trace topologies | 3,850 |
| Global fusion paths | 35,130 |
| $q_N$-contributing paths | 27,202 |
| $A_N$-contributing paths | 950 |
| $B_N$-contributing paths | 13,096 |

### 6.5 Stage-3G implementation (v0.8 addition)

The trace networks in Stage 3G are evaluated by exact **partition/loop
dynamic programming**, not by numerical $SU(N)$ color matrices. The
standalone trace-wiring contractor passed all **147 self-tests**, including:

- $\mathbb{E}|\operatorname{Tr}U|^2=1$, $\mathbb{E}|\operatorname{Tr}U|^4=2$, $\mathbb{E}|\operatorname{Tr}U|^6=6$;
- two-link connected and disconnected pairings;
- 140/140 local signature/path interfaces;
- global charge-conjugation invariance;
- fourth-order folded-coefficient permutation symmetry.

The coefficient extraction formulas from the targeted Stage-3G reduction are:

$$
A_N = 4\bigl[C^\dagger H_{4,N} C\bigr]_{2e_0},\qquad
B_N = 4\bigl[C^\dagger H_{4,N} C\bigr]_{e_0+e_1},
$$

where $C$ is the cubic-symmetry basis matrix and $e_0$, $e_1$ label the
two invariant parity-point orbits. The identity $2(c_M-c_X)=c_R-c_X$ is
an exact consistency gate for $B_N$.

---

## 7. Global band theorem

**Theorem.** *For every integer $N\ge3$,*

$$
A_N > 0,\qquad B_N > 0.
$$

*Therefore $\Gamma=(0,0,0)$ is the unique global minimum of $c_{4,N}(k)$,
$R=(\pi,\pi,\pi)$ is the unique global maximum, and*

$$
\boxed{\Delta c_{4,N} = A_N + B_N > 0.}
$$

**Proof sketch.**
- $A_N>0$: immediate from the closed form $640/[N(N^2-1)^3]$ with $N\ge3$.
- $B_N>0$ at $N=3$: direct inspection of the exact rational.
- $B_N>0$ at $N=4,5,6$: direct inspection of exact rationals from
  determinant-complete finite-rank contractions.
- $B_N>0$ at $N\ge7$: positive Newton expansion with 403 non-negative
  integer coefficients about the base point $N=7$.

The minimum/maximum characterization follows because both $X_i\ge0$ and
both coefficients are positive, so $D_N(k)\ge0$ with equality only at
$\Gamma$, and $D_N(k)\le(A_N+B_N)\cdot2\sum_iX_i/(2\sum_iX_i)=A_N+B_N$
with equality only at $R$. $\square$

**Rank-unified structural summary:**

$$
\boxed{
\begin{aligned}
A_N &= \frac{640}{N(N^2-1)^3} && (N\ge3),\\[6pt]
B_N &= B_N^{\rm bal} && (N\ge4),\\[6pt]
B_3 &= B_3^{\rm bal} - \tfrac{25}{64},\\[6pt]
q_N &= q_N^{\rm bal} + \Delta q_N^{\rm exc},
\end{aligned}
}
$$

where $q_N^{\rm bal}$ and $B_N^{\rm bal}$ denote direct balanced
fixed-rank contractions at exceptional ranks, and
$\Delta q_N^{\rm exc}$ is the scalar shift from determinant sectors
(zero for $N=5$ and $N\ge7$).

---

## 8. Exact large-$N$ asymptotics (new in v0.8)

**Corollary.** *As $N\to\infty$ through integers $N\ge7$,*

$$
q_N = -\frac{227}{N^5} - \frac{1638943}{864\,N^7} + O(N^{-9}),
$$

$$
A_N = \frac{640}{N^7} + \frac{1920}{N^9} + O(N^{-11}),
$$

$$
B_N = \frac{6170}{9\,N^7} + \frac{677903}{324\,N^9} + O(N^{-11}),
$$

and therefore

$$
\Delta c_{4,N} = A_N + B_N = \frac{11930}{9\,N^7} + O(N^{-9}).
$$

The ratio of bandwidth to rest-energy magnitude satisfies

$$
\frac{\Delta c_{4,N}}{|q_N|} = \frac{11930}{2043\,N^2} + O(N^{-4}).
$$

**Interpretation.** The fourth-order rest energy scales as $N^{-5}$, while
the mobility bandwidth is suppressed by an additional $N^{-2}$ factor and
scales as $N^{-7}$. This is **parametric large-$N$ flattening**: the
one-plaquette $T_1^{+-}$ branch becomes asymptotically flat at large rank,
and the flatness is not an artifact of any finite-$N$ cancellation.

*Derivation.* The $q_N$ asymptotics follow from expanding the exact
$Q_{32}/D_{34}$ expression. The $A_N$ asymptotics are immediate from
$640/[N(N^2-1)^3] = 640N^{-7}(1-N^{-2})^{-3}$. The $B_N$ asymptotics
follow from leading-order expansion of the $P_{402}/D_{409}$ formula.

---

## 9. SU(3) fifth order

Everything in §§2–8 is fourth order and holds for all ranks. This section
continues the **SU(3)** band to fifth order in $u$. The fifth-order kernel is
again a 189-record real-space object, and the projected coefficient has the
**same two-invariant form** as fourth order, with positive shape coefficients
and the same unique-minimum/unique-maximum structure.

*Throughout §9 the gauge rank is fixed at $N=3$, and the subscript on
$q_n,A_n,B_n$ is the **coupling order** $n$ (not the gauge rank). So $q_5,A_5,B_5$
below are the fifth-order SU(3) coefficients; cf. the unrelated SU(5)
fourth-order value $q_5$ in §5.5.*

### 9.1 Fifth-order band

For $X_i=1-\cos k_i$, $S=\sum_iX_i$, $Q=\sum_iX_i^2$, $R=\sum_{i<j}X_iX_j$,

$$
\boxed{c_5(k) = q_5 + \frac{A_5\,Q + B_5\,R}{2S},}
$$

with

$$
q_5 = m_5 = -\frac{866236750503342026253096691057}{1169668083793811403447133488000}
\approx -0.740583386437,
$$

$$
\boxed{A_5 = \frac{313}{240}},
\qquad
\boxed{B_5 = \frac{1881863087742908605903793}{1652932248975967181040000}}.
$$

Both shape coefficients are positive ($A_5\approx1.3042$, $B_5\approx1.1385$),
so the fifth-order coefficient has its unique minimum at $\Gamma$, its unique
maximum at $R$, and exact bandwidth

$$
\boxed{\Delta c_5 = A_5 + B_5
= \frac{4037562229115732471176793}{1652932248975967181040000}
\approx 2.442666498652.}
$$

The parity anchors are

$$
c_X = \frac{659205375444420345742539899543}{1169668083793811403447133488000},
\qquad
c_M = \frac{13250388338835740713398569140103}{11696680837938114034471334880000},
$$
$$
c_R = \frac{475012476694676416524425923}{279077133945841621360740000},
$$

and they satisfy the exact consistency gate

$$
c_R = 2c_M - c_X,
$$

with the same extraction relations as fourth order:
$A_5 = c_X - q_5$ and $B_5 = 2(c_M-c_X) = c_R - c_X$. (Both $B_5$ extractions
were checked to agree exactly.)

> **Structural continuity.** The fifth-order band has identical algebraic shape
> to the fourth-order band: $c_n(k) = q_n + (A_n Q + B_n R)/(2S)$ with
> $A_n, B_n > 0$. The flat-band picture — unique minimum at $\Gamma$, unique
> maximum at $R$, no positivity violation — therefore persists through $O(u^5)$.
> What changes is only the magnitude: the fifth-order shape coefficients are
> $O(1)$, not the small fourth-order values, so the band is no longer
> approximately flat at this order.

### 9.2 Complete rest-mass series through fifth order

$$
\boxed{
\begin{aligned}
m_{1^{+-}}(u) = {}& \frac{8}{3} + u + \frac{11}{306}u^2
- \frac{109151}{249696}u^3 \\
&- \frac{20721577909065127111}{7250590288602460800}u^4
- \frac{866236750503342026253096691057}{1169668083793811403447133488000}u^5
+ O(u^6).
\end{aligned}
}
$$

### 9.3 Fifth-order census

The fifth-order contraction is substantially larger than fourth order:

| Object | Count |
|---|---:|
| Connected five-insertion supports | 6,676,658 |
| Support/output pairs | 39,368,491 |
| Triality classes | 1,280 |
| Canonical ordered words | 29,366 |
| Charge-conjugation orbits | 116,571 |
| Local signatures | 574 |
| Local fusion paths | 1,624 |
| Trace-wiring topologies | 22,071 |
| Global path contractions | 524,823 |
| Nonzero real-space kernel records | 189 |

The new local epsilon-delta sectors at fifth order are $(4,1)$ and $(5,2)$;
every Stage-2 invariant basis vector was reconstructed from the orthogonal
fusion-tree path basis for all 574 signatures.

### 9.4 Scale-matched ratio through fifth order

Using the project-native string tension (now in the corrected variable $u$),

$$
\sigma(u) = \frac{2}{3} - \frac{22}{153}u^2 - \frac{61}{408}u^3
- \frac{737327120374220449}{7250590288602460800}u^4 + O(u^5),
$$

and the exact historical Kogut–Pearson–Shigemitsu (KPS) fifth-order target
under the bridge $\sigma(u)=\tfrac12 W(2u)$,

$$
\sigma_5 = -\frac{137767222189182735950309}{2009803206414863779920000},
$$

the mass / string-tension ratio is

$$
\boxed{
\frac{m_{1^{+-}}(u)}{\sqrt{\sigma(u)}}
= \sqrt{6}\sum_{n=0}^{5} c_n u^n + O(u^6),
}
$$

with

$$
\begin{aligned}
c_0 &= \frac{4}{3}, & c_1 &= \frac{1}{2}, & c_2 &= \frac{11}{68}, \\
c_3 &= -\frac{7559}{499392}, &
c_4 &= -\frac{15752822901180179}{12642703205932800}, \\
c_5 &= -\frac{10670728893034386567182468628311}{46786723351752456137885339520000}.
\end{aligned}
$$

Numerically $c_5 \approx -0.228072$, so $\sqrt{6}\,c_5 \approx -0.558659$.
The full series $c_0,\dots,c_5$ was re-derived independently from the
rest-mass and string-tension series above; all six coefficients agree.

> **Provenance and convention (updated 2026-06-14, verified from source).**
> The fourth-order tension and below, $\sigma_0,\dots,\sigma_4$, are
> **project-native and reproduced from source**: the native connected-support
> torelon engine runs and yields $\sigma_2=-\tfrac{22}{153}$,
> $\sigma_3=-\tfrac{61}{408}$, $\sigma_4=-\tfrac{737\ldots}{7250\ldots}$ in the
> variable $u$ with $L=4$/$L=5$ length-independence. $\sigma_5$ (and $\sigma_6$
> below) remain exact **KPS historical targets**, not yet native reruns;
> promoting them requires extending that engine to fifth/sixth order. The
> conversion is the single bridge $\sigma(u)=\tfrac12 W(2u)$ with $x=2u$. This
> bridge — and the **negative** sign of $\sigma_5$ — is forced by the native
> engine: testing the alternatives, only $\tfrac12 W(2u)$ reproduces the
> engine's odd-order $\sigma_3=-61/408$, whereas the $\tfrac12 W(-2y)$
> convention gives $+61/408$ and hence the wrong sign at odd orders. (A
> separate KPS-extraction artifact that used $\tfrac12 W(-2y)$ and reported a
> *positive* $\sigma_5$ is therefore a convention sign error; its even-order
> $\sigma_6$ is unaffected.) The older mixed-variable $(-1/4)^n$ conversion is
> superseded and must not be combined with these coefficients.

### 9.5 State of sixth order ($m_6$)

The sixth-order rest-energy coefficient $q_6 = m_6 = \tfrac13\operatorname{tr}H_6(0)$
is the highest-value open physical coefficient: it is the only unknown numerator
needed to extend the ratio to $O(u^6)$, since

$$
c_6 = \frac{m_6}{2}
+ \frac{1181646977233006828729169209802562361069278851250351799}{168641444007491247688836385300053017225944999004544000000}.
$$

Two of the hard sixth-order components are **pre-cleared**:

1. **Folded/des-Cloizeaux weights.** The order-generic folding recurrence was
   checked at six insertions against all 32 zero/nonzero intermediate-denominator
   patterns, exact path-reversal symmetry, the nonresonant resolvent-product
   limit, and four independent rational-matrix regressions against the full
   Rayleigh–Schrödinger coefficient. All gates pass; folded terms are no longer
   an open part of $m_6$.

2. **Local carrier census.** The eight-event token space has $3^8-1=6560$ nonzero
   local link signatures; exact SU(3) fusion from singlet back to singlet leaves
   **2,186 feasible signatures** spanning the sectors
   $$(0,3),(0,6),(1,1),(1,4),(1,7),(2,2),(2,5),(3,3),(4,4).$$
   The genuinely new sixth-order sectors are the balanced degree-eight $(4,4)$
   and the double-determinant $(0,6)$ and $(1,7)$. The fusion-path basis is
   nonempty for every feasible signature (max singlet multiplicity 23, max
   intermediate irrep dimension 27), proving the path representation can carry
   every sixth-order sector without hand-selecting epsilon–delta cases.

The remaining sixth-order work is the global geometry census and contraction
(see §13).

---

## 10. SU(3) fourth-order exact values

For reference, the complete exact band data at $N=3$:

| Point | Exact $c_4$ | Exact lift above $\Gamma$ |
|---|---:|---:|
| $\Gamma$ | $-20721577909065127111/7250590288602460800$ | $0$ |
| $X$ | $-17700498622147435111/7250590288602460800$ | $5/12$ |
| $M$ | $-4367164159624988707/1812647572150615200$ | $247051057231349/550663802582400$ |
| $R$ | $-3447362930970494909/1450118057720492160$ | $132329431693349/275331901291200$ |

Kernel SHA-256: `d2a4121a9798b2c364a52f7845fd7014ce2463563642470102cb080336a9fd51`.
Semantic kernel SHA-256: `48a422a517c7c1e70b84fd88a0773943f81ae3f9bfafadbe2304f8eb7d2e9b77`.

---

## 11. Fixed-rank verification statement (corrected from v0.7)

The following replaces the overbroad v0.7 statement that "$q_N$, $A_N$, and
$B_N$ match exact fixed-rank contractions for every $N=7,\ldots,18$":

> Stored exact fixed-rank values of $q_N$ for $N=7,\ldots,18$ match the
> compact $Q_{32}/D_{34}$ formula. The bundled complete $N=7$ fixed-rank
> kernel independently matches $q_7$, $A_7$, and $B_7$ and passes both
> $B$ extraction channels. Independent full-kernel reruns at $N=7$ and $N=8$
> both match the stable symbolic formulas exactly.
>
> The all-rank signs and closed forms for $A_N$ and $B_N$ are certified by
> the exact symbolic residual, denominator factorizations, and positive
> Newton expansions. The stronger claim that independent full-kernel artifacts
> exist for every $N=7,\ldots,18$ cannot be made without including those
> artifacts or an active $A_N/B_N$ sample ledger with verifier assertions.

---

## 12. Source-chain status and reproducibility

| Layer | Status |
|---|---|
| SU(3) Stage 0–3J source chain (fourth order) | **Complete** — Stage-3I (`y4_stage3i_complete_folded_descloizeaux.py`) recovered; full pipeline reruns and produces 189-record kernel |
| Stable-rank Stage-0/1 geometry | **Independently reproduced** — 4,171 ordered words, 16,750 orbits, 140 signatures, 0 accidental denominator roots for $N\ge7$ |
| Stable-rank Stage-3G walled-Brauer contraction | **Complete** — exact $q_N$, $A_N$, $B_N$ symbolic formulas derived from 35,130 paths |
| Symbolic formula generator (35,130-path → $Q_{32}$, $P_{402}$) | **Present** in full symbolic bundle; the formula-generation script is the `y4_complete_from_scratch` notebook |
| Exceptional ranks ($N=3,4,5,6$) | **Complete** — all direct finite-rank contractions verified |
| SU(3) fifth-order band ($q_5$, $A_5$, $B_5$, kernel) | **Complete and independently reproduced** — verifier and arithmetic re-run from cold start; consistency gate $c_R=2c_M-c_X$ holds |
| Fifth/sixth-order string tension ($\sigma_5$, $\sigma_6$) | **Historical KPS targets** — not yet project-native torelon reruns |
| Sixth-order folded weights | **Pre-cleared** — 6 gates pass (32 patterns, reversal, resolvent, 4 regressions) |
| Sixth-order local carrier census | **Pre-cleared** — 2,186 feasible signatures, path basis nonempty for every record |
| Sixth-order global geometry + contraction ($m_6$) | **Open** — highest-value remaining physical coefficient |
| $B_N$ fixed-rank sample ledger ($N=7,\ldots,18$) | **Open** — required to restore the strong fourth-order holdout claim |
| Lower-order scripts (Appendix A) | **Open** — $N=3$ lower-order sources still absent from release bundle |

The release should either add a machine-readable $A_N/B_N$ fixed-rank ledger
with active verifier assertions, or qualify the fixed-rank validation scope
per §11 above.

### Recommended $m_6$ execution path

The efficient target is the scalar zero-momentum coefficient $q_6=m_6$, not
the full sixth-order dispersion:

1. Enumerate connected six-insertion supports with external-memory sharding
   (the fifth-order census already has 6.68M support classes, so a monolithic
   in-memory expansion is the wrong architecture).
2. Apply triality and charge-conjugation reduction before global contraction.
3. Use the fusion-path basis as the primary local basis (handles the new
   degree-eight and double-determinant sectors without hand-enumeration).
4. Contract only the zero-momentum trace first; build the full real-space
   kernel only after $m_6$ is fixed.

---

## 13. Theorem status summary

$$
\boxed{\text{SU(3) fourth-order }T_1^{+-}\text{ band theorem: proved}}
$$

$$
\boxed{\text{Rank-complete }(N\ge3)\text{ fourth-order band theorem: proved}}
$$

$$
\boxed{\text{Parametric large-}N\text{ flattening corollary: proved for }N\ge7}
$$

$$
\boxed{\text{SU(3) fifth-order band }(q_5,A_5,B_5)\text{: proved, independently reproduced}}
$$

$$
\boxed{\text{SU(3) ratio through }O(u^5)\text{: proved (historical }\sigma_5\text{ target)}}
$$

$$
\boxed{\text{Manuscript coupling variable: requires correction }y:=u=\beta/6}
$$

$$
\boxed{B_N\text{ fixed-rank holdout ledger: open}}
$$

$$
\boxed{\text{SU(3) sixth-order }m_6\text{: open (folded + carrier pre-cleared)}}
$$

$$
\boxed{\text{Native }\sigma_5,\sigma_6\text{ torelon rerun: open}}
$$
