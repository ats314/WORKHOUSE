# Exact two-cube B=4 charge-odd second-order folded kernel

**Status:** computational derivation package; the sealed certificate is the
machine-readable authority.  This note states the convention, derivation, and
claim boundary without promoting the B=4 result to channel-complete SU(3).

## 1. Frozen convention

On the open face-sharing two-cube prism with vertex shape `(3,2,2)` and B=4,

\[
H(u)=H_0+uV,\qquad H_0=E,\qquad V=-M,
\]

where `E` is stored exactly as an integer numerator over 3 and
`M=sum_p(W_p+W_p^dagger)`.  The normalized Hermitian charge-odd shell is

\[
Q_-={i\over\sqrt2}(W-W^\dagger)|0\rangle .
\]

The reduced resolvent and second-order Bloch/Feshbach operator are

\[
R_*=Q(E_*-H_0)^+Q,\qquad
K^{(2)}=PVR_*VP=PMR_*MP .
\]

The pseudoinverse removes every state with electric energy `E_*`, not only the
retained odd columns.

## 2. Complete zero-denominator census

The vacuum is discovered as the unique zero-electric-energy basis state and
has rank 0.  Every oriented one-plaquette state has exact energy

\[
E_*={8\over3}.
\]

The entire `H0=E_*` eigenspace has dimension 22.  Tensor-derived linear charge
conjugation has trace zero and no fixed basis state in that eigenspace, hence

\[
\dim P_{E_*,C=+}=11,\qquad \dim P_{E_*,C=-}=11.
\]

The eleven columns of `Q_-` have Gram matrix `I_11`; they therefore exhaust
the complete charge-odd zero-denominator sector.  This is a census result, not
an assumption based on the number of plaquettes.

## 3. First and second order

With `V=-M`, direct contraction gives

\[
PVP=I_{11}.
\]

Thus first order is nonzero but scalar: it shifts all eleven branches equally
and creates no branch ambiguity.  Reversing the sign of `V` reverses this
first-order block and leaves `K^(2)` unchanged.

Let `B` be the independently constructed oriented face-link boundary matrix
and `G=BB^T`.  For every nonzero off-diagonal entry,

\[
K^{(2)}_{ab}=-{1\over12}G_{ab}.
\]

The exact raw matrix, including nonuniform boundary/onsite diagonal entries,
is serialized as an integer matrix over its common denominator.  It is not
silently replaced by a scalar-plus-`G` ansatz.

## 4. Operator-level subcluster subtraction

The left cube, right cube, and shared face are folded with the same sign,
normalization, energy, and complete-zero-denominator policy.  Their normalized
source shells have dimensions 6, 6, and 1.  The existing exact coordinate
embeddings and explicit shell-coordinate maps satisfy the source-to-target
intertwining and Gram gates.

Only after forming the source operators do we compute

\[
K^-_{\rm conn}=Q_-^\dagger
\left(K_{LR}-J_LK_LJ_L^\dagger-J_RK_RJ_R^\dagger
+J_FK_FJ_F^\dagger\right)Q_- .
\]

No eigenvalue subtraction occurs.  The literal result is **not globally
proportional** to a graph Gram matrix.  Its exact decomposition is

\[
K^-_{\rm conn}=-{1\over12}G_{\rm conn}+D_{\rm conn},
\]

where `D_conn` is diagonal.  In canonical plaquette order its diagonal is

\[
(-7/4,-7/4,-15/4,-7/4,-7/4,
-7/4,-7/4,0,-7/4,-7/4,-15/4).
\]

The only off-diagonal entries are `+1/12` on cross-cell pairs
`(0,5),(1,6),(3,8),(4,9)` and their transposes; the sign is consistent with
`G_ab=-1` on those pairs.  The connected eigenvalues are

\[
\{-15/4^{(2)},-11/6^{(4)},-5/3^{(4)},0^{(1)}\}.
\]

The first-order Mobius block cancels exactly.

## 5. History and symmetry checks

Every nonzero two-action shell-to-shell history is reconstructed from the
serialized directed path ledger.  Each row retains both plaquette ownership
labels, both `W/W^dagger` branches, both local-transition ordinals, the exact
integer resolvent denominator numerator, intermediate rank, and hexadecimal
floating amplitudes.  Summing all histories reproduces the raw matrix; applying
the operator-level Mobius weights reproduces the connected matrix.  All local
transition ordinals used by those histories have a unique covariant image under
the tensor-derived cell-exchange reflection.

Hermiticity, charge-odd closure, vacuum invariance, cell-exchange covariance,
and source embedding intertwiners are separately gated.  The phase test is a
real 8,361-state coordinate reconstruction: a deterministic fourth-root
diagonal `D` is applied to form `M'=D^dagger M D` and `Q_-'=D^dagger Q_-`, after
which `PVP` and `K2` are refolded and compared.  Direct diagonalization of the
complete 4,180-dimensional charge-odd
finite Hamiltonian at training and held-out small `u` values verifies
`8/3+u+u^2 eig(K2)+O(u^3)` without using a fitted coefficient in the proof.

## 6. What this establishes—and what it does not

This establishes the exact B=4 two-cube one-plaquette charge-odd Bloch/Feshbach
operator through second order and its literal coordinate-embedding connected
subtraction.  It independently recovers the B=4 adjacent-face graph coefficient
`-1/12` on an actual face-sharing two-cube Hilbert space.

