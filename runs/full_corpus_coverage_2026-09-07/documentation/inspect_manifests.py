"""Read existing manifests and the parent's census; write this audit's evidence only."""
from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path('C:/WORKHOUSE')
REPO = ROOT / 'WORKHOUSE-autonomous-20260905'
OUT = REPO / 'outputs/corpus_coverage_20260907/documentation'
census = [json.loads(line) for line in (OUT.parent / 'snapshot_before/files.jsonl').read_text(encoding='utf-8').splitlines()]
by_hash = defaultdict(list)
for row in census:
    by_hash[row['sha256'].lower()].append(row['path'])
archive_by_hash = defaultdict(list)
archive_rows = 0
for line in (OUT.parent / 'archives/members.jsonl').read_text(encoding='utf-8').splitlines():
    row = json.loads(line)
    archive_rows += 1
    if row.get('sha256'):
        archive_by_hash[row['sha256'].lower()].append({key: row.get(key) for key in (
            'containerpath', 'container_sha256', 'nestedancestor', 'ancestor_sha256',
            'memberpath', 'member_index', 'size')})

result = {'scope': 'Bounded documentary audit, not a semantic review of every census file', 'census_rows': len(census), 'archive_member_rows': archive_rows}
manifests = {}
for relative, delimiter in [
    ('corpus/GLUEBALL_CANONICAL_SOURCE_MANIFEST_2026-08-20_v4_3.csv', ','),
    ('records/MAN_GOV_all_theory_local_path_index_v4_3.csv', ','),
    ('export/MAN_GOV_export_manifest.csv', ','),
    ('records/REORG_MANIFEST_2026-08-20.tsv', '\t'),
]:
    with (ROOT / 'ALL THEORY' / relative).open(encoding='utf-8-sig', newline='') as stream:
        reader = csv.DictReader(stream, delimiter=delimiter)
        rows = list(reader)
        summary = {'rows': len(rows), 'fields': reader.fieldnames}
    if rows and 'status' in rows[0]:
        summary['historical_status_counts'] = dict(Counter(r['status'] for r in rows))
    if rows and 'sha256' in rows[0]:
        summary['sha256_present_in_current_census'] = sum(r['sha256'].lower() in by_hash for r in rows)
        summary['sha256_not_found_in_current_census'] = [
            {'id': r.get('id'), 'source_path': r.get('source_path', r.get('original_path', r.get('file'))), 'sha256': r['sha256'], 'historical_status': r.get('status')}
            for r in rows if r['sha256'].lower() not in by_hash
        ]
        summary['sha256_present_in_disk_or_archive'] = sum(
            r['sha256'].lower() in by_hash or r['sha256'].lower() in archive_by_hash for r in rows)
        summary['recovered_only_in_archive'] = [
            {'id': r.get('id'), 'sha256': r['sha256'],
             'source_path': r.get('source_path', r.get('original_path', r.get('file'))),
             'archive_matches': archive_by_hash[r['sha256'].lower()]}
            for r in rows if r['sha256'].lower() not in by_hash and r['sha256'].lower() in archive_by_hash
        ]
        summary['sha256_unresolved_after_disk_and_archive_join'] = [
            {'id': r.get('id'), 'sha256': r['sha256'],
             'source_path': r.get('source_path', r.get('original_path', r.get('file'))),
             'historical_status': r.get('status')}
            for r in rows if r['sha256'].lower() not in by_hash and r['sha256'].lower() not in archive_by_hash
        ]
        if 'status' in rows[0]:
            summary['historically_missing_now_found_by_hash'] = [
                {'id': r.get('id'), 'sha256': r['sha256'], 'current_matches': by_hash[r['sha256'].lower()]}
                for r in rows if r['status'] == 'missing' and r['sha256'].lower() in by_hash
            ]
            summary['historically_missing_recovered_disk_or_archive'] = [
                {'id': r.get('id'), 'sha256': r['sha256'],
                 'current_matches': by_hash.get(r['sha256'].lower(), []),
                 'archive_matches': archive_by_hash.get(r['sha256'].lower(), [])}
                for r in rows if r['status'] == 'missing' and
                (r['sha256'].lower() in by_hash or r['sha256'].lower() in archive_by_hash)
            ]
    manifests[relative] = summary
result['manifests'] = manifests

cross = []
for number, line in enumerate((ROOT / 'CROSS_REFERENCE.md').read_text(encoding='utf-8').splitlines(), 1):
    cells = [c.strip() for c in line.split('|')]
    if len(cells) >= 4 and cells[1].startswith('ORGANIZED/'):
        mapped = cells[1].removeprefix('ORGANIZED/')
        cross.append({'line': number, 'copy': cells[1], 'source': cells[2], 'current_root_copy_exists': (ROOT / mapped).is_file(), 'literal_organized_path_exists': (ROOT / cells[1]).is_file()})
result['cross_reference'] = {'declared_rows': 195, 'actual_rows': len(cross), 'current_root_copy_matches_after_prefix_strip': sum(r['current_root_copy_exists'] for r in cross), 'literal_organized_path_matches': sum(r['literal_organized_path_exists'] for r in cross), 'fields': ['organized_path', 'original_path'], 'no_hash_or_review_fields': True}

result['review_ledger_warning'] = 'Ledger introduction explicitly records truncation, reconstructed descriptions, unknown units 38-44 and three unrecovered SKIP identities. Counts are historical, not comprehensive current review coverage.'

candidates = []
for row in census:
    path = row['path'].replace('\\', '/')
    if path.startswith('10_ALREADY_REVIEWED/') and ' - Copy.' in path and Path(path).suffix.lower() in {'.md', '.tex', '.pdf'}:
        retained = path.replace(' - Copy.', '.')
        matches = [p.replace('\\', '/') for p in by_hash[row['sha256'].lower()]]
        if retained in matches:
            checked = ['CROSS_REFERENCE.md', 'README.md', 'GAP_ANALYSIS.md', '10_ALREADY_REVIEWED/MANIFEST.md']
            refs = [p for p in checked if Path(path).name in (ROOT / p).read_text(encoding='utf-8')]
            candidates.append({'candidate': path, 'retained_exact_copy': retained, 'sha256': row['sha256'], 'size': row['size'], 'reason': 'Same bytes as same-folder non-Copy edition. Redundant physical copy only; mathematical content is not declared useless.', 'bounded_reference_files_checked': checked, 'exact_basename_references_found': refs, 'reference_check': 'Full reference and authoritative-copy validation remains parent-owned; not authorized by this audit for movement.'})
result['conditional_loose_duplicate_candidates'] = candidates[:5]
result['candidate_count_matching_this_narrow_rule'] = len(candidates)
OUT.mkdir(parents=True, exist_ok=True)
(OUT / 'MANIFEST_EVIDENCE.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
print(json.dumps({'census_rows': len(census), 'archive_rows': archive_rows,
 'manifests': {k: {f: (len(v) if isinstance(v, list) and f != 'fields' else v) for f,v in s.items()} for k,s in manifests.items()}}, ensure_ascii=False, indent=2))
