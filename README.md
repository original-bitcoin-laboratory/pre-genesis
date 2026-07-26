# Original Bitcoin Laboratory — Pre-Genesis (`OBL-NOV08`)

Self-contained reconstruction of the **November 15, 2008** Bitcoin pre-release
source witness — the earliest surviving Bitcoin code, predating the launched
network. One of the two editions of the Original Bitcoin Laboratory (the other is
the sibling `genesis` repo, Bitcoin v0.1.0).

> **Status caveat.** The November archive is a *pre-release source witness*. Its
> completeness and standalone buildability are **unproven** — establishing them is
> precisely this repo's job. See `profiles/nov08/PROFILE.md`.

## Quick start

```bash
./scripts/fetch-artifacts.sh          # pull the 2 canonical nov08 archives (Nakamoto Institute CDN)
python scripts/verify-artifacts.py    # hash-check against manifests/EXPECTED_CHECKSUMS.json
```

Archives land in `artifacts/nov08/` (gitignored) and are never edited. Verified
values: MD5/SHA-1 per the Satoshi Nakamoto Institute catalogue.

## Layout

```text
docs/         charter, evidence policy, status
provenance/   whitepaper + provenance sources
manifests/    expected checksums + generated manifests
profiles/     frozen OBL-NOV08 profile
scripts/      acquisition / verification / inventory tooling
artifacts/    acquired archive bytes (gitignored)
derivatives/  all modified / instrumented / modernized code
```

## Boundaries

- `artifacts/` holds acquired historical bytes and is never edited.
- `derivatives/` holds every patch, port, harness, UI, or experiment; a
  derivative is never described as canonical original code.
- The program-wide roadmap lives in the lab umbrella (`../common/ROADMAP.md`);
  see `docs/PROJECT_CHARTER.md` for method and evidence rules.

## License

MIT © 2026 Parth Mauria Saxena (new laboratory material only). Original Bitcoin
source retains Satoshi Nakamoto's original notices. See `LICENSE`.
