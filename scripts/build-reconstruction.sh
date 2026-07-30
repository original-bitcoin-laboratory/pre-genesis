#!/usr/bin/env bash
# Reproduces the November 2008 build-reconstruction finding (docs/BUILD_RECONSTRUCTION.md):
# the preview snapshot cannot compile standalone -- it #includes a headers.h it does not
# ship, and references script/key/bignum units that are absent. NOT money.
#
# Requires a C++ compiler and the R0-verified archive extracted at ../extracted/.
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$HERE/../extracted"
[ -x /c/msys64/mingw64/bin/g++.exe ] && export PATH="/c/msys64/mingw64/bin:$PATH"
GXX="${GXX:-g++}"

echo "== nov08 build-reconstruction =="
if [ ! -d "$SRC" ]; then echo "!! extract the R0-verified nov08 archive at extracted/ first"; exit 2; fi

echo "snapshot files:"; ls -1 "$SRC" | grep -E '\.(cpp|h)$' | sed 's/^/   /'
echo "headers referenced by the .cpp:"; grep -hoE '#include "[a-z0-9_]+\.h"' "$SRC"/*.cpp | sort -u | sed 's/^/   /'
echo "headers actually present:"; ls -1 "$SRC" | grep -E '\.h$' | sed 's/^/   /'

echo; echo "-- attempt: compile main.cpp standalone (expect: fatal error, missing headers.h) --"
if "$GXX" -std=gnu++11 -w -I"$SRC" -fsyntax-only "$SRC/main.cpp" 2>"$HERE/nov08_build.err"; then
  echo "!! UNEXPECTED: main.cpp compiled -- the finding would need revisiting"; exit 1
fi
first="$(grep -m1 -E 'fatal error|error:' "$HERE/nov08_build.err")"
echo "   compiler stopped at: $first"
rm -f "$HERE/nov08_build.err"

if echo "$first" | grep -q "headers.h"; then
  echo; echo "RESULT: confirmed -- standalone build impossible (no headers.h; script/key/bignum units absent)."
else
  echo; echo "!! stopped for a different reason than expected; inspect above."; exit 1
fi
