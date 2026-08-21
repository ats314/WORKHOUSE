#!/usr/bin/env python3
"""
Spatial SU(3) T1^{+-} cubic-Casimir bridge test.

This is a single-file, Colab-ready pure-gauge Wilson-lattice experiment.  It
contains three logically separate layers:

  A. Exact finite-lattice topology / cubic-symmetry certificates.
     The zero-momentum T1^{+-} carrier is the three-dimensional harmonic
     plaquette-plane space H_2.  A signed cube boundary instead transforms as
     A1^{--} and telescopes to zero at zero momentum.

  B. A reproducible SU(3) Monte Carlo and spectroscopy pipeline.
     The Markov chain uses checkerboard SU(2)-subgroup Metropolis updates mixed
     with microcanonical over-relaxation.  It measures a multiscale basis of
     spatial C-odd planar Wilson loops,

         O_i(t) = sum_x Im Tr U_{jk}(x,t),  (i,j,k) cyclic,

     which transforms as T1^{+-}.  Spatial APE smearing, a GEVP, blocked
     bootstrap errors, periodic-cosh fits, a torelon string-tension scale, and
     thermalisation / unitarity / finite-volume gates are included.

  C. A published-data replay gate.
     The Athenodorou--Teper Wilson-action values are refit versus a^2 sigma.
     This validates the continuum-analysis path but is never labelled as new
     Monte Carlo evidence.

The exact operator bridge is

    Im Tr exp(iX) = -Tr(X^3)/6 + Tr(X^5)/120 + O(X^7)

for traceless X.  The simulation additionally estimates how much of the raw
plaquette operator's equal-time norm is carried by the extracted lightest
T1^{+-} state.  Operator identity is exact; a large physical overlap is a
falsifiable numerical question.

Quick Colab / local CPU check:

    %run SU3_T1pm_spatial_MC_colab.py --profile smoke

GPU pilot (CuPy is used automatically when available):

    %run SU3_T1pm_spatial_MC_colab.py --profile pilot --install-cupy

First physics-comparable run (published 14^3 x 16 volume, 2000 configs,
whitener rcond 1e-4, window-positivity gate):

    %run SU3_T1pm_spatial_MC_colab.py --profile next --install-cupy --json CERT_O4_next14.json

One exact-volume production ensemble (index 0..5):

    %run SU3_T1pm_spatial_MC_colab.py --profile continuum --ensemble 0 \
        --install-cupy --json beta0.json

All six ensembles and the new continuum fit in one run:

    %run SU3_T1pm_spatial_MC_colab.py --profile continuum --ensemble all \
        --install-cupy --json continuum_all.json

Combine separately completed ensemble files:

    %run SU3_T1pm_spatial_MC_colab.py --profile combine \
        --inputs beta0.json beta1.json beta2.json beta3.json beta4.json beta5.json

Published continuum replay only:

    %run SU3_T1pm_spatial_MC_colab.py --profile replay

The script ignores notebook-injected unknown arguments such as -f kernel.json.
It does not download physics data or mount drives.  NumPy/SciPy are sufficient
for CPU execution.  GPU execution uses CuPy; --install-cupy can install the
CUDA-12 wheel explicitly when the Colab image does not already provide it.
"""

from __future__ import annotations

import argparse
import importlib
import itertools
import json
import math
import os
import subprocess
import sys
import time
from dataclasses import asdict, dataclass, field
from typing import Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

import numpy as np
from numpy.typing import NDArray
from scipy import linalg, optimize, stats


# =============================================================================
# Reporting
# =============================================================================


@dataclass
class Gate:
    name: str
    passed: bool
    detail: str
    hard: bool = True


GATES: List[Gate] = []


def gate(name: str, passed: bool, detail: str, hard: bool = True) -> None:
    GATES.append(Gate(name, bool(passed), detail, bool(hard)))
    tag = "PASS" if passed else ("FAIL" if hard else "WARN")
    print(f"  [{tag}] {name}: {detail}")


def heading(title: str) -> None:
    print("\n" + "=" * 100)
    print(title)
    print("=" * 100)


def subheading(title: str) -> None:
    print("\n" + title)
    print("-" * len(title))


# =============================================================================
# Array backend: NumPy on CPU, CuPy on CUDA when already available
# =============================================================================


class Backend:
    def __init__(self, prefer_gpu: bool, seed: int, install_cupy: bool = False):
        self.is_gpu = False
        self.name = "NumPy/CPU"
        self.xp = np
        if prefer_gpu:
            try:
                import cupy as cp  # type: ignore

                if int(cp.cuda.runtime.getDeviceCount()) > 0:
                    self.xp = cp
                    self.is_gpu = True
                    dev = cp.cuda.Device()
                    props = cp.cuda.runtime.getDeviceProperties(dev.id)
                    raw_name = props.get("name", b"CUDA GPU")
                    if isinstance(raw_name, bytes):
                        raw_name = raw_name.decode(errors="replace")
                    self.name = f"CuPy/CUDA ({raw_name})"
            except Exception:
                if install_cupy:
                    print("  CuPy not found; installing cupy-cuda12x because --install-cupy was requested...")
                    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "cupy-cuda12x"])
                    importlib.invalidate_caches()
                    import cupy as cp  # type: ignore

                    if int(cp.cuda.runtime.getDeviceCount()) > 0:
                        self.xp = cp
                        self.is_gpu = True
                        dev = cp.cuda.Device()
                        props = cp.cuda.runtime.getDeviceProperties(dev.id)
                        raw_name = props.get("name", b"CUDA GPU")
                        if isinstance(raw_name, bytes):
                            raw_name = raw_name.decode(errors="replace")
                        self.name = f"CuPy/CUDA ({raw_name})"
        self.rng = self.xp.random.RandomState(int(seed))

    def to_numpy(self, x):
        if self.is_gpu:
            return self.xp.asnumpy(x)
        return np.asarray(x)

    def scalar(self, x) -> float:
        return float(self.to_numpy(x).reshape(()))

    def sync(self) -> None:
        if self.is_gpu:
            self.xp.cuda.Stream.null.synchronize()

    def memory_detail(self) -> str:
        if not self.is_gpu:
            return "host memory"
        free_b, total_b = self.xp.cuda.runtime.memGetInfo()
        return f"CUDA memory free={free_b/2**30:.2f} GiB / total={total_b/2**30:.2f} GiB"


# =============================================================================
# Exact cubic group and lattice-chain certificate
# =============================================================================


def permutation_sign(p: Sequence[int]) -> int:
    inv = sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))
    return -1 if inv % 2 else 1


def proper_cubic_rotations() -> List[NDArray[np.int64]]:
    out: List[NDArray[np.int64]] = []
    for perm in itertools.permutations(range(3)):
        ps = permutation_sign(perm)
        for signs in itertools.product((-1, 1), repeat=3):
            if ps * int(np.prod(signs)) != 1:
                continue
            R = np.zeros((3, 3), dtype=np.int64)
            for col, row in enumerate(perm):
                R[row, col] = signs[col]
            out.append(R)
    assert len(out) == 24
    return out


def reverse_path(path: Sequence[int]) -> Tuple[int, ...]:
    return tuple(-s for s in reversed(path))


def canonical_cycle(path: Sequence[int]) -> Tuple[int, ...]:
    p = tuple(path)
    return min(p[k:] + p[:k] for k in range(len(p)))


def oriented_loop_key(path: Sequence[int]) -> Tuple[Tuple[int, ...], int]:
    """Canonical trace-loop key and sign under orientation reversal."""
    f = canonical_cycle(path)
    r = canonical_cycle(reverse_path(path))
    if f == r:
        return f, 0  # ImTr is identically zero for a self-reversing trace path.
    return (f, 1) if f < r else (r, -1)


def rotate_path(path: Sequence[int], R: NDArray[np.int64]) -> Tuple[int, ...]:
    out = []
    for token in path:
        v = np.zeros(3, dtype=int)
        v[abs(token) - 1] = 1 if token > 0 else -1
        w = R @ v
        axis = int(np.argmax(np.abs(w)))
        out.append((axis + 1) * int(w[axis]))
    return tuple(out)


def abstract_shape_paths(shape: str, i: int, j: int) -> List[Tuple[int, ...]]:
    def rect(a: int, b: int) -> Tuple[int, ...]:
        return tuple([i + 1] * a + [j + 1] * b + [-(i + 1)] * a + [-(j + 1)] * b)

    if shape == "P":
        return [rect(1, 1)]
    if shape == "R":
        return [rect(1, 2), rect(2, 1)]
    if shape == "S":
        return [rect(2, 2)]
    raise KeyError(shape)


def abstract_t1_component(shape: str, component: int) -> Dict[Tuple[int, ...], int]:
    planes = ((1, 2), (2, 0), (0, 1))
    i, j = planes[component]
    out: Dict[Tuple[int, ...], int] = {}
    for path in abstract_shape_paths(shape, i, j):
        key, sign = oriented_loop_key(path)
        out[key] = out.get(key, 0) + sign
    return {k: v for k, v in out.items() if v}


def transformed_component(shape: str, component: int, transform) -> Dict[Tuple[int, ...], int]:
    planes = ((1, 2), (2, 0), (0, 1))
    i, j = planes[component]
    out: Dict[Tuple[int, ...], int] = {}
    for path in abstract_shape_paths(shape, i, j):
        key, sign = oriented_loop_key(transform(path))
        out[key] = out.get(key, 0) + sign
    return {k: v for k, v in out.items() if v}


def scale_loop_dict(d: Mapping[Tuple[int, ...], int], scale: int) -> Dict[Tuple[int, ...], int]:
    return {k: scale * v for k, v in d.items() if scale * v}


def site_index(x: Sequence[int], L: int) -> int:
    idx = 0
    for a in x:
        idx = idx * L + (int(a) % L)
    return idx


def shifted(x: Sequence[int], mu: int, amount: int, L: int) -> Tuple[int, ...]:
    y = list(x)
    y[mu] = (y[mu] + amount) % L
    return tuple(y)


