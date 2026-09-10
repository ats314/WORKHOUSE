"""Use original member names for policy and recover known text representations."""
import collections
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
OUT = Path(__file__).resolve().parent
EXTRACTION = OUT / 'archive_extraction'


def main():
    policy_path = OUT.parent / 'extract_corpus.py'
    spec = importlib.util.spec_from_file_location('corpus_extraction_policy', policy_path)
    policy = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(policy)
    objects = {r['sha256']: r for r in json.loads((OUT/'archive_only_content.json').read_text(encoding='utf-8'))}
    old = [json.loads(line) for line in (EXTRACTION/'content_final.jsonl').read_text(encoding='utf-8').splitlines()]
    classes = [json.loads(line) for line in (EXTRACTION/'classifications.jsonl').read_text(encoding='utf-8').splitlines()]
    classified = {}
    for row in classes:
        original = objects[row['sha256']]
        occurrences = original['occurrences']
        original_reasons = [policy.infrastructure(o['memberpath']) for o in occurrences]
        reason = row['exclusion']
        if all(original_reasons):
            reason = '; '.join(sorted(set(original_reasons)))
        classified[row['sha256']] = {**row, 'exclusion': reason,
                                     'member_origins': occurrences,
                                     'policy_basis': 'Both original member path and materialized path; original configuration names are not lost.'}
    updated = []
    new_text = []
    for row in old:
        if classified[row['sha256']]['exclusion']:
            continue
        original = objects[row['sha256']]
        member_name = original['occurrences'][0]['memberpath']
        base = Path(member_name).name
        extension = Path(member_name).suffix.lower()
        text_format = extension in {'.ts', '.tsx', '.ndjson', '.sha256', '.time'} or base in {'.gitignore', 'lean-toolchain'} or '.json__' in base
        if row['extraction'] == 'unsupported' and text_format:
            data = (OUT/original['materialized_object']).read_bytes()
            if hashlib.sha256(data).hexdigest() != row['sha256']:
                raise ValueError('Object changed: ' + row['sha256'])
            text, encoding = policy.decode(data)
            encoded = text.encode('utf-8')
            target = EXTRACTION/'texts'/(row['sha256']+'.member-text.txt')
            with target.open('xb') as destination:
                destination.write(encoded)
            row = {**row, 'extraction': 'text-extracted', 'method': 'Original-member-aware full text recovery: '+encoding+'; no source execution',
                   'text_file': target.relative_to(EXTRACTION).as_posix(), 'text_sha256': hashlib.sha256(encoded).hexdigest(),
                   'characters': len(text), 'lines': text.count('\n')+1, 'recovered_from': 'unsupported'}
            new_text.append({'sha256': row['sha256'], 'memberpath': member_name, 'characters': len(text)})
        updated.append(row)
    for name, records in [('classifications_complete.jsonl', list(classified.values())), ('content_complete.jsonl', updated)]:
        with (EXTRACTION/name).open('x', encoding='utf-8', newline='\n') as stream:
            for row in records:
                stream.write(json.dumps(row, ensure_ascii=False, sort_keys=True)+'\n')
    summary = {'member_objects': len(objects), 'excluded_objects': sum(bool(r['exclusion']) for r in classified.values()),
               'eligible_unique_contents': len(updated), 'extraction_counts': dict(collections.Counter(r['extraction'] for r in updated)),
               'new_text_recoveries': new_text, 'unresolved_representations': [
                   {'sha256': r['sha256'], 'size': r['size'], 'origins': objects[r['sha256']]['occurrences']}
                   for r in updated if r['extraction'] == 'unsupported'],
               'extracted_characters': sum(r.get('characters', 0) for r in updated),
               'errors': [r for r in updated if r['extraction']=='error' or r.get('recovery_error')],
               'policy_source_sha256': hashlib.sha256(policy_path.read_bytes()).hexdigest(),
               'scope': 'Content extraction and provenance-aware eligibility only. No mathematical, visual, execution or numerical-data validity claim.'}
    (EXTRACTION/'COMPLETE_MEMBER_EXTRACTION.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k:v for k,v in summary.items() if k not in {'new_text_recoveries','unresolved_representations'}}, indent=2))


if __name__ == '__main__':
    main()
