# The primitive cell-completion coefficients of strong-coupling Hamiltonian SU(N) lattice gauge theory

**A self-contained referee brief.** 2026-08-21.

This document extracts one slice of a larger research program into a form an
outside reader can referee without access to that program: a family of exact
rational coefficients in strong-coupling perturbation theory of Hamiltonian
SU(N) lattice gauge theory, attached to the completion of closed cell
surfaces. Everything asserted here is either proved in this document, proved
in the accompanying machine-checked layer (Lean 4 for the rational algebra;
exhaustive exact enumeration in Python/sympy for the combinatorics), or
explicitly labelled as scope it does *not* claim. §7 states the limitations
before any reader has to hunt for them; §8 gives one-command reproduction.

## 1. Setting and conventions

Work in Hamiltonian (Kogut–Susskind) SU(N) lattice gauge theory at strong
coupling: the electric term is diagonal, `H₀ = (1/2) Σ_links E²`, and the
magnetic plaquette term is the perturbation, with expansion parameter
`u = β_N/(2N)` (for SU(3), `u = β/6 = 1/g_H⁴`). Each perturbation insertion
multiplies the state by a fundamental-representation Wilson loop around one
face and carries coefficient `+1` per insertion in the normalization used
throughout (the overall sign convention of V is discussed in §6.1).

Two constants recur:

- `C_F = (N² − 1)/(2N)`, the fundamental Casimir;
- `E(L) = L·C_F/2`, the electric rest energy of a simple loop of `L` links
  all carrying fundamental flux, which follows from `H₀` above. For SU(3):
  `E(4) = 8/3`, `E(5) = 10/3`.

## 2. Objects

**Cell.** A *cell* here is a closed, coherently oriented 2-complex: a finite
set of oriented polygonal faces such that every edge occurs in exactly two
faces, with opposite orientations. Examples used below: the tetrahedron (4
triangles) and the n-gonal prisms (2 n-gon caps + n squares; n = 4 is the
combinatorial cube).

**Sector.** An ordered pair of faces `(p, q)` of equal perimeter, the
*endpoints*. A completion coefficient is a property of `(cell, sector)`, not
of the cell alone — §6.2 shows why conflating sectors manufactures a fake
discrepancy.

**Primitive completion history.** Fix `(p, q)` and let `f₁, …, f_r` be the
remaining `r = F − 2` faces. A *history* is an ordering of these insertions
subject to, at every step:

1. the newly inserted face shares at least one edge with the current loop,
   the shared edges all appear with opposite orientation (guaranteed by the
   coherent orientation), and they form a single connected path;
2. after the merge the state is again a single simple loop (no repeated
   edge);
3. after the final insertion the loop equals the reversed boundary of `q`.

The state after `k` insertions is the boundary loop of `p ∪ {first k faces}`;
write `ℓ_k` for its length and `ℓ₀` for the endpoint perimeter.

**The coefficient.** Each insertion contributes a Haar merge factor (Lemma 1:
exactly `1/N`); each of the `r − 1` intermediate loops contributes one
Rayleigh–Schrödinger resolvent `1/(E(ℓ₀) − E(ℓ_k))`. The *primitive local
completion coefficient* is

```
c_prim(cell, sector)(N)  =  (1/N^r) · Σ_histories  Π_{k=1}^{r−1}  1/(E(ℓ₀) − E(ℓ_k))
                         =  S_r / (N^r · C_F^{r−1}),
```

where the second form defines the *signed count*

```
S_r  =  Σ_histories  Π_{k=1}^{r−1}  2/(ℓ₀ − ℓ_k)          (a rational number).
```

Since `C_F^{r−1} = (N²−1)^{r−1}/(2N)^{r−1}`, equivalently
`c_prim = 2^{r−1} S_r / (N (N²−1)^{r−1})`.

## 3. Lemma 1: a merge costs exactly 1/N, at every shared-path length

**Statement.** Let two fundamental Wilson loops share a connected path of
`k ≥ 1` links, traversed in opposite senses, with all other links distinct.
Integrating the shared links over Haar measure merges the two traces into the
single trace over the concatenated loop, with coefficient exactly `1/N` —
independent of `k`.

**Proof.** The only group integral needed is the fundamental-pair moment

```
∫ dU · U_ij (U†)_kl = (1/N) δ_il δ_jk ,
```

whose coefficient is the order-1 Weingarten value, i.e. the inverse of the
1×1 Gram matrix `[N]`. Applied per link, it yields the two closed-trace
rules `Tr(Xu)·Tr(Yu†) → (1/N)·Tr(XY)` (different traces) and
`Tr(XuYu†) → (1/N)·Tr(X)·Tr(Y)` (same trace), with `Tr(∅) = Tr(I) = N`.
Contract the shared links in path order: the first contraction (rule 1)
joins the traces at cost `1/N`; each of the remaining `k − 1` contractions
is rule 2 with `Y = ∅`, producing a factor `(1/N)·N = 1`. The net is
`(1/N)^k · N^{k−1} = 1/N`, and the surviving trace is the concatenated
loop. ∎

