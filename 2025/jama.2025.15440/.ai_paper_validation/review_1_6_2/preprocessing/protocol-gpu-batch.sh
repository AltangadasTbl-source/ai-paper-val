#!/usr/bin/env bash
set -eu
cd /home/juliz/ai-paper-val/2025/jama.2025.15440
for ocr_page in $(seq 2 26); do
  ocr_tag=$(printf '%03d' "$ocr_page")
  .ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py render joi250068supp1_prod_1760999665.28862.pdf --page "$ocr_page" ".ai_paper_validation/review_1_6_2/preprocessing/doc002-page-${ocr_tag}.png" --dpi 200
  bash .ai_paper_validation/review_1_6_2/preprocessing/gpu-ocr.sh ".ai_paper_validation/review_1_6_2/preprocessing/doc002-page-${ocr_tag}.png" > ".ai_paper_validation/review_1_6_2/preprocessing/doc002-page-${ocr_tag}-gpu-ocr.log" 2>&1
  perl .ai_paper_validation/review_1_6_2/preprocessing/ocr-log-to-text.pl ".ai_paper_validation/review_1_6_2/preprocessing/doc002-page-${ocr_tag}-gpu-ocr.log" > ".ai_paper_validation/review_1_6_2/preprocessing/doc002-page-${ocr_tag}-gpu-ocr.txt"
  test -s ".ai_paper_validation/review_1_6_2/preprocessing/doc002-page-${ocr_tag}-gpu-ocr.txt"
  if grep -Eq 'automatically shifted|Failed to create CUDA|Failed to load library|CUDA failure' ".ai_paper_validation/review_1_6_2/preprocessing/doc002-page-${ocr_tag}-gpu-ocr.log"; then
    printf 'GPU_ENGINE_CHECK_NEEDED page=%s\n' "$ocr_page"
    exit 3
  fi
  printf 'GPU_OCR_COMPLETE page=%s\n' "$ocr_page"
done
