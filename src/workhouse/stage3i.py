"""The historical pipeline's own word ledger, decoded, reassembled and read by cluster.

The June-2026 Y4 pipeline built the 189-record fourth-order kernel (Stage 3J)
from a Stage-3I ledger of 4,221 ordered insertion words, each carrying its
complete des Cloizeaux fourth-order weight. The kernel copies name that
ledger by hash in their ``meta`` blocks; the ledger itself is pinned in the
corpus as ``DATA_Y4_stagei_authority_fixture.xz.b85`` (manifest row A41F),
consumed by the pinned production engine and, until 2026-09-04, read by
nothing in this repository. ADR 0021 and the G3 route said this repository
did not hold the historical pipeline's face-resolved ledger. It does.

This module decodes it (base85 -> xz -> gzip -> JSON, hash-checked against
the kernel's own ``stage3i_input``), ports Stage 3J's rooted-stabilizer
assembly verbatim so the 189 records are reproduced from the words, and then
does what Stage 3J never did: groups each word's rooted images by the set of
plaquettes they touch. The sum over words with support exactly S is the
connected cumulant of the cluster S, directly comparable with the cluster
expansion of runs/g3_shared_link_pair_2026-09-02 and with workhouse.loopcalc.
Nothing here evaluates a Haar integral; it only re-adds the pipeline's own
numbers in a different order.
"""

from __future__ import annotations

import base64
import gzip
import hashlib
import itertools
import json
import lzma
from collections import defaultdict
from fractions import Fraction
from functools import cache
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
FIXTURE = (
    ROOT_DIR / "corpus-import" / "numerics" / "data" / "DATA_Y4_stagei_authority_fixture.xz.b85"
)
#: sha256 of the gzip payload -- the ``stage3i_input`` hash the kernel copies quote.
STAGE3I_SHA = "854a02e981098de7fcfd1a14dd5c9703aff0c36a2a81ea5589ddf4ff8c321bd0"

Plaquette = tuple  # (x, y, z, first_axis, second_axis), axes sorted
ROOT: Plaquette = (0, 0, 0, 0, 1)


@cache
def load_words() -> tuple:
    """The 4,221 ordered words, after checking the decoded gzip's hash."""
    raw = FIXTURE.read_bytes()
    xz = base64.b85decode(b"".join(raw.split()))
    gz = lzma.decompress(xz)
    digest = hashlib.sha256(gz).hexdigest()
    if digest != STAGE3I_SHA:
        raise ValueError(f"Stage-3I fixture hash {digest} != {STAGE3I_SHA}")
    payload = json.loads(gzip.decompress(gz))
    return tuple(payload["words"])


# ---- the cubic group and the rooted frame, as Stage 3J wrote them
def _parity(perm) -> int:
    inversions = sum(perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3))
    return -1 if inversions % 2 else 1


ROTATIONS = [
    (perm, signs)
    for perm in itertools.permutations(range(3))
    for signs in itertools.product((-1, 1), repeat=3)
    if _parity(perm) * signs[0] * signs[1] * signs[2] == 1
]


def _transform_vec(v, rotation):
    perm, signs = rotation
    out = [0, 0, 0]
    for axis in range(3):
        out[perm[axis]] += signs[axis] * v[axis]
    return tuple(out)


def transform_plaquette(pl: Plaquette, index: int) -> Plaquette:
    perm, signs = ROTATIONS[index]
    first, second = pl[3], pl[4]
    mf, ms = perm[first], perm[second]
    anchor = list(_transform_vec(pl[:3], (perm, signs)))
    if signs[first] < 0:
        anchor[mf] -= 1
    if signs[second] < 0:
        anchor[ms] -= 1
    mf, ms = sorted((mf, ms))
    return (anchor[0], anchor[1], anchor[2], mf, ms)


def orientation_sign(pl: Plaquette, index: int) -> int:
    perm, signs = ROTATIONS[index]
    first, second = pl[3], pl[4]
    reorder = -1 if perm[first] > perm[second] else 1
    return signs[first] * signs[second] * reorder


ROOT_STABILIZER = [i for i in range(24) if transform_plaquette(ROOT, i)[3:] == (0, 1)]
ROOT_SHIFTS = {i: transform_plaquette(ROOT, i)[:3] for i in ROOT_STABILIZER}


def rooted_transform(pl: Plaquette, index: int) -> Plaquette:
    t = transform_plaquette(pl, index)
    sh = ROOT_SHIFTS[index]
    return (t[0] - sh[0], t[1] - sh[1], t[2] - sh[2], t[3], t[4])


def _word_images(word: dict, sector: str):
    """Stage 3J's image set of one word under the root stabilizer, with signs."""
    amplitude = Fraction(word[f"canonical_complete_sum_{sector}"])
    if amplitude == 0:
        return amplitude, {}
    insertions = tuple(tuple(int(x) for x in row) for row in word["ordered_insertions"])
    output = tuple(int(x) for x in word["output"])
    images = {}
    for rotation in ROOT_STABILIZER:
        image = (
            tuple(rooted_transform(p, rotation) for p in insertions),
            rooted_transform(output, rotation),
        )
        sign = (
            orientation_sign(ROOT, rotation) * orientation_sign(output, rotation)
            if sector == "odd"
            else 1
        )
        if image in images and images[image] != sign:
            raise ValueError("inconsistent orientation sign on a repeated image")
        images[image] = sign
    return amplitude, images


