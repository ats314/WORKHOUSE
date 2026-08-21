#!/usr/bin/env python3
"""ENGINE_SHELL6_certify.py -- CERTIFY (or refute) the shell-6 C-odd O(y^2) ordering.

WHAT THIS DOES, AND WHY IT IS A CERTIFICATION (not a spot-check)
---------------------------------------------------------------
The shell-6 result rests on one unproven claim: that the single-layer effective
Hamiltonian H2 is "outer-W-independent" -- i.e. computing each matrix element with
the small outer W (plaquettes touching the reference loop L0) gives the SAME value
as with the large outer W (plaquettes touching the intermediate state y = R*W|L0>).
The diagonal has a structural locality proof; the OFF-diagonal did not, and in the
2026-06-13 session only THREE entries (diagonal, share-4, share-6) were checked by
hand before the result was (over-)labelled "certified".

This script removes the hedge by checking outer-W-independence for EVERY entry of
the full orbit-0 and orbit-1 rows, as a hard gate:

    for every coupled loop L':   <W_small L' | y>  ==  <W_large L' | y>   ?

If all agree, H2 is outer-W-independent on the whole row => the single layer is the
converged, exact effective Hamiltonian => the ordering is certified, and the script
prints CERTIFIED.  If ANY entry differs, it prints the discrepancies and EXITS
NON-ZERO -- no false certification.

It is cheap on top of the large-W row because W_small is a SUBSET of W_large (the
reference's links are a subset of y's links), so the small-W integrals are already
computed/cached when the large-W value is formed.

Speed: uses W self-adjoint (W = sum 2 Re Tr U_p, real) to read the row as
<W L'|y> with W L' tiny (one 2-trace per plaquette), instead of forming W y (~1e4
monomials).  Exact rational arithmetic throughout.

HOW TO RUN
----------
Put this file in  programs/one_plaquette/shell6_o2/  (next to ENGINE_HAAR_shell6_final3.py),
then:

    cd programs/one_plaquette/shell6_o2
    python3 ENGINE_SHELL6_certify.py            # rowbox=1 (matches the existing engines)
    python3 ENGINE_SHELL6_certify.py 2          # rowbox=2  -> also rules out missed couplings

It is RESUMABLE: integrals are cached to ./shell6_certify_cache.pkl (override with
the SHELL6_CACHE env var).  If it is interrupted, just run it again -- it picks up
where it left off.  First full run is the slow one (it fills the cache); re-runs are
fast.  Expect the orbit-0 row to dominate the time.

Dependencies (all already in the repo): shell6_final3, shell6_o2_engine2,
link_o2_v2, fast_haar, shell6_analyze, su3_moments_ext.  The script puts both its
own directory and the parent one_plaquette/ on sys.path so su3_moments_ext resolves
regardless of where you launch it from.
"""
import sys, os, itertools, pickle, atexit, tempfile, time
from fractions import Fraction as F
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))   # parent one_plaquette/ -> su3_moments_ext

import ENGINE_FLUX_shell6_o2_engine2 as G
import ENGINE_HAAR_fast_haar
import link_o2_v2 as E
import ENGINE_SHELL6_shell6_analyze as A
import ENGINE_HAAR_shell6_final3 as S3   # edges_at, plqs_touching, resolvent, woe, is_e0, csig, orbit

# ---------------------------------------------------------------- resumable cache
CACHE = os.environ.get("SHELL6_CACHE", os.path.join(HERE, "shell6_certify_cache.pkl"))
if os.path.exists(CACHE):
    try:
        fast_haar._TNCACHE = {k: F(v) for k, v in pickle.load(open(CACHE, "rb")).items()}
        print(f"[cache] loaded {len(fast_haar._TNCACHE)} integrals from {CACHE}", flush=True)
    except Exception as e:
        print("[cache] load failed:", e, flush=True)

def _save():
    try:
        d = os.path.dirname(CACHE) or "."
        fd, tmp = tempfile.mkstemp(dir=d)
        with os.fdopen(fd, "wb") as f:
            pickle.dump({k: str(v) for k, v in fast_haar._TNCACHE.items()}, f)
        os.replace(tmp, CACHE)
    except Exception as e:
        print("[cache] save failed:", e, flush=True)

_orig = fast_haar.haar_tn
_N = [0]
def _persist(words):
    key = tuple(tuple(w) for w in words)
    hit = key in fast_haar._TNCACHE
    r = _orig(words)
    if not hit:
        _N[0] += 1
        if _N[0] % 50 == 0:
            _save()
    return r
fast_haar.haar_tn = _persist
E.D.integrate_monomial = lambda m: _persist(list(m))
atexit.register(_save)

