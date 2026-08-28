#!/usr/bin/env python3
"""
carrier_scaling.py — the Z_a scaling campaign.

WHAT THIS MEASURES, and why it is the right thing to measure
------------------------------------------------------------
Define, for the zero-momentum charge-odd carrier source at lattice spacing a,

    C_a(t)  = <O(t) O(0)>            (C-odd => no vacuum subtraction needed)
    M_a     = -lim (1/t) log C_a(t)  (exists by log-convexity)
    F_a(t)  = e^{M_a t} C_a(t)/C_a(0)
    Z_a     = lim_{t->inf} F_a(t)    (exists: F_a is NON-INCREASING and >= 0)

Z_a is the residue.  It is not a hypothesis: it is a number the theory has at
every spacing, and it is exactly what spectroscopy calls the ground-state
overlap.  The open continuum question is the single scalar

    inf_a Z_a > 0 ?

Because F_a is non-increasing with limit Z_a, EVERY finite-t evaluation obeys

    Z_a <= F_a(t)                       (upper bound, always)
    Z_a >= (F_a(t) - e^{-D_a t}) / (1 - e^{-D_a t})   (lower bound, needs the gap D_a)

and the second inequality is SHARP (equality when the non-ground weight sits at
the gap edge).  So this run is a ONE-SIDED INSTRUMENT: it can refute
inf_a Z_a > 0, and can only confirm it via the gap.  Hence the gap D_a (to the
next T1^{+-} level) is measured in the same run, or the residue is
uninterpretable in the direction that matters.

THE DECISIVE COMPARISON
-----------------------
  * rho = 0 (bare local carrier): predicted Z_a ~ a^{2d-3} = a^9, since the
    C-odd carrier's lowest continuum operator d^{abc}F F F has dimension 6.
    (d = 4 gives a^5, reproducing Schierholz 1988.)
  * rho fixed in fm (spatial gradient flow): predicted Z_a roughly a-INDEPENDENT.

If a fixed-PHYSICAL-radius source still falls like a^9, the smearing premise is
in serious trouble.  That is the cheapest way for this to be wrong, and this run
finds it.  Note what the a^{2d-3} law refers to: the NORMALIZED fraction
Z_a / C_a(0), under a pinned flowed-source convention.  It is a candidate scaling
law, not a theorem -- operator mixing, multiplicative renormalization and
anomalous logarithms are not accounted for in the dimensional estimate.

CONVENTIONS
-----------
Matched to corpus-import/numerics/engines/ENGINE_MC_su3_t1pm_spatial_nextrun.py
so results are directly comparable to the stored beta=5.8941 run:
  * path tokens are +/- (direction+1)
  * operator is  Im Tr W / 3 , summed over space, divided by sqrt(L^3)
  * axial normal x,y,z <-> cyclic planes yz, zx, xy
CHANGED ON PURPOSE:
  * smearing is SPATIAL GRADIENT FLOW to a fixed PHYSICAL radius, not APE at a
    fixed level count (whose radius shrinks with a -- the Schierholz failure).
    Spatial-only, per time slice: 4D flow would mix time slices and break the
    transfer-matrix / OS reading of C(t).
  * A2^{+-} and T2^{+-} partner channels are measured.  The carrier has
    IDENTICALLY ZERO overlap with its own J=3 partners (T1 (x) A1 contains
    neither A2 nor T2), so it is structurally blind to its own falsifier.
    Verified by character decomposition in --selftest, not assumed: the SQUARE
    plaquette carries T1+ ALONE (matching the exact Sym^3 result); an asymmetric
    planar 1x2 rectangle already reaches T2+ (its orbit is 6, not 3, because it
    is not symmetric under swapping its in-plane axes); and A2+ is the one channel
    that genuinely demands NON-PLANAR loops -- cheapest source X6a =
    (x,y,z,-x,-y,-z), orbit 4.

Read-only w.r.t. the WORKHOUSE repository: this file lives outside it and
imports nothing from it.

Usage (Colab / Jupyter)
-----------------------
  # cell 1 -- put the file somewhere that survives a disconnect
  from google.colab import drive; drive.mount('/content/drive')
  %cd /content/drive/MyDrive/workhouse        # upload carrier_scaling.py here
  import sys; sys.path.insert(0, '.')

  # cell 2 -- check the machine BEFORE committing to a run
  import carrier_scaling as cs
  cs.nb_selftest()
  cs.nb_bench(device="cuda")     # prints projected wall clock per ensemble
  cs.nb_run(quick=True)          # minutes: validates the code path end to end

  # cell 3 -- the run.  checkpoint_every survives Colab disconnects:
  #           re-run this same cell after reconnecting and it resumes.
  cs.nb_run(device="cuda", colab=True, checkpoint_every=25)
  cs.nb_analyze("out_colab/*.npz")
  cs.nb_selftest()               # no GPU, no numpy, seconds
  cs.nb_plan()                   # sizes and cost
  cs.nb_run(quick=True)          # 6^3x12 toy lattices: validates the code path
  cs.nb_run(device="cuda")       # the real campaign
  cs.nb_analyze("out/*.npz")

Usage (AMD 7900 XTX / ROCm)
---------------------------
The 7900 XTX is Navi 31 = gfx1100, officially supported since ROCm 5.7, so no
HSA_OVERRIDE_GFX_VERSION is needed (that hack is for gfx1030).  Confirm with:

    rocminfo | grep -m1 gfx          # expect gfx1100

Install the ROCm build of PyTorch (check pytorch.org for the current index URL;
rocm6.2 is a known-good example):

    pip install --force-reinstall torch --index-url https://download.pytorch.org/whl/rocm6.2

IMPORTANT: on ROCm, PyTorch still names the device "cuda".  Use device="cuda"
(or "auto"), never "rocm" or "hip".

Then, before anything else:

    import carrier_scaling as cs
    cs.nb_check_gpu()          # exercises every torch op this script uses
    cs.nb_selftest()
    cs.nb_run(quick=True)      # minutes
    cs.nb_bench()              # projected wall clock for the real campaign
    cs.nb_run(checkpoint_every=25)

24 GB of VRAM is ample: the largest ensemble's gauge field is ~0.2 GiB and peak
working set stays well under 5 GiB.  The risk on ROCm is not memory, it is
whether batched complex64 GEMM is fast (or works at all) -- which is exactly
what nb_check_gpu and nb_bench measure.  If complex64 matmul fails, retry with
dtype="complex128".

Usage (CLI)
-----------
  python carrier_scaling.py --selftest            # no GPU needed, ~seconds
  python carrier_scaling.py --plan                # show the run plan and cost
  python carrier_scaling.py --run --device cuda   # the campaign
  python carrier_scaling.py --analyze out/*.npz   # re-analyze without re-running
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import os
import time
from dataclasses import dataclass, field, asdict
from typing import Dict, List, Sequence, Tuple

# ============================================================================
# 0. Run plan
# ============================================================================

R0_FM = 0.5  # Sommer scale r0 in fm; only sets the unit of "physical"


def necco_sommer_a_over_r0(beta: float) -> float:
    """Necco-Sommer (2002) interpolation, valid 5.7 <= beta <= 6.92.

    ln(a/r0) = -1.6805 - 1.7139(b-6) + 0.8155(b-6)^2 - 0.6667(b-6)^3
    At beta=6 this gives r0/a = 5.366 (published 5.368).
    """
    if not (5.7 <= beta <= 6.92):
        raise ValueError(f"beta={beta} outside Necco-Sommer validity [5.7, 6.92]")
    b = beta - 6.0
    return math.exp(-1.6805 - 1.7139 * b + 0.8155 * b * b - 0.6667 * b ** 3)


def a_fm(beta: float) -> float:
    return necco_sommer_a_over_r0(beta) * R0_FM


@dataclass
class Ensemble:
    beta: float
    L: int
    T: int
    n_therm: int = 2000
    n_meas: int = 4000
    n_sep: int = 10          # sweeps between measurements
    n_or: int = 4            # overrelaxation hits per heatbath sweep

    @property
    def a(self) -> float:
        return a_fm(self.beta)

    @property
    def box_fm(self) -> float:
        return self.L * self.a


#: set by nb_run(quick=True); None in normal operation
_ENSEMBLE_OVERRIDE: "List[Ensemble] | None" = None


def default_ensembles(target_box_fm: float = 1.9) -> List[Ensemble]:
    """Three spacings at ~fixed physical volume.

    Fixed physical volume matters: otherwise finite-volume effects confound the
    a-dependence you are trying to isolate.
    """
    if _ENSEMBLE_OVERRIDE is not None:
        return _ENSEMBLE_OVERRIDE
    out = []
    for beta, tratio in ((5.85, 2.0), (6.00, 2.0), (6.20, 2.0)):
        a = a_fm(beta)
        L = int(round(target_box_fm / a / 2.0)) * 2      # even
        T = int(round(L * tratio))
        out.append(Ensemble(beta=beta, L=L, T=T))
    return out


#: Physical smearing radii in fm.  rho=0 is the BARE source and is the a^9 test.
DEFAULT_RHO_FM: Tuple[float, ...] = (0.0, 0.15, 0.20, 0.25, 0.30)


def flow_time_lattice(rho_fm: float, a: float) -> float:
    """Gradient-flow time tau/a^2 giving smearing radius rho = sqrt(8 tau)."""
    if rho_fm <= 0:
        return 0.0
    return (rho_fm / a) ** 2 / 8.0


# ============================================================================
# 1. Octahedral group O_h, in pure Python (no numpy: --selftest runs anywhere)
# ============================================================================
# An element is (perm, signs): axis j -> perm[j], with sign signs[j].
# All 48 signed permutation matrices are exactly O_h.

GroupElem = Tuple[Tuple[int, int, int], Tuple[int, int, int]]


def oh_elements() -> List[GroupElem]:
    els: List[GroupElem] = []
    for perm in itertools.permutations((0, 1, 2)):
        for signs in itertools.product((1, -1), repeat=3):
            els.append((perm, signs))
    assert len(els) == 48
    return els


def elem_det(g: GroupElem) -> int:
    perm, signs = g
    # sign of the permutation times the product of the entry signs
    p = list(perm)
    swaps = 0
    for i in range(3):
        for j in range(i + 1, 3):
            if p[i] > p[j]:
                swaps += 1
    return (-1) ** swaps * signs[0] * signs[1] * signs[2]


def elem_matrix(g: GroupElem) -> List[List[int]]:
    perm, signs = g
    M = [[0, 0, 0] for _ in range(3)]
    for j in range(3):
        M[perm[j]][j] = signs[j]
    return M


def rotation_class(g: GroupElem) -> str:
    """Class of a det=+1 element of O, by trace and diagonality."""
    M = elem_matrix(g)
    tr = M[0][0] + M[1][1] + M[2][2]
    if tr == 3:
        return "E"
    if tr == 0:
        return "8C3"
    if tr == 1:
        return "6C4"
    if tr == -1:
        diagonal = all(M[i][j] == 0 for i in range(3) for j in range(3) if i != j)
        return "3C2" if diagonal else "6C2p"
    raise ValueError(f"not a rotation: trace {tr}")


#: characters of O in the class order (E, 8C3, 3C2, 6C4, 6C2p)
O_CHARACTERS: Dict[str, Dict[str, int]] = {
    "A1": {"E": 1, "8C3": 1, "3C2": 1, "6C4": 1, "6C2p": 1},
    "A2": {"E": 1, "8C3": 1, "3C2": 1, "6C4": -1, "6C2p": -1},
    "E":  {"E": 2, "8C3": -1, "3C2": 2, "6C4": 0, "6C2p": 0},
    "T1": {"E": 3, "8C3": 0, "3C2": -1, "6C4": 1, "6C2p": -1},
    "T2": {"E": 3, "8C3": 0, "3C2": -1, "6C4": -1, "6C2p": 1},
}
CLASS_SIZES = {"E": 1, "8C3": 8, "3C2": 3, "6C4": 6, "6C2p": 6}
IRREP_DIM = {"A1": 1, "A2": 1, "E": 2, "T1": 3, "T2": 3}


def invert_elem(g: GroupElem) -> GroupElem:
    """Multiply by spatial inversion: negate every sign."""
    perm, signs = g
    return (perm, tuple(-s for s in signs))


def character(irrep: str, parity: int, g: GroupElem) -> int:
    """chi^{Lambda,P}(g) for g in O_h.  parity = +1 (gerade) or -1 (ungerade)."""
    if elem_det(g) == 1:
        return O_CHARACTERS[irrep][rotation_class(g)]
    r = invert_elem(g)          # g = i * r with r in O
    assert elem_det(r) == 1
    return parity * O_CHARACTERS[irrep][rotation_class(r)]


# ============================================================================
# 2. Loop paths and their O_h orbits
# ============================================================================
# A path is a tuple of tokens +/-(d+1), d in {0,1,2}.  Closed <=> displacement 0.

Path = Tuple[int, ...]


def path_displacement(path: Path) -> Tuple[int, int, int]:
    d = [0, 0, 0]
    for tok in path:
        ax = abs(tok) - 1
        d[ax] += 1 if tok > 0 else -1
    return tuple(d)  # type: ignore[return-value]


def is_closed(path: Path) -> bool:
    return path_displacement(path) == (0, 0, 0)


def apply_elem(g: GroupElem, path: Path) -> Path:
    perm, signs = g
    out = []
    for tok in path:
        ax = abs(tok) - 1
        s = (1 if tok > 0 else -1) * signs[ax]
        out.append(s * (perm[ax] + 1))
    return tuple(out)


def reverse_path(path: Path) -> Path:
    """Traverse the loop backwards:  W(reverse) = W(path)^dagger."""
    return tuple(-t for t in reversed(path))


def canonical(path: Path) -> Tuple[Path, int]:
    """Canonical representative, with the sign Im Tr W picks up.

    Two identifications are physical and BOTH must be made:
      * cyclic rotation of the starting point -- the zero-momentum sum does not
        care where the loop starts, so these give the SAME operator, sign +1;
      * reversal -- W(reverse) = W(path)^dagger, so Tr W(reverse) = conj(Tr W),
        hence Im Tr W(reverse) = -Im Tr W(path), sign -1.

    Missing the second one double-counts reversed images instead of letting them
    cancel, and manufactures operators in channels that are actually empty.
    """
    n = len(path)
    best, sign = None, 1
    for src, sg in ((path, 1), (reverse_path(path), -1)):
        for i in range(n):
            rot = tuple(src[i:] + src[:i])
            if best is None or rot < best:
                best, sign = rot, sg
    return best, sign  # type: ignore[return-value]


def rectangle_path(i: int, j: int, m: int, n: int) -> Path:
    """Matches ENGINE_MC_su3_t1pm_spatial_nextrun.rectangle_path exactly."""
    return tuple([i + 1] * m + [j + 1] * n + [-(i + 1)] * m + [-(j + 1)] * n)


#: Prototype loops.  Planar shapes span only T1 in the C-odd sector; the
#: non-planar ones are what reach A2 and T2 -- the carrier's J=3 partners.
PROTOTYPES: Dict[str, Path] = {
    # planar (reach T1 only)
    "P11": rectangle_path(0, 1, 1, 1),
    "P12": rectangle_path(0, 1, 1, 2),
    "P22": rectangle_path(0, 1, 2, 2),
    # non-planar, 6 links
    "X6a": (1, 2, 3, -1, -2, -3),
    "X6b": (1, 2, -1, 3, -2, -3),
    # non-planar, 8 links
    "X8a": (1, 1, 2, 3, -1, -1, -2, -3),
    "X8b": (1, 2, 2, 3, -1, -2, -2, -3),
}


@dataclass
class ProjectedOperator:
    """One (prototype, irrep, parity) operator: a weighted sum of loop traces."""
    name: str
    prototype: str
    irrep: str
    parity: int
    terms: List[Tuple[Path, float]] = field(default_factory=list)

    @property
    def n_paths(self) -> int:
        return len(self.terms)


def project_prototype(proto_name: str, path: Path, irrep: str, parity: int) -> ProjectedOperator:
    """O^{Lambda,P} = sum_{g in O_h} chi^{Lambda,P}(g)* W(g . path).

    Sums over the full 48-element group and collects duplicate paths, so each
    distinct Wilson loop is computed once.  This projects onto the Lambda
    isotypic component summed over rows; all rows are degenerate, so the mass is
    unaffected and the basis stays small.
    """
    weights: Dict[Path, float] = {}
    for g in oh_elements():
        chi = character(irrep, parity, g)
        if chi == 0:
            continue
        p, sgn = canonical(apply_elem(g, path))
        weights[p] = weights.get(p, 0.0) + float(chi) * sgn
    terms = [(p, w) for p, w in sorted(weights.items()) if abs(w) > 1e-12]
    norm = math.sqrt(sum(w * w for _, w in terms)) or 1.0
    terms = [(p, w / norm) for p, w in terms]
    return ProjectedOperator(
        name=f"{proto_name}:{irrep}{'+' if parity > 0 else '-'}",
        prototype=proto_name, irrep=irrep, parity=parity, terms=terms,
    )


#: the channels this campaign needs: carrier + its J=3 partners, all C-odd
TARGET_CHANNELS: Tuple[Tuple[str, int], ...] = (("T1", +1), ("A2", +1), ("T2", +1))


def build_operator_basis() -> List[ProjectedOperator]:
    ops: List[ProjectedOperator] = []
    for pname, path in PROTOTYPES.items():
        if not is_closed(path):
            raise ValueError(f"prototype {pname} is not a closed loop")
        for irrep, parity in TARGET_CHANNELS:
            op = project_prototype(pname, path, irrep, parity)
            if op.terms:
                ops.append(op)
    return ops


# ============================================================================
# 3. Torch lattice (imported lazily so --selftest needs no GPU stack)
# ============================================================================

def _torch():
    import torch  # noqa: F401
    return torch


class Lattice:
    """SU(3) Wilson gauge theory on T x L^3, pseudo-heatbath + overrelaxation.

    Link layout: U[t, x, y, z, mu, 3, 3] with mu = 0 (time), 1..3 (space).
    """

    def __init__(self, ens: Ensemble, device: str = "cuda", dtype: str = "complex64", seed: int = 0):
        torch = _torch()
        self.torch = torch
        self.ens = ens
        self.device = torch.device(device)
        self.cdtype = torch.complex64 if dtype == "complex64" else torch.complex128
        self.rdtype = torch.float32 if dtype == "complex64" else torch.float64
        self.gen = torch.Generator(device=self.device).manual_seed(seed)
        self.shape = (ens.T, ens.L, ens.L, ens.L)
        eye = torch.eye(3, dtype=self.cdtype, device=self.device)
        self.U = eye.expand(*self.shape, 4, 3, 3).clone()   # cold start
        self._parity_masks = self._build_parity_masks()

    # -- geometry ---------------------------------------------------------
    def _build_parity_masks(self):
        torch = self.torch
        idx = torch.meshgrid(*[torch.arange(n, device=self.device) for n in self.shape], indexing="ij")
        s = idx[0] + idx[1] + idx[2] + idx[3]
        even = (s % 2 == 0)
        return even, ~even

    def shift(self, x, mu: int, disp: int):
        """Periodic shift along lattice axis mu (0=t,1..3=space) by disp sites."""
        return self.torch.roll(x, shifts=-disp, dims=mu)

    # -- action -----------------------------------------------------------
    def staple(self, mu: int, dirs: Sequence[int] | None = None):
        """Sum of staples A_mu(x) so that Re Tr(U_mu A_mu^dag) is the local action."""
        torch = self.torch
        U = self.U
        dirs = range(4) if dirs is None else dirs
        A = torch.zeros_like(U[..., mu, :, :])
        for nu in dirs:
            if nu == mu:
                continue
            Unu = U[..., nu, :, :]
            Umu = U[..., mu, :, :]
            # forward staple: U_nu(x) U_mu(x+nu) U_nu(x+mu)^dag
            A = A + Unu @ self.shift(Umu, nu, 1) @ self.shift(Unu, mu, 1).conj().transpose(-2, -1)
            # backward staple: U_nu(x-nu)^dag U_mu(x-nu) U_nu(x-nu+mu)
            Unu_m = self.shift(Unu, nu, -1)
            Umu_m = self.shift(Umu, nu, -1)
            A = A + Unu_m.conj().transpose(-2, -1) @ Umu_m @ self.shift(Unu_m, mu, 1)
        return A

    def plaquette(self) -> float:
        """(1/3) <Re Tr U_p> averaged over all plaquettes."""
        torch = self.torch
        tot = 0.0
        n = 0
        for mu in range(4):
            for nu in range(mu + 1, 4):
                Umu, Unu = self.U[..., mu, :, :], self.U[..., nu, :, :]
                P = Umu @ self.shift(Unu, mu, 1) @ self.shift(Umu, nu, 1).conj().transpose(-2, -1) \
                    @ Unu.conj().transpose(-2, -1)
                tot += float(torch.einsum("...ii->...", P).real.mean()) / 3.0
                n += 1
        return tot / n

    # -- SU(2) subgroup machinery ----------------------------------------
    @staticmethod
    def _su2_indices():
        return ((0, 1), (0, 2), (1, 2))

    def _extract_su2(self, W, i: int, j: int):
        """Quaternion components of the SU(2) part of W's (i,j) submatrix."""
        a00, a01, a10, a11 = W[..., i, i], W[..., i, j], W[..., j, i], W[..., j, j]
        x0 = (a00 + a11).real * 0.5
        x1 = (a01 + a10).imag * 0.5
        x2 = (a01 - a10).real * 0.5
        x3 = (a00 - a11).imag * 0.5
        k = self.torch.sqrt(self.torch.clamp(x0 * x0 + x1 * x1 + x2 * x2 + x3 * x3, min=1e-20))
        return x0 / k, x1 / k, x2 / k, x3 / k, k

    def _embed_su2(self, q, i: int, j: int, mask):
        """Embed quaternion q=(q0,q1,q2,q3) as an SU(2) block into SU(3)."""
        torch = self.torch
        q0, q1, q2, q3 = q
        M = torch.eye(3, dtype=self.cdtype, device=self.device).expand(*self.shape, 3, 3).clone()
        one = torch.ones_like(q0)
        z = lambda re, im: torch.complex(re, im)
        M[..., i, i] = torch.where(mask, z(q0, q3), z(one, torch.zeros_like(q0)))
        M[..., i, j] = torch.where(mask, z(q2, q1), torch.zeros_like(z(q0, q0)))
        M[..., j, i] = torch.where(mask, z(-q2, q1), torch.zeros_like(z(q0, q0)))
        M[..., j, j] = torch.where(mask, z(q0, -q3), z(one, torch.zeros_like(q0)))
        return M

    def _kp_a0(self, alpha, mask):
        """Kennedy-Pendleton sampling of a0 with density ~ sqrt(1-a0^2) e^{alpha a0}."""
        torch = self.torch
        alpha = torch.clamp(alpha, min=1e-8)
        a0 = torch.zeros_like(alpha)
        need = mask.clone()
        for _ in range(80):
            if not bool(need.any()):
                break
            r = [torch.rand(alpha.shape, generator=self.gen, device=self.device, dtype=self.rdtype)
                 .clamp_(min=1e-12) for _ in range(4)]
            delta = -(torch.log(r[0]) + torch.cos(2 * math.pi * r[1]) ** 2 * torch.log(r[2])) / alpha
            ok = (r[3] ** 2) <= (1.0 - 0.5 * delta)
            ok = ok & (delta <= 2.0) & need
            a0 = torch.where(ok, 1.0 - delta, a0)
            need = need & ~ok
        a0 = torch.where(need, torch.zeros_like(a0), a0)   # give up: leave unchanged
        return a0, ~need

    def heatbath_sweep(self):
        torch = self.torch
        beta = self.ens.beta
        for mu in range(4):
            A = self.staple(mu)
            for par in self._parity_masks:
                W = self.U[..., mu, :, :] @ A.conj().transpose(-2, -1)
                for (i, j) in self._su2_indices():
                    w0, w1, w2, w3, k = self._extract_su2(W, i, j)
                    alpha = (2.0 * beta / 3.0) * k
                    a0, ok = self._kp_a0(alpha, par)
                    norm = torch.sqrt(torch.clamp(1 - a0 * a0, min=0.0))
                    # uniform direction on S^2
                    c = 2 * torch.rand(a0.shape, generator=self.gen, device=self.device, dtype=self.rdtype) - 1
                    phi = 2 * math.pi * torch.rand(a0.shape, generator=self.gen, device=self.device, dtype=self.rdtype)
                    st = torch.sqrt(torch.clamp(1 - c * c, min=0.0))
                    b = (a0, norm * st * torch.cos(phi), norm * st * torch.sin(phi), norm * c)
                    # a = b * w^dagger  (so that a w has real part b0)
                    a = (b[0] * w0 + b[1] * w1 + b[2] * w2 + b[3] * w3,
                         -b[0] * w1 + b[1] * w0 - b[2] * w3 + b[3] * w2,
                         -b[0] * w2 + b[1] * w3 + b[2] * w0 - b[3] * w1,
                         -b[0] * w3 - b[1] * w2 + b[2] * w1 + b[3] * w0)
                    M = self._embed_su2(a, i, j, par & ok)
                    self.U[..., mu, :, :] = M @ self.U[..., mu, :, :]
                    W = M @ W
            self.reunitarize(mu)

    def overrelax_sweep(self):
        torch = self.torch
        for mu in range(4):
            A = self.staple(mu)
            for par in self._parity_masks:
                W = self.U[..., mu, :, :] @ A.conj().transpose(-2, -1)
                for (i, j) in self._su2_indices():
                    w0, w1, w2, w3, _ = self._extract_su2(W, i, j)
                    # a = (w^dag)^2 : microcanonical reflection, preserves the action
                    d0, d1, d2, d3 = w0, -w1, -w2, -w3
                    a = (d0 * d0 - d1 * d1 - d2 * d2 - d3 * d3,
                         2 * d0 * d1, 2 * d0 * d2, 2 * d0 * d3)
                    M = self._embed_su2(a, i, j, par)
                    self.U[..., mu, :, :] = M @ self.U[..., mu, :, :]
                    W = M @ W
            self.reunitarize(mu)

    def reunitarize(self, mu: int | None = None):
        torch = self.torch
        idx = range(4) if mu is None else [mu]
        for m in idx:
            U = self.U[..., m, :, :]
            a = U[..., 0, :]
            a = a / torch.linalg.vector_norm(a, dim=-1, keepdim=True)
            b = U[..., 1, :]
            b = b - (a.conj() * b).sum(-1, keepdim=True) * a
            b = b / torch.linalg.vector_norm(b, dim=-1, keepdim=True)
            c = torch.linalg.cross(a.conj(), b.conj())
            self.U[..., m, :, :] = torch.stack([a, b, c], dim=-2)

    # -- gradient flow ----------------------------------------------------
    def _flow_force(self, links, dirs: Sequence[int]):
        """Z = -[projection to su(3) of (staple^dag U)] for the Wilson flow."""
        torch = self.torch
        saved = self.U
        self.U = links
        out = {}
        for mu in dirs:
            A = self.staple(mu, dirs=dirs)
            Om = links[..., mu, :, :] @ A.conj().transpose(-2, -1)
            X = Om - Om.conj().transpose(-2, -1)
            tr = torch.einsum("...ii->...", X)[..., None, None]
            eye = torch.eye(3, dtype=self.cdtype, device=self.device)
            out[mu] = 0.5 * X - (1.0 / 6.0) * tr * eye
        self.U = saved
        return out

    @staticmethod
    def _expm_su3(X, torch, terms: int = 12):
        """exp(X) for anti-hermitian traceless X, by truncated series (X is small)."""
        R = torch.eye(3, dtype=X.dtype, device=X.device).expand_as(X).clone()
        term = R.clone()
        for n in range(1, terms + 1):
            term = term @ X / n
            R = R + term
        return R

    def gradient_flow(self, links, tau: float, eps: float = 0.01, spatial_only: bool = True):
        """Luscher 3-step RK Wilson flow to flow time tau (lattice units)."""
        torch = self.torch
        if tau <= 0:
            return links.clone()
        dirs = (1, 2, 3) if spatial_only else (0, 1, 2, 3)
        V = links.clone()
        n = max(1, int(math.ceil(tau / eps)))
        h = tau / n
        for _ in range(n):
            Z0 = self._flow_force(V, dirs)
            W1 = V.clone()
            for mu in dirs:
                W1[..., mu, :, :] = self._expm_su3(-(0.25 * h) * Z0[mu], torch) @ V[..., mu, :, :]
            Z1 = self._flow_force(W1, dirs)
            W2 = V.clone()
            for mu in dirs:
                Xm = -(8.0 / 9.0 * h) * Z1[mu] + (17.0 / 36.0 * h) * Z0[mu]
                W2[..., mu, :, :] = self._expm_su3(Xm, torch) @ W1[..., mu, :, :]
            Z2 = self._flow_force(W2, dirs)
            for mu in dirs:
                Xm = -(3.0 / 4.0 * h) * Z2[mu] + (8.0 / 9.0 * h) * Z1[mu] - (17.0 / 36.0 * h) * Z0[mu]
                V[..., mu, :, :] = self._expm_su3(Xm, torch) @ W2[..., mu, :, :]
        return V

    def clover_energy(self, links) -> float:
        """t^2 <E> observable for t0 scale setting (4D flow)."""
        torch = self.torch
        saved, self.U = self.U, links
        E = 0.0
        for mu in range(4):
            for nu in range(mu + 1, 4):
                Umu, Unu = links[..., mu, :, :], links[..., nu, :, :]
                P = Umu @ self.shift(Unu, mu, 1) @ self.shift(Umu, nu, 1).conj().transpose(-2, -1) \
                    @ Unu.conj().transpose(-2, -1)
                E += float((1.0 - torch.einsum("...ii->...", P).real.mean() / 3.0))
        self.U = saved
        return 2.0 * E   # <E> in the plaquette definition

    # -- operators --------------------------------------------------------
    def loop_trace_imag(self, spatial_links, path: Path):
        """Im Tr W(path)/3 at every site, matching the corpus engine."""
        torch = self.torch
        M = torch.eye(3, dtype=self.cdtype, device=self.device).expand(*self.shape, 3, 3).clone()
        pos = [0, 0, 0]
        for tok in path:
            ax = abs(tok) - 1
            if tok > 0:
                link = spatial_links[..., ax, :, :]
                for k, d in enumerate(pos):
                    if d:
                        link = torch.roll(link, shifts=-d, dims=k + 1)
                M = M @ link
                pos[ax] += 1
            else:
                pos[ax] -= 1
                link = spatial_links[..., ax, :, :]
                for k, d in enumerate(pos):
                    if d:
                        link = torch.roll(link, shifts=-d, dims=k + 1)
                M = M @ link.conj().transpose(-2, -1)
        if pos != [0, 0, 0]:
            raise ValueError(f"open loop {path} displacement {pos}")
        return torch.einsum("...ii->...", M).imag / 3.0

    def measure_operators(self, spatial_links, ops: List[ProjectedOperator]):
        """Zero-momentum operator values, shape [n_ops, T]."""
        torch = self.torch
        cache: Dict[Path, "torch.Tensor"] = {}
        vals = []
        for op in ops:
            acc = None
            for path, w in op.terms:
                if path not in cache:
                    cache[path] = self.loop_trace_imag(spatial_links, path)
                term = w * cache[path]
                acc = term if acc is None else acc + term
            s = acc.sum(dim=(1, 2, 3)) / math.sqrt(self.ens.L ** 3)
            vals.append(s.to(torch.float64).cpu())
        return torch.stack(vals, dim=0).numpy()


