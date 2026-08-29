# Representation-Theoretic Route to the Balaji (B=6) Cube Test

**Date:** 2026-08-28  
**Status:** local four-channel census **PASS**; direct reduced (B=6) cube Schur reconstruction **PASS**; full finite-(u) and full-global-basis diagonalizations remain unclaimed  
**Scope:** the vacuum-subtracted, charge-odd one-face shell through second order in (u=g^{-4})

## Executive result

The authors' public `ymcirc` development branch already contains the local
(B=6), trivalent-vertex magnetic table needed for the decisive test.  A
target-blind extraction from the pinned file finds all four and only the four
shared-link fusion channels that can enter the second-order one-face Schur
complement:

\[
3\otimes\bar3=1\oplus8,
\qquad
3\otimes3=\bar3\oplus6,
\qquad
\bar3\otimes\bar3=3\oplus\bar6.
\]

The extracted amplitudes are, to the ten decimal places stored by the authors,

\[
\frac13,qquad
\frac{2\sqrt2}{3},\qquad
\frac1{\sqrt3},\qquad
\sqrt{\frac23},
\]

so their exact squares are (1/9,8/9,1/3,2/3).  Combining these with the
electric denominators gives

\[
w_1=-\frac1{12},\qquad
w_8=-\frac{16}{51},\qquad
w_{3,\bar3}=-\frac16,\qquad
w_{6,\bar6}=-\frac29,
\]

and therefore

\[
\boxed{
t_3=(w_{3,\bar3}+w_{6,\bar6})-(w_1+w_8)=\frac5{612}.}
\]

Thus (B=6) is already **shared-link complete** and can decide the predicted
sign reversal.  It is not, however, complete for the common onsite scalar.
The same-face symmetric-sextet route has site energy (20/3), is absent at
(B=6), and first appears at an integer-labelled (B=7).  This distinction
changes the absolute acceptance target but not the relative shell or its
ordering.

The correct (B=6) second-order gap matrix is

\[
\boxed{
W^{(2)}_{B=6}=\frac{39}{68}I_6+\frac5{612}G,}
\]

where (G=\partial_2^\dagger\partial_2) is the oriented cube face Gram
matrix.  After removing the common scalar, the decisive identity is simply

\[
\boxed{
W^{(2)}_{B=6}-\frac{39}{68}I_6=\frac5{612}G.}
\]

A direct open-cube reconstruction has now generated all six local face tables
from the pinned public pyclebsch implementation and contracted the complete
one-action reachable space.  It obtains the matrix above with maximum
entrywise residual \(6.66\times10^{-16}\), without enumerating or diagonalizing
the full (B=6) global Hilbert space.

## 1. Public source pin

The primary author-data input is

```text
repository: https://github.com/hepqis-uiuc/ymcirc
branch: develop
observed develop commit: e9e190bfda405608de9cab71c0df0161cfcb1a10
path: ymcirc/_ymcirc_data/magnetic-hamiltonian-box-term-matrix-elements/
      B6_dim(3_2)_PBC_magnetic_hamiltonian.json.gz
Git blob: 34f445613943d6ab22db38b66a3446777256e054
bytes: 10247
SHA-256: 36f8c0992fb4e42b475878eb617034bba0511e45d725491ed8d9577c586f449f
raw transition keys: 1000
```

The file is visible directly in the public repository:

<https://github.com/hepqis-uiuc/ymcirc/blob/develop/ymcirc/_ymcirc_data/magnetic-hamiltonian-box-term-matrix-elements/B6_dim%283_2%29_PBC_magnetic_hamiltonian.json.gz>

Its metadata is

```json
{
  "dim": "d=3/2",
  "truncation_mode": "B",
  "num_sites": [3, 2, 1],
  "PBCs": [true, false, false],
  "cutoff": 6,
  "planes": ["(1, 2)"],
  "site_coords_for_comp": [[0, 0, 0]],
  "f_order": [1, 2, 3, -1, -2, -3]
}
```

