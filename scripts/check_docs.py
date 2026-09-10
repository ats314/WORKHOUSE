"""Read-only checks for explicit local links in curated maintained Markdown.

This is a small documentation checker, not a CommonMark renderer. See LIMITS
and the JSON output for the exact boundary. Historical trees are not crawled.
"""

from __future__ import annotations

import argparse
import html
import json
import posixpath
import re
import string
import unicodedata
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = "docs/documentation_manifest.json"
LIMITS = [
    "Only maintained Markdown paths listed in the manifest are scanned for outgoing links.",
    "Targets outside that list are read only to verify an explicitly linked Markdown anchor.",
    "HTTP(S) and mailto links are skipped; no external URL, GitHub state or command is executed.",
    "Checks inline links/images and single-line reference definitions with full, collapsed or "
    "defined shortcut references; multiline reference definitions are not parsed.",
    "Skips fenced code, inline code, indented code lines and HTML comments. Container-nested "
    "fences, HTML blocks, raw HTML href/src links, autolinks and MDX are not parsed.",
    "Heading anchors support ordinary ATX and single-line Setext headings, Unicode, duplicate "
    "GitHub-style slugs, and explicit HTML id or a[name] anchors. Complex rendered heading "
    "markup, container headings and HTML entity edge cases are not a full renderer emulation.",
    "Fragments on non-Markdown files or directories are not validated.",
]


def _blank(text: str) -> str:
    return re.sub(r"[^\n]", " ", text)


def visible_blocks(text: str) -> str:
    """Mask code/comments without changing character offsets or line numbers."""
    lines = []
    fence = None
    comment = False
    for line in text.splitlines(keepends=True):
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line.rstrip("\r\n"))
        if fence:
            if (
                marker
                and marker[1][0] == fence[0]
                and len(marker[1]) >= fence[1]
                and not marker[2].strip()
            ):
                fence = None
            lines.append(_blank(line))
        elif not comment and marker and (marker[1][0] != "`" or "`" not in marker[2]):
            fence = (marker[1][0], len(marker[1]))
            lines.append(_blank(line))
        elif not comment and line.startswith(("    ", "\t")):
            lines.append(_blank(line))
        else:
            # A fence marker in a comment is inert; comment markers inside an
            # active code fence are inert too. Track the active block before
            # interpreting delimiters instead of masking in two separate passes.
            pieces, cursor = [], 0
            while cursor < len(line):
                if comment:
                    end = line.find("-->", cursor)
                    if end == -1:
                        pieces.append(_blank(line[cursor:]))
                        break
                    pieces.append(_blank(line[cursor : end + 3]))
                    cursor, comment = end + 3, False
                else:
                    start = line.find("<!--", cursor)
                    if start == -1:
                        pieces.append(line[cursor:])
                        break
                    pieces.append(line[cursor:start])
                    cursor, comment = start, True
            lines.append("".join(pieces))
    return "".join(lines)


def _without_inline_code(text: str) -> str:
    return re.sub(
        r"(?<!`)(`+)(?!`)([\s\S]*?)(?<!`)\1(?!`)",
        lambda m: _blank(m[0]),
        text,
    )


def _unescape(text: str) -> str:
    return html.unescape(re.sub(r"\\([" + re.escape(string.punctuation) + r"])", r"\1", text))


def _label(text: str) -> str:
    return " ".join(_unescape(text).split()).casefold()


def _bracket_end(text: str, start: int) -> int | None:
    depth, i = 1, start + 1
    while i < len(text):
        if text[i] == "\\":
            i += 2
            continue
        if text[i] == "[":
            depth += 1
        elif text[i] == "]":
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return None


def _destination(text: str, start: int) -> tuple[str, int] | None:
    """Read an angle-delimited or balanced bare destination, before its title."""
    i = start
    if i < len(text) and text[i] == "<":
        i += 1
        begin = i
        while i < len(text) and text[i] not in ">\n":
            i += 2 if text[i] == "\\" else 1
        return (text[begin:i], i + 1) if i < len(text) and text[i] == ">" else None
    begin, depth = i, 0
    while i < len(text):
        char = text[i]
        if char == "\\":
            i += 2
            continue
        if char == "(":
            depth += 1
        elif char == ")":
            if depth == 0:
                break
            depth -= 1
        elif char.isspace():
            break
        i += 1
    return (text[begin:i], i) if depth == 0 else None