# ============================================================================
# 4. Statistics: correlators, binning, bootstrap, GEVP, Z bounds
# ============================================================================

def correlators(series):
    """series: [n_cfg, n_ops, T]  ->  C: [n_cfg, n_ops, n_ops, T] (t-averaged)."""
    import numpy as np
    n_cfg, n_ops, T = series.shape
    C = np.zeros((n_cfg, n_ops, n_ops, T))
    for dt in range(T):
        shifted = np.roll(series, -dt, axis=2)
        C[:, :, :, dt] = np.einsum("iat,ibt->iab", series, shifted) / T
    return C


def bin_configs(x, block: int):
    import numpy as np
    n = (x.shape[0] // block) * block
    if n == 0:
        return x
    return x[:n].reshape(n // block, block, *x.shape[1:]).mean(axis=1)


def bootstrap(x, n_boot: int, seed: int = 0):
    import numpy as np
    rng = np.random.default_rng(seed)
    n = x.shape[0]
    idx = rng.integers(0, n, size=(n_boot, n))
    return x[idx].mean(axis=1)


def gevp(C, t0: int, t: int, n_states: int = 2):
    """Generalized eigenvalue problem C(t) v = lam C(t0) v; returns sorted lam."""
    import numpy as np
    A, B = C[..., t], C[..., t0]
    B = 0.5 * (B + B.T)
    w, V = np.linalg.eigh(B)
    keep = w > w.max() * 1e-8
    Bi = V[:, keep] @ np.diag(1.0 / np.sqrt(w[keep])) @ V[:, keep].T
    M = Bi @ (0.5 * (A + A.T)) @ Bi
    lam = np.linalg.eigvalsh(M)[::-1]
    return lam[:n_states]


def effective_mass(lam, t: int, t0: int, a_fm_val: float):
    import numpy as np
    with np.errstate(divide="ignore", invalid="ignore"):
        m_lat = -np.log(np.clip(lam, 1e-300, None)) / max(t - t0, 1)
    return m_lat  # lattice units


def z_bounds(F_t: float, delta_lat: float, t: int, C0: float = 1.0):
    """Upper and (gap-dependent, sharp) lower bound on Z at Euclidean separation t.

    NORMALIZATION IS LOAD-BEARING.  With mu = Z delta_M + tail, tail supported in
    [M+Delta, inf), and q = exp(-Delta t):

        F(t) <= Z + q (C0 - Z)      =>      Z >= (F(t) - q C0) / (1 - q).

    Dropping the C0 gives a FALSE bound whenever C0 != 1.  Counterexample:
    mu = delta_M + 9 delta_{M+Delta} with q = 1/2 has Z = 1, C0 = 10, F = 5.5;
    the C0-free expression returns 10.  Both Z and C0 scale as |lambda|^2 under
    O -> lambda O, so only the FRACTION Z/C0 is convention-independent, and
    "inf_a Z_a > 0" is meaningful only once the source normalization is pinned.
    This code always works in the normalized convention C0 = 1 (see analyze()).
    """
    up = F_t
    q = math.exp(-delta_lat * t)
    lo = max(0.0, (F_t - q * C0) / (1.0 - q)) if (1.0 - q) > 1e-12 else float("nan")
    return up, lo


# ============================================================================
# 5. Self-test (no GPU, no numpy)
# ============================================================================

def selftest() -> int:
    fails = 0

    def check(name, cond, detail=""):
        nonlocal fails
        print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))
        if not cond:
            fails += 1

    print("group theory")
    els = oh_elements()
    check("|O_h| = 48", len(els) == 48)
    rots = [g for g in els if elem_det(g) == 1]
    check("|O| = 24", len(rots) == 24)
    from collections import Counter
    cc = Counter(rotation_class(g) for g in rots)
    check("class sizes of O", dict(cc) == CLASS_SIZES, str(dict(cc)))
    for irrep, chars in O_CHARACTERS.items():
        n = sum(CLASS_SIZES[c] * chars[c] ** 2 for c in CLASS_SIZES) / 24
        check(f"<{irrep},{irrep}> = 1", abs(n - 1) < 1e-12, f"got {n}")
    for i1, i2 in itertools.combinations(O_CHARACTERS, 2):
        n = sum(CLASS_SIZES[c] * O_CHARACTERS[i1][c] * O_CHARACTERS[i2][c] for c in CLASS_SIZES) / 24
        check(f"<{i1},{i2}> = 0", abs(n) < 1e-12, f"got {n}")

    print("paths")
    for name, p in PROTOTYPES.items():
        check(f"{name} closed", is_closed(p), str(p))
    check("P11 matches corpus rectangle_path", PROTOTYPES["P11"] == (1, 2, -1, -2))

    print("projection (checked against an independent character decomposition)")
    basis = build_operator_basis()
    ok_all = True
    for pname, path in PROTOTYPES.items():
        # independent route: the signed permutation rep carried by the orbit
        orbit = {}
        for g in oh_elements():
            rep, sgn = canonical(apply_elem(g, path))
            orbit.setdefault(rep, len(orbit))
        chars = {}
        for g in oh_elements():
            tr = 0
            for rep in orbit:
                img, sgn = canonical(apply_elem(g, rep))
                if img == rep:
                    tr += sgn
            chars[g] = tr
        mult = {}
        for irrep in O_CHARACTERS:
            for parity in (+1, -1):
                m = sum(chars[g] * character(irrep, parity, g) for g in oh_elements()) / 48
                if abs(m - round(m)) > 1e-9:
                    ok_all = False
                if round(m) != 0:
                    mult[f"{irrep}{'+' if parity > 0 else '-'}"] = round(m)
        got = {op.name.split(":")[1] for op in basis if op.prototype == pname}
        want = {k for k in mult if k in {f"{i}{'+' if p > 0 else '-'}" for i, p in TARGET_CHANNELS}}
        match = got == want
        ok_all &= match
        print(f"    {pname:<5} orbit={len(orbit):>3}  decomposition={mult}")
        if not match:
            print(f"          MISMATCH projector={sorted(got)} characters={sorted(want)}")
    check("projector agrees with character decomposition for every prototype", ok_all)
    t1 = sorted({op.prototype for op in basis if op.irrep == "T1"})
    a2 = sorted({op.prototype for op in basis if op.irrep == "A2"})
    t2 = sorted({op.prototype for op in basis if op.irrep == "T2"})
    print(f"    T1+ from {t1}")
    print(f"    A2+ from {a2}")
    print(f"    T2+ from {t2}")
    check("carrier channel T1+ is reachable", len(t1) > 0)
    check("A2+ partner channel is reachable", len(a2) > 0, f"{a2}")
    check("T2+ partner channel is reachable", len(t2) > 0, f"{t2}")
    # Verified above, not assumed: the SQUARE plaquette carries T1+ alone (matching
    # the exact Sym^3 result), but an ASYMMETRIC planar rectangle is not symmetric
    # under swapping its in-plane axes, so its orbit is 6 rather than 3 and carries
    # T1+ (+) T2+.  A2+ is the one that genuinely demands non-planar loops.
    check("square plaquette carries T1+ alone",
          {op.name.split(":")[1] for op in basis if op.prototype == "P11"} == {"T1+"})
    check("T2+ IS reachable from the planar 1x2 rectangle", "P12" in t2, f"{t2}")
    check("A2+ requires non-planar loops",
          all(pp not in {"P11", "P12", "P22"} for pp in a2), f"a2={a2}")
    check("X6a is the cheapest A2+ source (orbit 4)", "X6a" in a2)

    print("scale setting")
    r0a = 1.0 / necco_sommer_a_over_r0(6.0)
    check("Necco-Sommer r0/a at beta=6", abs(r0a - 5.368) < 0.01, f"got {r0a:.4f}")
    for e in default_ensembles():
        print(f"    beta={e.beta}  a={e.a:.4f} fm  L={e.L}  T={e.T}  box={e.box_fm:.2f} fm")

    print("Z-bound algebra (normalization is load-bearing)")
    F, D, t = 0.62, 0.40, 6
    up, lo = z_bounds(F, D, t, C0=1.0)
    check("Z upper = F(t)", abs(up - F) < 1e-15)
    check("Z lower <= Z upper", lo <= up + 1e-15, f"lo={lo:.6f} up={up:.6f}")
    Z = 0.5
    F_edge = Z + (1 - Z) * math.exp(-D * t)
    _, lo_edge = z_bounds(F_edge, D, t, C0=1.0)
    check("lower bound sharp at the gap edge", abs(lo_edge - Z) < 1e-12, f"got {lo_edge:.12f}")
    # the trap: mu = delta_M + 9 delta_{M+Delta}, q = 1/2  =>  Z = 1, C0 = 10, F = 5.5
    Dx = 0.7
    tx = math.log(2.0) / Dx
    Fx = 1.0 + 9.0 * math.exp(-Dx * tx)
    _, lo_bad = z_bounds(Fx, Dx, tx, C0=1.0)     # WRONG C0 on purpose
    _, lo_ok = z_bounds(Fx, Dx, tx, C0=10.0)
    check("C0-free bound is unsound when C0 != 1", lo_bad > 1.0 + 1e-9,
          f"returns {lo_bad:.4f} for a measure with Z = 1")
    check("C0-corrected bound is sound and sharp here", abs(lo_ok - 1.0) < 1e-9,
          f"got {lo_ok:.9f}")

    print(f"\n{'ALL PASS' if fails == 0 else str(fails) + ' FAILURE(S)'}")
    return fails


