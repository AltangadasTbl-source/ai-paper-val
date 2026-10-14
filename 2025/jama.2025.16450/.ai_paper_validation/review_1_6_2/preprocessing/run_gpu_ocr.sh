#!/usr/bin/env bash
set -euo pipefail
root=/home/juliz/ai-paper-val/2025/jama.2025.16450
cd "$root"
ocr_dir=.ai_paper_validation/review_1_6_2/preprocessing/gpu_ocr
mkdir -p "$ocr_dir"
export LD_LIBRARY_PATH=/home/juliz/venvs/stt/lib/python3.12/site-packages/nvidia/cu13/lib:/home/juliz/venvs/stt/lib/python3.12/site-packages/nvidia/cudnn/lib:/usr/lib/wsl/lib
for page in $(seq 1 35); do
  printf 'DOC-002\t%03d\t.ai_paper_validation/review_1_5_1/preprocessing/protocol/images/DOC-002-%02d.png\n' "$page" "$page"
done > "$ocr_dir/input_pages.tsv"
for page in $(seq 1 162); do
  if [ "$page" -le 81 ]; then
    printf 'DOC-003\t%03d\t.ai_paper_validation/review_1_5_1/preprocessing/manual_001_081/render-%03d.png\n' "$page" "$page"
  else
    printf 'DOC-003\t%03d\t.ai_paper_validation/review_1_5_1/preprocessing/manual_082_162/page-%03d.png\n' "$page" "$page"
  fi
done >> "$ocr_dir/input_pages.tsv"
for page in $(seq 1 48); do
  printf 'DOC-004\t%03d\t.ai_paper_validation/review_1_5_1/preprocessing/sap_results/sap_pages/page-%02d.png\n' "$page" "$page"
done >> "$ocr_dir/input_pages.tsv"
xargs -d '\n' -P 3 -I '{}' bash -c '
  IFS=$'"'"'\t'"'"' read -r doc page image <<< "$1"
  base=".ai_paper_validation/review_1_6_2/preprocessing/gpu_ocr/${doc}-p${page}"
  if [ ! -s "${base}.log" ]; then
    /home/juliz/venvs/stt/bin/rapidocr_onnxruntime -img "$image" --det_use_cuda --cls_use_cuda --rec_use_cuda --intra_op_num_threads 2 --inter_op_num_threads 2 -p > "${base}.log" 2>&1
  fi
  node .ai_paper_validation/review_1_6_2/preprocessing/transcribe_ocr_log.cjs "${base}.log" "${base}.txt"
' _ '{}' < "$ocr_dir/input_pages.tsv"
printf 'GPU OCR completed for %s page images.\n' "$(wc -l < "$ocr_dir/input_pages.tsv")"
