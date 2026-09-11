# Archive derivation validation receipts

The start/end JSON files retain the exact briefing bytes and source-manifest
identities. The end briefing and generated views reused byte-matched checks;
verify-all.json is the separate fresh 645/645 execution receipt. pytest-full.log
records the completed full regression run. validation.json records its observed
exit code and counts its progress marks. No Lean compilation is claimed.

integration-preservation.json proves all then-current main ledger records remain
unchanged and compares all eleven retained source copies to their originals.
graph-counts.json identifies the 31 added derivations and ten result groups.
The why logs demonstrate graph retrieval of the two targeted-search results.

The diff check applies to maintained edits, recognizes preserved CRLF endings,
and excludes verbatim source and first-pass files whose original whitespace is
part of their byte identity. It does not silently rewrite historical evidence.
SHA256SUMS pins every receipt in this directory except itself.
