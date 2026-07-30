# Build reconstruction — the November 2008 preview cannot build standalone

**Evidence level: NEW-EXP (host-toolchain build attempt of the unmodified snapshot).**
**NOT money.**

Roadmap R2 asks for "the maximum executable reconstruction possible for NOV08." For this
snapshot the answer is sharp and verifiable: **zero, standalone** — it cannot even begin to
compile from its own files, for a more basic reason than any toolchain-version lock.

Reproduce: `bash scripts/build-reconstruction.sh` (needs a C++ compiler and the R0-verified
archive extracted at `extracted/`).

## What the snapshot contains

Four files, 5,005 lines: `main.cpp`, `main.h`, `node.cpp`, `node.h`. That is the entire
preview as preserved — there is no build system beyond a header reference, and no crypto,
script, database, or UI unit.

## Why it can't compile

Both `.cpp` files begin with:

```cpp
#include "headers.h"
#include "sha.h"     // (main.cpp)
```

Neither `headers.h` nor `sha.h` exists in the snapshot — the only headers present are
`main.h` and `node.h`. The compiler stops immediately:

```
fatal error: headers.h: No such file or directory
```

And the gap is not just those two files. `main.*`/`node.*` reference `OP_CHECKSIG`,
`CScript`, `CKey`, and construct `CTransaction`, but the snapshot defines **none** of the
units those names live in — there is no `script.*`, `key.h`, `bignum.h`, `serialize.h`,
`db.*`, `net.*`, or `ui.*`. So even after supplying a `headers.h`, the referenced types have
no definitions. This confirms the inventory finding (`inventory/SOURCE_INVENTORY.md`): the
November preview is a **partial capture of the node/main layer only**, not a self-contained
program.

## What reconstruction therefore means for NOV08

Because the preview cannot stand alone, any executable reconstruction must be **donor-assisted**:
the missing units come from the January 2009 codebase and are marked as such. That is exactly
what the lab's **NOV08-X** derivative does — it executes November's constitution (the monetary
rules and the `main.*`/`node.*` structure) on the reconstructed substrate, every line
provenance-classed **N-ORIG / N-IFACE / J-DONOR / NEW-EXP** (see `derivatives/nov08x/` and its
design ledger). NOV08-X is the reconstruction vehicle; a standalone period build of the
snapshot is not possible, and that impossibility is a *finding about the artifact*, not a
limitation of the method.

For the January 2009 client — which is complete, and whose build is bound to a period toolchain
(32-bit; OpenSSL ≤ 1.0.2; wxWidgets 2.8) — see `derivatives/build-reconstruction/` in the
**genesis** repo.
