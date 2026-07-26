#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

command -v curl >/dev/null 2>&1 || {
  echo "error: curl is required" >&2
  exit 1
}

fetch() {
  local url="$1"
  local output="$2"
  mkdir -p "$(dirname "$output")"
  if [[ -f "$output" ]]; then
    echo "exists: $output"
    return
  fi
  echo "fetch:  $url"
  curl --fail --location --proto '=https' --tlsv1.2 \
    --output "$output.part" "$url"
  mv "$output.part" "$output"
}

# OBL-NOV08 - November 15, 2008 pre-release source witness
fetch "https://cdn.nakamotoinstitute.org/code/bitcoin-nov08.rar" \
      "artifacts/nov08/bitcoin-nov08.rar"
fetch "https://cdn.nakamotoinstitute.org/code/bitcoin-nov08.tgz" \
      "artifacts/nov08/bitcoin-nov08.tgz"

echo
echo "Artifacts acquired. Run: python scripts/verify-artifacts.py"
