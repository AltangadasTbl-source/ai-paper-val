from pathlib import Path
import json, subprocess, sys, os
import fitz

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / '.ai_paper_validation' / 'document_outputs'
JOBS = {
    'DOC-001-main-article': {
        'pdf': ROOT / 'jama_martin_2025_oi_250042_1753377747.91025.pdf',
        'pages': [1] + list(range(3, 11)),
        'reason': 'Page 1 native text contains a corrupted confidence-interval sign in the abstract; pages 3-10 contain Table 1/2 or Figures 1-3, including participant flow and primary/secondary outcome displays.',
    },
    'DOC-003-supplement-2-results': {
        'pdf': ROOT / 'joi250042supp2_prod_1753377747.93025.pdf',
        'pages': list(range(8, 28)),
        'reason': 'Result-relevant eFigures 1-7 and eTables 1-10; includes layout-dependent plots, a flow diagram, and numerical tables.',
    },
}

requested = set(sys.argv[1:])
for docid, job in JOBS.items():
    if requested and docid not in requested:
        continue
    requested_pages = os.environ.get('PREPROCESS_PAGES')
    pages = job['pages'] if not requested_pages else [int(x) for x in requested_pages.split(',')]
    docdir = OUT / docid
    imagedir, ocrdir = docdir / 'page_images', docdir / 'ocr_text'
    imagedir.mkdir(exist_ok=True); ocrdir.mkdir(exist_ok=True)
    pdf = fitz.open(job['pdf'])
    for pg in pages:
        image = imagedir / f'page-{pg:03d}.png'
        if not image.exists():
            pix = pdf[pg-1].get_pixmap(matrix=fitz.Matrix(200/72, 200/72), alpha=False)
            pix.save(str(image))
        ocr_base = ocrdir / f'page-{pg:03d}'
        ocr = ocr_base.with_suffix('.txt')
        if not ocr.exists() or ocr.stat().st_size < 100:
            psm = '11' if docid == 'DOC-003-supplement-2-results' and pg <= 14 else '6'
            try:
                subprocess.run(['tesseract', str(image), str(ocr_base), '--psm', psm], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except subprocess.CalledProcessError:
                # Sparse plot/figure labels may fail the dense-table segmentation mode.
                subprocess.run(['tesseract', str(image), str(ocr_base), '--psm', '11'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            raw = ocr.read_text(encoding='utf-8', errors='replace').strip()
            header = f'Source PDF: {job["pdf"].name}\nSource document ID: {docid}\nSource PDF page: {pg}\nExtraction method: selective OCR from rendered page image (200 dpi)\nOCR role: visual cross-check for layout-dependent table/figure/flow content; native text remains retained.\n\n'
            ocr.write_text(header + raw + '\n', encoding='utf-8')
    pdf.close()

    manifest_path = docdir / 'page_manifest.json'
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    for row in manifest:
        pg = row['source_page']
        if pg in job['pages']:
            row['image'] = str((imagedir / f'page-{pg:03d}.png').relative_to(ROOT)).replace('\\', '/')
            row['ocr_text'] = str((ocrdir / f'page-{pg:03d}.txt').relative_to(ROOT)).replace('\\', '/')
            row['rendering'] = 'PyMuPDF raster, 200 dpi'
            row['ocr_engine'] = 'Tesseract 5.5.0; page segmentation mode 11 for figures and 6 for tables (mode 11 fallback if needed)'
            row['extraction_method'] = 'native plus selective OCR'
            row['quality_assessment'] = 'layout-dependent: native retained; visual/OCR cross-check created'
            row['quality_rationale'] = job['reason']
        else:
            row['rendering'] = 'not needed'
            row['ocr_engine'] = 'not needed'
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
