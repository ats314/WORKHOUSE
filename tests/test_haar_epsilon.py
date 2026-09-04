"""The epsilon-network Haar integrator agrees with the pinned engine, exactly.

Three kinds of pin: closed forms a reader can check by hand (one baryon
singlet, the six-antifundamental count), fast engine cases across every
family the module handles, and two pure-six integrals of the shared-link
pair's baryonic history that the engine took 400 s each to produce and this
module does in a hundredth of a second. The failure this prevents: a
transcription slip in a projector that changes a fourth-order amplitude while
every cheap family still agrees.
"""

from __future__ import annotations

from fractions import Fraction as F

import pytest

from workhouse import haar_epsilon as H

M = H.M


def _plaquette(links, conj=False):
    steps = [(links[0], 1), (links[1], 1), (links[2], -1), (links[3], -1)]
    if conj:
        steps = [(lk, -d) for lk, d in reversed(steps)]
    return M.trace_state(steps)


def _prod(*words):
    out = words[0]
    for w in words[1:]:
        out = M.tensor_product(out, w)
    return out


P = _plaquette((0, 1, 2, 3))
Pb = _plaquette((0, 1, 2, 3), conj=True)
Q = _plaquette((1, 4, 5, 6))  # shares link 1 with P
Qb = _plaquette((1, 4, 5, 6), conj=True)
ONE = M.EMPTY_STATE


@pytest.mark.parametrize(
    "name, bra, ket, value",
    [
        ("<P|Pbar Pbar>: the baryon vertex", P, _prod(Pb, Pb), F(1)),
        ("<P P|Pbar>", _prod(P, P), Pb, F(1)),
        ("<P P P|1>: det U = 1", _prod(P, P, P), ONE, F(1)),
        ("<P|P>", P, P, F(1)),
        ("<P Q|Pbar Pbar Qbar Qbar>", _prod(P, Q), _prod(Pb, Pb, Qb, Qb), F(1)),
    ],
)
def test_closed_forms(name, bra, ket, value):
    assert H.haar_inner(bra, ket) == value, name


@pytest.mark.parametrize(
    "bra, ket",
    [
        (P, _prod(Pb, Pb)),
        (_prod(P, P), Pb),
        (_prod(P, P, P), ONE),
        (_prod(P, P, P, P), Pb),
        (P, _prod(Pb, Pb, Q, Qb)),
        (_prod(P, P), _prod(Pb, Q, Qb)),
        (_prod(P, Q), _prod(Q, Q)),
        (_prod(P, Qb), _prod(P, Qb)),
    ],
)
def test_agrees_with_the_engine_where_the_engine_is_fast(bra, ket):
    assert H.haar_inner(bra, ket) == M.haar_inner(bra, ket)


# Two words of the coplanar pair's baryonic sector {Q, Q, Pbar, Pbar} against
# the bra P, with the pure-six family on the shared link and four determinant
# links. The engine's values (400 s each, 2026-09-02) are pinned as data.
_BRA = M.State(
    ((0, True), (1, True), (2, False), (3, False)),
    (0, 1, 1, 2, 3, 2, 0, 3),
)
_OCC = (
    (4, True), (5, True), (6, False), (1, False),
    (4, True), (5, True), (6, False), (1, False),
    (4, True), (5, True), (6, False), (1, False),
    (3, True), (2, True), (1, False), (0, False),
    (3, True), (2, True), (1, False), (0, False),
)  # fmt: skip
_REFERENCE = [
    (
        (0, 1, 1, 2, 3, 2, 0, 3, 4, 5, 5, 6, 7, 6, 4, 7, 8, 9, 9, 10, 11, 10, 8, 11,
         12, 13, 13, 14, 15, 14, 12, 15, 16, 17, 17, 18, 19, 18, 16, 19),
        F(1),
    ),
    (
        (0, 1, 1, 2, 3, 2, 4, 3, 4, 5, 5, 6, 7, 6, 0, 7, 8, 9, 9, 10, 11, 10, 8, 11,
         12, 13, 13, 14, 15, 14, 12, 15, 16, 17, 17, 18, 19, 18, 16, 19),
        F(-1),
    ),
]  # fmt: skip


@pytest.mark.parametrize("part, value", _REFERENCE)
def test_pure_six_references_from_the_engine(part, value):
    word = M.State(_OCC, part)
    assert H.haar_inner(_BRA, word) == value


def test_triality_skip_is_exact_orthogonality():
    assert H.triality(P) != H.triality(Pb)
    assert H.haar_inner(P, Pb) == 0
    assert H.inner(P, {Pb: F(5), _prod(Pb, Pb): F(2)}) == F(2)
