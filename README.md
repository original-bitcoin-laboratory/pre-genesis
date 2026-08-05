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

## What the November source shows

Read directly from the hash‑verified pre‑release (`inventory/`, and the cross‑edition
[`common/conformance/NOV08_JAN09_DIFF.md`](https://github.com/original-bitcoin-laboratory/common/blob/main/conformance/NOV08_JAN09_DIFF.md)):

- **A different monetary constitution.** `COIN` = 1e6, `CENT` = 1e4 — **no "satoshi"**
  (the 1e8 unit is *genesis*‑born); a **100‑coin** subsidy halving every 100k blocks, a
  15‑minute target, a fixed `1*CENT` fee, and an **exact‑equality** coinbase rule.
- **A different proof‑of‑work.** `nBits` is the required **leading‑zero‑bit count**
  (`MINPROOFOFWORK = 20`, *"ridiculously easy for testing"*) with a primitive ±1‑bit
  retarget — *not* v0.1.0's compact target + proportional retarget.
- **A 5‑file partial witness** — the ledger + networking main loop only; Script, keys,
  db, and the marketplace all first appear in January.

November's constitution is **executed** as a live counterfactual network, **NOV08‑X**
([`genesis/derivatives/nov08x/`](https://github.com/original-bitcoin-laboratory/genesis/tree/main/derivatives/nov08x/)), under strict per‑line
provenance ([`common/nov08x/DESIGN_LEDGER.md`](https://github.com/original-bitcoin-laboratory/common/blob/main/nov08x/DESIGN_LEDGER.md)). This
is **not** recovered runnable Bitcoin — the surviving package cannot build standalone;
NOV08‑X is a provenance‑controlled *completion*, never presented as recovered code.

**It now runs as a live, joinable network.** A public NOV08‑X anchor is online — clone the `genesis`
repo and `python -m netnode --chain nov08x --datadir ./data --connect seed.bitcoin-lab.org:18008` to
sync and independently re‑validate its leading‑zero‑bits chain yourself. Experimental, **not money** — no value is assigned;
full invitation in [`genesis/docs/ANNOUNCE.md`](https://github.com/original-bitcoin-laboratory/genesis/blob/main/docs/ANNOUNCE.md).

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
- The program-wide roadmap lives in the lab umbrella (`common/ROADMAP.md`);
  see `docs/PROJECT_CHARTER.md` for method and evidence rules.

## License

MIT © 2026 parthod0x (new laboratory material only). Original Bitcoin
source retains Satoshi Nakamoto's original notices. See `LICENSE` for the named copyright holder.

---

**Rights, sourcing and corrections:** see [RIGHTS.md](RIGHTS.md) — what this project uses,
where it comes from, how named people are treated, and how to ask for a correction.
