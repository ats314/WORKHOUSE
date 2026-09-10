# Accurate integration of the pending Hodge and polymer formalizations

The integration base is GitHub main at
`42b0762e4ce382efa153a969e8bb44bb77537844`. The canonical checkout was actively
changing, so the received formalization was copied into an isolated worktree.
Original pending files, including the proposed theorem registrations, remain
under `C:\WORKHOUSE\research\formalization_scope_20260910\received` with a
SHA-256 manifest. Other pending work remains in the canonical checkout.

The [located source statements](../derivations/hodge-polymer-supported-statements.md)
distinguish abstract linear algebra, real inner-product rank-one operators,
finite word enumeration, supplied polynomials and scalar geometric series.
The up-Laplacian is U=ψψ† and the carrier projector is P=U/q. Both kill an
orthogonal excitation, but they are different operators.

The former theorem registrations promoted full physical checks from word
counts or scalar implications. These promotions are removed. Source mappings
now state the exact abstract conclusion and its explicit hypotheses. The
established incidence-algebra results retain their status and receive only
the relevant scoped support. The geometric-series lemmas do not discharge
the Hamiltonian polymer construction, a free-energy bound or G17.

The original Hodge source and G17 attempted transcription retain their bytes.
The new G9 and rough-gauge G19 drafts were not used as proof of a dynamical
sixth-order coefficient or uniform interacting coercivity.

The coordinated strict Lean build and dependency export passed for 389
registered theorems and 821 declarations. The
[run record](../../runs/hodge_polymer_scope_2026-09-10/README.md) preserves the
received inputs and strict export log. Scientific regeneration and regression
results are reported against the tested revision and its CI.
