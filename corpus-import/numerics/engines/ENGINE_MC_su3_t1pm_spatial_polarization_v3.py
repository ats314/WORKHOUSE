#!/usr/bin/env python3
"""
Spatial SU(3) T1^{+-} glueball polarization bridge -- hardened v3.

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
     thermalisation / unitarity / finite-volume gates are included.  The same
     multiscale T1 basis is additionally measured at momentum shells (100),
     (110), and (111), and projected with the exact lattice-incidence symbol
     d_i(k)=exp(i k_i)-1 into one longitudinal and two transverse polarizations.
     Atomic
     lattice checkpoints and append-only observation arrays make long Colab
     runs resumable without repeating committed measurements.

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

Hardened inference policy:

  * the configured rank/window is the primary estimator and is never replaced
    by whichever diagnostic fit looks best;
  * bootstrap success and optimizer-boundary rates are reported explicitly;
  * adjacent effective-mass support, positive correlators, nonzero fit degrees
    of freedom, relative precision, and rank/window stability are required;
  * binned correlator matrices are saved for independent reanalysis;
  * unresolved or finite-volume-invalid ensembles are labelled DIAGNOSTIC_ONLY
    and are refused by the new-ensemble continuum fitter.

Quick Colab / local CPU check:

    %run ENGINE_MC_su3_t1pm_spatial_polarization_v3.py --profile smoke

GPU pilot (CuPy is used automatically when available):

    %run ENGINE_MC_su3_t1pm_spatial_polarization_v3.py --profile pilot --install-cupy

One exact-volume production ensemble (index 0..5):

    %run ENGINE_MC_su3_t1pm_spatial_polarization_v3.py --profile continuum --ensemble 0 \
        --install-cupy --output-dir /content/SU3_T1pm_HARDENED_BETA0 \
        --json /content/SU3_T1pm_HARDENED_BETA0.json

All six ensembles and the new continuum fit in one run:

    %run ENGINE_MC_su3_t1pm_spatial_polarization_v3.py --profile continuum --ensemble all \
        --install-cupy --json continuum_all.json

Combine separately completed ensemble files:

    %run ENGINE_MC_su3_t1pm_spatial_polarization_v3.py --profile combine \
        --inputs beta0.json beta1.json beta2.json beta3.json beta4.json beta5.json

Published continuum replay only:

    %run ENGINE_MC_su3_t1pm_spatial_polarization_v3.py --profile replay

The script ignores notebook-injected unknown arguments such as -f kernel.json.
It does not download physics data or mount drives.  NumPy/SciPy are sufficient
for CPU execution.  GPU execution uses CuPy; --install-cupy can install the
CUDA-12 wheel explicitly when the Colab image does not already provide it.
Re-running the same command resumes automatically.  CuPy generator state is
not serializable, so a restore keeps the gauge field exactly and begins a
deterministic fresh random substream recorded in the checkpoint metadata.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib
import itertools
import json
import math
import os
import subprocess
import sys
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Callable, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

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
        self.seed = int(seed)
        self.rng = self.xp.random.RandomState(self.seed)

    def reseed(self, seed: int) -> None:
        """Start a deterministic fresh substream (used after checkpoint restore)."""
        self.seed = int(seed) & 0xFFFFFFFF
        self.rng = self.xp.random.RandomState(self.seed)

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
# Exact finite-momentum incidence polarization utilities
# =============================================================================


def momentum_from_mode(mode: Sequence[int], L: int) -> NDArray[np.float64]:
    """Return k_i=2*pi*n_i/L for one integer spatial Fourier mode."""
    if len(mode) != 3 or L <= 0:
        raise ValueError("mode must have three entries and L must be positive")
    return (2.0 * np.pi / float(L)) * np.asarray(mode, dtype=float)


def incidence_symbol(momentum: Sequence[float]) -> Tuple[NDArray[np.complex128], float]:
    """Exact forward-difference symbol d_i=exp(i k_i)-1 and d^dagger d."""
    k = np.asarray(momentum, dtype=float)
    if k.shape != (3,):
        raise ValueError("momentum must have three components")
    d = np.exp(1j * k) - 1.0
    gram = float(np.vdot(d, d).real)
    return d, gram


def polarization_coefficients(
    momentum: Sequence[float], tolerance: float = 1e-14
) -> Tuple[NDArray[np.complex128], NDArray[np.complex128], float]:
    """Match CAGE_CONTINUUM_OPERATORS: one incidence-longitudinal + two transverse rows."""
    d, gram = incidence_symbol(momentum)
    if gram <= tolerance:
        raise ValueError("longitudinal direction is undefined at zero momentum")
    longitudinal = d / np.sqrt(gram)
    transverse: List[NDArray[np.complex128]] = []
    for axis in np.argsort(np.abs(longitudinal)):
        vector = np.zeros(3, dtype=np.complex128)
        vector[int(axis)] = 1.0
        vector -= longitudinal * np.vdot(longitudinal, vector)
        for prior in transverse:
            vector -= prior * np.vdot(prior, vector)
        norm = float(np.sqrt(np.vdot(vector, vector).real))
        if norm > tolerance:
            transverse.append(vector / norm)
        if len(transverse) == 2:
            break
    if len(transverse) != 2:
        raise RuntimeError("failed to construct transverse polarization basis")
    return longitudinal, np.stack(transverse, axis=0), gram


def dispersion_shell_ratios(
    rest_energy: float,
    axis_energy: float,
    body_diagonal_energy: float,
    tolerance: float = 1e-14,
) -> Dict[str, float]:
    """Axis/body-diagonal rotational-restoration estimators."""
    rest, axis, diagonal = map(float, (rest_energy, axis_energy, body_diagonal_energy))
    if not np.all(np.isfinite((rest, axis, diagonal))):
        raise ValueError("energies must be finite")
    if axis <= rest or diagonal <= rest:
        raise ValueError("nonzero-momentum energies must exceed the rest energy")
    denominators = (
        diagonal - rest,
        diagonal * diagonal - rest * rest,
        np.cosh(diagonal) - np.cosh(rest),
    )
    if any(abs(value) <= tolerance for value in denominators):
        raise ValueError("body-diagonal energy difference is too small")
    return {
        "energy_shift": 3.0 * (axis - rest) / denominators[0],
        "continuum_e2": 3.0 * (axis * axis - rest * rest) / denominators[1],
        "lattice_cosh": 3.0 * (np.cosh(axis) - np.cosh(rest)) / denominators[2],
    }


def mode_label(mode: Sequence[int]) -> str:
    return "".join(str(int(x)) for x in mode)


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
    # Canonical finite-momentum shells.  Components are integer Fourier modes
    # in units 2*pi/L.  These are deliberately part of the trajectory
    # fingerprint because they change what is committed to the observation store.
    momentum_modes: Tuple[Tuple[int, int, int], ...] = ((1, 0, 0), (1, 1, 0), (1, 1, 1))
    measure_polarization: bool = True
    bootstrap_samples: int = 300
    fit_tmin: int = 1
    fit_tmax: int = 4
    gevp_rcond: float = 1e-5
    max_basis_rank: int = 8
    max_basis_condition: float = 1e5
    fit_scan_padding: int = 2
    min_bootstrap_success: float = 0.80
    max_bootstrap_boundary_fraction: float = 0.05
    max_t1_relative_error: float = 0.35
    max_torelon_relative_error: float = 0.25
    min_stable_fits: int = 3
    fit_stability_z: float = 2.5
    checkpoint_every: int = 50
    seed: int = 20260801
    prefer_gpu: bool = True
    install_cupy: bool = False
    cold_start: bool = True
    published_asqrt_sigma: Optional[float] = None
    published_asqrt_sigma_error: Optional[float] = None
    published_mass: Optional[float] = None
    published_mass_error: Optional[float] = None

    def validate(self) -> None:
        if self.L % 2 or self.Nt % 2:
            raise ValueError("checkerboard updates require even L and Nt")
        if self.L < 4 or self.Nt < 6:
            raise ValueError("lattice is too small even for a smoke test")
        if not self.ape_levels or self.ape_levels[0] != 0:
            raise ValueError("ape_levels must start at 0")
        if tuple(sorted(set(self.ape_levels))) != self.ape_levels:
            raise ValueError("ape_levels must be strictly increasing")
        if self.measure_polarization:
            if not self.momentum_modes:
                raise ValueError("momentum_modes cannot be empty when polarization measurement is enabled")
            cleaned_modes = []
            for mode in self.momentum_modes:
                if len(mode) != 3 or any(int(x) != x for x in mode):
                    raise ValueError(f"invalid integer momentum mode {mode!r}")
                mode = tuple(int(x) for x in mode)
                if mode == (0, 0, 0):
                    raise ValueError("zero momentum cannot be incidence-polarized")
                cleaned_modes.append(mode)
            if len(set(cleaned_modes)) != len(cleaned_modes):
                raise ValueError("momentum_modes must be unique")
        if self.fit_tmax >= self.Nt // 2:
            self.fit_tmax = self.Nt // 2 - 1
        if self.fit_tmin < 1 or self.fit_tmax <= self.fit_tmin:
            raise ValueError("invalid fit window")
        if self.bootstrap_samples < 30:
            raise ValueError("bootstrap_samples must be at least 30")
        if not (0.0 < self.gevp_rcond < 1.0):
            raise ValueError("gevp_rcond must lie in (0,1)")
        if self.max_basis_rank < 1 or self.max_basis_condition <= 1.0:
            raise ValueError("invalid variational-basis controls")
        if not (0.0 < self.min_bootstrap_success <= 1.0):
            raise ValueError("min_bootstrap_success must lie in (0,1]")
        if not (0.0 <= self.max_bootstrap_boundary_fraction < 1.0):
            raise ValueError("invalid bootstrap boundary threshold")
        if self.checkpoint_every < 1:
            raise ValueError("checkpoint_every must be positive")


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
        self._momentum_phases = []
        self._polarization_longitudinal = []
        self._polarization_transverse = []
        if config.measure_polarization:
            coords = self.xp.arange(config.L, dtype=self.xp.float64)
            norm = math.sqrt(config.L**3)
            for mode in config.momentum_modes:
                nx, ny, nz = (int(v) for v in mode)
                px = self.xp.exp((-2j * math.pi * nx / config.L) * coords)
                py = self.xp.exp((-2j * math.pi * ny / config.L) * coords)
                pz = self.xp.exp((-2j * math.pi * nz / config.L) * coords)
                phase = (px[:, None, None] * py[None, :, None] * pz[None, None, :]) / norm
                self._momentum_phases.append(phase.astype(self.xp.complex64))
                long_c, trans_c, _ = polarization_coefficients(momentum_from_mode(mode, config.L))
                self._polarization_longitudinal.append(self.xp.asarray(long_c, dtype=self.xp.complex64))
                self._polarization_transverse.append(self.xp.asarray(trans_c, dtype=self.xp.complex64))
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

    def t1_operators_with_polarization(
        self, spatial_links
    ) -> Tuple[NDArray[np.float64], NDArray[np.complex64]]:
        """Return zero-momentum T1 and finite-k incidence polarizations.

        zero has shape [n_shape,3,Nt].  polarized has shape
        [n_shape,n_mode,3,Nt], where channel 0 is longitudinal and channels
        1,2 are an orthonormal transverse basis.  Fourier phases use the same
        exp(-i k.x)/sqrt(V) convention as CAGE_CONTINUUM_OPERATORS.py.
        """
        zero_values = []
        polarized_values = []
        cyclic_planes = ((1, 2), (2, 0), (0, 1))
        nmodes = len(self.cfg.momentum_modes) if self.cfg.measure_polarization else 0
        for shape in self.cfg.loop_shapes:
            zero_comps = []
            mode_comps = []
            for j, k in cyclic_planes:
                val = self.xp.zeros(self.shape, dtype=self.xp.float32)
                paths = self.shape_paths(shape, j, k)
                for path in paths:
                    W = self.path_matrix(spatial_links, path)
                    val += W.diagonal(axis1=-2, axis2=-1).sum(axis=-1).imag.astype(self.xp.float32) / 3.0
                val /= float(len(paths))
                zero = val.sum(axis=(1, 2, 3), dtype=self.xp.float64) / math.sqrt(self.cfg.L**3)
                zero_comps.append(self.B.to_numpy(zero))
                if nmodes:
                    selected = []
                    for phase in self._momentum_phases:
                        # val[t,x,y,z] * exp(-ik.x)/sqrt(V)
                        selected.append(
                            self.xp.einsum("txyz,xyz->t", val, phase, optimize=True)
                        )
                    mode_comps.append(self.xp.stack(selected, axis=0))  # [mode,Nt]
            zero_values.append(np.stack(zero_comps, axis=0))
            if nmodes:
                triplet = self.xp.stack(mode_comps, axis=1)  # [mode,3,Nt]
                projected = []
                for imode in range(nmodes):
                    field = triplet[imode].swapaxes(0, 1)  # [Nt,3]
                    longitudinal = self.xp.einsum(
                        "i,ti->t", self._polarization_longitudinal[imode], field, optimize=True
                    )
                    transverse = self.xp.einsum(
                        "ai,ti->at", self._polarization_transverse[imode], field, optimize=True
                    )
                    projected.append(self.xp.concatenate((longitudinal[None, :], transverse), axis=0))
                polarized_values.append(
                    self.B.to_numpy(self.xp.stack(projected, axis=0)).astype(np.complex64, copy=False)
                )
        zero_array = np.stack(zero_values, axis=0).astype(np.float64, copy=False)
        if nmodes:
            pol_array = np.stack(polarized_values, axis=0).astype(np.complex64, copy=False)
        else:
            pol_array = np.empty((len(self.cfg.loop_shapes), 0, 3, self.cfg.Nt), dtype=np.complex64)
        return zero_array, pol_array

    def t1_operators(self, spatial_links) -> NDArray[np.float64]:
        """Backward-compatible zero-momentum T1 measurement."""
        zero, _ = self.t1_operators_with_polarization(spatial_links)
        return zero

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

    def measure_multiscale(
        self,
    ) -> Tuple[NDArray[np.float64], NDArray[np.complex128], NDArray[np.complex64]]:
        spatial = self.U[..., 1:4, :, :].copy()
        t1_levels: List[NDArray[np.float64]] = []
        pol_levels: List[NDArray[np.complex64]] = []
        poly_levels: List[NDArray[np.complex128]] = []
        target_levels = set(self.cfg.ape_levels)
        max_level = max(target_levels)
        for level in range(max_level + 1):
            if level in target_levels:
                zero, polarized = self.t1_operators_with_polarization(spatial)
                t1_levels.append(zero)
                pol_levels.append(polarized)
                poly_levels.append(self.spatial_polyakov_operators(spatial))
            if level < max_level:
                spatial = self.ape_step(spatial)
        # T1 basis ordering: level-major then shape. [n_ops,3,Nt]
        t1 = np.concatenate(t1_levels, axis=0)
        # Finite-k basis uses the same operator ordering. [n_ops,n_mode,3,Nt]
        polarization = np.concatenate(pol_levels, axis=0)
        # Torelon basis: one operator per smearing level; rotations are components.
        poly = np.stack(poly_levels, axis=0)  # [n_level,3,Nt]
        return t1, poly, polarization

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


def regularized_covariance(samples: NDArray[np.float64]) -> NDArray[np.float64]:
    """Bootstrap covariance with mild diagonal shrinkage for stable inversion."""
    samples = np.asarray(samples, dtype=float)
    if samples.ndim != 2 or len(samples) < 3:
        raise ValueError("at least three bootstrap curves are required")
    cov = np.atleast_2d(np.cov(samples, rowvar=False, ddof=1))
    diag = np.maximum(np.diag(cov), 1e-20)
    # More shrinkage when the bootstrap population is small relative to the
    # fit dimension.  This is a numerical regularizer, not a tuned fit choice.
    shrink = float(np.clip(samples.shape[1] / max(len(samples) - 1, 1), 0.05, 0.30))
    return (1.0 - shrink) * cov + shrink * np.diag(diag)


def fit_periodic_cosh(
    g: NDArray[np.float64],
    Nt: int,
    tmin: int,
    tmax: int,
    sigma: Optional[NDArray[np.float64]] = None,
    covariance: Optional[NDArray[np.float64]] = None,
    mass_bounds: Tuple[float, float] = (1e-4, 6.0),
) -> Tuple[float, float, float, int]:
    t = np.arange(tmin, tmax + 1, dtype=float)
    y = np.asarray(g[tmin : tmax + 1], dtype=float)
    if covariance is not None:
        cov = np.asarray(covariance, dtype=float)
        if cov.shape != (len(y), len(y)) or not np.isfinite(cov).all():
            raise RuntimeError("invalid correlator covariance")
        precision = linalg.pinvh(cov, rtol=1e-10)
    elif sigma is None:
        precision = np.eye(len(y), dtype=float)
    else:
        s = np.maximum(np.asarray(sigma[tmin : tmax + 1], dtype=float), 1e-14)
        precision = np.diag(1.0 / (s * s))
    if not np.isfinite(y).all() or np.any(y <= 0):
        raise RuntimeError("nonpositive/nonfinite correlator in fit window")

    def objective(m: float) -> float:
        f = np.exp(-m * t) + np.exp(-m * (Nt - t))
        denom = float(f @ precision @ f)
        if not np.isfinite(denom) or denom <= 0:
            return float("inf")
        A = float(f @ precision @ y / denom)
        residual = y - A * f
        return float(residual @ precision @ residual)

    result = optimize.minimize_scalar(
        objective,
        bounds=mass_bounds,
        method="bounded",
        options={"xatol": 1e-10},
    )
    if not result.success or not np.isfinite(result.fun):
        raise RuntimeError("periodic-cosh minimization failed")
    m = float(result.x)
    f = np.exp(-m * t) + np.exp(-m * (Nt - t))
    A = float(f @ precision @ y / (f @ precision @ f))
    if not np.isfinite(A) or A <= 0:
        raise RuntimeError("nonpositive/nonfinite fitted amplitude")
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
class FitDiagnostic:
    rank: int
    condition: float
    tmin: int
    tmax: int
    mass: float
    mass_error: float
    mass_q16: float
    mass_q50: float
    mass_q84: float
    amplitude: float
    chi2: float
    dof: int
    p_value: float
    bootstrap_attempts: int
    bootstrap_successes: int
    bootstrap_success_rate: float
    lower_boundary_hits: int
    upper_boundary_hits: int
    boundary_fraction: float
    relative_error: float
    positive_window: bool
    minimum_signal_to_noise: float
    plateau_times: List[int]
    plateau_pair: List[int]
    accepted: bool
    rejection_reasons: List[str]
    raw_ground_fraction: Optional[float] = None
    raw_ground_fraction_error: Optional[float] = None
    raw_ground_fraction_q16: Optional[float] = None
    raw_ground_fraction_q84: Optional[float] = None


@dataclass
class ChannelResult:
    mass: float
    mass_error: float
    mass_q16: float
    mass_q50: float
    mass_q84: float
    amplitude: float
    chi2: float
    dof: int
    p_value: float
    retained_basis: int
    basis_condition: float
    block_size: int
    n_blocks: int
    bootstrap_attempts: int
    bootstrap_successes: int
    bootstrap_success_rate: float
    lower_boundary_hits: int
    upper_boundary_hits: int
    boundary_fraction: float
    relative_error: float
    resolved: bool
    resolution_reasons: List[str]
    stable_fit_count: int
    stability_max_z: float
    plateau_times: List[int]
    plateau_pair: List[int]
    projected_correlator: List[float]
    projected_correlator_q16: List[float]
    projected_correlator_q84: List[float]
    effective_mass: List[float]
    effective_mass_error: List[float]
    fit_scan: List[Mapping[str, object]]
    raw_ground_fraction: Optional[float] = None
    raw_ground_fraction_error: Optional[float] = None
    raw_ground_fraction_q16: Optional[float] = None
    raw_ground_fraction_q84: Optional[float] = None
    raw_fraction_stable: Optional[bool] = None
    raw_fraction_stability_spread: Optional[float] = None


def fit_window_scan(tmin: int, tmax: int, Nt: int, padding: int) -> List[Tuple[int, int]]:
    """Predeclare nearby windows; always retain the configured primary window."""
    latest = Nt // 2 - 1
    windows = {(int(tmin), int(tmax))}
    lo_max = min(latest - 1, tmin + max(1, padding // 2))
    hi_max = min(latest, tmax + padding)
    for lo in range(max(1, tmin - 1), lo_max + 1):
        for hi in range(max(lo + 2, tmax - padding), hi_max + 1):
            windows.add((lo, hi))
    return sorted(windows)


def plateau_diagnostics(
    g: NDArray[np.float64],
    bootstrap_g: NDArray[np.float64],
    tmin: int,
    tmax: int,
) -> Tuple[List[int], List[int], NDArray[np.float64], NDArray[np.float64]]:
    central = effective_mass_cosh(g)
    if len(bootstrap_g):
        boot = np.asarray([effective_mass_cosh(row) for row in bootstrap_g], dtype=float)
        errors = np.full(boot.shape[1], np.nan, dtype=float)
        for column in range(boot.shape[1]):
            finite = boot[np.isfinite(boot[:, column]), column]
            if len(finite) >= 2:
                errors[column] = float(np.std(finite, ddof=1))
        valid_fraction = np.mean(np.isfinite(boot), axis=0)
    else:
        errors = np.full_like(central, np.nan)
        valid_fraction = np.zeros_like(central)

    times: List[int] = []
    upper = min(tmax, len(central) - 2)
    for t in range(max(1, tmin), upper + 1):
        if (
            np.isfinite(central[t])
            and np.isfinite(errors[t])
            and errors[t] > 0
            and valid_fraction[t] >= 0.50
        ):
            times.append(t)

    pair: List[int] = []
    for a, b in zip(times[:-1], times[1:]):
        if b != a + 1:
            continue
        denom = math.sqrt(errors[a] ** 2 + errors[b] ** 2)
        if denom > 0 and abs(central[a] - central[b]) <= 2.0 * denom:
            pair = [a, b]
            break
    return times, pair, central, errors


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
    rcond: float = 1e-5,
    max_rank: int = 8,
    max_condition: float = 1e5,
    fit_scan_padding: int = 2,
    min_bootstrap_success: float = 0.80,
    max_boundary_fraction: float = 0.05,
    max_relative_error: float = 0.35,
    min_stable_fits: int = 3,
    stability_z: float = 2.5,
) -> Tuple[ChannelResult, NDArray[np.float64]]:
    corr_cfg = time_correlation_matrices(obs, complex_channel=complex_channel)
    corr_blocks = block_mean(corr_cfg, block_size)
    nblock = len(corr_blocks)
    if nblock < 4:
        raise RuntimeError(f"only {nblock} independent blocks; need at least 4")
    C = corr_blocks.mean(axis=0)
    full_basis = build_whitener(C[0], rcond=rcond, max_rank=min(max_rank, C.shape[-1]))
    primary_rank = full_basis.retained
    td = 1
    rng = np.random.default_rng(seed)
    resamples = rng.integers(0, nblock, size=(n_boot, nblock))
    windows = fit_window_scan(tmin, tmax, Nt, fit_scan_padding)
    diagnostics: List[FitDiagnostic] = []
    rank_curves: Dict[int, NDArray[np.float64]] = {}
    rank_boot_curves: Dict[int, NDArray[np.float64]] = {}
    rank_meff: Dict[int, NDArray[np.float64]] = {}
    rank_meff_error: Dict[int, NDArray[np.float64]] = {}

    for rank in range(1, primary_rank + 1):
        basis = build_whitener(C[0], rcond=rcond, max_rank=rank)
        v = gevp_vector(C, basis, t0=0, td=td)
        g = np.einsum("i,tij,j->t", v, C, v, optimize=True)
        rank_curves[rank] = g

        boot_g: List[NDArray[np.float64]] = []
        boot_raw: List[Optional[NDArray[np.float64]]] = []
        for idx in resamples:
            Cb = corr_blocks[idx].mean(axis=0)
            try:
                vb = gevp_vector(Cb, basis, t0=0, td=td)
                gb = np.einsum("i,tij,j->t", vb, Cb, vb, optimize=True)
            except Exception:
                continue
            if not np.isfinite(gb).all():
                continue
            boot_g.append(gb)
            boot_raw.append(Cb[:, raw_index, raw_index] if raw_index is not None else None)
        boot_g_arr = np.asarray(boot_g, dtype=float)
        rank_boot_curves[rank] = boot_g_arr
        plateau_times_all, _, meff, meff_error = plateau_diagnostics(
            g, boot_g_arr, 1, len(g) - 2
        )
        del plateau_times_all
        rank_meff[rank] = meff
        rank_meff_error[rank] = meff_error

        for lo, hi in windows:
            reasons: List[str] = []
            positive_window = bool(np.isfinite(g[lo : hi + 1]).all() and np.all(g[lo : hi + 1] > 0))
            if len(boot_g_arr) >= 3:
                sigma_g = np.std(boot_g_arr, axis=0, ddof=1)
            else:
                sigma_g = np.full_like(g, np.inf)
            snr_slice = np.abs(g[lo : min(hi + 1, lo + 2)]) / np.maximum(
                sigma_g[lo : min(hi + 1, lo + 2)], 1e-30
            )
            minimum_snr = float(np.min(snr_slice)) if len(snr_slice) else 0.0

            mass = amp = chi2 = float("nan")
            dof = max(0, hi - lo - 1)
            pval = float("nan")
            covariance = None
            try:
                if len(boot_g_arr) < 3:
                    raise RuntimeError("too few bootstrap projected curves")
                covariance = regularized_covariance(boot_g_arr[:, lo : hi + 1])
                mass, amp, chi2, dof = fit_periodic_cosh(
                    g, Nt, lo, hi, covariance=covariance
                )
                pval = float(stats.chi2.sf(chi2, dof)) if dof > 0 else float("nan")
            except Exception as exc:
                reasons.append(f"central fit failed: {exc}")

            boot_masses: List[float] = []
            boot_fractions: List[float] = []
            lower_hits = 0
            upper_hits = 0
            mass_lo, mass_hi = 1e-4, 6.0
            boundary_width = 0.01 * (mass_hi - mass_lo)
            if covariance is not None:
                for ib, gb in enumerate(boot_g_arr):
                    try:
                        mb, _, _, _ = fit_periodic_cosh(
                            gb, Nt, lo, hi, covariance=covariance, mass_bounds=(mass_lo, mass_hi)
                        )
                    except Exception:
                        continue
                    boot_masses.append(mb)
                    lower_hits += int(mb <= mass_lo + boundary_width)
                    upper_hits += int(mb >= mass_hi - boundary_width)
                    raw = boot_raw[ib]
                    if raw is not None and np.isfinite(raw).all() and raw[0] > 0:
                        tt = np.arange(lo, hi + 1, dtype=float)
                        f = np.exp(-mb * tt) + np.exp(-mb * (Nt - tt))
                        Ar = float(np.dot(f, raw[lo : hi + 1]) / np.dot(f, f))
                        boot_fractions.append(Ar / float(raw[0]))

            successes = len(boot_masses)
            success_rate = successes / float(n_boot)
            boundary_fraction = (lower_hits + upper_hits) / float(max(successes, 1))
            if successes >= 2:
                q16, q50, q84 = (float(x) for x in np.quantile(boot_masses, [0.16, 0.50, 0.84]))
                mass_error = float(np.std(boot_masses, ddof=1))
            else:
                q16 = q50 = q84 = mass_error = float("nan")
            relative_error = mass_error / mass if np.isfinite(mass) and mass > 0 else float("inf")

            frac = frac_err = frac_q16 = frac_q84 = None
            if len(boot_fractions) >= 2:
                frac_q16, frac, frac_q84 = (
                    float(x) for x in np.quantile(boot_fractions, [0.16, 0.50, 0.84])
                )
                frac_err = float(np.std(boot_fractions, ddof=1))

            plateau_times, plateau_pair, _, _ = plateau_diagnostics(g, boot_g_arr, lo, hi)
            if basis.condition > max_condition:
                reasons.append(f"basis condition {basis.condition:.3e} exceeds {max_condition:.3e}")
            if not positive_window:
                reasons.append("central correlator is not positive across the fit window")
            if dof < 1:
                reasons.append("fit has zero degrees of freedom")
            if not np.isfinite(pval) or pval <= 0.01:
                reasons.append("fit p-value is not above 0.01")
            if success_rate < min_bootstrap_success:
                reasons.append(
                    f"bootstrap success {success_rate:.3f} is below {min_bootstrap_success:.3f}"
                )
            if boundary_fraction > max_boundary_fraction:
                reasons.append(
                    f"bootstrap boundary fraction {boundary_fraction:.3f} exceeds {max_boundary_fraction:.3f}"
                )
            if not np.isfinite(relative_error) or relative_error > max_relative_error:
                reasons.append(
                    f"relative mass error {relative_error:.3f} exceeds {max_relative_error:.3f}"
                )
            if minimum_snr < 1.0:
                reasons.append(f"first-two-point minimum S/N {minimum_snr:.3f} is below 1")
            if not plateau_pair:
                reasons.append("no adjacent bootstrap-supported effective-mass plateau")

            diagnostics.append(
                FitDiagnostic(
                    rank=rank,
                    condition=basis.condition,
                    tmin=lo,
                    tmax=hi,
                    mass=mass,
                    mass_error=mass_error,
                    mass_q16=q16,
                    mass_q50=q50,
                    mass_q84=q84,
                    amplitude=amp,
                    chi2=chi2,
                    dof=dof,
                    p_value=pval,
                    bootstrap_attempts=n_boot,
                    bootstrap_successes=successes,
                    bootstrap_success_rate=success_rate,
                    lower_boundary_hits=lower_hits,
                    upper_boundary_hits=upper_hits,
                    boundary_fraction=boundary_fraction,
                    relative_error=relative_error,
                    positive_window=positive_window,
                    minimum_signal_to_noise=minimum_snr,
                    plateau_times=plateau_times,
                    plateau_pair=plateau_pair,
                    accepted=not reasons,
                    rejection_reasons=reasons,
                    raw_ground_fraction=frac,
                    raw_ground_fraction_error=frac_err,
                    raw_ground_fraction_q16=frac_q16,
                    raw_ground_fraction_q84=frac_q84,
                )
            )

    primary = next(
        d for d in diagnostics
        if d.rank == primary_rank and d.tmin == tmin and d.tmax == tmax
    )
    comparable = [
        d for d in diagnostics
        if d.accepted and d.rank >= max(1, primary_rank - 2)
    ]
    stability_values: List[float] = []
    if np.isfinite(primary.mass) and np.isfinite(primary.mass_error):
        for d in comparable:
            denom = math.sqrt(primary.mass_error**2 + d.mass_error**2)
            if denom > 0:
                stability_values.append(abs(d.mass - primary.mass) / denom)
    stability_max = max(stability_values, default=float("inf"))
    resolution_reasons = list(primary.rejection_reasons)
    if len(comparable) < min_stable_fits:
        resolution_reasons.append(
            f"only {len(comparable)} accepted nearby rank/window fits; need {min_stable_fits}"
        )
    if not np.isfinite(stability_max) or stability_max > stability_z:
        resolution_reasons.append(
            f"rank/window stability max z={stability_max:.3f} exceeds {stability_z:.3f}"
        )
    resolved = not resolution_reasons

    raw_candidates = [
        d.raw_ground_fraction for d in comparable
        if d.raw_ground_fraction is not None and np.isfinite(d.raw_ground_fraction)
    ]
    raw_spread = float(max(raw_candidates) - min(raw_candidates)) if len(raw_candidates) >= 2 else None
    raw_stable: Optional[bool] = None
    if primary.raw_ground_fraction is not None and primary.raw_ground_fraction_error is not None:
        raw_stable = bool(
            len(raw_candidates) >= min_stable_fits
            and raw_spread is not None
            and raw_spread <= max(0.15, 2.0 * primary.raw_ground_fraction_error)
            and primary.raw_ground_fraction_error <= 0.30
            and -0.10 <= primary.raw_ground_fraction <= 1.10
        )

    primary_g = rank_curves[primary_rank]
    primary_boot_g = rank_boot_curves[primary_rank]
    if len(primary_boot_g) >= 2:
        corr_q16 = np.quantile(primary_boot_g, 0.16, axis=0)
        corr_q84 = np.quantile(primary_boot_g, 0.84, axis=0)
    else:
        corr_q16 = np.full_like(primary_g, np.nan)
        corr_q84 = np.full_like(primary_g, np.nan)

    return ChannelResult(
        mass=primary.mass,
        mass_error=primary.mass_error,
        mass_q16=primary.mass_q16,
        mass_q50=primary.mass_q50,
        mass_q84=primary.mass_q84,
        amplitude=primary.amplitude,
        chi2=primary.chi2,
        dof=primary.dof,
        p_value=primary.p_value,
        retained_basis=primary_rank,
        basis_condition=primary.condition,
        block_size=block_size,
        n_blocks=nblock,
        bootstrap_attempts=primary.bootstrap_attempts,
        bootstrap_successes=primary.bootstrap_successes,
        bootstrap_success_rate=primary.bootstrap_success_rate,
        lower_boundary_hits=primary.lower_boundary_hits,
        upper_boundary_hits=primary.upper_boundary_hits,
        boundary_fraction=primary.boundary_fraction,
        relative_error=primary.relative_error,
        resolved=resolved,
        resolution_reasons=resolution_reasons,
        stable_fit_count=len(comparable),
        stability_max_z=stability_max,
        plateau_times=primary.plateau_times,
        plateau_pair=primary.plateau_pair,
        projected_correlator=[float(x) for x in primary_g],
        projected_correlator_q16=[float(x) for x in corr_q16],
        projected_correlator_q84=[float(x) for x in corr_q84],
        effective_mass=[float(x) for x in rank_meff[primary_rank]],
        effective_mass_error=[float(x) for x in rank_meff_error[primary_rank]],
        fit_scan=[asdict(d) for d in diagnostics],
        raw_ground_fraction=primary.raw_ground_fraction,
        raw_ground_fraction_error=primary.raw_ground_fraction_error,
        raw_ground_fraction_q16=primary.raw_ground_fraction_q16,
        raw_ground_fraction_q84=primary.raw_ground_fraction_q84,
        raw_fraction_stable=raw_stable,
        raw_fraction_stability_spread=raw_spread,
    ), corr_blocks


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


def weighted_linear_fit(x: NDArray[np.float64], y: NDArray[np.float64], sy: NDArray[np.float64]) -> ContinuumFit:
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    sy = np.asarray(sy, dtype=float)
    if not (x.shape == y.shape == sy.shape) or x.ndim != 1 or len(x) < 3:
        raise ValueError("weighted linear fit needs >=3 aligned one-dimensional points")
    if not np.all(np.isfinite(x)) or not np.all(np.isfinite(y)) or not np.all(np.isfinite(sy)) or np.any(sy <= 0):
        raise ValueError("weighted linear fit received invalid values/errors")
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
        p_value=float(stats.chi2.sf(chi2, dof)) if dof > 0 else float("nan"),
    )


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
    polarization: Mapping[str, object] = field(default_factory=dict)
    polarization_ready: bool = False
    physics_ready: bool = False
    claim_status: str = "UNASSESSED"
    artifacts: Mapping[str, str] = field(default_factory=dict)


CHECKPOINT_SCHEMA = 3


@dataclass(frozen=True)
class EnsemblePaths:
    root: Path
    checkpoint: Path
    manifest: Path
    t1_observations: Path
    polarization_observations: Path
    torelon_observations: Path
    plaquettes: Path
    acceptances: Path
    analysis_bundle: Path


def ensemble_slug(cfg: EnsembleConfig) -> str:
    beta = f"{cfg.beta:.4f}".replace(".", "p")
    return f"beta_{beta}_L{cfg.L}_Nt{cfg.Nt}_seed{cfg.seed}"


def ensemble_paths(output_dir: Path, cfg: EnsembleConfig) -> EnsemblePaths:
    root = output_dir / ensemble_slug(cfg)
    return EnsemblePaths(
        root=root,
        checkpoint=root / "chain_checkpoint.npz",
        manifest=root / "manifest.json",
        t1_observations=root / "t1_observations.npy",
        polarization_observations=root / "polarization_observations.npy",
        torelon_observations=root / "torelon_observations.npy",
        plaquettes=root / "plaquettes.npy",
        acceptances=root / "acceptances.npy",
        analysis_bundle=root / "correlator_blocks.npz",
    )


def trajectory_fingerprint(cfg: EnsembleConfig) -> str:
    """Hash only fields that change the generated chain or measured operators."""
    payload = {
        key: value
        for key, value in asdict(cfg).items()
        if key not in {
            "prefer_gpu",
            "install_cupy",
            "bootstrap_samples",
            "fit_tmin",
            "fit_tmax",
            "gevp_rcond",
            "max_basis_rank",
            "max_basis_condition",
            "fit_scan_padding",
            "min_bootstrap_success",
            "max_bootstrap_boundary_fraction",
            "max_t1_relative_error",
            "max_torelon_relative_error",
            "min_stable_fits",
            "fit_stability_z",
            "checkpoint_every",
            "published_asqrt_sigma",
            "published_asqrt_sigma_error",
            "published_mass",
            "published_mass_error",
        }
    }
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def deterministic_resume_seed(cfg: EnsembleConfig, thermal_done: int, production_done: int, serial: int) -> int:
    raw = f"{cfg.seed}:{thermal_done}:{production_done}:{serial}:resume".encode("ascii")
    return int.from_bytes(hashlib.sha256(raw).digest()[:4], "little")


def atomic_json_write(path: Path, payload: Mapping[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


class MeasurementStore:
    """Fixed-shape append store; checkpoint count is the commit marker."""

    def __init__(self, paths: EnsemblePaths, cfg: EnsembleConfig, resume: bool):
        self.paths = paths
        self.cfg = cfg
        paths.root.mkdir(parents=True, exist_ok=True)
        nop = len(cfg.ape_levels) * len(cfg.loop_shapes)
        shapes = {
            paths.t1_observations: ((cfg.n_cfg, nop, 3, cfg.Nt), np.dtype(np.float64)),
            paths.polarization_observations: (
                (cfg.n_cfg, nop, len(cfg.momentum_modes) if cfg.measure_polarization else 0, 3, cfg.Nt),
                np.dtype(np.complex64),
            ),
            paths.torelon_observations: ((cfg.n_cfg, len(cfg.ape_levels), 3, cfg.Nt), np.dtype(np.complex128)),
            paths.plaquettes: ((cfg.n_cfg,), np.dtype(np.float64)),
            paths.acceptances: ((cfg.n_cfg,), np.dtype(np.float64)),
        }
        exists = {path: path.exists() for path in shapes}
        if any(exists.values()) and not all(exists.values()):
            missing = [str(path) for path, ok in exists.items() if not ok]
            raise RuntimeError(f"incomplete measurement store; missing {missing}")
        if all(exists.values()) and not resume:
            raise RuntimeError(
                f"measurement files already exist in {paths.root}; use --resume or choose a new --output-dir"
            )

        self.arrays: Dict[Path, NDArray] = {}
        for path, (shape, dtype) in shapes.items():
            mode = "r+" if all(exists.values()) else "w+"
            arr = np.lib.format.open_memmap(path, mode=mode, dtype=dtype, shape=shape)
            if arr.shape != shape or arr.dtype != dtype:
                raise RuntimeError(
                    f"measurement store mismatch for {path}: got {arr.shape}/{arr.dtype}, expected {shape}/{dtype}"
                )
            self.arrays[path] = arr

        self.t1 = self.arrays[paths.t1_observations]
        self.polarization = self.arrays[paths.polarization_observations]
        self.torelon = self.arrays[paths.torelon_observations]
        self.p = self.arrays[paths.plaquettes]
        self.acc = self.arrays[paths.acceptances]

    def record(
        self,
        index: int,
        t1: NDArray[np.float64],
        polarization: NDArray[np.complex64],
        torelon: NDArray[np.complex128],
        plaquette: float,
        acceptance: float,
    ) -> None:
        self.t1[index] = t1
        self.polarization[index] = polarization
        self.torelon[index] = torelon
        self.p[index] = plaquette
        self.acc[index] = acceptance

    def flush(self) -> None:
        for arr in self.arrays.values():
            arr.flush()

    def completed_arrays(self, count: int) -> Tuple[NDArray, NDArray, NDArray, NDArray, NDArray]:
        return (
            np.asarray(self.t1[:count]),
            np.asarray(self.polarization[:count]),
            np.asarray(self.torelon[:count]),
            np.asarray(self.p[:count]),
            np.asarray(self.acc[:count]),
        )


def save_chain_checkpoint(
    path: Path,
    lat: SU3WilsonLattice,
    cfg: EnsembleConfig,
    phase: str,
    thermal_done: int,
    production_done: int,
    thermal_plaquettes: Sequence[float],
    thermal_acceptances: Sequence[float],
    bridge_rows: Sequence[Mapping[str, float]],
    serial: int,
) -> None:
    lat.B.sync()
    metadata = {
        "schema": CHECKPOINT_SCHEMA,
        "fingerprint": trajectory_fingerprint(cfg),
        "phase": phase,
        "thermal_done": int(thermal_done),
        "production_done": int(production_done),
        "proposal_size": float(lat.proposal_size),
        "last_overrelaxation_error": float(lat._last_or_error),
        "bridge_rows": [dict(row) for row in bridge_rows],
        "serial": int(serial),
        "config": asdict(cfg),
        "saved_unix_time": time.time(),
        "rng_note": (
            "CuPy random states are not serializable; resume restores U exactly and starts a "
            "deterministic fresh substream derived from the checkpoint counters."
        ),
    }
    tmp = path.with_name(path.name + ".tmp.npz")
    np.savez(
        tmp,
        U=lat.B.to_numpy(lat.U).astype(np.complex64, copy=False),
        thermal_plaquettes=np.asarray(thermal_plaquettes, dtype=np.float64),
        thermal_acceptances=np.asarray(thermal_acceptances, dtype=np.float64),
        metadata=np.asarray(json.dumps(metadata, separators=(",", ":"))),
    )
    os.replace(tmp, path)


def load_chain_checkpoint(path: Path, lat: SU3WilsonLattice, cfg: EnsembleConfig) -> Mapping[str, object]:
    with np.load(path, allow_pickle=False) as payload:
        metadata = json.loads(str(payload["metadata"].item()))
        if int(metadata.get("schema", -1)) != CHECKPOINT_SCHEMA:
            raise RuntimeError(f"unsupported checkpoint schema in {path}")
        if metadata.get("fingerprint") != trajectory_fingerprint(cfg):
            raise RuntimeError(
                "checkpoint configuration does not match the requested chain/measurement configuration"
            )
        U = np.asarray(payload["U"], dtype=np.complex64)
        if U.shape != tuple(lat.U.shape):
            raise RuntimeError(f"checkpoint lattice shape {U.shape} != requested {tuple(lat.U.shape)}")
        lat.U = lat.xp.asarray(U)
        lat.proposal_size = float(metadata["proposal_size"])
        lat._last_or_error = float(metadata.get("last_overrelaxation_error", 0.0))
        metadata["thermal_plaquettes"] = np.asarray(payload["thermal_plaquettes"], dtype=float).tolist()
        metadata["thermal_acceptances"] = np.asarray(payload["thermal_acceptances"], dtype=float).tolist()
    resume_seed = deterministic_resume_seed(
        cfg,
        int(metadata["thermal_done"]),
        int(metadata["production_done"]),
        int(metadata.get("serial", 0)),
    )
    lat.B.reseed(resume_seed)
    metadata["resume_seed"] = resume_seed
    return metadata


def save_correlator_bundle(
    path: Path,
    cfg: EnsembleConfig,
    block_size: int,
    t1_blocks: NDArray[np.float64],
    torelon_blocks: NDArray[np.float64],
    plaquettes: NDArray[np.float64],
    acceptances: NDArray[np.float64],
    polarization_blocks: Optional[Mapping[str, NDArray[np.float64]]] = None,
) -> None:
    tmp = path.with_name(path.name + ".tmp.npz")
    np.savez_compressed(
        tmp,
        config=np.asarray(json.dumps(asdict(cfg), separators=(",", ":"))),
        block_size=np.asarray(block_size, dtype=np.int64),
        t1_correlator_blocks=np.asarray(t1_blocks, dtype=np.float64),
        torelon_correlator_blocks=np.asarray(torelon_blocks, dtype=np.float64),
        plaquettes=np.asarray(plaquettes, dtype=np.float64),
        acceptances=np.asarray(acceptances, dtype=np.float64),
        **{
            f"polarization_{name}_correlator_blocks": np.asarray(blocks, dtype=np.float64)
            for name, blocks in (polarization_blocks or {}).items()
        },
    )
    os.replace(tmp, path)


def standard_error_blocked(x: NDArray[np.float64], block_size: int) -> float:
    b = block_mean(np.asarray(x, dtype=float), block_size)
    return float(np.std(b, ddof=1) / math.sqrt(len(b))) if len(b) > 1 else float("nan")


def thermalize(
    lat: SU3WilsonLattice,
    start_cycle: int = 0,
    plaquettes: Optional[Sequence[float]] = None,
    acceptances: Optional[Sequence[float]] = None,
    on_monitor: Optional[Callable[[int, Sequence[float], Sequence[float]], None]] = None,
) -> Tuple[List[float], List[float]]:
    cfg = lat.cfg
    p_history = list(plaquettes or [])
    a_history = list(acceptances or [])
    subheading("Thermalisation")
    start = time.time()
    monitor_window: List[float] = []
    if start_cycle and start_cycle % cfg.monitor_every:
        raise RuntimeError("thermal checkpoint is not aligned to a monitor boundary")
    if start_cycle:
        print(f"  resuming after cycle {start_cycle}/{cfg.thermal_cycles}")
    for cyc in range(start_cycle + 1, cfg.thermal_cycles + 1):
        acc = lat.cycle(audit_overrelax=(cyc == start_cycle + 1))
        monitor_window.append(acc)
        if cyc % cfg.monitor_every == 0 or cyc == cfg.thermal_cycles:
            p = lat.plaquette()
            a = float(np.mean(monitor_window))
            p_history.append(p)
            a_history.append(a)
            # Robbins-Monro adaptation occurs only before production.
            lat.proposal_size *= math.exp(0.45 * (a - cfg.target_acceptance))
            lat.proposal_size = float(np.clip(lat.proposal_size, 0.03, 1.20))
            monitor_window.clear()
            print(
                f"  cycle {cyc:6d}/{cfg.thermal_cycles}: plaquette={p:.8f}, "
                f"accept={a:.4f}, proposal={lat.proposal_size:.4f}"
            )
            if on_monitor is not None:
                on_monitor(cyc, p_history, a_history)
        if cyc % 50 == 0:
            lat.reunitarize()
    lat.reunitarize()
    print(f"  thermalisation wall time: {time.time()-start:.2f} s")
    return p_history, a_history


def thermalization_gates(
    lat: SU3WilsonLattice,
    p_hist: Sequence[float],
    a_hist: Sequence[float],
    hard_equilibrium: bool,
) -> None:
    n = len(p_hist)
    gate(
        "thermalisation monitor coverage",
        n >= 12,
        f"{n} monitor points (target >=12)",
        hard=hard_equilibrium,
    )
    if n >= 8:
        tail = np.asarray(p_hist[n // 2 :], dtype=float)
        a, b = np.array_split(tail, 2)
        denom = math.sqrt(np.var(a, ddof=1) / len(a) + np.var(b, ddof=1) / len(b)) if len(a) > 1 and len(b) > 1 else float("inf")
        z = abs(float(a.mean() - b.mean())) / denom if denom > 0 else 0.0
        x = np.arange(len(tail), dtype=float)
        regression = stats.linregress(x, tail) if len(tail) >= 3 else None
        slope_z = (
            abs(float(regression.slope / regression.stderr))
            if regression is not None and regression.stderr not in (None, 0.0)
            else float("inf")
        )
        equilibrium_ok = z < 3.0 and slope_z < 3.0
        gate(
            "thermalisation stationarity",
            equilibrium_ok,
            f"tail split z={z:.3f}, slope z={slope_z:.3f} (both <3)",
            hard=hard_equilibrium,
        )
    else:
        gate("thermalisation stationarity", False, f"only {n} monitor points", hard=False)
    mean_acc = float(np.mean(a_hist[-max(1, len(a_hist)//2) :]))
    gate("Metropolis acceptance", 0.40 < mean_acc < 0.70, f"tail mean={mean_acc:.4f} (target 0.40-0.70)")
    gate("over-relaxation invariance", lat._last_or_error < 2e-4, f"max local action drift={lat._last_or_error:.3e}")
    unit, det = lat.group_errors()
    gate("SU(3) unitarity", unit < 2e-4 and det < 2e-4, f"max ||U^dag U-I||F={unit:.3e}, max |detU-1|={det:.3e}")


def run_ensemble(cfg: EnsembleConfig, output_dir: Path, resume: bool = True) -> EnsembleResult:
    heading(f"B. SU(3) T1^{{+-}} ENSEMBLE: beta={cfg.beta}, {cfg.L}^3 x {cfg.Nt}")
    start = time.time()
    gate_start = len(GATES)
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
    paths = ensemble_paths(output_dir, cfg)
    paths.root.mkdir(parents=True, exist_ok=True)
    print(f"  run directory: {paths.root}")

    lat = SU3WilsonLattice(cfg, backend)
    thermal_done = 0
    production_done = 0
    checkpoint_serial = 0
    p_hist: List[float] = []
    a_hist: List[float] = []
    bridge_rows: List[Mapping[str, float]] = []
    resumed = False
    if paths.checkpoint.exists():
        if not resume:
            raise RuntimeError(
                f"checkpoint already exists at {paths.checkpoint}; use --resume or choose a new --output-dir"
            )
        metadata = load_chain_checkpoint(paths.checkpoint, lat, cfg)
        thermal_done = int(metadata["thermal_done"])
        production_done = int(metadata["production_done"])
        checkpoint_serial = int(metadata.get("serial", 0))
        p_hist = [float(x) for x in metadata.get("thermal_plaquettes", [])]
        a_hist = [float(x) for x in metadata.get("thermal_acceptances", [])]
        bridge_rows = [dict(row) for row in metadata.get("bridge_rows", [])]
        if thermal_done > cfg.thermal_cycles or production_done > cfg.n_cfg:
            raise RuntimeError("checkpoint progress exceeds the requested profile")
        resumed = True
        print(
            f"  resumed checkpoint: phase={metadata.get('phase')}, thermal={thermal_done}/{cfg.thermal_cycles}, "
            f"measurements={production_done}/{cfg.n_cfg}, fresh RNG substream seed={metadata['resume_seed']}"
        )
    else:
        orphaned = [
            path for path in (
                paths.t1_observations,
                paths.polarization_observations,
                paths.torelon_observations,
                paths.plaquettes,
                paths.acceptances,
            )
            if path.exists()
        ]
        if orphaned:
            raise RuntimeError(
                f"measurement files exist without a checkpoint in {paths.root}; choose a new --output-dir"
            )

    atomic_json_write(
        paths.manifest,
        {
            "schema": CHECKPOINT_SCHEMA,
            "fingerprint": trajectory_fingerprint(cfg),
            "config": asdict(cfg),
            "checkpoint": str(paths.checkpoint),
            "resume_enabled": bool(resume),
        },
    )

    stencil_error = lat.audit_local_action_stencil()
    gate(
        "Wilson action/staple identity",
        stencil_error < 5e-5,
        f"one-link total/local trace mismatch={stencil_error:.3e}",
    )
    if stencil_error >= 5e-5:
        raise RuntimeError("Wilson action/staple audit failed; refusing to evolve the chain")

    def thermal_checkpoint(cycle: int, p_values: Sequence[float], a_values: Sequence[float]) -> None:
        nonlocal checkpoint_serial
        checkpoint_serial += 1
        save_chain_checkpoint(
            paths.checkpoint,
            lat,
            cfg,
            phase="thermal",
            thermal_done=cycle,
            production_done=0,
            thermal_plaquettes=p_values,
            thermal_acceptances=a_values,
            bridge_rows=bridge_rows,
            serial=checkpoint_serial,
        )

    if thermal_done < cfg.thermal_cycles:
        if production_done:
            raise RuntimeError("cannot resume production from an incompletely thermalized checkpoint")
        p_hist, a_hist = thermalize(
            lat,
            start_cycle=thermal_done,
            plaquettes=p_hist,
            acceptances=a_hist,
            on_monitor=thermal_checkpoint,
        )
        thermal_done = cfg.thermal_cycles
        checkpoint_serial += 1
        save_chain_checkpoint(
            paths.checkpoint,
            lat,
            cfg,
            phase="thermal_ready",
            thermal_done=thermal_done,
            production_done=0,
            thermal_plaquettes=p_hist,
            thermal_acceptances=a_hist,
            bridge_rows=bridge_rows,
            serial=checkpoint_serial,
        )
    else:
        print("\nThermalisation\n--------------")
        print("  complete in checkpoint; no thermal cycles repeated")
    thermalization_gates(lat, p_hist, a_hist, hard_equilibrium=physics_target)
    preproduction_failures = [g for g in GATES[gate_start:] if g.hard and not g.passed]
    if physics_target and preproduction_failures:
        names = ", ".join(g.name for g in preproduction_failures)
        atomic_json_write(
            paths.manifest,
            {
                "schema": CHECKPOINT_SCHEMA,
                "fingerprint": trajectory_fingerprint(cfg),
                "config": asdict(cfg),
                "checkpoint": str(paths.checkpoint),
                "claim_status": "THERMALIZATION_REJECTED",
                "failed_gates": names,
            },
        )
        raise AssertionError(f"production refused after failed pre-production gate(s): {names}")

    subheading("Production and measurements")
    store = MeasurementStore(paths, cfg, resume=resumed)
    prod_start = time.time()
    if 0 < production_done < cfg.n_cfg:
        print(f"  resuming at measurement {production_done + 1}/{cfg.n_cfg}")
    elif production_done == cfg.n_cfg:
        print("  complete in checkpoint; no production measurements repeated")
    for icfg in range(production_done, cfg.n_cfg):
        rates = []
        for _ in range(cfg.separation_cycles):
            rates.append(lat.cycle())
        if (icfg + 1) % 25 == 0:
            lat.reunitarize()
        p = lat.plaquette()
        t1, tor, pol = lat.measure_multiscale()
        acceptance = float(np.mean(rates))
        store.record(icfg, t1, pol, tor, p, acceptance)
        if icfg in {0, cfg.n_cfg // 2, cfg.n_cfg - 1}:
            bridge_rows.append(lat.sampled_weak_field_bridge())
        report_every = max(1, cfg.n_cfg // 10)
        if (icfg + 1) % report_every == 0 or icfg == 0:
            print(
                f"  cfg {icfg+1:5d}/{cfg.n_cfg}: plaquette={p:.8f}, "
                f"accept={acceptance:.4f}, elapsed={time.time()-prod_start:.1f}s"
            )
        committed = icfg + 1
        if committed % cfg.checkpoint_every == 0 or committed == cfg.n_cfg:
            store.flush()
            checkpoint_serial += 1
            save_chain_checkpoint(
                paths.checkpoint,
                lat,
                cfg,
                phase="complete" if committed == cfg.n_cfg else "production",
                thermal_done=thermal_done,
                production_done=committed,
                thermal_plaquettes=p_hist,
                thermal_acceptances=a_hist,
                bridge_rows=bridge_rows,
                serial=checkpoint_serial,
            )
            print(f"  checkpoint committed at measurement {committed}")

    production_done = cfg.n_cfg
    store.flush()
    t1_arr, pol_arr, tor_arr, p_arr, acceptance_arr = store.completed_arrays(production_done)
    if not bridge_rows:
        bridge_rows.append(lat.sampled_weak_field_bridge())

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
    gate(
        "bootstrap block count",
        nblock >= 24,
        f"{nblock} blocks of {block_size} measurements (physics target >=24)",
        hard=physics_target,
    )
    gate(
        "production Metropolis acceptance",
        0.40 < float(np.mean(acceptance_arr)) < 0.70,
        f"mean={float(np.mean(acceptance_arr)):.4f} (target 0.40-0.70)",
        hard=physics_target,
    )

    # Smoke runs can be deliberately too small for a mass.  The exact and
    # Markov-chain gates still run, while spectroscopy is reported honestly.
    if nblock >= 4:
        t1_res, t1_blocks = analyze_channel(
            t1_arr,
            Nt=cfg.Nt,
            tmin=cfg.fit_tmin,
            tmax=cfg.fit_tmax,
            n_boot=cfg.bootstrap_samples,
            seed=cfg.seed + 11,
            block_size=block_size,
            complex_channel=False,
            raw_index=0,
            rcond=cfg.gevp_rcond,
            max_rank=cfg.max_basis_rank,
            max_condition=cfg.max_basis_condition,
            fit_scan_padding=cfg.fit_scan_padding,
            min_bootstrap_success=cfg.min_bootstrap_success,
            max_boundary_fraction=cfg.max_bootstrap_boundary_fraction,
            max_relative_error=cfg.max_t1_relative_error,
            min_stable_fits=cfg.min_stable_fits,
            stability_z=cfg.fit_stability_z,
        )
        tor_res, tor_blocks = analyze_channel(
            tor_arr,
            Nt=cfg.Nt,
            tmin=cfg.fit_tmin,
            tmax=cfg.fit_tmax,
            n_boot=cfg.bootstrap_samples,
            seed=cfg.seed + 29,
            block_size=block_size,
            complex_channel=True,
            raw_index=None,
            rcond=cfg.gevp_rcond,
            max_rank=cfg.max_basis_rank,
            max_condition=cfg.max_basis_condition,
            fit_scan_padding=cfg.fit_scan_padding,
            min_bootstrap_success=cfg.min_bootstrap_success,
            max_boundary_fraction=cfg.max_bootstrap_boundary_fraction,
            max_relative_error=cfg.max_torelon_relative_error,
            min_stable_fits=cfg.min_stable_fits,
            stability_z=cfg.fit_stability_z,
        )
    else:
        raise RuntimeError("not enough blocks even for smoke spectroscopy")

    polarization_results: Dict[str, object] = {}
    polarization_blocks: Dict[str, NDArray[np.float64]] = {}
    polarization_ready = False
    if cfg.measure_polarization and pol_arr.shape[2] == len(cfg.momentum_modes):
        subheading("Finite-momentum incidence polarization spectroscopy")
        all_resolved = True
        for imode, mode in enumerate(cfg.momentum_modes):
            label = mode_label(mode)
            # [cfg,op,1,Nt] and [cfg,op,2,Nt]
            long_obs = np.asarray(pol_arr[:, :, imode, 0:1, :], dtype=np.complex128)
            trans_obs = np.asarray(pol_arr[:, :, imode, 1:3, :], dtype=np.complex128)
            long_res, long_blocks = analyze_channel(
                long_obs,
                Nt=cfg.Nt,
                tmin=cfg.fit_tmin,
                tmax=cfg.fit_tmax,
                n_boot=cfg.bootstrap_samples,
                seed=cfg.seed + 101 + 10 * imode,
                block_size=block_size,
                complex_channel=True,
                raw_index=None,
                rcond=cfg.gevp_rcond,
                max_rank=cfg.max_basis_rank,
                max_condition=cfg.max_basis_condition,
                fit_scan_padding=cfg.fit_scan_padding,
                min_bootstrap_success=cfg.min_bootstrap_success,
                max_boundary_fraction=cfg.max_bootstrap_boundary_fraction,
                max_relative_error=cfg.max_t1_relative_error,
                min_stable_fits=cfg.min_stable_fits,
                stability_z=cfg.fit_stability_z,
            )
            trans_res, trans_blocks = analyze_channel(
                trans_obs,
                Nt=cfg.Nt,
                tmin=cfg.fit_tmin,
                tmax=cfg.fit_tmax,
                n_boot=cfg.bootstrap_samples,
                seed=cfg.seed + 102 + 10 * imode,
                block_size=block_size,
                complex_channel=True,
                raw_index=None,
                rcond=cfg.gevp_rcond,
                max_rank=cfg.max_basis_rank,
                max_condition=cfg.max_basis_condition,
                fit_scan_padding=cfg.fit_scan_padding,
                min_bootstrap_success=cfg.min_bootstrap_success,
                max_boundary_fraction=cfg.max_bootstrap_boundary_fraction,
                max_relative_error=cfg.max_t1_relative_error,
                min_stable_fits=cfg.min_stable_fits,
                stability_z=cfg.fit_stability_z,
            )
            momentum = momentum_from_mode(mode, cfg.L)
            _, gram = incidence_symbol(momentum)
            polarization_results[label] = {
                "mode": [int(x) for x in mode],
                "momentum": momentum.tolist(),
                "momentum_norm": float(np.linalg.norm(momentum)),
                "lattice_phat": float(math.sqrt(gram)),
                "longitudinal": asdict(long_res),
                "transverse": asdict(trans_res),
            }
            polarization_blocks[f"{label}_L"] = long_blocks
            polarization_blocks[f"{label}_T"] = trans_blocks
            all_resolved &= bool(long_res.resolved and trans_res.resolved)
            print(
                f"  k={tuple(mode)}: E_L={long_res.mass:.6f} +/- {long_res.mass_error:.6f}; "
                f"E_T={trans_res.mass:.6f} +/- {trans_res.mass_error:.6f}; "
                f"resolved L/T={long_res.resolved}/{trans_res.resolved}"
            )
            gate(
                f"polarization {label} longitudinal resolved",
                long_res.resolved,
                f"E_L={long_res.mass:.4f}, relerr={long_res.relative_error:.3f}",
                hard=False,
            )
            gate(
                f"polarization {label} transverse resolved",
                trans_res.resolved,
                f"E_T={trans_res.mass:.4f}, relerr={trans_res.relative_error:.3f}",
                hard=False,
            )
        polarization_ready = bool(all_resolved)

    save_correlator_bundle(
        paths.analysis_bundle,
        cfg,
        block_size,
        t1_blocks,
        tor_blocks,
        p_arr,
        acceptance_arr,
        polarization_blocks=polarization_blocks,
    )

    asqrt = (
        string_tension_from_torelon(tor_res.mass, cfg.L)
        if np.isfinite(tor_res.mass) and tor_res.mass > 0
        else float("nan")
    )
    asqrt_err = (
        propagate_string_error(tor_res.mass, tor_res.mass_error, cfg.L)
        if np.isfinite(tor_res.mass_error) and np.isfinite(asqrt)
        else float("nan")
    )
    ratio = t1_res.mass / asqrt if np.isfinite(t1_res.mass) and asqrt > 0 else float("nan")
    ratio_err = (
        ratio * math.sqrt((t1_res.mass_error / t1_res.mass) ** 2 + (asqrt_err / asqrt) ** 2)
        if np.isfinite(ratio) and t1_res.mass > 0 and asqrt > 0
        else float("nan")
    )
    # Derived finite-momentum observables in the same ensemble scale.
    if polarization_results:
        for entry in polarization_results.values():
            if asqrt > 0 and np.isfinite(asqrt):
                entry["p_over_sqrt_sigma"] = float(entry["momentum_norm"] / asqrt)
                entry["phat_over_sqrt_sigma"] = float(entry["lattice_phat"] / asqrt)
        axis = polarization_results.get("100")
        diagonal = polarization_results.get("111")
        derived: Dict[str, object] = {}
        if axis is not None:
            l = axis["longitudinal"]
            t = axis["transverse"]
            EL, ET = float(l["mass"]), float(t["mass"])
            sEL, sET = float(l["mass_error"]), float(t["mass_error"])
            if asqrt > 0 and np.isfinite(EL) and np.isfinite(ET):
                delta = (EL - ET) / asqrt
                delta_err = math.sqrt(sEL * sEL + sET * sET) / asqrt
                derived["delta_LT_100_over_sqrt_sigma"] = delta
                derived["delta_LT_100_over_sqrt_sigma_error_independent"] = delta_err
                k2 = float(axis["momentum_norm"]) ** 2
                if k2 > 0 and np.isfinite(t1_res.mass):
                    derived["longitudinal_small_p_curvature"] = (EL - t1_res.mass) * asqrt / k2
                    derived["transverse_small_p_curvature"] = (ET - t1_res.mass) * asqrt / k2
                    derived["relativistic_curvature_from_rest_mass"] = 1.0 / (2.0 * ratio) if ratio > 0 else float("nan")
        if axis is not None and diagonal is not None:
            try:
                derived["longitudinal_shell_ratios"] = dispersion_shell_ratios(
                    t1_res.mass,
                    float(axis["longitudinal"]["mass"]),
                    float(diagonal["longitudinal"]["mass"]),
                )
            except Exception as exc:
                derived["longitudinal_shell_ratio_error"] = str(exc)
            try:
                derived["transverse_shell_ratios"] = dispersion_shell_ratios(
                    t1_res.mass,
                    float(axis["transverse"]["mass"]),
                    float(diagonal["transverse"]["mass"]),
                )
            except Exception as exc:
                derived["transverse_shell_ratio_error"] = str(exc)
        polarization_results = {
            "modes": polarization_results,
            "derived": derived,
        }
    p_err = standard_error_blocked(p_arr, block_size)

    subheading("Spectroscopy result")
    print(
        f"  T1^{{+-}}: aM={t1_res.mass:.6f} +/- {t1_res.mass_error:.6f}, "
        f"fit [{cfg.fit_tmin},{cfg.fit_tmax}], chi2/dof={t1_res.chi2:.2f}/{t1_res.dof}, p={t1_res.p_value:.3f}"
    )
    print(
        f"    bootstrap q16/median/q84={t1_res.mass_q16:.6f}/{t1_res.mass_q50:.6f}/{t1_res.mass_q84:.6f}; "
        f"success={t1_res.bootstrap_successes}/{t1_res.bootstrap_attempts}, "
        f"boundary={t1_res.boundary_fraction:.3f}"
    )
    print(
        f"    resolved={t1_res.resolved}; stable fits={t1_res.stable_fit_count}, "
        f"max stability z={t1_res.stability_max_z:.3f}, plateau={t1_res.plateau_pair or 'none'}"
    )
    if t1_res.resolution_reasons:
        print("    rejection: " + "; ".join(t1_res.resolution_reasons))
    print(
        f"  torelon:  aE={tor_res.mass:.6f} +/- {tor_res.mass_error:.6f} -> "
        f"a sqrt(sigma)={asqrt:.6f} +/- {asqrt_err:.6f}"
    )
    print(
        f"    bootstrap q16/median/q84={tor_res.mass_q16:.6f}/{tor_res.mass_q50:.6f}/{tor_res.mass_q84:.6f}; "
        f"success={tor_res.bootstrap_successes}/{tor_res.bootstrap_attempts}, "
        f"boundary={tor_res.boundary_fraction:.3f}, resolved={tor_res.resolved}"
    )
    if tor_res.resolution_reasons:
        print("    rejection: " + "; ".join(tor_res.resolution_reasons))
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
    gate(
        "T1 resolved spectroscopy",
        t1_res.resolved,
        f"aM={t1_res.mass:.4f}, relerr={t1_res.relative_error:.3f}, stable={t1_res.stable_fit_count}",
        hard=physical_run,
    )
    gate(
        "torelon resolved spectroscopy",
        tor_res.resolved,
        f"aE={tor_res.mass:.4f}, relerr={tor_res.relative_error:.3f}, stable={tor_res.stable_fit_count}",
        hard=physical_run,
    )
    volume_scale = cfg.L * asqrt
    gate(
        "finite-volume scale",
        np.isfinite(volume_scale) and volume_scale >= 3.0,
        f"L a sqrt(sigma)={volume_scale:.3f} (target >=3)",
        hard=physical_run,
    )

    if cfg.published_mass is not None:
        benchmark_error = float(cfg.published_mass_error or 0.0)
        denominator = math.sqrt(t1_res.mass_error**2 + benchmark_error**2)
        pull = (t1_res.mass - cfg.published_mass) / max(denominator, 1e-12)
        gate(
            "published lattice-mass benchmark",
            t1_res.resolved and abs(pull) < 4.0,
            f"new={t1_res.mass:.4f}, published={cfg.published_mass:.4f}, combined pull={pull:+.2f}",
            hard=physical_run,
        )
    if cfg.published_asqrt_sigma is not None:
        benchmark_error = float(cfg.published_asqrt_sigma_error or 0.0)
        denominator = math.sqrt(asqrt_err**2 + benchmark_error**2)
        pull = (asqrt - cfg.published_asqrt_sigma) / max(denominator, 1e-12)
        gate(
            "published string-scale benchmark",
            tor_res.resolved and abs(pull) < 4.0,
            f"new={asqrt:.5f}, published={cfg.published_asqrt_sigma:.5f}, combined pull={pull:+.2f}",
            hard=physical_run,
        )

    fraw = t1_res.raw_ground_fraction
    gate(
        "raw plaquette fraction stability",
        t1_res.raw_fraction_stable is True,
        (
            f"fraction={fraw:.4f} +/- {t1_res.raw_ground_fraction_error:.4f}, "
            f"rank/window spread={t1_res.raw_fraction_stability_spread}"
            if fraw is not None and t1_res.raw_ground_fraction_error is not None
            else "fraction not resolved"
        ),
        hard=physical_run,
    )

    if polarization_results:
        derived = polarization_results.get("derived", {})
        print("\n  polarization bridge diagnostics:")
        if "delta_LT_100_over_sqrt_sigma" in derived:
            print(
                f"    (E_L-E_T)_100/sqrt(sigma)={derived['delta_LT_100_over_sqrt_sigma']:.6f} "
                f"+/- {derived['delta_LT_100_over_sqrt_sigma_error_independent']:.6f} [independent-error approx]"
            )
        if "longitudinal_shell_ratios" in derived:
            rr = derived["longitudinal_shell_ratios"]
            print(
                f"    L rotational ratios: shift={rr['energy_shift']:.6f}, "
                f"E2={rr['continuum_e2']:.6f}, cosh={rr['lattice_cosh']:.6f}"
            )
        if "longitudinal_small_p_curvature" in derived:
            print(
                f"    axis curvature L/T={derived['longitudinal_small_p_curvature']:.6f}/"
                f"{derived['transverse_small_p_curvature']:.6f}; "
                f"relativistic target from rest mass={derived['relativistic_curvature_from_rest_mass']:.6f}"
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

    ensemble_hard_failures = [g for g in GATES[gate_start:] if g.hard and not g.passed]
    physics_ready = bool(
        physical_run
        and not ensemble_hard_failures
        and t1_res.resolved
        and tor_res.resolved
        and t1_res.raw_fraction_stable is True
        and volume_scale >= 3.0
    )
    if physics_ready:
        claim_status = "PHYSICS_READY"
    elif physical_run:
        claim_status = "REJECTED_BY_HARD_GATES"
    else:
        claim_status = "DIAGNOSTIC_ONLY"

    result = EnsembleResult(
        config=asdict(cfg),
        backend=backend.name,
        plaquette_mean=float(p_arr.mean()),
        plaquette_error=p_err,
        acceptance_mean=float(np.mean(acceptance_arr)),
        tau_int_measurements=tau,
        bridge_metrics=bridge,
        t1=asdict(t1_res),
        torelon=asdict(tor_res),
        asqrt_sigma=asqrt,
        asqrt_sigma_error=asqrt_err,
        mass_over_sqrt_sigma=ratio,
        mass_over_sqrt_sigma_error=ratio_err,
        wall_seconds=time.time() - start,
        polarization=polarization_results,
        polarization_ready=polarization_ready,
        physics_ready=physics_ready,
        claim_status=claim_status,
        artifacts={
            "run_directory": str(paths.root),
            "checkpoint": str(paths.checkpoint),
            "manifest": str(paths.manifest),
            "t1_observations": str(paths.t1_observations),
            "polarization_observations": str(paths.polarization_observations),
            "torelon_observations": str(paths.torelon_observations),
            "correlator_blocks": str(paths.analysis_bundle),
        },
    )
    manifest = {
        "schema": CHECKPOINT_SCHEMA,
        "fingerprint": trajectory_fingerprint(cfg),
        "config": asdict(cfg),
        "checkpoint": str(paths.checkpoint),
        "resume_enabled": bool(resume),
        "claim_status": claim_status,
        "physics_ready": physics_ready,
        "polarization_ready": polarization_ready,
        "analysis_bundle": str(paths.analysis_bundle),
        "completed_measurements": production_done,
    }
    atomic_json_write(paths.manifest, manifest)
    print(f"  claim status: {claim_status}")
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
            checkpoint_every=50,
            published_asqrt_sigma=0.26118,
            published_asqrt_sigma_error=0.00037,
            published_mass=1.591,
            published_mass_error=0.018,
            **common,
        )
    if name == "polarization":
        # First deliberate p/sqrt(sigma)<1 run.  Same beta/Nt as the published
        # beta=5.99 point, but enlarged spatial volume L=30.  The string-scale
        # reference is coupling-matched; no published finite-volume mass is
        # imposed as a gate on this enlarged box.
        return EnsembleConfig(
            beta=5.9900,
            L=30,
            Nt=18,
            thermal_cycles=3000,
            n_cfg=8000,
            separation_cycles=5,
            overrelax_per_cycle=4,
            monitor_every=125,
            ape_levels=(0, 5, 15, 30),
            loop_shapes=("P", "R", "S"),
            bootstrap_samples=600,
            fit_tmin=1,
            fit_tmax=4,
            checkpoint_every=500,
            published_asqrt_sigma=0.21982,
            published_asqrt_sigma_error=0.00077,
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
                checkpoint_every=500,
                seed=seed + 1009 * i,
                prefer_gpu=not no_gpu,
                install_cupy=install_cupy,
                published_asqrt_sigma=float(PUBLISHED["asqrt_sigma"][i]),
                published_asqrt_sigma_error=float(PUBLISHED["asqrt_sigma_err"][i]),
                published_mass=float(PUBLISHED["aM_T1pm"][i]),
                published_mass_error=float(PUBLISHED["aM_T1pm_err"][i]),
            )
        )
    return out


def continuum_from_ensemble_results(results: Sequence[EnsembleResult]) -> ContinuumFit:
    if len(results) < 3:
        raise ValueError("at least three completed ensembles are required for a continuum fit")
    rejected = [
        f"beta={float(r.config['beta']):.4f}:{r.claim_status}"
        for r in results if not r.physics_ready
    ]
    if rejected:
        raise ValueError(
            "continuum fit refused because ensemble spectroscopy is not physics-ready: "
            + ", ".join(rejected)
        )
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


def polarization_continuum_from_ensemble_results(
    results: Sequence[EnsembleResult],
) -> ContinuumFit:
    """Fixed-physical-momentum continuum fit of (E_L-E_T)/sqrt(sigma).

    The standard beta>=5.99 published-volume trajectory keeps p_100/sqrt(sigma)
    near 1.60.  The coarse beta=5.8941 point is intentionally excluded from
    this fit because its matched momentum is visibly different; enlarged
    low-p runs belong to a separate momentum-flow analysis.
    """
    selected = [
        r for r in results
        if r.physics_ready and r.polarization_ready and float(r.config["beta"]) >= 5.99
    ]
    if len(selected) < 3:
        raise ValueError("need at least three beta>=5.99 physics/polarization-ready ensembles")
    selected = sorted(selected, key=lambda r: float(r.config["beta"]))
    x = np.asarray([r.asqrt_sigma**2 for r in selected], dtype=float)
    y = np.asarray([
        float(r.polarization["derived"]["delta_LT_100_over_sqrt_sigma"])
        for r in selected
    ], dtype=float)
    sy = np.asarray([
        float(r.polarization["derived"]["delta_LT_100_over_sqrt_sigma_error_independent"])
        for r in selected
    ], dtype=float)
    pphys = np.asarray([
        float(r.polarization["modes"]["100"]["p_over_sqrt_sigma"])
        for r in selected
    ], dtype=float)
    spread = float((pphys.max() - pphys.min()) / pphys.mean())
    fit = weighted_linear_fit(x, y, sy)
    heading("E. FIXED-MOMENTUM POLARIZATION CONTINUUM TEST")
    print("  beta       a^2 sigma    p100/sqrt(sigma)    (E_L-E_T)/sqrt(sigma)")
    for r, pp, yy, ss in zip(selected, pphys, y, sy):
        print(
            f"  {float(r.config['beta']):7.4f}    {r.asqrt_sigma**2:10.7f}        "
            f"{pp:10.6f}          {yy:+.6f} +/- {ss:.6f}"
        )
    print(
        f"\n  delta_LT/sqrt(sigma) = {fit.intercept:+.6f} +/- {fit.intercept_error:.6f} "
        f"+ ({fit.slope:+.4f} +/- {fit.slope_error:.4f}) a^2 sigma"
    )
    print(f"  chi2/dof={fit.chi2:.3f}/{fit.dof}, p={fit.p_value:.4f}; momentum spread={100*spread:.2f}%")
    gate(
        "fixed physical momentum matching",
        spread <= 0.05,
        f"p100/sqrt(sigma) fractional spread={spread:.4f} (target <=0.05)",
        hard=False,
    )
    pull0 = fit.intercept / max(fit.intercept_error, 1e-30)
    gate(
        "continuum longitudinal/transverse recombination",
        abs(pull0) < 3.0,
        f"continuum delta_LT={fit.intercept:+.5f} +/- {fit.intercept_error:.5f}, zero-pull={pull0:+.2f}",
        hard=False,
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
        choices=("smoke", "pilot", "polarization", "production", "continuum", "combine", "replay"),
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
    default_output = "/content/SU3_T1pm_hardened_run" if Path("/content").exists() else "SU3_T1pm_hardened_run"
    parser.add_argument(
        "--output-dir",
        default=default_output,
        help="checkpoint, raw-observation, and correlator-bundle directory",
    )
    parser.add_argument(
        "--no-resume",
        dest="resume",
        action="store_false",
        help="refuse an existing checkpoint instead of resuming it",
    )
    parser.set_defaults(resume=True)
    parser.add_argument(
        "--checkpoint-every",
        type=int,
        default=0,
        help="override the profile's production checkpoint interval",
    )
    parser.add_argument("--json", default="", help="optional path for a compact JSON result")
    args, unknown = parser.parse_known_args(argv)
    # Notebook kernels inject -f <kernel.json>; all unknown arguments are ignored.
    if unknown and not any(x == "--help" for x in unknown):
        print(f"Ignoring notebook/unknown arguments: {' '.join(unknown)}")
    return args


def final_summary(
    results: Sequence[EnsembleResult],
    replay: ContinuumFit,
    elapsed: float,
    new_fit: Optional[ContinuumFit] = None,
    polarization_fit: Optional[ContinuumFit] = None,
) -> None:
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
    physical_results = [r for r in results if r.physics_ready]
    if physical_results:
        print("    * New physics-ready computational evidence: the reported lattice mass, string scale,")
        print("      raw-operator fraction, and all stability/volume gates passed.")
    elif results:
        statuses = ", ".join(r.claim_status for r in results)
        print(f"    * No new physics claim is admitted from these ensembles ({statuses}).")
        print("      Numerical masses remain diagnostics unless every resolution and volume gate passes.")
    else:
        print("    * No new gauge ensemble was generated in replay mode.")
    if new_fit is not None:
        print("    * New continuum computational result: the six/partial ensemble mass fit printed above;")
        print("      its validity is conditional on every ensemble-level hard gate passing.")
    if polarization_fit is not None:
        print("    * New polarization-continuum result: the fixed-p longitudinal/transverse splitting")
        print("      was extrapolated versus a^2 sigma on the beta>=5.99 matched-momentum trajectory.")
    polarization_ready_results = [r for r in results if r.polarization_ready]
    if polarization_ready_results:
        print("    * Finite-momentum bridge data resolved: incidence-longitudinal/transverse energies are available")
        print("      for the configured (100)/(110)/(111) shells and can be continuum-compared.")
    elif results:
        print("    * Finite-momentum polarization measurements were attempted but are not yet fully resolved.")
    print("    * Not proven: equality of the one-plaquette Hamiltonian gap and the physical glueball mass.")
    if hard_failures:
        names = ", ".join(g.name for g in hard_failures)
        raise AssertionError(f"{len(hard_failures)} hard gate(s) failed: {names}")


def main(argv: Optional[Sequence[str]] = None) -> None:
    started = time.time()
    args = parse_args(argv)
    print("Spatial SU(3) T1^{+-} glueball polarization bridge -- hardened v3")
    print(f"profile={args.profile}, seed={args.seed}")
    output_dir = Path(args.output_dir).expanduser().resolve()
    run_symmetry_topology_certificate()
    replay = run_published_replay()
    results: List[EnsembleResult] = []
    new_fit: Optional[ContinuumFit] = None
    polarization_fit: Optional[ContinuumFit] = None
    if args.profile == "continuum":
        suite = continuum_production_configs(args.no_gpu, args.seed, install_cupy=args.install_cupy)
        if args.ensemble == "all":
            selected = suite
        else:
            idx = int(args.ensemble)
            if not 0 <= idx < len(suite):
                raise ValueError("--ensemble must be 0..5 or all")
            selected = [suite[idx]]
        if args.checkpoint_every > 0:
            for cfg in selected:
                cfg.checkpoint_every = args.checkpoint_every
        for cfg in selected:
            result = run_ensemble(cfg, output_dir=output_dir, resume=args.resume)
            results.append(result)
            if len(selected) > 1 and not result.physics_ready:
                print(
                    "\nStopping the continuum suite before the next ensemble because the completed "
                    f"ensemble is {result.claim_status}."
                )
                break
        if len(results) >= 3 and all(result.physics_ready for result in results):
            new_fit = continuum_from_ensemble_results(results)
        else:
            print("\n  Fewer than three physics-ready ensembles completed. Save each with --json and combine using")
            print("  --profile combine --inputs beta0.json beta1.json beta2.json ...")
        try:
            polarization_fit = polarization_continuum_from_ensemble_results(results)
        except ValueError as exc:
            print(f"\n  Polarization continuum fit not yet available: {exc}")
    elif args.profile == "combine":
        if len(args.inputs) < 3:
            raise ValueError("--profile combine requires at least three --inputs JSON files")
        results = load_ensemble_jsons(args.inputs)
        new_fit = continuum_from_ensemble_results(results)
        try:
            polarization_fit = polarization_continuum_from_ensemble_results(results)
        except ValueError as exc:
            print(f"\n  Polarization continuum fit not yet available: {exc}")
    else:
        cfg = profile_config(args.profile, args.no_gpu, args.seed, install_cupy=args.install_cupy)
        if cfg is not None:
            if args.checkpoint_every > 0:
                cfg.checkpoint_every = args.checkpoint_every
            results = [run_ensemble(cfg, output_dir=output_dir, resume=args.resume)]
    json_path = Path(args.json).expanduser().resolve() if args.json else output_dir / f"{args.profile}_summary.json"
    if args.profile != "replay" or args.json:
        payload = {
            "profile": args.profile,
            "published_replay": asdict(replay),
            "ensemble": asdict(results[0]) if len(results) == 1 else None,
            "ensembles": [asdict(r) for r in results],
            "new_continuum_fit": asdict(new_fit) if new_fit is not None else None,
            "polarization_continuum_fit": asdict(polarization_fit) if polarization_fit is not None else None,
            "gates": [asdict(g) for g in GATES],
        }
        atomic_json_write(json_path, payload)
        print(f"\nWrote JSON result: {json_path}")
    final_summary(
        results, replay, time.time() - started, new_fit=new_fit, polarization_fit=polarization_fit
    )


if __name__ == "__main__":
    main()