def _after_title(text: str, start: int) -> int | None:
    i = start
    while i < len(text) and text[i].isspace():
        i += 1
    if i < len(text) and text[i] in "\"'(":
        quote = ")" if text[i] == "(" else text[i]
        i += 1
        while i < len(text) and text[i] != quote:
            i += 2 if text[i] == "\\" else 1
        if i >= len(text):
            return None
        i += 1
        while i < len(text) and text[i].isspace():
            i += 1
    return i


def markdown_links(text: str) -> tuple[list[tuple[int, str]], list[tuple[int, str]], list]:
    visible = _without_inline_code(visible_blocks(text))
    links, errors, warnings, definitions = [], [], [], {}
    definition = re.compile(r"^ {0,3}\[([^\]\n]+)\]:[ \t]*(.*)$", re.MULTILINE)
    spans = []
    for match in definition.finditer(visible):
        line = visible.count("\n", 0, match.start()) + 1
        parsed = _destination(match[2], 0)
        if not match[2].strip() or parsed is None:
            warnings.append((line, "Unsupported multiline or malformed reference definition"))
        else:
            label = _label(match[1])
            if label not in definitions:
                definitions[label] = parsed[0]
                links.append((line, parsed[0]))
        spans.append(match.span())
    for start, end in reversed(spans):
        visible = visible[:start] + _blank(visible[start:end]) + visible[end:]
    consumed = []
    for start in (m.start() for m in re.finditer(r"(?<!\\)\[", visible)):
        if any(begin <= start < end for begin, end in consumed):
            continue
        end = _bracket_end(visible, start)
        if end is None:
            continue
        after = end + 1
        line = visible.count("\n", 0, start) + 1
        # Allow a single line wrap between the label and destination/reference.
        whitespace = re.match(r"[ \t]*(?:\n[ \t]*)?", visible[after:])[0]
        after += len(whitespace)
        if after < len(visible) and visible[after] == "(":
            begin = after + 1
            while begin < len(visible) and visible[begin].isspace():
                begin += 1
            parsed = _destination(visible, begin)
            stop = _after_title(visible, parsed[1]) if parsed else None
            if stop is None or stop >= len(visible) or visible[stop] != ")":
                errors.append((line, "Malformed or unsupported inline link destination"))
            else:
                links.append((line, parsed[0]))
                consumed.append((after, stop + 1))
        elif after < len(visible) and visible[after] == "[":
            ref_end = _bracket_end(visible, after)
            if ref_end is not None:
                consumed.append((after, ref_end + 1))
                label = _label(visible[after + 1 : ref_end] or visible[start + 1 : end])
                if label not in definitions:
                    errors.append((line, f"Undefined link reference: {label}"))
    return links, errors, warnings