# ============================================================================
# 6. Driver
# ============================================================================

def plan(args):
    ens = default_ensembles(args.box_fm)
    ops = build_operator_basis()
    print(f"target box {args.box_fm} fm; r0 = {R0_FM} fm; {len(ops)} projected operators")
    print(f"{'beta':>6} {'a (fm)':>8} {'L':>4} {'T':>4} {'box':>6} "
          f"{'rho/a (0.20fm)':>15} {'tau/a^2':>9} {'links':>12} {'GiB(c64)':>9}")
    total = 0.0
    for e in ens:
        tau = flow_time_lattice(0.20, e.a)
        nlink = e.T * e.L ** 3 * 4
        gib = nlink * 9 * 8 / 2 ** 30
        total += gib
        print(f"{e.beta:>6} {e.a:>8.4f} {e.L:>4} {e.T:>4} {e.box_fm:>6.2f} "
              f"{0.20/e.a:>15.2f} {tau:>9.3f} {nlink:>12,} {gib:>9.2f}")
    print(f"\npeak field memory ~{max(1.0, total):.1f} GiB; A100-40GB is comfortable.")
    print(f"smearing radii (fm): {DEFAULT_RHO_FM}   (rho=0 is the bare a^9 test)")
    print("\noperator basis:")
    for op in ops:
        print(f"  {op.name:<12} {op.n_paths:>3} distinct paths")


