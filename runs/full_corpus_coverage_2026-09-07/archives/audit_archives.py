"""Read-only recursive archive-member census joined to the parent's file census.

Never extracts member paths. Temporary archive byte streams stay in this output
directory. Office/NPZ containers are hashed leaves; ZIP/TAR/GZ/7Z and compression
wrappers are recursively read. The current inventory is a byte-coverage census,
not a proof review or a recommendation to discard archived provenance.
"""
from __future__ import annotations

import collections
import gzip
import hashlib
import io
import json
import lzma
import bz2
import os
import re
from pathlib import Path, PurePosixPath
import subprocess
import tarfile
import tempfile
import zipfile

ROOT = Path('C:/WORKHOUSE')
REPO = ROOT / 'WORKHOUSE-autonomous-20260905'
OUT = REPO / 'outputs/corpus_coverage_20260907/archives'
SNAPSHOT = OUT.parent / 'snapshot_before/files.jsonl'
EXTENSIONS = {'.zip', '.tar', '.gz', '.7z', '.tgz', '.bz2', '.xz', '.txz', '.tbz2', '.whl'}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def write_json(path, obj):
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    rows = [json.loads(line) for line in SNAPSHOT.read_text(encoding='utf-8').splitlines()]
    by_hash = collections.defaultdict(list)
    for row in rows:
        by_hash[row['sha256']].append(row['path'])
    tracked = set(subprocess.check_output(['git', 'ls-files', '-z'], cwd=REPO).decode('utf-8').split('\0'))
    repo_prefix = REPO.name + '/'
    outer = [r for r in rows if Path(r['path']).suffix.lower() in EXTENSIONS]
    cache = {}
    active = set()
    objects = {}
    (OUT / 'objects').mkdir(exist_ok=True)

    def dependency_reason(name):
        lower = name.lower().replace('\\', '/')
        if lower.endswith('.whl'):
            return 'Dependency wheel; package byte hash recorded, dependency payload excluded.'
        if lower.endswith('tectonic.zip') and ('/tools/' in lower or '/.tools/' in lower):
            return 'Third-party Tectonic executable archive; byte hash recorded, runtime payload excluded.'
        if lower.endswith('godot_v4.7.1-stable_win64.exe.zip'):
            return 'Third-party Godot executable in existing unrelated quarantine; payload excluded.'
        return None

    def analyze(data, name):
        sha = digest(data)
        key = sha
        if key in cache:
            return key
        rec = {'sha256': sha, 'size': len(data), 'first_name': name, 'members': [], 'errors': [], 'status': 'complete'}
        cache[key] = rec
        reason = dependency_reason(name)
        if reason:
            rec.update(status='documented_dependency_exclusion', exclusion_reason=reason)
            return key
        if key in active:
            rec.update(status='cycle_not_expanded')
            return key
        active.add(key)

        def add(member_name, payload=None, kind='file', link_target=None, details=None):
            normalized = member_name.replace('\\', '/')
            parts = PurePosixPath(normalized).parts
            entry = {'memberpath': member_name, 'kind': kind, 'size': len(payload) if payload is not None else 0,
                     'sha256': digest(payload) if payload is not None else None,
                     'unsafe_extraction_path': normalized.startswith('/') or '..' in parts or ':' in parts[0] if parts else False}
            if link_target is not None:
                entry['link_target'] = link_target
            if details:
                entry.update(details)
            if payload is not None and entry['sha256'] not in by_hash:
                member_sha = entry['sha256']
                if member_sha not in objects:
                    suffix = Path(normalized).suffix.lower()
                    if not re.fullmatch(r'\.[a-z0-9]{1,16}', suffix):
                        suffix = '.bin'
                    target = OUT / 'objects' / (member_sha + suffix)
                    if not target.exists():
                        with target.open('xb') as destination:
                            destination.write(payload)
                    if digest(target.read_bytes()) != member_sha:
                        raise ValueError('Content-addressed object verification failed: ' + str(target))
                    objects[member_sha] = target.relative_to(OUT).as_posix()
                entry['materialized_object'] = objects[member_sha]
            rec['members'].append(entry)
            if payload is not None and Path(normalized).suffix.lower() in EXTENSIONS:
                entry['nested_archive_sha256'] = analyze(payload, member_name)

        try:
            if data.startswith(b'7z\xbc\xaf\x27\x1c'):
                # bsdtar/libarchive copies entries into a TAR byte stream, without
                # writing any user-supplied member path to disk.
                with tempfile.TemporaryDirectory(prefix='sevenzip_', dir=OUT) as temporary:
                    source = Path(temporary) / 'input.7z'
                    source.write_bytes(data)
                    result = subprocess.run(['tar', '-cf', '-', '@' + str(source)], capture_output=True, check=True)
                    tar_data = result.stdout
                with tarfile.open(fileobj=io.BytesIO(tar_data), mode='r:') as archive:
                    read_tar(archive, add, rec)
                rec['format'] = '7z via bsdtar 3.8.4 stream translation'
            elif zipfile.is_zipfile(io.BytesIO(data)):
                rec['format'] = 'zip'
                with zipfile.ZipFile(io.BytesIO(data)) as archive:
                    for index, member in enumerate(archive.infolist()):
                        try:
                            is_link = (member.external_attr >> 16) & 0o170000 == 0o120000
                            add(member.filename, None if member.is_dir() else archive.read(member),
                                'directory' if member.is_dir() else 'symlink' if is_link else 'file',
                                details={'member_index': index, 'compressed_size': member.compress_size,
                                         'crc32': f'{member.CRC:08x}', 'encrypted': bool(member.flag_bits & 1)})
                        except Exception as error:
                            rec['errors'].append({'memberpath': member.filename, 'error': repr(error)})
            else:
                try:
                    archive = tarfile.open(fileobj=io.BytesIO(data), mode='r:*')
                except tarfile.ReadError:
                    archive = None
                if archive is not None:
                    rec['format'] = 'tar or compressed tar'
                    with archive:
                        read_tar(archive, add, rec)
                elif data.startswith(b'\x1f\x8b'):
                    rec['format'] = 'gzip single logical uncompressed stream'
                    add(Path(name).name.removesuffix('.gz'), gzip.decompress(data))
                elif data.startswith(b'BZh'):
                    rec['format'] = 'bzip2 single stream'
                    add(Path(name).name.removesuffix('.bz2'), bz2.decompress(data))
                elif data.startswith(b'\xfd7zXZ\x00'):
                    rec['format'] = 'xz single stream'
                    add(Path(name).name.removesuffix('.xz'), lzma.decompress(data))
                else:
                    rec['status'] = 'unsupported_or_mislabeled'
        except Exception as error:
            rec['errors'].append({'error': repr(error)})
        if rec['errors']:
            rec['status'] = 'error_or_partial'
        names = collections.Counter(m['memberpath'] for m in rec['members'])
        rec['duplicate_member_names'] = {n: c for n, c in names.items() if c > 1}
        active.remove(key)
        return key

    def read_tar(archive, add, rec):
        for index, member in enumerate(archive):
            try:
                payload = archive.extractfile(member).read() if member.isfile() else None
                add(member.name, payload, 'file' if member.isfile() else 'directory' if member.isdir() else
                    'symlink' if member.issym() else 'hardlink' if member.islnk() else 'special',
                    member.linkname if member.issym() or member.islnk() else None,
                    {'member_index': index, 'declared_size': member.size})
            except Exception as error:
                rec['errors'].append({'memberpath': member.name, 'error': repr(error)})

    roots = []
    for index, row in enumerate(outer):
        try:
            data = (ROOT / row['path']).read_bytes()
            sha = digest(data)
            if sha != row['sha256']:
                roots.append({**row, 'status': 'changed_since_census', 'current_sha256': sha})
                continue
            key = analyze(data, row['path'])
            roots.append({**row, 'archive_sha256': key, 'status': cache[key]['status']})
        except Exception as error:
            roots.append({**row, 'status': 'outer_read_error', 'error': repr(error)})
        if (index + 1) % 25 == 0:
            print(f'outer {index+1}/{len(outer)}; distinct containers {len(cache)}', flush=True)

    counts = collections.Counter()
    unmatched = {}
    per_outer = []
    with (OUT / 'members.jsonl').open('w', encoding='utf-8', newline='\n') as stream:
        def emit(containerpath, key, ancestors, pathchain, totals):
            rec = cache[key]
            for member in rec['members']:
                sha = member['sha256']
                matches = by_hash.get(sha, []) if sha else []
                current_tracked = [p for p in matches if p.startswith(repo_prefix) and p[len(repo_prefix):] in tracked]
                current_local = [p for p in matches if p.startswith(repo_prefix)]
                row = {**member, 'containerpath': containerpath, 'container_sha256': key,
                       'nestedancestor': pathchain, 'ancestor_sha256': ancestors,
                       'matching_disk_paths': matches, 'matching_tracked_repository_paths': current_tracked,
                       'matching_repository_paths_including_ignored': current_local}
                stream.write(json.dumps(row, ensure_ascii=False) + '\n')
                counts['member_occurrences'] += 1
                if sha:
                    counts['hashed_member_occurrences'] += 1
                    totals['hashed_members'] += 1
                    totals['matched_disk_members'] += bool(matches)
                    totals['matched_tracked_members'] += bool(current_tracked)
                    if not matches:
                        counts['archive_only_member_occurrences'] += 1
                        item = unmatched.setdefault(sha, {'sha256': sha, 'size': member['size'],
                                                          'materialized_object': objects.get(sha), 'occurrences': []})
                        item['occurrences'].append({'containerpath': containerpath, 'nestedancestor': pathchain,
                                                    'memberpath': member['memberpath']})
                nested = member.get('nested_archive_sha256')
                if nested and nested not in ancestors + [key]:
                    emit(containerpath, nested, ancestors + [key], pathchain + [member['memberpath']], totals)
                elif nested:
                    counts['unexpanded_cycle_occurrences'] += 1
        for row in roots:
            totals = collections.Counter()
            if 'archive_sha256' in row:
                emit(row['path'], row['archive_sha256'], [], [], totals)
            per_outer.append({'path': row['path'], 'sha256': row['sha256'], 'status': row['status'], **totals})
    write_json(OUT / 'outer_archives.json', roots)
    write_json(OUT / 'distinct_containers.json', list(cache.values()))
    write_json(OUT / 'archive_only_content.json', list(unmatched.values()))
    write_json(OUT / 'per_archive_coverage.json', per_outer)
    duplicates = [{'sha256': sha, 'paths': [r['path'] for r in outer if r['sha256'] == sha]}
                  for sha, count in collections.Counter(r['sha256'] for r in outer).items() if count > 1]
    write_json(OUT / 'duplicate_archive_bytes.json', duplicates)
    summary = {'scope': 'All archive-extension files in parent snapshot; recursive nested archives; no member paths extracted.',
               'snapshot_sha256': digest(SNAPSHOT.read_bytes()), 'outer_archive_count': len(outer),
               'unique_outer_archive_bytes': len({r['sha256'] for r in outer}),
               'distinct_containers_including_nested': len(cache),
               'outer_status_counts': dict(collections.Counter(r['status'] for r in roots)),
               'container_status_counts': dict(collections.Counter(r['status'] for r in cache.values())),
               'archive_only_unique_member_hashes': len(unmatched), **counts,
               'verified_content_addressed_objects': len(objects),
               'materialized_unique_bytes': sum(r['size'] for r in unmatched.values()),
               'limitations': ['Office/NPZ document and numeric containers are hashed leaves, not expanded by this archive census.',
                               'A same-byte match is not proof review, scientific acceptance, or authorization to remove provenance.',
                               'Archive-only means no decompressed byte-identical census disk file; renamed/rewritten versions may exist.',
                               'Matches under ignored repository outputs are separated from tracked repository matches.']}
    write_json(OUT / 'ARCHIVE_CENSUS_SUMMARY.json', summary)
    print(json.dumps(summary, indent=2), flush=True)


if __name__ == '__main__':
    main()
