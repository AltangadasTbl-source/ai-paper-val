from pathlib import Path
from PIL import Image
import subprocess

ROOT = Path(__file__).resolve().parent.parent
doc = ROOT / '.ai_paper_validation' / 'document_outputs' / 'DOC-001-main-article'
full = doc / 'page_images' / 'page-001.png'
crop = doc / 'page_images' / 'page-001-abstract-crop.png'
# Narrow, downsampled Results-band crop avoids OCRing unrelated dense full-page content.
with Image.open(full) as im:
    band = im.crop((160, 1200, 1280, 1850))
    band.resize((560, 325)).save(crop)
base = doc / 'ocr_text' / 'page-001-abstract-crop'
subprocess.run(['tesseract', str(crop), str(base), '--psm', '6'], check=True)
raw = base.with_suffix('.txt').read_text(encoding='utf-8', errors='replace').strip()
(doc / 'ocr_text' / 'page-001.txt').write_text(
    'Source PDF: jama_martin_2025_oi_250042_1753377747.91025.pdf\n'
    'Source document ID: DOC-001-main-article\nSource PDF page: 1\n'
    'Extraction method: selective OCR from rendered abstract crop (200 dpi source page)\n'
    'OCR role: cross-check native text corruption affecting the abstract confidence-interval sign; full-page image retained.\n\n'
    + raw + '\n', encoding='utf-8')
