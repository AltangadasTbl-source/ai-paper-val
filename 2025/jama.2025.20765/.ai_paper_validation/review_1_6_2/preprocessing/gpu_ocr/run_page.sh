#!/usr/bin/env bash
set -euo pipefail
page_number=${1:?Provide one three-digit source page number}
[[ "$page_number" =~ ^[0-9]{3}$ ]] || exit 2
image_path=".ai_paper_validation/review_1_5_1/preprocessing/DOC-002/page_images/page-${page_number}.jpg"
output_base=".ai_paper_validation/review_1_6_2/preprocessing/gpu_ocr/DOC-002/page-${page_number}"
export LD_LIBRARY_PATH="/home/juliz/venvs/stt/lib/python3.12/site-packages/nvidia/cu13/lib:/home/juliz/venvs/stt/lib/python3.12/site-packages/nvidia/cudnn/lib:/usr/lib/wsl/lib"
/home/juliz/venvs/stt/bin/rapidocr_onnxruntime \
  --img_path "$image_path" --det_use_cuda --cls_use_cuda --rec_use_cuda \
  --intra_op_num_threads 2 --inter_op_num_threads 2 --print_cost \
  > "${output_base}.log" 2>&1
if rg -q 'automatically shifted|Failed to create CUDA|Failed to load library' "${output_base}.log"; then
  printf 'GPU execution was not confirmed; inspect the preserved log.\n' >&2
  exit 3
fi
perl -ne 'while (/\]\], ([\x27\x22])((?:\\.|(?!\1).)*?)\1, [0-9.]+\]/g) {print "$2\n";}' "${output_base}.log" > "${output_base}.txt"
printf 'DOC-002 PDF p. %s: RapidOCR ONNX Runtime 1.4.4; ONNX Runtime GPU 1.28.0; CUDA; RTX 5070 Laptop GPU; source image %s; log %s.log; text %s.txt\n' "$page_number" "$image_path" "$output_base" "$output_base" > "${output_base}.metadata.txt"