# ---------------------------------------------------------------- gates
PASS = []
def gate(name, cond):
    PASS.append(bool(cond))
    print(f"  GATE {'PASS' if cond else 'FAIL'} :: {name}", flush=True)
    if not cond:
        raise SystemExit("GATE FAILED: " + name)

# ---- published exact values to certify against (2026-06-13 RESULT note) ----
PUBLISHED = {
    "0--":      F(-12075379, 959310),
    "2--(E)":   F(-13034689, 959310),
    "2--(T2)":  F(-12714919, 959310),
    "3+-":      F(-21281, 1530),
}

# ---------------------------------------------------------------- the dual row
def dual_row(ref, rowbox=1):
    """Compute the H2 row for reference loop `ref` under BOTH outer-W choices and
    gate that they agree entry-by-entry.  Returns the (identical) row as {shape: F}.

    inner W (the resolvent input) is ALWAYS Winner = plaquettes touching the
    reference -- that one is provably complete (H0 is per-link, so the resolvent
    never leaves the reference's links).  Only the OUTER read W is varied:
        small outer W = Winner          (plaquettes touching the reference)
        large outer W = Wouter          (plaquettes touching the intermediate y)
    """
    L0e = S3.edges_at(ref, (0, 0, 0))
    H0 = E.make_H0_links()
    Winner = S3.plqs_touching(set(l for (l, _) in L0e))
    L0w = E.canon_word(S3.woe(L0e))
    v = E.apply_W_links(L0w, Winner)

    # close the basis under H0 (per-link), then project off the e0 manifold + solve
    basis = set(v.keys()); fr = list(v.keys())
    while fr:
        m = fr.pop()
        for mm in H0.mono(m):
            if mm not in basis:
                basis.add(mm); fr.append(mm)
    man = [{m: F(1)} for m in basis if S3.is_e0(m)]
    y = S3.resolvent(H0, F(4), man, v, f"{ref} resolvent")   # E0 = 4 (electric vacuum)
    _save()

    ylinks = set(l for m in y for w in m for (l, p) in w)
    Wouter = S3.plqs_touching(ylinks)
    assert set(map(tuple, Winner)) <= set(map(tuple, Wouter)), "Winner should nest in Wouter"
    print(f"  ref={ref}: |Winner|={len(Winner)} |Wouter|={len(Wouter)} |y|={len(y)} terms", flush=True)

    SH = G.shapes6()
    HEX = [s for s in SH if len(set(d // 2 for d in s)) == 3]
    Rsmall = {}; Rlarge = {}; diffs = []
    cnt = 0; t0 = time.time()
    for s in HEX:
        for tt in itertools.product(range(-rowbox, rowbox + 1), repeat=3):
            es = S3.edges_at(s, tt)
            if not G.is_simple_loop(es):
                continue
            # if L' shares no link with y, <W L'|y> = 0 under BOTH outer W -> skip
            if not any(l in ylinks for (l, _) in es):
                continue
            Lp = E.canon_word(S3.woe(es))
            vsmall = E.inner(E.apply_W_links(Lp, Winner), y)
            vlarge = E.inner(E.apply_W_links(Lp, Wouter), y)
            if vsmall != 0:
                Rsmall[s] = Rsmall.get(s, F(0)) + vsmall
            if vlarge != 0:
                Rlarge[s] = Rlarge.get(s, F(0)) + vlarge
            if vsmall != vlarge:
                diffs.append((s, tt, vsmall, vlarge))
            cnt += 1
            if cnt % 20 == 0:
                print(f"    ...{cnt} positions | {len(fast_haar._TNCACHE)} integrals "
                      f"| {time.time()-t0:.0f}s | diffs so far: {len(diffs)}", flush=True)
                _save()
    _save()
    nshapes = len(set(list(Rsmall) + list(Rlarge)))
    if diffs:
        print(f"  !! {len(diffs)} entries DIFFER between small and large outer W:", flush=True)
        for d in diffs[:30]:
            print("     DIFF shape=%s t=%s small=%s large=%s" % d, flush=True)
    gate(f"[{ref}] FULL-ROW outer-W-independence ({cnt} positions, {nshapes} shapes)", not diffs)
    return Rlarge

# ---------------------------------------------------------------- channel energies
def channel_energy(R0, L0, Gn, Ps, Cs):
    """Exact rational O(y^2) energy of a multiplicity-1 channel from its row R0,
    by the symmetry-projected Rayleigh quotient  num/den  (valid because H2
    commutes with O_h x C and the channel is mult-1)."""
    num = F(0); den = 0
    for c in (0, 1):
        for mi, M in enumerate(A.OH):
            g = A.gact(L0, M); g = A.rev(g) if c else g
            chi = A.CH[Gn][A.CLS[mi]] * (1 if A.DET[mi] == 1 else Ps) * (1 if c == 0 else Cs)
            num += chi * R0.get(g, F(0))
            if g == L0:
                den += chi
    return F(num, den) if den else None

def main():
    rowbox = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    print("=" * 72)
    print(f"shell-6 C-odd O(y^2) CERTIFICATION  (rowbox={rowbox})")
    print("full-row outer-W-independence test + exact channel rationals")
    print("=" * 72, flush=True)

    SH = G.shapes6()
    HEX = [s for s in SH if len(set(d // 2 for d in s)) == 3]
    L0 = HEX[0]
    orb0 = sorted(S3.orbit(L0, HEX))
    print(f"ORBIT 0 (size {len(orb0)}) -- carries 0--, 2--(E), 2--(T2), 2+-, exc 1+-:", flush=True)
    R0 = dual_row(L0, rowbox)

    # ---- assemble the 24x24, check Hermiticity + O_h x C symmetry ----
    N = len(orb0); idx = {s: i for i, s in enumerate(orb0)}
    gof = {}
    for c in (0, 1):
        for M in A.OH:
            t = A.gact(L0, M); t = A.rev(t) if c else t
            if t not in gof:
                gof[t] = (M, c)
    ginv = lambda s, M, c: A.gact(A.rev(s) if c else s, M.T)
    M2 = np.array([[float(R0.get(ginv(orb0[i], *gof[orb0[j]]), F(0))) for j in range(N)] for i in range(N)])
    gate("orbit-0 H2 Hermitian", np.allclose(M2, M2.T, atol=1e-9))
    def pm(M, c):
        P = np.zeros((N, N))
        for h in orb0:
            t = A.gact(h, M); t = A.rev(t) if c else t
            if t in idx:
                P[idx[t], idx[h]] = 1
        return P
    gate("orbit-0 H2 commutes with O_h x C",
         all(np.allclose(M2 @ pm(M, c), pm(M, c) @ M2, atol=1e-9) for M in A.OH[:8] for c in (0, 1)))

    energies = {}
    for Gn, Ps, Cs, nm in [('A1', -1, -1, '0--'), ('E', -1, -1, '2--(E)'),
                           ('T2', -1, -1, '2--(T2)'), ('T2', 1, -1, '2+-'),
                           ('T1', 1, -1, '1+-exc')]:
        e = channel_energy(R0, L0, Gn, Ps, Cs)
        if e is None:
            continue
        energies[nm] = e
        print(f"  {nm:8s}[{Gn}]: {e}  ~{float(e):+.6f}", flush=True)

    # ---- orbit 1 -> 3+- ----
    L1 = next(h for h in HEX if h not in set(orb0))
    print(f"ORBIT 1 (size {len(S3.orbit(L1, HEX))}) -- carries 3+-:", flush=True)
    R1 = dual_row(L1, rowbox)
    e3 = channel_energy(R1, L1, 'A2', 1, -1)
    if e3 is not None:
        energies['3+-'] = e3
        print(f"  3+-     [A2]: {e3}  ~{float(e3):+.6f}", flush=True)

    # ---- gate against the published exact values ----
    for nm, want in PUBLISHED.items():
        got = energies.get(nm)
        gate(f"{nm} == published {want}", got is not None and got == want)

    # ---- the ordering ----
    keys = ['3+-', '2--(E)', '2--(T2)', '0--']
    items = sorted([(k, energies[k]) for k in keys if k in energies], key=lambda kv: kv[1])
    print("\n" + "=" * 72)
    print("O(y^2) ORDERING (lightest -> heaviest):")
    print("  " + "  <  ".join(k for k, _ in items))
    b = energies.get('0--')
    for k, v in items:
        rel = f"   vs 0--: {v - b}" if b is not None else ""
        print(f"    {k:8s}: {v}  ~{float(v):+.6f}{rel}")
    allpass = all(PASS) and all(p for p in S3.PASS)
    print("=" * 72)
    print(f"gates (this script): {sum(PASS)}/{len(PASS)} | resolvent gates (S3): {sum(S3.PASS)}/{len(S3.PASS)}")
    if allpass:
        print("\n  RESULT: CERTIFIED -- H2 is outer-W-independent over the FULL row,")
        print("  the single-layer effective Hamiltonian is converged, and the exact")
        print("  rationals match the published ordering 3+- < 2--(E) < 2--(T2) < 0--.")
        if rowbox < 2:
            print("  (For full closure, re-run with `python3 ENGINE_SHELL6_certify.py 2` to confirm")
            print("   no coupled loop is missed by the rowbox.)")
    else:
        print("\n  RESULT: NOT CERTIFIED -- see failed gate(s) above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
