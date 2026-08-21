# 1. The code verifies; it does not adjudicate

Date: 2026-08-21

## Status

Accepted

## Context

The corpus contains an unresolved dispute between two computations of the SU(3)
`O(u⁴)` kernel (contradictions C1 and C2). Both are internally consistent. The
corpus's own verdict is *do not promote either*.

It would be easy to write code that picks one — the historical kernel is an
exact rational and looks more authoritative than a float, and choosing it would
make every downstream quantity computable. That would be a scientific error
wearing an engineering disguise: the exact rational's *upstream identification*
is precisely what is in question, and its exactness says nothing about it.

## Decision

This repository verifies arithmetic and records status. It does not adjudicate.

- Both sides of a dispute are stored, with their evidence class attached.
- No function returns "the" fourth-order kernel.
- Checks may verify the arithmetic *within* one kernel, and may quantify the
  disagreement *between* kernels. Neither is a promotion.
- Resolving C1/C2 requires the blind marked-cluster run described in gap G3,
  under its 11-item frozen protocol. That is a physics computation, and it will
  produce a new evidence record — not a code change that flips a flag.

## Consequences

Downstream quantities that depend on the fourth-order kernel — the rest-mass
series at `u⁴`–`u⁵`, the `m/√σ` ratio at those orders, the fourth-order
bandwidth — cannot be computed here, and that is the correct outcome. The
registry makes the blockage visible instead of hiding it behind a default.

Widening a tolerance or averaging the two kernels to obtain a number would
violate this decision.