The scalar-boundary control is the corresponding public
B7_dim(3_2)_PBC_magnetic_hamiltonian.json.gz file: 14,566 compressed bytes,
1,360 transition keys, SHA-256
00c65c7714085b9373b10f13f359c4c34741b1e37624b0d178b74d1e84fe9644,
and Git blob 4e4ea0bc7a19ed030e26e8c7361897d2e9349120.

This (d=3/2) line-of-plaquettes geometry is locally trivalent.  Every
plaquette vertex has two active face links and one control link, exactly as a
face corner of a one-cube open lattice.  Balaji et al. explicitly state that
these trivalent singlets embed into (d=3) at the same (B) by tensoring with
trivial representations.  The table is therefore sufficient for the local
channel census.  A direct OBC generator call remains preferable for fixing all
raw face-by-face phase conventions in a global matrix.

## 2. Why (B=6) is the exact shared-link threshold

Balaji et al. define the site cutoff by

\[
B_s=\sum_{\ell\ni s}C_2(R_\ell).
\]

At an endpoint of the shared edge of two adjacent fundamental plaquettes, the
other two incident edges are fundamental.  If the shared edge carries
\(\rho\), the local cutoff required by that intermediate state is

\[
B_\rho=2C_F+C_\rho,
\qquad C_F=\frac43.
\]

The complete ledger is

| shared irrep \(\rho\) | \(d_\rho\) | \(C_\rho\) | \(B_\rho\) | admitted by |
|---|---:|---:|---:|---:|
| \(1\) | 1 | 0 | \(8/3\) | \(B\ge8/3\) |
| \(3\) or \(\bar3\) | 3 | \(4/3\) | 4 | \(B\ge4\) |
| \(8\) | 8 | 3 | \(17/3\) | \(B\ge17/3\) |
| \(6\) or \(\bar6\) | 6 | \(10/3\) | 6 | \(B\ge6\) |

Consequently:

- (B=4=T_1) retains (1) and (3/\bar3), producing (-1/12);
- (B=17/3) restores the octet but not the sextet;
- (B=6) is the first cutoff containing all four adjacent-face channels.

This follows both from the Casimir arithmetic and from Table I of the Balaji
paper: (3\otimes\bar3\otimes8) appears at (17/3), while
(3\otimes3\otimes\bar6+\mathrm{c.c.}) appears at (6).

## 3. Target-blind extraction from the author table

The audit selected transitions using only their local state pattern:

1. the initial state has one nontrivial active link in (3) or (bar3);
2. exactly two control links are nontrivial fundamentals, representing the
   already-excited neighboring face;
3. the final state leaves the controls unchanged;
4. the other three active links become fundamental;
5. the old shared active link becomes the fused irrep.

There are exactly 16 stored rows: four channels, two conjugations, and two
equivalent placements.  No target coefficient is used in this selection.

| channel family | stored amplitude magnitude | exact square | extracted rows |
|---|---:|---:|---:|
| (1) | 0.3333333333 | (1/9) | 4 |
| (8) | 0.9428090416 | (8/9) | 4 |
| (3/\bar3) | 0.5773502692 | (1/3) | 4 |
| (6/\bar6) | 0.8164965809 | (2/3) | 4 |

The maximum discrepancy after squaring the stored decimal amplitudes is below
(10^{-10}).  The exact values are independently fixed by

\[
|M_\rho|^2=\frac{d_\rho}{3^2},
\]

which is also the dimension-ratio matrix element published by
Ciavarella--Burbano--Bauer.

## 4. Exact denominators and channel weights

The one-face electric energy in the dimensionless Hamiltonian

\[
K(u)=\frac12\sum_\ell C_2(R_\ell)-u\sum_p(\Box_p+\Box_p^\dagger),
\qquad u=g^{-4},
\]

is

\[
E_F=4\frac{C_F}{2}=2C_F=\frac83.
\]

An adjacent two-face intermediate has six nonshared fundamental links and one
shared link in \(\rho\), so

\[
E_\rho=3C_F+\frac{C_\rho}{2},
\qquad
\Delta_\rho=E_\rho-E_F=C_F+\frac{C_\rho}{2}.
\]

