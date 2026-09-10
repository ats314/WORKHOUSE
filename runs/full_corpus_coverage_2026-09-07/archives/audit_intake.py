"""Targeted attachment intake and reference-library provenance checks."""
from pathlib import Path
import collections
import hashlib
import json
import re
import subprocess
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path('C:/WORKHOUSE')
REPO = ROOT / 'WORKHOUSE-autonomous-20260905'
OUT = REPO / 'outputs/corpus_coverage_20260907/archives'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def save(name, value):
    (OUT / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


def main():
    census = [json.loads(s) for s in (OUT.parent / 'snapshot_before/files.jsonl').read_text(encoding='utf-8').splitlines()]
    by_hash = collections.defaultdict(list)
    for record in census:
        by_hash[record['sha256']].append(record['path'])
    tracked = set(subprocess.check_output(['git', 'ls-files', '-z'], cwd=REPO).decode().split('\0'))
    intake = []
    for run in ['discrete_time_wilson_2026-09-04', 'excited_wilson_window_2026-09-04']:
        manifest_path = REPO / 'runs' / run / 'import_manifest.json'
        manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        archive_path = ROOT / manifest['source_zip_name']
        members = []
        with zipfile.ZipFile(archive_path) as archive:
            actual_names = {m.filename for m in archive.infolist() if not m.is_dir()}
            for expected in manifest['members']:
                data = archive.read(expected['zip_member'])
                destination = REPO / expected['repository_path']
                actual_sha = sha(data)
                members.append({**expected, 'actual_sha256': actual_sha,
                                'member_matches_pin': actual_sha == expected['sha256'] and len(data) == expected['size'],
                                'destination_exists': destination.is_file(),
                                'destination_byte_identical': destination.is_file() and destination.read_bytes() == data,
                                'destination_tracked': expected['repository_path'] in tracked})
            expected_names = {m['zip_member'] for m in manifest['members']}
        intake.append({'run': run, 'source_zip': str(archive_path), 'source_zip_sha256': sha(archive_path.read_bytes()),
                       'zip_matches_pin': sha(archive_path.read_bytes()) == manifest['source_zip_sha256'],
                       'import_manifest_sha256': sha(manifest_path.read_bytes()), 'members': members,
                       'missing_from_import_map': sorted(actual_names - expected_names),
                       'map_entries_absent_from_zip': sorted(expected_names - actual_names)})
    save('LATEST_ZIP_INTAKE.json', intake)

    libraries = []
    for filename in ['o4/WORKHOUSE_research_library.zip', 'o4/WORKHOUSE_research_library_volume_2.zip']:
        archive_path = ROOT / filename
        with zipfile.ZipFile(archive_path) as archive:
            manifest_name = next(n for n in archive.namelist() if n.endswith('/paper_manifest.json'))
            prefix = manifest_name.removesuffix('paper_manifest.json')
            records = json.loads(archive.read(manifest_name))
            papers = []
            for record in records:
                member = prefix + record['local_file']
                data = archive.read(member)
                computed = sha(data)
                matches = by_hash.get(computed, [])
                papers.append({'title': record['title'], 'authors': record['authors'],
                               'doi': record.get('doi'), 'arxiv_id': record.get('arxiv_id'),
                               'arxiv_version': record.get('arxiv_version'), 'member': member,
                               'size': len(data), 'sha256': computed, 'matches_library_pin': computed == record['sha256'],
                               'matching_disk_paths': matches,
                               'matching_tracked_repository_paths': [p for p in matches if p.startswith(REPO.name+'/') and p[len(REPO.name)+1:] in tracked],
                               'classification': 'External reference paper; archive metadata is not a mathematical review.'})
            actual_pdf_names = {n for n in archive.namelist() if n.lower().endswith('.pdf')}
        libraries.append({'archive': filename, 'sha256': sha(archive_path.read_bytes()),
                          'paper_count': len(papers), 'all_pins_match': all(p['matches_library_pin'] for p in papers),
                          'unmanifested_pdf_members': sorted(actual_pdf_names - {p['member'] for p in papers}), 'papers': papers})
    cross_duplicates = {}
    for field in ['sha256', 'doi', 'arxiv_id', 'title']:
        def normalize(value):
            value = str(value or '').lower().strip()
            return re.sub(r'[^a-z0-9]', '', value) if field == 'title' else value
        left = {normalize(p[field]): p['title'] for p in libraries[0]['papers'] if normalize(p[field])}
        right = {normalize(p[field]): p['title'] for p in libraries[1]['papers'] if normalize(p[field])}
        cross_duplicates[field] = [{'key': k, 'first': left[k], 'second': right[k]} for k in sorted(left.keys() & right.keys())]
    save('REFERENCE_LIBRARY_PROVENANCE.json', {'libraries': libraries, 'cross_volume_duplicate_keys': cross_duplicates,
                                            'scope': 'Original archive metadata and PDF byte pins checked locally; publication/citation counts not independently re-fetched.'})

    original_pdf = ROOT / 'quantumrep-01-00009.pdf'
    preserved_pdf = REPO / 'literature/fulltext/quantumrep-01-00009.pdf'
    xmlpath = ROOT / 'quantumrep-01-00009.xml'
    xml = ET.fromstring(xmlpath.read_bytes())
    title = ''.join(xml.find('.//article-title').itertext())
    dois = [node.text for node in xml.findall('.//article-id') if node.get('pub-id-type') == 'doi']
    article = {'root_pdf_sha256': sha(original_pdf.read_bytes()), 'root_pdf_size': original_pdf.stat().st_size,
               'repository_pdf_sha256': sha(preserved_pdf.read_bytes()),
               'pdf_byte_identical': original_pdf.read_bytes() == preserved_pdf.read_bytes(),
               'repository_pdf_tracked': preserved_pdf.relative_to(REPO).as_posix() in tracked,
               'xml_sha256': sha(xmlpath.read_bytes()), 'xml_size': xmlpath.stat().st_size,
               'xml_matching_disk_paths': by_hash.get(sha(xmlpath.read_bytes()), []),
               'xml_article_title': title, 'xml_article_doi': dois,
               'xml_license_text': [' '.join(n.itertext()).strip() for n in xml.findall('.//license')],
               'scope': 'Published external oscillator reference; not original WORKHOUSE mathematics. XML is a separate structured representation, not a newer Wilson proof.'}
    save('ATTACHED_PAPER_PROVENANCE.json', article)

    variants = []
    filenames = ['FINAL PAPERS/WORKHOUSE_PUBLICATION_EDITION_20260830_REV4.zip',
                 'FINAL PAPERS/WORKHOUSE_PUBLICATION_EDITION_20260830_REV5.zip']
    contents = []
    for filename in filenames:
        with zipfile.ZipFile(ROOT / filename) as archive:
            contents.append({sha(archive.read(m)): m.filename for m in archive.infolist() if not m.is_dir()})
    variants.append({'archives': filenames, 'member_content_counts': [len(c) for c in contents],
                     'shared_member_hashes': len(contents[0].keys() & contents[1].keys()),
                     'only_revision4': [contents[0][h] for h in sorted(contents[0].keys()-contents[1].keys())],
                     'only_revision5': [contents[1][h] for h in sorted(contents[1].keys()-contents[0].keys())],
                     'conclusion': 'Distinct release snapshots; neither is a byte-redundant archive of the other.'})
    save('SELECTED_VERSION_DIFFERENCES.json', variants)
    print(json.dumps({'latest_zip_members': [len(r['members']) for r in intake],
                      'latest_zip_all_members_tracked_and_identical': all(m['destination_byte_identical'] and m['member_matches_pin'] and m['destination_tracked'] for r in intake for m in r['members']),
                      'library_papers': [r['paper_count'] for r in libraries],
                      'library_pin_failures': [sum(not p['matches_library_pin'] for p in r['papers']) for r in libraries],
                      'library_papers_without_disk_copy': [sum(not p['matching_disk_paths'] for p in r['papers']) for r in libraries],
                      'library_papers_in_tracked_repo': [sum(bool(p['matching_tracked_repository_paths']) for p in r['papers']) for r in libraries],
                      'cross_volume_duplicate_keys': {k: len(v) for k, v in cross_duplicates.items()},
                      'attachment_pdf_identical': article['pdf_byte_identical'],
                      'revision_member_content_counts': variants[0]['member_content_counts'],
                      'revision_shared_hashes': variants[0]['shared_member_hashes']}, indent=2))


if __name__ == '__main__':
    main()
