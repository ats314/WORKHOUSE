# Determinant-to-Incidence Reduction at Fourth Order

**Date:** 2026-08-08  
**Status:** exact structural reduction theorem + one remaining microscopic provenance gate for the \(SU(4)\) exceptional corpus.

## 1. Question

Why should an exceptional determinant-sector correction land in the cage-annihilator module

\[
\mathcal J_\psi
=
\{C(z)S(z)\},
\qquad
S=-\widetilde N^T,
\]

rather than producing an arbitrary operator on the one-plaquette fiber?

The strongest available source facts are:

1. the \(SU(4)\) exceptional scan introduces **no new ordered words**;
2. all exceptional corrections occur inside 76 of the existing 4,171 words;
3. determinant singlet channels occur **only at the third des-Cloizeaux resolvent cut**;
4. the ordinary one-plaquette endpoint geometry is carried by the signed plaquette-to-link incidence map;
5. the completed exceptional sum obeys the exact all-zone identity
   \(H^{\rm exc}_{4,4}\psi=\Delta q_4\psi\).

These facts suggest a sharper mechanism: the determinant algebra changes an
**internal propagator/channel weight**, while the spatial entrance and exit legs
remain the same incidence legs.

This note isolates the exact algebraic implication of that statement.

---

## 2. Abstract endpoint-incidence setup

Let

\[
P
\]

denote the one-plaquette space and

\[
L
\]

the link-incidence space. Let

\[
J:P\to L
\]

be the cellular boundary map. In the Bloch convention used for the flat-band
theorem,

\[
J=\widetilde N^\dagger,
\qquad
J\psi=0.
\]

Let \(Q\) be any intermediate representation/channel space. Suppose the
one-plaquette sector couples into \(Q\) through

\[
T=U J,
\]

where

\[
U:L\to Q
\]

contains all local color-channel data after the geometric boundary leg.

An arbitrary internal resolvent or channel correction

\[
\Delta G:Q\to Q
\]

then induces the one-plaquette correction

\[
\Delta H
=
T^\dagger\Delta G T.
\]

Substituting \(T=UJ\),

\[
\Delta H
=
J^\dagger
U^\dagger\Delta G U
J.
\]

Since \(J=\widetilde N^\dagger\),

\[
\boxed{
\Delta H
=
\widetilde N
M
\widetilde N^\dagger,
\qquad
M:=U^\dagger\Delta G U.
}
\]

Thus an internal determinant correction cannot escape the two-sided boundary
ideal unless it also modifies one of the endpoint maps.

This is stronger than membership in \(\mathcal J_\psi\).

---

## 3. Theorem — internal-resolvent inheritance

### Theorem DIR

Let \(P,L,Q\) be finite-dimensional modules over any commutative coefficient
ring with involution. Let

\[
J:P\to L,\qquad T=UJ:P\to Q.
\]

For every internal correction \(\Delta G:Q\to Q\),

\[
\boxed{
T^\dagger\Delta G T
=
J^\dagger
\left(U^\dagger\Delta G U\right)
J.
}
\]

Therefore

\[
\operatorname{im}
\left[
\Delta G\mapsto T^\dagger\Delta G T
\right]
\subset
J^\dagger\operatorname{End}(L)J.
\]

If \(\psi\in\ker J\), then

\[
\boxed{
T^\dagger\Delta G T\,\psi=0.
}
\]

### Proof

By associativity,

\[
T^\dagger\Delta G T
=
(UJ)^\dagger\Delta G(UJ)
=
J^\dagger U^\dagger\Delta G UJ.
\]

If \(J\psi=0\), the last factor annihilates \(\psi\). \(\square\)

---

## 4. Consequence for determinant channels

Assume a fourth-order exceptional determinant contribution is created only by
changing the internal representation-theory propagator at a resolvent cut,
while leaving the entrance and exit plaquette-to-intermediate couplings
unchanged.

Then

\[
\boxed{
\Delta H_{\det}^{\rm connected}
=
\widetilde N M_{\det}\widetilde N^\dagger
}
\]

for some link-space Laurent operator \(M_{\det}\). Consequently,

\[
\Delta H_{\det}^{\rm connected}\psi=0.
\]

Thus the connected determinant correction lies not merely in the one-sided
cage-annihilator module but in the stronger two-sided boundary ideal.

The only way an exceptional contraction can alter the caged quotient is to
escape **at an endpoint**:

\[
\boxed{
\text{internal representation change alone}
\;\not\Rightarrow\;
\text{new mobility};
}
\]

