# The Balaji T1 = B = 4 open cube, diagonalised

This is the full-Hamiltonian one-cube test that the finite-N bridge listed as
its **remaining decisive test** and had not done — for the `T1` branch of it.

## What was received

An author-data-derived reconstruction of the `B = 4` open-cube Hamiltonian:
the local plaquette coefficients are the authors' public `ymcirc` `d=3, B=4`
oriented matrix-element table (repository `hepqis-uiuc/ymcirc`, blob
`1808849c…`, file sha256 `4cad9538…`), embedded on the six faces of one open
cube with absent boundary control links fixed to the trivial irrep, then
restricted by Gauss' law at every vertex to a 243-state physical block.

## What was verified here

`independent_diagonalisation.log` is this session's own re-diagonalisation of
the pinned matrix — not a re-run of the shipped script, which needs the
upstream `ymcirc` file that did not travel with it.

    C^2 = I, [C, E] = 0, [C, M] = 0            charge conjugation is a symmetry
    charge-odd sector 121 of 243, single-face odd subspace 6

Projecting into the charge-odd sector, diagonalising `K(u) = E − u M`, and
tracking the six states by overlap onto the single-face subspace (minimum
overlap 1.0000 at u = 0.005):

    (E − E_max)/u^2  →  { −1/2 ×2,  −1/3 ×3,  0 ×1 }

with the deviation halving as `u` halves — an `O(u^3)` residual, as predicted.
That is the **reversed** `T1` ordering: doublet lowest, then triplet, then the
signed cube boundary. The channel-complete theory predicts the opposite,
`{0, (5/153)^3, (5/102)^2}`.

Stronger still, the certificate's second-order gap matrix equals

    (37/12) I − (1/12) G          to 4.3e-11,   G = B^T B the cube face Gram

so `t_3^T1 = −1/12` appears directly as the off-diagonal matrix element, and
the eigenvalues `{37/12 ×1, 11/4 ×3, 31/12 ×2}` are exactly the `T1` absolute
coefficients the independent CBB bridge certificate predicted. Two separately
produced certificates agree, and this one comes from published author data
rather than from the bridge's own algebra.

## What it does not establish

The `T1` branch only. The channel-complete `+5/612` prediction needs a `B = 6`
cube carrying all four shared-link channels, and nobody has run one.

It is also **not an independent-group replication**: the local table and the
cube paper share an author and code lineage, and the open-cube assembly is the
reconstructor's, not the authors'. The authors' own global ED matrix was not
obtained.

