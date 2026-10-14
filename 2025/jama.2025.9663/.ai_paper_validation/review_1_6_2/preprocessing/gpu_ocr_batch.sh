#!/usr/bin/env bash
set -euo pipefail
cd /home/juliz/ai-paper-val/2025/jama.2025.9663
seq 1 136 | xargs -P 2 -n 1 bash .ai_paper_validation/review_1_6_2/preprocessing/gpu_ocr_page.sh
