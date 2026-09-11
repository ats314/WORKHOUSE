# The odd orders of the strong-coupling band are determinant families

11 September 2026. A graph-guided derivation in the G16 task that follows
ADR 0046: the planar-band decision established the N^-(4k-1) law of the
even orders and left the odd orders unexamined. This note proves that the
odd orders are absent for every even N at every order, and for odd N below
order N - 2, by a centre-parity argument on the Haar integrals of the strong-
coupling expansion; it identifies the first odd order of odd N as a single
one-plaquette vertex with a closed form; and it tests the statements with
the third engine at N = 3..7 and over Q(N). It is a new connection relative
to the reviewed sources, not a claim of worldwide mathematical priority.

## 1. Setting

The band coefficients are matrix elements of the des Cloizeaux effective
operator on the one-plaquette sector of the Kogut-Susskind strong-coupling
Hamiltonian, `H0 = (1/2) sum_links E^2`, `V = -u W`, `W` the sum of all
plaquette characters in both orientations, `u = beta_N/(2N)` (CLAUDE.md,
non-negotiable 4). The order-m operator is

    H_m = (-1)^m P W R W ... W P + (folds),

with m factors of `W`, `R = Q (E0 - H0)^-1 Q`, and the folds are products of
lower-order elements whose orders sum to m (des Cloizeaux; at third order
`H_3 = -(P W R W R W P - (1/2){P W R^2 W P, P W P})`). Every element is a
finite sum of Haar integrals of products of face words: `m + 2` words for a
direct term (ket, m insertions, bra), and for a fold term each factor is
itself such an element of its own order.

For a history let `c_f` be the number of words of face `f` (either
orientation) and `phi_f` its net flux, the number of `f` words minus the
number of `f-bar` words. Then `phi_f = c_f (mod 2)`. A link's net flux is a
signed sum of the `phi_f` over the faces containing it, and the Haar integral
of a word vanishes unless every link's net flux is `0 mod N` (the SU(N)
centre; `loopcalc._charge_zero`).

## 2. The centre-parity theorem

**Lemma (the link set T).** Let `T` be the set of x-links at even y, y-links
at even z, and z-links at even x. Every plaquette of Z^3 contains an odd
number of links of `T`.

*Proof.* An (x,y)-face with base `(x, y, z)` contains the x-links at `y` and
`y + 1` (exactly one of them at even y) and two y-links both at the same `z`
(both or neither in `T`); its total is odd. An (x,z)-face contains two
x-links at the same `y` (both or neither), and the z-links at `x` and
`x + 1` (exactly one): odd. A (y,z)-face contains the y-links at `z` and
`z + 1` (exactly one) and two z-links at the same `x`: odd. The suite checks
this on every face of a 6^3 block. QED

**Theorem A (even N).** For even N, every history with an odd number of face
words has zero Haar weight. Consequently every odd-order matrix element of
the effective operator vanishes identically, on every cluster, in both
C-parity sectors, at every order.

*Proof.* Sum the link fluxes over the links of `T` modulo 2. By the lemma
each face contributes `phi_f` an odd number of times, so the sum is
`sum_f phi_f = sum_f c_f (mod 2)`. Each link flux is `0 mod N`, hence even,
so `sum_f c_f` is even. A direct order-m element has `m + 2` words; a fold
term at odd m is a product of elements whose orders sum to m, so one factor
has odd order and its own histories have an odd number of words. QED

**Theorem B (odd N).** For odd N, an odd-word history has a link of odd flux,
hence `|flux| >= N` on that link, hence at least N words touch it: the order
m of a nonvanishing odd element satisfies `m + 2 >= N`. The band is an even
series in u through order N - 3. At order `m = N - 2`, only the one-plaquette
diagonal element between a face and its conjugate survives.

*Proof.* If every link flux were even the argument of Theorem A would force
`sum_f c_f` even. So some link has odd flux, which is a nonzero multiple of
N, so at least N of the `m + 2` words contain that link. At `m + 2 = N` all
N words contain that link `l`, all traversing it in the same direction. Two
distinct plaquettes containing `l` meet only in `l`, so any other link `l'`
of a face `f` containing `l` is touched in this history by the words of `f`
alone, all of one orientation: its flux is `+-c_f`, which is `0 mod N` only
if `c_f = N`. Hence all N words are one face's, and the history is a
one-plaquette history. The pair hops and leakages, which need a word of the
second face, vanish; the surviving element is the one between
`chi_F` and `chi_F-bar` of one plaquette. QED

## 3. The first odd-order vertex of odd N