def run(args):
    import numpy as np
    os.makedirs(args.out, exist_ok=True)
    ckpt_every = int(getattr(args, "checkpoint_every", 0) or 0)
    ops = build_operator_basis()
    ens_list = default_ensembles(args.box_fm)
    for e in ens_list:
        t_start = time.time()
        print(f"\n=== beta={e.beta} L={e.L} T={e.T} a={e.a:.4f} fm ===", flush=True)
        lat = Lattice(e, device=args.device, dtype=args.dtype, seed=args.seed)
        rhos_pre = [float(r) for r in args.rho] if args.rho else list(DEFAULT_RHO_FM)
        ck = os.path.join(args.out, f"ckpt_b{e.beta}_L{e.L}.npz")
        start_meas, resumed = 0, None
        if ckpt_every and os.path.exists(ck):
            z = np.load(ck, allow_pickle=True)
            import torch as _T
            lat.U = _T.from_numpy(z["U"]).to(lat.device).to(lat.cdtype)
            start_meas = int(z["n_done"])
            resumed = {float(r): list(v) for r, v in
                       zip(z["rhos"], np.load(ck, allow_pickle=True)["series"])}
            print(f"  resumed from {ck} at measurement {start_meas}", flush=True)
        for i in (range(e.n_therm) if start_meas == 0 else range(0)):
            lat.heatbath_sweep()
            for _ in range(e.n_or):
                lat.overrelax_sweep()
            if (i + 1) % 200 == 0:
                print(f"  therm {i+1}/{e.n_therm}  plaq={lat.plaquette():.6f}", flush=True)
        rhos = rhos_pre
        series = {r: (resumed.get(r, []) if resumed else []) for r in rhos}
        t0_meas = []
        for m in range(start_meas, e.n_meas):
            for _ in range(e.n_sep):
                lat.heatbath_sweep()
                for _ in range(e.n_or):
                    lat.overrelax_sweep()
            spatial = lat.U[..., 1:4, :, :]
            prev_tau = 0.0
            flowed = spatial.clone()
            for r in sorted(rhos):
                tau = flow_time_lattice(r, e.a)
                if tau > prev_tau:
                    flowed = lat.gradient_flow(flowed, tau - prev_tau, eps=args.flow_eps,
                                               spatial_only=True)
                    prev_tau = tau
                series[r].append(lat.measure_operators(flowed, ops))
            if args.t0 and m % 20 == 0:
                V = lat.U.clone()
                rec = []
                tt = 0.0
                while tt < 1.5:
                    V = lat.gradient_flow(V, 0.05, eps=args.flow_eps, spatial_only=False)
                    tt += 0.05
                    rec.append((tt, tt * tt * lat.clover_energy(V)))
                t0_meas.append(rec)
            if (m + 1) % 100 == 0:
                print(f"  meas {m+1}/{e.n_meas}  ({time.time()-t_start:.0f}s)", flush=True)
            if ckpt_every and (m + 1) % ckpt_every == 0:
                np.savez_compressed(
                    ck, U=lat.U.detach().cpu().numpy(), n_done=m + 1,
                    rhos=np.array(sorted(rhos)),
                    series=np.array([np.stack(series[r]) for r in sorted(rhos)], dtype=object),
                )
                print(f"    checkpoint @ {m+1}", flush=True)
        path = os.path.join(args.out, f"carrier_b{e.beta}_L{e.L}.npz")
        np.savez_compressed(
            path,
            beta=e.beta, L=e.L, T=e.T, a_fm=e.a,
            op_names=np.array([o.name for o in ops]),
            rhos=np.array(sorted(rhos)),
            series=np.stack([np.stack(series[r]) for r in sorted(rhos)]),
            t0_meas=np.array(t0_meas, dtype=object) if t0_meas else np.array([]),
        )
        print(f"  wrote {path}")
    print("\nnow:  python carrier_scaling.py --analyze", os.path.join(args.out, "*.npz"))


