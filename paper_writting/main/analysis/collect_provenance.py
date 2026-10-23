#!/usr/bin/env python3
"""Collect source metadata without changing the final human workbooks."""
import csv
import hashlib
import json
import re
import subprocess
from pathlib import Path
from xml.etree import ElementTree as ET
from zipfile import ZipFile

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parent
REPO = PROJECT.parents[1]
CATALOG_ROOT = REPO / 'human_adjudication/human_adjudication_v_2_4_1'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def write_csv(name, rows):
    with (HERE / name).open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

catalog, papers, sources, hashes = [], [], [], []
for year in (2018, 2019, 2024, 2025):
    catfile = CATALOG_ROOT / str(year) / f'candidates_{year}.json'
    data = json.loads(catfile.read_text())
    hashes.append({'path': str(catfile), 'sha256': sha(catfile)})
    for c in data['candidates']:
        catalog.append({k: c[k] for k in ('key', 'domain', 'relationship_type', 'report_path', 'report_sha256')})
    for paper in data['papers']:
        package = REPO / str(year) / paper['paper']
        review = package / '.ai_paper_validation/review_1_6_2'
        report = package / '.ai_paper_validation/final_report_1_6_2.md'
        expected = next(c['report_sha256'] for c in data['candidates'] if c['paper'] == paper['paper'])
        assert sha(report) == expected, f'Report changed: {report}'
        state = (review / 'run_state.md').read_text()
        routing = (review / 'routing_preflight.md').read_text()
        def field(text, label):
            match = re.search(re.escape(label) + r'\*?\*?:\s*\*?\*?\s*([^\n]+)', text, re.I)
            return match.group(1).strip() if match else ''
        hashfile = review / 'source_hashes_before.sha256'
        direct = []
        for line in hashfile.read_text().splitlines():
            match = re.match(r'^([0-9a-f]{64})\s+\*?(.+?)\s*$', line)
            if not match:
                continue
            source = package / match.group(2)
            assert sha(source) == match.group(1), f'Source changed: {source}'
            direct.append(source)
        assert direct, f'No original source hashes: {hashfile}'
        pdfs = sorted(p for p in direct if p.suffix.lower() == '.pdf')
        workbooks = sorted(p for p in direct if p.suffix.lower() == '.xlsx')
        assert len(pdfs) + len(workbooks) == len(direct), f'Uncounted source type: {package}'
        pages = 0
        for pdf in pdfs:
            info = subprocess.check_output(['pdfinfo', str(pdf)], text=True)
            count = int(re.search(r'^Pages:\s+(\d+)', info, re.M).group(1))
            pages += count
            sources.append({'year': year, 'paper': paper['paper'], 'file': pdf.name,
                            'format': 'PDF', 'pages': count, 'worksheets': 0, 'sha256': sha(pdf)})
        worksheets = 0
        for workbook in workbooks:
            with ZipFile(workbook) as z:
                ns = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
                count = len(ET.fromstring(z.read('xl/workbook.xml')).findall('s:sheets/s:sheet', ns))
            worksheets += count
            sources.append({'year': year, 'paper': paper['paper'], 'file': workbook.name,
                            'format': 'XLSX', 'pages': 0, 'worksheets': count, 'sha256': sha(workbook)})
        papers.append({'year': year, 'paper': paper['paper'], 'candidates_catalog': paper['candidates'],
                       'documents': len(pdfs), 'pages': pages, 'workbooks': len(workbooks), 'worksheets': worksheets,
                       'started_utc': field(state, 'Started UTC'), 'finished_utc': field(state, 'Finished UTC'),
                       'model': field(routing, 'Run model'),
                       'report_sha256': expected})
for p in sorted((PROJECT / 'review_results_2_4_1_Rbulun_copy').glob('*.xlsx')):
    hashes.append({'path': str(p.relative_to(PROJECT)), 'sha256': sha(p)})
for p in [PROJECT / 'Outline_1021.md', CATALOG_ROOT / 'BUILD_SPEC.md']:
    hashes.append({'path': str(p), 'sha256': sha(p)})
write_csv('candidate_provenance.csv', catalog)
write_csv('package_metadata.csv', papers)
write_csv('source_files.csv', sources)
write_csv('input_hashes.csv', hashes)
print(f'{len(catalog)} candidates, {len(papers)} papers, {len(sources)} source files: '
      f'{sum(p["documents"] for p in papers)} PDFs, {sum(p["pages"] for p in papers)} pages, '
      f'{sum(p["workbooks"] for p in papers)} XLSX, {sum(p["worksheets"] for p in papers)} worksheet')
print('Recorded models:', sorted(set(p['model'] for p in papers)))
print('Run start dates:', min(p['started_utc'] for p in papers), 'to', max(p['started_utc'] for p in papers))
