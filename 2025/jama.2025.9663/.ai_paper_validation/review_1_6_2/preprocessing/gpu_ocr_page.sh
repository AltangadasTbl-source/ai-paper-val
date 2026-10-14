#!/usr/bin/env bash
set -euo pipefail
cd /home/juliz/ai-paper-val/2025/jama.2025.9663
n="$1"
tag=$(printf '%03d' "$n")
case "$n" in
  29|3[0-9]|4[0-9]|5[0-6]) image=".ai_paper_validation/review_1_5_1/preprocessing/doc002_b/page-$tag.png" ;;
  100) image=".ai_paper_validation/review_1_5_1/preprocessing/DOC-002/page_images/page-100.png" ;;
  120|121) image=".ai_paper_validation/review_1_5_1/preprocessing/stat_pass1/doc002_p-$n.png" ;;
  126) image=".ai_paper_validation/review_1_5_1/preprocessing/stat_pass1/doc002_p126.png" ;;
  *) image=".ai_paper_validation/review_1_6_2/preprocessing/doc002/page-$tag.png" ;;
esac
export LD_LIBRARY_PATH=/home/juliz/venvs/stt/lib/python3.12/site-packages/nvidia/cu13/lib:/home/juliz/venvs/stt/lib/python3.12/site-packages/nvidia/cudnn/lib:/usr/lib/wsl/lib
out=".ai_paper_validation/review_1_6_2/preprocessing/doc002/ocr-$tag"
if [ -s "$out.txt" ]; then exit 0; fi
/home/juliz/venvs/stt/bin/rapidocr_onnxruntime -img "$image" --det_use_cuda --cls_use_cuda --rec_use_cuda --intra_op_num_threads 2 --inter_op_num_threads 2 -p > "$out.log" 2>&1
perl -ne 'while (/(?:\x27((?:\\.|[^\x27\\])*)\x27|"((?:\\.|[^"\\])*)"),\s+[01]\.\d+/g) { print((defined($1) ? $1 : $2), "\n"); }' "$out.log" > "$out.txt"
printf '%s\t%s\t%s\t%s\n' "$n" "$image" "$out.txt" "rapidocr-onnxruntime==1.4.4 CUDA GPU via PowerShell 5.1 and WSL; CLI text transcription by Perl" > "$out.provenance.tsv"
test -s "$out.txt"
