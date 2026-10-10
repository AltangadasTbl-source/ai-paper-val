#!/usr/bin/env python3
"""Construction-only, read-only baseline inspection; Python standard library only."""
import hashlib
import json
import posixpath
from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree as ET

HERE = Path(__file__).resolve().parent
YEAR = int(HERE.name)
EXPECTED = {2018: (10, 119), 2019: (10, 71), 2024: (10, 91), 2025: (15, 131)}
# The historical directory was archived. Use the hash-verified, year-local
# extraction when the original directory is unavailable. Never modify sources.
ROOT = next(p for p in HERE.parents if (p / 'human_adjudication/previous').is_dir())
SOURCE = ROOT / 'human_adjudication/previous/human_adjudication_v_2_1_5_3'
if not SOURCE.is_dir():
    SOURCE = HERE / 'sources/human_adjudication_v_2_1_5_3'
NS = {'m': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
RID = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id'

def inspect(path):
    with ZipFile(path) as z:
        strings = []
        if 'xl/sharedStrings.xml' in z.namelist():
            strings = [''.join(t.text or '' for t in s.findall('.//m:t', NS))
                       for s in ET.fromstring(z.read('xl/sharedStrings.xml'))]
        rels = {r.get('Id'): r.get('Target') for r in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
        sheets = {}
        for s in ET.fromstring(z.read('xl/workbook.xml')).find('m:sheets', NS):
            target = rels[s.get(RID)]
            target = target.lstrip('/') if target.startswith('/') else posixpath.normpath('xl/' + target)
            xml = ET.fromstring(z.read(target))
            rows = []
            formulas = []
            for row in xml.findall('m:sheetData/m:row', NS):
                values = {}
                for c in row.findall('m:c', NS):
                    v, f = c.find('m:v', NS), c.find('m:f', NS)
                    value = v.text if v is not None else None
                    if c.get('t') == 's' and value is not None:
                        value = strings[int(value)]
                    elif c.get('t') == 'inlineStr':
                        value = ''.join(t.text or '' for t in c.findall('.//m:t', NS))
                    if f is not None:
                        formulas.append({'cell': c.get('r'), 'formula': f.text})
                    if value is not None or f is not None:
                        values[c.get('r')] = value
                rows.append(values)
            sheets[s.get('name')] = {'rows': rows, 'formulas': formulas,
                                     'protected': xml.find('m:sheetProtection', NS) is not None}
        return sheets

def main():
    annual = SOURCE / f'human_adjudication_v_2_1_5_3_{YEAR}.xlsx'
    catalog = SOURCE / 'resources/source_catalog_v_2_1_5_3.xlsx'
    sheets = inspect(annual)
    papers = []
    all_keys = []
    for name, sheet in sheets.items():
        if not name.startswith('C_'):
            continue
        keys = [value for row in sheet['rows'][1:] for cell, value in row.items()
                if cell.rstrip('0123456789') == 'A' and value]
        all_keys.extend(keys)
        papers.append({'sheet': name, 'candidates': len(keys), 'keys': keys,
                       'headers': sheet['rows'][0], 'default_formula_examples': sheet['formulas'][:8]})
    assert (len(papers), len(all_keys)) == EXPECTED[YEAR], 'Baseline totals changed; investigate before construction'
    assert len(all_keys) == len(set(all_keys)), 'Duplicate candidate keys'
    source_files = [annual, catalog, SOURCE/'USAGE.md', SOURCE/'DESIGN.md',
                    SOURCE/'VALIDATION.md', SOURCE/'maintenance/build.mjs', SOURCE/'maintenance/codebook.json']
    report = {'year': YEAR, 'expected_papers': EXPECTED[YEAR][0], 'expected_candidates': EXPECTED[YEAR][1],
              'source_files': [{'path': str(p), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()} for p in source_files],
              'sheet_names': list(sheets), 'protected_sheets': [n for n, s in sheets.items() if s['protected']],
              'papers': papers,
              'source_headers': {n: sheets[n]['rows'][0] for n in ['Candidates','Evidence','Links','Relations']},
              'scope': 'Baseline inventory only; not validation of any v.2.3.1 workbook.'}
    print(json.dumps(report, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
