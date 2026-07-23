from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / '.ai_paper_validation' / 'document_outputs'

def rel(path):
    return str(path.relative_to(ROOT)).replace('\\', '/')

# Main article: all source pages are in scientific scope.
main = BASE / 'DOC-001-main-article'
rows = json.loads((main / 'page_manifest.json').read_text(encoding='utf-8'))
for row in rows:
    pg = row['source_page']
    row['normalized_text'] = rel(main / 'normalized_text' / f'page-{pg:03d}.txt')
    if pg in range(3, 11):
        row['page_content_relevance'] = 'In scope: results table/figure/participant-flow or adjoining result display.'
    else:
        row['page_content_relevance'] = 'In scope: main-article narrative, abstract, methods, or end matter.'
(main / 'page_manifest.json').write_text(json.dumps(rows, indent=2), encoding='utf-8')

# Results supplement: preserve a record for excluded contents but no text artifact.
supp = BASE / 'DOC-003-supplement-2-results'
rows = json.loads((supp / 'page_manifest.json').read_text(encoding='utf-8'))
for row in rows:
    pg = row['source_page']
    if pg in {1, 28, 29}:
        text = supp / 'normalized_text' / f'page-{pg:03d}.txt'
        if text.exists():
            text.unlink()
        row.update({
            'normalized_text': None, 'image': None, 'ocr_text': None,
            'extraction_method': 'not performed', 'rendering': 'not performed', 'ocr_engine': 'not performed',
            'quality_assessment': 'Not Audited by Design',
            'quality_rationale': 'Contents/eReferences page is not result-relevant scientific audit content.',
            'page_content_relevance': 'Not Audited by Design: contents (page 1) or eReferences (pages 28-29).',
        })
    else:
        row['normalized_text'] = rel(supp / 'normalized_text' / f'page-{pg:03d}.txt')
        if pg <= 7:
            row['page_content_relevance'] = 'In scope: result-relevant eMethods.'
        elif pg <= 14:
            row['page_content_relevance'] = 'In scope: result-relevant eFigure.'
        else:
            row['page_content_relevance'] = 'In scope: result-relevant eTable.'
(supp / 'page_manifest.json').write_text(json.dumps(rows, indent=2), encoding='utf-8')

(main / 'preprocessing_status.md').write_text('''# PDF Preprocessing Status\n\n- Source PDF unchanged: `jama_martin_2025_oi_250042_1753377747.91025.pdf`\n- Processing status: `Complete`\n- Scientific extraction scope: all PDF pages 1-11 (full main article).\n- Native normalized text: pages 1-11.\n- Native-text quality: usable on every page; layout/character-spacing artifacts are retained alongside the page images and OCR where applicable.\n- Rendered and OCR cross-check: pages 1 and 3-10. Page 1 received a cropped abstract OCR cross-check for a corrupted confidence-interval sign; pages 3-10 contain the required participant-flow diagram, figures, tables, or adjoining result displays.\n- Not rendered/OCR: pages 2 and 11; native text was sufficient and no later visual/table/flow check requires a page image.\n- Page provenance: `page_manifest.json`; native text in `normalized_text/`; selected images in `page_images/`; selected OCR in `ocr_text/`.\n''', encoding='utf-8')

(supp / 'preprocessing_status.md').write_text('''# PDF Preprocessing Status\n\n- Source PDF unchanged: `joi250042supp2_prod_1753377747.93025.pdf`\n- Processing status: `Complete`\n- Scientific extraction scope: pages 2-27 (result-relevant eMethods, eFigures, and eTables).\n- Native normalized text: pages 2-27.\n- Native-text quality: usable on every scoped text page; layout-dependent figures/tables received visual/OCR cross-checks.\n- Rendered and OCR cross-check: pages 8-27 (eFigures 1-7 and eTables 1-10).\n- Native only: pages 2-7 (eMethods); no layout-dependent evidence requiring an image/OCR cross-check.\n- Not Audited by Design: page 1 (contents) and pages 28-29 (eReferences); no native text, rendering, or OCR retained for scientific processing.\n- Page provenance: `page_manifest.json`; native text in `normalized_text/`; selected images in `page_images/`; selected OCR in `ocr_text/`.\n''', encoding='utf-8')

protocol = BASE / 'DOC-002-supplement-1-protocol-sap'
(protocol / 'preprocessing_status.md').write_text('''# PDF Preprocessing Status\n\n- Source PDF unchanged: `joi250042supp1_prod_1753377747.92525.pdf`\n- Processing status: `Not Audited by Design`\n- Scientific extraction/OCR/rendering scope: none (pages 1-136 excluded).\n- Rationale: combined protocol and statistical analysis plan is excluded from default scientific auditing; it may be opened only for a specific parent-requested comparison.\n- Rights-screening record retained separately: `ai_training_restriction_record.md`.\n- Page-level status: `page_manifest.json`.\n''', encoding='utf-8')

(ROOT / '.ai_paper_validation' / 'preprocessing_summary.md').write_text('''# PDF Preprocessing Summary\n\n| Document | Scientific scope | Native text retained | Selective rendering/OCR | Status |\n|---|---|---|---|---|\n| DOC-001-main-article | pages 1-11 | pages 1-11 | pages 1 and 3-10 | Complete |\n| DOC-002-supplement-1-protocol-sap | none | none | none | Not Audited by Design |\n| DOC-003-supplement-2-results | pages 2-27 | pages 2-27 | pages 8-27 | Complete |\n\nNative text was extracted before any OCR. Images/OCR were retained only for in-scope layout-dependent evidence pages. Source PDFs were not modified. See document-specific `page_manifest.json` files for page-level source references and extraction method.\n''', encoding='utf-8')
