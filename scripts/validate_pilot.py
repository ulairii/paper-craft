"""Validate published specialist corpora and local Markdown links."""
from pathlib import Path
import json
import re

root = Path(__file__).resolve().parents[1]
catalog = (root / 'skills/paper-craft/references/catalog.md').read_text()
corpora = sorted(root.glob('skills/*/references/corpus.json'))
assert corpora, 'No specialist corpora found'
count = 0
for source in corpora:
    refs = source.parent
    skill = refs.parent
    assert (skill / 'SKILL.md').is_file(), skill
    assert skill.name in catalog, f'Unregistered specialist: {skill.name}'
    corpus = json.loads(source.read_text())
    assert len(corpus) >= 10, source
    assert len({p['id'] for p in corpus}) == len(corpus), source
    assert len({p['landing_url'] for p in corpus}) == len(corpus), source
    assert len({p['venue'] for p in corpus}) == 1, source
    for paper in corpus:
        if paper['reading_status'] == 'main_text_and_selected_appendices_read':
            assert paper['main_pages_read'] and paper['appendix_pages_read'], paper['id']
        else:
            assert paper['reading_status'] == 'main_text_read', paper['id']
            assert paper['reading_coverage'], paper['id']
            assert paper['authors'] and paper['bibtex'], paper['id']
            assert paper['bibtex'] in (refs / 'references.bib').read_text(), paper['id']
        assert re.fullmatch(r'[0-9a-f]{64}', paper['pdf_sha256']), paper['id']
        body = (refs / 'papers' / (paper['id'] + '.md')).read_text()
        assert paper['pdf_url'] in body and paper['landing_url'] in body, paper['id']
        for section in ('Experimental logic', 'Detail placement', 'Interpretation'):
            assert section in body, (source, paper['id'], section)
    count += len(corpus)
for path in root.rglob('*.md'):
    for link in re.findall(r'\]\(([^)]+)\)', path.read_text()):
        if '://' in link or link.startswith('#'):
            continue
        target = link.split('#')[0]
        assert (path.parent / target).exists(), (path, target)
print(f'PASS: {len(corpora)} specialist corpora, {count} paper records, references and local links.')
print('Structural checks only; semantic quality and external URL availability are not established by this script.')
