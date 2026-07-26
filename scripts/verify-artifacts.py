#!/usr/bin/env python3
"""Verify canonical archive bytes and emit a local SHA-256 manifest."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Final

ROOT: Final = Path(__file__).resolve().parent.parent
REGISTRY: Final = ROOT / "manifests" / "EXPECTED_CHECKSUMS.json"
LOCAL_MANIFEST: Final = ROOT / "manifests" / "LOCAL_SHA256SUMS"
CHUNK: Final = 1024 * 1024


def digest(path: Path, algorithm: str) -> str:
    h = hashlib.new(algorithm)
    with path.open("rb") as f:
        while block := f.read(CHUNK):
            h.update(block)
    return h.hexdigest()


def main() -> int:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    failures: list[str] = []
    local_sha256: list[tuple[str, str]] = []

    for item in registry["artifacts"]:
        relative = Path(item["path"])
        path = ROOT / relative
        if not path.is_file():
            failures.append(f"MISSING {relative}")
            continue

        print(f"VERIFY  {relative}")
        for algorithm, expected in item["expected"].items():
            actual = digest(path, algorithm)
            state = "OK" if actual.lower() == expected.lower() else "FAIL"
            print(f"  {algorithm:<7} {state}  {actual}")
            if state != "OK":
                failures.append(
                    f"MISMATCH {relative} {algorithm}: expected {expected}, got {actual}"
                )

        local_sha256.append((digest(path, "sha256"), relative.as_posix()))

    LOCAL_MANIFEST.write_text(
        "".join(f"{value}  {path}\n" for value, path in sorted(local_sha256)),
        encoding="utf-8",
    )

    if failures:
        print("\nVerification failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(f"\nAll registered checksums passed. Wrote {LOCAL_MANIFEST.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
