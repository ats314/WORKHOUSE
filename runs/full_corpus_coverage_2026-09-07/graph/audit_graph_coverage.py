"""Read-only content-hash join of a frozen census to existing graph registers.

Outputs describe evidence registration, not mathematical truth or discardability.
No inference from a filename, shared component, or scan to acceptance is made.
"""
from __future__ import annotations

import collections
import hashlib
import json
import re
from pathlib import Path

import yaml

ROOT = Path('C:/WORKHOUSE')
REPO = ROOT / 'WORKHOUSE-autonomous-20260905'
OUT = Path(__file__).resolve().parent
CENSUS = OUT.parent / 'snapshot_before/files.jsonl'


def rows(path):
    return [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(name, value):
    (OUT / name).write_text(json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + '\n', encoding='utf-8', newline='\n')


def jsonl(name, values):
    with (OUT / name).open('w', encoding='utf-8', newline='\n') as stream:
        for value in values:
            stream.write(json.dumps(value, ensure_ascii=False, sort_keys=True) + '\n')


def main():
    census = rows(CENSUS)
    by_hash = collections.defaultdict(list)
    by_path = {row['path']: row for row in census}
    for row in census:
        by_hash[row['sha256']].append(row)
    claims = rows(REPO / 'index/claims.jsonl')
    edges = rows(REPO / 'index/graph.jsonl')
    nodes = {row['id']: row for row in claims}
    notes = yaml.safe_load((REPO / 'ledger/notes.yaml').read_text(encoding='utf-8'))
    aliases = yaml.safe_load((REPO / 'ledger/documents.yaml').read_text(encoding='utf-8'))['aliases']
    results = yaml.safe_load((REPO / 'ledger/results.yaml').read_text(encoding='utf-8'))['results']
    provenance = yaml.safe_load((REPO / 'ledger/provenance.yaml').read_text(encoding='utf-8'))['documents']
    runs = yaml.safe_load((REPO / 'runs/index.yaml').read_text(encoding='utf-8'))['runs']
    refs = collections.defaultdict(list)
    all_source_paths = collections.defaultdict(set)
    missing = []
    def pin(path, category, identifier):
        path = re.sub(r':\d+$', '', path)
        target = REPO / path
        if target.is_file():
            key = f'WORKHOUSE-autonomous-20260905/{path}'
            sha = by_path[key]['sha256'] if key in by_path else digest(target)
            item = {'category': category, 'id': identifier, 'path': path}
            if item not in refs[sha]:
                refs[sha].append(item)
            all_source_paths[sha].add(path)
            return sha
        missing.append({'category': category, 'id': identifier, 'path': path})
        return None
    for row in claims:
        if row['kind'] not in {'note', 'archive'} and row.get('where'):
            pin(row['where'], 'graph_file', row['id'])
    for alias in aliases:
        if alias.get('path'):
            pin(alias['path'], 'citation_alias', 'CITE:' + alias['alias'])
    alias_map = {alias['alias']: alias for alias in aliases}
    for result in results:
        source = alias_map.get(result['source'].removeprefix('CITE:'))
        if source and source.get('path'):
            pin(source['path'], 'analytic_result_source', result['id'])
    for doc in provenance:
        refs[doc['sha256']].append({'category': 'curated_origin', 'id': 'DOC:' + doc['id'], 'path': 'corpus-import/' + doc['path']})
    run_pin_problems = []
    for run in runs:
        directory = REPO / run['dir']
        sums = directory / 'SHA256SUMS'
        if not sums.is_file():
            continue
        for line in sums.read_text(encoding='utf-8').splitlines():
            match = re.fullmatch(r'([a-fA-F0-9]{64})\s+\*?(.*)', line)
            if not match:
                continue
            sha, relative = match.groups()
            relative = relative.replace('\\', '/')
            path = f"{run['dir']}/{relative}"
            census_row = by_path.get(f'WORKHOUSE-autonomous-20260905/{path}')
            if census_row and census_row['sha256'] != sha.lower():
                run_pin_problems.append({'run': run['id'], 'path': path, 'declared': sha.lower(), 'observed': census_row['sha256']})
                continue
            refs[sha.lower()].append({'category': 'sealed_run_member', 'id': 'RUN:' + run['id'], 'path': path, 'pin_manifest': run['dir'] + '/SHA256SUMS', 'census_path_match': census_row is not None})
        imported = directory / 'import_manifest.json'
        if imported.is_file():
            imp = json.loads(imported.read_text(encoding='utf-8'))
            if imp.get('source_zip_sha256'):
                refs[imp['source_zip_sha256']].append({'category': 'registered_import_container', 'id': 'RUN:' + run['id'], 'path': imp['source_zip_name'], 'manifest': run['dir'] + '/import_manifest.json', 'comparison': imp.get('comparison')})
    reviews = collections.defaultdict(list)
    for review in notes.get('reviews', []):
        reviews[(review['archive'], review['digest'])].append(review)
    note_nodes = [n for n in claims if n['kind'] == 'note']
    manifests, archives = [], []
    for archive in notes['archives']:
        aid = archive['id']
        inventory = rows(REPO / f'notes/{aid}.jsonl')
        counts = collections.Counter()
        for row in inventory:
            rr = reviews[(aid, row['digest'])]
            counts['reviewed' if rr else 'pending'] += 1
            counts['scanner_supported' if row['scanned'] else 'scanner_unsupported'] += 1
            for review in rr:
                counts['verdict_' + review['verdict']] += 1
            entry = {'archive': aid, **row, 'reviews': rr, 'live_census_paths': [c['path'] for c in by_hash.get(row['digest'], [])]}
            manifests.append(entry)
            refs[row['digest']].append({'category': 'archive_inventory', 'id': aid, 'paths': row['paths'], 'scanned': row['scanned']})
            for review in rr:
                refs[row['digest']].append({'category': 'recorded_review', 'id': aid, 'verdict': review['verdict'], 'reason': review['reason']})
        archives.append({'id': aid, 'unique_content_rows': len(inventory), 'original_path_count': sum(len(r['paths']) for r in inventory), 'present_in_census': sum(bool(by_hash.get(r['digest'])) for r in inventory), **dict(counts), 'description': archive.get('description'), 'source': archive.get('source')})
    joined, unmatched = [], []
    for sha, copies in sorted(by_hash.items()):
        registrations = refs.get(sha, [])
        categories = sorted({ref['category'] for ref in registrations})
        row = {'sha256': sha, 'size': copies[0]['size'], 'paths': [c['path'] for c in copies], 'tops': sorted({c['top'] for c in copies}), 'extensions': sorted({c['extension'] for c in copies}), 'registration_categories': categories, 'registrations': registrations}
        joined.append(row)
        if not registrations:
            unmatched.append(row)
    by_top = []
    for top in sorted({r['top'] for r in census}):
        local = [r for r in census if r['top'] == top]
        hashes = {r['sha256'] for r in local}
        categories = collections.Counter(cat for sha in hashes for cat in {x['category'] for x in refs.get(sha, [])})
        by_top.append({'top': top, 'files': len(local), 'unique_digests': len(hashes), 'registered_digests': sum(bool(refs.get(sha)) for sha in hashes), 'unrepresented_digests': sum(not refs.get(sha) for sha in hashes), **dict(categories)})
    # Exact typed neighborhoods; undirected connectivity is deliberately not an acceptance metric.
    adj = collections.defaultdict(list)
    for edge in edges:
        adj[edge['src']].append(edge)
        adj[edge['dst']].append(edge)
    focus = {}
    for target in ['C2', 'G3', 'G14', 'G18', 'G19', 'G23']:
        neighborhood = {edge['src'] if edge['dst'] == target else edge['dst'] for edge in adj[target]}
        focus[target] = {'claim': nodes.get(target), 'direct_edges': adj[target], 'neighbor_kinds': dict(collections.Counter(nodes.get(n, {}).get('kind', 'symbol_or_unresolved') for n in neighborhood)), 'routes': [n for n in claims if n['kind'] == 'route' and n['id'].startswith('ROUTE:' + target + ':')]}
    note_connections = []
    for node in note_nodes:
        substantive = [e for e in adj[node['id']] if e['type'] not in {'contains', 'labels'}]
        if substantive:
            note_connections.append({'id': node['id'], 'status': node['status'], 'where': node['where'], 'edges': substantive})
    inputs = ['index/claims.jsonl', 'index/graph.jsonl', 'index/symbols.jsonl', 'ledger/notes.yaml', 'ledger/documents.yaml', 'ledger/results.yaml', 'ledger/provenance.yaml', 'ledger/gaps.yaml', 'ledger/contradictions.yaml']
    inputs += sorted(str(path.relative_to(REPO)).replace('\\', '/') for path in (REPO / 'notes').glob('*.jsonl'))
    write('INPUTS.json', {'census': {'path': str(CENSUS), 'sha256': digest(CENSUS)}, 'repository_inputs': [{'path': p, 'sha256': digest(REPO / p)} for p in inputs]})
    write('graph_summary.json', {'scope': 'Existing recorded registration and exact-byte census join; no new mathematical adjudication, no inferred equivalence for rewritten files, no archive extraction.', 'census_files': len(census), 'census_unique_digests': len(by_hash), 'claims': len(claims), 'kind_counts': dict(collections.Counter(n['kind'] for n in claims)), 'edge_count': len(edges), 'edge_types': dict(collections.Counter(e['type'] for e in edges)), 'alias_count': len(aliases), 'alias_standing': dict(collections.Counter(a.get('standing', 'unresolved') for a in aliases)), 'alias_ids_missing_from_graph': sorted('CITE:' + a['alias'] for a in aliases if 'CITE:' + a['alias'] not in nodes), 'result_count': len(results), 'result_status_evidence': dict(collections.Counter(str((r['status'], r['evidence'])) for r in results)), 'curated_origin_count': len(provenance), 'review_count': sum(len(v) for v in reviews.values()), 'review_verdicts': dict(collections.Counter(r['verdict'] for rr in reviews.values() for r in rr)), 'inventory_unique_digest_count': len({m['digest'] for m in manifests}), 'inventory_rows': len(manifests), 'inventory_pending_rows': sum(not m['reviews'] for m in manifests), 'inventory_missing_live_digest_rows': sum(not m['live_census_paths'] for m in manifests), 'notes_with_noncontainment_edges': len(note_connections), 'registered_census_digests': len(joined) - len(unmatched), 'unrepresented_census_digests': len(unmatched), 'by_top': by_top, 'missing_graph_file_locators': missing})
    write('archive_coverage.json', archives)
    write('focus_graph.json', focus)
    write('note_graph_connections.json', note_connections)
    write('run_pin_comparison.json', {'registered_runs': len(runs), 'mismatched_census_bytes': run_pin_problems, 'boundary': 'Explicit registered-run SHA256SUMS and import_manifest container pins, not every hash-shaped string in metadata; no replay performed by this audit.'})
    jsonl('census_registration_join.jsonl', joined)
    jsonl('unrepresented_contents.jsonl', unmatched)
    jsonl('archive_review_join.jsonl', manifests)
    jsonl('registered_external_copies.jsonl', ({'sha256': r['sha256'], 'paths': [p for p in r['paths'] if not p.startswith('WORKHOUSE-autonomous-20260905/')], 'registrations': r['registrations']} for r in joined if r['registrations'] and any(not p.startswith('WORKHOUSE-autonomous-20260905/') for p in r['paths'])))
    classifications = OUT.parent / 'extraction/classifications.jsonl'
    if classifications.exists():
        classified = rows(classifications)
        eligible = {row['path'] for row in classified if row['exclusion'] is None}
        eligible_join = [{**row, 'eligible_paths': [p for p in row['paths'] if p in eligible]} for row in joined if any(p in eligible for p in row['paths'])]
        jsonl('eligible_registration_join.jsonl', eligible_join)
        jsonl('eligible_unrepresented_contents.jsonl', (r for r in eligible_join if not r['registrations']))
        write('eligible_summary.json', {'classification_sha256': digest(classifications), 'eligible_paths': len(eligible), 'eligible_unique_digests': len(eligible_join), 'represented_digests': sum(bool(r['registrations']) for r in eligible_join), 'unrepresented_digests': sum(not r['registrations'] for r in eligible_join), 'exclusions': dict(collections.Counter(str(r['exclusion']) for r in classified)), 'by_top': [{'top': top, 'unique_digests': len(local := [r for r in eligible_join if any(p.split('/')[0] == top for p in r['eligible_paths'])]), 'represented_digests': sum(bool(r['registrations']) for r in local), 'unrepresented_digests': sum(not r['registrations'] for r in local)} for top in sorted({p.split('/')[0] for p in eligible})]})
    research_topics = []
    for topic in sorted({m['paths'][0].split('/')[0] for m in manifests if m['archive'] == 'RESEARCH_2026-08'}):
        group = [m for m in manifests if m['archive'] == 'RESEARCH_2026-08' and m['paths'][0].split('/')[0] == topic]
        research_topics.append({'topic': topic, 'inventory_rows': len(group), 'reviewed_rows': sum(bool(m['reviews']) for m in group), 'pending_rows': sum(not m['reviews'] for m in group), 'live_census_hashes': sum(bool(m['live_census_paths']) for m in group)})
    write('research_topic_coverage.json', research_topics)
    print(json.dumps({'census_files': len(census), 'unique': len(by_hash), 'represented': len(joined)-len(unmatched), 'unrepresented': len(unmatched), 'archive_rows': len(manifests), 'pending': sum(not m['reviews'] for m in manifests), 'aliases': len(aliases), 'results': len(results), 'note_graph_connections': len(note_connections)}, indent=2))


if __name__ == '__main__':
    main()
