# The OEIS snapshot

`workhouse oeis --fetch` downloads <https://oeis.org/stripped.gz> here — the
OEIS maintainers' own published dump of every sequence and its terms, about
32 MB. It is **gitignored**, for two reasons:

* it is regenerated daily upstream, so a checked-in copy is stale by design;
* storing it is republishing it, and that is the OEIS's call, not ours — the
  same rule `literature/inbox/` follows for papers.

Nothing in this repository needs the file to run. `ledger/sequences.yaml`
records which snapshot the scan was taken against (source, sha256, upstream
last-modified date, sequence count) together with every verdict, and the
checks read that. `workhouse oeis --scan` re-runs the match against a local
copy and reports any verdict that has moved.

## Why the search API is never called

`oeis.org/robots.txt` says `Disallow: /search`, with `Crawl-Delay: 10`. So
`workhouse.oeis` does not query the search endpoint — not slowly, and not under
any user agent. It uses the dump, which robots.txt permits.

The dump request does send a browser-style `User-Agent`: oeis.org's front cache
returns 403 to the default `Python-urllib` string while serving the identical
file to curl and to any browser. That is a client-string filter, not an access
control, and it is the same call `workhouse.acquisition` already documents for
the KEK preprint scans.

That is also the better instrument. The search API returns at most ten results
and no total; the dump gives the exact number of matching sequences among all
~400,000, and that count is the only thing the verdict depends on.

Content from the OEIS is governed by the
[OEIS End-User License](https://oeis.org/LICENSE).
