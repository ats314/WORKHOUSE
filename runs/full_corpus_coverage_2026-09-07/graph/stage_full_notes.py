"""Stage a complete content-addressed notes manifest, never edit canonical data."""
from __future__ import annotations

import collections
import hashlib
import json
import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[3]
BASE = REPO / 'outputs/corpus_coverage_20260907'
STAGE = BASE / 'graph/staged_notes'
ARCHIVE = 'WORKHOUSE_FULL_2026-09-07'
sys.path.insert(0, str(REPO / 'src'))
from workhouse import notes, triage  # noqa: E402


def read(path):
    return [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(name, value):
    (STAGE / name).write_text(json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + '\n', encoding='utf-8', newline='\n')


def main():
    STAGE.mkdir(parents=True, exist_ok=True)
    eligible = read(BASE / 'graph/eligible_registration_join.jsonl')
    old = read(BASE / 'graph/archive_review_join.jsonl')
    old_hashes = collections.defaultdict(list)
    for row in old:
        old_hashes[row['digest']].append(row)
    member_rows = read(BASE / 'archives/members.jsonl')
    members = collections.defaultdict(list)
    for row in member_rows:
        if row.get('kind') == 'file' and row.get('sha256'):
            members[row['sha256']].append(row)
    objects = json.loads((BASE / 'archives/archive_only_content.json').read_text(encoding='utf-8'))
    archive_classes = {r['sha256']: r for r in read(BASE / 'archives/archive_extraction/classifications_complete.jsonl')}
    roles = {r['sha256']: r for r in read(BASE / 'archives/content_roles.jsonl')}
    quarantine_path = REPO.parent / 'quarantine/2026-09-07-exact-duplicates/MANIFEST.json'
    quarantine = json.loads(quarantine_path.read_text(encoding='utf-8'))
    moved = {row['original_path']: row for row in quarantine['moves']}
    extractions = {}
    for root in [BASE / 'extraction', BASE / 'archives/archive_extraction']:
        filename = 'content_complete.jsonl' if root.name == 'archive_extraction' else 'content_final.jsonl'
        for row in read(root / filename):
            extractions[row['sha256']] = {'record': row, 'root': root}
    by_hash = {row['sha256']: row for row in eligible}
    excluded_objects = []
    for row in objects:
        classification = archive_classes.get(row['sha256'])
        if classification and classification.get('exclusion'):
            excluded_objects.append({'sha256': row['sha256'], 'exclusion': classification['exclusion'], 'materialized_object': row['materialized_object']})
            continue
        by_hash.setdefault(row['sha256'], {'sha256': row['sha256'], 'size': row['size'], 'paths': [], 'eligible_paths': [], 'registrations': [], 'recovered_object': row['materialized_object']})
    records = []
    extraction_counts = collections.Counter()
    for digest, row in sorted(by_hash.items()):
        prior = old_hashes[digest]
        locators = []
        for member in members[digest]:
            locators.append({k: member[k] for k in ['containerpath', 'container_sha256', 'nestedancestor', 'ancestor_sha256', 'memberpath', 'member_index', 'unsafe_extraction_path'] if k in member})
        paths = list(row['eligible_paths'])
        relocations = []
        current_loose_paths = []
        for path in row['eligible_paths']:
            if path in moved:
                move = moved[path]
                if move['sha256'] != digest:
                    raise ValueError(f'Quarantine mismatch for {path}')
                for name in ['quarantine_path', 'retained_path']:
                    if sha(REPO.parent / move[name]) != digest:
                        raise ValueError(f'Quarantine current bytes mismatch for {path}')
                    paths.append(move[name])
                    current_loose_paths.append(move[name])
                relocations.append(move)
            else:
                current_loose_paths.append(path)
        for loc in locators:
            path = '!/'.join([loc['containerpath'], *loc.get('nestedancestor', []), loc['memberpath']])
            paths.append('ARCHIVE_MEMBER/' + path)
        paths = sorted(set(paths))
        if not paths:
            raise ValueError(f'No source locator for {digest}')
        ext = extractions.get(digest)
        extraction = dict(ext['record']) if ext else {'extraction': 'not-yet-extracted', 'review': 'pending'}
        for key in ['paths', 'representative', 'sha256', 'size', 'review']:
            extraction.pop(key, None)
        if ext and extraction.get('text_file'):
            extraction['text_file'] = str((ext['root'] / extraction['text_file']).relative_to(REPO)).replace('\\', '/')
        extraction_counts[extraction['extraction']] += 1
        # Coefficient scanning uses the existing exact triage vocabulary. It is
        # not a review; PDF/DOCX text extraction retains its separate method.
        scanned = False
        coefficients = []
        has_erratum = False
        if extraction.get('text_file'):
            text_path = REPO / extraction['text_file']
            if text_path.stat().st_size <= triage.MAX_SCAN_BYTES:
                text = text_path.read_text(encoding='utf-8')
                scanned = True
                digits = re.sub(r'[^\d]', '', text)
                coefficients = [label for label, alternatives in triage.SIGNATURES.items() if any(all(part in digits for part in alt) for alt in alternatives)]
                has_erratum = any(pattern.search(text) for pattern in triage.ERRATUM_PATTERNS)
        date = triage.DATE_IN_NAME.search(Path(paths[0]).name)
        registered_paths = sorted({r['path'] for r in row['registrations'] if r.get('path') and (REPO / re.sub(r':\d+$', '', r['path'])).is_file()})
        prior_review_refs = [{'archive': previous['archive'], **review} for previous in prior for review in previous['reviews']]
        record = {'digest': digest, 'paths': paths, 'size': row['size'], 'scanned': scanned, 'coefficients': coefficients, 'has_erratum': has_erratum, 'superseded_hint': bool(triage.SUPERSEDED_HINTS.search(triage._normalise_name(Path(paths[0]).name))), 'date_hint': '-'.join(date.groups()) if date else None, 'pinned_as': registered_paths[0] if registered_paths else None, 'extraction': extraction, 'provenance': {'loose_paths': row['eligible_paths'], 'current_loose_paths': sorted(set(current_loose_paths)), 'exact_duplicate_relocations': relocations, 'archive_members': locators, 'existing_registration': row['registrations'], 'prior_inventory_archives': sorted({r['archive'] for r in prior}), 'prior_review_refs': prior_review_refs, 'review_transfer': 'none; prior verdicts remain attached to their original archive and scope', 'signal_scanner': 'Existing workhouse.triage coefficient and erratum patterns applied to successfully extracted text up to MAX_SCAN_BYTES; not mathematical reading'}}
        if digest in roles:
            record['provenance']['content_role'] = roles[digest]
        if row.get('recovered_object'):
            record['provenance']['recovered_object'] = 'outputs/corpus_coverage_20260907/archives/' + row['recovered_object']
        records.append(record)
    records.sort(key=lambda r: r['paths'][0])
    target = STAGE / f'{ARCHIVE}.jsonl'
    with target.open('w', encoding='utf-8', newline='\n') as stream:
        for record in records:
            stream.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + '\n')
    archive = {'id': ARCHIVE, 'description': 'Full C:/WORKHOUSE content-hash inventory of eligible loose research files and recursively audited archive members as of 2026-09-07. Includes registered exact-byte copies with pinned_as/provenance; no filename, extraction, capture or duplicate-count inference promotes mathematical claims. Existing review verdicts retain their original scope; new archive entries remain pending.', 'source': "Frozen census, exclusion, archive-member, extraction and quarantine metadata are pinned by runs/full_corpus_coverage_2026-09-07/COVERAGE_CONTRACT.json, with compressed source records under that run's inputs/ directory. See docs/corpus_coverage.md for scope and local full-text locators. Every eligible digest and container chain is retained; explicit runtime/generated/local-configuration exclusions remain recorded. Unsupported formats remain captured/pending. Text extraction and numeric scans are search metadata, not mathematical review or verbatim proof imports."}
    (STAGE / 'archive_declaration.yaml').write_text(yaml.safe_dump({'archives': [archive], 'reviews': []}, sort_keys=False, allow_unicode=True), encoding='utf-8', newline='\n')
    existing = notes.load()
    staged = notes.Notes(archives=[*existing.archives, archive], reviews=existing.reviews, manifests={**existing.manifests, ARCHIVE: records})
    validation = notes.validate(staged, REPO)
    if validation:
        raise ValueError(validation)
    required = {'digest', 'paths', 'size', 'scanned', 'coefficients', 'has_erratum', 'superseded_hint', 'date_hint', 'pinned_as'}
    assert len({r['digest'] for r in records}) == len(records)
    assert all(required <= r.keys() and notes._is_digest(r['digest']) and r['paths'] for r in records)
    assert len(staged.unreviewed(ARCHIVE)) == len(records)
    assert extraction_counts['not-yet-extracted'] == 0
    assert extraction_counts['error'] == 0
    input_paths = [BASE / 'snapshot_before/files.jsonl', BASE / 'extraction/classifications.jsonl', BASE / 'extraction/content_final.jsonl', BASE / 'archives/members.jsonl', BASE / 'archives/archive_only_content.json', BASE / 'archives/content_roles.jsonl', BASE / 'archives/archive_extraction/classifications_complete.jsonl', BASE / 'archives/archive_extraction/content_complete.jsonl', BASE / 'graph/eligible_registration_join.jsonl', BASE / 'graph/archive_review_join.jsonl', REPO / 'src/workhouse/notes.py', REPO / 'src/workhouse/triage.py']
    (STAGE / 'quarantine_locator_manifest.json').write_bytes(quarantine_path.read_bytes())
    input_paths.append(STAGE / 'quarantine_locator_manifest.json')
    write('STAGED_INVENTORY_REPORT.json', {'archive': ARCHIVE, 'canonical_applied': False, 'rows': len(records), 'loose_unique': len(eligible), 'member_only_included': len(records)-len(eligible), 'excluded_member_only': len(excluded_objects), 'records_with_existing_registered_path': sum(r['pinned_as'] is not None for r in records), 'records_with_prior_reviews': sum(bool(r['provenance']['prior_review_refs']) for r in records), 'new_verdicts': 0, 'pending': len(records), 'scanned_for_numeric_signatures': sum(r['scanned'] for r in records), 'extraction_counts': dict(extraction_counts), 'notes_validate_errors': validation, 'manifest_sha256': sha(target), 'manifest_bytes': target.stat().st_size, 'inputs': [{'path': str(p.relative_to(REPO)).replace('\\', '/'), 'sha256': sha(p)} for p in input_paths]})
    write('excluded_member_only.json', excluded_objects)
    print(json.dumps({'rows': len(records), 'member_only': len(records)-len(eligible), 'extraction': dict(extraction_counts), 'manifest': str(target), 'notes_validate': validation}, indent=2))


if __name__ == '__main__':
    main()
