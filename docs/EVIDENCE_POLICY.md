# Evidence Policy

## Claims must be scoped

Use one of these prefixes in reports:

- `NOV08-SOURCE:` visible in the November source witness.
- `JAN09-SOURCE:` visible in the January source release.
- `JAN09-EXECUTED:` reproduced with the historical implementation.
- `MODEL:` demonstrated only in a reimplementation or harness.
- `DERIVATIVE:` introduced by this project.
- `DESCENDANT:` observed in a later Bitcoin implementation.
- `UNRESOLVED:` evidence is incomplete or contradictory.

## Required evidence for an opcode claim

- byte value and declaration;
- evaluator implementation;
- reachability from transaction validation;
- positive and negative script vectors;
- transaction-context behavior where relevant;
- accepted/rejected block witness if consensus-relevant.

## Required evidence for a financial construction

- economic assumptions;
- transaction graph;
- exact scripts and signature commitments;
- raw serialized transactions;
- execution trace;
- resulting UTXO state;
- failure paths and security limitations;
- explicit distinction between native rule and external coordination.