def analyze(args):
    import numpy as np
    import glob
    files = sorted(itertools.chain.from_iterable(glob.glob(p) for p in args.files))
    rows = []
    for f in files:
        d = np.load(f, allow_pickle=True)
        beta, L, T, a = float(d["beta"]), int(d["L"]), int(d["T"]), float(d["a_fm"])
        names = [str(s) for s in d["op_names"]]
        rhos = d["rhos"]
        S = d["series"]                        # [n_rho, n_cfg, n_ops, T]
        for ir, rho in enumerate(rhos):
            x = bin_configs(S[ir], args.block)
            C_all = correlators(x)             # [n_bin, n_ops, n_ops, T]
            boot = bootstrap(C_all, args.n_boot, seed=args.seed)
            t0g, tg = args.gevp_t0, args.gevp_t
            for chan in ("T1", "A2", "T2"):
                sel = [i for i, n in enumerate(names) if f":{chan}+" in n]
                if not sel:
                    continue
                Zs, Ms, Ds, Fs, Los = [], [], [], [], []
                for b in range(boot.shape[0]):
                    Cb = boot[b][np.ix_(sel, sel)]
                    try:
                        lam = gevp(Cb, t0g, tg, n_states=2)
                    except Exception:
                        continue
                    m0 = -math.log(max(lam[0], 1e-300)) / max(tg - t0g, 1)
                    m1 = -math.log(max(lam[1], 1e-300)) / max(tg - t0g, 1)
                    delta = max(m1 - m0, 1e-9)
                    # residue of the FIRST (physical) operator in the channel
                    c = Cb[0, 0]
                    # normalized convention: F(0) = 1, so C0 = 1 below by construction
                    F = math.exp(m0 * args.z_t) * c[args.z_t] / max(c[0], 1e-300)
                    up, lo = z_bounds(F, delta, args.z_t, C0=1.0)
                    Ms.append(m0); Ds.append(delta); Fs.append(F); Zs.append(up); Los.append(lo)
                if not Ms:
                    continue
                q = lambda v: (float(np.mean(v)), float(np.std(v, ddof=1)))
                rows.append(dict(beta=beta, a_fm=a, L=L, rho_fm=float(rho), channel=chan,
                                 aM=q(Ms), aDelta=q(Ds), F=q(Fs),
                                 Z_upper=q(Zs), Z_lower=q(Los), op=names[sel[0]]))
    print(f"\n{'beta':>5} {'a(fm)':>7} {'rho':>5} {'chan':>4} {'aM':>16} {'aDelta':>16} "
          f"{'Z_upper':>16} {'Z_lower':>16}")
    for r in rows:
        f2 = lambda p: f"{p[0]:.4f}({p[1]:.4f})"
        print(f"{r['beta']:>5} {r['a_fm']:>7.4f} {r['rho_fm']:>5.2f} {r['channel']:>4} "
              f"{f2(r['aM']):>16} {f2(r['aDelta']):>16} {f2(r['Z_upper']):>16} {f2(r['Z_lower']):>16}")

    print("\n--- THE SCALING TEST ---")
    for rho in sorted({r["rho_fm"] for r in rows}):
        pts = [(r["a_fm"], r["Z_upper"][0]) for r in rows if r["channel"] == "T1" and r["rho_fm"] == rho]
        if len(pts) < 2:
            continue
        pts.sort()
        la = [math.log(p[0]) for p in pts]
        lz = [math.log(max(p[1], 1e-300)) for p in pts]
        n = len(la)
        mx, my = sum(la) / n, sum(lz) / n
        num = sum((x - mx) * (y - my) for x, y in zip(la, lz))
        den = sum((x - mx) ** 2 for x in la) or 1e-30
        slope = num / den
        verdict = ("CONSISTENT WITH a^9  -> smearing premise in trouble" if slope > 5
                   else "FLAT  -> residue survives; hypothesis not refuted" if abs(slope) < 1.5
                   else "intermediate")
        tag = "BARE" if rho == 0 else f"rho={rho:.2f} fm"
        print(f"  {tag:<14} d log Z / d log a = {slope:+.2f}   {verdict}")
    print("\nreminder, stated precisely:")
    print("  Z_upper = F(t) is an UPPER bound (F decreases to Z).  Only Z_lower, which")
    print("  needs aDelta, bounds the residue from below.")
    print("  A finite run REFUTES a SPECIFIED bound Z_a >= z_* when a controlled upper")
    print("  confidence limit on F_a(t) falls below z_*.  A downward TREND over three")
    print("  spacings is evidence, not a refutation: the values may fall to a positive")
    print("  plateau.  No finite set of points can rule out every positive z_*.")
    print("  aDelta is a gap in the SOURCE's own measure; it suffices only if no")
    print("  continuum or unobserved source-visible weight begins earlier.  A stability")
    print("  theorem needs the stronger full-sector gap, including dark states.")
    with open(args.json_out, "w") as fh:
        json.dump(rows, fh, indent=2)
    print(f"\nwrote {args.json_out}")


