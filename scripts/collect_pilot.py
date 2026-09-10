"""Fetch official paper PDFs into Palmetto scratch; retain only provenance locally."""
import concurrent.futures
import datetime
import hashlib
import json
from pathlib import Path
import subprocess

import bs4
import requests

ROOT = Path(__file__).resolve().parents[1]
REF = ROOT / 'skills/paper-craft-iclr-reasoning/references'
SCRATCH = '/scratch/runw/paper-craft/cache/papers'
PAPERS = [
    ('P01', 2023, 'Self-Consistency Improves Chain of Thought Reasoning in Language Models', '1PL1NIMMrw'),
    ('P02', 2023, 'Least-to-Most Prompting Enables Complex Reasoning in Large Language Models', 'WZH7099tgfM'),
    ('P03', 2024, 'Large Language Models Cannot Self-Correct Reasoning Yet', '8b4add8b0aa8749d80a34ca5d941c355'),
    ('P04', 2024, "Let's Verify Step by Step", 'aca97732e30bcf1303bc22ac3924fd16'),
    ('P05', 2025, 'Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning', '1b623663fd9b874366f3ce019fdfdd44'),
    ('P06', 2025, 'Training Language Models to Self-Correct via Reinforcement Learning', '871ac99fdc5282d0301934d23945ebaa'),
    ('P07', 2025, 'Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning', '98711dea460bdefe0e651ca23ec98ba2'),
    ('P08', 2025, 'Mutual Reasoning Makes Smaller LLMs Stronger Problem-Solver', '35514d533cdc278a7780daf0dbe7d0b7'),
    ('P09', 2025, 'On the self-verification limitations of large language models on reasoning and planning tasks', 'f3c5e56274140e0420baa3916c529210'),
    ('P10', 2025, 'To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning', 'ead542f13a38179d1b55b88610f959a1'),
]

def fetch(row):
    pid, year, title, key = row
    if year == 2023:
        landing = f'https://openreview.net/forum?id={key}'
        pdf_url = {'P01': 'https://arxiv.org/pdf/2203.11171v4', 'P02': 'https://arxiv.org/pdf/2205.10625v3'}[pid]
    else:
        landing = f'https://proceedings.iclr.cc/paper_files/paper/{year}/hash/{key}-Abstract-Conference.html'
        pdf_url = f'https://proceedings.iclr.cc/paper_files/paper/{year}/file/{key}-Paper-Conference.pdf'
    page = requests.get(landing, timeout=60)
    # OpenReview may serve a browser challenge; acceptance is checked separately.
    soup = bs4.BeautifulSoup(page.text, 'html.parser')
    pdf = requests.get(pdf_url, timeout=120)
    pdf.raise_for_status()
    if not pdf.content.startswith(b'%PDF'):
        raise ValueError(f'{pid}: not a PDF')
    raw = subprocess.run(['pdftotext', '-layout', '-', '-'], input=pdf.content, capture_output=True, check=True).stdout
    subprocess.run(['ssh', 'palmetto', f'cat > {SCRATCH}/{pid}.pdf'], input=pdf.content, check=True)
    subprocess.run(['ssh', 'palmetto', f'cat > {SCRATCH}/{pid}.txt'], input=raw, check=True)
    result = dict(id=pid, title=title, venue='ICLR', year=year, landing_url=landing, pdf_url=pdf_url,
                  retrieved_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  pdf_sha256=hashlib.sha256(pdf.content).hexdigest(), pdf_bytes=len(pdf.content),
                  pages=raw.count(b'\x0c'), cache_host='palmetto', cache_pdf=f'{SCRATCH}/{pid}.pdf',
                  cache_text=f'{SCRATCH}/{pid}.txt', reading_status='downloaded_not_yet_read',
                  page_metadata=[m.attrs for m in soup.select('meta[name^="citation_"]')])
    (REF / 'papers' / f'{pid}.metadata.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(pid, result['pages'], title, flush=True)
    return result

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        results = list(pool.map(fetch, PAPERS))
    (REF / 'corpus.json').write_text(json.dumps(results, ensure_ascii=False, indent=2) + '\n')