Thus

| \(\rho\) | \(|M_\rho|^2\) | \(\Delta_\rho\) | \(w_\rho=-|M_\rho|^2/\Delta_\rho\) |
|---|---:|---:|---:|
| (1) | (1/9) | (4/3) | (-1/12) |
| (8) | (8/9) | (17/6) | (-16/51) |
| (3/\bar3) | (1/3) | 2 | (-1/6) |
| (6/\bar6) | (2/3) | 3 | (-2/9) |

Opposite and same orientations on the shared edge enter the charge-odd
projection with opposite signs.  Hence

\[
A_3=w_1+w_8=-\frac{27}{68},
\qquad
B_3=w_{3,\bar3}+w_{6,\bar6}=-\frac7{18},
\]

and

\[
t_3=B_3-A_3=\frac5{612}.
\]

The omitted-channel correction relative to (B=4) is

\[
w_{6,\bar6}-w_8=\frac{14}{153},
\qquad
-\frac1{12}+\frac{14}{153}=\frac5{612}.
\]

### Complete one-action intermediate ledger at (B=6)

Let \(P_-\) be the six-dimensional charge-odd one-face shell.  Through second
order, only states in \(QVP_-\) can enter.  They divide into three geometric
classes, and there are no others because one plaquette action can change only
the four links of that plaquette.

1. **Same face.**  Vacuum and self-conjugate outputs cancel in the charge-odd
   combination, while the conjugate fundamental loop remains inside \(P_-\)
   and is removed by \(Q\).  The charge-odd double-winding pair
   \((6,6,\bar6,\bar6)\oplus(\bar6,\bar6,6,6)\) would be a genuine \(Q\)
   state, but its vertex threshold is \(20/3\), so it is absent at (B=6).
   Hence the same-face \(Q\)-space image is empty at this cutoff.
2. **Adjacent face.**  The union has six nonshared fundamental or
   antifundamental links and one shared link.  For opposite orientation on the
   shared link, that link is in \(1\) or \(8\); for equal orientation it is in
   \(3,\bar3,6,\bar6\).  Charge conjugation groups the six raw labels into the
   four channel families
   \[
   1,\qquad 8,\qquad 3/\bar3,\qquad 6/\bar6,
   \]
   with denominators \(4/3,17/6,2,3\), respectively.  Trivalent fusion is
   multiplicity free, so no unlisted intertwiner label occurs.
3. **Opposite face.**  The two loops have eight disjoint fundamental or
   antifundamental links.  The two charge-odd orientation combinations have
   denominator \(8/3\).  Their access amplitudes from the two opposite faces
   are \((1,1)\) and \((1,-1)\), so their off-diagonal Schur contributions
   cancel.  Each diagonal contribution is \(-3/4\), exactly canceled by the
   vacuum subtraction for the remote face.

The direct reconstruction confirms this exhaustive ledger operationally:
each shell vector has 40 raw image states, their union has dimension 127, and
the vacuum image has dimension 12.  Those counts describe the generated
raw-link basis; after charge projection and conjugate pairing, the only
nontrivial shape channels are the four adjacent-face families above.

## 5. The cube matrix and cubic irreps

Order the outward-oriented faces as

\[
(xy)_0,(xy)_1,(xz)_0,(xz)_1,(yz)_0,(yz)_1.
\]

The oriented edge--face incidence Gram matrix is

\[
G=
\begin{pmatrix}
4&0&1&-1&-1&1\\
0&4&-1&1&1&-1\\
1&-1&4&0&1&-1\\
-1&1&0&4&-1&1\\
-1&1&1&-1&4&0\\
1&-1&-1&1&0&4
\end{pmatrix},
\qquad
\operatorname{spec}G=\{0^{(1)},4^{(3)},6^{(2)}\}.
\]

Let (b_{\pm i}) be the charge-odd faces normal to axis (i).  Inversion acts
as

\[
P b_{+i}=-b_{-i}.
\]

Therefore

