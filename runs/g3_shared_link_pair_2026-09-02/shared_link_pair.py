"""The fourth-order nearest-neighbour amplitude on the lattice, by cluster expansion.

For a shared-link pair (P, Q) the lattice fourth-order element <P|H4|Q> is the
sum of cluster cumulants over the clusters a history of four insertions can
touch.  Such a history, with net charge P Qbar, is one of two kinds: P
and Qbar with one X Xbar pair besides, or -- when P and Q are two faces of one
cube -- the cube's OTHER four faces, each once, because a cube's six faces
have zero net triality.  So the lattice element between two adjacent
plaquettes is a finite sum of connected cluster cumulants:

    H4_PQ = W(P,Q)_PQ  +  sum_X [ W(P,Q,X)_PQ - W(P,Q)_PQ ]  +  sum_cubes D_cube,

X over every plaquette sharing a link with P or Q (an X sharing no link gives
a zero cumulant -- the linked-cluster gate checks that on one far X), and
D_cube the direct term over the cube-completion histories on the six-face
cluster, which no fold or A-term reaches.  The cube term is the -5/48 of the
normal orbit (it returns exactly -5/48 there); it exists for the rotation pair,
two faces of one cube, and for no coplanar pair, which is why the in-plane
element needs no such term.

W(P,Q) is the engine's full assembly on the pair, A-terms and J included, with
the baryonic histories {Q, Q, Pbar, Pbar} whose Haar families reach the
pure-six link.  The three-cluster cumulants need only X-touched histories, in
which the A-terms and J cancel (docstring of chain_amplitude.chain_cumulant).
"""

from __future__ import annotations

import json
import sys
import time
from collections import defaultdict
from fractions import Fraction as F

from pathlib import Path  # noqa: E402

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
# the cluster machinery is the replication run's, pinned there; the Haar
# integrals are workhouse.haar_epsilon (the engine's balanced contraction
# plus epsilon-network reduction for the determinant, mixed and pure-six
# families, which is what makes the pair's baryonic histories tractable)
sys.path.insert(0, str(ROOT / "runs" / "g3_chain_amplitude_replication_2026-09-02"))
sys.path.insert(0, str(ROOT / "src"))
import chain_amplitude as C  # noqa: E402
from workhouse.haar_epsilon import inner as batch_inner  # noqa: E402

M = C.M
PLANES = [(0, 1), (0, 2), (1, 2)]

# the registered records, for the comparison line only
PI_RECORD = F(-20535103905179, 1264270320593280)  # (0,1)->(0,1) at (1,0,0)
RHO_RECORD = F(238714892212171339, 29002361154409843200)  # (0,1)->(0,2) at (0,0,0)


def plaquette_links(plane, base):
    w = C.plaquette(plane, base)
    return frozenset(l for l, _ in w.occ)


def plaquettes_containing(site, d):
    """The four plaquettes containing the link (site, d)."""
    out = []
    for e in range(3):
        if e == d:
            continue
        plane = tuple(sorted((d, e)))
        out.append((plane, tuple(site)))
        base = list(site)
        base[e] -= 1
        out.append((plane, tuple(base)))
    return out


def neighbours(faces):
    """Every plaquette sharing a link with one of `faces`, excluding them."""
    seen = {plaquette_links(pl, b) for pl, b in faces}  # by link set: orientation-blind
    out = []
    for pl, b in faces:
        for l in plaquette_links(pl, b):
            inv = {v: k for k, v in C.LINKS.items()}
            site, d = inv[l]
            for x in plaquettes_containing(site, d):
                links = plaquette_links(*x)
                if links not in seen:
                    seen.add(links)
                    out.append(x)
    return out


import os  # noqa: E402

EPS_BLIND = os.environ.get("EPS_BLIND") == "1"


def _balanced_only(bra, w):
    """True if every link of <bra|w> is a balanced (a, a) family: no epsilon sector."""
    cnt = defaultdict(lambda: [0, 0])
    for l, is_u in bra.occ:
        cnt[l][0 if not is_u else 1] += 1
    for l, is_u in w.occ:
        cnt[l][0 if is_u else 1] += 1
    return all(a == b for a, b in cnt.values())


def element(cl, i, vec):
    """<d_i|vec>; with EPS_BLIND=1 every word whose integrand has an unbalanced
    link is dropped -- the "direct balanced contraction" U5 makes a prediction for."""
    bra = cl.words[i]
    if EPS_BLIND:
        vec = {w: c for w, c in vec.items() if _balanced_only(bra, w)}
    return batch_inner(bra, vec)


