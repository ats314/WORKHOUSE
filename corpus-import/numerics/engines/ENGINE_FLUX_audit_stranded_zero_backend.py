#!/usr/bin/env python3
"""
Cold audit of the claimed "stranded-flux" zero for the 20 fixed-side
pentagonal-prism O(u^4) histories.

This script deliberately does NOT evaluate the electric resolvents.  It tests
the logically prior claim made by the submitted backend: that every history has
zero SU(3) endpoint Haar contraction because some link is unbalanced.

Checks:
  1. Reconstruct the same 20 cap-P-irreducible words.
  2. Reconstruct the submitted backend's per-link U/U^dagger counts.
  3. Show that every rejection is caused by two balanced (2,2) links, not by an
     unbalanced or "stranded" link.
  4. Evaluate the exact SU(3) p=2 Weingarten tensor and exhibit a nonzero
     component, integral |U_11|^4 = 1/6.
  5. Contract the complete six-trace bare Haar network for every one of the 20
     words.  Each exact endpoint contraction is 1, not 0.

Evidence boundary:
  A nonzero bare Haar contraction disproves the claimed topological/Haar zero.
  It does not by itself determine the representation-resolved H0 resolvent
  coefficient h4_side; that remains a separate calculation.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path
from typing import Iterable, Sequence

N = 3
OUT_JSON = Path('/mnt/data/AUDIT_FLUX_stranded_zero_backend_results.json')
OUT_TXT = Path('/mnt/data/audit_stranded_flux_zero_backend_results.txt')

# Same reduced three-face boundary data as the submitted backend.
B_COLS: list[tuple[int, ...]] = [
    (1, 1, 1, 1, 1,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0,  1, 1, 1, 1, 1,  0, 0, 0, 0, 0),
    (1, 0, 0, 0, 0, -1, 0, 0, 0, 0,  1, -1, 0, 0, 0),
]
START = B_COLS[0]
CAP1 = B_COLS[1]
SIGNED_FACES = [(f, s) for f in range(3) for s in (-1, 1)]


def add(a: tuple[int, ...], b: tuple[int, ...], s: int = 1) -> tuple[int, ...]:
    return tuple(x + s * y for x, y in zip(a, b))


def mod3_equal(a: tuple[int, ...], b: tuple[int, ...]) -> bool:
    return all((x - y) % 3 == 0 for x, y in zip(a, b))


def retained_cap_p(q: tuple[int, ...]) -> bool:
    if all(x % 3 == 0 for x in q):
        return True
    return any(
        mod3_equal(q, tuple(s * x for x in B_COLS[f]))
        for f in (0, 1)
        for s in (-1, 1)
    )


def histories_20() -> list[tuple[tuple[int, int], ...]]:
    out: list[tuple[tuple[int, int], ...]] = []
    for word in itertools.product(SIGNED_FACES, repeat=4):
        if {f for f, _ in word if f == 2} != {2}:
            continue
        q = START
        prefixes = []
        for f, s in word:
            q = add(q, B_COLS[f], s)
            prefixes.append(q)
        if not (mod3_equal(q, CAP1) or mod3_equal(q, tuple(-x for x in CAP1))):
            continue
        if any(retained_cap_p(p) for p in prefixes[:-1]):
            continue
        out.append(tuple(word))
    return out


def endpoint_and_counts(word: Sequence[tuple[int, int]]) -> tuple[int, list[tuple[int, int]]]:
    """Return endpoint sign and total U/Udag counts including ket and bra."""
    counts = [[0, 0] for _ in range(15)]
    for i, x in enumerate(START):
        if x == 1:
            counts[i][0] += 1
        elif x == -1:
            counts[i][1] += 1

    q = START
    for f, s in word:
        q = add(q, B_COLS[f], s)
        for i, x in enumerate(B_COLS[f]):
            y = s * x
            if y == 1:
                counts[i][0] += 1
            elif y == -1:
                counts[i][1] += 1

    if q == CAP1:
        endpoint_sign = +1
        for i, x in enumerate(CAP1):
            if x == 1:
                counts[i][1] += 1  # positive cap bra is conjugate
    elif q == tuple(-x for x in CAP1):
        endpoint_sign = -1
        for i, x in enumerate(CAP1):
            if x == 1:
                counts[i][0] += 1  # negative cap bra is fundamental
    else:
        raise AssertionError(f'endpoint is not exactly +/-cap1: {q}')

    return endpoint_sign, [tuple(x) for x in counts]


# ---------------------------------------------------------------------------
# Exact p=1,2 unitary/SU(3) Haar projectors.
# Balanced p=2 SU(3) equals U(3) because p-q=0.
# ---------------------------------------------------------------------------


def wg2(same_permutation: bool, n: int = N) -> Fraction:
    if same_permutation:
        return Fraction(1, n * n - 1)
    return Fraction(-1, n * (n * n - 1))


def u11_fourth_moment(n: int = N) -> Fraction:
    # Four p=2 Weingarten terms with all Kronecker deltas equal to one.
    return 2 * wg2(True, n) + 2 * wg2(False, n)


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[rb] = ra

    def classes(self) -> int:
        return len({self.find(i) for i in range(len(self.parent))})


# Explicit cyclic order of the three oriented face traces.
# side0: b0 -> v1 -> t0^{-1} -> v0^{-1}.
FACE_CYCLES: dict[int, list[tuple[str, int]]] = {
    0: [('b0', +1), ('b1', +1), ('b2', +1), ('b3', +1), ('b4', +1)],
    1: [('t0', +1), ('t1', +1), ('t2', +1), ('t3', +1), ('t4', +1)],
    2: [('b0', +1), ('v1', +1), ('t0', -1), ('v0', -1)],
}


def oriented_cycle(face: int, sign: int) -> list[tuple[str, int]]:
    cycle = FACE_CYCLES[face]
    if sign == +1:
        return list(cycle)
    return [(link, -orient) for link, orient in reversed(cycle)]


def exact_bare_haar(trace_specs: Sequence[tuple[int, int]], n: int = N) -> Fraction:
    """Exact contraction of a closed product of traces with p<=2 on each link."""
    total_vars = sum(len(oriented_cycle(f, s)) for f, s in trace_specs)
    occurrences: dict[str, dict[str, list[tuple[int, int]]]] = {}

    base = 0
    for face, sign in trace_specs:
        cycle = oriented_cycle(face, sign)
        m = len(cycle)
        vars_for_trace = list(range(base, base + m))
        base += m
        for j, (link, orient) in enumerate(cycle):
            left = vars_for_trace[j]
            right = vars_for_trace[(j + 1) % m]
            bucket = occurrences.setdefault(link, {'U': [], 'D': []})
            if orient == +1:
                bucket['U'].append((left, right))
            else:
                # U^dag_{left,right} = conjugate(U_{right,left}).
                bucket['D'].append((right, left))

    link_terms: list[list[tuple[Fraction, list[tuple[int, int]]]]] = []
    for link, bucket in sorted(occurrences.items()):
        u = bucket['U']
        d = bucket['D']
        if len(u) != len(d):
            return Fraction(0)
        p = len(u)
        if p == 1:
            link_terms.append([
                (Fraction(1, n), [(u[0][0], d[0][0]), (u[0][1], d[0][1])])
            ])
        elif p == 2:
            terms = []
            perms = ((0, 1), (1, 0))
            for sigma in perms:
                for tau in perms:
                    coeff = wg2(sigma == tau, n)
                    pairs: list[tuple[int, int]] = []
                    for a in range(2):
                        pairs.append((u[a][0], d[sigma[a]][0]))
                        pairs.append((u[a][1], d[tau[a]][1]))
                    terms.append((coeff, pairs))
            link_terms.append(terms)
        else:
            raise AssertionError(f'unsupported link multiplicity p={p} on {link}')

    answer = Fraction(0)
    for choices in itertools.product(*link_terms):
        uf = UnionFind(total_vars)
        coeff = Fraction(1)
        for local_coeff, identifications in choices:
            coeff *= local_coeff
            for a, b in identifications:
                uf.union(a, b)
        answer += coeff * (n ** uf.classes())
    return answer


def traces_for_history(word: Sequence[tuple[int, int]], endpoint_sign: int) -> list[tuple[int, int]]:
    # Matrix element: conjugate(final) * operators * initial.
    final_bra = (1, -1) if endpoint_sign == +1 else (1, +1)
    return [(0, +1), *word, final_bra]


def main() -> int:
    words = histories_20()
    assert len(words) == 20, len(words)

    multisets = Counter(tuple(sorted(w)) for w in words)
    count_patterns = Counter()
    rejected_links = Counter()
    bare_values = []
    rows = []

    for word in words:
        endpoint_sign, counts = endpoint_and_counts(word)
        pattern = Counter(counts)
        count_patterns[tuple(sorted(pattern.items()))] += 1
        user_rejected = [i for i, c in enumerate(counts) if c not in ((0, 0), (1, 1), (3, 0), (0, 3))]
        for i in user_rejected:
            rejected_links[counts[i]] += 1

        bare = exact_bare_haar(traces_for_history(word, endpoint_sign))
        bare_values.append(bare)
        rows.append({
            'word': [[f, s] for f, s in word],
            'endpoint': '+cap1' if endpoint_sign > 0 else '-cap1',
            'nonempty_link_counts': {str(i): list(c) for i, c in enumerate(counts) if c != (0, 0)},
            'backend_rejected_links': user_rejected,
            'exact_bare_haar': str(bare),
        })

    all_two_22 = all(
        sum(1 for c in endpoint_and_counts(w)[1] if c == (2, 2)) == 2
        and all(c[0] == c[1] for c in endpoint_and_counts(w)[1])
        for w in words
    )
    all_bare_one = all(v == 1 for v in bare_values)

    checks = [
        ('history count is 20', len(words) == 20, len(words)),
        ('two expected temporal multisets, 10 each', sorted(multisets.values()) == [10, 10], dict(multisets)),
        ('every history is exactly endpoint-balanced', all(endpoint_and_counts(w)[0] in (-1, +1) for w in words), ''),
        ('every backend rejection is exactly two balanced (2,2) links', all_two_22, dict(rejected_links)),
        ('SU(3) p=2 coefficient Wg(e)=1/8', wg2(True) == Fraction(1, 8), wg2(True)),
        ('SU(3) p=2 coefficient Wg((12))=-1/24', wg2(False) == Fraction(-1, 24), wg2(False)),
        ('explicit balanced component integral |U_11|^4=1/6', u11_fourth_moment() == Fraction(1, 6), u11_fourth_moment()),
        ('all 20 complete bare endpoint Haar contractions equal 1', all_bare_one, Counter(map(str, bare_values))),
    ]

    passed = sum(ok for _, ok, _ in checks)
    result = {
        'schema': 'pentagonal-o4-stranded-flux-zero-audit-v1',
        'passed': passed,
        'total': len(checks),
        'all_pass': passed == len(checks),
        'verdict': 'ZERO_BACKEND_FALSIFIED' if passed == len(checks) else 'AUDIT_FAILURE',
        'history_multisets': {str(k): v for k, v in multisets.items()},
        'weingarten_SU3': {'identity': str(wg2(True)), 'transposition': str(wg2(False))},
        'u11_fourth_moment': str(u11_fourth_moment()),
        'bare_haar_values': dict(Counter(map(str, bare_values))),
        'checks': [{'name': n, 'passed': ok, 'detail': str(d)} for n, ok, d in checks],
        'histories': rows,
        'evidence_boundary': (
            'This falsifies the asserted stranded-flux/Haar-zero mechanism. '
            'It does not compute the representation-resolved electric resolvents or h4_side.'
        ),
    }
    OUT_JSON.write_text(json.dumps(result, indent=2), encoding='utf-8')

    lines = [
        'PENTAGONAL O(4) STRANDED-FLUX ZERO AUDIT',
        '=' * 72,
    ]
    for name, ok, detail in checks:
        lines.append(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}")
    lines += [
        '',
        f'RESULT: {passed}/{len(checks)} checks pass',
        f"VERDICT: {result['verdict']}",
        '',
        'Decisive witness:',
        '  Every submitted history has two links with (n_U,n_Udag)=(2,2).',
        '  The submitted backend returns zero for this balanced sector.',
        '  Exact SU(3) Haar gives Wg(e)=1/8, Wg((12))=-1/24,',
        '  and integral |U_11|^4 = 1/6 != 0.',
        '  Exact contraction of each complete six-trace endpoint network = 1.',
        '',
        result['evidence_boundary'],
    ]
    OUT_TXT.write_text('\n'.join(lines) + '\n', encoding='utf-8')

    source_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    print('\n'.join(lines))
    print('JSON:', OUT_JSON)
    print('TEXT:', OUT_TXT)
    print('SOURCE_SHA256:', source_hash)
    return 0 if passed == len(checks) else 1


if __name__ == '__main__':
    raise SystemExit(main())
