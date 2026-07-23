from pathlib import Path
import fitz
import json, re, unicodedata, subprocess

ROOT = Path.cwd()
OUT = ROOT / '.ai_paper_validation' / 'document_outputs'
SPECS = {
    'doc_001_main_article': {
        'source': 'jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf',
        'selected': list(range(1, 9)),
        'visual': [4, 5, 6, 7, 8],
    },
    'doc_004_results_supplement': {
        'source': 'joi250068supp3_prod_1760999665.30362.pdf',
        'selected': [1, *range(4, 12)],
        'visual': list(range(4, 12)),
    },
}

def normalize(text: str) -> str:
    text = unicodedata.normalize('NFKC', text or '')
    text = text.replace('\u00ad', '')
    text = ''.join(ch for ch in text if ch in '\n\t' or ord(ch) >= 32)
    text = re.sub(r'[ \t]+\n', '\n', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip() + '\n'

def score(text: str, page_num: int, doc_id: str) -> tuple[str, list[str]]:
    chars = len(re.sub(r'\s+', '', text))
    bad = len(re.findall(r'[\ufffd]|[\x00-\x08\x0b\x0c\x0e-\x1f]', text))
    reasons = []
    if chars < 80:
        reasons.append('sparse native text (<80 non-whitespace characters)')
    if bad:
        reasons.append(f'{bad} replacement/control characters')
    if doc_id == 'doc_001_main_article' and page_num == 1:
        reasons.append('minor character-mapping artifact in an author surname; scientific result text remains readable')
    return ('needs_ocr' if chars < 80 or bad else 'usable'), reasons

for doc_id, spec in SPECS.items():
    reader = fitz.open(ROOT / spec['source'])
    doc_dir = OUT / doc_id
    text_dir = doc_dir / 'normalized_text'
    image_dir = doc_dir / 'page_images'
    ocr_dir = doc_dir / 'ocr_text'
    text_dir.mkdir(parents=True, exist_ok=True)
    image_dir.mkdir(parents=True, exist_ok=True)
    ocr_dir.mkdir(parents=True, exist_ok=True)
    pages = []
    combined = []
    for page_num in spec['selected']:
        text = normalize(reader[page_num - 1].get_text('text') or '')
        quality, reasons = score(text, page_num, doc_id)
        fn = f'page_{page_num:03}.txt'
        (text_dir / fn).write_text(
            f'Source PDF: {spec["source"]}\nSource PDF page: {page_num}\nExtraction method: native PDF text\n\n{text}',
            encoding='utf-8')
        page_rec = {'source_page': page_num, 'source_pdf': spec['source'], 'text_file': f'normalized_text/{fn}', 'method': 'native', 'quality': quality, 'quality_notes': reasons, 'ocr_used': False, 'rendered_image': None, 'ocr_file': None}
        if page_num in spec['visual']:
            image_name = f'page_{page_num:03}.png'
            image_path = image_dir / image_name
            pix = reader[page_num - 1].get_pixmap(matrix=fitz.Matrix(4.167, 4.167), alpha=False)
            pix.save(image_path)
            ocr_path = ocr_dir / f'page_{page_num:03}.txt'
            subprocess.run(['C:/msys64/ucrt64/bin/tesseract.exe', str(image_path), str(ocr_path.with_suffix('')), '--dpi', '300'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
            ocr_text = normalize(ocr_path.read_text(encoding='utf-8', errors='replace'))
            ocr_path.write_text(f'Source PDF: {spec["source"]}\nSource PDF page: {page_num}\nExtraction method: OCR from rendered 300 dpi page image\n\n{ocr_text}', encoding='utf-8')
            page_rec['rendered_image'] = f'page_images/{image_name}'
            page_rec['ocr_file'] = f'ocr_text/page_{page_num:03}.txt'
            page_rec['ocr_used'] = True
            page_rec['ocr_reason'] = 'table, figure, or participant-flow content retained for downstream visual checks'
        pages.append(page_rec)
        combined.append(f'\n===== SOURCE PDF PAGE {page_num} | native extraction =====\n\n{text}')
    (doc_dir / 'normalized_text.md').write_text(
        f'# Normalized text: {doc_id}\n\nSource PDF: `{spec["source"]}`. Only selected audit pages are included.\n' + ''.join(combined),
        encoding='utf-8')
    (doc_dir / 'page_extraction_manifest.json').write_text(json.dumps({
        'document_id': doc_id, 'source_pdf': spec['source'], 'selected_audit_pages': spec['selected'],
        'pages': pages,
    }, indent=2), encoding='utf-8')
    print(doc_id, len(pages), 'pages', '; '.join(f"p{p['source_page']}={p['quality']}" for p in pages))
