"""Validate the pilot's provenance, coverage and local Markdown links."""
from pathlib import Path
import json
import re

root = Path(__file__).resolve().parents[1]
refs = root / 'skills/paper-craft-iclr-reasoning/references'
corpus = json.loads((refs / 'corpus.json').read_text())
assert len(corpus) >= 10
assert len({p['id'] for p in corpus}) == len(corpus)
assert {p['venue'] for p in corpus} == {'ICLR'}
for paper in corpus:
    assert paper['reading_status'] == 'main_text_and_selected_appendices_read'
    assert paper['main_pages_read'] and paper['appendix_pages_read']
    assert re.fullmatch(r'[0-9a-f]{64}', paper['pdf_sha256'])
    note = refs / 'papers' / (paper['id'] + '.md')
    body = note.read_text()
    assert paper['pdf_url'] in body and paper['landing_url'] in body
    assert 'Experimental logic' in body and 'Detail placement' in body and 'Interpretation' in body
for path in root.rglob('*.md'):
    for link in re.findall(r'\]\(([^)]+)\)', path.read_text()):
        if '://' in link or link.startswith('#'):
            continue
        target = link.split('#')[0]
        assert (path.parent / target).exists(), (path, target)
print(f'PASS: {len(corpus)} ICLR papers, reading records, note coverage, hashes and local links.')
print('Structural checks only; semantic quality and external URL availability are not established by this script.')
