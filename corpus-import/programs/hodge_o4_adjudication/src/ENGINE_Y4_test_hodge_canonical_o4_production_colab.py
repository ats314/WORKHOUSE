from __future__ import annotations

import base64
import ast
import contextlib
import copy
import errno
import gzip
import hashlib
import importlib.util
import inspect
import io
import json
import lzma
import os
import subprocess
import sys
import tempfile
import unittest
from fractions import Fraction
from pathlib import Path
from unittest import mock


HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "ENGINE_Y4_hodge_canonical_o4_production_colab.py"
NOTEBOOK = HERE / "NB_Y4_hodge_canonical_o4_production_colab.ipynb"
ARCHIVED_STAGE_I_FIXTURE = HERE / "DATA_Y4_stagei_authority_fixture.xz.b85"
SPEC = importlib.util.spec_from_file_location("hodge_y4_production_tested", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
Y4 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = Y4
SPEC.loader.exec_module(Y4)


# The 1,166-byte archived exact kernel is the only physical fixture needed by
# these cheap tests.  It is decoded into an operating-system temporary folder.
ARCHIVED_KERNEL_B64 = (
    "H4sICAAAAAAC/3k0X2Z1bGxfcmVhbF9zcGFjZV9INF9rZXJuZWwuanNvbgDNXE1v00AQ/S8+"
    "x83MrD/W3BAqHweERHtBCEVu7JRAm1R1WgRV/zvb9IBQaxTP7jwhRT24iV9m5828l51N7r"
    "Lv/fWmv8hefL7LuvVwddEu+8t+swsXcpnRjL7MsvXm6ma3CP/a9OEyzThc297snl780a/P"
    "v4aXZq6iQtiVPC/ISV0RN048UXY/ewrDs/CIxRHiygWEpqqKURwKSIh4tMuWC5UBhFxDJd"
    "fNnKUqpA6IVO7xRuEgUSGSFDIkAM49EAHBBdJTW8OFPRwiKnUh5UwllaV33j9gMZHnhqjw"
    "Ia5RLOUC1p58VXDDgWvOu4rruSNhqhvxVcN11fwDExYeiIdYGmJYiOgUIHECaRNWmjDKhB"
    "EmmBeawgPBeJS/YPLJrkEZT25nTwTkGwTjG/TLtldyAYSjZnUuztdc+EaEhWt2rplLkFQJ"
    "es5lUVDjiyTe4S/USFBGZI61mZuOw/hFVNM/EhVR2wJpiZP8kcQ4CkBDBOkVSq4wajXJTX"
    "Cc+h6cHgapL0eVzuHyy5GyKIhw1DTAqC+n1XwGZA5FRAQPOaKurD5Lc1R3VdeVlfQlZLi"
    "+10aCMiJzICJCeCh6gkyFIYjIj5SvGMyDWIWTxrVY4LD5uo2OTgxgANkZN3uCGdEcEE+U"
    "T1GTPBZVEMkjbe4m4xB+EbXlHGtsBVANjGiJYzstgpndGMAAyA6SK4xajR4ukdRbIFM4Y"
    "LDVMgXnwEMsunCSHi5JHhUiSRMthWAshUQeIJjSfNJvVQlmUGRDb9IXU/LDJXYRItIGqit"
    "gWSGqCiROIG3CShNGmTDC9B96ITY4XCLJpzQCCGeSa2CMa0g6MDncQDBG2WNnXbpFxOwIW"
    "EyDJPUmvLqu8jRjJwsgOClYX1i5lbpz+hMYYj7sQsSG0EWJaPBGbiJG5Z+H4eTTE3mWAm"
    "wydULEM9IXDAJ6ti8waIzGtpvwIztTbLwLv4cVRPJQZERwkfS1NRkGwHjSV1a8lWXAnInR"
    "1UzqqkpgoNlghgZgob7txk+DbFT+4GhiTAsrYXJDNyEgkU+9pXPQusFEXqLUVrmKuZ2sS"
    "zqrxDNMdIIoLtLXlqHMp96yMiYFqSsrxdeHGDIZsm5PpK6r+O/xsMGMCFBT+gZoJr8Mkl"
    "/GyC9HTj6naC5Haq59hkZmRAyaEU3DOejnUbSrlvD3RNJH9ezhEsaMoOwWT12ziQ+XWEa"
    "ISBuotLCVhSksRPMDiS1Ia4FSi1FaC6ENz7rsd2324i47a4f18HiHIdzicRfo0bzt7xeeO"
    "uza896tF/t3EO47v9zs5l27a+efisXrjx/eL05efXx5+urt4vT45PTh4snpyzfH7t38Z7"
    "FYbi+vLvpdv1htL7q+W/zYXoc/+7c4HH0btpuj81/ZH4zhaytlFUB8WbQkfeM5WPiur1f"
    "LVcctF11XLptQne1qRUtXtdJ67tuQtqbrVsVq5ZdO+KyjcM/b/npYbzcPH7RIqpyqnF3+C"
    "PQtv+Xs/v43CpkthD9PAAA="
)

FIXED_REFERENCE_ENVELOPE = {
    "schema": "hodge-y4-historical-q3-reference-v1",
    "label": "historical SU(3) 189-kernel q3 reference",
    "canonical_variable": "u=beta_H/6=1/g_H^4",
    "value_u4": "-20721577909065127111/7250590288602460800",
    "authority_sha256": Y4.V24C_AUTHORITY_SHA256,
    "authority_locator": "v24c line 7311; canonical v1.4 master lines 443-458",
    "sealed_for_terminal_only": True,
}


def write_archived_kernel(root: Path) -> Path:
    path = root / "Y4_STAGE3J" / "DATA_Y4_full_real_space_h4_kernel.json.gz"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(base64.b64decode(ARCHIVED_KERNEL_B64))
    return path


def read_archived_stage_i_words() -> bytes:
    encoded = b"".join(ARCHIVED_STAGE_I_FIXTURE.read_bytes().split())
    return lzma.decompress(base64.b85decode(encoded))


def load_notebook_pass_validator():
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    code_sources = [
        "".join(cell["source"])
        for cell in notebook["cells"]
        if cell["cell_type"] == "code"
    ]
    terminal_source = code_sources[-1]
    tree = ast.parse(terminal_source)
    function = next(
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
        and node.name == "verify_existing_terminal_pass"
    )
    namespace = {
        "Fraction": Fraction,
        "Path": Path,
        "gzip": gzip,
        "hashlib": hashlib,
        "json": json,
        "math": __import__("math"),
    }
    exec(compile(ast.Module(body=[function], type_ignores=[]), "<notebook-validator>", "exec"), namespace)
    return namespace["verify_existing_terminal_pass"]


def load_notebook_hash_bound_runner(*, os_module, fcntl_module):
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    first_source = next(
        "".join(cell["source"])
        for cell in notebook["cells"]
        if cell["cell_type"] == "code"
    )
    tree = ast.parse(first_source)
    function = next(
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == "run_hash_bound"
    )
    namespace = {
        "errno": errno,
        "fcntl": fcntl_module,
        "hashlib": hashlib,
        "os": os_module,
        "Path": Path,
        "subprocess": subprocess,
        "sys": sys,
    }
    exec(
        compile(ast.Module(body=[function], type_ignores=[]), "<notebook-runner>", "exec"),
        namespace,
    )
    return namespace["run_hash_bound"]


class FakeSealedOS:
    name = "posix"
    MFD_ALLOW_SEALING = 2
    MFD_CLOEXEC = 1

    def __init__(self) -> None:
        self.environ = {"PYTHONHASHSEED": "test"}
        self.buffers: dict[int, bytearray] = {}
        self.positions: dict[int, int] = {}
        self.closed: set[int] = set()
        self.sealed: set[int] = set()
        self._next_fd = 90

    def memfd_create(self, _name, flags=0):
        if flags != self.MFD_ALLOW_SEALING | self.MFD_CLOEXEC:
            raise AssertionError("memfd sealing flags are incomplete")
        self._next_fd += 1
        fd = self._next_fd
        self.buffers[fd] = bytearray()
        self.positions[fd] = 0
        return fd

    def write(self, fd, data):
        if fd in self.sealed:
            raise OSError(errno.EPERM, "sealed")
        payload = bytes(data)
        position = self.positions[fd]
        end = position + len(payload)
        if end > len(self.buffers[fd]):
            self.buffers[fd].extend(b"\0" * (end - len(self.buffers[fd])))
        self.buffers[fd][position:end] = payload
        self.positions[fd] = end
        return len(payload)

    def fsync(self, _fd):
        return None

    def pread(self, fd, length, offset):
        return bytes(self.buffers[fd][offset : offset + length])

    def pwrite(self, fd, data, offset):
        if fd in self.sealed:
            raise OSError(errno.EPERM, "sealed")
        old = self.positions[fd]
        self.positions[fd] = offset
        try:
            return self.write(fd, data)
        finally:
            self.positions[fd] = old

    def close(self, fd):
        self.closed.add(fd)


class FakeFcntl:
    F_ADD_SEALS = 1033
    F_GET_SEALS = 1034
    F_SEAL_SEAL = 1
    F_SEAL_SHRINK = 2
    F_SEAL_GROW = 4
    F_SEAL_WRITE = 8

    def __init__(self, fake_os: FakeSealedOS) -> None:
        self.os = fake_os
        self.seals: dict[int, int] = {}

    def fcntl(self, fd, operation, value=None):
        if operation == self.F_ADD_SEALS:
            self.seals[fd] = int(value)
            self.os.sealed.add(fd)
            return 0
        if operation == self.F_GET_SEALS:
            return self.seals.get(fd, 0)
        raise AssertionError(f"unexpected fcntl operation: {operation}")


class CanonicalProductionCheapTests(unittest.TestCase):
    def test_embedded_authorities_are_exact_and_worker_is_clean(self) -> None:
        authority = Y4._verify_embedded_authority()
        self.assertTrue(authority["passed"])
        self.assertEqual(
            authority["stage3i_authority_sha256"],
            "7662066c5516533ba531c414fc057c0f5c6e0d8bd1fe860a9c083fa8b2907abf",
        )
        workers = {
            "stage0": Y4.STAGE0_SOURCE,
            "stage12": Y4.STAGE12_SOURCE,
            **Y4._extract_inner_sources(),
            **Y4._extract_stage12_sources(),
            **Y4._extract_stage3bc_sources(),
        }
        for name, source in workers.items():
            lowered = source.lower()
            compact = "".join(lowered.split())
            for marker in Y4._FORBIDDEN_WORKER_MARKERS:
                self.assertNotIn("".join(marker.lower().split()), compact, (name, marker))
            self.assertNotIn("20721577909065127111", source, name)
        self.assertIn("--stage3h-topologies", SCRIPT.read_text(encoding="utf-8"))
        self.assertNotIn(
            "20721577909065127111", SCRIPT.read_text(encoding="utf-8")
        )

    def test_notebook_is_hash_bound_cpu_only_and_two_phase(self) -> None:
        notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
        code_cells = [
            "".join(cell["source"])
            for cell in notebook["cells"]
            if cell["cell_type"] == "code"
        ]
        self.assertEqual(len(code_cells), 2)
        for index, source in enumerate(code_cells, start=1):
            compile(source, f"<notebook-cell-{index}>", "exec")
        script_sha = hashlib.sha256(SCRIPT.read_bytes()).hexdigest()
        self.assertIn(f"EXPECTED_SCRIPT_SHA256 = '{script_sha}'", code_cells[0])
        self.assertNotIn("20721577909065127111", code_cells[0])
        self.assertIn("20721577909065127111", code_cells[1])
        self.assertIn(Y4.HISTORICAL_REFERENCE_ENVELOPE_SHA256, code_cells[1])
        metadata_text = json.dumps(notebook.get("metadata", {})).lower()
        self.assertNotIn("gpu", metadata_text)
        self.assertNotIn("accelerator", metadata_text)

    def test_notebook_runner_kernel_seals_fd_against_transient_overwrite(self) -> None:
        fake_os = FakeSealedOS()
        fake_fcntl = FakeFcntl(fake_os)
        runner = load_notebook_hash_bound_runner(
            os_module=fake_os, fcntl_module=fake_fcntl
        )
        with tempfile.TemporaryDirectory() as td:
            snapshot = Path(td) / "runner.verified.py"
            original = b"print('sealed')\n"
            expected = hashlib.sha256(original).hexdigest()
            snapshot.write_bytes(b"poison")
            with mock.patch("subprocess.run") as subprocess_run:
                with self.assertRaisesRegex(RuntimeError, "changed before subprocess"):
                    runner(snapshot, original, expected, ["--self-test"])
                subprocess_run.assert_not_called()
            snapshot.write_bytes(original)

            executed: list[bytes] = []

            def transient_swap(command, *, check, pass_fds, env):
                self.assertTrue(check)
                self.assertEqual(len(pass_fds), 1)
                sealed_fd = pass_fds[0]
                self.assertEqual(command[2], f"/proc/self/fd/{sealed_fd}")
                self.assertEqual(env["HODGE_Y4_SEALED_SOURCE_FD"], str(sealed_fd))
                snapshot.write_bytes(b"transient-poison")
                snapshot.write_bytes(original)
                with self.assertRaises(OSError) as blocked:
                    fake_os.pwrite(sealed_fd, b"fd-poison", 0)
                self.assertEqual(blocked.exception.errno, errno.EPERM)
                executed.append(fake_os.pread(sealed_fd, len(original) + 64, 0))

            with mock.patch.object(Path, "is_dir", return_value=True):
                with mock.patch("subprocess.run", side_effect=transient_swap):
                    runner(snapshot, original, expected, ["--self-test"])
            self.assertEqual(executed, [original])

            def persistent_mutation(_command, *, check, pass_fds, env):
                self.assertTrue(check)
                self.assertEqual(len(pass_fds), 1)
                self.assertEqual(
                    env["HODGE_Y4_SEALED_SOURCE_FD"], str(pass_fds[0])
                )
                snapshot.write_bytes(b"mutated-during-exec")

            with mock.patch.object(Path, "is_dir", return_value=True):
                with mock.patch("subprocess.run", side_effect=persistent_mutation):
                    with self.assertRaisesRegex(RuntimeError, "changed during subprocess"):
                        runner(snapshot, original, expected, ["--self-test"])

    def test_every_worker_uses_shared_kernel_sealed_memfd_launcher(self) -> None:
        fake_os = FakeSealedOS()
        fake_fcntl = FakeFcntl(fake_os)
        source = "print('sealed worker')\n"
        executed: list[bytes] = []

        def attack_worker(command, *, check, cwd, env, pass_fds):
            self.assertTrue(check)
            self.assertTrue(Path(cwd).is_dir())
            self.assertEqual(len(pass_fds), 1)
            fd = pass_fds[0]
            self.assertEqual(command[2], f"/proc/self/fd/{fd}")
            self.assertEqual(env["HODGE_Y4_SEALED_WORKER_FD"], str(fd))
            self.assertEqual(
                env["HODGE_Y4_SEALED_WORKER_SHA256"],
                hashlib.sha256(source.encode()).hexdigest(),
            )
            with self.assertRaises(OSError) as blocked:
                fake_os.pwrite(fd, b"worker-poison", 0)
            self.assertEqual(blocked.exception.errno, errno.EPERM)
            executed.append(fake_os.pread(fd, len(source) + 64, 0))

        with tempfile.TemporaryDirectory() as td:
            with mock.patch.object(Y4, "os", fake_os), mock.patch.object(
                Path, "is_dir", return_value=True
            ), mock.patch.dict(sys.modules, {"fcntl": fake_fcntl}), mock.patch.object(
                Y4.subprocess, "run", side_effect=attack_worker
            ):
                Y4.run_source(source, "synthetic_worker.py", [], cwd=Path(td))

        self.assertEqual(executed, [source.encode()])
        self.assertTrue(fake_os.closed)
        launcher_source = inspect.getsource(Y4.run_source)
        self.assertIn("_sealed_memfd_from_bytes", launcher_source)
        self.assertNotIn("TemporaryDirectory", launcher_source)
        backend_source = inspect.getsource(Y4._authoritative_main)
        for worker_name in (
            "y4_stage0_geometry_manifest.py",
            "y4_stage1_channel_denominator_manifest.py",
            "y4_stage2_exact_haar_library.py",
            "y4_stage3b_time_ordered_state_graph.py",
            "y4_stage3c_exact_casimir_projectors.py",
            "y4_stage3e_trace_wiring_compiler.py",
            "y4_stage3g_checkpointed.py",
            "y4_stage3i_complete_folded_descloizeaux.py",
            "y4_stage3j_final_flatband_verdict.py",
        ):
            self.assertIn(worker_name, backend_source)
        self.assertNotIn("'y4_stage1_stage2_autobundle.py'", backend_source)
        self.assertNotIn("'y4_stage3b_stage3c_autobundle.py'", backend_source)

        actual_workers = {
            "y4_stage0_geometry_manifest.py": Y4.STAGE0_SOURCE,
            "y4_stage1_channel_denominator_manifest.py": (
                Y4._extract_stage12_sources()["stage1"]
            ),
            "y4_stage2_exact_haar_library.py": (
                Y4._extract_stage12_sources()["stage2"]
            ),
            "y4_stage3b_time_ordered_state_graph.py": (
                Y4._extract_stage3bc_sources()["stage3b"]
            ),
            "y4_stage3c_exact_casimir_projectors.py": (
                Y4._extract_stage3bc_sources()["stage3c"]
            ),
        }
        inner = Y4._extract_inner_sources()
        for name in (
            "y4_stage3e_trace_wiring_compiler.py",
            "y4_stage3g_checkpointed.py",
            "y4_stage3i_complete_folded_descloizeaux.py",
            "y4_stage3j_final_flatband_verdict.py",
        ):
            actual_workers[name] = inner[name]
        for name, worker_source in actual_workers.items():
            worker_tree = ast.parse(worker_source, filename=f"<{name}>")
            for node in ast.walk(worker_tree):
                if not isinstance(node, ast.Call):
                    continue
                function = node.func
                qualified = ""
                if isinstance(function, ast.Name):
                    qualified = function.id
                elif (
                    isinstance(function, ast.Attribute)
                    and isinstance(function.value, ast.Name)
                ):
                    qualified = f"{function.value.id}.{function.attr}"
                self.assertNotIn(
                    qualified,
                    {
                        "subprocess.run",
                        "subprocess.call",
                        "subprocess.Popen",
                        "os.system",
                        "eval",
                    },
                    f"nested executable launch in {name}:{node.lineno}",
                )

    @unittest.skipUnless(
        os.name == "posix" and hasattr(os, "memfd_create"),
        "exact Linux memfd sealing integration",
    )
    def test_linux_memfd_blocks_real_fd_overwrite_for_runner_and_worker(self) -> None:
        import fcntl

        required_seals = (
            fcntl.F_SEAL_WRITE
            | fcntl.F_SEAL_SHRINK
            | fcntl.F_SEAL_GROW
            | fcntl.F_SEAL_SEAL
        )
        real_run = subprocess.run
        attacks: list[str] = []

        def attack_then_run(label):
            def attack(command, **kwargs):
                fd = kwargs["pass_fds"][0]
                self.assertEqual(fcntl.fcntl(fd, fcntl.F_GET_SEALS), required_seals)
                for mutation in (
                    lambda: os.pwrite(fd, b"poison", 0),
                    lambda: os.ftruncate(fd, 0),
                    lambda: os.ftruncate(fd, 1 << 20),
                ):
                    with self.assertRaises(OSError) as blocked:
                        mutation()
                    self.assertEqual(blocked.exception.errno, errno.EPERM)
                attacks.append(label)
                return real_run(command, **kwargs)

            return attack

        runner = load_notebook_hash_bound_runner(
            os_module=os, fcntl_module=fcntl
        )
        script_bytes = SCRIPT.read_bytes()
        script_sha = hashlib.sha256(script_bytes).hexdigest()
        with tempfile.TemporaryDirectory() as td:
            snapshot = Path(td) / "sealed-runner.py"
            snapshot.write_bytes(script_bytes)
            with mock.patch(
                "subprocess.run", side_effect=attack_then_run("runner")
            ):
                runner(snapshot, script_bytes, script_sha, ["--self-test"])

            worker_source = (
                "from pathlib import Path\n"
                "Path('sealed_worker_marker.txt').write_text('ok', encoding='utf-8')\n"
            )
            with mock.patch.object(
                Y4.subprocess,
                "run",
                side_effect=attack_then_run("worker"),
            ):
                Y4.run_source(
                    worker_source,
                    "synthetic_worker.py",
                    [],
                    cwd=Path(td),
                )
            self.assertEqual(
                (Path(td) / "sealed_worker_marker.txt").read_text(encoding="utf-8"),
                "ok",
            )
        self.assertEqual(attacks, ["runner", "worker"])

    def test_normalization_is_exactly_u_with_no_rescaling(self) -> None:
        cert = Y4._normalization_certificate()
        self.assertTrue(cert["passed"])
        self.assertEqual(cert["audit_sha256"], Y4.NORMALIZATION_AUDIT_SHA256)
        self.assertEqual(cert["character_coefficient_per_beta"], "-1/6")
        self.assertEqual(cert["worker_character_coefficient_per_beta"], "-1/6")
        self.assertTrue(cert["y_code_equals_u"])
        self.assertEqual(cert["rescaling"], "none")

    def test_schedule_is_exact_and_invalid_action_never_calls_backend(self) -> None:
        token = Y4._build_schedule_token()
        observed = tuple(
            (
                row[1], row[2], row[3], row[4], row[5], row[6]
            )
            for row in token.manifest
        )
        self.assertEqual(observed, Y4.HalfHistorySchedule.REQUIRED)
        self.assertEqual(sum(row[1] == "W" for row in token.manifest), 2)
        poison: list[str] = []
        schedule = Y4.HalfHistorySchedule()
        schedule.transition("W", "P0", "W1", "P", "Q1", 0, lambda: None)
        schedule.transition("R", "W1", "R1", "Q1", "Q1", 1, lambda: None)
        schedule.transition("W", "R1", "W2", "Q1", "Q2", 1, lambda: None)
        with self.assertRaises(Y4.ScheduleViolation):
            schedule.transition(
                "W", "W2", "W3", "Q2", "Q2", 2,
                lambda: poison.append("backend-called"),
            )
        self.assertEqual(poison, [])

        reentrant = Y4.HalfHistorySchedule()
        reached: list[str] = []

        def first_backend() -> None:
            reached.append("first")
            reentrant.transition(
                "W", "P0", "W1", "P", "Q1", 0,
                lambda: reached.append("nested"),
            )

        with self.assertRaises(Y4.ScheduleViolation):
            reentrant.transition("W", "P0", "W1", "P", "Q1", 0, first_backend)
        self.assertEqual(reached, ["first"])
        for bad_depth in (0.9, "0", False):
            typed = Y4.HalfHistorySchedule()
            typed_poison: list[str] = []
            with self.assertRaises(Y4.ScheduleViolation):
                typed.transition(
                    "W", "P0", "W1", "P", "Q1", bad_depth,
                    lambda: typed_poison.append("called"),
                )
            self.assertEqual(typed_poison, [])

    def test_forged_schedule_is_rejected_before_worker_or_root_creation(self) -> None:
        token = Y4._build_schedule_token()
        forged_manifest = list(token.manifest)
        last = list(forged_manifest[-1])
        last[3] = "W3"
        forged_manifest[-1] = tuple(last)
        forged = Y4._ScheduleToken(
            tuple(forged_manifest), token.manifest_sha256, Y4._SCHEDULE_SENTINEL
        )
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "must-not-be-created"
            with mock.patch.object(
                Y4, "run_source", side_effect=AssertionError("worker called")
            ):
                with self.assertRaises(Y4.ScheduleViolation):
                    Y4._authoritative_main(root, forged)
            self.assertFalse(root.exists())

    def test_output_derived_four_insertion_certificate_rejects_schedule_poisons(self) -> None:
        geometry = {
            "ordered_id": "W4-00001",
            "ordered_insertions": [[0, 0, 0, 0, 1]] * 4,
            "output": [0, 0, 0, 0, 1],
        }
        stage0_word = {
            **geometry,
            "root": [0, 0, 0, 0, 1],
            "triality_sign_assignment_count": 2,
            "triality_sign_assignments": [[1] * 6, [-1] * 6],
        }
        denominator = {
            "E6": [4, 4, 4],
            "denominator_numerators": [12, 12, 12],
            "channel_path_multiplicity": 1,
            "resonant_mask": 0,
            "vacuum_mask": 0,
            "raw_resolvent_product": "1/8",
            "requires_folded_terms": False,
        }
        orbit = {
            "orbit_id": "O-1",
            "sign_representative": [1] * 6,
            "charge_conjugate": [-1] * 6,
            "charge_conjugation_multiplicity": 2,
            "c_even_phase": 1,
            "c_odd_phase": 1,
            "resonance_class": "nonresonant_only",
            "exact_singlet_feasible": True,
            "touched_links": 1,
            "max_link_degree": 6,
            "max_local_invariant_dim": 6,
            "global_channel_path_multiplicity": 1,
            "local_moment_types": [
                {
                    "n_fund_canonical": 3,
                    "n_antifund_canonical": 3,
                    "singlet_multiplicity": 6,
                    "link_count": 1,
                }
            ],
            "link_token_signatures": [[1, -1, 1, -1, 1, -1]],
            "energy_signature_count": 1,
            "resonant_energy_signatures": 0,
            "nonresonant_energy_signatures": 1,
            "vacuum_energy_signatures": 0,
            "denominator_signatures": [denominator],
        }
        stage1_word = {
            **geometry,
            "root": [0, 0, 0, 0, 1],
            "has_link_sharing_contact": True,
            "has_site_only_corner_contact": False,
            "triality_sign_orbits": 1,
            "exact_singlet_orbits": 1,
            "rejected_sign_orbits": 0,
            "word_max_link_degree": 6,
            "word_max_local_invariant_dim": 6,
            "word_max_energy_signature_count": 1,
            "word_orbits_with_resonance": 0,
            "word_nonresonant_only_orbits": 1,
            "complexity_score": 66001,
            "orientation_orbits": [orbit],
        }
        stage_i_word = {
            **geometry,
            "canonical_complete_sum_even": "0",
            "canonical_complete_sum_odd": "0",
            "canonical_direct_sum_even": "0",
            "canonical_direct_sum_odd": "0",
            "canonical_folded_sum_even": "0",
            "canonical_folded_sum_odd": "0",
            "orientation_orbit_count": 1,
            "output_displacement_plane": [0, 0, 0, 0, 1],
            "rooted_complete_weight_even": "0",
            "rooted_complete_weight_odd": "0",
            "rooted_cubic_multiplicity_even": 1,
            "rooted_cubic_signed_multiplicity_odd": 1,
            "topology_count": 1,
        }
        stage0 = {"words": [stage0_word]}
        stage1 = {"words": [stage1_word]}
        stage_i = {"words": [stage_i_word]}

        def validate(a=stage0, b=stage1, c=stage_i):
            return Y4._validate_four_insertion_chain(
                a,
                b,
                c,
                expected_word_count=1,
                expected_moment_occurrences={(3, 3, 6): 1},
                expected_corpus_totals=(2, 1, 1, 0, 1, 1),
            )

        certificate = validate()
        self.assertTrue(certificate["passed"])
        self.assertEqual(certificate["insertion_count_per_word"], 4)
        self.assertEqual(
            Y4.EXPECTED_H4_OPERATOR_IDENTITY,
            "H4=PVRVRVRVP-a(PVR2VRVP+PVRVR2VP)+a2PVR3VP"
            "-1/2{PVRVP,PVR2VP}",
        )

        for mutate, pattern in (
            (
                lambda a, b, c: [
                    payload["words"][0]["ordered_insertions"].append(
                        [1, 0, 0, 0, 1]
                    )
                    for payload in (a, b, c)
                ],
                "non-four-insertion",
            ),
            (
                lambda a, b, c: b["words"][0]["orientation_orbits"][0][
                    "link_token_signatures"
                ][0].append(1),
                r"ket \+ four insertions \+ bra",
            ),
            (
                lambda a, b, c: (
                    b["words"][0]["orientation_orbits"][0][
                        "denominator_signatures"
                    ][0]["E6"].append(4),
                    b["words"][0]["orientation_orbits"][0][
                        "denominator_signatures"
                    ][0]["denominator_numerators"].append(12),
                ),
                "three intermediate denominators",
            ),
            (
                lambda a, b, c: b["words"][0]["orientation_orbits"][0][
                    "local_moment_types"
                ][0].update(
                    {"n_fund_canonical": 2, "n_antifund_canonical": 5}
                ),
                "forbidden local occurrence",
            ),
        ):
            a, b, c = copy.deepcopy((stage0, stage1, stage_i))
            mutate(a, b, c)
            with self.assertRaisesRegex(Y4.ProductionFailure, pattern):
                validate(a, b, c)

    def test_archived_kernel_hash_hermiticity_and_exact_gamma(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            kernel = write_archived_kernel(Path(td))
            self.assertEqual(
                hashlib.sha256(kernel.read_bytes()).hexdigest(),
                Y4.EXPECTED_CORE_ARTIFACT_SHA256[
                    "Y4_STAGE3J/DATA_Y4_full_real_space_h4_kernel.json.gz"
                ],
            )
            records = Y4._load_kernel_records(kernel)
            Y4._verify_kernel_hermiticity(records)
            matrix, q3 = Y4._gamma_scalar_from_records(records)
            expected = -Fraction(
                int("".join(("20721577909", "065127111"))),
                int("".join(("72505902886", "02460800"))),
            )
            self.assertEqual(q3, expected)
            self.assertEqual(
                matrix,
                [[expected, Fraction(0), Fraction(0)],
                 [Fraction(0), expected, Fraction(0)],
                 [Fraction(0), Fraction(0), expected]],
            )

    def test_kernel_physical_identity_is_invariant_under_runtime_path(self) -> None:
        archived_raw = base64.b64decode(ARCHIVED_KERNEL_B64)
        archived_payload = Y4._load_kernel_payload_bytes(archived_raw)
        archived_identity, _ = Y4._kernel_physical_identity(archived_payload)
        changed = copy.deepcopy(archived_payload)
        changed["meta"]["stage3i_input"] = (
            "/content/Y4_CANONICAL_PRODUCTION/Y4_STAGE3I/"
            "y4_complete_folded_word_weights.json.gz"
        )
        changed_raw = gzip.compress(
            json.dumps(changed, sort_keys=True, separators=(",", ":")).encode("utf-8"),
            compresslevel=9,
            mtime=0,
        )
        changed_payload = Y4._load_kernel_payload_bytes(changed_raw)
        changed_identity, _ = Y4._kernel_physical_identity(changed_payload)
        self.assertNotEqual(hashlib.sha256(archived_raw).digest(), hashlib.sha256(changed_raw).digest())
        self.assertEqual(archived_identity, changed_identity)
        self.assertEqual(archived_identity, Y4.EXPECTED_PHYSICAL_IDENTITY_SHA256["kernel"])

    def test_stage_i_and_kernel_physical_binding_is_portable_across_two_roots(self) -> None:
        words = [
            {"ordered_id": f"W4-{index:05d}", "synthetic_exact_weight": "0"}
            for index in range(1, Y4.EXPECTED_COUNTS["ordered_words"] + 1)
        ]

        def stage_payload(orbit_sha: str) -> dict[str, object]:
            return {
                "meta": {
                    "version": "2026-06-13-stage3i-v1",
                    "orbit_file": "y4_complete_folded_orbit_amplitudes.json.gz",
                    "orbit_sha256": orbit_sha,
                    "rooted_multiplicity": (
                        "orbit size under the 8-element proper cubic stabilizer of "
                        "the rooted input plaquette"
                    ),
                },
                "words": copy.deepcopy(words),
            }

        def gzip_payload(payload: object) -> bytes:
            return gzip.compress(
                Y4._canonical_json_bytes(payload), compresslevel=9, mtime=0
            )

        archived_kernel = Y4._load_kernel_payload_bytes(
            base64.b64decode(ARCHIVED_KERNEL_B64)
        )
        stage_a = stage_payload("1" * 64)
        stage_b = stage_payload("2" * 64)
        stage_a_raw = gzip_payload(stage_a)
        stage_b_raw = gzip_payload(stage_b)
        self.assertNotEqual(Y4._sha256_bytes(stage_a_raw), Y4._sha256_bytes(stage_b_raw))
        stage_physical, _ = Y4._stage_i_word_physical_identity(stage_a)
        self.assertEqual(
            stage_physical, Y4._stage_i_word_physical_identity(stage_b)[0]
        )

        def kernel_for(root: str, stage_raw: bytes) -> bytes:
            payload = copy.deepcopy(archived_kernel)
            payload["meta"]["stage3i_input"] = (
                f"{root}/Y4_STAGE3I/y4_complete_folded_word_weights.json.gz"
            )
            payload["meta"]["stage3i_sha256"] = Y4._sha256_bytes(stage_raw)
            return gzip_payload(payload)

        kernel_a_raw = kernel_for("/mnt/data/archive-run", stage_a_raw)
        kernel_b_raw = kernel_for("/content/fresh-colab-run", stage_b_raw)
        self.assertNotEqual(Y4._sha256_bytes(kernel_a_raw), Y4._sha256_bytes(kernel_b_raw))
        kernel_a_payload = Y4._load_kernel_payload_bytes(
            kernel_a_raw,
            expected_stage_i_raw_sha256=Y4._sha256_bytes(stage_a_raw),
        )
        kernel_physical, _ = Y4._kernel_physical_identity(
            kernel_a_payload, stage_physical
        )

        result_a = Y4._validate_stage_i_kernel_binding_bytes(
            stage_a_raw,
            kernel_a_raw,
            expected_stage_i_physical_sha256=stage_physical,
            expected_kernel_physical_sha256=kernel_physical,
        )
        result_b = Y4._validate_stage_i_kernel_binding_bytes(
            stage_b_raw,
            kernel_b_raw,
            expected_stage_i_physical_sha256=stage_physical,
            expected_kernel_physical_sha256=kernel_physical,
        )
        self.assertEqual(result_a[3:], result_b[3:])
        self.assertEqual(Y4.PORTABLE_RAW_HASH_GATES, ())

        mutated = copy.deepcopy(stage_b)
        mutated["words"][0]["synthetic_exact_weight"] = "1"
        mutated_raw = gzip_payload(mutated)
        mutated_kernel_raw = kernel_for("/content/fresh-colab-run", mutated_raw)
        with self.assertRaisesRegex(Y4.ProductionFailure, "physical identity mismatch"):
            Y4._validate_stage_i_kernel_binding_bytes(
                mutated_raw,
                mutated_kernel_raw,
                expected_stage_i_physical_sha256=stage_physical,
                expected_kernel_physical_sha256=kernel_physical,
            )

    def test_gamma_non_scalar_mutation_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            records = Y4._load_kernel_records(write_archived_kernel(Path(td)))
            mutated = copy.deepcopy(records)
            mutated[0]["weight"] = str(Fraction(mutated[0]["weight"]) + 1)
            with self.assertRaises(Y4.ProductionFailure):
                Y4._gamma_scalar_from_records(mutated)

    def test_intrinsic_gamma_is_frozen_before_terminal_reference_load(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "run"
            root.mkdir()
            kernel = write_archived_kernel(root)
            records = Y4._load_kernel_records(kernel)
            kernel_sha = Y4.sha256_file(kernel)
            snapshot = root / "Y4_KERNEL_SEALED_SNAPSHOT.json.gz"
            snapshot.write_bytes(kernel.read_bytes())
            payload = Y4._load_kernel_payload_bytes(snapshot.read_bytes())
            physical_sha, _identity = Y4._kernel_physical_identity(payload)
            preunblind = {
                "status": "PREUNBLIND_CANONICAL_PASS",
                "preunblind": {"historical_reference_loaded": False},
                "construction": {
                    "artifact_sha256": {
                        "Y4_STAGE3J/DATA_Y4_full_real_space_h4_kernel.json.gz": kernel_sha
                    },
                    "kernel": {
                        "records": records,
                        "sealed_snapshot": snapshot.name,
                        "sealed_snapshot_raw_sha256": kernel_sha,
                        "portable_physical_identity_sha256": physical_sha,
                    },
                },
            }
            pre_path = root / "Y4_CANONICAL_CERTIFICATE_PREUNBLIND.json"
            pre_sha = Y4._atomic_write_json(pre_path, preunblind)
            intrinsic_path, intrinsic_sha, computed = Y4._derive_gamma_from_sealed_kernel(
                root, pre_path, pre_sha
            )
            intrinsic = Y4.read_json(intrinsic_path)
            self.assertFalse(intrinsic["historical_reference_loaded"])
            self.assertTrue(intrinsic["diagonal_scalar"])
            reference_path = Path(td) / "terminal-reference.json"
            reference_raw = Y4._canonical_json_bytes(FIXED_REFERENCE_ENVELOPE)
            self.assertEqual(
                hashlib.sha256(reference_raw).hexdigest(),
                Y4.HISTORICAL_REFERENCE_ENVELOPE_SHA256,
            )
            reference_path.write_bytes(reference_raw)
            adaptive = dict(FIXED_REFERENCE_ENVELOPE)
            adaptive["value_u4"] = "0"
            adaptive_path = Path(td) / "adaptive-reference.json"
            adaptive_path.write_bytes(Y4._canonical_json_bytes(adaptive))
            with self.assertRaises(Y4.ProductionFailure):
                Y4._load_historical_q3_after_seal(
                    intrinsic_path, intrinsic_sha, adaptive_path
                )
            reference = Y4._load_historical_q3_after_seal(
                intrinsic_path, intrinsic_sha, reference_path
            )
            self.assertTrue(reference["loaded_after_kernel_and_gamma_seals"])
            self.assertEqual(computed, reference["fraction"])
            final_path, _final_sha, comparison = Y4._terminal_unblind(
                root,
                pre_path,
                pre_sha,
                intrinsic_path,
                intrinsic_sha,
                reference_path,
            )
            self.assertTrue(final_path.is_file())
            self.assertTrue(comparison["exact_equal"])

    def test_writer_generated_preunblind_roundtrips_through_terminal_and_notebook(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            parent = Path(td)
            requested_root = parent / "run"
            script_sha = Y4.sha256_file(SCRIPT)
            authority = Y4._verify_embedded_authority()
            normalization = Y4._normalization_certificate()
            token = Y4._build_schedule_token()
            binding = Y4._binding_payload(
                script_sha, token, authority, normalization
            )
            root = Y4._prepare_run_root(requested_root, False, binding)

            stage_i_raw = read_archived_stage_i_words()
            stage_i_path = (
                root / "Y4_STAGE3I" / "y4_complete_folded_word_weights.json.gz"
            )
            stage_i_path.parent.mkdir(parents=True)
            stage_i_path.write_bytes(stage_i_raw)
            stage_i_sha = Y4._sha256_bytes(stage_i_raw)
            self.assertEqual(
                stage_i_sha,
                "854a02e981098de7fcfd1a14dd5c9703aff0c36a2a81ea5589ddf4ff8c321bd0",
            )
            stage_i_payload = Y4._load_stage_i_word_payload_bytes(stage_i_raw)
            stage_i_physical, _stage_i_identity = (
                Y4._stage_i_word_physical_identity(stage_i_payload)
            )

            kernel_raw = base64.b64decode(ARCHIVED_KERNEL_B64)
            kernel_path = write_archived_kernel(root)
            kernel_payload = Y4._load_kernel_payload_bytes(
                kernel_raw, expected_stage_i_raw_sha256=stage_i_sha
            )
            kernel_physical, _kernel_identity = Y4._kernel_physical_identity(
                kernel_payload, stage_i_physical
            )
            self.assertEqual(
                kernel_physical, Y4.EXPECTED_PHYSICAL_IDENTITY_SHA256["kernel"]
            )
            snapshot = root / "Y4_KERNEL_SEALED_SNAPSHOT.json.gz"
            snapshot.write_bytes(kernel_raw)
            kernel_sha = Y4._sha256_bytes(kernel_raw)

            verdict = {
                "meta": {},
                "verdict": {},
                "high_symmetry_corrections": {},
                "gates": {
                    "J0_real_space_kernel": {
                        "stage3i_sha256": stage_i_sha,
                        "nonzero_full_kernel_entries": 189,
                        "passed": True,
                    },
                    "J1_cube_boundary": {"passed": True},
                    "J2_dispersion_witness": {"passed": True},
                    "J3_round_trip": {"passed": True},
                },
                "files": {},
                "scope": {},
                "passed": True,
            }
            Y4._atomic_write_json(
                root / "Y4_STAGE3J" / "CERT_Y4_stage3j_verdict.json", verdict
            )

            outputs = {
                "artifact_sha256": {
                    "Y4_STAGE3I/y4_complete_folded_word_weights.json.gz": stage_i_sha,
                },
                "physical_identity_sha256": {
                    "stage_i_word_weights": stage_i_physical,
                    "kernel": kernel_physical,
                },
                "four_insertion_order_certificate": {
                    "passed": True,
                    "insertion_count_per_word": 4,
                },
                "kernel": {
                    "records": kernel_payload["kernel"],
                    "source_run_raw_sha256": Y4.sha256_file(kernel_path),
                    "sealed_snapshot": snapshot.name,
                    "sealed_snapshot_raw_sha256": Y4.sha256_file(snapshot),
                    "portable_physical_identity_sha256": kernel_physical,
                },
            }
            with mock.patch.object(
                Y4,
                "_package_versions",
                return_value={"numpy": "test-fixture", "sympy": "test-fixture"},
            ):
                pre_path, pre_sha = Y4._freeze_preunblind_certificate(
                    root,
                    script_sha,
                    token,
                    authority,
                    normalization,
                    outputs,
                )
            written_pre = Y4.read_json(pre_path)
            self.assertEqual(
                written_pre["schema"], "hodge-y4-canonical-preunblind-v1"
            )
            self.assertEqual(written_pre["runner_version"], Y4.RUNNER_VERSION)
            intrinsic_path, intrinsic_sha, computed_q3 = (
                Y4._derive_gamma_from_sealed_kernel(root, pre_path, pre_sha)
            )
            Y4._write_status(
                root,
                "PREUNBLIND_PASS",
                script_sha,
                {
                    "preunblind_certificate": str(pre_path),
                    "preunblind_sha256": pre_sha,
                    "intrinsic_gamma_certificate": str(intrinsic_path),
                    "intrinsic_gamma_sha256": intrinsic_sha,
                    "kernel_physical_identity_sha256": kernel_physical,
                    "computed_q3_u4": str(computed_q3),
                    "historical_reference_loaded": False,
                    "walltime_s": 0.0,
                },
            )
            reference_path = parent / "terminal-reference.json"
            reference_path.write_bytes(
                Y4._canonical_json_bytes(FIXED_REFERENCE_ENVELOPE)
            )

            with mock.patch.object(
                Y4, "_validate_production_outputs", return_value=outputs
            ):
                Y4._verify_existing_sealed_run(root)
                Y4.terminal_unblind_main(root, reference_path)
                Y4._verify_existing_sealed_run(
                    root, require_terminal_pass=True
                )

            notebook_validator = load_notebook_pass_validator()
            final = notebook_validator(
                root,
                script_sha,
                Y4.HISTORICAL_REFERENCE_ENVELOPE_SHA256,
            )
            self.assertTrue(final["passed"])
            self.assertEqual(final["computed_q3_u4"], str(computed_q3))

            final_path = root / "Y4_CANONICAL_CERTIFICATE_FINAL.json"
            status_path = root / "Y4_CANONICAL_RUN_STATUS.json"
            final_path.chmod(0o644)
            original_final = Y4.read_json(final_path)
            original_status = Y4.read_json(status_path)
            for field, poison in (
                ("schema", "poison-schema"),
                ("sealed_for_terminal_only", False),
            ):
                tampered_final = copy.deepcopy(original_final)
                tampered_final["historical_reference"][field] = poison
                tampered_sha = Y4._atomic_write_json(final_path, tampered_final)
                tampered_status = copy.deepcopy(original_status)
                tampered_status["detail"]["final_sha256"] = tampered_sha
                Y4._atomic_write_json(status_path, tampered_status)
                with mock.patch.object(
                    Y4, "_validate_production_outputs", return_value=outputs
                ):
                    with self.assertRaisesRegex(
                        Y4.ProductionFailure, "historical reference fields"
                    ):
                        Y4._verify_existing_sealed_run(
                            root, require_terminal_pass=True
                        )
                with self.assertRaisesRegex(
                    RuntimeError, "historical reference commitment"
                ):
                    notebook_validator(
                        root,
                        script_sha,
                        Y4.HISTORICAL_REFERENCE_ENVELOPE_SHA256,
                    )
                Y4._atomic_write_json(final_path, original_final)
                Y4._atomic_write_json(status_path, original_status)

    def test_forged_pass_without_physical_artifacts_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            parent = Path(td)
            root = parent / "run"
            script_sha = Y4.sha256_file(SCRIPT)
            authority = Y4._verify_embedded_authority()
            normalization = Y4._normalization_certificate()
            token = Y4._build_schedule_token()
            binding = Y4._binding_payload(
                script_sha, token, authority, normalization
            )
            Y4._prepare_run_root(root, False, binding)
            kernel = write_archived_kernel(root)
            snapshot = root / "Y4_KERNEL_SEALED_SNAPSHOT.json.gz"
            snapshot.write_bytes(kernel.read_bytes())
            payload = Y4._load_kernel_payload_bytes(snapshot.read_bytes())
            physical_sha, _identity = Y4._kernel_physical_identity(payload)
            records = payload["kernel"]
            preunblind = {
                "status": "PREUNBLIND_CANONICAL_PASS",
                "runtime": {"script_sha256": script_sha},
                "preunblind": {"historical_reference_loaded": False},
                "construction": {
                    "physical_identity_sha256": {
                        "stage_i_word_weights": Y4.EXPECTED_PHYSICAL_IDENTITY_SHA256[
                            "stage_i_word_weights"
                        ],
                        "kernel": physical_sha,
                    },
                    "kernel": {
                        "records": records,
                        "sealed_snapshot": snapshot.name,
                        "sealed_snapshot_raw_sha256": Y4.sha256_file(snapshot),
                        "portable_physical_identity_sha256": physical_sha,
                    },
                },
            }
            pre_path = root / "Y4_CANONICAL_CERTIFICATE_PREUNBLIND.json"
            pre_sha = Y4._atomic_write_json(pre_path, preunblind)
            intrinsic_path, intrinsic_sha, _computed = (
                Y4._derive_gamma_from_sealed_kernel(root, pre_path, pre_sha)
            )
            reference = parent / "terminal-reference.json"
            reference.write_bytes(
                Y4._canonical_json_bytes(FIXED_REFERENCE_ENVELOPE)
            )
            final_path, final_sha, comparison = Y4._terminal_unblind(
                root,
                pre_path,
                pre_sha,
                intrinsic_path,
                intrinsic_sha,
                reference,
            )
            Y4._write_status(
                root,
                "PASS",
                script_sha,
                {
                    "phase": "terminal_unblind",
                    "preunblind_sha256": pre_sha,
                    "intrinsic_gamma_sha256": intrinsic_sha,
                    "final_certificate": str(final_path),
                    "final_sha256": final_sha,
                    "computed_q3_u4": comparison["computed_q3_u4"],
                    "historical_exact_equal": True,
                },
            )
            with self.assertRaisesRegex(Y4.ProductionFailure, "missing physical artifacts"):
                Y4._verify_existing_sealed_run(root, require_terminal_pass=True)
            validator = load_notebook_pass_validator()
            with self.assertRaisesRegex(RuntimeError, "missing physical artifacts"):
                validator(
                    root,
                    script_sha,
                    Y4.HISTORICAL_REFERENCE_ENVELOPE_SHA256,
                )
            with contextlib.redirect_stdout(io.StringIO()):
                with self.assertRaisesRegex(
                    Y4.ProductionFailure, "missing physical artifacts"
                ):
                    Y4.verify_sealed_run_main(root, require_terminal_pass=True)
            failed_status = Y4.read_json(root / "Y4_CANONICAL_RUN_STATUS.json")
            self.assertEqual(failed_status["status"], "FAIL")
            self.assertEqual(
                failed_status["detail"]["phase"], "sealed_run_verification"
            )
            snapshot.unlink()
            with self.assertRaisesRegex(Y4.ProductionFailure, "kernel_snapshot"):
                Y4._verify_existing_sealed_run(root, require_terminal_pass=True)

    def test_required_gate_manifest_cannot_be_partial(self) -> None:
        with self.assertRaises(Y4.ProductionFailure):
            Y4._require_passed_gates(
                {"I0_folded_formula": {"passed": True}},
                "Stage-I",
                frozenset({"I0_folded_formula", "I1_dependencies"}),
            )

    def test_stage_i_formula_and_stage1_lineage_are_exact(self) -> None:
        stage1_sha = "1" * 64
        summary = {
            "gates": {
                "I0_folded_formula": {
                    "operator_identity": Y4.EXPECTED_H4_OPERATOR_IDENTITY
                },
                "I1_dependencies": {"stage1_sha256": stage1_sha},
            }
        }
        Y4._require_stage_i_formula_and_lineage(summary, stage1_sha)
        bad_formula = copy.deepcopy(summary)
        bad_formula["gates"]["I0_folded_formula"]["operator_identity"] += "+poison"
        with self.assertRaises(Y4.ProductionFailure):
            Y4._require_stage_i_formula_and_lineage(bad_formula, stage1_sha)
        with self.assertRaises(Y4.ProductionFailure):
            Y4._require_stage_i_formula_and_lineage(summary, "2" * 64)

    def test_stage3h_is_sealed_out_before_and_after_stage_i(self) -> None:
        summary = {
            "counts": {"stage3h_regression_topologies": 0},
            "gates": {
                "I2_complete_topology_contraction": {
                    "stage3h_topologies_regressed": 0
                }
            },
        }
        with tempfile.TemporaryDirectory() as td:
            sentinel = Path(td) / "_SEALED_NO_STAGE3H_INPUT.json.gz"
            Y4._require_stage3h_sealed_out(summary, sentinel)
            sentinel.write_bytes(b"poison")
            with self.assertRaises(Y4.ProductionFailure):
                Y4._require_stage3h_sealed_out(summary, sentinel)
            sentinel.unlink()
            contaminated = copy.deepcopy(summary)
            contaminated["counts"]["stage3h_regression_topologies"] = 1478
            contaminated["gates"]["I2_complete_topology_contraction"][
                "stage3h_topologies_regressed"
            ] = 1478
            with self.assertRaises(Y4.ProductionFailure):
                Y4._require_stage3h_sealed_out(contaminated, sentinel)

    def test_run_binding_resume_and_stale_status_are_fail_closed(self) -> None:
        binding = {"schema": "test", "hash": "abc"}
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "run"
            self.assertEqual(Y4._prepare_run_root(root, False, binding), root.resolve())
            Y4._write_status(root, "PASS", "script", {"old": True})
            Y4._write_status(root, "RUNNING", "script", {"old": False})
            self.assertEqual(Y4.read_json(root / "Y4_CANONICAL_RUN_STATUS.json")["status"], "RUNNING")
            with self.assertRaises(Y4.ProductionFailure):
                Y4._prepare_run_root(root, False, binding)
            self.assertEqual(Y4._prepare_run_root(root, True, binding), root.resolve())
            with self.assertRaises(Y4.ProductionFailure):
                Y4._prepare_run_root(root, True, {"schema": "test", "hash": "wrong"})

    def test_worker_failure_writes_fail_and_never_loads_reference(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "failed-run"
            with mock.patch.object(
                Y4, "_authoritative_main", side_effect=Y4.ProductionFailure("poison")
            ), mock.patch.object(
                Y4,
                "_load_historical_q3_after_seal",
                side_effect=AssertionError("historical reference loaded"),
            ):
                with contextlib.redirect_stdout(io.StringIO()):
                    with self.assertRaisesRegex(Y4.ProductionFailure, "poison"):
                        Y4.production_main(root, False)
            status = Y4.read_json(root / "Y4_CANONICAL_RUN_STATUS.json")
            self.assertEqual(status["status"], "FAIL")
            self.assertFalse(status["detail"]["historical_reference_loaded"])

    def test_json_rejects_nonfinite_values(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            with self.assertRaises(ValueError):
                Y4._atomic_write_json(Path(td) / "bad.json", {"x": float("nan")})
            with self.assertRaises(Y4.ProductionFailure):
                Y4._assert_finite_tree({"x": float("inf")})
            for poison in (
                b'{"x":NaN}',
                b'{"x":Infinity}',
                b'{"x":1e9999}',
                b'{"x":1,"x":2}',
            ):
                with self.assertRaises(Y4.ProductionFailure):
                    Y4._strict_json_loads(poison, "poison")
            duplicate_path = Path(td) / "duplicate-status.json"
            duplicate_path.write_bytes(b'{"status":"PASS","status":"FAIL"}')
            with self.assertRaisesRegex(Y4.ProductionFailure, "duplicate JSON key"):
                Y4.read_json(duplicate_path)

    def test_kernel_reader_rejects_nan_duplicate_and_extra_metadata(self) -> None:
        archived = Y4._load_kernel_payload_bytes(base64.b64decode(ARCHIVED_KERNEL_B64))
        poisoned = copy.deepcopy(archived)
        poisoned["meta"]["poison"] = float("nan")
        poisoned_raw = gzip.compress(
            json.dumps(poisoned, sort_keys=True, separators=(",", ":")).encode(),
            mtime=0,
        )
        with self.assertRaises(Y4.ProductionFailure):
            Y4._load_kernel_payload_bytes(poisoned_raw)
        extra = copy.deepcopy(archived)
        extra["meta"]["poison"] = 0
        extra_raw = gzip.compress(Y4._canonical_json_bytes(extra), mtime=0)
        with self.assertRaisesRegex(Y4.ProductionFailure, "schema mismatch"):
            Y4._load_kernel_payload_bytes(extra_raw)
        duplicate_raw = gzip.compress(
            b'{"meta":{"version":"x","version":"y"},"kernel":[]}',
            mtime=0,
        )
        with self.assertRaisesRegex(Y4.ProductionFailure, "duplicate JSON key"):
            Y4._load_kernel_payload_bytes(duplicate_raw)

    def test_residual_uses_one_strict_snapshot_and_exact_kernel_binding(self) -> None:
        kernel_sha = "1" * 64
        residual = {
            "meta": {
                "version": "2026-06-13-stage3j-v1",
                "kernel_file": "DATA_Y4_full_real_space_h4_kernel.json.gz",
                "kernel_sha256": kernel_sha,
            },
            "cube_state": [],
            "rigid_component_c4": "0",
            "H4_cube_image": [],
            "residual": [],
            "dominant_leakage": [],
        }
        raw = Y4._canonical_json_bytes(residual)
        physical_sha, identity = Y4._residual_physical_identity(raw, kernel_sha)
        self.assertEqual(physical_sha, Y4._sha256_bytes(Y4._canonical_json_bytes(identity)))
        with self.assertRaisesRegex(Y4.ProductionFailure, "not bound"):
            Y4._residual_physical_identity(raw, "2" * 64)
        poisoned = copy.deepcopy(residual)
        poisoned["meta"]["extra"] = 0
        with self.assertRaisesRegex(Y4.ProductionFailure, "schema mismatch"):
            Y4._residual_physical_identity(
                Y4._canonical_json_bytes(poisoned), kernel_sha
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
