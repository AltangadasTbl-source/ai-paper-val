#!/usr/bin/env bash
set -eu
cd /home/juliz/ai-paper-val/2025/jama.2025.15440
ocr_cuda_libs=$(printf '%s:' /home/juliz/venvs/stt/lib/python3.12/site-packages/nvidia/*/lib /usr/lib/wsl/lib)
export LD_LIBRARY_PATH="${ocr_cuda_libs}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}"
exec /home/juliz/venvs/stt/bin/python -m rapidocr_onnxruntime.main --img_path "$1" --det_use_cuda --cls_use_cuda --rec_use_cuda --intra_op_num_threads 2 --inter_op_num_threads 2 --det_limit_side_len 1600 --det_limit_type max --print_cost