def two_insertion_moments(cl):
    m = len(cl.words)
    rng = range(m)
    vd = [cl.V(d) for d in cl.model]
    gv = [cl.G(v) for v in vd]
    ggv = [cl.G(x) for x in gv]
    gggv = [cl.G(x) for x in ggv]
    A = [[element(cl, i, vd[j]) for j in rng] for i in rng]
    K2 = [[element(cl, i, cl.V(gv[j])) for j in rng] for i in rng]
    N = [[element(cl, i, cl.V(ggv[j])) for j in rng] for i in rng]
    J = [[element(cl, i, cl.V(gggv[j])) for j in rng] for i in rng]
    for name, X in (("A", A), ("K2", K2), ("N", N), ("J", J)):
        assert all(X[i][j] == X[j][i] for i in rng for j in rng), f"{name} not symmetric"
    # PVP is the baryonic vertex <P|V|Pbar> = 1, a (0,3) determinant integral:
    # in the epsilon-blind contraction it is zero, and the assembly reduces to
    # the PVP = 0 form by itself.
    expected = 0 if EPS_BLIND else 1
    assert all(A[i][j] == (expected if (i // 2 == j // 2 and i != j) else 0) for i in rng for j in rng)
    return A, K2, N, J, gv


def pair_h4(faces2, log=print):
    """The engine's full H4 between the two faces of a shared-link pair, 2x2 block each way."""
    t0 = time.time()
    cl = C.Cluster(faces2)
    m = len(cl.words)
    rng = range(m)
    A, K2, N, J, gv = two_insertion_moments(cl)
    log(f"    pair two-insertion moments {time.time() - t0:.1f}s")
    ia, ib = (0, 1), (2, 3)
    pairs = [(i, j) for i in ia for j in ib] + [(i, j) for i in ib for j in ia]
    C1, D = {}, {}
    for bras, kets in ((ia, ib), (ib, ia)):
        targets = {C.triality(cl.words[i]) for i in bras}
        allow = [C.reachable(targets, cl.words, k) for k in range(4)]
        for j in kets:
            s1 = C.filt(cl.V(cl.model[j]), allow[3])
            s2 = C.filt(cl.V(cl.G(s1)), allow[2])
            r2 = cl.G(s2)
            vgr2 = C.filt(cl.V(cl.G(r2)), allow[0])
            s3 = C.filt(cl.V(r2), allow[1])
            z = C.filt(cl.V(cl.G(s3)), allow[0])
            for i in bras:
                t1 = time.time()
                C1[(i, j)] = element(cl, i, vgr2)
                D[(i, j)] = element(cl, i, z)
                log(f"    pair C1[{i}][{j}] = {C1[(i, j)]}  D[{i}][{j}] = {D[(i, j)]}  ({time.time() - t1:.0f}s, |z|={len(z)})")
    assert all(D[(i, j)] == D[(j, i)] for i, j in pairs), "D not symmetric"
    H4 = {}
    for i, j in pairs:
        fold = sum(K2[i][k] * N[k][j] + N[i][k] * K2[k][j] for k in rng) / 2
        H4[(i, j)] = D[(i, j)] - C1[(i ^ 1, j)] - C1[(j ^ 1, i)] - fold + J[i][j]
    assert all(H4[(i, j)] == H4[(j, i)] for i, j in pairs), "H4 not symmetric"
    log(f"    pair H4 done {time.time() - t0:.1f}s")
    return H4, {"A": A, "K2": K2, "N": N, "J": J, "C1": C1, "D": D}


def three_cluster_cumulant(faces2, x, log=print):
    """W(P,Q,X) - W(P,Q) on the P-block x Q-block elements, X-touched histories only."""
    t0 = time.time()
    faces3 = list(faces2) + [x]
    cl3 = C.Cluster(faces3)
    cl2 = C.Cluster(faces2)
    m3, m2 = 6, 4
    _, K2_3, N_3, _, _ = two_insertion_moments(cl3)
    _, K2_2, N_2, _, _ = two_insertion_moments(cl2)
    assert all(cl2.words[k] == cl3.words[k] for k in range(4))
    x_words = {cl3.words[4], cl3.words[5]}

    def V_split(u, t):
        out_u, out_t = {}, {}
        for w in cl3.words:
            mu, mt = C.word_mul(u, w), C.word_mul(t, w)
            if w in x_words:
                out_t = C.vadd(out_t, mu)
            else:
                out_u = C.vadd(out_u, mu)
            out_t = C.vadd(out_t, mt)
        return out_u, out_t

    D_t = {}
    for bras, kets in (((0, 1), (2, 3)), ((2, 3), (0, 1))):
        targets = {C.triality(cl3.words[i]) for i in bras}
        allow = [C.reachable(targets, cl3.words, k) for k in range(4)]
        for j in kets:
            u, t = V_split(cl3.model[j], {})
            u, t = C.filt(u, allow[3]), C.filt(t, allow[3])
            u, t = cl3.G(u), cl3.G(t)
            u, t = V_split(u, t)
            u, t = C.filt(u, allow[2]), C.filt(t, allow[2])
            u, t = cl3.G(u), cl3.G(t)
            u, t = V_split(u, t)
            u, t = C.filt(u, allow[1]), C.filt(t, allow[1])
            u, t = cl3.G(u), cl3.G(t)
            _, t = V_split(u, t)
            t = C.filt(t, allow[0])
            for i in bras:
                D_t[(i, j)] = element(cl3, i, t)
    assert all(D_t[(i, j)] == D_t[(j, i)] for (i, j) in D_t), "D_touched not symmetric"

    def fold(K2, N, i, j, m):
        return sum(K2[i][k] * N[k][j] + N[i][k] * K2[k][j] for k in range(m)) / 2

    W = {}
    for i in (0, 1):
        for j in (2, 3):
            W[(i, j)] = D_t[(i, j)] - (fold(K2_3, N_3, i, j, m3) - fold(K2_2, N_2, i, j, m2))
    log(f"    X = {x}: cumulant C-odd {codd(W)}  C-even {ceven(W)}  ({time.time() - t0:.0f}s)")
    return W


def cubes_containing(faces2):
    """Unit cubes having both faces among their six, each as its four other faces."""
    links = [plaquette_links(pl, b) for pl, b in faces2]
    out = []
    bases = {
        (x, y, z)
        for pl, b in faces2
        for x in (b[0] - 1, b[0])
        for y in (b[1] - 1, b[1])
        for z in (b[2] - 1, b[2])
    }
    for base in sorted(bases):
        faces = []
        for (i, j), k in (((0, 1), 2), ((0, 2), 1), ((1, 2), 0)):
            for off in (0, 1):
                bb = list(base)
                bb[k] += off
                faces.append(((i, j), tuple(bb)))
        fl = [plaquette_links(pl, b) for pl, b in faces]
        if all(any(fs == L for fs in fl) for L in links):
            out.append([f for f, fs in zip(faces, fl) if fs not in links])
    return out


def cube_completion(faces2, others, log=print):
    """D over the histories whose four insertions are the cube's other four faces, once each."""
    t0 = time.time()
    cl = C.Cluster(list(faces2) + list(others))
    side_words = {cl.words[k]: k // 2 for k in range(4, len(cl.words))}

    def V_sides(vec):
        out = defaultdict(F)
        for (w, used), c in vec.items():
            for sw, face in side_words.items():
                if face in used:
                    continue
                for w2, c2 in C.word_mul({w: c}, sw).items():
                    out[(w2, used | {face})] += c2
        return {k: v for k, v in out.items() if v}

    def G(vec):
        by_used = defaultdict(dict)
        for (w, used), c in vec.items():
            by_used[used][w] = c
        out = {}
        for used, sub in by_used.items():
            for w, c in cl.G(sub).items():
                out[(w, used)] = c
        return out

    def filt(vec, allow):
        return {k: v for k, v in vec.items() if C.triality(k[0]) in allow}

    D = {}
    for bras, kets in (((0, 1), (2, 3)), ((2, 3), (0, 1))):
        targets = {C.triality(cl.words[i]) for i in bras}
        allow = [C.reachable(targets, cl.words, k) for k in range(4)]
        for j in kets:
            v = {(cl.words[j], frozenset()): F(1)}
            for k in (3, 2, 1):
                v = G(filt(V_sides(v), allow[k]))
            v = filt(V_sides(v), allow[0])
            final = defaultdict(F)
            for (w, used), c in v.items():
                assert len(used) == 4
                final[w] += c
            for i in bras:
                D[(i, j)] = element(cl, i, dict(final))
    assert all(D[(i, j)] == D[(j, i)] for (i, j) in D), "cube term not symmetric"
    W = {(i, j): D[(i, j)] for i in (0, 1) for j in (2, 3)}
    log(f"    cube completion through {others}: C-odd {codd(W)}  C-even {ceven(W)}  ({time.time() - t0:.0f}s)")
    return W


def codd(W):
    return (W[(0, 2)] - W[(0, 3)] - W[(1, 2)] + W[(1, 3)]) / 2


def ceven(W):
    return (W[(0, 2)] + W[(0, 3)] + W[(1, 2)] + W[(1, 3)]) / 2


NU_RECORD = F(-1050558388351, 10081900483200)  # (0,1)->(0,1) at (0,0,1), the normal orbit nu

PAIRS = {
    # link-disjoint, joined by the four side faces of one cube: both kernels
    # agree here (A = 5/48 forces nu), so it validates the method, cube term
    # included, on an undisputed record
    "normal": ([((0, 1), (0, 0, 0)), ((0, 1), (0, 0, 1))], NU_RECORD, "(0,1)->(0,1) at (0,0,1), the normal orbit nu"),
    "coplanar": ([((0, 1), (0, 0, 0)), ((0, 1), (1, 0, 0))], PI_RECORD, "(0,1)->(0,1) at (1,0,0), the in-plane orbit pi"),
    # The corpus orients its plane basis as (0,1), (1,2), (2,0): x^y, y^z, z^x.
    # A (0,2) plaquette traversed x-then-z is the conjugate of the corpus's
    # (0,2) record plane, which flips the sign of every C-odd element; the
    # zigzag chain of the replication run shows it (-u against the record's
    # +u for (0,2)->(1,2) at (1,0,-1)).  So the perpendicular pair is built
    # with the (2,0) traversal, and its C-odd element compares to the record
    # directly.
    "perpendicular": ([((0, 1), (0, 0, 0)), ((2, 0), (0, 0, 0))], RHO_RECORD, "(0,1)->(0,2) at (0,0,0), the rotation orbit rho"),
}


def main(argv):
    which = argv[1] if len(argv) > 1 else "coplanar"
    stage = argv[2] if len(argv) > 2 else "all"
    faces2, record, label = PAIRS[which]
    log = print
    t_all = time.time()
    out = {"pair": which, "faces": faces2, "record_label": label, "record": str(record)}
    if stage in ("gate", "all"):
        far = ((0, 1), (5, 5, 5))
        log(f"== linked-cluster gate: X = {far}, link-disjoint from P and Q")
        W = three_cluster_cumulant(faces2, far, log)
        out["gate_far_X"] = {str(k): str(v) for k, v in W.items()}
        assert all(v == 0 for v in W.values()), f"far X cumulant is not zero: {W}"
        log("   gate passed: every element exactly 0")
    if stage in ("dressing", "all"):
        xs = neighbours(faces2)
        log(f"== {len(xs)} plaquettes share a link with P or Q")
        total = defaultdict(F)
        out["dressings"] = {}
        for x in xs:
            W = three_cluster_cumulant(faces2, x, log)
            out["dressings"][str(x)] = {"codd": str(codd(W)), "ceven": str(ceven(W)), "W": {str(k): str(v) for k, v in W.items()}}
            for k, v in W.items():
                total[k] += v
        out["dressing_sum_codd"] = str(codd(total))
        log(f"   dressing sum: C-odd {codd(total)}  C-even {ceven(total)}")
    if stage in ("cube", "all"):
        cubes = cubes_containing(faces2)
        log(f"== {len(cubes)} cube(s) contain both faces")
        out["cubes"] = []
        total = F(0)
        for others in cubes:
            W = cube_completion(faces2, others, log)
            out["cubes"].append({"other_faces": others, "codd": str(codd(W)), "ceven": str(ceven(W)), "W": {str(k): str(v) for k, v in W.items()}})
            total += codd(W)
        out["cube_sum_codd"] = str(total)
        log(f"   cube-completion sum, C-odd: {total}")
    if stage in ("pair", "all"):
        log("== the pair cluster itself, full assembly")
        H4, moments = pair_h4(faces2, log)
        Wp = {k: v for k, v in H4.items() if k[0] in (0, 1)}
        out["pair_cluster"] = {"codd": str(codd(Wp)), "ceven": str(ceven(Wp)), "W": {str(k): str(v) for k, v in Wp.items()}}
        log(f"   pair cluster: C-odd {codd(Wp)}  C-even {ceven(Wp)}")
        if "dressing_sum_codd" in out:
            lattice = codd(Wp) + F(out["dressing_sum_codd"])
            out["lattice_codd"] = str(lattice)
            log(f"== lattice fourth-order nearest-neighbour element, C-odd: {lattice} = {float(lattice):.9e}")
            log(f"   record {label}: {record} = {float(record):.9e};  ratio {float(lattice / record):.9f}")
    out["seconds"] = round(time.time() - t_all, 1)
    suffix = "_epsblind" if EPS_BLIND else ""
    with open(HERE / f"pair_route_{which}_{stage}{suffix}.json", "w") as fh:
        json.dump(out, fh, indent=1)
    log(f"total {time.time() - t_all:.0f}s")


if __name__ == "__main__":
    main(sys.argv)
