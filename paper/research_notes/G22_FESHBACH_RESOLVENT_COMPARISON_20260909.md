# The Feshbach resolvent comparison, and what it does not buy

**Date** 2026-09-09. **Bears on** G17, G22, G23. **Machine certification**
suite `the Feshbach resolvent comparison`
(`src/workhouse/invariants/feshbach_resolvent.py`), four T1 checks, exact
rational linear algebra on deterministic form pairs.

## The shape

A bound that recurs across the uniformity gaps pairs a *free* inverse image
against an *interacting* one on the Feshbach complement:

    (A_g - A_0)[A_0^-1 w, A_g^-1 w],   to be bounded by C|g|, uniformly in the volume.

The Gaussian half `A_0^-1 w` is typically under control. The interacting half
is not, and the standard attack — second resolvent identity, then Neumann
iteration — needs an absolute operator bound on `A_0^-1 (A_g - A_0)` uniform in
the volume. That is where such arguments stall.

## The mixed form is removable (checked, exact)

    (A_g - A_0)[R_0 w, R_g w] = <(R_0 - R_g) w, w>

Two lines: `A_g[R_0w, R_gw] = (R_0w)^T A_g A_g^-1 w = <R_0w, w>`, and
`A_0[R_0w, R_gw] = (A_0 R_0 w)^T R_g w = <w, R_gw>` by symmetry of `A_0`.
Subtract. Hypotheses: `A_0` symmetric, both forms invertible on the complement.
Nothing else — no positivity, no smallness, no geometry.

The content is that a mixed pairing of a free against an interacting inverse
image is a difference of two quadratic forms **of the same vector**. It is a
comparison of two forms, not a quantity requiring an absolute bound on the
interacting resolvent.

## One side is then pure Gaussian (checked)

With `A_0, A_g > 0`, Legendre duality gives
`<A^-1 w, w> = sup_u (2<u,w> - A[u,u])`, attained at `u = A^-1 w`. Evaluating
each supremum at the *other* problem's optimizer sandwiches the difference:

    g V[u_g, u_g]  <=  <(R_0 - R_g)w, w>  <=  g V[u_0, u_0]      (g > 0)

The upper side names only `u_0 = R_0 w`. A free-field estimate closes it with
no information about the interacting problem at all.

## The constant, when a relative form bound exists (checked)

If `|V[u,u]| <= kappa A_0[u,u]` with `|g| kappa < 1`, then
`A_g >= (1 - |g|kappa) A_0`, so `R_g <= R_0/(1 - |g|kappa)` in the form sense,
and the remaining slot closes:

    |<(R_0 - R_g)w, w>|  <=  |g| · kappa/(1 - |g|kappa)^2 · <R_0 w, w>

The constant is built from Gaussian data and `kappa` alone. No quantity is ever
evaluated on the interacting problem.

## What this does not buy (checked, with a witness)

The saving is that `kappa` is a **relative** (KLMN-type) bound rather than an
absolute operator bound. That is also the entire remaining exposure, and the
closing check records it as a witness rather than a caveat: scaling the
interaction at fixed `g` drives `kappa` linearly up while the margin
`1 - |g|kappa` collapses, the constant degrades like `margin^-2` (0.319 to
2306.0 across the recorded family), and past `|g| kappa = 1` the form `A_g`
loses positivity on the complement and the variational route is **void**, not
merely loose.

This is the shape of the large-field problem. For a lattice gauge interaction
the relative form bound with a volume-uniform `kappa` is precisely what fails
on the rough set — which is G22's registered statement — and nothing in this
note supplies it. So:

**The identity moves the difficulty rather than removing it** -- but it moves it
somewhere with different tools, which the next section makes precise. An absolute bound
on the interacting resolvent, uniform in volume, is replaced by a
volume-uniform relative form bound. The first three checks are exact linear
algebra and prove nothing about Yang-Mills; the physics is entirely in whether
`kappa` exists uniformly, and that question is open here.

## What the exchange opens (checked, and open)

The trade is not merely verbal. A relative bound is a **max over local terms**
where an operator bound is a **sum**: if `V = sum_x V_x` and `A_0 = sum_x
A_{0,x}` with `V_x <= kappa A_{0,x}` as forms, summing gives `V <= kappa A_0`
with the *same* kappa at any volume. The absolute bound has no such stability.

Checked on a one-dimensional local kinetic form with a near-zero mode, `n = 4`
to `64`:

| n | kappa (what the identity needs) | \|\|R_0 V\|\| (what Neumann needs) |
|---|---|---|
| 4 | 0.500000 | 1.2 |
| 16 | 0.499995 | 5.1 |
| 64 | 0.499968 | 20.4 |

kappa is flat to 3e-05 across the range; the Neumann quantity grows linearly.
**The quantity that diverges with the volume is precisely the one the identity
removes.** That is a caricature of a kinetic interaction in one dimension, not
a gauge statement, and it supplies no kappa for SU(N).

Two consequences follow, stated as open directions rather than results:

1. **The small-field half closes by locality alone.** Where the Wilson
   interaction admits a local decomposition dominated term-by-term by the free
   form -- which it does at small field, by Taylor expansion -- kappa is
   volume-uniform by summation, with no global estimate needed. The residual is
   then confined to the rough set, which is exactly G22's own set.

2. **The identity survives the loss of positivity; only the variational route
   does not.** Past `|g| kappa = 1` the sandwich is void, but the collapsed
   object `<(R_0 - R_g)w, w>` is a **resolvent difference**, and resolvent
   differences are the natural object of trace-class perturbation theory and
   the Krein spectral shift -- tools that need no positivity and no relative
   form bound. Whether they apply here is untested.

Neither is claimed. Both are reachable from the identity and were not reachable
from the estimate it replaces, which is the sense in which this is a path
rather than a restatement.

## Scope

Stated for arbitrary symmetric invertible `A_0`, `A_g` on a complement. That
generality is the point — the identity is available wherever the shape appears,
including outside this corpus's geometry — and it is also the limit. This note
establishes no infinite-volume statement, contributes nothing to G17's or G23's
hypotheses beyond removing one obstacle from one estimate shape, and does not
touch the continuum limit (G19).
