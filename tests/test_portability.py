"""The repository must read the same on every platform it is used from.

This corpus is edited on Windows and checked on Linux. The failure mode caught
here is silent on Linux and fatal on Windows: text opened without a named
encoding is decoded with the platform's locale, which on Windows is cp1252, and
this repository holds hundreds of files that are not cp1252-decodable.
"""

import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src" / "workhouse"
TEXT_SUFFIXES = {".lean", ".py", ".md", ".yaml", ".tex", ".csv", ".jsonl", ".txt"}
# Path methods whose text mode decodes with the locale unless told otherwise.
LOCALE_SENSITIVE = {"read_text", "write_text", "open"}


def _binary_mode(call: ast.Call) -> bool:
    """True when the call opens bytes, where an encoding would be an error."""
    for arg in list(call.args) + [k.value for k in call.keywords if k.arg == "mode"]:
        if isinstance(arg, ast.Constant) and isinstance(arg.value, str) and "b" in arg.value:
            return True
    return False


def test_text_io_names_its_encoding():
    """No text read or write in src/ may inherit the platform's locale encoding.

    `workhouse why C2` died on byte 0x81 in a Lean source until the caller set
    PYTHONUTF8=1. Reported against this repository in
    notes/imported/UPLOADS_2026-08-28i/THEORY_GRAPH_AGENT_EXPERIENCE_NOTES_20260828.md
    and fixed by naming utf-8 at every call site. Parsed rather than grepped so
    a call split across lines is judged by its keywords, not by its first line.
    """
    offenders = []
    for path in sorted(SRC.rglob("*.py")):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Attribute):
                continue
            if node.func.attr not in LOCALE_SENSITIVE or _binary_mode(node):
                continue
            if any(k.arg == "encoding" for k in node.keywords):
                continue
            offenders.append(f"{path.relative_to(ROOT)}:{node.lineno}: .{node.func.attr}()")
    assert not offenders, "text I/O without an explicit encoding:\n" + "\n".join(offenders)


def test_the_corpus_really_is_not_cp1252_decodable():
    """The premise of the test above, measured rather than asserted.

    If this ever came back near zero the encoding guard would be guarding
    nothing, and the interesting question would be where the corpus lost its
    non-Latin-1 bytes.
    """
    undecodable = 0
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or path.suffix not in TEXT_SUFFIXES or not path.is_file():
            continue
        try:
            path.read_bytes().decode("cp1252")
        except UnicodeDecodeError:
            undecodable += 1
    assert undecodable > 100, f"only {undecodable} files are non-cp1252; the guard may be moot"