- (b_{+i}+b_{-i}) is parity odd and decomposes as (A_1\oplus E);
- (b_{+i}-b_{-i}) is parity even and transforms as (T_1).

Including (C=-), the shell is

\[
\boxed{A_1^{--}\oplus T_1^{+-}\oplus E^{--}},
\]

with the representation-theoretic assignment

| irrep | multiplicity | \(G\) eigenvalue |
|---|---:|---:|
| (A_1^{--}) | 1 | 0 |
| (T_1^{+-}) | 3 | 4 |
| (E^{--}) | 2 | 6 |

Since (t_3>0), (B=6) predicts the ordering

\[
A_1^{--}<T_1^{+-}<E^{--},
\]

the reverse of the validated (B=4) ordering.

## 6. The scalar distinction: (B=6) versus onsite completion

This is the key hostile-review correction.

The same-face symmetric-sextet state has links

\[
(6,6,\bar6,\bar6)
\]

around the plaquette.  At each trivalent vertex its nontrivial pair is
(6\otimes\bar6), so its site cutoff is

\[
B_{\mathrm{same\ face},6}=2C_6=\frac{20}{3}>6.
\]

The public data verify this boundary directly:

- in the pinned (B=6) table, applying the directed plaquette operator to a
  one-face loop has only the determinant/conjugate-loop output already inside
  the degenerate shell;
- in the pinned (B=7) table, a second output
  ((6,6,\bar6,\bar6)) appears with amplitude 1.

That (B=7) intermediate lies four electric-energy units above the one-face
shell, so it contributes the common second-order shift

\[
-\frac{1^2}{4}=-\frac14.
\]

At (B=6), the charge-odd one-face state has no same-face (Q)-space route.
The vacuum energy correction is (-3/4) per face, so vacuum subtraction gives
a within-face gap contribution (+3/4).  For each of the four adjacent faces,

\[
\mathrm{leak}_{B=6}
=w_1+w_8+w_{3,\bar3}+w_{6,\bar6}+\frac34
=-\frac{11}{306}.
\]

The face-diagonal coefficient is therefore

\[
d_{B=6}=\frac34+4\left(-\frac{11}{306}\right)
=\frac{371}{612}.
\]

Writing the signed shared-link adjacency as (S=G-4I),

\[
d_{B=6}I+t_3S
=\boxed{\frac{39}{68}I+\frac5{612}G}.
\]

The absolute strong-coupling gap coefficients at (B=6) are consequently

| irrep | (B=6) coefficient |
|---|---:|
| (A_1^{--}) | (39/68) |
| (T_1^{+-}) | (371/612) |
| (E^{--}) | (127/204) |

At (B\ge20/3), or integer-labelled (B=7), the same-face sextet subtracts
(1/4) from every row and restores the onsite-complete expression

\[
W^{(2)}_{\mathrm{onsite\ complete}}
=\frac{11}{34}I+\frac5{612}G,
\]

whose eigenvalues are (11/34,109/306,19/51).  These are **not** the absolute
(B=6) coefficients.  They have the same relative splittings.

A direct six-face (B=7) reachable-state probe confirms this control.  It
generates 1,360 directed entries per face, retains a 139-state shell-image
union, and finds

\[
\alpha_{B=7}=\frac{11}{34},
\qquad
t_{B=7}=\frac5{612},
\]

with scalar-plus-Gram residual \(1.06\times10^{-15}\).  Thus the observed
(B=7)-(B=6) change is exactly the scalar \(-1/4\), while every relative
splitting is unchanged.

## 7. Direct reduced (B=6) cube reconstruction: PASS

The decisive second-order reconstruction has now been carried out directly on
an open cube with 8 vertices, 12 links, and 6 faces.  It did not insert the
four predicted amplitudes by hand.  Instead it:

1. generated the complete (B=6) local magnetic table separately on every cube
   face with the public pyclebsch master formula;
2. built the vacuum and six geometrically defined charge-odd one-face states;
3. formed the full one-action images \(M|0\rangle\) and
   \(M P_-\), retaining all generated states;
