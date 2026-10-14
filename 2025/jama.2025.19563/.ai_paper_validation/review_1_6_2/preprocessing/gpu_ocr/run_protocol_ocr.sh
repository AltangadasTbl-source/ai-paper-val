#!/usr/bin/env bash
set -u
export LD_LIBRARY_PATH=/home/juliz/venvs/stt/lib/python3.12/site-packages/nvidia/cu13/lib:/home/juliz/venvs/stt/lib/python3.12/site-packages/nvidia/cudnn/lib:/usr/lib/wsl/lib
run_out=.ai_paper_validation/review_1_6_2/preprocessing/gpu_ocr
for page in $(seq 74 90) $(seq 1 73); do
  if [ "$page" -le 30 ]; then shard=p001-p030; elif [ "$page" -le 60 ]; then shard=p031-p060; else shard=p061-p090; fi
  printf -v page2 '%02d' "$page"
  printf -v page3 '%03d' "$page"
  run_image=".ai_paper_validation/review_1_5_1/preprocessing/DOC-002/$shard/page-$page2.png"
  if [ ! -f "$run_image" ]; then printf 'MISSING_IMAGE %s\n' "$page"; continue; fi
  /home/juliz/venvs/stt/bin/rapidocr_onnxruntime -img "$run_image" --det_use_cuda --cls_use_cuda --rec_use_cuda --intra_op_num_threads 2 --inter_op_num_threads 2 --print_cost > "$run_out/protocol-page-$page3.log" 2>&1
  perl -ne 'while(/,\s*(\x27(?:[^\x27\\]|\\.)*\x27|"(?:[^"\\]|\\.)*"),\s*[0-9.]+\]/g){ print "$1\n"; }' "$run_out/protocol-page-$page3.log" > "$run_out/protocol-page-$page3.txt"
  if rg -q 'shifted|Failed to create CUDA|CUDA failure' "$run_out/protocol-page-$page3.log"; then printf 'GPU_FALLBACK %s\n' "$page"; exit 4; fi
  printf 'OCR_COMPLETE PDF_PAGE=%s text_bytes=%s\n' "$page" "$(wc -c < "$run_out/protocol-page-$page3.txt")"
done
