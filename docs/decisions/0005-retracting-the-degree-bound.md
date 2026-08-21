# 5. Retracting the degree bound

Date: 2026-08-21

## Status

Accepted. **Retracts the mechanism proposed in ADR 0004.** The reformulation in
that ADR stands; the mechanism and its prediction do not.

## What was claimed

ADR 0004 argued that `B_shp = D_shp = 0` is kinematics: order `u^{2r}` supplies
`2r` vertices, each linear in `d` or `conj(d)`, so the numerator has degree at
most `r` in the `aᵢ`. At fourth order that gave degree ≤ 2, spanning
`{q, q², e₂}`, with the degree-3 pair `{q·e₂, e₃}` unreachable — and hence a
prediction that the `L⁻⁴` tier first appears at sixth order.

## Why it is wrong

The numerator is not `H₄`. The carrier is the `d`-direction, so

```
ε₄ = (d†·H₄·d) / (d†·d),        d†·d = q
```

which is where the `1/q` in the ansatz comes from. The numerator is `d†H₄d`, and
the projection `d†(·)d` contributes **one further `d` and one further `conj(d)`**
— one more power of `a` — on top of whatever `H₄` carries.

So four vertices bound `H₄`'s entries at degree 2, and the numerator at degree
**3**. Degree 3 is exactly `{q·e₂, e₃}`. The count permits the pair it was
supposed to forbid.

A concrete witness: `diag(aᵢ²)` is a legal degree-2 entry structure, and

```
d†·diag(aᵢ²)·d = Σaᵢ³ = q³ − 3q·e₂ + 3e₃
```

carries a nonzero `e₃`.

## The evidence that was already in hand

`MASTER_THEORY §5.1` states that the enumeration of 144 ordered two-hop
sequences *gives* the numerator span `{q, q², q·e₂, e₂, e₃}`, **rank five**.
Rank five includes the degree-3 elements: the sequences produce those terms, and
the dynamics then sets their coefficients to zero.

That is a dynamical vanishing, not a kinematic exclusion — which is precisely
what the corpus called it in the first place. The counter-evidence was in the
document being modelled, and was under-weighted.

## What survives

**The reformulation, which is exact and needs no mechanism.** Clearing the
denominator, the numerator basis stratifies by total degree in the `aᵢ`, and the
vanishing pair `{B_shp, D_shp}` *is* the degree-3 part. Since `aᵢ ~ L⁻²`, "the
`L⁻⁴` tier" and "degree 3" are the same set.

**The incidence identity.** `B B† = q·I − d·conj(d)ᵀ` with eigenvalues
`(0, q, q)` reproduces the recorded second-order C-odd spectrum and identifies
the flat carrier as the `d`-direction. It also explains the `1/q`. It simply
does not bound what fourth order can reach.

## Consequences

G14 returns to **open**, better posed than before: the question is no longer
"why is the `L⁻⁴` tier unpopulated" but "why does the degree-3 part of `d†H₄d`
vanish when the two-hop enumeration produces it." The `G14 → G9` dependency is
removed, since the prediction that created it is withdrawn.

A second-order analogue does not help: `d†H₂d = 0` exactly, but that has a known
cause — homological protection, `B†ψ = 0` — so it is not an independent instance
of a top-degree-unpopulated pattern.

The retraction is recorded rather than deleted. A mechanism that failed a stress
test is evidence about the problem, and the specific way it failed — one
uncounted projection — is worth keeping where the next attempt will see it.
