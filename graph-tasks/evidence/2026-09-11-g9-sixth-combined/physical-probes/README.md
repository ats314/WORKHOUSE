# Uncompleted physical two-face probes

These are preserved diagnostic scripts and logs, not passing invariant checks.
The `.py.txt` files retain the exact script bytes; Python can execute such a path
with the canonical REPO environment. Run from REPO. These probes can consume
substantial memory; the tree probe ended on a FLINT allocation error.

- `cluster_probe`: original raw Haar/Fierz contraction. Reproduced the 5/612
  hopping and reached 844 terms per endpoint; stopped without a sixth-order result.
- `cluster_tree_probe`: spanning-tree gauge reduction applied only to Haar
  integration, leaving H0 on the original links. Reproduced the lower moments
  quickly, then FLINT failed allocating the dense third-resolvent block.
- `cluster_link_probe`: substituted the repository's independent per-link
  Casimir projectors. Reproduced the same A2 and A4, reached 359 terms per endpoint
  after the third resolvent, then the pinned Haar router refused family (4,4).

The third run exposes the next concrete backend extension: order-four balanced
SU(3) Haar contractions (with the rank-deficient Gram quotient), and a census of
any further multiplicities reached. It does not authorize treating every family
as supported, replacing a failed integral by zero, or inferring a direct H6 coefficient.
No complete A6, folded H6 matrix or connected shape coefficient was produced.
The single-face character calculation in the main derivation is complete and
separate. The exact endpoint/moment values above remain diagnostic observations,
not new promoted physical theorem entries.

A fourth diagnostic, `cluster_support_probe`, combines terminal integrands and
all already evaluated folds BEFORE Haar integration. It retains 2023 integrands
on each diagonal and 1998 on each off-diagonal of the two-face odd model. The
family census in `cluster_weighted_support.json` includes (4,4), (5,2), (7,1),
(6,0), and conjugates on the diagonals; even off-diagonal entries require the
two-determinant (6,0)/(0,6) family. This extends the concrete backend target beyond
the first router error. These are unreduced terminal integrands, not physical
SUR coefficients or an evaluated H6 matrix; Gram identities and Haar integration
can still remove them. The full requested direct support/shape evaluation remains
unfinished. Earlier logs and errors are retained unchanged.