# ============================================================================
# 6a. Notebook / Colab API
# ============================================================================
# In Jupyter/Colab, sys.argv carries the kernel's own "-f kernel.json", which
# argparse rejects.  Use these functions from a cell instead of the CLI.
#
#     import carrier_scaling as cs
#     cs.nb_selftest()
#     cs.nb_plan()
#     cs.nb_run(quick=True)          # ~minutes: validates the whole pipeline
#     cs.nb_run(device="cuda")       # the real campaign
#     cs.nb_analyze("out/*.npz")

from types import SimpleNamespace


def _defaults(**over):
    d = dict(device="cuda", dtype="complex64", out="out", box_fm=1.9, rho=None,
             flow_eps=0.01, t0=False, seed=20260822, block=10, n_boot=400,
             gevp_t0=2, gevp_t=4, z_t=4, json_out="carrier_scaling.json", files=None,
             checkpoint_every=0)
    d.update(over)
    return SimpleNamespace(**d)


def _in_notebook() -> bool:
    try:
        from IPython import get_ipython  # type: ignore
        return get_ipython() is not None
    except Exception:
        return False


#: tiny ensembles: wrong physics, right code path.  Run this FIRST.
def quick_ensembles() -> List[Ensemble]:
    return [Ensemble(beta=5.85, L=6, T=12, n_therm=30, n_meas=20, n_sep=2, n_or=2),
            Ensemble(beta=6.00, L=6, T=12, n_therm=30, n_meas=20, n_sep=2, n_or=2)]


