# OBL-NOV08 — Function catalog (R1)

Line-numbered functions in the November 2008 pre-release (`main.cpp`, `node.cpp`),
read from the extracted, hash-verified source. Evidence prefix: **NOV08-SOURCE**.

## `main.cpp` — free functions

| Line | Function | Area |
|--:|---|---|
| 75 | `AddKey` | wallet keys |
| 102 | `AddToWallet` | wallet |
| 151 | `AddToWalletIfMine` | wallet |
| 170 | `ReacceptWalletTransactions` | wallet |
| 185 | `RelayWalletTransactions` | wallet/relay |
| 652 | `GetBlockValue` | issuance (100-coin subsidy) |
| 660 | `GetNextWorkRequired` | difficulty (15-min target) |
| 708 | `GetOrphanRoot` | orphan handling |
| 778 | `Reorganize(CBlockIndex*, bool fWriteDisk)` | chain reorg |
| 911 | `ScanMessageStart` | wire framing |
| 951 / 971 | `OpenBlockFile` / `AppendBlockFile` | block storage |
| 992 | `LoadBlockIndex` | startup |
| 1094 | **`PrintTimechain`** | debug (see note) |
| 1258 | `ProcessBlock` | block ingress |
| 1328 | `AlreadyHave` | inv dedup |
| 1348 / 1423 | `ProcessMessages` / `ProcessMessage` | P2P dispatch |
| 1742 | `SendMessages` | P2P out |
| 1819 | `FormatHashBlocks` | mining hash prep |
| 1864 | `BitcoinMiner` | CPU miner |
| 2077 | **`CountMoney`** | wallet balance (see note) |
| 2095 | `SelectCoins` | coin selection |
| 2181 | `CreateTransaction` | tx build |
| 2246 | `SendMoney` | payment |

## `main.cpp` — `CTransaction` / `CBlock` methods

| Line | Method | Note vs JAN09 |
|--:|---|---|
| 354 | `CTransaction::DisconnectInputs(CTxDB&… )` → here `map<uint256,CTransaction>` | in-memory pool, **no `CTxDB`/`CTxIndex`** |
| 410 | `CTransaction::ConnectInputs(…, map<uint256,CTransaction>…)` | disk-index layer added only in JAN09 |
| 498 | `CTransaction::AcceptTransaction` | |
| 647 | `CBlock::ReadFromDisk` | |
| 724 / 732 | `CBlock::TestDisconnectBlock` / `TestConnectBlock` | later refactored |
| 744 / 753 | `CBlock::DisconnectBlock` / `ConnectBlock(nFile,nBlockPos,nHeight)` | JAN09 takes `(CTxDB&, CBlockIndex*)` |
| 853 | `CBlock::AddToBlockIndex(nFile,nBlockPos,fWriteDisk)` | contains the height-based chain-selection |
| 1161 | `CBlock::CheckBlock` | |
| 1196 | `CBlock::AcceptBlock` | |

## `node.cpp` — free functions

| Line | Function | Area |
|--:|---|---|
| 57 | `AddAddress` | peer address db |
| 88 | `AbandonRequests` | request tracking |
| 236 | `ThreadSocketHandler` | P2P sockets |
| 515 | `ThreadOpenConnections` | outbound peers |
| 650 | `ThreadMessageHandler` | message pump |
| 709 | `ThreadBitcoinMiner` | mining thread (lives in the networking unit) |
| 732 / 840 | `StartNode` / `StopNode` | lifecycle |
| 854 | `CheckForShutdown` | shutdown |

## Notes — pre-genesis vocabulary

- **`PrintTimechain`** (`main.cpp:1094`): Satoshi's term here is *timechain*; by
  January this debug routine is `PrintBlockTree`. The "timechain" wording is a
  pre-genesis artifact.
- **`CountMoney`** (`main.cpp:2077`): renamed `GetBalance` in January.
- `ConnectInputs`/`DisconnectInputs` operate over an in-memory
  `map<uint256, CTransaction>` — the November tree has **no `CTxDB` / `CTxIndex`**
  disk-index layer (that arrives with `db.*` and the two new `main.h` classes in
  January; see `../common/conformance/NOV08_JAN09_DIFF.md`).
