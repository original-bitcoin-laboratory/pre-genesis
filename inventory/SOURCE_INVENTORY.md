# OBL-NOV08 — Source inventory (`v0.1.0-source-inventory`, R1)

Structural map of the November 15, 2008 Bitcoin pre-release. Line counts and
symbol names are read directly from the extracted, hash-verified source
(`manifests/SOURCE_MANIFEST.json`).

Evidence prefix: **NOV08-SOURCE** (visible in the November pre-release witness).

## The whole tree — 4 source units + readme (5,005 lines)

| File | lines | Key classes | Role |
|---|--:|---|---|
| `main.h` | 1136 | COutPoint, CInPoint, CDiskTxPos, CCoinBase, CTxIn, CTxOut, CTransaction, CMerkleTx, CWalletTx, CBlock, CBlockIndex, CBlockLocator | transactions, blocks, chain state, wallet (declarations) |
| `main.cpp` | 2261 | — | validation, mining, chain, wallet (impl) |
| `node.h` | 746 | CMessageHeader, CAddress, CInv, CRequestTracker, CNode | P2P messages, peers |
| `node.cpp` | 862 | — | P2P transport (later renamed `net.*`) |
| `readme.txt` | — | — | pre-release note |

## Key finding — the pre-release is a *partial* snapshot

The archive references the Script machinery but **does not contain it**:

- **No `opcodetype` enum, no `class CScript`, no `EvalScript`, no `SIGHASH`**
  definitions anywhere in the four files (verified: zero matches).
- `main.cpp` nonetheless *uses* `CScript() << OP_CODESEPARATOR << <pubkey> <<
  OP_CHECKSIG` in 5 places — so those symbols were defined in a **script module
  that is absent from the preserved pre-release**.
- Only **two** opcodes are referenced at all: `OP_CHECKSIG` and
  `OP_CODESEPARATOR` (the bare pay-to-pubkey pattern).

Likewise absent (all first appear in the January v0.1.0 tree): `key.*`, `db.*`,
`market.*`, `irc.*`, `sha.*`, `ui.*`/`uibase.*`, `base58.h`, `bignum.h`,
`serialize.h`, `uint256.h`, `util.*`.

**Conclusion (NOV08-SOURCE):** on the preserved bytes alone, the November archive
is an early *architectural witness* of the ledger + networking layer, **not a
complete, standalone-buildable Bitcoin**. This matches the profile's stated
caveat and is the cleanest available evidence for it.

## Relationship to January

The nov08 → jan09 structural diff (file renames, class additions, and the
externalised Script module) is recorded in the lab umbrella:
`../common/conformance/NOV08_JAN09_DIFF.md`.