class _ExplicitAnchors(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.anchors = set()

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if value is not None and (key == "id" or (tag == "a" and key == "name")):
                self.anchors.add(value)


def _slug(text: str) -> str:
    text = re.sub(r"!?\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\[[^\]]*\]", r"\1", text)
    text = re.sub(r"<[^>]*>", "", text)
    text = re.sub(r"(?<!\w)_([^_]+)_(?!\w)", r"\1", text)
    text = _unescape(text).strip().lower()
    return "".join(
        "-" if char == " " else char
        for char in text
        if char in " -_" or unicodedata.category(char)[0] in "LNM"
    )


def markdown_anchors(text: str) -> set[str]:
    visible = visible_blocks(text)
    parser = _ExplicitAnchors()
    parser.feed(_without_inline_code(visible))
    anchors, used = set(parser.anchors), set()
    lines = visible.splitlines()
    for i, line in enumerate(lines):
        atx = re.match(r"^ {0,3}#{1,6}(?:[ \t]+(.*?)|[ \t]*)$", line)
        title = None
        if atx:
            title = re.sub(r"[ \t]+#+[ \t]*$", "", atx[1] or "")
        elif (
            i + 1 < len(lines)
            and line.strip()
            and re.fullmatch(r" {0,3}(?:=+|-+)[ \t]*", lines[i + 1])
        ):
            title = line.strip()
        if title is not None:
            base = _slug(title)
            slug, number = base, 0
            while slug in used:
                number += 1
                slug = f"{base}-{number}"
            used.add(slug)
            anchors.add(slug)
    return anchors


def _local_target(root: Path, source: str, destination: str) -> tuple[Path, str] | str:
    try:
        split = urlsplit(_unescape(destination))
        path = unquote(split.path, errors="strict")
        fragment = unquote(split.fragment, errors="strict")
    except (ValueError, UnicodeError):
        return "Invalid URL or UTF-8 percent encoding"
    if split.scheme.lower() in {"http", "https", "mailto"}:
        return "external"
    if split.scheme or split.netloc or path.startswith(("/", "~")) or "\\" in path:
        return "Absolute/local-machine paths and nonportable URL schemes are not allowed"
    if re.match(r"^[A-Za-z]:", path):
        return "Windows absolute or drive-relative paths are not allowed"
    relative = (
        posixpath.normpath(posixpath.join(posixpath.dirname(source), path)) if path else source
    )
    if relative == ".." or relative.startswith("../"):
        return "Link escapes the checkout"
    target = root
    for component in relative.split("/"):
        if component in {"", "."}:
            continue
        if not target.is_dir():
            return f"Missing local target: {relative}"
        names = {p.name for p in target.iterdir()}
        if component not in names:
            alternatives = sorted(name for name in names if name.casefold() == component.casefold())
            if alternatives:
                return f"Filename case mismatch: {component!r}; on disk: {alternatives[0]!r}"
            return f"Missing local target: {relative}"
        target /= component
    if not target.resolve().is_relative_to(root.resolve()):
        return "Link resolves outside the checkout (including symlinks)"
    return target, fragment


def check(root: Path = ROOT, manifest: Path | None = None) -> dict:
    root = root.resolve()
    manifest = manifest or root / DEFAULT_MANIFEST
    result = dict(
        schema="documentation-check/v1",
        checked_documents=0,
        checked_links=0,
        skipped_external_links=0,
        unchecked_non_markdown_fragments=0,
        errors=[],
        warnings=[],
        scope_limits=LIMITS,
    )

    def issue(source, line, message, destination=None, *, warning=False):
        row = dict(source=source, line=line, message=message)
        if destination is not None:
            row["destination"] = destination
        result["warnings" if warning else "errors"].append(row)

    try:
        data = json.loads(manifest.read_text(encoding="utf-8-sig"))
        maintained = data.get("maintained") if isinstance(data, dict) else None
        if (
            not isinstance(data, dict)
            or data.get("schema") != "documentation-manifest/v1"
            or not isinstance(maintained, list)
            or not maintained
            or not all(isinstance(path, str) and path.endswith(".md") for path in maintained)
            or len(maintained) != len(set(maintained))
        ):
            raise ValueError("Expected unique maintained .md paths in documentation-manifest/v1")
    except (OSError, UnicodeError, ValueError) as exc:
        issue(str(manifest), 0, f"Cannot load documentation manifest: {exc}")
        return result
    anchor_cache = {}
    for source in maintained:
        located = _local_target(root, "", source)
        if isinstance(located, str) or not located[0].is_file() or located[1]:
            issue(source, 0, f"Invalid maintained document path: {located}")
            continue
        try:
            text = located[0].read_text(encoding="utf-8-sig")
            links, errors, warnings = markdown_links(text)
            result["checked_documents"] += 1
            for line, message in errors:
                issue(source, line, message)
            for line, message in warnings:
                issue(source, line, message, warning=True)
            for line, destination in links:
                resolved = _local_target(root, source, destination)
                if resolved == "external":
                    result["skipped_external_links"] += 1
                    continue
                result["checked_links"] += 1
                if isinstance(resolved, str):
                    issue(source, line, resolved, destination)
                    continue
                target, fragment = resolved
                if fragment and target.is_file() and target.suffix.lower() == ".md":
                    if target not in anchor_cache:
                        anchor_cache[target] = markdown_anchors(
                            target.read_text(encoding="utf-8-sig")
                        )
                    if fragment not in anchor_cache[target]:
                        issue(source, line, f"Missing Markdown anchor: #{fragment}", destination)
                elif fragment:
                    result["unchecked_non_markdown_fragments"] += 1
        except (OSError, UnicodeError, ValueError) as exc:
            issue(source, 0, f"Cannot inspect documentation: {exc}")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--json", action="store_true", help="Print the full result as JSON")
    args = parser.parse_args()
    manifest = args.manifest
    if manifest is not None and not manifest.is_absolute():
        manifest = args.root / manifest
    result = check(args.root, manifest)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=True))
    else:
        print(
            f"Documentation: {result['checked_documents']} maintained files, "
            f"{result['checked_links']} local links, {len(result['errors'])} errors, "
            f"{len(result['warnings'])} warnings."
        )
        for kind in ("errors", "warnings"):
            for row in result[kind]:
                print(f"{kind[:-1]}: {row['source']}:{row['line']}: {row['message']}")
        print("Scope: curated explicit links only; external URLs and historical trees not scanned.")
        print("Use --json for parser limits and skipped-link counts.")
    return bool(result["errors"])


if __name__ == "__main__":
    raise SystemExit(main())