\[
\boxed{
\text{new endpoint geometry}
\text{ or endpoint color-incidence tensor}
\;\Rightarrow\;
\text{possible escape}.
}
\]

This gives a microscopic interpretation of the protection criterion.

---

## 5. Folded/subtraction terms do not create an escape by themselves

The des-Cloizeaux effective Hamiltonian contains folded/subtraction terms, so
it is not enough to analyze only one connected chain.

Define the protected algebra

\[
\mathfrak A_J
=
\left\{
cI+J^\dagger M J
\right\}.
\]

It is closed under multiplication.

Take

\[
H_1=cI+J^\dagger MJ,
\qquad
H_2=dI+J^\dagger NJ.
\]

Then

\[
H_1H_2
=
cdI+
J^\dagger
\left(
cN+dM+MJ J^\dagger N
\right)
J.
\]

Hence

\[
\boxed{
\mathfrak A_J\mathfrak A_J
\subseteq
\mathfrak A_J.
}
\]

Therefore folded terms constructed algebraically from already-protected lower
orders remain protected. A folded term can only spoil the argument if it
contains a genuinely new endpoint operator outside the incidence factor.

This closes an algebraic gap explicitly identified in the earlier Hodge audit:
"folded/subtraction terms must be controlled in the same ideal."

---

## 6. Application to the known \(SU(4)\) corpus

The accepted \(SU(4)\) records establish:

- exceptional structure occurs in 76 pre-existing ordered words;
- no new ordered words are introduced;
- determinant singlet channels occur only at the third des-Cloizeaux cut;
- 78 exact rank-one joint Casimir channels are reconstructed;
- the completed exceptional operator satisfies the all-zone quotient-scalar
  identity.

These facts are exactly what one would expect if the exceptional correction
changes the internal \(Q\)-space propagator/channel decomposition but inherits
the same endpoint incidence maps.

If this interpretation is verified word-by-word, then

\[
\boxed{
H^{\rm exc}_{4,4}-\Delta q_4 I
\in
\mathcal I_\partial
=
\left\{
\widetilde N M\widetilde N^\dagger
\right\},
}
\]

which is strictly stronger than the already-proved conclusion

\[
H^{\rm exc}_{4,4}-\Delta q_4I
\in
\mathcal J_\psi.
\]

---

## 7. Why this is not yet declared a complete microscopic proof

The active source bundle available in this session contains the theorem,
certificate, topology ledger, and word-level rational corrections, but not the
persistent archive containing the explicit endpoint geometry of all 76
exceptional-bearing ordered words.

The current records prove that the exceptional algebra appears only at the
third resolvent cut, but they do not expose enough raw word data here to verify
the stronger statement

\[
\boxed{
T_w^{\rm exc}=U_w^{\rm exc}J_w
\quad\text{with the same }J_w
\text{ as the stable word}
}
\]

for every exceptional-bearing word \(w\).

That is now the **single microscopic gate**.

---

## 8. Exact binary gate required for closure

For every exceptional-bearing word \(w\):

1. recover its initial plaquette, first attachment link, final attachment link,
   output plaquette, and orientation signs;
2. compare those endpoint data against the corresponding stable-rank word;
3. verify that the exceptional correction modifies only the internal
   representation/channel factor;
4. write its correction as

   \[
   \delta H_w
   =
   J_w^\dagger M_w J_w;
   \]

5. assemble all 76 words and folded terms.

The required machine-readable output should state

\[
\boxed{
\texttt{endpoint\_changed}=0
}
\]

for every exceptional word.

If this gate passes, Theorem DIR gives immediately

\[
\boxed{
H^{\rm exc}_{4,4}-\Delta q_4I
=
\widetilde N M_4\widetilde N^\dagger,
}
\]

and the previously open two-sided boundary-ideal question is closed.

---

## 9. Conceptual answer

The candidate microscopic reason is therefore:

\[
\boxed{
\textbf{determinant tensors alter the internal color propagator,
not the cellular boundary legs.}
}
\]

The caged state is killed by those boundary legs. Therefore any modification
confined behind them is invisible on the caged quotient.

In diagrammatic language,

\[
\text{plaquette}
\xrightarrow{\;\partial_2\;}
\text{link/channel}
\xrightarrow{\;\text{representation dynamics}\;}
\text{link/channel}
\xrightarrow{\;\partial_2^\dagger\;}
\text{plaquette}.
\]

Changing the middle box changes amplitudes and rest-energy bookkeeping, but it
cannot couple to a closed cube boundary unless the determinant sector creates
a new way around one of the two incidence vertices.

That is the mechanism to prove microscopically.
