# Status — Pre-Genesis (`OBL-NOV08`)

## Release 0 — Provenance freeze

- [x] Self-contained edition repository created.
- [x] Charter, evidence policy, profile, and checksum registry in place.
- [x] Whitepaper captured under `provenance/`.
- [x] Canonical nov08 archives fetched (Nakamoto Institute CDN) and verified.
- [x] `.tgz` source tree extracted read-only + per-file manifest generated.
- [ ] `.rar` tree extracted and diffed against the `.tgz` tree (needs `unrar`/`7z`).

### Verified archives (2026-07-26)

| Artifact | md5 | sha1 |
|---|:--:|:--:|
| `bitcoin-nov08.rar` | OK | OK |
| `bitcoin-nov08.tgz` | OK | OK |

Whitepaper matches `manifests/PROVENANCE_SHA256SUMS`. Verified bytes live under
`artifacts/nov08/` (gitignored, never edited). Per-file hashes of the extracted
tree are recorded in `manifests/SOURCE_MANIFEST.json` (the source bytes themselves
stay local under `extracted/`).

## First finding — source inventory

The November 2008 pre-release tree is **5 files**:

```
main.cpp    66174
main.h      29219
node.cpp    28112
node.h      18491
readme.txt    451
```

No `script.*`, `key.*`, `db.*`, `net.*`, `ui.*`, or `market.*`. Networking lives in
`node.*` (renamed/expanded to `net.*` by January). This is the earliest surviving
architectural witness — core validation + networking only — and on its face is
**not** a complete standalone release. (Contrast: the JAN09 edition ships 21 source
files plus a runnable `bitcoin.exe`.)

## Next

`v0.1.0-source-inventory`: line-numbered class/function enumeration and a formal
NOV08 → JAN09 structural diff.