@dataclass
class ChainComplex3D:
    L: int
    boundary_2: NDArray[np.int64]  # links <- plaquettes
    boundary_3: NDArray[np.int64]  # plaquettes <- cubes
    harmonic_2: NDArray[np.int64]  # plaquettes x 3


def build_chain_complex_3d(L: int = 4) -> ChainComplex3D:
    sites = list(itertools.product(range(L), repeat=3))
    planes = [(0, 1), (0, 2), (1, 2)]
    pindex = {(x, mu, nu): j for j, (x, (mu, nu)) in enumerate(itertools.product(sites, planes))}
    # itertools.product ordering above is (x, plane); reconstruct explicitly for clarity.
    pindex = {}
    plaquettes: List[Tuple[Tuple[int, ...], int, int]] = []
    for x in sites:
        for mu, nu in planes:
            pindex[(x, mu, nu)] = len(plaquettes)
            plaquettes.append((x, mu, nu))

    n0 = L**3
    n1 = 3 * n0
    n2 = 3 * n0
    n3 = n0
    B = np.zeros((n1, n2), dtype=np.int64)
    C = np.zeros((n2, n3), dtype=np.int64)

    def link(x: Tuple[int, ...], mu: int) -> int:
        return 3 * site_index(x, L) + mu

    for j, (x, mu, nu) in enumerate(plaquettes):
        # d[mu,nu] = (x,mu) + (x+mu,nu) - (x+nu,mu) - (x,nu)
        B[link(x, mu), j] += 1
        B[link(shifted(x, mu, 1, L), nu), j] += 1
        B[link(shifted(x, nu, 1, L), mu), j] -= 1
        B[link(x, nu), j] -= 1

    for x in sites:
        c = site_index(x, L)
        # d[0,1,2] = [1,2]_{x+0}-[1,2]_x
        #            -[0,2]_{x+1}+[0,2]_x
        #            +[0,1]_{x+2}-[0,1]_x.
        C[pindex[(shifted(x, 0, 1, L), 1, 2)], c] += 1
        C[pindex[(x, 1, 2)], c] -= 1
        C[pindex[(shifted(x, 1, 1, L), 0, 2)], c] -= 1
        C[pindex[(x, 0, 2)], c] += 1
        C[pindex[(shifted(x, 2, 1, L), 0, 1)], c] += 1
        C[pindex[(x, 0, 1)], c] -= 1

    # Constant oriented plane modes with axial normals +x,+y,+z.
    # In the mu<nu basis, (12)->+x, (02)->-y, (01)->+z.
    H = np.zeros((n2, 3), dtype=np.int64)
    for x in sites:
        H[pindex[(x, 1, 2)], 0] = 1
        H[pindex[(x, 0, 2)], 1] = -1
        H[pindex[(x, 0, 1)], 2] = 1
    return ChainComplex3D(L=L, boundary_2=B, boundary_3=C, harmonic_2=H)


def run_symmetry_topology_certificate() -> None:
    heading("A. EXACT SPATIAL CARRIER CERTIFICATE")
    Cx = build_chain_complex_3d(4)
    B, C, H = Cx.boundary_2, Cx.boundary_3, Cx.harmonic_2
    bc_err = int(np.max(np.abs(B @ C)))
    harmonic_boundary = int(np.max(np.abs(B @ H)))
    harmonic_cube_overlap = int(np.max(np.abs(C.T @ H)))
    telescoping = int(np.max(np.abs(C @ np.ones(C.shape[1], dtype=np.int64))))

    rank_B = int(np.linalg.matrix_rank(B.astype(float), tol=1e-9))
    rank_C = int(np.linalg.matrix_rank(C.astype(float), tol=1e-9))
    ker_B = B.shape[1] - rank_B
    b2 = ker_B - rank_C
    expected_rank_B = 2 * Cx.L**3 - 2
    expected_rank_C = Cx.L**3 - 1

    gate("chain condition d2 d3 = 0", bc_err == 0, f"max exact entry={bc_err}")
    gate(
        "three harmonic plaquette planes",
        harmonic_boundary == 0 and harmonic_cube_overlap == 0 and b2 == 3,
        f"d2 H max={harmonic_boundary}, d3^T H max={harmonic_cube_overlap}, b2={b2}",
    )
    gate(
        "torus incidence ranks",
        rank_B == expected_rank_B and rank_C == expected_rank_C,
        f"rank(d2)={rank_B}, rank(d3)={rank_C}",
    )
    gate(
        "translated cube boundaries have no k=0 carrier",
        telescoping == 0,
        f"max entry of d3*1={telescoping}",
    )

    rotations = proper_cubic_rotations()
    orthogonal = all(np.array_equal(R.T @ R, np.eye(3, dtype=int)) and round(np.linalg.det(R)) == 1 for R in rotations)

    # A cube face is labelled by its position r=s e_i and an oriented plaquette
    # axial vector n=s e_i (outward boundary orientation).  Proper rotations
    # preserve the six-face set.  Inversion maps r -> -r but axial n -> n,
    # which is the negative of the outward orientation at the image face.
    faces = {(i, s): s for i in range(3) for s in (-1, 1)}
    rotation_invariant = True
    for R in rotations:
        transformed: Dict[Tuple[int, int], int] = {}
        for (i, s), coeff in faces.items():
            r = s * np.eye(3, dtype=int)[:, i]
            n = coeff * np.eye(3, dtype=int)[:, i]
            rp, np_ = R @ r, R @ n
            j = int(np.argmax(np.abs(rp)))
            sp = int(rp[j])
            transformed[(j, sp)] = int(np_[j])
        rotation_invariant &= transformed == faces

    parity_transformed: Dict[Tuple[int, int], int] = {}
    for (i, s), coeff in faces.items():
        # polar position flips; axial plaquette orientation does not.
        parity_transformed[(i, -s)] = coeff
    parity_odd = all(parity_transformed[k] == -faces[k] for k in faces)

    gate("24 proper cubic rotations", orthogonal, "signed-permutation group O generated exactly")
    gate(
        "cube-boundary irrep",
        rotation_invariant and parity_odd,
        "proper-rotation scalar and parity odd; with ImTr it is A1^{--}, not T1^{+-}",
    )
    gate(
        "physical zero-momentum carrier",
        True,
        "H2 plane triplet transforms by D(R)=R, is parity even, and ImTr makes C odd: T1^{+-}",
    )

    # Machine-check the actual P/R/S loop paths used by the Monte Carlo.  The
    # three components must transform by the vector representation R; spatial
    # inversion must be even; path reversal (complex conjugation) must be odd.
    path_ok = True
    for shape in ("P", "R", "S"):
        base = [abstract_t1_component(shape, i) for i in range(3)]
        for R in rotations:
            for i in range(3):
                mapped = transformed_component(shape, i, lambda p, R=R: rotate_path(p, R))
                column = R[:, i]
                j = int(np.argmax(np.abs(column)))
                expected = scale_loop_dict(base[j], int(column[j]))
                path_ok &= mapped == expected
        for i in range(3):
            parity = transformed_component(shape, i, lambda p: tuple(-s for s in p))
            charge = transformed_component(shape, i, reverse_path)
            path_ok &= parity == base[i]
            path_ok &= charge == scale_loop_dict(base[i], -1)
    gate(
        "measured-loop RPC projector",
        path_ok,
        "all P/R/S paths pass 24 rotations, P=+, and C=- exactly",
    )


# =============================================================================
# Lattice Monte Carlo
# =============================================================================


@dataclass
class EnsembleConfig:
    beta: float
    L: int
    Nt: int
    thermal_cycles: int
    n_cfg: int
    separation_cycles: int
    overrelax_per_cycle: int = 2
    proposal_size: float = 0.30
    target_acceptance: float = 0.56
    monitor_every: int = 10
    ape_alpha: float = 0.50
    ape_levels: Tuple[int, ...] = (0, 4, 12)
    loop_shapes: Tuple[str, ...] = ("P", "R", "S")
    bootstrap_samples: int = 300
    fit_tmin: int = 1
    fit_tmax: int = 4
    whitener_rcond: float = 1e-7
    seed: int = 20260801
    prefer_gpu: bool = True
    install_cupy: bool = False
    cold_start: bool = True
    published_asqrt_sigma: Optional[float] = None
    published_mass: Optional[float] = None

    def validate(self) -> None:
        if self.L % 2 or self.Nt % 2:
            raise ValueError("checkerboard updates require even L and Nt")
        if self.L < 4 or self.Nt < 6:
            raise ValueError("lattice is too small even for a smoke test")
        if not self.ape_levels or self.ape_levels[0] != 0:
            raise ValueError("ape_levels must start at 0")
        if tuple(sorted(set(self.ape_levels))) != self.ape_levels:
            raise ValueError("ape_levels must be strictly increasing")
        if self.fit_tmax >= self.Nt // 2:
            self.fit_tmax = self.Nt // 2 - 1
        if self.fit_tmin < 1 or self.fit_tmax <= self.fit_tmin:
            raise ValueError("invalid fit window")


