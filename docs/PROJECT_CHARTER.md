# Project Charter

## Research question

What functionality was demonstrably present, reachable, enforceable, and usable in the November 2008 and January 2009 Bitcoin codebases before later Bitcoin descendants selected, disabled, modified, restored, or extended different parts of the system?

## Core method

1. Freeze provenance before modifying code.
2. Keep canonical bytes immutable and outside derivative trees.
3. Distinguish source declaration from executable behavior.
4. Require transaction/block witnesses for consensus claims.
5. Compare descendants only after the original profiles are frozen.
6. Report negative and ambiguous findings without forcing a preferred conclusion.

## Two profiles

### OBL-NOV08 — Pre-Genesis

The November 2008 archive is treated as an early source witness, not presumed to be a complete standalone release. The project must determine its completeness, buildability, internal rules, and differences from January 2009.

### OBL-JAN09 — Genesis

The January 2009 v0.1.0 archive is treated as the first publicly released operational Bitcoin implementation. It is the principal historical execution oracle for the project.

## Evidence ladder

A claimed feature progresses through these levels:

1. **Declared** — identifier or structure appears in source.
2. **Implemented** — executable code path exists.
3. **Reachable** — ordinary parsing or validation can reach it.
4. **Consensus-relevant** — its result can affect transaction or block validity.
5. **Executed** — a controlled witness invokes it successfully.
6. **Mined** — an accepted block contains a transaction depending on it.
7. **Wallet-exposed** — original software could construct/use it without code modification.

No feature is described as native consensus functionality merely because its name appears in source.

## Authority order

1. Canonical archive bytes and locally verified hashes.
2. Bitcoin whitepaper and contemporaneous release records.
3. Executed behavior of the canonical implementation.
4. Satoshi-era releases, corrections, and clarifications.
5. Early-chain execution evidence.
6. Later commentary and descendant documentation.

## Integrity boundary

- `artifacts/` contains acquired historical bytes and is never edited.
- `derivatives/` contains every patch, port, harness, UI, test node, or experimental chain.
- A derivative must never be described as canonical original code.

## Initial success criterion

Release 0 succeeds when another researcher can independently acquire the same artifacts, verify all published hashes, reproduce the repository manifests, and understand exactly which evidence is original and which is derivative.