4. evaluated every electric denominator from the link Casimirs;
5. contracted the reachable-state Schur complement and only afterward compared
   it with the predicted Gram form.

The generated local irrep set is exactly

\[
\{1,3,\bar3,6,8,\bar6\},
\]

with 24 ordered trivalent singlet tuples.  Each of the six faces produces
1,000 directed local entries.  Their absolute coefficient multisets agree
with the public (B=6) trivalent table to at worst
\(4.82\times10^{-11}\).

The source provenance used by this run is:

| object | SHA-256 |
|---|---|
| downloaded pyclebsch OBC source archive | 6d16ee0fa055b143d8373efa8d57e4f5a745b362bcab6eb12318a9c09922111b |
| executed plaquette matrix-element source | 3d35eb1614bd6bf36432f6345bc16d45a51a6c68ab387a33dbfd47c77c045c45 |
| executed lattice-data source | 0eebd22d10d7bdead992f625c49879f6bcbf148e4859645dfe4c2b13b6d5a41b |
| public non-PBC (B=6), (d=3/2) local table used for multiset cross-check (11,017 bytes; Git blob 9c62ce708ed15da937ef2cd792b6c0cd325637df) | d72c876489193b89429b190426493e53219e79b58e2fe51b91ba5dd7f6e32f0e |

Before the second-order comparison, the reconstruction independently finds

\[
P_-VP_-=I_6,
\qquad
E_{\mathrm{vac}}^{(2)}=-\frac92.
\]

For every adjacent face pair, the six raw shared-link labels
\(1,3,\bar3,6,\bar6,8\) group into four conjugacy-complete routes.  For a
positive signed-incidence entry their off-diagonal contributions are

\[
\frac1{12},\qquad
-\frac1{12}-\frac1{12},\qquad
-\frac19-\frac19,\qquad
\frac{16}{51},
\]

from \(1\), \(3/\bar3\), \(6/\bar6\), and \(8\), respectively.  Their sum is
\(5/612\); every negative signed-incidence entry reverses all four signs.
Thus the matrix is obtained entrywise, not inferred only from its eigenvalues:

\[
\boxed{
W_{\mathrm{gap},B=6}^{(2)}
=\frac{39}{68}I_6+\frac5{612}G
}
\]

The generator enumerates faces in a different order from Section 5; its
incidence Gram matrix is related to the displayed \(G\) by a signed
permutation of the face basis.  The entrywise comparison is made in the
generator's own geometric ordering, not by matching sorted spectra.

The maximum entrywise residual is

\[
6.661338147750939\times10^{-16}.
\]

Its observed eigenvalue groups agree with the exact rationals

\[
\frac{39}{68}\ (1),\qquad
\frac{371}{612}\ (3),\qquad
\frac{127}{204}\ (2),
\]

and, relative to the singleton,

\[
0\ (1),\qquad
\frac5{153}\ (3),\qquad
\frac5{102}\ (2).
\]

This is a complete **second-order reachable-state Schur calculation**.  It is
not a full enumeration of the global (B=6) basis, not a 3,864-state
diagonalization, and not a finite-(u) spectrum.  The public Clebsch--Gordan
coefficients are stored in double precision, so the rational identities are
certified by numerical residual plus rational reconstruction, rather than by
a symbolic-CGC execution.

## 8. Validation gates and remaining tests

The combined source census and direct reconstruction pass gates 1, 2, 4, 5,
and 6 below.  Charge preservation in gate 3 and the cubic labels in gate 7
follow analytically from the conjugation and face representations; the
calculation did not separately build their full matrices and commutators.
Gate 8 remains open.  A bounded six-face, second-order (B=7) replay passes the
scalar-only prediction in gate 9, although it is not a full finite-(u)
diagonalization.

1. **Source pin.** Fail closed on the B6 table's compressed bytes, SHA-256, Git
   blob, metadata, and 1,000 transition keys.
2. **Independent shell definition.** Construct the six
   ((|p,3\rangle-|p,\bar3\rangle)/\sqrt2) states geometrically, not by fitting
   eigenvectors.
