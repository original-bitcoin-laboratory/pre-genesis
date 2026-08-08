# The whitepaper is identified here, not stored here

**`bitcoin-whitepaper.pdf` was removed from this directory on 8 August 2026.** Its identity is
preserved in full; only the copy is gone.

```
CANONICAL WHITEPAPER, 24 March 2009
  sha256  b1674191a88ec5cdd733e4240a81803105dc412d6c6708d53ab94fc248f4f553
  md5     d56d71ecadf2137be09d8b1d35c6c042
  bytes   184,292        pages 9
```

**Why.** The whitepaper carries no licence and no copyright notice. It is not public domain and not
MIT — copyright subsists automatically and vests in an author who has never been identified. This
project's own rule is that **a SHA-256 is not a reproduction**: we publish facts about documents and
point at sources others published. Serving an unlicensed copy while saying that was the weaker
position.

**Nothing is lost.** The canonical file is embedded in the block chain, where it cannot be revoked:

```bash
python verify/whitepaper_from_chain.py out.pdf    # carves it out of block 230009
sha256sum out.pdf                                 # must equal b1674191…f4f553
```

**That is a better source than this directory ever was** — it needs no website, no host, and no trust
in us.

See [`docs/WHITEPAPER.md`](https://github.com/original-bitcoin-laboratory/genesis/blob/main/docs/WHITEPAPER.md) for every known version by hash, and
[bitcoinwhitepaper.online](https://bitcoinwhitepaper.online) for the full record.
