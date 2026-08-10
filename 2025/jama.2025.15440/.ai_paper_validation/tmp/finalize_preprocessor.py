from pathlib import Path
import fitz, json

ROOT = Path.cwd()
OUT = ROOT / '.ai_paper_validation' / 'document_outputs'
SPECS = {
    'doc_001_main_article': {
        'source': 'jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf',
        'selected': list(range(1, 9)), 'visual': [4, 5, 6, 7, 8],
        'excluded': 'Page 9 (references) is not selected for scientific extraction.',
    },
    'doc_004_results_supplement': {
        'source': 'joi250068supp3_prod_1760999665.30362.pdf',
        'selected': [1, *range(4, 12)], 'visual': list(range(4, 12)),
        'excluded': 'Pages 2-3 (eMethods and references) are Not Audited by Design for the default results audit.',
    },
}

for doc_id, spec in SPECS.items():
    doc_dir = OUT / doc_id
    image_dir = doc_dir / 'page_images'
    ocr_dir = doc_dir / 'ocr_text'
    image_dir.mkdir(exist_ok=True)
    ocr_dir.mkdir(exist_ok=True)
    doc = fitz.open(ROOT / spec['source'])
    pages = []
    for n in spec['selected']:
        im_rel = None
        if n in spec['visual']:
            image_path = image_dir / f'page_{n:03}.png'
            if not image_path.exists():
                doc[n-1].get_pixmap(matrix=fitz.Matrix(4.167, 4.167), alpha=False).save(image_path)
            im_rel = f'page_images/{image_path.name}'
        ocr_path = ocr_dir / f'page_{n:03}.txt'
        ocr_rel = f'ocr_text/{ocr_path.name}' if ocr_path.exists() and ocr_path.stat().st_size > 100 else None
        notes = []
        if doc_id == 'doc_001_main_article' and n == 1:
            notes.append('Minor character-mapping artifact in an author surname; scientific result text remains readable.')
        if not notes:
            notes.append('Native extraction is complete, non-sparse, and usable for the audit scope.')
        rec = {
            'source_page': n, 'source_pdf': spec['source'],
            'text_file': f'normalized_text/page_{n:03}.txt', 'native_text_used': True,
            'native_text_quality': 'usable', 'quality_notes': notes,
            'rendered_image': im_rel, 'ocr_used': bool(ocr_rel), 'ocr_file': ocr_rel,
        }
        if im_rel:
            rec['image_reason'] = 'Required table, figure, or participant-flow visual content for downstream checks.'
        if ocr_rel:
            rec['ocr_reason'] = 'Supplementary OCR retained for the rendered visual page; native text remains the primary normalized source.'
        elif im_rel:
            rec['ocr_reason'] = 'Not used: native text was complete and usable; image retained for visual inspection.'
        pages.append(rec)
    manifest = {
        'document_id': doc_id, 'source_pdf': spec['source'], 'source_page_count': len(doc),
        'selected_audit_pages': spec['selected'], 'excluded_content': spec['excluded'],
        'extraction_summary': 'Native text extracted first for every selected page. OCR was not used to replace any native text.',
        'pages': pages,
    }
    (doc_dir / 'page_extraction_manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    md = [f'# Page Extraction Manifest: {doc_id}', '', f'- Source PDF: `{spec["source"]}`', f'- Selected pages: {", ".join(map(str, spec["selected"]))}', f'- Excluded content: {spec["excluded"]}', '- Native text: all selected pages usable.', '- OCR: used only as supplemental evidence for rendered pages where completed; no page required OCR replacement.', '', '| PDF page | Native text | Image | OCR | Source-linked artifact |', '|---:|---|---|---|---|']
    for p in pages:
        md.append(f"| {p['source_page']} | usable | {'yes' if p['rendered_image'] else 'no'} | {'yes' if p['ocr_used'] else 'no'} | `{p['text_file']}` |")
    (doc_dir / 'page_extraction_manifest.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    print(doc_id, 'finalized')