On one plaquette the four links are private, so by Peter-Weyl the product
`U_1 U_2 U_3 U_4` is one Haar matrix and the states are characters `chi_R`;
`H0` on `chi_R` is `2 C_2(R)` (four links, `C_2(R)/2` each), `E0 = 2 C_F`,
and `W chi_R = chi_R chi_F + chi_R chi_F-bar` adds or removes one box. The
only path from `F` (one box) to `F-bar = Lambda^(N-1)` in `N - 2` steps
runs through the columns `Lambda^k`, k = 2..N-2, each step adding a box to
the column (any other irrep on the path would have a second column and could
never reach a single column of N - 1 boxes by adding boxes). With
`C_2(Lambda^k) = k(N-k)(N+1)/(2N)`,

    E_k - E_0 = (k - 1)(N - k - 1)(N + 1)/N,

so the direct term is `(-1)^(N-2) prod_(k=2)^(N-2) 1/(E_0 - E_k)` and the
folds vanish (every fold contains an odd-order factor of order below N - 2):

    H_(N-2)(F-bar, F) = -(N/(N+1))^(N-3) / ((N-3)!)^2 .

At N = 3 this is `-1`: the first-order vertex `-P W P`, which is `+u` in the
C-odd sector `(chi_F - chi_F-bar)/sqrt 2` and `-u` in the C-even sector, the
corpus's `E_flat = 8/3 + u + ...`. At N = 5 it is `-25/144`, so the C-odd
and C-even third-order towers split by `+-25/144` while every third-order hop
and leakage is zero.

## 4. What the third engine confirms

`runs/odd_order_band_2026-09-11` and the suite "the odd orders of the band
are determinant families (G16)" (seven T1 checks). Two engines are used: the
word engine `loopcalc` with its third-order des Cloizeaux operator, and a
one-plaquette character engine (Pieri rule for `chi_F` and `chi_F-bar`,
`H0 = 2 C_2`, Rayleigh-Schrodinger series in each C-parity sector, which on
a one-dimensional sector model space is the des Cloizeaux diagonal). The two
agree on every tower and vacuum energy at N = 3, 4, 6, 7 through third order.

- N = 3: the third-order operator reproduces the whole SU(3) third-order
  ledger, every number a (3,0) determinant family: `B_3 = 1975/124848`
  (coplanar `-B_3`, perpendicular `+B_3`), `t_3+ = -6335/249696` in both
  geometries, the domino diagonals `-24541/62424` and `-517313/6242400`, the
  vacuum route `<1|H_3|1> = -9/32` (and `<1|H_2|1> = -3/4`), hence the
  vacuum-subtracted towers `7/32` and `101/200`, `leak_3 = -12331/249696`
  in both geometries, and `d_3 = 7/32 + 12 leak_3 - 4 B_3 = -109151/249696`.
- N = 4 and N = 6: every first- and third-order tower, hop and leakage is
  zero in both sectors, as is the third-order vacuum.
- N = 5: the towers split by `+-25/144` (character engine; the word
  engine's five-box determinant families are too expensive here), and the
  word engine's hops and X-touched leakages of both pairs are zero.
- N = 7: every first- and third-order element is zero.
- Character engine, N = 3..11 through seventh order: the odd orders 1, 3, 5,
  7 vanish at N = 4, 6, 8, 10; at N = 5, 7, 9 the first odd order is N - 2
  with the C-odd tower `(N/(N+1))^(N-3)/((N-3)!)^2` (25/144, 2401/2359296,
  6561/6400000000), every lower odd order zero.
- Over Q(N), where only balanced Haar families exist, the eight third-order
  pair elements are identically zero: the third order has no balanced-family
  content at any rank.

## 5. Consequence for G16 and the planar limit

ADR 0046 wrote the band as a series in `tau^2 = (beta/N^3)^2` with
N-independent limits through fourth order. Theorems A and B make the absence
of odd terms exact: for even N at every order, for odd N through order
N - 3, so at any fixed order the planar limit has no odd term. The first odd
term of odd N is the vertex of section 3 at order N - 2; with `u = N^2 tau/2`
its size relative to the plaquette energy `2 C_F ~ N` is, by Stirling,
`(e^2 tau/2)^N` times a power of N. It is exponentially small in N for
`tau < 2/e^2 = 0.27` and exponentially large above it. Nothing here bears on
the even orders' N^-(4k-1) law or on the overlap theorem G16 asks for.

## 6. Hypotheses and scope

The statements concern the strong-coupling series of the one-plaquette
sector on Z^3 with the Kogut-Susskind `H0` and the plaquette perturbation, at
fixed order, on finite clusters of the infinite lattice (on a periodic
lattice the lemma needs even extents). They are statements about the
coefficients, not about convergence, and they use only the SU(N) centre
constraint of the Haar integral and the Peter-Weyl structure of one
plaquette. The N = 3..7 numbers are exact engine computations; the closed
form at odd N is derived, and checked against the engines at N = 3, 5, 7 and 9.
