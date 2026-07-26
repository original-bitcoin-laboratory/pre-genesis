#!/usr/bin/env python3
"""Generate a deterministic manifest for an extracted source tree."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

CHUNK = 1024 * 1024


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while block := f.read(CHUNK):
            h.update(block)
    return h.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("tree", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    tree = args.tree.resolve()
    if not tree.is_dir():
        parser.error(f"not a directory: {tree}")

    entries = []
    for path in sorted(p for p in tree.rglob("*") if p.is_file()):
        entries.append(
            {
                "path": path.relative_to(tree).as_posix(),
                "size": path.stat().st_size,
                "sha256": sha256(path),
            }
        )

    payload = {"schema": 1, "root": tree.name, "file_count": len(entries), "files": entries}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {args.output} ({len(entries)} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