def nb_selftest() -> int:
    return selftest()


def nb_plan(box_fm: float = 1.9):
    return plan(_defaults(box_fm=box_fm))


def nb_run(device: str = "auto", quick: bool = False, colab: bool = False, **kw):
    """Run the campaign.

    quick=True   6^3x12 toys, minutes -- validates the code path, no physics.
    colab=True   reduced statistics sized to finish in one Colab session.
    Pass checkpoint_every=25 to survive a disconnect; re-run the same cell to resume.
    """
    args = _defaults(device=pick_device(device), **kw)
    global _ENSEMBLE_OVERRIDE
    if colab and not quick:
        args.out = kw.get("out", "out_colab")
        _ENSEMBLE_OVERRIDE = colab_ensembles()
        try:
            return run(args)
        finally:
            _ENSEMBLE_OVERRIDE = None
    if quick:
        args.out = kw.get("out", "out_quick")
        _ENSEMBLE_OVERRIDE = quick_ensembles()
        try:
            return run(args)
        finally:
            _ENSEMBLE_OVERRIDE = None
    return run(args)



def pick_device(device: str = "auto") -> str:
    """Resolve a device string.  On ROCm, PyTorch still calls the device 'cuda'."""
    if device != "auto":
        return device
    try:
        import torch
        if torch.cuda.is_available():
            return "cuda"
    except Exception:
        pass
    return "cpu"


def nb_check_gpu(device: str = "auto"):
    """Preflight: exercise EVERY torch op this script depends on, on THIS card.

    Written because the ROCm path here has never been executed.  Run it before
    nb_bench and before any campaign.  A failure here is a one-line fix; the same
    failure 40 minutes into a run is not.
    """
    import torch
    dev = pick_device(device)
    print(f"torch {torch.__version__}   device -> {dev}")
    print(f"  built for ROCm/HIP : {getattr(torch.version, 'hip', None)}")
    print(f"  built for CUDA     : {getattr(torch.version, 'cuda', None)}")
    if dev.startswith("cuda"):
        try:
            print(f"  gpu   : {torch.cuda.get_device_name(0)}")
            free, tot = torch.cuda.mem_get_info()
            print(f"  vram  : {tot/2**30:.1f} GiB total, {free/2**30:.1f} GiB free")
        except Exception as ex:
            print(f"  (device query failed: {ex})")
    D = torch.device(dev)
    fails = []

    def t(name, fn):
        try:
            fn()
            print(f"  [ok]   {name}")
        except Exception as ex:
            print(f"  [FAIL] {name}: {type(ex).__name__}: {ex}")
            fails.append(name)

    n = 4096
    A = torch.randn(n, 3, 3, dtype=torch.complex64, device=D)
    B = torch.randn(n, 3, 3, dtype=torch.complex64, device=D)
    t("complex64 batched matmul  A @ B", lambda: (A @ B).sum().item())
    t("complex64 adjoint         .conj().transpose", lambda: (A.conj().transpose(-2, -1) @ B).sum().item())
    t("complex einsum trace      '...ii->...'", lambda: torch.einsum("...ii->...", A).sum().item())
    t("torch.roll on complex", lambda: torch.roll(A, 1, dims=0).sum().item())
    t("torch.linalg.vector_norm complex", lambda: torch.linalg.vector_norm(A[:, 0, :], dim=-1).sum().item())
    t("torch.linalg.cross complex", lambda: torch.linalg.cross(A[:, 0, :].conj(), A[:, 1, :].conj()).sum().item())
    t("torch.complex(re, im)", lambda: torch.complex(A.real[:, 0, 0], A.imag[:, 0, 0]).sum().item())
    t("torch.where on complex", lambda: torch.where(torch.rand(n, device=D) > .5, A[:, 0, 0], A[:, 1, 1]).sum().item())
    g = torch.Generator(device=D).manual_seed(0)
    t("device Generator + rand", lambda: torch.rand(n, generator=g, device=D).sum().item())
    t("float32 trig / log on device",
      lambda: (torch.cos(torch.rand(n, device=D)) + torch.log(torch.rand(n, device=D).clamp(min=1e-9))).sum().item())
    t("complex128 batched matmul (fallback dtype)",
      lambda: (A.to(torch.complex128) @ B.to(torch.complex128)).sum().item())

    print()
    if fails:
        print(f"{len(fails)} FAILURE(S): {fails}")
        print("If only the complex64 matmul failed, try dtype='complex128'.")
        print("If torch.linalg.cross failed, tell me -- reunitarize() can avoid it.")
    else:
        print("ALL OPS OK -- the lattice code path should run on this device.")
    return len(fails)