def build_root_kernel(words, sector: str = "odd") -> dict:
    """Stage 3J's rooted kernel: output plaquette -> amplitude, root xy at the origin."""
    root = defaultdict(Fraction)
    for word in words:
        amplitude, images = _word_images(word, sector)
        for (_ins, out), sign in images.items():
            root[out] += sign * amplitude
    return {pl: v for pl, v in root.items() if v}


def build_full_kernel(root: dict) -> dict:
    """Stage 3J's full kernel: (input plane, output plane, displacement) -> weight."""
    candidates = defaultdict(set)
    for output, amplitude in root.items():
        for rotation in range(24):
            tin = transform_plaquette(ROOT, rotation)
            tout = transform_plaquette(output, rotation)
            displacement = tuple(tout[i] - tin[i] for i in range(3))
            sign = orientation_sign(ROOT, rotation) * orientation_sign(output, rotation)
            candidates[(tin[3:], tout[3:], displacement)].add(sign * amplitude)
    if any(len(v) != 1 for v in candidates.values()):
        raise ValueError("a kernel key received two different amplitudes")
    kernel = {k: next(iter(v)) for k, v in candidates.items() if next(iter(v))}
    for (ip, op, d), value in kernel.items():
        if kernel.get((op, ip, tuple(-x for x in d)), Fraction(0)) != value:
            raise ValueError("kernel is not Hermitian")
    return kernel


# ---- the cluster ledger
def _links(pl: Plaquette) -> set:
    x, y, z, a, b = pl
    out = set()
    for d1, d2 in ((a, b), (b, a)):
        for off in (0, 1):
            s = [x, y, z]
            s[d2] += off
            out.add((tuple(s), d1))
    return out


def classify(support) -> str:
    """The cluster type of a support set, by pairwise shared links."""
    faces = sorted(support)
    n = len(faces)
    ls = [_links(f) for f in faces]
    shared = sum(1 for i in range(n) for j in range(i + 1, n) if ls[i] & ls[j])
    if n == 1:
        return "one-plaquette"
    if n == 2:
        return "pair(shared link)" if shared == 1 else "pair(disjoint)"
    if n == 3 and shared == 3:
        common = set.intersection(*ls)
        return "fan(three on one link)" if common else "corner(three faces at a vertex)"
    if n == 3 and shared == 2:
        return "chain3(two shared links)"
    if n == 3 and shared == 1:
        return "pair+single-contact"
    if n == 6 and shared == 12:
        return "cube(six faces once each)"
    return f"other(n={n},shared={shared})"


@cache
def support_ledger(sector: str = "odd") -> dict:
    """output plaquette -> {support frozenset -> summed amplitude}, in the rooted frame."""
    by = defaultdict(lambda: defaultdict(Fraction))
    for word in load_words():
        amplitude, images = _word_images(word, sector)
        for (ins, out), sign in images.items():
            by[out][frozenset(set(ins) | {ROOT, out})] += sign * amplitude
    return {out: {s: v for s, v in d.items() if v} for out, d in by.items()}


def cluster_classes(output: Plaquette, sector: str = "odd") -> dict:
    """The historical record's connected cumulants by cluster class."""
    out = defaultdict(lambda: {"sum": Fraction(0), "supports": 0, "values": []})
    for support, value in support_ledger(sector).get(output, {}).items():
        c = classify(support)
        out[c]["sum"] += value
        out[c]["supports"] += 1
        out[c]["values"].append(value)
    return dict(out)


def dressing_by_face(output: Plaquette, sector: str = "odd") -> dict:
    """third plaquette X -> the three-cluster cumulant W(ROOT, output, X) - W(ROOT, output)."""
    out = {}
    for support, value in support_ledger(sector).get(output, {}).items():
        others = sorted(set(support) - {ROOT, output})
        if len(others) == 1:
            out[others[0]] = value
    return out


def cube_words(output: Plaquette):
    """The ordered words whose rooted images give the six-face cluster at `output`."""
    found = []
    for word in load_words():
        amplitude, images = _word_images(word, "odd")
        for (ins, out), sign in images.items():
            if out == output and len(set(ins) | {ROOT, out}) == 6 and len(set(ins)) == 4:
                found.append((word["ordered_id"], ins, sign * amplitude))
    return found


#: The rotation record's output in the rooted frame: the (0,2) face at the origin.
ROTATION_OUTPUT: Plaquette = (0, 0, 0, 0, 2)
IN_PLANE_OUTPUT: Plaquette = (1, 0, 0, 0, 1)
NORMAL_OUTPUT: Plaquette = (0, 0, 1, 0, 1)
