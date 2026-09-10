"""Acquire the version-pinned related sources; preserve PDFs and record their hashes."""

from __future__ import annotations

import hashlib
import json
import urllib.request
from datetime import UTC, datetime
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    manifest = root / "literature/yangmills/sources_related.json"
    records = json.loads(manifest.read_text(encoding="utf-8"))
    for record in records:
        folder = (
            "literature/fulltext"
            if record["licence"] == "cc-by"
            else "literature/inbox/JW_2006/sources"
        )
        path = root / folder / f"{record['id']}.pdf"
        path.parent.mkdir(parents=True, exist_ok=True)
        record["retrieved_at"] = datetime.now(UTC).isoformat()
        try:
            request = urllib.request.Request(
                record["download_url"], headers={"User-Agent": "WORKHOUSE source acquisition"}
            )
            with urllib.request.urlopen(request, timeout=60) as response:
                data = response.read()
                record["resolved_url"] = response.url
            if not data.startswith(b"%PDF"):
                raise ValueError("Source response was not a PDF")
            path.write_bytes(data)
            record.update(
                local_path=path.relative_to(root).as_posix(),
                sha256=hashlib.sha256(data).hexdigest(),
                access_status="downloaded",
            )
            print(record["id"], len(data), record["sha256"])
        except (OSError, ValueError) as exc:
            record["access_status"] = "download-failed"
            record["access_note"] = str(exc)
            print(record["id"], record["access_note"])
    manifest.write_text(json.dumps(records, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