def nb_bench(device: str = "auto", L: int = 8, T: int = 16, beta: float = 6.0,
             n_sweep: int = 3, rho_fm: float = 0.20):
    """Time the hot loops on THIS machine and project the real campaign cost.

    Run this before committing to anything.  It is the difference between a
    campaign and a session that dies at hour three.
    """
    import time as _t
    e = Ensemble(beta=beta, L=L, T=T)
    device = pick_device(device)
    lat = Lattice(e, device=device, dtype="complex64", seed=1)
    ops = build_operator_basis()

    def timeit(fn, n):
        try:
            import torch
            if device.startswith("cuda"):
                torch.cuda.synchronize()
        except Exception:
            pass
        t0 = _t.time()
        for _ in range(n):
            fn()
        try:
            import torch
            if device.startswith("cuda"):
                torch.cuda.synchronize()
        except Exception:
            pass
        return (_t.time() - t0) / n

    for _ in range(2):
        lat.heatbath_sweep()
    t_hb = timeit(lat.heatbath_sweep, n_sweep)
    t_or = timeit(lat.overrelax_sweep, n_sweep)
    tau = flow_time_lattice(rho_fm, e.a)
    sp = lat.U[..., 1:4, :, :]
    t_fl = timeit(lambda: lat.gradient_flow(sp, tau, eps=0.01, spatial_only=True), 1)
    t_ms = timeit(lambda: lat.measure_operators(sp, ops), 1)
    vol = T * L ** 3
    print(f"benchmark on {device}, {L}^3x{T} (vol {vol:,})")
    print(f"  heatbath sweep      {t_hb*1e3:8.1f} ms")
    print(f"  overrelax sweep     {t_or*1e3:8.1f} ms")
    print(f"  spatial flow to rho={rho_fm}fm  {t_fl*1e3:8.1f} ms")
    print(f"  measure {len(ops)} operators   {t_ms*1e3:8.1f} ms")
    print()
    print("projected wall clock (scaling by volume; ignores memory-bandwidth cliffs):")
    print(f"{'beta':>6} {'L':>4} {'T':>4} {'therm':>9} {'measure':>10} {'TOTAL':>10}")
    for ens in default_ensembles():
        f = (ens.T * ens.L ** 3) / vol
        per_step = (t_hb + ens.n_or * t_or) * f
        therm = ens.n_therm * per_step
        meas = ens.n_meas * (ens.n_sep * per_step + 5 * (t_fl + t_ms) * f)
        tot = therm + meas
        hrs = lambda x: f"{x/3600:.1f} h" if x > 3600 else f"{x/60:.0f} min"
        print(f"{ens.beta:>6} {ens.L:>4} {ens.T:>4} {hrs(therm):>9} {hrs(meas):>10} {hrs(tot):>10}")
    print()
    print("Colab sessions cap out around 12 h and disconnect on idle.  If TOTAL exceeds")
    print("a couple of hours, use nb_run(..., checkpoint_every=25) and re-run the same")
    print("cell after each reconnect -- it resumes from the last checkpoint.")
    print("Scale statistics with colab_ensembles() if you need a first pass today.")


def colab_ensembles(box_fm: float = 1.6) -> List[Ensemble]:
    """Reduced statistics that can realistically finish in a Colab session.

    Honest about what it costs: error bars roughly 3x the full campaign, and the
    coarsest/finest lever arm is shorter.  Good enough to see whether Z_a falls
    off a cliff; not good enough to quote a scaling exponent.
    """
    out = []
    for beta in (5.85, 6.00, 6.20):
        a = a_fm(beta)
        L = int(round(box_fm / a / 2.0)) * 2
        out.append(Ensemble(beta=beta, L=L, T=2 * L,
                            n_therm=300, n_meas=400, n_sep=4, n_or=3))
    return out


def nb_analyze(pattern="out/*.npz", **kw):
    args = _defaults(**kw)
    args.files = [pattern] if isinstance(pattern, str) else list(pattern)
    return analyze(args)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--selftest", action="store_true")
    p.add_argument("--plan", action="store_true")
    p.add_argument("--run", action="store_true")
    p.add_argument("--analyze", dest="files", nargs="*")
    p.add_argument("--device", default="auto")
    p.add_argument("--dtype", default="complex64", choices=["complex64", "complex128"])
    p.add_argument("--out", default="out")
    p.add_argument("--box-fm", dest="box_fm", type=float, default=1.9)
    p.add_argument("--rho", nargs="*", default=None)
    p.add_argument("--flow-eps", dest="flow_eps", type=float, default=0.01)
    p.add_argument("--t0", action="store_true", help="also measure t0 for scale cross-check")
    p.add_argument("--seed", type=int, default=20260822)
    p.add_argument("--block", type=int, default=10)
    p.add_argument("--n-boot", dest="n_boot", type=int, default=400)
    p.add_argument("--gevp-t0", dest="gevp_t0", type=int, default=2)
    p.add_argument("--gevp-t", dest="gevp_t", type=int, default=4)
    p.add_argument("--z-t", dest="z_t", type=int, default=4, help="t for F(t) / Z bounds")
    p.add_argument("--json-out", dest="json_out", default="carrier_scaling.json")
    p.add_argument("--checkpoint-every", dest="checkpoint_every", type=int, default=0,
                   help="save gauge field + partial data every N measurements (Colab)")
    import sys
    argv = sys.argv[1:]
    if _in_notebook() or os.path.basename(sys.argv[0]).startswith(("colab_kernel", "ipykernel")):
        # Jupyter injects "-f /path/kernel.json"; drop unknown args rather than exit
        a, unknown = p.parse_known_args([x for x in argv if not x.startswith("-f")])
        if not any([a.selftest, a.plan, a.run, a.files is not None]):
            print(__doc__.split("Usage")[0])
            print("Notebook detected. Use the cell API instead of CLI flags:\n"
                  "    import carrier_scaling as cs\n"
                  "    cs.nb_selftest(); cs.nb_plan()\n"
                  "    cs.nb_run(quick=True)      # smoke test first\n"
                  "    cs.nb_run(device='cuda')   # the campaign\n"
                  "    cs.nb_analyze('out/*.npz')")
            return
    else:
        a = p.parse_args(argv)
    if a.selftest:
        raise SystemExit(selftest())
    if a.plan:
        return plan(a)
    if a.run:
        a.device = pick_device(a.device)
        return run(a)
    if a.files is not None:
        return analyze(a)
    p.print_help()


if __name__ == "__main__":
    main()
