from __future__ import annotations

import ast
import errno
import fcntl
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SCRIPT = ROOT / "ENGINE_Y4_hodge_canonical_o4_production_colab.py"
NOTEBOOK = ROOT / "NB_Y4_hodge_canonical_o4_production_colab.ipynb"
EXPECTED = "1970c63a426812bece12b1be1706958fd8ea9ecfbeb3d305875d40ff6f2266b5"

source = SCRIPT.read_bytes()
assert hashlib.sha256(source).hexdigest() == EXPECTED

# Extract the notebook function without altering it.
notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
cell = next("".join(c["source"]) for c in notebook["cells"] if c["cell_type"] == "code")
tree = ast.parse(cell)
node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "run_hash_bound")

real_subprocess = subprocess
observed: dict[str, object] = {}


class AttackProxy:
    def __init__(self, visible: Path):
        self.visible = visible

    def run(self, command, **kwargs):
        fd = kwargs["pass_fds"][0]
        assert command[2] == f"/proc/self/fd/{fd}"
        assert kwargs["env"]["HODGE_Y4_SEALED_SOURCE_FD"] == str(fd)
        observed["argv0"] = command[2]
        observed["fd_target"] = os.readlink(command[2])
        observed["fd_sha256"] = hashlib.sha256(os.pread(fd, len(source) + 1, 0)).hexdigest()
        failures = {}
        for label, operation in (
            ("overwrite", lambda: os.pwrite(fd, b"X", 0)),
            ("shrink", lambda: os.ftruncate(fd, 0)),
            ("grow", lambda: os.ftruncate(fd, len(source) + 1)),
        ):
            try:
                operation()
            except OSError as exc:
                failures[label] = exc.errno
            else:
                raise AssertionError(f"sealed memfd allowed {label}")
        assert failures == {"overwrite": errno.EPERM, "shrink": errno.EPERM, "grow": errno.EPERM}
        observed["mutation_errno"] = failures

        # Strong TOCTOU model: replace the visible snapshot after its pre-hash,
        # leave it poisoned for the entire child lifetime, then restore it before
        # the runner's post-hash. The child must still execute the memfd bytes.
        self.visible.write_bytes(b"print('POISON PATH EXECUTED')\n")
        try:
            result = real_subprocess.run(
                command,
                check=kwargs["check"],
                pass_fds=kwargs["pass_fds"],
                env=kwargs["env"],
                capture_output=True,
                text=True,
            )
        finally:
            self.visible.write_bytes(source)
        observed["stdout"] = result.stdout
        observed["returncode"] = result.returncode
        assert "SELF-TEST PASS" in result.stdout
        assert "POISON PATH EXECUTED" not in result.stdout
        return result


with tempfile.TemporaryDirectory(prefix="hodge_frozen_runner_") as td:
    visible = Path(td) / "verified.py"
    visible.write_bytes(source)
    namespace = {
        "errno": errno,
        "fcntl": fcntl,
        "hashlib": hashlib,
        "os": os,
        "Path": Path,
        "subprocess": AttackProxy(visible),
        "sys": sys,
    }
    exec(compile(ast.Module(body=[node], type_ignores=[]), "<exact-notebook-runner>", "exec"), namespace)
    namespace["run_hash_bound"](visible, source, EXPECTED, ["--self-test"])
    assert visible.read_bytes() == source
    observed["visible_restored"] = True

# Exercise the production worker launcher itself with a synthetic child while
# attacking its inherited descriptor. This executes the exact frozen function.
spec = importlib.util.spec_from_file_location("frozen_worker_audit", SCRIPT)
assert spec is not None and spec.loader is not None
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)

worker_source = """from __future__ import annotations
import hashlib, json, os, sys
fd = int(os.environ['HODGE_Y4_SEALED_WORKER_FD'])
path = f'/proc/self/fd/{fd}'
raw = open(path, 'rb').read()
assert hashlib.sha256(raw).hexdigest() == os.environ['HODGE_Y4_SEALED_WORKER_SHA256']
open(sys.argv[1], 'w', encoding='utf-8').write(json.dumps({'argv0':sys.argv[0],'fd':fd,'sha256':hashlib.sha256(raw).hexdigest(),'target':os.readlink(path)}))
"""

worker_real_subprocess = module.subprocess
worker_attack: dict[str, object] = {}


class WorkerAttackProxy:
    def run(self, command, **kwargs):
        fd = kwargs["pass_fds"][0]
        assert command[2] == f"/proc/self/fd/{fd}"
        failures = {}
        for label, operation in (
            ("overwrite", lambda: os.pwrite(fd, b"X", 0)),
            ("shrink", lambda: os.ftruncate(fd, 0)),
            ("grow", lambda: os.ftruncate(fd, len(worker_source.encode("utf-8")) + 1)),
        ):
            try:
                operation()
            except OSError as exc:
                failures[label] = exc.errno
            else:
                raise AssertionError(f"worker memfd allowed {label}")
        worker_attack["mutation_errno"] = failures
        return worker_real_subprocess.run(command, **kwargs)


with tempfile.TemporaryDirectory(prefix="hodge_frozen_worker_") as td:
    td_path = Path(td)
    output = td_path / "worker.json"
    module.subprocess = WorkerAttackProxy()
    try:
        module.run_source(worker_source, "independent_worker.py", [str(output)], cwd=td_path)
    finally:
        module.subprocess = worker_real_subprocess
    worker_result = json.loads(output.read_text(encoding="utf-8"))
    assert worker_result["argv0"] == f"/proc/self/fd/{worker_result['fd']}"
    assert worker_result["sha256"] == hashlib.sha256(worker_source.encode("utf-8")).hexdigest()
    assert worker_attack["mutation_errno"] == {"overwrite": errno.EPERM, "shrink": errno.EPERM, "grow": errno.EPERM}

print(json.dumps({
    "runner": {k: v for k, v in observed.items() if k != "stdout"},
    "runner_self_test_pass": "SELF-TEST PASS" in str(observed.get("stdout", "")),
    "worker": worker_result,
    "worker_attack": worker_attack,
}, indent=2, sort_keys=True))