The channel-complete B=6 comparator `+5/612` is recorded only after the B=4
construction.  It is not an input, and this result does not reproduce it: B=4
omits the sextet and octet shared-link routes responsible for the known sign
reversal.  No B=6 two-cube, continuum, infinite-volume, or field-changing claim
is made here.

## 7. Reproducibility boundary

The fast verifier reads only pickle-free sealed artifacts and does not import
`pyclebsch` or any private scratch archive.  A separate **deterministic replay**
uses the same builder; it is not described as an independent implementation.
It compares every artifact array, the canonical scientific certificate fields,
and all canonical history-ledger bytes and hashes.

The manifest schema is `workhouse.su3-two-cube-b4-codd-o2-connected-kernel.v1.manifest.v2`.
It has an exact ordered ten-role file list, safe basename-only paths, and no
missing, extra, duplicate, or reordered records.  It is detached and published
last: it seals every other release byte but deliberately does not include its
own hash.  The build prints the detached manifest SHA-256, which must be carried
beside the release or recomputed directly.  This avoids a circular self-hash.

Publication validates lexical, resolved, same-file, symlink, hard-link,
nonregular, Windows reserved/trailing-dot-or-space/ADS, input-output, and
output-output aliases before computation.  Each publication candidate is
created directly beneath the destination parent, rather than inside a private
temporary directory, so Windows gives it the parent's inherited DACL before
the same-volume atomic replacement.  Existing outputs move to recoverable
same-parent backup files; the manifest is replaced last; any in-process failure
restores both prior bytes and prior ACLs.  A failed rollback retains the
direct-parent candidates, backups, and recovery record for manual repair.  A
false scientific gate and `--skip-direct-validation` publish nothing.

Windows regression tests inspect security-descriptor control flags and
inherited ACEs, exercise ordinary read/write opens, and compare the full prior
DACL after an injected rollback.  A separate isolated child process loads the
complete release and independently hashes every manifest record.  The final
canonical four-file release is additionally checked with ordinary,
non-elevated `Get-Content`/`Get-FileHash`, the strict `load_release` API, and the
artifact-only verifier; these checks are capability evidence, not additional
scientific evidence.

## 8. Numerical-to-rational boundary

Electric energies, resolvent denominators, incidence matrices, and Mobius
weights are exact integers or integer ratios.  Local CGCs and Wilson transition
amplitudes come from the hash-pinned upstream implementation in double
precision; they are not symbolic exact CGCs.  Rational matrices are accepted
only after continued-fraction reconstruction with maximum denominator
1,000,000 and residual below `2e-11`, followed by deterministic replay from the
sealed doubles.  Accordingly, “exact” here means exact within this declared
sealed numerical-to-rational protocol, not a formal exact-arithmetic Haar proof.

The pinned upstream archive is `pyclebsch-feature-obc.zip`, SHA-256
`6d16ee0fa055b143d8373efa8d57e4f5a745b362bcab6eb12318a9c09922111b`.
The certificate records critical member hashes.  The replay recipe requires
verifying that archive hash before extraction, executing hash-pinned source
bytes only, and disabling the pickle CGC cache.

## 9. Exact commands and dependencies

Requirements are CPython 3.12, NumPy 2.3.5, and SciPy 1.17.1.  From the flat
release directory:

```text
python two_cube_b4_codd_o2_connected_kernel.py
python verify_two_cube_b4_codd_o2_connected_kernel.py
python -m unittest test_two_cube_b4_codd_o2_connected_kernel.py test_two_cube_b4_codd_o2_release_safety.py -v
python rebuild_verify_two_cube_b4_codd_o2_connected_kernel.py
```

An ordinary Windows shell can check the publication boundary without
administrative elevation:

```powershell
Get-Content -Raw two_cube_b4_codd_o2_connected_kernel_manifest.json | Out-Null
Get-FileHash -Algorithm SHA256 two_cube_b4_codd_o2_connected_kernel.npz,two_cube_b4_codd_o2_connected_kernel_certificate.json,two_cube_b4_codd_o2_history_ledger.jsonl,two_cube_b4_codd_o2_connected_kernel_manifest.json
python -c "import two_cube_b4_codd_o2_kernel_loader as L; L.load_release(); print('STRICT_LOAD_OK')"
python verify_two_cube_b4_codd_o2_connected_kernel.py
```

The first command requires the three sealed upstream NPZ artifacts.  The fast
verifier and public `load_release()` API require only the ten manifest-listed
release files.  The deterministic replay again requires the upstream artifacts
and the pinned scientific Python environment.

## 10. Frozen prospective B6 protocol

Before any B6 run, freeze the same open `(3,2,2)` geometry, plaquette order and
orientation, `H0=E`, `V=-M`, normalized `Q_-`, complete `E_*` census, removal of
the entire zero-denominator eigenspace, source embeddings, and operator-level
Mobius subtraction.  Construct the incidence matrix independently and extract
the off-diagonal coefficient blindly.  The literal `5/612` must remain absent
from executable construction, branching, fitting, and acceptance tests.

Only after the B6 artifact is sealed may it be compared with `5/612`.  Shared-
link channel completeness must be proved separately, and the onsite scalar must
remain distinct from the hopping coefficient.  This protocol is prospective;
the present package contains no B6 two-cube result.
