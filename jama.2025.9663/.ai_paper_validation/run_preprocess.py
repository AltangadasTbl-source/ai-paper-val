from pathlib import Path
import json, re
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / '.ai_paper_validation'
DOCS = {
    'DOC-001-main-article': ROOT / 'jama_martin_2025_oi_250042_1753377747.91025.pdf',
    'DOC-003-supplement-2-results': ROOT / 'joi250042supp2_prod_1753377747.93025.pdf',
}

def quality(text):
    n = len(text.strip())
    bad = sum(1 for c in text if c == '\ufffd' or ord(c) < 9 or (0xE000 <= ord(c) <= 0xF8FF))
    printable = sum(1 for c in text if c.isprintable() or c in '\n\t')
    tokens = len(re.findall(r"[A-Za-z0-9][A-Za-z0-9%.,;:()/'-]*", text))
    return n, tokens, round(printable / max(1, len(text)), 3), bad

all_rows = []
for doc_id, source in DOCS.items():
    docdir = OUT / 'document_outputs' / doc_id
    textdir = docdir / 'normalized_text'
    textdir.mkdir(parents=True, exist_ok=True)
    reader = PdfReader(str(source))
    rows = []
    for ix, page in enumerate(reader.pages, 1):
        text = page.extract_text(extraction_mode='layout') or ''
        chars, tokens, printable_ratio, bad = quality(text)
        status = 'acceptable_native'
        reason = 'Native text is legible and sufficiently dense for page content.'
        if chars < 40 or tokens < 8:
            status, reason = 'sparse_native', 'Native text is sparse; visual/OCR review needed if page is audit-relevant.'
        elif printable_ratio < .97 or bad:
            status, reason = 'corrupted_native', 'Native text contains nonstandard/corrupted glyphs; visual/OCR review needed.'
        target = textdir / f'page-{ix:03d}.txt'
        header = f'Source PDF: {source.name}\nSource document ID: {doc_id}\nSource PDF page: {ix}\nExtraction method: native\n\n'
        target.write_text(header + text.strip() + '\n', encoding='utf-8')
        row = {
            'document_id': doc_id, 'source_pdf': source.name, 'source_page': ix,
            'normalized_text': str(target.relative_to(ROOT)).replace('\\\\','/'),
            'native_characters': chars, 'native_tokens': tokens,
            'printable_ratio': printable_ratio, 'nonstandard_characters': bad,
            'quality_assessment': status, 'quality_rationale': reason,
            'extraction_method': 'native', 'image': None, 'ocr_text': None,
            'page_content_relevance': 'Scientific audit in scope',
        }
        rows.append(row); all_rows.append(row)
    (docdir / 'page_manifest.json').write_text(json.dumps(rows, indent=2), encoding='utf-8')

# DOC-002: intentionally no scientific extraction/render/OCR.
doc2 = OUT / 'document_outputs' / 'DOC-002-supplement-1-protocol-sap'
doc2.mkdir(parents=True, exist_ok=True)
(doc2 / 'page_manifest.json').write_text(json.dumps([{
    'document_id':'DOC-002-supplement-1-protocol-sap',
    'source_pdf':'joi250042supp1_prod_1753377747.92525.pdf',
    'source_pages':'1-136', 'processing_status':'Not Audited by Design',
    'extraction_method':'not performed', 'rendering':'not performed', 'ocr':'not performed',
    'rationale':'Combined protocol/SAP excluded from scientific audit; retained only for completed rights screening and may be opened for a specific parent-requested comparison.'
}], indent=2), encoding='utf-8')

print(json.dumps(all_rows, indent=2))