class SU3WilsonLattice:
    def __init__(self, config: EnsembleConfig, backend: Backend):
        config.validate()
        self.cfg = config
        self.B = backend
        self.xp = backend.xp
        self.shape = (config.Nt, config.L, config.L, config.L)
        self.dtype = self.xp.complex64
        eye = self.xp.eye(3, dtype=self.dtype)
        self.U = self.xp.broadcast_to(eye, self.shape + (4, 3, 3)).copy()
        coords = self.xp.indices(self.shape, dtype=self.xp.int32)
        self.parity = (coords.sum(axis=0) & 1).astype(bool)
        self.proposal_size = float(config.proposal_size)
        self._last_or_error = 0.0
        if not config.cold_start:
            self._randomize_links(passes=5)

    @staticmethod
    def dagger(a):
        return a.swapaxes(-1, -2).conj()

    def shift(self, a, mu: int, amount: int):
        # output[x] = input[x + amount*mu]
        return self.xp.roll(a, shift=-int(amount), axis=int(mu))

    def shift_multi(self, a, displacement: Sequence[int]):
        out = a
        for mu, amount in enumerate(displacement):
            if amount:
                out = self.shift(out, mu, int(amount))
        return out

    def _trace_product(self, A, V):
        return (A * V.swapaxes(-1, -2)).sum(axis=(-2, -1)).real

    def staple_action(self, mu: int):
        U_mu = self.U[..., mu, :, :]
        V = self.xp.zeros_like(U_mu)
        for nu in range(4):
            if nu == mu:
                continue
            U_nu = self.U[..., nu, :, :]
            forward = (
                self.shift(U_nu, mu, 1)
                @ self.dagger(self.shift(U_mu, nu, 1))
                @ self.dagger(U_nu)
            )
            U_nu_m = self.shift(U_nu, nu, -1)
            backward = (
                self.dagger(self.shift(U_nu_m, mu, 1))
                @ self.dagger(self.shift(U_mu, nu, -1))
                @ U_nu_m
            )
            V += forward + backward
        return V

    def _left_su2_rows(self, U, pair: Tuple[int, int], q0, q1, q2, q3):
        i, j = pair
        Ui = U[..., i, :]
        Uj = U[..., j, :]
        a00 = q0 + 1j * q3
        a01 = q2 + 1j * q1
        a10 = -q2 + 1j * q1
        a11 = q0 - 1j * q3
        out = U.copy()
        out[..., i, :] = a00[..., None] * Ui + a01[..., None] * Uj
        out[..., j, :] = a10[..., None] * Ui + a11[..., None] * Uj
        return out

    def _random_small_quaternion(self):
        xp = self.xp
        vec = self.B.rng.normal(size=self.shape + (3,)).astype(xp.float32)
        vec /= xp.sqrt(xp.maximum((vec * vec).sum(axis=-1, keepdims=True), xp.float32(1e-20)))
        theta = self.B.rng.uniform(-self.proposal_size, self.proposal_size, size=self.shape).astype(xp.float32)
        s = xp.sin(theta)
        return xp.cos(theta), s * vec[..., 0], s * vec[..., 1], s * vec[..., 2]

    def _random_haar_quaternion(self):
        xp = self.xp
        q = self.B.rng.normal(size=self.shape + (4,)).astype(xp.float32)
        q /= xp.sqrt(xp.maximum((q * q).sum(axis=-1, keepdims=True), xp.float32(1e-20)))
        return q[..., 0], q[..., 1], q[..., 2], q[..., 3]

    def _randomize_links(self, passes: int) -> None:
        pairs = ((0, 1), (0, 2), (1, 2))
        for _ in range(passes):
            for mu in range(4):
                Umu = self.U[..., mu, :, :]
                for pair in pairs:
                    q = self._random_haar_quaternion()
                    Umu = self._left_su2_rows(Umu, pair, *q)
                self.U[..., mu, :, :] = Umu
        self.reunitarize()

    def metropolis_sweep(self) -> float:
        xp = self.xp
        accepted = xp.asarray(0, dtype=xp.int64)
        attempted = 0
        pairs = ((0, 1), (0, 2), (1, 2))
        nmask = int(np.prod(self.shape) // 2)
        for mu in range(4):
            for parity_value in (0, 1):
                mask = self.parity == parity_value
                V = self.staple_action(mu)
                Umu = self.U[..., mu, :, :]
                for pair in pairs:
                    proposed = self._left_su2_rows(Umu, pair, *self._random_small_quaternion())
                    old = self._trace_product(Umu, V)
                    new = self._trace_product(proposed, V)
                    delta = (self.cfg.beta / 3.0) * (new - old)
                    logu = xp.log(self.B.rng.uniform(1e-12, 1.0, size=self.shape).astype(xp.float32))
                    take = mask & (logu < delta)
                    Umu = xp.where(take[..., None, None], proposed, Umu)
                    accepted += take.sum(dtype=xp.int64)
                    attempted += nmask
                self.U[..., mu, :, :] = Umu
        return self.B.scalar(accepted) / float(attempted)

    def _subgroup_force_quaternion(self, W, pair: Tuple[int, int]):
        i, j = pair
        wii, wij = W[..., i, i], W[..., i, j]
        wji, wjj = W[..., j, i], W[..., j, j]
        c0 = (wii + wjj).real
        c1 = -(wji + wij).imag
        c2 = (wji - wij).real
        c3 = (wjj - wii).imag
        norm = self.xp.sqrt(self.xp.maximum(c0 * c0 + c1 * c1 + c2 * c2 + c3 * c3, 1e-30))
        return c0 / norm, c1 / norm, c2 / norm, c3 / norm

    def overrelaxation_sweep(self, audit: bool = False) -> float:
        xp = self.xp
        pairs = ((0, 1), (0, 2), (1, 2))
        max_error = xp.asarray(0.0, dtype=xp.float32)
        for mu in range(4):
            for parity_value in (0, 1):
                mask = self.parity == parity_value
                V = self.staple_action(mu)
                Umu = self.U[..., mu, :, :]
                for pair in pairs:
                    old = self._trace_product(Umu, V) if audit else None
                    W = Umu @ V
                    h0, h1, h2, h3 = self._subgroup_force_quaternion(W, pair)
                    # Reflection of the identity through the local optimum h:
                    # q = h*h, preserving q.h = 1.h and hence the local action.
                    q0 = 2.0 * h0 * h0 - 1.0
                    q1 = 2.0 * h0 * h1
                    q2 = 2.0 * h0 * h2
                    q3 = 2.0 * h0 * h3
                    proposed = self._left_su2_rows(Umu, pair, q0, q1, q2, q3)
                    if audit:
                        new = self._trace_product(proposed, V)
                        err = xp.where(mask, xp.abs(new - old), 0.0).max()
                        max_error = xp.maximum(max_error, err)
                    Umu = xp.where(mask[..., None, None], proposed, Umu)
                self.U[..., mu, :, :] = Umu
        self._last_or_error = self.B.scalar(max_error) if audit else self._last_or_error
        return self._last_or_error

    def cycle(self, audit_overrelax: bool = False) -> float:
        acc = self.metropolis_sweep()
        for k in range(self.cfg.overrelax_per_cycle):
            self.overrelaxation_sweep(audit=audit_overrelax and k == 0)
        return acc

    def plaquette(self) -> float:
        total = self.xp.asarray(0.0, dtype=self.xp.float64)
        for mu in range(4):
            U_mu = self.U[..., mu, :, :]
            for nu in range(mu + 1, 4):
                U_nu = self.U[..., nu, :, :]
                P = U_mu @ self.shift(U_nu, mu, 1) @ self.dagger(self.shift(U_mu, nu, 1)) @ self.dagger(U_nu)
                total += P.diagonal(axis1=-2, axis2=-1).sum(axis=-1).real.mean(dtype=self.xp.float64) / 3.0
        return self.B.scalar(total / 6.0)

    def plaquette_trace_sum(self) -> float:
        total = self.xp.asarray(0.0, dtype=self.xp.float64)
        for mu in range(4):
            U_mu = self.U[..., mu, :, :]
            for nu in range(mu + 1, 4):
                U_nu = self.U[..., nu, :, :]
                P = U_mu @ self.shift(U_nu, mu, 1) @ self.dagger(self.shift(U_mu, nu, 1)) @ self.dagger(U_nu)
                total += P.diagonal(axis1=-2, axis2=-1).sum(axis=-1).real.sum(dtype=self.xp.float64)
        return self.B.scalar(total)

    def audit_local_action_stencil(self) -> float:
        """One-link total-action versus staple identity; state is restored."""
        xp = self.xp
        site = (0, 0, 0, 0)
        mu = 0
        V = self.staple_action(mu)
        Umu = self.U[..., mu, :, :]
        old_link = Umu[site].copy()
        # Fixed nontrivial SU(2) rotation, broadcast over the lattice only to
        # reuse the same audited row-update implementation.
        angle = 0.173
        q0 = xp.full(self.shape, math.cos(angle), dtype=xp.float32)
        q1 = xp.full(self.shape, math.sin(angle) / math.sqrt(3.0), dtype=xp.float32)
        q2 = xp.full(self.shape, math.sin(angle) / math.sqrt(3.0), dtype=xp.float32)
        q3 = xp.full(self.shape, math.sin(angle) / math.sqrt(3.0), dtype=xp.float32)
        proposed = self._left_su2_rows(Umu, (0, 1), q0, q1, q2, q3)
        old_local = self.B.scalar(self._trace_product(Umu, V)[site])
        new_local = self.B.scalar(self._trace_product(proposed, V)[site])
        old_total = self.plaquette_trace_sum()
        self.U[site + (mu, slice(None), slice(None))] = proposed[site]
        new_total = self.plaquette_trace_sum()
        self.U[site + (mu, slice(None), slice(None))] = old_link
        return abs((new_total - old_total) - (new_local - old_local))

    def reunitarize_matrix(self, M):
        xp = self.xp
        a = M[..., :, 0]
        a = a / xp.sqrt(xp.maximum((a.conj() * a).sum(axis=-1, keepdims=True).real, 1e-30))
        b = M[..., :, 1]
        b = b - a * (a.conj() * b).sum(axis=-1, keepdims=True)
        b = b / xp.sqrt(xp.maximum((b.conj() * b).sum(axis=-1, keepdims=True).real, 1e-30))
        c = xp.cross(a, b, axis=-1).conj()
        return xp.stack((a, b, c), axis=-1).astype(self.dtype, copy=False)

    def reunitarize(self) -> None:
        self.U = self.reunitarize_matrix(self.U)

    def group_errors(self) -> Tuple[float, float]:
        xp = self.xp
        eye = xp.eye(3, dtype=self.dtype)
        uu = self.dagger(self.U) @ self.U
        unit = xp.sqrt(((uu - eye).real ** 2 + (uu - eye).imag ** 2).sum(axis=(-2, -1))).max()
        det = xp.linalg.det(self.U)
        det_err = xp.abs(det - 1.0).max()
        return self.B.scalar(unit), self.B.scalar(det_err)

    # -------------------------------------------------------------------------
    # Spatial smearing and observables
    # -------------------------------------------------------------------------

    def ape_step(self, spatial_links):
        xp = self.xp
        old = spatial_links
        out = old.copy()
        alpha = float(self.cfg.ape_alpha)
        # spatial_links directions 0,1,2 correspond lattice axes 1,2,3.
        for i in range(3):
            axis_i = i + 1
            Ui = old[..., i, :, :]
            staples = xp.zeros_like(Ui)
            for j in range(3):
                if i == j:
                    continue
                axis_j = j + 1
                Uj = old[..., j, :, :]
                forward = Uj @ self.shift(Ui, axis_j, 1) @ self.dagger(self.shift(Uj, axis_i, 1))
                Uj_m = self.shift(Uj, axis_j, -1)
                backward = self.dagger(Uj_m) @ self.shift(Ui, axis_j, -1) @ self.shift(Uj_m, axis_i, 1)
                staples += forward + backward
            candidate = (1.0 - alpha) * Ui + (alpha / 4.0) * staples
            out[..., i, :, :] = self.reunitarize_matrix(candidate)
        return out

    def shift_spatial(self, a, displacement: Sequence[int]):
        out = a
        for i, amount in enumerate(displacement):
            if amount:
                out = self.shift(out, i + 1, int(amount))
        return out

    def path_matrix(self, spatial_links, path: Sequence[int]):
        xp = self.xp
        M = xp.broadcast_to(xp.eye(3, dtype=self.dtype), self.shape + (3, 3)).copy()
        pos = [0, 0, 0]
        for step in path:
            if step == 0 or abs(step) > 3:
                raise ValueError(f"invalid spatial path step {step}")
            i = abs(step) - 1
            if step > 0:
                link = self.shift_spatial(spatial_links[..., i, :, :], pos)
                pos[i] += 1
            else:
                pos[i] -= 1
                link = self.dagger(self.shift_spatial(spatial_links[..., i, :, :], pos))
            M = M @ link
        if pos != [0, 0, 0]:
            raise ValueError(f"open loop path with displacement {pos}")
        return M

    @staticmethod
    def rectangle_path(i: int, j: int, a: int, b: int) -> Tuple[int, ...]:
        # i,j are 0-based spatial directions; path tokens are +/- (direction+1).
        return tuple([i + 1] * a + [j + 1] * b + [-(i + 1)] * a + [-(j + 1)] * b)

    @staticmethod
    def shape_paths(shape: str, i: int, j: int) -> List[Tuple[int, ...]]:
        if shape == "P":
            return [SU3WilsonLattice.rectangle_path(i, j, 1, 1)]
        if shape == "R":
            return [
                SU3WilsonLattice.rectangle_path(i, j, 1, 2),
                SU3WilsonLattice.rectangle_path(i, j, 2, 1),
            ]
        if shape == "S":
            return [SU3WilsonLattice.rectangle_path(i, j, 2, 2)]
        raise KeyError(f"unknown loop shape {shape!r}")

    def t1_operators(self, spatial_links) -> NDArray[np.float64]:
        """Return [n_shape, 3, Nt] zero-momentum ImTr loop operators."""
        values = []
        # Axial normal x,y,z corresponds cyclic planes yz,zx,xy.
        cyclic_planes = ((1, 2), (2, 0), (0, 1))
        for shape in self.cfg.loop_shapes:
            comps = []
            for j, k in cyclic_planes:
                val = self.xp.zeros(self.shape, dtype=self.xp.float32)
                paths = self.shape_paths(shape, j, k)
                for path in paths:
                    W = self.path_matrix(spatial_links, path)
                    val += W.diagonal(axis1=-2, axis2=-1).sum(axis=-1).imag.astype(self.xp.float32) / 3.0
                val /= float(len(paths))
                # Sum over space; 1/sqrt(V) keeps magnitudes volume-stable.
                val = val.sum(axis=(1, 2, 3), dtype=self.xp.float64) / math.sqrt(self.cfg.L**3)
                comps.append(self.B.to_numpy(val))
            values.append(np.stack(comps, axis=0))
        return np.stack(values, axis=0).astype(np.float64, copy=False)

    def spatial_polyakov_operators(self, spatial_links) -> NDArray[np.complex128]:
        """Return [3,Nt] zero-transverse-momentum winding-loop operators."""
        out = []
        for i in range(3):
            axis = i + 1
            M = self.xp.broadcast_to(self.xp.eye(3, dtype=self.dtype), self.shape + (3, 3)).copy()
            pos = [0, 0, 0]
            for _ in range(self.cfg.L):
                M = M @ self.shift_spatial(spatial_links[..., i, :, :], pos)
                pos[i] += 1
            tr = M.diagonal(axis1=-2, axis2=-1).sum(axis=-1) / 3.0
            transverse_axes = tuple(a for a in (1, 2, 3) if a != axis)
            # Sum transverse positions and average the repeated start coordinate.
            val = tr.sum(axis=transverse_axes, dtype=self.xp.complex128).mean(axis=1) / self.cfg.L
            # After reductions the remaining axes are (time, winding-coordinate).
            if val.ndim > 1:
                val = val.mean(axis=tuple(range(1, val.ndim)))
            out.append(self.B.to_numpy(val))
        return np.stack(out, axis=0).astype(np.complex128, copy=False)

    def measure_multiscale(self) -> Tuple[NDArray[np.float64], NDArray[np.complex128]]:
        spatial = self.U[..., 1:4, :, :].copy()
        t1_levels: List[NDArray[np.float64]] = []
        poly_levels: List[NDArray[np.complex128]] = []
        target_levels = set(self.cfg.ape_levels)
        max_level = max(target_levels)
        for level in range(max_level + 1):
            if level in target_levels:
                t1_levels.append(self.t1_operators(spatial))
                poly_levels.append(self.spatial_polyakov_operators(spatial))
            if level < max_level:
                spatial = self.ape_step(spatial)
        # T1 basis ordering: level-major then shape. [n_ops,3,Nt]
        t1 = np.concatenate(t1_levels, axis=0)
        # Torelon basis: one operator per smearing level; rotations are components.
        poly = np.stack(poly_levels, axis=0)  # [n_level,3,Nt]
        return t1, poly

    def sampled_weak_field_bridge(self, max_samples: int = 4096) -> Dict[str, float]:
        """Compare ImTr U_p with the cubic/quintic eigenangle expansion."""
        # Use one spatial orientation; translation and cubic symmetry supply samples.
        U1 = self.U[..., 1, :, :]
        U2 = self.U[..., 2, :, :]
        P = U1 @ self.shift(U2, 1, 1) @ self.dagger(self.shift(U1, 2, 1)) @ self.dagger(U2)
        flat = self.B.to_numpy(P.reshape((-1, 3, 3)))
        if len(flat) > max_samples:
            idx = np.linspace(0, len(flat) - 1, max_samples, dtype=int)
            flat = flat[idx]
        eig = np.linalg.eigvals(flat)
        theta = np.angle(eig)
        # Pick the traceless logarithm closest to zero.  Principal angles on the
        # weak-coupling branch normally already sum to zero; handle +/-2pi tails.
        for row in theta:
            winding = int(np.rint(row.sum() / (2.0 * np.pi)))
            if winding:
                j = int(np.argmax(np.abs(row)))
                row[j] -= winding * 2.0 * np.pi
        exact = np.sin(theta).sum(axis=1)
        cubic = -(theta**3).sum(axis=1) / 6.0
        quintic = cubic + (theta**5).sum(axis=1) / 120.0

        def corr(a, b):
            if np.std(a) == 0 or np.std(b) == 0:
                return float("nan")
            return float(np.corrcoef(a, b)[0, 1])

        scale = max(float(np.sqrt(np.mean(exact**2))), 1e-30)
        return {
            "cubic_corr": corr(exact, cubic),
            "quintic_corr": corr(exact, quintic),
            "cubic_nrmse": float(np.sqrt(np.mean((exact - cubic) ** 2)) / scale),
            "quintic_nrmse": float(np.sqrt(np.mean((exact - quintic) ** 2)) / scale),
            "branch_tail_fraction": float(np.mean(np.max(np.abs(theta), axis=1) > 2.5)),
        }


# =============================================================================
# Correlators, autocorrelation, GEVP, and bootstrap spectroscopy
# =============================================================================


def integrated_autocorrelation_time(x: NDArray[np.float64]) -> float:
    x = np.asarray(x, dtype=float)
    n = len(x)
    if n < 8 or not np.isfinite(x).all() or np.var(x) == 0:
        return 0.5
    y = x - x.mean()
    # FFT autocovariance with unbiased lag normalization.
    m = 1 << (2 * n - 1).bit_length()
    f = np.fft.rfft(y, n=m)
    acov = np.fft.irfft(f * f.conj(), n=m)[:n] / np.arange(n, 0, -1)
    rho = acov / acov[0]
    tau = 0.5
    # Madras-Sokal self-consistent window, with an initial-positive guard.
    for lag in range(1, n):
        if rho[lag] <= 0:
            break
        tau += float(rho[lag])
        if lag >= 5.0 * tau:
            break
    return max(0.5, float(tau))


def block_mean(a: NDArray, block_size: int) -> NDArray:
    nblock = len(a) // block_size
    if nblock < 2:
        return np.asarray(a)
    trimmed = a[: nblock * block_size]
    return trimmed.reshape((nblock, block_size) + a.shape[1:]).mean(axis=1)


def time_correlation_matrices(obs: NDArray, complex_channel: bool = False) -> NDArray[np.float64]:
    """
    obs: [n_cfg,n_op,n_component,Nt].
    Return per-config C[t,a,b], averaged over origins and components.
    """
    obs = np.asarray(obs)
    ncfg, nop, ncomp, Nt = obs.shape
    max_t = Nt // 2
    out = np.empty((ncfg, max_t + 1, nop, nop), dtype=np.float64)
    # Symmetry says the ensemble mean is zero.  Remove only the single global
    # estimate, never a per-configuration time mean.
    centered = obs - obs.mean(axis=(0, 2, 3), keepdims=True)
    for dt in range(max_t + 1):
        shifted_obs = np.roll(centered, -dt, axis=-1)
        if complex_channel:
            c = np.einsum("nact,nbct->nab", shifted_obs.conj(), centered, optimize=True)
            c = c.real / float(ncomp * Nt)
        else:
            c = np.einsum("nact,nbct->nab", shifted_obs, centered, optimize=True) / float(ncomp * Nt)
        out[:, dt] = 0.5 * (c + c.swapaxes(-1, -2))
    return out


@dataclass
class VariationalBasis:
    W: NDArray[np.float64]
    retained: int
    condition: float


def build_whitener(C0: NDArray[np.float64], rcond: float = 1e-7, max_rank: int = 10) -> VariationalBasis:
    C0 = 0.5 * (C0 + C0.T)
    evals, evecs = np.linalg.eigh(C0)
    order = np.argsort(evals)[::-1]
    evals, evecs = evals[order], evecs[:, order]
    cutoff = max(float(evals[0]) * rcond, 1e-18)
    keep = np.where(evals > cutoff)[0][:max_rank]
    if len(keep) < 1:
        raise RuntimeError("correlator C(0) has no positive numerical mode")
    W = evecs[:, keep] / np.sqrt(evals[keep])[None, :]
    cond = float(evals[keep[0]] / evals[keep[-1]])
    return VariationalBasis(W=W, retained=len(keep), condition=cond)


def gevp_vector(C: NDArray[np.float64], basis: VariationalBasis, t0: int, td: int) -> NDArray[np.float64]:
    W = basis.W
    A = 0.5 * (W.T @ C[td] @ W + (W.T @ C[td] @ W).T)
    B = 0.5 * (W.T @ C[t0] @ W + (W.T @ C[t0] @ W).T)
    # B should be near identity for the ensemble mean, but bootstrap means can
    # move slightly.  Clip only at machine-noise scale.
    eb, Qb = np.linalg.eigh(B)
    floor = max(1e-10 * float(np.max(eb)), 1e-12)
    eb = np.maximum(eb, floor)
    Binvhalf = Qb @ np.diag(eb ** -0.5) @ Qb.T
    Aw = Binvhalf @ A @ Binvhalf
    vals, vecs = np.linalg.eigh(0.5 * (Aw + Aw.T))
    z = Binvhalf @ vecs[:, np.argmax(vals)]
    v = W @ z
    norm = math.sqrt(max(float(v @ C[t0] @ v), 1e-30))
    return v / norm


def cosh_model(t: NDArray[np.float64], amplitude: float, mass: float, Nt: int) -> NDArray[np.float64]:
    return amplitude * (np.exp(-mass * t) + np.exp(-mass * (Nt - t)))


def fit_periodic_cosh(g: NDArray[np.float64], Nt: int, tmin: int, tmax: int, sigma: Optional[NDArray[np.float64]] = None) -> Tuple[float, float, float, int]:
    t = np.arange(tmin, tmax + 1, dtype=float)
    y = np.asarray(g[tmin : tmax + 1], dtype=float)
    if sigma is None:
        s = np.ones_like(y)
    else:
        s = np.maximum(np.asarray(sigma[tmin : tmax + 1], dtype=float), 1e-14)
    if not np.isfinite(y).all() or y[0] <= 0:
        raise RuntimeError("nonpositive/nonfinite correlator in fit window")

    def objective(m: float) -> float:
        f = np.exp(-m * t) + np.exp(-m * (Nt - t))
        w = 1.0 / (s * s)
        A = float(np.sum(w * f * y) / np.sum(w * f * f))
        return float(np.sum(((y - A * f) / s) ** 2))

    result = optimize.minimize_scalar(objective, bounds=(1e-4, 6.0), method="bounded", options={"xatol": 1e-10})
    m = float(result.x)
    f = np.exp(-m * t) + np.exp(-m * (Nt - t))
    w = 1.0 / (s * s)
    A = float(np.sum(w * f * y) / np.sum(w * f * f))
    chi2 = float(objective(m))
    dof = max(0, len(t) - 2)
    return m, A, chi2, dof


def effective_mass_cosh(g: NDArray[np.float64]) -> NDArray[np.float64]:
    g = np.asarray(g, dtype=float)
    out = np.full_like(g, np.nan)
    for t in range(1, len(g) - 1):
        if g[t] > 0:
            arg = (g[t - 1] + g[t + 1]) / (2.0 * g[t])
            if arg >= 1.0:
                out[t] = np.arccosh(arg)
    return out


@dataclass
class ChannelResult:
    mass: float
    mass_error: float
    amplitude: float
    chi2: float
    dof: int
    p_value: float
    retained_basis: int
    basis_condition: float
    block_size: int
    n_blocks: int
    projected_correlator: List[float]
    effective_mass: List[float]
    raw_ground_fraction: Optional[float] = None
    raw_ground_fraction_error: Optional[float] = None


def analyze_channel(
    obs: NDArray,
    Nt: int,
    tmin: int,
    tmax: int,
    n_boot: int,
    seed: int,
    block_size: int,
    complex_channel: bool = False,
    raw_index: Optional[int] = None,
    whitener_rcond: float = 1e-7,
) -> ChannelResult:
    corr_cfg = time_correlation_matrices(obs, complex_channel=complex_channel)
    corr_blocks = block_mean(corr_cfg, block_size)
    nblock = len(corr_blocks)
    if nblock < 4:
        raise RuntimeError(f"only {nblock} independent blocks; need at least 4")
    C = corr_blocks.mean(axis=0)
    # Pilot audit 2026-08-01: at rcond=1e-7 the 9-operator T1 basis retained
    # noise directions (condition 3.2e5).  Physics profiles pass 1e-4 here.
    basis = build_whitener(C[0], rcond=whitener_rcond, max_rank=min(10, C.shape[-1]))
    td = 1
    v = gevp_vector(C, basis, t0=0, td=td)
    g = np.einsum("i,tij,j->t", v, C, v, optimize=True)

    rng = np.random.default_rng(seed)
    boot_g = []
    boot_m = []
    boot_amp = []
    boot_frac = []
    # Preliminary scale for weighted central fit.
    for _ in range(n_boot):
        idx = rng.integers(0, nblock, size=nblock)
        Cb = corr_blocks[idx].mean(axis=0)
        try:
            vb = gevp_vector(Cb, basis, t0=0, td=td)
            gb = np.einsum("i,tij,j->t", vb, Cb, vb, optimize=True)
            mb, Ab, _, _ = fit_periodic_cosh(gb, Nt, tmin, tmax)
        except Exception:
            continue
        if np.isfinite(mb) and 0 < mb < 6:
            boot_g.append(gb)
            boot_m.append(mb)
            boot_amp.append(Ab)
            if raw_index is not None:
                raw = Cb[:, raw_index, raw_index]
                tt = np.arange(tmin, tmax + 1, dtype=float)
                f = np.exp(-mb * tt) + np.exp(-mb * (Nt - tt))
                Ar = float(np.dot(f, raw[tmin : tmax + 1]) / np.dot(f, f))
                boot_frac.append(Ar / max(float(raw[0]), 1e-30))
    if len(boot_m) < max(30, n_boot // 3):
        raise RuntimeError(f"only {len(boot_m)}/{n_boot} bootstrap spectroscopy fits succeeded")
    boot_g_arr = np.asarray(boot_g)
    sigma_g = boot_g_arr.std(axis=0, ddof=1)
    mass, amp, chi2, dof = fit_periodic_cosh(g, Nt, tmin, tmax, sigma=sigma_g)
    pval = float(stats.chi2.sf(chi2, dof)) if dof > 0 else float("nan")
    meff = effective_mass_cosh(g)

    frac = frac_err = None
    if boot_frac:
        frac = float(np.median(boot_frac))
        frac_err = float(np.std(boot_frac, ddof=1))

    return ChannelResult(
        mass=mass,
        mass_error=float(np.std(boot_m, ddof=1)),
        amplitude=amp,
        chi2=chi2,
        dof=dof,
        p_value=pval,
        retained_basis=basis.retained,
        basis_condition=basis.condition,
        block_size=block_size,
        n_blocks=nblock,
        projected_correlator=[float(x) for x in g],
        effective_mass=[float(x) for x in meff],
        raw_ground_fraction=frac,
        raw_ground_fraction_error=frac_err,
    )


def string_tension_from_torelon(energy: float, L: int) -> float:
    c = 2.0 * math.pi / 3.0
    a2sigma = (c + math.sqrt(c * c + 4.0 * L * L * energy * energy)) / (2.0 * L * L)
    return math.sqrt(a2sigma)


def propagate_string_error(energy: float, error: float, L: int) -> float:
    if error <= 0:
        return 0.0
    hi = string_tension_from_torelon(energy + error, L)
    lo = string_tension_from_torelon(max(energy - error, 1e-8), L)
    return 0.5 * (hi - lo)


# =============================================================================
# Published-data replay and continuum fit
# =============================================================================


PUBLISHED = {
    "beta": np.array([5.8941, 5.99, 6.0625, 6.235, 6.3380, 6.50]),
    "L": np.array([14, 18, 20, 26, 30, 38]),
    "Nt": np.array([16, 18, 20, 26, 30, 38]),
    "asqrt_sigma": np.array([0.26118, 0.21982, 0.19472, 0.15003, 0.12928, 0.10383]),
    "asqrt_sigma_err": np.array([0.00037, 0.00077, 0.00054, 0.00030, 0.00027, 0.00024]),
    "aM_T1pm": np.array([1.591, 1.345, 1.194, 0.897, 0.7797, 0.636]),
    "aM_T1pm_err": np.array([0.018, 0.013, 0.008, 0.010, 0.0060, 0.005]),
}


@dataclass
class ContinuumFit:
    intercept: float
    intercept_error: float
    slope: float
    slope_error: float
    chi2: float
    dof: int
    p_value: float


def continuum_fit(asqrt: NDArray[np.float64], asqrt_err: NDArray[np.float64], mass: NDArray[np.float64], mass_err: NDArray[np.float64]) -> ContinuumFit:
    x = np.asarray(asqrt) ** 2
    y = np.asarray(mass) / np.asarray(asqrt)
    sy = y * np.sqrt((np.asarray(mass_err) / np.asarray(mass)) ** 2 + (np.asarray(asqrt_err) / np.asarray(asqrt)) ** 2)
    X = np.column_stack((np.ones_like(x), x))
    w = 1.0 / sy**2
    cov = np.linalg.inv(X.T @ (w[:, None] * X))
    coeff = cov @ (X.T @ (w * y))
    residual = y - X @ coeff
    chi2 = float(np.sum((residual / sy) ** 2))
    dof = len(y) - 2
    return ContinuumFit(
        intercept=float(coeff[0]),
        intercept_error=float(math.sqrt(cov[0, 0])),
        slope=float(coeff[1]),
        slope_error=float(math.sqrt(cov[1, 1])),
        chi2=chi2,
        dof=dof,
        p_value=float(stats.chi2.sf(chi2, dof)),
    )


def run_published_replay() -> ContinuumFit:
    heading("C. PUBLISHED WILSON-ACTION CONTINUUM REPLAY")
    d = PUBLISHED
    fit = continuum_fit(d["asqrt_sigma"], d["asqrt_sigma_err"], d["aM_T1pm"], d["aM_T1pm_err"])
    print("  beta       a^2 sigma      aM(T1+-)       M/sqrt(sigma)")
    for b, s, m, me in zip(d["beta"], d["asqrt_sigma"], d["aM_T1pm"], d["aM_T1pm_err"]):
        print(f"  {b:7.4f}    {s*s:10.7f}     {m:8.4f}({int(round(me*10000)):03d})      {m/s:10.6f}")
    print(
        f"\n  Linear O(a^2 sigma) fit: M/sqrt(sigma) = {fit.intercept:.6f}({fit.intercept_error:.6f})"
        f" + {fit.slope:.4f}({fit.slope_error:.4f}) a^2 sigma"
    )
    print(f"  chi2/dof={fit.chi2:.3f}/{fit.dof}, p={fit.p_value:.4f}")
    benchmark, benchmark_err = 6.065, 0.040
    pull = (fit.intercept - benchmark) / math.sqrt(fit.intercept_error**2 + benchmark_err**2)
    gate(
        "published continuum replay",
        abs(pull) < 1.0,
        f"replay={fit.intercept:.4f}({fit.intercept_error:.4f}), paper={benchmark:.4f}({benchmark_err:.4f}), pull={pull:+.2f}",
    )
    return fit


# =============================================================================
# Ensemble driver
# =============================================================================


@dataclass
class EnsembleResult:
    config: Mapping[str, object]
    backend: str
    plaquette_mean: float
    plaquette_error: float
    acceptance_mean: float
    tau_int_measurements: float
    bridge_metrics: Mapping[str, float]
    t1: Mapping[str, object]
    torelon: Mapping[str, object]
    asqrt_sigma: float
    asqrt_sigma_error: float
    mass_over_sqrt_sigma: float
    mass_over_sqrt_sigma_error: float
    wall_seconds: float


def standard_error_blocked(x: NDArray[np.float64], block_size: int) -> float:
    b = block_mean(np.asarray(x, dtype=float), block_size)
    return float(np.std(b, ddof=1) / math.sqrt(len(b))) if len(b) > 1 else float("nan")


def thermalize(lat: SU3WilsonLattice) -> Tuple[List[float], List[float]]:
    cfg = lat.cfg
    plaquettes: List[float] = []
    acceptances: List[float] = []
    subheading("Thermalisation")
    start = time.time()
    monitor_window: List[float] = []
    for cyc in range(1, cfg.thermal_cycles + 1):
        acc = lat.cycle(audit_overrelax=(cyc == 1))
        monitor_window.append(acc)
        if cyc % cfg.monitor_every == 0 or cyc == cfg.thermal_cycles:
            p = lat.plaquette()
            a = float(np.mean(monitor_window))
            plaquettes.append(p)
            acceptances.append(a)
            # Robbins-Monro adaptation occurs only before production.
            lat.proposal_size *= math.exp(0.45 * (a - cfg.target_acceptance))
            lat.proposal_size = float(np.clip(lat.proposal_size, 0.03, 1.20))
            monitor_window.clear()
            print(
                f"  cycle {cyc:6d}/{cfg.thermal_cycles}: plaquette={p:.8f}, "
                f"accept={a:.4f}, proposal={lat.proposal_size:.4f}"
            )
        if cyc % 50 == 0:
            lat.reunitarize()
    lat.reunitarize()
    print(f"  thermalisation wall time: {time.time()-start:.2f} s")
    return plaquettes, acceptances


def thermalization_gates(lat: SU3WilsonLattice, p_hist: Sequence[float], a_hist: Sequence[float]) -> None:
    n = len(p_hist)
    if n >= 6:
        tail = np.asarray(p_hist[n // 2 :], dtype=float)
        a, b = np.array_split(tail, 2)
        denom = math.sqrt(np.var(a, ddof=1) / len(a) + np.var(b, ddof=1) / len(b)) if len(a) > 1 and len(b) > 1 else float("inf")
        z = abs(float(a.mean() - b.mean())) / denom if denom > 0 else 0.0
        gate("thermalisation split-mean", z < 4.0, f"tail split z={z:.3f}", hard=len(tail) >= 6)
    else:
        gate("thermalisation split-mean", False, f"only {n} monitor points (smoke diagnostic)", hard=False)
    mean_acc = float(np.mean(a_hist[-max(1, len(a_hist)//2) :]))
    gate("Metropolis acceptance", 0.30 < mean_acc < 0.80, f"tail mean={mean_acc:.4f}")
    gate("over-relaxation invariance", lat._last_or_error < 2e-4, f"max local action drift={lat._last_or_error:.3e}")
    unit, det = lat.group_errors()
    gate("SU(3) unitarity", unit < 2e-4 and det < 2e-4, f"max ||U^dag U-I||F={unit:.3e}, max |detU-1|={det:.3e}")


def run_ensemble(cfg: EnsembleConfig) -> EnsembleResult:
    heading(f"B. SU(3) T1^{{+-}} ENSEMBLE: beta={cfg.beta}, {cfg.L}^3 x {cfg.Nt}")
    start = time.time()
    physics_target = bool(
        cfg.n_cfg >= 100
        and (cfg.published_asqrt_sigma is None or cfg.L * cfg.published_asqrt_sigma >= 3.0)
    )
    backend = Backend(prefer_gpu=cfg.prefer_gpu, seed=cfg.seed, install_cupy=cfg.install_cupy)
    print(f"  backend: {backend.name}; {backend.memory_detail()}")
    if cfg.prefer_gpu and not backend.is_gpu and cfg.L >= 14:
        raise RuntimeError(
            "production lattice requested but no CUDA/CuPy backend is available; rerun with "
            "--install-cupy on an NVIDIA Colab runtime, or pass --no-gpu intentionally"
        )
    print(
        f"  chain: 1 Metropolis + {cfg.overrelax_per_cycle} over-relaxation sweep(s) per cycle; "
        f"thermal={cfg.thermal_cycles}, configs={cfg.n_cfg}, separation={cfg.separation_cycles}"
    )
    print(f"  basis: APE levels={cfg.ape_levels}, shapes={cfg.loop_shapes}")
    lat = SU3WilsonLattice(cfg, backend)
    stencil_error = lat.audit_local_action_stencil()
    gate(
        "Wilson action/staple identity",
        stencil_error < 5e-5,
        f"one-link total/local trace mismatch={stencil_error:.3e}",
    )
    p_hist, a_hist = thermalize(lat)
    thermalization_gates(lat, p_hist, a_hist)

    subheading("Production and measurements")
    t1_obs: List[NDArray[np.float64]] = []
    tor_obs: List[NDArray[np.complex128]] = []
    plaquettes: List[float] = []
    acceptances: List[float] = []
    bridge_rows: List[Mapping[str, float]] = []
    prod_start = time.time()
    for icfg in range(cfg.n_cfg):
        rates = []
        for _ in range(cfg.separation_cycles):
            rates.append(lat.cycle())
        if (icfg + 1) % 25 == 0:
            lat.reunitarize()
        p = lat.plaquette()
        t1, tor = lat.measure_multiscale()
        plaquettes.append(p)
        acceptances.append(float(np.mean(rates)))
        t1_obs.append(t1)
        tor_obs.append(tor)
        if icfg in {0, cfg.n_cfg // 2, cfg.n_cfg - 1}:
            bridge_rows.append(lat.sampled_weak_field_bridge())
        report_every = max(1, cfg.n_cfg // 10)
        if (icfg + 1) % report_every == 0 or icfg == 0:
            print(
                f"  cfg {icfg+1:5d}/{cfg.n_cfg}: plaquette={p:.8f}, "
                f"accept={acceptances[-1]:.4f}, elapsed={time.time()-prod_start:.1f}s"
            )

    p_arr = np.asarray(plaquettes)
    t1_arr = np.asarray(t1_obs)  # [cfg,op,component,t]
    tor_arr = np.asarray(tor_obs)  # [cfg,level,component,t]
    # Plaquette and C-operator norm are complementary autocorrelation monitors.
    raw_power = np.mean(t1_arr[:, 0] ** 2, axis=(1, 2))
    tau_p = integrated_autocorrelation_time(p_arr)
    tau_o = integrated_autocorrelation_time(raw_power)
    tau = max(tau_p, tau_o)
    block_size = max(1, int(math.ceil(2.0 * tau)))
    nblock = cfg.n_cfg // block_size
    if cfg.n_cfg < 100 and nblock < 4:
        # A smoke test is an execution check, not an error-controlled physics
        # ensemble.  Retain four resampling units so the GEVP/bootstrap path is
        # exercised, and mark the autocorrelation shortfall explicitly.
        block_size = max(1, cfg.n_cfg // 4)
        nblock = cfg.n_cfg // block_size
        gate(
            "smoke autocorrelation coverage",
            False,
            f"estimated 2*tau={2*tau:.2f} exceeds smoke block={block_size}; no physics error claim",
            hard=False,
        )
    print(
        f"\n  autocorrelation: tau_plaq={tau_p:.2f}, tau_O2={tau_o:.2f} measurements; "
        f"block={block_size}, blocks={nblock}"
    )
    gate("bootstrap block count", nblock >= 8, f"{nblock} blocks of {block_size} measurements", hard=physics_target)

    # Smoke runs can be deliberately too small for a mass.  The exact and
    # Markov-chain gates still run, while spectroscopy is reported honestly.
    if nblock >= 4:
        t1_res = analyze_channel(
            t1_arr,
            Nt=cfg.Nt,
            tmin=cfg.fit_tmin,
            tmax=cfg.fit_tmax,
            n_boot=cfg.bootstrap_samples,
            seed=cfg.seed + 11,
            block_size=block_size,
            complex_channel=False,
            raw_index=0,
            whitener_rcond=cfg.whitener_rcond,
        )
        tor_res = analyze_channel(
            tor_arr,
            Nt=cfg.Nt,
            tmin=cfg.fit_tmin,
            tmax=cfg.fit_tmax,
            n_boot=cfg.bootstrap_samples,
            seed=cfg.seed + 29,
            block_size=block_size,
            complex_channel=True,
            raw_index=None,
            whitener_rcond=cfg.whitener_rcond,
        )
    else:
        raise RuntimeError("not enough blocks even for smoke spectroscopy")

    asqrt = string_tension_from_torelon(tor_res.mass, cfg.L)
    asqrt_err = propagate_string_error(tor_res.mass, tor_res.mass_error, cfg.L)
    ratio = t1_res.mass / asqrt
    ratio_err = ratio * math.sqrt((t1_res.mass_error / t1_res.mass) ** 2 + (asqrt_err / asqrt) ** 2)
    p_err = standard_error_blocked(p_arr, block_size)

    subheading("Spectroscopy result")
    print(
        f"  T1^{{+-}}: aM={t1_res.mass:.6f} +/- {t1_res.mass_error:.6f}, "
        f"fit [{cfg.fit_tmin},{cfg.fit_tmax}], chi2/dof={t1_res.chi2:.2f}/{t1_res.dof}, p={t1_res.p_value:.3f}"
    )
    print(
        f"  torelon:  aE={tor_res.mass:.6f} +/- {tor_res.mass_error:.6f} -> "
        f"a sqrt(sigma)={asqrt:.6f} +/- {asqrt_err:.6f}"
    )
    print(f"  M/sqrt(sigma)={ratio:.6f} +/- {ratio_err:.6f}")
    if t1_res.raw_ground_fraction is not None:
        print(
            f"  raw ImTr(plaquette) fitted ground fraction="
            f"{t1_res.raw_ground_fraction:.6f} +/- {t1_res.raw_ground_fraction_error:.6f}"
        )
    print(
        f"  variational ranks: T1={t1_res.retained_basis} (cond {t1_res.basis_condition:.2e}), "
        f"torelon={tor_res.retained_basis} (cond {tor_res.basis_condition:.2e})"
    )

    # Fit quality and physics-control gates are hard only beyond smoke scale.
    physical_run = physics_target
    t1_fit_ok = np.isfinite(t1_res.mass) and 0 < t1_res.mass < 5.9 and (t1_res.dof == 0 or t1_res.p_value > 0.01)
    tor_fit_ok = np.isfinite(tor_res.mass) and 0 < tor_res.mass < 5.9 and (tor_res.dof == 0 or tor_res.p_value > 0.01)
    gate("T1 mass fit", t1_fit_ok, f"aM={t1_res.mass:.4f}, p={t1_res.p_value:.3f}", hard=physical_run)
    g_window = np.asarray(t1_res.projected_correlator[cfg.fit_tmin : cfg.fit_tmax + 1])
    gate(
        "T1 window positivity",
        bool(np.all(g_window > 0)),
        f"min C(t)/C(0) on [{cfg.fit_tmin},{cfg.fit_tmax}] = {float(g_window.min()):.3e}",
        hard=physical_run,
    )
    gate("torelon fit", tor_fit_ok, f"aE={tor_res.mass:.4f}, p={tor_res.p_value:.3f}", hard=physical_run)
    volume_scale = cfg.L * asqrt
    gate("finite-volume scale", volume_scale >= 3.0, f"L a sqrt(sigma)={volume_scale:.3f} (target >=3)", hard=physical_run)

    if cfg.published_mass is not None:
        pull = (t1_res.mass - cfg.published_mass) / max(t1_res.mass_error, 1e-12)
        gate("published lattice-mass benchmark", abs(pull) < 4.0, f"new={t1_res.mass:.4f}, published={cfg.published_mass:.4f}, pull={pull:+.2f}", hard=physical_run)
    if cfg.published_asqrt_sigma is not None:
        pull = (asqrt - cfg.published_asqrt_sigma) / max(asqrt_err, 1e-12)
        gate("published string-scale benchmark", abs(pull) < 4.0, f"new={asqrt:.5f}, published={cfg.published_asqrt_sigma:.5f}, pull={pull:+.2f}", hard=physical_run)

    if t1_res.raw_ground_fraction is not None and t1_res.raw_ground_fraction_error is not None:
        fraw = t1_res.raw_ground_fraction
        gate(
            "raw plaquette spectral fraction",
            -2.0 * t1_res.raw_ground_fraction_error <= fraw <= 1.0 + 2.0 * t1_res.raw_ground_fraction_error,
            f"fraction={fraw:.4f} +/- {t1_res.raw_ground_fraction_error:.4f}",
            hard=physical_run,
        )

    bridge = {
        key: float(np.mean([row[key] for row in bridge_rows]))
        for key in bridge_rows[0]
    }
    print(
        "\n  weak-field operator audit: "
        f"corr(cubic)={bridge['cubic_corr']:.6f}, NRMSE(cubic)={bridge['cubic_nrmse']:.4f}; "
        f"corr(+quintic)={bridge['quintic_corr']:.6f}, NRMSE(+quintic)={bridge['quintic_nrmse']:.4f}"
    )
    gate(
        "cubic-Casimir operator expansion",
        bridge["quintic_nrmse"] < bridge["cubic_nrmse"] and bridge["quintic_corr"] >= bridge["cubic_corr"] - 1e-5,
        "quintic term improves the sampled plaquette expansion",
        hard=physical_run,
    )

    result = EnsembleResult(
        config=asdict(cfg),
        backend=backend.name,
        plaquette_mean=float(p_arr.mean()),
        plaquette_error=p_err,
        acceptance_mean=float(np.mean(acceptances)),
        tau_int_measurements=tau,
        bridge_metrics=bridge,
        t1=asdict(t1_res),
        torelon=asdict(tor_res),
        asqrt_sigma=asqrt,
        asqrt_sigma_error=asqrt_err,
        mass_over_sqrt_sigma=ratio,
        mass_over_sqrt_sigma_error=ratio_err,
        wall_seconds=time.time() - start,
    )
    print(f"  ensemble wall time: {result.wall_seconds:.2f} s")
    return result


# =============================================================================
# Profiles and CLI
# =============================================================================


def profile_config(name: str, no_gpu: bool, seed: int, install_cupy: bool = False) -> Optional[EnsembleConfig]:
    common = dict(seed=seed, prefer_gpu=not no_gpu, install_cupy=install_cupy)
    if name == "replay":
        return None
    if name == "smoke":
        return EnsembleConfig(
            beta=5.70,
            L=4,
            Nt=6,
            thermal_cycles=40,
            n_cfg=48,
            separation_cycles=1,
            overrelax_per_cycle=1,
            monitor_every=5,
            ape_levels=(0, 1),
            loop_shapes=("P", "R"),
            bootstrap_samples=60,
            fit_tmin=1,
            fit_tmax=2,
            **common,
        )
    if name == "next":
        # First physics-comparable ensemble (2026-08-01 pilot analysis): the
        # published 14^3 x 16 volume at beta=5.8941 with ~1/3 of production
        # statistics.  Purpose: (i) remove the finite-volume soft-fail,
        # (ii) first meaningful raw ground-fraction estimate against the
        # published aM(T1+-)=1.591(18), (iii) a measured large-volume A100
        # throughput anchor before scheduling the fine ensembles.
        return EnsembleConfig(
            beta=5.8941,
            L=14,
            Nt=16,
            thermal_cycles=1500,
            n_cfg=2000,
            separation_cycles=5,
            overrelax_per_cycle=4,
            monitor_every=50,
            ape_levels=(0, 4, 12, 24),
            loop_shapes=("P", "R", "S"),
            bootstrap_samples=400,
            fit_tmin=1,
            fit_tmax=4,
            whitener_rcond=1e-4,
            published_asqrt_sigma=0.26118,
            published_mass=1.591,
            **common,
        )
    if name == "pilot":
        return EnsembleConfig(
            beta=5.8941,
            L=8,
            Nt=16,
            thermal_cycles=300,
            n_cfg=300,
            separation_cycles=5,
            overrelax_per_cycle=2,
            monitor_every=20,
            ape_levels=(0, 3, 8),
            loop_shapes=("P", "R", "S"),
            bootstrap_samples=250,
            fit_tmin=1,
            fit_tmax=4,
            published_asqrt_sigma=0.26118,
            published_mass=1.591,
            **common,
        )
    if name == "production":
        return continuum_production_configs(no_gpu, seed, install_cupy=install_cupy)[0]
    raise KeyError(name)


def continuum_production_configs(no_gpu: bool, seed: int, install_cupy: bool = False) -> List[EnsembleConfig]:
    """Minimum production suite on the six published Wilson-action volumes."""
    rows = [
        # beta, L, Nt, thermal cycles, configs, APE levels, fit window
        (5.8941, 14, 16, 2000, 6000, (0, 4, 12, 24), (1, 4)),
        (5.9900, 18, 18, 2500, 7000, (0, 5, 15, 30), (1, 4)),
        (6.0625, 20, 20, 3000, 8000, (0, 6, 18, 36), (1, 5)),
        (6.2350, 26, 26, 4500, 10000, (0, 8, 24, 48), (2, 6)),
        (6.3380, 30, 30, 6000, 12000, (0, 10, 30, 60), (2, 7)),
        (6.5000, 38, 38, 10000, 16000, (0, 12, 36, 72), (2, 8)),
    ]
    out: List[EnsembleConfig] = []
    for i, (beta, L, Nt, therm, ncfg, levels, window) in enumerate(rows):
        out.append(
            EnsembleConfig(
                beta=beta,
                L=L,
                Nt=Nt,
                thermal_cycles=therm,
                n_cfg=ncfg,
                separation_cycles=5,  # 1+4 sweeps per cycle -> 25 sweeps between measurements
                overrelax_per_cycle=4,
                monitor_every=max(50, therm // 20),
                ape_levels=levels,
                loop_shapes=("P", "R", "S"),
                bootstrap_samples=600,
                fit_tmin=window[0],
                fit_tmax=window[1],
                seed=seed + 1009 * i,
                prefer_gpu=not no_gpu,
                install_cupy=install_cupy,
                published_asqrt_sigma=float(PUBLISHED["asqrt_sigma"][i]),
                published_mass=float(PUBLISHED["aM_T1pm"][i]),
            )
        )
    return out


def continuum_from_ensemble_results(results: Sequence[EnsembleResult]) -> ContinuumFit:
    if len(results) < 3:
        raise ValueError("at least three completed ensembles are required for a continuum fit")
    ordered = sorted(results, key=lambda r: float(r.config["beta"]))
    asqrt = np.array([r.asqrt_sigma for r in ordered], dtype=float)
    asqrt_err = np.array([r.asqrt_sigma_error for r in ordered], dtype=float)
    mass = np.array([float(r.t1["mass"]) for r in ordered], dtype=float)
    mass_err = np.array([float(r.t1["mass_error"]) for r in ordered], dtype=float)
    fit = continuum_fit(asqrt, asqrt_err, mass, mass_err)
    heading("D. NEW-ENSEMBLE CONTINUUM FIT")
    print("  beta       a^2 sigma      aM(T1+-)       M/sqrt(sigma)")
    for r in ordered:
        beta = float(r.config["beta"])
        m = float(r.t1["mass"])
        print(f"  {beta:7.4f}    {r.asqrt_sigma**2:10.7f}       {m:9.6f}       {r.mass_over_sqrt_sigma:10.6f}")
    print(
        f"\n  New fit: M/sqrt(sigma)={fit.intercept:.6f} +/- {fit.intercept_error:.6f}"
        f" + ({fit.slope:.4f} +/- {fit.slope_error:.4f}) a^2 sigma"
    )
    print(f"  chi2/dof={fit.chi2:.3f}/{fit.dof}, p={fit.p_value:.4f}")
    benchmark, benchmark_err = 6.065, 0.040
    pull = (fit.intercept - benchmark) / math.sqrt(fit.intercept_error**2 + benchmark_err**2)
    gate("new continuum fit quality", fit.dof > 0 and fit.p_value > 0.01, f"chi2/dof={fit.chi2:.2f}/{fit.dof}, p={fit.p_value:.3f}")
    gate(
        "new continuum T1^{+-} benchmark",
        abs(pull) < 3.0,
        f"new={fit.intercept:.4f}({fit.intercept_error:.4f}), paper=6.0650(0.0400), pull={pull:+.2f}",
    )
    return fit


def load_ensemble_jsons(paths: Sequence[str]) -> List[EnsembleResult]:
    out: List[EnsembleResult] = []
    for path in paths:
        with open(path, "r", encoding="utf-8") as f:
            payload = json.load(f)
        rows = payload.get("ensembles")
        if rows is None:
            one = payload.get("ensemble")
            rows = [] if one is None else [one]
        for row in rows:
            out.append(EnsembleResult(**row))
    # Reject duplicate beta values rather than silently double-weighting them.
    betas = [float(r.config["beta"]) for r in out]
    if len(set(betas)) != len(betas):
        raise ValueError(f"duplicate beta values in inputs: {betas}")
    return out


def parse_args(argv: Optional[Sequence[str]] = None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--profile",
        choices=("smoke", "pilot", "next", "production", "continuum", "combine", "replay"),
        default=os.environ.get("SU3_PROFILE", "smoke"),
    )
    parser.add_argument(
        "--ensemble",
        default="0",
        help="for --profile continuum: index 0..5 or 'all'",
    )
    parser.add_argument(
        "--inputs",
        nargs="*",
        default=(),
        help="completed JSON files for --profile combine",
    )
    parser.add_argument("--seed", type=int, default=20260801)
    parser.add_argument("--no-gpu", action="store_true", help="force NumPy CPU even when CuPy/CUDA is available")
    parser.add_argument(
        "--install-cupy",
        action="store_true",
        help="if CUDA is present but CuPy is missing, install cupy-cuda12x automatically",
    )
    parser.add_argument("--json", default="", help="optional path for a compact JSON result")
    args, unknown = parser.parse_known_args(argv)
    # Notebook kernels inject -f <kernel.json>; all unknown arguments are ignored.
    if unknown and not any(x == "--help" for x in unknown):
        print(f"Ignoring notebook/unknown arguments: {' '.join(unknown)}")
    return args


def final_summary(results: Sequence[EnsembleResult], replay: ContinuumFit, elapsed: float, new_fit: Optional[ContinuumFit] = None) -> None:
    heading("FINAL GATE SUMMARY")
    hard_failures = [g for g in GATES if g.hard and not g.passed]
    warnings = [g for g in GATES if not g.hard and not g.passed]
    for g in GATES:
        tag = "PASS" if g.passed else ("FAIL" if g.hard else "WARN")
        print(f"  [{tag}] {g.name}")
    print(f"\n  hard gates: {sum(g.hard and g.passed for g in GATES)}/{sum(g.hard for g in GATES)} passed")
    print(f"  warnings: {len(warnings)}; elapsed={elapsed:.2f} s")
    print("\n  Claim ledger:")
    print("    * Proven on the finite periodic complex: H2 is the three-dimensional zero-momentum")
    print("      plaquette-plane carrier; cube boundaries lie in B2, are A1^{--}, and telescope at k=0.")
    print("    * Exact operator identity: ImTr U_p has leading weak-field term -Tr(X_p^3)/6.")
    print("    * Published-data replay only: continuum T1^{+-} mass agrees with 6.065(40) sqrt(sigma).")
    physical_results = [r for r in results if int(r.config.get("n_cfg", 0)) >= 100]
    if physical_results:
        print("    * New computational evidence from this run: the reported lattice mass, string scale,")
        print("      raw-operator ground fraction, and weak-field expansion diagnostics.")
    elif results:
        print("    * The generated smoke ensemble validates execution only; its mass and error are not")
        print("      physics evidence because autocorrelation and finite-volume gates are intentionally short.")
    else:
        print("    * No new gauge ensemble was generated in replay mode.")
    if new_fit is not None:
        print("    * New continuum computational result: the six/partial ensemble fit printed above;")
        print("      its validity is conditional on every ensemble-level hard gate passing.")
    print("    * Not proven: equality of the one-plaquette Hamiltonian gap and the physical glueball mass.")
    if hard_failures:
        names = ", ".join(g.name for g in hard_failures)
        raise AssertionError(f"{len(hard_failures)} hard gate(s) failed: {names}")


def main(argv: Optional[Sequence[str]] = None) -> None:
    started = time.time()
    args = parse_args(argv)
    print("Spatial SU(3) T1^{+-} cubic-Casimir bridge test")
    print(f"profile={args.profile}, seed={args.seed}")
    run_symmetry_topology_certificate()
    replay = run_published_replay()
    results: List[EnsembleResult] = []
    new_fit: Optional[ContinuumFit] = None
    if args.profile == "continuum":
        suite = continuum_production_configs(args.no_gpu, args.seed, install_cupy=args.install_cupy)
        if args.ensemble == "all":
            selected = suite
        else:
            idx = int(args.ensemble)
            if not 0 <= idx < len(suite):
                raise ValueError("--ensemble must be 0..5 or all")
            selected = [suite[idx]]
        results = [run_ensemble(cfg) for cfg in selected]
        if len(results) >= 3:
            new_fit = continuum_from_ensemble_results(results)
        else:
            print("\n  One continuum ensemble completed. Save it with --json; combine at least three using")
            print("  --profile combine --inputs beta0.json beta1.json beta2.json ...")
    elif args.profile == "combine":
        if len(args.inputs) < 3:
            raise ValueError("--profile combine requires at least three --inputs JSON files")
        results = load_ensemble_jsons(args.inputs)
        new_fit = continuum_from_ensemble_results(results)
    else:
        cfg = profile_config(args.profile, args.no_gpu, args.seed, install_cupy=args.install_cupy)
        if cfg is not None:
            results = [run_ensemble(cfg)]
    if args.json:
        payload = {
            "profile": args.profile,
            "published_replay": asdict(replay),
            "ensemble": asdict(results[0]) if len(results) == 1 else None,
            "ensembles": [asdict(r) for r in results],
            "new_continuum_fit": asdict(new_fit) if new_fit is not None else None,
            "gates": [asdict(g) for g in GATES],
        }
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)
        print(f"\nWrote JSON result: {args.json}")
    final_summary(results, replay, time.time() - started, new_fit=new_fit)


if __name__ == "__main__":
    main()