Because every link in a primitive history carries at most a single unit of
fundamental flux (histories are square-free by requirement 2), no
determinant/epsilon channel can enter, and the SU(N) and U(N) fundamental-pair
moments coincide — the lemma holds verbatim for SU(N), all `N ≥ 2`.

## 4. Theorem 1: the tetrahedral coefficient

**Statement.** For the tetrahedron, any endpoint pair:

```
S₂ = −4 ,        c_prim = −8 / (N (N² − 1)) ,        c_prim(3) = −1/3 .
```

**Proof.** Label vertices 1..4 and orient the four faces coherently, e.g.
(123), (134), (142), (243). Fix endpoints `p, q`; the two remaining faces can
be inserted in `2! = 2` orders, and both are admissible. In either order the
first merge glues along one shared edge (the shared path has length 1) and
produces the unique intermediate: a 4-link loop — for `p = (123)`,
`f = (134)` the shared edge is 13 and the merged boundary is the
quadrilateral 1→2→3→4→1 — so `ℓ₁ = 3 + 3 − 2 = 4`. The second merge glues along a
connected 2-link path (the two edges the last-but-one loop shares with the
inserted face meet in a vertex) and closes onto the reversed boundary of `q`
by the tetrahedron's boundary relation ∂(sum of all four coherently oriented
faces) = 0. By Lemma 1 each insertion costs `1/N` at both path lengths.
Each history carries the single resolvent
`1/(E(3) − E(4)) = 1/(−C_F/2) = −2/C_F`, so

```
S₂ = 2 · (2/(3−4)) = −4 ,     c_prim = −4/(N²·C_F) = −8/(N(N²−1)) . ∎
```

The full 12-fold check (every ordered endpoint pair, every hypothesis of §2
enforced mechanically rather than assumed) is exhaustive in the machine
layer; face-transitivity of the tetrahedron makes the pairs equivalent.

## 5. Theorem 2: the n-gonal prism cap family is central-binomial

**Statement.** For the n-gonal prism with the two caps as endpoints
(`r = n` square insertions):

```
S_n = (−1)^{n−1} · C(2n−2, n−1),
c_prim = (−1)^{n−1} · 2^{n−1} · C(2n−2, n−1) / (N (N²−1)^{n−1}).
```

Instances (exhaustively verified for n = 3, 4, 5, 6 — i.e. up to 720
histories): `S = 6, −20, 70, −252`, giving coefficients
`24/(N(N²−1)²)`, `−160/(N(N²−1)³)`, `1120/(N(N²−1)⁴)`, `−8064/(N(N²−1)⁵)`.
For all n the closed form rests on a run-length Catalan factorization of the
subset sums (a dynamic-programming identity); the instances above are what
this brief certifies exhaustively.

**Key step.** Let `T` be the set of inserted squares after `k` steps. The
boundary loop of `cap ∪ T` has length

```
ℓ(T) = n + 2·blocks(T),
```

where `blocks(T)` is the number of cyclically contiguous runs of `T` around
the prism: the cap contributes its `n − k` unclaimed edges, each square in
`T` contributes its top edge, and a vertical edge lies on the boundary iff
exactly one of its two neighbouring squares is in `T` — twice per run. Hence
each resolvent denominator is `(E(n) − E(ℓ)) = −blocks(T)·C_F`, every
denominator is negative, and

```
S_n = (−1)^{n−1} Σ_orderings Π_{k=1}^{n−1} 1/blocks(T_k) ,
```

with `blocks(T₁) = blocks(T_{n−1}) = 1` always. For n = 5 this sum is `70`
across all `120` orderings — matching, digit for digit, the independent
record of that computation (§6.3).

**The cube.** n = 4 is the cube with opposite endpoints: 24 orderings in
two length-signature classes, `(6,6,6)` (16 orderings) and `(6,8,6)` (8
orderings), with per-history amplitudes `−8` and `−4` in units of
`N⁴E₀³`, `E₀ = (N²−1)/N` — reproducing exactly the three multiplicity-8
temporal classes `(−8, −8, −4)` of the independent derivation record, and

```
S₄ = −20 ,   c_prim = −160/(N(N²−1)³) ,   c_prim(3) = −5/48 .
```

## 6. Consistency structure

### 6.1 The sign is the resolvent parity

Every intermediate loop in every admissible history of these cells is longer
than the endpoints, so all `r − 1` resolvent denominators are negative and
`sign(S_r) = (−1)^{r−1}`. No sign is imposed by hand; the even-order cube
value `−5/48` (which is anchored independently, §6.3) fixes the overall
convention, and odd orders follow by the parity.

### 6.2 Sectors, not cells: 24 vs 64

The triangular prism carries **two** coefficients. Cap sector (triangle →
triangle through 3 squares): `S = 6`, `c = 24/(N(N²−1)²)` — the n = 3 row of
Theorem 2. Square sector (vertical square → vertical square through the
third square and both triangles): `S₃ = 16` from six histories with
length signatures `(5,6)`, `(5,5)`, `(6,5)` (each twice), giving
`c = 64/(N(N²−1)²)`. Both come from the same definition and the same code
path; "24 vs 64" is a sector label, not a disagreement — a physical
application must say which sector its retained states live in.