3. **Charge check.** Verify ([C,H]=0) before projection.
4. **Complete (Q) space.** Generate the one-action Krylov frontier from the
   shell and include every state allowed at (B=6).  Do not manually insert
   only the four expected channels.
5. **Full matrix check.** Verify entrywise
   
   \[
   W^{(2)}_{\mathrm{gap},B=6}
   =\frac{39}{68}I+\frac5{612}G.
   \]
6. **Scalar-free check.** Independently subtract the (A_1^{--}) eigenvalue
   and verify
   
   \[
   \{0^{(1)},(5/153)^{(3)},(5/102)^{(2)}\}.
   \]
7. **Symmetry check.** Build the cube rotation and inversion action and identify
   (A_1^{--},T_1^{+-},E^{--}) without using numerical multiplicity alone.
8. **Finite-(u) check.** Track the shell by overlap at decreasing (u) and
   verify
   
   \[
   \lim_{u\downarrow0}u^{-2}
   (\Delta K_{T_1}-\Delta K_{A_1},
    \Delta K_E-\Delta K_{A_1})
   =\left(\frac5{153},\frac5{102}\right).
   \]
9. **B7 scalar control.** Repeating at (B=7) should leave the two relative
   limits unchanged and lower all three absolute (u^2) coefficients by
   exactly (1/4).

The ninth gate is a particularly strong discriminator: it separates genuine
cutoff reconstruction from a calculation that hard-coded only the desired
shape coefficient.

## 9. Exact public generator calls that suffice

The public `pyclebsch` draft branch supporting open and mixed boundary
conditions is

<https://github.com/hepqis-uiuc/pyclebsch/tree/feature/OBC-and-mixed-BC-ymcirc>

at observed head commit

```text
2f632685b81c7ed514c6793665257e17ed04ae51
```

and draft PR #15:

<https://github.com/hepqis-uiuc/pyclebsch/pull/15>

The minimal direct-generation route is

```python
FORDER = [1, 2, 3, -1, -2, -3]
N = 3
sites, links, plaquettes = sites_links_and_plaquettes(
    (2, 2, 2), (False, False, False), FORDER
)
irreps, singlets, conj = irreps_and_singlets(
    N, sites, "B", 6
)

for plaquette_address in plaquettes:
    elements = calc_plaquette_elements(
        N,
        plaquette_address,
        sites,
        plaquettes,
        irreps,
        singlets,
        conj,
        FORDER,
        1e-12,
        14,
        False,
    )
```

The exact callable signature in that branch is

```python
calc_plaquette_elements(
    N, P, sites, plaquettes, truncation_irreps,
    singlets, conj_dict, FORDER, EPS, PRES,
    parallelize=True,
)
```

For a second-order test, a full enumeration of the global (B=6) Hilbert space
is unnecessary.  It is sufficient to:

1. construct the vacuum and six charge-odd one-face states;
2. apply the six generated face operators once;
3. retain the resulting (Q)-space frontier;
4. evaluate the exact electric diagonal from the link Casimirs;
5. form (PVQ(E_F-QH_0Q)^{-1}QVP), with the correct overall perturbative
   sign;
6. subtract the independently computed vacuum correction.

This reduced-Krylov calculation is still a full second-order Hamiltonian test:
one application of (V) exactly exhausts the intermediate states that can
appear at this order.

The generator route has one provenance caveat.  The OBC branch is public but
is a draft pull request with no recorded review or CI checks on its GitHub page.
It is pinned here and cross-checked against the public author PBC (B=6)
table's 16 relevant amplitudes; that cross-check does not turn the result into
an independent-group replication.

## 10. Published external comparison search

The targeted primary-source search found related one-cube calculations, but no
published coefficient-level (B=6) charge-odd cube spectrum.

