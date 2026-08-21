#!/usr/bin/env python3
"""Bounded full-T1 SU(3) O(u^4) physical-state occurrence preflight.

Scope is deliberately narrow.  The program constructs only

    P0 -> W1 -> R1 -> W2 -> R2
                    `-> R12

independently for each of the three origin T1 plaquettes on the L=5 periodic
cubic lattice.  Each root has exactly two magnetic applications: P0->W1 and
R1->W2.  For every required moment it keeps each ket root anchored, scans all
125 translations of every physical bra block, and covers all nine ordered
bra/ket polarization pairs.  Every local occurrence reaching a Haar path is
inspected before that contractor.  The program stops at this census boundary.

The trace-network, exact H0 projector, extended SU(3) Haar, reduced-resolvent,
and support-labelled half-history functions below are copied or guard-wrapped
without changing their mathematical action from the accepted
v10a24c source (SHA-256 935A3A5BA680D1373A5842486B10231D83232D8CB3393BBC250351BC51A68C8B),
with source line locators recorded in SOURCE_LOCATORS.  New code is limited to
the fail-closed order guard, provenance capture, deterministic census, gates,
and command-line wrapper.

This is a preflight, not a coefficient or matrix evaluator.  It is safe to run
in ordinary Python or in Colab; no accelerator-specific package is required.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import itertools
import json
import math
import os
import platform
import sys
import time
import traceback
from datetime import datetime, timezone
from collections import Counter, defaultdict
from contextlib import contextmanager
from dataclasses import asdict, dataclass
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping, Sequence


DEFAULT_JSON_NAME = "CERT_O4_hodge_fullt1_occurrence_preflight.json"


def _bootstrap_json_path(argv: Sequence[str]) -> Path:
    for index, token in enumerate(argv):
        if token == "--json-out" and index + 1 < len(argv):
            return Path(argv[index + 1]).resolve()
        if token.startswith("--json-out="):
            return Path(token.split("=", 1)[1]).resolve()
    return Path(DEFAULT_JSON_NAME).resolve()


def _bootstrap_atomic_write(path: Path, payload: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    text = json.dumps(payload, indent=2, sort_keys=True, allow_nan=False)
    temporary.write_text(text + "\n", encoding="utf-8")
    os.replace(temporary, path)


_BOOTSTRAP_PATH: Path | None = None
_ORIGINAL_EXCEPTHOOK = sys.excepthook
if __name__ == "__main__":
    _BOOTSTRAP_PATH = _bootstrap_json_path(sys.argv[1:])
    _bootstrap = {
        "schema": "hodge-preflight-envelope/v1",
        "status": "RUNNING",
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "script": str(Path(__file__).resolve()),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest().upper(),
    }
    _bootstrap_atomic_write(_BOOTSTRAP_PATH, _bootstrap)

    def _bootstrap_failure_hook(exc_type, exc, tb):
        try:
            _bootstrap_atomic_write(_BOOTSTRAP_PATH, {
                **_bootstrap,
                "status": "FAIL",
                "failed_utc": datetime.now(timezone.utc).isoformat(),
                "error_type": exc_type.__name__,
                "error": str(exc),
            })
        finally:
            _ORIGINAL_EXCEPTHOOK(exc_type, exc, tb)
    sys.excepthook = _bootstrap_failure_hook

try:
    import numpy as np
    import opt_einsum as oe
    import sympy as sp
    from scipy.linalg import qr
except ImportError as exc:  # Colab normally supplies these packages.
    if _BOOTSTRAP_PATH is not None:
        _bootstrap_atomic_write(_BOOTSTRAP_PATH, {
            **_bootstrap,
            "status": "FAIL",
            "failed_utc": datetime.now(timezone.utc).isoformat(),
            "error_type": type(exc).__name__,
            "error": str(exc),
        })
    raise SystemExit(
        "Missing numerical dependency. Install numpy scipy sympy opt_einsum, "
        f"then rerun. Original error: {exc}"
    ) from exc


SCHEMA = "hodge-o4-full-t1-occurrence-preflight/v4"
REQUESTED_ORDER = 4
N = 3
L = 5
T1_POLS = ((1, 2), (0, 2), (0, 1))
TOL_COEFF = 2e-13
TOL_NORM = 2e-10
V10A3_COEFF_TOL = TOL_COEFF
V10A3_NORM_TOL = TOL_NORM
V10A7_PROGRESS = 1

DEFAULT_MAX_WALL_SECONDS = 6 * 60 * 60
DEFAULT_MAX_RSS_GIB = 48.0
DEFAULT_MAX_W_ACTIONS_PER_CALL = 100_000
DEFAULT_MAX_W_CHANNELS_PER_CALL = 1_000_000
DEFAULT_MAX_SUPPORTS_PER_STAGE = 1_000
DEFAULT_MAX_PAIR_TESTS_PER_UNIT = 5_000_000
DEFAULT_MAX_PAIR_TESTS_TOTAL = 50_000_000
DEFAULT_MAX_PAYLOAD_MIB = 64.0
HEARTBEAT_SECONDS = 15.0

ALLOWED_BLOCKS = ("PP", "P1", "1P", "11", "12", "21")
FORBIDDEN_BLOCKS = ("P2", "2P", "22")
BASELINE_CENTER_NEUTRAL = frozenset(
    {(0, 3), (0, 6), (1, 1), (1, 4), (2, 2), (3, 0), (3, 3), (4, 1), (6, 0)}
)
FORBIDDEN_OCCURRENCES = frozenset({(2, 5), (5, 2)})

EXECUTED_V10A2_REFERENCE = {
    "schema": "hodge-v10a2-executed-contractor-domain-reference/v2",
    "notebook_sha256": "026DA360679CC7B7BCAC161A1DEAAA9A9E52B5D52C3892F624FF6B3DE6D82CE4",
    "code_cell_sha256": "AA55F3317A116A645FA5DF680F1EA700CA5712F7B61533CE17C582FD580578F2",
    "stored_gate_summary": "17/17",
    "binding_purpose": "executed contractor-domain provenance only; no historical numerical target",
    "center_neutral_occurrences": [
        [0, 3], [0, 6], [1, 1], [1, 4], [2, 2],
        [3, 0], [3, 3], [4, 1], [6, 0],
    ],
}
EXECUTED_V10A2_REFERENCE_SHA256 = "8540E9B49AB463E0687195DC96023AFC010ED8042B77020F8CB4FD871F667337"

SOURCE_LOCATORS = {
    "authority": "sources/hodge_v10a24c_RootedFullT1_DualColdOracle_O4_A100(1).py",
    "authority_sha256": "935A3A5BA680D1373A5842486B10231D83232D8CB3393BBC250351BC51A68C8B",
    "graph_algebra": "321-521",
    "loop_geometry": "622-659",
    "joint_canonicalization": "1803-1817",
    "numerical_haar_tensors": "2672-2697,3462-3471",
    "exact_h0_projectors": "2791-2838",
    "flux_and_occurrence_keys": "3539-3548,3895-3901",
    "extended_haar": "4124-4214",
    "dynamic_irreps": "4382-4400",
    "physical_states_and_resolvent": "4546-4727",
    "periodic_state_translation": "4936-4967",
    "local_face_cache": "5123-5132",
    "support_half_history": "6309-6344",
    "canonical_schedule": "6405-6424",
    "moment_definitions": "6438-6447,6712-6720",
    "oneface_character_certificate": "3235-3253,5330-5358",
    "D_samepol_shortcut_crosspol_fallback": "5658-5774",
    "full_T1_generic_endpoint_scan": "6581-6667",
    "ordered_3x3_endpoint_dispatch": "6670-6684",
}


class PreflightFailure(RuntimeError):
    """Fail-closed root preflight error."""


class ScheduleViolation(PreflightFailure):
    """An operator request outside the order-four schedule."""


class OccurrenceViolation(ScheduleViolation):
    """A local occurrence outside the executed baseline corpus."""


@dataclass(frozen=True)
class LXState:
    occ: tuple
    part: tuple


REQUIRED_GATES = (
    "negative occurrence poison callback remains untouched",
    "negative schedule poison callback remains untouched",
    "contractor domain is bound to the executed v10a2 reference manifest",
    "all Haar diagnostics are finite",
    "balanced rank-three inverse certificate",
    "pure-six singlet rank certificate",
    "pure-six projector trace equals five",
    "pure-six projector is symmetric",
    "pure-six projector is idempotent",
    "all three full-T1 root histories are constructed",
    "each root history has exactly two sealed magnetic applications",
    "all magnetic transition statistics satisfy operational bounds",
    "all reduced resolvents are finite and free of retained-energy poles",
    "all 63 full-T1 census units are complete and substantive where required",
    "every left H0 block scans exactly 125 translations",
    "all ordered 3x3 polarization pairs are covered for every moment",
    "D same-polarization analytic and all cross-polarization generic routes are exact",
    "observed center-neutral occurrences are contained in the executed corpus",
    "forbidden seven-factor occurrences are absent",
    "all local occurrences have at most six factors",
    "checkpoint binding and unit completeness are exact",
    "policy: magnetic block ledger is Hermitian-closed",
    "policy: static prohibited-token scope scan is clear",
)


def ensure_finite(name: str, value: Any) -> Any:
    """Reject every non-finite numeric value, recursively."""
    if isinstance(value, Fraction):
        return value
    if isinstance(value, np.ndarray):
        if not bool(np.all(np.isfinite(value))):
            raise PreflightFailure(f"{name}: non-finite array")
        return value
    if isinstance(value, np.generic):
        value = value.item()
    if isinstance(value, float):
        if not math.isfinite(value):
            raise PreflightFailure(f"{name}: non-finite value {value!r}")
        return value
    if isinstance(value, Mapping):
        for key, item in value.items():
            ensure_finite(f"{name}.{key}", item)
    elif isinstance(value, (list, tuple, set, frozenset)):
        for index, item in enumerate(value):
            ensure_finite(f"{name}[{index}]", item)
    return value


@dataclass
class GateBook:
    passed: list[dict[str, Any]]

    def __init__(self) -> None:
        self.passed = []

    def require(self, name: str, condition: bool, detail: Any) -> None:
        ordinal = len(self.passed)
        if ordinal >= len(REQUIRED_GATES) or name != REQUIRED_GATES[ordinal]:
            expected = REQUIRED_GATES[ordinal] if ordinal < len(REQUIRED_GATES) else None
            raise PreflightFailure(f"gate manifest mismatch at {ordinal}: expected {expected!r}, got {name!r}")
        if any(row["name"] == name for row in self.passed):
            raise PreflightFailure(f"duplicate required gate: {name}")
        ensure_finite(f"gate.{name}.condition", condition)
        ensure_finite(f"gate.{name}.detail", detail)
        if not bool(condition):
            raise PreflightFailure(f"{name}: {detail}")
        self.passed.append({"name": name, "detail": json_safe(detail)})

    def finalize(self) -> None:
        names = tuple(row["name"] for row in self.passed)
        if names != REQUIRED_GATES or len(set(names)) != len(REQUIRED_GATES):
            raise PreflightFailure(f"required gate manifest incomplete: {names!r}")


def json_safe(value: Any) -> Any:
    ensure_finite("json", value)
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, LXState):
        return {"occ": [list(x) for x in value.occ], "part": list(value.part)}
    if isinstance(value, (set, frozenset, tuple)):
        return [json_safe(x) for x in value]
    if isinstance(value, list):
        return [json_safe(x) for x in value]
    if isinstance(value, Mapping):
        return {str(k): json_safe(v) for k, v in value.items()}
    if isinstance(value, np.generic):
        return json_safe(value.item())
    return value


def canonical_json(value: Any) -> str:
    return json.dumps(
        json_safe(value), sort_keys=True, separators=(",", ":"),
        ensure_ascii=True, allow_nan=False,
    )


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest().upper()


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def _portable_certificate_id(material: Mapping[str, Any]) -> str:
    """Hash a discrete structural projection, never raw checkpoint integrity data."""
    forbidden_checkpoint_keys = frozenset({
        "checkpoint_integrity", "chain_head_sha256", "file_sha256",
        "record_sha256", "previous_record_sha256",
    })

    def inspect(value: Any, path: str) -> None:
        if isinstance(value, np.generic):
            value = value.item()
        if isinstance(value, float):
            raise PreflightFailure(
                f"portable certificate identity contains a raw float at {path}"
            )
        if isinstance(value, Mapping):
            for key, item in value.items():
                key_text = str(key)
                if key_text in forbidden_checkpoint_keys:
                    raise PreflightFailure(
                        f"portable certificate identity contains external checkpoint "
                        f"integrity field {key_text!r} at {path}"
                    )
                inspect(item, f"{path}.{key_text}")
        elif isinstance(value, (list, tuple, set, frozenset)):
            for index, item in enumerate(value):
                inspect(item, f"{path}[{index}]")

    inspect(material, "certificate_identity_material")
    ensure_finite("certificate_identity_material", material)
    return sha256_text(canonical_json(material))


def process_rss_gib() -> float:
    failures = []
    try:
        import psutil
        value = float(psutil.Process(os.getpid()).memory_info().rss) / (1024.0 ** 3)
    except Exception as exc:
        failures.append(f"psutil:{type(exc).__name__}:{exc}")
        try:
            import resource
            raw = float(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            value = raw / (1024.0 ** 2) if sys.platform != "darwin" else raw / (1024.0 ** 3)
        except Exception as fallback_exc:
            failures.append(f"resource:{type(fallback_exc).__name__}:{fallback_exc}")
            raise PreflightFailure(
                "RAM ceiling cannot be enforced because RSS measurement failed: "
                + " | ".join(failures)
            ) from fallback_exc
    ensure_finite("rss_gib", value)
    return value


@dataclass(frozen=True)
class OperationalLimits:
    max_wall_seconds: int = DEFAULT_MAX_WALL_SECONDS
    max_rss_gib: float = DEFAULT_MAX_RSS_GIB
    max_w_actions_per_call: int = DEFAULT_MAX_W_ACTIONS_PER_CALL
    max_w_channels_per_call: int = DEFAULT_MAX_W_CHANNELS_PER_CALL
    max_supports_per_stage: int = DEFAULT_MAX_SUPPORTS_PER_STAGE
    max_pair_tests_per_unit: int = DEFAULT_MAX_PAIR_TESTS_PER_UNIT
    max_pair_tests_total: int = DEFAULT_MAX_PAIR_TESTS_TOTAL
    max_payload_bytes: int = int(DEFAULT_MAX_PAYLOAD_MIB * 1024 * 1024)


class ResourceBudget:
    def __init__(self, limits: OperationalLimits) -> None:
        ensure_finite("operational_limits", asdict(limits))
        self.limits = limits
        self.started = time.monotonic()
        self.last_heartbeat = self.started
        self.total_pair_tests = 0
        self.peak_rss_gib = process_rss_gib()

    def elapsed(self) -> float:
        value = time.monotonic() - self.started
        ensure_finite("elapsed_seconds", value)
        return value

    def check(self, label: str, *, current: int | None = None,
              total: int | None = None, pair_increment: int = 0,
              force_heartbeat: bool = False) -> None:
        elapsed = self.elapsed()
        rss = process_rss_gib()
        self.peak_rss_gib = max(self.peak_rss_gib, rss)
        ensure_finite("peak_rss_gib", self.peak_rss_gib)
        if elapsed > self.limits.max_wall_seconds:
            raise PreflightFailure(f"wall-clock ceiling exceeded in {label}: {elapsed:.1f}s")
        if rss > self.limits.max_rss_gib:
            raise PreflightFailure(f"RAM ceiling exceeded in {label}: {rss:.2f} GiB")
        if pair_increment:
            self.total_pair_tests += int(pair_increment)
            if self.total_pair_tests > self.limits.max_pair_tests_total:
                raise PreflightFailure(
                    f"total pair-test ceiling exceeded in {label}: {self.total_pair_tests}"
                )
        now = time.monotonic()
        if force_heartbeat or now - self.last_heartbeat >= HEARTBEAT_SECONDS:
            eta = None
            if current is not None and total is not None and current > 0:
                rate = current / max(elapsed, 1e-9)
                eta = (total-current)/rate if rate > 0 else None
            eta_text = "unknown" if eta is None else f"{eta:.1f}s"
            print(
                f"[heartbeat] {label}; elapsed={elapsed:.1f}s; RAM={rss:.2f} GiB; "
                f"progress={current}/{total}; ETA={eta_text}; pairs={self.total_pair_tests}",
                flush=True,
            )
            self.last_heartbeat = now

    def report(self) -> dict[str, Any]:
        return {
            "limits": asdict(self.limits),
            "elapsed_seconds": self.elapsed(),
            "peak_rss_gib": self.peak_rss_gib,
            "total_pair_tests": self.total_pair_tests,
        }


# ---------------------------------------------------------------------------
# Accepted cubic geometry.  Source lines 169-205.
# ---------------------------------------------------------------------------

def shift(v, d, step=1):
    w = list(v)
    w[d] = (w[d] + step) % L
    return tuple(w)


def build_cubic_complex():
    verts = [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]
    links = []
    lid = {}
    for v in verts:
        for d in range(3):
            lid[(v, d)] = len(links)
            links.append((v, d))
    faces = []
    for v in verts:
        for a, b in ((0, 1), (0, 2), (1, 2)):
            faces.append((v, a, b))
    B2 = np.zeros((len(links), len(faces)), dtype=np.int8)
    for f, (v, a, b) in enumerate(faces):
        va = shift(v, a)
        vb = shift(v, b)
        B2[lid[(v, a)], f] += 1
        B2[lid[(va, b)], f] += 1
        B2[lid[(vb, a)], f] -= 1
        B2[lid[(v, b)], f] -= 1
    return verts, links, faces, B2


verts, links, faces, B2 = build_cubic_complex()
E, P = B2.shape
link_faces = [[] for _ in range(E)]
for _face in range(P):
    for _link in np.flatnonzero(B2[:, _face]):
        link_faces[int(_link)].append(_face)


# ---------------------------------------------------------------------------
# Accepted trace-network graph algebra.  Source lines 321-521.
# ---------------------------------------------------------------------------

def lx_canon(labels):
    mp = {}
    out = []
    for x in labels:
        if x not in mp:
            mp[x] = len(mp)
        out.append(mp[x])
    return tuple(out)


def lx_trace_state(steps):
    m = len(steps)
    occ, labels = [], []
    for j, (link, d) in enumerate(steps):
        a, b = j, (j + 1) % m
        if int(d) > 0:
            occ.append((int(link), True))
            labels.extend((a, b))
        else:
            occ.append((int(link), False))
            labels.extend((b, a))
    return LXState(tuple(occ), lx_canon(labels))


def lx_tensor_product(a, b):
    off = (max(a.part) + 1) if a.part else 0
    return LXState(a.occ + b.occ, lx_canon(a.part + tuple(x + off for x in b.part)))


def lx_classes(part):
    out = defaultdict(list)
    for i, c in enumerate(part):
        out[c].append(i)
    return out


def lx_merge_classes(part, pairs):
    n = len(part)
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            parent[b] = a
    first = {}
    for i, c in enumerate(part):
        if c in first:
            union(i, first[c])
        else:
            first[c] = i
    for a, b in pairs:
        union(int(a), int(b))
    return lx_canon([find(i) for i in range(n)])


def lx_swap_rows(part, r1, r2):
    if part[r1] == part[r2]:
        return part
    z = list(part)
    z[r1], z[r2] = z[r2], z[r1]
    return lx_canon(z)


def lx_opposite_reconnect(part, r1, r2):
    n = len(part)
    cls = lx_classes(part)
    c1, c2 = part[r1], part[r2]
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            parent[b] = a
    for members in cls.values():
        rem = [x for x in members if x not in (r1, r2)]
        for x in rem[1:]:
            union(rem[0], x)
    rem1 = [x for x in cls[c1] if x not in (r1, r2)]
    rem2 = [x for x in cls[c2] if x not in (r1, r2)]
    if rem1 and rem2:
        union(rem1[0], rem2[0])
    union(r1, r2)
    return lx_canon([find(i) for i in range(n)])


def lx_remove_pair(state, i, j, merge_slots):
    part = lx_merge_classes(state.part, [merge_slots])
    removed = {2*i, 2*i+1, 2*j, 2*j+1}
    keep = [k for k in range(len(part)) if k not in removed]
    keep_classes = {part[k] for k in keep}
    lost = len(set(part) - keep_classes)
    scalar = Fraction(N ** max(0, lost - 1), 1)
    new_occ = tuple(o for k, o in enumerate(state.occ) if k not in (i, j))
    new_part = lx_canon([part[k] for k in keep])
    return scalar, LXState(new_occ, new_part)


def lx_simplify_unitarity(state):
    s = state
    scalar = Fraction(1)
    changed = True
    while changed:
        changed = False
        cls = lx_classes(s.part)
        bylink = defaultdict(list)
        for i, (link, typ) in enumerate(s.occ):
            bylink[link].append((i, typ))
        for _, items in bylink.items():
            done = False
            for (i, t1), (j, t2) in itertools.combinations(items, 2):
                if t1 == t2:
                    continue
                r1, c1 = 2*i, 2*i+1
                r2, c2 = 2*j, 2*j+1
                if set(cls[s.part[r1]]) == {r1, r2}:
                    fac, s = lx_remove_pair(s, i, j, (c1, c2))
                    scalar *= fac
                    changed = done = True
                    break
                if set(cls[s.part[c1]]) == {c1, c2}:
                    fac, s = lx_remove_pair(s, i, j, (r1, r2))
                    scalar *= fac
                    changed = done = True
                    break
            if done:
                break
    return scalar, s


def lx_pinv(p):
    out = [0] * len(p)
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)


def lx_pcompose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def lx_pcycles(p):
    seen = [False] * len(p)
    c = 0
    for i in range(len(p)):
        if not seen[i]:
            c += 1
            j = i
            while not seen[j]:
                seen[j] = True
                j = p[j]
    return c


@lru_cache(None)
def lx_wg_fixed(k):
    ps = list(itertools.permutations(range(k)))
    G = sp.Matrix([
        [sp.Integer(N) ** lx_pcycles(lx_pcompose(lx_pinv(a), b)) for b in ps]
        for a in ps
    ])
    W = G.inv()
    WW = [[Fraction(int(sp.numer(W[i, j])), int(sp.denom(W[i, j]))) for j in range(len(ps))] for i in range(len(ps))]
    return ps, WW


def lx_combine_bra_ket(a, b):
    bra_occ = tuple((link, not typ) for link, typ in a.occ)
    off = (max(a.part) + 1) if a.part else 0
    return bra_occ + b.occ, lx_canon(a.part + tuple(x + off for x in b.part))


# ---------------------------------------------------------------------------
# Accepted loop ordering and joint canonicalization.  Source 622-659,1803-1817.
# ---------------------------------------------------------------------------

def ordered_loop_steps(q, links_obj, shift_fn):
    out = {}
    for li in np.flatnonzero(q):
        li = int(li)
        v, d = links_obj[li]
        w = shift_fn(v, d)
        src, dst = (v, w) if q[li] > 0 else (w, v)
        out[src] = (dst, li, int(q[li]))
    if not out:
        raise RuntimeError("empty loop")
    start = min(out)
    cur = start
    steps = []
    while True:
        dst, li, sg = out[cur]
        steps.append((li, sg))
        cur = dst
        if cur == start:
            return steps
        if len(steps) > len(out) + 1:
            raise RuntimeError("loop ordering failed")


def face_steps_generic(face_id, s, faces_obj, lid_obj, shift_fn):
    v, a, b = faces_obj[face_id]
    va = shift_fn(v, a)
    vb = shift_fn(v, b)
    steps = [
        (lid_obj[(v, a)], +1),
        (lid_obj[(va, b)], +1),
        (lid_obj[(vb, a)], -1),
        (lid_obj[(v, b)], -1),
    ]
    if int(s) < 0:
        steps = [(l, -d) for l, d in reversed(steps)]
    return steps


def _joint_canon_states(*states):
    mp = {}
    out = []
    for st in states:
        if st is None:
            out.append(None)
            continue
        occ = []
        for link, typ in st.occ:
            if link not in mp:
                mp[link] = len(mp)
            occ.append((mp[link], typ))
        out.append(LXState(tuple(occ), st.part))
    return tuple(out)


# ---------------------------------------------------------------------------
# Accepted exact single-link H0 projectors.  Source lines 2791-2838.
# ---------------------------------------------------------------------------

def _rep_sig_from_flux(q):
    q = np.asarray(q, dtype=np.int8)
    return tuple((int(l), +1 if int(q[l]) > 0 else -1) for l in np.flatnonzero(q))


def _Hlink_action(state, target_link):
    fac0, st = lx_simplify_unitarity(state)
    out = defaultdict(Fraction)
    items = [(i, typ) for i, (link, typ) in enumerate(st.occ) if int(link) == int(target_link)]
    if not items:
        return {}
    out[st] += fac0 * Fraction(len(items), 1) * Fraction(2, 3)
    for (i, t1), (j, t2) in itertools.combinations(items, 2):
        r1, r2 = 2*i, 2*j
        if t1 == t2:
            raw = LXState(st.occ, lx_swap_rows(st.part, r1, r2))
            fac, z = lx_simplify_unitarity(raw)
            out[z] += fac0 * fac * Fraction(1, 2)
            out[st] -= fac0 * Fraction(1, 2*N)
        else:
            raw = LXState(st.occ, lx_opposite_reconnect(st.part, r1, r2))
            fac, z = lx_simplify_unitarity(raw)
            out[z] -= fac0 * fac * Fraction(1, 2)
            out[st] += fac0 * Fraction(1, 2*N)
    return {z: c for z, c in out.items() if c}


def _vec_Hlink(v, link):
    out = defaultdict(Fraction)
    for st, c in v.items():
        for z, a in _Hlink_action(st, link).items():
            out[z] += c * a
    return {z: c for z, c in out.items() if c}


def _project_link(v, link, eig, eigs):
    eig = Fraction(eig); eigs = tuple(Fraction(x) for x in eigs)
    outv = dict(v)
    for mu in eigs:
        if mu == eig:
            continue
        den = eig - mu
        hv = _vec_Hlink(outv, link)
        nxt = defaultdict(Fraction)
        for st, c in hv.items(): nxt[st] += c / den
        for st, c in outv.items(): nxt[st] -= mu * c / den
        outv = {st: c for st, c in nxt.items() if c}
    return outv


# ---------------------------------------------------------------------------
# Accepted numerical SU(3) tensors.  Source lines 2672-2697,3462-3471.
# ---------------------------------------------------------------------------

_FAST_T11 = np.zeros((3,3,3,3), dtype=np.float64)
for _i,_j,_k,_l in itertools.product(range(3), repeat=4):
    if _i == _k and _j == _l:
        _FAST_T11[_i,_j,_k,_l] = 1.0/3.0

_FAST_T22 = np.zeros((3,3,3,3,3,3,3,3), dtype=np.float64)
_fast_perms = ((0,1),(1,0))
_fast_W = ((1.0/8.0, -1.0/24.0), (-1.0/24.0, 1.0/8.0))
for _inds in itertools.product(range(3), repeat=8):
    _ur=(_inds[0],_inds[2]); _uc=(_inds[1],_inds[3])
    _br=(_inds[4],_inds[6]); _bc=(_inds[5],_inds[7])
    _val=0.0
    for _si,_sig in enumerate(_fast_perms):
        for _ti,_tau in enumerate(_fast_perms):
            if all(_ur[r] == _br[_sig[r]] and _uc[r] == _bc[_tau[r]] for r in range(2)):
                _val += _fast_W[_si][_ti]
    _FAST_T22[_inds] = _val

_FAST_EPS = np.zeros((3,3,3), dtype=np.float64)
for _perm in itertools.permutations(range(3)):
    _inv = sum(_perm[i] > _perm[j] for i in range(3) for j in range(i+1,3))
    _FAST_EPS[_perm] = -1.0 if _inv % 2 else 1.0
_FAST_T30 = np.einsum('abc,def->adbecf', _FAST_EPS, _FAST_EPS).reshape((3,)*6) / 6.0

_V9_C41=np.array([
    [ 1/32, 1/96,-1/96, 1/96],
    [ 1/96, 1/32, 1/96,-1/96],
    [-1/96, 1/96, 1/32, 1/96],
    [ 1/96,-1/96, 1/96, 1/32],
],dtype=np.float64)


# ---------------------------------------------------------------------------
# Accepted flux key and extended Haar constructor.  Source 3539-3548,4124-4214.
# ---------------------------------------------------------------------------

def _v9_flux_key_state(st):
    cnt=defaultdict(int)
    for l,typ in st.occ:
        cnt[int(l)]+=1 if typ else -1
    out=[]
    for l,c in cnt.items():
        r=c%3
        if r==2: r=-1
        if r: out.append((int(l),int(r)))
    return tuple(sorted(out))


def _v10_endpoint_patterns(a, b):
    aa, bb = _joint_canon_states(a, b)
    occ, part = lx_combine_bra_ket(aa, bb)
    bylink = defaultdict(lambda: [0, 0])
    for link, typ in occ:
        bylink[int(link)][0 if typ else 1] += 1
    return {tuple(x) for x in bylink.values()}


def _v10a2_install_q2_haar(ns):
    ps,W=ns['lx_wg_fixed'](3)
    Ds=[]
    for sig in ps:
        D=np.zeros((3,)*6,dtype=np.float64)
        for r in np.ndindex((3,3,3)):
            br=[0,0,0]
            for i in range(3): br[sig[i]]=r[i]
            D[r[0],r[1],r[2],br[0],br[1],br[2]]=1.0
        Ds.append(D)
    T33=np.zeros((3,)*12,dtype=np.float64)
    for i,Di in enumerate(Ds):
        for j,Dj in enumerate(Ds):
            co=float(W[i][j])
            if co:
                T33 += co*np.einsum('abcABC,defDEF->adbecfADBECF',Di,Dj,optimize=True)
    EPS=ns['_FAST_EPS']; Inv41=[]
    for r in range(4):
        I=np.zeros((3,)*5,dtype=np.float64)
        for idx in np.ndindex((3,)*5):
            maj=idx[:4]; k=idx[4]
            if maj[r]==k:
                I[idx]=EPS[tuple(maj[j] for j in range(4) if j!=r)]
        Inv41.append(I)
    T41=np.zeros((3,)*10,dtype=np.float64)
    for r,I in enumerate(Inv41):
        for s,J in enumerate(Inv41):
            co=float(ns['_V9_C41'][r,s])
            if co:
                T41 += co*np.einsum('abcde,fghij->afbgchdiej',I,J,optimize=True)
    ns['_V9_T41']=T41
    parts=[]
    for comb in itertools.combinations(range(1,6),2):
        A=(0,)+comb; B=tuple(i for i in range(6) if i not in A); parts.append((A,B))
    Inv60=[]
    for A,B in parts:
        I=np.zeros((3,)*6,dtype=np.float64)
        for idx in np.ndindex((3,)*6):
            I[idx]=EPS[tuple(idx[i] for i in A)]*EPS[tuple(idx[i] for i in B)]
        Inv60.append(I)
    G60=np.array([[np.tensordot(A,B,axes=6) for B in Inv60] for A in Inv60],dtype=np.float64)
    _,_,piv=qr(G60,pivoting=True)
    rank60=int(np.linalg.matrix_rank(G60,tol=1e-10)); keep=list(map(int,piv[:rank60]))
    I5=[Inv60[i] for i in keep]; C5=np.linalg.inv(G60[np.ix_(keep,keep)])
    T60=np.zeros((3,)*12,dtype=np.float64)
    for i,I in enumerate(I5):
        for j,J in enumerate(I5):
            co=float(C5[i,j])
            if co:
                T60 += co*np.einsum('abcdef,ghijkl->agbhcidjekfl',I,J,optimize=True)
    M60=np.transpose(T60,(0,2,4,6,8,10,1,3,5,7,9,11)).reshape(729,729)
    cert={
        'wg3_inverse_error': float(np.max(np.abs(np.array([[float(x) for x in row] for row in W]) @ np.array([[3**ns['lx_pcycles'](ns['lx_pcompose'](ns['lx_pinv'](a),b)) for b in ps] for a in ps],dtype=float) - np.eye(6)))),
        'rank60': rank60,
        'T60_trace': float(np.trace(M60)),
        'T60_symmetry_error': float(np.max(np.abs(M60-M60.T))),
        'T60_idempotence_error': float(np.max(np.abs(M60@M60-M60))),
    }
    supported={(1,1),(2,2),(3,3),(3,0),(0,3),(4,1),(1,4),(6,0),(0,6)}
    @lru_cache(maxsize=500000)
    def _canon(a,b):
        occ,part=ns['lx_combine_bra_ket'](a,b)
        by=defaultdict(lambda:{True:[],False:[]})
        for i,(l,t) in enumerate(occ): by[int(l)][bool(t)].append(i)
        args=[]
        for g in by.values():
            U,B=g[True],g[False]; pat=(len(U),len(B))
            if (pat[0]-pat[1])%3: return 0.0
            if pat==(1,1): pos=U+B; ten=ns['_FAST_T11']
            elif pat==(2,2): pos=U+B; ten=ns['_FAST_T22']
            elif pat==(3,3): pos=U+B; ten=T33
            elif pat in ((3,0),(0,3)): pos=U if len(U)==3 else B; ten=ns['_FAST_T30']
            elif pat in ((4,1),(1,4)): pos=(U+B) if len(U)==4 else (B+U); ten=T41
            elif pat in ((6,0),(0,6)): pos=U if len(U)==6 else B; ten=T60
            else: raise RuntimeError(f'Q2 Haar unsupported occurrence pattern {pat}')
            inds=[]
            for p0 in pos: inds.extend((int(part[2*p0]),int(part[2*p0+1])))
            args.extend((ten,inds))
        if not args: return float(ns['N']**len(set(part)))
        return float(ns['oe'].contract(*args,[],optimize='greedy'))
    def haar(a,b):
        aa,bb=ns['_joint_canon_states'](a,b)
        ka=(aa.occ,aa.part); kb=(bb.occ,bb.part)
        if kb < ka: aa,bb=bb,aa
        return _canon(aa,bb)
    return haar,supported,cert,_canon


# ---------------------------------------------------------------------------
# Accepted dynamic irreps and physical half-history.  Source 4382-4400,
# 4546-4727,5123-5132,6309-6344.
# ---------------------------------------------------------------------------

_V10A2_IMAP={1:(1,0),-1:(0,1),2:(2,0),-2:(0,2),8:(1,1)}

def _v10a2_energy_dyn(r):
    p,q=r; return Fraction(p*p+q*q+p*q+3*p+3*q,6)

def _v10a2_fuse(r,sg):
    p,q=r; out=[]
    if sg>0:
        out.append((p+1,q))
        if p>=1: out.append((p-1,q+1))
        if q>=1: out.append((p,q-1))
    else:
        out.append((p,q+1))
        if q>=1: out.append((p+1,q-1))
        if p>=1: out.append((p-1,q))
    return tuple(out)

def _v10a2_sig_dyn(sig): return tuple(sorted((int(l),)+_V10A2_IMAP[int(r)] for l,r in sig))
def _v10a2_sig_conj(sig): return tuple(sorted((l,q,p) for l,p,q in sig))
def _v10a2_sig_canon(sig):
    c=_v10a2_sig_conj(sig);return min(sig,c)
def _v10a2_sig_E(sig): return sum((_v10a2_energy_dyn((p,q)) for _,p,q in sig),Fraction(0))


def su3_c2_pq(p, q):
    p=int(p); q=int(q)
    return (p*p + q*q + p*q + 3*p + 3*q) / 3.0


def su3_fuse_fundamental(rep):
    p,q=map(int,rep)
    out=[(p+1,q)]
    if p>=1: out.append((p-1,q+1))
    if q>=1: out.append((p,q-1))
    return tuple(out)


def su3_fuse_antifundamental(rep):
    p,q=map(int,rep)
    out=[(p,q+1)]
    if q>=1: out.append((p+1,q-1))
    if p>=1: out.append((p-1,q))
    return tuple(out)


def _v10a11_oneface_axial_character():
    """Exact C- one-plaquette character moments through the direct fourth order.

    This replaces the 54 (1-face,1-face) raw Haar block contractions, whose
    largest expanded partition block is 432x432.  It is the same physical
    one-face sector in the Haar-orthonormal SU(3) character basis.
    """
    # C- irreps reachable within two magnetic steps from 3-3bar:
    # (3-3b), (6-6b), (10-10b), ((2,1)-(1,2)).
    odd=((1,0),(2,0),(3,0),(2,1))
    # Build M in the normalized odd character basis by fusion, not by targets.
    # For each representative R, act with chi_3+chi_3bar on R-Rbar and collect
    # its coefficient on S-Sbar.
    M=np.zeros((4,4),dtype=np.float64)
    def conj(r): return (r[1],r[0])
    def fusions(r): return tuple(su3_fuse_fundamental(r))+tuple(su3_fuse_antifundamental(r))
    for j,r in enumerate(odd):
        coeff=Counter(fusions(r)); coeffb=Counter(fusions(conj(r)))
        for i,sr in enumerate(odd):
            # normalized odd states give the coefficient of chi_sr in
            # M(chi_r-chi_rbar); conjugation symmetry guarantees antisym pair.
            M[i,j]=float(coeff[sr]-coeffb[sr])
    H0=np.diag([2.0*su3_c2_pq(*r) for r in odd])
    V=-M; E0=H0[0,0]
    B=V[1:,0].copy(); W=V[1:,1:].copy(); den=E0-np.diag(H0)[1:]
    R=np.diag(1.0/den)
    r1=R@B; w2=W@r1; r2=R@w2; r12=R@r1
    return dict(e1=float(V[0,0]),e2=float(B@r1),sigma3=float(r1@w2),
                N=float(r1@r1),C=float(r1@r2),J=float(r1@r12),D=float(w2@r2))


def _v10a3_prune(v, tol=V10A3_COEFF_TOL):
    out = {}
    for st,c in v.items():
        value = float(c)
        ensure_finite("prune.coefficient", value)
        if abs(value) > tol:
            out[st] = value
    return out

def _v10a3_add_vec(dst, src, scale=1.0):
    ensure_finite("vector.scale", float(scale))
    for st,c in src.items():
        term = float(scale)*float(c)
        ensure_finite("vector.term", term)
        dst[st] += term
        ensure_finite("vector.accumulator", float(dst[st]))

def _v10a3_vec_inner(v, w, haar):
    """Physical inner product with exact center prefilter and extended SU(3) Haar."""
    if not v or not w:
        return 0.0
    ga=defaultdict(list); gb=defaultdict(list)
    for st,c in v.items(): ga[_v9_flux_key_state(st)].append((st,float(c)))
    for st,c in w.items(): gb[_v9_flux_key_state(st)].append((st,float(c)))
    ans=0.0
    for k,la in ga.items():
        lb=gb.get(k)
        if not lb: continue
        for a,ca in la:
            for b,cb in lb:
                audit = getattr(haar, "audit", None)
                if audit is None:
                    h = float(haar(a,b))
                else:
                    with audit.context(
                        flux_key=k,
                        bra_coefficient=float(ca),
                        ket_coefficient=float(cb),
                    ):
                        h = float(haar(a,b))
                ensure_finite("overlap.haar", h)
                term = ca*cb*h
                ensure_finite("overlap.term", term)
                ans += term
                ensure_finite("overlap.accumulator", ans)
    ensure_finite("overlap.result", float(ans))
    return float(ans)

def _v10a3_vec_norm(v, haar):
    x=_v10a3_vec_inner(v,v,haar)
    ensure_finite("norm.square", x)
    if x < -V10A3_NORM_TOL:
        raise RuntimeError(f"physical vector has negative norm2 {x:.3e}")
    result=max(0.0,float(x))
    ensure_finite("norm.result", result)
    return result

def _v10a3_sig_vec_add(state, sig, vec, scale=1.0):
    d=state.setdefault(sig,defaultdict(float))
    _v10a3_add_vec(d,vec,scale)

def _v10a3_compress_state(state):
    out={}
    for sig,v in state.items():
        z=_v10a3_prune(v)
        if z: out[sig]=z
    return out

def _v10a3_candidate_faces_vec(v):
    cand=set()
    for st in v:
        for l,_ in st.occ:
            cand.update(link_faces[int(l)])
    return cand

def _v10a3_project_action_dyn(model,v,sig,face,orient):
    fs=model['v9_fs_cached'](face,orient); fd={int(l):int(s) for l,s in fs}
    cur={int(l):(int(p),int(q)) for l,p,q in sig}
    prod=defaultdict(Fraction)
    for st,c in v.items(): prod[lx_tensor_product(st,lx_trace_state(fs))]+=c
    chans=[(dict(prod),dict(cur))]
    for l,sg in fd.items():
        r=cur.get(l,(0,0)); opts=_v10a2_fuse(r,sg); eigs=tuple(_v10a2_energy_dyn(x) for x in opts)
        if len(set(eigs))!=len(eigs): raise RuntimeError(f"degenerate local fusion {r},{sg},{opts}")
        nxt=[]
        for vec,smap in chans:
            for rr,ee in zip(opts,eigs):
                pv=vec if len(opts)==1 else _project_link(vec,l,ee,eigs)
                if not pv: continue
                sm=dict(smap)
                if rr==(0,0): sm.pop(l,None)
                else: sm[l]=rr
                nxt.append((pv,sm))
        chans=nxt
    return [(vec,tuple(sorted((l,p,q) for l,(p,q) in sm.items()))) for vec,sm in chans]

def _v10a3_face_state(face):
    q=np.asarray(B2[:,int(face)],dtype=np.int8)
    st=lx_trace_state(ordered_loop_steps(q,links,shift))
    stc=lx_trace_state(ordered_loop_steps(-q,links,shift))
    sig=_v10a2_sig_dyn(_rep_sig_from_flux(q))
    sigc=_v10a2_sig_dyn(_rep_sig_from_flux(-q))
    s=1.0/math.sqrt(2.0)
    return {sig:{st:s},sigc:{stc:-s}}

def _v10a3_face_pvec(face):
    q=np.asarray(B2[:,int(face)],dtype=np.int8)
    st=lx_trace_state(ordered_loop_steps(q,links,shift))
    stc=lx_trace_state(ordered_loop_steps(-q,links,shift))
    s=1.0/math.sqrt(2.0)
    return {st:s,stc:-s}

def _v10a3_physical_blocks(state):
    """Combine conjugate H0 signatures into physical C- blocks."""
    out=defaultdict(lambda:defaultdict(float))
    for sig,v in state.items():
        cs=_v10a2_sig_canon(sig); Esg=_v10a2_sig_E(sig)
        _v10a3_add_vec(out[(cs,Esg)],v,1.0)
    return {k:_v10a3_prune(v) for k,v in out.items() if _v10a3_prune(v)}

def _v10a3_p0_catalog():
    faces0=[]; vecs=[]; keymap=defaultdict(list)
    for f in range(P):
        v,a,b=faces[f]
        q=np.asarray(B2[:,f],dtype=np.int8)
        sig=_v10a2_sig_dyn(_rep_sig_from_flux(q))
        cs=_v10a2_sig_canon(sig)
        key=(cs,_v10a2_sig_E(sig))
        faces0.append(f); vecs.append(_v10a3_face_pvec(f)); keymap[key].append(f)
    return faces0,vecs,keymap


P0_FACES,P0_VECS,P0_BY_SIG=_v10a3_p0_catalog()


def _v10a3_reduced_resolvent(state, haar, label="R"):
    """R=(E0-H0)^-1 on the complement of the full plaquette E0 band."""
    out={}; resonance_max=0.0; resonance_groups=0
    blocks=_v10a3_physical_blocks(state)
    for (cs,Esg),v0 in blocks.items():
        if Esg != Fraction(8,3):
            continue
        resonance_groups += 1
        v=dict(v0)
        for f in P0_BY_SIG.get((cs,Esg),()):
            pv=P0_VECS[f]
            audit = getattr(haar, "audit", None)
            if audit is None:
                ov=_v10a3_vec_inner(pv,v,haar)
            else:
                with audit.context(
                    resolver_phase="P0-projector subtraction",
                    p0_projector_face=int(f),
                    p0_projector_geometry=json_safe(faces[int(f)]),
                    bra_support=frozenset((int(f),)),
                    h0_signature=cs,
                    h0_energy=Esg,
                ):
                    ov=_v10a3_vec_inner(pv,v,haar)
            ensure_finite(f"{label}.overlap", ov)
            if abs(ov)>V10A3_COEFF_TOL:
                for st,c in pv.items(): v[st]=v.get(st,0.0)-ov*c
        v=_v10a3_prune(v)
        audit = getattr(haar, "audit", None)
        if audit is None:
            n2=_v10a3_vec_norm(v,haar)
        else:
            with audit.context(
                resolver_phase="post-P0 residual norm",
                p0_projector_face=None,
                p0_projector_geometry=None,
                h0_signature=cs,
                h0_energy=Esg,
            ):
                n2=_v10a3_vec_norm(v,haar)
        ensure_finite(f"{label}.resonance_norm2", n2)
        resonance_max=max(resonance_max,n2)
        ensure_finite(f"{label}.resonance_max", resonance_max)
    if resonance_max > V10A3_NORM_TOL:
        raise RuntimeError(f"{label}: unresolved physical E0 resonance norm2={resonance_max:.3e}")
    for sig,v in state.items():
        Esg=_v10a2_sig_E(sig)
        if Esg == Fraction(8,3):
            continue
        den=float(Fraction(8,3)-Esg)
        ensure_finite(f"{label}.denominator", den)
        if abs(den)<1e-14: raise RuntimeError(f"{label}: zero denominator outside P0")
        out[sig]={st:float(c)/den for st,c in v.items()}
    return _v10a3_compress_state(out), {'E0_groups':resonance_groups,'E0_residual_norm2_max':resonance_max}


def _v10a4_fs_model():
    """Only the oriented plaquette-step cache required by the local W recursion."""
    lid={(v,d):i for i,(v,d) in enumerate(links)}
    cache={}
    def fs(face,orient):
        key=(int(face),int(orient))
        if key not in cache:
            cache[key]=tuple(face_steps_generic(int(face),int(orient),faces,lid,shift))
        return cache[key]
    return {'v9_fs_cached':fs}


_fsmodel = _v10a4_fs_model()

_V10A3_LID={(v,d):i for i,(v,d) in enumerate(links)}
_V17_FID = {(tuple(v),int(a),int(b)):i for i,(v,a,b) in enumerate(faces)}


def _v10a3_translate_state(st, dv):
    """Periodic spatial translation of a trace-network state; color contractions are untouched."""
    dx,dy,dz=(int(dv[0])%L,int(dv[1])%L,int(dv[2])%L)
    occ=[]
    for li,typ in st.occ:
        v,d=links[int(li)]
        vv=((v[0]+dx)%L,(v[1]+dy)%L,(v[2]+dz)%L)
        occ.append((_V10A3_LID[(vv,d)],typ))
    return LXState(tuple(occ),st.part)


def _v10a3_translate_sig(sig,dv):
    dx,dy,dz=(int(dv[0])%L,int(dv[1])%L,int(dv[2])%L)
    out=[]
    for li,p,q in sig:
        v,d=links[int(li)]
        vv=((v[0]+dx)%L,(v[1]+dy)%L,(v[2]+dz)%L)
        out.append((_V10A3_LID[(vv,d)],int(p),int(q)))
    return tuple(sorted(out))


def _v17_translate_face(f,dv):
    v,a,b=faces[int(f)]
    vv=((v[0]+int(dv[0]))%L,(v[1]+int(dv[1]))%L,(v[2]+int(dv[2]))%L)
    return _V17_FID[(vv,int(a),int(b))]


def _v17_translate_support(S,dv):
    return frozenset(_v17_translate_face(f,dv) for f in S)


def _v17_add_state(dst,src,scale=1.0):
    for sig,v in src.items(): _v10a3_sig_vec_add(dst,sig,v,scale)

def _v17_aggregate(LD):
    out={}
    for st in LD.values(): _v17_add_state(out,st,1.0)
    return _v10a3_compress_state(out)

_ACTIVE_BUDGET: ResourceBudget | None = None

def _v17_apply_W_labeled(LD,label='W'):
    out={}; actions=channels=0
    items=list(LD.items()); t0=time.time()
    for ii,(S,state) in enumerate(items):
        for sig,v in state.items():
            cand=_v10a3_candidate_faces_vec(v)
            for f in cand:
                for o in (-1,+1):
                    actions+=1
                    if _ACTIVE_BUDGET is not None:
                        if actions > _ACTIVE_BUDGET.limits.max_w_actions_per_call:
                            raise PreflightFailure(f"W action ceiling exceeded in {label}: {actions}")
                        if actions % 128 == 0:
                            _ACTIVE_BUDGET.check(label, current=ii+1, total=len(items))
                    for pv,osig in _v10a3_project_action_dyn(_fsmodel,v,sig,int(f),int(o)):
                        channels+=1
                        if _ACTIVE_BUDGET is not None and channels > _ACTIVE_BUDGET.limits.max_w_channels_per_call:
                            raise PreflightFailure(f"W channel ceiling exceeded in {label}: {channels}")
                        T=frozenset(set(S)|{int(f)})
                        d=out.setdefault(T,{})
                        _v10a3_sig_vec_add(d,osig,pv,-1.0)
                        if _ACTIVE_BUDGET is not None and len(out) > _ACTIVE_BUDGET.limits.max_supports_per_stage:
                            raise PreflightFailure(f"support ceiling exceeded in {label}: {len(out)}")
        if V10A7_PROGRESS and len(items)>20 and (ii+1)%max(1,len(items)//4)==0:
            print(f'      {label} supports {ii+1}/{len(items)}; out supports={len(out)}; elapsed={time.time()-t0:.1f}s')
    result={S:_v10a3_compress_state(st) for S,st in out.items() if _v10a3_compress_state(st)}
    stats=dict(actions=actions,channels=channels,supports=len(result))
    ensure_finite(f"{label}.transition_stats", stats)
    if _ACTIVE_BUDGET is not None:
        _ACTIVE_BUDGET.check(label, current=len(items), total=len(items), force_heartbeat=True)
    return result,stats


# ---------------------------------------------------------------------------
# Fail-closed schedule, provenance, full-T1 pre-Haar census, and checkpoints.
# ---------------------------------------------------------------------------

CHECKPOINT_SCHEMA = "hodge-full-t1-occurrence-checkpoint/v2"
UNIT_AUDIT_SCHEMA = "hodge-occurrence-unit/v2"


def finite_max(name: str, values: Iterable[float], *, default: float = 0.0) -> float:
    checked = [float(ensure_finite(f"{name}[{i}]", value)) for i, value in enumerate(values)]
    result = float(max(checked, default=float(default)))
    ensure_finite(name, result)
    return result


def _state_json(st: LXState) -> dict[str, Any]:
    return {"occ": [[int(link), bool(kind)] for link, kind in st.occ],
            "part": [int(x) for x in st.part]}


def _support_json(support: Iterable[int] | None) -> list[int] | None:
    return None if support is None else sorted(map(int, support))


def _counts_json(counts: Counter[tuple[int, int]]) -> dict[str, int]:
    return {f"{a},{b}": int(n) for (a, b), n in sorted(counts.items())}


def _parse_counts(payload: Mapping[str, Any], label: str) -> Counter[tuple[int, int]]:
    result: Counter[tuple[int, int]] = Counter()
    for key, value in payload.items():
        parts = str(key).split(",")
        if len(parts) != 2:
            raise PreflightFailure(f"{label}: malformed occurrence key {key!r}")
        pattern = (int(parts[0]), int(parts[1]))
        count = int(value)
        if count <= 0:
            raise PreflightFailure(f"{label}: non-positive count for {pattern}")
        result[pattern] = count
    return result


def _validate_representatives(payload: Any,
                              counts: Counter[tuple[int, int]],
                              consumer: str) -> dict[str, Mapping[str, Any]]:
    if not isinstance(payload, Mapping):
        raise PreflightFailure(f"{consumer}: representative ledger is malformed")
    expected_keys = {f"{a},{b}" for a, b in counts}
    actual_keys = {str(key) for key in payload}
    if actual_keys != expected_keys:
        raise PreflightFailure(
            f"{consumer}: representative ledger is incomplete: "
            f"expected={sorted(expected_keys)}, actual={sorted(actual_keys)}"
        )
    result: dict[str, Mapping[str, Any]] = {}
    for key, provenance in payload.items():
        text_key = str(key)
        pattern = tuple(map(int, text_key.split(",")))
        if len(pattern) != 2 or pattern not in counts or not isinstance(provenance, Mapping):
            raise PreflightFailure(f"{consumer}: representative mismatch for {text_key}")
        ensure_finite(f"{consumer}.representative.{text_key}", provenance)
        if provenance.get("consumer") != consumer:
            raise PreflightFailure(f"{consumer}: representative consumer mismatch for {text_key}")
        if tuple(map(int, provenance.get("occurrence", ()))) != pattern:
            raise PreflightFailure(f"{consumer}: representative occurrence mismatch for {text_key}")
        result[text_key] = provenance
    return result


class OccurrenceAudit:
    def __init__(self, root_faces: Sequence[int], budget: ResourceBudget | None = None) -> None:
        self.root_faces = tuple(map(int, root_faces))
        if len(self.root_faces) != 3 or len(set(self.root_faces)) != 3:
            raise PreflightFailure(f"full-T1 audit needs three distinct roots: {self.root_faces}")
        self.budget = budget
        self.action_log: list[dict[str, Any]] = []
        self.all_counts: Counter[tuple[int, int]] = Counter()
        self.center_neutral_counts: Counter[tuple[int, int]] = Counter()
        self.by_consumer: dict[str, Counter[tuple[int, int]]] = defaultdict(Counter)
        self.pair_tests: Counter[str] = Counter()
        self.representatives: dict[tuple[str, tuple[int, int]], dict[str, Any]] = {}
        self._context: dict[str, Any] = {"consumer": "initialization"}

    @contextmanager
    def context(self, **fields: Any):
        previous = self._context
        self._context = {**previous, **fields}
        try:
            yield
        finally:
            self._context = previous

    def record_action(self, *, polarization_index: int, source_stage: str,
                      target_stage: str, source_history_depth: int,
                      direct_blocks: Sequence[str], state_count: int) -> None:
        root_face = self.root_faces[int(polarization_index)]
        self.action_log.append({
            "global_ordinal": len(self.action_log) + 1,
            "polarization_index": int(polarization_index),
            "polarization": list(T1_POLS[int(polarization_index)]),
            "root_face": int(root_face),
            "root_geometry": json_safe(faces[root_face]),
            "source_stage": str(source_stage),
            "target_stage": str(target_stage),
            "source_history_depth": int(source_history_depth),
            "direct_blocks_policy_label": list(direct_blocks),
            "input_supports": int(state_count),
        })

    def inspect(self, bra: LXState, ket: LXState, **fields: Any) -> None:
        context = {**self._context, **fields}
        consumer = str(context.get("consumer", "unknown"))
        ensure_finite(f"{consumer}.bra_coefficient", context.get("bra_coefficient", 0.0))
        ensure_finite(f"{consumer}.ket_coefficient", context.get("ket_coefficient", 0.0))
        if self.budget is not None:
            self.budget.check(
                str(context.get("budget_label", consumer)), pair_increment=1,
            )
        self.pair_tests[consumer] += 1

        physical_links: list[int] = []
        seen_links: set[int] = set()
        for state in (bra, ket):
            for link, _ in state.occ:
                if int(link) not in seen_links:
                    seen_links.add(int(link))
                    physical_links.append(int(link))

        aa, bb = _joint_canon_states(bra, ket)
        swapped = False
        if (bb.occ, bb.part) < (aa.occ, aa.part):
            aa, bb = bb, aa
            swapped = True
        combined_occ, combined_part = lx_combine_bra_ket(aa, bb)
        by_link: dict[int, list[int]] = defaultdict(lambda: [0, 0])
        for link, kind in combined_occ:
            by_link[int(link)][0 if kind else 1] += 1

        bra_index = context.get("bra_polarization_index")
        ket_index = context.get("ket_polarization_index")
        bra_root = None if bra_index is None else self.root_faces[int(bra_index)]
        ket_root = None if ket_index is None else self.root_faces[int(ket_index)]
        displacement = context.get("dv")
        for canonical_link in sorted(by_link):
            pattern = tuple(map(int, by_link[canonical_link]))
            self.all_counts[pattern] += 1
            self.by_consumer[consumer][pattern] += 1
            neutral = (pattern[0] - pattern[1]) % 3 == 0
            if neutral:
                self.center_neutral_counts[pattern] += 1

            occurrence_bound_violation = pattern in FORBIDDEN_OCCURRENCES or sum(pattern) > 6
            contractor_domain_violation = neutral and pattern not in BASELINE_CENTER_NEUTRAL
            representative_key = (consumer, pattern)
            if (representative_key in self.representatives
                    and not occurrence_bound_violation
                    and not contractor_domain_violation):
                continue

            provenance = {
                "requested_order": REQUESTED_ORDER,
                "consumer": consumer,
                "moment": context.get("moment"),
                "bra_polarization_index": bra_index,
                "bra_polarization": None if bra_index is None else list(T1_POLS[int(bra_index)]),
                "bra_root_face": bra_root,
                "bra_root_geometry": None if bra_root is None else json_safe(faces[bra_root]),
                "ket_polarization_index": ket_index,
                "ket_polarization": None if ket_index is None else list(T1_POLS[int(ket_index)]),
                "ket_root_face": ket_root,
                "ket_root_geometry": None if ket_root is None else json_safe(faces[ket_root]),
                "dv": None if displacement is None else list(map(int, displacement)),
                "source_stage": context.get("source_stage"),
                "target_stage": context.get("target_stage"),
                "source_history_depth": context.get("source_history_depth"),
                "target_history_depth": context.get("target_history_depth"),
                "block_origin": context.get("block_origin"),
                "operator_between_endpoints": bool(context.get("operator_between_endpoints", False)),
                "bra_support": _support_json(context.get("bra_support")),
                "ket_support": _support_json(context.get("ket_support")),
                "h0_signature": repr(context.get("h0_signature")),
                "h0_energy": (None if context.get("h0_energy") is None
                              else str(context.get("h0_energy"))),
                "flux_key": json_safe(context.get("flux_key")),
                "resolver_context": json_safe(context.get("resolver_context")),
                "resolver_phase": context.get("resolver_phase"),
                "p0_projector_face": context.get("p0_projector_face"),
                "p0_projector_geometry": json_safe(context.get("p0_projector_geometry")),
                "route": context.get("route"),
                "canonical_link": int(canonical_link),
                "physical_link_order": physical_links,
                "occurrence": list(pattern),
                "bra_coefficient": context.get("bra_coefficient"),
                "ket_coefficient": context.get("ket_coefficient"),
                "bra": _state_json(bra),
                "ket": _state_json(ket),
                "combined_occ": [[int(link), bool(kind)] for link, kind in combined_occ],
                "combined_part": [int(x) for x in combined_part],
                "symmetric_canonicalization_swapped": swapped,
                "action_log": list(self.action_log),
            }
            ensure_finite(f"{consumer}.provenance", provenance)
            self.representatives.setdefault(representative_key, provenance)

            if occurrence_bound_violation:
                raise OccurrenceViolation(canonical_json({
                    "error": "upstream order-four schedule violation: local occurrence bound",
                    "provenance": provenance,
                    "contractor_called": False,
                }))
            if contractor_domain_violation:
                raise OccurrenceViolation(canonical_json({
                    "error": "upstream schedule violation: occurrence outside executed contractor domain",
                    "provenance": provenance,
                    "approved": [list(x) for x in sorted(BASELINE_CENTER_NEUTRAL)],
                    "contractor_called": False,
                }))

    def unit_payload(self, consumer: str) -> dict[str, Any]:
        counts = self.by_consumer.get(consumer, Counter())
        neutral = Counter({pattern: count for pattern, count in counts.items()
                           if (pattern[0] - pattern[1]) % 3 == 0})
        representatives = {
            f"{pattern[0]},{pattern[1]}": self.representatives[(consumer, pattern)]
            for pattern in sorted(counts)
            if (consumer, pattern) in self.representatives
        }
        result = {
            "schema": UNIT_AUDIT_SCHEMA,
            "consumer": consumer,
            "pair_tests": int(self.pair_tests.get(consumer, 0)),
            "all_occurrences": _counts_json(counts),
            "center_neutral_occurrences": _counts_json(neutral),
            "representatives": representatives,
        }
        ensure_finite(f"unit_payload.{consumer}", result)
        return result

    def merge_unit(self, payload: Mapping[str, Any]) -> None:
        if payload.get("schema") != UNIT_AUDIT_SCHEMA:
            raise PreflightFailure("checkpoint unit audit schema mismatch")
        consumer = str(payload.get("consumer"))
        if consumer in self.by_consumer or consumer in self.pair_tests:
            raise PreflightFailure(f"checkpoint unit would duplicate audit consumer {consumer}")
        counts = _parse_counts(payload.get("all_occurrences", {}), consumer)
        neutral = _parse_counts(payload.get("center_neutral_occurrences", {}), consumer)
        expected_neutral = Counter({pattern: count for pattern, count in counts.items()
                                    if (pattern[0] - pattern[1]) % 3 == 0})
        if neutral != expected_neutral:
            raise PreflightFailure(f"checkpoint neutral ledger mismatch for {consumer}")
        representatives = _validate_representatives(
            payload.get("representatives", {}), counts, consumer,
        )
        pair_tests = int(payload.get("pair_tests", -1))
        if pair_tests < 0:
            raise PreflightFailure(f"checkpoint pair-test count invalid for {consumer}")
        occurrence_total = sum(counts.values())
        if ((pair_tests == 0) != (occurrence_total == 0)
                or occurrence_total < pair_tests):
            raise PreflightFailure(
                f"checkpoint pair/occurrence ledger mismatch for {consumer}: "
                f"pairs={pair_tests}, occurrences={occurrence_total}"
            )
        if self.budget is not None:
            self.budget.check(
                f"resume {consumer}", pair_increment=pair_tests,
            )
        self.by_consumer[consumer].update(counts)
        self.all_counts.update(counts)
        self.center_neutral_counts.update(neutral)
        self.pair_tests[consumer] = pair_tests
        for key, provenance in representatives.items():
            pattern = tuple(map(int, str(key).split(",")))
            self.representatives[(consumer, pattern)] = dict(provenance)

    def report(self) -> dict[str, Any]:
        return {
            "action_log": self.action_log,
            "pair_tests": dict(sorted((key, int(value)) for key, value in self.pair_tests.items())),
            "all_occurrences": _counts_json(self.all_counts),
            "center_neutral_occurrences": _counts_json(self.center_neutral_counts),
            "by_consumer": {
                key: _counts_json(value) for key, value in sorted(self.by_consumer.items())
            },
            "representatives": {
                f"{consumer}:{pattern[0]},{pattern[1]}": self.representatives[(consumer, pattern)]
                for consumer, pattern in sorted(self.representatives)
            },
        }


class GuardedHaar:
    def __init__(self, raw_haar: Callable[[LXState, LXState], float],
                 audit: OccurrenceAudit) -> None:
        self.raw_haar = raw_haar
        self.audit = audit

    def __call__(self, a: LXState, b: LXState) -> float:
        self.audit.inspect(a, b)
        value = float(self.raw_haar(a, b))
        ensure_finite("guarded_haar.result", value)
        return value


class MagneticSchedule:
    EXPECTED = (
        ("P0", "W1", 0, ("PP", "1P")),
        ("R1", "W2", 1, ("P1", "11", "21")),
    )

    def __init__(self, audit: OccurrenceAudit, polarization_index: int,
                 engine: Callable[..., Any] = _v17_apply_W_labeled) -> None:
        self.audit = audit
        self.polarization_index = int(polarization_index)
        self.engine = engine
        self.step = 0

    def apply(self, state, *, source_stage: str, target_stage: str,
              source_history_depth: int, direct_blocks: Sequence[str]):
        request = (source_stage, target_stage, int(source_history_depth), tuple(direct_blocks))
        expected = self.EXPECTED[self.step] if self.step < len(self.EXPECTED) else None
        if request != expected or not set(direct_blocks).issubset(ALLOWED_BLOCKS):
            raise ScheduleViolation(canonical_json({
                "error": "magnetic request does not match the sealed two-step root schedule",
                "requested_order": REQUESTED_ORDER,
                "root_step": self.step + 1,
                "request": request,
                "expected": expected,
                "polarization_index": self.polarization_index,
                "polarization": list(T1_POLS[self.polarization_index]),
                "root_face": self.audit.root_faces[self.polarization_index],
                "action_log": self.audit.action_log,
                "contractor_called": False,
            }))
        self.audit.record_action(
            polarization_index=self.polarization_index,
            source_stage=source_stage,
            target_stage=target_stage,
            source_history_depth=source_history_depth,
            direct_blocks=direct_blocks,
            state_count=len(state),
        )
        result = self.engine(state, f"{target_stage} pol{self.polarization_index}")
        ensure_finite(f"{target_stage}.engine_stats", result[1])
        self.step += 1
        return result


def _resolvent_labeled(LD, haar: GuardedHaar, label: str,
                       polarization_index: int, root_face: int,
                       budget: ResourceBudget):
    if len(LD) > budget.limits.max_supports_per_stage:
        raise PreflightFailure(f"support ceiling exceeded entering {label}: {len(LD)}")
    out = {}
    residuals: list[float] = []
    groups = 0
    supports = sorted(LD, key=lambda value: (len(value), tuple(sorted(value))))
    for support_index, support in enumerate(supports, 1):
        state = LD[support]
        with haar.audit.context(
            consumer=f"_resolver:{label}:pol{polarization_index}",
            budget_label=f"resolver {label} pol{polarization_index}",
            moment=None,
            bra_polarization_index=polarization_index,
            ket_polarization_index=polarization_index,
            dv=(0, 0, 0),
            source_stage=label,
            target_stage=label,
            source_history_depth=_stage_depth(label),
            target_history_depth=_stage_depth(label),
            block_origin="exact reduced-resolvent norm",
            operator_between_endpoints=False,
            bra_support=support,
            ket_support=support,
            resolver_context={"stage": label, "root_face": int(root_face)},
        ):
            resolved, stats = _v10a3_reduced_resolvent(state, haar, label)
        ensure_finite(f"{label}.support_stats", stats)
        residuals.append(float(stats["E0_residual_norm2_max"]))
        groups += int(stats["E0_groups"])
        if resolved:
            out[support] = resolved
        budget.check(
            f"resolver {label} pol{polarization_index}",
            current=support_index, total=len(supports),
        )
    result_stats = {
        "input_supports": len(supports),
        "output_supports": len(out),
        "E0_groups": groups,
        "E0_residual_norm2_max": finite_max(f"{label}.residual_max", residuals),
    }
    ensure_finite(f"{label}.stats", result_stats)
    return out, result_stats


MOMENTS = (
    ("e1", "P0", "W1", "PP", True, False),
    ("K2/e2", "W1", "R1", "P1 + 1P", False, False),
    ("sigma3", "R1", "W2", "11", True, False),
    ("N", "R1", "R1", "P1 + 1P", False, False),
    ("C1", "R1", "R2", "11", False, False),
    ("J", "R1", "R12", "P1 + 1P", False, False),
    ("D", "W2", "R2", "11·11 + 12·21", False, True),
)

MOMENT_BLOCK_COMPONENTS = {
    "e1": ("PP",),
    "K2/e2": ("P1", "1P"),
    "sigma3": ("11",),
    "N": ("P1", "1P"),
    "C1": ("11",),
    "J": ("P1", "1P"),
    "D": ("11", "12", "21"),
}

# Rows are ket polarizations and columns are bra polarizations, exactly matching
# the accepted v24c ordered endpoint dispatcher.  True means the accepted route
# performs substantive H0, flux, pair, and occurrence work and this preflight
# must observe all four.  False is not a free pass: the 125-translation scan is
# still mandatory, but an empty endpoint ledger is allowed for the stated exact
# structural reason.
NONVACUITY_MATRIX = {
    "e1": (
        (True, False, False),
        (False, True, False),
        (False, False, True),
    ),
    "K2/e2": (
        (True, True, True),
        (True, True, True),
        (True, True, True),
    ),
    "sigma3": (
        (False, False, False),
        (False, False, False),
        (False, False, False),
    ),
    "N": (
        (True, True, True),
        (True, True, True),
        (True, True, True),
    ),
    "C1": (
        (True, True, True),
        (True, True, True),
        (True, True, True),
    ),
    "J": (
        (True, True, True),
        (True, True, True),
        (True, True, True),
    ),
    "D": (
        (True, True, True),
        (True, True, True),
        (True, True, True),
    ),
}

STRUCTURAL_ZERO_JUSTIFICATIONS = {
    "e1:cross-polarization": (
        "accepted v24c physical PVP is the polarization-diagonal identity; "
        "cross-polarization e1 endpoint ledgers may therefore be empty "
        "(authority lines 6563-6575)"
    ),
    "sigma3:all-polarizations": (
        "accepted v24c exact source-sector identity Q1 W Q1 = 0; sigma3 "
        "endpoint ledgers may therefore be empty (authority lines 5998-6003)"
    ),
}

NONVACUITY_EVIDENCE = {
    "e1": "v24c computed physical PVP=I (authority lines 6563-6575)",
    "K2/e2": (
        "v24c K2 scans every face against all three ket polarizations "
        "(authority lines 5880-5894, 6712-6715)"
    ),
    "sigma3": "v24c exact source-sector Q1 W Q1=0 identity (authority lines 5998-6003)",
    "N,C1,J,D": (
        "v24c ordered 3x3 endpoint dispatcher and calls "
        "(authority lines 6670-6684, 6717-6720)"
    ),
}


def _nonvacuity_expected(moment: str, bra_index: int, ket_index: int) -> bool:
    return bool(NONVACUITY_MATRIX[str(moment)][int(ket_index)][int(bra_index)])


def _substantive_unit_stats(stats: Mapping[str, Any]) -> bool:
    return (
        int(stats.get("matched_h0_support_blocks", 0)) > 0
        and int(stats.get("matched_flux_groups", 0)) > 0
        and int(stats.get("state_pair_tests", 0)) > 0
        and int(stats.get("local_occurrences", 0)) > 0
    )


def _valid_same_d_route(stats: Mapping[str, Any]) -> bool:
    certificate = stats.get("analytic_oneface_route_certificate")
    if not isinstance(certificate, Mapping):
        return False
    local = certificate.get("local_displacement")
    if not isinstance(local, list) or len(local) != 3:
        return False
    try:
        local = list(map(int, local))
        local_key = ",".join(map(str, local))
        skips = int(stats.get("samepol_oneface_analytic_skips", 0))
        derived = float(certificate.get("derived_value", math.inf))
        error = float(certificate.get("absolute_error", math.inf))
        computed_error = float(abs(derived + 13.0 / 896.0))
    except (TypeError, ValueError, OverflowError):
        return False
    displacements = stats.get("samepol_oneface_skip_displacements")
    candidates = stats.get("samepol_oneface_skip_candidates")
    cross_candidates = stats.get("crosspol_oneface_fallback_candidates")
    cross_displacements = stats.get("crosspol_oneface_fallback_displacements")
    cross_audited = stats.get("crosspol_oneface_audited_pair_displacements")
    return (
        stats.get("moment") == "D"
        and bool(stats.get("d_special_routing"))
        and not bool(stats.get("operator_between_endpoints"))
        and bool(stats.get("same_polarization"))
        and skips > 0
        and skips <= int(stats.get("matched_h0_support_blocks", 0))
        and isinstance(displacements, Mapping)
        and set(map(str, displacements)) == {local_key}
        and int(displacements[local_key]) == skips
        and sum(map(int, displacements.values())) == skips
        and isinstance(candidates, list)
        and len(candidates) == skips
        and all(
            isinstance(candidate, Mapping)
            and candidate.get("unit") == stats.get("unit")
            and candidate.get("moment") == "D"
            and candidate.get("dv") == local
            and candidate.get("expected_local_dv") == local
            and candidate.get("route")
                == "accepted same-polarization analytic one-face certificate"
            for candidate in candidates
        )
        and int(stats.get("crosspol_oneface_fallback_candidate_blocks", 0)) == 0
        and int(stats.get("crosspol_oneface_fallback_matches", 0)) == 0
        and cross_candidates == []
        and cross_displacements == {}
        and cross_audited == {}
        and certificate.get("candidate_matches") == skips
        and certificate.get("registered_analytic_contributions") == 1
        and certificate.get("expected_exact_fraction") == "-13/896"
        and math.isfinite(derived)
        and math.isfinite(error)
        and math.isfinite(computed_error)
        and 0.0 <= error < 5e-13
        and error == computed_error
    )


def _valid_cross_d_route(stats: Mapping[str, Any]) -> bool:
    candidate_displacements = stats.get("crosspol_oneface_fallback_displacements")
    audited_displacements = stats.get("crosspol_oneface_audited_pair_displacements")
    candidates = stats.get("crosspol_oneface_fallback_candidates")
    skip_candidates = stats.get("samepol_oneface_skip_candidates")
    skip_displacements = stats.get("samepol_oneface_skip_displacements")
    try:
        candidate_blocks = int(
            stats.get("crosspol_oneface_fallback_candidate_blocks", 0)
        )
        matches = int(stats.get("crosspol_oneface_fallback_matches", 0))
        pair_tests = int(stats.get("state_pair_tests", 0))
        candidate_keys = {
            ",".join(map(str, map(int, candidate.get("dv", ()))))
            for candidate in candidates
        } if isinstance(candidates, list) else set()
    except (TypeError, ValueError, OverflowError):
        return False
    return (
        stats.get("moment") == "D"
        and bool(stats.get("d_special_routing"))
        and not bool(stats.get("operator_between_endpoints"))
        and not bool(stats.get("same_polarization"))
        and int(stats.get("samepol_oneface_analytic_skips", 0)) == 0
        and skip_candidates == []
        and skip_displacements == {}
        and stats.get("analytic_oneface_route_certificate") is None
        and candidate_blocks > 0
        and candidate_blocks <= int(stats.get("matched_h0_support_blocks", 0))
        and isinstance(candidates, list)
        and len(candidates) == candidate_blocks
        and all(
            isinstance(candidate, Mapping)
            and candidate.get("unit") == stats.get("unit")
            and candidate.get("moment") == "D"
            and candidate.get("bra_polarization_index")
                == stats.get("bra_polarization_index")
            and candidate.get("ket_polarization_index")
                == stats.get("ket_polarization_index")
            and isinstance(candidate.get("dv"), list)
            and len(candidate["dv"]) == 3
            and candidate.get("route") == "cross-polarization general fallback"
            for candidate in candidates
        )
        and isinstance(candidate_displacements, Mapping)
        and all(int(count) > 0 for count in candidate_displacements.values())
        and sum(map(int, candidate_displacements.values())) == candidate_blocks
        and set(map(str, candidate_displacements)) == candidate_keys
        and 0 < matches <= pair_tests
        and isinstance(audited_displacements, Mapping)
        and all(int(count) > 0 for count in audited_displacements.values())
        and sum(map(int, audited_displacements.values())) == matches
        and set(map(str, audited_displacements)).issubset(candidate_keys)
        and _substantive_unit_stats(stats)
    )


def _stage_depth(stage: str) -> int:
    return {"P0": 0, "W1": 1, "R1": 1, "W2": 2, "R2": 2, "R12": 1}[stage]


def _v17_phys_index(LD):
    idx=defaultdict(list)
    for S,st in LD.items():
        for key,v in _v10a3_physical_blocks(st).items(): idx[key].append((S,v))
    return idx


def _unit_key(moment: str, bra_index: int, ket_index: int) -> str:
    return f"{moment}:bra{int(bra_index)}->ket{int(ket_index)}"


def _expected_unit_keys() -> tuple[str, ...]:
    return tuple(
        _unit_key(moment, bra_index, ket_index)
        for moment, *_ in MOMENTS
        for ket_index in range(3)
        for bra_index in range(3)
    )


def census_unit(moment: str, left_name: str, right_name: str, block_origin: str,
                operator_between_endpoints: bool, d_special: bool,
                bra_index: int, ket_index: int, left, right,
                audit: OccurrenceAudit, budget: ResourceBudget,
                stage_contexts: Mapping[int, Mapping[str, Any]]) -> dict[str, Any]:
    """Apply the accepted v24c endpoint scan to one fixed half-history pairing."""
    unit = _unit_key(moment, bra_index, ket_index)
    before_pairs = int(audit.pair_tests.get(unit, 0))
    before_occurrences = sum(audit.by_consumer.get(unit, Counter()).values())
    right_index = _v17_phys_index(right)
    left_items = []
    for left_support, state in left.items():
        for key, left_vector in _v10a3_physical_blocks(state).items():
            left_items.append((left_support, key, left_vector))
    left_items.sort(key=lambda item: len(item[2]))

    matched_blocks = matched_flux = raw_pair_upper = 0
    samepol_oneface_skips = 0
    crosspol_oneface_fallback_candidate_blocks = 0
    crosspol_oneface_fallback_matches = 0
    samepol_skip_displacements: Counter[tuple[int, int, int]] = Counter()
    crosspol_fallback_displacements: Counter[tuple[int, int, int]] = Counter()
    crosspol_audited_displacements: Counter[tuple[int, int, int]] = Counter()
    samepol_skip_candidates: list[dict[str, Any]] = []
    crosspol_fallback_candidates: list[dict[str, Any]] = []
    scan_counts: list[int] = []
    same_polarization = T1_POLS[int(bra_index)] == T1_POLS[int(ket_index)]
    left_root_face = audit.root_faces[int(bra_index)]
    right_root_face = audit.root_faces[int(ket_index)]
    left_root_geometry = faces[int(left_root_face)]
    right_root_geometry = faces[int(right_root_face)]
    analytic_local_displacement = tuple(
        (int(right_root_geometry[0][axis]) - int(left_root_geometry[0][axis])) % L
        for axis in range(3)
    )
    local_pair_tests = 0

    for block_index, (left_support, (signature, energy), left_vector0) in enumerate(left_items, 1):
        ensure_finite(f"{unit}.left_vector", left_vector0)
        scans_for_block = 0
        for displacement_index, dv in enumerate(verts, 1):
            scans_for_block += 1
            translated_signature = _v10a2_sig_canon(_v10a3_translate_sig(signature, dv))
            candidates = right_index.get((translated_signature, energy), ())
            if candidates:
                left_vector = {
                    _v10a3_translate_state(state, dv): float(coefficient)
                    for state, coefficient in left_vector0.items()
                }
                ensure_finite(f"{unit}.translated_left_vector", left_vector)
                translated_support = _v17_translate_support(left_support, dv)
                for right_support, right_vector in candidates:
                    pair_route = "general endpoint route"
                    ensure_finite(f"{unit}.right_vector", right_vector)
                    matched_blocks += 1
                    raw_pair_upper += len(left_vector) * len(right_vector)
                    if d_special and len(left_support) == 1 and len(right_support) == 1:
                        if same_polarization:
                            samepol_oneface_skips += 1
                            samepol_skip_displacements[tuple(map(int, dv))] += 1
                            samepol_skip_candidates.append({
                                "unit": unit,
                                "moment": moment,
                                "bra_polarization_index": int(bra_index),
                                "bra_polarization": list(T1_POLS[int(bra_index)]),
                                "bra_root_face": int(left_root_face),
                                "bra_root_geometry": json_safe(left_root_geometry),
                                "ket_polarization_index": int(ket_index),
                                "ket_polarization": list(T1_POLS[int(ket_index)]),
                                "ket_root_face": int(right_root_face),
                                "ket_root_geometry": json_safe(right_root_geometry),
                                "dv": list(map(int, dv)),
                                "expected_local_dv": list(analytic_local_displacement),
                                "left_anchored_support": _support_json(left_support),
                                "left_translated_support": _support_json(translated_support),
                                "right_support": _support_json(right_support),
                                "h0_signature": repr(translated_signature),
                                "h0_energy": str(energy),
                                "left_state_terms": len(left_vector),
                                "right_state_terms": len(right_vector),
                                "bra_stage": json_safe(stage_contexts[int(bra_index)][left_name]),
                                "ket_stage": json_safe(stage_contexts[int(ket_index)][right_name]),
                                "operator_between_endpoints": False,
                                "route": "accepted same-polarization analytic one-face certificate",
                            })
                            continue
                        crosspol_oneface_fallback_candidate_blocks += 1
                        crosspol_fallback_displacements[tuple(map(int, dv))] += 1
                        pair_route = "cross-polarization general fallback"
                        crosspol_fallback_candidates.append({
                            "unit": unit,
                            "moment": moment,
                            "bra_polarization_index": int(bra_index),
                            "bra_polarization": list(T1_POLS[int(bra_index)]),
                            "bra_root_face": int(left_root_face),
                            "bra_root_geometry": json_safe(left_root_geometry),
                            "ket_polarization_index": int(ket_index),
                            "ket_polarization": list(T1_POLS[int(ket_index)]),
                            "ket_root_face": int(right_root_face),
                            "ket_root_geometry": json_safe(right_root_geometry),
                            "dv": list(map(int, dv)),
                            "left_anchored_support": _support_json(left_support),
                            "left_translated_support": _support_json(translated_support),
                            "right_support": _support_json(right_support),
                            "h0_signature": repr(translated_signature),
                            "h0_energy": str(energy),
                            "left_state_terms": len(left_vector),
                            "right_state_terms": len(right_vector),
                            "bra_stage": json_safe(stage_contexts[int(bra_index)][left_name]),
                            "ket_stage": json_safe(stage_contexts[int(ket_index)][right_name]),
                            "operator_between_endpoints": False,
                            "route": pair_route,
                        })

                    left_flux: dict[Any, list[tuple[LXState, float]]] = defaultdict(list)
                    right_flux: dict[Any, list[tuple[LXState, float]]] = defaultdict(list)
                    for state, coefficient in left_vector.items():
                        left_flux[_v9_flux_key_state(state)].append((state, float(coefficient)))
                    for state, coefficient in right_vector.items():
                        right_flux[_v9_flux_key_state(state)].append((state, float(coefficient)))
                    for flux_key in sorted(set(left_flux) & set(right_flux), key=repr):
                        matched_flux += 1
                        for bra, bra_coefficient in sorted(
                            left_flux[flux_key], key=lambda item: (item[0].occ, item[0].part)
                        ):
                            for ket, ket_coefficient in sorted(
                                right_flux[flux_key], key=lambda item: (item[0].occ, item[0].part)
                            ):
                                local_pair_tests += 1
                                if local_pair_tests > budget.limits.max_pair_tests_per_unit:
                                    raise PreflightFailure(
                                        f"per-unit pair-test ceiling exceeded in {unit}: {local_pair_tests}"
                                    )
                                resolver_context = {
                                    "bra_stage": json_safe(stage_contexts[int(bra_index)][left_name]),
                                    "ket_stage": json_safe(stage_contexts[int(ket_index)][right_name]),
                                    "left_physical_block": {
                                        "block_index": block_index,
                                        "left_blocks": len(left_items),
                                        "anchored_support": _support_json(left_support),
                                        "translated_support": _support_json(translated_support),
                                        "signature": repr(signature),
                                        "translated_signature": repr(translated_signature),
                                        "energy": str(energy),
                                        "state_terms": len(left_vector0),
                                    },
                                    "right_physical_block": {
                                        "support": _support_json(right_support),
                                        "state_terms": len(right_vector),
                                    },
                                }
                                audit.inspect(
                                    bra, ket,
                                    consumer=unit,
                                    budget_label=f"census {unit}",
                                    moment=moment,
                                    bra_polarization_index=bra_index,
                                    ket_polarization_index=ket_index,
                                    dv=dv,
                                    source_stage=right_name,
                                    target_stage=left_name,
                                    source_history_depth=_stage_depth(right_name),
                                    target_history_depth=_stage_depth(left_name),
                                    block_origin=block_origin,
                                    operator_between_endpoints=operator_between_endpoints,
                                    bra_support=translated_support,
                                    ket_support=right_support,
                                    h0_signature=translated_signature,
                                    h0_energy=energy,
                                    flux_key=flux_key,
                                    bra_coefficient=bra_coefficient,
                                    ket_coefficient=ket_coefficient,
                                    resolver_context=resolver_context,
                                    route=pair_route,
                                )
                                if pair_route == "cross-polarization general fallback":
                                    # Count only a state pair that actually passed the
                                    # occurrence audit on the generic route.  Merely
                                    # finding a 1x1 H0 support candidate is not enough.
                                    crosspol_oneface_fallback_matches += 1
                                    crosspol_audited_displacements[tuple(map(int, dv))] += 1
            if displacement_index % 25 == 0:
                budget.check(
                    f"census {unit}", current=(block_index - 1) * len(verts) + displacement_index,
                    total=max(1, len(left_items) * len(verts)),
                )
        scan_counts.append(scans_for_block)
        if scans_for_block != len(verts):
            raise PreflightFailure(
                f"incomplete translation scan in {unit} block {block_index}: {scans_for_block}"
            )

    analytic_route_certificate = None
    if d_special and same_polarization and samepol_oneface_skips:
        escaped = set(samepol_skip_displacements) - {analytic_local_displacement}
        if escaped:
            raise PreflightFailure(
                f"{unit}: same-polarization one-face matches escaped local displacement: "
                f"{dict(samepol_skip_displacements)}"
            )
        oneface_d = float(_v10a11_oneface_axial_character()["D"])
        ensure_finite(f"{unit}.oneface_D", oneface_d)
        oneface_error = float(abs(oneface_d + 13.0 / 896.0))
        ensure_finite(f"{unit}.oneface_D_error", oneface_error)
        if not 0.0 <= oneface_error < 5e-13:
            raise PreflightFailure(
                f"{unit}: one-face analytic certificate mismatch: {oneface_d}"
            )
        analytic_route_certificate = {
            "derivation": "accepted exact one-plaquette character construction",
            "derived_value": oneface_d,
            "expected_exact_fraction": "-13/896",
            "absolute_error": oneface_error,
            "local_displacement": list(analytic_local_displacement),
            "candidate_matches": samepol_oneface_skips,
            "registered_analytic_contributions": 1,
            "is_endpoint_census_certificate_not_final_output": True,
        }
    if d_special and not same_polarization and samepol_oneface_skips:
        raise PreflightFailure(f"{unit}: cross-polarization match entered analytic shortcut")

    result = {
        "unit": unit,
        "moment": moment,
        "bra_polarization_index": int(bra_index),
        "bra_polarization": list(T1_POLS[int(bra_index)]),
        "ket_polarization_index": int(ket_index),
        "ket_polarization": list(T1_POLS[int(ket_index)]),
        "left_blocks": len(left_items),
        "left_block_scan_counts": scan_counts,
        "translation_signature_tests": int(sum(scan_counts)),
        "expected_translation_signature_tests": int(len(left_items) * len(verts)),
        "matched_h0_support_blocks": matched_blocks,
        "raw_pair_upper": raw_pair_upper,
        "matched_flux_groups": matched_flux,
        "state_pair_tests": int(audit.pair_tests.get(unit, 0)) - before_pairs,
        "local_occurrences": sum(audit.by_consumer.get(unit, Counter()).values()) - before_occurrences,
        "same_polarization": same_polarization,
        "samepol_oneface_analytic_skips": samepol_oneface_skips,
        "samepol_oneface_skip_displacements": {
            ",".join(map(str, dv)): int(count)
            for dv, count in sorted(samepol_skip_displacements.items())
        },
        "samepol_oneface_skip_candidates": samepol_skip_candidates,
        "analytic_oneface_route_certificate": analytic_route_certificate,
        "crosspol_oneface_fallback_candidate_blocks":
            crosspol_oneface_fallback_candidate_blocks,
        "crosspol_oneface_fallback_matches": crosspol_oneface_fallback_matches,
        "crosspol_oneface_fallback_displacements": {
            ",".join(map(str, dv)): int(count)
            for dv, count in sorted(crosspol_fallback_displacements.items())
        },
        "crosspol_oneface_audited_pair_displacements": {
            ",".join(map(str, dv)): int(count)
            for dv, count in sorted(crosspol_audited_displacements.items())
        },
        "crosspol_oneface_fallback_candidates": crosspol_fallback_candidates,
        "operator_between_endpoints": bool(operator_between_endpoints),
        "block_origin": block_origin,
        "d_special_routing": bool(d_special),
    }
    ensure_finite(f"{unit}.stats", result)
    budget.check(f"census {unit}", current=len(left_items), total=len(left_items), force_heartbeat=True)
    return result


def state_stats(LD) -> dict[str, int]:
    ensure_finite("state_coefficients", LD)
    aggregate = _v17_aggregate(LD)
    result = {
        "supports": len(LD),
        "signature_blocks": len(aggregate),
        "network_terms": sum(len(vector) for vector in aggregate.values()),
    }
    ensure_finite("state_stats", result)
    return result


def _strict_json_load(path: Path) -> Any:
    def reject_constant(token: str):
        raise PreflightFailure(f"non-finite JSON constant {token!r} in {path}")
    def reject_duplicate_keys(pairs: Sequence[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise PreflightFailure(f"duplicate JSON key {key!r} in {path}")
            result[key] = value
        return result
    return json.loads(
        path.read_text(encoding="utf-8"),
        parse_constant=reject_constant,
        object_pairs_hook=reject_duplicate_keys,
    )


def _serialized_json_bytes(payload: Mapping[str, Any]) -> bytes:
    ensure_finite("json_serialization", payload)
    text = json.dumps(json_safe(payload), indent=2, sort_keys=True,
                      ensure_ascii=True, allow_nan=False)
    return (text + "\n").encode("utf-8")


def atomic_write_json(path: Path, payload: Mapping[str, Any], *,
                      max_bytes: int | None = None) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    encoded = _serialized_json_bytes(payload)
    if max_bytes is not None and len(encoded) > int(max_bytes):
        raise PreflightFailure(
            f"JSON payload ceiling exceeded for {path}: {len(encoded)} > {int(max_bytes)} bytes"
        )
    temporary.write_bytes(encoded)
    os.replace(temporary, path)
    return len(encoded)


class CheckpointStore:
    def __init__(self, path: Path, binding: Mapping[str, Any], *, resume: bool,
                 max_file_bytes: int | None = None) -> None:
        self.path = path.resolve()
        self.binding = json_safe(binding)
        self.resume_requested = bool(resume)
        self.existed_at_open = self.path.exists()
        self.max_file_bytes = max_file_bytes
        self.document: dict[str, Any]
        if self.path.exists():
            if not resume:
                raise PreflightFailure(
                    f"checkpoint already exists; pass --resume or choose another path: {self.path}"
                )
            loaded = _strict_json_load(self.path)
            if not isinstance(loaded, dict) or loaded.get("schema") != CHECKPOINT_SCHEMA:
                raise PreflightFailure("checkpoint schema mismatch")
            if canonical_json(loaded.get("binding")) != canonical_json(self.binding):
                raise PreflightFailure("checkpoint binding mismatch; stale work cannot be resumed")
            if not isinstance(loaded.get("units"), dict):
                raise PreflightFailure("checkpoint units ledger is malformed")
            if not isinstance(loaded.get("unit_order"), list):
                raise PreflightFailure("checkpoint ordered unit ledger is malformed")
            if len(loaded["unit_order"]) != len(set(loaded["unit_order"])):
                raise PreflightFailure("checkpoint ordered unit ledger contains duplicates")
            if set(loaded["unit_order"]) != set(loaded["units"]):
                raise PreflightFailure("checkpoint unit keys and ordered ledger disagree")
            ensure_finite("checkpoint", loaded)
            self._verify_chain(loaded)
            self.document = loaded
        else:
            self.document = {
                "schema": CHECKPOINT_SCHEMA,
                "binding": self.binding,
                "unit_order": [],
                "units": {},
                "chain_head_sha256": None,
            }
            atomic_write_json(self.path, self.document, max_bytes=self.max_file_bytes)
        self.initial_units = tuple(self.document["unit_order"])

    @staticmethod
    def _record_digest(record: Mapping[str, Any]) -> str:
        body = {
            "previous_record_sha256": record.get("previous_record_sha256"),
            "unit": record.get("unit"),
            "stats": record.get("stats"),
            "audit": record.get("audit"),
        }
        return sha256_text(canonical_json(body))

    @classmethod
    def _verify_chain(cls, document: Mapping[str, Any]) -> None:
        previous = None
        for unit in document["unit_order"]:
            record = document["units"].get(unit)
            if not isinstance(record, Mapping):
                raise PreflightFailure(f"checkpoint record missing for {unit}")
            if record.get("unit") != unit:
                raise PreflightFailure(f"checkpoint record unit mismatch for {unit}")
            if record.get("previous_record_sha256") != previous:
                raise PreflightFailure(f"checkpoint hash chain predecessor mismatch for {unit}")
            actual = cls._record_digest(record)
            if record.get("record_sha256") != actual:
                raise PreflightFailure(f"checkpoint record digest mismatch for {unit}")
            previous = actual
        if document.get("chain_head_sha256") != previous:
            raise PreflightFailure("checkpoint hash chain head mismatch")

    def completed_units(self) -> tuple[str, ...]:
        return tuple(self.document["unit_order"])

    def get(self, unit: str, *, expected: Mapping[str, Any]) -> Mapping[str, Any] | None:
        value = self.document["units"].get(unit)
        if value is not None:
            ensure_finite(f"checkpoint.unit.{unit}", value)
            if value.get("record_sha256") != self._record_digest(value):
                raise PreflightFailure(f"checkpoint record digest mismatch for {unit}")
            stats = value.get("stats")
            audit = value.get("audit")
            if not isinstance(stats, Mapping) or not isinstance(audit, Mapping):
                raise PreflightFailure(f"checkpoint record payload malformed for {unit}")
            required_stats = {
                "unit": unit,
                "moment": expected["moment"],
                "bra_polarization_index": int(expected["bra_polarization_index"]),
                "bra_polarization": list(T1_POLS[int(expected["bra_polarization_index"])]),
                "ket_polarization_index": int(expected["ket_polarization_index"]),
                "ket_polarization": list(T1_POLS[int(expected["ket_polarization_index"])]),
                "same_polarization": bool(expected["same_polarization"]),
                "d_special_routing": bool(expected["d_special_routing"]),
                "block_origin": expected["block_origin"],
                "operator_between_endpoints": bool(expected["operator_between_endpoints"]),
            }
            for key, required in required_stats.items():
                if stats.get(key) != required:
                    raise PreflightFailure(
                        f"checkpoint {unit} metadata mismatch for {key}: "
                        f"{stats.get(key)!r} != {required!r}"
                    )
            if audit.get("schema") != UNIT_AUDIT_SCHEMA or audit.get("consumer") != unit:
                raise PreflightFailure(f"checkpoint audit identity mismatch for {unit}")
            audit_counts = _parse_counts(audit.get("all_occurrences", {}), unit)
            if int(stats.get("state_pair_tests", -1)) != int(audit.get("pair_tests", -2)):
                raise PreflightFailure(f"checkpoint pair-test cross-field mismatch for {unit}")
            if int(stats.get("local_occurrences", -1)) != sum(audit_counts.values()):
                raise PreflightFailure(f"checkpoint occurrence cross-field mismatch for {unit}")
            pair_tests = int(stats.get("state_pair_tests", -1))
            occurrence_total = int(stats.get("local_occurrences", -1))
            matched_flux = int(stats.get("matched_flux_groups", -1))
            matched_h0 = int(stats.get("matched_h0_support_blocks", -1))
            raw_pair_upper = int(stats.get("raw_pair_upper", -1))
            if (pair_tests < 0 or occurrence_total < 0 or matched_flux < 0
                    or matched_h0 < 0 or raw_pair_upper < 0
                    or (pair_tests == 0) != (occurrence_total == 0)
                    or occurrence_total < pair_tests
                    or (pair_tests == 0) != (matched_flux == 0)
                    or (pair_tests > 0 and matched_h0 == 0)
                    or raw_pair_upper < pair_tests):
                raise PreflightFailure(f"checkpoint substantive-work ledger mismatch for {unit}")
            if (_nonvacuity_expected(
                    str(expected["moment"]),
                    int(expected["bra_polarization_index"]),
                    int(expected["ket_polarization_index"]),
                ) and not _substantive_unit_stats(stats)):
                raise PreflightFailure(f"checkpoint required unit is vacuous: {unit}")
            _validate_representatives(audit.get("representatives", {}), audit_counts, unit)
            scan_counts = stats.get("left_block_scan_counts")
            expected_translation_tests = int(
                stats.get("expected_translation_signature_tests", -1)
            )
            if (not isinstance(scan_counts, list)
                    or len(scan_counts) != int(stats.get("left_blocks", -1))
                    or any(int(count) != len(verts) for count in scan_counts)
                    or int(stats.get("translation_signature_tests", -1))
                       != int(stats.get("left_blocks", -1)) * len(verts)
                    or expected_translation_tests
                       != int(stats.get("translation_signature_tests", -1))):
                raise PreflightFailure(f"checkpoint translation ledger mismatch for {unit}")
            skip_count = int(stats.get("samepol_oneface_analytic_skips", -1))
            skip_displacements = stats.get("samepol_oneface_skip_displacements")
            skip_candidates = stats.get("samepol_oneface_skip_candidates")
            analytic_certificate = stats.get("analytic_oneface_route_certificate")
            cross_candidate_blocks = int(
                stats.get("crosspol_oneface_fallback_candidate_blocks", -1)
            )
            cross_count = int(stats.get("crosspol_oneface_fallback_matches", -1))
            cross_displacements = stats.get("crosspol_oneface_fallback_displacements")
            cross_candidates = stats.get("crosspol_oneface_fallback_candidates")
            cross_audited_displacements = stats.get(
                "crosspol_oneface_audited_pair_displacements"
            )
            if (not isinstance(skip_displacements, Mapping)
                    or not isinstance(skip_candidates, list)
                    or len(skip_candidates) != skip_count):
                raise PreflightFailure(f"checkpoint one-face provenance count mismatch for {unit}")
            if (cross_candidate_blocks < 0
                    or not isinstance(cross_displacements, Mapping)
                    or not isinstance(cross_candidates, list)
                    or len(cross_candidates) != cross_candidate_blocks):
                raise PreflightFailure(f"checkpoint cross-fallback provenance count mismatch for {unit}")
            if (not isinstance(cross_audited_displacements, Mapping)
                    or any(int(count) <= 0 for count in cross_audited_displacements.values())
                    or sum(map(int, cross_audited_displacements.values())) != cross_count):
                raise PreflightFailure(f"checkpoint audited cross-fallback ledger mismatch for {unit}")
            if bool(expected["d_special_routing"]):
                if bool(expected["same_polarization"]):
                    if not _valid_same_d_route(stats):
                        raise PreflightFailure(f"checkpoint same-pol D route mismatch for {unit}")
                elif not _valid_cross_d_route(stats):
                    raise PreflightFailure(f"checkpoint cross-pol D route mismatch for {unit}")
            elif (skip_count != 0 or cross_candidate_blocks != 0 or cross_count != 0
                  or analytic_certificate is not None or cross_candidates
                  or skip_displacements or cross_displacements
                  or cross_audited_displacements):
                raise PreflightFailure(f"checkpoint non-D unit contains D routing metadata for {unit}")
            for candidate in skip_candidates:
                if (candidate.get("unit") != unit
                        or candidate.get("moment") != expected["moment"]
                        or candidate.get("bra_polarization_index")
                           != int(expected["bra_polarization_index"])
                        or candidate.get("ket_polarization_index")
                           != int(expected["ket_polarization_index"])):
                    raise PreflightFailure(f"checkpoint one-face provenance mismatch for {unit}")
                if (isinstance(analytic_certificate, Mapping)
                        and candidate.get("dv")
                           != analytic_certificate.get("local_displacement")):
                    raise PreflightFailure(f"checkpoint one-face locality mismatch for {unit}")
            for candidate in cross_candidates:
                if (candidate.get("unit") != unit
                        or candidate.get("moment") != expected["moment"]
                        or candidate.get("bra_polarization_index")
                           != int(expected["bra_polarization_index"])
                        or candidate.get("ket_polarization_index")
                           != int(expected["ket_polarization_index"])
                        or candidate.get("route")
                           != "cross-polarization general fallback"):
                    raise PreflightFailure(f"checkpoint cross-fallback provenance mismatch for {unit}")
        return value

    def put(self, unit: str, stats: Mapping[str, Any], audit: Mapping[str, Any]) -> None:
        if unit in self.document["units"]:
            raise PreflightFailure(f"checkpoint unit already exists: {unit}")
        record = {
            "previous_record_sha256": self.document["chain_head_sha256"],
            "unit": unit,
            "stats": json_safe(stats),
            "audit": json_safe(audit),
        }
        record["record_sha256"] = self._record_digest(record)
        ensure_finite(f"checkpoint.unit.{unit}", record)
        self.document["units"][unit] = record
        self.document["unit_order"].append(unit)
        self.document["chain_head_sha256"] = record["record_sha256"]
        atomic_write_json(self.path, self.document, max_bytes=self.max_file_bytes)


def environment_info() -> dict[str, Any]:
    packages = {}
    for name in ("numpy", "scipy", "sympy", "opt_einsum", "psutil"):
        try:
            packages[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            packages[name] = "not-installed"
    result = {
        "python": platform.python_version(),
        "python_implementation": platform.python_implementation(),
        "platform": platform.platform(),
        "machine": platform.machine(),
        "byteorder": sys.byteorder,
        "packages": packages,
    }
    ensure_finite("environment", result)
    return result


def negative_controls(root_faces: Sequence[int]) -> dict[str, Any]:
    """Use poison callbacks to prove both failures happen before downstream work."""
    poison_calls = {"contractor": 0, "magnetic_engine": 0}

    def poison_contractor(_a, _b):
        poison_calls["contractor"] += 1
        raise AssertionError("poison contractor was called")

    def poison_engine(_state, _label):
        poison_calls["magnetic_engine"] += 1
        raise AssertionError("poison magnetic engine was called")

    root_face = int(root_faces[0])
    link = int(np.flatnonzero(B2[:, root_face])[0])
    bra = LXState(((link, False),) * 2, tuple(range(4)))
    ket = LXState(((link, False),) * 5, tuple(range(10)))
    occurrence_audit = OccurrenceAudit(root_faces)
    poisoned_haar = GuardedHaar(poison_contractor, occurrence_audit)
    try:
        with occurrence_audit.context(
            consumer="negative-occurrence-control",
            moment="negative-control",
            bra_polarization_index=0,
            ket_polarization_index=0,
            dv=(0, 0, 0),
            source_stage="forbidden-depth-two-source",
            target_stage="forbidden-depth-two-target",
            source_history_depth=2,
            target_history_depth=2,
            block_origin="negative-control",
            operator_between_endpoints=True,
            h0_signature="negative-control",
            h0_energy=Fraction(1),
            flux_key=((link, 1),),
            resolver_context={"control": "forbidden (2,5)/(5,2)"},
        ):
            poisoned_haar(bra, ket)
    except OccurrenceViolation as exc:
        occurrence_message = str(exc)
    else:
        raise PreflightFailure("negative occurrence poison control did not fail")

    schedule_audit = OccurrenceAudit(root_faces)
    schedule = MagneticSchedule(schedule_audit, 0, engine=poison_engine)
    try:
        schedule.apply(
            {}, source_stage="forbidden-depth-two-source",
            target_stage="forbidden-third-magnetic-action",
            source_history_depth=2,
            direct_blocks=("22",),
        )
    except ScheduleViolation as exc:
        schedule_message = str(exc)
    else:
        raise PreflightFailure("negative schedule poison control did not fail")

    result = {
        "occurrence_failure": json.loads(occurrence_message),
        "schedule_failure": json.loads(schedule_message),
        "poison_calls": poison_calls,
    }
    ensure_finite("negative_controls", result)
    return result


def _anchor_faces() -> tuple[int, int, int]:
    return tuple(
        next(face for face, (vertex, a, b) in enumerate(faces)
             if vertex == (0, 0, 0) and (a, b) == polarization)
        for polarization in T1_POLS
    )


def _root_orbit_report(root_faces: Sequence[int]) -> dict[str, Any]:
    rows = []
    union: set[int] = set()
    for index, root_face in enumerate(root_faces):
        orbit = {
            int(next(iter(_v17_translate_support(frozenset((int(root_face),)), dv))))
            for dv in verts
        }
        expected = {face for face, (_, a, b) in enumerate(faces)
                    if (a, b) == T1_POLS[index]}
        rows.append({
            "polarization_index": index,
            "polarization": list(T1_POLS[index]),
            "root_face": int(root_face),
            "orbit_size": len(orbit),
            "expected_same_polarization_faces": len(expected),
            "orbit_equals_same_polarization_faces": orbit == expected,
        })
        union.update(orbit)
    return {"roots": rows, "union_size": len(union), "expected_union_size": P}


def _config_payload(limits: OperationalLimits) -> dict[str, Any]:
    return {
        "schema": SCHEMA,
        "requested_order": REQUESTED_ORDER,
        "lattice_size": L,
        "t1_polarizations": T1_POLS,
        "moments": MOMENTS,
        "nonvacuity_matrix": NONVACUITY_MATRIX,
        "nonvacuity_evidence": NONVACUITY_EVIDENCE,
        "structural_zero_justifications": STRUCTURAL_ZERO_JUSTIFICATIONS,
        "allowed_blocks": ALLOWED_BLOCKS,
        "forbidden_blocks": FORBIDDEN_BLOCKS,
        "limits": asdict(limits),
    }


def _static_scope_policy_report(script_text: str) -> dict[str, Any]:
    prohibited = (
        "gel" + "fand", "factor" + "52", "ha" + "mer",
        "local" + "_shift", "un" + "blind", "m4" + "_oracle",
        "v23c" + "_fit_cluster",
    )
    found = [token for token in prohibited if token in script_text.lower()]
    return {
        "method": "static substring scope scan; not a proof of semantic absence",
        "searched_tokens_sha256": sha256_text(canonical_json(prohibited)),
        "found": found,
    }


def run_root_preflight(*, limits: OperationalLimits, checkpoint_path: Path,
                       resume: bool, notebook_expected_script_sha: str | None = None) -> dict[str, Any]:
    global _ACTIVE_BUDGET
    gates = GateBook()
    budget = ResourceBudget(limits)
    _ACTIVE_BUDGET = budget
    script_path = Path(__file__).resolve()
    script_sha = sha256_file(script_path)
    if notebook_expected_script_sha is not None:
        notebook_expected_script_sha = notebook_expected_script_sha.upper()
        if notebook_expected_script_sha != script_sha:
            raise PreflightFailure(
                f"notebook/script hash mismatch: expected {notebook_expected_script_sha}, got {script_sha}"
            )
    authority_path = script_path.parent / SOURCE_LOCATORS["authority"]
    authority_runtime_status = "not-present-in-uploaded-Colab-bundle"
    if authority_path.is_file():
        authority_actual = sha256_file(authority_path)
        if authority_actual != SOURCE_LOCATORS["authority_sha256"]:
            raise PreflightFailure(
                f"authority source hash mismatch: {authority_actual}"
            )
        authority_runtime_status = "verified"

    environment = environment_info()
    environment_hash = sha256_text(canonical_json(environment))
    config = _config_payload(limits)
    config_hash = sha256_text(canonical_json(config))
    reference_hash = sha256_text(canonical_json(EXECUTED_V10A2_REFERENCE))
    binding = {
        "script_sha256": script_sha,
        "config_sha256": config_hash,
        "authority_sha256": SOURCE_LOCATORS["authority_sha256"],
        "authority_runtime_status": authority_runtime_status,
        "environment_sha256": environment_hash,
        "executed_v10a2_reference_sha256": reference_hash,
    }
    checkpoint = CheckpointStore(
        checkpoint_path, binding, resume=resume,
        max_file_bytes=limits.max_payload_bytes,
    )
    expected_units = _expected_unit_keys()
    checkpoint_prefix = checkpoint.completed_units()
    if checkpoint_prefix != expected_units[:len(checkpoint_prefix)]:
        raise PreflightFailure(
            "checkpoint unit_order is not an exact prefix of the fixed 63-unit manifest"
        )
    resumed_units = list(checkpoint_prefix)
    fresh_units: list[str] = []
    roots = _anchor_faces()
    root_orbits = _root_orbit_report(roots)
    audit = OccurrenceAudit(roots, budget)

    print(f"[preflight] L={L}; roots={[(root, faces[root]) for root in roots]}", flush=True)
    print("[preflight] fail-closed poison controls", flush=True)
    negative = negative_controls(roots)
    gates.require(
        "negative occurrence poison callback remains untouched",
        negative["poison_calls"]["contractor"] == 0
        and negative["occurrence_failure"]["contractor_called"] is False,
        negative,
    )
    gates.require(
        "negative schedule poison callback remains untouched",
        negative["poison_calls"]["magnetic_engine"] == 0
        and negative["schedule_failure"]["contractor_called"] is False,
        negative,
    )

    print("[preflight] installing accepted extended Haar contractor", flush=True)
    raw_haar, supported, haar_certificate, _ = _v10a2_install_q2_haar(globals())
    ensure_finite("haar_certificate", haar_certificate)
    manifest_domain = {
        tuple(map(int, value))
        for value in EXECUTED_V10A2_REFERENCE["center_neutral_occurrences"]
    }
    gates.require(
        "contractor domain is bound to the executed v10a2 reference manifest",
        reference_hash == EXECUTED_V10A2_REFERENCE_SHA256
        and frozenset(supported) == BASELINE_CENTER_NEUTRAL
        and manifest_domain == BASELINE_CENTER_NEUTRAL,
        {
            "reference_sha256": reference_hash,
            "notebook_sha256": EXECUTED_V10A2_REFERENCE["notebook_sha256"],
            "code_cell_sha256": EXECUTED_V10A2_REFERENCE["code_cell_sha256"],
            "domain": sorted(supported),
            "purpose": "contractor-domain provenance; historical counts are not replay targets",
        },
    )
    gates.require("all Haar diagnostics are finite", True, haar_certificate)
    gates.require(
        "balanced rank-three inverse certificate",
        float(haar_certificate["wg3_inverse_error"]) < 5e-13,
        haar_certificate["wg3_inverse_error"],
    )
    gates.require(
        "pure-six singlet rank certificate",
        int(haar_certificate["rank60"]) == 5,
        haar_certificate["rank60"],
    )
    gates.require(
        "pure-six projector trace equals five",
        abs(float(haar_certificate["T60_trace"]) - 5.0) < 5e-12,
        haar_certificate["T60_trace"],
    )
    gates.require(
        "pure-six projector is symmetric",
        float(haar_certificate["T60_symmetry_error"]) < 5e-13,
        haar_certificate["T60_symmetry_error"],
    )
    gates.require(
        "pure-six projector is idempotent",
        float(haar_certificate["T60_idempotence_error"]) < 5e-13,
        haar_certificate["T60_idempotence_error"],
    )
    qhaar = GuardedHaar(raw_haar, audit)

    stages: dict[int, dict[str, Any]] = {}
    stage_contexts: dict[int, dict[str, Any]] = {}
    transition_stats: dict[int, dict[str, Any]] = {}
    schedules: list[MagneticSchedule] = []
    for polarization_index, root_face in enumerate(roots):
        print(
            f"[history] polarization {polarization_index} {T1_POLS[polarization_index]} "
            f"root={root_face}", flush=True,
        )
        schedule = MagneticSchedule(audit, polarization_index)
        schedules.append(schedule)
        P0 = {frozenset((root_face,)): _v10a3_face_state(root_face)}
        W1, w1_stats = schedule.apply(
            P0, source_stage="P0", target_stage="W1", source_history_depth=0,
            direct_blocks=("PP", "1P"),
        )
        R1, r1_stats = _resolvent_labeled(
            W1, qhaar, "R1", polarization_index, root_face, budget,
        )
        W2, w2_stats = schedule.apply(
            R1, source_stage="R1", target_stage="W2", source_history_depth=1,
            direct_blocks=("P1", "11", "21"),
        )
        R2, r2_stats = _resolvent_labeled(
            W2, qhaar, "R2", polarization_index, root_face, budget,
        )
        R12, r12_stats = _resolvent_labeled(
            R1, qhaar, "R12", polarization_index, root_face, budget,
        )
        stage = {"P0": P0, "W1": W1, "R1": R1, "W2": W2, "R2": R2, "R12": R12}
        stage_stats = {name: state_stats(value) for name, value in stage.items()}
        stages[polarization_index] = stage
        transition_stats[polarization_index] = {
            "W1": w1_stats, "R1": r1_stats, "W2": w2_stats,
            "R2": r2_stats, "R12": r12_stats,
        }
        stage_contexts[polarization_index] = {
            "P0": {"history_depth": 0, "state": stage_stats["P0"]},
            "W1": {"history_depth": 1, "state": stage_stats["W1"], "transition": w1_stats},
            "R1": {"history_depth": 1, "state": stage_stats["R1"], "resolvent": r1_stats},
            "W2": {"history_depth": 2, "state": stage_stats["W2"], "transition": w2_stats},
            "R2": {"history_depth": 2, "state": stage_stats["R2"], "resolvent": r2_stats},
            "R12": {"history_depth": 1, "state": stage_stats["R12"], "resolvent": r12_stats},
        }

    gates.require(
        "all three full-T1 root histories are constructed",
        set(stages) == {0, 1, 2}
        and roots == (2, 1, 0)
        and all(row["orbit_size"] == 125
                and row["orbit_equals_same_polarization_faces"]
                for row in root_orbits["roots"])
        and root_orbits["union_size"] == P,
        root_orbits,
    )
    gates.require(
        "each root history has exactly two sealed magnetic applications",
        all(schedule.step == 2 for schedule in schedules)
        and len(audit.action_log) == 6
        and all(
            [row["source_stage"] for row in audit.action_log
             if row["polarization_index"] == index] == ["P0", "R1"]
            for index in range(3)
        ),
        audit.action_log,
    )
    all_w_stats = [transition_stats[index][name]
                   for index in range(3) for name in ("W1", "W2")]
    ensure_finite("all_w_stats", all_w_stats)
    gates.require(
        "all magnetic transition statistics satisfy operational bounds",
        all(
            int(stats["actions"]) <= limits.max_w_actions_per_call
            and int(stats["channels"]) <= limits.max_w_channels_per_call
            and int(stats["supports"]) <= limits.max_supports_per_stage
            for stats in all_w_stats
        ),
        all_w_stats,
    )
    all_resolvent_stats = [transition_stats[index][name]
                           for index in range(3) for name in ("R1", "R2", "R12")]
    residual_max = finite_max(
        "all_resolvent_residual_max",
        (stats["E0_residual_norm2_max"] for stats in all_resolvent_stats),
    )
    gates.require(
        "all reduced resolvents are finite and free of retained-energy poles",
        residual_max < TOL_NORM,
        {"max": residual_max, "stats": all_resolvent_stats},
    )

    moment_report: dict[str, dict[str, Any]] = {moment[0]: {} for moment in MOMENTS}
    for moment, left_name, right_name, block_origin, has_operator, d_special in MOMENTS:
        if not set(MOMENT_BLOCK_COMPONENTS[moment]).issubset(ALLOWED_BLOCKS):
            raise ScheduleViolation(f"moment block policy escaped allowed set: {moment}")
        for ket_index in range(3):
            print(
                f"[census] {moment}; ket polarization {ket_index} {T1_POLS[ket_index]}",
                flush=True,
            )
            for bra_index in range(3):
                unit = _unit_key(moment, bra_index, ket_index)
                expected_record = {
                    "moment": moment,
                    "bra_polarization_index": bra_index,
                    "ket_polarization_index": ket_index,
                    "same_polarization": bra_index == ket_index,
                    "d_special_routing": d_special,
                    "block_origin": block_origin,
                    "operator_between_endpoints": has_operator,
                }
                stored = checkpoint.get(unit, expected=expected_record)
                if stored is not None:
                    if stored.get("unit") != unit:
                        raise PreflightFailure(f"checkpoint unit key mismatch for {unit}")
                    stats = dict(stored["stats"])
                    if stats.get("unit") != unit:
                        raise PreflightFailure(f"checkpoint statistics mismatch for {unit}")
                    if int(stats["state_pair_tests"]) > limits.max_pair_tests_per_unit:
                        raise PreflightFailure(
                            f"resumed unit exceeds per-unit pair-test ceiling: {unit}"
                        )
                    audit.merge_unit(stored["audit"])
                    print(f"[checkpoint] resumed {unit}", flush=True)
                else:
                    stats = census_unit(
                        moment, left_name, right_name, block_origin,
                        has_operator, d_special, bra_index, ket_index,
                        stages[bra_index][left_name], stages[ket_index][right_name],
                        audit, budget, stage_contexts,
                    )
                    checkpoint.put(unit, stats, audit.unit_payload(unit))
                    checkpoint.get(unit, expected=expected_record)
                    fresh_units.append(unit)
                ensure_finite(f"moment_report.{unit}", stats)
                moment_report[moment][unit] = stats

    actual_units = tuple(
        unit for moment, *_ in MOMENTS
        for ket_index in range(3)
        for bra_index in range(3)
        for unit in (_unit_key(moment, bra_index, ket_index),)
        if unit in moment_report[moment]
    )
    all_unit_stats = [moment_report[moment][unit]
                      for moment, *_ in MOMENTS
                      for ket_index in range(3)
                      for bra_index in range(3)
                      for unit in (_unit_key(moment, bra_index, ket_index),)]
    unit_nonvacuity = {}
    for stats in all_unit_stats:
        moment = str(stats["moment"])
        bra_index = int(stats["bra_polarization_index"])
        ket_index = int(stats["ket_polarization_index"])
        expected_work = _nonvacuity_expected(moment, bra_index, ket_index)
        substantive = _substantive_unit_stats(stats)
        exception = None
        if not expected_work:
            exception = (
                STRUCTURAL_ZERO_JUSTIFICATIONS["sigma3:all-polarizations"]
                if moment == "sigma3" else
                STRUCTURAL_ZERO_JUSTIFICATIONS["e1:cross-polarization"]
            )
        unit_nonvacuity[str(stats["unit"])] = {
            "substantive_required": expected_work,
            "substantive_observed": substantive,
            "valid": substantive if expected_work else True,
            "structural_zero_exception": exception,
            "matched_h0_support_blocks": int(stats["matched_h0_support_blocks"]),
            "matched_flux_groups": int(stats["matched_flux_groups"]),
            "state_pair_tests": int(stats["state_pair_tests"]),
            "local_occurrences": int(stats["local_occurrences"]),
        }
    gates.require(
        "all 63 full-T1 census units are complete and substantive where required",
        actual_units == expected_units and len(set(actual_units)) == 63
        and all(row["valid"] for row in unit_nonvacuity.values()),
        {
            "expected": list(expected_units),
            "actual": list(actual_units),
            "matrix_indexing": "NONVACUITY_MATRIX[moment][ket][bra]",
            "matrix": NONVACUITY_MATRIX,
            "accepted_v24c_evidence": NONVACUITY_EVIDENCE,
            "units": unit_nonvacuity,
        },
    )
    gates.require(
        "every left H0 block scans exactly 125 translations",
        all(
            int(stats["left_blocks"]) > 0
            and len(stats["left_block_scan_counts"]) == int(stats["left_blocks"])
            and all(int(count) == 125 for count in stats["left_block_scan_counts"])
            and int(stats["translation_signature_tests"])
                == int(stats["left_blocks"]) * 125
                == int(stats["expected_translation_signature_tests"])
            for stats in all_unit_stats
        ),
        {
            stats["unit"]: {
                "left_blocks": stats["left_blocks"],
                "translation_signature_tests": stats["translation_signature_tests"],
            } for stats in all_unit_stats
        },
    )
    ordered_pairs = {(stats["bra_polarization_index"], stats["ket_polarization_index"])
                     for stats in all_unit_stats}
    gates.require(
        "all ordered 3x3 polarization pairs are covered for every moment",
        ordered_pairs == {(bra, ket) for ket in range(3) for bra in range(3)}
        and all(
            {(stats["bra_polarization_index"], stats["ket_polarization_index"])
             for stats in moment_report[moment].values()}
            == {(bra, ket) for ket in range(3) for bra in range(3)}
            for moment, *_ in MOMENTS
        ),
        sorted(ordered_pairs),
    )
    d_stats = list(moment_report["D"].values())
    cross_d = [stats for stats in d_stats if not stats["same_polarization"]]
    same_d = [stats for stats in d_stats if stats["same_polarization"]]
    gates.require(
        "D same-polarization analytic and all cross-polarization generic routes are exact",
        len(cross_d) == 6 and len(same_d) == 3
        and all(_valid_cross_d_route(stats) for stats in cross_d)
        and all(_valid_same_d_route(stats) for stats in same_d),
        {
            "cross_pairs": {
                stats["unit"]: {
                    "candidate_blocks": stats["crosspol_oneface_fallback_candidate_blocks"],
                    "audited_generic_pairs": stats["crosspol_oneface_fallback_matches"],
                    "valid": _valid_cross_d_route(stats),
                }
                for stats in cross_d
            },
            "same_pairs": {
                stats["unit"]: {
                    "skips": stats["samepol_oneface_analytic_skips"],
                    "certificate": stats["analytic_oneface_route_certificate"],
                    "valid": _valid_same_d_route(stats),
                }
                for stats in same_d
            },
        },
    )
    gates.require(
        "observed center-neutral occurrences are contained in the executed corpus",
        set(audit.center_neutral_counts).issubset(BASELINE_CENTER_NEUTRAL),
        sorted(audit.center_neutral_counts),
    )
    gates.require(
        "forbidden seven-factor occurrences are absent",
        set(audit.all_counts).isdisjoint(FORBIDDEN_OCCURRENCES),
        sorted(audit.all_counts),
    )
    maximum_occurrence = max((sum(pattern) for pattern in audit.all_counts), default=0)
    gates.require(
        "all local occurrences have at most six factors",
        maximum_occurrence <= 6,
        maximum_occurrence,
    )
    checkpoint_units = tuple(checkpoint.completed_units())
    CheckpointStore._verify_chain(checkpoint.document)
    checkpoint_chain_head = checkpoint.document.get("chain_head_sha256")
    checkpoint_file_sha = sha256_file(checkpoint.path)
    gates.require(
        "checkpoint binding and unit completeness are exact",
        canonical_json(checkpoint.document["binding"]) == canonical_json(binding)
        and checkpoint_units == expected_units
        and len(set(checkpoint_units)) == 63
        and tuple(resumed_units + fresh_units) == expected_units
        and set(resumed_units).isdisjoint(fresh_units)
        and isinstance(checkpoint_chain_head, str)
        and len(checkpoint_chain_head) == 64
        and len(checkpoint_file_sha) == 64,
        {
            "binding": binding,
            "completed_units": list(checkpoint_units),
            "resumed_units": resumed_units,
            "fresh_units": fresh_units,
            "chain_head_sha256": checkpoint_chain_head,
            "checkpoint_file_sha256": checkpoint_file_sha,
            "hash_semantics": "unkeyed integrity checksums; not authenticity signatures",
        },
    )

    reflections = {"PP": "PP", "P1": "1P", "1P": "P1",
                   "11": "11", "12": "21", "21": "12"}
    requested_policy_blocks = {
        block for row in audit.action_log for block in row["direct_blocks_policy_label"]
    }
    hermitian_policy_closure = requested_policy_blocks | {
        reflections[block] for block in requested_policy_blocks
    }
    n_reflection_checks = {}
    for bra_index in range(3):
        for ket_index in range(3):
            forward = _unit_key("N", bra_index, ket_index)
            reflected = _unit_key("N", ket_index, bra_index)
            equal = audit.by_consumer[forward] == audit.by_consumer[reflected]
            n_reflection_checks[f"{bra_index},{ket_index}"] = equal
    gates.require(
        "policy: magnetic block ledger is Hermitian-closed",
        hermitian_policy_closure == set(ALLOWED_BLOCKS)
        and not requested_policy_blocks.intersection(FORBIDDEN_BLOCKS)
        and all(n_reflection_checks.values()),
        {
            "policy_check_only_for_block_labels": True,
            "requested_policy_blocks": sorted(requested_policy_blocks),
            "closure_with_reflections": sorted(hermitian_policy_closure),
            "computational_N_occurrence_reflection_checks": n_reflection_checks,
            "claim": "labels constrain schedule metadata; N occurrence ledgers supply the computational reflection check",
        },
    )
    prohibited_report = _static_scope_policy_report(script_path.read_text(encoding="utf-8"))
    gates.require(
        "policy: static prohibited-token scope scan is clear",
        not prohibited_report["found"],
        prohibited_report,
    )
    gates.finalize()

    audit_report = audit.report()
    structural_stage_counts = {
        str(index): {
            stage_name: {
                "history_depth": context["history_depth"],
                "state": context["state"],
                **({
                    "transition": {
                        key: int(context["transition"][key])
                        for key in ("actions", "channels", "supports")
                    }
                } if "transition" in context else {}),
                **({
                    "resolvent": {
                        key: int(context["resolvent"][key])
                        for key in ("input_supports", "output_supports", "E0_groups")
                    }
                } if "resolvent" in context else {}),
            }
            for stage_name, context in stage_contexts[index].items()
        }
        for index in range(3)
    }
    structural_moment_stats = {
        moment: {
            unit: {
                key: stats[key]
                for key in (
                    "unit", "moment", "bra_polarization_index", "bra_polarization",
                    "ket_polarization_index", "ket_polarization", "left_blocks",
                    "left_block_scan_counts", "translation_signature_tests",
                    "expected_translation_signature_tests", "matched_h0_support_blocks",
                    "raw_pair_upper", "matched_flux_groups", "state_pair_tests",
                    "local_occurrences", "same_polarization",
                    "samepol_oneface_analytic_skips",
                    "samepol_oneface_skip_displacements",
                    "crosspol_oneface_fallback_candidate_blocks",
                    "crosspol_oneface_fallback_matches",
                    "crosspol_oneface_fallback_displacements",
                    "crosspol_oneface_audited_pair_displacements",
                    "operator_between_endpoints", "block_origin", "d_special_routing",
                )
            } | ({
                "analytic_registered_contributions": stats["analytic_oneface_route_certificate"]
                    ["registered_analytic_contributions"],
                "analytic_expected_exact_fraction": stats["analytic_oneface_route_certificate"]
                    ["expected_exact_fraction"],
            } if stats["analytic_oneface_route_certificate"] is not None else {})
            for unit, stats in moment_report[moment].items()
        }
        for moment, *_ in MOMENTS
    }
    structural_identity = {
        "schema": SCHEMA,
        "binding": binding,
        "execution": {
            "mode": "DIAGNOSTIC_RESUME" if resume else "FRESH",
            "resumed_units": resumed_units,
            "fresh_units": fresh_units,
        },
        "checkpoint_structure": {
            "schema": CHECKPOINT_SCHEMA,
            "unit_order": list(checkpoint_units),
        },
        "roots": roots,
        "action_log": audit.action_log,
        "stage_state_stats": structural_stage_counts,
        "moment_stats": structural_moment_stats,
        "occurrence_counts": audit_report["all_occurrences"],
        "center_neutral_counts": audit_report["center_neutral_occurrences"],
        "gate_names": [row["name"] for row in gates.passed],
    }
    certificate_id = _portable_certificate_id(structural_identity)
    terminal_status = "DIAGNOSTIC_RESUME" if resume else "PASS"
    promotable = (
        terminal_status == "PASS"
        and not resumed_units
        and tuple(fresh_units) == expected_units
    )
    payload: dict[str, Any] = {
        "schema": SCHEMA,
        "status": terminal_status,
        "promotable_pass": promotable,
        "scope": "full-T1 root-face physical-state order/occurrence census only",
        "requested_order": REQUESTED_ORDER,
        "lattice": {"L": L, "vertices": len(verts), "links": E, "faces": P},
        "roots": root_orbits,
        "allowed_blocks": list(ALLOWED_BLOCKS),
        "forbidden_blocks": list(FORBIDDEN_BLOCKS),
        "executed_v10a2_reference": EXECUTED_V10A2_REFERENCE,
        "executed_v10a2_reference_sha256": reference_hash,
        "source_locators": SOURCE_LOCATORS,
        "runtime_provenance": {
            "script_path": str(script_path),
            "script_sha256": script_sha,
            "authority_path": SOURCE_LOCATORS["authority"],
            "authority_sha256": SOURCE_LOCATORS["authority_sha256"],
            "authority_runtime_status": authority_runtime_status,
            "notebook_expected_script_sha256": notebook_expected_script_sha,
            "notebook_hash_binding": (
                "runner verifies the exact script SHA; notebook SHA is omitted "
                "from the script certificate to avoid a circular hash"
            ),
            "environment": environment,
            "environment_sha256": environment_hash,
            "environment_binding_semantics": (
                "package/platform fingerprint only; not a container, BLAS-build, "
                "or hardware attestation"
            ),
            "config": config,
            "config_sha256": config_hash,
        },
        "haar_certificate": haar_certificate,
        "states": stage_contexts,
        "transition_stats": transition_stats,
        "moments": moment_report,
        "negative_controls": negative,
        "occurrence_audit": audit_report,
        "checkpoint": {
            "path": str(checkpoint.path),
            "schema": CHECKPOINT_SCHEMA,
            "binding": binding,
            "completed_units": list(checkpoint_units),
            "resumed_units": resumed_units,
            "fresh_units": fresh_units,
            "chain_head_sha256": checkpoint_chain_head,
            "file_sha256": checkpoint_file_sha,
            "hash_semantics": "unkeyed integrity checksums; not authenticity signatures",
        },
        "execution": {
            "mode": "DIAGNOSTIC_RESUME" if resume else "FRESH",
            "resume_requested": bool(resume),
            "checkpoint_existed_at_open": checkpoint.existed_at_open,
            "resumed_units": resumed_units,
            "fresh_units": fresh_units,
            "promotable": promotable,
        },
        "nonvacuity_policy": {
            "matrix_indexing": "NONVACUITY_MATRIX[moment][ket][bra]",
            "matrix": NONVACUITY_MATRIX,
            "structural_zero_justifications": STRUCTURAL_ZERO_JUSTIFICATIONS,
            "unit_results": unit_nonvacuity,
        },
        "operational_report": budget.report(),
        "gates": gates.passed,
        "certificate_identity_material": structural_identity,
        "certificate_identity_scope": {
            "certificate_id": certificate_id,
            "included": (
                "script/config hashes, authority hash and runtime-verification status, "
                "environment fingerprint, reference manifest, execution freshness, structural "
                "checkpoint schema/unit order, roots, structural stage counts, integer census "
                "ledgers, occurrence counts, and gate names"
            ),
            "excluded": (
                "raw checkpoint records, checkpoint chain/file hashes, timestamps, elapsed "
                "time, RAM high-water mark, floating Haar/resolvent diagnostics, and floating "
                "representative coefficients; checkpoint hashes remain external integrity "
                "metadata and are not inputs to the portable certificate ID"
            ),
            "environment_fingerprint_bound": True,
            "exact_environment_attestation": False,
            "checkpoint_integrity_external_only": True,
            "portable_across_nonstructural_checkpoint_float_changes": True,
            "portable_identity_raw_float_policy": "reject every raw float before hashing",
        },
        "certificate_id": certificate_id,
        "next_stage_authorized": False,
        "gpu_requested": False,
        "gpu_go": False,
    }
    ensure_finite("pass_payload", payload)
    return payload


def _positive_int(value: str) -> int:
    parsed = int(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("value must be positive")
    return parsed


def _positive_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed) or parsed <= 0:
        raise argparse.ArgumentTypeError("value must be finite and positive")
    return parsed


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json-out", type=Path, default=Path(DEFAULT_JSON_NAME))
    parser.add_argument("--checkpoint", type=Path)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--notebook-expected-script-sha")
    parser.add_argument("--max-wall-seconds", type=_positive_int,
                        default=DEFAULT_MAX_WALL_SECONDS)
    parser.add_argument("--max-rss-gib", type=_positive_float, default=DEFAULT_MAX_RSS_GIB)
    parser.add_argument("--max-w-actions", type=_positive_int,
                        default=DEFAULT_MAX_W_ACTIONS_PER_CALL)
    parser.add_argument("--max-w-channels", type=_positive_int,
                        default=DEFAULT_MAX_W_CHANNELS_PER_CALL)
    parser.add_argument("--max-supports", type=_positive_int,
                        default=DEFAULT_MAX_SUPPORTS_PER_STAGE)
    parser.add_argument("--max-pair-tests-per-unit", type=_positive_int,
                        default=DEFAULT_MAX_PAIR_TESTS_PER_UNIT)
    parser.add_argument("--max-pair-tests-total", type=_positive_int,
                        default=DEFAULT_MAX_PAIR_TESTS_TOTAL)
    parser.add_argument("--max-payload-mib", type=_positive_float,
                        default=DEFAULT_MAX_PAYLOAD_MIB)
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    destination = _bootstrap_json_path(sys.argv[1:] if argv is None else argv)
    started = datetime.now(timezone.utc).isoformat()
    try:
        args = parse_args(argv)
        destination = args.json_out.resolve()
        checkpoint_path = (
            args.checkpoint.resolve() if args.checkpoint is not None
            else destination.with_suffix(destination.suffix + ".checkpoint.json")
        )
        limits = OperationalLimits(
            max_wall_seconds=args.max_wall_seconds,
            max_rss_gib=args.max_rss_gib,
            max_w_actions_per_call=args.max_w_actions,
            max_w_channels_per_call=args.max_w_channels,
            max_supports_per_stage=args.max_supports,
            max_pair_tests_per_unit=args.max_pair_tests_per_unit,
            max_pair_tests_total=args.max_pair_tests_total,
            max_payload_bytes=int(args.max_payload_mib * 1024 * 1024),
        )
        running = {
            "schema": "hodge-preflight-envelope/v1",
            "status": "RUNNING",
            "started_utc": started,
            "script": str(Path(__file__).resolve()),
            "script_sha256": sha256_file(Path(__file__).resolve()),
            "checkpoint": str(checkpoint_path),
            "limits": asdict(limits),
            "gpu_requested": False,
        }
        atomic_write_json(destination, running)
        payload = run_root_preflight(
            limits=limits,
            checkpoint_path=checkpoint_path,
            resume=args.resume,
            notebook_expected_script_sha=args.notebook_expected_script_sha,
        )
        if _ACTIVE_BUDGET is None:
            raise PreflightFailure("operational budget disappeared before publication")
        _ACTIVE_BUDGET.check("final payload before serialization", force_heartbeat=True)
        payload["started_utc"] = started
        payload["completed_utc"] = datetime.now(timezone.utc).isoformat()
        payload["wall_clock_enforcement"] = (
            "cooperative checks between bounded operations; no asynchronous watchdog; "
            "a surviving terminal document also passed a post-write budget check"
        )
        payload["publication"] = {
            "payload_ceiling_bytes": limits.max_payload_bytes,
            "serialized_bytes": 0,
            "finite_serialization_required": True,
            "post_write_budget_check_required": True,
        }
        payload["operational_report"] = _ACTIVE_BUDGET.report()
        ensure_finite("final_payload", payload)
        # Establish the exact byte count before publication.  The field contains
        # its own decimal representation, so converge the tiny fixed point.
        for _ in range(8):
            size = len(_serialized_json_bytes(payload))
            if size == payload["publication"]["serialized_bytes"]:
                break
            payload["publication"]["serialized_bytes"] = size
        else:
            raise PreflightFailure("final payload byte-count fixed point did not converge")
        expected_size = len(_serialized_json_bytes(payload))
        if expected_size != payload["publication"]["serialized_bytes"]:
            raise PreflightFailure("final payload byte-count certificate mismatch")
        if expected_size > limits.max_payload_bytes:
            raise PreflightFailure(
                f"final payload ceiling exceeded: {expected_size} > {limits.max_payload_bytes} bytes"
            )
        _ACTIVE_BUDGET.check("final payload after serialization", force_heartbeat=True)
        published_size = atomic_write_json(
            destination, payload, max_bytes=limits.max_payload_bytes,
        )
        if published_size != expected_size:
            raise PreflightFailure(
                f"published payload size mismatch: {published_size} != {expected_size}"
            )
        _ACTIVE_BUDGET.check("final payload after atomic write", force_heartbeat=True)
        label = "PASS" if payload["status"] == "PASS" else "DIAGNOSTIC_RESUME"
        print(
            f"\nFULL-T1 ROOT PREFLIGHT {label}: {len(payload['gates'])}/{len(REQUIRED_GATES)} "
            f"required gates; certificate={payload['certificate_id']}",
            flush=True,
        )
        print(f"Certificate written atomically to {destination}", flush=True)
        print(
            "PROMOTABLE PASS: YES" if payload["promotable_pass"] else
            "PROMOTABLE PASS: NO (resumed runs are diagnostic only)",
            flush=True,
        )
        print("GPU GO: NO (this artifact stops at the occurrence boundary)", flush=True)
        return 0
    except BaseException as exc:
        failure = {
            "schema": "hodge-preflight-envelope/v1",
            "status": "FAIL",
            "started_utc": started,
            "failed_utc": datetime.now(timezone.utc).isoformat(),
            "script": str(Path(__file__).resolve()),
            "script_sha256": sha256_file(Path(__file__).resolve()),
            "error_type": type(exc).__name__,
            "error": str(exc),
            "traceback": traceback.format_exc().splitlines()[-40:],
            "gpu_requested": False,
            "gpu_go": False,
        }
        try:
            atomic_write_json(destination, failure)
        except Exception as write_exc:
            print(f"FAIL envelope write also failed: {write_exc}", file=sys.stderr)
        print("FULL-T1 ROOT PREFLIGHT FAILED", file=sys.stderr)
        print(f"{type(exc).__name__}: {exc}", file=sys.stderr)
        print(f"FAIL envelope: {destination}", file=sys.stderr)
        print("GPU GO: NO", file=sys.stderr)
        return 130 if isinstance(exc, KeyboardInterrupt) else 2


if __name__ == "__main__":
    raise SystemExit(main())