### 6.3 Independent anchors

Each row of the family matches at least one record produced independently of
this derivation (and, for the starred rows, independently of the research
program's own later syntheses):

| Result here | Independent record |
|---|---|
| `E(4) = 8/3`, `E(5) = 10/3` at SU(3) | the program's certified isotropic electric pair, and the free one-plaquette energy `8/3` |
| cube: classes `(−8,−8,−4)`, mult. 8; `c(3) = −5/48` | a prior derivation record of the 24 temporal orderings, and a separately certified SU(3) coefficient the program's two otherwise-disputing computations both fix* |
| pentagonal: 120 histories, `S₅ = 70`, `c(3) = 35/384` | a prior independent computation record stating precisely these three numbers |
| Catalan family incl. `n = 6` value `−8064/(N(N²−1)⁵)` | an upstream notebook (24/24 internal gates) computing the cap family by a different method (subset DP with exact resolvent resummation via a Feshbach block) |
| sign `(−1)^{r−1}` | an upstream erratum recording the same factor as `(−1)^{r+1}` by hand — derived here instead |
| tetrahedron `−8/(N(N²−1))` | asserted upstream **without any derivation or artifact**; this brief's Theorem 1 is, to our knowledge, its first proof |

*The `−5/48` anchor is the strongest: it is the one row certified before this
work by two mutually disputing computations that agree on it.

## 7. What this brief does NOT claim

1. **Primitive channel only.** At each cut, only the merged simple-loop
   (singlet) channel is kept — that is the *definition* of `c_prim`, not an
   approximation theorem. Fierz side channels (e.g. adjoint flux on shared
   links), folded and linked-cluster terms, and finite-N determinant sectors
   are outside it; in the source program a fifth-order determinant dressing
   demonstrably shifts the pentagonal row's physical value at SU(3).
2. **No mobility claim.** A nonzero `c_prim` does not by itself imply the
   corresponding excitation disperses: the assembled operator must also act
   non-scalarly after compression to the degenerate sector, and for the
   tetrahedron that compression question is open. (What *is* proved: the
   tetrahedral second-order proper-return operator is exactly scalar on the
   face space — three 4-link returns at weight −2 per face — so primitive
   returns shift the rest energy only.)
3. **No continuum statement.** Everything is finite-order strong-coupling
   perturbation theory about isolated flux loops on the lattice.
4. **Novelty unverified.** We have not established that this family is
   absent from the strong-coupling literature; the central-binomial pattern
   in particular looks like something a 1980s series expansion may contain.
   Pointers welcome — a prior source would *strengthen* the anchor table.
   *(Update 2026-08-21: a bounded negative search is on record —
   `novelty_search_2026-08-21.md` beside this file. Everything on arXiv
   citing Hamer 1989 has been read and is clean; the five priority primary
   sources that remain unread, led by Munster 1981 and Seo 1982, are named
   there with why each is where the family would live. The search's
   sharpest find: O'Brien–Zuber, Nucl. Phys. B253 (1985) 621, attaches
   signed central binomials to the sewing of closed plaquette surfaces at
   large N, and `C(2n−2,n−1) = n·Cat(n−1)` ties this family's signed counts
   to those weights up to the cyclic factor n — same combinatorial family,
   different limit and dynamics. Whether Theorem 2 is derivable from their
   cumulant weights is the open adjudication any novelty claim must argue.)*

## 8. Reproduction

Everything above re-derives in seconds from a clean clone:

```bash
make bootstrap
workhouse verify --only 'tetrahedral'     # the full 11-check suite
workhouse verify --only 'G5: the tetrahedral coefficient'
workhouse verify --only 'the cube instance'
workhouse verify --only 'the n-gonal cap family'
```

The enumeration engine is `src/workhouse/cellular.py` (~350 lines, sympy
only): cells are validated for coherent orientation, every hypothesis of §2
is enforced (not assumed) at every merge, and the Haar lemma's contraction is
implemented as the two trace rules of §3 acting on formal cyclic words. The
rational-algebra layer is additionally machine-proved in Lean 4
(`lean/Workhouse/Basic.lean`: `cPrimTwo_forms`, `tetra_from_count`,
`tetraCompletion_three`, `prismCompletion_three`, `cubeCompletion_three`,
`pentCompletion_three`, `alphaPen_eq_neg_four_cube`; no `sorry`; axioms
`propext`, `Classical.choice`, `Quot.sound` only): `lake build` in `lean/`.

A referee wishing to check without any of this can reproduce Theorem 1 in a
dozen lines of any CAS: enumerate the two orderings, verify the merged loop
lengths 3 → 4 → 3, apply `∫U_ij U†_kl = δδ/N` twice, and divide by
`E(4) − E(3) = C_F/2`.