- Balaji et al., [arXiv:2509.25865](https://arxiv.org/abs/2509.25865), publish
  the open-cube exact curve only at (B=4=T_1).  Their (B=6) numerical plots
  concern periodic (2\times2) plaquettes and ground-state preparation, not
  this charge-odd cube shell.
- Ciavarella, Burbano, and Bauer,
  [arXiv:2503.11888](https://arxiv.org/abs/2503.11888), publish the exact
  dimension-ratio matrix element and all four local truncation amplitudes.  The
  paper's numerical spectra are two-dimensional and scalar/even; its
  three-dimensional results are resource estimates, not a one-cube
  charge-odd spectrum.
- Carlsson and McKellar,
  [arXiv:hep-lat/0303022](https://arxiv.org/abs/hep-lat/0303022), study
  (SU(N)) on a single cube and report variational (0^{++}) and (1^{+-})
  masses.  Their character-truncated variational calculation is not the
  finite-(B) reduced-electric Hamiltonian and does not publish the rational
  (1+3+2) second-order shell needed here.
- Kimura's 1984 strong-coupling calculation provides an independent
  translation-projected (T_1^{+-}) comparison, but not the finite open-cube
  (A_1/E/T_1) coefficient triplet.

This is a bounded negative result, not a claim that no such calculation exists
anywhere in the literature.

## 11. Hostile-review claim boundary

The strongest statement supported now is:

> The pinned public (B=6) author table contains every adjacent-face
> representation channel required by the charge-odd second-order Schur
> complement.  A separate direct open-cube assembly generated all six face
> tables from public pyclebsch source, retained the complete one-action
> reachable space, and obtained
> \((39/68)I+(5/612)G\) with entrywise residual
> \(6.66\times10^{-16}\).  This closes the proposed (B=6) second-order test:
> restoring the shared-link \(6\) and \(8\) channels reverses the hopping
> coefficient from \(-1/12\) to \(+5/612\) and reverses the ordered
> \(1+3+2\) shell.  The conclusion is author-code-derived, finite-volume, and
> perturbative.

What must not be claimed yet:

- The completed result is a reachable-state second-order Schur contraction,
  not a full 3,864-state matrix construction or a finite-(u) diagonalization.
- Its rational values come from double-precision public coefficients plus
  residual-controlled rational reconstruction, not symbolic CGC arithmetic.
- It is not an independent-group replication; `ymcirc`, `pyclebsch`, and the
  Balaji paper have shared author/code lineage.
- (B=6) is not onsite-complete.  The absolute matrix
  (11/34I+(5/612)G) belongs to (B\ge20/3), practically (B=7), not to
  (B=6).
- No continuum, infinite-volume, or physical glueball-mass conclusion follows
  from this finite strong-coupling shell.

## Reproduction artifacts

- `audit_balaji_b6_channel_completion.py` is a standard-library, fail-closed
  extractor and exact rational verifier.
- `balaji_b6_channel_completion_certificate.json` records the source pins,
  16-row channel census, B6/B7 same-face control, exact matrices, and claim
  boundary.

The promoted direct reconstruction artifacts are at the workspace root:

- reduced_b6_cube_second_order.py, SHA-256
  fb79dd04e532b54d1a7136da039b421d55d22b841bbe3f7db581558d8cab4575;
- b6_cube_reduced_certificate.json, SHA-256
  2aab926a1387a143aa56440fc563d95b2566b79f1b4d24fc9826be599d54a6a1;
- b6_cube_reduced_certificate_fresh_replay.json, SHA-256
  de16a1bb94060d9b7893a7671f27ee43eeee56aed1468ede19061cb1ab576ea9;
- .scratch/b6_cube_reduced/probe_b7_same_face_scalar.py, SHA-256
  e2a8a0c66dd375fd3ca2d6833a1543da1abb902292052a366292d1e56246fb59;
- b7_same_face_scalar_probe.json, SHA-256
  62ef39c9f6dad7b72fa1beee4880aae0c7b5cb373a7747116e2cd4f2a7369b2b.

A fresh channel-census run prints

```text
PASS: public B6 data contain all four shared-link channels
PASS: t3 = 5/612
PASS: B6 absolute matrix = (39/68) I + (5/612) G
PASS: same-face symmetric sextet begins at B=20/3 (integer B7)
```
