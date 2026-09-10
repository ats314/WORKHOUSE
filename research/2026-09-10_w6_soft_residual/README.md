# W6 with soft modes: a corrected-residual criterion

10 September 2026. Target: G19, selected-inverse wall W6.
Analytic conditional theorem; finite exact controls supplied separately.
This is a candidate new application of existing Schur and residual identities,
not a claim of literature priority or an established Wilson estimate.

## Established inputs and question

The source `docs/derivations/track-a-supported-statements.md`, W6-V and W6-E,
establishes, for u=A0^{-1}t and rho=Ag u-t,

    <t,(Ag^{-1}-A0^{-1})t> = -<u,(Ag-A0)u> + <rho,Ag^{-1}rho>.

Its sufficient residual certificate divides a squared residual norm by a
global coercivity constant. The selected-inverse wall, section 3, only needs
the left side to be O(|g|) b[p]. Can a soft interacting sector be allowed?

Yes, conditionally: its *corrected* residual must vanish fast enough. This
refines the sufficient W6 certificate without assuming a global uniform floor.
It does not remove the separate fast-floor requirement elsewhere in W5.

## Theorem: split inverse-energy certificate

Let H=H_s direct-sum H_h be a real or complex Hilbert space. Work first with
bounded self-adjoint operators at each fixed 0<|g|<=g0<=1. Write

    Ag = [ D  B* ; B  C ],   C >= c I > 0,
    S = D-B* C^{-1} B >= s |g|^alpha I > 0.

Here c,s are independent of g and volume, and alpha>=0. All operators may
depend on g and volume. Split rho=(rho_s,rho_h) and define

    eta = rho_s-B* C^{-1}rho_h.

Then, exactly,

    <rho,Ag^{-1}rho>
       = <rho_h,C^{-1}rho_h> + <eta,S^{-1}eta>.                 (1)

Proof: solve Ag(x,y)=rho. The second row gives
y=C^{-1}rho_h-C^{-1}Bx; substitution in the first gives Sx=eta.
In <rho_s,x>+<rho_h,y>, the two mixed terms combine into <eta,x>.
This proves (1), including noncommuting blocks and complex adjoints.

For a linear family of sources t=t(p), suppose, uniformly for every p in
the intended complete source energy space,

    |<u,(Ag-A0)u>| <= a |g| b[p],
    ||C^{-1/2}rho_h|| <= h |g| sqrt(b[p]),
    ||eta|| <= e |g|^beta sqrt(b[p]).

If q=2 beta-alpha>=1, then (1) and W6-V imply

    |<t,(Ag^{-1}-A0^{-1})t>|
       <= [a+h^2 g0+(e^2/s) g0^(q-1)] |g| b[p].              (2)

Indeed the nonnegative inverse residual energy is bounded by
[h^2 |g|^2+(e^2/s)|g|^q] b[p]; add the diagonal bound.
For a positive source weight W, taking t=T W^{-1/2}v and b[p]=||v||^2
gives the self-adjoint selected operator norm bound through the supremum
of its quadratic form on unit vectors. Separate column bounds do not suffice.

In particular, a soft floor s g^2 is compatible with W6 if eta=O(g^2),
since the soft inverse energy is O(g^2). The direct global certificate with
||rho||=O(g) and coercivity O(g^2) would only yield O(1).
More generally beta >= (alpha+1)/2 is sufficient for the required O(|g|).

## Why raw orthogonality is the wrong test

Take C=1, B=g, D=2g^2. Then S=g^2 and

    Ag = [2g^2  g ; g  1].

For rho=(0,g), raw soft projection vanishes, yet eta=-g^2 and
<rho,Ag^{-1}rho>=2g^2. This is harmless but shows the induced component.
With B=1, D=1+g^2 and the same rho, S=g^2 but eta=-g:
the inverse energy is 1+g^2, so raw orthogonality does NOT imply W6's
residual budget. The missing ingredient is corrected-source cancellation.

An exact complete residual realization checks that this is more than an
arbitrary vector example. Take A0=diag(g^2,1), Ag as in the first example,
t=(0,1). Then u=t, rho=(g,0), diagonal difference zero, and the selected
inverse difference equals 1. Thus a soft floor and small off-diagonal
coupling alone do not establish W6. The eta hypothesis excludes this case.

A successful realization uses A0=diag(2g^2,1),
Ag=[2g^2,g^2;g^2,1], and t=(0,1). Here S=2g^2-g^4,
rho=(g^2,0), eta=g^2, and the inverse difference is g^2/(2-g^2).
The full coercivity still degenerates, but W6 holds with O(g^2).

## Concrete Wilson successor

Use the actual vacuum-subtracted fast form Ag=Fg-z and full force
t=t1 p of W5, including magnetic, metric/Haar, moving-source and vacuum jets.
Choose H_s to contain the actual soft or near-harmonic channels inside Q;
this split refines Q and must not silently change the physical projection.
The specific calculation to attempt next is

    P_s rho - B* C^{-1} P_h rho = O(g^2) sqrt(b[p]),            (3)

together with an actual soft Schur floor S>=s g^2 and the hard weighted
residual bound. A symmetry cancellation of P_s rho alone is insufficient.
Both (3) and its constants must hold for the full source synthesis and
interacting ground law, uniformly in volume. No Gaussian marginal is
substituted here. For unbounded Wilson forms one must first construct the
closed square factorization and continuous dual residual; the bounded proof
above does not establish those domain hypotheses.

Hypothesis refined: uniform global coercivity in this particular residual
certificate can be replaced by a soft Schur floor plus corrected cancellation.
Downstream: once these Wilson estimates and the diagonal bound are proved,
(2) supplies W6's selected inverse bound. W5's other hypotheses are still
needed for the cubic Schur excess, followed by the physical scale/source/clock
and summability requirements. No continuum or mass-gap closure is claimed.

## Reproduction and handoff

Run `python research/2026-09-10_w6_soft_residual/check_exact.py` from REPO.
It uses only Python's Fraction and verifies exact inverse identities for
noncommuting 2-by-2 blocks and the successful/failed scalar-block families.
The general theorem is the analytic proof above, not a finite-check inference.
No Lean compilation was performed.

Brief unavailable: the local virtualenv points at a missing interpreter;
bundled Python lacks PyYAML. The local protocol's graph-task CLI/README is
also absent. A manual fallback task record and source hashes are retained;
there is no valid briefing fingerprint and no graph/ledger integration claim.
GitHub fetch failed on network connection, so novelty was checked only against
the local source paths and cached origin/main history. Existing concurrent
changes were preserved. Continue by repairing the briefing environment,
reconciling live GitHub, and checking (3) on an actual interacting Wilson block.
